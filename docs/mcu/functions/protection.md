# MCU - `protection` functions

23 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_12b_supervisor_update`](#mcu_12b_supervisor_update) | (removed) | 12b: threshold supervisor on A68 that updates status bits 0x1 and 0x2 in AF8 |
| [`mcu_a50_debounce_latch`](#mcu_a50_debounce_latch) | 0x08005690 | Latch flag DAT_20000E36 from the debounced test DAT_20000A50 above -5.0 |
| [`mcu_bus_threshold_monitor`](#mcu_bus_threshold_monitor) | 0x08005A00 | Monitor DAT_20000B14 against thresholds 0x3E8 and 0x3EA and mirror trips into B1C bit 0x20 |
| [`mcu_cmd_state_clear`](#mcu_cmd_state_clear) | 0x08007DC8 | Clear the command-pending word and byte, release owner 10 and clear bit 0x8 of 0x20000B1C |
| [`mcu_cond_mode_bit0_and_level_ok`](#mcu_cond_mode_bit0_and_level_ok) | 0x08004B1C | Return 1 if mode bit0 of 0x2000065d is set and 0x200003ea is at least 10 above both thresholds |
| [`mcu_digital_input_debounce`](#mcu_digital_input_debounce) | 0x080051BC | Debounce digital input bytes 0x1BC and 0x1BD through a bank of edge counters |
| [`mcu_f30_range_latch`](#mcu_f30_range_latch) | 0x08006580 | Latch flag 0x2000010F from the magnitude of the s32 at 0x20000F30; argument 0 clears the latch |
| [`mcu_fault_b1c_mask_any`](#mcu_fault_b1c_mask_any) | 0x08004E48 | Return 1 when any status bit in mask 0x44A7 of B1C is set |
| [`mcu_fault_monitor_update`](#mcu_fault_monitor_update) | 0x08005B3C | Main protection tick: filter the references, run threshold monitors, set hall fault bits |
| [`mcu_fault_norm_sq_debounce_check`](#mcu_fault_norm_sq_debounce_check) | 0x080062F0 | Return 0 when the squared magnitude of (+0x18, +0x1C) exceeds the limit at +0x3C |
| [`mcu_fault_owner_arbitrate`](#mcu_fault_owner_arbitrate) | 0x080061FC | Request or withdraw fault IDs in the owner byte at 0x200003BC, driven by bits of 0x20000B1C |
| [`mcu_fb_threshold_monitor`](#mcu_fb_threshold_monitor) | 0x08005AB0 | Monitor DAT_20000A40 against the A80 thresholds and mirror trips into B1C bits 0x1 and 0x2 |
| [`mcu_flag_1fce_is_clear`](#mcu_flag_1fce_is_clear) | 0x08004E64 | Return 1 if the byte at 0x20001fce is zero, else 0 |
| [`mcu_limit_ramp_update`](#mcu_limit_ramp_update) | (removed) | Update a ramped limit (halve/x1.2 on flag change, +0x1999 per call) and clamp an output |
| [`mcu_over_limit_latch_12b`](#mcu_over_limit_latch_12b) | (removed) | 12b: integrate an over-limit condition and latch fault bit 0x4 of status BD0 |
| [`mcu_speed_mismatch_check`](#mcu_speed_mismatch_check) | 0x08005A58 | Set status bit 0x4000 when DAT_20000780 is large while the command is near zero |
| [`mcu_status_bf4_any_low_bits`](#mcu_status_bf4_any_low_bits) | 0x08003624 | Return 1 if either of the low two bits of status byte 0x20000bf4 is set |
| [`mcu_threshold_debounce_init_v12b`](#mcu_threshold_debounce_init_v12b) | (removed) | Initialise a 12b threshold debounce object: thresholds, mode, counter limits, clear state |
| [`mcu_threshold_debounce_update_v12b`](#mcu_threshold_debounce_update_v12b) | (removed) | Debounce an upper and/or lower threshold with per-side counters and latched trip flags (12b) |
| [`mcu_threshold_monitor_init_std`](#mcu_threshold_monitor_init_std) | 0x080084DC | Initialise the 143/152/0160 threshold monitor object with limits, reload values and mode |
| [`mcu_threshold_monitor_update_std`](#mcu_threshold_monitor_update_std) | 0x0800844C | Update thresholds and run upper/lower trip monitor with reload counters and hysteresis (143/152/0160) |
| [`mcu_threshold_status_12b`](#mcu_threshold_status_12b) | (removed) | 12b: run the threshold debounce on A80 and mirror its trip states into status bit 0x20 |
| [`mcu_update_inhibit_latch_1fcd`](#mcu_update_inhibit_latch_1fcd) | 0x0800B2C0 | Set or clear the drive-inhibit latch at 0x20001fcd from fault flags and the value at 0x20000f30 |

## mcu_12b_supervisor_update

**12b: threshold supervisor on A68 that updates status bits 0x1 and 0x2 in AF8**

12b-only supervisor. It runs mcu_threshold_debounce_update_v12b on the object at 0x20000A68 with sample DAT_20000A28. While the upper trip state DAT_20000A7A is clear it counts DAT_200000B8 up to 4000 while DAT_20000A2C is below DAT_200003DC x 0x8000, then clears bit 0x2 of DAT_20000AF8; when the state is set it resets the count and sets bit 0x2. While the lower trip state DAT_20000A7B is set it counts DAT_200000B4 up to 1000 while DAT_20000A2C is below DAT_200003DE x 0x8000 - 0x4000; once the count is exceeded it sets DAT_20000B00 to (DAT_20000AFC > 449), sets bit 0x1 unless that holds, and clears DAT_200000B2. While the lower trip is clear it resets B4, and when DAT_20000A2C is above DAT_200003DE x 0x8000 it counts DAT_200000B2 up to 16000, then clears bit 0x1 and DAT_20000B00.

**Notes:** The limits and the meanings of DAT_20000A2C and DAT_20000AFC are 12b-specific and not established. The counter DAT_20000AFC is read as a count, as in mcu_over_limit_latch_12b.

- Addresses by version: 12b: 0x08005A80
- Called by: `mcu_0160_0800a49c`
- Calls: `mcu_bits_clear`, `mcu_bits_set`, `mcu_threshold_debounce_update_v12b`
- Confidence: medium

## mcu_a50_debounce_latch

**Latch flag DAT_20000E36 from the debounced test DAT_20000A50 above -5.0**

Feeds the test DAT_20000A50 > -0x28000 (above -5.0 in Q15) into the edge counter at 0x20000CEC and writes its output to DAT_20000E36, but only while that byte is still zero. Once set, the flag therefore stays set, since nothing in this function clears it. The threshold and the counter limit together set the debounce; both are outside this packet.

**Notes:** Meaning of DAT_20000A50 is not established.

- Addresses by version: 12b: 0x08005688, 143: 0x0800558C, 152: 0x080055F0, 0160: 0x08005690
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_edge_counter_step`
- Confidence: medium

