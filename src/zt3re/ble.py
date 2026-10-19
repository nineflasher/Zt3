"""BLE_219-specific image preparation: RAW4TFT container header and the .data init image."""
from __future__ import annotations

from . import ghidra_boot

HEADER_SIZE = 0x400
# From the reset handler: .data is copied from flash (LMA) to SRAM; bss is cleared after it.
DATA_LMA_OFFSET = 0x0C0899D8 - 0x0C028000     # file offset of the .data load image
DATA_VMA = 0x20003D88
DATA_SIZE = 0xC8C


def apply(prog, data: bytes) -> None:
    from java.io import ByteArrayInputStream
    from ghidra.program.model.data import (ArrayDataType, ByteDataType, CategoryPath, DWordDataType,
                                           StructureDataType, StringDataType, UnsignedIntegerDataType)
    from ghidra.program.model.symbol import SourceType
    from ghidra.util.task import TaskMonitor

    mem = prog.getMemory()
    listing = prog.getListing()

    # --- container header ------------------------------------------------------------------
    st = StructureDataType(CategoryPath("/zt3"), "RAW4TFT_Header", 0)
    u32 = UnsignedIntegerDataType()
    st.add(ArrayDataType(ByteDataType(), 8, 1), "magic", 'ASCII "RAW4TFT\\0" container magic')
    st.add(u32, "reserved0", "always 0")
    st.add(u32, "payload_len", "bytes after the header (file size - 0x400)")
    st.add(u32, "checksum", "checksum of unresolved scope (0xF539D849 in v0x219)")
    st.add(u32, "reserved1", "always 0")
    st.add(u32, "header_size", "offset of the payload (0x400)")
    st.add(ArrayDataType(ByteDataType(), 16, 1), "payload_md5", "MD5 of file[header_size:]")
    st.add(u32, "version", "firmware version (0x219)")
    st.add(ArrayDataType(ByteDataType(), HEADER_SIZE - 0x30, 1), "padding", "zero padding to 0x400")
    dt = prog.getDataTypeManager().resolve(st, None)
    base = ghidra_boot.addr(prog, 0x0C028000)
    listing.clearCodeUnits(base, base.add(HEADER_SIZE - 1), False)
    listing.createData(base, dt)
    prog.getSymbolTable().createLabel(base, "raw4tft_header", SourceType.IMPORTED)

    # --- split SRAM so the initialised .data image is real memory ---------------------------
    sram = mem.getBlock("SRAM")
    if sram is not None:
        end = sram.getEnd().getOffset() + 1
        mem.removeBlock(sram, TaskMonitor.DUMMY)
        lo = mem.createUninitializedBlock("SRAM_ROM_AREA", ghidra_boot.addr(prog, 0x20000000),
                                          DATA_VMA - 0x20000000, False)
        payload = data[DATA_LMA_OFFSET:DATA_LMA_OFFSET + DATA_SIZE]
        db = mem.createInitializedBlock(".data", ghidra_boot.addr(prog, DATA_VMA),
                                        ByteArrayInputStream(bytes(payload)), len(payload),
                                        TaskMonitor.DUMMY, False)
        rest_start = DATA_VMA + DATA_SIZE
        hi = mem.createUninitializedBlock(".bss_heap", ghidra_boot.addr(prog, rest_start),
                                          end - rest_start, False)
        for b in (lo, db, hi):
            b.setRead(True)
            b.setWrite(True)
        lo.setComment("SRAM below .data: BT ROM/controller state, not initialised by this image")
        db.setComment("Initialised data copied from flash 0x0C0899D8 by Reset_Handler")
        hi.setComment("bss (0x20004A18..0x20019544, zeroed by Reset_Handler), heap and stacks")
