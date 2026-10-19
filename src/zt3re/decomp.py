"""Bulk decompilation of every function of an image (cached as JSON, not committed)."""
from __future__ import annotations

import json
from pathlib import Path

from . import config
from .config import Image


def decomp_path(image: Image) -> Path:
    return config.ANALYSIS_DIR / "decomp" / image.component / f"{image.name}.json"


def decompile_image(prog, timeout: int = 60) -> dict:
    from ghidra.app.decompiler import DecompInterface, DecompileOptions
    from ghidra.util.task import ConsoleTaskMonitor

    di = DecompInterface()
    opts = DecompileOptions()
    opts.grabFromProgram(prog)
    opts.setRespectReadOnly(True)      # fold flash literal-pool loads into constants
    di.setOptions(opts)
    di.openProgram(prog)
    mon = ConsoleTaskMonitor()
    out = {}
    for f in prog.getFunctionManager().getFunctions(True):
        if f.isExternal():
            continue
        res = di.decompileFunction(f, timeout, mon)
        key = f"{f.getEntryPoint().getOffset():#x}"
        if res is not None and res.decompileCompleted():
            out[key] = {"sig": str(res.getDecompiledFunction().getSignature()),
                        "c": str(res.getDecompiledFunction().getC())}
        else:
            out[key] = {"sig": None, "c": None,
                        "error": str(res.getErrorMessage()) if res is not None else "no result"}
    di.dispose()
    return out


def write(image: Image, payload: dict) -> Path:
    p = decomp_path(image)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, separators=(",", ":")))
    return p
