# MCU - `motor` functions

75 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_12b_ctrl_block_init`](#mcu_12b_ctrl_block_init) | (removed) | 12b-build control block init: defaults, a parameter block and two compact band blocks |
| [`mcu_12b_position_observer_update`](#mcu_12b_position_observer_update) | (removed) | 12b-build position observer update: cascade observer step, then Q30 low-pass, store input |
| [`mcu_12b_ramp_limit_update`](#mcu_12b_ramp_limit_update) | (removed) | 12b-build ramp limiter: halve on enable, decay to 0.6 on disable, slew toward the target |
| [`mcu_12b_speed_band_update`](#mcu_12b_speed_band_update) | (removed) | 12b-build speed band update: recompute filter coefficients when out of band, then rate-limited update |
| [`mcu_12b_speed_lpf_band_update`](#mcu_12b_speed_lpf_band_update) | (removed) | 12b-build speed-adaptive band update, the counterpart of the 0160 band function |
| [`mcu_b90_low_and_enabled`](#mcu_b90_low_and_enabled) | 0x080039E0 | Return 1 when enable byte F54 is set and the value at B90 is below 0x666 |
| [`mcu_band_block_arm_setpoint`](#mcu_band_block_arm_setpoint) | 0x0800725C | Arm a compact band block: set the byte at +0x1C to 1 and store two values at +0x08 and +0x18 |
| [`mcu_band_block_init`](#mcu_band_block_init) | 0x08007198 | Initialise a band block: bounds, half-span \|p4-p5\|/2 and mode bytes +0x20..+0x22 |
| [`mcu_band_block_init_compact`](#mcu_band_block_init_compact) | 0x080071DE | Initialise a compact band block: bounds, half-span \|p4-p5\|/2 and mode bytes at +0x1C..+0x1E |
| [`mcu_below_10pct_of_window`](#mcu_below_10pct_of_window) | 0x08003638 | Return 1 if a Q15-scaled value lies in the lowest 10% of the window [DAT_20000bee, DAT_20000bec] |
| [`mcu_cascade_observer_step`](#mcu_cascade_observer_step) | 0x08001E5A | Three-stage cascaded observer step: Q30 low-pass plus two gain-K integrator stages |
| [`mcu_cmd_ramp_update`](#mcu_cmd_ramp_update) | 0x0800ADF0 | Per-tick command conditioning: scale the VCU command words to Q15 and slew-limit them |
| [`mcu_ctrl_block_init_default`](#mcu_ctrl_block_init_default) | 0x080029AC | Initialises a control block: parameter blocks, a compact band block and its setpoint |
| [`mcu_ctrl_block_reset_flags`](#mcu_ctrl_block_reset_flags) | 0x08006C86 | Reset a control block: clear three state words, set the byte at +0x29 to 1, clear +0x28 |
| [`mcu_ctrl_ramp_limit_update`](#mcu_ctrl_ramp_limit_update) | 0x08002A64 | Ramp limiter with rising and falling edge handling for a control output |
| [`mcu_dq_power_estimate`](#mcu_dq_power_estimate) | 0x0800767C | Step the value at +0x18 toward a limit, then return 1.5 times a two-term Q15 product sum |
| [`mcu_drive_state_set`](#mcu_drive_state_set) | 0x08005978 | Store drive state DAT_20000F44 and set the transition flag DAT_20000E37 |
| [`mcu_drive_state_update`](#mcu_drive_state_update) | 0x080052BC | Enter or leave active drive mode DAT_20000E33 from speed, faults and counters |
| [`mcu_edge_pos_track`](#mcu_edge_pos_track) | 0x08003434 | Track the edge-counted position estimate and retarget the ramp in drive-active mode |
| [`mcu_fb_lpf_select_update`](#mcu_fb_lpf_select_update) | 0x08005090 | Low-pass the feedback with a Q30 coefficient chosen from the drive state |
| [`mcu_get_limit_min3_or_unbounded`](#mcu_get_limit_min3_or_unbounded) | 0x08004AC4 | Return DAT_20000660 clamped to >= 0x18000, or 0x7fff8000 if it is zero |
| [`mcu_limit_668_or_default`](#mcu_limit_668_or_default) | 0x080047D0 | Return the RAM limit DAT_20000668 when enabled, else 0.5 (0x4000) |
| [`mcu_limit_block_arm_setpoint`](#mcu_limit_block_arm_setpoint) | 0x0800724E | Arm a limit block: set the enable byte at +0x20 to 1 and store two values at +0x08 and +0x1C |
| [`mcu_limit_block_bind_io`](#mcu_limit_block_bind_io) | 0x08006F44 | Bind gains and the reference and output pointers into a limit block and set all mode bytes to 1 |
| [`mcu_limit_block_init_params`](#mcu_limit_block_init_params) | 0x08006DE8 | Store seven configuration words and a flag into a limit block; set the Q15 word at +0x20 to 1.0 |
| [`mcu_limit_block_update`](#mcu_limit_block_update) | 0x08006E18 | Per-cycle limit update: bounds X and Y from two Q15 gains, output selected by mode bytes |
| [`mcu_limit_chan_cfg_a`](#mcu_limit_chan_cfg_a) | (removed) | Load limit channel A from RAM block 0x224 and reset edge counter D58 |
| [`mcu_limit_chan_cfg_b`](#mcu_limit_chan_cfg_b) | (removed) | Load limit channel B from RAM block 0x240 and reset edge counter D58 |
| [`mcu_limit_chan_cfg_d`](#mcu_limit_chan_cfg_d) | 0x08003A0C | Load limit channel D with \|DAT_20000780\|/4 capped at 10.0 and gain 0.8 |
| [`mcu_limit_chan_cfg_high_seed`](#mcu_limit_chan_cfg_high_seed) | 0x08003CC8 | Seed limit channel from block 0xB3C, set mode 1, and force edge counter D78 high |
| [`mcu_limit_chan_init_mode6`](#mcu_limit_chan_init_mode6) | 0x08003608 | Set limit channel to mode 6 and enabled, clear +0x0C, reset edge counter D78 |
| [`mcu_limit_chan_update_c`](#mcu_limit_chan_update_c) | 0x08003664 | Update limit channel C: decay its limit on a hold counter and reload gain constants |
| [`mcu_limit_ratio_with_floor`](#mcu_limit_ratio_with_floor) | 0x0800CE3C | Map two values against a limit to a Q15 ratio with a 10 percent floor, saturating at full scale |
| [`mcu_limit_target_b3c_update`](#mcu_limit_target_b3c_update) | 0x080055C4 | Compute the limited target DAT_20000B3C from the B14 band and base DAT_200003DE |
| [`mcu_limiter_set_range`](#mcu_limiter_set_range) | 0x08004D3C | Store the larger of two bounds at cfg+0x25C and retarget limiter object C0 |
| [`mcu_main_ctx_flag4_clear`](#mcu_main_ctx_flag4_clear) | 0x08003130 | Returns true when the flag byte at +0x04 of the main context object is clear |
| [`mcu_motor_calib_apply`](#mcu_motor_calib_apply) | 0x0800A4E8 | Pass the stored calibration words to the controller block setup when the record is valid |
| [`mcu_mul_q15_f5e_by_3f2`](#mcu_mul_q15_f5e_by_3f2) | 0x08002208 | Q15 multiply of RAM value 0x20000f5e (shifted to Q15) by 0x200003f2, result >> 15 |
| [`mcu_neg_limit_flag_update`](#mcu_neg_limit_flag_update) | 0x08005424 | Update flag DAT_20000E35 from the cfg+0x28 value and DAT_20000F2C |
| [`mcu_param_block3_init_checked`](#mcu_param_block3_init_checked) | 0x08001E18 | Validate and fill a 3-word parameter block, setting a valid flag at +0x2c |
| [`mcu_param_block4_init_checked`](#mcu_param_block4_init_checked) | (removed) | Fill a 4-word parameter block if the first two values are positive |
| [`mcu_param_block8_init_checked`](#mcu_param_block8_init_checked) | 0x08002A34 | Fill an 8-word parameter block if the first and third values are positive |
| [`mcu_param_record_load`](#mcu_param_record_load) | 0x0800A0F8 | Decode the stored motor parameter record into the runtime block, rejecting blank or erased records |
| [`mcu_pi_update_gain_sched`](#mcu_pi_update_gain_sched) | 0x0800833C | PI step with speed-scheduled gains (Kp doubled, Ki halved below 0xF0001) and one-sided anti-windup |
| [`mcu_pid_set_limits`](#mcu_pid_set_limits) | 0x08008282 | Store PID output limits (min < max) and clamp the live output when the loop is enabled |
| [`mcu_pid_sync_integrator`](#mcu_pid_sync_integrator) | 0x08008260 | Reset PID integrator to the clamped current output and latch the current measurement |
| [`mcu_pid_update_q15`](#mcu_pid_update_q15) | 0x08008128 | PID-style controller step in Q15 with derivative on measurement and clamped output |
| [`mcu_position_multiturn_compute`](#mcu_position_multiturn_compute) | 0x08009050 | Compute relative position = raw + wraps x 0x6487E - reference, saturated to +-0x7FBC0000 |
| [`mcu_position_multiturn_half`](#mcu_position_multiturn_half) | 0x080031B8 | Returns the half-scale multi-turn position of the main context object |
| [`mcu_position_observer_update`](#mcu_position_observer_update) | 0x08002E9C | Per-sample position observer update: cascade observer step, then Q30 low-pass of the estimate |
| [`mcu_position_outlier_reject`](#mcu_position_outlier_reject) | 0x0800314C | Accepts a new half-scale position sample unless it jumps more than 0x15E0000 from the last one |
| [`mcu_position_rebase`](#mcu_position_rebase) | 0x08009044 | Set the multi-turn reference to the current raw counter and clear the wrap count |
| [`mcu_position_zero_and_latch`](#mcu_position_zero_and_latch) | 0x08004D94 | Rebase the multi-turn position at the context object and latch the new reference |
| [`mcu_q15_to_percent_s16`](#mcu_q15_to_percent_s16) | 0x080047B4 | Convert the Q15 value at 0x20000a50 to a percentage (x * 100 / 32768) as s16 |
| [`mcu_ramp_asym_track`](#mcu_ramp_asym_track) | 0x0800337C | Ramp DAT_20000BE0 toward its target: distance-scaled steps down, fixed 0x20 up |
| [`mcu_ramp_toward_target_s32`](#mcu_ramp_toward_target_s32) | 0x08002982 | Move *value toward target by at most \|step\| (slew-rate limiter) |
| [`mcu_ratio_gain_clamped_q15`](#mcu_ratio_gain_clamped_q15) | 0x08005D3C | Compute a Q15 gain clamped to 0.8..1.3 when both inputs reach the 0x18000 gate, else unity |
| [`mcu_run_enable_update`](#mcu_run_enable_update) | 0x080056E4 | Set or clear run-enable DAT_20000E34 from hall input bit 2, speed and B20 |
| [`mcu_sample_history3_rise_detect`](#mcu_sample_history3_rise_detect) | 0x0800D9C4 | Push a 0..200 sample into a 3-deep history and flag three consecutive large rises |
| [`mcu_scale_delta_q15`](#mcu_scale_delta_q15) | 0x08002078 | Return (DAT_20000f5a - DAT_2000027e) * 0xdbf using Q15 fixed-point arithmetic |
| [`mcu_sensor_filter_tick_v12b`](#mcu_sensor_filter_tick_v12b) | (removed) | 12b periodic tick: sample two inputs, run seven Q30 low-pass stages and mirror two status bits |
| [`mcu_setpoint_slew_limit_std`](#mcu_setpoint_slew_limit_std) | 0x08007F24 | Slew-limit the scaled setpoint into filter DAT_20000F46 and derive output limit DAT_20000F48 |
| [`mcu_setpoint_slew_limit_v12b`](#mcu_setpoint_slew_limit_v12b) | (removed) | Slew-limit the scaled setpoint into filter DAT_20000F02 and derive output limit DAT_20000F04 (12b) |
| [`mcu_speed_estimate_update`](#mcu_speed_estimate_update) | 0x080031CC | Turn the encoder count accumulator into a filtered Q15 speed estimate |
| [`mcu_speed_from_max_u12`](#mcu_speed_from_max_u12) | 0x08002148 | Speed estimate from the maximum of 20 samples of a 12-bit channel, with a status code |
| [`mcu_speed_from_period_min`](#mcu_speed_from_period_min) | 0x0800209C | Speed estimate from the minimum of 20 captured periods, table lookup, status code |
| [`mcu_speed_limit_calc`](#mcu_speed_limit_calc) | 0x0800576C | Compute limit outputs F38, F3C and F40 from a speed-like input and the mcu limit |
| [`mcu_speed_lpf_band_update`](#mcu_speed_lpf_band_update) | 0x08002B64 | Speed-adaptive band update: recomputes Q30 filter alphas, sets band flags and accumulators |
| [`mcu_speed_range_setup_core`](#mcu_speed_range_setup_core) | 0x08007C08 | Validate and store a speed range, derive a 1/p7 count and a 0.01*(max^2-min^2)*p5 term |
| [`mcu_speed_range_setup_wrap`](#mcu_speed_range_setup_wrap) | 0x08007BD4 | Call the speed-range setup core, store a flag byte at +0x36 and return the accept byte |
| [`mcu_sq_scale_block_init`](#mcu_sq_scale_block_init) | 0x0800641A | Initialise a block with (n*n/64) in Q15 for 0 <= n <= 2000 and set its valid byte |
| [`mcu_target_derate_calc`](#mcu_target_derate_calc) | 0x0800480C | Compute the Q15 drive target from the B14 band, base DAT_200003DC and a derate term |
| [`mcu_update_flag_e32_from_mode_3`](#mcu_update_flag_e32_from_mode_3) | 0x080056C4 | Set DAT_20000e32 to 1 when mode byte 0x2000065a equals 3, else 0 |
| [`mcu_update_motion_direction_flags`](#mcu_update_motion_direction_flags) | 0x08005550 | Set one of two flags (0x20000e1d / 0x20000e1e) from mode bits 3..4 when \|value\| and counter qualify |
| [`mcu_update_motion_flag_old`](#mcu_update_motion_flag_old) | (removed) | Set flag 0x20000dfd when a counter >= 20, \|value\| <= 0x50000 and mode bit2 is set (12b/143) |

## mcu_12b_ctrl_block_init

**12b-build control block init: defaults, a parameter block and two compact band blocks**

The 12b-build counterpart of mcu_ctrl_block_init_default. It writes the defaults 1000, 0x11859820, 0x12F1E16 and 0 into the words at +0x10..+0x1C, sets the byte at +0x3C to 1 and calls mcu_param_block4_init_checked with the four parameters. It then initialises two compact band blocks, at +0x40 and +0x60, each with bound 0x1F30A6E and half-span from the words at +0xC4. After each band init it overwrites the words at +0x48 and +0x58 with 0x2533914 and 0x3C2B6380 in swapped order and sets the byte at +0x5C to 1. Returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | control block base |
| `param_2` | `u32` | forwarded to mcu_param_block4_init_checked |
| `param_3` | `u32` | forwarded |
| `param_4` | `u32` | forwarded |
| `param_5` | `u32` | forwarded |

**Returns** `u32`: always 1

**Notes:** The overwrites of +0x48 and +0x58 land inside the first band block, so the first block's setpoints are the swapped pair. This follows the code exactly, but the intent is not clear.

- Addresses by version: 12b: 0x08002B70
- Called by: `mcu_0160_08003784`
- Calls: `mcu_band_block_init_compact`, `mcu_param_block4_init_checked`
- Confidence: medium

## mcu_12b_position_observer_update

**12b-build position observer update: cascade observer step, then Q30 low-pass, store input**

The 12b build of mcu_position_observer_update, with the same steps at 12b offsets: mcu_cascade_observer_step on the block at +0x10, mcu_lpf_q30_step_alt on the state at +0x30 with the input word at +0xC0 and coefficient 0x03C89460 (about 0.059 in Q30), and the raw input stored at +0xC4. Returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | observer object (observer block at +0x10, filter state at +0x30, input word at +0xC0, last input at +0xC4) |
| `param_2` | `s32` | raw sample for this period |

**Returns** `u32`: always 1

**Notes:** Same algorithm as mcu_position_observer_update, at the 12b layout. The packet's callee name for the observer step is mcu_0160_08001e5a, so this build calls the 0160 routine by the same behaviour.

- Addresses by version: 12b: 0x08003010
- Called by: `mcu_0160_0800a320`
- Calls: `mcu_cascade_observer_step`, `mcu_lpf_q30_step_alt`
- Confidence: medium

## mcu_12b_ramp_limit_update

**12b-build ramp limiter: halve on enable, decay to 0.6 on disable, slew toward the target**

Ramp limiter for the 12b build. Byte +0x9C is the current enable and +0x9D the previous one. On a rising edge the accumulator at +0x80 is halved, and on a falling edge it is multiplied by 0x9999/32768 (about 0.6). While disabled, the accumulator slews toward param_2 by a step of 0x8000 / rate (Q15 reciprocal), with rate from +0x8C clamped to 0xCCC..0x10000 and forced to 0xCCC when +0x0C <= rate, and it snaps to the target when within one step. When param_4 is nonzero *param_3 is min-clamped to the output, which is the accumulator while disabled and 0 while enabled. Returns 1 only when param_4 is set and the block is enabled.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ramp block (enable bytes at +0x9C/+0x9D, accumulator at +0x80, rate and limit words) |
| `param_2` | `s32` | target value |
| `param_3` | `ptr` | output word, min-clamped when param_4 is set |
| `param_4` | `s32` | clamp enable (nonzero) |

**Returns** `u32`: 1 when clamp enabled and block enabled, else 0

**Notes:** This is the 12b analogue of mcu_ctrl_ramp_limit_update, without the edge-initialisation from a gain. The output-clamp-to-0 on the enabled path matches the 0160 version.

- Addresses by version: 12b: 0x08002C3E
- Called by: `mcu_0160_08003f2c`
- Calls: `mcu_q15_div_sat`
- Confidence: medium

## mcu_12b_speed_band_update

**12b-build speed band update: recompute filter coefficients when out of band, then rate-limited update**

The 12b-only counterpart of the band update in mcu_0160_08002b64 (smaller). It tests the difference p[0x29] - p[0x31] against p[1] and the sign of p[0x31] and p[0x29]. When out of band it recomputes an alpha pair with the same constants (2*pi, 0.005, 1.0 as IEEE-754 bit patterns), scales by 2^30 and converts, stores the result at p[0x1E] and sets the byte at +0x7C, and writes 0x37366F40 to p[0x1A]; when in band it stores 0x1F30A6E in p[0x1E]. It then copies 0xB8 bytes of the block to a stack buffer, calls mcu_12b_select_stack_local_fragment and updates p[0x29] and the flag byte at +0x7C according to range checks.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | int word block (speed, band and flag fields) |

**Returns** `u32`: always 1

**Notes:** Only the structure and the constants are certain. The field meanings are inferred from the matching 0160 function, and the range checks are not fully decoded.

- Addresses by version: 12b: 0x08002A3C
- Called by: `mcu_12b_08002c26`
- Calls: `__aeabi_memcpy`, `__aeabi_fadd`, `__aeabi_fmul`, `__ARM_scalbnf`, `__aeabi_fdiv`, `__aeabi_f2iz`, `__aeabi_i2f`, `mcu_lpf_asym_update`, `mcu_12b_select_stack_local_fragment`
- Confidence: low

## mcu_12b_speed_lpf_band_update

**12b-build speed-adaptive band update, the counterpart of the 0160 band function**

The 12b counterpart of mcu_0160_08002b64, with the same overall flow. It checks p[0x21] (the speed-like value at +0x84) against p[0x31] and the band limits, and when out of band it recomputes two Q30 alpha coefficients from the 2*pi*0.005 constants (scalbnf by 30, then a float to int conversion) and writes them into p[0x12] and p[0x16] with the flag byte at +0x5C. A Q15 accumulator is then driven from the sign-band tests on p[0x25] against -0x4FFFF and p[0x24] against 0xC8000, and a global flag DAT_20000720 is set from them. Accumulators p[0x23..0x26] and the filtered value p[0x22] are updated from the magnitude of param_2, as in the 0160 build.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | int word block of the speed/band object |
| `param_2` | `s32` | signed speed-like input |

**Returns** `u32`: always 1

**Notes:** Structure matches mcu_0160_08002b64 but the field offsets and the flag (DAT_20000720 rather than DAT_20000734) differ. Read the details from the disassembly before relying on them. Caller mcu_12b_08002c26 is outside this batch.

- Addresses by version: 12b: 0x08002D0C
- Called by: `mcu_12b_08002c26`
- Calls: `__aeabi_memcpy`, `__aeabi_fadd`, `__aeabi_fmul`, `__ARM_scalbnf`, `__aeabi_fdiv`, `__aeabi_f2iz`, `mcu_q15_div_sat`, `mcu_q15_mul_sat`, `__aeabi_i2f`, `mcu_lpf_asym_update`, `mcu_12b_select_stack_local_fragment`
- Confidence: low

## mcu_b90_low_and_enabled

**Return 1 when enable byte F54 is set and the value at B90 is below 0x666**

Returns 1 only when DAT_20000F54 is non-zero and the scaled field of the object at 0x20000B90 is below 0x666 (1638, about 0.05 in Q15). The field value comes from the thunk at 0x0800A56C (decompiled as thunk_FUN_0800a588), which tail-calls mcu_get_field_0x0c_ashr_scale: the s32 at +0x0C shifted right by the signed byte at +0x32. The callers listed in the packet are mcu_0160_08003ab8, mcu_0160_08003f2c, mcu_0160_0800517c, mcu_0160_08005930 and mcu_143_080052ac, none of which is in this packet. Reading it as a near-zero test on the B90 quantity is a guess from the threshold.

**Returns** `bool`: 1 when enabled and the value is below 0x666, else 0

**Notes:** The thunk relation between 0x0800A56C and 0x0800A588 is inferred from the decompiled call name and the caller list of mcu_get_field_0x0c_ashr_scale, which includes mcu_0160_0800a56c. mcu_0160_0800a56c itself is listed as not yet described.

- Addresses by version: 12b: 0x08003954, 143: 0x080038E4, 152: 0x08003940, 0160: 0x080039E0
- Called by: `mcu_0160_08003ab8`, `mcu_0160_08003f2c`, `mcu_0160_0800517c`, `mcu_0160_08005930`
- Calls: `mcu_get_field_0x0c_ashr_scale_thunk1`
- Confidence: medium

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
- Called by: `mcu_ctrl_block_init_default`, `mcu_speed_lpf_band_update`
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
- Called by: `mcu_ctrl_block_init_default`
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
- Called by: `mcu_fb_lpf_select_update`, `mcu_digital_input_debounce`
- Confidence: medium

## mcu_cascade_observer_step

**Three-stage cascaded observer step: Q30 low-pass plus two gain-K integrator stages**

Advances a three-stage observer kept in a block of words (byte offsets used here). +0x00 is the integer gain K, +0x04, +0x08 and +0x0C are Q30 coefficients a1, a2 and a3, +0x10 holds the input x, +0x18 is the state s0, +0x20 and +0x28 are the states of stages 2 and 3, and the byte at +0x2C enables the observer. When enabled, stage 1 is a Q30 one-pole low-pass v1 = s0 + a1*(x - s0). Stage 2 is w = s2 + a2*K*(x - s0), stage 3 is y = s3 + a3*2*K*K16*(x - s0) (K16 is the low half of K), and the returned estimate is s0 = v1 + w/K + (y/K^2)/2, with the states updated to w + y/K and y. When disabled it just stores x and returns it.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | observer block (K, coefficients, input, states, enable byte at +0x2C) |
| `param_2` | `s32` | new input sample x |

**Returns** `s32`: fused estimate (state s0), or x when disabled

**Notes:** The decompile indexes the block with ushort offsets, and the byte offsets above come from that indexing. What the observer tracks (speed, angle or position) is not settled by this function alone. Caller mcu_0160_08002e9c adds a Q30 low-pass at +0x40.

- Addresses by version: 12b: 0x08001E84, 143: 0x08001EBA, 152: 0x08001E3E, 0160: 0x08001E5A
- Called by: `mcu_position_observer_update`
- Calls: `mcu_q15_mul_sat`, `mcu_q30_mul`
- Confidence: low

## mcu_cmd_ramp_update

**Per-tick command conditioning: scale the VCU command words to Q15 and slew-limit them**

Per-tick conditioning of the drive command words. When the byte at 0x20001FCE is non-zero (mcu_flag_1fce_is_clear returns 0) the ramp integrators at 0x20000664 and 0x200001F8 are cleared. Otherwise the command words at 0x20001FD6, 0x20001FD8 and 0x20001FDA are converted to Q15 (shifted left 15) and moved toward their targets with mcu_ramp_toward_target_s32, at most 0x333 per tick for the first and 0xCCC per tick for the second. A third value at 0x200001FC is slewed toward 0x20000684, or toward 0x20000174 when 0x20000E33 is set. The outputs 0x20000668, 0x20000204 and 0x20000214 are published and the flag at 0x2000066D is set on every active pass. Rises at 0x20000214 are rate-limited and falls are immediate.

**Notes:** The command words are the decoded frame fields at 0x20001FD0 to 0x20001FE8; their origin in the VCU frame is inferred, not shown here.

- Addresses by version: 12b: 0x0800AC98, 143: 0x0800AEC0, 152: 0x0800AD7C, 0160: 0x0800ADF0
- Called by: `mcu_0160_0800adde`
- Calls: `mcu_ramp_toward_target_s32`, `mcu_flag_1fce_is_clear`
- Confidence: medium

## mcu_ctrl_block_init_default

**Initialises a control block: parameter blocks, a compact band block and its setpoint**

Initialises a motor control block whose base is param_1 and returns 1. It calls mcu_param_block3_init_checked on the sub-block at +0x20 with the constants 1000, 0x11859820 and 0x12F1E16, passes its other arguments through to mcu_param_block8_init_checked for the whole block, initialises a compact band block at +0x50 with bound 0x1F30A6E, half-span from the words at +0xDC, mode 1 (mcu_band_block_init_compact), and then arms it with 0x2533914 and 0x3C2B6380 (mcu_band_block_arm_setpoint). The raw constants are fixed-point or IEEE-754 words; their units are not confirmed.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | control block base |
| `param_2` | `u32` | forwarded to the 8-word parameter block initialiser |
| `param_3` | `u32` | forwarded |
| `param_4` | `u32` | forwarded |
| `param_5` | `u32` | forwarded |
| `param_6` | `u32` | forwarded |
| `param_7` | `u32` | forwarded |
| `param_8` | `u32` | forwarded |
| `param_9` | `u32` | forwarded |

**Returns** `u32`: always 1

**Notes:** This build (MCU 143, 152, 0160) only. The 12b counterpart is mcu_12b_ctrl_block_init.

- Addresses by version: 143: 0x08002A0C, 152: 0x08002990, 0160: 0x080029AC
- Called by: `mcu_0160_08003784`, `mcu_motor_calib_apply`
- Calls: `mcu_param_block3_init_checked`, `mcu_param_block8_init_checked`, `mcu_band_block_init_compact`, `mcu_band_block_arm_setpoint`
- Confidence: medium

## mcu_ctrl_block_reset_flags

**Reset a control block: clear three state words, set the byte at +0x29 to 1, clear +0x28**

Clears the words at +0x18, +0x20 and +0x24 (state accumulators or last-sample registers), clears the byte at +0x28 and sets the byte at +0x29 to 1, then returns 1. This is the reset routine of a controller block whose state occupies +0x18..+0x2C. The byte at +0x29 is probably an enable or armed flag, which is inferred. Called from mcu_0160_08006b70.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | control block, at least 0x2A bytes |

**Returns** `bool`: always 1

- Addresses by version: 12b: 0x08006DDA, 143: 0x08006CAE, 152: 0x08006CDE, 0160: 0x08006C86
- Called by: `mcu_pulse_burst_decode`
- Confidence: medium

## mcu_ctrl_ramp_limit_update

**Ramp limiter with rising and falling edge handling for a control output**

Edge-aware ramp for a control output. Byte +0xB0 is the current enable and +0xB1 the previous one. On a rising edge, +0x90, +0x94 and DAT_20000738 are set to param_4 times gain +0x18 in Q15, and on a falling edge +0x94 is scaled by 0x9999/32768 (about 0.6). While disabled, +0x94 is slewed toward param_2: the step is q15_div_sat(+0x1C, rate), where rate is +0xA0 clamped to 0xCCC..0x10000 and forced to 0xCCC when +0x10 <= rate, and the value moves by the step or snaps to the target when within one step. While enabled, +0x90 is multiplied by the Q15 gain at +0x14. If param_5 is nonzero, *param_3 is min-clamped to the computed value, and the function returns 1 only when param_5 is set and the block is enabled.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ramp block (enable bytes at +0xB0/+0xB1, accumulators at +0x90/+0x94, gains and limits) |
| `param_2` | `s32` | target value |
| `param_3` | `ptr` | output word, min-clamped when param_5 is set |
| `param_4` | `s32` | input value used on the rising edge (scaled by gain +0x18) |
| `param_5` | `s32` | clamp enable (nonzero to clamp the output) |

**Returns** `s32`: 1 when clamp enabled and block enabled, else 0

**Notes:** While the block is enabled the clamp uses the value 0 (iVar5 stays 0 there), so *param_3 is clamped to min(*param_3, 0) on that path. This matches the code but looks odd and is worth checking against the callers.

- Addresses by version: 143: 0x08002AD0, 152: 0x08002A54, 0160: 0x08002A64
- Called by: `mcu_0160_08003f2c`
- Calls: `mcu_q15_div_sat`
- Confidence: medium

## mcu_dq_power_estimate

**Step the value at +0x18 toward a limit, then return 1.5 times a two-term Q15 product sum**

Reads the value at +0x18 and the reference DAT_200003DE / 70.0 in Q15 as in mcu_dynamic_bound_clamp_update. If the word at +0x28 is at least the reference, the value at +0x18 drops by the step at +0x23C, and if it is at most the negative reference it rises by the step, otherwise it is unchanged. It then forms two products in Q30 with the constant 0x5E97D0: the word at +0x28 times the adjusted value at +0x18, and the word at +0x24 times the value at +0x14. The return value is 1.5 (0xC000 in Q15) times the sum of the two products shifted right by 15.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | estimator object (offsets +0x14, +0x18, +0x23C and the words at +0x24 and +0x28) |

**Returns** `s32`: Q15 value, 1.5 times the sum of the two products

**Notes:** The 1.5 factor fits an amplitude-invariant dq-to-abc power or torque relation, which is a guess. The meaning of the inputs is not identified.

- Addresses by version: 12b: 0x08007768, 143: 0x0800765C, 152: 0x080076D4, 0160: 0x0800767C
- Called by: `mcu_0160_08005d84`
- Calls: `__ARM_scalbnf`, `__aeabi_ui2f`, `__aeabi_fdiv`, `__aeabi_f2iz`, `mcu_q30_mul`
- Confidence: low

## mcu_drive_state_set

**Store drive state DAT_20000F44 and set the transition flag DAT_20000E37**

Setter for the drive state byte DAT_20000F44 that also maintains the transition flag DAT_20000E37. If the state changes the flag is cleared, then set for the transitions 3 to anything, 2 to 1 and 1 to 2. Afterwards the flag is cleared if mcu_status_bf4_any_low_bits() is set and the new state is not 2, and cleared again if mcu_fault_b1c_mask_any() is set; the new state is then stored. The callers are not in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | new drive state |

**Notes:** The meaning of states 1 to 3 is not established.

- Addresses by version: 12b: 0x08005970, 143: 0x08005874, 152: 0x080058D8, 0160: 0x08005978
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_status_bf4_any_low_bits`, `mcu_fault_b1c_mask_any`
- Confidence: medium

