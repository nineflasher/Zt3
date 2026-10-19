# VCU - `display` functions

16 functions.

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
| [`vcu_display_anim_step`](#vcu_display_anim_step) | 0x0800C31C | Display animation step per mode: blink icons (10), sweep segments up (12), icons on |
| [`vcu_display_sweep_down_step`](#vcu_display_sweep_down_step) | 0x0800C4F0 | Downward segment sweep (20 to 0) while DAT_20001f58 is set; otherwise all icons on |

## lcd_fb_clear_cd_low_nibble

**Clear the low nibble of frame-buffer byte 0x200021cd**

Masks DAT_200021cd with 0xf0, turning off the four segments set by lcd_fb_set_cd_low_nibble; the upper nibble (icon group B bits) is kept. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. The decompiler lists 0x200021c6 as address-taken only because the byte is addressed relative to the buffer base via the literal pool; it is not accessed.

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B92C, 14a: 0x0800BD70, 14b: 0x0800C1FC, 14e: 0x0800C290, 14f: 0x0800C3CC, 152: 0x0800C658, 153: 0x0800C74C, 0159: 0x0800C7B8
- Called by: `vcu_0159_080057ac`
- Confidence: medium

## lcd_fb_set_c9_low2

**Set or clear bits 1:0 of frame-buffer byte 0x200021c9**

Clears the two low bits of DAT_200021c9 (mask 0xfc) and sets both (0x03) when param_1 is non-zero. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Two-segment setter.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = both segments on |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B93C, 14a: 0x0800BD80, 14b: 0x0800C20C, 14e: 0x0800C2A0, 14f: 0x0800C3DC, 152: 0x0800C668, 153: 0x0800C75C, 0159: 0x0800C7C8
- Called by: `vcu_0159_080057ac`
- Confidence: medium

## lcd_fb_set_cd_low_nibble

**Set low nibble of frame-buffer byte 0x200021cd to 0xC or 0x3**

Keeps the upper nibble of DAT_200021cd and writes the low nibble as 0x0c when param_1 is non-zero, 0x03 when it is zero (two complementary 2-bit segment pairs). Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Paired with lcd_fb_clear_cd_low_nibble which blanks the nibble.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero selects pattern 0xC, zero selects pattern 0x3 |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B900, 14a: 0x0800BD44, 14b: 0x0800C1D0, 14e: 0x0800C264, 14f: 0x0800C3A0, 152: 0x0800C62C, 153: 0x0800C720, 0159: 0x0800C78C
- Called by: `vcu_0159_080057ac`
- Confidence: medium

## lcd_fb_set_d1_bit2

**Set or clear bit 2 of frame-buffer byte 0x200021d1**

Read-modify-write of DAT_200021d1: clears bit 2 (mask 0xfb), sets it when param_1 is non-zero. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Single-segment (icon) setter.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = segment on |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B7D4, 14a: 0x0800BC18, 14b: 0x0800C0A4, 14e: 0x0800C138, 14f: 0x0800C274, 152: 0x0800C500, 153: 0x0800C5F4, 0159: 0x0800C660
- Called by: `vcu_0159_080057ac`
- Confidence: medium

## lcd_fb_set_d1_bit6

**Set or clear bit 6 of frame-buffer byte 0x200021d1**

Read-modify-write of DAT_200021d1: clears bit 6 (mask 0xbf), sets it when param_1 is non-zero. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Single-segment (icon) setter; bits 0/1 of the same byte are touched by other helpers (0x200021d0/d1 are also written by the neighbouring routines at 0x0800aa9c and 0x0800be30).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = segment on |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B7F0, 14a: 0x0800BC34, 14b: 0x0800C0C0, 14e: 0x0800C154, 14f: 0x0800C290, 152: 0x0800C51C, 153: 0x0800C610, 0159: 0x0800C67C
- Called by: `vcu_0159_080057ac`
- Confidence: medium

## lcd_fb_set_d3_bit3

**Set or clear bit 3 of frame-buffer byte 0x200021d3**

Clears bit 3 of DAT_200021d3 (mask 0xf7) and sets it when param_1 is non-zero. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Single-segment setter; also called from vcu_0159_0800b0c4 and vcu_148_0800a138, i.e. from outside the main display routine.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = segment on |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B990, 14a: 0x0800BDD4, 14b: 0x0800C260, 14e: 0x0800C2F4, 14f: 0x0800C430, 152: 0x0800C6BC, 153: 0x0800C7B0, 0159: 0x0800C81C
- Called by: `vcu_0159_080057ac`, `vcu_0159_0800b0c4`
- Confidence: medium

## lcd_fb_set_d4_bit2

**Set or clear bit 2 of frame-buffer byte 0x200021d4**

Read-modify-write of DAT_200021d4: clears bit 2 (mask 0xfb) and sets it again when param_1 is non-zero. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Single-segment (icon) setter.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = segment on |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B7B8, 14a: 0x0800BBFC, 14b: 0x0800C088, 14e: 0x0800C11C, 14f: 0x0800C258, 152: 0x0800C4E4, 153: 0x0800C5D8, 0159: 0x0800C644
- Called by: `vcu_0159_080057ac`
- Confidence: medium

## lcd_fb_set_d4_bits45

**Set or clear bits 5:4 of frame-buffer byte 0x200021d4**

Clears bits 5:4 of DAT_200021d4 (mask 0xcf) and sets both (0x30) when param_1 is non-zero. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Two-segment setter.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = both segments on |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B974, 14a: 0x0800BDB8, 14b: 0x0800C244, 14e: 0x0800C2D8, 14f: 0x0800C414, 152: 0x0800C6A0, 153: 0x0800C794, 0159: 0x0800C800
- Called by: `vcu_0159_080057ac`
- Confidence: medium

## lcd_fb_set_d4_low2

**Set or clear bits 1:0 of frame-buffer byte 0x200021d4**

Clears the two low bits of DAT_200021d4 (mask 0xfc) and sets both (0x03) when param_1 is non-zero. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Two-segment setter.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = both segments on |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B958, 14a: 0x0800BD9C, 14b: 0x0800C228, 14e: 0x0800C2BC, 14f: 0x0800C3F8, 152: 0x0800C684, 153: 0x0800C778, 0159: 0x0800C7E4
- Called by: `vcu_0159_080057ac`
- Confidence: medium

## lcd_fb_set_icon_group_a

**Set or clear bits 4-6 of frame-buffer bytes 0x200021c7, c9 and cb**

Clears bits 6:4 (mask 0x8f keeps the rest) of DAT_200021c7, DAT_200021c9 and DAT_200021cb, then, if param_1 is non-zero, ORs 0x70 back into all three so the three-bit group is all on; otherwise all three groups are off. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Each byte is the high nibble area next to a digit (the digit low nibble is written by lcd_fb_show_number_2digit); likely an icon/bar-segment group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = turn the 0x70 bits on, zero = off |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B748, 14a: 0x0800BB8C, 14b: 0x0800C018, 14e: 0x0800C0AC, 14f: 0x0800C1E8, 152: 0x0800C474, 153: 0x0800C568, 0159: 0x0800C5D4
- Called by: `vcu_0159_080057ac`, `vcu_display_anim_step`, `vcu_display_sweep_down_step`
- Confidence: medium

## lcd_fb_set_icon_group_b

**Set or clear icon bits in frame-buffer bytes 0x200021cd, d4 and d5**

Clears bits 6:4 of DAT_200021cd, bits 7:6 of DAT_200021d4 and the low nibble of DAT_200021d5 (masks 0x8f, 0x3f, 0xf0). If param_1 is non-zero it then sets 0x70 in cd, 0xc0 in d4 and 0x0f in d5, i.e. a 3+2+4 = 9-segment group is switched on or off as a unit. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Sibling of lcd_fb_set_icon_group_a.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero = all nine segments on, zero = all off |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B780, 14a: 0x0800BBC4, 14b: 0x0800C050, 14e: 0x0800C0E4, 14f: 0x0800C220, 152: 0x0800C4AC, 153: 0x0800C5A0, 0159: 0x0800C60C
- Called by: `vcu_0159_080057ac`, `vcu_display_anim_step`, `vcu_display_sweep_down_step`
- Confidence: medium

## lcd_fb_set_mode_indicator

**Select one of four exclusive indicator segments in frame-buffer byte 0x200021cf**

Clears bits 1, 2, 3 and 5 of DAT_200021cf (mask 0xd1, bits 0, 4, 6, 7 are preserved), then lights exactly one segment by value: 1 -> 0x08, 2 -> 0x04, 3 -> 0x02, 4 -> 0x20; any other value (e.g. 0) leaves all four off. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Behaves like a mutually exclusive mode / level indicator (e.g. riding mode or gear icons); the meaning of the four icons is not visible here.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | indicator index 1..4, anything else = none lit |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known.

- Addresses by version: 148: 0x0800B80C, 14a: 0x0800BC50, 14b: 0x0800C0DC, 14e: 0x0800C170, 14f: 0x0800C2AC, 152: 0x0800C538, 153: 0x0800C62C, 0159: 0x0800C698
- Called by: `vcu_0159_080057ac`
- Confidence: medium

## lcd_fb_show_digit_units

**Show one decimal digit in the units position and blank the tens position**

param_1 is clamped (values above 10 become 9) and reduced modulo 10, so 10 shows as 0. The tens position is blanked: DAT_200021c6=0, low nibble of DAT_200021c7=0, DAT_200021c8=0. The units position is loaded from the glyph tables: DAT_200021ca = table_A[d] (0x20001548+d), low nibble of DAT_200021cb = table_B[d] (0x20001552+d), DAT_200021cc = table_C[d] (0x2000155c+d); the upper nibble of cb is preserved because it belongs to the 0x70 icon group. The display frame buffer is the 16-byte RAM block 0x200021c6..0x200021d5 (fb[0]=0x200021c6 ... fb[15]=0x200021d5); the three digit glyph tables are 10-byte arrays at 0x20001548, 0x20001552 and 0x2000155c. Part of the segment/LCD frame-buffer helper group (0x0800c5d4..0x0800c81c) that is driven by the main vehicle state/display routine vcu_0159_080057ac; the group is a bit-field setter family over the 0x200021c6..0x200021d5 buffer. Always displays, unlike lcd_fb_show_number_2digit which has an enable flag.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | digit 0..9 (values above 10 are forced to 9, 10 wraps to 0) |

**Notes:** Role as an LCD/segment frame buffer is inferred from the glyph tables and nibble/bit masking; which physical icon each bit drives is not known. The 7-segment glyph encoding of the tables is assumed; the tables are RAM and presumably initialised at startup.

- Addresses by version: 148: 0x0800B84C, 14a: 0x0800BC90, 14b: 0x0800C11C, 14e: 0x0800C1B0, 14f: 0x0800C2EC, 152: 0x0800C578, 153: 0x0800C66C, 0159: 0x0800C6D8
- Called by: `vcu_0159_080057ac`
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
- Called by: `vcu_0159_080057ac`, `vcu_0159_0800b0c4`
- Confidence: medium

## vcu_display_anim_step

**Display animation step per mode: blink icons (10), sweep segments up (12), icons on**

Called once per tick with the requested mode. A new mode is accepted into DAT_2000150c only while the frame counter DAT_200021de is zero. Mode 10 blinks the icon groups: at counter multiples of 50 both groups are cleared and at multiples of 100 both are set and the counter wraps, giving 50 ticks on and 50 off. Modes 0, 9 and 13 turn both icon groups on. Mode 12 runs an upward segment sweep every DAT_200014f2 ticks: while the position DAT_2000150e is below DAT_200014f3 it clears the segment pair at the position, then it sets the pair at position minus the width until twice the width, and then wraps. Other modes do nothing.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | requested mode code, 0..13 |

**Notes:** Mode meanings are inferred from the animation each one produces. The segment and icon helpers are defined in the packet callee list.

- Addresses by version: 148: 0x0800B490, 14a: 0x0800B8D4, 14b: 0x0800BD60, 14e: 0x0800BDF4, 14f: 0x0800BF30, 152: 0x0800C1BC, 153: 0x0800C2B0, 0159: 0x0800C31C
- Called by: `vcu_0159_080057ac`
- Calls: `led_frame_set_segment_a`, `led_frame_set_segment_b`, `lcd_fb_set_icon_group_a`, `lcd_fb_set_icon_group_b`
- Confidence: medium

## vcu_display_sweep_down_step

**Downward segment sweep (20 to 0) while DAT_20001f58 is set; otherwise all icons on**

When DAT_20001f58 is zero it turns both icon groups on, resets its counter DAT_200021e2 and returns. Otherwise every DAT_200014f0 ticks it steps the position DAT_2000150a down from 20: while the position is above 10 it sets the segment pair at position minus DAT_200014f1 (the window width), and otherwise it clears the segment pair at the position, wrapping back to 20 at zero. The result is a window of lit segments that moves downward and then blanks out.

**Notes:** Companion of vcu_display_anim_step, which sweeps upward.

- Addresses by version: 148: 0x0800B664, 14a: 0x0800BAA8, 14b: 0x0800BF34, 14e: 0x0800BFC8, 14f: 0x0800C104, 152: 0x0800C390, 153: 0x0800C484, 0159: 0x0800C4F0
- Called by: `vcu_0159_080057ac`
- Calls: `led_frame_set_segment_a`, `led_frame_set_segment_b`, `lcd_fb_set_icon_group_a`, `lcd_fb_set_icon_group_b`
- Confidence: medium
