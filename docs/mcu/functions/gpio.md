# MCU - `gpio` functions

3 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`gpio_pin_remap_config`](#gpio_pin_remap_config) | 0x0800CF94 | Set or clear one bit field of an IOMUX remap register from a packed remap code |
| [`mcu_gpio_cfg_shadow_build`](#mcu_gpio_cfg_shadow_build) | 0x0800CEE2 | Fold a pin configuration record into the 4-bit pin nibbles of two shadow config words |
| [`mcu_poll_pc9_input_and_flag`](#mcu_poll_pc9_input_and_flag) | 0x080059D0 | Sample GPIOC PC9 (active low) into a flag byte and mirror a flag bit into status bit 3 |

## gpio_pin_remap_config

**Set or clear one bit field of an IOMUX remap register from a packed remap code**

SDK gpio_pin_remap_config. The register is the IOMUX base plus the top byte of the code (the packet shows IOMUX.EVTOUT). The field offset is bits 16..23, the field width is bits 8..15 and the value is the low byte. The field mask is built as in the SDK, cleared, and if new_state is set the value is ORed in at the field offset. The remap codes are packed constants, so each remap function passes its own code.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | packed remap code: register offset in bits 24..31, bit offset 16..23, width 8..15, value 0..7 |
| `param_2` | `bool` | new state: true sets the value, false only clears the field |

- Addresses by version: 12b: 0x0800CC70, 143: 0x0800CEEC, 152: 0x0800CF34, 0160: 0x0800CF94
- Peripheral registers: `IOMUX.EVTOUT` (A)
- Called by: `mcu_0160_0800325c`, `mcu_0160_08009800`
- Confidence: high

## mcu_gpio_cfg_shadow_build

**Fold a pin configuration record into the 4-bit pin nibbles of two shadow config words**

Applies one pin configuration record to a shadow of two 32-bit words, where each pin owns a 4-bit nibble. Word 0 holds pins 0..7 and word 1 holds pins 8..15, like the GPIO CFGLR and CFGHR layout. The 16-bit pin mask is the halfword at record+0. The nibble value follows the SDK gpio_init rule: analog mode (mode byte +6 = 3) gives 0, input mode (0) takes the low four bits of byte +5, and other modes give (mode & 8) | (out type byte +4 & 4) | (drive byte +7 & 3). For input records whose byte +5 is 0x18 or 0x28 the pin mask is also stored at shadow +0x10 or +0x14, most likely the pull-up and pull-down (set and clear) masks. Nothing is written to a peripheral register here.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | shadow block: nibble words at +0 (pins 0..7) and +4 (pins 8..15), pin masks at +0x10 and +0x14 |
| `param_2` | `ptr` | pin record: pin mask u16 +0, out type byte +4, pull byte +5, mode byte +6, drive byte +7 |

**Notes:** The record layout is taken from the code, not from a header. The 0x18 and 0x28 pull codes and the +0x10 and +0x14 mask roles are guesses from gpio_init semantics.

- Addresses by version: 12b: 0x0800CBBE, 143: 0x0800CE3A, 152: 0x0800CE82, 0160: 0x0800CEE2
- Called by: `mcu_0160_08006524`, `mcu_0160_0800c058`
- Confidence: low

## mcu_poll_pc9_input_and_flag

**Sample GPIOC PC9 (active low) into a flag byte and mirror a flag bit into status bit 3**

Reads GPIOC.IDT (0x40011008) and stores the inverted level of bit 9 (PC9) as a 0/1 byte at 0x200001BD. It then rewrites bit 3 of the 16-bit status word at 0x20001FEE with bit 0 of the byte at 0x20000E1C, leaving the other bits unchanged. Called from mcu_0160_0800a320, which runs the input and status service.

**Notes:** Register behaviour is certain (active-low via the ~ operator). The function of PC9 on this board is not identified.

- Addresses by version: 12b: 0x080059BC, 143: 0x080058C0, 152: 0x08005930, 0160: 0x080059D0
- Peripheral registers: `GPIOC.IDT` (R)
- Called by: `mcu_0160_0800a320`
- Confidence: high
