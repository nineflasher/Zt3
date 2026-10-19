#!/usr/bin/env python3
"""Verify the SVD-generated headers/JSON (tools/svd2hw.py) with Ghidra's C parser.

Covers the two chips identified in the scooter firmware (see README.md, "Artery AT32" section):
  at32f415   Artery AT32F415, Cortex-M4F   (VCU and MCU boards)
  stm32g0b1  STM32G0B1, Cortex-M0+         (BMS board)

Run:
    GHIDRA_INSTALL_DIR=/opt/ghidra_12.1.4_PUBLIC /opt/zt3-venv/bin/python verify_artery.py [-v]

For each chip the script
  1. parses <chip>.h with ghidra.app.util.cparser.C.CParserUtils into a throwaway
     StandAloneDataTypeManager and prints every struct's size (and, with -v, every member);
  2. asserts ~30 hand-written struct sizes / member offsets per chip (taken from the vendor
     reference manuals / CMSIS headers, independent of the generator);
  3. cross-checks EVERY register of <chip>_registers.json that is flagged "in_struct" against
     the parsed struct member offset, and every dropped alias against the register it overlaps;
  4. asserts every peripherals_<chip>.json "type" exists, "size" == sizeof(type) (and <= the SVD
     address block unless flagged), names unique, undeclared overlaps absent, base addresses of
     ~50 well-known peripherals right;
  5. checks <chip>_irqs.json / <chip>_core.json (IRQ numbers, vector-table length) and, when the
     firmware images are present, that the reserved (zero) vector slots of the real VCU/MCU/BMS
     images are exactly the reserved slots of the chip description;
  6. runs tools/svd2hw.py --selftest (synthetic SVD with derivedFrom, dim arrays, clusters,
     8/16-bit registers, alias registers, name collisions) and checks the resulting struct.

Exit status is non-zero on any failure.
"""
import glob
import importlib.util
import json
import os
import re
import struct
import sys
import tempfile

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
VERBOSE = "-v" in sys.argv

os.environ.setdefault("GHIDRA_INSTALL_DIR", "/opt/ghidra_12.1.4_PUBLIC")

