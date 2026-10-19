"""PyGhidra bootstrap and small helpers shared by every stage."""
from __future__ import annotations

import contextlib
import os
from typing import Iterator

from . import config

_started = False


def start() -> None:
    """Launch the in-process JVM exactly once (idempotent)."""
    global _started
    if _started:
        return
    os.environ.setdefault("GHIDRA_INSTALL_DIR", str(config.GHIDRA_INSTALL_DIR))
    import pyghidra

    pyghidra.start()
    _started = True


@contextlib.contextmanager
def project(create: bool = False):
    """Open (or create) the shared Ghidra project."""
    start()
    import pyghidra

    config.GHIDRA_PROJECT_DIR.mkdir(parents=True, exist_ok=True)
    with pyghidra.open_project(config.GHIDRA_PROJECT_DIR, config.GHIDRA_PROJECT_NAME, create=create) as p:
        yield p


def ensure_folder(project, path: str):
    """Create (recursively) a project folder and return it."""
    folder = project.getProjectData().getRootFolder()
    for part in [p for p in path.split("/") if p]:
        sub = folder.getFolder(part)
        folder = sub if sub is not None else folder.createFolder(part)
    return folder


def get_file(project, folder: str, name: str):
    """Return the DomainFile `name` in project `folder`, or None."""
    node = project.getProjectData().getRootFolder()
    for part in [p for p in folder.split("/") if p]:
        node = node.getFolder(part)
        if node is None:
            return None
    return node.getFile(name)


@contextlib.contextmanager
def open_program(project, name: str, folder: str = "/") -> Iterator:
    """Open a program of the project (use `save(prog)` to persist changes)."""
    start()
    import pyghidra

    if get_file(project, folder, name) is None:
        raise FileNotFoundError(f"program not in project: {folder}/{name}")
    with pyghidra.program_context(project, f"{folder.rstrip('/')}/{name}") as prog:
        yield prog


def save(prog, message: str = "zt3re") -> None:
    from ghidra.util.task import TaskMonitor

    prog.save(message, TaskMonitor.DUMMY)


def addr(program, value: int):
    return program.getAddressFactory().getDefaultAddressSpace().getAddress(value)
