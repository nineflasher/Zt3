# BMS - `soc` functions

19 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_capacity_integrate_step`](#bms_capacity_integrate_step) | 0x0800746C | Integrate current into hour and remainder counters with rest-time voltage correction |
| [`bms_capacity_seed_from_voltage`](#bms_capacity_seed_from_voltage) | 0x080076B4 | Seed the capacity counters from the IR-compensated voltage permille |
| [`bms_charge_integrate_step`](#bms_charge_integrate_step) | 0x08006F90 | Integrate the signed current step into the charge counters, rolling over into hours and cycles |
| [`bms_meas_alt_steps_run`](#bms_meas_alt_steps_run) | 0x0800CE4E | Run the alternate measurement steps bms_4168_080071C8 and bms_4168_080076B4 in order |
| [`bms_meas_interp_filter_dispatch`](#bms_meas_interp_filter_dispatch) | 0x0800C638 | Interpolate a 16-bit level estimate, low-pass filter it and run the measurement update chain |
| [`bms_pct_hysteresis_step`](#bms_pct_hysteresis_step) | 0x0800E67C | Track commanded and estimated percent values with a 30 s trim timer and a hysteresis output |
| [`bms_remaining_time_4130`](#bms_remaining_time_4130) | (removed) | Update the minutes-like estimate at status +0x128 with hold and hysteresis (BMS_4130) |
| [`bms_remaining_time_4139`](#bms_remaining_time_4139) | (removed) | Update the minutes-like estimate at status +0x128 with hold and hysteresis (BMS_4139) |
| [`bms_remaining_time_4168`](#bms_remaining_time_4168) | 0x08004A40 | Update the minutes-like remaining-time estimate at +0x128 with hold and hysteresis (BMS_4148, BMS_4168) |
| [`bms_soc_band_classify`](#bms_soc_band_classify) | 0x0800E748 | Classify the state-of-charge value at +0x104 and set the mode code in the low bits of DAT_200005C0 |
| [`bms_soc_estimate_4130`](#bms_soc_estimate_4130) | (removed) | 4130 state-of-charge estimator: rest-voltage or coulomb-count mode, 8-sample OCV filter, slewed integrators |
| [`bms_soc_from_ocv_table`](#bms_soc_from_ocv_table) | 0x08006674 | Piecewise-linear 0-100 percent lookup from an 11-point table at 0x20000EB6 |
| [`bms_soc_main_step`](#bms_soc_main_step) | 0x080068E8 | Per-tick 4168 SOC step: integrate current, blend count and OCV estimates, step the reported SOC |
| [`bms_soc_tick_update`](#bms_soc_tick_update) | 0x08007348 | Refresh SOC percent, capacity words and OCV resync timers on each SOC tick |
| [`bms_soc_update_from_voltage`](#bms_soc_update_from_voltage) | 0x080071C8 | Recompute SOC percent from IR-compensated voltage and refresh the capacity words |
| [`bms_state_refresh_scaled`](#bms_state_refresh_scaled) | 0x08006730 | Refresh scaled measurement and derived-limit fields of the BMS state block at 0x20000BDC |
| [`bms_throughput_accumulate`](#bms_throughput_accumulate) | 0x08003868 | Integrate \|sample\| x 10 and return whole 3600-scaled units to add to a total |
| [`bms_tracking_filter_step`](#bms_tracking_filter_step) | 0x080072EC | One step of a dead-band tracking filter that slews an estimate toward a measurement |
| [`bms_voltage_error_track`](#bms_voltage_error_track) | 0x0800708C | Accumulate the IR-compensated voltage over samples, average it, and refresh the OCV-based charge estimate |

## bms_capacity_integrate_step

**Integrate current into hour and remainder counters with rest-time voltage correction**

Coulomb-count integrator run once per sample. param_1 points to a sample record whose s32 at +0 is the current sample and whose u16 at +4 is compared with 0x1022 (4130). Status bit 4 at state+0x124 zeroes the counters, and status bit 2 with the u16 above 4130 and a current below 20 pins them to full (permille 1000, hour counter at 0x20000E44, remainder at 0x20000E48). Otherwise, while |current| is above 9, current times param_2 (elapsed time) divided by 10 with bms_sdiv32 is added to the sub-hour accumulator 0x2000024C, and each 3600000 units move the hour counter 0x20000E3C one step toward its full value 0x20000E44 (or down when negative). The permille 0x20000E38 = hours * 1000 / full is compared with the reference permille 0x20000E3A, and the remainder 0x20000E40 is reduced (status bit 1) or increased (status bit 2, capped at 0x20000E48) by a gain that depends on the gap between the two permille values. At rest, after 3600000 units in 0x20000248, bms_table_interp_permille of the voltage gives a new permille, the reference 0x20000E3A is lowered by one when it is above that value, and the hour counter is re-derived from the percent 0x20000E24.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | sample record: s32 current sample at +0, u16 at +4 compared with 4130 |
| `param_2` | `s32` | elapsed time since the previous call (units inferred as ms from the 3600000 rollover) |

**Notes:** The gain table is read off the decompile: x3, x2, x1.5 and x1.25 when the reference permille is larger, and x1/3, x1/2, x2/3 and x4/5 when the new permille is larger, with the largest gap tested first. The direction and purpose of each counter (charge or discharge, Ah or hours) are inferred.

- Addresses by version: 4130: 0x08006598, 4139: 0x0800698C, 4148: 0x080071B8, 4168: 0x0800746C
- Called by: `bms_meas_interp_filter_dispatch`
- Calls: `bms_udiv32`, `bms_sdiv32`, `bms_table_interp_permille`, `bms_ram_20000bdc_addr`
- Confidence: low

## bms_capacity_seed_from_voltage

**Seed the capacity counters from the IR-compensated voltage permille**

Restarts the counters from the voltage. It computes the IR-compensated voltage (0x200001F0 minus bms_sdiv32(state+0x11A * 0x20000E96, 100)), converts it with bms_table_interp_permille to a permille and stores that in 0x20000E38 and 0x20000E3A. The full-scale words 0x20000E44 and 0x20000E48 are both set from 0x20000E84, and the hour counter 0x20000E3C and the remainder 0x20000E40 become permille * 0x20000E84 / 1000 (bms_udiv32).

**Notes:** 0x20000E84 is read as the full-scale capacity value; its name is not established in this packet.

- Addresses by version: 4130: 0x080067E0, 4139: 0x08006BD4, 4148: 0x08007400, 4168: 0x080076B4
- Called by: `bms_meas_interp_filter_dispatch`, `bms_meas_alt_steps_run`
- Calls: `bms_udiv32`, `bms_sdiv32`, `bms_table_interp_permille`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_charge_integrate_step

**Integrate the signed current step into the charge counters, rolling over into hours and cycles**

A sub-count accumulator at 0x20000EF8 is advanced by current_step * 10 * current (state+0x11A) when mode is 0, or by -35 when mode is 1, with an extra -12 when the current is zero. Whole multiples of 10 move from 0x20000EF8 to 0x20000EFC, and whole multiples of 3600 (0xE10) move from 0x20000EFC into the estimate at 0x20000EEC, which is clamped to 0 when negative. When the current is above 10 and bit 2 of the 16-bit word at +0x124 is set, positive whole-3600 counts are added to the 32-bit word at +0x1BE; once it exceeds 97 percent of 0x20000E34 that threshold is subtracted, the 16-bit counter at +0xB2 is incremented and bit 0x80 is set in the flag word at 0x200001C8. The 32-bit word is stored back at +0x1BE and +0x1C0.

| Parameter | Type | Description |
|---|---|---|
| `current_step` | `s32` | signed current step (scaled), multiplied by 10 before accumulation |
| `mode` | `s32` | 1 selects the -35 offset update; any other value uses the current-proportional update |

**Notes:** The 3600-tick unit is assumed to be one hour if the tick is one second, which is a guess. The meaning of the +0xB2 counter as a cycle count is inferred from its use as the aging input in bms_4168_08006730.

- Addresses by version: 4139: 0x080064BC, 4148: 0x08006CE8, 4168: 0x08006F90
- Called by: `bms_soc_main_step`, `bms_soc_tick_update`
- Calls: `bms_udiv32`, `bms_sdiv32`, `bms_ram_20000bdc_addr`, `bms_ram_200001c8_addr`
- Confidence: medium

## bms_meas_alt_steps_run

**Run the alternate measurement steps bms_4168_080071C8 and bms_4168_080076B4 in order**

Thin wrapper that calls bms_4168_080071C8 and then bms_4168_080076B4. These are the same two calls that bms_4168_0800C638 makes on its param_4 != 0 branch, so this is the alternate measurement path invoked on its own. Both callees are described in other packets, so what they update is not repeated here. The only caller in this packet's scope is bms_4168_080082F0.

**Notes:** The wrapper behaviour is certain from the four instructions. The category is inferred from the sibling call in bms_4168_0800C638.

- Addresses by version: 4130: 0x0800BAF2, 4139: 0x0800C0C2, 4148: 0x0800CA66, 4168: 0x0800CE4E
- Called by: `bms_4168_080082f0`
- Calls: `bms_soc_update_from_voltage`, `bms_capacity_seed_from_voltage`
- Confidence: high

## bms_meas_interp_filter_dispatch

**Interpolate a 16-bit level estimate, low-pass filter it and run the measurement update chain**

Measurement update over a channel record param_1 that holds a 16-bit target at +4 and a threshold at +0xE. It computes uVar3 = (DAT_20000ECA - DAT_20000EB6) masked to 16 bits; if uVar3 exceeds the threshold and the sample DAT_20000EB6 is below the target, the value is DAT_20000EB6 + uVar3*(target - DAT_20000EB6)/(uVar3 - threshold), using bms_udiv32, and otherwise it is the target. The first call only sets DAT_200001E9 to 1. Later calls, unless bit 5 of the byte at 0x200001C8 is set, low-pass filter the value as (3*DAT_200001F0 + new + 1) >> 2 before storing it back to DAT_200001F0. param_4 == 0 runs bms_4168_080068E8, bms_4168_0800746C and bms_4168_08007704 with param_2 and param_3, otherwise bms_4168_080071C8 and bms_4168_080076B4 run; then bms_state_refresh_scaled and bms_4168_08004A40 are called.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | channel record: u16 target at +4, u16 threshold at +0xE |
| `param_2` | `u32` | passed through to the param_4 == 0 chain (bms_4168_080068E8, bms_4168_08007704) |
| `param_3` | `u32` | passed through to the param_4 == 0 chain (bms_4168_080068E8, bms_4168_0800746C) |
| `param_4` | `s32` | selects the primary chain when zero, the alternate chain when nonzero |

**Notes:** The units of DAT_20000EB6 and DAT_20000ECA are not identified (type not shown by the decompiler). The filter constant and the interpolation form are read directly from the code. Callees bms_4168_080068E8, bms_4168_0800746C, bms_4168_08007704, bms_4168_080071C8, bms_4168_080076B4 and bms_4168_08004A40 are not described yet, so the meaning of the two chains is inferred only from the names of the RAM they touch.

- Addresses by version: 4130: 0x0800B5E8, 4139: 0x0800BB40, 4148: 0x0800C324, 4168: 0x0800C638
- Called by: `bms_4168_08007a0c`
- Calls: `bms_udiv32`, `bms_remaining_time_4168`, `bms_state_refresh_scaled`, `bms_soc_main_step`, `bms_soc_update_from_voltage`, `bms_capacity_integrate_step`, `bms_capacity_seed_from_voltage`, `bms_current_limit_derate`, `bms_ram_200001c8_addr`
- Confidence: medium

## bms_pct_hysteresis_step

**Track commanded and estimated percent values with a 30 s trim timer and a hysteresis output**

Percent-level supervisor run once per tick. uVar1 is the u16 at +0x104 of the BMS state block at 0x20000BDC (the commanded percent, written by the CAN handler bms_can_cmd_set_handler) and uVar2 is the u16 at +0x11E (the estimate). While bit 0 of 0x200005C0 is set, param_1 is accumulated into DAT_200005CC and every 30000 ticks bits 1 and 2 are set when the estimate is at or above the command and cleared when it is below; bit 0 is cleared when the command is exactly 100 and bit 1 is clear. When bit 0 is clear, bit 1 and the timer are cleared. The output DAT_20000DE7 is forced to 0, and DAT_200005C5 to 0, when the u16 at +6 of the reply buffer is zero or DAT_20000DDC or DAT_20000DDF is set. Otherwise the reference is min(command, 90): an estimate below 76 forces output 0 and latches DAT_200005C5 to 1; an estimate at or above the reference clears the latch and sets output 1; in between the output is 1 only when the latch is clear.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | elapsed ticks added to the 30 s trim timer |

**Notes:** The meaning of uVar1 and uVar2 as commanded and estimated percent is inferred from the 76 and 90 limits, the 100 test and the CAN handler that writes +0x104. The flags DAT_20000DDC and DAT_20000DDF are not identified. Bits 1 and 2 of 0x200005C0 are set but not read by this function; their readers are not in this packet.

- Addresses by version: 4168: 0x0800E67C
- Called by: `bms_setpoint_service_step`
- Calls: `bms_ram_20000bdc_addr`, `bms_reply_buffer_get`
- Confidence: medium

## bms_remaining_time_4130

**Update the minutes-like estimate at status +0x128 with hold and hysteresis (BMS_4130)**

Per-tick estimator for the value at status +0x128. The status object comes from the BMS_4130 accessor (bms_ram_20000bdc_addr in this build), and bit 2 of its u16 at +0x124 gates everything. While the bit is set it samples the s16 at +0x11A into 0x20000116 when the value is 1 to 1399, and after ten counts latches it into 0x20000114. The estimate is ((u16 +0x104 x DAT_20000CDC / 100) - (DAT_20000D94 x 0x50 + DAT_20000D90 x 0x14) / 100) x 1000 / reference x 60 / 10000, with 30 added when +0x104 exceeds 95. Above 0x1503 on +0x118 the estimate loses one unit every 600 ticks, and a hold in 0x20000118 with a switch-over rule decides what reaches +0x128, which is written only inside range checks (499). When the gate bit is clear the holds are reset.

**Notes:** The x60 and /10000 scaling suggests minutes, which is an inference. The reference 0x20000116 and the RAM terms 0x20000CDC, 0x20000D90 and 0x20000D94 are not identified in this packet. Helper bms_4168_0800113c is not yet described.

- Addresses by version: 4130: 0x08004410
- Called by: `bms_meas_interp_filter_dispatch`
- Calls: `bms_udiv32`, `bms_sdiv32`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_remaining_time_4139

**Update the minutes-like estimate at status +0x128 with hold and hysteresis (BMS_4139)**

Estimator of the same family as bms_remaining_time_4130 for BMS_4139, using the RAM terms DAT_20000D38, DAT_20000DEC and DAT_20000DF0 and the reference DAT_20000158. Bit 2 of the u16 at +0x124 gates it: when set it samples the s16 at +0x11A into the holds at 0x20000156..0x2000015C, latching after ten counts, and when clear it resets the holds. The estimate is ((u16 +0x104 x DAT_20000D38 / 100) - (DAT_20000DF0 x 0x50 + DAT_20000DEC x 0x14) / 100) x 1000 / reference x 60 / 10000, clamped at zero. A one-shot flag at 0x2000014C enables a band correction on +0x118 above 0x1503, and a count of 599 steps lowers the held value by one. The result is written to +0x128 inside a range check of 499.

**Notes:** The minutes reading and the meaning of the RAM terms are inferences, as for bms_remaining_time_4130. Helper bms_4168_0800113c is not yet described.

- Addresses by version: 4139: 0x08004618
- Called by: `bms_meas_interp_filter_dispatch`
- Calls: `bms_udiv32`, `bms_sdiv32`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_remaining_time_4168

**Update the minutes-like remaining-time estimate at +0x128 with hold and hysteresis (BMS_4148, BMS_4168)**

Computes a time-to-go value in minutes. It takes the energy gap between the SOC-based charge (+0x104 percent times full capacity DAT_20000E34) and a blended estimate (DAT_20000EEC times 80 plus DAT_20000EE8 times 20, over 100), divides it by a reference current (DAT_200001FA, learned from +0x11A while the 0x124 bit 2 flag is set) and scales by 60/10000. Two paths are taken by the reply-buffer word +6: when it is zero the estimate uses only the local current and the 0x124 bit 2 flag; otherwise it adds a term from the reply words +6, +8 and +0x16, and clamps +0x16 to 100 outside 80 to 100. A pack-voltage band (+0x118 against 0x1504 and 0x152D) adds 20 minutes when the SOC is above 95 and applies a linear correction in between. The published value at +0x128 rises only after a change event (DAT_200001EE) and is otherwise held at the lower value; it is cleared when the current is within +/-24 of zero and the SOC does not exceed the ceiling at +0x11E.

**Notes:** The units of +0x118 (apparently a pack voltage in 10 mV steps), +0x11A and the reference current are inferred. bms_reply_buffer_get can clear the reply buffer. The counter and latch names (DAT_200001EA to DAT_20000200) are address-only names. The 4130 and 4139 versions of this estimator are separate families (bms_remaining_time_4130, bms_remaining_time_4139).

- Addresses by version: 4148: 0x080048E0, 4168: 0x08004A40
- Called by: `bms_meas_interp_filter_dispatch`
- Calls: `bms_udiv32`, `bms_sdiv32`, `bms_ram_20000bdc_addr`, `bms_reply_buffer_get`
- Confidence: medium

## bms_soc_band_classify

**Classify the state-of-charge value at +0x104 and set the mode code in the low bits of DAT_200005C0**

Reads the 16-bit value at state block +0x104, which is treated as a percentage with 100 meaning full, and sets the low three bits of DAT_200005C0 as a mode code. A value above 99 is forced to 100 and bits 0 and 1 are cleared, keeping bit 2. Otherwise, when the value is at or below the 16-bit limit at +0x11E the mode becomes 3 (bits 0 and 1 set, bit 2 cleared), and in all other cases it becomes 1 (bit 0 only).

**Notes:** The source tests (value - 80) > 19 as a signed comparison, so only values of 100 and above take the forced-100 branch; values from 80 to 99 fall through to the threshold test. The reading of +0x104 as state of charge is inferred from the value 100 and the bms_4148 use in bms_balance_timer_step.

- Addresses by version: 4130: 0x0800CCCC, 4139: 0x0800D2B4, 4148: 0x0800E2B4, 4168: 0x0800E748
- Called by: `bms_tail_call_unnamed_a`
- Calls: `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_soc_estimate_4130