## mcu_drive_state_update

**Enter or leave active drive mode DAT_20000E33 from speed, faults and counters**

Decides whether the drive is in active mode (DAT_20000E33) and seeds the ramp and position state when it enters. It reads x = mcu_get_cfg_field_0x28_q15() and steps counter D50 on x > DAT_2000040A x 0x8000; that output ANDed with DAT_20000E20 is the over-limit flag. The gate requires DAT_20000E34 set, DAT_20000E32 and DAT_20000E1A clear, no over-limit flag, mcu_status_bf4_any_low_bits clear and bit 0x4 of DAT_20000BF4 clear, and the counter DB4 is stepped on bit 1 of DAT_20001FD4. Entering needs the gate, E33 clear, the DB4 output set and DAT_20000F30 above 0x27FFF; it sets DAT_20000E24 to the lesser of F30 and (byte 0x20001FDC + 1) x 0x4000, computes a ramp value from the limit (x 10/9) and sets DAT_20000164 and DAT_20000168 to it, and sets DAT_20000BE0 and E33. While active it stays active while the gate and the DB4 output hold and |F30| is above 0x10000, and otherwise E33, E24 and DAT_20000E28 are cleared; whenever the gate fails those three are cleared as well.

**Notes:** The meaning of the state byte DAT_20000E33 is taken as the active drive or ramp mode. Caller mcu_0160_08004e78 is not in this packet. The limit used on entry comes from mcu_0160_0800ce3c and mcu_get_var_34c_ashr_scale as in the decompile.

