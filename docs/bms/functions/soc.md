# BMS - `soc` functions

8 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_charge_integrate_step`](#bms_charge_integrate_step) | 0x08006F90 | Integrate the signed current step into the charge counters, rolling over into hours and cycles |
| [`bms_remaining_time_4130`](#bms_remaining_time_4130) | (removed) | Update the minutes-like estimate at status +0x128 with hold and hysteresis (BMS_4130) |
| [`bms_remaining_time_4139`](#bms_remaining_time_4139) | (removed) | Update the minutes-like estimate at status +0x128 with hold and hysteresis (BMS_4139) |
| [`bms_soc_band_classify`](#bms_soc_band_classify) | 0x0800E748 | Classify the state-of-charge value at +0x104 and set the mode code in the low bits of DAT_200005C0 |
| [`bms_soc_from_ocv_table`](#bms_soc_from_ocv_table) | 0x08006674 | Piecewise-linear 0-100 percent lookup from an 11-point table at 0x20000EB6 |
| [`bms_state_refresh_scaled`](#bms_state_refresh_scaled) | 0x08006730 | Refresh scaled measurement and derived-limit fields of the BMS state block at 0x20000BDC |
| [`bms_throughput_accumulate`](#bms_throughput_accumulate) | 0x08003868 | Integrate \|sample\| x 10 and return whole 3600-scaled units to add to a total |
| [`bms_tracking_filter_step`](#bms_tracking_filter_step) | 0x080072EC | One step of a dead-band tracking filter that slews an estimate toward a measurement |

## bms_charge_integrate_step

**Integrate the signed current step into the charge counters, rolling over into hours and cycles**

A sub-count accumulator at 0x20000EF8 is advanced by current_step * 10 * current (state+0x11A) when mode is 0, or by -35 when mode is 1, with an extra -12 when the current is zero. Whole multiples of 10 move from 0x20000EF8 to 0x20000EFC, and whole multiples of 3600 (0xE10) move from 0x20000EFC into the estimate at 0x20000EEC, which is clamped to 0 when negative. When the current is above 10 and bit 2 of the 16-bit word at +0x124 is set, positive whole-3600 counts are added to the 32-bit word at +0x1BE; once it exceeds 97 percent of 0x20000E34 that threshold is subtracted, the 16-bit counter at +0xB2 is incremented and bit 0x80 is set in the flag word at 0x200001C8. The 32-bit word is stored back at +0x1BE and +0x1C0.

| Parameter | Type | Description |
|---|---|---|
| `current_step` | `s32` | signed current step (scaled), multiplied by 10 before accumulation |
| `mode` | `s32` | 1 selects the -35 offset update; any other value uses the current-proportional update |

**Notes:** The 3600-tick unit is assumed to be one hour if the tick is one second, which is a guess. The meaning of the +0xB2 counter as a cycle count is inferred from its use as the aging input in bms_4168_08006730.

- Addresses by version: 4139: 0x080064BC, 4148: 0x08006CE8, 4168: 0x08006F90
- Called by: `bms_4168_080068e8`, `bms_4168_08007348`
- Calls: `bms_udiv32`, `bms_4168_0800113c`, `bms_ram_20000bdc_addr`, `bms_ram_200001c8_addr`
- Confidence: medium

## bms_remaining_time_4130

**Update the minutes-like estimate at status +0x128 with hold and hysteresis (BMS_4130)**

Per-tick estimator for the value at status +0x128. The status object comes from the BMS_4130 accessor (bms_ram_20000bdc_addr in this build), and bit 2 of its u16 at +0x124 gates everything. While the bit is set it samples the s16 at +0x11A into 0x20000116 when the value is 1 to 1399, and after ten counts latches it into 0x20000114. The estimate is ((u16 +0x104 x DAT_20000CDC / 100) - (DAT_20000D94 x 0x50 + DAT_20000D90 x 0x14) / 100) x 1000 / reference x 60 / 10000, with 30 added when +0x104 exceeds 95. Above 0x1503 on +0x118 the estimate loses one unit every 600 ticks, and a hold in 0x20000118 with a switch-over rule decides what reaches +0x128, which is written only inside range checks (499). When the gate bit is clear the holds are reset.

**Notes:** The x60 and /10000 scaling suggests minutes, which is an inference. The reference 0x20000116 and the RAM terms 0x20000CDC, 0x20000D90 and 0x20000D94 are not identified in this packet. Helper bms_4168_0800113c is not yet described.

- Addresses by version: 4130: 0x08004410
- Called by: `bms_4168_0800c638`
- Calls: `bms_udiv32`, `bms_4168_0800113c`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_remaining_time_4139

**Update the minutes-like estimate at status +0x128 with hold and hysteresis (BMS_4139)**

Estimator of the same family as bms_remaining_time_4130 for BMS_4139, using the RAM terms DAT_20000D38, DAT_20000DEC and DAT_20000DF0 and the reference DAT_20000158. Bit 2 of the u16 at +0x124 gates it: when set it samples the s16 at +0x11A into the holds at 0x20000156..0x2000015C, latching after ten counts, and when clear it resets the holds. The estimate is ((u16 +0x104 x DAT_20000D38 / 100) - (DAT_20000DF0 x 0x50 + DAT_20000DEC x 0x14) / 100) x 1000 / reference x 60 / 10000, clamped at zero. A one-shot flag at 0x2000014C enables a band correction on +0x118 above 0x1503, and a count of 599 steps lowers the held value by one. The result is written to +0x128 inside a range check of 499.

**Notes:** The minutes reading and the meaning of the RAM terms are inferences, as for bms_remaining_time_4130. Helper bms_4168_0800113c is not yet described.

- Addresses by version: 4139: 0x08004618
- Called by: `bms_4168_0800c638`
- Calls: `bms_udiv32`, `bms_4168_0800113c`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_soc_band_classify

**Classify the state-of-charge value at +0x104 and set the mode code in the low bits of DAT_200005C0**

Reads the 16-bit value at state block +0x104, which is treated as a percentage with 100 meaning full, and sets the low three bits of DAT_200005C0 as a mode code. A value above 99 is forced to 100 and bits 0 and 1 are cleared, keeping bit 2. Otherwise, when the value is at or below the 16-bit limit at +0x11E the mode becomes 3 (bits 0 and 1 set, bit 2 cleared), and in all other cases it becomes 1 (bit 0 only).

**Notes:** The source tests (value - 80) > 19 as a signed comparison, so only values of 100 and above take the forced-100 branch; values from 80 to 99 fall through to the threshold test. The reading of +0x104 as state of charge is inferred from the value 100 and the bms_4148 use in bms_balance_timer_step.

- Addresses by version: 4130: 0x0800CCCC, 4139: 0x0800D2B4, 4148: 0x0800E2B4, 4168: 0x0800E748
- Called by: `bms_tail_call_unnamed_a`
- Calls: `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_soc_from_ocv_table

