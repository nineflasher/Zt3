"""`zt3 doctor`: freshness, ownership and orphan checks that need no Ghidra.

Finding codes (gating unless noted):
  UNOWNED       tracked path matches no MANIFEST.toml rule
  MISSING       expected derived file absent (export/match/families for a firmware image or component)
  ORPHAN        derived file whose input no longer exists (export of a removed image, match of a removed
                pair, annotation key that is not a family)
  STALE         provenance stamp disagrees with the current inputs (export sha256 vs .bin, families vs exports)
  DANGLING-REF  prose cites a family id that does not exist
  LITERAL       doc names a `zt3` subcommand / `make` target / repo path that does not exist, or an absolute path
  LINK          relative markdown link does not resolve
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import tomllib
from dataclasses import dataclass
from pathlib import Path

from . import annotations as ann
from . import config

GATING = {"UNOWNED", "MISSING", "ORPHAN", "STALE", "DANGLING-REF", "LITERAL", "LINK"}


@dataclass
class Finding:
    code: str
    path: str
    reason: str

    def __str__(self) -> str:
        return f"{self.code:12} {self.path}: {self.reason}"


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _brace_expand(g: str) -> list[str]:
    m = re.search(r"\{([^}]*)\}", g)
    if not m:
        return [g]
    return [x for alt in m.group(1).split(",") for x in _brace_expand(g[:m.start()] + alt + g[m.end():])]


def load_manifest() -> list[dict]:
    return tomllib.loads((config.REPO_ROOT / "MANIFEST.toml").read_text())["rule"]


def tracked_files() -> list[str]:
    out = subprocess.run(["git", "ls-files"], cwd=config.REPO_ROOT, capture_output=True, text=True, check=True)
    return out.stdout.split()


def _glob_re(g: str) -> re.Pattern:
    """Path-aware glob: `*` never crosses a `/`, `**/` matches zero or more directories."""
    out = ""
    i = 0
    while i < len(g):
        if g.startswith("**/", i):
            out += "(?:.*/)?"
            i += 3
        elif g[i] == "*":
            out += "[^/]*"
            i += 1
        else:
            out += re.escape(g[i])
            i += 1
    return re.compile("^" + out + "$")


def rule_for(path: str, rules: list[dict]) -> dict | None:
    for r in rules:
        if any(_glob_re(g).match(path) for g in _brace_expand(r["glob"])):
            return r
    return None


# ---------------------------------------------------------------------------------------------
def check_manifest(findings: list[Finding]) -> None:
    rules = load_manifest()
    for f in tracked_files():
        if rule_for(f, rules) is None:
            findings.append(Finding("UNOWNED", f, "no MANIFEST.toml rule; add one or remove the file"))


def check_pipeline(findings: list[Finding]) -> None:
    from .vt import pairs_for

    images = config.discover_images()
    by_comp: dict[str, list] = {}
    for img in images:
        by_comp.setdefault(img.component, []).append(img)
    exp_root = config.ANALYSIS_DIR / "export"
    mat_root = config.ANALYSIS_DIR / "matches"
    fam_root = config.ANALYSIS_DIR / "families"
    for comp, imgs in by_comp.items():
        names = {i.name for i in imgs}
        for img in imgs:
            ep = exp_root / comp / f"{img.name}.json"
            if not ep.exists():
                findings.append(Finding("MISSING", str(ep.relative_to(config.REPO_ROOT)), "run `zt3 export`"))
                continue
            j = json.loads(ep.read_text())
            if j.get("sha256") != sha256(img.path):
                findings.append(Finding("STALE", str(ep.relative_to(config.REPO_ROOT)),
                                        "export was made from a different .bin; re-run `zt3 import --force` and `zt3 export`"))
        for ep in (exp_root / comp).glob("*.json") if (exp_root / comp).exists() else []:
            if ep.stem not in names:
                findings.append(Finding("ORPHAN", str(ep.relative_to(config.REPO_ROOT)), "no such firmware image"))
        if len(imgs) > 1:
            want = {f"{a}__{b}.json" for a, b in pairs_for(sorted(imgs, key=lambda i: int(i.version, 16)))}
            have = {p.name for p in (mat_root / comp).glob("*.json")} if (mat_root / comp).exists() else set()
            for m in sorted(want - have):
                findings.append(Finding("MISSING", f"analysis/matches/{comp}/{m}", "run `zt3 match`"))
            for m in sorted(have - want):
                findings.append(Finding("ORPHAN", f"analysis/matches/{comp}/{m}", "pair no longer in the version set"))
        fp = fam_root / f"{comp}.json"
        if not fp.exists():
            findings.append(Finding("MISSING", f"analysis/families/{comp}.json", "run `zt3 families`"))
            continue
        fam = json.loads(fp.read_text())
        prov = fam.get("_prov", {})
        cur = families_inputs(comp)
        if prov.get("inputs") != cur:
            changed = sorted(k for k in set(cur) | set(prov.get("inputs", {})) if cur.get(k) != prov.get("inputs", {}).get(k))
            findings.append(Finding("STALE", f"analysis/families/{comp}.json",
                                    f"inputs changed since build: {', '.join(changed[:4])}{' ...' if len(changed) > 4 else ''}; run `zt3 families`"))
        # annotation keys must be families
        for kind, loader in (("functions", ann.load_functions), ("globals", ann.load_globals), ("tables", ann.load_tables)):
            for k in loader(comp):
                if k not in fam[kind]:
                    findings.append(Finding("ORPHAN", f"annotations/{comp}/{kind}", f"key {k} is not a {kind[:-1]} family"))
        # prose references (ids of any component are legitimate, e.g. "the VCU twin of this routine")
        valid = all_family_ids()
        for k, n in ann.load_functions(comp).items():
            for field in ("summary", "description", "notes"):
                for ref in ann.FID_RE.findall(n.get(field) or ""):
                    if ref not in valid:
                        findings.append(Finding("DANGLING-REF", f"annotations/{comp}/functions:{k}", f"{field} cites unknown id {ref}"))


_ALL_IDS: set[str] | None = None


def all_family_ids() -> set[str]:
    global _ALL_IDS
    if _ALL_IDS is None:
        _ALL_IDS = set()
        for p in (config.ANALYSIS_DIR / "families").glob("*.json"):
            j = json.loads(p.read_text())
            for k in ("functions", "globals", "tables"):
                _ALL_IDS |= set(j[k])
    return _ALL_IDS


def families_inputs(comp: str) -> dict[str, str]:
    """Content digests of everything `zt3 families` reads for a component (the provenance stamp)."""
    out = {}
    for p in sorted((config.ANALYSIS_DIR / "export" / comp).glob("*.json")):
        out[str(p.relative_to(config.REPO_ROOT))] = sha256(p)
    mat = config.ANALYSIS_DIR / "matches" / comp
    if mat.exists():
        for p in sorted(mat.glob("*.json")):
            out[str(p.relative_to(config.REPO_ROOT))] = sha256(p)
    out["src/zt3re/families.py"] = sha256(Path(__file__).with_name("families.py"))
    return out


_LINK = re.compile(r"\[[^\]]*\]\(([^)\s#]+)(#[^)]*)?\)")
_ABS = re.compile(r"(?<![\w/])/(?:home|opt|tmp)/[\w./-]+")
_ZT3 = re.compile(r"`zt3 ([a-z-]+)")
_MAKE = re.compile(r"`make ([a-z-]+)`")
_REPO_PATH = re.compile(r"`((?:src|docs|analysis|annotations|firmware|tests|tools)/[\w./*{},-]+)`")


def check_docs(findings: list[Finding]) -> None:
    from .cli import build_parser

    subs = set(build_parser()._subparsers._group_actions[0].choices)  # noqa: SLF001
    targets = set(re.findall(r"^([a-z-]+):", (config.REPO_ROOT / "Makefile").read_text(), re.M))
    rules = load_manifest()
    for md in sorted(config.REPO_ROOT.rglob("*.md")):
        rel = md.relative_to(config.REPO_ROOT)
        if rel.parts[0] in ("ghidra_project", "analysis", ".git") or not rule_for(str(rel), rules):
            continue
        rule = rule_for(str(rel), rules)
        text = md.read_text()
        if not rule.get("allow_absolute_paths") and (m := _ABS.search(text)):
            findings.append(Finding("LITERAL", str(rel), f"absolute path {m.group(0)}"))
        for s in set(_ZT3.findall(text)) - subs:
            findings.append(Finding("LITERAL", str(rel), f"unknown subcommand `zt3 {s}`"))
        for t in set(_MAKE.findall(text)) - targets:
            findings.append(Finding("LITERAL", str(rel), f"unknown make target `{t}`"))
        for p in set(_REPO_PATH.findall(text)):
            if any(c in p for c in "*{<") or p.endswith("/"):
                continue
            if not (config.REPO_ROOT / p).exists() and not (config.REPO_ROOT / p.rstrip(":")).exists():
                findings.append(Finding("LITERAL", str(rel), f"path `{p}` does not exist"))
        for target, _anchor in _LINK.findall(text):
            if "://" in target or target.startswith("mailto:"):
                continue
            if not (target.endswith(".md") or "/" in target):
                continue                                   # prose in brackets, not a link
            if not (md.parent / target).exists():
                findings.append(Finding("LINK", str(rel), f"broken link {target}"))


def run(ci: bool = False) -> list[Finding]:
    findings: list[Finding] = []
    check_manifest(findings)
    check_pipeline(findings)
    check_docs(findings)
    return findings