- Addresses by version: 12b: 0x08005200, 143: 0x08005104, 152: 0x0800521C, 0160: 0x080052BC
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_status_bf4_any_low_bits`, `mcu_get_cfg_field_0x28_q15`, `mcu_get_limit_min3_or_unbounded`, `mcu_edge_counter_step`, `mcu_get_var_34c_ashr_scale`, `mcu_limit_ratio_with_floor`
- Confidence: medium

## mcu_edge_pos_track

**Track the edge-counted position estimate and retarget the ramp in drive-active mode**

Per-tick position tracker. While DAT_20000E33 (drive-active flag) is clear it resets the four edge counters at 0x20000D14, D00, D3C and D28 and clears DAT_20000E24 and DAT_20000E28. While active it steps those counters on bit 12 (A) and bit 13 (B) of DAT_20001FD4. A debounced A-only pulse from the first pair adds 0x8000 (one unit in Q15) to the position DAT_20000164, a B-only pulse subtracts 0x8000, and both or neither change nothing. The second pair counts pulses in groups of 200 and resets the first pair, and sets the event flag DAT_20000E39 on the limit comparisons (A pulses test the new position against DAT_20000660, B pulses against 0x28000). When the position changes, the target DAT_20000168 is set to the position bounded by 0x28000 below and DAT_20000660 above, mcu_ramp_toward_target_s32 moves DAT_20000164 toward it by at most 0x1EB per call, and DAT_20000170 is set to mcu_0160_0800ce3c(DAT_20000164, 0x28000).

**Notes:** The meaning of the event flag DAT_20000E39 and of the 200-count second pair is only partly understood. Caller mcu_0160_08004e78 is not in this packet.

- Addresses by version: 12b: 0x08003510, 143: 0x08003410, 152: 0x08003394, 0160: 0x08003434
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_ramp_toward_target_s32`, `mcu_edge_counter_step`, `mcu_edge_counter_reset`, `mcu_limit_ratio_with_floor`
- Confidence: medium