## mcu_bus_threshold_monitor

**Monitor DAT_20000B14 against thresholds 0x3E8 and 0x3EA and mirror trips into B1C bit 0x20**

Runs mcu_threshold_monitor_update_std on the object at 0x20000A9C with sample DAT_20000B14, thresholds DAT_200003E8 (upper, also used as the release level) and DAT_200003EA (lower), each shifted left by 15, and a trailing 0. If the upper trip flag DAT_20000AB4 is set it sets bit 0x20 of the status word DAT_20000B1C, and if the lower trip flag DAT_20000AB5 is set it clears that bit and returns. The sample is the filtered value written by mcu_fault_monitor_update, and its nominal band (0x348000 to 0x370000) suggests a voltage, though that is a guess.

**Notes:** The identity of the monitored quantity is inferred from its band and from the default 0x368000 that mcu_fault_monitor_update uses for it.

- Addresses by version: 143: 0x080058F0, 152: 0x08005960, 0160: 0x08005A00
- Called by: `mcu_fault_monitor_update`
- Calls: `mcu_bits_clear`, `mcu_bits_set`, `mcu_threshold_monitor_update_std`
- Confidence: medium

## mcu_cmd_state_clear

**Clear the command-pending word and byte, release owner 10 and clear bit 0x8 of 0x20000B1C**

