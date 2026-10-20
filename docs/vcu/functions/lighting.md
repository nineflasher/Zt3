# VCU - `lighting` functions

16 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`led_driver_shift_out_byte`](#led_driver_shift_out_byte) | 0x0800ED24 | Shift one byte out LSB first: data on PB7, clock pulse on PB6 for each bit |
| [`led_frame_apply_mode_pattern`](#led_frame_apply_mode_pattern) | 0x0800C57C | Light a fixed bit pattern in the LED image for display mode 1..4 |
| [`led_frame_set_bit16`](#led_frame_set_bit16) | 0x0800BDF4 | Set/clear one of 16 output bits in the LED image bytes 0x200021d2-0x200021d3 |
| [`led_frame_set_cf_bit4`](#led_frame_set_cf_bit4) | 0x0800BFB4 | Set or clear bit 4 of LED image byte 0x200021cf |
| [`led_frame_set_d3_bit2`](#led_frame_set_d3_bit2) | 0x0800BEE8 | Set or clear bit 2 of LED image byte 0x200021d3 |
| [`led_frame_set_group_all`](#led_frame_set_group_all) | 0x0800BE30 | Set or clear the whole 9-bit groups in LED image bytes 0x200021ce-0x200021d1 |
| [`led_frame_set_pair_d1_d4`](#led_frame_set_pair_d1_d4) | 0x0800BF04 | Set or clear bit 4 of 0x200021d1 and bit 3 of 0x200021d4 together |
| [`led_frame_set_segment_a`](#led_frame_set_segment_a) | 0x0800C420 | Set/clear one of 9 segments in the LED image (bytes 0x200021cd/d4/d5) |
| [`led_frame_set_segment_b`](#led_frame_set_segment_b) | 0x0800C488 | Set/clear one of 9 segments in the LED image (bytes 0x200021c7/c9/cb) |
| [`lighting_brightness_percent_set`](#lighting_brightness_percent_set) | 0x0800E60C | Set the LED brightness target 0..100 percent, with a stepped fade when enabled |
| [`lighting_fade_step`](#lighting_fade_step) | 0x0800BF30 | Ramp counter step with threshold 51 that issues LED command codes 0x81/0x86 |
| [`vcu_c14_c15_blink_step`](#vcu_c14_c15_blink_step) | 0x08009FE4 | Blink PC14 and PC15 together in a 40-tick cycle while blink request 10 is set |
| [`vcu_channel_sweep_animation`](#vcu_channel_sweep_animation) | 0x0800BE64 | Lighting animation: all groups on when bit 6 of DAT_20001e68 is 0, else a channel sweep |
| [`vcu_double_pulse_indicator_step`](#vcu_double_pulse_indicator_step) | 0x0800A050 | 55-tick two-pulse indicator pattern on status word f98, sets DAT_20001fa8 when done |
| [`vcu_level_bar_draw`](#vcu_level_bar_draw) | 0x0800BF84 | Light the first param/10 of the ten LED bar segments and clear the rest |
| [`vcu_level_bar_update_hysteresis`](#vcu_level_bar_update_hysteresis) | 0x0800BC4C | Map a 0..100 level to 10-segment bar values with dithering between neighbouring steps |

## led_driver_shift_out_byte

**Shift one byte out LSB first: data on PB7, clock pulse on PB6 for each bit**

Serial output of one byte, least significant bit first, to an external shift-register style LED driver. For each of the eight bits it sets PB7 to that bit (vcu_0159_0800ed0c or ed18), drives PB6 low (vcu_0159_0800ed00) and then high again (vcu_0159_0800ecf4), and shifts the value right. The clock idles high, so each rising edge of PB6 presents one data bit. PA9 is not touched here; it is driven separately by vcu_0159_0800ed94 and vcu_0159_0800eda4.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | byte to shift out in bits 0..7 |

**Notes:** Latching on the rising edge of PB6 is inferred from the order of operations and is not checked against the driver part.

- Addresses by version: 148: 0x0800DD00, 14a: 0x0800E19C, 14b: 0x0800E62C, 14e: 0x0800E6CC, 14f: 0x0800E818, 152: 0x0800EAC0, 153: 0x0800EBB4, 0159: 0x0800ED24
- Called by: `vcu_display_frame_render_tick`, `vcu_led_tm1640_frame_commit`
- Calls: `vcu_gpio_pb6_set`, `vcu_gpio_pb6_reset`, `vcu_gpio_pb7_set`, `vcu_gpio_pb7_reset`
- Confidence: medium

## led_frame_apply_mode_pattern

**Light a fixed bit pattern in the LED image for display mode 1..4**

Switch on DAT_20002047: mode 1 ORs 0x0f into DAT_200021c6 and DAT_200021ca; mode 2 ORs 0x0f into DAT_200021c7 and DAT_200021cb; mode 3 ORs 0x33 into DAT_200021c8; mode 4 ORs 0xcc into DAT_200021cc; any other value does nothing. It only sets bits (never clears), so the image must be cleared first by the frame builder. Caller: vcu_0159_080057ac. The bytes 0x200021c6..0x200021d5 form a 16-byte bit-mapped image that other code (vcu_0159_0800b0c4, vcu_0159_0800bfd0 and the sender vcu_0159_0800ed4c) transmits to an LED/indicator driver; this helper is part of the lighting group called from the 1 ms service vcu_0159_080057ac and the mode handlers around vcu_0159_0800c31c/0800c4f0.

**Notes:** DAT_20002047 is written by wave2/3 mode code; its meaning (drive mode / light mode?) is not established here.

- Addresses by version: 148: 0x0800B6F0, 14a: 0x0800BB34, 14b: 0x0800BFC0, 14e: 0x0800C054, 14f: 0x0800C190, 152: 0x0800C41C, 153: 0x0800C510, 0159: 0x0800C57C
- Called by: `vcu_display_frame_render_tick`
- Confidence: low

## led_frame_set_bit16

**Set/clear one of 16 output bits in the LED image bytes 0x200021d2-0x200021d3**

If param_1 < 8 the mask 1<<param_1 is applied to DAT_200021d2, otherwise 1<<(param_1-8) to DAT_200021d3; param_2 == 0 clears the bit, nonzero sets it. Index 0..7 low byte, 8..15 high byte. The bytes 0x200021c6..0x200021d5 form a 16-byte bit-mapped image that other code (vcu_0159_0800b0c4, vcu_0159_0800bfd0 and the sender vcu_0159_0800ed4c) transmits to an LED/indicator driver; this helper is part of the lighting group called from the 1 ms service vcu_0159_080057ac and the mode handlers around vcu_0159_0800c31c/0800c4f0. Callers: vcu_0159_0800bc4c and vcu_0159_0800bf84.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | bit index 0..15 |
| `param_2` | `s32` | nonzero = on, 0 = off |

**Notes:** Purpose (LED/indicator image) inferred from neighbouring packets; the physical meaning of the bits is unknown.

- Addresses by version: 148: 0x0800AFB4, 14a: 0x0800B3AC, 14b: 0x0800B838, 14e: 0x0800B8CC, 14f: 0x0800BA08, 152: 0x0800BC94, 153: 0x0800BD88, 0159: 0x0800BDF4
- Called by: `vcu_level_bar_update_hysteresis`, `vcu_level_bar_draw`
- Confidence: low

## led_frame_set_cf_bit4

**Set or clear bit 4 of LED image byte 0x200021cf**

Clears bit4 (0x10) of DAT_200021cf, then sets it again when param_1 != 0. Caller: vcu_0159_080057ac. The bytes 0x200021c6..0x200021d5 form a 16-byte bit-mapped image that other code (vcu_0159_0800b0c4, vcu_0159_0800bfd0 and the sender vcu_0159_0800ed4c) transmits to an LED/indicator driver; this helper is part of the lighting group called from the 1 ms service vcu_0159_080057ac and the mode handlers around vcu_0159_0800c31c/0800c4f0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | nonzero = on, 0 = off |

**Notes:** What the bit drives is unknown.

- Addresses by version: 148: 0x0800B124, 14a: 0x0800B56C, 14b: 0x0800B9F8, 14e: 0x0800BA8C, 14f: 0x0800BBC8, 152: 0x0800BE54, 153: 0x0800BF48, 0159: 0x0800BFB4
- Called by: `vcu_display_frame_render_tick`
- Confidence: low

## led_frame_set_d3_bit2

**Set or clear bit 2 of LED image byte 0x200021d3**

Clears bit2 (mask 0x04) of DAT_200021d3 and sets it again when param_1 != 0. Callers: vcu_0159_0800bc4c and vcu_0159_0800e60c. The bytes 0x200021c6..0x200021d5 form a 16-byte bit-mapped image that other code (vcu_0159_0800b0c4, vcu_0159_0800bfd0 and the sender vcu_0159_0800ed4c) transmits to an LED/indicator driver; this helper is part of the lighting group called from the 1 ms service vcu_0159_080057ac and the mode handlers around vcu_0159_0800c31c/0800c4f0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | nonzero = on, 0 = off |

**Notes:** Single-indicator helper; what bit 2 drives is unknown. Note bit 2 is also covered by the 16-bit helper led_frame_set_bit16 (index 10).

- Addresses by version: 148: 0x0800B0AC, 14a: 0x0800B4A0, 14b: 0x0800B92C, 14e: 0x0800B9C0, 14f: 0x0800BAFC, 152: 0x0800BD88, 153: 0x0800BE7C, 0159: 0x0800BEE8
- Called by: `vcu_level_bar_update_hysteresis`, `lighting_brightness_percent_set`
- Confidence: low

## led_frame_set_group_all

**Set or clear the whole 9-bit groups in LED image bytes 0x200021ce-0x200021d1**

Clears bytes 0x200021ce and 0x200021d0 and bit0 of 0x200021cf and 0x200021d1; if param_1 is nonzero they are then set to 0xff, 0xff and bit0 (two groups of 9 bits, all on). param_1 == 0 gives all off. The bytes 0x200021c6..0x200021d5 form a 16-byte bit-mapped image that other code (vcu_0159_0800b0c4, vcu_0159_0800bfd0 and the sender vcu_0159_0800ed4c) transmits to an LED/indicator driver; this helper is part of the lighting group called from the 1 ms service vcu_0159_080057ac and the mode handlers around vcu_0159_0800c31c/0800c4f0. Callers: vcu_0159_080057ac and vcu_0159_0800be64.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | nonzero = all on, 0 = all off |

**Notes:** 9-bit group structure matches the 9-segment helpers vcu_0159_0800c420/0800c488; meaning unconfirmed.

- Addresses by version: 148: 0x0800AFF0, 14a: 0x0800B3E8, 14b: 0x0800B874, 14e: 0x0800B908, 14f: 0x0800BA44, 152: 0x0800BCD0, 153: 0x0800BDC4, 0159: 0x0800BE30
- Called by: `vcu_display_frame_render_tick`, `vcu_channel_sweep_animation`
- Confidence: low

## led_frame_set_pair_d1_d4

**Set or clear bit 4 of 0x200021d1 and bit 3 of 0x200021d4 together**

param_1 != 0: DAT_200021d1 |= 0x10 and DAT_200021d4 |= 0x08; param_1 == 0 clears both bits. The two bits are always driven in unison (a single logical indicator mapped to two positions). Caller: vcu_0159_080057ac. The bytes 0x200021c6..0x200021d5 form a 16-byte bit-mapped image that other code (vcu_0159_0800b0c4, vcu_0159_0800bfd0 and the sender vcu_0159_0800ed4c) transmits to an LED/indicator driver; this helper is part of the lighting group called from the 1 ms service vcu_0159_080057ac and the mode handlers around vcu_0159_0800c31c/0800c4f0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | nonzero = on, 0 = off |

**Notes:** Which indicator this is is unknown.

- Addresses by version: 148: 0x0800B0C8, 14a: 0x0800B4BC, 14b: 0x0800B948, 14e: 0x0800B9DC, 14f: 0x0800BB18, 152: 0x0800BDA4, 153: 0x0800BE98, 0159: 0x0800BF04
- Called by: `vcu_display_frame_render_tick`
- Confidence: low

## led_frame_set_segment_a

**Set/clear one of 9 segments in the LED image (bytes 0x200021cd/d4/d5)**

Index 0..2 map to bits 4..6 of DAT_200021cd (1<<(idx+4)), 3..4 to bits 6..7 of DAT_200021d4 (1<<(idx+3)), 5..8 to bits 0..3 of DAT_200021d5 (1<<(idx-5)); indices >= 9 are ignored. param_2 == 0 clears, nonzero sets. Companion of led_frame_set_segment_b (same 9-segment indexing on another set of bytes), called from vcu_0159_0800c31c and vcu_0159_0800c4f0. The bytes 0x200021c6..0x200021d5 form a 16-byte bit-mapped image that other code (vcu_0159_0800b0c4, vcu_0159_0800bfd0 and the sender vcu_0159_0800ed4c) transmits to an LED/indicator driver; this helper is part of the lighting group called from the 1 ms service vcu_0159_080057ac and the mode handlers around vcu_0159_0800c31c/0800c4f0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | segment index 0..8 |
| `param_2` | `s32` | nonzero = on, 0 = off |

**Notes:** Likely a 9-step bar graph (e.g. speed or battery level); inferred from the 0..8 range only.

- Addresses by version: 148: 0x0800B594, 14a: 0x0800B9D8, 14b: 0x0800BE64, 14e: 0x0800BEF8, 14f: 0x0800C034, 152: 0x0800C2C0, 153: 0x0800C3B4, 0159: 0x0800C420
- Called by: `vcu_display_anim_step`, `vcu_display_sweep_down_step`
- Confidence: low

## led_frame_set_segment_b

**Set/clear one of 9 segments in the LED image (bytes 0x200021c7/c9/cb)**

Index 0..2 map to bits 4..6 of DAT_200021c7 (1<<(idx+4)), 3..5 to bits 4..6 of DAT_200021c9 (1<<(idx+1)), 6..8 to bits 4..6 of DAT_200021cb (1<<(idx-2)); indices >= 9 are ignored. param_2 == 0 clears, nonzero sets. Second 9-segment bar next to led_frame_set_segment_a, called from vcu_0159_0800c31c and vcu_0159_0800c4f0. The bytes 0x200021c6..0x200021d5 form a 16-byte bit-mapped image that other code (vcu_0159_0800b0c4, vcu_0159_0800bfd0 and the sender vcu_0159_0800ed4c) transmits to an LED/indicator driver; this helper is part of the lighting group called from the 1 ms service vcu_0159_080057ac and the mode handlers around vcu_0159_0800c31c/0800c4f0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | segment index 0..8 |
| `param_2` | `s32` | nonzero = on, 0 = off |

**Notes:** Same caveat as led_frame_set_segment_a.

- Addresses by version: 148: 0x0800B5FC, 14a: 0x0800BA40, 14b: 0x0800BECC, 14e: 0x0800BF60, 14f: 0x0800C09C, 152: 0x0800C328, 153: 0x0800C41C, 0159: 0x0800C488
- Called by: `vcu_display_anim_step`, `vcu_display_sweep_down_step`
- Confidence: low

## lighting_brightness_percent_set

**Set the LED brightness target 0..100 percent, with a stepped fade when enabled**

Clamps the argument to 100 and stores its 0..10 level in DAT_20001507 (util_map_range_clamp_high, vcu_0159_0800f050). If bit 2 of DAT_20001AEC (the fade enable) is set, a counter in DAT_20001506 advances on each call and, whenever it passes the level, the ramp value in DAT_20001505 rises by 5 and the counter restarts. The ramp is kept only while it lies between the target and 109 (0x6D); otherwise the target is used. With fading off the target is used directly. It then clears bit 2 of LED image byte 0x200021D3 (led_frame_set_d3_bit2 with 0, vcu_0159_0800bee8) and calls vcu_0159_0800bf84 with a byte read through a pointer in r3 that the decompiler cannot attribute.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | brightness target in percent; values above 100 are clamped |

**Notes:** The byte passed to vcu_0159_0800bf84 comes from r3 after the bee8 call, so its source is uncertain.

- Addresses by version: 148: 0x0800D5F4, 14a: 0x0800DA88, 14b: 0x0800DF14, 14e: 0x0800DFB4, 14f: 0x0800E100, 152: 0x0800E3A8, 153: 0x0800E49C, 0159: 0x0800E60C
- Called by: `vcu_display_frame_render_tick`
- Calls: `led_frame_set_d3_bit2`, `vcu_level_bar_draw`, `util_map_range_clamp_high`
- Confidence: medium

## lighting_fade_step

**Ramp counter step with threshold 51 that issues LED command codes 0x81/0x86**

Called each tick from vcu_0159_080057ac. If flag DAT_20001cfa is nonzero the counter DAT_2000153e is incremented; when it was already above 0x32 (51) it is reset to 0 and DAT_200022dd is set to 0x81. If the flag is zero the counter is decremented down to 0; when it is already 0 DAT_200022dd is set to 0x86 instead. DAT_200022dd is the command/mode byte later passed to the LED sender vcu_0159_0800ed4c, so this behaves like a hysteresis/dimming timer between two lighting states. Not present in VCU_148.

**Notes:** Meaning of 0x81 vs 0x86 and of flag 0x20001cfa not confirmed; only the counter arithmetic is certain.

- Addresses by version: 14a: 0x0800B4E8, 14b: 0x0800B974, 14e: 0x0800BA08, 14f: 0x0800BB44, 152: 0x0800BDD0, 153: 0x0800BEC4, 0159: 0x0800BF30
- Called by: `vcu_display_frame_render_tick`
- Confidence: low

## vcu_c14_c15_blink_step

**Blink PC14 and PC15 together in a 40-tick cycle while blink request 10 is set**

Called once per tick. When DAT_20001fe8 is 10 the counter DAT_20001368 increments: counts 1..19 drive both pins high, counts 20..39 drive both low, and at 40 the counter wraps to 0 without touching the pins, giving a 40-tick period (19 high, 20 low, 1 idle). When DAT_20001fe8 is 11 the blink ends: the counter and the request byte are cleared and both pins are driven low. Other request values do nothing.

**Notes:** Meaning of the request codes 10 and 11 is inferred from the blink pattern. What the two pins drive is not traced.

- Addresses by version: 148: 0x0800910C, 14a: 0x080095B4, 14b: 0x08009A34, 14e: 0x08009AC8, 14f: 0x08009C04, 152: 0x08009E18, 153: 0x08009F0C, 0159: 0x08009FE4
- Called by: `vcu_0159_0800a15c`, `vcu_0159_0800a1d0`, `vcu_state2_periodic_tick`, `vcu_state0_periodic_tick_v0159`, `vcu_0159_0800a55c`, `vcu_0159_0800a5c8`
- Calls: `vcu_gpio_c14_set`, `vcu_gpio_c15_set`
- Confidence: medium

## vcu_channel_sweep_animation

**Lighting animation: all groups on when bit 6 of DAT_20001e68 is 0, else a channel sweep**

Latches bit 6 of DAT_20001e68 into DAT_20001512. When the latch is 0 it calls led_frame_set_group_all(1) to light every group. When it is 1, a counter DAT_200021e0 advances each call, and every DAT_200014f4 counts the sweep index DAT_20001510 steps: while the index is below the width DAT_200014f5 it sets channel index (vcu_chan_mask_update with 1), and for an index from the width up to twice the width it clears channel index minus width. At twice the width both counters reset, so a lit window of the given width travels across the ten channels.

**Notes:** vcu_chan_mask_update (FUN_0800aa9c) sets or clears one of the ten channel bits in the byte masks at 0x200021ce, as described in the packet callee list.

- Addresses by version: 148: 0x0800B024, 14a: 0x0800B41C, 14b: 0x0800B8A8, 14e: 0x0800B93C, 14f: 0x0800BA78, 152: 0x0800BD04, 153: 0x0800BDF8, 0159: 0x0800BE64
- Called by: `vcu_display_frame_render_tick`
- Calls: `vcu_chan_mask_update`, `led_frame_set_group_all`
- Confidence: medium

## vcu_double_pulse_indicator_step

**55-tick two-pulse indicator pattern on status word f98, sets DAT_20001fa8 when done**

Runs when DAT_20001fbf is 1 and advances the counter DAT_20001372 each tick. Ticks 0..14 are the first on-phase (f98 bit 14 set, and bits 11..9 set to 2 by clearing them and adding 0x400; for variants 2 and 5 it calls FUN_08005d9c(1) instead). Ticks 15..34 are the off-phase (bit 14 cleared, bits 11..9 zeroed, or FUN_08005d9c(0) for variants 2 and 5). Ticks 35..54 repeat the on-phase, and at tick 55 the counter wraps, DAT_20001fa8 is set to 1 to signal completion, and bit 14 is cleared unless DAT_20001b12 bit 1 is set. DAT_20001360 and DAT_20001fb4 are cleared on every active tick.

**Notes:** f98 is treated as an output/indicator word; the consumer of its bit 14 and bits 11..9 is not traced. The 15/20/20 tick split is read from the compare constants.

- Addresses by version: 148: 0x08009178, 14a: 0x08009620, 14b: 0x08009AA0, 14e: 0x08009B34, 14f: 0x08009C70, 152: 0x08009E84, 153: 0x08009F78, 0159: 0x0800A050
- Called by: `vcu_0159_080047ac`
- Calls: `vcu_pa6_output_set`
- Confidence: medium

## vcu_level_bar_draw

**Light the first param/10 of the ten LED bar segments and clear the rest**

Loops over bar segments 0..9 calling led_frame_set_bit16 (FUN_0800bdf4) with 1 for each index below param_1 divided by 10 and 0 for the others. Levels of 100 or more light all ten segments. No other state is touched.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | level, nominally 0..100 |

- Addresses by version: 148: 0x0800B0F4, 14a: 0x0800B53C, 14b: 0x0800B9C8, 14e: 0x0800BA5C, 14f: 0x0800BB98, 152: 0x0800BE24, 153: 0x0800BF18, 0159: 0x0800BF84
- Called by: `vcu_level_gauge_update_v0159`, `lighting_brightness_percent_set`
- Calls: `led_frame_set_bit16`
- Confidence: high

## vcu_level_bar_update_hysteresis

**Map a 0..100 level to 10-segment bar values with dithering between neighbouring steps**

Quantises the level into two 10-step values: DAT_200014f6 (lower) and DAT_200014f7 (upper). Level bands of five values map to pairs such as 90..94 giving (90, 100), 85..89 giving (90, 90), 80..84 giving (80, 90), and so on down to 10..14 giving (10, 20). Levels 95 and above give (100, 100), and levels 0..9 give (0, 0), with extra effects: at 5..9 led_frame_set_d3_bit2 is called and, the first time, app_set_state(2) is called; at 0..4 a flag is set. The bar is redrawn only when the counter DAT_200014f8 reaches 60 (using the upper value) or 119 (using the lower value, then wrapping), so the displayed segment count alternates between the two values and the average shows intermediate levels. Each redraw lights the first value/10 segments through led_frame_set_bit16 and clears the rest.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | level, nominally 0..100 |

**Notes:** The meaning of the level input (state of charge, speed or other) is not established here. The 60/119 redraw points and the bands are read from the compare constants.

- Addresses by version: 148: 0x0800AE0C, 14a: 0x0800B204, 14b: 0x0800B690, 14e: 0x0800B724, 14f: 0x0800B860, 152: 0x0800BAEC, 153: 0x0800BBE0, 0159: 0x0800BC4C
- Called by: `vcu_display_frame_render_tick`
- Calls: `app_set_state`, `led_frame_set_bit16`, `led_frame_set_d3_bit2`
- Confidence: medium