**4130 state-of-charge estimator: rest-voltage or coulomb-count mode, 8-sample OCV filter, slewed integrators**

Runs once per tick on the 4130 state block (bms_ram_20000bdc_addr), with the elapsed time in param_3 divided by 100 as the step. Bit 6 of the byte at 0x200001C8 (bms_ram_200001c8_addr) selects the rest branch: SOC is taken from the OCV lookup (bms_soc_from_ocv_table) applied to DAT_20000108 minus the current times DAT_20000D3E, clamped to 0 to 100 in DAT_20000CCC, and after 1200 rest ticks the integrators DAT_20000D90, D94 and D98 are seeded from it and bit 4 of the flag byte is set. In active mode the rest counters are cleared and current times time is integrated into DAT_20000DA8 with a 3600-unit rollover into the hour integrators DAT_20000D94 and D98 (clamped at 0), keeping the sub-unit residual in DAT_20000DA4. Every ten steps, or on a large step, a voltage-error sample (DAT_20000108 minus a current-compensated term) goes into an eight-entry ring at DAT_20000DAC indexed by DAT_200000FC, and the mean of the ring feeds the filtered estimate DAT_20000D90. D94 and D98 are slewed toward it with +/-128 hysteresis accumulators (DAT_2000010E and DAT_20000110), and the 16-bit value at +0x1F4 is latched into DAT_20000112 when bit 4 of the byte at 0x200005C0 is set. The reported SOC is a blend of 20 percent of D90 and 80 percent of D94 or D98 (selected by bit 2 of the state word at +0x124), with rate-limited 1 percent steps of DAT_20000CCE driven by the accumulators at DAT_20000130, 0x2000012C, 0x20000134 to 0x2000013C and 0x20000140.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | unused |
| `param_2` | `u32` | unused |
| `param_3` | `u32` | elapsed time of this step; divided by 100 to give the integration step |

