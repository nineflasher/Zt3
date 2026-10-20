"""Static description of the firmware set: components, memory maps and repo paths."""
from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(os.environ.get("ZT3_ROOT", Path(__file__).resolve().parents[2]))
FIRMWARE_DIR = REPO_ROOT / "firmware"
ANNOTATIONS_DIR = REPO_ROOT / "annotations"
ANALYSIS_DIR = REPO_ROOT / "analysis"
DOCS_DIR = REPO_ROOT / "docs"
GHIDRA_PROJECT_DIR = REPO_ROOT / "ghidra_project"
GHIDRA_PROJECT_NAME = "zt3"
GHIDRA_INSTALL_DIR = Path(os.environ.get("GHIDRA_INSTALL_DIR", "/opt/ghidra_12.1.4_PUBLIC"))


@dataclass(frozen=True)
class Region:
    """One block of the target address space."""

    name: str
    start: int
    size: int
    read: bool = True
    write: bool = False
    execute: bool = False
    volatile: bool = False
    comment: str = ""


@dataclass(frozen=True)
class Component:
    """A firmware family (one microcontroller on the scooter)."""

    key: str                      # directory / annotation key, e.g. "vcu"
    title: str                    # human title
    role: str                     # one-line role description
    language: str                 # Ghidra language id
    chip: str = "stm32f103"       # key into cortexm.IRQ_TABLES / hw peripheral maps
    base: int = 0x08001000        # load address of the .bin
    sram_size: int = 0x8000
    vector_offset: int = 0        # offset of the vector table inside the .bin
    max_vectors: int = 59         # vector-table slots (16 core + IRQs) incl. the initial SP
    regions: tuple[Region, ...] = field(default_factory=tuple)

    @property
    def firmware_dir(self) -> Path:
        return FIRMWARE_DIR / self.key

    @property
    def annotations_dir(self) -> Path:
        return ANNOTATIONS_DIR / self.key


def _cortex_m_regions(chip: str) -> tuple[Region, ...]:
    """Memory regions of the supported Cortex-M parts (application image is loaded at 0x08001000)."""
    boot = Region("BOOTLOADER", 0x08000000, 0x1000, execute=True,
                  comment="4 KiB bootloader area below the application image (not part of the .bin)")
    system = Region("SYSTEM", 0xE0000000, 0x100000, write=True, volatile=True,
                    comment="Cortex-M private peripheral bus (SysTick, NVIC, SCB, DWT)")
    if chip == "at32f415":
        return (boot,
                Region("SRAM", 0x20000000, 0x8000, write=True, comment="32 KiB on-chip SRAM"),
                Region("PERIPH", 0x40000000, 0x30000, write=True, volatile=True,
                       comment="APB1/APB2/AHB peripheral window (CRM, IOMUX, EXINT, ERTC, TMR, USART, CAN ...)"),
                Region("PERIPH_USB", 0x50000000, 0x40000, write=True, volatile=True,
                       comment="USB OTG FS controller"),
                Region("SYSMEM", 0x1FFFF000, 0x1000, write=False, volatile=True,
                       comment="System memory / ROM bootloader, device ID words and user system data"),
                system)
    if chip == "stm32g0b1":
        return (boot,
                Region("SRAM", 0x20000000, 0x24000, write=True, comment="144 KiB on-chip SRAM"),
                Region("PERIPH", 0x40000000, 0x30000, write=True, volatile=True,
                       comment="APB/AHB peripheral window (RCC, EXTI 0x40021800, TIM, USART, FDCAN ...)"),
                Region("PERIPH_IOPORT", 0x50000000, 0x1800, write=True, volatile=True,
                       comment="GPIO ports A-F (IOPORT bus)"),
                Region("SYSMEM", 0x1FFF0000, 0x8000, write=False, volatile=True,
                       comment="System memory, UID (0x1FFF7590), flash size (0x1FFF75E0), option bytes (0x1FFF7800)"),
                system)
    raise KeyError(chip)


COMPONENTS: dict[str, Component] = {
    "mcu": Component(
        key="mcu", title="Motor controller (MCU)", role="Motor / FOC drive controller firmware (AT32F415)",
        language="ARM:LE:32:Cortex", chip="at32f415", max_vectors=92,
        regions=_cortex_m_regions("at32f415")),
    "vcu": Component(
        key="vcu", title="Vehicle control unit (VCU)",
        role="Main vehicle controller / dash and CAN gateway firmware (AT32F415)",
        language="ARM:LE:32:Cortex", chip="at32f415", max_vectors=92,
        regions=_cortex_m_regions("at32f415")),
    "bms": Component(
        key="bms", title="Battery management system (BMS)",
        role="Battery pack monitor / protection firmware (STM32G0B1, Cortex-M0+)",
        language="ARM:LE:32:Cortex", chip="stm32g0b1", max_vectors=47,
        regions=_cortex_m_regions("stm32g0b1")),
}

COMPONENTS["ble"] = Component(
    key="ble", title="Bluetooth LE module (BLE)",
    role="Bestechnic BES Bluetooth SoC firmware: BLE host stack, Find My, UART bridge to the VCU",
    language="ARM:LE:32:v8-m", chip="bes-m33",
    base=0x0C028000, sram_size=0x80000, vector_offset=0x400, max_vectors=92,
    regions=(
        Region("SRAM", 0x20000000, 0x80000, write=True, comment="512 KiB SRAM (ROM/controller data below 0x20003D88)"),
        Region("PERIPH", 0x40000000, 0x100000, write=True, volatile=True, comment="BES peripheral window"),
        Region("SYSTEM", 0xE0000000, 0x100000, write=True, volatile=True,
               comment="Cortex-M33 private peripheral bus"),
    ))

IMAGE_RE = re.compile(r"^(?P<fam>[A-Z]+)_(?P<ver>[0-9a-fA-F]+)\.bin$")


@dataclass(frozen=True)
class Image:
    component: str
    version: str
    path: Path

    @property
    def name(self) -> str:
        return f"{self.component.upper()}_{self.version}"


def discover_images(components: list[str] | None = None) -> list[Image]:
    """List all firmware images under firmware/, ordered by (component, version as hex)."""
    out: list[Image] = []
    for comp_dir in sorted(p for p in FIRMWARE_DIR.iterdir() if p.is_dir()):
        if components and comp_dir.name not in components:
            continue
        for f in sorted(comp_dir.glob("*.bin")):
            m = IMAGE_RE.match(f.name)
            if not m:
                continue
            out.append(Image(comp_dir.name, m["ver"], f))
    out.sort(key=lambda i: (i.component, int(i.version, 16)))
    return out
