# MCU - `hall` functions

10 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_hall_dispatch_pc12_output`](#mcu_hall_dispatch_pc12_output) | 0x08007268 | Run the hall dispatcher, then drive GPIOC pin 12 from bit 0x4000 of the word at 0x20001FDA |
| [`mcu_hall_get_transition_status`](#mcu_hall_get_transition_status) | 0x0800915C | Return the hall sector transition status byte at +0x01 |
| [`mcu_hall_position_update`](#mcu_hall_position_update) | 0x08009598 | Update the hall-sensor rotor angle and speed estimate, resyncing at sector edges |
| [`mcu_hall_sector_transition`](#mcu_hall_sector_transition) | 0x080090A0 | Validate a 60-degree hall sector step from +0x5C to +0x60 and set direction +0x38 to +1 or -1 |
| [`mcu_hall_sector_window_update`](#mcu_hall_sector_window_update) | 0x08008F78 | Set magnitude fault 0x4305 and recompute the expected-sector window bounds at +0x50 and +0x54 |
| [`mcu_hall_state_dispatch`](#mcu_hall_state_dispatch) | 0x08003034 | Dispatch to a per-state handler selected by bits 9..11 of a status word |
| [`mcu_hall_transition_counter_update_v12b`](#mcu_hall_transition_counter_update_v12b) | (removed) | 12b: count hall transition codes in two edge counters and raise event flags 0x400 and 0x80000 |
| [`mcu_pos_tracker_filter_pair_step`](#mcu_pos_tracker_filter_pair_step) | 0x0800A644 | Run one tracker filter step on the scaled primary sample and on the global second channel |
| [`mcu_pos_tracker_init`](#mcu_pos_tracker_init) | 0x0800A594 | Initialise the position tracker object: range, Q15 scale, filter coefficient and gains |
| [`mcu_pos_tracker_update_v143`](#mcu_pos_tracker_update_v143) | (removed) | Update the 12b/143 position tracker: scaled delta, Q30 filter, jump and holdoff state |

## mcu_hall_dispatch_pc12_output

**Run the hall dispatcher, then drive GPIOC pin 12 from bit 0x4000 of the word at 0x20001FDA**

Calls mcu_hall_state_dispatch, then the routine at 0x0800A90C (mcu_0160_0800a90c, not yet described). It then writes mask 0x1000 to the GPIOC set register (SCR) when bit 0x4000 of the word at 0x20001FDA is set, and to the clear register (CLR) otherwise. The dispatcher's notes place this routine at interrupt level.

**Notes:** The packet's register list names GPIOC.CFGLR, but the code uses the SCR and CLR offsets.

- Addresses by version: 12b: 0x0800739E, 143: 0x08007290, 152: 0x080072C0, 0160: 0x08007268
- Peripheral registers: `GPIOC.CFGLR` (A)
- Called by: `mcu_0160_0800a320`
- Calls: `mcu_hall_state_dispatch`, `mcu_indicator_update`, `mcu_ctx_set_field_0x14`, `mcu_ctx_set_field_0x10`
- Confidence: medium

## mcu_hall_get_transition_status

**Return the hall sector transition status byte at +0x01**

Getter for byte +0x01 of the object, which mcu_hall_sector_transition sets to 0 for a valid step or to 1..6 for an invalid one.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | drive context |

**Returns** `u8`: transition status

**Notes:** Callers mcu_0160_08005b3c and mcu_12b_08005d30 are outside this packet.

- Addresses by version: 12b: 0x08008F00, 143: 0x0800909C, 152: 0x080090E8, 0160: 0x0800915C
- Called by: `mcu_fault_monitor_update`
- Confidence: high

## mcu_hall_position_update

**Update the hall-sensor rotor angle and speed estimate, resyncing at sector edges**

Per-tick position and speed tracker for the hall-sensor drive context. It reads the current hall sector through the callback at +0x0C, stores it at +0x00 and loads the reference angle of that sector from the 32-bit table at 0x20000714. It integrates the speed-scaled step (from the helper at 0x08001E0C, result at +0x64) into the electrical angle at +0x4C and wraps it modulo 0x6487E, which is 2*pi in Q16. On a sector change it snaps the angle into the expected-sector window (bounds at +0x50 and +0x54) and nudges the correction counter at +0xA4 within -0x145E..0x145E. When the byte at +0x08 is set it also smooths the angle through the Q30 low-pass step and recomputes the window through mcu_hall_sector_window_update, and the result goes to +0x44. Group with mcu_hall_sector_window_update.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | hall drive context: sector +0x00, flags +0x03, +0x04, +0x06, +0x08, sector callback +0x0C, angle +0x4C, output +0x44, direction word +0x38 |
| `param_2` | `s32` | signed rate input, multiplied by the direction word at +0x38 |

**Notes:** Field roles are read from the arithmetic and the callee summaries. The two branches and the constants 0x5C273, 0x860A and 0x53C69 are not fully resolved. Reading 0x6487E as 2*pi in Q16 is an inference from the value.

- Addresses by version: 12b: 0x0800933C, 143: 0x080094D8, 152: 0x08009524, 0160: 0x08009598
- Called by: `mcu_0160_08003104`
- Calls: `mcu_q16_mul_round`, `mcu_q30_div_sat`, `mcu_q30_mul_round`, `mcu_q30_lerp`, `mcu_hall_sector_window_update`
- Confidence: medium

## mcu_hall_sector_transition

**Validate a 60-degree hall sector step from +0x5C to +0x60 and set direction +0x38 to +1 or -1**

Six sector codes are used: 0, 0x10C15, 0x2182A, 0x3243F, 0x43054 and 0x53C69, i.e. k x 0x10C15 for sectors k = 0..5 (60 degrees each, six per electrical revolution). The status byte +0x01 is cleared first. If the current code (+0x5C) is one of the six and the new code (+0x60) is one of its two neighbours mod 6, the direction halfword +0x38 is set to +1 for a step to the lower index (including 0 to 5) and to -1 for a step to the higher index (including 5 to 0), and the status stays 0. An invalid step leaves +0x38 unchanged and stores k+1 (1..6) in the status byte. A current code outside the six leaves the status at 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | drive context: current sector +0x5C, new sector +0x60, direction +0x38, status byte +0x01 |

**Returns** `u8`: 0 for a valid step, 1..6 (k+1 of the current sector) for an invalid step

**Notes:** The hall sensor interpretation is inferred from the six-state, neighbour-only transitions. Callers mcu_0160_08009160 is outside this packet.

- Addresses by version: 12b: 0x08008E44, 143: 0x08008FE0, 152: 0x0800902C, 0160: 0x080090A0
- Called by: `mcu_0160_08009160`
- Confidence: high

## mcu_hall_sector_window_update

**Set magnitude fault 0x4305 and recompute the expected-sector window bounds at +0x50 and +0x54**

If the flag byte at +0x04 is not 1 and |+0x70| is at least the limit at +0x88, byte +0x05 is set and fault code 0x4305 is stored at +0x58; otherwise both are 0. The window centre is C = +0x5C + +0x48, where +0x5C is the sector code (k x 0x10C15) produced by mcu_hall_sector_transition. The window depends on the direction state +0x38 (a signed halfword): 0 gives [C-10, C+10]; +1 gives [C-0x860A-f, C+f] (upper bound C+0x860B+f when +0x04 is 0); -1 gives [C-f, C+0x860A+f] (lower bound C-0x860B-f when +0x04 is 0), where f is the fault offset in +0x58. Half a sector is 0x860A, so the window covers about 30 degrees either side of the sector edge.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | drive context: flag +0x04, value +0x70, limit +0x88, centre inputs +0x48/+0x5C, direction +0x38, outputs +0x50/+0x54/+0x58 |

**Notes:** The meaning of the fault code 0x4305 and of the value at +0x70 is not established. The window interpretation rests on 0x860A being half of the 0x10C15 sector step. Callers mcu_0160_08009160 and mcu_0160_08009598 are outside this packet.

- Addresses by version: 12b: 0x08008D28, 143: 0x08008EC4, 152: 0x08008F04, 0160: 0x08008F78
- Called by: `mcu_0160_08009160`, `mcu_hall_position_update`
- Confidence: medium

## mcu_hall_state_dispatch

**Dispatch to a per-state handler selected by bits 9..11 of a status word**

Extracts idx = (DAT_20001fda & 0xfff) >> 9 (a 3-bit value 0..7, most likely the Hall-sensor pattern) and calls the function pointer at 0x20000698[idx] (a RAM table of 8 handlers) with argument DAT_20000678 ^ idx, i.e. the bit mask of what changed since the previous state. It then stores the new index (same bit field 9..11 re-extracted) into DAT_20000678 as the previous state. Called from mcu_0160_08007268, an interrupt-level routine. A Hall-commutation/edge interpretation is a guess based on the 3-bit field.

**Notes:** 0x20000698 is address-taken: an 8-entry function-pointer table in RAM. Actual source of 0x20001fda (Hall inputs vs. captured timer value) not shown.

- Addresses by version: 12b: 0x08003114, 143: 0x08003010, 152: 0x08002F94, 0160: 0x08003034
- Called by: `mcu_hall_dispatch_pc12_output`
- Confidence: medium

## mcu_hall_transition_counter_update_v12b

**12b: count hall transition codes in two edge counters and raise event flags 0x400 and 0x80000**

Takes the hall transition status of the object pointed to by DAT_2000002C from mcu_hall_get_transition_status, stores it in DAT_200000B0, and uses it to drive two edge counters with mcu_edge_counter_step. Counter 0x20000AC4 steps up only when the status is 7 and down otherwise. Counter 0x20000AD8 steps up when the status is 1 to 6, the invalid-transition codes, and down for 0 or 7. An output of 1 from the first counter sets flag bit 0x400 in 0x20000AF8, and an output of 1 from the second sets 0x80000, both through mcu_bits_set. Each counter output changes only after its limit is reached, so the two counters filter the transition stream.

**Notes:** Status code 7 is outside the 0..6 range documented for mcu_hall_get_transition_status, so its meaning is open. Counter limits are set elsewhere and are not visible here.

- Addresses by version: 12b: 0x08005D30
- Called by: `mcu_sensor_filter_tick_v12b`
- Calls: `mcu_bits_set`, `mcu_hall_get_transition_status`, `mcu_edge_counter_step`
- Confidence: medium

## mcu_pos_tracker_filter_pair_step

**Run one tracker filter step on the scaled primary sample and on the global second channel**

Two-channel update used by the MCU_152 and MCU_0160 builds. The primary sample in param_2 is stored at +0x20, its delta from the minimum at +0x24 is scaled by the Q15 factor at +0x2C and clamped to the ceiling at +0x1C, the target goes to +0x08, and one Q30 low-pass step runs into the filtered output at +0x0C (mcu_lpf_q30_step). The second input param_3 gets the same scaling, clamped at zero below the minimum, and is filtered into the global state at 0x2000034C with the same coefficient at +0x00. Group with mcu_pos_tracker_init.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | position tracker object |
| `param_2` | `s32` | primary sample |
| `param_3` | `s32` | secondary sample |

- Addresses by version: 152: 0x0800A5D0, 0160: 0x0800A644
- Called by: `mcu_fb_lpf_select_update`
- Calls: `mcu_lpf_q30_step`
- Confidence: medium

## mcu_pos_tracker_init

**Initialise the position tracker object: range, Q15 scale, filter coefficient and gains**

Constructor for the position tracker object used by mcu_pos_tracker_update_v143 and mcu_pos_tracker_filter_pair_step. It validates the arguments (min >= 0, min <= max, rate >= 50) and stores the range minimum at +0x24 and maximum at +0x28. The ceiling at +0x1C is 0x10000000, and the Q15 scale at +0x2C is 2^28 divided by the range width (saturating division). The Q30 coefficient at +0x00 is t/(t+1) with t = 100*pi/rate (the constant 315.16 is about 100*pi). The shift count 13 at +0x32 scales three gain constants, 0x50000, 0x30000 and 0x3D7, stored at +0x40, +0x44 and +0x48. The bounds +0x38 = 0x190000 and +0x3C = 0x147 are set, and the validity byte at +0x34 is 1 when every argument was accepted.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | position tracker object, at least 0x35 bytes |
| `param_2` | `s32` | range minimum, must be >= 0 |
| `param_3` | `s32` | range maximum, must be >= param_2 |
| `param_4` | `s32` | filter rate, must be >= 50 |

**Notes:** The validity byte is written even when the arguments are rejected (as 0), so callers must test +0x34 before use.

- Addresses by version: 12b: 0x0800A29C, 143: 0x0800A4D0, 152: 0x0800A520, 0160: 0x0800A594
- Called by: `mcu_0160_08005054`
- Calls: `__aeabi_fadd`, `__aeabi_fmul`, `__ARM_scalbnf`, `__aeabi_ui2f`, `__aeabi_fdiv`, `__aeabi_f2iz`, `mcu_q15_div_sat`
- Confidence: medium

## mcu_pos_tracker_update_v143

**Update the 12b/143 position tracker: scaled delta, Q30 filter, jump and holdoff state**

Per-sample update of the position tracker object in the MCU_12b and MCU_143 builds (group with mcu_pos_tracker_init and mcu_pos_tracker_filter_pair_step). The raw sample is stored at +0x20, the delta from the range minimum at +0x24 is scaled by the Q15 factor at +0x2C and clamped to the range ceiling at +0x1C into the target at +0x08, and that target is low-pass filtered into +0x0C (mcu_lpf_q30_step, alternate copy at 0x08007242). Globals: 0x20000338 flags a large step, 0x20000340 is a holdoff counter that is cleared by very large steps, reloaded from the halfword at +0x30 times 150/1000 on fast changes and decremented otherwise, and 0x2000033C is the filter bound (at least 0x18000, set to 0x190000 on a jump). A second filter step uses the coefficient x/(1+x) with x = 2*pi*bound/rate, converted to Q30 with __ARM_scalbnf and __aeabi_f2iz, and the output at +0x18 is the fixed-point square root helper applied to a Q28 product of the filtered value.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | position tracker object (see mcu_pos_tracker_init for the fields) |
| `param_2` | `s32` | new raw sample |

**Notes:** Field roles are inferred from the arithmetic and sibling routines. The float chain and the sqrt helper mcu_0160_08001D60 (mcu_math_sqrt_fixed_v143) are only partly resolved.

- Addresses by version: 12b: 0x0800A34C, 143: 0x0800A580
- Called by: `mcu_fb_lpf_select_update`
- Calls: `__aeabi_fadd`, `__aeabi_fmul`, `__ARM_scalbnf`, `__aeabi_ui2f`, `__aeabi_fdiv`, `__aeabi_f2iz`, `__aeabi_i2f`, `mcu_lpf_q30_step`, `mcu_q28_mul`, `mcu_math_sqrt_fixed_v143`
- Confidence: low
