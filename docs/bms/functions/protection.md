# BMS - `protection` functions

19 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_fault_class_get`](#bms_fault_class_get) | 0x0800A2BC | Priority-encode three RAM flags into a 0..3 class code |
| [`bms_fault_record_service`](#bms_fault_record_service) | 0x0800FABC | Run the fault sub-state handler with a 20-tick window, then commit the fault record to status bits |
| [`bms_fault_timers_step`](#bms_fault_timers_step) | 0x08003FCC | Advance the fault-timer accumulators by one step; return 1 when one passes its limit |
| [`bms_history_ring_commit`](#bms_history_ring_commit) | 0x08005CDC | Fill the history ring on first call; later calls commit staged blocks and queue a snapshot |
| [`bms_level_hysteresis_update`](#bms_level_hysteresis_update) | 0x0800AACC | Two-threshold hysteresis from the level byte at 0x20000630 into the flag at 0x2000062F |
| [`bms_limit_derate_legacy_4130`](#bms_limit_derate_legacy_4130) | (removed) | Derate the two current limits and the gated output from one sampled reading and a SOC-like byte |
| [`bms_profile_block_fill_4139`](#bms_profile_block_fill_4139) | (removed) | Fill the 4139 parameter block for profile id 0x20000016 (nine cases, default otherwise) |
| [`bms_profile_block_fill_4168`](#bms_profile_block_fill_4168) | 0x08004128 | Fill the 4168 parameter block for profile id 0x20000026 (13 ids, default set otherwise) |
| [`bms_profile_table_fill_4130`](#bms_profile_table_fill_4130) | (removed) | Write the 4130 table of 12-byte limit records and set the thresholds for profile id 0x20000014 |
| [`bms_profile_table_fill_4139`](#bms_profile_table_fill_4139) | (removed) | Fill the 4139 record table and threshold bytes for profile id 0x20000014 |
| [`bms_profile_table_fill_4168`](#bms_profile_table_fill_4168) | 0x08004488 | Fill the 4168 record table and threshold bytes for profile id 0x20000024 |
| [`bms_prot_debounce_quad`](#bms_prot_debounce_quad) | 0x0800C380 | Run four debounced protection timers over a measurement record and update latch bits |
| [`bms_prot_latch_pairs_update`](#bms_prot_latch_pairs_update) | 0x0800CE78 | Update seven debounced set/clear timer pairs and mirror the latch word into status bits |
| [`bms_prot_latch_pairs_update_alt`](#bms_prot_latch_pairs_update_alt) | (removed) | BMS_4130/4139 variant of the latch-pair update: seven timer pairs and latch word 0x2000019C |
| [`bms_protect_latch_evaluate`](#bms_protect_latch_evaluate) | 0x0800D2EC | Evaluate eight dwell-timed threshold latches and update protection status word 0x20000254 |
| [`bms_status_event_snapshot`](#bms_status_event_snapshot) | 0x08005AB0 | Maintain the status-flag byte at 0x2000056B and snapshot the state when a flag rises |
| [`bms_status_timeout_latch_4139`](#bms_status_timeout_latch_4139) | (removed) | Set a status flag after 2000 units of a low-value condition (4139 switch case body) |
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

## bms_fault_timers_step

**Advance the fault-timer accumulators by one step; return 1 when one passes its limit**

param_1 is the elapsed time added to each active accumulator. It reads the BMS status object at DAT_2000002C (u16 at +0x124 status bits, s16 at +0x11A, u16 at +0x19C, bit 0 of the byte at +0x194) and the object from bms_u32_20000dec_addr (u16 at +0x04). Five accumulators run while their conditions hold and clear when they fail: 0x20000048 and 0x2000004C for the +0x19C count below 10 and below 20 (limits 60,480,000 and 120,960,000); 0x20000058 for the count below 3 (limit 3,600,000), where the 0x124 bits 1 and 2 and the s16 below -49 decide resets; 0x20000054 while 0x124 bits 1 and 2 are clear and the object value is 3000 or less (limit 30,000); and 0x20000050 while 0x124 bit 4 is set and bit 2 is clear (limit 6,000). An accumulator that passes its limit is clamped and makes the function return 1. The 0x2000005C timer runs only while bit 3 of the byte at *DAT_20000030 is set: it drives PA15 low through gpio_pa15_reset and returns 1 after 200, and this function never resets it.

| Parameter | Type | Description |
|---|---|---|
| `elapsed` | `u32` | param_1; time added to every active accumulator this step |

**Returns** `bool`: 1 when a timer has expired, 0 otherwise

**Notes:** The limits read as milliseconds if the step is 1 ms (3600000 is one hour); that is an inference. The fields at +0x124, +0x194 and +0x19C are not labelled in the packet.

- Addresses by version: 4130: 0x080040B8, 4139: 0x08003F94, 4148: 0x08003FA0, 4168: 0x08003FCC
- Called by: `bms_4168_080082f0`
- Calls: `gpio_pa15_reset`, `bms_u32_20000dec_addr`
- Confidence: medium

## bms_history_ring_commit

**Fill the history ring on first call; later calls commit staged blocks and queue a snapshot**

Two-pass history routine for the buffers at 0x200010A8 to 0x200012FC. The first call (flag at 0x20000569 clear) sets the flag and fills ten 64-byte history records at stride 0x40 from 0x200010A8. Each holds a timestamp from bms_4168_08009d84, 13 u16 words from status +0x140, the s16 at +0x11A, six low bytes from the u16 words at +0x12C, +0x12E, +0x130, +0x134, +0x136 and +0x138, the bytes at +0x11E and +0x19C, the 0x124/0x126 and 0x194/0x196 words, and the words at +0x13C, +0x13E, +0x180 and +0x1D2. Later calls copy nine 64-byte blocks from 0x200010FC to 0x200010BC, store a current snapshot at 0x200012FC to 0x20001331 in the same field order, and count DAT_2000056A. After five counts with a pending snapshot it clears DAT_20000568 and hands the snapshot at 0x200010A8 to bms_slot_pool_register with tag 5.

**Notes:** The record layout is inferred from the stores. The first-call records overlap the snapshot written by bms_status_event_snapshot at 0x200010A8, and the packet does not show how the two layouts line up. Tag 5 is not identified.

- Addresses by version: 4130: 0x08005460, 4139: 0x0800567C, 4148: 0x08005B88, 4168: 0x08005CDC
- Called by: `bms_4168_0800a8a0`
- Calls: `memcpy`, `bms_rtc_datetime_pack`, `bms_slot_pool_register`, `bms_ram_20000bdc_addr`
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

## bms_profile_block_fill_4139

**Fill the 4139 parameter block for profile id 0x20000016 (nine cases, default otherwise)**

Chooses one parameter set from the profile id at DAT_20000016: ids 0, 2, 3, 4, 5, 6, 7 and 8 each have their own values, and every other id (including 1) takes the default set. The set supplies a capacity-like constant (values 5100 to 19200), used directly and divided by 10 into DAT_2000001C+0x26, several 16-bit limits (values such as 255, 765, 800 and 1200), and smaller fields stored into the block returned by FUN_0800C0D0 at offsets 0x2C, 0x30, 0x34, 0x38, 0x3A, 0x3C, 0x3E, 0x74, 0x76 and 0x7D. It copies three 11-entry u16 tables from RAM into the block at +0x00, +0x16 and +0x5E, chosen by id group (0-4, 6-8, or other). Fixed bytes go to +0x80 to +0x8F; only +0x81 and +0x87 differ between the 6-8 group and the rest.

**Notes:** The values are constants from this code, not measurements, and the units of the capacity-like value and of the block are not in the packet. Sibling fills: bms_profile_block_fill_4168, bms_profile_table_fill_4130 and bms_profile_table_fill_4139, which have different record layouts.

- Addresses by version: 4139: 0x080040E4
- Called by: `bms_4168_08003cc0`
- Calls: `bms_udiv32`, `bms_get_block_20000e58_ptr`
- Confidence: medium

## bms_profile_block_fill_4168

**Fill the 4168 parameter block for profile id 0x20000026 (13 ids, default set otherwise)**

Picks one of nine sets from the profile id at DAT_20000026: ids 4 and 12 share a set, 3 and 11 share one (differing only in the byte at +0x3E, 7 or 6), 2 and 10 share one (byte at +0x3E 8 or 2), and 9, 0, 8, 6, 5 and 7 each have their own; any other id takes the default. Each set supplies a capacity-like value (5100 to 19200, used directly and divided by 10 into DAT_2000002C+0x26), 16-bit limits and small fields at +0x2C, +0x34, +0x38, +0x3A, +0x3C, +0x3E, +0x74 and +0x7D of the block returned by FUN_0800CE5C. It copies three 11-entry u16 tables for the id group (0-4, 6-8, 9-10, 11-12, or other) into +0x00, +0x16 and +0x5E. Fixed bytes go to +0x80 to +0x8F; +0x81, +0x82, +0x83 and +0x87 differ between the 6-8 group and the rest.

**Notes:** Same role as bms_profile_block_fill_4139 for the 4168 build, with a different id-to-set mapping and different fixed bytes. The meaning of the capacity-like value is not in the packet.

- Addresses by version: 4148: 0x080040FC, 4168: 0x08004128
- Called by: `bms_4168_08003cc0`
- Calls: `bms_udiv32`, `bms_get_block_20000e58_ptr`
- Confidence: medium

## bms_profile_table_fill_4130

**Write the 4130 table of 12-byte limit records and set the thresholds for profile id 0x20000014**

Fills 17 records through bms_record12_addr (FUN_0800BAE0). Fourteen of them (1, 2, 3, 5, 7, 9, 10, 0x0C, 0x0F, 0x16, 0x18, 0x1D, 0x1F and 0x21) are fixed u16 pairs with u32 words of 4000 or 10000, while records 0x11, 0x2B and 0x30 are derived from the status block. The profile id at DAT_20000014 selects threshold values stored in the status block: +0x52 and +0x86/+0x88 for id 5 or other ids, and +0x6C/+0x70/+0x76 for groups (4-5), (3), (2), (0) and other. Record 0x11 copies +0x86 and +0x88, record 0x2B takes +0x6C and +0x6C-2, and record 0x30 takes -(+0x70) and 2-(+0x70). The routine only writes.

**Notes:** The purpose of individual records is not stated in the packet. The 4000 and 10000 words are probably limits or durations, which is an inference. The 4139 counterpart is bms_profile_table_fill_4139, which writes its threshold to +0x192 rather than +0x52.

- Addresses by version: 4130: 0x08004208
- Called by: `bms_4168_08003cc0`
- Calls: `bms_record12_addr`
- Confidence: medium

## bms_profile_table_fill_4139

**Fill the 4139 record table and threshold bytes for profile id 0x20000014**

Fills 18 records through bms_record12_addr for the 4139 build (its accessor is FUN_0800C0B0). Records 2 and 3 take 4000 as the second word for ids 6, 7 and 8 and 0x1004 otherwise; record 0x12 copies +0x86 and +0x88; records 0x2C and 0x31 are derived from the status block; the rest are fixed pairs with u32 words of 4000 or 10000. The profile id at DAT_20000014 sets +0x86 and +0x88 (0x35 and 0x30 for ids 5 to 8, 0x3A and 0x35 otherwise) and the threshold at +0x192 (0x17C for id 5, 400 otherwise), and sets +0x6C, +0x70 and +0x76 by group: (4-5), (3, 6, 8), (2, 7), (0) and other. Records 0x2C and 0x31 take +0x6C and -(+0x70) as in the 4130 table.

**Notes:** Same structure as bms_profile_table_fill_4130 with different ids, record numbers and offsets. The purpose of individual records is not stated in the packet.

- Addresses by version: 4139: 0x08004388
- Called by: `bms_4168_08003cc0`
- Calls: `bms_record12_addr`
- Confidence: medium

## bms_profile_table_fill_4168

**Fill the 4168 record table and threshold bytes for profile id 0x20000024**

Fills 20 records through bms_record12_addr for the 4168 build (accessor FUN_0800CE3C). The record at index 1 takes 0x35 for id 5 and 0x2D otherwise, and record 2 takes 0xFD2 for id 5 and 0x1036 otherwise; record 0x12 copies +0x86 and +0x88, records 0x2C, 0x2B and 0x31 are derived from the status block (0x2C from +0x6C, 0x2B and 0x31 from +0x70), and the rest are fixed pairs. The profile id at DAT_20000024 sets +0x86 and +0x88 (0x35 and 0x30 for ids 6 to 8, 0x3A and 0x35 otherwise) and +0x192 (0x17C for id 5, 400 otherwise), and +0x6C, +0x70 and +0x76 by group: (4-5), (3, 6, 8), (2, 7), (0) and other. The routine only writes records and status fields.

**Notes:** Sibling of bms_profile_table_fill_4139 and bms_profile_table_fill_4130 with a different id mapping and record set. The purpose of each record is not stated in the packet.

- Addresses by version: 4148: 0x080043A4, 4168: 0x08004488
- Called by: `bms_4168_08003cc0`
- Calls: `bms_record12_addr`
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

## bms_status_event_snapshot

**Maintain the status-flag byte at 0x2000056B and snapshot the state when a flag rises**

Keeps a flag byte at 0x2000056B that mirrors status bits with hysteresis. Bits 0 and 1 form a two-bit state for the 0x124 bit 2 condition (armed by DAT_20000DDC and s16 +0x11A of at least 10); bit 2 mirrors 0x124 bit 4, bit 3 mirrors 0x124 bit 3, bit 4 mirrors 0x124 bits 7 to 10 and 12, bit 5 mirrors 0x124 bits 5 and 6 and 0x126 bit 2, bit 6 mirrors 0x124 bits 13 and 14, and bit 7 mirrors 0x126 bits 4, 7, 8 and 12. When any flag rises and the pending slot DAT_20000568 is clear, it writes a snapshot at 0x200010A8: the flag byte, a 32-bit timestamp from bms_4168_08009d84, the u16 at +0x118, the s16 at +0x11A, a byte from the object at 0x20000DFC, the u16 words at +0xB4 and +0xB6, and the 0x124/0x126 pair as one word.

**Notes:** The bit mapping is read from the shift tests, so the status-bit names are not given in the packet. The snapshot layout is as stored and the field meanings are inferred.

- Addresses by version: 4130: 0x0800524C, 4139: 0x08005468, 4148: 0x08005964, 4168: 0x08005AB0
- Called by: `bms_4168_0800a8a0`
- Calls: `bms_rtc_datetime_pack`, `bms_ram_20000bdc_addr`, `bms_u16_20000dfc_addr`
- Confidence: medium

## bms_status_timeout_latch_4139

**Set a status flag after 2000 units of a low-value condition (4139 switch case body)**

This is a case body of a switch (decompiler label switchD_0800c0e2::caseD_2); the dispatcher is not in this packet. It reads the status object from the 0x20000BDC accessor. When byte +0x194 bit 5 is set and the s16 at +0x11A is 4 or less, it adds param_1 to the accumulator at 0x20000D18 and returns until that accumulator reaches 2000; if the s16 is above 4 it clears the accumulator and returns. When bit 5 is clear, or the accumulator reaches 2000, it clears bit 2 and sets bit 0 of the u16 at +0x124 and sets 0x20000D24 to 1. The result is a latched status flag after a sustained condition.

| Parameter | Type | Description |
|---|---|---|
| `elapsed` | `s32` | param_1; time added to the accumulator |

**Notes:** Because the decompiled structure runs the flag set when bit 5 is clear, the delay applies only in the bit-5-set case. The switch dispatcher and the meaning of bit 0 of +0x124 are not in the packet.

- Addresses by version: 4130: 0x08005748, 4139: 0x08005964
- Called by: `bms_4168_0800ce64`
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