## mcu_fb_lpf_select_update

**Low-pass the feedback with a Q30 coefficient chosen from the drive state**

Per-tick feedback filter. While DAT_20000E33 (drive-active) is clear it clears DAT_20000E30 and sets be4 = mcu_get_param_654_q15() and r118 = mcu_get_var_67c(). While active it sets be4 = DAT_20000BEC x DAT_20000BE0 and sets DAT_20000E30 when that product is outside the lowest 10% of the window (mcu_below_10pct_of_window returns 0). The Q30 coefficient DAT_20000144 is 0x05832840 (about 0.086), or 0x00664D0A (about 0.0062) when DAT_2000010B is set, or 1.0 (0x40000000, no filtering) while active; if DAT_20000E19 is set it is forced to 1.0, otherwise 0x23A3A3C0 (about 0.55) is used when |DAT_20000BE8 - P| is below 4 percent of DAT_20000BEC, or when DAT_20000BE8 is below P (P is the parameter value). mcu_lpf_q30_step then filters be4 into DAT_20000BE8 and r118 into r11c, and mcu_0160_0800a644 (not yet described) updates the object at 0x20000B90 from them. DAT_2000010B is copied from DAT_20000E33 at the end.

**Notes:** What DAT_20000BE8 represents is not established. The coefficient selection follows the decompiled order, including the override by DAT_20000E19. mcu_0160_0800a644 is not described.

- Addresses by version: 12b: 0x08004FEC, 143: 0x08004EF0, 152: 0x08004FF0, 0160: 0x08005090
- Peripheral registers: `TMR2.CTRL1` (A)
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_below_10pct_of_window`, `mcu_get_param_654_q15`, `mcu_get_var_67c`, `mcu_nop_stub`, `mcu_lpf_q30_step`, `mcu_pos_tracker_filter_pair_step`
- Confidence: medium

## mcu_get_limit_min3_or_unbounded

**Return DAT_20000660 clamped to >= 0x18000, or 0x7fff8000 if it is zero**

If the 32-bit value at 0x20000660 is zero the function returns 0x7fff8000, effectively an unlimited maximum (about 65535.0 in Q15). Otherwise it returns the value but never less than 0x18000 (3.0 in Q15). Treats 0 as 'feature/limit disabled' and enforces a floor on configured limits. Called from mcu_0160_08003d2c, 080052bc, 0800576c and 0800ce3c.

**Returns** `s32`: limit in Q15, minimum 0x18000, 0x7fff8000 when unset

**Notes:** Physical unit unknown (current, speed or time).

- Addresses by version: 12b: 0x08004950, 143: 0x08004944, 152: 0x08004A24, 0160: 0x08004AC4
- Called by: `mcu_0160_08003d2c`, `mcu_drive_state_update`, `mcu_speed_limit_calc`, `mcu_limit_ratio_with_floor`
- Confidence: medium

## mcu_limit_668_or_default

**Return the RAM limit DAT_20000668 when enabled, else 0.5 (0x4000)**

Selects the limit used by the caller. If the inhibit byte DAT_20000A9A is set it returns 0 and, when the latch DAT_200000B5 is still zero, copies the inhibit value into it (a one-time latch). With the inhibit clear it calls mcu_cond_658_and_not_a9a, which is true when the enable byte DAT_20000658 is set; in that case it returns the word DAT_20000668, otherwise the default 0x4000 (0.5 in Q15). The only caller listed is mcu_0160_080054fc, which is not in this packet.

**Returns** `s32`: Q15 limit; 0 while inhibited, DAT_20000668 when enabled, else 0x4000

**Notes:** The meaning of the inhibit and enable bytes is inferred from their names only.

- Addresses by version: 12b: 0x0800465C, 143: 0x08004650, 152: 0x08004730, 0160: 0x080047D0
- Called by: `mcu_0160_080054fc`
- Calls: `mcu_cond_658_and_not_a9a`
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

## mcu_limit_chan_cfg_a

**Load limit channel A from RAM block 0x224 and reset edge counter D58**

Fills a limit channel object from the RAM configuration block at 0x20000224..0x2000023D: DAT_20000224 goes to +0x00, DAT_20000230 to +0x04, DAT_20000234 to +0x10, DAT_20000238 to +0x14 and the byte at 0x2000023D to +0x28. It also copies DAT_20000654 to +0x1C and DAT_20000E08 to +0x20, writes the constants 0x78000 at +0x0C and 0x8F999 at +0x18, and writes two 32-bit words 0x41F00000 (f32 30.0) at +0x2C and +0x30. It zeroes +0x08 and the bytes at +0x24..+0x26, sets the mode byte at +0x27 to 5, and finishes by resetting the edge counter at DAT_20000D58 with mcu_edge_counter_reset (called as 0x080099AE in this image). Present only in the 12b and 143 builds, and no caller is listed in the packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | limit channel object |

**Notes:** The packet callee list names mcu_edge_counter_reset for this call; the 143 image address for that routine is 0x080099AE. The 0x41F00000 words are read as f32 30.0.

- Addresses by version: 12b: 0x08003724, 143: 0x08003624
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_edge_counter_reset`
- Confidence: medium

