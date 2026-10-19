#!/usr/bin/env python3
"""Verify stm32f1.h / stm32f0.h (and the peripherals_*.json maps) with Ghidra's C parser.

Run:
    GHIDRA_INSTALL_DIR=/opt/ghidra_12.1.4_PUBLIC /opt/zt3-venv/bin/python verify_headers.py [-v]

For each header the script
  1. parses it with ghidra.app.util.cparser.C.CParserUtils into a throwaway
     StandAloneDataTypeManager (Ghidra 12.x name; there is no "Standalone..." class),
  2. prints every struct's name, size and (with -v) every member offset,
  3. asserts sizes / member offsets against tables derived from ST's CMSIS device
     headers (cmsis_device_f1 stm32f103xb.h, cmsis_device_f0 stm32f091xc.h/stm32f072xb.h)
     and ARM's core_cm3.h / core_cm0.h,
  4. asserts every JSON "type" exists in the parsed header, "size" == sizeof(type),
     names are unique, and a handful of well-known base addresses are right.

Exit status is non-zero on any failure.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERBOSE = "-v" in sys.argv

os.environ.setdefault("GHIDRA_INSTALL_DIR", "/opt/ghidra_12.1.4_PUBLIC")

# --------------------------------------------------------------------------
# Expected layouts: type -> (sizeof, {top-level member: byte offset})
# --------------------------------------------------------------------------
F1 = {
    "GPIO_TypeDef": (0x1C, dict(CRL=0, CRH=4, IDR=8, ODR=0xC, BSRR=0x10, BRR=0x14, LCKR=0x18)),
    "AFIO_TypeDef": (0x20, dict(EVCR=0, MAPR=4, EXTICR=8, RESERVED0=0x18, MAPR2=0x1C)),
    "EXTI_TypeDef": (0x18, dict(IMR=0, EMR=4, RTSR=8, FTSR=0xC, SWIER=0x10, PR=0x14)),
    "RCC_TypeDef": (0x28, dict(CR=0, CFGR=4, CIR=8, APB2RSTR=0xC, APB1RSTR=0x10, AHBENR=0x14,
                               APB2ENR=0x18, APB1ENR=0x1C, BDCR=0x20, CSR=0x24)),
    "FLASH_TypeDef": (0x24, dict(ACR=0, KEYR=4, OPTKEYR=8, SR=0xC, CR=0x10, AR=0x14,
                                 RESERVED=0x18, OBR=0x1C, WRPR=0x20)),
    "OB_TypeDef": (0x10, dict(RDP=0, USER=2, Data0=4, Data1=6, WRP0=8, WRP1=0xA, WRP2=0xC, WRP3=0xE)),
    "PWR_TypeDef": (8, dict(CR=0, CSR=4)),
    "BKP_TypeDef": (0x38, dict(RESERVED0=0, DR1=4, DR2=8, DR10=0x28, RTCCR=0x2C, CR=0x30, CSR=0x34)),
    "DMA_Channel_TypeDef": (0x10, dict(CCR=0, CNDTR=4, CPAR=8, CMAR=0xC)),
    "DMA_TypeDef": (8, dict(ISR=0, IFCR=4)),
    "TIM_TypeDef": (0x54, dict(CR1=0, CR2=4, SMCR=8, DIER=0xC, SR=0x10, EGR=0x14, CCMR1=0x18,
                               CCMR2=0x1C, CCER=0x20, CNT=0x24, PSC=0x28, ARR=0x2C, RCR=0x30,
                               CCR1=0x34, CCR2=0x38, CCR3=0x3C, CCR4=0x40, BDTR=0x44, DCR=0x48,
                               DMAR=0x4C, OR=0x50)),
    "RTC_TypeDef": (0x28, dict(CRH=0, CRL=4, PRLH=8, PRLL=0xC, DIVH=0x10, DIVL=0x14,
                               CNTH=0x18, CNTL=0x1C, ALRH=0x20, ALRL=0x24)),
    "IWDG_TypeDef": (0x10, dict(KR=0, PR=4, RLR=8, SR=0xC)),
    "WWDG_TypeDef": (0xC, dict(CR=0, CFR=4, SR=8)),
    "USART_TypeDef": (0x1C, dict(SR=0, DR=4, BRR=8, CR1=0xC, CR2=0x10, CR3=0x14, GTPR=0x18)),
    "SPI_TypeDef": (0x20, dict(CR1=0, CR2=4, SR=8, DR=0xC, CRCPR=0x10, RXCRCR=0x14,
                               TXCRCR=0x18, I2SCFGR=0x1C)),
    "I2C_TypeDef": (0x24, dict(CR1=0, CR2=4, OAR1=8, OAR2=0xC, DR=0x10, SR1=0x14, SR2=0x18,
                               CCR=0x1C, TRISE=0x20)),
    "CAN_TxMailBox_TypeDef": (0x10, dict(TIR=0, TDTR=4, TDLR=8, TDHR=0xC)),
    "CAN_FIFOMailBox_TypeDef": (0x10, dict(RIR=0, RDTR=4, RDLR=8, RDHR=0xC)),
    "CAN_FilterRegister_TypeDef": (8, dict(FR1=0, FR2=4)),
    # NB: bxCAN register block as defined by CMSIS ends at the last filter bank (0x2B0);
    # the peripheral's 1 KB address window is larger than sizeof(CAN_TypeDef).
    "CAN_TypeDef": (0x2B0, dict(MCR=0, MSR=4, TSR=8, RF0R=0xC, RF1R=0x10, IER=0x14, ESR=0x18,
                                BTR=0x1C, RESERVED0=0x20, sTxMailBox=0x180, sFIFOMailBox=0x1B0,
                                RESERVED1=0x1D0, FMR=0x200, FM1R=0x204, RESERVED2=0x208,
                                FS1R=0x20C, RESERVED3=0x210, FFA1R=0x214, RESERVED4=0x218,
                                FA1R=0x21C, RESERVED5=0x220, sFilterRegister=0x240)),
    "USB_TypeDef": (0x54, dict(EP0R=0, EP1R=4, EP7R=0x1C, CNTR=0x40, ISTR=0x44, FNR=0x48,
                               DADDR=0x4C, BTABLE=0x50)),
    "ADC_TypeDef": (0x50, dict(SR=0, CR1=4, CR2=8, SMPR1=0xC, SMPR2=0x10, JOFR1=0x14, HTR=0x24,
                               LTR=0x28, SQR1=0x2C, SQR2=0x30, SQR3=0x34, JSQR=0x38, JDR1=0x3C,
                               JDR4=0x48, DR=0x4C)),
    "ADC_Common_TypeDef": (0x50, dict(SR=0, CR1=4, CR2=8, RESERVED=0xC, DR=0x4C)),
    "CRC_TypeDef": (0xC, dict(DR=0, IDR=4, RESERVED0=5, RESERVED1=6, CR=8)),
    "DBGMCU_TypeDef": (8, dict(IDCODE=0, CR=4)),
    # Cortex-M3 core
    "SCnSCB_Type": (0xC, dict(RESERVED0=0, ICTR=4, ACTLR=8)),
    "SysTick_Type": (0x10, dict(CTRL=0, LOAD=4, VAL=8, CALIB=0xC)),
    "NVIC_Type": (0xE04, dict(ISER=0, ICER=0x80, ISPR=0x100, ICPR=0x180, IABR=0x200, IP=0x300, STIR=0xE00)),
    "SCB_Type": (0x8C, dict(CPUID=0, ICSR=4, VTOR=8, AIRCR=0xC, SCR=0x10, CCR=0x14, SHP=0x18,
                            SHCSR=0x24, CFSR=0x28, HFSR=0x2C, DFSR=0x30, MMFAR=0x34, BFAR=0x38,
                            AFSR=0x3C, PFR=0x40, DFR=0x48, ADR=0x4C, MMFR=0x50, ISAR=0x60,
                            CPACR=0x88)),
    "ITM_Type": (0x1000, dict(PORT=0, TER=0xE00, TPR=0xE40, TCR=0xE80, LAR=0xFB0, LSR=0xFB4,
                              PID4=0xFD0, CID3=0xFFC)),
    "DWT_Type": (0x5C, dict(CTRL=0, CYCCNT=4, CPICNT=8, EXCCNT=0xC, SLEEPCNT=0x10, LSUCNT=0x14,
                            FOLDCNT=0x18, PCSR=0x1C, COMP0=0x20, MASK0=0x24, FUNCTION0=0x28,
                            COMP1=0x30, COMP2=0x40, COMP3=0x50, FUNCTION3=0x58)),
    "TPI_Type": (0xFD0, dict(SSPSR=0, CSPSR=4, ACPR=0x10, SPPR=0xF0, FFSR=0x300, FFCR=0x304)),
    "CoreDebug_Type": (0x10, dict(DHCSR=0, DCRSR=4, DCRDR=8, DEMCR=0xC)),
}

F0 = {
    "GPIO_TypeDef": (0x2C, dict(MODER=0, OTYPER=4, OSPEEDR=8, PUPDR=0xC, IDR=0x10, ODR=0x14,
                                BSRR=0x18, LCKR=0x1C, AFR=0x20, BRR=0x28)),
    "SYSCFG_TypeDef": (0x100, dict(CFGR1=0, RESERVED=4, EXTICR=8, CFGR2=0x18, RESERVED1=0x1C,
                                   IT_LINE_SR=0x80)),
    "EXTI_TypeDef": (0x18, dict(IMR=0, EMR=4, RTSR=8, FTSR=0xC, SWIER=0x10, PR=0x14)),
    "RCC_TypeDef": (0x38, dict(CR=0, CFGR=4, CIR=8, APB2RSTR=0xC, APB1RSTR=0x10, AHBENR=0x14,
                               APB2ENR=0x18, APB1ENR=0x1C, BDCR=0x20, CSR=0x24, AHBRSTR=0x28,
                               CFGR2=0x2C, CFGR3=0x30, CR2=0x34)),
    "FLASH_TypeDef": (0x24, dict(ACR=0, KEYR=4, OPTKEYR=8, SR=0xC, CR=0x10, AR=0x14,
                                 RESERVED=0x18, OBR=0x1C, WRPR=0x20)),
    "OB_TypeDef": (0x10, dict(RDP=0, USER=2, DATA0=4, DATA1=6, WRP0=8, WRP1=0xA, WRP2=0xC, WRP3=0xE)),
    "PWR_TypeDef": (8, dict(CR=0, CSR=4)),
    "CRS_TypeDef": (0x10, dict(CR=0, CFGR=4, ISR=8, ICR=0xC)),
    "DMA_Channel_TypeDef": (0x10, dict(CCR=0, CNDTR=4, CPAR=8, CMAR=0xC)),
    "DMA_TypeDef": (0xAC, dict(ISR=0, IFCR=4, RESERVED0=8, CSELR=0xA8)),
    "TIM_TypeDef": (0x54, dict(CR1=0, CR2=4, SMCR=8, DIER=0xC, SR=0x10, EGR=0x14, CCMR1=0x18,
                               CCMR2=0x1C, CCER=0x20, CNT=0x24, PSC=0x28, ARR=0x2C, RCR=0x30,
                               CCR1=0x34, CCR2=0x38, CCR3=0x3C, CCR4=0x40, BDTR=0x44, DCR=0x48,
                               DMAR=0x4C, OR=0x50)),
    "RTC_TypeDef": (0x64, dict(TR=0, DR=4, CR=8, ISR=0xC, PRER=0x10, WUTR=0x14, ALRMAR=0x1C,
                               WPR=0x24, SSR=0x28, SHIFTR=0x2C, TSTR=0x30, TSDR=0x34, TSSSR=0x38,
                               CALR=0x3C, TAFCR=0x40, ALRMASSR=0x44, BKP0R=0x50, BKP4R=0x60)),
    "IWDG_TypeDef": (0x14, dict(KR=0, PR=4, RLR=8, SR=0xC, WINR=0x10)),
    "WWDG_TypeDef": (0xC, dict(CR=0, CFR=4, SR=8)),
    "USART_TypeDef": (0x2C, dict(CR1=0, CR2=4, CR3=8, BRR=0xC, GTPR=0x10, RTOR=0x14, RQR=0x18,
                                 ISR=0x1C, ICR=0x20, RDR=0x24, TDR=0x28)),
    "SPI_TypeDef": (0x24, dict(CR1=0, CR2=4, SR=8, DR=0xC, CRCPR=0x10, RXCRCR=0x14, TXCRCR=0x18,
                               I2SCFGR=0x1C, I2SPR=0x20)),
    "I2C_TypeDef": (0x2C, dict(CR1=0, CR2=4, OAR1=8, OAR2=0xC, TIMINGR=0x10, TIMEOUTR=0x14,
                               ISR=0x18, ICR=0x1C, PECR=0x20, RXDR=0x24, TXDR=0x28)),
    "CAN_TxMailBox_TypeDef": (0x10, dict(TIR=0, TDTR=4, TDLR=8, TDHR=0xC)),
    "CAN_FIFOMailBox_TypeDef": (0x10, dict(RIR=0, RDTR=4, RDLR=8, RDHR=0xC)),
    "CAN_FilterRegister_TypeDef": (8, dict(FR1=0, FR2=4)),
    "CAN_TypeDef": (0x2B0, dict(MCR=0, MSR=4, TSR=8, RF0R=0xC, RF1R=0x10, IER=0x14, ESR=0x18,
                                BTR=0x1C, RESERVED0=0x20, sTxMailBox=0x180, sFIFOMailBox=0x1B0,
                                RESERVED1=0x1D0, FMR=0x200, FM1R=0x204, RESERVED2=0x208,
                                FS1R=0x20C, RESERVED3=0x210, FFA1R=0x214, RESERVED4=0x218,
                                FA1R=0x21C, RESERVED5=0x220, sFilterRegister=0x240)),
    "CEC_TypeDef": (0x18, dict(CR=0, CFGR=4, TXDR=8, RXDR=0xC, ISR=0x10, IER=0x14)),
    "USB_TypeDef": (0x5C, dict(EP0R=0, EP7R=0x1C, CNTR=0x40, ISTR=0x44, FNR=0x48, DADDR=0x4C,
                               BTABLE=0x50, LPMCSR=0x54, BCDR=0x58)),
    "ADC_TypeDef": (0x44, dict(ISR=0, IER=4, CR=8, CFGR1=0xC, CFGR2=0x10, SMPR=0x14, TR=0x20,
                               CHSELR=0x28, DR=0x40)),
    "ADC_Common_TypeDef": (4, dict(CCR=0)),
    "COMP_TypeDef": (2, dict(CSR=0)),
    "COMP_Common_TypeDef": (4, dict(CSR=0)),
    "DAC_TypeDef": (0x38, dict(CR=0, SWTRIGR=4, DHR12R1=8, DHR12L1=0xC, DHR8R1=0x10,
                               DHR12R2=0x14, DHR12RD=0x20, DOR1=0x2C, DOR2=0x30, SR=0x34)),
    "TSC_TypeDef": (0x54, dict(CR=0, IER=4, ICR=8, ISR=0xC, IOHCR=0x10, IOASCR=0x18, IOSCR=0x20,
                               IOCCR=0x28, IOGCSR=0x30, IOGXCR=0x34)),
    "CRC_TypeDef": (0x18, dict(DR=0, IDR=4, CR=8, INIT=0x10, POL=0x14)),
    "DBGMCU_TypeDef": (0x10, dict(IDCODE=0, CR=4, APB1FZ=8, APB2FZ=0xC)),
    # Cortex-M0 core
    "SysTick_Type": (0x10, dict(CTRL=0, LOAD=4, VAL=8, CALIB=0xC)),
    "NVIC_Type": (0x320, dict(ISER=0, ICER=0x80, ISPR=0x100, ICPR=0x180, IP=0x300)),
    "SCB_Type": (0x28, dict(CPUID=0, ICSR=4, AIRCR=0xC, SCR=0x10, CCR=0x14, SHP=0x1C, SHCSR=0x24)),
}

# Spot checks of instance base addresses (name -> base), straight from the RMs.
F1_BASES = dict(TIM2=0x40000000, TIM3=0x40000400, TIM4=0x40000800, RTC=0x40002800, WWDG=0x40002C00,
                IWDG=0x40003000, SPI2=0x40003800, USART2=0x40004400, USART3=0x40004800,
                I2C1=0x40005400, I2C2=0x40005800, USB=0x40005C00, CAN1=0x40006400, BKP=0x40006C00,
                PWR=0x40007000, AFIO=0x40010000, EXTI=0x40010400, GPIOA=0x40010800,
                GPIOB=0x40010C00, GPIOC=0x40011000, GPIOD=0x40011400, GPIOE=0x40011800,
                ADC1=0x40012400, ADC2=0x40012800, TIM1=0x40012C00, SPI1=0x40013000,
                USART1=0x40013800, DMA1=0x40020000, DMA1_Channel1=0x40020008,
                DMA1_Channel7=0x40020080, RCC=0x40021000, FLASH=0x40022000, CRC=0x40023000,
                DBGMCU=0xE0042000, SysTick=0xE000E010, NVIC=0xE000E100, SCB=0xE000ED00,
                OB=0x1FFFF800)
F0_BASES = dict(TIM2=0x40000000, TIM3=0x40000400, TIM6=0x40001000, TIM7=0x40001400,
                TIM14=0x40002000, RTC=0x40002800, WWDG=0x40002C00, IWDG=0x40003000,
                SPI2=0x40003800, USART2=0x40004400, USART3=0x40004800, USART4=0x40004C00,
                USART5=0x40005000, I2C1=0x40005400, I2C2=0x40005800, CAN=0x40006400,
                CRS=0x40006C00, PWR=0x40007000, DAC1=0x40007400, CEC=0x40007800,
                SYSCFG=0x40010000, EXTI=0x40010400, USART6=0x40011400, USART7=0x40011800,
                USART8=0x40011C00, ADC1=0x40012400, TIM1=0x40012C00, SPI1=0x40013000,
                USART1=0x40013800, TIM15=0x40014000, TIM16=0x40014400, TIM17=0x40014800,
                DBGMCU=0x40015800, DMA1=0x40020000, DMA1_Channel1=0x40020008,
                DMA2=0x40020400, RCC=0x40021000, FLASH=0x40022000, CRC=0x40023000,
                TSC=0x40024000, GPIOA=0x48000000, GPIOB=0x48000400, GPIOC=0x48000800,
                GPIOD=0x48000C00, GPIOE=0x48001000, GPIOF=0x48001400,
                SysTick=0xE000E010, NVIC=0xE000E100, SCB=0xE000ED00)

SUITES = [
    ("stm32f1", F1, F1_BASES),
    ("stm32f0", F0, F0_BASES),
]


def start_ghidra():
    import pyghidra
    pyghidra.start()
    from ghidra.app.util.cparser.C import CParserUtils
    from ghidra.program.model.data import StandAloneDataTypeManager
    from ghidra.util.task import TaskMonitor
    return CParserUtils, StandAloneDataTypeManager, TaskMonitor


def parse(CParserUtils, SADTM, TaskMonitor, header):
    dtm = SADTM("verify_" + os.path.basename(header))
    tx = dtm.startTransaction("parse")
    try:
        res = CParserUtils.parseHeaderFiles(None, [header], [], dtm, TaskMonitor.DUMMY)
        if not res.successful():
            raise AssertionError("C parse of %s failed:\n%s" % (header, res.getFormattedParseMessage(None)))
        msg = str(res.getFormattedParseMessage(None) or "").strip()
        if msg:
            print("  parser messages:", msg)
    finally:
        dtm.endTransaction(tx, True)
    structs = {}
    it = dtm.getAllStructures()
    for s in it:
        comps = {}
        for c in s.getDefinedComponents():
            comps.setdefault(str(c.getFieldName()), (c.getOffset(), c.getLength(), str(c.getDataType().getName())))
        structs[str(s.getName())] = (s.getLength(), comps)
    return dtm, structs


def main():
    CParserUtils, SADTM, TaskMonitor = start_ghidra()
    failures = []

    def check(cond, msg):
        if not cond:
            failures.append(msg)
            print("  FAIL:", msg)

    for stem, expected, bases in SUITES:
        header = os.path.join(HERE, stem + ".h")
        jpath = os.path.join(HERE, "peripherals_%s.json" % stem)
        print("== %s ==" % header)
        dtm, structs = parse(CParserUtils, SADTM, TaskMonitor, header)
        for name in sorted(structs):
            size, comps = structs[name]
            print("  %-30s size=0x%03X  members=%d" % (name, size, len(comps)))
            if VERBOSE:
                for fn, (off, ln, tn) in sorted(comps.items(), key=lambda kv: kv[1][0]):
                    print("      +0x%03X  %-18s %s (%d bytes)" % (off, fn, tn, ln))

        # structure checks
        for tname, (esize, eoffs) in expected.items():
            if tname not in structs:
                check(False, "%s: struct %s missing" % (stem, tname))
                continue
            size, comps = structs[tname]
            check(size == esize, "%s: sizeof(%s)=0x%X, expected 0x%X" % (stem, tname, size, esize))
            for m, eo in eoffs.items():
                if m not in comps:
                    check(False, "%s.%s: member %s missing" % (stem, tname, m))
                else:
                    check(comps[m][0] == eo, "%s.%s.%s at 0x%X, expected 0x%X" % (stem, tname, m, comps[m][0], eo))
        extra = set(structs) - set(expected)
        check(not extra, "%s: structs with no expected-table entry: %s" % (stem, sorted(extra)))

        # JSON checks
        items = json.load(open(jpath))
        names = [i["name"] for i in items]
        check(len(names) == len(set(names)), "%s: duplicate peripheral names in JSON" % stem)
        by_name = {i["name"]: i for i in items}
        for i in items:
            for k in ("name", "base", "size", "type", "description"):
                check(k in i, "%s: %s lacks key %s" % (stem, i.get("name"), k))
            check(isinstance(i["base"], int) and isinstance(i["size"], int),
                  "%s: %s base/size must be ints" % (stem, i["name"]))
            t = i["type"]
            if t is not None:
                check(t in structs, "%s: JSON %s uses unknown type %s" % (stem, i["name"], t))
                if t in structs:
                    check(structs[t][0] == i["size"],
                          "%s: JSON %s size 0x%X != sizeof(%s)=0x%X" % (stem, i["name"], i["size"], t, structs[t][0]))
        for n, b in bases.items():
            check(n in by_name, "%s: JSON missing peripheral %s" % (stem, n))
            if n in by_name:
                check(by_name[n]["base"] == b, "%s: %s base 0x%X, expected 0x%X" % (stem, n, by_name[n]["base"], b))
        # any overlap must be declared via "overlaps"
        srt = sorted(items, key=lambda d: d["base"])
        for a in srt:
            for b in srt:
                if a is not b and a["base"] < b["base"] + b["size"] and b["base"] < a["base"] + a["size"]:
                    check(b["name"] in a.get("overlaps", []),
                          "%s: undeclared overlap %s/%s" % (stem, a["name"], b["name"]))
        print("  %d structs, %d peripherals in JSON" % (len(structs), len(items)))
        dtm.close()

    print()
    if failures:
        print("FAILED: %d problem(s)" % len(failures))
        sys.exit(1)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
