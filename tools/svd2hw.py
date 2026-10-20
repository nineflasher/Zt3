#!/usr/bin/env python3
"""svd2hw.py - turn a vendor CMSIS-SVD file into Ghidra-friendly hardware descriptions.

Pure standard library (xml.etree), python >= 3.8.

Outputs (all written to --out-dir, default: src/zt3re/data/hw next to this tool):

  <chip>.h                    C header for Ghidra's CParser: fundamental typedefs, one
                              ``typedef struct {...} <X>_Type;`` per distinct peripheral
                              layout, plus the Cortex-M core structs (SysTick, NVIC, SCB ...).
  peripherals_<chip>.json     [{name, base, size, type, description, ...}] for every
                              peripheral instance (SVD + core + a few non-SVD regions).
  <chip>_registers.json       {peripheral: {base, description, type, registers:[{name, offset,
                              size, access, reset, description, fields:[...]}]}} - the full
                              register documentation incl. registers that could not be put in
                              the struct (aliases, flagged "in_struct": false).
  <chip>_irqs.json            [{number, name, description, ...}] (exception number = number+16)
  <chip>_core.json            core / vector-table description (slot names, reserved IRQ slots)

Header conventions (see README.md in the output directory):
  * no #include / volatile / macros / bitfields / unions; only uint8_t/uint16_t/uint32_t.
  * member name = SVD register name (a ``PERIPH_`` prefix shared by *all* registers of a
    peripheral, as ST's SVDs have, is stripped; the registers JSON keeps the SVD name).
  * holes become explicit ``RESERVEDn`` padding; every member has a ``/* 0xNNN */`` offset.
  * registers whose byte ranges overlap an already placed register (SVD "alternate"
    registers, e.g. CCMR1_Input vs CCMR1_Output) are NOT placed in the struct; the registers
    JSON lists them with ``"in_struct": false, "alias_of": "<kept name>"``.
  * ``dim`` arrays: ``NAME[%s]`` with indices 0..n-1 and stride == register size becomes a C
    array; every other ``dim`` is expanded into NAME0, NAME1, ... members.  Clusters are
    flattened (``CLUSTER_REG``).
  * struct size = end of last register rounded up to the struct alignment, exactly what a C
    compiler / Ghidra computes, so JSON ``size`` == sizeof(type).

Usage (from the repo root; inputs default to the copies in src/zt3re/data/hw/svd/):
  python3 tools/svd2hw.py --chip at32f415      # VCU + MCU: Artery AT32F415, Cortex-M4F
  python3 tools/svd2hw.py --chip stm32g0b1     # BMS: STM32G0B1, Cortex-M0+
  python3 tools/svd2hw.py --selftest           # synthetic SVD (derivedFrom, dim, cluster, 8/16 bit, aliases)
Known chips (--chip) carry a profile (SVD, core kind, IRQ header, startup file, extra regions);
for another part pass --svd X --core {m4f,m0plus} [--irq-header H] [--startup S].
"""
import argparse
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUT = os.path.normpath(os.path.join(HERE, "..", "src", "zt3re", "data", "hw"))
SVD_DIR = os.path.join(DEFAULT_OUT, "svd")  # vendor inputs shipped with the repo (see svd/SOURCES.md)

# --------------------------------------------------------------------------------------
# chip profiles
# --------------------------------------------------------------------------------------
PROFILES = {
    "at32f415": dict(
        core="m4f",
        label="Artery AT32F415 (Cortex-M4F, up to 150 MHz)",
        svd=os.path.join(SVD_DIR, "AT32F415xx_v2.svd"),
        irq_header=os.path.join(SVD_DIR, "at32f415_irqn.h"),
        startup=os.path.join(SVD_DIR, "startup_at32f415.s"),
        extras=[],
    ),
    "stm32g0b1": dict(
        core="m0plus",
        label="STMicroelectronics STM32G0B1 (Cortex-M0+)",
        svd=os.path.join(SVD_DIR, "STM32G0B1.svd"),
        irq_header=os.path.join(SVD_DIR, "stm32g0b1_irqn.h"),
        startup=os.path.join(SVD_DIR, "startup_stm32g0b1xx.s"),
        extras=[
            dict(name="PACKAGE_DATA", base=0x1FFF7500, size=2, description="Package data register (16 bit, system memory)"),
            dict(name="UID", base=0x1FFF7590, size=12, description="96-bit unique device ID (system memory)"),
            dict(name="FLASHSIZE", base=0x1FFF75E0, size=2, description="Flash size register, 16 bit, in KBytes (system memory)"),
            dict(name="SRAMCAN_FDCAN1", base=0x4000B400, size=0x350,
                 description="FDCAN1 message RAM (212 words) - not in SVD, from RM0444 / stm32g0b1xx.h SRAMCAN_BASE"),
            dict(name="SRAMCAN_FDCAN2", base=0x4000B750, size=0x350,
                 description="FDCAN2 message RAM (212 words) - not in SVD, = SRAMCAN_BASE + 0x350"),
        ],
    ),
}

CORE_NAMES_M4 = ["_estack", "Reset_Handler", "NMI_Handler", "HardFault_Handler", "MemManage_Handler",
                 "BusFault_Handler", "UsageFault_Handler", None, None, None, None, "SVC_Handler",
                 "DebugMon_Handler", None, "PendSV_Handler", "SysTick_Handler"]
CORE_NAMES_M0P = ["_estack", "Reset_Handler", "NMI_Handler", "HardFault_Handler"] + [None] * 7 + [
    "SVC_Handler", None, None, "PendSV_Handler", "SysTick_Handler"]