**Notes:** This is the 4130 counterpart of the 4148 and 4168 estimator (bms_soc_main_step). The full rate-limit and step-direction logic of DAT_20000CCE and the meaning of DAT_20000D3E are not traced in detail; the description is a structural summary. The 4130 state-block helpers are the packet's family names (bms_ram_20000bdc_addr, bms_ram_200001c8_addr, bms_get_block_200005c0_ptr); their 4130 addresses differ from the 4168 ones.

- Addresses by version: 4130: 0x08005D2C
- Called by: `bms_meas_interp_filter_dispatch`
- Calls: `bms_udiv32`, `bms_sdiv32`, `bms_soc_from_ocv_table`, `bms_ram_20000bdc_addr`, `bms_ram_200001c8_addr`, `bms_get_block_200005c0_ptr`
- Confidence: low

## bms_soc_from_ocv_table

**Piecewise-linear 0-100 percent lookup from an 11-point table at 0x20000EB6**

Maps a value (param_1) through an 11-point table of ascending u16 breakpoints at 0x20000EB6 + 2k, k = 0 to 10. It returns 0 at or below the first breakpoint and 100 at or above the last (at 0x20000ECA). Between them it finds the segment k where the value is at most T[k], and returns 10 x (k-1) plus 10 times the position inside that segment, computed with bms_4168_0800113c as (x - T[k-1]) x 10 / (T[k] - T[k-1]). The result is stored at 0x200001DC and returned.

