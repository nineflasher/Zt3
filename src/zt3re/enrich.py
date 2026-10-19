"""Post-analysis enrichment: hardware register structs, peripheral labels and strings."""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path

from . import ghidra_boot
from .config import Component

log = logging.getLogger("zt3re.enrich")

HW_DIR = Path(__file__).parent / "data" / "hw"
HW_FILES = {
    "stm32f103": ("stm32f1.h", "peripherals_stm32f1.json"),
    "stm32f0": ("stm32f0.h", "peripherals_stm32f0.json"),
}
HW_CATEGORY = "/stm32"


def apply_hw(prog, comp: Component) -> int:
    """Parse the CMSIS-style header into the program, label peripherals and type their registers."""
    if comp.chip not in HW_FILES:
        return 0
    from ghidra.app.util.cparser.C import CParserUtils
    from ghidra.program.model.data import CategoryPath
    from ghidra.program.model.symbol import SourceType
    from ghidra.util.task import TaskMonitor

    header, pjson = HW_FILES[comp.chip]
    dtm = prog.getDataTypeManager()
    tx = dtm.startTransaction("hw headers")
    try:
        res = CParserUtils.parseHeaderFiles(None, [str(HW_DIR / header)], [], dtm, TaskMonitor.DUMMY)
        if not res.successful():
            raise RuntimeError(res.getFormattedParseMessage(None))
    finally:
        dtm.endTransaction(tx, True)

    listing = prog.getListing()
    symtab = prog.getSymbolTable()
    periphs = json.loads((HW_DIR / pjson).read_text())
    n = 0
    for p in sorted(periphs, key=lambda e: e["size"]):       # small structs win over big overlays
        a = ghidra_boot.addr(prog, p["base"])
        if prog.getMemory().getBlock(a) is None:
            continue
        try:
            symtab.createLabel(a, p["name"], SourceType.IMPORTED)
        except Exception:                                    # duplicate label etc.
            pass
        if not p.get("type"):
            continue
        dt = dtm.getDataType(CategoryPath("/"), p["type"]) or next(iter(dtm.getAllDataTypes()), None) and None
        if dt is None:
            dt = _find_type(dtm, p["type"])
        if dt is None or dt.getLength() <= 0:
            continue
        end = a.add(dt.getLength() - 1)
        if not listing.isUndefined(a, end):
            continue
        listing.createData(a, dt)
        listing.setComment(a, 0, p["description"])           # EOL comment
        n += 1
    return n


def _find_type(dtm, name):
    it = dtm.getAllDataTypes()
    for dt in it:
        if dt.getName() == name:
            return dt
    return None


_PRINTABLE = re.compile(rb"[\x20-\x7e\t\r\n]{4,}\x00")


def define_strings(prog, min_len: int = 4) -> int:
    """Create terminated-string data for ASCII runs sitting in undefined bytes."""
    from ghidra.program.model.data import TerminatedStringDataType

    mem = prog.getMemory()
    listing = prog.getListing()
    count = 0
    for blk in mem.getBlocks():
        if not blk.isInitialized() or not blk.isRead():
            continue
        start = blk.getStart()
        raw = bytes((b & 0xFF) for b in _read(blk, mem))
        for m in _PRINTABLE.finditer(raw):
            s, e = m.span()
            if e - s - 1 < min_len:
                continue
            a = start.add(s)
            end = start.add(e - 1)
            if not listing.isUndefined(a, end):
                continue
            try:
                listing.createData(a, TerminatedStringDataType())
                count += 1
            except Exception:
                pass
    return count


def _read(blk, mem):
    import jpype

    buf = jpype.JArray(jpype.JByte)(int(blk.getSize()))
    mem.getBytes(blk.getStart(), buf)
    return bytes(buf)


def apply(prog, comp: Component) -> dict:
    return {"hw_structs": apply_hw(prog, comp), "strings": define_strings(prog)}