Sets the 32-bit word at 0x200003B8 and the byte at 0x20001FCE to zero, calls mcu_owner_release_if_match with ID 10 so the owner byte is cleared if this ID holds it, and clears bit 0x8 of the request word 0x20000B1C with mcu_bits_clear. Its only caller in this packet is mcu_can_rx_command_dispatch, which runs it at the start of each command.

- Addresses by version: 12b: 0x08007EA4, 143: 0x08007D98, 152: 0x08007E20, 0160: 0x08007DC8
- Called by: `mcu_can_rx_command_dispatch`
- Calls: `mcu_bits_clear`, `mcu_owner_release_if_match`
- Confidence: medium

## mcu_cond_mode_bit0_and_level_ok

**Return 1 if mode bit0 of 0x2000065d is set and 0x200003ea is at least 10 above both thresholds**

True when (DAT_2000065d & 1) != 0 and both signed 16-bit thresholds DAT_20000024 and DAT_20000026 are <= DAT_200003ea - 10 (a 10-count hysteresis/margin). 0x2000065d is a mode/status byte also used by mcu_0160_08004b54 (bit1) and mcu_0160_08005550 (bit2 and bits 3..4). Called from mcu_0160_08003f2c, 0800480c, 08004944, 0800a320 and 0800e238.

**Returns** `bool`: 1 if condition met

**Notes:** Operands are probably a measured value compared with two limits; unknown which.

- Addresses by version: 12b: 0x0800499C, 143: 0x08004990, 152: 0x08004A7C, 0160: 0x08004B1C
- Called by: `mcu_0160_08003f2c`, `mcu_target_derate_calc`, `mcu_0160_08004944`, `mcu_0160_0800a320`, `mcu_0160_0800e238`
- Confidence: medium

## mcu_digital_input_debounce

**Debounce digital input bytes 0x1BC and 0x1BD through a bank of edge counters**

Runs a bank of six edge counters that debounce digital inputs. DAT_20000E18 comes from counter C60 on DAT_200001BC, DAT_20000E1A (copied to E1B) from counter C74 on DAT_200001BC, DAT_20000E19 from counter C88 on that output, DAT_20000E1C from counter CC4 on DAT_200001BD, DAT_20000E20 from counter CB0 on the result of mcu_below_10pct_of_window, and DAT_20000E1F from counter D8C on DAT_20000E33 == 0. A counter output changes only after its input has been held for its limit count, so the E-bytes are debounced versions of the inputs. The call to mcu_below_10pct_of_window passes whatever is left in r0 by the mcu_get_param_654_q15 call made just before it, so its input is that parameter value.

**Notes:** Counter limits are set in the edge counter init routines, not here. The meaning of the input bytes 0x1BC and 0x1BD is not established.

- Addresses by version: 12b: 0x08005100, 143: 0x08005004, 152: 0x0800511C, 0160: 0x080051BC
- Called by: `mcu_0160_08004e78`
- Calls: `mcu_below_10pct_of_window`, `mcu_get_param_654_q15`, `mcu_edge_counter_step`
- Confidence: medium

## mcu_f30_range_latch

**Latch flag 0x2000010F from the magnitude of the s32 at 0x20000F30; argument 0 clears the latch**

An argument of 0 clears the latch byte at 0x2000010F and returns 1. Otherwise it takes the absolute value of the s32 at 0x20000F30. If that magnitude is above 0xFFFF and the latch is clear it returns 1 without changing anything. In all other cases (magnitude at most 0xFFFF, or latch already set) it sets the latch and returns 2, and the latch stays set until the caller passes 0. Called from mcu_0160_08003ab8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | 0 = clear the latch, non-zero = evaluate |

