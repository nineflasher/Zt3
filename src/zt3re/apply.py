"""Apply the annotation store to the Ghidra programs (names, comments, namespaces, types, data)."""
from __future__ import annotations

import logging

from . import annotations as ann
from . import ghidra_boot, objects

log = logging.getLogger("zt3re.apply")

TYPE_CATEGORY = "/zt3"


def _prim(name: str):
    from ghidra.program.model.data import (BooleanDataType, ByteDataType, CharDataType, DoubleDataType,
                                           FloatDataType, PointerDataType, SignedByteDataType,
                                           ShortDataType, UnsignedShortDataType, IntegerDataType,
                                           UnsignedIntegerDataType, LongLongDataType,
                                           UnsignedLongLongDataType, VoidDataType)
    return {
        "u8": ByteDataType, "s8": SignedByteDataType, "u16": UnsignedShortDataType, "s16": ShortDataType,
        "u32": UnsignedIntegerDataType, "s32": IntegerDataType, "u64": UnsignedLongLongDataType,
        "s64": LongLongDataType, "f32": FloatDataType, "f64": DoubleDataType, "bool": BooleanDataType,
        "char": CharDataType, "ptr": PointerDataType, "void": VoidDataType,
    }[name]()


def build_types(prog, types: dict) -> dict:
    """Create/replace the annotated structs and enums in the program; returns {name: DataType}."""
    from ghidra.program.model.data import (ArrayDataType, CategoryPath, DataTypeConflictHandler, EnumDataType,
                                           PointerDataType, StructureDataType)

    dtm = prog.getDataTypeManager()
    cat = CategoryPath(TYPE_CATEGORY)
    made: dict = {}
    for name, e in types.get("enums", {}).items():
        et = EnumDataType(cat, name, e.get("size", 4))
        for v in e["values"]:
            et.add(v["name"], v["value"], v.get("description", ""))
        made[name] = dtm.resolve(et, DataTypeConflictHandler.REPLACE_HANDLER)

    def resolve_type(t: str):
        base, _, arg = t.partition(":")
        if base == "ptr" and arg and arg != "void":
            tgt = made.get(arg)
            return PointerDataType(tgt) if tgt is not None else PointerDataType()
        if base in ("u8", "u16", "u32", "u64", "s8", "s16", "s32", "s64", "f32", "f64", "bool", "ptr", "void", "char"):
            return _prim(base)
        return made[t]

    # structs may reference each other: iterate until all resolved
    pending = dict(types.get("structs", {}))
    for _ in range(len(pending) + 1):
        for name in list(pending):
            s = pending[name]
            deps = [f["type"].partition(":")[2] if f["type"].startswith("ptr:") else f["type"] for f in s["fields"]]
            if any(d in pending and d != name and d not in made for d in deps if d in types["structs"]):
                continue
            st = StructureDataType(cat, name, s["size"])
            for f in s["fields"]:
                dt = resolve_type(f["type"])
                count = f.get("count", 1)
                if count and count > 1:
                    dt = ArrayDataType(dt, count, dt.getLength())
                    length = dt.getLength()
                else:
                    length = dt.getLength()
                if length <= 0:
                    length = 1
                st.replaceAtOffset(f["offset"], dt, length, f["name"], f["description"])
            st.setDescription(s["description"])
            made[name] = dtm.resolve(st, DataTypeConflictHandler.REPLACE_HANDLER)
            del pending[name]
        if not pending:
            break
    if pending:
        raise RuntimeError(f"unresolvable struct dependencies: {sorted(pending)}")
    return made


def _plate(n: dict) -> str:
    lines = [n["summary"].strip(), "", n["description"].strip()]
    if n.get("params"):
        lines += ["", "Parameters:"] + [f"  {p['name']} ({p['type']}): {p['description']}" for p in n["params"]]
    r = n.get("returns")
    if r and r.get("type") and r["type"] != "void":
        lines += ["", f"Returns ({r['type']}): {r['description']}"]
    if n.get("notes"):
        lines += ["", "Notes: " + n["notes"].strip()]
    lines += ["", f"[confidence: {n['confidence']}] [module: {n['category']}]"]
    return "\n".join(lines)


def apply_image(prog, comp: str, image: str, fam: dict, funcs: dict, globals_resolved: dict,
                globals_notes: dict, tables_resolved: dict, tables_notes: dict, types: dict) -> dict:
    from ghidra.program.model.symbol import SourceType
    from ghidra.program.model.listing import CodeUnit

    fm = prog.getFunctionManager()
    symtab = prog.getSymbolTable()
    listing = prog.getListing()
    stats = {"functions": 0, "data": 0, "params": 0}
    made = build_types(prog, types) if types.get("structs") or types.get("enums") else {}

    node = {(n, a): fid for fid, f in fam["functions"].items() for n, a in f["members"].items()}
    gns = prog.getGlobalNamespace()
    for f in fm.getFunctions(True):
        fid = node.get((image, f.getEntryPoint().getOffset()))
        n = funcs.get(fid)
        if not n:
            continue
        f.setName(n["name"], SourceType.USER_DEFINED)
        ns = symtab.getOrCreateNameSpace(gns, n["category"], SourceType.USER_DEFINED)
        f.setParentNamespace(ns)
        f.setComment(_plate(n))
        params = n.get("params") or []
        if params and f.getParameterCount() == len(params):
            for p, gp in zip(params, f.getParameters()):
                try:
                    gp.setName(p["name"], SourceType.USER_DEFINED)
                    gp.setComment(p["description"])
                    stats["params"] += 1
                except Exception as e:                    # name clashes etc. are non-fatal
                    log.debug("param %s: %s", p["name"], e)
        stats["functions"] += 1

    for kind, resolved, notes in (("g", globals_resolved, globals_notes), ("t", tables_resolved, tables_notes)):
        for oid, r in resolved.items():
            start = r["starts"].get(image)
            n = notes[oid]
            if start is None:
                continue
            a = ghidra_boot.addr(prog, start)
            try:
                end = a.add(n["size"] - 1)
                dt = _data_type(n, made)
                if dt is not None and dt.getLength() > 0:
                    listing.clearCodeUnits(a, a.add(max(dt.getLength(), 1) - 1), False)
                    listing.createData(a, dt)
                symtab.createLabel(a, n["name"], SourceType.USER_DEFINED)
                listing.setComment(a, CodeUnit.PLATE_COMMENT, n["description"])
                stats["data"] += 1
            except Exception as e:
                log.warning("%s %s @%#x: %s", image, n["name"], start, e)
    return stats


def _data_type(n: dict, made: dict):
    from ghidra.program.model.data import ArrayDataType

    t = n["type"]
    count = n.get("count", 1) or 1
    base, _, arg = t.partition(":")
    if base in ("u8", "u16", "u32", "u64", "s8", "s16", "s32", "s64", "f32", "f64", "bool", "char", "ptr"):
        dt = _prim(base)
    elif t in made:
        dt = made[t]
    else:
        return None
    if count > 1:
        return ArrayDataType(dt, count, dt.getLength())
    return dt
