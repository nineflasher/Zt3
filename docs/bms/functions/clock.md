# BMS - `clock` functions

5 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`HAL_RCC_EnableCSS`](#hal_rcc_enablecss) | 0x08002334 | Sets RCC.CR.CSSON to enable the clock security system for HSE failure detection |
| [`LL_APB1_GRP1_EnableClock`](#ll_apb1_grp1_enableclock) | 0x08002AF0 | Sets bits in RCC APBENR1 to enable APB1 group 1 peripheral clocks |
| [`LL_IOP_GRP1_EnableClock`](#ll_iop_grp1_enableclock) | 0x08002CF0 | Sets bits in RCC IOPENR to enable GPIO port clocks |
| [`rcc_hclk_divide`](#rcc_hclk_divide) | 0x08003474 | Divide a clock frequency by the AHB (HCLK) prescaler read from RCC_CFGR |
| [`rcc_pclk_divide`](#rcc_pclk_divide) | 0x08003494 | Divide a clock frequency by the APB (PCLK) prescaler read from RCC_CFGR |

## HAL_RCC_EnableCSS

**Sets RCC.CR.CSSON to enable the clock security system for HSE failure detection**

Read-modify-write that sets RCC CR bit 19 (CSSON, clock security system enable) at 0x40021000 and leaves all other bits alone. With CSS on, a detected HSE failure switches the system clock to the internal oscillator and reports the failure through the NMI vector. It takes no arguments and returns nothing.

- Addresses by version: 4130: 0x08002334, 4139: 0x08002334, 4148: 0x08002334, 4168: 0x08002334
- Peripheral registers: `RCC.CR` (ARW)
- Called by: `bms_4168_08003440`, `bms_4168_0800a23c`
- Confidence: high

## LL_APB1_GRP1_EnableClock

**Sets bits in RCC APBENR1 to enable APB1 group 1 peripheral clocks**

ORs the argument into RCC APBENR1 (0x4002103C) by read-modify-write and then reads the register back, which is the LL driver's dummy read that makes sure the clock write has taken effect before the caller touches the peripheral. The mask uses the LL_APB1_GRP1_PERIPH bit positions; for example bit 10 is the RTC APB clock and bit 28 is PWR. Existing enable bits are kept.

| Parameter | Type | Description |
|---|---|---|
| `periphs` | `u32` | APBENR1 bit mask of peripherals to enable |

- Addresses by version: 4130: 0x08002AF0, 4139: 0x08002AF0, 4148: 0x08002AF0, 4168: 0x08002AF0
- Peripheral registers: `RCC.APBENR1` (RW)
- Called by: `bms_4168_0800a3e8`
- Confidence: high

## LL_IOP_GRP1_EnableClock

**Sets bits in RCC IOPENR to enable GPIO port clocks**

ORs the argument into RCC IOPENR (0x40021034) by read-modify-write and then reads it back, as the LL driver does, so the clock is running before the port is used. Bit n of the argument enables port n. Existing enable bits are kept.

| Parameter | Type | Description |
|---|---|---|
| `periphs` | `u32` | IOPENR bit mask of ports to enable |

- Addresses by version: 4130: 0x08002CF0, 4139: 0x08002CF0, 4148: 0x08002CF0, 4168: 0x08002CF0
- Peripheral registers: `RCC.IOPENR` (RW)
- Called by: `bms_i2c_bb_bus_init`
- Confidence: high

## rcc_hclk_divide

**Divide a clock frequency by the AHB (HCLK) prescaler read from RCC_CFGR**

Reads RCC.CFGR (0x40021008) and takes the HPRE field (bits 7:4) as a 4-byte-stride index into a 16-entry table in flash at 0x08010a54. Each table entry is the right-shift count for one AHB prescaler setting (0 for undivided, 1 for /2, 2 for /4, ... 9 for /512). The function returns its argument shifted right by that count, which is the input divided by the AHB prescaler. Used in clock-tree arithmetic to derive HCLK from SYSCLK; no writes and no side effects.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | input frequency to divide, e.g. SYSCLK in Hz |

**Returns** `u32`: param_1 divided by the AHB prescaler

**Notes:** Table contents are inferred from the STM32 HAL AHBPrescTable layout, not read from the image. The table is read at a 4-byte stride as decompiled; the element width is unverified.

- Addresses by version: 4130: 0x08003474, 4139: 0x08003474, 4148: 0x08003474, 4168: 0x08003474
- Peripheral registers: `RCC.CFGR` (R)
- Called by: `bms_4168_08002d0c`, `bms_4168_08002d24`
- Confidence: medium

## rcc_pclk_divide

**Divide a clock frequency by the APB (PCLK) prescaler read from RCC_CFGR**

Reads RCC.CFGR (0x40021008), masks it to 15 bits and takes bits 14:12 as the index of a 8-entry shift-count table at 0x08010a94 (4-byte stride), i.e. the APB prescaler selection. The function returns its argument shifted right by the selected count, which is the input divided by the APB prescaler. No writes and no side effects. Companion of rcc_hclk_divide.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | input frequency to divide, e.g. HCLK in Hz |

**Returns** `u32`: param_1 divided by the APB prescaler

**Notes:** The index uses CFGR bits 14:12. In the STM32G0 reference manual the APB prescaler PPRE field is at bits 10:8, so either the field position or the decompiled shift needs checking against the RM before the exact divider is trusted. Table location and element width are inferred the same way as in rcc_hclk_divide.

- Addresses by version: 4130: 0x08003494, 4139: 0x08003494, 4148: 0x08003494, 4168: 0x08003494
- Peripheral registers: `RCC.CFGR` (R)
- Called by: `bms_4168_08002d0c`, `bms_4168_08002d24`
- Confidence: medium
