# MCU - `clock` functions

18 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`crm_adc_clock_div_set`](#crm_adc_clock_div_set) | 0x0800C2E4 | Set the ADC clock divider in CRM.CFG (ADCDIV low 2 bits and high bit) |
| [`crm_ahb_div_set`](#crm_ahb_div_set) | 0x0800C300 | Set the AHB prescaler (AHBDIV) in CRM.CFG bits 7:4 |
| [`crm_apb1_div_set`](#crm_apb1_div_set) | 0x0800C310 | Set the APB1 prescaler (APB1DIV) in CRM.CFG bits 10:8 |
| [`crm_apb2_div_set`](#crm_apb2_div_set) | 0x0800C320 | Set the APB2 prescaler (APB2DIV) in CRM.CFG bits 13:11 |
| [`crm_auto_step_mode_enable`](#crm_auto_step_mode_enable) | 0x0800C330 | Enable or disable automatic AHB step-up mode (CRM.MISC2 bits 5:4) |
| [`crm_clock_source_enable`](#crm_clock_source_enable) | 0x0800C350 | Enable or disable an oscillator or PLL (HICK, HEXT, PLL, LEXT, LICK) |
| [`crm_clocks_freq_get`](#crm_clocks_freq_get) | 0x0800C398 | Compute SYSCLK, AHB, APB2, APB1 and ADC clock frequencies from the CRM registers |
| [`crm_flag_get`](#crm_flag_get) | 0x0800C4C4 | Test a CRM status flag given as packed register offset and bit number |
| [`crm_hext_bypass`](#crm_hext_bypass) | 0x0800C4E8 | Set or clear the HEXT bypass bit (CRM.CTRL bit 18, HEXTBYPS) |
| [`crm_hext_stable_wait`](#crm_hext_stable_wait) | 0x0800C4F8 | Wait up to 0x3000 polls for the HEXT stable flag and return 1 if it is set |
| [`crm_lext_bypass`](#crm_lext_bypass) | 0x0800C524 | Set or clear the LEXT bypass bit (CRM.BPDC bit 2, LEXTBYPS) |
| [`crm_periph_clock_enable`](#crm_periph_clock_enable) | 0x0800C534 | Enable or disable a peripheral bus clock (AHBEN, APB1EN or APB2EN bit) |
| [`crm_periph_reset`](#crm_periph_reset) | 0x0800C55C | Assert or release a peripheral reset bit (APB1RST, APB2RST) |
| [`crm_pll_config`](#crm_pll_config) | 0x0800C584 | Select the PLL input (HICK, HEXT or HEXT/2), set its FREF band and multiplier |
| [`crm_reset`](#crm_reset) | 0x0800C684 | Reset the clock tree to its power-on state, switching SYSCLK to HICK first |
| [`crm_sysclk_switch`](#crm_sysclk_switch) | 0x0800C6D0 | Select the system clock source (CFG.SCLKSEL bits 1:0) |
| [`crm_sysclk_switch_status_get`](#crm_sysclk_switch_status_get) | 0x0800C6E0 | Read which clock currently drives SYSCLK (CFG.SCLKSTS bits 3:2) |
| [`system_clock_config`](#system_clock_config) | 0x08008DC0 | Start HEXT and the PLL, switch SYSCLK to the PLL and store the resulting SYSCLK frequency |

## crm_adc_clock_div_set

**Set the ADC clock divider in CRM.CFG (ADCDIV low 2 bits and high bit)**

Read-modify-write of CRM.CFG (0x40021004). The low two bits of the divider code go to ADCDIV_L (bits 15:14), and bit 2 of the code goes to ADCDIV_H (bit 28). Matches the SDK crm_adc_clock_div_set. The VCU build names the same routine identically (vcu_0159_0800b37c). Callers: mcu_0160_08001fb0, mcu_0160_08002068.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | ADC divider code 0..7 (3 bits) |

- Addresses by version: 12b: 0x0800C038, 143: 0x0800C280, 152: 0x0800C284, 0160: 0x0800C2E4
- Peripheral registers: `CRM.CFG` (RW)
- Called by: `mcu_0160_08001fb0`, `mcu_0160_08002068`
- Confidence: high

## crm_ahb_div_set

**Set the AHB prescaler (AHBDIV) in CRM.CFG bits 7:4**

Read-modify-write of CRM.CFG (0x40021004): replaces bits 7:4 with the low four bits of the argument. Only the division code is written, so the clock tree is unchanged until SYSCLK is switched. Matches the SDK crm_ahb_div_set. Caller: mcu_0160_08008dc0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | AHB divider code (4 bits) |

- Addresses by version: 12b: 0x0800C054, 143: 0x0800C29C, 152: 0x0800C2A0, 0160: 0x0800C300
- Peripheral registers: `CRM.CFG` (RW)
- Called by: `system_clock_config`
- Confidence: high

## crm_apb1_div_set

**Set the APB1 prescaler (APB1DIV) in CRM.CFG bits 10:8**

Read-modify-write of CRM.CFG (0x40021004): replaces bits 10:8 with the low three bits of the argument. Matches the SDK crm_apb1_div_set. Caller: mcu_0160_08008dc0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | APB1 divider code (3 bits) |

- Addresses by version: 12b: 0x0800C064, 143: 0x0800C2AC, 152: 0x0800C2B0, 0160: 0x0800C310
- Peripheral registers: `CRM.CFG` (RW)
- Called by: `system_clock_config`
- Confidence: high

## crm_apb2_div_set

**Set the APB2 prescaler (APB2DIV) in CRM.CFG bits 13:11**

Read-modify-write of CRM.CFG (0x40021004): replaces bits 13:11 with the low three bits of the argument. Matches the SDK crm_apb2_div_set. Caller: mcu_0160_08008dc0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | APB2 divider code (3 bits) |

- Addresses by version: 12b: 0x0800C074, 143: 0x0800C2BC, 152: 0x0800C2C0, 0160: 0x0800C320
- Peripheral registers: `CRM.CFG` (RW)
- Called by: `system_clock_config`
- Confidence: high

## crm_auto_step_mode_enable

**Enable or disable automatic AHB step-up mode (CRM.MISC2 bits 5:4)**

Writes both bits of the AUTO_STEP_EN field (bits 5:4 of CRM.MISC2, 0x40021054) to 1 when the argument is 1, and to 0 for any other value. Matches the SDK crm_auto_step_mode_enable. The VCU build names the same routine identically (vcu_0159_0800b3c8). Caller: mcu_0160_08008dc0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | 1 = enable, other = disable |

- Addresses by version: 12b: 0x0800C084, 143: 0x0800C2CC, 152: 0x0800C2D0, 0160: 0x0800C330
- Peripheral registers: `CRM.MISC2` (RW)
- Called by: `system_clock_config`
- Confidence: high

## crm_clock_source_enable

**Enable or disable an oscillator or PLL (HICK, HEXT, PLL, LEXT, LICK)**

Switches on the source code. 0 HICK sets CTRL bit 0 (HICKEN). 1 HEXT sets CTRL bit 16 (HEXTEN). 2 PLL sets CTRL bit 24 (PLLEN). 3 LEXT sets BPDC bit 0 (LEXTEN, 0x40021020). 4 LICK sets CTRLSTS bit 0 (LICKEN, 0x40021024). The bit is written from bit 0 of param_2, and unknown codes do nothing. The routine does not wait for the ready flag; callers poll with mcu_0160_0800c4c4. Matches the SDK crm_clock_source_enable and the VCU build's function of the same name. Callers: mcu_0160_08006028, mcu_0160_08008dc0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | clock source code 0..4 (HICK, HEXT, PLL, LEXT, LICK) |
| `param_2` | `u32` | bit 0: 1 = enable, 0 = disable |

- Addresses by version: 12b: 0x0800C0A4, 143: 0x0800C2EC, 152: 0x0800C2F0, 0160: 0x0800C350
- Peripheral registers: `CRM.CTRL` (RW), `CRM.BPDC` (RW), `CRM.CTRLSTS` (RW)
- Called by: `mcu_0160_08006028`, `system_clock_config`
- Confidence: high

## crm_clocks_freq_get

**Compute SYSCLK, AHB, APB2, APB1 and ADC clock frequencies from the CRM registers**

SDK crm_clocks_freq_get, compiled. The SYSCLK source comes from crm_sysclk_switch_status_get. HICK gives 8 MHz, or 48 MHz when MISC2 hick_to_sclk and MISC1 hickdiv are both set. HEXT gives 16 MHz on this board, where the SDK constant is 8 MHz. For the PLL the input is HICK/2 or HEXT (halved when the pllhextdiv bit is set) and the multiplier is either the CFG pllmult field plus 2 (with the high bits handled as in the SDK) or, when PLL bit 31 is set, the NS/MS/FR fields divided through __udivdi3. The results are written in SDK order: sclk_freq, ahb_freq, apb2_freq, apb1_freq, adc_freq, shifted by the AHB, APB2 and APB1 prescaler tables and divided by the ADC table (2, 4, 6, 8, 2, 12, 8, 16).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | crm_clocks_freq_type output: sclk, ahb, apb2, apb1, adc frequencies in Hz, five u32 words |

**Notes:** The SDK source at libraries/drivers/src/at32f415_crm.c matches this function's structure. The HEXT value 16 MHz is from this build.

- Addresses by version: 12b: 0x0800C0EC, 143: 0x0800C334, 152: 0x0800C338, 0160: 0x0800C398
- Peripheral registers: `CRM.CFG` (R), `CRM.PLL` (R), `CRM.MISC1` (R), `CRM.MISC2` (R)
- Called by: `mcu_0160_0800e1c0`
- Calls: `__udivdi3`, `crm_sysclk_switch_status_get`
- Confidence: high

## crm_flag_get

**Test a CRM status flag given as packed register offset and bit number**

The argument packs the register offset from the CRM base in bits 31:16 and the bit number in bits 4:0. It returns 1 when that bit is set in the register, computed as ((1 << bit) & ~reg) == 0. Used to poll oscillator-ready and PLL-lock flags during clock bring-up. Matches the SDK crm_flag_get, and the VCU build's function of the same name (vcu_0159_0800b578). Callers: mcu_0160_08008dc0, mcu_0160_0800c4f8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | packed flag code: (register offset << 16) \| bit |

**Returns** `bool`: true if the flag bit is set

- Addresses by version: 12b: 0x0800C218, 143: 0x0800C460, 152: 0x0800C464, 0160: 0x0800C4C4
- Peripheral registers: `CRM.CTRL` (A)
- Called by: `system_clock_config`, `crm_hext_stable_wait`
- Confidence: high

## crm_hext_bypass

**Set or clear the HEXT bypass bit (CRM.CTRL bit 18, HEXTBYPS)**

Writes bit 18 (HEXTBYPS) of CRM.CTRL from bit 0 of the argument. Bypass lets an external clock signal drive HEXT without the crystal oscillator. Matches the SDK crm_hext_bypass. Caller: mcu_0160_08006028.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | bit 0: 1 = bypass, 0 = crystal mode |

- Addresses by version: 12b: 0x0800C23C, 143: 0x0800C484, 152: 0x0800C488, 0160: 0x0800C4E8
- Peripheral registers: `CRM.CTRL` (RW)
- Called by: `mcu_0160_08006028`
- Confidence: high

## crm_hext_stable_wait

**Wait up to 0x3000 polls for the HEXT stable flag and return 1 if it is set**

SDK crm_hext_stable_wait. It polls CRM_HEXT_STABLE_FLAG (packed code 0x11, CRM.CTRL bit 17) until the flag is set or HEXT_STARTUP_TIMEOUT (0x3000) polls have elapsed, then returns 1 (SUCCESS) when the flag is set and 0 (ERROR) otherwise. It has no side effects beyond reading the flag.

**Returns** `bool`: 1 when HEXT reports stable within the timeout, 0 otherwise

- Addresses by version: 12b: 0x0800C24C, 143: 0x0800C494, 152: 0x0800C498, 0160: 0x0800C4F8
- Called by: `system_clock_config`
- Calls: `crm_flag_get`
- Confidence: high

## crm_lext_bypass

**Set or clear the LEXT bypass bit (CRM.BPDC bit 2, LEXTBYPS)**

Writes bit 2 (LEXTBYPS) of CRM.BPDC (0x40021020) from bit 0 of the argument. Bypass lets an external clock drive the low-speed oscillator input. Matches the SDK crm_lext_bypass. Caller: mcu_0160_08006028.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | bit 0: 1 = bypass, 0 = crystal mode |

- Addresses by version: 12b: 0x0800C278, 143: 0x0800C4C0, 152: 0x0800C4C4, 0160: 0x0800C524
- Peripheral registers: `CRM.BPDC` (RW)
- Called by: `mcu_0160_08006028`
- Confidence: high

## crm_periph_clock_enable

**Enable or disable a peripheral bus clock (AHBEN, APB1EN or APB2EN bit)**

param_1 packs the CRM register offset in bits 31:16 (0x14 AHBEN, 0x18 APB2EN, 0x1C APB1EN) and the bit position in bits 4:0. The bit is set when param_2 == 1 and cleared otherwise, with a plain read-modify-write. Called by nearly every peripheral init routine in the MCU build, including mcu_0160_08001f34, mcu_0160_08001fb0 and mcu_0160_08002068. Matches the SDK crm_periph_clock_enable, and the VCU build's function of the same name (vcu_0159_0800b5cc).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | packed peripheral clock code: (register offset << 16) \| bit |
| `param_2` | `s32` | 1 = enable clock, other = disable |

- Addresses by version: 12b: 0x0800C288, 143: 0x0800C4D0, 152: 0x0800C4D4, 0160: 0x0800C534
- Peripheral registers: `CRM.CTRL` (A)
- Called by: `mcu_adc1_dma_init`, `mcu_0160_08001fb0`, `mcu_0160_08002068`, `mcu_0160_08003060`, `mcu_can_init`, `mcu_0160_08006028`, `mcu_gpio_port_clock_enable`, `mcu_0160_08009800`, `mcu_pvm_init`, `mcu_0160_0800a6b8`, `mcu_dma_channel_start`, `mcu_0160_0800ac52` ...
- Confidence: high

## crm_periph_reset

**Assert or release a peripheral reset bit (APB1RST, APB2RST)**

Same bit set/clear code as crm_periph_clock_enable, applied to the reset registers: packed offsets 0x0C (APB2RST) and 0x10 (APB1RST). param_2 == 1 holds the peripheral in reset and any other value releases it. The one caller in the packet family, mcu_0160_0800c278, pulses 0x100019 (APB1RST bit 25, CAN1RST) with 1 and then 0, which is a CAN1 reset pulse. Matches the SDK crm_periph_reset, and the VCU build's function of the same name (vcu_0159_0800b5f4).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | packed peripheral reset code: (register offset << 16) \| bit |
| `param_2` | `s32` | 1 = hold in reset, other = release |

**Notes:** The machine code is identical to crm_periph_clock_enable. The reset role comes from the 1-then-0 pulse at its call site, not from the code itself.

- Addresses by version: 12b: 0x0800C2B0, 143: 0x0800C4F8, 152: 0x0800C4FC, 0160: 0x0800C55C
- Peripheral registers: `CRM.CTRL` (A)
- Called by: `mcu_can1_reset_pulse`
- Confidence: high

## crm_pll_config

**Select the PLL input (HICK, HEXT or HEXT/2), set its FREF band and multiplier**

param_1 chooses the PLL input. 0 is HICK (CFG.PLLRCS = 0, reference 4 MHz). 1 is HEXT direct (PLLRCS = 1, PLLHEXTDIV = 0, reference 16 MHz). Any other value is HEXT/2 (PLLHEXTDIV = 1, reference 8 MHz). The reference frequency selects the PLL.PLLFREF code in CRM+0x2C bits 26:24: 4 MHz = 0, 6 MHz = 1, 8 MHz = 2, 12 MHz = 3, 16 MHz = 4, 25 MHz = 5. param_2 is the multiplier code: bits 3:0 go to CFG bits 21:18 (PLLMULT_L) and bits 5:4 go to CFG bits 30:29 (PLLMULT_H). The SDK version also sets MISC1.HICKDIV for the HICK source, which this build does not do. Matches the SDK crm_pll_config and the VCU build's function (vcu_0159_0800b61c). Caller: mcu_0160_08008dc0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | PLL source: 0 HICK, 1 HEXT, other = HEXT/2 |
| `param_2` | `u32` | 6-bit PLL multiplier code |

- Addresses by version: 12b: 0x0800C2D8, 143: 0x0800C520, 152: 0x0800C524, 0160: 0x0800C584
- Peripheral registers: `CRM.CFG` (RW), `CRM.PLL` (RW)
- Called by: `system_clock_config`
- Confidence: high

## crm_reset

**Reset the clock tree to its power-on state, switching SYSCLK to HICK first**

Sets CTRL.HICKEN and busy-waits for HICKSTBL. It selects HICK as SYSCLK (CFG.SCLKSEL = 0) and waits for SCLKSTS to show HICK. It clears CTRL bits 16 (HEXTEN), 18 (HEXTBYPS), 19 (CFDEN) and 24 (PLLEN), zeroes CFG, and loads the power-on values PLL = 0x1F10, MISC1 = 0x100000 and CLKINT = 0x9F0000. Both waits have no timeout. Matches the SDK crm_reset. Caller: mcu_0160_08008dc0.

- Addresses by version: 12b: 0x0800C3D8, 143: 0x0800C620, 152: 0x0800C624, 0160: 0x0800C684
- Peripheral registers: `CRM.CTRL` (ARW), `CRM.CFG` (RW), `CRM.CLKINT` (W), `CRM.PLL` (W), `CRM.MISC1` (W)
- Called by: `system_clock_config`
- Confidence: high

## crm_sysclk_switch

**Select the system clock source (CFG.SCLKSEL bits 1:0)**

Replaces CFG bits 1:0 with the low two bits of the argument: 0 HICK, 1 HEXT, 2 PLL. No wait is done here. Callers poll the result with crm_sysclk_switch_status_get. Matches the SDK crm_sysclk_switch. Caller: mcu_0160_08008dc0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | SYSCLK source code 0..3 |

- Addresses by version: 12b: 0x0800C424, 143: 0x0800C66C, 152: 0x0800C670, 0160: 0x0800C6D0
- Peripheral registers: `CRM.CFG` (RW)
- Called by: `system_clock_config`
- Confidence: high

## crm_sysclk_switch_status_get

**Read which clock currently drives SYSCLK (CFG.SCLKSTS bits 3:2)**

Returns CFG bits 3:2 (SCLKSTS): 0 HICK, 1 HEXT, 2 PLL. Used after crm_sysclk_switch to wait until the switch has taken effect. Matches the SDK crm_sysclk_switch_status_get, and the VCU build's function of the same name (vcu_0159_0800b760). Callers: mcu_0160_08008dc0, mcu_0160_0800c398.

**Returns** `u32`: current SYSCLK source code 0..2

- Addresses by version: 12b: 0x0800C434, 143: 0x0800C67C, 152: 0x0800C680, 0160: 0x0800C6E0
- Peripheral registers: `CRM.CFG` (R)
- Called by: `system_clock_config`, `crm_clocks_freq_get`
- Confidence: high

## system_clock_config

**Start HEXT and the PLL, switch SYSCLK to the PLL and store the resulting SYSCLK frequency**

System clock bring-up with the call order of the Artery demo system_clock_config: clock tree reset (crm_reset), FLASH.PSR = 0x14 (prefetch on, 4 wait states), HEXT enable and a retry loop around crm_hext_stable_wait, PLL from HEXT with multiplier code 7 (x9) through crm_pll_config, PLL enable and wait for the PLL stable flag (0x19), AHB /1, APB1 /2 and APB2 /2, auto step-up mode on, SYSCLK switched to the PLL and confirmed by reading back 2, auto step-up mode off. Every wait is an unbounded loop, so the function does not return until HEXT and the PLL are stable. Finally it recomputes SYSCLK from the CRM registers, applies the AHB prescaler and stores the result in the global at 0x200000A8 (SystemCoreClock). With the 16 MHz HEXT of this board and the HEXT/2 bit clear, SYSCLK is 144 MHz.

**Notes:** The name is the usual Artery BSP routine name, matched by call sequence to the SDK demo at utilities/at32f415_usb_iap_demo style clock code. HEXT is 16 MHz from this function's own frequency branch; the SDK template constant is 8 MHz.

- Addresses by version: 12b: 0x08008B70, 143: 0x08008D0C, 152: 0x08008D4C, 0160: 0x08008DC0
- Peripheral registers: `CRM.CFG` (R), `CRM.PLL` (R), `CRM.MISC1` (R), `CRM.MISC2` (R), `FLASH.PSR` (W)
- Called by: `mcu_0160_0800d548`
- Calls: `__udivdi3`, `crm_ahb_div_set`, `crm_apb1_div_set`, `crm_apb2_div_set`, `crm_auto_step_mode_enable`, `crm_clock_source_enable`, `crm_flag_get`, `crm_hext_stable_wait`, `crm_pll_config`, `crm_reset`, `crm_sysclk_switch`, `crm_sysclk_switch_status_get`
- Confidence: high