## mcu_limit_chan_cfg_b

**Load limit channel B from RAM block 0x240 and reset edge counter D58**

Same pattern as mcu_limit_chan_cfg_a for the second configuration block. DAT_20000240 goes to +0x00, DAT_2000024C to +0x04, DAT_20000250 to +0x10, DAT_20000254 to +0x14 and the byte at 0x20000259 to +0x28, with DAT_20000E08 at +0x20 and DAT_20000654 at +0x1C. The constants are 0x78000 at +0x0C, 0x11F333 at +0x18 and two 0x41F00000 words (f32 30.0) at +0x2C and +0x30. It zeroes +0x08 and the bytes at +0x24..+0x26, sets mode 5 at +0x27, and resets the edge counter at DAT_20000D58 (called as 0x080099AE in this image). Present only in the 12b and 143 builds, and no caller is listed in the packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | limit channel object |

**Notes:** Object layout inferred from writes only. Constant 0x11F333 is taken as a limit or rate value.

- Addresses by version: 12b: 0x08003980, 143: 0x08003910
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_edge_counter_reset`
- Confidence: medium

## mcu_limit_chan_cfg_d

**Load limit channel D with |DAT_20000780|/4 capped at 10.0 and gain 0.8**

Configures a limit channel object for the 152 and 0160 builds from the signed value DAT_20000780. Its magnitude divided by 4 (signed division rounding) goes to +0x0C while the magnitude is below 0x140000 (40.0 in Q15), otherwise +0x0C is 0x50000 (10.0). It then loads the object from RAM block 0x2000024C..0x20000265 and DAT_20000E2C and DAT_20000668 (DAT_2000024C to +0x00, DAT_20000258 to +0x04, DAT_2000025C to +0x10, DAT_20000260 to +0x14, the byte at 0x20000265 to +0x28), with constant 0x5FBBB at +0x18, mode 5 at +0x27 and enable cleared at +0x29. It resets the shared edge counter DAT_20000D78 and sets DAT_200008BC = 0x294000 and DAT_200008B4 = 0x6999 (0.8 in Q15).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | limit channel object |

**Notes:** Caller mcu_0160_08004e78 is not in this packet. The meaning of DAT_20000780 is not established.

- Addresses by version: 152: 0x0800396C, 0160: 0x08003A0C
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_edge_counter_reset`
- Confidence: medium

## mcu_limit_chan_cfg_high_seed

**Seed limit channel from block 0xB3C, set mode 1, and force edge counter D78 high**

Loads a limit channel object from the 0x20000B3C block: DAT_20000B3C goes to +0x00, the larger of DAT_20000B40 and DAT_20000B48 to +0x04, DAT_20000B4C to +0x10, DAT_20000B50 to +0x14, DAT_20000F20 to +0x18 and DAT_20000F24 to +0x1C. It zeroes +0x08, +0x0C, +0x24..+0x26, +0x29 and finally +0x28, sets the mode byte at +0x27 to 1, and writes two 0x41A00000 words (f32 20.0) at +0x2C and +0x30. The shared edge counter at DAT_20000D78 is then forced high with mcu_edge_counter_force_high, which reloads it and drives its output high, so the next step continues from the reload value. DAT_20000B3C is the output of mcu_limit_target_b3c_update (0x080055C4).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | limit channel object |

**Notes:** Object layout inferred from writes only. The 0x41A00000 words are read as f32 20.0.

- Addresses by version: 12b: 0x08003BF8, 143: 0x08003B88, 152: 0x08003C28, 0160: 0x08003CC8
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_edge_counter_force_high`
- Confidence: medium

## mcu_limit_chan_init_mode6

**Set limit channel to mode 6 and enabled, clear +0x0C, reset edge counter D78**

Configures the limit channel object passed in param_1 (its layout is inferred from these writes and is not yet typed). It clears the 32-bit word at +0x0C, sets the mode byte at +0x27 to 6 and the enable byte at +0x29 to 1, then calls mcu_edge_counter_reset on the shared edge counter at DAT_20000D78. Mode 6 differs from the mode 5 used by the other channel setups in this packet, so this channel presumably takes a different limiting branch in its consumer. The only caller is mcu_0160_08004e78, which is not in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | limit channel object |

**Notes:** Object layout inferred from writes only.

- Addresses by version: 152: 0x08003568, 0160: 0x08003608
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_edge_counter_reset`
- Confidence: medium

## mcu_limit_chan_update_c

**Update limit channel C: decay its limit on a hold counter and reload gain constants**

Recomputes limit channel C for the 152 and 0160 builds. When |DAT_20000F30| is below 0x147 the hold counter DAT_20000114 counts down toward zero and, on reaching zero from 1, increments the event count DAT_20000109 (capped at 5); a larger |DAT_20000F30| reloads the hold counter to 2000. While the hold counter is below 2 and DAT_20000109 is below 3, the word at +0x0C is reduced by 0x147 per call toward 0, otherwise it is set to 0x30000 (6.0 in Q15). The object is then loaded from RAM 0x20000230..0x20000249 and DAT_20000E2C and DAT_20000668 with mode 5 and enable cleared at +0x29, and the shared edge counter DAT_20000D78 is reset. Finally the leaky counter DAT_20000112 (+10 when |DAT_20000F30| is at least 0x10CCC, otherwise -1 per call, capped at 1000) selects the constant pair written to DAT_200008B4 and DAT_200008BC: 0x1A666 and 0xA50000 below 10, otherwise 0x6999 and 0x294000.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | limit channel object |

**Notes:** Caller mcu_0160_08004e78 is not in this packet. The gain constants are read as Q15/Q16 values but their consumers are not identified.

- Addresses by version: 152: 0x080035C4, 0160: 0x08003664
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_edge_counter_reset`
- Confidence: medium

## mcu_limit_ratio_with_floor

**Map two values against a limit to a Q15 ratio with a 10 percent floor, saturating at full scale**

Returns a Q15 derating factor. The limit comes from mcu_get_limit_min3_or_unbounded (DAT_20000660, at least 0x18000). If the limit is at or below param_1 the result is full scale (0x8000). Otherwise the larger of the two inputs is divided by the limit in Q15 and mapped to 0.9 times that ratio plus 0.1 (0x8E38 is 1/0.9 and 0xCCC is 0.1 in Q15), so the result runs from about 0.1 up to 1.0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | first input, compared with the limit |
| `param_2` | `s32` | second input |

**Returns** `s32`: Q15 factor, 0x8000 at full scale

**Notes:** Which physical quantities the two inputs are is not visible in this packet.

- Addresses by version: 12b: 0x0800CB20, 143: 0x0800CD9C, 152: 0x0800CDDC, 0160: 0x0800CE3C
- Called by: `mcu_ramp_asym_track`, `mcu_edge_pos_track`, `mcu_drive_state_update`
- Calls: `mcu_q15_div_sat`, `mcu_get_limit_min3_or_unbounded`
- Confidence: medium

## mcu_limit_target_b3c_update

**Compute the limited target DAT_20000B3C from the B14 band and base DAT_200003DE**

Computes the limited output DAT_20000B3C from the base DAT_200003DE x 0x8000 and the band of DAT_20000B14. Inside 0x348001..0x36FFFF the output is base + base x offset, where offset is q15 division of (0x348000 - B14) by 0x50000 clamped to [-0x4000, 0]; at or above 0x370000 the offset is q15 division of (0x370000 - B14) by 0x88000, shifted by -0x4000 and clamped to [-0x6666, -0x4000]. At or below 0x348000 the output is just the cap. The result is capped at the first word of the object selected by the pointer table at 0x20000268 with index DAT_20000B54, and then mcu_0160_080070AC (not yet described; it calls mcu_lpf_q30_step) filters the object at 0x20000C3C.

**Notes:** The cap table at 0x20000268 is read as pointers to objects whose first word is the cap. Caller mcu_0160_08004e78 is not in this packet.

- Addresses by version: 12b: 0x080055BC, 143: 0x080054C0, 152: 0x08005524, 0160: 0x080055C4
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_q15_div_sat`, `mcu_q15_mul_sat`, `mcu_lpf_or_step_tracker_update`
- Confidence: medium

## mcu_limiter_set_range

**Store the larger of two bounds at cfg+0x25C and retarget limiter object C0**

Stores the larger of param_1 and param_2 at cfg+0x25C, where cfg is the pointer at DAT_200000F8. It then calls mcu_0160_08007c08 (not yet described) on the limiter object at 0x200000C0 with both bounds, each paired with a Q15 limit taken from the low and high bytes of DAT_20001FDE (each shifted left by 15), and the constant 0xA3 (163). Finally it stores param_3 as a flag byte in DAT_200000F6. The only caller listed is mcu_0160_08003c78, which is not in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | first bound (Q15) |
| `param_2` | `s32` | second bound (Q15) |
| `param_3` | `u8` | flag value stored at DAT_200000F6 |

**Notes:** The roles of the two bounds, the 0xA3 constant and the meaning of the limiter object at 0x200000C0 are not established.

- Addresses by version: 12b: 0x08004BBC, 143: 0x08004BB0, 152: 0x08004C9C, 0160: 0x08004D3C
- Called by: `mcu_0160_08003c78`
- Calls: `mcu_speed_range_setup_core`
- Confidence: medium

## mcu_main_ctx_flag4_clear

**Returns true when the flag byte at +0x04 of the main context object is clear**

Wrapper for mcu_ctx_flag4_is_clear applied to the global context pointer DAT_2000002C. Returns 1 when the byte at +0x04 of that object is zero, otherwise 0.

**Returns** `bool`: true when the context flag at +0x04 is clear

- Addresses by version: 12b: 0x08003210, 143: 0x0800310C, 152: 0x08003090, 0160: 0x08003130
- Called by: `mcu_0160_08007364`
- Calls: `mcu_ctx_flag4_is_clear`
- Confidence: high

## mcu_motor_calib_apply

**Pass the stored calibration words to the controller block setup when the record is valid**