| Parameter | Type | Description |
|---|---|---|
| `x` | `u32` | param_1; compared with the breakpoints at 0x20000EB6..0x20000ECA |

**Returns** `u8`: 0 to 100 percent

**Notes:** The OCV-to-SOC reading comes from the 0-100 range in ten-percent segments; the unit of the input (probably a cell voltage) and the table source are not shown in the packet. Callers bms_4130_08005d2c and bms_4168_0800708c, 080071c8 and 08007348 are outside it.

- Addresses by version: 4130: 0x08005AC4, 4139: 0x08005CE0, 4148: 0x08006508, 4168: 0x08006674
- Called by: `bms_voltage_error_track`, `bms_soc_update_from_voltage`, `bms_soc_tick_update`
- Calls: `bms_sdiv32`
- Confidence: medium

## bms_soc_main_step

**Per-tick 4168 SOC step: integrate current, blend count and OCV estimates, step the reported SOC**

Runs once per tick with dt = param_3/100. If bit 6 of the byte at 0x200001C8 is set it hands off to bms_4168_08007348 and returns. It calls bms_charge_integrate_step with dt, then bms_voltage_error_track (bms_4168_0800708c), which refreshes DAT_20000EE8 from the OCV table. The blended charge DAT_20000EF0 depends on the profile class: for profiles 6 to 8 it is the count estimate DAT_20000EEC times 100 unless a latch from low current, near-full voltage (16-bit value at +8 of param_1 at or above 4101 mV for 1200 ticks) or low SOC (below 21 percent) is set, in which case EEC is slewed toward EE8 by bms_tracking_filter_step and blended 80/20; for other profiles it is EEC alone or a 70/30 blend of EEC and EE8 at low SOC or at high SOC with the 0x124 bit 2 flag. A cell voltage below 3000 mV (value at +4 of param_1) zeroes EE8, the reported SOC DAT_20000E26 and EEC. The blend is converted to a 0 to 100 SOC in DAT_20000EF4, the capacity DAT_20000E28 is derived from it, and the reported SOC DAT_20000E26 moves in rate-limited 1 percent steps with direction and rate set by the current bands, the 0x124 bits 1 and 2, and the timers at DAT_20000210, DAT_20000224 and DAT_2000023C.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | voltage record: u16 at +4 (mV, checked against 3000) and u16 at +8 (mV, checked against 4101 and 4150) |
| `param_2` | `ptr` | context record: s16 at +2 gates the low-voltage reset (below 6, or below 10 with a latch) |
| `param_3` | `u32` | elapsed time of this step; divided by 100 to give the integration step |

