"""Resolve annotated data objects (globals / tables) to concrete addresses in every firmware version."""
from __future__ import annotations

import json
from collections import Counter, defaultdict

from . import config


def load_families(comp: str) -> dict:
    return json.loads((config.ANALYSIS_DIR / "families" / f"{comp}.json").read_text())


def parse_addr(v) -> int:
    return int(v, 16) if isinstance(v, str) else int(v)


def resolve(comp: str, notes: dict, fam_key: str) -> tuple[dict, list[str]]:
    """Return ({object_id: {"covers": [fam ids], "starts": {image: addr}, "size"}}, errors).

    An object anchored at (image, start) with `size` covers every family with a member inside
    [start, start+size) of that image.  Its start in the other images follows from those families'
    members; families living only in those other images are then covered too (second pass), so one
    object describes the variable in every build even where the family map could not align it.
    """
    fam = load_families(comp)[fam_key]
    by_img: dict[str, list[tuple[int, str]]] = defaultdict(list)
    for fid, f in fam.items():
        for img, a in f["members"].items():
            by_img[img].append((a, fid))
    for lst in by_img.values():
        lst.sort()
    errs: list[str] = []
    out: dict = {}
    for oid, n in notes.items():
        img, start = n["anchor"][0], parse_addr(n["anchor"][1])
        size = n["size"]
        starts_best = {img: start}
        covered: set[str] = set()
        for _ in range(2):                                    # anchor pass, then cross-build pass
            starts: dict[str, Counter] = defaultdict(Counter)
            for i, s0 in starts_best.items():
                for a, fid in by_img.get(i, []):
                    if s0 <= a < s0 + size:
                        covered.add(fid)
                        for img2, a2 in fam[fid]["members"].items():
                            starts[img2][a2 - (a - s0)] += 1
            new_starts = {i: c.most_common(1)[0][0] for i, c in starts.items()}
            new_starts[img] = start
            if new_starts == starts_best:
                break
            starts_best = new_starts
        out[oid] = {"covers": sorted(covered), "starts": starts_best, "size": size}
    return out, errs


def uncovered(comp: str, notes: dict, fam_key: str) -> list[str]:
    """Family ids not covered by any annotated object (in the image the object is anchored to)."""
    fam = load_families(comp)[fam_key]
    resolved, _ = resolve(comp, notes, fam_key)
    covered = {fid for r in resolved.values() for fid in r["covers"]}
    return sorted(set(fam) - covered)


def overlaps(comp: str, notes: dict, fam_key: str, exclude_file_keys: set[str] | None = None) -> list[str]:
    """Objects in `notes` that overlap objects already defined elsewhere in the component (same image)."""
    from . import annotations as ann

    others = ann.load_globals(comp) if fam_key == "globals" else ann.load_tables(comp)
    others = {k: v for k, v in others.items() if k not in notes}
    mine, _ = resolve(comp, notes, fam_key)
    theirs, _ = resolve(comp, others, fam_key)
    errs: list[str] = []
    for oid, r in mine.items():
        for img, start in r["starts"].items():
            end = start + r["size"]
            for oid2, r2 in theirs.items():
                s2 = r2["starts"].get(img)
                if s2 is None:
                    continue
                if start < s2 + r2["size"] and s2 < end:
                    errs.append(f"{oid} ({notes[oid]['name']}) overlaps {oid2} ({others[oid2]['name']}) in {img}: "
                                f"{start:#x}+{r['size']} vs {s2:#x}+{r2['size']}")
                    break
    return errs
