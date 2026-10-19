# BMS - `protection` functions

5 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_fault_class_get`](#bms_fault_class_get) | 0x0800A2BC | Priority-encode three RAM flags into a 0..3 class code |
| [`bms_level_hysteresis_update`](#bms_level_hysteresis_update) | 0x0800AACC | Two-threshold hysteresis from the level byte at 0x20000630 into the flag at 0x2000062F |
| [`bms_limit_derate_legacy_4130`](#bms_limit_derate_legacy_4130) | (removed) | Derate the two current limits and the gated output from one sampled reading and a SOC-like byte |
| [`bms_window_latch_narrow`](#bms_window_latch_narrow) | 0x080038C8 | Debounced latch for the narrow window (+8 < 40, +10 > 5); counts whole units while latched |
| [`bms_window_latch_wide`](#bms_window_latch_wide) | 0x08003954 | Debounced latch for the wide window (+8 < 55, +10 > -15); counts whole units while latched |

## bms_fault_class_get

**Priority-encode three RAM flags into a 0..3 class code**

Reads three byte flags at 0x2000068C, 0x2000068D and 0x2000068E and returns a class code by priority: 1 if 0x2000068C is nonzero; otherwise 2 if 0x2000068D is nonzero; otherwise 3 if 0x2000068E is nonzero; otherwise 0. It is read-only with no side effects. The priority order suggests the three flags are alarm or fault levels of decreasing severity, but the class names are not established in this packet.

**Returns** `u8`: 0 when none is set, else 1, 2 or 3 by priority

**Notes:** Callers: bms_4139_0800be74 and bms_4168_0800c96c.

- Addresses by version: 4130: 0x0800925C, 4139: 0x0800975C, 4148: 0x08009FA8, 4168: 0x0800A2BC
- Called by: `bms_4168_0800c96c`
- Confidence: medium

## bms_level_hysteresis_update

**Two-threshold hysteresis from the level byte at 0x20000630 into the flag at 0x2000062F**

Updates the flag byte at 0x2000062F from the level byte at 0x20000630. The flag is cleared when the level is below 2 and set when it is above 2. At exactly 2 the flag keeps its previous value, which is the hysteresis band. The updated flag is returned. The level's unit and the flag's role are not established in this packet.

**Returns** `u8`: the updated flag, 0 or 1

**Notes:** Callers: bms_4168_0800c4cc and bms_4168_0800c80c.

- Addresses by version: 4130: 0x08009B64, 4139: 0x0800A09C, 4148: 0x0800A7B8, 4168: 0x0800AACC
- Called by: `bms_4168_0800c4cc`, `bms_4168_0800c80c`
- Confidence: medium

## bms_limit_derate_legacy_4130

**Derate the two current limits and the gated output from one sampled reading and a SOC-like byte**

The signed 16-bit sample at param_2 selects a trapezoid factor f1 (0..100) between thresholds 0x20000D80..0x20000D83 with floor 0x20000D86, and a second factor f2 combines the sample with the byte at 0x20000CCC using floor 0x20000D87 and thresholds D83..D85. DAT_20000CF8 = f1*f2*DAT_20000D7D*DAT_20000D74/1000, clamped to 10 times DAT_20000D38. A third factor is 0 outside a dead band (0x20000D8A +/- one margin from bms_udiv32, edges D8A and D8C) and is otherwise reduced by slopes D8B below and D8D above; a fourth factor reduces by D8E per unit above 80 of the byte at 0x20000CCC. DAT_20000CF4 = f3*f4*D7D*D76/1000, clamped to 10 times DAT_20000D3A, and DAT_20000CFC = D8F*CF4/10 is forced to 0 unless the sample lies in [D88, D89). The sample unit is not established; it is probably a temperature.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | unused by the body in the decompile |
| `param_2` | `ptr` | pointer to a signed 16-bit reading (unit not established) |

**Notes:** No direct caller in this packet (entry point, callback or indirect). Helper bms_4168_0800aeac is called first with no result used; its role is not in this packet.

- Addresses by version: 4130: 0x08006830
- Called by: `bms_4168_0800c638`
- Calls: `bms_udiv32`, `bms_4168_0800113c`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_window_latch_narrow

**Debounced latch for the narrow window (+8 < 40, +10 > 5); counts whole units while latched**

Per-sample update of a time-debounced hysteresis latch. param_1 is a sample record: byte +0 is the time step added per call, byte +1 is an enable (0 clears all state and returns param_2 unchanged), and signed 16-bit readings at +8 and +10 are tested against the window, which is in-window when +8 < 40 and +10 > 5. Inside the window with the latch clear, or outside the 3-unit hysteresis band (+8 > 37 or +10 < 8), the timer DAT_20000608 is reset. Otherwise the timer accumulates the step, and at 30 the latch DAT_20000601 is cleared; outside the window the timer accumulates to 30 and then sets the latch and clamps the timer to 30. While the latch is set, the sub-accumulator DAT_2000060a adds the step and each time it exceeds 9 it subtracts 10 and increments param_2, so the return value counts whole tens of step units spent latched.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | sample record: +0 u8 step, +1 u8 enable, +8 s16 reading A (upper limit 40), +10 s16 reading B (lower limit 5) |
| `param_2` | `s32` | running count in units of 10 step units, returned incremented |

**Returns** `s32`: param_2 plus whole tens of latched time accumulated in this call

**Notes:** Readings A and B are probably max and min pack temperatures in degrees C, since 5..40 is a typical charge window; this is inferred from the thresholds only. The latch semantics are read from the control flow and are high confidence; the physical meaning is medium. Sibling of bms_window_latch_wide with the same algorithm and a different window.

- Addresses by version: 4130: 0x080038C8, 4139: 0x080038C8, 4148: 0x080038C8, 4168: 0x080038C8
- Called by: `bms_4168_0800e3bc`
- Confidence: medium

## bms_window_latch_wide

**Debounced latch for the wide window (+8 < 55, +10 > -15); counts whole units while latched**

Same algorithm as bms_window_latch_narrow with its own state: byte +0 is the time step, byte +1 the enable, and signed readings at +8 and +10 are tested against a wider window (in-window when +8 < 55 and +10 > -15). Hysteresis exits at +8 > 52 or +10 < -12, the latch threshold is 30 step units, and the state is held in DAT_20000600 (latch), DAT_20000604 (timer) and DAT_20000606 (sub-accumulator, carry at 10). Returns param_2 with whole tens of latched time added.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | sample record: +0 u8 step, +1 u8 enable, +8 s16 reading A (upper limit 55), +10 s16 reading B (lower limit -15) |
| `param_2` | `s32` | running count in units of 10 step units, returned incremented |

**Returns** `s32`: param_2 plus whole tens of latched time accumulated in this call

**Notes:** The window limits suggest a discharge-type window (-15..55 C) while the narrow one suggests charge (5..40 C); the readings are inferred as temperatures from the limits only.

- Addresses by version: 4130: 0x08003954, 4139: 0x08003954, 4148: 0x08003954, 4168: 0x08003954
- Called by: `bms_4168_0800e3bc`
- Confidence: medium
