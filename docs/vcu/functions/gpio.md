# VCU - `gpio` functions

28 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`gpio_bits_reset`](#gpio_bits_reset) | 0x0800D06C | Drive the selected GPIO port pins low through the write-only CLR register |
| [`gpio_bits_set`](#gpio_bits_set) | 0x0800D070 | Drive the selected GPIO port pins high through the write-only SCR register |
| [`gpio_default_para_init`](#gpio_default_para_init) | 0x0800D074 | Fill a gpio_init_type with defaults: all pins, input, push-pull, no pull, stronger drive |
| [`gpio_exint_line_config`](#gpio_exint_line_config) | 0x0800D08C | Route a GPIO port pin to an EXINT line by writing its 4-bit port field in IOMUX.EXINTCn |
| [`gpio_init`](#gpio_init) | 0x0800D0E8 | Configure the mode, pull and drive of the selected pins in CFGLR/CFGHR |
| [`gpio_pin_remap_config`](#gpio_pin_remap_config) | 0x0800D19C | Set or clear a bit field in an IOMUX remap register, encoded in one 32-bit code |
| [`vcu_gpio_b10_high_b2_low`](#vcu_gpio_b10_high_b2_low) | 0x080089BC | Return 1 when GPIOB pin 10 reads high and GPIOB pin 2 reads low |
| [`vcu_gpio_b10_low_b2_high`](#vcu_gpio_b10_low_b2_high) | 0x080089E4 | Return 1 when GPIOB pin 10 reads low and GPIOB pin 2 reads high |
| [`vcu_gpio_board_init`](#vcu_gpio_board_init) | 0x0800248C | Board GPIO bring-up: configure the port A/B/C pin group, set levels, then init PA9 and PB6/PB7 |
| [`vcu_gpio_c14_set`](#vcu_gpio_c14_set) | 0x08008A0C | Drive GPIOC pin 14 high for a nonzero argument, low for zero |
| [`vcu_gpio_c15_set`](#vcu_gpio_c15_set) | 0x08008A28 | Drive GPIOC pin 15 high for a nonzero argument, low for zero |
| [`vcu_gpio_out_pins_config`](#vcu_gpio_out_pins_config) | 0x0800237C | Configure nine GPIO pins on ports A, B and C with packed config words |
| [`vcu_gpio_outputs_set_levels`](#vcu_gpio_outputs_set_levels) | 0x080022D4 | Drive 15 GPIO output pins to their start-up levels with the set and clear registers |
| [`vcu_gpio_pa0_init`](#vcu_gpio_pa0_init) | 0x08001E30 | Configure PA0 as a GPIO input with packed word 0x01080400 and enable the GPIOA clock |
| [`vcu_gpio_pa9_pb67_init`](#vcu_gpio_pa9_pb67_init) | 0x08002674 | Configure PA9, PB6 and PB7 with pull-up words, then drive PB6 and PB7 low |
| [`vcu_gpio_pa9_reset`](#vcu_gpio_pa9_reset) | 0x0800EDA4 | Drive GPIOA pin 9 low through the bit-clear register |
| [`vcu_gpio_pa9_set`](#vcu_gpio_pa9_set) | 0x0800ED94 | Drive GPIOA pin 9 high through the bit-set register |
| [`vcu_gpio_pb6_reset`](#vcu_gpio_pb6_reset) | 0x0800ED00 | Drive GPIOB pin 6 low through the bit-clear register |
| [`vcu_gpio_pb6_set`](#vcu_gpio_pb6_set) | 0x0800ECF4 | Drive GPIOB pin 6 high through the bit-set register |
| [`vcu_gpio_pb7_reset`](#vcu_gpio_pb7_reset) | 0x0800ED18 | Drive GPIOB pin 7 low through the bit-clear register |
| [`vcu_gpio_pb7_set`](#vcu_gpio_pb7_set) | 0x0800ED0C | Drive GPIOB pin 7 high through the bit-set register |
| [`vcu_gpio_pins_all_high`](#vcu_gpio_pins_all_high) | 0x0800D18E | Return 1 if every pin in the mask reads high on a GPIO port |
| [`vcu_pa11_pulse_step`](#vcu_pa11_pulse_step) | 0x0800854C | Step a 5-tick high then 1-tick low pulse on PA11 while DAT_20001fc0 is armed |
| [`vcu_pa1_input_high`](#vcu_pa1_input_high) | 0x08007A9C | Return 1 when GPIOA pin 0x2 (PA1) reads high |
| [`vcu_pa6_output_set`](#vcu_pa6_output_set) | 0x08005D9C | Drive GPIOA pin 6 high when the argument is nonzero, low when it is zero |
| [`vcu_pb11_input_active_low`](#vcu_pb11_input_active_low) | 0x08006994 | Return 1 when GPIOB pin 0x800 (PB11) reads low |
| [`vcu_pb12_input_active_low`](#vcu_pb12_input_active_low) | 0x08007AB8 | Return 1 when GPIOB pin 0x1000 (PB12) reads low |
| [`vcu_pb13_input_active_low`](#vcu_pb13_input_active_low) | 0x080056E8 | Return 1 when GPIOB pin 0x2000 (PB13) reads low |

## gpio_bits_reset

**Drive the selected GPIO port pins low through the write-only CLR register**

Stores the pin mask into the port's CLR register at offset 0x14 of the GPIO block. Writing 1 to a CLR bit drives that pin low and writing 0 has no effect, so only the selected pins change and no read-modify-write is needed. This is the Artery SDK gpio_bits_reset. It has many callers across the application (vcu_0159_080022d4 and others).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | GPIO port base (GPIOA..GPIOF register block) |
| `param_2` | `u16` | pin bit mask, bit n selects pin n |

- Addresses by version: 148: 0x0800C1E0, 14a: 0x0800C624, 14b: 0x0800CAB0, 14e: 0x0800CB44, 14f: 0x0800CC80, 152: 0x0800CF0C, 153: 0x0800D000, 0159: 0x0800D06C
- Peripheral registers: `GPIOC.CLR` (W)
- Called by: `vcu_gpio_outputs_set_levels`, `vcu_gpio_board_init`, `vcu_gpio_pa9_pb67_init`, `vcu_fault_warning_evaluate`, `vcu_0159_080047ac`, `vcu_pa6_output_set`, `vcu_pa11_pulse_step`, `vcu_gpio_c14_set`, `vcu_gpio_c15_set`, `vcu_0159_0800a39c`, `vcu_gpio_pb6_reset`, `vcu_gpio_pb7_reset` ...
- Confidence: high

## gpio_bits_set

**Drive the selected GPIO port pins high through the write-only SCR register**

Stores the pin mask into the port's SCR register at offset 0x10 of the GPIO block. Writing 1 to an SCR bit drives that pin high and writing 0 has no effect. This is the Artery SDK gpio_bits_set and is the counterpart of gpio_bits_reset (vcu_0159_0800d06c).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | GPIO port base (GPIOA..GPIOF register block) |
| `param_2` | `u16` | pin bit mask, bit n selects pin n |

- Addresses by version: 148: 0x0800C1E4, 14a: 0x0800C628, 14b: 0x0800CAB4, 14e: 0x0800CB48, 14f: 0x0800CC84, 152: 0x0800CF10, 153: 0x0800D004, 0159: 0x0800D070
- Peripheral registers: `GPIOC.SCR` (W)
- Called by: `vcu_gpio_outputs_set_levels`, `vcu_gpio_board_init`, `vcu_fault_warning_evaluate`, `vcu_0159_080047ac`, `vcu_pa6_output_set`, `vcu_pa11_pulse_step`, `vcu_gpio_c14_set`, `vcu_gpio_c15_set`, `vcu_0159_0800a39c`, `vcu_gpio_pb6_set`, `vcu_gpio_pb7_set`, `vcu_gpio_pa9_set`
- Confidence: high

## gpio_default_para_init

**Fill a gpio_init_type with defaults: all pins, input, push-pull, no pull, stronger drive**

Sets the 8-byte init structure to the Artery SDK defaults: gpio_pins = 0xFFFF (all 16 pins), gpio_mode = GPIO_MODE_INPUT (0), gpio_out_type = push-pull (0), gpio_pull = GPIO_PULL_NONE (0x04) and gpio_drive_strength = GPIO_DRIVE_STRENGTH_STRONGER (1). Callers such as the GPIO setup in vcu_0159_08001ca8 overwrite the fields they need and then call gpio_init (vcu_0159_0800d0e8). Field layout: u32 pins at +0, then bytes out_type +4, pull +5, mode +6, drive +7.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | gpio_init_type structure to fill (8 bytes) |

- Addresses by version: 148: 0x0800C1E8, 14a: 0x0800C62C, 14b: 0x0800CAB8, 14e: 0x0800CB4C, 14f: 0x0800CC88, 152: 0x0800CF14, 153: 0x0800D008, 0159: 0x0800D074
- Called by: `vcu_adc_analog_pins_init`, `vcu_gpio_pa0_init`, `vcu_usart2_pins_init`, `vcu_exint14_pb14_init`, `vcu_exint_pb12_pb14_init`, `vcu_gpio_out_pins_config`, `vcu_spi_pins_remap_init`, `vcu_exint3_pa3_init`, `vcu_can1_pins_remap_init`
- Confidence: high

## gpio_exint_line_config

**Route a GPIO port pin to an EXINT line by writing its 4-bit port field in IOMUX.EXINTCn**

Splits the pin number into a register index (pin >> 2, selecting IOMUX.EXINTC1..EXINTC4) and a 4-bit field position ((pin & 3) * 4). It clears that field and writes the port source value into it, so EXINT line 'pin' is driven by port 'port' (0 = GPIOA, 1 = GPIOB, ...). Other lines keep their settings. This is the Artery SDK gpio_exint_line_config Its callers include vcu_0159_080020a4, vcu_0159_080021c4 and vcu_0159_080026f0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | port source (0 = GPIOA ... 5 = GPIOF) |
| `param_2` | `u32` | pin number 0..15 within the port |

- Addresses by version: 148: 0x0800C200, 14a: 0x0800C644, 14b: 0x0800CAD0, 14e: 0x0800CB64, 14f: 0x0800CCA0, 152: 0x0800CF2C, 153: 0x0800D020, 0159: 0x0800D08C
- Peripheral registers: `IOMUX.EXINTC1` (RW), `IOMUX.EXINTC2` (RW), `IOMUX.EXINTC3` (RW), `IOMUX.EXINTC4` (RW)
- Called by: `vcu_exint14_pb14_init`, `vcu_exint_pb12_pb14_init`, `vcu_exint3_pa3_init`
- Confidence: high

## gpio_init

**Configure the mode, pull and drive of the selected pins in CFGLR/CFGHR**

Applies a gpio_init_type to the pins in its mask. Each pin owns a 4-bit nibble in CFGLR (pins 0..7) or CFGHR (pins 8..15), and the code writes the nibble from the structure: analog mode gives 0; input mode gives the pull field & 0xF (4 = floating) and also sets the output-data bit through SCR for GPIO_PULL_UP (0x18) or clears it through CLR for GPIO_PULL_DOWN (0x28); output and mux modes give (mode & 8) | (out_type & 4) | (drive & 3). The mask bits are walked one by one so untouched pins keep their configuration. This is the Artery SDK gpio_init. The structure layout is u32 pins at +0, out_type +4, pull +5, mode +6 and drive +7.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | GPIO port base |
| `param_2` | `ptr` | gpio_init_type: pins mask, output type, pull, mode and drive strength |

**Notes:** The decompiler shows the pull comparison against full byte values 0x18 and 0x28 (GPIO_PULL_UP and GPIO_PULL_DOWN in the SDK header).

- Addresses by version: 148: 0x0800C25C, 14a: 0x0800C6A0, 14b: 0x0800CB2C, 14e: 0x0800CBC0, 14f: 0x0800CCFC, 152: 0x0800CF88, 153: 0x0800D07C, 0159: 0x0800D0E8
- Called by: `vcu_adc_analog_pins_init`, `vcu_gpio_pa0_init`, `vcu_usart2_pins_init`, `vcu_exint14_pb14_init`, `vcu_exint_pb12_pb14_init`, `vcu_gpio_out_pins_config`, `vcu_spi_pins_remap_init`, `vcu_gpio_pa9_pb67_init`, `vcu_exint3_pa3_init`, `vcu_can1_pins_remap_init`
- Confidence: high

## gpio_pin_remap_config

**Set or clear a bit field in an IOMUX remap register, encoded in one 32-bit code**

Decodes a remap code: the top byte selects the IOMUX register, bits 23..16 give the field's bit offset, bits 15..8 its width and bits 7..0 the value to write. It clears the field and, when new_state is non-zero, ORs in the value shifted to the field position, so a remap is turned on or off with one call. This is the Artery SDK gpio_pin_remap_config. Each call is a read-modify-write of one IOMUX register, so it is not atomic.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | remap code: [31:24] IOMUX register index, [23:16] bit offset, [15:8] width, [7:0] value |
| `param_2` | `s32` | confirm_state: non-zero enables the remap, zero disables it |

- Addresses by version: 148: 0x0800C310, 14a: 0x0800C754, 14b: 0x0800CBE0, 14e: 0x0800CC74, 14f: 0x0800CDB0, 152: 0x0800D03C, 153: 0x0800D130, 0159: 0x0800D19C
- Peripheral registers: `IOMUX.EVTOUT` (A)
- Called by: `vcu_0159_08002060`, `vcu_spi_pins_remap_init`, `vcu_can1_pins_remap_init`
- Confidence: high

## vcu_gpio_b10_high_b2_low

**Return 1 when GPIOB pin 10 reads high and GPIOB pin 2 reads low**

Calls vcu_gpio_pins_all_high on GPIOB mask 0x400 (PB10), which must return 1, and then on mask 0x004 (PB2), which must return 0. The result is 1 only when both conditions hold, otherwise 0. The function has no side effects. It is the complement pair of vcu_gpio_b10_low_b2_high, so at most one of the two can return 1.

**Returns** `bool`: 1 when PB10 is high and PB2 is low

- Addresses by version: 148: 0x08007F88, 14a: 0x080083E4, 14b: 0x0800875C, 14e: 0x0800879C, 14f: 0x080087F8, 152: 0x080088BC, 153: 0x08008958, 0159: 0x080089BC
- Peripheral registers: `GPIOB.CFGLR` (A)
- Called by: `vcu_input_sm_d_tick`
- Calls: `vcu_gpio_pins_all_high`
- Confidence: high

## vcu_gpio_b10_low_b2_high

**Return 1 when GPIOB pin 10 reads low and GPIOB pin 2 reads high**

The mirror of vcu_gpio_b10_high_b2_low: vcu_gpio_pins_all_high on GPIOB mask 0x004 (PB2) must return 1 and on mask 0x400 (PB10) must return 0. Returns 1 only when PB10 is low and PB2 is high, otherwise 0, with no side effects.

**Returns** `bool`: 1 when PB10 is low and PB2 is high

- Addresses by version: 148: 0x08007FB0, 14a: 0x0800840C, 14b: 0x08008784, 14e: 0x080087C4, 14f: 0x08008820, 152: 0x080088E4, 153: 0x08008980, 0159: 0x080089E4
- Peripheral registers: `GPIOB.CFGLR` (A)
- Called by: `vcu_input_sm_e_tick`
- Calls: `vcu_gpio_pins_all_high`
- Confidence: high

## vcu_gpio_board_init

**Board GPIO bring-up: configure the port A/B/C pin group, set levels, then init PA9 and PB6/PB7**

Board GPIO bring-up for one hardware variant. It calls vcu_0159_0800237c to configure the nine-pin group, then drives PA10, PA12 and PA8 high and PA11, PC13, PC14, PC15 and PA6 low. It then calls vcu_0159_08002674 to configure PA9, PB6 and PB7. The caller is vcu_0159_08002060, the init sequence.

**Notes:** Levels differ from vcu_0159_080022d4 for PA10 (high here, low there), so the two are different variants of the same board setup.

- Addresses by version: 148: 0x080020A0, 14a: 0x08002110, 14b: 0x080023EC, 14e: 0x080023EC, 14f: 0x08002448, 152: 0x08002484, 153: 0x080024A0, 0159: 0x0800248C
- Peripheral registers: `GPIOA.CFGLR` (A), `GPIOC.CFGLR` (A)
- Called by: `vcu_0159_08002060`
- Calls: `vcu_gpio_out_pins_config`, `vcu_gpio_pa9_pb67_init`, `gpio_bits_reset`, `gpio_bits_set`
- Confidence: high

## vcu_gpio_c14_set

**Drive GPIOC pin 14 high for a nonzero argument, low for zero**

A nonzero argument calls gpio_bits_set on GPIOC; zero calls gpio_bits_reset(&GPIOC, 0x4000), which drives PC14 low. The set branch in the decompile passes only the port, so the pin mask is inferred as the same 0x4000 used by the reset branch. Used by vcu_c14_c15_blink_step and by the other paths listed in the packet callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | nonzero to drive the pin high, zero to drive it low |

**Notes:** The pin argument of the set call is not visible in the decompile; 0x4000 is inferred.

- Addresses by version: 148: 0x08007FD8, 14a: 0x08008434, 14b: 0x080087AC, 14e: 0x080087EC, 14f: 0x08008848, 152: 0x0800890C, 153: 0x080089A8, 0159: 0x08008A0C
- Peripheral registers: `GPIOC.CFGLR` (A)
- Called by: `vcu_pair_pulse_pattern_step`, `vcu_0159_080042f8`, `vcu_0159_080047ac`, `vcu_0159_080057ac`, `vcu_0159_08005938`, `vcu_c14_c15_blink_step`
- Calls: `gpio_bits_reset`, `gpio_bits_set`
- Confidence: medium

## vcu_gpio_c15_set

**Drive GPIOC pin 15 high for a nonzero argument, low for zero**

Same behaviour as vcu_gpio_c14_set on the other pin: nonzero calls gpio_bits_set on GPIOC, zero calls gpio_bits_reset(&GPIOC, 0x8000), so PC15 is the pin. Used together with PC14 by vcu_c14_c15_blink_step.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | nonzero to drive the pin high, zero to drive it low |

**Notes:** The pin argument of the set call is not visible in the decompile; 0x8000 is inferred from the reset branch.

- Addresses by version: 148: 0x08007FF4, 14a: 0x08008450, 14b: 0x080087C8, 14e: 0x08008808, 14f: 0x08008864, 152: 0x08008928, 153: 0x080089C4, 0159: 0x08008A28
- Peripheral registers: `GPIOC.CFGLR` (A)
- Called by: `vcu_pair_pulse_pattern_step`, `vcu_0159_080042f8`, `vcu_0159_080047ac`, `vcu_0159_080057ac`, `vcu_0159_08005938`, `vcu_c14_c15_blink_step`
- Calls: `gpio_bits_reset`, `gpio_bits_set`
- Confidence: medium

## vcu_gpio_out_pins_config

**Configure nine GPIO pins on ports A, B and C with packed config words**

Enables the IOMUX and GPIOA, GPIOB and GPIOC clocks, then configures PA10, PA11, PA12, PC14, PC15, PB15, PA8, PC13 and PA6 through gpio_default_para_init and gpio_init. Most pins use packed word 0x01100400, and PA6 uses 0x01102800. The call is one of two pin-group setups, and vcu_0159_0800248c calls it and then drives the levels. The decompiler shows four argument registers that the caller does not set, so the word values are recorded rather than fully decoded.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | not used by the routine |
| `param_2` | `u32` | not used by the routine |
| `param_3` | `u32` | packed config word low (register leftover) |
| `param_4` | `u32` | packed config word high (register leftover) |

**Notes:** The per-pin mode bytes are overwritten by the routine, so only the pin masks are certain.

- Addresses by version: 148: 0x08001F90, 14a: 0x08002000, 14b: 0x080022DC, 14e: 0x080022DC, 14f: 0x08002338, 152: 0x08002374, 153: 0x08002390, 0159: 0x0800237C
- Peripheral registers: `GPIOA.CFGLR` (A), `GPIOB.CFGLR` (A), `GPIOC.CFGLR` (A)
- Called by: `vcu_gpio_board_init`
- Calls: `crm_periph_clock_enable`, `gpio_default_para_init`, `gpio_init`
- Confidence: medium

## vcu_gpio_outputs_set_levels

**Drive 15 GPIO output pins to their start-up levels with the set and clear registers**

Sets the start-up level of 15 output pins using gpio_bits_reset (CLR register) and gpio_bits_set (SCR register). Driven low: PA10, PA11, PA6, PA9, PB6, PB7, PC14, PC15 and PF6. Driven high: PA12, PA15, PB3, PB4, PB5 and PC13. The pins are configured elsewhere in the init sequence, and the function is called from vcu_0159_0800688c.

**Notes:** The pins' functions (power, enable or reset lines) are not determinable from this function. Levels here differ from vcu_0159_0800248c for PA10, PA11 and PA8, which are used by a different init path.

- Addresses by version: 148: 0x08001EE8, 14a: 0x08001F58, 14b: 0x08002234, 14e: 0x08002234, 14f: 0x08002290, 152: 0x080022CC, 153: 0x080022E8, 0159: 0x080022D4
- Peripheral registers: `GPIOA.CFGLR` (A), `GPIOB.CFGLR` (A), `GPIOC.CFGLR` (A), `GPIOF.CFGLR` (A)
- Called by: `vcu_0159_0800688c`
- Calls: `gpio_bits_reset`, `gpio_bits_set`
- Confidence: high

## vcu_gpio_pa0_init

**Configure PA0 as a GPIO input with packed word 0x01080400 and enable the GPIOA clock**

Enables the GPIOA clock and configures pin 0 (PA0) through gpio_default_para_init and gpio_init, using the packed mode word 0x01080400. The word has no pull and drive strength 1, which matches the SDK default drive. It is called from vcu_0159_08001e6c and from vcu_14a_08001af0. The purpose of PA0 is not visible in this routine.

**Notes:** The input direction is inferred from the packed word; the function's use of PA0 is unknown.

- Addresses by version: 148: 0x08001A4C, 14a: 0x08001AB4, 14b: 0x08001D68, 14e: 0x08001D68, 14f: 0x08001DC4, 152: 0x08001E00, 153: 0x08001E1C, 0159: 0x08001E30
- Peripheral registers: `GPIOA.CFGLR` (A)
- Called by: `vcu_0159_08001e6c`
- Calls: `crm_periph_clock_enable`, `gpio_default_para_init`, `gpio_init`
- Confidence: medium

## vcu_gpio_pa9_pb67_init

**Configure PA9, PB6 and PB7 with pull-up words, then drive PB6 and PB7 low**

Enables the GPIOA and GPIOB clocks and configures PA9 (mask 0x200) and PB6 and PB7 (masks 0x40 and 0x80) with the same packed word 0x01101800, which includes a pull-up setting, through gpio_init. It then drives PB6 and PB7 low with gpio_bits_reset. The peripheral that uses these pins is not configured in this function. It is called from vcu_0159_0800248c and vcu_0159_080047ac.

**Notes:** PA9 is the default USART1 TX pin and PB6/PB7 are common USART1 or I2C1 pins; neither is confirmed here.

- Addresses by version: 148: 0x080022AC, 14a: 0x0800231C, 14b: 0x080025D4, 14e: 0x080025D4, 14f: 0x08002630, 152: 0x0800266C, 153: 0x08002688, 0159: 0x08002674
- Peripheral registers: `GPIOA.CFGLR` (A), `GPIOB.CFGLR` (A)
- Called by: `vcu_gpio_board_init`, `vcu_0159_080047ac`
- Calls: `crm_periph_clock_enable`, `gpio_bits_reset`, `gpio_init`
- Confidence: medium

## vcu_gpio_pa9_reset

**Drive GPIOA pin 9 low through the bit-clear register**

Calls gpio_bits_reset(GPIOA, 0x0200), the low counterpart of vcu_gpio_pa9_set. Same callers: vcu_0159_080057ac and vcu_0159_0800ed4c.

- Addresses by version: 148: 0x0800DD80, 14a: 0x0800E21C, 14b: 0x0800E6AC, 14e: 0x0800E74C, 14f: 0x0800E898, 152: 0x0800EB40, 153: 0x0800EC34, 0159: 0x0800EDA4
- Peripheral registers: `GPIOA.CFGLR` (A)
- Called by: `vcu_0159_080057ac`, `vcu_0159_0800ed4c`
- Calls: `gpio_bits_reset`
- Confidence: high

## vcu_gpio_pa9_set

**Drive GPIOA pin 9 high through the bit-set register**

Calls gpio_bits_set(GPIOA, 0x0200). PA9 is a separate output line whose role is not visible in this packet; its callers are vcu_0159_080057ac and vcu_0159_0800ed4c.

- Addresses by version: 148: 0x0800DD70, 14a: 0x0800E20C, 14b: 0x0800E69C, 14e: 0x0800E73C, 14f: 0x0800E888, 152: 0x0800EB30, 153: 0x0800EC24, 0159: 0x0800ED94
- Peripheral registers: `GPIOA.CFGLR` (A)
- Called by: `vcu_0159_080057ac`, `vcu_0159_0800ed4c`
- Calls: `gpio_bits_set`
- Confidence: high

## vcu_gpio_pb6_reset

**Drive GPIOB pin 6 low through the bit-clear register**

Calls gpio_bits_reset(GPIOB, 0x0040), which writes bit 6 to the GPIOB clear register so PB6 goes low. Within vcu_0159_0800ed24 it starts each clock pulse.

- Addresses by version: 148: 0x0800DCDC, 14a: 0x0800E178, 14b: 0x0800E608, 14e: 0x0800E6A8, 14f: 0x0800E7F4, 152: 0x0800EA9C, 153: 0x0800EB90, 0159: 0x0800ED00
- Peripheral registers: `GPIOB.CFGLR` (A)
- Called by: `led_driver_shift_out_byte`
- Calls: `gpio_bits_reset`
- Confidence: high

## vcu_gpio_pb6_set

**Drive GPIOB pin 6 high through the bit-set register**

Calls gpio_bits_set(GPIOB, 0x0040), which writes bit 6 to the GPIOB set register so PB6 goes high without a read-modify-write. Within vcu_0159_0800ed24 PB6 is the clock of the byte shifter, so this call ends each clock pulse.

- Addresses by version: 148: 0x0800DCD0, 14a: 0x0800E16C, 14b: 0x0800E5FC, 14e: 0x0800E69C, 14f: 0x0800E7E8, 152: 0x0800EA90, 153: 0x0800EB84, 0159: 0x0800ECF4
- Peripheral registers: `GPIOB.CFGLR` (A)
- Called by: `vcu_0159_080057ac`, `led_driver_shift_out_byte`
- Calls: `gpio_bits_set`
- Confidence: high

## vcu_gpio_pb7_reset

**Drive GPIOB pin 7 low through the bit-clear register**

Calls gpio_bits_reset(GPIOB, 0x0080). This is the data-low case used by the byte shifter vcu_0159_0800ed24.

- Addresses by version: 148: 0x0800DCF4, 14a: 0x0800E190, 14b: 0x0800E620, 14e: 0x0800E6C0, 14f: 0x0800E80C, 152: 0x0800EAB4, 153: 0x0800EBA8, 0159: 0x0800ED18
- Peripheral registers: `GPIOB.CFGLR` (A)
- Called by: `led_driver_shift_out_byte`
- Calls: `gpio_bits_reset`
- Confidence: high

## vcu_gpio_pb7_set

**Drive GPIOB pin 7 high through the bit-set register**

Calls gpio_bits_set(GPIOB, 0x0080). PB7 is the data line of the byte shifter vcu_0159_0800ed24, where it is high for a 1 bit.

- Addresses by version: 148: 0x0800DCE8, 14a: 0x0800E184, 14b: 0x0800E614, 14e: 0x0800E6B4, 14f: 0x0800E800, 152: 0x0800EAA8, 153: 0x0800EB9C, 0159: 0x0800ED0C
- Peripheral registers: `GPIOB.CFGLR` (A)
- Called by: `vcu_0159_080057ac`, `led_driver_shift_out_byte`
- Calls: `gpio_bits_set`
- Confidence: high

## vcu_gpio_pins_all_high

**Return 1 if every pin in the mask reads high on a GPIO port**

Computes (mask & ~IDT) == 0, where IDT is the port input data register at offset 0x08 of the GPIO block. The function therefore returns true only when all selected pins are high, and an empty mask gives true. Its callers pass single pins or pin pairs on GPIOA and GPIOB. It does not change any state.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | GPIO port base |
| `param_2` | `u32` | pin bit mask to test |

**Returns** `bool`: 1 when all masked pins read high, else 0

- Addresses by version: 148: 0x0800C302, 14a: 0x0800C746, 14b: 0x0800CBD2, 14e: 0x0800CC66, 14f: 0x0800CDA2, 152: 0x0800D02E, 153: 0x0800D122, 0159: 0x0800D18E
- Called by: `vcu_pb13_input_active_low`, `vcu_pb11_input_active_low`, `vcu_pa1_input_high`, `vcu_pb12_input_active_low`, `vcu_gpio_b10_high_b2_low`, `vcu_gpio_b10_low_b2_high`, `vcu_0159_08009fa4`
- Confidence: high

## vcu_pa11_pulse_step

**Step a 5-tick high then 1-tick low pulse on PA11 while DAT_20001fc0 is armed**

Returns 1 on the call that finishes the pulse and 0 otherwise. While DAT_20001fc0 equals 1 the step counter DAT_20001fc2 advances on each call. The first five calls drive PA11 high through FUN_0800d070 (gpio_bits_set); the sixth call drives it low with gpio_bits_reset(&GPIOA, 0x800), clears DAT_20001fc2 and DAT_20001fc0, and returns 1. Each call is one tick of a fixed 5-high, 1-low pattern.

**Returns** `bool`: true on the call that completes the pulse

**Notes:** The set call in the decompile shows only the port argument, so the pin mask 0x800 is inferred from the reset call in the same function. PA11 is shared with USB D- and CAN1 RX on this part; which role this pulse serves is not established here.

- Addresses by version: 148: 0x08007B58, 14a: 0x08007F94, 14b: 0x080082EC, 14e: 0x0800832C, 14f: 0x08008388, 152: 0x0800844C, 153: 0x080084E8, 0159: 0x0800854C
- Peripheral registers: `GPIOA.CFGLR` (A)
- Called by: `vcu_0159_080047ac`
- Calls: `gpio_bits_reset`, `gpio_bits_set`
- Confidence: medium

## vcu_pa1_input_high

**Return 1 when GPIOA pin 0x2 (PA1) reads high**

Calls vcu_gpio_pins_all_high on GPIOA with mask 0x2 and returns 1 when PA1 is high, 0 when it is low. Called from vcu_0159_080020a4, which is outside this packet.

**Returns** `u32`: 1 when PA1 is high, else 0

- Addresses by version: 14a: 0x080074AC, 14b: 0x08007810, 14e: 0x08007848, 14f: 0x080078A4, 152: 0x08007968, 153: 0x08007A04, 0159: 0x08007A9C
- Peripheral registers: `GPIOA.CFGLR` (A)
- Called by: `vcu_exint14_pb14_init`
- Calls: `vcu_gpio_pins_all_high`
- Confidence: high

## vcu_pa6_output_set

**Drive GPIOA pin 6 high when the argument is nonzero, low when it is zero**

Writes GPIOA pin 0x40 (PA6) with gpio_bits_set when the argument is nonzero and with gpio_bits_reset when it is zero. It is the only function that touches that pin in this packet, and both the output controller vcu_pa6_output_status_update and the special-mode gate use it.

| Parameter | Type | Description |
|---|---|---|
| `high` | `u32` | nonzero drives PA6 high, zero drives it low |

- Addresses by version: 148: 0x0800539C, 14a: 0x08005788, 14b: 0x08005AB0, 14e: 0x08005AE8, 14f: 0x08005B44, 152: 0x08005B9C, 153: 0x08005C38, 0159: 0x08005D9C
- Peripheral registers: `GPIOA.CFGLR` (A)
- Called by: `vcu_pa6_output_status_update`, `vcu_0159_080047ac`, `vcu_0159_080057ac`, `vcu_0159_08005938`, `vcu_0159_08008614`, `vcu_double_pulse_indicator_step`
- Calls: `gpio_bits_reset`, `gpio_bits_set`
- Confidence: high

## vcu_pb11_input_active_low

**Return 1 when GPIOB pin 0x800 (PB11) reads low**

Calls vcu_gpio_pins_all_high on GPIOB with mask 0x800 and returns 1 only when PB11 is low, so the input is active-low. Returns 0 when PB11 is high. Called from vcu_0159_0800809c, which is outside this packet.

**Returns** `u32`: 1 when PB11 is low, else 0

- Addresses by version: 148: 0x08005F40, 14a: 0x08006360, 14b: 0x080066D0, 14e: 0x08006708, 14f: 0x08006764, 152: 0x08006808, 153: 0x080068A4, 0159: 0x08006994
- Peripheral registers: `GPIOB.CFGLR` (A)
- Called by: `vcu_input_sm_b_tick`
- Calls: `vcu_gpio_pins_all_high`
- Confidence: high

## vcu_pb12_input_active_low

**Return 1 when GPIOB pin 0x1000 (PB12) reads low**

Calls vcu_gpio_pins_all_high on GPIOB with mask 0x1000 and returns 1 only when PB12 is low, so the input is active-low. Returns 0 when PB12 is high. Called from several places outside this packet.

**Returns** `u32`: 1 when PB12 is low, else 0

- Addresses by version: 148: 0x0800708C, 14a: 0x080074C8, 14b: 0x0800782C, 14e: 0x08007864, 14f: 0x080078C0, 152: 0x08007984, 153: 0x08007A20, 0159: 0x08007AB8
- Peripheral registers: `GPIOB.CFGLR` (A)
- Called by: `vcu_0159_080047ac`, `vcu_0159_08007ecc`, `vcu_input_sm_c_tick`, `vcu_0159_0800a120`, `vcu_0159_0800a39c`
- Calls: `vcu_gpio_pins_all_high`
- Confidence: high

## vcu_pb13_input_active_low

**Return 1 when GPIOB pin 0x2000 (PB13) reads low**

Calls vcu_gpio_pins_all_high on GPIOB with mask 0x2000 and returns 1 only when PB13 is low, so the input is active-low. Returns 0 when PB13 is high. The only caller in the family is vcu_0159_08007e28, which is outside this packet.

**Returns** `u32`: 1 when PB13 is low, else 0

- Addresses by version: 148: 0x08004DC0, 14a: 0x08005150, 14b: 0x08005478, 14e: 0x080054B0, 14f: 0x0800550C, 152: 0x0800556C, 153: 0x08005584, 0159: 0x080056E8
- Peripheral registers: `GPIOB.CFGLR` (A)
- Called by: `vcu_input_sm_a_tick`
- Calls: `vcu_gpio_pins_all_high`
- Confidence: high
