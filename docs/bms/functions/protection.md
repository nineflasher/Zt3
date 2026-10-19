# BMS - `protection` functions

10 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_fault_class_get`](#bms_fault_class_get) | 0x0800A2BC | Priority-encode three RAM flags into a 0..3 class code |
| [`bms_fault_record_service`](#bms_fault_record_service) | 0x0800FABC | Run the fault sub-state handler with a 20-tick window, then commit the fault record to status bits |
| [`bms_level_hysteresis_update`](#bms_level_hysteresis_update) | 0x0800AACC | Two-threshold hysteresis from the level byte at 0x20000630 into the flag at 0x2000062F |
| [`bms_limit_derate_legacy_4130`](#bms_limit_derate_legacy_4130) | (removed) | Derate the two current limits and the gated output from one sampled reading and a SOC-like byte |
| [`bms_prot_debounce_quad`](#bms_prot_debounce_quad) | 0x0800C380 | Run four debounced protection timers over a measurement record and update latch bits |
| [`bms_prot_latch_pairs_update`](#bms_prot_latch_pairs_update) | 0x0800CE78 | Update seven debounced set/clear timer pairs and mirror the latch word into status bits |
| [`bms_prot_latch_pairs_update_alt`](#bms_prot_latch_pairs_update_alt) | (removed) | BMS_4130/4139 variant of the latch-pair update: seven timer pairs and latch word 0x2000019C |
| [`bms_protect_latch_evaluate`](#bms_protect_latch_evaluate) | 0x0800D2EC | Evaluate eight dwell-timed threshold latches and update protection status word 0x20000254 |
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

## bms_fault_record_service

**Run the fault sub-state handler with a 20-tick window, then commit the fault record to status bits**

Takes the fault record at 0x2000068F and runs the handler at index DAT_20001C8A of the function table at 0x080108A8 repeatedly while it returns 1, giving up after 20 ticks from DAT_20001C7C (on timeout it sets DAT_20001C8B and commits). The commit updates the record: when byte 0 is nonzero, byte 1 equal to 1 clears bytes 0 and 2, and a byte 0 above 9 saturates it to 10 and sets byte 2 to 1, so byte 0 acts as a debounce counter that latches as confirmed. It then copies bit 0 of byte 3 into bit 15 of the state block word at +0x126, bit 0 of byte 2 into bit 14 of +0x196, and bits 0, 1 and 2 of byte 4, byte 5 and byte 1 into bits 0 to 2 of +0x19A.

**Notes:** The record field meanings are inferred from their use. The table contents at 0x080108A8 are not visible in this packet. bms_seq_state_reset sets up the variables used here.

- Addresses by version: 4130: 0x0800DDCC, 4139: 0x0800E420, 4148: 0x0800F5DC, 4168: 0x0800FABC
- Called by: `bms_tail_call_unnamed_b`
- Calls: `bms_ram_2000068f_addr`, `bms_tick_get`, `bms_tick_timeout_check`, `bms_ram_20000bdc_addr`
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

The signed 16-bit sample at sample selects a trapezoid factor f1 (0..100) between thresholds 0x20000D80..0x20000D83 with floor 0x20000D86, and a second factor f2 combines the sample with the byte at 0x20000CCC using floor 0x20000D87 and thresholds D83..D85. DAT_20000CF8 = f1*f2*DAT_20000D7D*DAT_20000D74/1000, clamped to 10 times DAT_20000D38. A third factor is 0 outside a dead band (0x20000D8A +/- one margin from bms_udiv32, edges D8A and D8C) and is otherwise reduced by slopes D8B below and D8D above; a fourth factor reduces by D8E per unit above 80 of the byte at 0x20000CCC. DAT_20000CF4 = f3*f4*D7D*D76/1000, clamped to 10 times DAT_20000D3A, and DAT_20000CFC = D8F*CF4/10 is forced to 0 unless the sample lies in [D88, D89). The sample unit is not established; it is probably a temperature.

| Parameter | Type | Description |
|---|---|---|
| `unused_arg` | `u32` | unused by the body in the decompile |
| `sample` | `ptr` | pointer to a signed 16-bit reading (unit not established) |

**Notes:** No direct caller in this packet (entry point, callback or indirect). Helper at 0x0800AEAC (id unresolved: not a function in any BMS build) is called first with no result used; its role is not in this packet.

- Addresses by version: 4130: 0x08006830
- Called by: `bms_4168_0800c638`
- Calls: `bms_udiv32`, `bms_4168_0800113c`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_prot_debounce_quad

**Run four debounced protection timers over a measurement record and update latch bits**

Per-tick evaluator for four debounced conditions. param_2 points to the sampled 16-bit measurements (fields at +2, +4, +6 and +0x12), and param_3 is the elapsed time added to the timers. Each timer (DAT_200004CC, DAT_200004D0, DAT_200004D4, DAT_200004D8) accumulates param_3 while its trigger test holds and resets to 0 otherwise, and is held at 0 while its own latch bit is set. When the first timer reaches DAT_200004E0 it clamps, sets 0x100 in the status word at +0x126 and sets 0x10 in DAT_200004C8. The second timer uses DAT_200004EC and sets 0x80 at +0x126 and 0x20 in DAT_200004C8, while the third, against DAT_200004F8, sets 0x2 in DAT_200004C8 and 0x2000 at +0x124. The fourth, against DAT_200004FC, clears that 0x2 latch and the 0x2000 status bit once the condition has cleared.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | not used by the routine |
| `param_2` | `ptr` | sampled measurement record with 16-bit fields at +2, +4, +6 and +0x12 |
| `param_3` | `s32` | elapsed time added to each accumulator per call |

**Notes:** The trigger thresholds (DAT_200004DC, E4, E8, F0, F4, F5) and the meanings of the sampled fields are not identified in this packet. Latch bits 0x10 and 0x20 are set here and never cleared here. The object is from bms_ram_20000bdc_addr.

- Addresses by version: 4130: 0x0800B330, 4139: 0x0800B888, 4148: 0x0800C06C, 4168: 0x0800C380
- Called by: `bms_4168_08007a0c`
- Calls: `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_prot_latch_pairs_update