# --------------------------------------------------------------------------------------
# hand-written expectations: type -> (sizeof or None, {member: byte offset})
# --------------------------------------------------------------------------------------
F415 = {
    "GPIO_Type": (0x1C, dict(CFGLR=0, CFGHR=4, IDT=8, ODT=0xC, SCR=0x10, CLR=0x14, WPR=0x18)),
    "CRM_Type": (None, dict(CTRL=0, CFG=4, CLKINT=8, APB2RST=0xC, APB1RST=0x10, AHBEN=0x14, APB2EN=0x18,
                            APB1EN=0x1C, BPDC=0x20, CTRLSTS=0x24, AHBRST=0x28)),
    "USART_Type": (0x1C, dict(STS=0, DT=4, BAUDR=8, CTRL1=0xC, CTRL2=0x10, CTRL3=0x14, GDIV=0x18)),
    "TMR1_Type": (0x50, dict(CTRL1=0, CTRL2=4, STCTRL=8, IDEN=0xC, ISTS=0x10, SWEVT=0x14, CM1_OUTPUT=0x18,
                             CM2_OUTPUT=0x1C, CCTRL=0x20, CVAL=0x24, DIV=0x28, PR=0x2C, RPR=0x30, C1DT=0x34,
                             C4DT=0x40, BRK=0x44, DMACTRL=0x48, DMADT=0x4C)),
    "TMR2_Type": (0x50, dict(CTRL1=0, CVAL=0x24, DIV=0x28, PR=0x2C, C1DT=0x34, C4DT=0x40, DMADT=0x4C)),
    "ADC1_Type": (0x50, dict(STS=0, CTRL1=4, CTRL2=8, SPT1=0xC, SPT2=0x10, PCDTO1=0x14, VMHB=0x24, VMLB=0x28,
                             OSQ1=0x2C, OSQ2=0x30, OSQ3=0x34, PSQ=0x38, PDT1=0x3C, PDT4=0x48, ODT=0x4C)),
    "DMA_Type": (None, dict(STS=0, CLR=4, C1CTRL=8, C1DTCNT=0xC, C1PADDR=0x10, C1MADDR=0x14, C2CTRL=0x1C,
                            C7CTRL=0x80, C7MADDR=0x8C)),
    "EXINT_Type": (0x18, dict(INTEN=0, EVTEN=4, POLCFG1=8, POLCFG2=0xC, SWTRG=0x10, INTSTS=0x14)),
    "IOMUX_Type": (None, dict(EVTOUT=0, REMAP=4, EXINTC1=8, EXINTC4=0x14, REMAP2=0x1C)),
    "WDT_Type": (0x10, dict(CMD=0, DIV=4, RLD=8, STS=0xC)),
    "WWDT_Type": (0xC, dict(CTRL=0, CFG=4, STS=8)),
    "PWC_Type": (8, dict(CTRL=0, CTRLSTS=4)),
    "SPI_Type": (0x24, dict(CTRL1=0, CTRL2=4, STS=8, DT=0xC, CPOLY=0x10, RCRC=0x14, TCRC=0x18, I2SCTRL=0x1C,
                            I2SCLK=0x20)),
    "I2C_Type": (0x24, dict(CTRL1=0, CTRL2=4, OADDR1=8, OADDR2=0xC, DT=0x10, STS1=0x14, STS2=0x18, CLKCTRL=0x1C,
                            TMRISE=0x20)),
    "FLASH_Type": (None, dict(PSR=0, UNLOCK=4, USD_UNLOCK=8, STS=0xC, CTRL=0x10, ADDR=0x14, USD=0x1C, EPPS=0x20)),
    "CRC_Type": (None, dict(DT=0, CDT=4, CTRL=8, IDT=0x10)),
    "DEBUG_Type": (8, dict(DEBUG_IDCODE=0, CTRL=4)),
    "CAN1_Type": (0x2B0, dict(MCTRL=0, MSTS=4, TSTS=8, RF0=0xC, RF1=0x10, INTEN=0x14, ESTS=0x18, BTMG=0x1C,
                              TMI0=0x180, TMC0=0x184, TMDTL0=0x188, TMDTH0=0x18C, TMI2=0x1A0, RFI0=0x1B0,
                              RFI1=0x1C0, FCTRL=0x200, FMCFG=0x204, FBWCFG=0x20C, FRF=0x214, FACFG=0x21C,
                              F0FB1=0x240, F1FB1=0x248)),
    "ERTC_Type": (None, dict(TIME=0, DATE=4, CTRL=8, STS=0xC, DIV=0x10, WAT=0x14, WP=0x24, TAMP=0x40,
                             BPR1DT=0x50)),
    "SDIO1_Type": (None, dict(POWER=0, CLKCTRL=4, ARG=8, CMD=0xC, STS=0x34, INTEN=0x3C)),
    # Cortex-M4F core
    "SCnSCB_Type": (0xC, dict(ICTR=4, ACTLR=8)),
    "SysTick_Type": (0x10, dict(CTRL=0, LOAD=4, VAL=8, CALIB=0xC)),
    "NVIC_Type": (0xE04, dict(ISER=0, ICER=0x80, ISPR=0x100, ICPR=0x180, IABR=0x200, IP=0x300, STIR=0xE00)),
    "SCB_Type": (0x8C, dict(CPUID=0, ICSR=4, VTOR=8, AIRCR=0xC, SCR=0x10, CCR=0x14, SHP=0x18, SHCSR=0x24,
                            CFSR=0x28, HFSR=0x2C, DFSR=0x30, MMFAR=0x34, BFAR=0x38, AFSR=0x3C, CPACR=0x88)),
    "MPU_Type": (0x2C, dict(TYPE=0, CTRL=4, RNR=8, RBAR=0xC, RASR=0x10, RBAR_A3=0x24, RASR_A3=0x28)),
    "FPU_Type": (0x18, dict(FPCCR=4, FPCAR=8, FPDSCR=0xC, MVFR0=0x10, MVFR1=0x14)),
    "ITM_Type": (0x1000, dict(PORT=0, TER=0xE00, TPR=0xE40, TCR=0xE80, LAR=0xFB0, LSR=0xFB4, CID3=0xFFC)),
    "DWT_Type": (0x5C, dict(CTRL=0, CYCCNT=4, CPICNT=8, EXCCNT=0xC, SLEEPCNT=0x10, LSUCNT=0x14, FOLDCNT=0x18,
                            PCSR=0x1C, COMP0=0x20, FUNCTION3=0x58)),
    "TPI_Type": (0xFD0, dict(SSPSR=0, CSPSR=4, ACPR=0x10, SPPR=0xF0, FFSR=0x300, FFCR=0x304)),
    "CoreDebug_Type": (0x10, dict(DHCSR=0, DCRSR=4, DCRDR=8, DEMCR=0xC)),
}
F415_BASES = dict(
    TMR2=0x40000000, TMR3=0x40000400, TMR4=0x40000800, TMR5=0x40000C00, CMP=0x40002400, ERTC=0x40002800,
    WWDT=0x40002C00, WDT=0x40003000, SPI2=0x40003800, USART2=0x40004400, USART3=0x40004800, UART4=0x40004C00,
    UART5=0x40005000, I2C1=0x40005400, I2C2=0x40005800, CAN1=0x40006400, PWC=0x40007000, IOMUX=0x40010000,
    EXINT=0x40010400, GPIOA=0x40010800, GPIOB=0x40010C00, GPIOC=0x40011000, GPIOD=0x40011400, GPIOF=0x40011C00,
    ADC1=0x40012400, TMR1=0x40012C00, SPI1=0x40013000, USART1=0x40013800, TMR9=0x40014C00, TMR10=0x40015000,
    TMR11=0x40015400, ACC=0x40015800, SDIO1=0x40018000, DMA1=0x40020000, DMA2=0x40020400, CRM=0x40021000,
    FLASH=0x40022000, CRC=0x40023000, USB_OTG_GLOBAL=0x50000000, USB_OTG_HOST=0x50000400,
    USB_OTG_DEVICE=0x50000800, DEBUG=0xE0042000, SysTick=0xE000E010, NVIC=0xE000E100, SCB=0xE000ED00,
    SCnSCB=0xE000E000, MPU=0xE000ED90, FPU=0xE000EF30, DWT=0xE0001000, ITM=0xE0000000)