**Notes:** Units are read from the constants: the 1000 to 3000 ticks and 100 ticks per 1 percent rate, and the mV thresholds. The OCV table and the rest handler bms_4168_08007348 are not described in this packet. The per-class blend weights and step thresholds are summarised, not fully traced.

- Addresses by version: 4139: 0x08005F54, 4148: 0x0800677C, 4168: 0x080068E8
- Called by: `bms_meas_interp_filter_dispatch`
- Calls: `bms_udiv32`, `bms_sdiv32`, `bms_charge_integrate_step`, `bms_voltage_error_track`, `bms_tracking_filter_step`, `bms_soc_tick_update`, `bms_ram_20000bdc_addr`, `bms_ram_200001c8_addr`, `bms_reply_buffer_get`
- Confidence: medium

## bms_soc_tick_update

**Refresh SOC percent, capacity words and OCV resync timers on each SOC tick**

Runs once per SOC tick and works on the same capacity words as bms_soc_update_from_voltage. It recomputes the IR-compensated voltage, calls bms_soc_from_ocv_table on it (the result is discarded here, but the call refreshes the OCV percent at 0x200001DC), and rebuilds 0x20000E28 and 0x20000E2C from the percents in 0x20000E24 and 0x20000E26 with 0x20000E34 as the full capacity. In modes 6, 7 and 8 while the OCV percent is in the 50 to 97 band, the percent is recalculated from the charge counter 0x20000EEC and bms_charge_integrate_step is called with param_1 / 100. Outside that band a counter at 0x2000020C advances and after 1800 ticks the percent and the counters 0x20000EE8, 0x20000EEC and 0x20000E28 are resynchronised to the OCV percent; in other modes the same resync happens after 1200 ticks. The percent is clamped to 100, and when it stays below the displayed percent at 0x20000E26 for 14400 ticks (counter 0x20000208) the displayed percent is lowered by one.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | charge step passed to bms_charge_integrate_step after division by 100 |