**Update seven debounced set/clear timer pairs and mirror the latch word into status bits**

Per-tick fault-latch engine for all four firmware builds. It first copies four flag bits from param_2 (bits 5, 4, 3 and 2) into the latch word DAT_20000258 as 0x4, 0x40, 0x800 and 0x8000. It then runs seven set/clear timer pairs with accumulators from DAT_20000F90 to DAT_20001024, in 8-byte pairs, each pair latching a bit in DAT_20000258 (0x2, 0x10, 0x400, 0x2000, 0x80000, 0x200000 or 0x800000). A pair's set timer accumulates param_3 while its trigger test holds and latches when it reaches its limit, and its clear timer releases the latch the same way. Each pair is held off while its own latch bit is set. Finally it rewrites the bit fields of the status halfwords at +0x124, +0x126, +0x196 and +0x198 of the object from bms_ram_20000bdc_addr from the latch word.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | sampled measurement record with 16-bit fields at +2, +4, +6, +8 and +0x12 |
| `param_2` | `s32` | flag word; bits 2 to 5 are the four input flags |
| `param_3` | `s32` | elapsed time added to each accumulator per call |

**Notes:** Pair thresholds and the exact trigger tests are not identified, and the bit mapping of the rewritten status fields is only partly decoded. Consumers of the status bits are outside this packet.