**Piecewise-linear 0-100 percent lookup from an 11-point table at 0x20000EB6**

Maps a value (param_1) through an 11-point table of ascending u16 breakpoints at 0x20000EB6 + 2k, k = 0 to 10. It returns 0 at or below the first breakpoint and 100 at or above the last (at 0x20000ECA). Between them it finds the segment k where the value is at most T[k], and returns 10 x (k-1) plus 10 times the position inside that segment, computed with bms_4168_0800113c as (x - T[k-1]) x 10 / (T[k] - T[k-1]). The result is stored at 0x200001DC and returned.

| Parameter | Type | Description |
|---|---|---|
| `x` | `u32` | param_1; compared with the breakpoints at 0x20000EB6..0x20000ECA |

**Returns** `u8`: 0 to 100 percent

**Notes:** The OCV-to-SOC reading comes from the 0-100 range in ten-percent segments; the unit of the input (probably a cell voltage) and the table source are not shown in the packet. Callers bms_4130_08005d2c and bms_4168_0800708c, 080071c8 and 08007348 are outside it.

- Addresses by version: 4130: 0x08005AC4, 4139: 0x08005CE0, 4148: 0x08006508, 4168: 0x08006674
- Called by: `bms_4168_0800708c`, `bms_4168_080071c8`, `bms_4168_08007348`
- Calls: `bms_4168_0800113c`
- Confidence: medium

## bms_state_refresh_scaled

**Refresh scaled measurement and derived-limit fields of the BMS state block at 0x20000BDC**

Reads raw RAM globals (0x20000E24, E26, E3A, E40, E44, E4C, E50, E54, E88, E94, EE8, EEC) and writes each into a fixed 16-bit field of the state block from bms_ram_20000bdc_addr, dividing by 10, 100 or 1000 with bms_udiv32 or the signed divider bms_4168_0800113c. The capacity pair 0x20000E30 and 0x20000E34 is recomputed from E88, the second scaled by 97 percent. The derating factor is a three-band curve on the 16-bit value at +0xB2 with a floor of 80 applied to +0x11C, and bit 1 of +0x196 is set when that floor clamps. The 16-bit value at 0x20000E26 is lowered to the field at +0x104 when bits 0 and 2 of the byte at 0x200005C0 are both set. Caller is bms_4168_0800c638.

**Notes:** Packed fields: +0x1D8 high byte receives the signed quotient of the value at +0x11A by 100 (negated when below -99); +0x1DA holds (k*8/10) in the high byte and (k*15/10) in the low byte, where k = (DAT_20000E50/10)/100. Whether 0x0800113c is signed division is inferred from its use with negative inputs.

- Addresses by version: 4130: 0x08005B74, 4139: 0x08005D9C, 4148: 0x080065C4, 4168: 0x08006730
- Called by: `bms_4168_0800c638`
- Calls: `bms_udiv32`, `bms_4168_0800113c`, `bms_ram_20000bdc_addr`, `bms_get_block_200005c0_ptr`
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
- Called by: `bms_4168_080068e8`
- Confidence: medium