F415_TYPES = dict(GPIOB="GPIO_Type", GPIOF="GPIO_Type", USART3="USART_Type", UART5="USART_Type",
                  I2C2="I2C_Type", SPI2="SPI_Type", DMA2="DMA_Type", TMR3="TMR2_Type", TMR4="TMR2_Type",
                  TMR5="TMR2_Type", TMR1="TMR1_Type", ADC1="ADC1_Type")
F415_IRQS = dict(WWDT=0, PVM=1, TAMP_STAMP=2, ERTC_WKUP=3, FLASH=4, CRM=5, EXINT0=6, EXINT4=10,
                 DMA1_Channel1=11, DMA1_Channel7=17, ADC1=18, CAN1_TX=19, CAN1_RX0=20, CAN1_RX1=21, CAN1_SE=22,
                 EXINT9_5=23, TMR1_BRK_TMR9=24, TMR1_OVF_TMR10=25, TMR1_TRG_HALL_TMR11=26, TMR1_CH=27,
                 TMR2_GLOBAL=28, TMR3_GLOBAL=29, TMR4_GLOBAL=30, I2C1_EVT=31, SPI1=35, USART1=37, USART2=38,
                 USART3=39, EXINT15_10=40, ERTCAlarm=41, OTGFS1_WKUP=42, SDIO1=49, TMR5_GLOBAL=50, UART4=52,
                 UART5=53, DMA2_Channel1=56, DMA2_Channel4_5=59, OTGFS1=67, CMP1=70, CMP2=71,
                 DMA2_Channel6_7=75)

