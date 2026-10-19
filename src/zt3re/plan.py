"""Create annotation work packets (markdown) for subagents, bottom-up through the call graph."""
from __future__ import annotations

import json
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
    for fid, f in fam["functions"].items():
        img = f["anchor"][0]
        if img not in exports:
            exports[img] = {x["addr"]: x for x in json.loads(
                (config.ANALYSIS_DIR / "export" / comp / f"{img}.json").read_text())["functions"]}
            decomps[img] = json.loads((config.ANALYSIS_DIR / "decomp" / comp / f"{img}.json").read_text())
    return fam, exports, decomps


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


def make_waves(comp: str, wave: int | None = None, force: bool = False) -> list[Path]:
    from .config import COMPONENTS

    cobj = COMPONENTS[comp]
    fam, exports, decomps = _load_inputs(comp)
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
    for fid in fam["functions"]:
        if fid in done and not force:
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
        for bi, batch in enumerate(batches, 1):
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
