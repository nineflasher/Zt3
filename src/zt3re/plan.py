"""Create annotation work packets (markdown) for subagents, bottom-up through the call graph."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from . import annotations, config, hwmap

WAVE_BOUNDS = [(0, 0), (1, 2), (3, 5), (6, 10_000)]       # call-depth ranges per wave
MAX_FUNCS = 36
MAX_CHARS = 60_000


def _load_inputs(comp: str):
    fam = json.loads((config.ANALYSIS_DIR / "families" / f"{comp}.json").read_text())
    exports = {}
    decomps = {}
    strings = {}
    for img in fam["versions"]:                      # every build: data families may anchor anywhere
        ex = json.loads((config.ANALYSIS_DIR / "export" / comp / f"{img}.json").read_text())
        exports[img] = {x["addr"]: x for x in ex["functions"]}
        strings[img] = {x["addr"]: x for x in ex["strings"]}
        dp = config.ANALYSIS_DIR / "decomp" / comp / f"{img}.json"
        decomps[img] = json.loads(dp.read_text()) if dp.exists() else {}
    return fam, exports, decomps, strings


_HEAD = re.compile(r"^## `([\w]+)`", re.M)


def _issued_path(comp: str) -> Path:
    """Issued-packet list: committed, so a fresh clone cannot re-hand-out in-flight work."""
    return config.ANALYSIS_DIR / "plan" / f"{comp}.issued.txt"


def issued(comp: str) -> set[str]:
    p = _issued_path(comp)
    return set(p.read_text().split()) if p.exists() else set()


def mark_issued(comp: str, packets: list[str]) -> None:
    """Record packets as handed to an agent: they are never regenerated or re-assigned."""
    _issued_path(comp).parent.mkdir(parents=True, exist_ok=True)
    allp = sorted(issued(comp) | set(packets))
    _issued_path(comp).write_text("\n".join(allp) + "\n")


def packeted(comp: str) -> set[str]:
    """Family ids contained in issued work packets (a re-plan must not hand them out again)."""
    out: set[str] = set()
    for name in issued(comp):
        p = config.ANALYSIS_DIR / "work" / comp / f"{name}.md"
        if p.exists():
            out |= set(_HEAD.findall(p.read_text()))
    return out


def drop_unissued(comp: str, wave: int | None) -> int:
    """Delete generated-but-never-issued packets so they can be regenerated with fresh context."""
    done = issued(comp)
    n = 0
    for p in (config.ANALYSIS_DIR / "work" / comp).glob("wave*_batch*.md"):
        if p.stem in done:
            continue
        if wave is None or p.stem.startswith(f"wave{wave}_"):
            p.unlink()
            n += 1
    return n


def next_batch_index(comp: str, wave: int) -> int:
    pat = re.compile(rf"wave{wave}_batch(\d+)")
    idx = [int(m.group(1)) for d, ext in ((config.ANALYSIS_DIR / "work" / comp, "*.md"),
                                           (config.ANNOTATIONS_DIR / comp / "functions", "*.json"))
           for f in d.glob(ext) if (m := pat.search(f.name))]
    return max(idx, default=0) + 1


def call_depths(fam: dict, exports: dict) -> tuple[dict[str, int], dict[str, list[str]], dict[str, list[str]]]:
    node_to_fam = {(n, a): fid for fid, f in fam["functions"].items() for n, a in f["members"].items()}
    callees: dict[str, set[str]] = {}
    for fid, f in fam["functions"].items():
        img, addr = f["anchor"]
        fx = exports[img][addr]
        cs = set()
        for c in fx["callees"]:
            cf = node_to_fam.get((img, c))
            if cf and cf != fid:
                cs.add(cf)
        callees[fid] = cs
    callers: dict[str, set[str]] = defaultdict(set)
    for fid, cs in callees.items():
        for c in cs:
            callers[c].add(fid)
    # Tarjan SCC -> DAG depth
    index, low, onstack, stack, comp_of = {}, {}, set(), [], {}
    sccs: list[list[str]] = []
    counter = [0]

    def strong(v):
        stack_ = [(v, iter(sorted(callees[v])))]
        index[v] = low[v] = counter[0]
        counter[0] += 1
        stack.append(v)
        onstack.add(v)
        while stack_:
            node, it = stack_[-1]
            adv = False
            for w in it:
                if w not in index:
                    index[w] = low[w] = counter[0]
                    counter[0] += 1
                    stack.append(w)
                    onstack.add(w)
                    stack_.append((w, iter(sorted(callees[w]))))
                    adv = True
                    break
                elif w in onstack:
                    low[node] = min(low[node], index[w])
            if adv:
                continue
            stack_.pop()
            if stack_:
                low[stack_[-1][0]] = min(low[stack_[-1][0]], low[node])
            if low[node] == index[node]:
                scc = []
                while True:
                    w = stack.pop()
                    onstack.discard(w)
                    scc.append(w)
                    comp_of[w] = len(sccs)
                    if w == node:
                        break
                sccs.append(scc)

    for v in sorted(callees):
        if v not in index:
            strong(v)
    depth_scc: dict[int, int] = {}
    for i, scc in enumerate(sccs):                      # Tarjan emits callees' SCCs first
        d = 0
        for v in scc:
            for w in callees[v]:
                j = comp_of[w]
                if j != i:
                    d = max(d, depth_scc[j] + 1)
        depth_scc[i] = d
    depth = {v: depth_scc[comp_of[v]] for v in callees}
    return depth, {k: sorted(v) for k, v in callees.items()}, {k: sorted(v) for k, v in callers.items()}


def wave_of(depth: int) -> int:
    for i, (lo, hi) in enumerate(WAVE_BOUNDS):
        if lo <= depth <= hi:
            return i + 1
    return len(WAVE_BOUNDS)


def make_waves(comp: str, wave: int | None = None, force: bool = False, replan: bool = False) -> list[Path]:
    from .config import COMPONENTS

    cobj = COMPONENTS[comp]
    fam, exports, decomps, strings = _load_inputs(comp)
    depth, callees, callers = call_depths(fam, exports)
    done = annotations.load_functions(comp)
    hw = hwmap.get(cobj.chip)

    def label(fid: str) -> str:
        n = done.get(fid)
        return f"`{n['name']}`" if n else f"`{fid}`"

    out_dir = config.ANALYSIS_DIR / "work" / comp
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    waves = defaultdict(list)
    drop_unissued(comp, wave)
    handed_out = set() if replan else packeted(comp)
    for fid in fam["functions"]:
        if (fid in done and not force) or fid in handed_out:
            continue
        waves[wave_of(depth[fid])].append(fid)
    for w, fids in sorted(waves.items()):
        if wave is not None and w != wave:
            continue
        fids.sort(key=lambda f: (fam["functions"][f]["anchor"][1]))
        batches, cur, cur_chars = [], [], 0
        for fid in fids:
            img, addr = fam["functions"][fid]["anchor"]
            c = len(decomps[img].get(f"{addr:#x}", {}).get("c") or "")
            if cur and (len(cur) >= MAX_FUNCS or cur_chars + c > MAX_CHARS):
                batches.append(cur)
                cur, cur_chars = [], 0
            cur.append(fid)
            cur_chars += c
        if cur:
            batches.append(cur)
        first = 1 if replan else next_batch_index(comp, w)
        for bi, batch in enumerate(batches, first):
            p = out_dir / f"wave{w}_batch{bi:02d}.md"
            lines = [f"# {comp.upper()} wave {w} batch {bi:02d}  ({len(batch)} functions)\n",
                     f"Component: **{cobj.title}** - {cobj.role}. Chip: `{cobj.chip}`.\n",
                     f"Write your answer to `annotations/{comp}/functions/wave{w}_batch{bi:02d}.json`.\n"]
            for fid in batch:
                f = fam["functions"][fid]
                img, addr = f["anchor"]
                fx = exports[img][addr]
                dec = decomps[img].get(f"{addr:#x}", {})
                lines.append(f"\n## `{fid}`  @ {img}:{addr:#010x}  ({fx['n_insn']} insns, depth {depth[fid]})")
                lines.append(f"- present in: {', '.join(sorted(f['members'], key=lambda n: int(n.split('_')[1], 16)))}")
                if fx.get("vector"):
                    lines.append(f"- interrupt/exception vector: **{fx['vector']}**")
                if callers.get(fid):
                    lines.append("- callers: " + ", ".join(label(c) for c in callers[fid][:12]) +
                                 (" ..." if len(callers[fid]) > 12 else ""))
                else:
                    lines.append("- callers: none direct (entry point / callback / indirect)")
                if callees.get(fid):
                    lines.append("- callees:")
                    for c in callees[fid][:14]:
                        n = done.get(c)
                        lines.append(f"  - {label(c)}" + (f": {n['summary']}" if n else " (not yet described)"))
                    if len(callees[fid]) > 14:
                        lines.append("  - ...")
                refs = [strings[img][a] for a in fx.get("strings", []) if a in strings[img]]
                if refs:
                    lines.append("- string literals referenced: " + "; ".join(
                        json.dumps(r["text"][:90]) for r in refs[:8]))
                if fx["indirect_calls"]:
                    lines.append(f"- indirect calls (function pointers): {fx['indirect_calls']}")
                if fx["periph"]:
                    lines.append("- peripheral registers: " + ", ".join(
                        f"{hw.name(int(a, 16))}[{m}]" for a, m in list(fx["periph"].items())[:24]))
                if fx["ram"]:
                    lines.append("- RAM variables: " + ", ".join(f"{a}[{m}]" for a, m in list(fx["ram"].items())[:24]))
                lines.append("```c\n" + (dec.get("c") or "/* decompilation failed */").strip() + "\n```")
            p.write_text("\n".join(lines) + "\n")
            written.append(p)
    return written


# ---------------------------------------------------------------------------------------------
# Data packets: RAM variables and flash tables, grouped by the module that uses them.
# ---------------------------------------------------------------------------------------------
DATA_PER_PACKET = 60
_DAT_RE = re.compile(r"\b_?DAT_([0-9a-f]{8})\b")


def _accessors(fam: dict, exports: dict, kind: str) -> dict[str, list[tuple[str, str]]]:
    """family id -> [(function family id, 'R'|'W'|'RW'|'A')], via one reverse index per image."""
    node_to_fam = {(n, a): fid for fid, f in fam["functions"].items() for n, a in f["members"].items()}
    index: dict[str, dict[int, list[tuple[str, str]]]] = {}
    for img, funcs in exports.items():
        idx: dict[int, list[tuple[str, str]]] = defaultdict(list)
        for fx in funcs.values():
            ffid = node_to_fam.get((img, fx["addr"]))
            if ffid is None:
                continue
            if kind == "globals":
                for a, m in fx["ram"].items():
                    idx[int(a, 16)].append((ffid, m))
            else:
                for a in fx["rodata"]:
                    idx[a].append((ffid, "R"))
        index[img] = idx
    out: dict[str, list[tuple[str, str]]] = {}
    for oid, f in fam[kind].items():
        img, addr = f["anchor"]
        out[oid] = index.get(img, {}).get(addr, [])
    return out


def make_data_waves(comp: str, kind: str = "globals") -> list[Path]:
    """Write data work packets for every not-yet-covered global (or table) family."""
    from . import objects
    from .config import COMPONENTS

    cobj = COMPONENTS[comp]
    fam, exports, decomps, strings = _load_inputs(comp)
    funcs = annotations.load_functions(comp)
    notes = annotations.load_globals(comp) if kind == "globals" else annotations.load_tables(comp)
    covered = {fid for r in objects.resolve(comp, notes, kind)[0].values() for fid in r["covers"]}
    handed = packeted(comp)
    acc = _accessors(fam, exports, kind)
    todo = [oid for oid in fam[kind] if oid not in covered and oid not in handed]
    # group by dominant category of the accessing functions, then by address
    def category(oid: str) -> str:
        cats = Counter(funcs[f]["category"] for f, _ in acc.get(oid, []) if f in funcs)
        return cats.most_common(1)[0][0] if cats else "unreferenced"

    groups: dict[str, list[str]] = defaultdict(list)
    for oid in todo:
        groups[category(oid)].append(oid)
    out_dir = config.ANALYSIS_DIR / "work" / comp
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    tag = "data" if kind == "globals" else "table"
    idx = next_batch_index_named(comp, tag)
    for cat, oids in sorted(groups.items()):
        oids.sort(key=lambda o: fam[kind][o]["anchor"][1])
        for i in range(0, len(oids), DATA_PER_PACKET):
            batch = oids[i:i + DATA_PER_PACKET]
            name = f"{tag}_{cat}_batch{idx:02d}"
            idx += 1
            p = out_dir / f"{name}.md"
            lines = [f"# {comp.upper()} {tag} packet `{name}`  ({len(batch)} objects, module `{cat}`)\n",
                     f"Component: **{cobj.title}**. Chip `{cobj.chip}`.  Kind: **{kind}**.\n",
                     f"Write your answer to `annotations/{comp}/{kind}/{name}.json` "
                     f"(and new structs/enums to `annotations/{comp}/types/{name}.json`).\n",
                     "Objects are listed in address order: adjacent addresses with the same accessors are usually "
                     "one array or struct - describe them as ONE object with `size` covering all of them.\n"]
            for oid in batch:
                f = fam[kind][oid]
                img, addr = f["anchor"]
                lines.append(f"\n## `{oid}`  @ {img}:{addr:#010x}")
                vers = ", ".join(v.split("_")[1] for v in sorted(f["members"], key=lambda n: int(n.split("_")[1], 16)))
                lines.append(f"- present in builds: {vers}")
                lines.append("- accessed by: " + ", ".join(
                    f"`{funcs[fn]['name']}`[{m}]" if fn in funcs else f"`{fn}`[{m}]" for fn, m in acc.get(oid, [])[:12])
                             + (" ..." if len(acc.get(oid, [])) > 12 else ""))
                # evidence: decompiled lines mentioning the address, from up to 3 accessors
                shown = 0
                for fn, _ in acc.get(oid, [])[:3]:
                    fimg, faddr = fam["functions"][fn]["anchor"]
                    c = decomps.get(fimg, {}).get(f"{faddr:#x}", {}).get("c") or ""
                    hits = [ln.strip() for ln in c.splitlines() if f"{addr:08x}" in ln.lower()]
                    for ln in hits[:3]:
                        lines.append(f"  - `{funcs[fn]['name'] if fn in funcs else fn}`: `{ln[:140]}`")
                        shown += 1
                if not shown:
                    lines.append("  - (no decompiled line names this address directly; accessed through a pointer or base register)")
            p.write_text("\n".join(lines) + "\n")
            written.append(p)
    return written


def next_batch_index_named(comp: str, tag: str) -> int:
    pat = re.compile(rf"^{tag}_.*_batch(\d+)")
    idx = [int(m.group(1)) for d in (config.ANALYSIS_DIR / "work" / comp, config.ANNOTATIONS_DIR / comp / "globals",
                                     config.ANNOTATIONS_DIR / comp / "tables")
           if d.exists() for f in d.iterdir() if (m := pat.match(f.name))]
    return max(idx, default=0) + 1