G0 = {
    "GPIO_Type": (0x2C, dict(MODER=0, OTYPER=4, OSPEEDR=8, PUPDR=0xC, IDR=0x10, ODR=0x14, BSRR=0x18, LCKR=0x1C,
                             AFRL=0x20, AFRH=0x24, BRR=0x28)),
    "RCC_Type": (0x64, dict(CR=0, ICSCR=4, CFGR=8, PLLCFGR=0xC, CRRCR=0x14, CIER=0x18, CIFR=0x1C, CICR=0x20,
                            IOPRSTR=0x24, AHBRSTR=0x28, APBRSTR1=0x2C, APBRSTR2=0x30, IOPENR=0x34, AHBENR=0x38,
                            APBENR1=0x3C, APBENR2=0x40, IOPSMENR=0x44, CCIPR=0x54, BDCR=0x5C, CSR=0x60)),
    "USART_Type": (0x30, dict(CR1_FIFO_ENABLED=0, CR2=4, CR3=8, BRR=0xC, GTPR=0x10, RTOR=0x14, RQR=0x18,
                              ISR_FIFO_ENABLED=0x1C, ICR=0x20, RDR=0x24, TDR=0x28, PRESC=0x2C)),
    "TIM1_Type": (0x6C, dict(CR1=0, CR2=4, SMCR=8, DIER=0xC, SR=0x10, EGR=0x14, CCMR1_Output=0x18,
                             CCMR2_Output=0x1C, CCER=0x20, CNT=0x24, PSC=0x28, ARR=0x2C, RCR=0x30, CCR1=0x34,
                             CCR4=0x40, BDTR=0x44, DCR=0x48, DMAR=0x4C, AF1=0x60, AF2=0x64, TISEL=0x68)),
    "TIM6_Type": (0x30, dict(CR1=0, CR2=4, DIER=0xC, SR=0x10, EGR=0x14, CNT=0x24, PSC=0x28, ARR=0x2C)),
    "ADC_Type": (0x30C, dict(ISR=0, IER=4, CR=8, CFGR1=0xC, CFGR2=0x10, SMPR=0x14, AWD1TR=0x20, AWD2TR=0x24,
                             CHSELR=0x28, AWD3TR=0x2C, DR=0x40, AWD2CR=0xA0, AWD3CR=0xA4, CALFACT=0xB4,
                             CCR=0x308)),
    "EXTI_Type": (None, dict(RTSR1=0, FTSR1=4, SWIER1=8, RPR1=0xC, FPR1=0x10, RTSR2=0x28, EXTICR1=0x60,
                             EXTICR4=0x6C, IMR1=0x80, EMR1=0x84, IMR2=0x90)),
    "I2C_Type": (0x2C, dict(CR1=0, CR2=4, OAR1=8, OAR2=0xC, TIMINGR=0x10, TIMEOUTR=0x14, ISR=0x18, ICR=0x1C,
                            PECR=0x20, RXDR=0x24, TXDR=0x28)),
    "FLASH_Type": (None, dict(ACR=0, KEYR=8, OPTKEYR=0xC, SR=0x10, CR=0x14, ECCR=0x18, OPTR=0x20)),
    "SYSCFG_Type": (0x100, dict(CFGR1=0, CFGR2=0x18, ITLINE0=0x80)),
    "RTC_Type": (None, dict(TR=0, DR=4, SSR=8, ICSR=0xC, PRER=0x10, WUTR=0x14, CR=0x18, WPR=0x24, CALR=0x28,
                            ALRMAR=0x40)),
    "FDCAN_Type": (0x104, dict(CREL=0, ENDN=4, DBTP=0xC, TEST=0x10, RWD=0x14, CCCR=0x18, NBTP=0x1C, TSCC=0x20,
                               IR=0x50, IE=0x54, ILE=0x5C)),
    "DBG_Type": (0x10, dict(IDCODE=0, CR=4, APB_FZ1=8, APB_FZ2=0xC)),
    "IWDG_Type": (0x14, dict(KR=0, PR=4, RLR=8, SR=0xC, WINR=0x10)),
    "WWDG_Type": (0xC, dict(CR=0, CFR=4, SR=8)),
    "PWR_Type": (None, dict(CR1=0, CR2=4, CR3=8, CR4=0xC, SR1=0x10, SR2=0x14, SCR=0x18, PUCRA=0x20)),
    "CRC_Type": (None, dict(DR=0, IDR=4, CR=8, INIT=0x10, POL=0x14)),
    "DMA_Type": (None, dict(ISR=0, IFCR=4, CCR1=8, CNDTR1=0xC, CPAR1=0x10, CMAR1=0x14, CCR2=0x1C)),
    "SPI_Type": (0x22, dict(CR1=0, CR2=4, SR=8, DR=0xC, CRCPR=0x10, RXCRCR=0x14, TXCRCR=0x18, I2SCFGR=0x1C,
                            I2SPR=0x20)),
    "DMAMUX_Type": (None, dict(C0CR=0, C1CR=4, C6CR=0x18)),
    # Cortex-M0+ core
    "SysTick_Type": (0x10, dict(CTRL=0, LOAD=4, VAL=8, CALIB=0xC)),
    "NVIC_Type": (0x320, dict(ISER=0, ICER=0x80, ISPR=0x100, ICPR=0x180, IP=0x300)),
    "SCB_Type": (0x28, dict(CPUID=0, ICSR=4, VTOR=8, AIRCR=0xC, SCR=0x10, CCR=0x14, SHP=0x1C, SHCSR=0x24)),
    "MPU_Type": (0x14, dict(TYPE=0, CTRL=4, RNR=8, RBAR=0xC, RASR=0x10)),
}
G0_BASES = dict(
    TIM2=0x40000000, TIM3=0x40000400, TIM4=0x40000800, TIM6=0x40001000, TIM7=0x40001400, TIM14=0x40002000,
    RTC=0x40002800, WWDG=0x40002C00, IWDG=0x40003000, SPI2=0x40003800, SPI3=0x40003C00, USART2=0x40004400,
    USART3=0x40004800, USART4=0x40004C00, USART5=0x40005000, I2C1=0x40005400, I2C2=0x40005800, USB=0x40005C00,
    FDCAN1=0x40006400, FDCAN2=0x40006800, PWR=0x40007000, DAC=0x40007400, HDMI_CEC=0x40007800,
    LPTIM1=0x40007C00, LPUART1=0x40008000, LPUART2=0x40008400, I2C3=0x40008800, LPTIM2=0x40009400,
    UCPD1=0x4000A000, UCPD2=0x4000A400, TAMP=0x4000B000, SYSCFG=0x40010000, VREFBUF=0x40010030,
    COMP=0x40010200, ADC=0x40012400, TIM1=0x40012C00, SPI1=0x40013000, USART1=0x40013800, USART6=0x40013C00,
    TIM15=0x40014000, TIM16=0x40014400, TIM17=0x40014800, DBG=0x40015800, DMA1=0x40020000, DMA2=0x40020400,
    DMAMUX=0x40020800, RCC=0x40021000, EXTI=0x40021800, FLASH=0x40022000, CRC=0x40023000, GPIOA=0x50000000,
    GPIOB=0x50000400, GPIOC=0x50000800, GPIOD=0x50000C00, GPIOE=0x50001000, GPIOF=0x50001400,
    SysTick=0xE000E010, NVIC=0xE000E100, SCB=0xE000ED00, MPU=0xE000ED90, SRAMCAN_FDCAN1=0x4000B400,
    SRAMCAN_FDCAN2=0x4000B750, UID=0x1FFF7590, FLASHSIZE=0x1FFF75E0)