**Returns** `s32`: 1 = not latched, 2 = latched

**Notes:** The sense of the threshold looks unusual (small magnitude latches). Confirm against the caller.

- Addresses by version: 12b: 0x080065E8, 143: 0x080064B0, 152: 0x080064E0, 0160: 0x08006580
- Called by: `mcu_0160_08003ab8`
- Confidence: medium

## mcu_fault_b1c_mask_any

**Return 1 when any status bit in mask 0x44A7 of B1C is set**

Returns 1 if (DAT_20000B1C & 0x44A7) is non-zero, that is if any of bits 0, 1, 2, 5, 7, 10 or 14 of the 32-bit status word is set. That word collects status bits set by mcu_bus_threshold_monitor, mcu_fb_threshold_monitor, mcu_speed_mismatch_check and mcu_fault_monitor_update. Its only caller in the packet is mcu_drive_state_set, which uses the result to clear the transition flag.

**Returns** `bool`: 1 when any masked status bit is set

**Notes:** The meaning of the individual status bits is not established in this packet.

- Addresses by version: 12b: 0x08004CC8, 143: 0x08004CBC, 152: 0x08004DA8, 0160: 0x08004E48
- Called by: `mcu_drive_state_set`
- Calls: `mcu_bits_and`
- Confidence: medium

## mcu_fault_monitor_update

**Main protection tick: filter the references, run threshold monitors, set hall fault bits**

Protection and reference update called from mcu_0160_0800a320 that does nothing unless DAT_20000B38 is set. It reads a40 = mcu_mul_q15_f5e_by_3f2() and b10 = mcu_0160_08002148(&b18), using 0x368000 as b10 when b18 is non-zero. When DAT_200000B1 is clear it runs seven mcu_lpf_q30_step filters on their own inputs (a40 into a48 and a44, a4c into a50, a54 into a58, a5c into a60, a64 into a68, and b10 into b14) with fixed Q30 coefficients; when the flag is set it copies the samples into the filter states, sets a60 to 0x8000 and clears the flag. It then calls mcu_bus_threshold_monitor, reads the hall transition status of the context object with mcu_hall_get_transition_status, and steps two counters: AE8 on status 7 sets bit 0x400 of B1C when it fires, and AFC on statuses 1 to 6 (invalid transitions) sets bit 0x80000 when it fires.

**Notes:** Status 7 and statuses 1 to 6 follow the mcu_hall_get_transition_status summary. The 0x80000 bit is set on an invalid transition, which reads as a fault, but the counter output polarity is assumed. mcu_0160_08002148 is not described.

- Addresses by version: 143: 0x08005A2C, 152: 0x08005A9C, 0160: 0x08005B3C
- Called by: `mcu_0160_0800a320`
- Calls: `mcu_speed_from_max_u12`, `mcu_mul_q15_f5e_by_3f2`, `mcu_bits_set`, `mcu_bus_threshold_monitor`, `mcu_lpf_q30_step`, `mcu_hall_get_transition_status`, `mcu_edge_counter_step`
- Confidence: medium

## mcu_fault_norm_sq_debounce_check

**Return 0 when the squared magnitude of (+0x18, +0x1C) exceeds the limit at +0x3C**

Computes (x/8)^2 and (y/8)^2 for the s32 values x at +0x18 and y at +0x1C, shifts each product right by 15 and sums them, which is about (x^2 + y^2) / 2^21. If the sum is greater than the s32 limit at +0x3C, the counter 0x20000344 is incremented, and the function returns 0 only when the counter's previous value was above 3. Every other path clears the counter and returns 1. As written, the counter can only exceed 3 if another writer sets it, so the intended four-sample debounce does not accumulate by itself.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object with x (+0x18), y (+0x1C) and limit (+0x3C), all s32 |

