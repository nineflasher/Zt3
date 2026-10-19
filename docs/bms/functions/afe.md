# BMS - `afe` functions

1 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_sample_window_process`](#bms_sample_window_process) | 0x0800E3BC | Update wide and narrow window latches, derate and scale a sample into the 0x200024CC result block |

## bms_sample_window_process

**Update wide and narrow window latches, derate and scale a sample into the 0x200024CC result block**

Processes one measurement record and returns a pointer to the result block at 0x200024CC. It runs bms_window_latch_wide and bms_window_latch_narrow on the record, keeping their states in DAT_200024DC and DAT_200024E0, and stores the result of bms_4168_0800379c in the low half of DAT_200024CC. The 16-bit value at record+6 selects a per-mille factor: 1000 below 20, 1000 - v/2 for 20 to 99, 975 - v/4 for 100 to 199 and 950 - v/8 from 200 upwards; the 16-bit value at +0x10 times that factor, divided by 1000 through bms_4168_0800113c, goes to the high half of DAT_200024CC. A rising edge of the byte at record+3 (tracked in DAT_20000602) increments the 16-bit counter DAT_200024D0. Finally DAT_200024D4 receives bms_4168_08003868 of the record and DAT_200024D8 receives (DAT_200024D4 * (value at +0x12 / 100)) / 1000 through bms_udiv32.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | measurement record: byte +3 event flag, 16-bit +6 scaling input, +0x10 and +0x12 values, +8 and +10 window inputs |
| `param_2` | `u32` | unused by this function |
| `param_3` | `u32` | passed through to bms_window_latch_wide |
| `param_4` | `u32` | passed through to bms_window_latch_wide (twice) |

**Returns** `ptr`: pointer to the result block at 0x200024CC

**Notes:** The units of the record fields and the derating curve's meaning are not identified. The callees bms_4168_0800379c, bms_4168_0800113c and bms_4168_08003868 are not yet described in the packet.

- Addresses by version: 4130: 0x0800C96C, 4139: 0x0800CF68, 4148: 0x0800DF68, 4168: 0x0800E3BC
- Called by: `bms_4168_08007a0c`
- Calls: `bms_udiv32`, `bms_4168_0800113c`, `bms_banded_offset_compute`, `bms_throughput_accumulate`, `bms_window_latch_narrow`, `bms_window_latch_wide`
- Confidence: medium