**Notes:** The 1800, 1200 and 14400 tick periods depend on the tick rate, which this packet does not state. Mode numbers 6, 7 and 8 are taken as given by the decompile.

- Addresses by version: 4139: 0x08006860, 4148: 0x0800708C, 4168: 0x08007348
- Called by: `bms_soc_main_step`
- Calls: `bms_udiv32`, `bms_sdiv32`, `bms_soc_from_ocv_table`, `bms_charge_integrate_step`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_soc_update_from_voltage

**Recompute SOC percent from IR-compensated voltage and refresh the capacity words**

Runs once per SOC tick on the BMS state block (bms_ram_20000bdc_addr). It takes the IR-drop term bms_sdiv32(0x20000E96 * current at state+0x11A, 100) and subtracts it from the voltage word at 0x200001F0 to get a compensated voltage, which it stores in the eight 16-bit words at 0x20000F00 to 0x20000F0E. That voltage is mapped to a percent with bms_soc_from_ocv_table and kept at 0x20000E26. For modes 6, 7 and 8 (byte at 0x20000024) the percent is held or pinned inside the 50 to 97 band using the byte at 0x200001E6, and while the current is within +/-50 units it is forced to 100 above 4101 and to 0 below 3100. The result is copied to 0x20000E24 (clamped to 100), and the remaining-capacity words 0x20000E28, 0x20000E2C, 0x20000EE8, 0x20000EEC and 0x20000EF0 are recomputed as percent times a full capacity (state+0x11C scaled by 0x20000E88 * 97 / 100) divided by 100 with bms_udiv32.