# --------------------------------------------------------------------------------------
# Cortex core structs (CMSIS core_cm4.h / core_cm0plus.h, flattened for the Ghidra CParser)
# --------------------------------------------------------------------------------------
CORE_M4_TEXT = r'''typedef struct {
    /* 0x000 */ uint32_t RESERVED0[1];
    /* 0x004 */ uint32_t ICTR;                    /* Interrupt Controller Type Register */
    /* 0x008 */ uint32_t ACTLR;                   /* Auxiliary Control Register */
} SCnSCB_Type;  /* sizeof = 0xC */

typedef struct {
    /* 0x000 */ uint32_t CTRL;                    /* SysTick Control and Status Register */
    /* 0x004 */ uint32_t LOAD;                    /* SysTick Reload Value Register */
    /* 0x008 */ uint32_t VAL;                     /* SysTick Current Value Register */
    /* 0x00C */ uint32_t CALIB;                   /* SysTick Calibration Register */
} SysTick_Type;  /* sizeof = 0x10 */

typedef struct {
    /* 0x000 */ uint32_t ISER[8];                 /* Interrupt Set Enable Register */
    /* 0x020 */ uint32_t RESERVED0[24];
    /* 0x080 */ uint32_t ICER[8];                 /* Interrupt Clear Enable Register */
    /* 0x0A0 */ uint32_t RESERVED1[24];
    /* 0x100 */ uint32_t ISPR[8];                 /* Interrupt Set Pending Register */
    /* 0x120 */ uint32_t RESERVED2[24];
    /* 0x180 */ uint32_t ICPR[8];                 /* Interrupt Clear Pending Register */
    /* 0x1A0 */ uint32_t RESERVED3[24];
    /* 0x200 */ uint32_t IABR[8];                 /* Interrupt Active bit Register */
    /* 0x220 */ uint32_t RESERVED4[56];
    /* 0x300 */ uint8_t IP[240];                  /* Interrupt Priority Register (8Bit wide) */
    /* 0x3F0 */ uint32_t RESERVED5[644];
    /* 0xE00 */ uint32_t STIR;                    /* Software Trigger Interrupt Register */
} NVIC_Type;  /* sizeof = 0xE04 */

typedef struct {
    /* 0x000 */ uint32_t CPUID;                   /* CPUID Base Register */
    /* 0x004 */ uint32_t ICSR;                    /* Interrupt Control and State Register */
    /* 0x008 */ uint32_t VTOR;                    /* Vector Table Offset Register */
    /* 0x00C */ uint32_t AIRCR;                   /* Application Interrupt and Reset Control Register */
    /* 0x010 */ uint32_t SCR;                     /* System Control Register */
    /* 0x014 */ uint32_t CCR;                     /* Configuration Control Register */
    /* 0x018 */ uint8_t SHP[12];                  /* System Handlers Priority Registers (4-7, 8-11, 12-15) */
    /* 0x024 */ uint32_t SHCSR;                   /* System Handler Control and State Register */
    /* 0x028 */ uint32_t CFSR;                    /* Configurable Fault Status Register */
    /* 0x02C */ uint32_t HFSR;                    /* HardFault Status Register */
    /* 0x030 */ uint32_t DFSR;                    /* Debug Fault Status Register */
    /* 0x034 */ uint32_t MMFAR;                   /* MemManage Fault Address Register */
    /* 0x038 */ uint32_t BFAR;                    /* BusFault Address Register */
    /* 0x03C */ uint32_t AFSR;                    /* Auxiliary Fault Status Register */
    /* 0x040 */ uint32_t PFR[2];                  /* Processor Feature Register */
    /* 0x048 */ uint32_t DFR;                     /* Debug Feature Register */
    /* 0x04C */ uint32_t ADR;                     /* Auxiliary Feature Register */
    /* 0x050 */ uint32_t MMFR[4];                 /* Memory Model Feature Register */
    /* 0x060 */ uint32_t ISAR[5];                 /* Instruction Set Attributes Register */
    /* 0x074 */ uint32_t RESERVED0[5];
    /* 0x088 */ uint32_t CPACR;                   /* Coprocessor Access Control Register */
} SCB_Type;  /* sizeof = 0x8C */

typedef struct {
    /* 0x000 */ uint32_t PORT[32];                /* ITM Stimulus Port Registers */
    /* 0x080 */ uint32_t RESERVED0[864];
    /* 0xE00 */ uint32_t TER;                     /* ITM Trace Enable Register */
    /* 0xE04 */ uint32_t RESERVED1[15];
    /* 0xE40 */ uint32_t TPR;                     /* ITM Trace Privilege Register */
    /* 0xE44 */ uint32_t RESERVED2[15];
    /* 0xE80 */ uint32_t TCR;                     /* ITM Trace Control Register */
    /* 0xE84 */ uint32_t RESERVED3[32];
    /* 0xF04 */ uint32_t RESERVED4[43];
    /* 0xFB0 */ uint32_t LAR;                     /* ITM Lock Access Register */
    /* 0xFB4 */ uint32_t LSR;                     /* ITM Lock Status Register */
    /* 0xFB8 */ uint32_t RESERVED5[6];
    /* 0xFD0 */ uint32_t PID4;                    /* ITM Peripheral Identification Register #4 */
    /* 0xFD4 */ uint32_t PID5;                    /* ITM Peripheral Identification Register #5 */
    /* 0xFD8 */ uint32_t PID6;                    /* ITM Peripheral Identification Register #6 */
    /* 0xFDC */ uint32_t PID7;                    /* ITM Peripheral Identification Register #7 */
    /* 0xFE0 */ uint32_t PID0;                    /* ITM Peripheral Identification Register #0 */
    /* 0xFE4 */ uint32_t PID1;                    /* ITM Peripheral Identification Register #1 */
    /* 0xFE8 */ uint32_t PID2;                    /* ITM Peripheral Identification Register #2 */
    /* 0xFEC */ uint32_t PID3;                    /* ITM Peripheral Identification Register #3 */
    /* 0xFF0 */ uint32_t CID0;                    /* ITM Component Identification Register #0 */
    /* 0xFF4 */ uint32_t CID1;                    /* ITM Component Identification Register #1 */
    /* 0xFF8 */ uint32_t CID2;                    /* ITM Component Identification Register #2 */
    /* 0xFFC */ uint32_t CID3;                    /* ITM Component Identification Register #3 */
} ITM_Type;  /* sizeof = 0x1000 */

typedef struct {
    /* 0x000 */ uint32_t CTRL;                    /* Control Register */
    /* 0x004 */ uint32_t CYCCNT;                  /* Cycle Count Register */
    /* 0x008 */ uint32_t CPICNT;                  /* CPI Count Register */
    /* 0x00C */ uint32_t EXCCNT;                  /* Exception Overhead Count Register */
    /* 0x010 */ uint32_t SLEEPCNT;                /* Sleep Count Register */
    /* 0x014 */ uint32_t LSUCNT;                  /* LSU Count Register */
    /* 0x018 */ uint32_t FOLDCNT;                 /* Folded-instruction Count Register */
    /* 0x01C */ uint32_t PCSR;                    /* Program Counter Sample Register */
    /* 0x020 */ uint32_t COMP0;                   /* Comparator Register 0 */
    /* 0x024 */ uint32_t MASK0;                   /* Mask Register 0 */
    /* 0x028 */ uint32_t FUNCTION0;               /* Function Register 0 */
    /* 0x02C */ uint32_t RESERVED0[1];
    /* 0x030 */ uint32_t COMP1;                   /* Comparator Register 1 */
    /* 0x034 */ uint32_t MASK1;                   /* Mask Register 1 */
    /* 0x038 */ uint32_t FUNCTION1;               /* Function Register 1 */
    /* 0x03C */ uint32_t RESERVED1[1];
    /* 0x040 */ uint32_t COMP2;                   /* Comparator Register 2 */
    /* 0x044 */ uint32_t MASK2;                   /* Mask Register 2 */
    /* 0x048 */ uint32_t FUNCTION2;               /* Function Register 2 */
    /* 0x04C */ uint32_t RESERVED2[1];
    /* 0x050 */ uint32_t COMP3;                   /* Comparator Register 3 */
    /* 0x054 */ uint32_t MASK3;                   /* Mask Register 3 */
    /* 0x058 */ uint32_t FUNCTION3;               /* Function Register 3 */
} DWT_Type;  /* sizeof = 0x5C */

typedef struct {
    /* 0x000 */ uint32_t SSPSR;                   /* Supported Parallel Port Size Register */
    /* 0x004 */ uint32_t CSPSR;                   /* Current Parallel Port Size Register */
    /* 0x008 */ uint32_t RESERVED0[2];
    /* 0x010 */ uint32_t ACPR;                    /* Asynchronous Clock Prescaler Register */
    /* 0x014 */ uint32_t RESERVED1[55];
    /* 0x0F0 */ uint32_t SPPR;                    /* Selected Pin Protocol Register */
    /* 0x0F4 */ uint32_t RESERVED2[131];
    /* 0x300 */ uint32_t FFSR;                    /* Formatter and Flush Status Register */
    /* 0x304 */ uint32_t FFCR;                    /* Formatter and Flush Control Register */
    /* 0x308 */ uint32_t FSCR;                    /* Formatter Synchronization Counter Register */
    /* 0x30C */ uint32_t RESERVED3[759];
    /* 0xEE8 */ uint32_t TRIGGER;                 /* TRIGGER Register */
    /* 0xEEC */ uint32_t FIFO0;                   /* Integration ETM Data */
    /* 0xEF0 */ uint32_t ITATBCTR2;               /* ITATBCTR2 */
    /* 0xEF4 */ uint32_t RESERVED4[1];
    /* 0xEF8 */ uint32_t ITATBCTR0;               /* ITATBCTR0 */
    /* 0xEFC */ uint32_t FIFO1;                   /* Integration ITM Data */
    /* 0xF00 */ uint32_t ITCTRL;                  /* Integration Mode Control */
    /* 0xF04 */ uint32_t RESERVED5[39];
    /* 0xFA0 */ uint32_t CLAIMSET;                /* Claim tag set */
    /* 0xFA4 */ uint32_t CLAIMCLR;                /* Claim tag clear */
    /* 0xFA8 */ uint32_t RESERVED7[8];
    /* 0xFC8 */ uint32_t DEVID;                   /* TPIU_DEVID */
    /* 0xFCC */ uint32_t DEVTYPE;                 /* TPIU_DEVTYPE */
} TPI_Type;  /* sizeof = 0xFD0 */

typedef struct {
    /* 0x000 */ uint32_t DHCSR;                   /* Debug Halting Control and Status Register */
    /* 0x004 */ uint32_t DCRSR;                   /* Debug Core Register Selector Register */
    /* 0x008 */ uint32_t DCRDR;                   /* Debug Core Register Data Register */
    /* 0x00C */ uint32_t DEMCR;                   /* Debug Exception and Monitor Control Register */
} CoreDebug_Type;  /* sizeof = 0x10 */


typedef struct {
    /* 0x000 */ uint32_t TYPE;                    /* MPU Type Register */
    /* 0x004 */ uint32_t CTRL;                    /* MPU Control Register */
    /* 0x008 */ uint32_t RNR;                     /* MPU Region Number Register */
    /* 0x00C */ uint32_t RBAR;                    /* MPU Region Base Address Register */
    /* 0x010 */ uint32_t RASR;                    /* MPU Region Attribute and Size Register */
    /* 0x014 */ uint32_t RBAR_A1;                 /* MPU Alias 1 Region Base Address Register */
    /* 0x018 */ uint32_t RASR_A1;                 /* MPU Alias 1 Region Attribute and Size Register */
    /* 0x01C */ uint32_t RBAR_A2;                 /* MPU Alias 2 Region Base Address Register */
    /* 0x020 */ uint32_t RASR_A2;                 /* MPU Alias 2 Region Attribute and Size Register */
    /* 0x024 */ uint32_t RBAR_A3;                 /* MPU Alias 3 Region Base Address Register */
    /* 0x028 */ uint32_t RASR_A3;                 /* MPU Alias 3 Region Attribute and Size Register */
} MPU_Type;  /* sizeof = 0x2C */

typedef struct {
    /* 0x000 */ uint32_t RESERVED0[1];
    /* 0x004 */ uint32_t FPCCR;                   /* Floating-Point Context Control Register */
    /* 0x008 */ uint32_t FPCAR;                   /* Floating-Point Context Address Register */
    /* 0x00C */ uint32_t FPDSCR;                  /* Floating-Point Default Status Control Register */
    /* 0x010 */ uint32_t MVFR0;                   /* Media and FP Feature Register 0 */
    /* 0x014 */ uint32_t MVFR1;                   /* Media and FP Feature Register 1 */
} FPU_Type;  /* sizeof = 0x18 */'''
CORE_M0P_TEXT = r'''typedef struct {
    /* 0x000 */ uint32_t CTRL;                    /* SysTick Control and Status Register */
    /* 0x004 */ uint32_t LOAD;                    /* SysTick Reload Value Register */
    /* 0x008 */ uint32_t VAL;                     /* SysTick Current Value Register */
    /* 0x00C */ uint32_t CALIB;                   /* SysTick Calibration Register */
} SysTick_Type;  /* sizeof = 0x10 */

typedef struct {
    /* 0x000 */ uint32_t ISER[1];                 /* Interrupt Set Enable Register */
    /* 0x004 */ uint32_t RESERVED0[31];
    /* 0x080 */ uint32_t ICER[1];                 /* Interrupt Clear Enable Register */
    /* 0x084 */ uint32_t RESERVED1[31];
    /* 0x100 */ uint32_t ISPR[1];                 /* Interrupt Set Pending Register */
    /* 0x104 */ uint32_t RESERVED2[31];
    /* 0x180 */ uint32_t ICPR[1];                 /* Interrupt Clear Pending Register */
    /* 0x184 */ uint32_t RESERVED3[31];
    /* 0x200 */ uint32_t RESERVED4[64];
    /* 0x300 */ uint32_t IP[8];                   /* Interrupt Priority Register */
} NVIC_Type;  /* sizeof = 0x320 */

typedef struct {
    /* 0x000 */ uint32_t CPUID;                   /* CPUID Base Register */
    /* 0x004 */ uint32_t ICSR;                    /* Interrupt Control and State Register */
    /* 0x008 */ uint32_t VTOR;                    /* Vector Table Offset Register */
    /* 0x00C */ uint32_t AIRCR;                   /* Application Interrupt and Reset Control Register */
    /* 0x010 */ uint32_t SCR;                     /* System Control Register */
    /* 0x014 */ uint32_t CCR;                     /* Configuration Control Register */
    /* 0x018 */ uint32_t RESERVED1;
    /* 0x01C */ uint32_t SHP[2];                  /* System Handlers Priority Registers. [0] is RESERVED */
    /* 0x024 */ uint32_t SHCSR;                   /* System Handler Control and State Register */
} SCB_Type;  /* sizeof = 0x28 */


typedef struct {
    /* 0x000 */ uint32_t TYPE;                    /* MPU Type Register */
    /* 0x004 */ uint32_t CTRL;                    /* MPU Control Register */
    /* 0x008 */ uint32_t RNR;                     /* MPU Region Number Register */
    /* 0x00C */ uint32_t RBAR;                    /* MPU Region Base Address Register */
    /* 0x010 */ uint32_t RASR;                    /* MPU Region Attribute and Size Register */
} MPU_Type;  /* sizeof = 0x14 */'''