G0_TYPES = dict(GPIOB="GPIO_Type", GPIOF="GPIO_Type", USART6="USART_Type", USART1="USART_Type",
                TIM3="TIM2_Type", TIM4="TIM2_Type", TIM7="TIM6_Type", TIM17="TIM16_Type", FDCAN2="FDCAN_Type",
                I2C3="I2C_Type", SPI3="SPI_Type", DMA2="DMA_Type", LPUART2="LPUART_Type")
G0_IRQS = dict(WWDG=0, PVD_VDDIO2=1, RTC_TAMP=2, FLASH=3, RCC_CRS=4, EXTI0_1=5, EXTI2_3=6, EXTI4_15=7,
               USB_UCPD1_2=8, DMA1_Channel1=9, DMA1_Channel2_3=10, DMA1_Ch4_7_DMA2_Ch1_5_DMAMUX1_OVR=11,
               ADC1_COMP=12, TIM1_BRK_UP_TRG_COM=13, TIM1_CC=14, TIM2=15, TIM3_TIM4=16, TIM6_DAC_LPTIM1=17,
               TIM7_LPTIM2=18, TIM14=19, TIM15=20, TIM16_FDCAN_IT0=21, TIM17_FDCAN_IT1=22, I2C1=23, I2C2_3=24,
               SPI1=25, SPI2_3=26, USART1=27, USART2_LPUART2=28, USART3_4_5_6_LPUART1=29, CEC=30)