**Notes:** Units of 0x200001F0 (taken as mV from the 4101 and 3100 limits) and of state+0x11A are inferred. 0x20000E88 is treated as a health percent and the 97 factor as a derating; neither is named elsewhere in this packet. The byte at 0x200001E6 is copied from state+0x11E at entry.

- Addresses by version: 4130: 0x080064F4, 4139: 0x080066F0, 4148: 0x08006F1C, 4168: 0x080071C8
- Called by: `bms_meas_interp_filter_dispatch`, `bms_meas_alt_steps_run`
- Calls: `bms_udiv32`, `bms_sdiv32`, `bms_soc_from_ocv_table`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_state_refresh_scaled

**Refresh scaled measurement and derived-limit fields of the BMS state block at 0x20000BDC**

Reads raw RAM globals (0x20000E24, E26, E3A, E40, E44, E4C, E50, E54, E88, E94, EE8, EEC) and writes each into a fixed 16-bit field of the state block from bms_ram_20000bdc_addr, dividing by 10, 100 or 1000 with bms_udiv32 or the signed divider bms_4168_0800113c. The capacity pair 0x20000E30 and 0x20000E34 is recomputed from E88, the second scaled by 97 percent. The derating factor is a three-band curve on the 16-bit value at +0xB2 with a floor of 80 applied to +0x11C, and bit 1 of +0x196 is set when that floor clamps. The 16-bit value at 0x20000E26 is lowered to the field at +0x104 when bits 0 and 2 of the byte at 0x200005C0 are both set. Caller is bms_4168_0800c638.

**Notes:** Packed fields: +0x1D8 high byte receives the signed quotient of the value at +0x11A by 100 (negated when below -99); +0x1DA holds (k*8/10) in the high byte and (k*15/10) in the low byte, where k = (DAT_20000E50/10)/100. Whether 0x0800113c is signed division is inferred from its use with negative inputs.

- Addresses by version: 4130: 0x08005B74, 4139: 0x08005D9C, 4148: 0x080065C4, 4168: 0x08006730
- Called by: `bms_meas_interp_filter_dispatch`
- Calls: `bms_udiv32`, `bms_sdiv32`, `bms_ram_20000bdc_addr`, `bms_get_block_200005c0_ptr`
- Confidence: medium

## bms_throughput_accumulate