**Returns** `bool`: 1 = within limit or not tripped, 0 = tripped

**Notes:** Check whether 0x20000344 is written anywhere else. The debounce logic looks incomplete or inverted.

- Addresses by version: 12b: 0x08006368, 143: 0x08006220, 152: 0x08006250, 0160: 0x080062F0
- Called by: `mcu_0160_08007364`
- Confidence: medium

## mcu_fault_owner_arbitrate

**Request or withdraw fault IDs in the owner byte at 0x200003BC, driven by bits of 0x20000B1C**

Reads the request word at 0x20000B1C and, for each bit group, either requests an ID or withdraws it. A set bit calls mcu_track_min_nonzero_u8, which keeps the smallest non-zero ID in the byte at 0x200003BC. A clear bit calls mcu_owner_release_if_match, which clears the owner byte if it holds that ID. The groups are: ID 0x18 from bit 0x1 or 0x2, ID 0x37 from 0x4, ID 0x29 from 0x20, ID 0x28 from 0x80, ID 0x12 from 0x400, and ID 0x38 from 0x4000. ID 0x0E is driven by bit 0x100 and then overwritten by bit 0x200, so bit 0x200 alone decides it. The owner byte therefore holds the most urgent active request, and withdrawing the owner leaves it at zero until another request arrives.

**Notes:** The meanings of IDs 0x0E, 0x12, 0x18, 0x28, 0x29, 0x37 and 0x38 are not known from this packet. The caller is mcu_0160_0800a320.

- Addresses by version: 12b: 0x08006274, 143: 0x0800612C, 152: 0x0800615C, 0160: 0x080061FC
- Called by: `mcu_0160_0800a320`
- Calls: `mcu_bits_and`, `mcu_owner_release_if_match`, `mcu_track_min_nonzero_u8`
- Confidence: medium

## mcu_fb_threshold_monitor

**Monitor DAT_20000A40 against the A80 thresholds and mirror trips into B1C bits 0x1 and 0x2**

Runs mcu_threshold_monitor_update_std on the object at 0x20000A80 with sample DAT_20000A40, upper DAT_200003E2 and lower DAT_200003E6 (each shifted left by 15), release DAT_200003E4 (shifted left by 15) and a trailing 0x1A000 (3.25 in Q15). Bit 0x2 of the status word DAT_20000B1C follows the upper trip state DAT_20000A98 (set when set, cleared when clear). Bit 0x1 follows the lower trip state DAT_20000A99: when it is clear, the bit is cleared and DAT_20000B24 is cleared; when it is set, the bit is set if DAT_20000B20 is below 450 and DAT_20000B24 is cleared, and otherwise DAT_20000B24 is set and the bit is left as it was. The sample DAT_20000A40 is the output of mcu_mul_q15_f5e_by_3f2 in mcu_fault_monitor_update.

**Notes:** Meaning of the monitored quantity and of DAT_20000B20 is not established.

- Addresses by version: 143: 0x080059A0, 152: 0x08005A10, 0160: 0x08005AB0
- Called by: `mcu_0160_0800a49c`
- Calls: `mcu_bits_clear`, `mcu_bits_set`, `mcu_threshold_monitor_update_std`
- Confidence: medium

## mcu_flag_1fce_is_clear

**Return 1 if the byte at 0x20001fce is zero, else 0**

Logical-not of DAT_20001fce, returned as 0/1. Callers mcu_0160_080056e4, 08008a14, 0800adf0 and 0800b10c use it as a gating condition (the byte is likely a fault/disable flag). Highly likely 'not faulted/enabled' semantics, but unproven.

**Returns** `bool`: 1 if DAT_20001fce == 0

**Notes:** Name chosen neutrally; byte meaning unknown.

- Addresses by version: 12b: 0x08004CE4, 143: 0x08004CD8, 152: 0x08004DC4, 0160: 0x08004E64
- Called by: `mcu_run_enable_update`, `mcu_0160_08008a14`, `mcu_cmd_ramp_update`, `mcu_0160_0800b10c`
- Confidence: medium

