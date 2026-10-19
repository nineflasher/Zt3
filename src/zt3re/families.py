"""Build cross-version families of functions, RAM globals and flash tables.

Input : analysis/export/<comp>/<image>.json   (zt3 export)
        analysis/matches/<comp>/<src>__<dst>.json   (zt3 match, Ghidra Version Tracking)
Output: analysis/families/<comp>.json

A *family* groups the same logical function (or variable) across every firmware version.  The
anchor of a family is its occurrence in the newest version that contains it; descriptions are
written once per family and applied to all members.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from . import config

Node = tuple[str, int]      # (image name, address)


class UnionFind:
    def __init__(self):
        self.p: dict[Node, Node] = {}

    def find(self, x: Node) -> Node:
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a: Node, b: Node) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra


def _load(path: Path):
    return json.loads(path.read_text())


def _best_function_matches(rows: list[dict], valid_src: set[int], valid_dst: set[int]) -> list[tuple[int, int, str]]:
    """Pick a 1:1 assignment from the (many, overlapping) VT function matches of one pair."""
    cand = []
    for r in rows:
        if r["kind"] != "Function" or r["src"] not in valid_src or r["dst"] not in valid_dst:
            continue
        accepted = r["status"] == "ACCEPTED"
        if not accepted and r["sim"] < 0.6:
            continue
        cand.append((accepted, r["sim"], r["conf"], r["src"], r["dst"], r["correlator"]))
    cand.sort(reverse=True)
    used_s, used_d, out = set(), set(), []
    for acc, sim, conf, s, d, corr in cand:
        if s in used_s or d in used_d:
            continue
        used_s.add(s)
        used_d.add(d)
        out.append((s, d, corr))
    return out




def _lis_anchors(pm: dict[int, int]) -> list[tuple[int, int]]:
    """Longest increasing subsequence of (src, dst) pairs: the order-consistent anchors."""
    items = sorted(pm.items())
    tails: list[int] = []
    idx: list[int] = []
    prev = [-1] * len(items)
    for i, (_, d) in enumerate(items):
        lo, hi = 0, len(tails)
        while lo < hi:
            mid = (lo + hi) // 2
            if items[tails[mid]][1] < d:
                lo = mid + 1
            else:
                hi = mid
        if lo > 0:
            prev[i] = tails[lo - 1]
        if lo == len(tails):
            tails.append(i)
        else:
            tails[lo] = i
    out, k = [], tails[-1] if tails else -1
    while k != -1:
        out.append(items[k])
        k = prev[k]
    return out[::-1]


def _gap_align(fa: dict[int, dict], fb: dict[int, dict], pm: dict[int, int]) -> list[tuple[int, int]]:
    """Align still-unmatched functions that sit between the same pair of anchors (diff-style)."""
    anchors = _lis_anchors(pm)
    matched_s, matched_d = set(pm), set(pm.values())
    sa = sorted(fa)
    sb = sorted(fb)
    bounds = [(-1, -1)] + anchors + [(1 << 40, 1 << 40)]
    new: list[tuple[int, int]] = []
    for (s0, d0), (s1, d1) in zip(bounds, bounds[1:]):
        ga = [a for a in sa if s0 < a < s1 and a not in matched_s]
        gb = [b for b in sb if d0 < b < d1 and b not in matched_d]
        if not ga or not gb:
            continue
        for key in ("hash_norm", "hash_mnem"):            # LCS on the hash, strongest first
            ka = [fa[a][key] for a in ga]
            kb = [fb[b][key] for b in gb]
            n, m = len(ka), len(kb)
            dp = [[0] * (m + 1) for _ in range(n + 1)]
            for i in range(n - 1, -1, -1):
                for j in range(m - 1, -1, -1):
                    dp[i][j] = dp[i + 1][j + 1] + 1 if ka[i] == kb[j] else max(dp[i + 1][j], dp[i][j + 1])
            i = j = 0
            ra, rb = [], []
            while i < n and j < m:
                if ka[i] == kb[j]:
                    new.append((ga[i], gb[j]))
                    i += 1
                    j += 1
                elif dp[i + 1][j] >= dp[i][j + 1]:
                    ra.append(ga[i]); i += 1
                else:
                    rb.append(gb[j]); j += 1
            ra += ga[i:]
            rb += gb[j:]
            matched_here = {a for a, _ in new}
            ga = [a for a in ga if a not in matched_here]
            gb = [b for b in gb if b not in {d for _, d in new}]
            if not ga or not gb:
                break
        # leftovers: same count and similar size -> positional match
        if ga and gb and len(ga) == len(gb):
            for a, b in zip(ga, gb):
                x, y = fa[a]["n_insn"], fb[b]["n_insn"]
                if abs(x - y) <= max(3, 0.3 * max(x, y)):
                    new.append((a, b))
    return new


def _index_map(fs: dict, fd: dict) -> dict[int, int]:
    """Map 1-based instruction index of function fs -> fd (identity if bytes-equivalent, else diff)."""
    if fs["hash_norm"] == fd["hash_norm"]:
        return {i: i for i in range(1, fs["n_insn"] + 1)}
    import difflib

    a = [fs["isq"][k:k + 4] for k in range(0, len(fs["isq"]), 4)]
    b = [fd["isq"][k:k + 4] for k in range(0, len(fd["isq"]), 4)]
    out = {}
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            out[blk.a + k + 1] = blk.b + k + 1
    return out


def _infer_by_delta(fams: dict, names: list[str], order: dict[str, int]) -> int:
    """Merge leftover single-version variables into the family at `addr + local delta`.

    Variables are laid out in runs; between two builds a whole run usually moves by one constant.
    If the matched neighbours of an unmatched address agree on the delta, apply it.
    """
    import bisect

    newest = names[-1]
    by_anchor = {tuple(f["anchor"]): fid for fid, f in fams.items()}
    merged = 0
    for v in names[:-1]:
        pts = sorted((f["members"][v], f["members"][newest], fid) for fid, f in fams.items()
                     if v in f["members"] and newest in f["members"])
        xs = [p[0] for p in pts]
        for fid, f in list(fams.items()):
            if len(f["members"]) != 1 or v not in f["members"] or fid not in fams:
                continue
            a = f["members"][v]
            i = bisect.bisect_left(xs, a)
            if i == 0 or i >= len(pts):
                continue
            d_lo = pts[i - 1][1] - pts[i - 1][0]
            d_hi = pts[i][1] - pts[i][0]
            if d_lo != d_hi:
                continue
            tgt = by_anchor.get((newest, a + d_lo))
            if tgt is None or tgt == fid or v in fams[tgt]["members"]:
                continue
            fams[tgt]["members"][v] = a
            del fams[fid]
            merged += 1
    return merged


def build(comp: str) -> dict:
    exp_dir = config.ANALYSIS_DIR / "export" / comp
    imgs = sorted(exp_dir.glob("*.json"), key=lambda p: int(p.stem.split("_")[1], 16))
    exports = {p.stem: _load(p) for p in imgs}
    names = list(exports)                                   # ascending version order
    funcs = {n: {f["addr"]: f for f in e["functions"]} for n, e in exports.items()}

    uf = UnionFind()
    for n in names:
        for a in funcs[n]:
            uf.find((n, a))

    # --- function families from VT matches (adjacent pairs first, then ->newest pairs) -------
    pair_files = sorted((config.ANALYSIS_DIR / "matches" / comp).glob("*__*.json"))
    pairs = []
    for pf in pair_files:
        j = _load(pf)
        pairs.append((j["source"], j["dest"], j["matches"]))
    order = {n: i for i, n in enumerate(names)}
    pairs.sort(key=lambda t: (order[t[1]] - order[t[0]], order[t[0]]))      # adjacent first
    pair_map: dict[tuple[str, str], dict[int, int]] = {}
    members_by_root: dict[Node, dict[str, int]] = {}

    def root_members(root: Node) -> dict[str, int]:
        return members_by_root.setdefault(root, {root[0]: root[1]})

    edge_stats = Counter()
    for src, dst, rows in pairs:
        picks = _best_function_matches(rows, set(funcs[src]), set(funcs[dst]))
        pm = {}
        for s, d, corr in picks:
            rs, rd = uf.find((src, s)), uf.find((dst, d))
            if rs == rd:
                pm[s] = d
                continue
            ms, md = root_members(rs), root_members(rd)
            if set(ms) & set(md):                              # would put two functions of one version together
                edge_stats["conflict"] += 1
                continue
            uf.union(rs, rd)
            new = uf.find(rs)
            merged = {**ms, **md}
            members_by_root.pop(rs, None)
            members_by_root.pop(rd, None)
            members_by_root[new] = merged
            pm[s] = d
            edge_stats[corr] += 1
        # second stage: order-preserving gap alignment for what VT left unmatched
        for s_, d_ in _gap_align(funcs[src], funcs[dst], pm):
            rs, rd = uf.find((src, s_)), uf.find((dst, d_))
            if rs == rd:
                pm[s_] = d_
                continue
            ms, md = root_members(rs), root_members(rd)
            if set(ms) & set(md):
                edge_stats["gap_conflict"] += 1
                continue
            uf.union(rs, rd)
            new_root = uf.find(rs)
            members_by_root.pop(rs, None)
            members_by_root.pop(rd, None)
            members_by_root[new_root] = {**ms, **md}
            pm[s_] = d_
            edge_stats["gap_alignment"] += 1
        pair_map[(src, dst)] = pm

    fam_nodes: dict[Node, dict[str, int]] = defaultdict(dict)
    for n in names:
        for a in funcs[n]:
            fam_nodes[uf.find((n, a))][n] = a

    families = {}
    comp_upper = comp.upper()
    for root, mem in fam_nodes.items():
        anchor_img = max(mem, key=lambda x: order[x])
        anchor = mem[anchor_img]
        ver = anchor_img.split("_")[1]
        fid = f"{comp}_{ver}_{anchor:08x}"
        families[fid] = {"anchor": [anchor_img, anchor], "members": mem}

    node_to_fam = {(n, a): fid for fid, f in families.items() for n, a in f["members"].items()}

    # --- globals / tables aligned through matched functions -------------------------------------
    def vote(kind_seq: str, kind_set: str):
        votes: dict[tuple[str, str], Counter] = defaultdict(Counter)
        for (src, dst), pm in pair_map.items():
            for s, d in pm.items():
                fs, fd = funcs[src][s], funcs[dst][d]
                if not fs[kind_seq] or not fd[kind_seq]:
                    continue
                imap = _index_map(fs, fd)
                ia, ib = defaultdict(set), defaultdict(set)
                for i, x in fs[kind_seq]:
                    ia[i].add(x)
                for i, y in fd[kind_seq]:
                    ib[i].add(y)
                for i, xs in ia.items():
                    j = imap.get(i)
                    ys = ib.get(j) if j is not None else None
                    if ys and len(xs) == 1 and len(ys) == 1:
                        votes[(src, dst)][(next(iter(xs)), next(iter(ys)))] += 1
        return votes

    def link(votes):
        guf = UnionFind()
        for (src, dst), cnt in votes.items():
            used_s, used_d = set(), set()
            for (x, y), c in cnt.most_common():
                if x in used_s or y in used_d:
                    continue
                used_s.add(x)
                used_d.add(y)
                guf.union((src, x), (dst, y))
        groups: dict[Node, dict[str, int]] = defaultdict(dict)
        for node in list(guf.p):
            groups[guf.find(node)].setdefault(node[0], node[1])
        return groups

    out_globals, out_tables = {}, {}
    gl_all = {n: {g["addr"]: g for g in e["globals"]} for n, e in exports.items()}
    tb_all = {n: {t["addr"]: t for t in e["tables"]} for n, e in exports.items()}
    for kind, seq, allmap, out, tag in (
            ("globals", "ram_seq", gl_all, out_globals, "g"),
            ("tables", "rodata_seq", tb_all, out_tables, "t")):
        groups = link(vote(seq, kind))
        seen = set()
        for mem in groups.values():
            for n, a in mem.items():
                seen.add((n, a))
        for n in names:                                     # singletons
            for a in allmap[n]:
                if (n, a) not in seen:
                    groups[(n, a)] = {n: a}
        for mem in groups.values():
            anchor_img = max(mem, key=lambda x: order[x])
            anchor = mem[anchor_img]
            fid = f"{comp}_{tag}_{anchor_img.split('_')[1]}_{anchor:08x}"
            out[fid] = {"anchor": [anchor_img, anchor], "members": mem}

    for out in (out_globals, out_tables):
        _infer_by_delta(out, names, order)

    newest = names[-1]
    cov = {n: round(100.0 * sum(1 for a in funcs[n] if len(families[node_to_fam[(n, a)]]["members"]) > 1) / len(funcs[n]), 1)
           for n in names}
    result = {
        "component": comp, "versions": names,
        "functions": families, "globals": out_globals, "tables": out_tables,
        "stats": {
            "n_functions_total": sum(len(v) for v in funcs.values()),
            "n_function_families": len(families),
            "n_global_families": len(out_globals),
            "n_table_families": len(out_tables),
            "pct_functions_in_multi_version_family": cov,
            "vt_edges": dict(edge_stats),
        },
    }
    return result


def write(comp: str, payload: dict) -> Path:
    p = config.ANALYSIS_DIR / "families" / f"{comp}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, separators=(",", ":")))
    return p
