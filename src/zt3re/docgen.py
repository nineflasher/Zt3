"""Generate the markdown documentation set under docs/ from annotations + analysis data."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from . import annotations as ann
from . import config, hwmap, objects


def _vkey(img: str) -> int:
    return int(img.split("_")[1], 16)


def _esc(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ")


def build_component(comp: str, out_root: Path | None = None) -> list[Path]:
    cobj = config.COMPONENTS[comp]
    fam = objects.load_families(comp)
    funcs, globs, tabs, types = (ann.load_functions(comp), ann.load_globals(comp),
                                 ann.load_tables(comp), ann.load_types(comp))
    exports = {n: json.loads((config.ANALYSIS_DIR / "export" / comp / f"{n}.json").read_text())
               for n in fam["versions"]}
    by_addr = {n: {f["addr"]: f for f in e["functions"]} for n, e in exports.items()}
    hw = hwmap.get(cobj.chip)
    out = (out_root or config.DOCS_DIR) / comp
    out.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    versions = fam["versions"]
    newest = versions[-1]

    # ---- per-category function reference ---------------------------------------------------
    cats: dict[str, list[str]] = defaultdict(list)
    for fid, n in funcs.items():
        if fid in fam["functions"]:
            cats[n["category"]].append(fid)
    node_to_fam = {(n, a): fid for fid, f in fam["functions"].items() for n, a in f["members"].items()}

    def callers_callees(fid: str):
        img, addr = fam["functions"][fid]["anchor"]
        fx = by_addr[img][addr]
        cs = sorted({node_to_fam[(img, c)] for c in fx["callees"] if (img, c) in node_to_fam})
        cr = sorted({node_to_fam[(img, c)] for c in fx["callers"] if (img, c) in node_to_fam})
        return cr, cs, fx

    def nm(fid: str) -> str:
        return f"`{funcs[fid]['name']}`" if fid in funcs else f"`{fid}`"

    fdir = out / "functions"
    fdir.mkdir(exist_ok=True)
    for cat, fids in sorted(cats.items()):
        fids.sort(key=lambda f: funcs[f]["name"])
        lines = [f"# {cobj.key.upper()} - `{cat}` functions\n", f"{len(fids)} functions.\n",
                 "| Function | Address (" + newest + ") | Summary |", "|---|---|---|"]
        for fid in fids:
            m = fam["functions"][fid]["members"]
            a = m.get(newest)
            lines.append(f"| [`{funcs[fid]['name']}`](#{funcs[fid]['name'].lower()}) | "
                         f"{('0x%08X' % a) if a else '(removed)'} | {_esc(funcs[fid]['summary'])} |")
        for fid in fids:
            n = funcs[fid]
            cr, cs, fx = callers_callees(fid)
            lines += ["", f"## {n['name']}", "", f"**{n['summary']}**", "", n["description"], ""]
            if n.get("params"):
                lines += ["| Parameter | Type | Description |", "|---|---|---|"]
                lines += [f"| `{p['name']}` | `{p['type']}` | {_esc(p['description'])} |" for p in n["params"]]
                lines.append("")
            r = n.get("returns") or {}
            if r.get("type") and r["type"] != "void":
                lines += [f"**Returns** `{r['type']}`: {r['description']}", ""]
            if n.get("notes"):
                lines += [f"**Notes:** {n['notes']}", ""]
            addrs = ", ".join(f"{v.split('_')[1]}: 0x{a:08X}" for v, a in
                              sorted(fam["functions"][fid]["members"].items(), key=lambda kv: _vkey(kv[0])))
            lines.append(f"- Addresses by version: {addrs}")
            if fx.get("vector"):
                lines.append(f"- Vector: `{fx['vector']}`")
            if fx["periph"]:
                lines.append("- Peripheral registers: " + ", ".join(
                    f"`{hw.name(int(a, 16))}` ({m})" for a, m in list(fx["periph"].items())[:16]))
            if cr:
                lines.append("- Called by: " + ", ".join(nm(c) for c in cr[:12]) + (" ..." if len(cr) > 12 else ""))
            if cs:
                lines.append("- Calls: " + ", ".join(nm(c) for c in cs[:16]) + (" ..." if len(cs) > 16 else ""))
            lines.append(f"- Confidence: {n['confidence']}")
        p = fdir / f"{cat}.md"
        p.write_text("\n".join(lines) + "\n")
        written.append(p)

    # ---- data dictionary ---------------------------------------------------------------------
    lines = [f"# {cobj.key.upper()} data dictionary\n"]
    for title, notes in (("RAM variables", globs), ("Flash tables and constants", tabs)):
        lines += [f"## {title}\n", "| Name | Type | Size | Anchor | Description |", "|---|---|---|---|---|"]
        for oid, n in sorted(notes.items(), key=lambda kv: kv[1]["name"]):
            img, a = n["anchor"]
            lines.append(f"| `{n['name']}` | `{n['type']}`{('[%d]' % n['count']) if n.get('count', 1) > 1 else ''} | "
                         f"{n['size']} | {img} 0x{objects.parse_addr(a):08X} | {_esc(n['description'])} |")
        lines.append("")
    p = out / "data.md"
    p.write_text("\n".join(lines) + "\n")
    written.append(p)

    # ---- types ------------------------------------------------------------------------------
    lines = [f"# {cobj.key.upper()} data types\n"]
    for name, s in sorted(types.get("structs", {}).items()):
        lines += [f"## struct `{name}` ({s['size']} bytes)\n", s["description"], "",
                  "| Offset | Field | Type | Description |", "|---|---|---|---|"]
        for f in s["fields"]:
            t = f["type"] + (f"[{f['count']}]" if f.get("count", 1) > 1 else "")
            lines.append(f"| 0x{f['offset']:02X} | `{f['name']}` | `{t}` | {_esc(f['description'])} |")
        lines.append("")
    for name, e in sorted(types.get("enums", {}).items()):
        lines += [f"## enum `{name}`\n", e["description"], "", "| Value | Name | Description |", "|---|---|---|"]
        lines += [f"| {v['value']} | `{v['name']}` | {_esc(v['description'])} |" for v in e["values"]]
        lines.append("")
    p = out / "types.md"
    p.write_text("\n".join(lines) + "\n")
    written.append(p)

    # ---- version evolution ------------------------------------------------------------------
    lines = [f"# {cobj.key.upper()} version evolution\n",
             "Functions are tracked across builds with Ghidra Version Tracking (see methodology).\n",
             "| From | To | Added | Removed | Modified | Unchanged |", "|---|---|---|---|---|---|"]
    for a, b in zip(versions, versions[1:]):
        added = removed = modified = same = 0
        for fid, f in fam["functions"].items():
            m = f["members"]
            if a in m and b in m:
                if by_addr[a][m[a]]["hash_norm"] == by_addr[b][m[b]]["hash_norm"]:
                    same += 1
                else:
                    modified += 1
            elif b in m:
                added += 1
            elif a in m:
                removed += 1
        lines.append(f"| {a} | {b} | {added} | {removed} | {modified} | {same} |")
    lines += ["", "## Per-function changes (newest build vs previous)\n", "| Function | Change |", "|---|---|"]
    prev = versions[-2] if len(versions) > 1 else None
    if prev:
        for fid, f in sorted(fam["functions"].items(), key=lambda kv: funcs.get(kv[0], {}).get("name", kv[0])):
            m = f["members"]
            nme = nm(fid)
            if newest in m and prev not in m:
                lines.append(f"| {nme} | added in {newest} |")
            elif prev in m and newest not in m:
                lines.append(f"| {nme} | removed in {newest} |")
            elif prev in m and newest in m and by_addr[prev][m[prev]]["hash_norm"] != by_addr[newest][m[newest]]["hash_norm"]:
                lines.append(f"| {nme} | modified |")
    p = out / "versions.md"
    p.write_text("\n".join(lines) + "\n")
    written.append(p)

    # ---- hardware usage matrix --------------------------------------------------------------
    use: dict[str, set[str]] = defaultdict(set)
    for fid in funcs:
        if fid not in fam["functions"]:
            continue
        img, addr = fam["functions"][fid]["anchor"]
        for a in by_addr[img][addr]["periph"]:
            h = hw.find(int(a, 16))
            if h:
                use[h[0]["name"]].add(funcs[fid]["name"])
    lines = [f"# {cobj.key.upper()} hardware usage ({cobj.chip})\n", "| Peripheral | Used by |", "|---|---|"]
    for pn, fs in sorted(use.items()):
        lines.append(f"| {pn} | {', '.join(f'`{x}`' for x in sorted(fs)[:30])}{' ...' if len(fs) > 30 else ''} |")
    p = out / "hardware.md"
    p.write_text("\n".join(lines) + "\n")
    written.append(p)

    # ---- component index -----------------------------------------------------------------------
    mod = config.ANNOTATIONS_DIR / comp / "module.json"
    modinfo = json.loads(mod.read_text()) if mod.exists() else {}
    lines = [f"# {cobj.title}\n", modinfo.get("overview", cobj.role), "",
             f"- Chip: `{cobj.chip}`  - Load address: `0x{cobj.base:08X}`  - Versions: {', '.join(v.split('_')[1] for v in versions)}",
             f"- Functions documented: {len(funcs)}  - Variables: {len(globs)}  - Tables: {len(tabs)}  - Structs: {len(types.get('structs', {}))}",
             "", "## Modules\n", "| Module | Functions | Description |", "|---|---|---|"]
    for cat in sorted(cats):
        lines.append(f"| [{cat}](functions/{cat}.md) | {len(cats[cat])} | {_esc(modinfo.get('modules', {}).get(cat, ''))} |")
    lines += ["", "See also: [data dictionary](data.md), [types](types.md), [hardware usage](hardware.md), "
                  "[version evolution](versions.md)."]
    p = out / "README.md"
    p.write_text("\n".join(lines) + "\n")
    written.append(p)
    return written


def check_component(comp: str) -> list[str]:
    """Regenerate into a temp dir and report files that differ from docs/ (regenerate-and-diff)."""
    import filecmp
    import tempfile

    diffs: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        written = build_component(comp, Path(tmp))
        for p in written:
            rel = p.relative_to(tmp)
            real = config.DOCS_DIR / rel
            if not real.exists() or not filecmp.cmp(p, real, shallow=False):
                diffs.append(str(rel))
        expected = {str(p.relative_to(tmp)) for p in written}
        for real in (config.DOCS_DIR / comp).rglob("*.md") if (config.DOCS_DIR / comp).exists() else []:
            rel = str(real.relative_to(config.DOCS_DIR))
            if rel not in expected and real.name != "architecture.md":
                diffs.append(rel + " (orphan: not produced by `zt3 docs`)")
    return diffs