## mcu_limit_ramp_update

**Update a ramped limit (halve/x1.2 on flag change, +0x1999 per call) and clamp an output**

Works on a control object: byte flag at +0xbc (current limiting/fault request), byte at +0xbd (previous flag state) and the int limit state at +0xa0. On a 0->1 edge of the flag the stored limit is halved; on a 1->0 edge it is multiplied by 0x9999/0x8000 (about 1.2, Q15). The previous flag is then updated. If the flag is clear, the limit is raised by 0x1999 (about 0.2 in Q15) per call but not above the ceiling param_2 and stored back; if the flag is set the working limit is 0. When param_4 is non-zero the limit is applied to *param_3 as *param_3 = min(*param_3, limit) (so a set flag forces it to 0 or below) and the function returns 1 if the flag is set, else 0. Only present in the 12b build; later builds restructured it (see the plain getter mcu_152_08002a18 / mcu_0160_08002a20 neighbours).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | control object (fields at +0xa0 limit, +0xbc flag, +0xbd previous flag) |
| `param_2` | `s32` | upper ceiling for the ramped limit |
| `param_3` | `ptr` | in/out command (s32) clamped by the limit |
| `param_4` | `s32` | non-zero to apply the limit to *param_3 |

**Returns** `bool`: 1 if clamping was applied while the flag is set, else 0

**Notes:** Interpretation as a current/torque derating limit is a guess from structure; no direct callers (indirect or inlined).

- Addresses by version: 12b: 0x080029CE
- Called by: `mcu_0160_08003f2c`
- Confidence: medium

## mcu_over_limit_latch_12b

**12b: integrate an over-limit condition and latch fault bit 0x4 of status BD0**

12b-only supervisor for one over-limit condition. It takes a measurement from FUN_08004970 (no summary in this packet) and debounces the test measurement > DAT_20000BCC x 0x8000 through FUN_080096F8 on the object at 0x20000D40. Bit 0x2 of DAT_20000BD0 follows the debounced result, and DAT_20000144 integrates it: it counts up while bit 0x2 is set and latches bit 0x4 once it reaches 201, and counts down otherwise. A window timer DAT_20000140 runs for 200 ticks after DAT_20000B9F is set, and while it runs a measurement above (DAT_20000BC8 + 1) x 0x8000 sets bits 0x2 and 0x4 and ends the window. Bit 0x1 is cleared when FUN_080036F8 returns non-zero and DAT_20000AFC is above 99.

**Notes:** Which real condition this guards, and what FUN_08004970, FUN_080096F8 and FUN_080036F8 do, are not in the packet, so the name is generic. These three callees are not in the packet's callee list.

- Addresses by version: 12b: 0x08004E74
- Called by: `mcu_fb_lpf_select_update`
- Calls: `mcu_below_10pct_of_window`, `mcu_get_param_654_q15`, `mcu_edge_counter_step`
- Confidence: medium

## mcu_speed_mismatch_check

**Set status bit 0x4000 when DAT_20000780 is large while the command is near zero**

Counts the condition that |DAT_20000780| is above 0x1DFFFF (about 60.0 in Q15) while |DAT_20000F30| is below 0x8000 (1.0). The condition is debounced by edge counter AD4 and, when that counter fires, bit 0x4000 of the status word DAT_20000B1C is set with mcu_bits_set. The meaning of DAT_20000780 is not established, so the name describes the test rather than a known fault.

**Notes:** Name describes the test only. The fault meaning of bit 0x4000 is inferred.

- Addresses by version: 12b: 0x08005A28, 143: 0x08005948, 152: 0x080059B8, 0160: 0x08005A58
- Called by: `mcu_0160_0800a480`
- Calls: `mcu_bits_set`, `mcu_edge_counter_step`
- Confidence: low

## mcu_status_bf4_any_low_bits

**Return 1 if either of the low two bits of status byte 0x20000bf4 is set**

