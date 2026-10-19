# BMS - `soc` functions

3 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_charge_integrate_step`](#bms_charge_integrate_step) | 0x08006F90 | Integrate the signed current step into the charge counters, rolling over into hours and cycles |
| [`bms_state_refresh_scaled`](#bms_state_refresh_scaled) | 0x08006730 | Refresh scaled measurement and derived-limit fields of the BMS state block at 0x20000BDC |
| [`bms_tracking_filter_step`](#bms_tracking_filter_step) | 0x080072EC | One step of a dead-band tracking filter that slews an estimate toward a measurement |

## bms_charge_integrate_step

**Integrate the signed current step into the charge counters, rolling over into hours and cycles**

A sub-count accumulator at 0x20000EF8 is advanced by param_1 * 10 * current (state+0x11A) when param_2 is 0, or by -35 when param_2 is 1, with an extra -12 when the current is zero. Whole multiples of 10 move from 0x20000EF8 to 0x20000EFC, and whole multiples of 3600 (0xE10) move from 0x20000EFC into the estimate at 0x20000EEC, which is clamped to 0 when negative. When the current is above 10 and bit 2 of the 16-bit word at +0x124 is set, positive whole-3600 counts are added to the 32-bit word at +0x1BE; once it exceeds 97 percent of 0x20000E34 that threshold is subtracted, the 16-bit counter at +0xB2 is incremented and bit 0x80 is set in the flag word at 0x200001C8. The 32-bit word is stored back at +0x1BE and +0x1C0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | signed current step (scaled), multiplied by 10 before accumulation |
| `param_2` | `s32` | 1 selects the -35 offset update; any other value uses the current-proportional update |

**Notes:** The 3600-tick unit is assumed to be one hour if the tick is one second, which is a guess. The meaning of the +0xB2 counter as a cycle count is inferred from its use as the aging input in bms_4168_08006730.

- Addresses by version: 4139: 0x080064BC, 4148: 0x08006CE8, 4168: 0x08006F90
- Called by: `bms_4168_080068e8`, `bms_4168_08007348`
- Calls: `bms_udiv32`, `bms_4168_0800113c`, `bms_ram_20000bdc_addr`, `bms_ram_200001c8_addr`
- Confidence: medium

## bms_state_refresh_scaled

**Refresh scaled measurement and derived-limit fields of the BMS state block at 0x20000BDC**

Reads raw RAM globals (0x20000E24, E26, E3A, E40, E44, E4C, E50, E54, E88, E94, EE8, EEC) and writes each into a fixed 16-bit field of the state block from bms_ram_20000bdc_addr, dividing by 10, 100 or 1000 with bms_udiv32 or the signed divider bms_4168_0800113c. The capacity pair 0x20000E30 and 0x20000E34 is recomputed from E88, the second scaled by 97 percent. The derating factor is a three-band curve on the 16-bit value at +0xB2 with a floor of 80 applied to +0x11C, and bit 1 of +0x196 is set when that floor clamps. The 16-bit value at 0x20000E26 is lowered to the field at +0x104 when bits 0 and 2 of the byte at 0x200005C0 are both set. Caller is bms_4168_0800c638.

**Notes:** Packed fields: +0x1D8 high byte receives the signed quotient of the value at +0x11A by 100 (negated when below -99); +0x1DA holds (k*8/10) in the high byte and (k*15/10) in the low byte, where k = (DAT_20000E50/10)/100. Whether 0x0800113c is signed division is inferred from its use with negative inputs.

- Addresses by version: 4130: 0x08005B74, 4139: 0x08005D9C, 4148: 0x080065C4, 4168: 0x08006730
- Called by: `bms_4168_0800c638`
- Calls: `bms_udiv32`, `bms_4168_0800113c`, `bms_ram_20000bdc_addr`, `bms_get_block_200005c0_ptr`
- Confidence: medium

## bms_tracking_filter_step

**One step of a dead-band tracking filter that slews an estimate toward a measurement**

Moves the estimate DAT_20000eec one count toward the measurement DAT_20000ee8 with a dead-band accumulator. When the two differ, the step is the absolute difference masked to 20 bits and shifted right by 4, with a minimum of 5, signed toward the measurement, and it is added to the 16-bit accumulator DAT_200001f6. When the accumulator reaches 129 or more, the estimate is incremented and 128 is subtracted from the accumulator; when it reaches -129 or less, the estimate is decremented (clamped at 0) and 128 is added. Between those limits the estimate and accumulator are left alone, which is the dead band. No peripherals are touched.

**Notes:** Globals: DAT_20000ee8 read-only measurement, DAT_20000eec estimate (read/write), DAT_200001f6 accumulator (16-bit signed). The 20-bit mask and >>4 suggest a high-resolution ADC or AFE reading, but the quantity (SOC, current, voltage) is a guess.

- Addresses by version: 4139: 0x08006804, 4148: 0x08007030, 4168: 0x080072EC
- Called by: `bms_4168_080068e8`
- Confidence: medium
