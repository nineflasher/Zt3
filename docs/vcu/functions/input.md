# VCU - `input` functions

5 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`vcu_input_sm_a_tick`](#vcu_input_sm_a_tick) | 0x08007E28 | Debounce state machine A: advance the input-A presence states once per tick |
| [`vcu_input_sm_b_tick`](#vcu_input_sm_b_tick) | 0x0800809C | Debounce state machine B for input B (qualifier FUN_08006994) with a 150-tick hold state |
| [`vcu_input_sm_c_tick`](#vcu_input_sm_c_tick) | 0x08008144 | Debounce state machine C (qualifier FUN_08007ab8) with a 150-tick hold state |
| [`vcu_input_sm_d_tick`](#vcu_input_sm_d_tick) | 0x080081EC | Debounce state machine D on the GPIOB pin-10/pin-2 read, with status bit f92[12] |
| [`vcu_input_sm_e_tick`](#vcu_input_sm_e_tick) | 0x080082B4 | Debounce state machine E on the GPIOB pin-10/pin-2 read, with status bit f92[13] |

## vcu_input_sm_a_tick

**Debounce state machine A: advance the input-A presence states once per tick**

Periodic tick of input state machine A. The qualifier FUN_080056e8 (not yet described) is sampled; nonzero means the input is present. Present ticks only act after the armed latch DAT_200014c8 has been set by an earlier absent tick: the presence counter DAT_200014e0 (saturates at 10000) increments, and once the old value exceeds 4 the state DAT_200021b8 goes 0 -> 6, or 7 -> 8 while the new count is 3..24. Absent ticks clear the presence counter, set the armed latch, count absent ticks in DAT_200014e2, move 6 -> 7 and 8 -> 2, and after more than 9 absent ticks a machine in state 7 latches state 1 and sets the shared event flag DAT_20001fbc, while any other state falls back to 0.

**Notes:** The physical input is not identified; FUN_080056e8 is not yet described. State 1 is an event latch; DAT_20001fbc is also set by the other input machines (vcu_input_sm_b_tick to vcu_input_sm_e_tick). No 150-tick long-hold state exists in this machine, unlike B to E.

- Addresses by version: 148: 0x08007438, 14a: 0x08007874, 14b: 0x08007BD8, 14e: 0x08007C10, 14f: 0x08007C6C, 152: 0x08007D30, 153: 0x08007DCC, 0159: 0x08007E28
- Called by: `vcu_0159_080069b4`, `vcu_0159_080088f4`, `vcu_0159_0800a5c8`
- Calls: `vcu_pb13_input_active_low`
- Confidence: medium

## vcu_input_sm_b_tick

**Debounce state machine B for input B (qualifier FUN_08006994) with a 150-tick hold state**

Periodic tick of input state machine B. The qualifier FUN_08006994 (not yet described) is sampled; nonzero means present. Present: the counter DAT_200014cc (saturating at 10000) increments; when the old value exceeded 4 the state DAT_200021c1 goes 0 -> 6, goes 7 -> 8 while the new count is 3..19, and a new count of 150 (0x96) forces state 3 from any state. Absent: DAT_200014cc clears, DAT_200014ce counts absent ticks, 6 -> 7 and 8 -> 2 happen, more than 9 absent ticks in state 7 latch state 1 and set DAT_20001fbc, and more than 9 in any other state drops the machine to 0. State 3 is the long-hold state read by vcu_input_b_hold_start_tick (0x08009094).

**Notes:** The physical input behind FUN_08006994 is unknown. Thresholds (4, 3..19, 150) are read from the compare constants in the decompile.

- Addresses by version: 148: 0x080076B8, 14a: 0x08007AF4, 14b: 0x08007E4C, 14e: 0x08007E84, 14f: 0x08007EE0, 152: 0x08007FA4, 153: 0x08008040, 0159: 0x0800809C
- Called by: `vcu_0159_0800193c`, `vcu_0159_0800673c`, `vcu_0159_080069b4`, `vcu_0159_080088f4`
- Calls: `vcu_pb11_input_active_low`
- Confidence: medium

## vcu_input_sm_c_tick

**Debounce state machine C (qualifier FUN_08007ab8) with a 150-tick hold state**

Periodic tick of input state machine C, using the same state sequence as vcu_input_sm_b_tick: state DAT_200021b5 moves 0 -> 6 -> 7 -> 8 -> 2 and latches 1 on a long absence in state 7, with 3 forced after 150 consecutive present ticks. The qualifier is FUN_08007ab8 (not yet described); present activation needs the old presence count above 9 (ten ticks) instead of above 4, and the 7 -> 8 window is 3..24. Present ticks clear DAT_200014de and use DAT_200014dc (saturating at 10000); absent ticks use DAT_200014de and set DAT_20001fbc on the state-1 latch.

**Notes:** Physical input unknown. Has no armed latch (unlike vcu_input_sm_a_tick).

- Addresses by version: 148: 0x08007760, 14a: 0x08007B9C, 14b: 0x08007EF4, 14e: 0x08007F2C, 14f: 0x08007F88, 152: 0x0800804C, 153: 0x080080E8, 0159: 0x08008144
- Called by: `vcu_0159_0800193c`, `vcu_0159_0800673c`, `vcu_0159_080069b4`, `vcu_0159_080088f4`, `vcu_0159_08009fa4`, `vcu_0159_0800a55c`, `vcu_0159_0800a5c8`
- Calls: `vcu_pb12_input_active_low`
- Confidence: medium

## vcu_input_sm_d_tick

**Debounce state machine D on the GPIOB pin-10/pin-2 read, with status bit f92[12]**

Periodic tick of input state machine D. The qualifier vcu_gpio_b10_high_b2_low (0x080089bc) is sampled, so presence means PB10 high and PB2 low. The status word DAT_20001f92 bit 12 (0x1000) is cleared on every absent tick and set on present ticks when the variant DAT_20001fa7 is 4 or 6. The state byte is DAT_200021be, the counters are DAT_200014d0 (present) and DAT_200014d2 (absent), and the transitions are the same as vcu_input_sm_b_tick (activation above 4 ticks, 3..19 for 7 -> 8, 150 ticks forces state 3, long absence latches state 1 and sets DAT_20001fbc).

**Notes:** Purpose of the paired pin pattern (PB10 and PB2) is not established; vcu_input_sm_e_tick reads the complementary pattern and uses status bit f92[13].

- Addresses by version: 148: 0x08007808, 14a: 0x08007C44, 14b: 0x08007F9C, 14e: 0x08007FD4, 14f: 0x08008030, 152: 0x080080F4, 153: 0x08008190, 0159: 0x080081EC
- Called by: `vcu_0159_0800193c`, `vcu_0159_0800673c`, `vcu_0159_080069b4`, `vcu_0159_080088f4`
- Calls: `vcu_gpio_b10_high_b2_low`
- Confidence: medium

## vcu_input_sm_e_tick

**Debounce state machine E on the GPIOB pin-10/pin-2 read, with status bit f92[13]**

Periodic tick of input state machine E, the complement of vcu_input_sm_d_tick. The qualifier vcu_gpio_b10_low_b2_high (0x080089e4) is sampled, so presence means PB10 low and PB2 high. Status bit DAT_20001f92 bit 13 (0x2000) is set on present ticks when the variant DAT_20001fa7 is 4 or 6 and cleared on absent ticks. The state byte is DAT_200021bb, the counters are DAT_200014d4 and DAT_200014d6, and the transition rules match vcu_input_sm_d_tick.

**Notes:** Together with vcu_input_sm_d_tick this reads a two-position switch on PB10/PB2; the switch itself is not named here.

- Addresses by version: 148: 0x080078CC, 14a: 0x08007D08, 14b: 0x08008060, 14e: 0x0800809C, 14f: 0x080080F8, 152: 0x080081BC, 153: 0x08008258, 0159: 0x080082B4
- Called by: `vcu_0159_0800193c`, `vcu_0159_0800673c`, `vcu_0159_080069b4`, `vcu_0159_080088f4`
- Calls: `vcu_gpio_b10_low_b2_high`
- Confidence: medium
