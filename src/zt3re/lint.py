"""Style / hygiene lint for annotation text (errors fail the build, warnings are quality hints)."""
from __future__ import annotations

import re
from collections import Counter

from . import annotations as ann

HEX_BLOB = re.compile(r"(?:\b(?:0x)?[0-9a-fA-F]{2}\b[ ,:-]*){16,}")        # >= 16 hex bytes in a row
# a run of 16+ letters/digits with >= 3 lower, 3 upper and 3 digits and no 0x prefix: a key, not an identifier
KEYISH = re.compile(r"(?<![\w/])(?!0x)(?=[A-Za-z0-9]{16,}\b)(?=(?:[^a-z]*[a-z]){3})(?=(?:[^A-Z]*[A-Z]){3})(?=(?:[^0-9]*[0-9]){3})[A-Za-z0-9]{16,64}\b")
BANNED = ("todo", "tbd", "unknown function", "does something", "not sure what", "lorem")
ADDR_SUFFIX = re.compile(r"_[0-9a-f]{6,8}$")
PARAM_DEFAULT = re.compile(r"^param_\d+$")
SNAKE = re.compile(r"^[a-z][a-z0-9_]*$")


def _text_fields(n: dict):
    for k in ("summary", "description", "notes"):
        if n.get(k):
            yield k, n[k]
    for p in n.get("params") or []:
        yield "param", p.get("description", "")


def lint_component(comp: str) -> dict:
    errors: list[str] = []
    warns: list[str] = []
    funcs = ann.load_functions(comp)
    data = {**ann.load_globals(comp), **ann.load_tables(comp)}
    conf = Counter()
    for fid, n in funcs.items():
        conf[n.get("confidence")] += 1
        if len(n.get("summary", "")) > 110:
            warns.append(f"{fid}: summary longer than 110 chars")
        if n.get("summary", "").strip().lower() == n.get("description", "").strip().lower():
            warns.append(f"{fid}: description merely repeats the summary")
        if ADDR_SUFFIX.search(n.get("name", "")):
            warns.append(f"{fid}: name carries an address suffix ({n['name']})")
        if not SNAKE.match(n.get("category", "")):
            warns.append(f"{fid}: category {n.get('category')!r} is not snake_case")
        dflt = [p["name"] for p in n.get("params") or [] if PARAM_DEFAULT.match(p.get("name", ""))]
        if dflt:
            warns.append(f"{fid}: parameters keep decompiler names {dflt}")
        for k, t in _text_fields(n):
            low = t.lower()
            if any(b in low for b in BANNED):
                warns.append(f"{fid}: placeholder wording in {k}")
            if HEX_BLOB.search(t):
                errors.append(f"{fid}: long hex byte run in {k} (never record key/secret bytes)")
            if KEYISH.search(t):
                errors.append(f"{fid}: key-like token in {k} (never record key/secret values)")
    for oid, n in data.items():
        for k, t in _text_fields(n):
            if HEX_BLOB.search(t):
                errors.append(f"{oid}: long hex byte run in {k} (never record key/secret bytes)")
    return {"component": comp, "functions": len(funcs), "data_objects": len(data),
            "confidence": dict(conf), "errors": errors, "warnings": warns}
