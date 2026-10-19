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
    """Return ({object_id: {"covers": [fam ids], "starts": {image: addr}}}, errors).

    `fam_key` is 'globals' or 'tables'.  An object anchored at (image, start) with `size` covers every
    family that has a member address inside [start, start+size) of that image.  The object's start in
    another image is derived from the covered families' member addresses.
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
        lst = by_img.get(img, [])
        covered = [(a, fid) for a, fid in lst if start <= a < start + size]
        starts: dict[str, Counter] = defaultdict(Counter)
        for a, fid in covered:
            for img2, a2 in fam[fid]["members"].items():
                starts[img2][a2 - (a - start)] += 1
        starts_best = {i: c.most_common(1)[0][0] for i, c in starts.items()}
        starts_best.setdefault(img, start)
        out[oid] = {"covers": sorted({fid for _, fid in covered}), "starts": starts_best, "size": size}
    return out, errs


def uncovered(comp: str, notes: dict, fam_key: str) -> list[str]:
    """Family ids not covered by any annotated object (in the image the object is anchored to)."""
    fam = load_families(comp)[fam_key]
    resolved, _ = resolve(comp, notes, fam_key)
    covered = {fid for r in resolved.values() for fid in r["covers"]}
    return sorted(set(fam) - covered)
