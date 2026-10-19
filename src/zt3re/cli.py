"""`zt3` command line entry point."""
from __future__ import annotations

import argparse
import json
import logging
import sys

from . import config, ghidra_boot


def _select(args) -> list[config.Image]:
    imgs = config.discover_images(args.component or None)
    if getattr(args, "image", None):
        want = {w.upper() for w in args.image}
        imgs = [i for i in imgs if i.name.upper() in want]
    return imgs


def cmd_import(args) -> int:
    from . import importer

    results = []
    with ghidra_boot.project(create=True) as proj:
        for img in _select(args):
            if img.component not in config.COMPONENTS:
                logging.warning("skipping %s: component not registered", img.name)
                continue
            results.append(importer.import_image(proj, img, config.COMPONENTS[img.component],
                                                 analyze=not args.no_analyze, force=args.force))
    print(json.dumps(results, indent=1))
    return 0


def cmd_stats(args) -> int:
    from . import stats

    out = {}
    with ghidra_boot.project() as proj:
        for img in _select(args):
            if ghidra_boot.get_file(proj, f"/{img.component}", img.name) is None:
                continue
            with ghidra_boot.open_program(proj, img.name, f"/{img.component}") as prog:
                out[img.name] = stats.flash_coverage(prog)
    print(json.dumps(out, indent=1))
    return 0


def cmd_match(args) -> int:
    from . import vt

    imgs = _select(args)
    results = []
    with ghidra_boot.project() as proj:
        for comp in sorted({i.component for i in imgs}):
            if comp not in config.COMPONENTS:
                continue
            group = [i for i in imgs if i.component == comp]
            for a, b in vt.pairs_for(group):
                results.append(vt.run_pair(proj, comp, a, b, force=args.force))
    print(json.dumps(results, indent=1))
    return 0


def cmd_export(args) -> int:
    from . import export

    with ghidra_boot.project() as proj:
        for img in _select(args):
            if img.component not in config.COMPONENTS or ghidra_boot.get_file(proj, f"/{img.component}", img.name) is None:
                continue
            with ghidra_boot.open_program(proj, img.name, f"/{img.component}") as prog:
                payload = export.export_image(prog, img, config.COMPONENTS[img.component])
            path = export.write(img, payload)
            logging.info("%s -> %s (%d functions, %d globals, %d strings)", img.name,
                         path.relative_to(config.REPO_ROOT), len(payload["functions"]),
                         len(payload["globals"]), len(payload["strings"]))
    return 0


def cmd_decompile(args) -> int:
    from . import decomp

    with ghidra_boot.project() as proj:
        for img in _select(args):
            if img.component not in config.COMPONENTS or ghidra_boot.get_file(proj, f"/{img.component}", img.name) is None:
                continue
            with ghidra_boot.open_program(proj, img.name, f"/{img.component}") as prog:
                payload = decomp.decompile_image(prog)
            path = decomp.write(img, payload)
            bad = sum(1 for v in payload.values() if v["c"] is None)
            logging.info("%s -> %s (%d functions, %d failed)", img.name,
                         path.relative_to(config.REPO_ROOT), len(payload), bad)
    return 0


def cmd_families(args) -> int:
    from . import families

    for comp in args.component or sorted(config.COMPONENTS):
        if not (config.ANALYSIS_DIR / "export" / comp).exists():
            continue
        payload = families.build(comp)
        families.write(comp, payload)
        print(comp, json.dumps(payload["stats"], indent=1))
    return 0


def cmd_plan(args) -> int:
    from . import plan

    for comp in args.component or sorted(config.COMPONENTS):
        paths = plan.make_waves(comp, wave=args.wave, force=args.force)
        print(f"{comp}: {len(paths)} work packets")
        for p in paths:
            print("  ", p.relative_to(config.REPO_ROOT))
    return 0


def cmd_check(args) -> int:
    from . import check

    bad = 0
    for comp in args.component or sorted(config.COMPONENTS):
        r = check.check_component(comp)
        errs, miss = r.pop("_errors"), r.pop("_missing_functions")
        print(json.dumps({k: v for k, v in r.items() if k != "per_image"}, indent=1))
        if args.verbose_errors:
            print("\n".join(errs), miss)
        bad += 0 if r["ok"] else 1
    return 1 if bad else 0


def cmd_apply(args) -> int:
    from . import annotations as ann, apply as ap, objects

    with ghidra_boot.project() as proj:
        for comp in args.component or sorted(config.COMPONENTS):
            fam = objects.load_families(comp)
            funcs, gl, tb, types = (ann.load_functions(comp), ann.load_globals(comp),
                                    ann.load_tables(comp), ann.load_types(comp))
            gres, _ = objects.resolve(comp, gl, "globals")
            tres, _ = objects.resolve(comp, tb, "tables")
            for img in fam["versions"]:
                with ghidra_boot.open_program(proj, img, f"/{comp}") as prog:
                    import pyghidra

                    with pyghidra.transaction(prog):
                        st = ap.apply_image(prog, comp, img, fam, funcs, gres, gl, tres, tb, types)
                    ghidra_boot.save(prog, "zt3re: apply annotations")
                logging.info("%s applied %s", img, st)
    return 0


