# VCU - `display` functions

23 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`lcd_fb_clear_cd_low_nibble`](#lcd_fb_clear_cd_low_nibble) | 0x0800C7B8 | Clear the low nibble of frame-buffer byte 0x200021cd |
| [`lcd_fb_set_c9_low2`](#lcd_fb_set_c9_low2) | 0x0800C7C8 | Set or clear bits 1:0 of frame-buffer byte 0x200021c9 |
| [`lcd_fb_set_cd_low_nibble`](#lcd_fb_set_cd_low_nibble) | 0x0800C78C | Set low nibble of frame-buffer byte 0x200021cd to 0xC or 0x3 |
| [`lcd_fb_set_d1_bit2`](#lcd_fb_set_d1_bit2) | 0x0800C660 | Set or clear bit 2 of frame-buffer byte 0x200021d1 |
| [`lcd_fb_set_d1_bit6`](#lcd_fb_set_d1_bit6) | 0x0800C67C | Set or clear bit 6 of frame-buffer byte 0x200021d1 |
| [`lcd_fb_set_d3_bit3`](#lcd_fb_set_d3_bit3) | 0x0800C81C | Set or clear bit 3 of frame-buffer byte 0x200021d3 |
| [`lcd_fb_set_d4_bit2`](#lcd_fb_set_d4_bit2) | 0x0800C644 | Set or clear bit 2 of frame-buffer byte 0x200021d4 |
| [`lcd_fb_set_d4_bits45`](#lcd_fb_set_d4_bits45) | 0x0800C800 | Set or clear bits 5:4 of frame-buffer byte 0x200021d4 |
| [`lcd_fb_set_d4_low2`](#lcd_fb_set_d4_low2) | 0x0800C7E4 | Set or clear bits 1:0 of frame-buffer byte 0x200021d4 |
| [`lcd_fb_set_icon_group_a`](#lcd_fb_set_icon_group_a) | 0x0800C5D4 | Set or clear bits 4-6 of frame-buffer bytes 0x200021c7, c9 and cb |
| [`lcd_fb_set_icon_group_b`](#lcd_fb_set_icon_group_b) | 0x0800C60C | Set or clear icon bits in frame-buffer bytes 0x200021cd, d4 and d5 |
| [`lcd_fb_set_mode_indicator`](#lcd_fb_set_mode_indicator) | 0x0800C698 | Select one of four exclusive indicator segments in frame-buffer byte 0x200021cf |
| [`lcd_fb_show_digit_units`](#lcd_fb_show_digit_units) | 0x0800C6D8 | Show one decimal digit in the units position and blank the tens position |
| [`lcd_fb_show_number_2digit`](#lcd_fb_show_number_2digit) | 0x0800C720 | Render a 0..99 number as two seven-segment-style digits in the frame buffer |
| [`vcu_countdown_start_handshake`](#vcu_countdown_start_handshake) | 0x080046C0 | Start the countdown display on request, then send 0x7A to peer 7 when it finishes |
| [`vcu_display_anim_step`](#vcu_display_anim_step) | 0x0800C31C | Display animation step per mode: blink icons (10), sweep segments up (12), icons on |
| [`vcu_display_frame_render_tick`](#vcu_display_frame_render_tick) | 0x080057AC | Per-tick display renderer: build the 16-byte LED/LCD image for the mode and send it |
| [`vcu_display_sweep_down_step`](#vcu_display_sweep_down_step) | 0x0800C4F0 | Downward segment sweep (20 to 0) while DAT_20001f58 is set; otherwise all icons on |
| [`vcu_led_pattern_anim_step`](#vcu_led_pattern_anim_step) | 0x0800BFD0 | Advance the three-phase LED row animation one step, drawing and clearing rows from tables |
| [`vcu_led_tm1640_frame_commit`](#vcu_led_tm1640_frame_commit) | 0x0800ED4C | Write the 16-byte LED frame to the TM1640-style driver on PB6, PB7 and PA9 |
| [`vcu_level_gauge_update_v0159`](#vcu_level_gauge_update_v0159) | 0x0800B0C4 | Update the VCU_0159 level gauge, switching to a cycling status table when a group is active |
| [`vcu_level_gauge_update_v148`](#vcu_level_gauge_update_v148) | (removed) | Update the VCU_148 level gauge: bar, 2-digit number and LED frame commit |
| [`vcu_level_gauge_update_v14a_153`](#vcu_level_gauge_update_v14a_153) | (removed) | Update the level gauge for VCU_14A to VCU_153: 2-digit number, bar and LED frame commit |

## lcd_fb_clear_cd_low_nibble

**Clear the low nibble of frame-buffer byte 0x200021cd**

Masks DAT_200021cd with 0xf0, turning off the four segments set by lcd_fb_set_cd_low_nibble; the upper nibble (icon group B bits) is kept. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. The decompiler lists 0x200021c6 as address-taken only because the byte is addressed relative to the buffer base via the literal pool; it is not accessed.

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B92C, 14a: 0x0800BD70, 14b: 0x0800C1FC, 14e: 0x0800C290, 14f: 0x0800C3CC, 152: 0x0800C658, 153: 0x0800C74C, 0159: 0x0800C7B8
- Called by: `vcu_display_frame_render_tick`
- Confidence: medium

## lcd_fb_set_c9_low2

**Set or clear bits 1:0 of frame-buffer byte 0x200021c9**

Clears the two low bits of DAT_200021c9 (mask 0xfc) and sets both (0x03) when param_1 is non-zero. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Two-segment setter.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = both segments on |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B93C, 14a: 0x0800BD80, 14b: 0x0800C20C, 14e: 0x0800C2A0, 14f: 0x0800C3DC, 152: 0x0800C668, 153: 0x0800C75C, 0159: 0x0800C7C8
- Called by: `vcu_display_frame_render_tick`
- Confidence: medium

## lcd_fb_set_cd_low_nibble

**Set low nibble of frame-buffer byte 0x200021cd to 0xC or 0x3**

Keeps the upper nibble of DAT_200021cd and writes the low nibble as 0x0c when param_1 is non-zero, 0x03 when it is zero (two complementary 2-bit segment pairs). Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Paired with lcd_fb_clear_cd_low_nibble which blanks the nibble.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero selects pattern 0xC, zero selects pattern 0x3 |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B900, 14a: 0x0800BD44, 14b: 0x0800C1D0, 14e: 0x0800C264, 14f: 0x0800C3A0, 152: 0x0800C62C, 153: 0x0800C720, 0159: 0x0800C78C
- Called by: `vcu_display_frame_render_tick`
- Confidence: medium

## lcd_fb_set_d1_bit2

**Set or clear bit 2 of frame-buffer byte 0x200021d1**

Read-modify-write of DAT_200021d1: clears bit 2 (mask 0xfb), sets it when param_1 is non-zero. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Single-segment (icon) setter.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = segment on |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B7D4, 14a: 0x0800BC18, 14b: 0x0800C0A4, 14e: 0x0800C138, 14f: 0x0800C274, 152: 0x0800C500, 153: 0x0800C5F4, 0159: 0x0800C660
- Called by: `vcu_display_frame_render_tick`
- Confidence: medium

## lcd_fb_set_d1_bit6

**Set or clear bit 6 of frame-buffer byte 0x200021d1**

Read-modify-write of DAT_200021d1: clears bit 6 (mask 0xbf), sets it when param_1 is non-zero. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Single-segment (icon) setter; bits 0/1 of the same byte are touched by other helpers (0x200021d0/d1 are also written by the neighbouring routines at 0x0800aa9c and 0x0800be30).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = segment on |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B7F0, 14a: 0x0800BC34, 14b: 0x0800C0C0, 14e: 0x0800C154, 14f: 0x0800C290, 152: 0x0800C51C, 153: 0x0800C610, 0159: 0x0800C67C
- Called by: `vcu_display_frame_render_tick`
- Confidence: medium

## lcd_fb_set_d3_bit3

**Set or clear bit 3 of frame-buffer byte 0x200021d3**

Clears bit 3 of DAT_200021d3 (mask 0xf7) and sets it when param_1 is non-zero. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Single-segment setter; also called from vcu_0159_0800b0c4 and vcu_148_0800a138, i.e. from outside the main display routine.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = segment on |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B990, 14a: 0x0800BDD4, 14b: 0x0800C260, 14e: 0x0800C2F4, 14f: 0x0800C430, 152: 0x0800C6BC, 153: 0x0800C7B0, 0159: 0x0800C81C
- Called by: `vcu_display_frame_render_tick`, `vcu_level_gauge_update_v0159`
- Confidence: medium

## lcd_fb_set_d4_bit2

**Set or clear bit 2 of frame-buffer byte 0x200021d4**

Read-modify-write of DAT_200021d4: clears bit 2 (mask 0xfb) and sets it again when param_1 is non-zero. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Single-segment (icon) setter.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = segment on |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B7B8, 14a: 0x0800BBFC, 14b: 0x0800C088, 14e: 0x0800C11C, 14f: 0x0800C258, 152: 0x0800C4E4, 153: 0x0800C5D8, 0159: 0x0800C644
- Called by: `vcu_display_frame_render_tick`
- Confidence: medium

## lcd_fb_set_d4_bits45

**Set or clear bits 5:4 of frame-buffer byte 0x200021d4**

Clears bits 5:4 of DAT_200021d4 (mask 0xcf) and sets both (0x30) when param_1 is non-zero. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Two-segment setter.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = both segments on |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B974, 14a: 0x0800BDB8, 14b: 0x0800C244, 14e: 0x0800C2D8, 14f: 0x0800C414, 152: 0x0800C6A0, 153: 0x0800C794, 0159: 0x0800C800
- Called by: `vcu_display_frame_render_tick`
- Confidence: medium

## lcd_fb_set_d4_low2

**Set or clear bits 1:0 of frame-buffer byte 0x200021d4**

Clears the two low bits of DAT_200021d4 (mask 0xfc) and sets both (0x03) when param_1 is non-zero. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Two-segment setter.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = both segments on |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B958, 14a: 0x0800BD9C, 14b: 0x0800C228, 14e: 0x0800C2BC, 14f: 0x0800C3F8, 152: 0x0800C684, 153: 0x0800C778, 0159: 0x0800C7E4
- Called by: `vcu_display_frame_render_tick`
- Confidence: medium

## lcd_fb_set_icon_group_a

**Set or clear bits 4-6 of frame-buffer bytes 0x200021c7, c9 and cb**

Clears bits 6:4 (mask 0x8f keeps the rest) of DAT_200021c7, DAT_200021c9 and DAT_200021cb, then, if param_1 is non-zero, ORs 0x70 back into all three so the three-bit group is all on; otherwise all three groups are off. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Each byte is the high nibble area next to a digit (the digit low nibble is written by lcd_fb_show_number_2digit); likely an icon/bar-segment group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = turn the 0x70 bits on, zero = off |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B748, 14a: 0x0800BB8C, 14b: 0x0800C018, 14e: 0x0800C0AC, 14f: 0x0800C1E8, 152: 0x0800C474, 153: 0x0800C568, 0159: 0x0800C5D4
- Called by: `vcu_display_frame_render_tick`, `vcu_display_anim_step`, `vcu_display_sweep_down_step`
- Confidence: medium

## lcd_fb_set_icon_group_b

**Set or clear icon bits in frame-buffer bytes 0x200021cd, d4 and d5**

Clears bits 6:4 of DAT_200021cd, bits 7:6 of DAT_200021d4 and the low nibble of DAT_200021d5 (masks 0x8f, 0x3f, 0xf0). If param_1 is non-zero it then sets 0x70 in cd, 0xc0 in d4 and 0x0f in d5, i.e. a 3+2+4 = 9-segment group is switched on or off as a unit. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Sibling of lcd_fb_set_icon_group_a.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = all nine segments on, zero = all off |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B780, 14a: 0x0800BBC4, 14b: 0x0800C050, 14e: 0x0800C0E4, 14f: 0x0800C220, 152: 0x0800C4AC, 153: 0x0800C5A0, 0159: 0x0800C60C
- Called by: `vcu_display_frame_render_tick`, `vcu_display_anim_step`, `vcu_display_sweep_down_step`
- Confidence: medium

## lcd_fb_set_mode_indicator

**Select one of four exclusive indicator segments in frame-buffer byte 0x200021cf**

Clears bits 1, 2, 3 and 5 of DAT_200021cf (mask 0xd1, bits 0, 4, 6, 7 are preserved), then lights exactly one segment by value: 1 -> 0x08, 2 -> 0x04, 3 -> 0x02, 4 -> 0x20; any other value (e.g. 0) leaves all four off. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Behaves like a mutually exclusive mode / level indicator (e.g. riding mode or gear icons); the meaning of the four icons is not visible here.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | indicator index 1..4, anything else = none lit |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B80C, 14a: 0x0800BC50, 14b: 0x0800C0DC, 14e: 0x0800C170, 14f: 0x0800C2AC, 152: 0x0800C538, 153: 0x0800C62C, 0159: 0x0800C698
- Called by: `vcu_display_frame_render_tick`
- Confidence: medium

## lcd_fb_show_digit_units

**Show one decimal digit in the units position and blank the tens position**

param_1 is clamped (values above 10 become 9) and reduced modulo 10, so 10 shows as 0. The tens position is blanked: DAT_200021c6=0, low nibble of DAT_200021c7=0, DAT_200021c8=0. The units position is loaded from the glyph tables: DAT_200021ca = table_A[d] (0x20001548+d), low nibble of DAT_200021cb = table_B[d] (0x20001552+d), DAT_200021cc = table_C[d] (0x2000155c+d); the upper nibble of cb is preserved because it belongs to the 0x70 icon group. The display frame buffer is the 16-byte RAM block 0x200021c6..0x200021d5 (fb[0]=0x200021c6 ... fb[15]=0x200021d5); the three digit glyph tables are 10-byte arrays at 0x20001548, 0x20001552 and 0x2000155c. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Always displays, unlike lcd_fb_show_number_2digit which has an enable flag.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | digit 0..9 (values above 10 are forced to 9, 10 wraps to 0) |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known. The 7-segment glyph encoding of the tables is assumed; the tables are RAM and presumably initialised at startup.

- Addresses by version: 148: 0x0800B84C, 14a: 0x0800BC90, 14b: 0x0800C11C, 14e: 0x0800C1B0, 14f: 0x0800C2EC, 152: 0x0800C578, 153: 0x0800C66C, 0159: 0x0800C6D8
- Called by: `vcu_display_frame_render_tick`
- Confidence: medium

## lcd_fb_show_number_2digit

**Render a 0..99 number as two seven-segment-style digits in the frame buffer**

Clamps param_1 to 99, splits it into tens and units, and clears both digit cells (tens: fb bytes c6, low nibble of c7, c8; units: ca, low nibble of cb, cc; upper nibbles of c7/cb are kept). If param_2 is non-zero, the tens cell is filled from glyph tables A/B/C (0x20001548, 0x20001552, 0x2000155c) only when the tens digit is non-zero (leading-zero suppression) and the units cell is always filled; with param_2 == 0 both cells stay blank. The display frame buffer is the 16-byte RAM block 0x200021c6..0x200021d5 (fb[0]=0x200021c6 ... fb[15]=0x200021d5); the three digit glyph tables are 10-byte arrays at 0x20001548, 0x20001552 and 0x2000155c. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Also called from vcu_0159_0800b0c4 (and the 148/153 equivalents), i.e. from outside the main display routine.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value to show, 0..99 (clamped) |
| `param_2` | `s32` | non-zero = display, zero = blank the two digits |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known. Digit glyph layout is a guess: three table bytes per digit (full byte, nibble, full byte).

- Addresses by version: 148: 0x0800B894, 14a: 0x0800BCD8, 14b: 0x0800C164, 14e: 0x0800C1F8, 14f: 0x0800C334, 152: 0x0800C5C0, 153: 0x0800C6B4, 0159: 0x0800C720
- Called by: `vcu_display_frame_render_tick`, `vcu_level_gauge_update_v0159`
- Confidence: medium

## vcu_countdown_start_handshake

**Start the countdown display on request, then send 0x7A to peer 7 when it finishes**

When the start request DAT_20001F45 is set, the first call moves the countdown state DAT_20001D36 from 0 to 1 and sets app state 1. When the state has reached 2, which vcu_display_frame_render_tick sets after its countdown runs out, the function clears the request, sends a 0x7A frame from 0x3E to peer 7 with a 4-byte zero payload through vcu_0159_0800D018 (not yet described) and raises the display update request DAT_20001FB4.

**Notes:** The 0x7A frame is also sent from the countdown in vcu_display_frame_render_tick at count 200 to 299, so the same frame appears on both paths. As decompiled, that send runs on every tick of that band, which may repeat it up to 100 times; this should be checked against the intended behaviour.

- Addresses by version: 148: 0x08003D08, 14a: 0x08004060, 14b: 0x080043A0, 14e: 0x080043CC, 14f: 0x08004428, 152: 0x0800448C, 153: 0x080044AC, 0159: 0x080046C0
- Called by: `vcu_0159_0800a1d0`
- Calls: `app_set_state`, `vcu_can_ef00_message_send`
- Confidence: medium

## vcu_display_anim_step

**Display animation step per mode: blink icons (10), sweep segments up (12), icons on**

Called once per tick with the requested mode. A new mode is accepted into DAT_2000150c only while the frame counter DAT_200021de is zero. Mode 10 blinks the icon groups: at counter multiples of 50 both groups are cleared and at multiples of 100 both are set and the counter wraps, giving 50 ticks on and 50 off. Modes 0, 9 and 13 turn both icon groups on. Mode 12 runs an upward segment sweep every DAT_200014f2 ticks: while the position DAT_2000150e is below DAT_200014f3 it clears the segment pair at the position, then it sets the pair at position minus the width until twice the width, and then wraps. Other modes do nothing.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | requested mode code, 0..13 |

**Notes:** Mode meanings are inferred from the animation each one produces. The segment and icon helpers are defined in the packet callee list.

- Addresses by version: 148: 0x0800B490, 14a: 0x0800B8D4, 14b: 0x0800BD60, 14e: 0x0800BDF4, 14f: 0x0800BF30, 152: 0x0800C1BC, 153: 0x0800C2B0, 0159: 0x0800C31C
- Called by: `vcu_display_frame_render_tick`
- Calls: `led_frame_set_segment_a`, `led_frame_set_segment_b`, `lcd_fb_set_icon_group_a`, `lcd_fb_set_icon_group_b`
- Confidence: medium

## vcu_display_frame_render_tick

**Per-tick display renderer: build the 16-byte LED/LCD image for the mode and send it**

Each tick it runs vcu_0159_0800BF30 (lighting_fade_step), and when the display mode DAT_2000123E differs from the previous mode in DAT_20001508 it clears the 16-byte image at 0x200021C6 first. A switch on DAT_2000123E then runs one of the mode handlers, which set the image bits through the lcd_fb_*, led_frame_* and lighting helpers, and the image is sent with vcu_0159_0800ED4C (not yet described) using the display control byte DAT_200022DD. The handlers include a passcode entry screen (mode 2, bit 7 of DAT_20001AEE) that shows the pending key DAT_20002044 as a digit with a progress bar from DAT_20001CEC, a main run display (mode 3) with a level bar, icon groups, fault-code cycling and a 3-2-1-0 countdown over 400 ticks while DAT_20001D36 is nonzero, and a 500-tick lamp test (mode 12) that drives all 16 bytes to 0xFF before a blank frame. Modes 0, 5 and 10, and the tail of the lamp test, clear the image and the fault and warning tables DAT_200021E8 and DAT_20002248 and write the blank frame inline.

**Notes:** Mode map from the switch: 1 power-on sweep until DAT_20001FBF, using variant-dependent tables (DAT_20001FA7); 2 passcode screen (bit 7 of DAT_20001AEE) or progress bars from DAT_20001CEC (bit 8), otherwise the frame is left alone; 3 main run display; 4 lighting table via vcu_0159_0800BFD0 (not described) until DAT_20001FBF, then blank; 6 alert blink on C14/C15 with PA6 through vcu_pa6_output_set; 7 vcu_0159_0800B0C4 (not described) with the 0..100 value DAT_20001D08; 8 like mode 3 with state word DAT_2000152C and brightness from DAT_20001D08 through lighting_brightness_percent_set; 9 progress bars from DAT_20001CEC into DAT_200021D2; 11 fault and warning display from the 48-bit fault map; 12 lamp test; any other value sets mode 0 and returns. The frame writes use the sequence 0x40 (auto-increment), 0xC0 (address), 16 data bytes and a display control byte, on PA9 as strobe, PB6 as clock and PB7 as data, which is consistent with a TM1638-style driver (identified from the sequence, not a datasheet).

- Addresses by version: 152: 0x08005630, 153: 0x08005648, 0159: 0x080057AC
- Calls: `vcu_buf_zero`, `app_set_state`, `vcu_pa6_output_set`, `vcu_gpio_c14_set`, `vcu_gpio_c15_set`, `vcu_level_gauge_update_v0159`, `vcu_level_bar_update_hysteresis`, `led_frame_set_group_all`, `vcu_channel_sweep_animation`, `led_frame_set_pair_d1_d4`, `lighting_fade_step`, `led_frame_set_cf_bit4`, `vcu_led_pattern_anim_step`, `vcu_display_anim_step`, `vcu_display_sweep_down_step`, `led_frame_apply_mode_pattern` ...
- Confidence: medium

## vcu_display_sweep_down_step

**Downward segment sweep (20 to 0) while DAT_20001f58 is set; otherwise all icons on**

When DAT_20001f58 is zero it turns both icon groups on, resets its counter DAT_200021e2 and returns. Otherwise every DAT_200014f0 ticks it steps the position DAT_2000150a down from 20: while the position is above 10 it sets the segment pair at position minus DAT_200014f1 (the window width), and otherwise it clears the segment pair at the position, wrapping back to 20 at zero. The result is a window of lit segments that moves downward and then blanks out.

**Notes:** Companion of vcu_display_anim_step, which sweeps upward.

- Addresses by version: 148: 0x0800B664, 14a: 0x0800BAA8, 14b: 0x0800BF34, 14e: 0x0800BFC8, 14f: 0x0800C104, 152: 0x0800C390, 153: 0x0800C484, 0159: 0x0800C4F0
- Called by: `vcu_display_frame_render_tick`
- Calls: `led_frame_set_segment_a`, `led_frame_set_segment_b`, `lcd_fb_set_icon_group_a`, `lcd_fb_set_icon_group_b`
- Confidence: medium

## vcu_led_pattern_anim_step

**Advance the three-phase LED row animation one step, drawing and clearing rows from tables**

One step of a LED pattern animation that acts every third call (DAT_200021d8 modulo 3). Two tables of 10-byte rows are passed in: each row starts with a count followed by frame-position and bit-mask pairs, and the second table supplies the masks. Phase 0 (DAT_200021da == 0) ORs in rows 17 down to 9, one row per step, committing the frame after each, until DAT_200021d6 reaches 9 and phase 1 starts. Phase 1 clears the row above and draws the current row while counting DAT_200021d6 down, then phase 2 starts at 9. Phase 2 clears the rows one by one; at 0 it clears the whole 16-byte frame, sets DAT_20001fbf = 1 and returns to phase 0. Frame commits use vcu_0159_0800ed4c with DAT_200022dd.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | first table: 10-byte rows, count then frame positions |
| `param_2` | `ptr` | second table: 10-byte rows of bit masks, same layout |

**Notes:** The phase names are inferred from the transitions. The tables are not shown in this packet.

- Addresses by version: 148: 0x0800B140, 14a: 0x0800B588, 14b: 0x0800BA14, 14e: 0x0800BAA8, 14f: 0x0800BBE4, 152: 0x0800BE70, 153: 0x0800BF64, 0159: 0x0800BFD0
- Called by: `vcu_display_frame_render_tick`
- Calls: `vcu_led_tm1640_frame_commit`
- Confidence: medium

## vcu_led_tm1640_frame_commit

**Write the 16-byte LED frame to the TM1640-style driver on PB6, PB7 and PA9**

Sends a 16-byte display frame over a bit-banged serial bus to a TM1640-style LED driver: data on PB7 and clock on PB6 (led_driver_shift_out_byte), strobe on PA9 (vcu_gpio_pa9_set and vcu_gpio_pa9_reset). It sends command 0x40 (auto-increment data write), then command 0xC0 (start address 0) followed by the 16 frame bytes, then the display control byte param_2 | 0x88, with the strobe asserted around each command.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 16-byte frame buffer |
| `param_2` | `u32` | brightness code, low 3 bits; OR-ed with 0x88 to turn the display on |

**Notes:** The TM1640 identification is inferred from the command bytes 0x40, 0xC0 and 0x88 plus brightness, and from the bus pins. The code does not name the chip.

- Addresses by version: 148: 0x0800DD28, 14a: 0x0800E1C4, 14b: 0x0800E654, 14e: 0x0800E6F4, 14f: 0x0800E840, 152: 0x0800EAE8, 153: 0x0800EBDC, 0159: 0x0800ED4C
- Called by: `vcu_display_frame_render_tick`, `vcu_level_gauge_update_v0159`, `vcu_led_pattern_anim_step`
- Calls: `led_driver_shift_out_byte`, `vcu_gpio_pa9_set`, `vcu_gpio_pa9_reset`
- Confidence: medium

## vcu_level_gauge_update_v0159

**Update the VCU_0159 level gauge, switching to a cycling status table when a group is active**

VCU_0159 variant of the level gauge. It clamps the level to 100 and zeroes the 16-byte frame DAT_200021c6. While DAT_20001fd4 is clear, it takes one of two paths. If the four words DAT_20001cd8, DAT_20001cda, DAT_20001cdc and DAT_20001cde are all zero, it computes a divider DAT_20001538 with util_map_range_clamp_high and returns early (skipping the frame commit) until DAT_20001504 has counted past it; otherwise it shows the level as two digits (0 at 100 and above) with vcu_level_bar_draw, and steps the displayed level DAT_20001502 by at most +5 toward the target when DAT_20001aec bit 3 is set. If any of the four words is nonzero, it sets the LCD bit 3 and shows the next entry of the table DAT_20002248 (count DAT_200021e6) two digits at a time, each for 301 calls. Unless it returned early, the frame is committed with vcu_0159_0800ed4c(frame, DAT_200022dd) on every call.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | display level 0..100 (clamped to 100) |

**Notes:** The meaning of the four group words and of the table DAT_20002248 is not defined in this packet.

- Addresses by version: 0159: 0x0800B0C4
- Called by: `vcu_display_frame_render_tick`
- Calls: `vcu_level_bar_draw`, `lcd_fb_show_number_2digit`, `lcd_fb_set_d3_bit3`, `vcu_led_tm1640_frame_commit`, `util_map_range_clamp_high`
- Confidence: medium

## vcu_level_gauge_update_v148

**Update the VCU_148 level gauge: bar, 2-digit number and LED frame commit**

VCU_148-only variant of the 0..100 level display. It clamps the level to 100, zeroes the 16-byte frame DAT_200021ce and maps the level to a divider DAT_20001482 (0..10) with util_map_range_clamp_high. Unless the rate gate returns early, it updates the display once every divider+1 calls and sets bit 0 of DAT_20001488 when group A (DAT_20001c0c, 0e, 10, 12) is nonzero and bit 5 when group B (DAT_20001c14, 16, 18) is nonzero. With group A zero and either group B zero or DAT_200022de zero, it shows the level as two digits; with only group B set it sets the LCD bit 3 and cycles a per-item table at offset 0x12 every 301 calls, and with group A set it sets the LCD bit 3 and cycles a table at offset 0x72. The displayed level DAT_2000144f is drawn with vcu_level_bar_draw and may step up by at most 5 per update toward the target (never above the target or 109) when DAT_20001a20 bit 2 is set. Unless the rate gate returned early, the frame is committed with vcu_0159_0800ed4c(frame, 0x87).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | display level 0..100 (clamped to 100) |

**Notes:** The table base pointers come from a register that the decompile does not show, so the table contents are not known. Item names are not defined in this packet.

- Addresses by version: 148: 0x0800A138
- Calls: `vcu_level_bar_draw`, `lcd_fb_show_number_2digit`, `lcd_fb_set_d3_bit3`, `vcu_led_tm1640_frame_commit`, `util_map_range_clamp_high`
- Confidence: medium

## vcu_level_gauge_update_v14a_153

**Update the level gauge for VCU_14A to VCU_153: 2-digit number, bar and LED frame commit**

Level display for builds 14a to 153, the same design as vcu_level_gauge_update_v148 but without the group logic. It clamps the level to 100, zeroes the 16-byte frame DAT_200021b6 and maps the level to a divider DAT_2000152a with util_map_range_clamp_high. It returns early, without committing the frame, until DAT_200014f7 has counted past the divider; on an update it shows the level as two digits when it is below 100 (0 otherwise), then sets DAT_200014f6 to the level, stepping up by at most 5 toward the target (never above the target or 109) when DAT_20001adc bit 2 is set, and draws the bar with vcu_level_bar_draw. The frame is committed with vcu_0159_0800ed4c(frame, DAT_200022cd) on every call that does not return early.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | display level 0..100 (clamped to 100) |

**Notes:** The divider rate-gate and the target step are as coded. The variant is present in six builds, so the RAM addresses differ from VCU_148 and VCU_0159.

- Addresses by version: 14a: 0x0800A618, 14b: 0x0800AAA0, 14e: 0x0800AB34, 14f: 0x0800AC70, 152: 0x0800AEF0, 153: 0x0800AFE4
- Called by: `vcu_display_frame_render_tick`
- Calls: `vcu_level_bar_draw`, `lcd_fb_show_number_2digit`, `vcu_led_tm1640_frame_commit`, `util_map_range_clamp_high`
- Confidence: medium
