"""Coverage statistics for an analysed program (how much of FLASH is code/data/undefined)."""
from __future__ import annotations


def flash_coverage(prog, top_gaps: int = 8) -> dict:
    from ghidra.program.model.listing import Instruction

    mem = prog.getMemory()
    flash = mem.getBlock("FLASH")
    listing = prog.getListing()
    code = data = undef = 0
    gaps: list[tuple[int, int]] = []
    cur_start = None
    cur_len = 0
    for cu in listing.getCodeUnits(flash.getStart(), True):
        a = cu.getAddress()
        if a.compareTo(flash.getEnd()) > 0:
            break
        n = cu.getLength()
        if isinstance(cu, Instruction):
            code += n
            kind = "c"
        elif cu.getDataType().getName().lower().startswith("undefined"):
            undef += n
            kind = "u"
        else:
            data += n
            kind = "d"
        if kind == "u":
            if cur_start is None:
                cur_start = a.getOffset()
            cur_len += n
        elif cur_start is not None:
            gaps.append((cur_len, cur_start))
            cur_start, cur_len = None, 0
    if cur_start is not None:
        gaps.append((cur_len, cur_start))
    gaps.sort(reverse=True)
    total = code + data + undef
    return {
        "total": total, "code": code, "data": data, "undefined": undef,
        "code_pct": round(100.0 * code / total, 1), "undefined_pct": round(100.0 * undef / total, 1),
        "functions": prog.getFunctionManager().getFunctionCount(),
        "largest_gaps": [(hex(s), n) for n, s in gaps[:top_gaps]],
    }