Called every tick. When the validity byte at 0x20001F40 is neither 0x00 nor 0xFF it calls mcu_ctrl_block_init_default (mcu_0160_080029ac) on the controller object at 0x20000E3C, with eight 16-bit calibration words from 0x20001F30 to 0x20001F3E (even offsets), each scaled by 128, and with the validity byte as the last argument. Nothing is written when the record is blank or erased. The wrapper keeps no state of its own.

**Notes:** The last argument (0x20001F40) may be a count or a mode rather than a validity byte; the packet does not say which.

- Addresses by version: 143: 0x0800A428, 152: 0x0800A474, 0160: 0x0800A4E8
- Called by: `mcu_0160_0800a0b0`
- Calls: `mcu_ctrl_block_init_default`
- Confidence: medium

## mcu_mul_q15_f5e_by_3f2

**Q15 multiply of RAM value 0x20000f5e (shifted to Q15) by 0x200003f2, result >> 15**

Loads the 16-bit value at 0x20000f5e, shifts it left by 15 (so it is treated as an integer in Q15), multiplies it by the 16-bit value at 0x200003f2 with a 64-bit signed multiply and returns the product >> 15, i.e. effectively f5e * 3f2 without overflow. Called from mcu_0160_08005b3c (and the 12b equivalent). Acts as a gain/scale step; the second operand is probably a calibration or configuration scale factor.

**Returns** `u32`: DAT_20000f5e * DAT_200003f2

**Notes:** Operand meanings unknown; arithmetic is certain.

- Addresses by version: 12b: 0x0800222C, 143: 0x08002268, 152: 0x080021EC, 0160: 0x08002208
- Called by: `mcu_fault_monitor_update`
- Confidence: medium

## mcu_neg_limit_flag_update

**Update flag DAT_20000E35 from the cfg+0x28 value and DAT_20000F2C**

Updates the flag DAT_20000E35 from x = mcu_get_cfg_field_0x28_q15(). When DAT_20000E1A and DAT_20000E31 are both clear and x is below -0x20000 (-4.0) with DAT_20000E1D clear, the flag is set if DAT_20000F2C is below -0x1999 (about -0.2) and cleared if it is 1 or more, and is otherwise left as it was. If that first case does not apply and x is above -0x10000 (-2.0), the flag is cleared. When DAT_20000E1A or DAT_20000E31 is set, the flag is forced to 1. Only DAT_20000E35 is written.

**Notes:** The name reflects the thresholds; the meaning of DAT_20000E35 is not established. Caller mcu_0160_08004e78 is not in this packet.

- Addresses by version: 12b: 0x0800534C, 143: 0x08005250, 152: 0x08005384, 0160: 0x08005424
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_get_cfg_field_0x28_q15`
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
- Called by: `mcu_ctrl_block_init_default`
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
- Called by: `mcu_12b_ctrl_block_init`
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
- Called by: `mcu_ctrl_block_init_default`
- Confidence: medium

## mcu_param_record_load

**Decode the stored motor parameter record into the runtime block, rejecting blank or erased records**

Loads the stored parameter record at param_2 into the runtime block at param_1. Byte 0 of the record is a validity marker: 0x00 and 0xFF (erased flash) are rejected, the function returns 1 and writes nothing. For a valid record the 16-bit big-endian fields at record offsets 0x02, 0x04, 0x06, 0x10, 0x12, 0x14, 0x3A, 0x3D and 0x83 are read with mcu_read_be16 and stored as halfwords, the values at 0x10, 0x12 and 0x14 are halved, and the fields at 0x51, 0x53 and 0x55 become floats divided by 1e6, 1000 and 1000. Fields the record does not carry get fixed defaults: halfwords 0x73, 0x99, 0x32, 0x96 and 1, floats 0.1, 1.1, 7.0, 2.0 and 1.0, and a float of about 0.288 built from the halfword pair 0x74BC/0x3E93. The byte at block +0x4D is cleared.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | runtime parameter block, about 0x4E bytes of halfword and float slots |
| `param_2` | `ptr` | stored parameter record, validity byte at offset 0 |

**Returns** `u8`: 0 when the record was loaded, 1 when it was rejected as blank or erased

**Notes:** The physical meaning of each record field is not visible in this packet; the defaults are the values the code writes.

- Addresses by version: 12b: 0x08009E88, 143: 0x0800A038, 152: 0x0800A084, 0160: 0x0800A0F8
- Peripheral registers: `TMR2.CTRL1` (A)
- Called by: `mcu_0160_08005edc`, `mcu_0160_0800b324`
- Calls: `__aeabi_ui2f`, `__aeabi_fdiv`, `mcu_read_be16`
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
- Called by: `mcu_0160_08003f2c`, `mcu_foc_pid_limits_set`, `mcu_0160_08008204`
- Confidence: high

## mcu_pid_sync_integrator

**Reset PID integrator to the clamped current output and latch the current measurement**

Sets the integrator at +0x30 to the present output *(+0x1C) clamped to [+0x24, +0x28], and stores the current measurement *(+0x18) in the previous-measurement slot +0x34. The clamp takes the output as-is if it lies within the limits and otherwise uses the nearer limit. Used to make the controller start from its current output (bumpless transfer), so the derivative term does not see a step at the restart.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | PID object (layout as in mcu_pid_update_q15) |

**Notes:** The bumpless-transfer purpose is inferred. Its caller mcu_0160_080082ac is outside this packet.

- Addresses by version: 12b: 0x08008150, 143: 0x08008158, 152: 0x08008248, 0160: 0x08008260
- Called by: `mcu_pid_enable_bumpless`
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
- Called by: `mcu_0160_08007364`, `mcu_foc_control_tick`
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
- Called by: `mcu_position_multiturn_half`
- Confidence: high

## mcu_position_multiturn_half

**Returns the half-scale multi-turn position of the main context object**

Calls mcu_position_multiturn_compute on the global context DAT_2000002C and returns the result arithmetically shifted right by one, which halves the position scale.

**Returns** `s32`: multi-turn position >> 1

- Addresses by version: 12b: 0x08003298, 143: 0x08003194, 152: 0x08003118, 0160: 0x080031B8
- Called by: `mcu_position_zero_and_latch`, `mcu_foc_control_tick`
- Calls: `mcu_position_multiturn_compute`
- Confidence: high

## mcu_position_observer_update

**Per-sample position observer update: cascade observer step, then Q30 low-pass of the estimate**

Runs mcu_cascade_observer_step on the input with the observer block at +0x20 (the estimate it returns is not used here). It then runs mcu_lpf_q30_step_alt on the state at +0x40 with the word at +0xD8 as its input and the coefficient 0x03C89460 (about 0.059 in Q30), and stores the raw input at +0xDC for the next call. Returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | observer object (observer block at +0x20, filter state at +0x40, input word at +0xD8, last input at +0xDC) |
| `param_2` | `s32` | raw sample for this period |

**Returns** `u32`: always 1

**Notes:** The link between the cascade's estimate and the word at +0xD8 is not visible in this function. The 12b build's counterpart is mcu_12b_position_observer_update.

- Addresses by version: 143: 0x08002F08, 152: 0x08002E8C, 0160: 0x08002E9C
- Called by: `mcu_0160_0800a320`
- Calls: `mcu_cascade_observer_step`, `mcu_lpf_q30_step_alt`
- Confidence: medium

## mcu_position_outlier_reject

**Accepts a new half-scale position sample unless it jumps more than 0x15E0000 from the last one**

Reads the word at +0x6C of the context DAT_2000002C with mcu_get_word_at_0x6c and halves it (>> 1) into DAT_200000A4. If that differs from DAT_200000A0 by more than 0x15E0000 in either direction, the old value DAT_200000A0 is returned and the new one is not accepted; otherwise the new value is returned. DAT_200000A0 is not written in this function, so the caller decides when the new value becomes the reference.

**Returns** `s32`: the new half-scale position, or the previous reference on a jump

**Notes:** The units of the 0x15E0000 threshold are position units of the context word, which are not confirmed.

- Addresses by version: 12b: 0x0800322C, 143: 0x08003128, 152: 0x080030AC, 0160: 0x0800314C
- Called by: `mcu_0160_08003178`, `mcu_0160_08007364`
- Calls: `mcu_get_word_at_0x6c`
- Confidence: medium

## mcu_position_rebase

**Set the multi-turn reference to the current raw counter and clear the wrap count**

Copies the raw counter at +0x44 into the reference at +0xAC and clears the wrap count at +0xA4. After this call mcu_position_multiturn_compute reports zero for the current position.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | drive context |

**Notes:** Caller mcu_0160_08004d94 is outside this packet.

- Addresses by version: 12b: 0x08008DF4, 143: 0x08008F90, 152: 0x08008FD0, 0160: 0x08009044
- Called by: `mcu_position_zero_and_latch`
- Confidence: high

## mcu_position_zero_and_latch

**Rebase the multi-turn position at the context object and latch the new reference**

Rebases the position of the context object at DAT_2000002C to its current raw counter by calling mcu_position_rebase, which also clears the wrap count, so the reported multi-turn position becomes zero. It then stores the value returned by mcu_0160_080031b8 (not yet described) into DAT_200008F8 and copies it to DAT_200008FC. The callers mcu_0160_08004e78, mcu_0160_08005480 and mcu_143_080052ac are not in this packet.

**Notes:** The rebase effect is taken from the mcu_position_rebase summary. mcu_0160_080031b8 is not described.

- Addresses by version: 12b: 0x08004C14, 143: 0x08004C08, 152: 0x08004CF4, 0160: 0x08004D94
- Called by: `mcu_0160_08004e78`, `mcu_0160_08005480`
- Calls: `mcu_position_multiturn_half`, `mcu_position_rebase`
- Confidence: high

## mcu_q15_to_percent_s16

**Convert the Q15 value at 0x20000a50 to a percentage (x * 100 / 32768) as s16**

Multiplies DAT_20000a50 (32-bit signed) by 0x320000 (= 100 * 0x8000) in 64 bits, shifts right by 15 (so x * 100) and again by 15 (divide by 0x8000), then truncates to a signed 16-bit result. So 1.0 in Q15 maps to 100. Called from mcu_0160_0800c6f0, the code that builds the externally visible/communicated values.

**Returns** `s16`: percent value 0..100 (negative values possible)

**Notes:** What 0x20000a50 represents (throttle request? torque fraction?) is not known.

- Addresses by version: 12b: 0x08004640, 143: 0x08004634, 152: 0x08004714, 0160: 0x080047B4
- Called by: `mcu_telemetry_group_get`
- Confidence: medium

## mcu_ramp_asym_track

**Ramp DAT_20000BE0 toward its target: distance-scaled steps down, fixed 0x20 up**

Moves the ramp output DAT_20000BE0 one step toward the target DAT_20000170 on each call. The call mcu_0160_0800ce3c(DAT_20000F30, 0x28000) is made for side effects only (its result is discarded and that callee is not yet described). When the target is below the output, the step depends on the distance: 0x20 up to a distance of 0x146, 0x41 up to 0x665, 0xA3 up to 0xCCB, 0x147 up to 0x1998, 0x666 up to 0x3FFF and 0xCCC beyond that. The step is forced to 0x20 while DAT_20000168 differs from DAT_20000164 (a target change still pending), and the output snaps to the target when the distance is below the step. When the target is above the output, the output rises by a fixed 0x20 per call and snaps when within 0x20. DAT_2000010A is set to 1 while DAT_20000168 differs from the position DAT_20000164.

**Notes:** Caller mcu_0160_08004e78 is not in this packet. The asymmetry (distance-scaled fast down, fixed slow up) is read directly from the decompiled comparisons.

- Addresses by version: 12b: 0x08003458, 143: 0x08003358, 152: 0x080032DC, 0160: 0x0800337C
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_limit_ratio_with_floor`
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
- Called by: `mcu_edge_pos_track`, `mcu_0160_08003f2c`, `mcu_cmd_ramp_update`, `mcu_0160_0800b10c`
- Confidence: high