def cmd_docs(args) -> int:
    from . import docgen

    for comp in args.component or sorted(config.COMPONENTS):
        for p in docgen.build_component(comp):
            logging.info("wrote %s", p.relative_to(config.REPO_ROOT))
    return 0


def cmd_validate(args) -> int:
    """Validate one annotation file (functions/globals/tables/types) against schema and families."""
    import re
    from pathlib import Path

    from . import annotations as ann, objects

    path = Path(args.file).resolve()
    comp = path.parent.parent.name if path.name != "types.json" else path.parent.name
    kind = path.parent.name
    j = json.loads(path.read_text())
    errs: list[str] = []
    if path.name == "types.json":
        errs += ann.validate_types(j)
    else:
        fam = objects.load_families(comp)
        key = {"functions": "functions", "globals": "globals", "tables": "tables"}[kind]
        for k, n in j.items():
            if k not in fam[key]:
                errs.append(f"{k}: not a known {key[:-1]} family of {comp}")
                continue
            errs += ann.validate_function(k, n) if kind == "functions" else ann.validate_data(k, n)
        existing = {"functions": ann.load_functions, "globals": ann.load_globals, "tables": ann.load_tables}[kind](comp)
        mine = {k: n.get("name") for k, n in j.items()}
        taken = {v.get("name"): k for k, v in existing.items() if k not in j and path.name not in str(k)}
        for k, nm in mine.items():
            if nm in taken:
                errs.append(f"{k}: name {nm!r} already used by {taken[nm]} in another file")
        if args.packet:
            ids = set(re.findall(r"^## `([\w]+)`", Path(args.packet).read_text(), re.M))
            miss = sorted(ids - set(j))
            extra = sorted(set(j) - ids)
            errs += [f"missing answer for {m}" for m in miss]
            errs += [f"unexpected entry {m} (not in packet)" for m in extra]
        names = [n.get("name") for n in j.values()]
        dup = {x for x in names if names.count(x) > 1}
        errs += [f"duplicate name inside file: {d}" for d in sorted(dup)]
    for e in errs:
        print("ERROR", e)
    print(f"{path.name}: {len(j)} entries, {len(errs)} problems")
    return 1 if errs else 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="zt3", description=__doc__)
    p.add_argument("-v", "--verbose", action="store_true")
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp):
        sp.add_argument("-c", "--component", action="append", choices=sorted(config.COMPONENTS))
        sp.add_argument("-i", "--image", action="append", help="image name, e.g. VCU_153")

    s = sub.add_parser("import", help="import images into the Ghidra project and auto-analyse")
    common(s)
    s.add_argument("--no-analyze", action="store_true")
    s.add_argument("--force", action="store_true")
    s.set_defaults(fn=cmd_import)

    s = sub.add_parser("stats", help="print code/data/undefined coverage per image")
    common(s)
    s.set_defaults(fn=cmd_stats)

    s = sub.add_parser("match", help="Ghidra Version Tracking between versions of each component")
    common(s)
    s.add_argument("--force", action="store_true")
    s.set_defaults(fn=cmd_match)

    s = sub.add_parser("export", help="export per-image facts to analysis/export/*.json")
    common(s)
    s.set_defaults(fn=cmd_export)

    s = sub.add_parser("decompile", help="decompile all functions into analysis/decomp/*.json (cache)")
    common(s)
    s.set_defaults(fn=cmd_decompile)

    s = sub.add_parser("families", help="merge VT matches into cross-version function/global families")
    s.add_argument("-c", "--component", action="append", choices=sorted(config.COMPONENTS))
    s.set_defaults(fn=cmd_families)

    s = sub.add_parser("plan", help="write annotation work packets (markdown) for subagents")
    s.add_argument("-c", "--component", action="append", choices=sorted(config.COMPONENTS))
    s.add_argument("-w", "--wave", type=int)
    s.add_argument("--force", action="store_true")
    s.set_defaults(fn=cmd_plan)

    s = sub.add_parser("check", help="coverage gate: everything described?")
    s.add_argument("-c", "--component", action="append", choices=sorted(config.COMPONENTS))
    s.add_argument("--verbose-errors", action="store_true")
    s.set_defaults(fn=cmd_check)

    s = sub.add_parser("apply", help="apply annotations to the Ghidra programs")
    s.add_argument("-c", "--component", action="append", choices=sorted(config.COMPONENTS))
    s.set_defaults(fn=cmd_apply)

    s = sub.add_parser("docs", help="generate markdown docs under docs/")
    s.add_argument("-c", "--component", action="append", choices=sorted(config.COMPONENTS))
    s.set_defaults(fn=cmd_docs)

    s = sub.add_parser("validate", help="validate one annotation JSON file (use before finishing a work packet)")
    s.add_argument("file")
    s.add_argument("--packet", help="work packet .md: every function in it must be answered")
    s.set_defaults(fn=cmd_validate)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format="%(asctime)s %(name)s %(levelname)s %(message)s")
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