**Integrate |sample| x 10 and return whole 3600-scaled units to add to a total**

param_1 is a record: byte +0x00 is a step added to the sample counter at 0x20000603, byte +0x02 is an enable flag, and s16 +0x14 is a signed sample. When enabled it adds |sample| x 10 to the running total at 0x2000060C and adds the step to the counter. Once the counter reaches 10 it divides the total by counter x 3600 with bms_udiv32, keeps the remainder in 0x2000060C, resets the counter and returns the quotient added to param_2. Below 10 it returns param_2 unchanged and both accumulators keep running. When the enable flag is clear it zeroes the total and the counter.

| Parameter | Type | Description |
|---|---|---|
| `rec` | `ptr` | param_1; byte +0x00 step, byte +0x02 enable, s16 +0x14 sample |
| `acc` | `s32` | param_2; value the whole units are added to |

**Returns** `s32`: param_2 plus any whole units flushed this call

**Notes:** The 3600 divisor suggests a seconds-to-hours scale, so this is probably charge throughput in ampere-hours. The sample's unit and source are not in the packet.

- Addresses by version: 4130: 0x08003868, 4139: 0x08003868, 4148: 0x08003868, 4168: 0x08003868
- Called by: `bms_sample_window_process`
- Calls: `bms_udiv32`
- Confidence: medium

## bms_tracking_filter_step

**One step of a dead-band tracking filter that slews an estimate toward a measurement**

Moves the estimate DAT_20000eec one count toward the measurement DAT_20000ee8 with a dead-band accumulator. When the two differ, the step is the absolute difference masked to 20 bits and shifted right by 4, with a minimum of 5, signed toward the measurement, and it is added to the 16-bit accumulator DAT_200001f6. When the accumulator reaches 129 or more, the estimate is incremented and 128 is subtracted from the accumulator; when it reaches -129 or less, the estimate is decremented (clamped at 0) and 128 is added. Between those limits the estimate and accumulator are left alone, which is the dead band. No peripherals are touched.

**Notes:** Globals: DAT_20000ee8 read-only measurement, DAT_20000eec estimate (read/write), DAT_200001f6 accumulator (16-bit signed). The 20-bit mask and >>4 suggest a high-resolution ADC or AFE reading, but the quantity (SOC, current, voltage) is a guess.

- Addresses by version: 4139: 0x08006804, 4148: 0x08007030, 4168: 0x080072EC
- Called by: `bms_soc_main_step`
- Confidence: medium

## bms_voltage_error_track

**Accumulate the IR-compensated voltage over samples, average it, and refresh the OCV-based charge estimate**

Called once per tick from bms_soc_main_step with the elapsed step. It adds the step to a high-current timer at DAT_200001DE (capped at 40) when the current at +0x11A is above 300. When the current is at or below 300 or the sample timer DAT_200001F4 exceeds 100, it adds a weighted voltage sample to the accumulator DAT_20000214: the reference DAT_200001F0 minus the current times a profile-dependent weight (DAT_20000E96 plus 4, with a low-SOC boost) divided by 100, and counts it in DAT_200001F2. Every ten samples, or when the timer passes 100, it divides the accumulator by the count with bms_sdiv32 to form one voltage sample and pushes it into an eight-entry ring at DAT_20000F00 indexed by DAT_200001DD. If the sample exceeds the threshold DAT_20000EBC, it substitutes the rounded mean of the eight ring entries. The sample is mapped to a 0 to 100 percent value with bms_soc_from_ocv_table (bms_4168_08006674), and DAT_20000EE8 is set to DAT_20000E34 times that percentage over 100. The accumulators DAT_20000214, DAT_200001F2 and DAT_200001F4 are then cleared.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s16` | elapsed time of this step; added to the sample timer DAT_200001F4 |

**Notes:** The division bms_4168_0800113c (bms_sdiv32) is called without visible arguments in the decompile, so the dividend and divisor (DAT_20000214 over DAT_200001F2) are inferred from the surrounding code. The source of DAT_200001F0 is not identified. The profile weights are summarised; the exact boost formula is not fully traced.

- Addresses by version: 4139: 0x080065B4, 4148: 0x08006DE0, 4168: 0x0800708C
- Called by: `bms_soc_main_step`
- Calls: `bms_udiv32`, `bms_sdiv32`, `bms_soc_from_ocv_table`, `bms_ram_20000bdc_addr`
- Confidence: medium
