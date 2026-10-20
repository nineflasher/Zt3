"""Documentation coverage gate: every function, global, table and type must be described."""
from __future__ import annotations

import json

from . import annotations as ann
from . import config, objects


def check_component(comp: str) -> dict:
    fam = objects.load_families(comp)
    funcs = ann.load_functions(comp)
    globs = ann.load_globals(comp)
    tabs = ann.load_tables(comp)
    types = ann.load_types(comp)
    errors = ann.validate_all(comp)
    missing_f = sorted(set(fam["functions"]) - set(funcs))
    stale_f = sorted(set(funcs) - set(fam["functions"]))
    unc_g = objects.uncovered(comp, globs, "globals")
    unc_t = objects.uncovered(comp, tabs, "tables")
    # per-image function coverage
    per_image = {}
    for img in fam["versions"]:
        ex = json.loads((config.ANALYSIS_DIR / "export" / comp / f"{img}.json").read_text())
        node = {(n, a): fid for fid, f in fam["functions"].items() for n, a in f["members"].items()}
        miss = [f["addr"] for f in ex["functions"] if node[(img, f["addr"])] not in funcs]
        per_image[img] = {"functions": len(ex["functions"]), "undocumented": len(miss)}
    ok = not (errors or missing_f or stale_f or unc_g or unc_t)
    return {
        "component": comp, "ok": ok,
        "function_families": len(fam["functions"]), "documented_functions": len(funcs) - len(stale_f),
        "missing_functions": len(missing_f), "stale_function_notes": len(stale_f),
        "global_families": len(fam["globals"]), "uncovered_globals": len(unc_g),
        "table_families": len(fam["tables"]), "uncovered_tables": len(unc_t),
        "structs": len(types.get("structs", {})), "enums": len(types.get("enums", {})),
        "validation_errors": len(errors), "per_image": per_image,
        "_errors": errors[:50], "_missing_functions": missing_f[:20],
    }