## mcu_ratio_gain_clamped_q15

**Compute a Q15 gain clamped to 0.8..1.3 when both inputs reach the 0x18000 gate, else unity**

Works on the object at param_1. If the word at +0x18 and the global DAT_20000F30 are both at least 0x18000 (the gate threshold), it divides the word at +0x10 with mcu_q15_div_sat and clamps the quotient to [0x6666, 0xA666], which is 0.8 to 1.3 in Q15, storing it at +0x1C. Otherwise it stores unity (0x8000) at +0x1C. The DAT_20000F30 value is noted elsewhere as a Q16 speed, voltage or current quantity, which is not confirmed.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object: +0x10 numerator, +0x18 gated value, +0x1C receives the gain |

**Notes:** The second operand of the division is not visible in the decompile: it is passed in a register without an argument, so the exact ratio is unknown.

- Addresses by version: 12b: 0x08005D9C, 143: 0x08005C2C, 152: 0x08005C9C, 0160: 0x08005D3C
- Called by: `mcu_0160_0800a320`
- Calls: `mcu_q15_div_sat`
- Confidence: medium

## mcu_run_enable_update

**Set or clear run-enable DAT_20000E34 from hall input bit 2, speed and B20**

Updates the run-enable flag DAT_20000E34. Its input is bit 2 of DAT_20001FD4 ANDed with mcu_flag_1fce_is_clear(), debounced by counter DC8. While DAT_20000E1D is set the flag is cleared. Otherwise it is set when it is currently clear, DAT_20000B20 is above 0x31 (49), DAT_2000066C is clear and the debounced input is high. It is cleared when it is set and either the debounced input is low or DAT_2000066C is set, but only while |DAT_20000F30| is below 0x24000 (4.5 in Q15).

**Notes:** Meaning of DAT_20000B20, DAT_2000066C and the 0x20001FCE flag is not established in this packet. Bit 2 of 0x20001FD4 is taken as a digital input.