Normalises (DAT_20000bf4 & 3) to a boolean. The byte is a state/fault bitfield; callers are the main control routines mcu_0160_08003f2c, 080052bc and 08005978. Which conditions bits 0 and 1 stand for is unknown.

**Returns** `bool`: 1 if bit0 or bit1 set, else 0

**Notes:** Bit semantics unknown.

- Addresses by version: 12b: 0x080036E4, 143: 0x080035E4, 152: 0x08003584, 0160: 0x08003624
- Called by: `mcu_0160_08003f2c`, `mcu_drive_state_update`, `mcu_drive_state_set`
- Confidence: medium

## mcu_threshold_debounce_init_v12b

**Initialise a 12b threshold debounce object: thresholds, mode, counter limits, clear state**

Writes the upper threshold (param_2) at +0x00 and lower threshold (param_3) at +0x04, the upper and lower counter limits (param_4 at +0x0E, param_5 at +0x10) as halfwords, and the mode byte (param_6) at +0x08. The up and down counters at +0x0A and +0x0C, the state and latch bytes +0x12, +0x13, +0x14 and +0x15 are all cleared. Returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | threshold debounce object |
| `param_2` | `s32` | upper threshold |
| `param_3` | `s32` | lower threshold |
| `param_4` | `u16` | upper counter limit |
| `param_5` | `u16` | lower counter limit |
| `param_6` | `u8` | mode: 0 upper only, 1 lower only, 2 both |

**Returns** `bool`: always 1

**Notes:** Only caller in this packet's scope: mcu_12b_08005c80.

- Addresses by version: 12b: 0x0800829E
- Called by: `mcu_12b_08005c80`
- Confidence: high

## mcu_threshold_debounce_update_v12b

**Debounce an upper and/or lower threshold with per-side counters and latched trip flags (12b)**

Control object: upper threshold word at +0x00, lower at +0x04, mode byte at +0x08 (0 = upper only, 1 = lower only, 2 = both), counters at +0x0A (upper) and +0x0C (lower) as halfwords with limits at +0x0E and +0x10, state bytes +0x12 and +0x13, latched flags +0x14 and +0x15. For the upper side, each sample above the threshold increments the counter until it reaches its limit, which latches the trip (+0x12 and +0x14 set to 1); a sample at or below the threshold decrements the counter, and when it is already zero clears +0x12. The lower side works the same with samples below the lower threshold and state bytes +0x13 and +0x15. The function always returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | threshold debounce object (layout above) |
| `param_2` | `s32` | current sample |

**Returns** `bool`: always 1

**Notes:** Only in the 12b build. The thresholds' physical meaning (for example over-current or over-temperature) is not shown here.

- Addresses by version: 12b: 0x0800822A
- Called by: `mcu_threshold_status_12b`, `mcu_12b_supervisor_update`
- Confidence: high

## mcu_threshold_monitor_init_std

**Initialise the 143/152/0160 threshold monitor object with limits, reload values and mode**

Writes the mode byte (param_8) at +0x08, thresholds param_2 at +0x00 and param_3 at +0x04, counter A limit param_4 at +0x0E, reload value param_5 at +0x10, counter B limit param_6 at +0x12 and reload value param_7 (word) at +0x14. The counters at +0x0A and +0x0C and the flag and latch bytes +0x18, +0x19, +0x1A and +0x1B are cleared. Returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | threshold monitor object |
| `param_2` | `s32` | upper threshold |
| `param_3` | `s32` | lower threshold |
| `param_4` | `u16` | counter A limit |
| `param_5` | `u16` | counter A reload value |
| `param_6` | `u16` | counter B limit |
| `param_7` | `u32` | counter B reload value |
| `param_8` | `u8` | mode: 0 upper only, 1 lower only, 2 both |

**Returns** `bool`: always 1

**Notes:** Only caller: mcu_0160_08005c0c.

- Addresses by version: 143: 0x080083D4, 152: 0x080084C4, 0160: 0x080084DC
- Called by: `mcu_0160_08005c0c`
- Confidence: high