SUITES = [
    # stem, expected struct table, expected bases, expected instance->type, expected irqs, vector slots,
    # firmware images whose reserved (zero) slots must equal the chip's, expected struct count lower bound
    dict(stem="at32f415", expected=F415, bases=F415_BASES, types=F415_TYPES, irqs=F415_IRQS, slots=92,
         images="firmware/vcu/*.bin firmware/mcu/*.bin"),
    dict(stem="stm32g0b1", expected=G0, bases=G0_BASES, types=G0_TYPES, irqs=G0_IRQS, slots=47,
         images="firmware/bms/*.bin"),
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
    for s in dtm.getAllStructures():
        comps = {}
        for c in s.getDefinedComponents():
            comps.setdefault(str(c.getFieldName()), (c.getOffset(), c.getLength(), str(c.getDataType().getName())))
        structs[str(s.getName())] = (s.getLength(), comps)
    return dtm, structs


def load_svd2hw():
    spec = importlib.util.spec_from_file_location("svd2hw", os.path.join(REPO, "tools", "svd2hw.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fw_zero_irq_slots(path, nslots):
    d = open(path, "rb").read()
    w = struct.unpack("<%dI" % (len(d) // 4), d)
    return [i - 16 for i in range(16, nslots) if w[i] == 0], [i for i in range(1, 16) if w[i] == 0]


def main():
    CParserUtils, SADTM, TaskMonitor = start_ghidra()
    failures = []
    ncheck = [0]

    def check(cond, msg):
        ncheck[0] += 1
        if not cond:
            failures.append(msg)
            print("  FAIL:", msg)

    for S in SUITES:
        stem = S["stem"]
        header = os.path.join(HERE, stem + ".h")
        print("== %s ==" % header)
        dtm, structs = parse(CParserUtils, SADTM, TaskMonitor, header)
        for name in sorted(structs):
            size, comps = structs[name]
            print("  %-26s size=0x%03X  members=%d" % (name, size, len(comps)))
            if VERBOSE:
                for fn, (off, ln, tn) in sorted(comps.items(), key=lambda kv: kv[1][0]):
                    print("      +0x%03X  %-22s %s (%d bytes)" % (off, fn, tn, ln))

        # ---- 2. hand-written struct expectations
        nspot = 0
        for tname, (esize, eoffs) in S["expected"].items():
            if tname not in structs:
                check(False, "%s: struct %s missing" % (stem, tname))
                continue
            size, comps = structs[tname]
            if esize is not None:
                check(size == esize, "%s: sizeof(%s)=0x%X, expected 0x%X" % (stem, tname, size, esize))
                nspot += 1
            for m, eo in eoffs.items():
                nspot += 1
                if m not in comps:
                    check(False, "%s.%s: member %s missing" % (stem, tname, m))
                else:
                    check(comps[m][0] == eo, "%s.%s.%s at 0x%X, expected 0x%X" % (stem, tname, m, comps[m][0], eo))
        print("  %d hand-written size/offset spot checks" % nspot)
        check(nspot >= 30, "%s: fewer than 30 spot checks" % stem)

        # ---- 3. every register of <chip>_registers.json vs the parsed struct
        regs = json.load(open(os.path.join(HERE, "%s_registers.json" % stem)))
        items = json.load(open(os.path.join(HERE, "peripherals_%s.json" % stem)))
        by_name = {i["name"]: i for i in items}
        nreg = nalias = 0
        for pname, doc in regs.items():
            if doc.get("core"):
                continue
            t = doc["type"]
            check(t in structs, "%s: registers[%s] type %s not in header" % (stem, pname, t))
            if t not in structs:
                continue
            check(by_name.get(pname, {}).get("type") == t, "%s: %s type differs between JSONs" % (stem, pname))
            check(doc["base"] == by_name.get(pname, {}).get("base"), "%s: %s base differs between JSONs" % (stem, pname))
            size, comps = structs[t]
            kept = []
            for r in doc["registers"]:
                if r["in_struct"]:
                    m = re.fullmatch(r"(\w+?)(?:\[(\d+)\])?", r["member"])
                    mem, k = m.group(1), int(m.group(2) or 0)
                    if mem not in comps:
                        check(False, "%s.%s: member %s (%s) missing" % (stem, pname, mem, r["name"]))
                        continue
                    off, ln, tn = comps[mem]
                    eo = off + k * (r["size"] // 8)
                    nreg += 1
                    check(eo == r["offset"], "%s.%s.%s: struct offset 0x%X != SVD offset 0x%X" % (
                        stem, pname, r["member"], eo, r["offset"]))
                    check(r["offset"] + r["size"] // 8 <= size, "%s.%s.%s exceeds struct" % (stem, pname, r["name"]))
                    kept.append((r["offset"], r["offset"] + r["size"] // 8, r["name"]))
            for r in doc["registers"]:
                if not r["in_struct"]:
                    nalias += 1
                    ok = any(r["offset"] < ke and ko < r["offset"] + r["size"] // 8 for ko, ke, _ in kept)
                    check(ok and r.get("alias_of"), "%s.%s: dropped register %s overlaps no kept register" % (
                        stem, pname, r["name"]))
        print("  %d registers cross-checked against struct members, %d alias registers (not in struct) checked" % (
            nreg, nalias))

        # ---- 4. peripherals JSON
        names = [i["name"] for i in items]
        check(len(names) == len(set(names)), "%s: duplicate peripheral names in JSON" % stem)
        for i in items:
            for k in ("name", "base", "size", "type", "description"):
                check(k in i, "%s: %s lacks key %s" % (stem, i.get("name"), k))
            check(isinstance(i["base"], int) and isinstance(i["size"], int), "%s: %s base/size must be ints" % (stem, i["name"]))
            t = i["type"]
            if t is not None:
                check(t in structs, "%s: JSON %s uses unknown type %s" % (stem, i["name"], t))
                if t in structs:
                    check(structs[t][0] == i["size"], "%s: JSON %s size 0x%X != sizeof(%s)=0x%X" % (
                        stem, i["name"], i["size"], t, structs[t][0]))
                    if i.get("source") == "svd" and i.get("block"):
                        check(i["size"] <= i["block"] or i.get("block_overflow"),
                              "%s: %s struct 0x%X exceeds SVD address block 0x%X" % (stem, i["name"], i["size"], i["block"]))
                        check(not i.get("block_overflow"), "%s: %s struct exceeds its SVD address block" % (stem, i["name"]))
        used = set(i["type"] for i in items if i["type"])
        check(used == set(structs), "%s: structs without instance / instances without struct: %s" % (
            stem, sorted(used ^ set(structs))))
        for n, b in S["bases"].items():
            check(n in by_name, "%s: JSON missing peripheral %s" % (stem, n))
            if n in by_name:
                check(by_name[n]["base"] == b, "%s: %s base 0x%X, expected 0x%X" % (stem, n, by_name[n]["base"], b))
        for n, t in S["types"].items():
            check(by_name.get(n, {}).get("type") == t, "%s: %s type %s, expected %s" % (stem, n, by_name.get(n, {}).get("type"), t))
        srt = sorted(items, key=lambda d: d["base"])
        for a in srt:
            for b in srt:
                if a is not b and a["size"] > 0 and b["size"] > 0 and a["base"] < b["base"] + b["size"] and b["base"] < a["base"] + a["size"]:
                    check(b["name"] in a.get("overlaps", []), "%s: undeclared overlap %s/%s" % (stem, a["name"], b["name"]))
        for a in items:
            for o in a.get("overlaps", []):
                check(a["name"] in by_name[o].get("overlaps", []), "%s: overlap %s->%s not symmetric" % (stem, a["name"], o))
        print("  %d structs, %d peripherals in JSON, %d well-known bases checked" % (len(structs), len(items), len(S["bases"])))

        # ---- 5. IRQs / core / firmware vector table
        irqs = json.load(open(os.path.join(HERE, "%s_irqs.json" % stem)))
        core = json.load(open(os.path.join(HERE, "%s_core.json" % stem)))
        nums = [i["number"] for i in irqs]
        check(nums == sorted(set(nums)), "%s: IRQ numbers not unique/sorted" % stem)
        iby = dict((i["name"], i["number"]) for i in irqs)
        for n, v in S["irqs"].items():
            check(iby.get(n) == v, "%s: IRQ %s = %s, expected %d" % (stem, n, iby.get(n), v))
        check(core["vector_table_slots"] == S["slots"], "%s: vector_table_slots %s != %d" % (stem, core["vector_table_slots"], S["slots"]))
        check(len(core["vectors"]) == S["slots"], "%s: vectors list length" % stem)
        for i in irqs:
            if "startup" in i["sources"] and not i.get("startup_reserved"):
                check(core["vectors"][i["number"] + 16]["name"] == i["handler"], "%s: vector slot name for IRQ %d" % (stem, i["number"]))
        print("  %d IRQs; vector table %d slots; %d reserved IRQ slots" % (len(irqs), core["vector_table_slots"], len(core["reserved_irq_numbers"])))
        imgs = sorted(sum((glob.glob(os.path.join(REPO, p)) for p in S["images"].split()), []))
        if not imgs:
            print("  (no firmware images found, skipping the vector-table cross-check)")
        for img in imgs:
            zero_irq, zero_core = fw_zero_irq_slots(img, S["slots"])
            check(zero_irq == core["reserved_irq_numbers"], "%s: %s zero IRQ slots %s != reserved %s" % (
                stem, os.path.basename(img), zero_irq, core["reserved_irq_numbers"]))
            exp_core = [v["slot"] for v in core["vectors"][1:16] if v["reserved"]]
            check(zero_core == exp_core, "%s: %s zero core slots %s != reserved %s" % (stem, os.path.basename(img), zero_core, exp_core))
        if imgs:
            print("  %d firmware image(s): reserved vector slots identical to %s startup file" % (len(imgs), stem))
        dtm.close()

    # ---- 6. converter self-test
    print("== svd2hw.py --selftest ==")
    mod = load_svd2hw()
    tmpdir = tempfile.TemporaryDirectory(prefix="svd2hw_selftest_")
    tmp = tmpdir.name
    import contextlib
    import io
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        mod.main(["--selftest", "--out-dir", tmp])
    dtm, structs = parse(CParserUtils, SADTM, TaskMonitor, os.path.join(tmp, "selftest.h"))
    exp = {
        # "FOO_" is stripped from the member names: 10 of the 14 non-alternate registers carry it (>= 70 %)
        "FOO_Type": (0x94, dict(CR=0, B8=4, H16=6, ARR=0x10, X0=0x20, X1=0x28, CH0_CTL=0x40,
                                CH1_CNT=0x54, OUT=0x80, TAIL16=0x90)),
        "BAR_Type": (0xC, dict(SR=0, SR_8=8)),
    }
    for t, (es, eo) in exp.items():
        check(t in structs, "selftest: %s missing" % t)
        if t in structs:
            check(structs[t][0] == es, "selftest: sizeof(%s)=0x%X expected 0x%X" % (t, structs[t][0], es))
            for m, o in eo.items():
                check(m in structs[t][1] and structs[t][1][m][0] == o, "selftest: %s.%s offset" % (t, m))
    check(structs["FOO_Type"][1]["ARR"][1] == 12, "selftest: ARR should be uint32_t[3]")
    check(structs["FOO_Type"][1]["B8"][1] == 1 and structs["FOO_Type"][1]["H16"][1] == 2, "selftest: 8/16-bit member widths")
    sp = json.load(open(os.path.join(tmp, "peripherals_selftest.json")))
    sd = dict((i["name"], i) for i in sp)
    check(sd["FOO2"]["type"] == "FOO_Type" and sd["FOO2"]["derivedFrom"] == "FOO1" and sd["FOO2"]["base"] == 0x40000400,
          "selftest: derivedFrom instance")
    sr = json.load(open(os.path.join(tmp, "selftest_registers.json")))
    alias = [r for r in sr["FOO2"]["registers"] if r["name"] == "FOO_IN"][0]
    check(alias["in_struct"] is False and alias["alias_of"] == "FOO_OUT" and alias["alternate_of"] == "FOO_OUT", "selftest: alias register recorded")
    dtm.close()
    tmpdir.cleanup()
    print("  selftest struct parsed and checked")

    print()
    print("%d checks" % ncheck[0])
    if failures:
        print("FAILED: %d problem(s)" % len(failures))
        sys.exit(1)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
