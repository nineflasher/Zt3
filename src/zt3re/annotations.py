"""Annotation store: schemas, loading, merging and validation.

Layout (per component <c>):
  annotations/<c>/functions/*.json   {family_id: FunctionNote}
  annotations/<c>/globals/*.json     {object_id: DataNote}     (RAM variables)
  annotations/<c>/tables/*.json      {object_id: DataNote}     (flash tables / constants)
  annotations/<c>/types.json         {"structs": {...}, "enums": {...}}
  annotations/<c>/module.json        component overview and module (category) descriptions

FunctionNote : name, summary, description, category, params[{name,type,description}],
               returns{type,description}, confidence (high|medium|low), [notes], [hw]
DataNote     : name, type, size, description, category, [anchor addr], [members]
All text fields must be non-empty; names must be valid C identifiers and unique per component.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from . import config

IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
CONFIDENCE = {"high", "medium", "low"}
PRIMS = {"u8", "u16", "u32", "u64", "s8", "s16", "s32", "s64", "f32", "f64", "bool", "ptr", "void", "char"}


class AnnotationError(Exception):
    pass


def _load_dir(d: Path) -> dict:
    out: dict = {}
    if not d.exists():
        return out
    for p in sorted(d.glob("*.json")):
        try:
            j = json.loads(p.read_text())
        except json.JSONDecodeError as e:
            raise AnnotationError(f"{p}: invalid JSON: {e}") from e
        for k, v in j.items():
            if k in out:
                raise AnnotationError(f"{p}: duplicate key {k} (also defined elsewhere)")
            out[k] = v
    return out


def load_functions(comp: str) -> dict:
    return _load_dir(config.ANNOTATIONS_DIR / comp / "functions")


def load_globals(comp: str) -> dict:
    return _load_dir(config.ANNOTATIONS_DIR / comp / "globals")


def load_tables(comp: str) -> dict:
    return _load_dir(config.ANNOTATIONS_DIR / comp / "tables")


def load_types(comp: str) -> dict:
    """Merge annotations/<c>/types/*.json (one per data packet) and the optional legacy types.json."""
    out: dict = {"structs": {}, "enums": {}}
    files = sorted((config.ANNOTATIONS_DIR / comp / "types").glob("*.json")) if (config.ANNOTATIONS_DIR / comp / "types").exists() else []
    legacy = config.ANNOTATIONS_DIR / comp / "types.json"
    if legacy.exists():
        files.append(legacy)
    for p in files:
        j = json.loads(p.read_text())
        for sect in ("structs", "enums"):
            for k, v in j.get(sect, {}).items():
                if k in out[sect]:
                    raise AnnotationError(f"{p}: {sect[:-1]} {k} already defined in another file")
                out[sect][k] = v
    return out


def _text(errs: list[str], where: str, d: dict, key: str, min_len: int = 3) -> None:
    v = d.get(key)
    if not isinstance(v, str) or len(v.strip()) < min_len:
        errs.append(f"{where}: missing/empty '{key}'")


def validate_function(fid: str, n: dict) -> list[str]:
    errs: list[str] = []
    w = f"function {fid}"
    if not isinstance(n.get("name"), str) or not IDENT.match(n["name"]):
        errs.append(f"{w}: invalid name {n.get('name')!r}")
    _text(errs, w, n, "summary", 8)
    _text(errs, w, n, "description", 20)
    _text(errs, w, n, "category", 2)
    if n.get("confidence") not in CONFIDENCE:
        errs.append(f"{w}: confidence must be one of {sorted(CONFIDENCE)}")
    for i, p in enumerate(n.get("params") or []):
        for k in ("name", "type", "description"):
            if not isinstance(p.get(k), str) or not p[k].strip():
                errs.append(f"{w}: params[{i}] missing '{k}'")
    r = n.get("returns")
    if not isinstance(r, dict) or not isinstance(r.get("type"), str) or not isinstance(r.get("description"), str):
        errs.append(f"{w}: 'returns' must be {{type, description}}")
    return errs


def validate_data(oid: str, n: dict, types: dict | None = None) -> list[str]:
    errs: list[str] = []
    w = f"data {oid}"
    if not isinstance(n.get("name"), str) or not IDENT.match(n["name"]):
        errs.append(f"{w}: invalid name {n.get('name')!r}")
    _text(errs, w, n, "description", 8)
    _text(errs, w, n, "type", 2)
    if not isinstance(n.get("size"), int) or n["size"] <= 0:
        errs.append(f"{w}: size must be a positive int")
    if not isinstance(n.get("anchor"), list) or len(n["anchor"]) != 2:
        errs.append(f"{w}: anchor must be [image, address]")
    return errs


def validate_types(t: dict) -> list[str]:
    errs: list[str] = []
    structs, enums = t.get("structs", {}), t.get("enums", {})
    for name, s in structs.items():
        w = f"struct {name}"
        if not IDENT.match(name):
            errs.append(f"{w}: invalid name")
        _text(errs, w, s, "description", 8)
        if not isinstance(s.get("size"), int) or s["size"] <= 0:
            errs.append(f"{w}: size must be a positive int")
        last_end = 0
        for f in s.get("fields", []):
            fw = f"{w}.{f.get('name')}"
            if not isinstance(f.get("name"), str) or not IDENT.match(f["name"]):
                errs.append(f"{fw}: invalid field name")
            _text(errs, fw, f, "description", 4)
            if not isinstance(f.get("offset"), int) or f["offset"] < last_end:
                errs.append(f"{fw}: offset missing/overlapping/unsorted")
            else:
                last_end = f["offset"] + _type_size(f.get("type", ""), f.get("count", 1), structs, enums)
            _check_type(errs, fw, f.get("type", ""), structs, enums)
        if last_end > s.get("size", 0):
            errs.append(f"{w}: fields extend to {last_end} beyond size {s.get('size')}")
    for name, e in enums.items():
        w = f"enum {name}"
        _text(errs, w, e, "description", 8)
        for v in e.get("values", []):
            if not IDENT.match(str(v.get("name", ""))) or not isinstance(v.get("value"), int):
                errs.append(f"{w}: bad value entry {v}")
            _text(errs, f"{w}.{v.get('name')}", v, "description", 3)
    return errs


_SIZES = {"u8": 1, "s8": 1, "bool": 1, "char": 1, "u16": 2, "s16": 2, "u32": 4, "s32": 4, "f32": 4, "ptr": 4,
          "u64": 8, "s64": 8, "f64": 8}


def _type_size(t: str, count: int, structs: dict, enums: dict) -> int:
    base = t.split(":")[0]
    if base in _SIZES:
        sz = _SIZES[base]
    elif t in structs:
        sz = structs[t].get("size", 0)
    elif t in enums:
        sz = enums[t].get("size", 4)
    else:
        sz = 0
    return sz * (count or 1)


def _check_type(errs: list[str], where: str, t: str, structs: dict, enums: dict) -> None:
    base, _, arg = t.partition(":")
    if base in PRIMS:
        if arg and arg not in structs and arg not in enums and base == "ptr" and arg != "void":
            errs.append(f"{where}: unknown pointer target {arg!r}")
        return
    if t not in structs and t not in enums:
        errs.append(f"{where}: unknown type {t!r}")


def validate_all(comp: str) -> list[str]:
    errs: list[str] = []
    funcs, globs, tabs, types = load_functions(comp), load_globals(comp), load_tables(comp), load_types(comp)
    names: dict[str, str] = {}
    for fid, n in funcs.items():
        errs += validate_function(fid, n)
    for oid, n in {**globs, **tabs}.items():
        errs += validate_data(oid, n, types)
    for kind, d in (("function", funcs), ("data", {**globs, **tabs})):
        for k, n in d.items():
            nm = n.get("name")
            if nm in names and names[nm] != k:
                errs.append(f"{kind} {k}: name {nm!r} already used by {names[nm]}")
            names[nm] = k
    errs += validate_types(types)
    return errs


FID_RE = re.compile(r"\b(?:ble|vcu|mcu|bms)_(?:[gt]_)?[0-9a-f]{3,5}_[0-9a-f]{8}\b")


def expand_refs(text: str, names: dict[str, str]) -> str:
    """Replace raw family ids mentioned in prose by the documented names (`fid` -> `name`)."""
    return FID_RE.sub(lambda m: names.get(m.group(0), m.group(0)), text or "")


def name_map(comp: str) -> dict[str, str]:
    out = {fid: n["name"] for fid, n in load_functions(comp).items()}
    out.update({oid: n["name"] for oid, n in {**load_globals(comp), **load_tables(comp)}.items()})
    return out
