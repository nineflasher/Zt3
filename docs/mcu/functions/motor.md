# MCU - `motor` functions

30 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_band_block_arm_setpoint`](#mcu_band_block_arm_setpoint) | 0x0800725C | Arm a compact band block: set the byte at +0x1C to 1 and store two values at +0x08 and +0x18 |
| [`mcu_band_block_init`](#mcu_band_block_init) | 0x08007198 | Initialise a band block: bounds, half-span \|p4-p5\|/2 and mode bytes +0x20..+0x22 |
| [`mcu_band_block_init_compact`](#mcu_band_block_init_compact) | 0x080071DE | Initialise a compact band block: bounds, half-span \|p4-p5\|/2 and mode bytes at +0x1C..+0x1E |
| [`mcu_below_10pct_of_window`](#mcu_below_10pct_of_window) | 0x08003638 | Return 1 if a Q15-scaled value lies in the lowest 10% of the window [DAT_20000bee, DAT_20000bec] |
| [`mcu_ctrl_block_reset_flags`](#mcu_ctrl_block_reset_flags) | 0x08006C86 | Reset a control block: clear three state words, set the byte at +0x29 to 1, clear +0x28 |
| [`mcu_get_limit_min3_or_unbounded`](#mcu_get_limit_min3_or_unbounded) | 0x08004AC4 | Return DAT_20000660 clamped to >= 0x18000, or 0x7fff8000 if it is zero |
| [`mcu_limit_block_arm_setpoint`](#mcu_limit_block_arm_setpoint) | 0x0800724E | Arm a limit block: set the enable byte at +0x20 to 1 and store two values at +0x08 and +0x1C |
| [`mcu_limit_block_bind_io`](#mcu_limit_block_bind_io) | 0x08006F44 | Bind gains and the reference and output pointers into a limit block and set all mode bytes to 1 |
| [`mcu_limit_block_init_params`](#mcu_limit_block_init_params) | 0x08006DE8 | Store seven configuration words and a flag into a limit block; set the Q15 word at +0x20 to 1.0 |
| [`mcu_limit_block_update`](#mcu_limit_block_update) | 0x08006E18 | Per-cycle limit update: bounds X and Y from two Q15 gains, output selected by mode bytes |
| [`mcu_mul_q15_f5e_by_3f2`](#mcu_mul_q15_f5e_by_3f2) | 0x08002208 | Q15 multiply of RAM value 0x20000f5e (shifted to Q15) by 0x200003f2, result >> 15 |
| [`mcu_param_block3_init_checked`](#mcu_param_block3_init_checked) | 0x08001E18 | Validate and fill a 3-word parameter block, setting a valid flag at +0x2c |
| [`mcu_param_block4_init_checked`](#mcu_param_block4_init_checked) | (removed) | Fill a 4-word parameter block if the first two values are positive |
| [`mcu_param_block8_init_checked`](#mcu_param_block8_init_checked) | 0x08002A34 | Fill an 8-word parameter block if the first and third values are positive |
| [`mcu_pi_update_gain_sched`](#mcu_pi_update_gain_sched) | 0x0800833C | PI step with speed-scheduled gains (Kp doubled, Ki halved below 0xF0001) and one-sided anti-windup |
| [`mcu_pid_set_limits`](#mcu_pid_set_limits) | 0x08008282 | Store PID output limits (min < max) and clamp the live output when the loop is enabled |
| [`mcu_pid_sync_integrator`](#mcu_pid_sync_integrator) | 0x08008260 | Reset PID integrator to the clamped current output and latch the current measurement |
| [`mcu_pid_update_q15`](#mcu_pid_update_q15) | 0x08008128 | PID-style controller step in Q15 with derivative on measurement and clamped output |
| [`mcu_position_multiturn_compute`](#mcu_position_multiturn_compute) | 0x08009050 | Compute relative position = raw + wraps x 0x6487E - reference, saturated to +-0x7FBC0000 |
| [`mcu_position_rebase`](#mcu_position_rebase) | 0x08009044 | Set the multi-turn reference to the current raw counter and clear the wrap count |
| [`mcu_q15_to_percent_s16`](#mcu_q15_to_percent_s16) | 0x080047B4 | Convert the Q15 value at 0x20000a50 to a percentage (x * 100 / 32768) as s16 |
| [`mcu_ramp_toward_target_s32`](#mcu_ramp_toward_target_s32) | 0x08002982 | Move *value toward target by at most \|step\| (slew-rate limiter) |
| [`mcu_sample_history3_rise_detect`](#mcu_sample_history3_rise_detect) | 0x0800D9C4 | Push a 0..200 sample into a 3-deep history and flag three consecutive large rises |
| [`mcu_scale_delta_q15`](#mcu_scale_delta_q15) | 0x08002078 | Return (DAT_20000f5a - DAT_2000027e) * 0xdbf using Q15 fixed-point arithmetic |
| [`mcu_setpoint_slew_limit_std`](#mcu_setpoint_slew_limit_std) | 0x08007F24 | Slew-limit the scaled setpoint into filter DAT_20000F46 and derive output limit DAT_20000F48 |
| [`mcu_setpoint_slew_limit_v12b`](#mcu_setpoint_slew_limit_v12b) | (removed) | Slew-limit the scaled setpoint into filter DAT_20000F02 and derive output limit DAT_20000F04 (12b) |
| [`mcu_sq_scale_block_init`](#mcu_sq_scale_block_init) | 0x0800641A | Initialise a block with (n*n/64) in Q15 for 0 <= n <= 2000 and set its valid byte |
| [`mcu_update_flag_e32_from_mode_3`](#mcu_update_flag_e32_from_mode_3) | 0x080056C4 | Set DAT_20000e32 to 1 when mode byte 0x2000065a equals 3, else 0 |
| [`mcu_update_motion_direction_flags`](#mcu_update_motion_direction_flags) | 0x08005550 | Set one of two flags (0x20000e1d / 0x20000e1e) from mode bits 3..4 when \|value\| and counter qualify |
| [`mcu_update_motion_flag_old`](#mcu_update_motion_flag_old) | (removed) | Set flag 0x20000dfd when a counter >= 20, \|value\| <= 0x50000 and mode bit2 is set (12b/143) |

## mcu_band_block_arm_setpoint

**Arm a compact band block: set the byte at +0x1C to 1 and store two values at +0x08 and +0x18**

Sets the byte at +0x1C to 1, stores param_2 in word 2 (+0x08), stores param_3 in word 6 (+0x18), and returns 1. Callers are mcu_0160_080029ac and mcu_0160_08002b64.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | compact band block |
| `param_2` | `s32` | value stored at +0x08 |
| `param_3` | `s32` | value stored at +0x18 |

**Returns** `bool`: always 1

**Notes:** mcu_band_block_init_compact clears the byte at +0x1C and uses +0x1D as its enable, so the relation between these two functions is unclear.

- Addresses by version: 143: 0x08007284, 152: 0x080072B4, 0160: 0x0800725C
- Called by: `mcu_0160_080029ac`, `mcu_0160_08002b64`
- Confidence: medium

## mcu_band_block_init

**Initialise a band block: bounds, half-span |p4-p5|/2 and mode bytes +0x20..+0x22**

Stores p2 in word 2, p3 in word 0, the bounds p4 and p5 in words 3 and 4, and p6 in the byte at +0x18. Word 5 gets half the distance between the bounds, |p4 - p5| / 2, using the x*0x4000 >> 15 idiom. The mode bytes are set to +0x20 = 0 (pass-through), +0x21 = 1 (enabled) and +0x22 = p7. Returns 1. Called from mcu_0160_08003784 and mcu_0160_080078f0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | band block |
| `param_2` | `s32` | stored in word 2 |
| `param_3` | `s32` | stored in word 0 |
| `param_4` | `s32` | lower or upper bound, word 3 |
| `param_5` | `s32` | other bound, word 4 |
| `param_6` | `u8` | stored at byte +0x18 |
| `param_7` | `u8` | stored at byte +0x22 |

**Returns** `bool`: always 1

**Notes:** Uses the same mode-byte convention as mcu_limit_block_update, but the +0x18 field is a byte here and a pointer there, so these may be different objects.

- Addresses by version: 12b: 0x080072E6, 143: 0x080071C0, 152: 0x080071F0, 0160: 0x08007198
- Called by: `mcu_0160_08003784`, `mcu_0160_080078f0`
- Confidence: medium

## mcu_band_block_init_compact

**Initialise a compact band block: bounds, half-span |p4-p5|/2 and mode bytes at +0x1C..+0x1E**

Stores p2 in word 2, p3 in word 0, the bounds p4 and p5 in words 3 and 4, and word 5 = |p4 - p5| / 2. It clears the byte at +0x1C, sets the byte at +0x1D to 1 (enable) and stores p6 at +0x1E. The layout is the same as mcu_band_block_init but without the +0x18 byte, with the mode bytes four bytes lower. Called from mcu_0160_080029ac and mcu_12b_08002b70. Returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | compact band block |
| `param_2` | `s32` | stored in word 2 |
| `param_3` | `s32` | stored in word 0 |
| `param_4` | `s32` | bound, word 3 |
| `param_5` | `s32` | bound, word 4 |
| `param_6` | `u8` | stored at byte +0x1E |

**Returns** `bool`: always 1

- Addresses by version: 12b: 0x0800732C, 143: 0x08007206, 152: 0x08007236, 0160: 0x080071DE
- Called by: `mcu_0160_080029ac`
- Confidence: medium

## mcu_below_10pct_of_window

**Return 1 if a Q15-scaled value lies in the lowest 10% of the window [DAT_20000bee, DAT_20000bec]**

Computes (param_1 - bee * 0x8000) / (bec - bee + 1) with signed 32-bit division, where bee and bec are 16-bit RAM values (low and high bounds) and param_1 is the input scaled by 0x8000. That yields the position within the window as a Q15 fraction; returns 1 if it is below 0xccc (3276, about 0.0999 = 10%), else 0. Called from mcu_0160_08005090 and 080051bc (and mcu_12b_08004e74).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | value in Q15 (raw * 0x8000) to test against the window |

**Returns** `bool`: 1 if in the lowest 10% of the window

**Notes:** Interpretation of the window (speed/throttle/torque range) unknown.

- Addresses by version: 12b: 0x080036F8, 143: 0x080035F8, 152: 0x08003598, 0160: 0x08003638
- Called by: `mcu_0160_08005090`, `mcu_0160_080051bc`
- Confidence: medium

## mcu_ctrl_block_reset_flags

**Reset a control block: clear three state words, set the byte at +0x29 to 1, clear +0x28**

Clears the words at +0x18, +0x20 and +0x24 (state accumulators or last-sample registers), clears the byte at +0x28 and sets the byte at +0x29 to 1, then returns 1. This is the reset routine of a controller block whose state occupies +0x18..+0x2C. The byte at +0x29 is probably an enable or armed flag, which is inferred. Called from mcu_0160_08006b70.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | control block, at least 0x2A bytes |

**Returns** `bool`: always 1

- Addresses by version: 12b: 0x08006DDA, 143: 0x08006CAE, 152: 0x08006CDE, 0160: 0x08006C86
- Called by: `mcu_0160_08006b70`
- Confidence: medium

## mcu_get_limit_min3_or_unbounded

**Return DAT_20000660 clamped to >= 0x18000, or 0x7fff8000 if it is zero**

If the 32-bit value at 0x20000660 is zero the function returns 0x7fff8000, effectively an unlimited maximum (about 65535.0 in Q15). Otherwise it returns the value but never less than 0x18000 (3.0 in Q15). Treats 0 as 'feature/limit disabled' and enforces a floor on configured limits. Called from mcu_0160_08003d2c, 080052bc, 0800576c and 0800ce3c.

**Returns** `s32`: limit in Q15, minimum 0x18000, 0x7fff8000 when unset

**Notes:** Physical unit unknown (current, speed or time).

- Addresses by version: 12b: 0x08004950, 143: 0x08004944, 152: 0x08004A24, 0160: 0x08004AC4
- Called by: `mcu_0160_08003d2c`, `mcu_0160_080052bc`, `mcu_0160_0800576c`, `mcu_0160_0800ce3c`
- Confidence: medium

## mcu_limit_block_arm_setpoint

**Arm a limit block: set the enable byte at +0x20 to 1 and store two values at +0x08 and +0x1C**

Sets the byte at +0x20 to 1, stores param_2 in word 2 (+0x08) and param_3 in word 7 (+0x1C), and returns 1. This hands a new setpoint and a second value to the block and enables it for the next update. Callers are mcu_0160_08003784 and mcu_0160_08004e78.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | limit block |
| `param_2` | `s32` | setpoint, stored in word 2 |
| `param_3` | `s32` | second value, stored in word 7 |

**Returns** `bool`: always 1

**Notes:** Word 7 is the output pointer in mcu_limit_block_update, so this writes a value over a pointer. Either it is a different object type or it is a bug. Check the callers.

- Addresses by version: 12b: 0x08007390, 143: 0x08007276, 152: 0x080072A6, 0160: 0x0800724E
- Called by: `mcu_0160_08003784`, `mcu_0160_08004e78`
- Confidence: medium

## mcu_limit_block_bind_io

**Bind gains and the reference and output pointers into a limit block and set all mode bytes to 1**

If both param_4 (reference pointer, stored in word 6) and param_5 (output pointer, word 7) are non-null, it stores param_2 as gain w0 and param_3 as gain w1, sets the mode bytes +0x20, +0x21 and +0x22 to 1 (enable, low clamp, high clamp, mode value 7), and returns 1. Otherwise it changes nothing and returns 0. Called from mcu_0160_080078f0 after mcu_limit_block_init_params.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | limit block |
| `param_2` | `s32` | gain w0 |
| `param_3` | `s32` | gain w1 |
| `param_4` | `ptr` | reference S, stored in word 6 |
| `param_5` | `ptr` | output, stored in word 7 |

**Returns** `bool`: 1 = bound, 0 = rejected (null pointer)

- Addresses by version: 12b: 0x08007098, 143: 0x08006F6C, 152: 0x08006F9C, 0160: 0x08006F44
- Called by: `mcu_0160_080078f0`
- Confidence: high

## mcu_limit_block_init_params

**Store seven configuration words and a flag into a limit block; set the Q15 word at +0x20 to 1.0**

Writes param_8 to word 0, param_3 to word 2, param_4 to word 3, param_5 to word 4, param_6 to word 5, param_2 to word 6 and param_7 to word 7, and writes param_9 to the byte at +0x3C. It clears the words at +0x24 and +0x2C and stores 0x8000 (Q15 1.0) in the word at +0x20. The byte at +0x20 is the mode byte that mcu_limit_block_update reads, and the 0x8000 leaves it 0, so the block starts in pass-through mode. Called from mcu_0160_080078f0 alongside mcu_limit_block_bind_io.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | limit block |
| `param_2` | `s32` | stored in word 6 |
| `param_3` | `s32` | stored in word 2 |
| `param_4` | `s32` | stored in word 3 |
| `param_5` | `s32` | stored in word 4 |
| `param_6` | `s32` | stored in word 5 |
| `param_7` | `s32` | stored in word 7 |
| `param_8` | `s32` | stored in word 0, later overwritten by mcu_limit_block_bind_io |
| `param_9` | `u8` | stored at byte +0x3C |

**Returns** `bool`: always 1

**Notes:** Physical meaning of the configuration words is not visible here.

- Addresses by version: 12b: 0x08006F3C, 143: 0x08006E10, 152: 0x08006E40, 0160: 0x08006DE8
- Called by: `mcu_0160_080078f0`
- Confidence: medium

## mcu_limit_block_update

**Per-cycle limit update: bounds X and Y from two Q15 gains, output selected by mode bytes**

Inputs are the block and four samples p2..p5. The block holds gains w0 and w1 (Q15), the current and previous sample (words 4 and 5), pointers to a reference S (word 6) and to the output (word 7), and mode bytes at +0x20 (enable), +0x21 (low clamp) and +0x22 (high clamp). It forms X = p3 + w0*(p4-p2) - w1*(p2-prev) and Y = p3 + w0*(p5-p2) - w1*(p2-prev), each product Q15 rounded, then selects the output: S when the enable byte is 0; max(S,Y) for the low clamp alone; min(S,X) for the high clamp alone; and with both, max(S,Y) if S <= X and X otherwise. A final rule forces a negative output to zero when the value at 0x20000F30 is <= 0 and bit 2 of 0x2000065D is clear. Intermediate values are copied to 0x20000350..0x200003A0 for monitoring.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | limit block (see description) |
| `param_2` | `s32` | current sample p2 |
| `param_3` | `s32` | base value p3 |
| `param_4` | `s32` | upper sample p4 |
| `param_5` | `s32` | lower sample p5 |

**Notes:** The mode table and arithmetic are read directly from the code. The physical meaning of the gains, bounds and the 0x2000065D bit is unknown.

- Addresses by version: 12b: 0x08006F6C, 143: 0x08006E40, 152: 0x08006E70, 0160: 0x08006E18
- Called by: `mcu_0160_0800a320`
- Confidence: medium

## mcu_mul_q15_f5e_by_3f2

**Q15 multiply of RAM value 0x20000f5e (shifted to Q15) by 0x200003f2, result >> 15**

Loads the 16-bit value at 0x20000f5e, shifts it left by 15 (so it is treated as an integer in Q15), multiplies it by the 16-bit value at 0x200003f2 with a 64-bit signed multiply and returns the product >> 15, i.e. effectively f5e * 3f2 without overflow. Called from mcu_0160_08005b3c (and the 12b equivalent). Acts as a gain/scale step; the second operand is probably a calibration or configuration scale factor.

**Returns** `u32`: DAT_20000f5e * DAT_200003f2

**Notes:** Operand meanings unknown; arithmetic is certain.

- Addresses by version: 12b: 0x0800222C, 143: 0x08002268, 152: 0x080021EC, 0160: 0x08002208
- Called by: `mcu_0160_08005b3c`
- Confidence: medium

## mcu_param_block3_init_checked

**Validate and fill a 3-word parameter block, setting a valid flag at +0x2c**

Accepts (block, a, b, c). If a != 0, 0 <= b <= 0x40000000 and c >= 0 it stores a, b, c into words 0..2 of the block, clears word 3 (a running/accumulator value) and sets the byte at offset 0x2c (param_1+0xb words) to 1, returning 1. Otherwise it only clears the valid byte at +0x2c and returns 0. Looks like the init routine of a controller/filter object (gain, limit, initial value); called once from the larger setup function mcu_0160_080029ac together with mcu_0160_08002a34. Exact meaning of the three fields is not visible here.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | block to initialise (>= 0x30 bytes; word0..2 params, word3 state, byte at +0x2c = valid) |
| `param_2` | `s32` | must be non-zero, stored in word 0 |
| `param_3` | `s32` | 0..0x40000000, stored in word 1 |
| `param_4` | `s32` | >= 0, stored in word 2 |

**Returns** `bool`: 1 if parameters accepted, 0 if rejected

**Notes:** Role of the block (probably a PI/limiter or filter object) is a guess; behaviour itself is certain.

- Addresses by version: 143: 0x08001E78, 152: 0x08001DFC, 0160: 0x08001E18
- Called by: `mcu_0160_080029ac`
- Confidence: medium

## mcu_param_block4_init_checked

**Fill a 4-word parameter block if the first two values are positive**

If param_3 > 0 and param_2 > 0 stores param_2..param_5 in words 0..3 of the block and returns 1, else returns 0 without modification. 12b-build predecessor of mcu_param_block8_init_checked (mcu_0160_08002a34); called from mcu_12b_08002b70.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination block of 4 words |
| `param_2` | `s32` | word 0, must be > 0 |
| `param_3` | `s32` | word 1, must be > 0 |
| `param_4` | `s32` | word 2 |
| `param_5` | `s32` | word 3 |

**Returns** `bool`: 1 = stored, 0 = rejected

**Notes:** Field semantics unknown.

- Addresses by version: 12b: 0x08002C0E
- Called by: `mcu_12b_08002b70`
- Confidence: medium

## mcu_param_block8_init_checked

**Fill an 8-word parameter block if the first and third values are positive**

If param_4 > 0 and param_2 > 0, copies the eight input values param_2..param_9 into words 0..7 of the block param_1 and returns 1; otherwise leaves the block untouched and returns 0. Nine arguments (the last five on the stack). Called from the same setup function mcu_0160_080029ac as mcu_param_block3_init_checked; group of parameter-block initialisers for controller objects (cf. mcu_12b_08002c0e, a 4-word predecessor).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination block of 8 words |
| `param_2` | `s32` | word 0, must be > 0 |
| `param_3` | `s32` | word 1 |
| `param_4` | `s32` | word 2, must be > 0 |
| `param_5` | `s32` | word 3 |
| `param_6` | `s32` | word 4 |
| `param_7` | `s32` | word 5 |
| `param_8` | `s32` | word 6 |
| `param_9` | `s32` | word 7 |

**Returns** `bool`: 1 = stored, 0 = rejected

**Notes:** Field semantics unknown (probably PI gains/limits).

- Addresses by version: 143: 0x08002A9A, 152: 0x08002A1E, 0160: 0x08002A34
- Called by: `mcu_0160_080029ac`
- Confidence: medium

## mcu_pi_update_gain_sched

**PI step with speed-scheduled gains (Kp doubled, Ki halved below 0xF0001) and one-sided anti-windup**

Error e = *(+0x20) - *(+0x18). The divisor g is 2 when DAT_20000F30 < 0xF0001 and 1 otherwise: the proportional gain is Kp*g (Kp at +0x0C) and the integral gain is Ki/g (Ki at +0x10), i.e. gain scheduling on DAT_20000F30. The integrator at +0x30 accumulates (Ki/g * e + 0x4000) >> 15; the step is one-sided while the previous output saturated high (DAT_20000348 set: only negative steps) or low (DAT_20000349 set: only positive steps). The integrator is clamped to [+0x24, +0x28]. The output (Kp*g*e + 0x4000) >> 15 plus the integrator is clamped: above max it writes max and sets DAT_20000348, below min it writes min and sets DAT_20000349, otherwise both flags are cleared. The result goes to *(+0x1C). There is no derivative term and no enable check.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | PI object: refs +0x18/+0x20, output ptr +0x1C, Kp +0x0C, Ki +0x10, integrator +0x30, limits +0x24/+0x28 |

**Notes:** The scheduling interpretation (low-speed gain change) follows from the threshold constant only; DAT_20000F30 units unknown. Only caller: mcu_0160_08003f2c.

- Addresses by version: 143: 0x08008234, 152: 0x08008324, 0160: 0x0800833C
- Called by: `mcu_0160_08003f2c`
- Confidence: medium

## mcu_pid_set_limits

**Store PID output limits (min < max) and clamp the live output when the loop is enabled**

Accepts the new limits only when min (param_2) is below max (param_3): min is stored at +0x24 and max at +0x28, and 1 is returned. Otherwise nothing changes and 0 is returned. If the enable byte +0x3E is set, the output *(+0x1C) is clamped to [min, max] at once: a value above max becomes max, a value below min becomes min.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | PID object (layout as in mcu_pid_update_q15) |
| `param_2` | `s32` | new minimum output |
| `param_3` | `s32` | new maximum output |

**Returns** `bool`: 1 if the limits were accepted, 0 if min >= max

**Notes:** Callers mcu_0160_08003f2c, mcu_0160_08007822 and mcu_0160_08008204 are outside this packet.

- Addresses by version: 12b: 0x08008172, 143: 0x0800817A, 152: 0x0800826A, 0160: 0x08008282
- Called by: `mcu_0160_08003f2c`, `mcu_0160_08007822`, `mcu_0160_08008204`
- Confidence: high

## mcu_pid_sync_integrator

**Reset PID integrator to the clamped current output and latch the current measurement**

Sets the integrator at +0x30 to the present output *(+0x1C) clamped to [+0x24, +0x28], and stores the current measurement *(+0x18) in the previous-measurement slot +0x34. The clamp takes the output as-is if it lies within the limits and otherwise uses the nearer limit. Used to make the controller start from its current output (bumpless transfer), so the derivative term does not see a step at the restart.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | PID object (layout as in mcu_pid_update_q15) |

**Notes:** The bumpless-transfer purpose is inferred. Its caller mcu_0160_080082ac is outside this packet.

- Addresses by version: 12b: 0x08008150, 143: 0x08008158, 152: 0x08008248, 0160: 0x08008260
- Called by: `mcu_0160_080082ac`
- Confidence: medium

## mcu_pid_update_q15

**PID-style controller step in Q15 with derivative on measurement and clamped output**

Controller object fields: enable byte +0x3E, gate byte +0x3F, Kp at +0x0C, Ki at +0x10, Kd at +0x14, error-abort threshold at +0x38, output minimum +0x24 and maximum +0x28, integrator +0x30, previous measurement +0x34, saturation status byte +0x3C. The error is e = *(+0x20) - *(+0x18) (reference minus measurement). If disabled it returns 0 and changes nothing. If the gate byte is set and |e| exceeds +0x38 the integrator is cleared and no integral step is taken. The integral step is (Ki*e + 0x4000) >> 15, applied one-sided while the output was saturated high (flag +0x3C or +0x3D equal to 1: only negative steps) or low (equal to 2: only positive steps) - conditional-integration anti-windup. The output is param_2 (feed-forward base) + (Kp*e >> 15) + integrator - (Kd*(meas - previous) >> 15), clamped to [min,max]; +0x3C becomes 1 (high), 2 (low) or 0, the result is written through *(+0x1C) and the measurement is stored at +0x34.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | controller object (layout above) |
| `param_2` | `s32` | feed-forward base value added to the output |

**Returns** `bool`: 1 if the controller ran, 0 if disabled

**Notes:** The algorithm is read directly from the code; the role as a motor or current loop is a guess. Callers mcu_0160_08007364 and mcu_0160_0800772c are outside this packet.

- Addresses by version: 12b: 0x08008018, 143: 0x08008020, 152: 0x08008110, 0160: 0x08008128
- Called by: `mcu_0160_08007364`, `mcu_0160_0800772c`
- Confidence: high

## mcu_position_multiturn_compute

**Compute relative position = raw + wraps x 0x6487E - reference, saturated to +-0x7FBC0000**

Computes raw(+0x44) + wraps(+0xA4) x 0x6487E - reference(+0xAC) in 32-bit signed arithmetic. 0x6487E = 411774 = 6 x 0x10C15, which is one electrical revolution when each of the six hall sectors is 0x10C15 counts, so the wrap count +0xA4 counts electrical revolutions. If the result lies within +-0x7FBC0000 it is stored at +0xA8 and returned. Otherwise the saturated value +0x7FBC0000 (positive overflow) or -0x7FBC0000 = 0x80440000 (negative overflow) is stored and returned.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | drive context: raw +0x44, wrap count +0xA4, reference +0xAC, result +0xA8 |

**Returns** `s32`: relative position in counts, or the saturated +-0x7FBC0000

**Notes:** The relation of 0x6487E to the sector step is numerical, confirmed by 6 x 0x10C15 = 0x6487E. The wrap counter is maintained elsewhere, not in this packet. Caller mcu_0160_080031b8 is outside this packet.

- Addresses by version: 12b: 0x08008E00, 143: 0x08008F9C, 152: 0x08008FDC, 0160: 0x08009050
- Called by: `mcu_0160_080031b8`
- Confidence: high

## mcu_position_rebase

**Set the multi-turn reference to the current raw counter and clear the wrap count**

Copies the raw counter at +0x44 into the reference at +0xAC and clears the wrap count at +0xA4. After this call mcu_position_multiturn_compute reports zero for the current position.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | drive context |

**Notes:** Caller mcu_0160_08004d94 is outside this packet.

- Addresses by version: 12b: 0x08008DF4, 143: 0x08008F90, 152: 0x08008FD0, 0160: 0x08009044
- Called by: `mcu_0160_08004d94`
- Confidence: high

## mcu_q15_to_percent_s16

**Convert the Q15 value at 0x20000a50 to a percentage (x * 100 / 32768) as s16**

Multiplies DAT_20000a50 (32-bit signed) by 0x320000 (= 100 * 0x8000) in 64 bits, shifts right by 15 (so x * 100) and again by 15 (divide by 0x8000), then truncates to a signed 16-bit result. So 1.0 in Q15 maps to 100. Called from mcu_0160_0800c6f0, the code that builds the externally visible/communicated values.

**Returns** `s16`: percent value 0..100 (negative values possible)

**Notes:** What 0x20000a50 represents (throttle request? torque fraction?) is not known.

- Addresses by version: 12b: 0x08004640, 143: 0x08004634, 152: 0x08004714, 0160: 0x080047B4
- Called by: `mcu_0160_0800c6f0`
- Confidence: medium

## mcu_ramp_toward_target_s32

**Move *value toward target by at most |step| (slew-rate limiter)**

Takes the absolute value of step, then if *value is above target by more than step subtracts step, else if below target by more than step adds step, otherwise snaps *value to target exactly. Implements a per-call rate limit (ramp) on a 32-bit signed quantity, e.g. a torque/current/speed command. Called from four places (mcu_0160_08003434, 08003f2c, 0800adf0, 0800b10c), the control-loop code.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | target value |
| `param_2` | `ptr` | pointer to the current value (s32), updated in place |
| `param_3` | `s32` | maximum step per call (sign ignored) |

- Addresses by version: 12b: 0x080029A6, 143: 0x080029E2, 152: 0x08002966, 0160: 0x08002982
- Called by: `mcu_0160_08003434`, `mcu_0160_08003f2c`, `mcu_0160_0800adf0`, `mcu_0160_0800b10c`
- Confidence: high

## mcu_sample_history3_rise_detect

**Push a 0..200 sample into a 3-deep history and flag three consecutive large rises**

Ignores samples of 201 or more. For a valid sample it writes the output word at 0x20000680 as floor(sample * 4095 / 242) shifted left by 15 (a scaled Q-format value). It then checks whether the new sample and the three most recent history bytes at 0x20000670..0x20000672 form a run where each step (newer minus older) exceeds 35 (0x23); if so the byte at 0x20000673 is set to 20 (0x14). The history is then shifted by one (newest in 0x20000670). The flag is only set here and is not cleared, so some other code must clear or count it down. The meaning of the input signal is not visible in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | new sample, 0..200 |

**Notes:** The 4095 / 242 scaling was checked numerically for inputs 0..200. The purpose of the signal and the 0x20000673 consumer are unknown.

- Addresses by version: 152: 0x0800D884, 0160: 0x0800D9C4
- Called by: `mcu_0160_080085bc`
- Confidence: low

## mcu_scale_delta_q15

**Return (DAT_20000f5a - DAT_2000027e) * 0xdbf using Q15 fixed-point arithmetic**

Computes the unsigned 16-bit difference of two RAM values (0x20000f5a minus 0x2000027e, e.g. a measured value minus its offset/reference), shifts it into Q15 (<<15) and multiplies by the Q15 constant 0xdbf (3519, about 0.1074) using a 64-bit signed multiply, then shifts the 64-bit product right by 15. The net result is delta * 3519, i.e. a fixed-point rescale of a raw count difference. Called from mcu_0160_08005d84. The same Q15 pattern (0x8000 = 1.0) is used by the neighbouring helpers in this group.

**Returns** `u32`: (f5a - 27e) * 3519, a scaled difference

**Notes:** What the two RAM values physically are (ADC counts? current offset?) is not determinable from this function alone.

- Addresses by version: 12b: 0x0800209C, 143: 0x080020D8, 152: 0x0800205C, 0160: 0x08002078
- Called by: `mcu_0160_08005d84`
- Confidence: medium

## mcu_setpoint_slew_limit_std

**Slew-limit the scaled setpoint into filter DAT_20000F46 and derive output limit DAT_20000F48**

Same algorithm as mcu_setpoint_slew_limit_v12b with the 143/152/0160 RAM layout: input DAT_20000F30 scaled by 20/65536, filter DAT_20000F46 (+-1 step inside 20 counts, otherwise about delta/20, clamped to >= 0), output DAT_20000F48, mode byte DAT_20000E33 and threshold T = 5 x round-up-even(DAT_20001FDC). When the mode byte is not 1, the output follows the filter 20 or 10 counts above it, holds T inside a 10-count band and uses counter DAT_2000063C (up to 200) as a sustain count on the upper edge. When the mode byte is 1, DAT_2000063A counts how long the filter stays one bucket (200 calls) or two buckets (500 calls) away from DAT_20000E24 >> 15, and the output then snaps to DAT_20000E24 scaled by 20/65536; a filter more than two buckets away resets the count and passes the filter through.

**Notes:** Built for MCU_143, MCU_152 and MCU_0160 (not 12b). Units of DAT_20000F30, DAT_20000E24 and the mode byte are not established. Only caller: mcu_0160_0800a480.

- Addresses by version: 143: 0x08007E1C, 152: 0x08007F0C, 0160: 0x08007F24
- Called by: `mcu_0160_0800a480`
- Confidence: medium

## mcu_setpoint_slew_limit_v12b

**Slew-limit the scaled setpoint into filter DAT_20000F02 and derive output limit DAT_20000F04 (12b)**

The raw setpoint DAT_20000EEC is scaled by 20/65536 (x * 0x14 >> 16). The filter state DAT_20000F02 moves toward it: within +-20 counts it steps by 1 per call, beyond that it steps by about one twentieth of the error, and it is clamped to be non-negative. If the mode byte DAT_20000E0B is 1, the output DAT_20000F04 follows the filter until the filter's 10-count bucket, (F02 + 10) / 10, equals DAT_20000DFC >> 15 for 200 consecutive calls (counter DAT_2000062A); then it snaps to DAT_20000DFC scaled by 20/65536. Otherwise a threshold T = 5 x (byte at 0x20001F98 rounded up to even) sets flag DAT_20000628 (T <= DAT_20000F04), and the output follows the filter outside a 10-count band around T, holds T inside the band, and keeps its old value on the lower edge of the band unless DAT_20001F8E >= 195 and T <= output.

**Notes:** Units of the setpoint and of the mode byte are not established. The decompiler renders the step as a magic-number division by 20 with a sign fix-up, read here as delta/20. The 12b build has its own variant of the 143/152/0160 function mcu_setpoint_slew_limit_std.

- Addresses by version: 12b: 0x08007EF4
- Called by: `mcu_0160_0800a480`
- Confidence: medium

## mcu_sq_scale_block_init

**Initialise a block with (n*n/64) in Q15 for 0 <= n <= 2000 and set its valid byte**

Clears the valid byte at +0x40 first. If the block pointer is non-null and 0 <= param_2 <= 2000 (0x7D0), it zeroes words +0x00 and +0x04, stores (n*n)/64 shifted left by 15 into the word at +0x3C, sets the valid byte to 1 and returns 1. Otherwise it returns 0 with the valid byte cleared. The NULL check comes after the first store, so a NULL pointer faults. Called from mcu_0160_080078f0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | block of at least 0x44 bytes |
| `param_2` | `s32` | n, valid range 0..2000 |

**Returns** `bool`: 1 = initialised, 0 = rejected

**Notes:** The meaning of n and of the scaled value is not visible in this packet.

- Addresses by version: 12b: 0x08006492, 143: 0x0800634A, 152: 0x0800637A, 0160: 0x0800641A
- Called by: `mcu_0160_080078f0`
- Confidence: medium

## mcu_update_flag_e32_from_mode_3

**Set DAT_20000e32 to 1 when mode byte 0x2000065a equals 3, else 0**

Single comparison storing (DAT_2000065a == 3) into DAT_20000e32. Called from mcu_0160_08004e78 together with mcu_0160_08005550; part of the group of small per-cycle update routines that derive boolean flags from the configuration/mode bytes at 0x2000065x.

**Notes:** Meaning of mode value 3 unknown.

- Addresses by version: 12b: 0x080056BC, 143: 0x080055C0, 152: 0x08005624, 0160: 0x080056C4
- Called by: `mcu_0160_08004e78`
- Confidence: high

## mcu_update_motion_direction_flags

**Set one of two flags (0x20000e1d / 0x20000e1e) from mode bits 3..4 when |value| and counter qualify**

Clears both output flags (DAT_20000e1d, DAT_20000e1e) if the counter DAT_20000b20 < 20, if abs(DAT_20000f30) > 0x50000 (10.0 in Q15) or if bit 2 of mode byte 0x2000065d is clear. Otherwise it examines field m = (DAT_2000065d & 0x1f) >> 3 (bits 3..4): m == 2 sets e1d=1 / e1e=0, m == 3 sets e1d=0 / e1e=1, any other value clears both. Called from mcu_0160_08004e78 (a periodic update routine, with mcu_0160_080056c4). Successor of mcu_143_08005478 in the 152 and 0160 builds.

**Notes:** The two flags are probably mutually exclusive mode indicators (e.g. forward/reverse or two operating modes); not proven.

- Addresses by version: 152: 0x080054B0, 0160: 0x08005550
- Called by: `mcu_0160_08004e78`
- Confidence: medium

## mcu_update_motion_flag_old

**Set flag 0x20000dfd when a counter >= 20, |value| <= 0x50000 and mode bit2 is set (12b/143)**

If DAT_20000b00 < 20, clears DAT_20000dfd. Otherwise takes abs(DAT_20000f0c); if it is <= 0x50000 (10.0 in Q15) and bit 2 of the mode byte at 0x20000649 is set, sets DAT_20000dfd to 1, else to 0. Older (12b, 143) version of mcu_0160_08005550, which in later builds splits the result into two flags depending on mode bits 3..4. No direct callers (called through a pointer or tail jump).

**Notes:** Likely 'speed low and stable for N cycles' qualifier; guess. Addresses differ from later builds (0x649 vs 0x65d, dfd vs e1d).

- Addresses by version: 12b: 0x08005574, 143: 0x08005478
- Called by: `mcu_0160_08004e78`
- Confidence: medium