- Addresses by version: 4130: 0x0800BB1C, 4139: 0x0800C0EC, 4148: 0x0800CA90, 4168: 0x0800CE78
- Called by: `bms_4168_08007a0c`
- Calls: `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_prot_latch_pairs_update_alt

**BMS_4130/4139 variant of the latch-pair update: seven timer pairs and latch word 0x2000019C**

Per-tick fault evaluator for the BMS_4130 and BMS_4139 builds, structured like bms_prot_latch_pairs_update but with its own sensor set. It takes a status record (param_1, with 16-bit fields at +2 and +4), a sample record (param_2, with words at +0, +4 and +8 and a 16-bit field at +0xE), the flag word param_3 and the elapsed time param_4. Flag bit 0 sets latch 0x8 and bit 1 sets 0x1000 in DAT_2000019C. Seven set/clear timer pairs at DAT_20000E24 to DAT_20000E80 latch the bits 0x2, 0x40, 0x400, 0x4000, 0x20000 and 0x80000 in that word, with the first two pairs sharing latch 0x2. In modes 6, 7 and 8 of DAT_20000014, a hysteresis on the field at param_1+2 (below 6 selects DAT_2000020C, from 6 to 10 keeps the previous choice, above 10 selects DAT_20000200) chooses the threshold; other modes use DAT_20000200. The latch word is written back into the status halfwords at +0x124, +0x126, +0x194 and +0x198.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | status record with 16-bit fields at +2 and +4 |
| `param_2` | `ptr` | sample record with u32 words at +0, +4 and +8 and a 16-bit field at +0xE |
| `param_3` | `u32` | flag word; bit 0 sets latch 0x8, bit 1 sets latch 0x1000 |
| `param_4` | `s32` | elapsed time added to each accumulator per call |

**Notes:** Threshold and sensor meanings are not identified in this packet. Callers are bms_4139_08006f08 only. The helper FUN_0800B3E4 is taken to be bms_ram_20000bdc_addr for this build.

- Addresses by version: 4130: 0x0800BF8C, 4139: 0x0800C560
- Called by: `bms_4139_08006f08`
- Calls: `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_protect_latch_evaluate

**Evaluate eight dwell-timed threshold latches and update protection status word 0x20000254**

Runs the protection latch engine once per call over eight channels. Each channel has a trigger timer and a release timer (accumulators at 0x20000F20 to 0x20000F7C): while the channel's measurement is on its arming side of the threshold pair the trigger timer adds param_4, and when it reaches the channel limit the channel's status bit is set and the timer is clamped (bits 0x10, 0x02, 0x40, 0x200, 0x400, 0x4000, 0x20000 and 0x80000 for channels 1 to 8). A set latch clears through its release timer while the measurement is on the release side, and the clear masks also drop bits 0x04 and 0x08 that channels 1 and 2 share. Param_3 bit 0 sets status 0x08 and bit 1 sets status 0x1000 directly. At the end the status word is mirrored into the BMS state block: bits 1 to 8 into bit 3 of the 16-bit word at +0x124, bits 10 to 16 into bit 4 of +0x124, bits 19 to 22 into bit 4 of +0x126, bit 17 into bit 11 of +0x194, and bits 0, 9 and 18 into bits 4, 7 and 8 of +0x198.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | measurement record: 16-bit values at +2 and +4 (+4 is the channel 1 input, +2 selects channel 5 thresholds) |
| `param_2` | `ptr` | measurement record: 32-bit value at +0, 16-bit values at +4, +8 and +0xE |
| `param_3` | `u32` | flag word: bit 0 sets status 0x08, bit 1 sets status 0x1000 |
| `param_4` | `s32` | elapsed ticks added to the dwell timers while a channel is armed |

**Notes:** Which measurement is compared against which limit and the threshold units are not identified; the arming side comes from the compares. Channel 5 picks its threshold from DAT_20000024 (values 6 to 8) and the sticky flag DAT_20000250. The accumulators 0x20000F20 to 0x20000F7C are not in this packet's RAM reference list and were taken from the decompile.

- Addresses by version: 4148: 0x0800CF04, 4168: 0x0800D2EC
- Called by: `bms_4168_08007a0c`
- Calls: `bms_ram_20000bdc_addr`
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
- Called by: `bms_sample_window_process`
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
- Called by: `bms_sample_window_process`
- Confidence: medium