- Addresses by version: 12b: 0x080056DC, 143: 0x080055E0, 152: 0x08005644, 0160: 0x080056E4
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_flag_1fce_is_clear`, `mcu_edge_counter_step`
- Confidence: medium

## mcu_sample_history3_rise_detect

**Push a 0..200 sample into a 3-deep history and flag three consecutive large rises**

Ignores samples of 201 or more. For a valid sample it writes the output word at 0x20000680 as floor(sample * 4095 / 242) shifted left by 15 (a scaled Q-format value). It then checks whether the new sample and the three most recent history bytes at 0x20000670..0x20000672 form a run where each step (newer minus older) exceeds 35 (0x23); if so the byte at 0x20000673 is set to 20 (0x14). The history is then shifted by one (newest in 0x20000670). The flag is only set here and is not cleared, so some other code must clear or count it down. The meaning of the input signal is not visible in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | new sample, 0..200 |

**Notes:** The 4095 / 242 scaling was checked numerically for inputs 0..200. The purpose of the signal and the 0x20000673 consumer are unknown.

- Addresses by version: 152: 0x0800D884, 0160: 0x0800D9C4
- Called by: `mcu_can_rx_command_dispatch`
- Confidence: low

## mcu_scale_delta_q15

**Return (DAT_20000f5a - DAT_2000027e) * 0xdbf using Q15 fixed-point arithmetic**

Computes the unsigned 16-bit difference of two RAM values (0x20000f5a minus 0x2000027e, e.g. a measured value minus its offset/reference), shifts it into Q15 (<<15) and multiplies by the Q15 constant 0xdbf (3519, about 0.1074) using a 64-bit signed multiply, then shifts the 64-bit product right by 15. The net result is delta * 3519, i.e. a fixed-point rescale of a raw count difference. Called from mcu_0160_08005d84. The same Q15 pattern (0x8000 = 1.0) is used by the neighbouring helpers in this group.

**Returns** `u32`: (f5a - 27e) * 3519, a scaled difference

**Notes:** What the two RAM values physically are (ADC counts? current offset?) is not determinable from this function alone.

- Addresses by version: 12b: 0x0800209C, 143: 0x080020D8, 152: 0x0800205C, 0160: 0x08002078
- Called by: `mcu_0160_08005d84`
- Confidence: medium

## mcu_sensor_filter_tick_v12b

**12b periodic tick: sample two inputs, run seven Q30 low-pass stages and mirror two status bits**

Periodic routine of the 12b build with no direct caller in this packet. It returns at once while the ready byte DAT_20000B14 is zero. Otherwise it stores a Q15 product from mcu_mul_q15_f5e_by_3f2 as the first sample (0x20000A28) and a second value from the routine at 0x0800216C (mcu_0160_08002148, not yet described) into 0x20000AEC; that routine also reports a flag in 0x20000AF4, and when the flag is set the value is forced to 0x368000. On the first pass after reset (DAT_200000B1 == 0) seven mcu_lpf_q30_step stages run with Q30 weights 0x000A49B4 (about 0.0006), 0x23A3A3C0 (0.557), 0x07250810 (0.112, used for two stages), 0x00664D0B (0.006), 0x01F30A72 (0.030) and 0x0014901A (0.001), with the states at 0x20000A30, 0x20000A2C, 0x20000A38, 0x20000A40, 0x20000A48, 0x20000A50 and 0x20000AF0. When DAT_200000B1 is set it clears it, reseeds the states from the current inputs and sets 0x20000A48 to 0x8000 (1.0 in Q15). It then calls mcu_12b_080059ec (not yet described) and mcu_12b_08005d30, and mirrors bits 0x2 and 0x4 of DAT_20000BD0 into bits 0x100 and 0x200 of the flag word 0x20000AF8 with mcu_bits_set and mcu_bits_clear.

**Notes:** The signals behind the inputs are not visible in this packet. Stage order and weights were read from the call list and the decompiled constants. Larger Q30 weights track faster.

- Addresses by version: 12b: 0x08005B60
- Called by: `mcu_0160_0800a320`
- Calls: `mcu_speed_from_max_u12`, `mcu_mul_q15_f5e_by_3f2`, `mcu_bits_clear`, `mcu_bits_set`, `mcu_lpf_q30_step`, `mcu_threshold_status_12b`, `mcu_hall_transition_counter_update_v12b`
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

## mcu_speed_estimate_update

**Turn the encoder count accumulator into a filtered Q15 speed estimate**

Periodic speed estimator called from mcu_0160_0800a320. Inside an interrupt-disabled section it reads the 32-bit accumulator at +0x9C of the context object whose pointer is in DAT_2000002C (mcu_ctx_get_field_0x9c) and clears it (mcu_ctx_clear_field_0x9c), so each call consumes the counts gathered since the previous call. The count is clamped to +/-0x270 (624), converted to float, multiplied by 0x42D16EF3 (about 104.72, which is 1000 x 2pi / 60 and suggests an rpm to milli-rad/s conversion) and scaled by 2^15 before truncation to int. That sample is blended into the filtered value as DAT_200000A0 = 0.4 x sample + 0.6 x previous, using soft-float and the routine at mcu_0160_080012b8 (assumed to be a float add). DAT_2000009C is incremented on entry and cleared on exit, so it works as a sampling-in-progress marker.

**Notes:** Units and the meaning of the +0x9C accumulator are inferred from the constants. mcu_0160_080012b8 is assumed to be a float add and is not yet described.

- Addresses by version: 12b: 0x080032AC, 143: 0x080031A8, 152: 0x0800312C, 0160: 0x080031CC
- Called by: `mcu_0160_0800a320`
- Calls: `__aeabi_fadd`, `__aeabi_fmul`, `__ARM_scalbnf`, `mcu_i2f_lzc`, `__aeabi_f2iz`, `mcu_irq_disable_thunk`, `mcu_irq_enable_thunk`, `mcu_ctx_clear_field_0x9c`, `mcu_ctx_get_field_0x9c`
- Confidence: medium

## mcu_speed_from_max_u12

**Speed estimate from the maximum of 20 samples of a 12-bit channel, with a status code**

Companion of mcu_speed_from_period_min for the second filtered channel DAT_20000F5C. It uses the same 20-entry ring (at DAT_20000F64, index DAT_20000280) and every-20-call cadence, but takes the maximum (mcu_array_max_s32) and looks up 0x1000 - max in the same 236-entry table at 0x0800F45C, storing (index - 30) << 15 in DAT_20000284. While DAT_20000B20 > 500 the status byte at *param_1 is set from the maximum: 0xFD when it is below 0x51, 0 from 0x51 to 0xFF0, and 0xFE from 0xFF1 up, which are the regions near the two wrap points of a 12-bit value. Returns DAT_20000284, or 0xC8000 before the validity count passes.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | status byte output (0xFE, 0 or 0xFD) |

**Returns** `s32`: speed in Q15 (table index minus 30, shifted by 15), or 0xC8000 when not yet valid

**Notes:** The 12-bit channel is taken to be an angle-like or position-like counter from its 0x1000 wrap and thresholds. The status code thresholds are read directly from the compare chain.

- Addresses by version: 12b: 0x0800216C, 143: 0x080021A8, 152: 0x0800212C, 0160: 0x08002148
- Called by: `mcu_fault_monitor_update`
- Calls: `mcu_array_max_s32`, `mcu_u16_table_bsearch_desc`
- Confidence: medium

## mcu_speed_from_period_min

**Speed estimate from the minimum of 20 captured periods, table lookup, status code**

Every 20th call (the counter DAT_20000290 wraps at 20) pushes the current filtered capture DAT_20000F58 into a 20-entry ring of s32 at DAT_20000294 (index DAT_20000282, wrapping modulo 20). The minimum of the ring (mcu_array_min_s32) is looked up in a 236-entry descending u16 table at 0x0800F45C with mcu_u16_table_bsearch_desc, giving DAT_2000028C = (index - 30) << 15 in Q15, a speed-like value. While DAT_20000B20 > 500 the status byte at *param_1 is set from the minimum: 0xFE below 16, 0 from 16 to 3999, 0xFD at 4000 and above. The function returns DAT_2000028C while DAT_20000B20 > 500, otherwise the fallback 0xC8000 (25.0 in Q15).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | status byte output (0xFE, 0 or 0xFD) |

**Returns** `s32`: speed in Q15 (table index minus 30, shifted by 15), or 0xC8000 when not yet valid

**Notes:** The units of the captured period and the meaning of the table are inferred from the shape of the code (period to speed inverse table). DAT_20000B20 is read as a validity or warm-up count, which is also an inference.

- Addresses by version: 12b: 0x080020C0, 143: 0x080020FC, 152: 0x08002080, 0160: 0x0800209C
- Called by: `mcu_0160_0800a320`
- Calls: `mcu_array_min_s32`, `mcu_u16_table_bsearch_desc`
- Confidence: medium

## mcu_speed_limit_calc

**Compute limit outputs F38, F3C and F40 from a speed-like input and the mcu limit**

Takes a speed-like Q15 input param_2 and writes three outputs. DAT_20000F38 is param_2 x 30 - 3.0 (0xF0000 and 0x18000) when param_2 is below 0.1 (0xCCC), and otherwise (param_2 - 0.1) x mcu_get_limit_min3_or_unbounded() x 10/9 (0x8E38 in Q15). DAT_20000F3C is the mcu limit when that limit is below F38, otherwise F38 floored at 0x18000. DAT_20000F40 is copied from the word at +0x14 of param_1. Callers are mcu_0160_08003f2c and mcu_143_080052ac, not in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object whose +0x14 word is copied to DAT_20000F40 |
| `param_2` | `s32` | speed-like input in Q15 |

**Notes:** Meaning of the input and of the limit reported by mcu_get_limit_min3_or_unbounded is inferred from the names and constants.

- Addresses by version: 12b: 0x08005764, 143: 0x08005668, 152: 0x080056CC, 0160: 0x0800576C
- Called by: `mcu_0160_08003f2c`
- Calls: `mcu_get_limit_min3_or_unbounded`
- Confidence: medium

## mcu_speed_lpf_band_update

**Speed-adaptive band update: recomputes Q30 filter alphas, sets band flags and accumulators**

Structure of the 0160-build band update (about 280 instructions, so this summarises it). When the difference p[0x37] - p[0x26] is outside the band from p[0] or a value is below 1, it recomputes two Q30 first-order filter coefficients alpha = wT/(1+wT), with w = 2*pi*f and T = 0.005 s (IEEE-754 constants 0x40C90FDC, 0x3BA3D70A and 0x3F800000). Here f is a clamped function of |param_2| and a second clamped quotient 0xC80000/param_2, each converted to Q30 by __ARM_scalbnf and __aeabi_f2iz, and armed on the band block at +0x14 with mcu_band_block_arm_setpoint. In band, +0x14 is armed with 0xFD6114 or 0x37366F40 depending on the flag at +0x2C. The global DAT_20000734 is set from a stack-local comparison (mcu_select_stack_local_fragment) when p[0x27] is below 0x18000, and +0x26 takes the maximum of p[3] and the value from mcu_0160_08007160. The accumulators p[0x29], p[0x2A] and p[0x2B] and the filtered output p[0x27] are then updated from the magnitude of param_2.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | int word block of the speed/band object (fields at +0x00..+0xB0) |
| `param_2` | `s32` | signed speed-like input |

**Returns** `u32`: always 1

**Notes:** The field meanings and the threshold constants are inferred. mcu_0160_08007160 is not described yet. The 12b counterpart is mcu_12b_speed_lpf_band_update.

- Addresses by version: 143: 0x08002BD0, 152: 0x08002B54, 0160: 0x08002B64
- Called by: `mcu_0160_0800143c`
- Calls: `__aeabi_memcpy`, `__aeabi_fadd`, `__aeabi_fmul`, `__ARM_scalbnf`, `__aeabi_fdiv`, `__aeabi_f2iz`, `mcu_q15_div_sat`, `mcu_q15_mul_sat`, `__aeabi_i2f`, `mcu_select_stack_local_fragment`, `mcu_lpf_asym_update`, `mcu_band_block_arm_setpoint`
- Confidence: low

## mcu_speed_range_setup_core

**Validate and store a speed range, derive a 1/p7 count and a 0.01*(max^2-min^2)*p5 term**

Takes the bound max(param_4, param_2) as the upper value and accepts the call only when that bound, param_2, param_5 and param_7 are all positive. On acceptance it stores param_2 at +0x00, param_3 at +0x04, the bound at +0x08, param_5 at +0x0C, param_6 at +0x10 and param_7 at +0x14, and sets the accept byte at +0x35 to 1. It derives the count k = floor(32768 / param_7) rounded down to a multiple of 10 at +0x18, and the term 0.01 times (bound^2 - param_2^2) times param_5 at +0x20 (0x147 in Q15 as the 0.01 factor). The accumulator at +0x1C is kept at 0 or above when the term is non-negative. A rejected call clears the accept byte and returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object |
| `param_2` | `s32` | minimum value |
| `param_3` | `s32` | stored at +0x04 |
| `param_4` | `s32` | candidate maximum |
| `param_5` | `s32` | scale factor |
| `param_6` | `s32` | stored at +0x10 |
| `param_7` | `s32` | divisor for the count |

**Returns** `u8`: accept byte: 1 if accepted, 0 if rejected

**Notes:** The meaning of the speed range and of the term is a guess; the squared-difference term resembles a kinetic-energy or ramp term. Group with mcu_speed_range_setup_wrap.

- Addresses by version: 12b: 0x08007CE4, 143: 0x08007BD8, 152: 0x08007C60, 0160: 0x08007C08
- Called by: `mcu_limiter_set_range`, `mcu_speed_range_setup_wrap`
- Calls: `mcu_q15_div_sat`, `mcu_q15_mul_sat`
- Confidence: low

## mcu_speed_range_setup_wrap

**Call the speed-range setup core, store a flag byte at +0x36 and return the accept byte**

Forwards its six value arguments to mcu_speed_range_setup_core, stores the byte argument at +0x36 of the object, and returns the byte at +0x35 that the core sets to 1 when it accepted the parameters. The +0x36 byte is written whether or not the core accepted them.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object |
| `param_2` | `s32` | forwarded to the core as its minimum |
| `param_3` | `s32` | forwarded to the core, stored at +0x04 |
| `param_4` | `s32` | forwarded to the core as the candidate maximum |
| `param_5` | `s32` | forwarded to the core as the scale factor |
| `param_6` | `s32` | forwarded to the core, stored at +0x10 |
| `param_7` | `s32` | forwarded to the core as the divisor |
| `param_8` | `u8` | flag stored at +0x36 |

**Returns** `u8`: accept byte at +0x35: 1 if accepted, 0 if rejected

**Notes:** Group with mcu_speed_range_setup_core.

- Addresses by version: 12b: 0x08007CB0, 143: 0x08007BA4, 152: 0x08007C2C, 0160: 0x08007BD4
- Called by: `mcu_0160_08003c38`
- Calls: `mcu_speed_range_setup_core`
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

## mcu_target_derate_calc

**Compute the Q15 drive target from the B14 band, base DAT_200003DC and a derate term**

Computes a Q15 target, returns it, and stores a physical value in DAT_200000FC. The base is DAT_200003DC x 0x8000. An offset is taken from DAT_20000B14: zero at or below 0x2F8000, then a negative offset that falls linearly (Q15 division by 0xA0000) to -0x4000 at 0x348000, -0x6000 at 0x370000 and clamps at -0x8000. The target is base + base x offset (mcu_q15_mul_sat), then multiplied by (1 + k/2), where k = clamp(DAT_20000A44 - DAT_200003E6 - 2.0, -1.87, 0) in Q15. The result is capped at DAT_20000664 and at the base, and floored at 0x10000 (2.0); DAT_200000FC is set to the float target divided by 35.885 (f32 0x420F999A) and truncated. Finally mcu_cond_mode_bit0_and_level_ok selects a lower bound: when it holds the function returns the larger of the target and the word at +0x30 of an object whose pointer the decompiler lost.

**Returns** `s32`: Q15 target, or the lower bound when that applies

**Notes:** The meaning of DAT_20000B14, the 35.885 divisor and the final clamp are not established. The +0x30 object pointer is lost in the decompile (extraout_r3). Callers listed: mcu_0160_080054fc.

- Addresses by version: 12b: 0x08004698, 143: 0x0800468C, 152: 0x0800476C, 0160: 0x0800480C
- Called by: `mcu_0160_080054fc`
- Calls: `mcu_i2f_lzc`, `__aeabi_fdiv`, `__aeabi_f2iz`, `mcu_q15_div_sat`, `mcu_q15_mul_sat`, `mcu_cond_mode_bit0_and_level_ok`
- Confidence: low

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
