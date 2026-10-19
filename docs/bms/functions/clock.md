# BMS - `clock` functions

12 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`HAL_RCC_EnableCSS`](#hal_rcc_enablecss) | 0x08002334 | Sets RCC.CR.CSSON to enable the clock security system for HSE failure detection |
| [`HAL_RCC_GetSysClockFreq`](#hal_rcc_getsysclockfreq) | 0x080034B4 | Computes SYSCLK from RCC CFGR SWS: the PLL output, or HSI16 divided by HSIDIV |
| [`LL_APB1_GRP1_EnableClock`](#ll_apb1_grp1_enableclock) | 0x08002AF0 | Sets bits in RCC APBENR1 to enable APB1 group 1 peripheral clocks |
| [`LL_IOP_GRP1_EnableClock`](#ll_iop_grp1_enableclock) | 0x08002CF0 | Sets bits in RCC IOPENR to enable GPIO port clocks |
| [`bms_css_enable_sram_parity_lock`](#bms_css_enable_sram_parity_lock) | 0x0800A23C | Enable the clock security system and set the SRAM parity lock in SYSCFG_CFGR2 |
| [`bms_rcc_get_clock_freqs`](#bms_rcc_get_clock_freqs) | 0x08002D0C | Fills a three-word record with SYSCLK, HCLK and PCLK frequencies in Hz |
| [`bms_rcc_periph_clk_get`](#bms_rcc_periph_clk_get) | 0x08002D24 | Returns a peripheral's kernel clock selected from a CCIPR field: SYSCLK, HSI16, LSE or PCLK |
| [`bms_sysclk_hse_pll_bringup`](#bms_sysclk_hse_pll_bringup) | 0x0800A130 | Start HSE and PLL as SYSCLK with HSI16 fallback, record 16 MHz, reset on failure |
| [`bms_sysclk_hsi16_switch`](#bms_sysclk_hsi16_switch) | 0x0800A2E0 | Switch SYSCLK to HSI16 with APB prescaler cleared, record 16 MHz, reset on failure |
| [`bms_system_clock_setup`](#bms_system_clock_setup) | 0x080086D4 | Set the vector table, bring up SYSCLK from HSE/PLL, enable CSS and set the SysTick base |
| [`rcc_hclk_divide`](#rcc_hclk_divide) | 0x08003474 | Divide a clock frequency by the AHB (HCLK) prescaler read from RCC_CFGR |
| [`rcc_pclk_divide`](#rcc_pclk_divide) | 0x08003494 | Divide a clock frequency by the APB (PCLK) prescaler read from RCC_CFGR |

## HAL_RCC_EnableCSS

**Sets RCC.CR.CSSON to enable the clock security system for HSE failure detection**

Read-modify-write that sets RCC CR bit 19 (CSSON, clock security system enable) at 0x40021000 and leaves all other bits alone. With CSS on, a detected HSE failure switches the system clock to the internal oscillator and reports the failure through the NMI vector. It takes no arguments and returns nothing.

- Addresses by version: 4130: 0x08002334, 4139: 0x08002334, 4148: 0x08002334, 4168: 0x08002334
- Peripheral registers: `RCC.CR` (ARW)
- Called by: `RCC_CRS_IRQHandler`, `bms_css_enable_sram_parity_lock`
- Confidence: high

## HAL_RCC_GetSysClockFreq

**Computes SYSCLK from RCC CFGR SWS: the PLL output, or HSI16 divided by HSIDIV**

Reads CFGR SWS (bits 3-5). For SWS 2 (PLL) it computes source * PLLN / (PLLM * PLLR), where the source is HSI16 at 16 MHz unless PLLCFGR source bits are 3 (HSE, assumed 8 MHz), PLLM = PLLCFGR bits 6-4 plus 1, PLLN = PLLCFGR bits 14-8, and PLLR = PLLCFGR bits 31-29 plus 1. For HSI16 (SWS 0 and other values) it returns 16 MHz divided by 2^HSIDIV, where HSIDIV is CR bits 13-11. For SWS 1 (HSE) the decompile shows no value being produced, so the result is undefined.

**Returns** `u32`: SYSCLK in Hz

**Notes:** The HSE branch is missing from the decompile, so callers get whatever is in r0 when SWS is 1. HSE is not read anywhere in this packet. The PLL bit positions are as they appear in the decompile and were not checked against the reference manual.

- Addresses by version: 4130: 0x080034B4, 4139: 0x080034B4, 4148: 0x080034B4, 4168: 0x080034B4
- Peripheral registers: `RCC.CR` (AR), `RCC.CFGR` (R), `RCC.PLLCFGR` (R)
- Called by: `bms_rcc_get_clock_freqs`, `bms_rcc_periph_clk_get`
- Calls: `bms_udiv32`
- Confidence: high

## LL_APB1_GRP1_EnableClock

**Sets bits in RCC APBENR1 to enable APB1 group 1 peripheral clocks**

ORs the argument into RCC APBENR1 (0x4002103C) by read-modify-write and then reads the register back, which is the LL driver's dummy read that makes sure the clock write has taken effect before the caller touches the peripheral. The mask uses the LL_APB1_GRP1_PERIPH bit positions; for example bit 10 is the RTC APB clock and bit 28 is PWR. Existing enable bits are kept.

| Parameter | Type | Description |
|---|---|---|
| `periphs` | `u32` | APBENR1 bit mask of peripherals to enable |

- Addresses by version: 4130: 0x08002AF0, 4139: 0x08002AF0, 4148: 0x08002AF0, 4168: 0x08002AF0
- Peripheral registers: `RCC.APBENR1` (RW)
- Called by: `bms_tim6_tim7_start`
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

## bms_css_enable_sram_parity_lock

**Enable the clock security system and set the SRAM parity lock in SYSCFG_CFGR2**

Calls HAL_RCC_EnableCSS (FUN_08002334), which sets RCC.CR.CSSON so that a failed HSE is detected. It then sets bit 1 of SYSCFG_CFGR2 at 0x40010018 by read-modify-write. On STM32G0 that bit is the SRAM parity lock, which can be cleared only by reset, so the setting is permanent once made. The bit meaning is taken from the STM32G0 reference, not from the packet.

**Notes:** The SYSCFG_CFGR2 bit 1 meaning is from the reference manual and was not checked against the SVD in this packet.

- Addresses by version: 4130: 0x080091DC, 4139: 0x080096DC, 4148: 0x08009F28, 4168: 0x0800A23C
- Peripheral registers: `SYSCFG.CFGR1` (A), `SYSCFG.CFGR2` (RW)
- Called by: `bms_4168_080082f0`, `bms_system_clock_setup`
- Calls: `HAL_RCC_EnableCSS`
- Confidence: medium

## bms_rcc_get_clock_freqs

**Fills a three-word record with SYSCLK, HCLK and PCLK frequencies in Hz**

Stores HAL_RCC_GetSysClockFreq (bms_4168_080034b4) in word 0, applies the AHB prescaler (rcc_hclk_divide, bms_4168_08003474) for HCLK in word 1, and applies the APB prescaler (rcc_pclk_divide, bms_4168_08003494) for PCLK in word 2. It has no side effects beyond the output record. Its caller bms_4168_08003140 is outside this packet.

| Parameter | Type | Description |
|---|---|---|
| `out` | `ptr` | param_1, three-word output record: SYSCLK, HCLK, PCLK in Hz |

- Addresses by version: 4130: 0x08002D0C, 4139: 0x08002D0C, 4148: 0x08002D0C, 4168: 0x08002D0C
- Called by: `bms_usart_init_from_config`
- Calls: `rcc_hclk_divide`, `rcc_pclk_divide`, `HAL_RCC_GetSysClockFreq`
- Confidence: high

## bms_rcc_periph_clk_get

**Returns a peripheral's kernel clock selected from a CCIPR field: SYSCLK, HSI16, LSE or PCLK**

Selects one RCC_CCIPR field from the argument: 3 uses bits 1-0, 0xC uses bits 3-2 and 0x30 uses bits 5-4. A field value of 1 gives SYSCLK (bms_4168_080034b4), 2 gives HSI16 at 16 MHz when CR HSIRDY is set (0 otherwise), and 3 gives LSE at 32768 Hz when BDCR LSERDY is set (0 otherwise). Field value 0 or any other value gives the APB clock (bms_4168_08003494). Any argument other than 3, 0xC or 0x30 returns 0.

| Parameter | Type | Description |
|---|---|---|
| `selector` | `u32` | param_1, peripheral selector: 3, 0xC or 0x30 choose a CCIPR field |

**Returns** `u32`: clock frequency in Hz, 0 if the source is not ready or the selector is unknown

**Notes:** The mapping from selector values to peripherals is not identified in this packet.

- Addresses by version: 4130: 0x08002D24, 4139: 0x08002D24, 4148: 0x08002D24, 4168: 0x08002D24
- Peripheral registers: `RCC.CR` (R), `RCC.APBENR2` (A), `RCC.CCIPR` (R), `RCC.BDCR` (R)
- Called by: `bms_usart_init_from_config`
- Calls: `rcc_hclk_divide`, `rcc_pclk_divide`, `HAL_RCC_GetSysClockFreq`
- Confidence: medium

## bms_sysclk_hse_pll_bringup

**Start HSE and PLL as SYSCLK with HSI16 fallback, record 16 MHz, reset on failure**

Brings up the system clock. It sets RCC.CR HSEON and polls HSERDY for at most 3000 iterations. If HSE is ready, it writes PLLCFGR with PLLSRC = HSE and a fixed pattern (masked value OR 0xA0000C03), turns on the PLL and waits for PLLRDY, then selects the PLL as SYSCLK (CFGR.SW = 2) and waits for SWS to report it. If HSE does not come up it starts HSI16 (CR.HSION), waits for HSIRDY and selects HSI16 (SW = 0). In both cases it then calls bms_rtc_clock_bringup, clears CFGR bits 11:8 and 14:12, stores 16000000 through bms_set_state_word, and calls bms_4168_080021ec(3); a nonzero result calls NVIC_SystemReset. It ends by clearing CCIPR2 bits 9:8.

**Notes:** The 16 MHz value is stored whichever source is used, so the stored frequency is an assumption rather than a measurement. bms_4168_080021ec is not described in this packet. The meaning of the CCIPR2 bits is not confirmed.

- Addresses by version: 4130: 0x080090D0, 4139: 0x080095D0, 4148: 0x08009E1C, 4168: 0x0800A130
- Peripheral registers: `RCC.CR` (RW), `RCC.CFGR` (RW), `RCC.PLLCFGR` (RW), `RCC.APBENR2` (A), `RCC.CCIPR2` (RW)
- Called by: `RCC_CRS_IRQHandler`, `bms_4168_080082f0`, `bms_system_clock_setup`
- Calls: `NVIC_SystemReset`, `bms_systick_1khz_start`, `bms_set_state_word`, `bms_rtc_clock_bringup`
- Confidence: medium

## bms_sysclk_hsi16_switch

**Switch SYSCLK to HSI16 with APB prescaler cleared, record 16 MHz, reset on failure**

Falls back to the 16 MHz HSI oscillator as SYSCLK. It sets RCC.CR HSION, waits for HSIRDY, clears CFGR bits 11:8, sets CFGR.SW to 0 (HSI16) and waits until SWS shows HSI. It then clears CFGR bits 14:12, stores 16000000 through bms_set_state_word, and calls bms_4168_080021ec(3); a nonzero result calls NVIC_SystemReset. Finally it clears CCIPR2 bits 9:8. This is the HSI tail of bms_sysclk_hse_pll_bringup without the RTC step, so it is probably the re-clock after a STOP wake-up, which resumes on HSI16 (inferred).

**Notes:** The STOP-wake use is inferred from the pairing with bms_enter_stop_mode. Caller is bms_4168_08003290.

- Addresses by version: 4130: 0x08009280, 4139: 0x08009780, 4148: 0x08009FCC, 4168: 0x0800A2E0
- Peripheral registers: `RCC.CR` (RW), `RCC.CFGR` (RW), `RCC.CCIPR2` (RW)
- Called by: `bms_4168_08003290`
- Calls: `NVIC_SystemReset`, `bms_systick_1khz_start`, `bms_set_state_word`
- Confidence: medium

## bms_system_clock_setup

**Set the vector table, bring up SYSCLK from HSE/PLL, enable CSS and set the SysTick base**

Startup clock sequence. It calls bms_4168_0800A260 (VTOR and reset-cause latch), bms_sysclk_hse_pll_bringup (HSE and PLL as SYSCLK with HSI16 fallback, recorded as 16 MHz), bms_css_enable_sram_parity_lock (clock security system and SRAM parity lock in SYSCFG_CFGR2) and bms_systick_base_set with 16, which stores the SysTick base count used by the busy-wait helpers.

- Addresses by version: 4130: 0x08007688, 4139: 0x08007B88, 4148: 0x080083D4, 4168: 0x080086D4
- Called by: `bms_4168_08010558`
- Calls: `bms_systick_base_set`, `bms_sysclk_hse_pll_bringup`, `bms_css_enable_sram_parity_lock`, `bms_vtor_reset_cause_latch`
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
- Called by: `bms_rcc_get_clock_freqs`, `bms_rcc_periph_clk_get`
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
- Called by: `bms_rcc_get_clock_freqs`, `bms_rcc_periph_clk_get`
- Confidence: medium
