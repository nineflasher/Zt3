"""Exception-vector naming for the supported chips (names come from the vendor startup/SVD data)."""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

HW_DIR = Path(__file__).parent / "data" / "hw"

# ARMv8-M core vector names for the BES BLE SoC (no vendor SVD available).
_V8M_CORE = {0: "__initial_sp", 1: "Reset_Handler", 2: "NMI_Handler", 3: "HardFault_Handler",
             4: "MemManage_Handler", 5: "BusFault_Handler", 6: "UsageFault_Handler",
             7: "SecureFault_Handler", 11: "SVC_Handler", 12: "DebugMon_Handler",
             14: "PendSV_Handler", 15: "SysTick_Handler"}


@lru_cache(maxsize=None)
def _tables(chip: str):
    core = json.loads((HW_DIR / f"{chip}_core.json").read_text())
    irqs = json.loads((HW_DIR / f"{chip}_irqs.json").read_text())
    core_names = {v["slot"]: v["name"] for v in core["vectors"] if v.get("name") and v["slot"] < 16}
    irq_names = {i["exception"]: i["handler"] for i in irqs}
    return core_names, irq_names


def vector_name(index: int, chip: str) -> str:
    """Name of vector-table slot `index` (0 = initial SP)."""
    if chip == "bes-m33":
        if index in _V8M_CORE:
            return _V8M_CORE[index]
        return f"Reserved_{index}" if index < 16 else f"IRQ{index - 16}_Handler"
    core_names, irq_names = _tables(chip)
    if index < 16:
        name = core_names.get(index)
        return {"_estack": "__initial_sp"}.get(name, name) if name else f"Reserved_{index}"
    return irq_names.get(index, f"IRQ{index - 16}_Handler")
