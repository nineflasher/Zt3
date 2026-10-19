"""Import firmware images into the shared Ghidra project and prepare them for analysis.

Per image we: load the raw bytes, relocate them to the component's load address, build a
proper memory map (flash / SRAM / peripheral / system blocks), decode the Cortex-M vector
table (labels, pointer types, seed functions) and run Ghidra's auto-analysis.
"""
from __future__ import annotations

import logging
from collections import Counter

from . import config, ghidra_boot
from .config import Component, Image
from .cortexm import vector_name

log = logging.getLogger("zt3re.import")


def _create_memory_map(prog, comp: Component, image_len: int):
    from ghidra.util.task import TaskMonitor
    from ghidra.program.model.address import AddressSet

    mem = prog.getMemory()
    blk = mem.getBlocks()[0]
    mem.moveBlock(blk, ghidra_boot.addr(prog, comp.base), TaskMonitor.DUMMY)
    blk.setName("FLASH")
    blk.setRead(True)
    blk.setWrite(False)
    blk.setExecute(True)
    blk.setComment(f"Application image ({image_len} bytes) loaded at {comp.base:#010x}")
    for r in comp.regions:
        if mem.getBlock(r.name) is not None:
            continue
        if r.size <= 0:
            continue
        b = mem.createUninitializedBlock(r.name, ghidra_boot.addr(prog, r.start), r.size, False)
        b.setRead(r.read)
        b.setWrite(r.write)
        b.setExecute(r.execute)
        b.setVolatile(r.volatile)
        b.setComment(r.comment)
    # Thumb mode everywhere in flash (Cortex-M has no ARM state).
    ctx = prog.getProgramContext()
    tmode = ctx.getRegister("TMode")
    if tmode is not None:
        from java.math import BigInteger

        ctx.setValue(tmode, blk.getStart(), blk.getEnd(), BigInteger.ONE)
    return blk


def _decode_vectors(prog, comp: Component, data: bytes) -> list[tuple[int, int, str]]:
    """Return [(slot, value, name)] for the exception vector table of the image."""
    import struct

    lo, hi = comp.base, comp.base + len(data)
    out: list[tuple[int, int, str]] = []
    for i in range(0, comp.max_vectors):
        off = comp.vector_offset + i * 4
        if off + 4 > len(data):
            break
        (v,) = struct.unpack_from("<I", data, off)
        if i == 0:
            if not (0x20000000 <= v < 0x20100000):
                raise ValueError(f"{comp.key}: slot 0 is not an initial SP ({v:#x})")
        elif v == 0 or (v & 1 and lo <= (v & ~1) < hi):
            pass
        else:
            break
        out.append((i, v, vector_name(i, comp.chip)))
    while len(out) > 16 and out[-1][1] == 0:   # trailing zero padding is not part of the table
        out.pop()
    return out


def _apply_vectors(prog, comp: Component, vectors):
    from ghidra.program.flatapi import FlatProgramAPI
    from ghidra.program.model.data import PointerDataType, DWordDataType
    from ghidra.program.model.symbol import SourceType
    from ghidra.program.model.listing import CodeUnit

    api = FlatProgramAPI(prog)
    listing = prog.getListing()
    symtab = prog.getSymbolTable()
    targets = Counter(v & ~1 for (i, v, _) in vectors if i > 0 and v)
    for slot, v, name in vectors:
        a = ghidra_boot.addr(prog, comp.base + comp.vector_offset + slot * 4)
        listing.clearCodeUnits(a, a.add(3), False)
        dt = DWordDataType() if slot == 0 else PointerDataType()
        listing.createData(a, dt)
        symtab.createLabel(a, f"vector_{name}", SourceType.IMPORTED)
        listing.setComment(a, CodeUnit.EOL_COMMENT, f"vector[{slot}] = {v:#010x}")
        if slot == 0 or not v:
            continue
        t = ghidra_boot.addr(prog, v & ~1)
        fname = name if targets[v & ~1] < 3 else "Default_Handler"
        if listing.getFunctionAt(t) is None:
            api.disassemble(t)
            api.createFunction(t, fname)
        else:
            api.getFunctionAt(t).setName(fname, SourceType.IMPORTED)
        f = api.getFunctionAt(t)
        if f is not None and fname != name and symtab.getGlobalSymbol(name, t) is None:
            symtab.createLabel(t, name, SourceType.IMPORTED)
    entry = ghidra_boot.addr(prog, vectors[1][1] & ~1)
    symtab.addExternalEntryPoint(entry)


def import_image(project, image: Image, comp: Component, analyze: bool = True, force: bool = False) -> dict:
    import pyghidra
    from ghidra.app.util.opinion import BinaryLoader
    from ghidra.util.task import TaskMonitor

    folder = f"/{comp.key}"
    ghidra_boot.ensure_folder(project, folder)
    existing = ghidra_boot.get_file(project, folder, image.name)
    if existing is not None:
        if not force:
            log.info("%s already imported (use --force to redo)", image.name)
            return {"image": image.name, "skipped": True}
        existing.delete()
    data = image.path.read_bytes()
    builder = (pyghidra.program_loader().project(project).source(str(image.path))
               .projectFolderPath(folder).name(image.name).language(comp.language).loaders(BinaryLoader))
    with builder.load() as res:
        prog = res.getPrimaryDomainObject()
        with pyghidra.transaction(prog):
            _create_memory_map(prog, comp, len(data))
            if comp.key == "ble":
                from . import ble

                ble.apply(prog, data)
            vectors = _decode_vectors(prog, comp, data)
            _apply_vectors(prog, comp, vectors)
        info = {}
        if analyze:
            pyghidra.analyze(prog)
            from . import enrich

            with pyghidra.transaction(prog):
                info = enrich.apply(prog, comp)
            pyghidra.analyze(prog)
        res.save(TaskMonitor.DUMMY)
        nfun = prog.getFunctionManager().getFunctionCount()
    log.info("%s: %d vectors, %d functions, %s", image.name, len(vectors), nfun, info)
    return {"image": image.name, "vectors": len(vectors), "functions": nfun}