CORE = {
    "m4f": dict(
        text=CORE_M4_TEXT,
        title="Cortex-M4F core (CMSIS core_cm4.h)",
        cpu="Cortex-M4F",
        instances=[  # name, base, type, size, description
            ("ITM", 0xE0000000, "ITM_Type", 0x1000, "Instrumentation Trace Macrocell"),
            ("DWT", 0xE0001000, "DWT_Type", 0x5C, "Data Watchpoint and Trace"),
            ("SCnSCB", 0xE000E000, "SCnSCB_Type", 0xC, "System Control and ID registers not in the SCB (ICTR, ACTLR)"),
            ("SysTick", 0xE000E010, "SysTick_Type", 0x10, "System timer"),
            ("NVIC", 0xE000E100, "NVIC_Type", 0xE04, "Nested Vectored Interrupt Controller (CMSIS struct also spans SCB/MPU/CoreDebug)"),
            ("SCB", 0xE000ED00, "SCB_Type", 0x8C, "System Control Block (VTOR, AIRCR, fault status ...)"),
            ("MPU", 0xE000ED90, "MPU_Type", 0x2C, "Memory Protection Unit"),
            ("CoreDebug", 0xE000EDF0, "CoreDebug_Type", 0x10, "Core debug registers (DHCSR, DEMCR ...)"),
            ("FPU", 0xE000EF30, "FPU_Type", 0x18, "Floating-point unit control (FPCCR, FPCAR, FPDSCR)"),
            ("TPI", 0xE0040000, "TPI_Type", 0xFD0, "Trace Port Interface Unit"),
        ],
        core_types={"SCnSCB_Type", "SysTick_Type", "NVIC_Type", "SCB_Type", "ITM_Type", "DWT_Type",
                    "TPI_Type", "CoreDebug_Type", "MPU_Type", "FPU_Type"},
    ),
    "m0plus": dict(
        text=CORE_M0P_TEXT,
        title="Cortex-M0+ core (CMSIS core_cm0plus.h)",
        cpu="Cortex-M0+",
        instances=[
            ("SysTick", 0xE000E010, "SysTick_Type", 0x10, "System timer"),
            ("NVIC", 0xE000E100, "NVIC_Type", 0x320, "Nested Vectored Interrupt Controller"),
            ("SCB", 0xE000ED00, "SCB_Type", 0x28, "System Control Block (VTOR, AIRCR ...)"),
            ("MPU", 0xE000ED90, "MPU_Type", 0x14, "Memory Protection Unit"),
        ],
        core_types={"SysTick_Type", "NVIC_Type", "SCB_Type", "MPU_Type"},
    ),
}

