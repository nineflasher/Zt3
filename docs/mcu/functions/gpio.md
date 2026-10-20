# MCU - `gpio` functions

12 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`gpio_pin_remap_config`](#gpio_pin_remap_config) | 0x0800CF94 | Set or clear one bit field of an IOMUX remap register from a packed remap code |
| [`mcu_gpio_cfg_shadow_build`](#mcu_gpio_cfg_shadow_build) | 0x0800CEE2 | Fold a pin configuration record into the 4-bit pin nibbles of two shadow config words |
| [`mcu_gpio_pin_setup`](#mcu_gpio_pin_setup) | 0x08006524 | Enable a port clock and fold one pin group's mode settings into the port's shadow config |
| [`mcu_gpio_port_clock_enable`](#mcu_gpio_port_clock_enable) | 0x080064B4 | Enable the APB2 clock of GPIO port A, B, C, D or F from its peripheral pointer |
| [`mcu_gpioa_pin_cfg_init`](#mcu_gpioa_pin_cfg_init) | 0x0800C058 | Enable the GPIOA clock and build the shadow configuration for PA11 and PA12 |
| [`mcu_gpioc_pin10_follow_flag`](#mcu_gpioc_pin10_follow_flag) | 0x08006624 | Drive GPIOC pin 10 from bit 0x200 of the word at 0x20001FD4 through SCR or CLR |
| [`mcu_indicator_update`](#mcu_indicator_update) | 0x0800A90C | Drive the GPIOC.8 and GPIOB.2 indicator pins from request bits and latch fault 0x4 after 50 ticks |
| [`mcu_poll_pc9_input_and_flag`](#mcu_poll_pc9_input_and_flag) | 0x080059D0 | Sample GPIOC PC9 (active low) into a flag byte and mirror a flag bit into status bit 3 |
| [`mcu_pulse_burst_decode`](#mcu_pulse_burst_decode) | 0x08006B70 | Decode a sampled input into a pulse count per burst, or 0xFF after a long high level |
| [`mcu_pulse_burst_decoder_init`](#mcu_pulse_burst_decoder_init) | 0x08008998 | Initialise the PC3 pulse-burst decoder: 6-sample debounce, gap 40, long high 400 |
| [`mcu_pulse_burst_sample_pc3`](#mcu_pulse_burst_sample_pc3) | 0x08008978 | Sample GPIOC pin 3 into the pulse-burst decoder and store its result at 0x20002026 |
| [`mcu_status_drive_pb6_pc11`](#mcu_status_drive_pb6_pc11) | 0x080089CC | Drive GPIOB pin 6 from status bit 0x1000 and GPIOC pin 11 from bits 0x180 of 0x20001FDA |

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
- Called by: `mcu_gpio_pin_setup`, `mcu_gpioa_pin_cfg_init`
- Confidence: low

## mcu_gpio_pin_setup

**Enable a port clock and fold one pin group's mode settings into the port's shadow config**

When the port pointer is not null it enables the port clock through mcu_0160_080064b4 and builds an 8-byte record: the pin mask (param_2, low halfword) at +0, the output type (param_4) at +4, the pull or input byte (param_5) at +5, the mode (param_3) at +6, and the drive value 1 at +7. It passes the record and the port pointer to mcu_gpio_cfg_shadow_build, which converts the mode and pin mask into CFGLR and CFGHR nibbles. A null port does nothing. The routine itself writes no peripheral register.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | GPIO port pointer, 0 to skip |
| `param_2` | `u32` | pin mask in the low halfword |
| `param_3` | `u8` | pin mode |
| `param_4` | `u8` | output type |
| `param_5` | `u8` | pull or input configuration |

**Notes:** The pin-mode and pull semantics come from the low-confidence description of mcu_gpio_cfg_shadow_build. Callers include mcu_0160_08001fb0, 08002068, 08003060, 08006028, 08009800, 0800A6B8 and 0800A9DC.

- Addresses by version: 12b: 0x0800659C, 143: 0x08006454, 152: 0x08006484, 0160: 0x08006524
- Called by: `mcu_0160_08001fb0`, `mcu_0160_08002068`, `mcu_0160_08003060`, `mcu_0160_08006028`, `mcu_0160_08009800`, `mcu_0160_0800a6b8`, `mcu_0160_0800a9dc`
- Calls: `mcu_gpio_port_clock_enable`, `mcu_gpio_cfg_shadow_build`
- Confidence: medium

## mcu_gpio_port_clock_enable

**Enable the APB2 clock of GPIO port A, B, C, D or F from its peripheral pointer**

Maps the GPIO peripheral pointer to its clock-enable bit in the APB2 enable register (CRM offset 0x18): GPIOA bit 2, GPIOB bit 3, GPIOC bit 4, GPIOD bit 5 and GPIOF bit 7. It calls crm_periph_clock_enable with the packed register and bit codes 0x180002, 0x180003, 0x180004, 0x180005 or 0x180007 and enable 1. GPIOE and unknown pointers are ignored, and the routine never disables a clock.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | GPIO peripheral pointer (GPIO_Type) |

- Addresses by version: 12b: 0x0800652C, 143: 0x080063E4, 152: 0x08006414, 0160: 0x080064B4
- Called by: `mcu_gpio_pin_setup`
- Calls: `crm_periph_clock_enable`
- Confidence: high

## mcu_gpioa_pin_cfg_init

**Enable the GPIOA clock and build the shadow configuration for PA11 and PA12**

Enables the GPIOA bus clock (crm_periph_clock_enable with code 0x180002), fills an 8-byte pin record with mcu_rec8_reset_defaults, and then folds two pin configurations into the shadow CFGLR words through mcu_gpio_cfg_shadow_build: pin mask 0x1000 (PA12) with its fixed mode and pull bytes, then pin mask 0x800 (PA11) with its own bytes. The GPIOA.CFGLR register is written from those shadow words later. PA11 and PA12 are the CAN1 RX and TX pins on the default remap, so this is the CAN1 pin setup, an inference from the pin numbers.

**Notes:** The exact per-pin mode and pull codes are not decoded in this packet.

- Addresses by version: 12b: 0x0800BD44, 143: 0x0800BFF4, 152: 0x0800BFF8, 0160: 0x0800C058
- Peripheral registers: `GPIOA.CFGLR` (A)
- Called by: `mcu_can_init`, `mcu_0160_0800dc08`
- Calls: `crm_periph_clock_enable`, `mcu_rec8_reset_defaults`, `mcu_gpio_cfg_shadow_build`
- Confidence: medium

## mcu_gpioc_pin10_follow_flag

**Drive GPIOC pin 10 from bit 0x200 of the word at 0x20001FD4 through SCR or CLR**

If bit 0x200 of the word at 0x20001FD4 is set, it writes mask 0x400 to the GPIOC set register (SCR, offset 0x10) to drive pin 10 high. Otherwise it writes 0x400 to the GPIOC clear register (CLR, offset 0x14) to drive it low. Each write goes through one of the setter helpers mcu_ctx_set_field_0x10 or mcu_ctx_set_field_0x14, so exactly one register is written per call. This is an output mirror of a status flag that sits in the 0x20001FD2 block refreshed by the 0x100 frame in mcu_0160_080085bc.

**Notes:** The packet's register list names GPIOC.CFGLR, but the code writes SCR and CLR, and the register file confirms those offsets.

- Addresses by version: 12b: 0x0800668C, 143: 0x08006554, 152: 0x08006584, 0160: 0x08006624
- Peripheral registers: `GPIOC.CFGLR` (A)
- Called by: `mcu_0160_0800a320`
- Calls: `mcu_ctx_set_field_0x14`, `mcu_ctx_set_field_0x10`
- Confidence: high

## mcu_indicator_update

**Drive the GPIOC.8 and GPIOB.2 indicator pins from request bits and latch fault 0x4 after 50 ticks**

Called once per tick. GPIOC pin 8 (mask 0x100) follows bit 0 of the request byte at 0x20001FDA, and GPIOB pin 2 (mask 0x4) follows bit 1, written through the set register (GPIO offset 0x10, via mcu_ctx_set_field_0x10) and the clear register (offset 0x14, via mcu_ctx_set_field_0x14). When neither request bit is set it clears the counter at 0x20000679 and bit 2 (0x4) of the status word 0x20001FF8. Otherwise it reads the 16-bit value from mcu_get_var_f60 (0x20000F60). Above 299 the counter and the latch are cleared. At 299 or below, the counter counts up to 50 ticks and then sets bit 2 of 0x20001FF8, which latches the indication.

**Notes:** The role of the two pins and of the latch bit in the wider system is inferred from the code shape only.

- Addresses by version: 12b: 0x0800A7A8, 143: 0x0800A9DC, 152: 0x0800A898, 0160: 0x0800A90C
- Peripheral registers: `GPIOB.CFGLR` (A), `GPIOC.CFGLR` (A)
- Called by: `mcu_hall_dispatch_pc12_output`
- Calls: `mcu_get_var_f60`, `mcu_ctx_set_field_0x14`, `mcu_ctx_set_field_0x10`
- Confidence: medium

## mcu_poll_pc9_input_and_flag

**Sample GPIOC PC9 (active low) into a flag byte and mirror a flag bit into status bit 3**

Reads GPIOC.IDT (0x40011008) and stores the inverted level of bit 9 (PC9) as a 0/1 byte at 0x200001BD. It then rewrites bit 3 of the 16-bit status word at 0x20001FEE with bit 0 of the byte at 0x20000E1C, leaving the other bits unchanged. Called from mcu_0160_0800a320, which runs the input and status service.

**Notes:** Register behaviour is certain (active-low via the ~ operator). The function of PC9 on this board is not identified.

- Addresses by version: 12b: 0x080059BC, 143: 0x080058C0, 152: 0x08005930, 0160: 0x080059D0
- Peripheral registers: `GPIOC.IDT` (R)
- Called by: `mcu_0160_0800a320`
- Confidence: high

## mcu_pulse_burst_decode

**Decode a sampled input into a pulse count per burst, or 0xFF after a long high level**

Operates on the decoder object at param_1, whose layout is set by mcu_pulse_burst_decoder_init. It steps the object's edge counter with mcu_edge_counter_step, which gives a debounced level, and then tracks rising edges (count at +0x24), high time in calls (+0x20) and low time in calls (+0x18). A rising edge resets the low counter and clears the done flag at +0x29. After a falling edge the low counter counts up until it reaches the gap threshold at +0x14; the routine then returns the burst's rising-edge count, clears it, and sets the done flag. If the level stays high for at least the threshold at +0x1C calls it returns 0xFF, and a falling edge after such a long high calls mcu_ctrl_block_reset_flags and returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pulse decoder object (0x20001FFC in this build) |

**Returns** `u8`: 0 while idle, the burst's rising-edge count when a burst ends, or 0xFF after a long high

**Notes:** The direction argument of mcu_edge_counter_step is not a parameter of this routine. Its only caller, mcu_0160_08008978, leaves bit 3 of GPIOC.IDT in r1, so the counter follows pin PC3. Group with mcu_pulse_burst_sample_pc3 and mcu_pulse_burst_decoder_init.

- Addresses by version: 12b: 0x08006CC4, 143: 0x08006B98, 152: 0x08006BC8, 0160: 0x08006B70
- Called by: `mcu_pulse_burst_sample_pc3`
- Calls: `mcu_ctrl_block_reset_flags`, `mcu_edge_counter_step`
- Confidence: medium

## mcu_pulse_burst_decoder_init

**Initialise the PC3 pulse-burst decoder: 6-sample debounce, gap 40, long high 400**

Calls mcu_edge_counter_init on the decoder object at 0x20001FFC with limit 6, reload 6 and output mode 1 (phase high), so the counter output changes only after six consecutive steps in one direction. It then sets the gap threshold to 40 calls at +0x14 and the long-high threshold to 400 calls at +0x1C, and clears the low and high counters at +0x18 and +0x20, the pulse count at +0x24, the last level at +0x28 and the done flag at +0x29. It returns 1.

**Returns** `u32`: always 1

**Notes:** Group with mcu_pulse_burst_decode and mcu_pulse_burst_sample_pc3.

- Addresses by version: 12b: 0x08008754, 143: 0x080088E4, 152: 0x08008924, 0160: 0x08008998
- Called by: `mcu_0160_0800d548`
- Calls: `mcu_edge_counter_init`
- Confidence: high

## mcu_pulse_burst_sample_pc3

**Sample GPIOC pin 3 into the pulse-burst decoder and store its result at 0x20002026**

Reads the GPIOC input data register at 0x40011008, takes bit 3 (pin PC3) as the direction, calls mcu_pulse_burst_decode on the decoder object at 0x20001FFC, and stores the returned byte at 0x20002026. The stored byte is read through the getter mcu_get_var_2026, which is called by mcu_0160_08008a14.

- Addresses by version: 12b: 0x08008734, 143: 0x080088C4, 152: 0x08008904, 0160: 0x08008978
- Peripheral registers: `GPIOC.IDT` (R)
- Called by: `mcu_0160_0800a320`
- Calls: `mcu_pulse_burst_decode`
- Confidence: high

## mcu_status_drive_pb6_pc11

**Drive GPIOB pin 6 from status bit 0x1000 and GPIOC pin 11 from bits 0x180 of 0x20001FDA**

If bit 0x1000 of the status word at 0x20001FDA is clear, it clears GPIOB pin 6 through the CLR register (offset 0x14, mask 0x40), otherwise it sets it through SCR (offset 0x10). Then, if either bit of mask 0x180 in the same word is set, it sets GPIOC pin 11 (mask 0x800) through SCR, otherwise it clears it through CLR. This is the output side of the status word that mcu_0160_080085bc refreshes from the 0x20C frame.

- Addresses by version: 12b: 0x08008788, 143: 0x08008918, 152: 0x08008958, 0160: 0x080089CC
- Peripheral registers: `GPIOB.CFGLR` (A), `GPIOC.CFGLR` (A)
- Called by: `mcu_0160_0800a320`
- Calls: `mcu_ctx_set_field_0x14`, `mcu_ctx_set_field_0x10`
- Confidence: high
