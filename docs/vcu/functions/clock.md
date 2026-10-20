# VCU - `clock` functions

20 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`crm_adc_clock_div_set`](#crm_adc_clock_div_set) | 0x0800B37C | Set the ADC clock divider in CRM.CFG (SDK crm_adc_clock_div_set) |
| [`crm_ahb_div_set`](#crm_ahb_div_set) | 0x0800B398 | Set the AHB prescaler in CRM.CFG (SDK crm_ahb_div_set) |
| [`crm_apb1_div_set`](#crm_apb1_div_set) | 0x0800B3A8 | Set the APB1 prescaler in CRM.CFG (SDK crm_apb1_div_set) |
| [`crm_apb2_div_set`](#crm_apb2_div_set) | 0x0800B3B8 | Set the APB2 prescaler in CRM.CFG (SDK crm_apb2_div_set) |
| [`crm_auto_step_mode_enable`](#crm_auto_step_mode_enable) | 0x0800B3C8 | Enable/disable automatic clock step-up mode (SDK crm_auto_step_mode_enable) |
| [`crm_battery_powered_domain_reset`](#crm_battery_powered_domain_reset) | 0x0800B3E8 | Assert or release the battery-powered domain reset (SDK crm_battery_powered_domain_reset) |
| [`crm_clock_source_enable`](#crm_clock_source_enable) | 0x0800B3F8 | Enable/disable a clock source (SDK crm_clock_source_enable) |
| [`crm_clocks_freq_get`](#crm_clocks_freq_get) | 0x0800B440 | Compute SYSCLK, AHB, APB2, APB1 and ADC clock frequencies from the CRM registers |
| [`crm_ertc_clock_enable`](#crm_ertc_clock_enable) | 0x0800B558 | Enable/disable the ERTC clock (SDK crm_ertc_clock_enable) |
| [`crm_ertc_clock_select`](#crm_ertc_clock_select) | 0x0800B568 | Select the ERTC clock source (SDK crm_ertc_clock_select) |
| [`crm_flag_get`](#crm_flag_get) | 0x0800B578 | Test a CRM status flag (SDK crm_flag_get) |
| [`crm_periph_clock_enable`](#crm_periph_clock_enable) | 0x0800B5CC | Enable/disable a peripheral bus clock (SDK crm_periph_clock_enable) |
| [`crm_periph_reset`](#crm_periph_reset) | 0x0800B5F4 | Assert/release a peripheral reset bit (SDK crm_periph_reset) |
| [`crm_pll_config`](#crm_pll_config) | 0x0800B61C | Select the PLL source, multiplier and reference range (SDK crm_pll_config) |
| [`crm_reset`](#crm_reset) | 0x0800B708 | Reset the CRM clock configuration to its default state (SDK crm_reset) |
| [`crm_sysclk_switch`](#crm_sysclk_switch) | 0x0800B750 | Select the system clock source (SDK crm_sysclk_switch) |
| [`crm_sysclk_switch_status_get`](#crm_sysclk_switch_status_get) | 0x0800B760 | Read which clock currently drives SYSCLK (SDK crm_sysclk_switch_status_get) |
| [`system_clock_config`](#system_clock_config) | 0x0800E8E0 | Bring SYSCLK up from HEXT and PLL with flash wait states, then update the core clock value |
| [`vcu_hext_enable_and_wait`](#vcu_hext_enable_and_wait) | 0x0800B598 | Poll for the HEXT stable flag up to 0x3000 times, enable HEXT, and report whether it is stable |
| [`vcu_sysclk_switch_to_pll`](#vcu_sysclk_switch_to_pll) | 0x0800E950 | Switch SYSCLK to the configured PLL (enable HEXT and PLL, wait, switch) without reset |

## crm_adc_clock_div_set

**Set the ADC clock divider in CRM.CFG (SDK crm_adc_clock_div_set)**

Read-modify-write of CRM.CFG: low two bits of the divider go to ADCDIV_L (CFG[15:14]) and bit 2 goes to ADCDIV_H (CFG[28]). Called once by the ADC init routine vcu_0159_08001d5c. Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | crm_adc_div_type, 0..7 (3-bit divider code) |

- Addresses by version: 148: 0x0800A45C, 14a: 0x0800A854, 14b: 0x0800ACDC, 14e: 0x0800AD70, 14f: 0x0800AEAC, 152: 0x0800B138, 153: 0x0800B22C, 0159: 0x0800B37C
- Peripheral registers: `CRM.CFG` (RW)
- Called by: `vcu_adc1_scan_init`
- Confidence: high

## crm_ahb_div_set

**Set the AHB prescaler in CRM.CFG (SDK crm_ahb_div_set)**

Replaces CRM.CFG[7:4] (AHBDIV) with the low nibble of param_1. Called from the system clock setup vcu_0159_0800e8e0. Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | crm_ahb_div_type, 4-bit AHBDIV code |

- Addresses by version: 148: 0x0800A478, 14a: 0x0800A870, 14b: 0x0800ACF8, 14e: 0x0800AD8C, 14f: 0x0800AEC8, 152: 0x0800B154, 153: 0x0800B248, 0159: 0x0800B398
- Peripheral registers: `CRM.CFG` (RW)
- Called by: `system_clock_config`
- Confidence: high

## crm_apb1_div_set

**Set the APB1 prescaler in CRM.CFG (SDK crm_apb1_div_set)**

Replaces CRM.CFG[10:8] (APB1DIV) with the low 3 bits of param_1. Called from the system clock setup vcu_0159_0800e8e0. Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | crm_apb1_div_type, 3-bit code |

- Addresses by version: 148: 0x0800A488, 14a: 0x0800A880, 14b: 0x0800AD08, 14e: 0x0800AD9C, 14f: 0x0800AED8, 152: 0x0800B164, 153: 0x0800B258, 0159: 0x0800B3A8
- Peripheral registers: `CRM.CFG` (RW)
- Called by: `system_clock_config`
- Confidence: high

## crm_apb2_div_set

**Set the APB2 prescaler in CRM.CFG (SDK crm_apb2_div_set)**

Replaces CRM.CFG[13:11] (APB2DIV) with the low 3 bits of param_1. Called from the system clock setup vcu_0159_0800e8e0. Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | crm_apb2_div_type, 3-bit code |

- Addresses by version: 148: 0x0800A498, 14a: 0x0800A890, 14b: 0x0800AD18, 14e: 0x0800ADAC, 14f: 0x0800AEE8, 152: 0x0800B174, 153: 0x0800B268, 0159: 0x0800B3B8
- Peripheral registers: `CRM.CFG` (RW)
- Called by: `system_clock_config`
- Confidence: high

## crm_auto_step_mode_enable

**Enable/disable automatic clock step-up mode (SDK crm_auto_step_mode_enable)**

Writes CRM.MISC2 (0x40021054) AUTO_STEP_EN field (bits 5:4): sets both bits (0x30) when param_1 == 1, otherwise clears them. The auto-step mode lets the hardware step the AHB clock when switching to a fast PLL clock above 108 MHz; it is called around system clock switching in vcu_0159_0800e8e0 and vcu_0159_0800e950. Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | 1 = enable (TRUE), anything else = disable |

- Addresses by version: 148: 0x0800A4A8, 14a: 0x0800A8A0, 14b: 0x0800AD28, 14e: 0x0800ADBC, 14f: 0x0800AEF8, 152: 0x0800B184, 153: 0x0800B278, 0159: 0x0800B3C8
- Peripheral registers: `CRM.MISC2` (RW)
- Called by: `system_clock_config`, `vcu_sysclk_switch_to_pll`
- Confidence: high

## crm_battery_powered_domain_reset

**Assert or release the battery-powered domain reset (SDK crm_battery_powered_domain_reset)**

Writes CRM.BPDC (0x40021020) bit16 (BPDRST) with bit0 of param_1. The BPD reset clears the ERTC, backup registers and LEXT/ERTC clock selection. Called from the ERTC/backup-domain setup vcu_0159_0800c960 (surrounded by crm_ertc_clock_* calls). Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 1 = hold BPD in reset, 0 = release |

- Addresses by version: 148: 0x0800A4C8, 14a: 0x0800A8C0, 14b: 0x0800AD48, 14e: 0x0800ADDC, 14f: 0x0800AF18, 152: 0x0800B1A4, 153: 0x0800B298, 0159: 0x0800B3E8
- Peripheral registers: `CRM.BPDC` (RW)
- Called by: `vcu_ertc_default_datetime_init`
- Confidence: high

## crm_clock_source_enable

**Enable/disable a clock source (SDK crm_clock_source_enable)**

Switch on the crm_clock_source_type: 0 HICK -> CRM.CTRL bit0 (HICKEN), 1 HEXT -> CTRL bit16 (HEXTEN), 2 PLL -> CTRL bit24 (PLLEN), 3 LEXT -> BPDC (0x40021020) bit0 (LEXTEN), 4 LICK -> CTRLSTS (0x40021024) bit0 (LICKEN). The bit written is bit0 of param_2. Used by clock bring-up (vcu_0159_0800e8e0, vcu_0159_0800e950), the ERTC setup (vcu_0159_0800c960) and vcu_0159_0800b598. Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | crm_clock_source_type 0..4 (HICK, HEXT, PLL, LEXT, LICK) |
| `param_2` | `u32` | 1 = enable, 0 = disable |

- Addresses by version: 148: 0x0800A4D8, 14a: 0x0800A8D0, 14b: 0x0800AD58, 14e: 0x0800ADEC, 14f: 0x0800AF28, 152: 0x0800B1B4, 153: 0x0800B2A8, 0159: 0x0800B3F8
- Peripheral registers: `CRM.CTRL` (RW), `CRM.BPDC` (RW), `CRM.CTRLSTS` (RW)
- Called by: `vcu_hext_enable_and_wait`, `vcu_ertc_default_datetime_init`, `system_clock_config`, `vcu_sysclk_switch_to_pll`
- Confidence: high

## crm_clocks_freq_get

**Compute SYSCLK, AHB, APB2, APB1 and ADC clock frequencies from the CRM registers**

Matches the Artery SDK crm_clocks_freq_get: the output words are sclk, ahb, apb2, apb1 and adc in the crm_clocks_freq_type order. The SYSCLK source comes from crm_sysclk_switch_status_get (FUN_0800b760). HICK gives 8 MHz, or 48 MHz when both the MISC2 and MISC1 selection bits are set; HEXT is taken as 16 MHz; PLL is computed from CRM_CFG (multiplier bits 18..21 and 29..30, source bit 16, HEXT/2 bit 17) or, when bit 31 of the PLL register is set (extended mode), as input times NS over MS shifted by FR, using a 64-bit divide (FUN_080011ac). AHB, APB2 and APB1 come from divider tables indexed by CFG bits 4..7, 11..13 and 8..10, and the ADC clock is APB2 divided by a table entry.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | crm_clocks_freq_type output: five u32 frequencies in Hz |

**Notes:** The ADC divider index mixes CFG bits 14..15 with bits 28..31 and was not traced against the SDK adc_div_table. The 16 MHz HEXT value is the SDK HEXT_VALUE used by this board.

- Addresses by version: 148: 0x0800A520, 14a: 0x0800A918, 14b: 0x0800ADA0, 14e: 0x0800AE34, 14f: 0x0800AF70, 152: 0x0800B1FC, 153: 0x0800B2F0, 0159: 0x0800B440
- Peripheral registers: `CRM.CFG` (R), `CRM.PLL` (R), `CRM.MISC1` (R), `CRM.MISC2` (R)
- Called by: `vcu_tmr2_ch1_pwm_init`, `vcu_tmr5_1khz_tick_init`, `vcu_usart_baud_frame_config`
- Calls: `vcu_udiv64_shift_subtract`, `crm_sysclk_switch_status_get`
- Confidence: high

## crm_ertc_clock_enable

**Enable/disable the ERTC clock (SDK crm_ertc_clock_enable)**

Writes CRM.BPDC (0x40021020) bit15 (ERTCEN) from bit0 of param_1. Called from the ERTC init vcu_0159_0800c960. Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 1 = enable, 0 = disable |

- Addresses by version: 148: 0x0800A638, 14a: 0x0800AA30, 14b: 0x0800AEB8, 14e: 0x0800AF4C, 14f: 0x0800B088, 152: 0x0800B314, 153: 0x0800B408, 0159: 0x0800B558
- Peripheral registers: `CRM.BPDC` (RW)
- Called by: `vcu_ertc_default_datetime_init`
- Confidence: high

## crm_ertc_clock_select

**Select the ERTC clock source (SDK crm_ertc_clock_select)**

Writes CRM.BPDC (0x40021020) bits 9:8 (ERTCSEL) from the low two bits of param_1 (0 none, 1 LEXT, 2 LICK, 3 HEXT/32). Called from the ERTC init vcu_0159_0800c960. Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | crm_ertc_clock_type, 0..3 |

- Addresses by version: 148: 0x0800A648, 14a: 0x0800AA40, 14b: 0x0800AEC8, 14e: 0x0800AF5C, 14f: 0x0800B098, 152: 0x0800B324, 153: 0x0800B418, 0159: 0x0800B568
- Peripheral registers: `CRM.BPDC` (RW)
- Called by: `vcu_ertc_default_datetime_init`
- Confidence: high

## crm_flag_get

**Test a CRM status flag (SDK crm_flag_get)**

The flag code packs the register byte offset in bits 31:16 and the bit number in bits 4:0 (SDK MAKE_VALUE). Returns 1 when that bit in the register at CRM+offset is set (computed as (1<<bit & ~reg) == 0). Used to poll HICK/HEXT/PLL/LEXT/LICK stable flags during clock bring-up (vcu_0159_0800b598, vcu_0159_0800c960, vcu_0159_0800e8e0, vcu_0159_0800e950). Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | packed flag code: (reg_offset<<16)\|bit |

**Returns** `bool`: true if the flag bit is set

- Addresses by version: 148: 0x0800A658, 14a: 0x0800AA50, 14b: 0x0800AED8, 14e: 0x0800AF6C, 14f: 0x0800B0A8, 152: 0x0800B334, 153: 0x0800B428, 0159: 0x0800B578
- Peripheral registers: `CRM.CTRL` (A)
- Called by: `vcu_hext_enable_and_wait`, `vcu_ertc_default_datetime_init`, `system_clock_config`, `vcu_sysclk_switch_to_pll`
- Confidence: high

## crm_periph_clock_enable

**Enable/disable a peripheral bus clock (SDK crm_periph_clock_enable)**

param_1 packs the CRM register offset (bits 31:16: 0x14 AHBEN, 0x18 APB2EN, 0x1c APB1EN) and the bit position (bits 4:0). Sets the bit when param_2 == 1, clears it otherwise. Called by essentially every peripheral init routine (GPIO, USART, TMR, ADC, CAN, DMA, ... e.g. vcu_0159_08001bca, 08001c3c, 08001ca8, 08001d5c). Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | packed peripheral clock code (reg offset<<16 \| bit) |
| `param_2` | `s32` | 1 = enable clock, other = disable |

- Addresses by version: 148: 0x0800A6AC, 14a: 0x0800AAA4, 14b: 0x0800AF2C, 14e: 0x0800AFC0, 14f: 0x0800B0FC, 152: 0x0800B388, 153: 0x0800B47C, 0159: 0x0800B5CC
- Peripheral registers: `CRM.CTRL` (A)
- Called by: `vcu_tmr2_ch1_pwm_init`, `vcu_adc_dma_ring_init`, `vcu_adc_analog_pins_init`, `vcu_adc1_scan_init`, `vcu_gpio_pa0_init`, `vcu_usart2_pins_init`, `vcu_usart2_init`, `vcu_usart2_rx_dma_init`, `vcu_usart2_tx_dma_init`, `vcu_exint14_pb14_init`, `vcu_exint_pb12_pb14_init`, `vcu_can1_clock_disable` ...
- Confidence: high

## crm_periph_reset

**Assert/release a peripheral reset bit (SDK crm_periph_reset)**

Same bit-set/clear helper as crm_periph_clock_enable but for the APBxRST/AHBRST registers (offsets 0x0c/0x10 in the packed code): sets the bit when param_2 == 1, clears it otherwise. Its single caller vcu_0159_0800b06c is most likely the SDK gpio_reset-style routine that pulses the reset of a GPIO port/peripheral. Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | packed peripheral reset code (reg offset<<16 \| bit) |
| `param_2` | `s32` | 1 = hold in reset, other = release |

**Notes:** Machine code is identical to crm_periph_clock_enable; the distinction (reset vs clock vs sleep-mode clock) is inferred from the single caller only.

- Addresses by version: 148: 0x0800A6D4, 14a: 0x0800AACC, 14b: 0x0800AF54, 14e: 0x0800AFE8, 14f: 0x0800B124, 152: 0x0800B3B0, 153: 0x0800B4A4, 0159: 0x0800B5F4
- Peripheral registers: `CRM.CTRL` (A)
- Called by: `vcu_can1_reset_pulse`
- Confidence: medium

## crm_pll_config

**Select the PLL source, multiplier and reference range (SDK crm_pll_config)**

param_1 selects the source: 0 = HICK (CFG.PLLRCS=0, MISC1 bit25 HICKDIV=no div, ref assumed 4 MHz), 1 = HEXT direct (PLLRCS=1, PLLHEXTDIV=0, ref 16 MHz), other = HEXT/2 (PLLHEXTDIV=1, ref 8 MHz). It then maps the reference frequency to the PLL.PLLFREF code (CRM+0x2c bits 26:24): 4M=0, 6M=1, 8M=2, 12M=3, 16M=4, 25M=5, using the SDK range thresholds. The multiplier param_2 is split into CFG[21:18] (low 4 bits) and CFG[30:29] (high 2 bits). The constants imply HEXT_VALUE = 16 MHz in this build. Called from vcu_0159_0800e8e0. Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | crm_pll_clock_source_type: 0 HICK, 1 HEXT, 2 HEXT/2 |
| `param_2` | `u32` | crm_pll_mult_type, 6-bit PLL multiplier code |

- Addresses by version: 148: 0x0800A6FC, 14a: 0x0800AAF4, 14b: 0x0800AF7C, 14e: 0x0800B010, 14f: 0x0800B14C, 152: 0x0800B3D8, 153: 0x0800B4CC, 0159: 0x0800B61C
- Peripheral registers: `CRM.CFG` (RW), `CRM.PLL` (RW), `CRM.MISC1` (RW)
- Called by: `system_clock_config`
- Confidence: high

## crm_reset

**Reset the CRM clock configuration to its default state (SDK crm_reset)**

Sets HICKEN and waits for HICKSTBL (CTRL bit1), switches SCLKSEL to HICK and waits for SCLKSTS == 0, clears CTRL bits 0x010D0000 (HEXTEN, HEXTBYPS, CFDEN, PLLEN), zeroes CFG, sets PLL to 0x1f10, MISC1 to 0x100000 and CLKINT to 0x9f0000 (disable all clock interrupts and clear flags). Used at the start of the system clock configuration vcu_0159_0800e8e0. Blocks in busy-wait loops with no timeout. Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

- Addresses by version: 148: 0x0800A7E8, 14a: 0x0800ABE0, 14b: 0x0800B068, 14e: 0x0800B0FC, 14f: 0x0800B238, 152: 0x0800B4C4, 153: 0x0800B5B8, 0159: 0x0800B708
- Peripheral registers: `CRM.CTRL` (ARW), `CRM.CFG` (RW), `CRM.CLKINT` (W), `CRM.PLL` (W), `CRM.MISC1` (W)
- Called by: `system_clock_config`
- Confidence: high

## crm_sysclk_switch

**Select the system clock source (SDK crm_sysclk_switch)**

Writes CRM.CFG[1:0] (SCLKSEL) with the low 2 bits of param_1 (0 HICK, 1 HEXT, 2 PLL). The switch completes asynchronously; the caller polls crm_sysclk_switch_status_get. Called from vcu_0159_0800e8e0 and vcu_0159_0800e950. Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | crm_sclk_type 0..2 |

- Addresses by version: 148: 0x0800A830, 14a: 0x0800AC28, 14b: 0x0800B0B0, 14e: 0x0800B144, 14f: 0x0800B280, 152: 0x0800B50C, 153: 0x0800B600, 0159: 0x0800B750
- Peripheral registers: `CRM.CFG` (RW)
- Called by: `system_clock_config`, `vcu_sysclk_switch_to_pll`
- Confidence: high

## crm_sysclk_switch_status_get

**Read which clock currently drives SYSCLK (SDK crm_sysclk_switch_status_get)**

Returns CRM.CFG bits 3:2 (SCLKSTS): 0 HICK, 1 HEXT, 2 PLL. Called from vcu_0159_0800e8e0 / vcu_0159_0800e950 (wait loops after crm_sysclk_switch) and vcu_0159_0800b440 (likely crm_clocks_freq_get). Artery SDK at32f415_crm.c driver; accesses CRM registers directly.

**Returns** `u32`: active system clock source code 0..2

- Addresses by version: 148: 0x0800A840, 14a: 0x0800AC38, 14b: 0x0800B0C0, 14e: 0x0800B154, 14f: 0x0800B290, 152: 0x0800B51C, 153: 0x0800B610, 0159: 0x0800B760
- Peripheral registers: `CRM.CFG` (R)
- Called by: `crm_clocks_freq_get`, `system_clock_config`, `vcu_sysclk_switch_to_pll`
- Confidence: high

## system_clock_config

**Bring SYSCLK up from HEXT and PLL with flash wait states, then update the core clock value**

AT32 SDK system_clock_config from the Artery demo sources, with system_core_clock_update inlined at the end. It runs crm_reset (vcu_0159_0800b708), sets FLASH.PSR to 0x14 (4 wait states, prefetch on), enables HEXT and waits with vcu_0159_0800b598 (crm_hext_stable_wait), then configures the PLL with crm_pll_config(1 = HEXT, 7 = CRM_PLL_MULT_9), enables it and waits for the PLL stable flag (CRM CTRL bit 25). It sets AHB /1, APB2 /2 and APB1 /2, turns on auto-step mode around crm_sysclk_switch(2 = PLL), polls crm_sysclk_switch_status_get until the PLL drives SYSCLK, and turns auto-step off. The last part decodes the active source, the PLL multiplier and the AHB divider and writes the resulting frequency to the global at 0x200018BC, using the AHB shift table at 0x0800F284.

**Notes:** Decoded result for the PLL path (HEXT direct times multiplier code 7 read as x9) is 144 MHz SYSCLK. That looks above the AT32F415 120 MHz maximum, so verify the PLL setting or the crystal frequency before trusting the value. The HICK branch gives 8 or 48 MHz depending on the MISC1/MISC2 bits.

- Addresses by version: 148: 0x0800D8C0, 14a: 0x0800DD5C, 14b: 0x0800E1E8, 14e: 0x0800E288, 14f: 0x0800E3D4, 152: 0x0800E67C, 153: 0x0800E770, 0159: 0x0800E8E0
- Peripheral registers: `CRM.CFG` (R), `CRM.PLL` (R), `CRM.MISC1` (R), `CRM.MISC2` (R), `FLASH.PSR` (W)
- Called by: `vcu_0159_0800d858`
- Calls: `vcu_udiv64_shift_subtract`, `crm_ahb_div_set`, `crm_apb1_div_set`, `crm_apb2_div_set`, `crm_auto_step_mode_enable`, `crm_clock_source_enable`, `crm_flag_get`, `vcu_hext_enable_and_wait`, `crm_pll_config`, `crm_reset`, `crm_sysclk_switch`, `crm_sysclk_switch_status_get`
- Confidence: high

## vcu_hext_enable_and_wait

**Poll for the HEXT stable flag up to 0x3000 times, enable HEXT, and report whether it is stable**

Polls the HEXT stable flag (crm_flag_get with CRM_HEXT_STABLE_FLAG, which is 0x11) for up to 0x3000 iterations, then calls crm_clock_source_enable on CRM_CLOCK_SOURCE_HEXT (value 1), polls the flag again and returns 1 only if it reads set. The SDK crm_hext_stable_wait is the wait portion only, without the enable. Because the stable flag cannot set before HEXT is running, the first loop always runs to its timeout unless HEXT was already on.

**Returns** `bool`: 1 when HEXT reads stable after the enable, else 0

**Notes:** The enable argument of crm_clock_source_enable is not visible in the decompile; TRUE is presumed from the context.

- Addresses by version: 148: 0x0800A678, 14a: 0x0800AA70, 14b: 0x0800AEF8, 14e: 0x0800AF8C, 14f: 0x0800B0C8, 152: 0x0800B354, 153: 0x0800B448, 0159: 0x0800B598
- Called by: `system_clock_config`, `vcu_sysclk_switch_to_pll`
- Calls: `crm_clock_source_enable`, `crm_flag_get`
- Confidence: medium

## vcu_sysclk_switch_to_pll

**Switch SYSCLK to the configured PLL (enable HEXT and PLL, wait, switch) without reset**

Short clock switch used when the PLL is already configured. It enables HEXT and waits for it with vcu_0159_0800b598, enables the PLL and waits for its stable flag, turns on auto-step mode, selects PLL with crm_sysclk_switch(2), polls crm_sysclk_switch_status_get until PLL is active and then turns auto-step off. It writes no dividers, flash wait states or PLL multiplier and has no timeouts, so it spins forever if a clock never stabilises. Called from vcu_0159_0800688c (not described in this packet).

- Addresses by version: 148: 0x0800D930, 14a: 0x0800DDCC, 14b: 0x0800E258, 14e: 0x0800E2F8, 14f: 0x0800E444, 152: 0x0800E6EC, 153: 0x0800E7E0, 0159: 0x0800E950
- Called by: `vcu_deep_sleep_enter_and_restore`
- Calls: `crm_auto_step_mode_enable`, `crm_clock_source_enable`, `crm_flag_get`, `vcu_hext_enable_and_wait`, `crm_sysclk_switch`, `crm_sysclk_switch_status_get`
- Confidence: high