C_KEYWORDS = set("""auto break case char const continue default do double else enum extern float for goto if
inline int long register restrict return short signed sizeof static struct switch typedef union unsigned
void volatile while int8_t int16_t int32_t uint8_t uint16_t uint32_t bool""".split())

CTYPE = {8: "uint8_t", 16: "uint16_t", 32: "uint32_t"}


# --------------------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------------------
def num(s, default=None):
    if s is None:
        return default
    s = s.strip()
    if not s:
        return default
    if s.lower().startswith("0x"):
        return int(s, 16)
    if s.startswith("#"):
        return int(s[1:], 2)
    return int(s, 10)


def txt(el, tag, default=None):
    if el is None:
        return default
    c = el.find(tag)
    if c is None or c.text is None:
        return default
    return c.text.strip()


def clean(s):
    """Normalise SVD description text to one ASCII line."""
    if not s:
        return ""
    s = " ".join(s.split())
    return s.encode("ascii", "replace").decode("ascii")


def ccomment(s, limit=70):
    s = clean(s).replace("*/", "* /").replace("/*", "/ *").replace("\\", "/")
    if len(s) > limit:
        s = s[: limit - 3].rstrip() + "..."
    return s


def cident(s):
    s = re.sub(r"[^0-9A-Za-z_]", "_", s)
    if not s or s[0].isdigit():
        s = "_" + s
    if s in C_KEYWORDS:
        s += "_"
    return s


def warn(msg):
    sys.stderr.write("svd2hw: warning: %s\n" % msg)


def dim_indexes(el):
    """Return list of index strings for an element with <dim>, or None."""
    d = el.find("dim")
    if d is None:
        return None
    n = num(d.text)
    idx = txt(el, "dimIndex")
    if idx:
        if "," in idx:
            return [x.strip() for x in idx.split(",")]
        m = re.fullmatch(r"(\d+)\s*-\s*(\d+)", idx)
        if m:
            return [str(i) for i in range(int(m.group(1)), int(m.group(2)) + 1)]
        m = re.fullmatch(r"([A-Za-z])\s*-\s*([A-Za-z])", idx)
        if m:
            return [chr(c) for c in range(ord(m.group(1)), ord(m.group(2)) + 1)]
        return [idx]
    return [str(i) for i in range(n)]


def subst(name, idx):
    if "[%s]" in name:
        return name.replace("[%s]", idx)
    if "%s" in name:
        return name.replace("%s", idx)
    return name + idx


