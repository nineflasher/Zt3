"""Cross-version correlation with Ghidra's Version Tracking (Auto VT).

For every pair of images (source -> destination) we create a VT session inside the Ghidra
project, run Ghidra's Auto Version Tracking chain (exact bytes / instructions / mnemonics,
symbol, data, duplicate-function and reference-propagation correlators) and export all
matches (function and data associations, with similarity and confidence scores) to JSON.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path

from . import config, ghidra_boot

log = logging.getLogger("zt3re.vt")

VT_FOLDER = "/vt"


def _options():
    from ghidra.feature.vt.api.util import VTOptions
    from ghidra.feature.vt.gui.util import VTOptionDefines as D

    o = VTOptions("zt3")
    o.setBoolean(D.CREATE_IMPLIED_MATCHES_OPTION, True)
    o.setBoolean(D.RUN_EXACT_SYMBOL_OPTION, False)       # symbol names are synthetic (FUN_xxxx)
    o.setBoolean(D.RUN_EXACT_DATA_OPTION, True)
    o.setBoolean(D.RUN_EXACT_FUNCTION_BYTES_OPTION, True)
    o.setBoolean(D.RUN_EXACT_FUNCTION_INST_OPTION, True)
    o.setBoolean(D.RUN_DUPE_FUNCTION_OPTION, True)
    o.setBoolean(D.RUN_REF_CORRELATORS_OPTION, True)
    o.setInt(D.DATA_CORRELATOR_MIN_LEN_OPTION, 5)
    o.setInt(D.SYMBOL_CORRELATOR_MIN_LEN_OPTION, 3)
    o.setInt(D.FUNCTION_CORRELATOR_MIN_LEN_OPTION, 10)
    o.setInt(D.DUPE_FUNCTION_CORRELATOR_MIN_LEN_OPTION, 10)
    o.setDouble(D.REF_CORRELATOR_MIN_SCORE_OPTION, 0.95)
    o.setDouble(D.REF_CORRELATOR_MIN_CONF_OPTION, 10.0)
    o.setBoolean(D.APPLY_IMPLIED_MATCHES_OPTION, True)
    o.setInt(D.MIN_VOTES_OPTION, 2)
    o.setInt(D.MAX_CONFLICTS_OPTION, 0)
    return o


def _extract(session) -> list[dict]:
    rows = []
    for ms in session.getMatchSets():
        corr = str(ms.getProgramCorrelatorInfo().getName())
        for m in ms.getMatches():
            assoc = m.getAssociation()
            rows.append({
                "kind": str(assoc.getType()),          # Function | Data
                "src": m.getSourceAddress().getOffset(),
                "dst": m.getDestinationAddress().getOffset(),
                "src_len": int(m.getSourceLength()),
                "dst_len": int(m.getDestinationLength()),
                "sim": float(m.getSimilarityScore().getScore()),
                "conf": float(m.getConfidenceScore().getScore()),
                "correlator": corr,
                "status": str(assoc.getStatus()),
            })
    return rows


def run_pair(project, comp: str, src: str, dst: str, force: bool = False) -> dict:
    """Run Auto VT for src -> dst (image names, e.g. VCU_152 -> VCU_153); returns summary."""
    from java.lang import Object
    from ghidra.feature.vt.api.db import VTSessionDB
    from ghidra.feature.vt.gui.actions import AutoVersionTrackingTask
    from ghidra.util.task import TaskMonitor

    out_dir = config.ANALYSIS_DIR / "matches" / comp
    out_dir.mkdir(parents=True, exist_ok=True)
    out_json = out_dir / f"{src}__{dst}.json"
    if out_json.exists() and not force:
        return {"pair": f"{src}->{dst}", "skipped": True}

    sname = f"{src}__{dst}"
    folder = ghidra_boot.ensure_folder(project, f"{VT_FOLDER}/{comp}")
    old = folder.getFile(sname)
    if old is not None:
        old.delete()

    consumer = Object()
    with ghidra_boot.open_program(project, src, f"/{comp}") as sprog, \
            ghidra_boot.open_program(project, dst, f"/{comp}") as dprog:
        session = VTSessionDB(sname, sprog, dprog, consumer)
        try:
            folder.createFile(sname, session, TaskMonitor.DUMMY)
            task = AutoVersionTrackingTask(session, _options())
            task.run(TaskMonitor.DUMMY)
            session.save()
            rows = _extract(session)
            msg = str(task.getStatusMsg())
        finally:
            session.release(consumer)
    out_json.write_text(json.dumps({"source": src, "dest": dst, "status": msg, "matches": rows}, indent=1))
    nf = sum(1 for r in rows if r["kind"] == "Function")
    log.info("%s -> %s: %d matches (%d function)", src, dst, len(rows), nf)
    return {"pair": f"{src}->{dst}", "matches": len(rows), "functions": nf, "status": msg}


def pairs_for(images: list) -> list[tuple[str, str]]:
    """Adjacent pairs plus every older version against the newest (images sorted ascending)."""
    names = [i.name for i in images]
    pairs = [(a, b) for a, b in zip(names, names[1:])]
    newest = names[-1]
    pairs += [(n, newest) for n in names[:-2]]
    return pairs
