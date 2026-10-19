# MCU - `protection` functions

11 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_cond_mode_bit0_and_level_ok`](#mcu_cond_mode_bit0_and_level_ok) | 0x08004B1C | Return 1 if mode bit0 of 0x2000065d is set and 0x200003ea is at least 10 above both thresholds |
| [`mcu_f30_range_latch`](#mcu_f30_range_latch) | 0x08006580 | Latch flag 0x2000010F from the magnitude of the s32 at 0x20000F30; argument 0 clears the latch |
| [`mcu_fault_norm_sq_debounce_check`](#mcu_fault_norm_sq_debounce_check) | 0x080062F0 | Return 0 when the squared magnitude of (+0x18, +0x1C) exceeds the limit at +0x3C |
| [`mcu_flag_1fce_is_clear`](#mcu_flag_1fce_is_clear) | 0x08004E64 | Return 1 if the byte at 0x20001fce is zero, else 0 |
| [`mcu_limit_ramp_update`](#mcu_limit_ramp_update) | (removed) | Update a ramped limit (halve/x1.2 on flag change, +0x1999 per call) and clamp an output |
| [`mcu_status_bf4_any_low_bits`](#mcu_status_bf4_any_low_bits) | 0x08003624 | Return 1 if either of the low two bits of status byte 0x20000bf4 is set |
| [`mcu_threshold_debounce_init_v12b`](#mcu_threshold_debounce_init_v12b) | (removed) | Initialise a 12b threshold debounce object: thresholds, mode, counter limits, clear state |
| [`mcu_threshold_debounce_update_v12b`](#mcu_threshold_debounce_update_v12b) | (removed) | Debounce an upper and/or lower threshold with per-side counters and latched trip flags (12b) |
| [`mcu_threshold_monitor_init_std`](#mcu_threshold_monitor_init_std) | 0x080084DC | Initialise the 143/152/0160 threshold monitor object with limits, reload values and mode |
| [`mcu_threshold_monitor_update_std`](#mcu_threshold_monitor_update_std) | 0x0800844C | Update thresholds and run upper/lower trip monitor with reload counters and hysteresis (143/152/0160) |
| [`mcu_update_inhibit_latch_1fcd`](#mcu_update_inhibit_latch_1fcd) | 0x0800B2C0 | Set or clear the drive-inhibit latch at 0x20001fcd from fault flags and the value at 0x20000f30 |

## mcu_cond_mode_bit0_and_level_ok

**Return 1 if mode bit0 of 0x2000065d is set and 0x200003ea is at least 10 above both thresholds**

True when (DAT_2000065d & 1) != 0 and both signed 16-bit thresholds DAT_20000024 and DAT_20000026 are <= DAT_200003ea - 10 (a 10-count hysteresis/margin). 0x2000065d is a mode/status byte also used by mcu_0160_08004b54 (bit1) and mcu_0160_08005550 (bit2 and bits 3..4). Called from mcu_0160_08003f2c, 0800480c, 08004944, 0800a320 and 0800e238.

**Returns** `bool`: 1 if condition met

**Notes:** Operands are probably a measured value compared with two limits; unknown which.

- Addresses by version: 12b: 0x0800499C, 143: 0x08004990, 152: 0x08004A7C, 0160: 0x08004B1C
- Called by: `mcu_0160_08003f2c`, `mcu_0160_0800480c`, `mcu_0160_08004944`, `mcu_0160_0800a320`, `mcu_0160_0800e238`
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

## mcu_flag_1fce_is_clear

**Return 1 if the byte at 0x20001fce is zero, else 0**

Logical-not of DAT_20001fce, returned as 0/1. Callers mcu_0160_080056e4, 08008a14, 0800adf0 and 0800b10c use it as a gating condition (the byte is likely a fault/disable flag). Highly likely 'not faulted/enabled' semantics, but unproven.

**Returns** `bool`: 1 if DAT_20001fce == 0

**Notes:** Name chosen neutrally; byte meaning unknown.

- Addresses by version: 12b: 0x08004CE4, 143: 0x08004CD8, 152: 0x08004DC4, 0160: 0x08004E64
- Called by: `mcu_0160_080056e4`, `mcu_0160_08008a14`, `mcu_0160_0800adf0`, `mcu_0160_0800b10c`
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

## mcu_status_bf4_any_low_bits

**Return 1 if either of the low two bits of status byte 0x20000bf4 is set**

Normalises (DAT_20000bf4 & 3) to a boolean. The byte is a state/fault bitfield; callers are the main control routines mcu_0160_08003f2c, 080052bc and 08005978. Which conditions bits 0 and 1 stand for is unknown.

**Returns** `bool`: 1 if bit0 or bit1 set, else 0

**Notes:** Bit semantics unknown.

- Addresses by version: 12b: 0x080036E4, 143: 0x080035E4, 152: 0x08003584, 0160: 0x08003624
- Called by: `mcu_0160_08003f2c`, `mcu_0160_080052bc`, `mcu_0160_08005978`
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
- Called by: `mcu_12b_080059ec`, `mcu_12b_08005a80`
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
- Called by: `mcu_0160_08005a00`, `mcu_0160_08005ab0`
- Confidence: high

## mcu_update_inhibit_latch_1fcd

**Set or clear the drive-inhibit latch at 0x20001fcd from fault flags and the value at 0x20000f30**

Recomputes a one-byte latch at 0x20001fcd, where 1 means inhibit and 0 means allowed. The allow predicate is: (bit 2 of byte 0x20001fd4 is clear, or (bytes 0x20001fd2 and 0x20001fd3 are both zero and (bit 2 of 0x20001fe2 is clear or 0x20000f30 < 0x28001))) AND (flag 0x20000e32 is zero or 0x20000f30 < 0x10000). If the predicate is false the latch is set to 1. If it is true and 0x20000f30 < 0x10000 the latch is cleared to 0; if it is true and the value is at or above 0x10000 the latch is left unchanged. Flag 0x20000e32 is the one set by mcu_update_flag_e32_from_mode_3 (mode byte equal to 3).

**Notes:** The constants 0x10000 (1.0 in Q16) and 0x28001 (just above 2.5 in Q16) suggest 0x20000f30 is a Q16 quantity such as speed, voltage or current; not confirmed. The individual flags at 0x20001fd2 to 0x20001fe2 are unknown.

- Addresses by version: 12b: 0x0800B054, 143: 0x0800B2E4, 152: 0x0800B260, 0160: 0x0800B2C0
- Called by: `mcu_0160_0800a320`
- Confidence: medium