# --------------------------------------------------------------------------------------
# SVD model
# --------------------------------------------------------------------------------------
class Reg(object):
    __slots__ = ("name", "offset", "bits", "access", "reset", "mask", "desc", "fields", "alt",
                 "order", "arr", "member", "in_struct", "alias_of", "display")

    def __init__(self, **kw):
        for k in self.__slots__:
            setattr(self, k, kw.get(k))
        self.in_struct = False
        self.alias_of = None

    @property
    def nbytes(self):
        return max(1, (self.bits + 7) // 8)


def parse_fields(reg_el):
    out = []
    fs = reg_el.find("fields")
    if fs is None:
        return out
    for f in fs.findall("field"):
        names = [txt(f, "name")]
        idxs = dim_indexes(f)
        if idxs is not None:
            names = [subst(txt(f, "name"), i) for i in idxs]
        inc = num(txt(f, "dimIncrement"), 0)
        if f.find("bitRange") is not None:
            m = re.fullmatch(r"\[\s*(\d+)\s*:\s*(\d+)\s*\]", txt(f, "bitRange"))
            msb, lsb = int(m.group(1)), int(m.group(2))
            boff, bw = lsb, msb - lsb + 1
        elif f.find("bitOffset") is not None:
            boff, bw = num(txt(f, "bitOffset")), num(txt(f, "bitWidth"), 1)
        else:
            lsb, msb = num(txt(f, "lsb")), num(txt(f, "msb"))
            boff, bw = lsb, msb - lsb + 1
        enums = {}
        for ev in f.findall("enumeratedValues/enumeratedValue"):
            v = txt(ev, "value")
            try:
                enums[str(num(v))] = txt(ev, "name")
            except (ValueError, TypeError):
                pass
        for k, nm in enumerate(names):
            d = {"name": nm, "bitOffset": boff + k * inc, "bitWidth": bw, "description": clean(txt(f, "description"))}
            acc = txt(f, "access")
            if acc:
                d["access"] = acc
            if enums:
                d["enums"] = enums
            out.append(d)
    return out


class Counter(object):
    n = 0


def expand_children(container, base_off, prefix, dflt, out, order):
    """Flatten <register>/<cluster> children of `container` into Reg objects appended to `out`."""
    for ch in container:
        if ch.tag == "register":
            expand_register(ch, base_off, prefix, dflt, out, order)
        elif ch.tag == "cluster":
            cd = dict(dflt)
            for k in ("size", "access", "resetValue", "resetMask"):
                v = txt(ch, k)
                if v is not None:
                    cd[k] = v
            idxs = dim_indexes(ch)
            inc = num(txt(ch, "dimIncrement"), 0)
            off = num(txt(ch, "addressOffset"), 0)
            cname = txt(ch, "name")
            if ch.get("derivedFrom"):
                warn("cluster %s uses derivedFrom (unsupported, skipped)" % cname)
                continue
            if idxs is None:
                expand_children(ch, base_off + off, prefix + cname + "_", cd, out, order)
            else:
                for k, ix in enumerate(idxs):
                    expand_children(ch, base_off + off + k * inc, prefix + subst(cname, ix) + "_", cd, out, order)


def expand_register(el, base_off, prefix, dflt, out, order):
    name = txt(el, "name")
    off = num(txt(el, "addressOffset"), 0)
    bits = num(txt(el, "size"), None)
    if bits is None:
        bits = num(dflt.get("size"), 32)
    access = txt(el, "access") or dflt.get("access") or "read-write"
    reset = txt(el, "resetValue") or dflt.get("resetValue") or "0x0"
    mask = txt(el, "resetMask") or dflt.get("resetMask")
    desc = clean(txt(el, "description") or txt(el, "displayName") or "")
    fields = parse_fields(el)
    alt = txt(el, "alternateRegister")
    idxs = dim_indexes(el)
    inc = num(txt(el, "dimIncrement"), 0)
    common = dict(bits=bits, access=access, reset=num(reset, 0), mask=num(mask) if mask else None, desc=desc,
                  fields=fields, alt=alt)
    if idxs is None:
        out.append(Reg(name=prefix + name, offset=base_off + off, order=len(order), arr=None, **common))
        order.append(1)
        return
    Counter.n += 1
    arr_id = Counter.n
    is_arr_form = "[%s]" in name
    for k, ix in enumerate(idxs):
        nm = prefix + subst(name, ix)
        out.append(Reg(name=nm, offset=base_off + off + k * inc, order=len(order),
                       arr=dict(id=arr_id, base=prefix + name.replace("[%s]", "").replace("%s", ""), idx=ix, k=k,
                                n=len(idxs), stride=inc, arrform=is_arr_form), **common))
        order.append(1)


class Periph(object):
    def __init__(self):
        self.name = None
        self.desc = ""
        self.group = None
        self.base = 0
        self.derived_from = None
        self.root = None  # root Periph (self if not derived)
        self.blocks = []
        self.regs = []
        self.irqs = []
        self.type = None
        self.struct_size = None
        self.members = None


def load_svd(path):
    root = ET.parse(path).getroot()
    dev = dict(
        name=txt(root, "name"), version=txt(root, "version"), description=clean(txt(root, "description")),
        vendor=txt(root, "vendor"), cpu=txt(root, "cpu/name"),
        dflt=dict(size=txt(root, "size"), access=txt(root, "access"),
                  resetValue=txt(root, "resetValue"), resetMask=txt(root, "resetMask")),
    )
    pel = {}
    order = []
    for p in root.find("peripherals").findall("peripheral"):
        pel[txt(p, "name")] = p
        order.append(txt(p, "name"))
    periphs = {}

    def build(name, stack=()):
        if name in periphs:
            return periphs[name]
        if name in stack:
            raise ValueError("derivedFrom cycle at %s" % name)
        el = pel[name]
        P = Periph()
        P.name = name
        P.desc = clean(txt(el, "description"))
        P.group = txt(el, "groupName")
        P.base = num(txt(el, "baseAddress"), 0)
        P.blocks = [(num(txt(a, "offset"), 0), num(txt(a, "size"), 0)) for a in el.findall("addressBlock")]
        for i in el.findall("interrupt"):
            P.irqs.append((num(txt(i, "value")), txt(i, "name"), clean(txt(i, "description"))))
        df = el.get("derivedFrom")
        dflt = dict(dev["dflt"])
        for k in ("size", "access", "resetValue", "resetMask"):
            v = txt(el, k)
            if v is not None:
                dflt[k] = v
        own = []
        regs_el = el.find("registers")
        if regs_el is not None:
            expand_children(regs_el, 0, "", dflt, own, [])
        if df:
            if df not in pel:
                raise ValueError("%s derivedFrom unknown %s" % (name, df))
            R = build(df, stack + (name,))
            P.derived_from = df
            P.root = R.root
            if not P.group:
                P.group = R.group
            if not P.desc:
                P.desc = R.desc
            if not P.blocks:
                P.blocks = R.blocks
            if own:
                # override-by-name (rare); otherwise inherit
                byname = dict((r.name, r) for r in R.regs)
                for r in own:
                    byname[r.name] = r
                P.regs = sorted(byname.values(), key=lambda r: r.order)
                P.root = P
            else:
                P.regs = R.regs
        else:
            P.root = P
            P.regs = own
        periphs[name] = P
        return P

    for n in order:
        build(n)
    return dev, [periphs[n] for n in order]


# --------------------------------------------------------------------------------------
# struct layout
# --------------------------------------------------------------------------------------
def common_prefix_strip(P):
    """Upper-case prefix (incl. '_') to strip from the member names of root P, else ''.

    ST's SVDs prefix register names with the peripheral (ADC_ISR, TIM1_CR1, ...), often with a few
    exceptions (CCMR1_Output, IDCODE).  The prefix is stripped when it names the peripheral/group and
    at least 70 % (and >= 2) of the non-alternate registers carry it and the result stays unique."""
    regs = [r for r in P.regs if not r.alt]  # alternate registers may be named differently
    names = [r.name for r in regs]
    if len(names) < 2:
        return ""
    cands = []
    for c in (P.name, P.group, re.sub(r"\d+$", "", P.name or "")):
        if c and c.upper() + "_" not in cands:
            cands.append(c.upper() + "_")
    for pre in cands:
        hit = [n for n in names if n.upper().startswith(pre) and len(n) > len(pre)]
        if len(hit) >= 2 and len(hit) >= 0.7 * len(names):
            new = [cident(strip_name(r.name, pre)) for r in P.regs]
            if len(set(new)) == len(new):
                return pre
    return ""


def strip_name(name, strip):
    if strip and name.upper().startswith(strip):
        return name[len(strip):]
    return name


def layout(P):
    """Compute member list for root peripheral P. Returns (members, size, align). Sets reg.member/in_struct."""
    strip = common_prefix_strip(P)
    regs = P.regs
    for r in regs:
        r.display = r.name
        r.member = cident(strip_name(r.name, strip))
        r.in_struct = False
        r.alias_of = None
    # group arrays
    items = []  # (offset, nbytes, is_alt, order, kind, payload)
    seen = set()
    groups = {}
    for r in regs:
        if r.arr:
            groups.setdefault(r.arr["id"], []).append(r)
    for r in regs:
        if r.arr and r.arr["id"] in groups:
            g = groups[r.arr["id"]]
            if r.arr["id"] in seen:
                continue
            seen.add(r.arr["id"])
            a = g[0].arr
            idxs = [x.arr["idx"] for x in g]
            ok = (a["arrform"] and idxs == [str(i) for i in range(len(g))] and a["stride"] == g[0].nbytes
                  and g[0].bits in CTYPE and g[0].offset % g[0].nbytes == 0)
            if ok:
                items.append((g[0].offset, g[0].nbytes * len(g), bool(g[0].alt), g[0].order, "array", g))
                continue
            for x in g:
                items.append((x.offset, x.nbytes, bool(x.alt), x.order, "reg", x))
        else:
            items.append((r.offset, r.nbytes, bool(r.alt), r.order, "reg", r))
    items.sort(key=lambda t: (t[0], t[2], t[3]))
    members = []  # dicts: off, ctype, name, count, comment, nbytes, align
    used = set()
    kept = []  # (off, end, name)
    cur = 0
    rsv = [0]
    max_align = 1

    def uniq(name, off):
        n = name
        if re.fullmatch(r"RESERVED\d*", n):
            n += "_REG"
        if n in used:
            n = "%s_%X" % (name, off)
        k = 2
        while n in used:
            n = "%s_%X_%d" % (name, off, k)
            k += 1
        used.add(n)
        return n

    def pad(frm, to):
        nonlocal max_align
        while frm < to:
            gap = to - frm
            if frm % 4 == 0 and gap >= 4:
                cnt = gap // 4
                members.append(dict(off=frm, ctype="uint32_t", name="RESERVED%d" % rsv[0], count=cnt, comment="",
                                    nbytes=4 * cnt, align=4))
                max_align = max(max_align, 4)
                frm += 4 * cnt
            else:
                cnt = min(gap, 4 - frm % 4) if frm % 4 else gap
                members.append(dict(off=frm, ctype="uint8_t", name="RESERVED%d" % rsv[0], count=cnt, comment="",
                                    nbytes=cnt, align=1))
                frm += cnt
            used.add("RESERVED%d" % rsv[0])
            rsv[0] += 1

    for off, nb, isalt, order, kind, payload in items:
        end = off + nb
        if off < cur:
            owner = None
            for (ko, ke, kn) in kept:
                if off < ke and ko < end:
                    owner = kn
                    break
            regs_ = payload if kind == "array" else [payload]
            for r in regs_:
                r.in_struct = False
                r.alias_of = owner
            continue
        pad(cur, off)
        if kind == "array":
            g = payload
            nm = uniq(cident(strip_name(g[0].arr["base"], strip)), off)
            ct = CTYPE[g[0].bits]
            members.append(dict(off=off, ctype=ct, name=nm, count=len(g), comment=g[0].desc, nbytes=nb, align=g[0].nbytes))
            max_align = max(max_align, g[0].nbytes)
            for k, x in enumerate(g):
                x.member = "%s[%d]" % (nm, k)
                x.in_struct = True
            kept.append((off, end, g[0].arr["base"]))
        else:
            r = payload
            nm = uniq(r.member, off)
            r.member = nm
            r.in_struct = True
            if r.bits in CTYPE and off % r.nbytes == 0:
                members.append(dict(off=off, ctype=CTYPE[r.bits], name=nm, count=0, comment=r.desc, nbytes=r.nbytes, align=r.nbytes))
                max_align = max(max_align, r.nbytes)
            else:
                members.append(dict(off=off, ctype="uint8_t", name=nm, count=r.nbytes, comment=r.desc, nbytes=r.nbytes, align=1))
            kept.append((off, end, r.name))
        cur = end
    size = (cur + max_align - 1) // max_align * max_align
    if size > cur:
        pad(cur, size)
    return members, size, max_align


def sig_of(P):
    return tuple((r.member, r.offset, r.bits, r.in_struct) for r in P.regs)


def assign_types(roots, core_types, all_hw):
    """Lay out every root, merge identical layouts, return {typename: (members,size,[roots])}."""
    for P in roots:
        P.members, P.struct_size, _ = layout(P)
    # group by SVD groupName
    bygroup = {}
    for P in roots:
        bygroup.setdefault(P.group or P.name, []).append(P)
    types = {}
    for g, lst in bygroup.items():
        lst = [P for P in lst if P.regs]
        if not lst:
            continue
        sigs = {}
        for P in lst:
            sigs.setdefault(sig_of(P), []).append(P)
        for sig, ps in sigs.items():
            ninst = sum(1 for P in all_hw if P.root in ps)
            if len(sigs) == 1 and ninst > 1:
                base = cident(g)
            else:
                base = cident(ps[0].name)
            tn = base + "_Type"
            if tn in core_types:
                tn = base + "_Periph_Type"
            k = 2
            while tn in types:
                tn = "%s_%d_Type" % (base, k)
                k += 1
            types[tn] = (ps[0].members, ps[0].struct_size, ps)
            for P in ps:
                P.type = tn
    return types


# --------------------------------------------------------------------------------------
# emitters
# --------------------------------------------------------------------------------------
def emit_struct(tn, members, size, header_comment):
    out = []
    if header_comment:
        out.append("/* %s */" % header_comment)
    out.append("typedef struct {")
    for m in members:
        decl = "%s %s" % (m["ctype"], m["name"])
        if m["count"]:
            decl += "[%d]" % m["count"]
        decl += ";"
        line = "    /* 0x%03X */ %s" % (m["off"], decl)
        if m["comment"]:
            line = line.ljust(52) + " /* %s */" % ccomment(m["comment"])
        out.append(line)
    out.append("} %s;  /* sizeof = 0x%X */" % (tn, size))
    return "\n".join(out)


def parse_startup(path):
    toks = []
    started = False
    for line in open(path, errors="replace"):
        s = line.strip()
        if s.startswith("g_pfnVectors:"):
            started = True
            continue
        if not started:
            continue
        m = re.match(r"\.word\s+(\S+)", s)
        if m:
            toks.append(m.group(1))
        elif s.startswith(".size") or (toks and s and not s.startswith(("/", "*", "."))):
            break
    return toks


def parse_irq_header(path):
    out = {}
    pat = re.compile(r"^\s*(\w+?)_IRQn\s*=\s*(-?\d+)\s*,?\s*(?:/\*!?<?\s*(.*?)\s*\*/)?")
    for line in open(path, errors="replace"):
        m = pat.match(line)
        if m and int(m.group(2)) >= 0:
            out.setdefault(int(m.group(2)), (m.group(1), clean(m.group(3) or "")))
    return out


def build_irqs(periphs, header, startup_toks):
    svd = {}
    for P in periphs:
        for (val, nm, ds) in P.irqs:
            e = svd.setdefault(val, dict(name=nm, desc=ds, periph=[]))
            if P.name not in e["periph"]:
                e["periph"].append(P.name)
    st = {}
    reserved = []
    if startup_toks:
        for slot in range(16, len(startup_toks)):
            t = startup_toks[slot]
            if t == "0":
                reserved.append(slot - 16)
            else:
                st[slot - 16] = re.sub(r"_IRQHandler$", "", t)
    nums = sorted(set(svd) | set(header) | set(st))
    res = []
    for n in nums:
        srcs = []
        if n in st:
            srcs.append("startup")
        if n in header:
            srcs.append("header")
        if n in svd:
            srcs.append("svd")
        name = st.get(n) or (header[n][0] if n in header else svd[n]["name"])
        desc = (header[n][1] if n in header and header[n][1] else (svd[n]["desc"] if n in svd else ""))
        e = {"number": n, "exception": n + 16, "name": name, "description": desc, "handler": name + "_IRQHandler"}
        if n in svd:
            e["svd_name"] = svd[n]["name"]
            e["peripherals"] = svd[n]["periph"]
        if n in header:
            e["header_name"] = header[n][0]
        e["sources"] = srcs
        if startup_toks and n in reserved:
            e["startup_reserved"] = True
        res.append(e)
    return res, reserved


def reg_doc(r):
    d = {"name": r.display, "offset": r.offset, "size": r.bits, "access": r.access,
         "reset": "0x%0*X" % (max(2, r.bits // 4), r.reset), "description": r.desc,
         "member": r.member if r.in_struct else None, "in_struct": r.in_struct}
    if r.mask is not None and r.mask != (1 << r.bits) - 1:
        d["resetMask"] = "0x%X" % r.mask
    if r.alias_of:
        d["alias_of"] = r.alias_of
    if r.alt:
        d["alternate_of"] = r.alt
    d["fields"] = r.fields
    return d


def overlap_names(items):
    res = {}
    for a in items:
        for b in items:
            if a is b or a["size"] <= 0 or b["size"] <= 0:
                continue
            if a["base"] < b["base"] + b["size"] and b["base"] < a["base"] + a["size"]:
                res.setdefault(a["name"], []).append(b["name"])
    return res


def run(args):
    prof = PROFILES.get(args.chip, {})
    core_kind = args.core or prof.get("core")
    if core_kind not in CORE:
        sys.exit("need --core m4f|m0plus")
    core = CORE[core_kind]
    irq_header = args.irq_header or prof.get("irq_header")
    startup = args.startup or prof.get("startup")
    args.svd = args.svd or prof.get("svd")
    if not args.svd:
        sys.exit("--svd is required for chips without a profile")
    dev, periphs = load_svd(args.svd)
    # SVD pseudo-peripherals living in the System Control Space are covered by the core structs
    scs = [P for P in periphs if 0xE000E000 <= P.base < 0xE000F000]
    hw = [P for P in periphs if P not in scs]
    roots = [P for P in hw if P.root is P]
    types = assign_types(roots, core["core_types"], hw)
    for P in hw:
        if P.root is not P:
            P.type = P.root.type
            P.members, P.struct_size = P.root.members, P.root.struct_size

    # ---------------- header ----------------
    L = []
    L.append("/*")
    L.append(" * %s - peripheral register layouts" % (prof.get("label") or dev["name"]))
    L.append(" *")
    L.append(" * Register-layout structs for Ghidra's C parser (ghidra.app.util.cparser.C.CParser).")
    L.append(" * Generated by tools/svd2hw.py from the vendor CMSIS-SVD file %s (%s, version %s)" % (
        os.path.basename(args.svd), dev["name"], dev["version"]))
    L.append(" * plus Cortex core structs from ARM CMSIS. Do not hand-edit; see README.md in this directory.")
    L.append(" * Members are named after SVD registers; every member carries its byte offset in a leading")
    L.append(" * comment; holes are explicit RESERVEDn padding; alias (overlapping) SVD registers are not members.")
    L.append(" */")
    L.append("")
    L.append("typedef unsigned char uint8_t;")
    L.append("typedef unsigned short uint16_t;")
    L.append("typedef unsigned int uint32_t;")
    L.append("")
    for tn in sorted(types):
        members, size, ps = types[tn]
        inst = ", ".join(P.name for P in hw if P.type == tn)
        hc = ccomment("%s - instances: %s" % (ps[0].desc or ps[0].group or ps[0].name, inst), 160)
        L.append("")
        L.append(emit_struct(tn, members, size, hc))
    L.append("")
    L.append("")
    L.append("/* ---- %s %s ---- */" % (core["title"], "-" * max(3, 60 - len(core["title"]))))
    L.append("")
    L.append(core["text"].rstrip())
    L.append("")
    header_text = "\n".join(L)

    # ---------------- peripherals json ----------------
    items = []
    for P in hw:
        blk = max([o + s for (o, s) in P.blocks] or [0])
        it = {"name": P.name, "base": P.base, "size": P.struct_size if P.type else blk, "type": P.type,
              "description": P.desc, "source": "svd", "block": blk}
        if P.group:
            it["group"] = P.group
        if P.derived_from:
            it["derivedFrom"] = P.derived_from
        if P.irqs:
            it["interrupts"] = [{"number": v, "name": n} for (v, n, d) in P.irqs]
        if P.type and blk and P.struct_size > blk:
            it["block_overflow"] = True
        items.append(it)
    for (n, b, t, s, d) in core["instances"]:
        items.append({"name": n, "base": b, "size": s, "type": t, "description": d, "source": "core"})
    for x in prof.get("extras", []):
        items.append({"name": x["name"], "base": x["base"], "size": x["size"], "type": x.get("type"),
                      "description": x["description"], "source": "extra"})
    items.sort(key=lambda d: (d["base"], d["name"]))
    names = [i["name"] for i in items]
    dup = set(n for n in names if names.count(n) > 1)
    if dup:
        sys.exit("duplicate peripheral names: %s" % sorted(dup))
    ov = overlap_names(items)
    for i in items:
        if i["name"] in ov:
            i["overlaps"] = sorted(ov[i["name"]])
    # ---------------- registers json ----------------
    regs = {}
    for P in periphs:
        doc = {"base": P.base, "description": P.desc, "group": P.group, "type": P.type if P not in scs else None}
        if P.derived_from:
            doc["derivedFrom"] = P.derived_from
        if P in scs:
            doc["core"] = True
            doc["note"] = ("SVD pseudo-peripheral for the System Control Space; offsets are relative to 0x%08X. "
                           "Typed in the header through the core structs (NVIC_Type at 0xE000E100 etc.)." % P.base)
        r_sorted = sorted(P.regs, key=lambda r: (r.offset, r.order))
        # make sure member/in_struct reflect the root's layout
        doc["registers"] = [reg_doc(r) for r in r_sorted]
        regs[P.name] = doc
    # ---------------- irqs / core ----------------
    htab = parse_irq_header(irq_header) if irq_header and os.path.exists(irq_header) else {}
    stok = parse_startup(startup) if startup and os.path.exists(startup) else []
    irqs, reserved = build_irqs(periphs, htab, stok)
    names_core = list(CORE_NAMES_M4 if core_kind == "m4f" else CORE_NAMES_M0P)
    vectors = []
    nslots = len(stok) if stok else 16 + (max([i["number"] for i in irqs]) + 1 if irqs else 0)
    for s in range(nslots):
        if s < 16:
            nm = stok[s] if stok else names_core[s]
            if nm == "0":
                nm = None
            vectors.append({"slot": s, "name": nm, "reserved": nm is None,
                            "standard_name": names_core[s]})
        else:
            e = next((i for i in irqs if i["number"] == s - 16), None)
            vectors.append({"slot": s, "irq": s - 16, "name": (e["handler"] if e and not e.get("startup_reserved") else None),
                            "reserved": (e is None) or bool(e.get("startup_reserved"))})
    corej = {"chip": args.chip, "cpu": core["cpu"], "svd_cpu": dev["cpu"], "svd_device": dev["name"],
             "vector_table_slots": nslots, "vector_table_source": (os.path.basename(startup) if stok else None),
             "reserved_irq_numbers": reserved, "vectors": vectors,
             "note": "slot = exception number; slot 0 holds the initial stack pointer; IRQ n is slot n+16; "
                     "'reserved' slots are .word 0 in the vendor startup file"}

    # ---------------- write ----------------
    os.makedirs(args.out_dir, exist_ok=True)
    chip = args.chip

    def w(fname, text):
        with open(os.path.join(args.out_dir, fname), "w") as f:
            f.write(text)

    w(chip + ".h", header_text)
    w("peripherals_%s.json" % chip, json.dumps(items, indent=1) + "\n")
    # registers json: one peripheral per block of lines to keep diffs sane
    parts = []
    for k, v in regs.items():
        parts.append(json.dumps(k) + ": " + json.dumps(v, separators=(",", ":")))
    w("%s_registers.json" % chip, "{\n" + ",\n".join(parts) + "\n}\n")
    w("%s_irqs.json" % chip, json.dumps(irqs, indent=1) + "\n")
    w("%s_core.json" % chip, json.dumps(corej, indent=1) + "\n")

    # ---------------- report ----------------
    nalias = sum(1 for P in roots for r in P.regs if not r.in_struct)
    sys.stderr.write("svd2hw: %s: %d peripherals (%d roots), %d struct types, %d IRQs, %d alias registers dropped\n" % (
        chip, len(hw), len(roots), len(types), len(irqs), nalias))
    for P in roots:
        for r in P.regs:
            if not r.in_struct:
                sys.stderr.write("svd2hw:   alias %s.%s @0x%X overlaps %s\n" % (P.name, r.name, r.offset, r.alias_of))
    for i in items:
        if i.get("block_overflow"):
            sys.stderr.write("svd2hw:   note: %s struct (0x%X) exceeds its SVD address block (0x%X)\n" % (i["name"], i["size"], i["block"]))
    return 0


# --------------------------------------------------------------------------------------
# self test: tiny synthetic SVD exercising derivedFrom, dim, cluster, 8/16-bit regs, aliases
# --------------------------------------------------------------------------------------
SELFTEST_SVD = """<?xml version="1.0"?>
<device><name>TEST</name><version>1</version><description>t</description>
<cpu><name>CM4</name></cpu><size>32</size><access>read-write</access><resetValue>0</resetValue><resetMask>0xFFFFFFFF</resetMask>
<peripherals>
 <peripheral><name>FOO1</name><groupName>FOO</groupName><description>foo</description><baseAddress>0x40000000</baseAddress>
  <addressBlock><offset>0</offset><size>0x400</size><usage>registers</usage></addressBlock>
  <interrupt><name>FOO1_IRQ</name><value>3</value></interrupt>
  <registers>
   <register><name>FOO_CR</name><addressOffset>0x0</addressOffset><size>32</size><fields><field><name>EN</name><bitOffset>0</bitOffset><bitWidth>1</bitWidth></field></fields></register>
   <register><name>FOO_B8</name><addressOffset>0x4</addressOffset><size>8</size></register>
   <register><name>FOO_H16</name><addressOffset>0x6</addressOffset><size>16</size></register>
   <register><name>FOO_ARR[%s]</name><addressOffset>0x10</addressOffset><dim>3</dim><dimIncrement>4</dimIncrement><dimIndex>0-2</dimIndex></register>
   <register><name>FOO_X%s</name><addressOffset>0x20</addressOffset><dim>2</dim><dimIncrement>8</dimIncrement></register>
   <cluster><name>CH%s</name><dim>2</dim><dimIncrement>0x10</dimIncrement><addressOffset>0x40</addressOffset>
     <register><name>CTL</name><addressOffset>0</addressOffset></register>
     <register><name>CNT</name><addressOffset>4</addressOffset></register></cluster>
   <register><name>FOO_OUT</name><addressOffset>0x80</addressOffset></register>
   <register><name>FOO_IN</name><addressOffset>0x80</addressOffset><alternateRegister>FOO_OUT</alternateRegister></register>
   <register><name>FOO_TAIL16</name><addressOffset>0x90</addressOffset><size>16</size></register>
  </registers></peripheral>
 <peripheral derivedFrom="FOO1"><name>FOO2</name><baseAddress>0x40000400</baseAddress></peripheral>
 <peripheral><name>BAR</name><baseAddress>0x40001000</baseAddress>
  <addressBlock><offset>0</offset><size>0x100</size><usage>registers</usage></addressBlock>
  <registers><register><name>SR</name><addressOffset>0x0</addressOffset></register>
   <register><name>SR</name><addressOffset>0x8</addressOffset></register></registers></peripheral>
</peripherals></device>
"""


def selftest(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    svd = os.path.join(out_dir, "selftest.svd")
    with open(svd, "w") as f:
        f.write(SELFTEST_SVD)
    ns = argparse.Namespace(chip="selftest", svd=svd, core="m4f", out_dir=out_dir, irq_header=None, startup=None)
    run(ns)
    print(open(os.path.join(out_dir, "selftest.h")).read().split("Cortex-M4F core")[0])
    return svd


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--svd")
    ap.add_argument("--chip", help="output stem, e.g. at32f415 (a known name selects a profile)")
    ap.add_argument("--core", choices=sorted(CORE))
    ap.add_argument("--irq-header", help="vendor CMSIS device header with the IRQn_Type enum")
    ap.add_argument("--startup", help="vendor GCC startup .s file (vector table layout / reserved slots)")
    ap.add_argument("--out-dir", default=DEFAULT_OUT)
    ap.add_argument("--selftest", action="store_true", help="convert a synthetic SVD into --out-dir (default: ./svd2hw_selftest)")
    a = ap.parse_args(argv)
    if a.selftest:
        selftest(a.out_dir if a.out_dir != DEFAULT_OUT else "svd2hw_selftest")
        return 0
    if not a.chip:
        ap.error("--chip is required")
    return run(a)


if __name__ == "__main__":
    sys.exit(main())
