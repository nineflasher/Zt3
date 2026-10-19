# MCU - `foc` functions

14 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_angle_sincos_update`](#mcu_angle_sincos_update) | 0x08006402 | Store the sine and cosine of the Q15 angle at +0x30 into the object's +0x34 and +0x38 fields |
| [`mcu_clarke_alpha_beta_step`](#mcu_clarke_alpha_beta_step) | 0x08006334 | Store the previous +0x20 sample at +0x18 and compute beta = (ia + 2*ib) / sqrt(3) in Q15 |
| [`mcu_dynamic_bound_clamp_update`](#mcu_dynamic_bound_clamp_update) | 0x08006C9C | Derive upper and lower bounds for a target from two limits, filter them and clamp the input |
| [`mcu_foc_control_tick`](#mcu_foc_control_tick) | 0x0800772C | Per-cycle FOC supervisor: filter a sample, run PID +0x15C, gate TMR1 outputs, time itself |
| [`mcu_foc_loops_enable`](#mcu_foc_loops_enable) | 0x080072FC | Enable PID blocks at +0x7C, +0xC0 and +0x15C and latch the speed-scaled limit at +0xAC |
| [`mcu_foc_pid_limits_set`](#mcu_foc_pid_limits_set) | 0x08007822 | Set the output limits of the PID blocks at +0x7C, +0xC0 and +0x15C; 1 if all accepted |
| [`mcu_gain_triple_q15_from_float`](#mcu_gain_triple_q15_from_float) | 0x080082C8 | Convert three float parameters into six Q15 controller words, using a float from +0x2C |
| [`mcu_inv_park_transform`](#mcu_inv_park_transform) | 0x080063C0 | Inverse Park transform: (d, q) to (alpha, beta) using the Q15 sin/cos at +0x34/+0x38 |
| [`mcu_math_cos_q15`](#mcu_math_cos_q15) | 0x08001B14 | Fixed-point cosine: Q15 radians in, Q15 result (sin(x+pi/2)) |
| [`mcu_math_sin_q15`](#mcu_math_sin_q15) | 0x08001C54 | Fixed-point sine: Q15 radians in, Q15 result via 513-entry table with interpolation |
| [`mcu_park_transform_deadband`](#mcu_park_transform_deadband) | 0x0800635E | Park transform of (alpha, beta) with Q15 sin/cos at +0x34/+0x38 and a dead-band on d and q |
| [`mcu_pid_enable_bumpless`](#mcu_pid_enable_bumpless) | 0x080082AC | Set a PID block's enable byte and resync its integrator on an off-to-on transition |
| [`mcu_scaled_ratio_clamp_q15`](#mcu_scaled_ratio_clamp_q15) | 0x0800702C | Scale the first argument, divide by the second register argument, clamp to +/-100.0 (Q15) |
| [`mcu_sqrt_limit_setup_float`](#mcu_sqrt_limit_setup_float) | 0x08006F74 | Store float-coded limit parameters and derive a sqrt-based Q15 limit; 0 if rejected |

## mcu_angle_sincos_update

**Store the sine and cosine of the Q15 angle at +0x30 into the object's +0x34 and +0x38 fields**

Reads the Q15 angle word at +0x30 of the object, computes its sine with mcu_math_sin_q15 and stores it at +0x34, then computes the cosine with mcu_math_cos_q15 and stores it at +0x38. It returns 1 unconditionally. The only caller in this packet is mcu_0160_08007364, and the pair is the usual input to a Park or inverse-Park transform.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object with the angle at +0x30 and the sine and cosine outputs at +0x34 and +0x38 |

**Returns** `u32`: always 1

- Addresses by version: 12b: 0x0800647A, 143: 0x08006332, 152: 0x08006362, 0160: 0x08006402
- Called by: `mcu_0160_08007364`
- Calls: `mcu_math_cos_q15`, `mcu_math_sin_q15`
- Confidence: high

## mcu_clarke_alpha_beta_step

**Store the previous +0x20 sample at +0x18 and compute beta = (ia + 2*ib) / sqrt(3) in Q15**

Copies the sample at +0x20 into +0x18, a one-sample delay of the first component. It then computes beta = (value at +0x20 + 2 * value at +0x24) * 0x49E6 / 2^15 and writes it to +0x1C. The constant 0x49E6 / 2^15 = 0.5773 is 1/sqrt(3) in Q15. This matches the Clarke transform beta term for phase currents ia = +0x20 and ib = +0x24, though the field roles are inferred from the arithmetic. Always returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object with ia (+0x20), ib (+0x24), delayed alpha (+0x18), beta (+0x1C), s32 |

**Returns** `bool`: always 1

- Addresses by version: 12b: 0x080063AC, 143: 0x08006264, 152: 0x08006294, 0160: 0x08006334
- Called by: `mcu_0160_08007364`
- Confidence: medium

## mcu_dynamic_bound_clamp_update

**Derive upper and lower bounds for a target from two limits, filter them and clamp the input**

When the enable byte at +0x3C is zero it copies the input *(+0x18) to the output and returns. Otherwise it forms a threshold from DAT_200003DE divided by 70.0 and converted to Q15, then moves the local target *(+0x08) by the step at +0x00: up when the reference at *(+0x14) is at most minus the threshold, down when it is at least the threshold, and unchanged in between. Two bound candidates are formed from the parameters times 0x39BC29 (Q15) minus the Q15 product of +0x0C and +0x10, and they are divided by the target with mcu_q15_div_sat, with the sign of the target swapping them. Below a magnitude of 0x8000 the bounds are left open (0x7FFFFFF and -0x8000000). The three bounds are then low-passed with coefficient 0xF4CB6C8 into +0x30, +0x34 and +0x38, and the output is the input clamped to [lower, upper]. The filtered upper bound is also written to DAT_2000036C.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | limiter object (see the body for offsets) |
| `param_2` | `s32` | upper reference |
| `param_3` | `s32` | lower reference |

**Notes:** The mechanism is read from the arithmetic and the offsets. The physical quantity being limited is not identified. The shape resembles a voltage-limited current or torque bound, which is a guess. Shares the DAT_200003DE/70 reference with mcu_dq_power_estimate.

- Addresses by version: 12b: 0x08006DF0, 143: 0x08006CC4, 152: 0x08006CF4, 0160: 0x08006C9C
- Called by: `mcu_0160_0800a320`
- Calls: `__ARM_scalbnf`, `__aeabi_ui2f`, `__aeabi_fdiv`, `__aeabi_f2iz`, `mcu_q15_div_sat`, `mcu_lpf_q30_step`
- Confidence: low

## mcu_foc_control_tick

**Per-cycle FOC supervisor: filter a sample, run PID +0x15C, gate TMR1 outputs, time itself**

Stores the value from mcu_0160_080031b8 (not yet described) at +0x1A0 and low-passes it into +0x1A4 with Q30 coefficient 0x05832848 (about 0.086). If the output-enable byte at +0x2E6 is zero, it clears the six channel-enable bits 0x555 of TMR1.CCTRL (mask 0xFFFFFAAA) and leaves the other bits alone, then clears the byte at +0x2E5. Otherwise, if the run byte at +0x19A is set, it sets the value at +0x168 to the word at +0x15C scaled by one third of the absolute difference of two pointed-to values (when that difference is below 0x18000, else the full word), copies +0x164 to +0x170, and calls mcu_pid_update_q15 on the block at +0x15C with zero feed-forward. Finally it stores in +0x2D8 the SysTick cycles the call took: SysTick VAL at 0xE000E018 is read at entry and exit, a fixed 10 cycles of overhead are subtracted, and the 24-bit down-counter wrap is corrected. It returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | FOC control object |

**Returns** `u32`: always 1

**Notes:** The meanings of the flags at +0x19A and +0x2E6 and of the pointers at +0x174 and +0x17C are not known. The timing word at +0x2D8 is the only self-timing output. Group with mcu_foc_loops_enable and mcu_foc_pid_limits_set.

- Addresses by version: 12b: 0x08007818, 143: 0x0800770C, 152: 0x08007784, 0160: 0x0800772C
- Peripheral registers: `TMR1.CCTRL` (RW), `SysTick+0x8` (R)
- Called by: `mcu_0160_0800a320`
- Calls: `mcu_position_multiturn_half`, `mcu_lpf_q30_step`, `mcu_pid_update_q15`
- Confidence: medium

## mcu_foc_loops_enable

**Enable PID blocks at +0x7C, +0xC0 and +0x15C and latch the speed-scaled limit at +0xAC**

Calls mcu_pid_enable_bumpless on the block at +0x7C with param_2, on the block at +0xC0 with param_3, and on the block at +0x15C with param_5. When param_2 is non-zero it also computes the limit stored at +0xAC: it multiplies the word at +0x2E0 by 0x145F (Q15), multiplies the word at +0x10 by that, and divides it by DAT_20000A44 through mcu_scaled_ratio_clamp_q15. The routine returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | control object |
| `param_2` | `s32` | enable for the block at +0x7C, also gates the limit |
| `param_3` | `u32` | enable for the block at +0xC0 |
| `param_4` | `u32` | unused in the decompile |
| `param_5` | `u32` | enable for the block at +0x15C |

**Returns** `u32`: always 1

**Notes:** Group with mcu_foc_pid_limits_set and mcu_foc_control_tick, which act on the same three blocks.

- Addresses by version: 12b: 0x08007410, 143: 0x08007304, 152: 0x08007354, 0160: 0x080072FC
- Called by: `mcu_0160_08007700`, `mcu_0160_080077e0`
- Calls: `mcu_scaled_ratio_clamp_q15`, `mcu_pid_enable_bumpless`
- Confidence: medium

## mcu_foc_pid_limits_set

**Set the output limits of the PID blocks at +0x7C, +0xC0 and +0x15C; 1 if all accepted**

Calls mcu_pid_set_limits on the block at +0x7C with the word at +0x2A4 as the minimum argument and the word at +0x2A0 as the maximum, on the block at +0xC0 with +0x2AC and +0x2A8, and on the block at +0x15C with +0x2B4 and +0x2B0, in the argument order the decompile shows. The three results are ANDed, so the return value is 1 only when every block accepts its limits, which means each minimum is below its maximum.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | control object |

**Returns** `bool`: 1 if all three limit pairs were accepted

**Notes:** The minimum and maximum words are taken as the decompile passes them, so the +0x2A4 and +0x2A0 order should be confirmed against the caller.

- Addresses by version: 12b: 0x08007906, 143: 0x080077FA, 152: 0x0800787A, 0160: 0x08007822
- Called by: `mcu_0160_080078f0`, `mcu_0160_0800a320`
- Calls: `mcu_pid_set_limits`
- Confidence: high

## mcu_gain_triple_q15_from_float

**Convert three float parameters into six Q15 controller words, using a float from +0x2C**

If each of the three float arguments has bits below 0x80800000 (non-negative values and -0.0), it passes the float at +0x2C of the object through mcu_0160_080013e4 (not yet described) to get u, then stores the Q15 value of param_2 at +0x00 and +0x0C, the Q15 value of param_3 divided by u at +0x04 and +0x10, and the Q15 value of param_4 times u at +0x08 and +0x14. It returns 1 when stored and 0 when any argument is rejected.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | controller object |
| `param_2` | `u32` | IEEE-754 single bits |
| `param_3` | `u32` | IEEE-754 single bits |
| `param_4` | `u32` | IEEE-754 single bits |

**Returns** `bool`: 1 if stored, 0 if any input was rejected

**Notes:** The pairs at +0x00 and +0x0C, +0x04 and +0x10, +0x08 and +0x14 are written identically, so the duplicates may be a current copy and an active copy. Callers: mcu_0160_08004DB8 and mcu_0160_08008204.

- Addresses by version: 12b: 0x080081B8, 143: 0x080081C0, 152: 0x080082B0, 0160: 0x080082C8
- Called by: `mcu_0160_08004db8`, `mcu_0160_08008204`
- Calls: `__aeabi_fmul`, `__ARM_scalbnf`, `mcu_i2f_lzc`, `__aeabi_fdiv`, `__aeabi_f2iz`
- Confidence: low

## mcu_inv_park_transform

**Inverse Park transform: (d, q) to (alpha, beta) using the Q15 sin/cos at +0x34/+0x38**

Reads d from word 0 and q from word 1 of the int block, and sin from word 13 (+0x34) and cos from word 14 (+0x38), all Q15. Writes alpha = d*cos - q*sin to word 2 (+0x08) and beta = q*cos + d*sin to word 3 (+0x0C), each product shifted right by 15 after a 64-bit multiply. This is the inverse of mcu_park_transform_deadband. Called from mcu_0160_08007364. Always returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | int block: d, q in; alpha, beta out; sin at +0x34, cos at +0x38 |

**Returns** `bool`: always 1

- Addresses by version: 12b: 0x08006438, 143: 0x080062F0, 152: 0x08006320, 0160: 0x080063C0
- Called by: `mcu_0160_08007364`
- Confidence: high

## mcu_math_cos_q15

**Fixed-point cosine: Q15 radians in, Q15 result (sin(x+pi/2))**

Same algorithm as mcu_0160_08001c54 (sine), but 0x40000000 (pi/2 in the Q31-of-pi phase) is added to the phase first, so it returns cos(x). The input angle is multiplied by 0x517cc1b7 (1/pi in Q32) to get a phase where 2^31 = pi, quadrant-folded, then the top 10 bits index a 513-entry sine table at 0x0800ec20 (step pi/1024) and a second-order interpolation sin(a+d) ~ sin(a) + d*(cos(a) - d*sin(a)/2) is applied using table[i] and table[512-i]. The result is negated for the lower half-plane and rounded to Q15 (+/-32768 = +/-1.0). Only caller: mcu_0160_08006402, probably the Park/inverse-Park transform.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | angle in Q15 radians (pi = 102944) |

**Returns** `s32`: cos in Q15

**Notes:** Input/output Q-format inferred from the 1/pi constant and final >>16; table contents not dumped here.

- Addresses by version: 12b: 0x08001AF8, 143: 0x08001AF8, 152: 0x08001AF8, 0160: 0x08001B14
- Called by: `mcu_angle_sincos_update`
- Confidence: medium

## mcu_math_sin_q15

**Fixed-point sine: Q15 radians in, Q15 result via 513-entry table with interpolation**

Multiplies the input by 0x517cc1b7 (1/pi, Q32) and keeps bits 16..47 to get a phase where 2^31 = pi. Bit 30 folds the second quadrant (0x80000000 - phase), bit 31 selects the sign. The top 10 bits of the 31-bit magnitude index the table at 0x0800ec20 (sin(i*pi/1024)); with the fractional angle d = low bits * pi/1024 it evaluates sin(a) + d*(cos(a) - d*sin(a)/2) using table[i] and table[512-i], negates for the sign and rounds to Q15. When the table index is 0 it uses sin(x)~x: (x<<1)*0xc90fcd37 >> 47. Single caller mcu_0160_08006402; companion of mcu_0160_08001b14 (cos).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | angle in Q15 radians (pi = 102944) |

**Returns** `s32`: sin in Q15 (+/-32768 = +/-1.0)

**Notes:** Input scale deduced from the 1/pi constant: the angle may be a Q15 radian value; the table is not decoded here.

- Addresses by version: 12b: 0x08001C38, 143: 0x08001C38, 152: 0x08001C38, 0160: 0x08001C54
- Called by: `mcu_angle_sincos_update`
- Confidence: medium

## mcu_park_transform_deadband

**Park transform of (alpha, beta) with Q15 sin/cos at +0x34/+0x38 and a dead-band on d and q**

Reads alpha at +0x18, beta at +0x1C, sin at +0x34 and cos at +0x38, all Q15. Computes d = alpha*cos + beta*sin into +0x10 and q = beta*cos - alpha*sin into +0x14, each product taken as a 64-bit value shifted right by 15. Any component whose absolute value is below the threshold param_2 is then forced to zero, which suppresses small values near zero. Called from mcu_0160_08007364.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object: alpha, beta, sin, cos in, d, q out |
| `param_2` | `s32` | dead-band threshold, same units as d and q |

**Returns** `bool`: always 1

**Notes:** Park sign convention is the standard one; the field names are inferred.

- Addresses by version: 12b: 0x080063D6, 143: 0x0800628E, 152: 0x080062BE, 0160: 0x0800635E
- Called by: `mcu_0160_08007364`
- Confidence: high

## mcu_pid_enable_bumpless

**Set a PID block's enable byte and resync its integrator on an off-to-on transition**

Takes the controller object as param_1 and the enable flag as param_2. If the flag is non-zero and the enable byte at +0x3E was zero, it calls mcu_pid_sync_integrator first, so the integrator starts from the current output and the derivative does not see a step. It then stores the flag at +0x3E. Used by mcu_foc_loops_enable for each of the three blocks.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | PID controller object |
| `param_2` | `u32` | enable flag |

- Addresses by version: 12b: 0x0800819C, 143: 0x080081A4, 152: 0x08008294, 0160: 0x080082AC
- Called by: `mcu_0160_08003784`, `mcu_foc_loops_enable`
- Calls: `mcu_pid_sync_integrator`
- Confidence: high

## mcu_scaled_ratio_clamp_q15

**Scale the first argument, divide by the second register argument, clamp to +/-100.0 (Q15)**

Multiplies param_1 by 0x569A40 and shifts the 64-bit product right by 15, then divides it with mcu_q15_div_sat by the value passed in the second argument register, which the decompile does not show. The caller mcu_0160_080072FC passes DAT_20000A44 there. The quotient is clamped to [-0x320000, +0x320000], which is plus or minus 100.0 in Q15.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | value to scale; the divisor is the second argument register |

**Returns** `s32`: clamped Q15 ratio in [-0x320000, 0x320000]

- Addresses by version: 12b: 0x08007180, 143: 0x08007054, 152: 0x08007084, 0160: 0x0800702C
- Called by: `mcu_foc_loops_enable`
- Calls: `mcu_q15_div_sat`
- Confidence: medium

## mcu_sqrt_limit_setup_float

**Store float-coded limit parameters and derive a sqrt-based Q15 limit; 0 if rejected**

Rejects the call (returns 0) when either float argument is zero or subnormal, or when any of param_2 to param_8 is zero. On success it stores the raw words of param_2 through param_10 in the object, with param_9 at +0x1C and param_10 at +0x20. It then computes the Q15 integer of param_9 (stored at +0x28), the Q15 integer of 16000 times param_10, and a square root of their Q15 product with mcu_math_sqrt_fixed. It stores at +0x2C the value 1.414 times the root (0xB4FD in Q15) minus the Q15 integer of param_9, and returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object |
| `param_2` | `u32` | raw parameter 1, stored at +0x00, must be non-zero |
| `param_3` | `u32` | raw parameter 2, stored at +0x04, must be non-zero |
| `param_4` | `u32` | raw parameter 3, stored at +0x08, must be non-zero |
| `param_5` | `u32` | raw parameter 4, stored at +0x0C, must be non-zero |
| `param_6` | `u32` | raw parameter 5, stored at +0x10, must be non-zero |
| `param_7` | `u32` | raw parameter 6, stored at +0x14, must be non-zero |
| `param_8` | `u32` | raw parameter 7, stored at +0x18, must be non-zero |
| `param_9` | `u32` | IEEE-754 single bits, stored at +0x1C |
| `param_10` | `u32` | IEEE-754 single bits, stored at +0x20 |

**Returns** `bool`: 1 if stored and derived, 0 if rejected

**Notes:** The physical meaning of the limit is not identified. The caller is mcu_0160_080078F0.

- Addresses by version: 12b: 0x080070C8, 143: 0x08006F9C, 152: 0x08006FCC, 0160: 0x08006F74
- Called by: `mcu_0160_080078f0`
- Calls: `__aeabi_fmul`, `__ARM_scalbnf`, `__aeabi_f2iz`, `mcu_math_sqrt_fixed`
- Confidence: low
