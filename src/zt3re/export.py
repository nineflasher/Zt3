"""Export per-image facts (functions, call graph, globals, tables, strings) from Ghidra to JSON.

The JSON files under analysis/export/<component>/<image>.json are the interface between
Ghidra and everything else (matching across versions, annotation tooling, docs, checks).
"""
from __future__ import annotations

import hashlib
import json
import re
import zlib
from collections import defaultdict
from pathlib import Path

from . import config, ghidra_boot
from .config import Component, Image

_HEX = re.compile(r"0x[0-9a-fA-F]+")
_REG_RAM = ("SRAM", ".data", ".bss_heap", "SRAM_ROM_AREA")
_PERIPH = ("PERIPH", "PERIPH_AHB2", "SYSTEM")


def _norm(ins) -> str:
    return _HEX.sub("K", str(ins))


def _jbytes(b) -> bytes:
    return bytes((x & 0xFF) for x in b)


def export_image(prog, image: Image, comp: Component) -> dict:
    mem = prog.getMemory()
    listing = prog.getListing()
    fm = prog.getFunctionManager()
    symtab = prog.getSymbolTable()
    refmgr = prog.getReferenceManager()
    flash = mem.getBlock("FLASH")
    data = image.path.read_bytes()

    def block_name(a):
        b = mem.getBlock(a)
        return b.getName() if b else None

    funcs = []
    callers: dict[int, set[int]] = defaultdict(set)
    ram_refs: dict[int, dict] = defaultdict(lambda: {"r": set(), "w": set(), "widths": set()})
    flash_refs: dict[int, set[int]] = defaultdict(set)
    str_refs: dict[int, set[int]] = defaultdict(set)

    for f in fm.getFunctions(True):
        if f.isExternal():
            continue
        entry = f.getEntryPoint().getOffset()
        body = f.getBody()
        h_bytes = hashlib.sha1()
        h_norm = hashlib.sha1()
        h_mnem = hashlib.sha1()
        n_ins = 0
        callees: set[int] = set()
        indirect = 0
        periph: dict[int, set[str]] = defaultdict(set)
        rams: dict[int, set[str]] = defaultdict(set)
        fl_data: set[int] = set()
        strs: set[int] = set()
        ram_seq: list[list[int]] = []       # [instruction index, address] in execution-text order
        rod_seq: list[list[int]] = []
        isq: list[str] = []                 # 4-hex normalised hash per instruction (for diff alignment)
        for ins in listing.getInstructions(body, True):
            n_ins += 1
            h_bytes.update(_jbytes(ins.getBytes()))
            nt = _norm(ins).encode()
            h_norm.update(nt)
            isq.append("%04x" % (zlib.crc32(nt) & 0xFFFF))
            h_mnem.update(ins.getMnemonicString().encode())
            mnem = ins.getMnemonicString().lower()
            for r in ins.getReferencesFrom():
                rt = r.getReferenceType()
                to = r.getToAddress()
                if not to.isMemoryAddress():
                    continue
                off = to.getOffset()
                bn = block_name(to)
                if rt.isCall():
                    if rt.isComputed():
                        indirect += 1
                    else:
                        callees.add(off)
                elif rt.isJump():
                    # tail call into another function
                    tf = fm.getFunctionContaining(to)
                    if tf is not None and tf.getEntryPoint().getOffset() != entry and not body.contains(to):
                        callees.add(tf.getEntryPoint().getOffset())
                elif bn in _PERIPH:
                    periph[off].add("R" if rt.isRead() else "W" if rt.isWrite() else "A")
                elif bn in _REG_RAM:
                    kind = "R" if rt.isRead() else "W" if rt.isWrite() else "A"
                    rams[off].add(kind)
                    ram_seq.append([n_ins, off])
                    ram_refs[off]["widths"].add(_width(mnem))
                    if kind == "R":
                        ram_refs[off]["r"].add(entry)
                    elif kind == "W":
                        ram_refs[off]["w"].add(entry)
                    else:
                        ram_refs[off]["r"].add(entry)     # address taken
                elif bn == "FLASH" and not rt.isFlow():
                    if r.getSource().toString() == "DEFAULT":
                        continue                       # pc-relative literal-pool slot, not a data object
                    d = listing.getDataAt(to)
                    if d is not None and d.hasStringValue():
                        strs.add(off)
                        str_refs[off].add(entry)
                    elif listing.getInstructionAt(to) is None:
                        fl_data.add(off)
                        rod_seq.append([n_ins, off])
                        flash_refs[off].add(entry)
        for c in callees:
            callers[c].add(entry)
        name = f.getName()
        funcs.append({
            "addr": entry,
            "name": name,
            "auto_name": bool(re.match(r"^(FUN|thunk_FUN|LAB|SUB)_", name)),
            "size": int(body.getNumAddresses()),
            "n_insn": n_ins,
            "hash_bytes": h_bytes.hexdigest()[:16],
            "hash_norm": h_norm.hexdigest()[:16],
            "hash_mnem": h_mnem.hexdigest()[:16],
            "callees": sorted(callees),
            "indirect_calls": indirect,
            "periph": {hex(a): "".join(sorted(k)) for a, k in sorted(periph.items())},
            "ram": {hex(a): "".join(sorted(k)) for a, k in sorted(rams.items())},
            "isq": "".join(isq),
            "ram_seq": ram_seq,
            "rodata": sorted(fl_data),
            "rodata_seq": rod_seq,
            "strings": sorted(strs),
            "is_thunk": bool(f.isThunk()),
            "vector": None,
        })
    for fn in funcs:
        fn["callers"] = sorted(callers.get(fn["addr"], ()))

    # strings -------------------------------------------------------------------------------
    strings = []
    for d in listing.getDefinedData(True):
        if d.hasStringValue() and block_name(d.getAddress()) in ("FLASH", ".data"):
            a = d.getAddress().getOffset()
            strings.append({"addr": a, "text": str(d.getValue())[:200], "refs": sorted(str_refs.get(a, ()))})

    # flash tables / constants referenced from code ------------------------------------------
    tables = []
    for a, refs in sorted(flash_refs.items()):
        d = listing.getDataAt(ghidra_boot.addr(prog, a))
        tables.append({"addr": a, "type": str(d.getDataType().getName()) if d else None,
                       "size": d.getLength() if d else None, "refs": sorted(refs)})

    # globals ---------------------------------------------------------------------------------
    globals_ = [{"addr": a, "reads": sorted(v["r"]), "writes": sorted(v["w"]),
                 "widths": sorted(v["widths"])} for a, v in sorted(ram_refs.items())]

    vectors = []
    for sym in symtab.getAllSymbols(False):
        if sym.getName().startswith("vector_"):
            d = listing.getDataAt(sym.getAddress())
            vectors.append({"slot": (sym.getAddress().getOffset() - comp.base - comp.vector_offset) // 4,
                            "name": sym.getName()[7:], "value": int(d.getValue().getOffset()) if d and d.getValue() is not None and hasattr(d.getValue(), "getOffset") else None})
    vectors.sort(key=lambda v: v["slot"])
    by_addr = {f["addr"]: f for f in funcs}
    for v in vectors:
        if v["value"] and (v["value"] & ~1) in by_addr:
            by_addr[v["value"] & ~1]["vector"] = v["name"]

    return {
        "image": image.name, "component": comp.key, "version": image.version,
        "sha256": hashlib.sha256(data).hexdigest(), "size": len(data),
        "base": comp.base, "chip": comp.chip,
        "functions": funcs, "globals": globals_, "tables": tables, "strings": strings,
        "vectors": vectors,
    }


def _width(mnem: str) -> int:
    m = mnem.split(".")[0]
    if m.endswith("b") or m in ("ldrsb", "strb", "ldrb"):
        return 1
    if m.endswith("h") or m in ("ldrsh", "strh", "ldrh"):
        return 2
    if m.startswith(("vldr", "vstr")):
        return 4
    if m.startswith(("ldm", "stm", "ldrd", "strd", "push", "pop")):
        return 4
    return 4


def out_path(image: Image) -> Path:
    return config.ANALYSIS_DIR / "export" / image.component / f"{image.name}.json"


def write(image: Image, payload: dict) -> Path:
    p = out_path(image)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, separators=(",", ":")))
    return p
