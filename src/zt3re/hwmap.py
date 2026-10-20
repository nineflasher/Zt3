"""Resolve peripheral register addresses to names (PERIPH.REG) using the vendor SVD-derived JSON."""
from __future__ import annotations

import bisect
import json
from functools import lru_cache
from pathlib import Path

HW_DIR = Path(__file__).parent / "data" / "hw"


class HwMap:
    def __init__(self, chip: str):
        self.chip = chip
        pj = HW_DIR / f"peripherals_{chip}.json"
        rj = HW_DIR / f"{chip}_registers.json"
        self.periph = sorted(json.loads(pj.read_text()), key=lambda p: p["base"]) if pj.exists() else []
        self.regs = json.loads(rj.read_text()) if rj.exists() else {}
        self._bases = [p["base"] for p in self.periph]
        self._reg_index: dict[str, list[tuple[int, str, str]]] = {}
        for pname, pd in self.regs.items():
            lst = [(r["offset"], r["name"], r.get("description", "")) for r in pd.get("registers", [])]
            self._reg_index[pname] = sorted(lst)

    def find(self, addr: int):
        """Return (peripheral dict, offset) or None.  Smaller peripherals win over big overlays."""
        i = bisect.bisect_right(self._bases, addr) - 1
        best = None
        while i >= 0 and i >= max(0, bisect.bisect_right(self._bases, addr) - 8):
            p = self.periph[i]
            if p["base"] <= addr < p["base"] + max(p["size"], 4):
                if best is None or p["size"] < best["size"]:
                    best = p
            i -= 1
        return (best, addr - best["base"]) if best else None

    def name(self, addr: int) -> str:
        hit = self.find(addr)
        if hit is None:
            return f"{addr:#010x}"
        p, off = hit
        regs = self._reg_index.get(p["name"])
        if regs:
            offs = [r[0] for r in regs]
            k = bisect.bisect_right(offs, off) - 1
            if k >= 0 and off - regs[k][0] < 4:
                return f"{p['name']}.{regs[k][1]}"
        return f"{p['name']}+{off:#x}"

    def describe(self, addr: int) -> str:
        hit = self.find(addr)
        if hit is None:
            return self.name(addr)
        p, off = hit
        regs = self._reg_index.get(p["name"], [])
        offs = [r[0] for r in regs]
        k = bisect.bisect_right(offs, off) - 1
        if k >= 0 and off - regs[k][0] < 4 and regs[k][2]:
            return f"{p['name']}.{regs[k][1]} - {regs[k][2][:80]}"
        return f"{p['name']}+{off:#x} ({p.get('description', '')[:60]})"


@lru_cache(maxsize=None)
def get(chip: str) -> HwMap:
    return HwMap(chip)
