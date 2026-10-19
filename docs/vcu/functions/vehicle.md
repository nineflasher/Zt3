# VCU - `vehicle` functions

25 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`app_apply_mode_limits`](#app_apply_mode_limits) | 0x080017E8 | Load 16-bit parameter pairs into the config block according to the mode in 0x20001fa7 |
| [`vcu_angle_deg_calc_legacy`](#vcu_angle_deg_calc_legacy) | (removed) | Compute (a*360)/b into a 16-bit angle value, 0 if b <= 0 (VCU_148/14a only) |
| [`vcu_angle_deg_update`](#vcu_angle_deg_update) | 0x08008DEC | Recompute angle = counter*360/period when the counter changed; 0 when period <= 0 |
| [`vcu_aux_flags_reset`](#vcu_aux_flags_reset) | 0x080054B4 | Zero five auxiliary state bytes (DAT_20002028, 2023, 2022, 200021be, 200021bb) |
| [`vcu_chan_mask_update`](#vcu_chan_mask_update) | 0x0800AA9C | Set or clear the flag for channel 0..9 in a set of byte bitmasks at 0x200021ce |
| [`vcu_clear_flag_bits_9_11`](#vcu_clear_flag_bits_9_11) | 0x080054A4 | Clear bits 9..11 of the 16-bit flag word DAT_20001f98 |
| [`vcu_condition_b_latch_flags`](#vcu_condition_b_latch_flags) | 0x0800339C | Set or clear flag bit 2 of DAT_20001aec and DAT_20001875 from status bits |
| [`vcu_cycle_mode_on_request`](#vcu_cycle_mode_on_request) | 0x08003BF0 | On a request flag, step a 3-state selector and map it to DAT_20001b94 |
| [`vcu_debounce_condition_a`](#vcu_debounce_condition_a) | 0x0800332C | Up/down debounce counter (limit 20) that drives the output flag DAT_20001f69 |
| [`vcu_event_countdown_a`](#vcu_event_countdown_a) | 0x08003B00 | Countdown timer reloaded on input change; sets DAT_20001fb4 on expiry |
| [`vcu_event_countdown_b`](#vcu_event_countdown_b) | 0x08003B74 | Countdown timer reloaded on event latch change; sets DAT_20001fd4 at expiry |
| [`vcu_input_b_hold_start_tick`](#vcu_input_b_hold_start_tick) | 0x08009094 | Hold-to-start sequencer driven by input B reaching its long-hold state 3 |
| [`vcu_latch_event_flags_a`](#vcu_latch_event_flags_a) | (removed) | One-shot: set bit0 then bit1 of DAT_20001a7a, setting bit 11 of DAT_20001a38/20001a36 |
| [`vcu_latch_event_flags_b`](#vcu_latch_event_flags_b) | 0x0800691C | One-shot: set bits 0..2 of DAT_20001b32 and the matching flags in aee/af0/b12 |
| [`vcu_level_hold_latch`](#vcu_level_hold_latch) | (removed) | Latch flag 0x200021B4 after ten consecutive ticks at or above 60 in the value shifted right by 4 |
| [`vcu_periodic_100_tick_check`](#vcu_periodic_100_tick_check) | 0x08003400 | Every 100 calls of the counter DAT_2000102c, raise DAT_20001fc0 if conditions hold |
| [`vcu_ready_sequence_step_v148_14a`](#vcu_ready_sequence_step_v148_14a) | (removed) | Ready/arm/run/disarm state machine for builds 148 and 14a |
| [`vcu_ready_sequence_step_v14b_0159`](#vcu_ready_sequence_step_v14b_0159) | 0x08002FC0 | Ready/arm/run/disarm state machine for builds 14b to 0159 |
| [`vcu_sensor_limit_derate_eval`](#vcu_sensor_limit_derate_eval) | 0x08003594 | Evaluate three scaled sensor words into limit flags and the derate word DAT_20001f90 |
| [`vcu_speed_mode_snapshot_update`](#vcu_speed_mode_snapshot_update) | 0x08008CC0 | Per-tick speed conversion, drive sub-mode selection and periodic telemetry snapshot |
| [`vcu_state_params_reset`](#vcu_state_params_reset) | 0x0800837C | Reset the packed state words at 0x20001f8c and load default 0x2800/0x3200 limit and 0xF00 base |
| [`vcu_status_flags_mask_low`](#vcu_status_flags_mask_low) | 0x08007CFC | Clear the low 12 bits of two 16-bit status/limit words at 0x20001f92 and 0x20001f98 |
| [`vcu_timebase_100_tick`](#vcu_timebase_100_tick) | 0x0800900C | Divide-by-100 prescaler that advances four saturating elapsed-time counters |
| [`vcu_toggle_special_mode`](#vcu_toggle_special_mode) | 0x08004F74 | Toggle mode byte DAT_20001fa4 between its current value and the special value 4 |
| [`vcu_wheel_odometer_limit_update`](#vcu_wheel_odometer_limit_update) | 0x08009080 | Accumulate wheel angle and revolutions, then compute the drive output limit |

## app_apply_mode_limits

**Load 16-bit parameter pairs into the config block according to the mode in 0x20001fa7**

Switch on the byte DAT_20001fa7 (modes 0..6, other values use the default). Every mode writes DAT_20001b38 = 3, DAT_20001b3a = DAT_20001b3c = 0x0505 (5,5), a pair 0x140F (20,15) or 0x190F (25,15) into DAT_20001b3e and DAT_20001b42, and a second pair into DAT_20001b40 and DAT_20001b44: 0x1919 (25,25) for modes 0 and 5/default, 0x1414 (20,20) for mode 2, 0x2828 (40,40) for mode 3, 0x2020 (32,32) for modes 4 and 6, and for mode 1 either 0x2020 or 0x1919 depending on bit 4 of DAT_20001b32. It also adjusts flag bits in DAT_20001aee: bit 3 (0x0008) is set only in mode 3 and cleared otherwise, and bit 12 (0x1000) is cleared in all modes except 0, 3, 4 and 6. Appears to select per-ride-mode limit/threshold pairs (byte pairs, units unknown); called from vcu_0159_08009da8 and vcu_0159_0800b294.

**Notes:** Mapping of mode numbers to ride modes and the physical meaning of the byte pairs are unconfirmed.

- Addresses by version: 148: 0x0800148C, 14a: 0x0800148C, 14b: 0x08001734, 14e: 0x08001734, 14f: 0x08001790, 152: 0x080017CC, 153: 0x080017CC, 0159: 0x080017E8
- Called by: `vcu_0159_08009da8`, `vcu_runtime_defaults_init`
- Confidence: medium

## vcu_angle_deg_calc_legacy

**Compute (a*360)/b into a 16-bit angle value, 0 if b <= 0 (VCU_148/14a only)**

If DAT_20001ac8 > 0, stores (DAT_20001ac4 * 360) / DAT_20001ac8 as a 16-bit value in DAT_20001ace; otherwise stores 0. This is the old-version counterpart of vcu_angle_deg_update (0x08008dec): a numerator/denominator ratio scaled to degrees. No direct caller (likely called indirectly or inlined in the older builds). Probably a position or phase angle derived from a count and a period.

**Notes:** What the two counters measure (hall/pulse timing, steering, wheel angle) is unknown.

- Addresses by version: 148: 0x08008374, 14a: 0x080087E4
- Called by: `vcu_wheel_odometer_limit_update`
- Confidence: low

## vcu_angle_deg_update

**Recompute angle = counter*360/period when the counter changed; 0 when period <= 0**

If DAT_20001b88 (period/denominator, maintained by vcu_timebase_100_tick) is positive and DAT_20001b84 differs from the cached copy DAT_2000137c, the cache is refreshed and DAT_20001b8e (16-bit) = DAT_20001b84 * 360 / DAT_20001b88, i.e. a fraction of a full cycle in degrees. If the period is not positive, DAT_20001b8e is set to 0. Called from the periodic routine 0x08009080 together with vcu_timebase_100_tick. Newer-build counterpart of vcu_angle_deg_calc_legacy.

**Notes:** The physical quantity (rotor/phase angle, pedal or wheel position) is not determinable from this function.

- Addresses by version: 14b: 0x08008B84, 14e: 0x08008BC4, 14f: 0x08008C20, 152: 0x08008CE4, 153: 0x08008D80, 0159: 0x08008DEC
- Called by: `vcu_wheel_odometer_limit_update`
- Confidence: low

## vcu_aux_flags_reset

**Zero five auxiliary state bytes (DAT_20002028, 2023, 2022, 200021be, 200021bb)**

Stores 0 to DAT_20002028, DAT_20002023, DAT_20002022, DAT_200021be and DAT_200021bb in that order. Called only from vcu_0159_0800a39c alongside vcu_error_state_reset and vcu_warning_state_reset, so it is a state-clear helper of the same reset event.

**Notes:** Meaning of the five variables is unknown.

- Addresses by version: 148: 0x08004BAC, 14a: 0x08004F38, 14b: 0x0800523C, 14e: 0x08005274, 14f: 0x080052D0, 152: 0x08005330, 153: 0x08005348, 0159: 0x080054B4
- Called by: `vcu_0159_0800a39c`
- Confidence: low

## vcu_chan_mask_update

**Set or clear the flag for channel 0..9 in a set of byte bitmasks at 0x200021ce**

For param_2 != 0 sets, for param_2 == 0 clears: channel 0 -> bit 0 of DAT_200021cf; channels 1..8 -> bit (n-1) in both DAT_200021ce and DAT_200021d0; channel 9 -> bit 0 of DAT_200021d1. Values >= 10 do nothing. The doubled ce/d0 masks suggest a live mask plus a shadow/pending copy. Called from 0x0800be64.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | channel 0..9 |
| `param_2` | `s32` | 0 = clear, non-zero = set |

**Notes:** Purpose unknown (input/output enable mask, key/button bits, lamp flags?).

- Addresses by version: 148: 0x08009B14, 14a: 0x08009FF0, 14b: 0x0800A478, 14e: 0x0800A50C, 14f: 0x0800A648, 152: 0x0800A8C8, 153: 0x0800A9BC, 0159: 0x0800AA9C
- Called by: `vcu_channel_sweep_animation`
- Confidence: low

## vcu_clear_flag_bits_9_11

**Clear bits 9..11 of the 16-bit flag word DAT_20001f98**

Performs DAT_20001f98 &= 0xF1FF, clearing the three-bit field at bits 9-11. Part of the group of clear/reset helpers called together from vcu_0159_0800a39c. DAT_20001f8c is address-taken nearby so f98 is probably a member of a status structure.

**Notes:** Field meaning unknown.

- Addresses by version: 148: 0x08004B9C, 14a: 0x08004F28, 14b: 0x0800522C, 14e: 0x08005264, 14f: 0x080052C0, 152: 0x08005320, 153: 0x08005338, 0159: 0x080054A4
- Called by: `vcu_0159_0800a39c`
- Confidence: low

## vcu_condition_b_latch_flags

**Set or clear flag bit 2 of DAT_20001aec and DAT_20001875 from status bits**

Companion of vcu_debounce_condition_a. If bit6 of DAT_20001e68 is set, DAT_20001b62 < 10, bit0 of DAT_20001f78 is clear and bit3 of DAT_20001e6a is set, it ORs 4 into the flag word DAT_20001aec and sets DAT_20001875 to 1. If instead bit6 of e68 is clear or bit3 of e6a is clear it clears bit 2 of aec (AND 0xFFFB) and clears DAT_20001875. In all other cases the state is left unchanged (latching behaviour). No counter is involved, so the change is immediate.

**Notes:** Semantics of the individual bits are not known.

- Addresses by version: 148: 0x08002E40, 14a: 0x08002F30, 14b: 0x08003240, 14e: 0x08003240, 14f: 0x0800329C, 152: 0x08003308, 153: 0x08003328, 0159: 0x0800339C
- Called by: `vcu_0159_0800a15c`, `vcu_0159_0800a1d0`, `vcu_0159_0800a4e8`, `vcu_0159_0800a500`
- Confidence: medium

## vcu_cycle_mode_on_request

**On a request flag, step a 3-state selector and map it to DAT_20001b94**

When the request flag DAT_20001f75 is nonzero it is cleared and the selector DAT_2000135c (0,1,2) is mapped to the output DAT_20001b94 as 0 -> 2, 1 -> 1, 2 -> 0, then the selector is incremented and wrapped back to 0 after 2. So each request cycles through three values, in the order 2, 1, 0 for the output. Looks like a three-level setting (e.g. riding/speed mode or light level) toggled by a button press; called from the main handlers vcu_0159_0800a15c and 0800a1d0.

**Notes:** What DAT_20001b94 controls (speed mode / light level) is unverified.

- Addresses by version: 148: 0x08003548, 14a: 0x08003760, 14b: 0x08003A84, 14e: 0x08003A84, 14f: 0x08003AE0, 152: 0x08003B44, 153: 0x08003B64, 0159: 0x08003BF0
- Called by: `vcu_0159_0800a15c`, `vcu_0159_0800a1d0`
- Confidence: medium

## vcu_debounce_condition_a

**Up/down debounce counter (limit 20) that drives the output flag DAT_20001f69**

Part of a family of small per-tick condition/flag helpers (see vcu_condition_b_latch_flags) called from the main loop handlers. When DAT_20001b62 < 10 (likely a speed value), bit0 of status word DAT_20001f78 is clear and bit3 of DAT_20001f78 or of DAT_20001e6a is set, the saturating counter DAT_20001880 is incremented; once it has reached 0x14 (20 calls) DAT_20001f69 is set to 1. Otherwise, when bit3 of DAT_20001f78 or bit3 of DAT_20001e6a is clear, the counter is decremented and DAT_20001f69 is cleared when it is already 0. This gives hysteresis so the flag only changes after about 20 consecutive calls.

**Notes:** Meaning of the status bits (f78 bit0/bit3, e6a bit3) and of b62 as speed is unknown; the decompiled OR/AND mixture of the bit tests is reproduced literally.

- Addresses by version: 148: 0x08002DD0, 14a: 0x08002EC0, 14b: 0x080031D0, 14e: 0x080031D0, 14f: 0x0800322C, 152: 0x08003298, 153: 0x080032B8, 0159: 0x0800332C
- Called by: `vcu_0159_0800a15c`, `vcu_0159_0800a1d0`, `vcu_0159_0800a500`, `vcu_0159_0800a55c`, `vcu_0159_0800a5c8`
- Confidence: medium

## vcu_event_countdown_a

**Countdown timer reloaded on input change; sets DAT_20001fb4 on expiry**

One of a group of countdown helpers (see vcu_event_countdown_b). If DAT_20001f48 is 0 and DAT_20001b62 < 30: when DAT_200021b5 == 3 it sets DAT_20001fb4 = 1; when the event latch DAT_20001fbc differs from the remembered copy DAT_2000134c, it copies it into 134c, clears fbc and reloads the countdown DAT_20001fac with param_1. A nonzero countdown is decremented each call and when it reaches 0 sets DAT_20001fb4 = 1. If the guard fails, the countdown is zeroed and DAT_200021b5 is cleared if it was 3. At the end a pending latch value of 1 in fbc is cleared. param_1 is the timeout in calls.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | countdown reload value in calls (timeout) |

**Notes:** DAT_20001fbc looks like a shared change/event latch (button or input edge) but its source is unknown.

- Addresses by version: 148: 0x08003454, 14a: 0x0800366C, 14b: 0x08003990, 14e: 0x08003990, 14f: 0x080039EC, 152: 0x08003A54, 153: 0x08003A74, 0159: 0x08003B00
- Called by: `vcu_0159_0800a15c`, `vcu_0159_0800a1d0`, `vcu_0159_0800a264`, `vcu_0159_0800a55c`
- Confidence: medium

## vcu_event_countdown_b

**Countdown timer reloaded on event latch change; sets DAT_20001fd4 at expiry**

Sibling of vcu_event_countdown_a. When the latch DAT_20001fbc differs from the stored copy DAT_2000134d it copies it, clears the latch, reloads the 16-bit countdown DAT_20001fd2 with param_1 and, if DAT_20001fd4 was 1, clears DAT_20001fd4 and DAT_200021b8. Then, while the countdown is nonzero it decrements it and sets DAT_20001fd4 = 1 when it reaches 0; if it is already 0 it re-arms it with param_1. Effectively a repeating timer whose expiry flag is DAT_20001fd4.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s16` | countdown reload value in calls |

**Notes:** Purpose of DAT_200021b8 and the consumer of fd4 not identified.

- Addresses by version: 148: 0x080034CC, 14a: 0x080036E4, 14b: 0x08003A08, 14e: 0x08003A08, 14f: 0x08003A64, 152: 0x08003AC8, 153: 0x08003AE8, 0159: 0x08003B74
- Called by: `vcu_0159_0800a500`
- Confidence: medium

## vcu_input_b_hold_start_tick

**Hold-to-start sequencer driven by input B reaching its long-hold state 3**

Runs only while status bits aec[11] and aee[12] are set and DAT_20001b68 equals the sub-mode DAT_20001fa4; otherwise it clears status bit f92[1], DAT_2000139a and DAT_20001d0a. Inside the gate, DAT_2000139a is a three-state machine: state 0 (idle) enters state 1 when input B (DAT_200021c1) is 3, status bit f92[2] is set, DAT_20001f50 is nonzero and the speed is above 59 and at most 10*(DAT_20001b44>>8)+15; it also sets f92[1]. State 1 (armed) moves to state 2 when f78[2] is set, calling app_set_state(4) and recording the low byte of DAT_20001f90, and it times out back to 0 after 300 ticks. State 2 (running) watches for speed or throttle-byte changes and returns to state 0 through app_set_state(1) when DAT_20001f4f is set or a stop condition holds. DAT_2000123d is a cancel request that clears input B's state 3.

**Notes:** The inputs f78[2], f50, f4f and the throttle-like byte DAT_20001f90 are not named in the packet. The 59/300/10-tick constants are read from the decompile.

- Addresses by version: 148: 0x0800859C, 14a: 0x08008A28, 14b: 0x08008DF8, 14e: 0x08008E5C, 14f: 0x08008EB8, 152: 0x08008F7C, 153: 0x08009018, 0159: 0x08009094
- Called by: `vcu_0159_0800a15c`, `vcu_0159_0800a1d0`
- Calls: `app_set_state`
- Confidence: medium

## vcu_latch_event_flags_a

**One-shot: set bit0 then bit1 of DAT_20001a7a, setting bit 11 of DAT_20001a38/20001a36**

If bit0 of the latch byte DAT_20001a7a is clear it sets it and ORs 0x800 into the flag word DAT_20001a38; if bit1 is clear it sets it and ORs 0x800 into DAT_20001a36. So each flag word gets bit 11 set exactly once, guarded by a latch. The duplicated test in the decompilation is an artifact of an atomic/exclusive access. Older-build (148..14f) counterpart of vcu_latch_event_flags_b; no direct callers (invoked indirectly).

**Notes:** The meaning of bit 11 of these words is unknown.

- Addresses by version: 148: 0x08005EEC, 14a: 0x0800630C, 14b: 0x0800667C, 14e: 0x080066B4, 14f: 0x08006710
- Called by: `vcu_0159_0800d858`
- Confidence: low

## vcu_latch_event_flags_b

**One-shot: set bits 0..2 of DAT_20001b32 and the matching flags in aee/af0/b12**

Three independent latches in DAT_20001b32. If bit0 is clear it sets it and ORs 0x800 into DAT_20001af0; if bit1 is clear it sets it and ORs 0x800 into DAT_20001aee; if bit2 is clear it sets it and ORs 2 into DAT_20001b12. The duplicate tests are decompiler artifacts. Newer-build (152/153/0159) version of vcu_latch_event_flags_a with an additional third latch. Called from vcu_0159_0800d858.

**Notes:** The meaning of the flag bits is unknown; it might be a one-time announcement/feature-present flag.

- Addresses by version: 152: 0x08006790, 153: 0x0800682C, 0159: 0x0800691C
- Called by: `vcu_0159_0800d858`
- Confidence: low

## vcu_level_hold_latch

**Latch flag 0x200021B4 after ten consecutive ticks at or above 60 in the value shifted right by 4**

Takes the 16-bit value from app_get_u16_2000329e and shifts it right by 4. While the shifted value is at least 60, counter DAT_200014be counts consecutive calls, and once the count passes 9 (the tenth call) it sets DAT_200021b4 to 1 and holds the counter. When the shifted value is below 60, both the counter and DAT_200021b4 are cleared at once.

**Notes:** The unit of the 16-bit value is not established; a shift of 4 suggests a 12-bit ADC or a count scaled by 16. Callers are not in this packet.

- Addresses by version: 148: 0x080073FC, 14a: 0x08007838, 14b: 0x08007B9C, 14e: 0x08007BD4, 14f: 0x08007C30, 152: 0x08007CF4, 153: 0x08007D90
- Called by: `vcu_0159_080069b4`
- Calls: `app_get_u16_2000329e`
- Confidence: medium

## vcu_periodic_100_tick_check

**Every 100 calls of the counter DAT_2000102c, raise DAT_20001fc0 if conditions hold**

DAT_2000102c is a free-running tick counter incremented elsewhere (the access is flagged as address-taken/RW). When it reaches 100 it is reset to 0 and, if bit6 of DAT_20001e68 and bit4 of DAT_20001af2 are both set, or DAT_2000123e equals 6, the request flag DAT_20001fc0 is set to 1 (consumed elsewhere). Below 100 nothing happens. Acts as a 100-period timed event generator.

**Notes:** Tick period (and whether 0x123e is a state/mode byte) not determined.

- Addresses by version: 148: 0x08002E9C, 14a: 0x08002F90, 14b: 0x080032A4, 14e: 0x080032A4, 14f: 0x08003300, 152: 0x0800336C, 153: 0x0800338C, 0159: 0x08003400
- Called by: `vcu_0159_08009fa4`, `vcu_0159_0800a55c`, `vcu_0159_0800a5c8`
- Confidence: medium

## vcu_ready_sequence_step_v148_14a

**Ready/arm/run/disarm state machine for builds 148 and 14a**

Tick handler for a ready-to-run sequence with a quiet timer, an arm step, a 250-tick confirm, a run phase and a disarm. Counter DAT_200013a6 counts ticks while input flag DAT_20001e8f is low and sub-state DAT_20001c38 is clear, and latches DAT_2000138b once it passes 100. The arm test needs DAT_20001e90 and DAT_20001e8f high, DAT_2000138a clear, DAT_20001aa2 below 10, DAT_20001f11 clear, status DAT_20001a2e bit 10 set, mode byte DAT_20001ee4 equal to 3, DAT_20001da6 / 100 above 30, DAT_20001f12 clear and DAT_2000138b set; then sub-state DAT_20001c3c becomes 10 and a confirm counter runs to 250. At the end of the confirm, if DAT_20001a2c bit 11 or DAT_20001a2e bit 10 is clear, or DAT_2000123b is nonzero, it aborts (sub-state 9, flags cleared, app_set_state(1), DAT_20001c54 cleared); otherwise it sets DAT_2000138a and DAT_20001389, calls app_set_state(4) and goes to sub-state 13. When DAT_20001e90 and DAT_20001e8f both fall with DAT_2000138a set, it enters the run phase (DAT_20001f11 and DAT_20001c54 set, bit 7 of DAT_20001ed2 set); the run phase uses sub-state 12 while DAT_20001ed0 is at least 180, leaves when DAT_20001a84 high byte minus 5 is at most DAT_20001aa2 / 10 or after 1000 ticks, and disarms when DAT_200013ac passes 100 with DAT_20001e8f high, DAT_200013aa passes 3000 with DAT_20001e90 low, or DAT_20001ee4 is not 3.

**Notes:** Same logic as vcu_ready_sequence_step_v14b_0159 with the RAM relocated for this build, so the two form one group (arming state machine). In this build the app_set_state call appears as FUN_080017f4, which the family map places at the app_set_state address of VCU_14a. Input flags DAT_20001e8f and DAT_20001e90 are unnamed.

- Addresses by version: 148: 0x08002B2C, 14a: 0x08002BB0
- Called by: `vcu_0159_0800a1d0`
- Calls: `app_set_state`
- Confidence: medium

## vcu_ready_sequence_step_v14b_0159

**Ready/arm/run/disarm state machine for builds 14b to 0159**

Tick handler for the same ready-to-run sequence as vcu_ready_sequence_step_v148_14a, using the RAM of builds 14b to 0159: quiet counter DAT_200013a8 with latch DAT_2000138f, arm flag DAT_2000138e, sub-state DAT_20001cfc (9 idle, 10 arming, 12 run, 13 armed), run flag DAT_20001fd5, confirm counter DAT_200013aa and run timer DAT_200013a6. The arm test uses mode byte DAT_20001fa4 equal to 3 and the same ready conditions, and the confirm, abort and disarm steps match the other build. The run phase tests the byte DAT_20001f90 low byte against 180 and the derate flags DAT_20001f50 and DAT_20001f4f from vcu_sensor_limit_derate_eval. It also sets DAT_20001d14 while armed, DAT_20001fd9 when a restart is requested, and bit 7 of DAT_20001f92 while the sequence is armed, and app_set_state(4) on arming and app_set_state(1) on abort or disarm.

**Notes:** Twin of vcu_ready_sequence_step_v148_14a: same logic with different RAM and the mode byte at DAT_20001fa4 rather than DAT_20001ee4. Callers are not in this packet. DAT_20001fd9 is used as a restart request by vcu_standby_entry_timer.

- Addresses by version: 14b: 0x08002E68, 14e: 0x08002E68, 14f: 0x08002EC4, 152: 0x08002F30, 153: 0x08002F4C, 0159: 0x08002FC0
- Called by: `vcu_0159_0800a1d0`
- Calls: `app_set_state`
- Confidence: medium

## vcu_sensor_limit_derate_eval

**Evaluate three scaled sensor words into limit flags and the derate word DAT_20001f90**

Reads three 16-bit words through app_get_u16_2000329c, app_get_u16_2000329e and app_get_u16_200032a0, scales each by 1/14 (1/15 when DAT_20001feb is set) and keeps the raw values at DAT_20003346..DAT_2000334a. Hard limit flags DAT_20001f62, DAT_20001f63 and DAT_20001f6a are set outside the window 30 to DAT_20001393 (or DAT_20001395), which is 220 when DAT_20001feb is set and 215 otherwise. Soft band flags DAT_20001f67, DAT_20001f66 and DAT_20001f64 take the window 30-55 (channel 1) or 30-60 (channels 2 and 3) and, when mode is nonzero, use hysteresis. When channel 1 is inside its limits, the low byte of DAT_20001f90 ramps from 0 at 56 to 200 at 180 ((value - 55) * 200 / 125), except that bit 3 of DAT_20001f92 holds it at 0; channels 2 and 3 use the larger reading, ramped from 61 to 180 ((value - 60) * 200 / 120) into the high byte. DAT_20001f50 and DAT_20001f4f flag the two ramps, and DAT_20001fbc is requested when either is active.

| Parameter | Type | Description |
|---|---|---|
| `mode` | `u32` | 0 evaluates the soft bands without hysteresis; 2 forces the low byte of DAT_20001f90 to zero after the ramp; any other value applies hysteresis to the soft bands |

**Notes:** The physical quantity is not established: the 30, 55, 60 and 180 limits could be temperatures, and 215 or 220 as a high limit is unusual for that. The window constants are also written to DAT_20001392, DAT_20001394 and DAT_20001396 (180, 60, 180) for other code to read. When DAT_20001fd6 is set or bit 3 of DAT_20001e6a is set, the low byte of DAT_20001f90 is cleared.

- Addresses by version: 148: 0x08003030, 14a: 0x08003124, 14b: 0x08003438, 14e: 0x08003438, 14f: 0x08003494, 152: 0x08003500, 153: 0x08003520, 0159: 0x08003594
- Called by: `vcu_0159_0800a15c`, `vcu_0159_0800a1d0`, `vcu_0159_0800a264`, `vcu_0159_0800a39c`, `vcu_0159_0800a500`, `vcu_0159_0800a55c`, `vcu_0159_0800a5c8`
- Calls: `app_get_u16_2000329e`, `app_get_u16_200032a0`, `app_get_u16_2000329c`
- Confidence: medium

## vcu_speed_mode_snapshot_update

**Per-tick speed conversion, drive sub-mode selection and periodic telemetry snapshot**

Runs once per tick. It copies the speed value DAT_20001cc6 into DAT_20001b62 (units presumed 0.1 km/h from the divide-by-10 steps) and forms the displayed speed DAT_20001cf8: when bit 0 of the status word DAT_20001aee is set it multiplies km/h by about 0.621 (float 0x3f1ef9db, km/h to mph) and rounds, otherwise it divides by 10. It copies DAT_20001aee bit 0 and DAT_20001af0 bits 5 and 4 into status words DAT_20001f92 and DAT_20001f98, and selects the drive sub-mode DAT_20001fa4 (1..4) from request bits af0[7], af0[8], aee[4] and whether speed is below 5.0 km/h; a nonzero sub-mode is copied to the operating mode DAT_20001b68 when the low byte of DAT_20001f90 is zero. Every 11th call it writes a snapshot of about 35 halfwords at 0x20003360 with magic 0x515c and a value of 3 at 0x200033b6, and it reports a pending warning code through vcu_warning_code_set when DAT_20001f80 is nonzero.

**Notes:** The source of the speed value and the meaning of the request bits are inferred from how they are used. The snapshot block is presumably read by a telemetry or diagnostic consumer that is not traced here.

- Addresses by version: 148: 0x0800828C, 14a: 0x080086E8, 14b: 0x08008A60, 14e: 0x08008AA0, 14f: 0x08008AFC, 152: 0x08008BC0, 153: 0x08008C5C, 0159: 0x08008CC0
- Called by: `vcu_0159_080047ac`
- Calls: `__aeabi_fmul`, `__aeabi_ui2f`, `__aeabi_d2iz`, `__aeabi_f2d`, `__aeabi_dadd`, `vcu_warning_code_set`
- Confidence: medium

## vcu_state_params_reset

**Reset the packed state words at 0x20001f8c and load default 0x2800/0x3200 limit and 0xF00 base**

Masks DAT_20001f98 with 0xe000 and DAT_20001f92 with 0xb000 (keeping only the top 3 / flag bits). Then, depending on the byte DAT_20001fa7, sets DAT_20001f96 = 0x2800 (10240) if the byte is not 0 and not 3, otherwise 0x3200 (12800), and sets DAT_20001f94 = (DAT_20001f94 & 0xc000) + 0xf00 (keeps the top two bits, base value 3840). The two constants look like 12-bit/14-bit scaled limits selected by a vehicle mode (0/3 versus other modes). Called from the init routine 0x08009da8.

**Notes:** Units of 0x2800/0x3200/0xF00 and the meaning of the mode byte 0x20001fa7 are guesses; the struct at 0x20001f8c is address-taken only.

- Addresses by version: 148: 0x08007990, 14a: 0x08007DCC, 14b: 0x08008124, 14e: 0x08008164, 14f: 0x080081C0, 152: 0x08008284, 153: 0x08008320, 0159: 0x0800837C
- Called by: `vcu_0159_08009da8`
- Confidence: low

## vcu_status_flags_mask_low

**Clear the low 12 bits of two 16-bit status/limit words at 0x20001f92 and 0x20001f98**

Does DAT_20001f92 &= 0xf000 and DAT_20001f98 &= 0xf000, i.e. keeps only the top nibble of each halfword and zeroes the 12-bit value fields. Both halfwords belong to a packed state structure based at 0x20001f8c that is also manipulated by vcu_state_params_reset. Called from 0x0800a39c, probably when a mode/state is entered to wipe accumulated values.

**Notes:** Meaning of the 4 flag bits and 12-bit values in these words is unknown; the structure at 0x20001f8c is only address-taken here.

- Addresses by version: 148: 0x080072D0, 14a: 0x0800770C, 14b: 0x08007A70, 14e: 0x08007AA8, 14f: 0x08007B04, 152: 0x08007BC8, 153: 0x08007C64, 0159: 0x08007CFC
- Called by: `vcu_0159_0800a39c`
- Confidence: low

## vcu_timebase_100_tick

**Divide-by-100 prescaler that advances four saturating elapsed-time counters**

Increments the byte/word DAT_20001384; when it reaches 100 it resets to 0 and (once per 100 calls) increments DAT_20001b86 (saturating at 0x7FFF) and the 32-bit DAT_20001b7c (saturating at 0xFFFFFFFF). If bit 2 of the status halfword DAT_20001f92 is set and DAT_20001b62 > 9, it also increments DAT_20001b88 (saturating at 0x7FFF) and 32-bit DAT_20001b80. Called from the periodic routine 0x08009080; if that runs every 10 ms the counters tick in seconds.

**Notes:** Call rate and the meaning of the counters are unknown; the decompiler warned that 32-bit globals overlap smaller ones at 0x20001b7c/b80.

- Addresses by version: 148: 0x08008514, 14a: 0x080089A0, 14b: 0x08008D70, 14e: 0x08008DD4, 14f: 0x08008E30, 152: 0x08008EF4, 153: 0x08008F90, 0159: 0x0800900C
- Called by: `vcu_wheel_odometer_limit_update`
- Confidence: low

## vcu_toggle_special_mode

**Toggle mode byte DAT_20001fa4 between its current value and the special value 4**

Active only when bit4 of DAT_20001aee is set and the request flag DAT_20001f72 is nonzero; the flag is consumed (cleared). If the mode DAT_20001fa4 is already 4, it is restored from the saved value DAT_20001354. Otherwise, if DAT_20001b62 < 0x32, the current mode is saved in DAT_20001354 and DAT_20001fa4 is set to 4. Called from the main handlers (vcu_0159_0800a15c, 0800a1d0).

**Notes:** DAT_20001b62 < 50 is a gate, probably a speed limit in some unit; meaning of mode 4 unknown.

- Addresses by version: 148: 0x080045A8, 14a: 0x08004904, 14b: 0x08004C44, 14e: 0x08004C7C, 14f: 0x08004CD8, 152: 0x08004D38, 153: 0x08004D50, 0159: 0x08004F74
- Called by: `vcu_0159_0800a15c`, `vcu_0159_0800a1d0`
- Confidence: medium

## vcu_wheel_odometer_limit_update

**Accumulate wheel angle and revolutions, then compute the drive output limit**

Calls vcu_angle_deg_update and vcu_timebase_100_tick, then, whenever the speed snapshot DAT_20001b62 divided by 10 is nonzero, adds it to the wheel angle accumulator DAT_20001388 (wrapping at 360000, read as thousandths of a degree). On wrap, if status bit 2 of DAT_20001f92 is set, the revolution counters DAT_20001b78 (unless -1) and DAT_20001b84 (up to 0x7fff) increment. Then a limit is chosen by a switch on the variant DAT_20001fa7 and the sub-mode DAT_20001fa4, from the values 7000, 5000, 3000, 4000, 5600, 3800 and 3200 (default 7000, and 5100 for variant 6), and multiplied by DAT_20001e62 / 100: the clamped result goes to DAT_20001b72, DAT_20001b70 receives 80% of it, and the unclamped product goes to DAT_20001cd2.

**Notes:** In variant 0, sub-mode 3 selects 3000 on both branches of an if on the aee bit, so one branch is dead. The variant table is read from compare constants and may be incomplete. The 360000 wrap and the 0x20001e62 percent scale are inferred.

- Addresses by version: 148: 0x08008588, 14a: 0x08008A14, 14b: 0x08008DE4, 14e: 0x08008E48, 14f: 0x08008EA4, 152: 0x08008F68, 153: 0x08009004, 0159: 0x08009080
- Called by: `vcu_0159_080047ac`
- Calls: `vcu_angle_deg_update`, `vcu_timebase_100_tick`
- Confidence: medium