## mcu_threshold_monitor_update_std

**Update thresholds and run upper/lower trip monitor with reload counters and hysteresis (143/152/0160)**

Stores the new thresholds param_3 at +0x00 and param_4 at +0x04. Upper side (mode byte +0x08 equal to 0 or 2): a sample above the upper threshold increments counter A at +0x0A up to its limit at +0x0E; at the limit the trip flag +0x18 and latch +0x1A are set and counter A is reloaded from +0x10. A sample at or below the release level param_5 decrements the counter and clears +0x18 when it is zero. Lower side (mode 1 or 2): a sample below +0x04 increments counter B at +0x0C up to its limit at +0x12; at the limit flag +0x19 and latch +0x1B are set and counter B is reloaded from +0x14. A sample at or above (+0x04 + param_6 hysteresis) decrements counter B and clears +0x19 at zero. Returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | monitor object (layout above) |
| `param_2` | `s32` | current sample |
| `param_3` | `s32` | new upper threshold |
| `param_4` | `s32` | new lower threshold |
| `param_5` | `s32` | upper release level |
| `param_6` | `s32` | lower hysteresis width |

**Returns** `bool`: always 1

**Notes:** The protected quantity is not identified in this packet. Callers mcu_0160_08005a00 and mcu_0160_08005ab0 are outside this packet.

- Addresses by version: 143: 0x08008344, 152: 0x08008434, 0160: 0x0800844C
- Called by: `mcu_bus_threshold_monitor`, `mcu_fb_threshold_monitor`
- Confidence: high

## mcu_threshold_status_12b

**12b: run the threshold debounce on A80 and mirror its trip states into status bit 0x20**

12b-only wrapper. It runs mcu_threshold_debounce_update_v12b on the object at 0x20000A80 with sample DAT_20000AF0. If the upper trip state byte DAT_20000A92 is set it sets bit 0x20 of the status word DAT_20000AF8 with mcu_bits_set; if the lower trip state byte DAT_20000A93 is set it clears that bit with mcu_bits_clear and returns, so the bit ends cleared when both are set. The caller listed is mcu_12b_08005b60, which is not in this packet.

**Notes:** Trip state byte meanings follow the mcu_threshold_debounce_update_v12b summary.

- Addresses by version: 12b: 0x080059EC
- Called by: `mcu_sensor_filter_tick_v12b`
- Calls: `mcu_bits_clear`, `mcu_bits_set`, `mcu_threshold_debounce_update_v12b`
- Confidence: high

## mcu_update_inhibit_latch_1fcd

**Set or clear the drive-inhibit latch at 0x20001fcd from fault flags and the value at 0x20000f30**

Recomputes a one-byte latch at 0x20001fcd, where 1 means inhibit and 0 means allowed. The allow predicate is: (bit 2 of byte 0x20001fd4 is clear, or (bytes 0x20001fd2 and 0x20001fd3 are both zero and (bit 2 of 0x20001fe2 is clear or 0x20000f30 < 0x28001))) AND (flag 0x20000e32 is zero or 0x20000f30 < 0x10000). If the predicate is false the latch is set to 1. If it is true and 0x20000f30 < 0x10000 the latch is cleared to 0; if it is true and the value is at or above 0x10000 the latch is left unchanged. Flag 0x20000e32 is the one set by mcu_update_flag_e32_from_mode_3 (mode byte equal to 3).

**Notes:** The constants 0x10000 (1.0 in Q16) and 0x28001 (just above 2.5 in Q16) suggest 0x20000f30 is a Q16 quantity such as speed, voltage or current; not confirmed. The individual flags at 0x20001fd2 to 0x20001fe2 are unknown.

- Addresses by version: 12b: 0x0800B054, 143: 0x0800B2E4, 152: 0x0800B260, 0160: 0x0800B2C0
- Called by: `mcu_0160_0800a320`
- Confidence: medium
