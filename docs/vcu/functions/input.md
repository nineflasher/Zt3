# VCU - `input` functions

11 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`vcu_code_digit_entry_tick`](#vcu_code_digit_entry_tick) | 0x080069B4 | Advance the 4-digit code entry: cycle digits, move the cursor, compare on commit |
| [`vcu_code_nibble_entry_tick`](#vcu_code_nibble_entry_tick) | 0x0800673C | Pack button presses into a nibble code and compare it with the stored code after idle |
| [`vcu_input_edge_actions`](#vcu_input_edge_actions) | 0x08008614 | Apply input edge events: PA6 toggle, mode bits, item flags and the press state machine |
| [`vcu_input_sm_a_tick`](#vcu_input_sm_a_tick) | 0x08007E28 | Debounce state machine A: advance the input-A presence states once per tick |
| [`vcu_input_sm_b_tick`](#vcu_input_sm_b_tick) | 0x0800809C | Debounce state machine B for input B (qualifier FUN_08006994) with a 150-tick hold state |
| [`vcu_input_sm_c_tick`](#vcu_input_sm_c_tick) | 0x08008144 | Debounce state machine C (qualifier FUN_08007ab8) with a 150-tick hold state |
| [`vcu_input_sm_d_tick`](#vcu_input_sm_d_tick) | 0x080081EC | Debounce state machine D on the GPIOB pin-10/pin-2 read, with status bit f92[12] |
| [`vcu_input_sm_e_tick`](#vcu_input_sm_e_tick) | 0x080082B4 | Debounce state machine E on the GPIOB pin-10/pin-2 read, with status bit f92[13] |
| [`vcu_key_sequence_entry_tick`](#vcu_key_sequence_entry_tick) | 0x0800193C | Per-tick key-sequence entry: check debounced key presses against the stored code |
| [`vcu_panel_key_report_telemetry_tick`](#vcu_panel_key_report_telemetry_tick) | 0x08005938 | Report key presses as 0x56 frames, blink C14/C15, and send three levels every 10 ticks |
| [`vcu_pb14_timed_edge_sequence`](#vcu_pb14_timed_edge_sequence) | 0x08009FA4 | Run the PB14 timed edge-count sequence: 200 and 700 tick windows, 4 edges, timeout to 6 |

## vcu_code_digit_entry_tick

**Advance the 4-digit code entry: cycle digits, move the cursor, compare on commit**

Digit-wise code entry. It runs the five input debouncers (vcu_input_sm_a_tick to vcu_input_sm_e_tick), then input DAT_200021c1 decrements and input DAT_200021b5 increments the digit at the cursor DAT_2000202d in the byte array DAT_2000204c (wrapping 0 and 9), each change calling app_set_state(3) and mirroring the digit in DAT_20002044. DAT_200021be moves the cursor left and DAT_200021bb moves it right, up to the high-water mark DAT_20002050. A rising edge of DAT_20001f4f, or DAT_200021b8 set, commits the digit: at the high-water mark both DAT_20002050 and the cursor advance, otherwise the cursor jumps to the high-water mark. Once the cursor is past digit 3, vcu_digits4_to_int converts the four digits and compares the result with the stored code DAT_20001b76: a match calls app_set_state(4) and returns 1, a mismatch calls app_set_state(1), increments DAT_20002048 and calls vcu_nibble_count_snapshot.

**Returns** `bool`: 1 when the four digits match DAT_20001b76 (state 4 entered), else 0

**Notes:** The stored code DAT_20001b76 is written elsewhere. The button roles are inferred from the state transitions only.

- Addresses by version: 148: 0x08005F60, 14a: 0x08006380, 14b: 0x080066F0, 14e: 0x08006728, 14f: 0x08006784, 152: 0x08006828, 153: 0x080068C4, 0159: 0x080069B4
- Called by: `vcu_state2_periodic_tick`
- Calls: `app_set_state`, `vcu_digits4_to_int`, `vcu_nibble_count_snapshot`, `vcu_input_sm_a_tick`, `vcu_input_sm_b_tick`, `vcu_input_sm_c_tick`, `vcu_input_sm_d_tick`, `vcu_input_sm_e_tick`
- Confidence: medium

## vcu_code_nibble_entry_tick

**Pack button presses into a nibble code and compare it with the stored code after idle**

Periodic tick of a button-code entry. It first runs vcu_input_sm_c_tick, vcu_input_sm_b_tick, vcu_input_sm_e_tick and vcu_input_sm_d_tick, then consumes the press flags DAT_200021c1 (code 1), DAT_200021b5 (code 2), DAT_200021be (code 3) and DAT_200021bb (code 4) into the pending code DAT_20002044 and the last-code register DAT_20002047. While the entry count DAT_2000202d is below the required length DAT_20002046, a pending code is shifted into the low nibble of the 32-bit word DAT_20002030 (word = word << 4 | code), the count is incremented, DAT_20001fac is reloaded with 3000, the redraw flag DAT_20001fbc is set and app_set_state(3) is called; the idle counter DAT_20001356 is held at 0. Once the count reaches the length, the idle counter runs past about 60 ticks, then DAT_20002030 is compared with the stored code DAT_20002034: a match calls app_set_state(4) and returns 1, a mismatch calls app_set_state(1), increments the failure counter DAT_20002048 and calls vcu_nibble_count_snapshot. The entry word and the count are not cleared on mismatch.

**Returns** `bool`: 1 when the entered code equals DAT_20002034 (state 4 entered), else 0

**Notes:** The meaning of the four input codes and of the stored code DAT_20002034 is not shown by this function; the labels follow the state values it sets.

- Addresses by version: 148: 0x08005D10, 14a: 0x08006130, 14b: 0x080064A0, 14e: 0x080064D8, 14f: 0x08006534, 152: 0x080065B4, 153: 0x08006650, 0159: 0x0800673C
- Called by: `vcu_state2_periodic_tick`
- Calls: `app_set_state`, `vcu_nibble_count_snapshot`, `vcu_input_sm_b_tick`, `vcu_input_sm_c_tick`, `vcu_input_sm_d_tick`, `vcu_input_sm_e_tick`
- Confidence: medium

## vcu_input_edge_actions

**Apply input edge events: PA6 toggle, mode bits, item flags and the press state machine**

Edge processor. Each event flag is compared with its shadow copy and any change sets the redraw flag DAT_20001fbc. Input-B press (DAT_200021b5 against DAT_200021b4): unless the sub-mode DAT_20001fa4 is 4, it toggles PA6 through vcu_pa6_output_set and flips DAT_20001cfa and DAT_20001f53, and if DAT_2000123e is 3, 7 or 8 it queues command 0x61 with a 3-byte payload. Events DAT_200021be and DAT_200021bb toggle the mode bits DAT_20002020 to DAT_20002026 on press 1 and step DAT_20002024 through 0, 1, 2 on press 3. Event DAT_200021b8 on press sets one of DAT_20001f70 to DAT_20001f75 or DAT_20001f4a according to the item in DAT_20001b48, with item 6 setting DAT_20001f73 unless both DAT_20001af2 bit 4 and DAT_20001e6a bit 3 are set; on release all of them are cleared. The DAT_200021c1 press runs a four-state machine in DAT_20001fa4 (1 idle, 2 to 4) using bits of DAT_20001af0, DAT_20001aee, DAT_20001aec and DAT_20001f78, and the threshold DAT_20001b62 below 50.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | not used; returned unchanged in the pair |
| `param_2` | `u32` | not used; returned unchanged in the pair |

**Returns** `u64`: param_2:param_1 unchanged

**Notes:** The item and mode names are not defined in this packet; they are described by the flags they set. The four-state machine's state names are inferred from the transitions.

- Addresses by version: 148: 0x08007C20, 14a: 0x0800805C, 14b: 0x080083B4, 14e: 0x080083F4, 14f: 0x08008450, 152: 0x08008514, 153: 0x080085B0, 0159: 0x08008614
- Called by: `vcu_status_update_if_enabled`
- Calls: `vcu_pa6_output_set`, `vcu_ninebot_tx_queue_push`
- Confidence: medium

## vcu_input_sm_a_tick

**Debounce state machine A: advance the input-A presence states once per tick**

Periodic tick of input state machine A. The qualifier FUN_080056e8 (not yet described) is sampled; nonzero means the input is present. Present ticks only act after the armed latch DAT_200014c8 has been set by an earlier absent tick: the presence counter DAT_200014e0 (saturates at 10000) increments, and once the old value exceeds 4 the state DAT_200021b8 goes 0 -> 6, or 7 -> 8 while the new count is 3..24. Absent ticks clear the presence counter, set the armed latch, count absent ticks in DAT_200014e2, move 6 -> 7 and 8 -> 2, and after more than 9 absent ticks a machine in state 7 latches state 1 and sets the shared event flag DAT_20001fbc, while any other state falls back to 0.

**Notes:** The physical input is not identified; FUN_080056e8 is not yet described. State 1 is an event latch; DAT_20001fbc is also set by the other input machines (vcu_input_sm_b_tick to vcu_input_sm_e_tick). No 150-tick long-hold state exists in this machine, unlike B to E.

- Addresses by version: 148: 0x08007438, 14a: 0x08007874, 14b: 0x08007BD8, 14e: 0x08007C10, 14f: 0x08007C6C, 152: 0x08007D30, 153: 0x08007DCC, 0159: 0x08007E28
- Called by: `vcu_code_digit_entry_tick`, `vcu_level_hold_timer_update`, `vcu_0159_0800a5c8`
- Calls: `vcu_pb13_input_active_low`
- Confidence: medium

## vcu_input_sm_b_tick

**Debounce state machine B for input B (qualifier FUN_08006994) with a 150-tick hold state**

Periodic tick of input state machine B. The qualifier FUN_08006994 (not yet described) is sampled; nonzero means present. Present: the counter DAT_200014cc (saturating at 10000) increments; when the old value exceeded 4 the state DAT_200021c1 goes 0 -> 6, goes 7 -> 8 while the new count is 3..19, and a new count of 150 (0x96) forces state 3 from any state. Absent: DAT_200014cc clears, DAT_200014ce counts absent ticks, 6 -> 7 and 8 -> 2 happen, more than 9 absent ticks in state 7 latch state 1 and set DAT_20001fbc, and more than 9 in any other state drops the machine to 0. State 3 is the long-hold state read by vcu_input_b_hold_start_tick (0x08009094).

**Notes:** The physical input behind FUN_08006994 is unknown. Thresholds (4, 3..19, 150) are read from the compare constants in the decompile.

- Addresses by version: 148: 0x080076B8, 14a: 0x08007AF4, 14b: 0x08007E4C, 14e: 0x08007E84, 14f: 0x08007EE0, 152: 0x08007FA4, 153: 0x08008040, 0159: 0x0800809C
- Called by: `vcu_key_sequence_entry_tick`, `vcu_code_nibble_entry_tick`, `vcu_code_digit_entry_tick`, `vcu_level_hold_timer_update`
- Calls: `vcu_pb11_input_active_low`
- Confidence: medium

## vcu_input_sm_c_tick

**Debounce state machine C (qualifier FUN_08007ab8) with a 150-tick hold state**

Periodic tick of input state machine C, using the same state sequence as vcu_input_sm_b_tick: state DAT_200021b5 moves 0 -> 6 -> 7 -> 8 -> 2 and latches 1 on a long absence in state 7, with 3 forced after 150 consecutive present ticks. The qualifier is FUN_08007ab8 (not yet described); present activation needs the old presence count above 9 (ten ticks) instead of above 4, and the 7 -> 8 window is 3..24. Present ticks clear DAT_200014de and use DAT_200014dc (saturating at 10000); absent ticks use DAT_200014de and set DAT_20001fbc on the state-1 latch.

**Notes:** Physical input unknown. Has no armed latch (unlike vcu_input_sm_a_tick).

- Addresses by version: 148: 0x08007760, 14a: 0x08007B9C, 14b: 0x08007EF4, 14e: 0x08007F2C, 14f: 0x08007F88, 152: 0x0800804C, 153: 0x080080E8, 0159: 0x08008144
- Called by: `vcu_key_sequence_entry_tick`, `vcu_code_nibble_entry_tick`, `vcu_code_digit_entry_tick`, `vcu_level_hold_timer_update`, `vcu_pb14_timed_edge_sequence`, `vcu_0159_0800a55c`, `vcu_0159_0800a5c8`
- Calls: `vcu_pb12_input_active_low`
- Confidence: medium

## vcu_input_sm_d_tick

**Debounce state machine D on the GPIOB pin-10/pin-2 read, with status bit f92[12]**

Periodic tick of input state machine D. The qualifier vcu_gpio_b10_high_b2_low (0x080089bc) is sampled, so presence means PB10 high and PB2 low. The status word DAT_20001f92 bit 12 (0x1000) is cleared on every absent tick and set on present ticks when the variant DAT_20001fa7 is 4 or 6. The state byte is DAT_200021be, the counters are DAT_200014d0 (present) and DAT_200014d2 (absent), and the transitions are the same as vcu_input_sm_b_tick (activation above 4 ticks, 3..19 for 7 -> 8, 150 ticks forces state 3, long absence latches state 1 and sets DAT_20001fbc).

**Notes:** Purpose of the paired pin pattern (PB10 and PB2) is not established; vcu_input_sm_e_tick reads the complementary pattern and uses status bit f92[13].

- Addresses by version: 148: 0x08007808, 14a: 0x08007C44, 14b: 0x08007F9C, 14e: 0x08007FD4, 14f: 0x08008030, 152: 0x080080F4, 153: 0x08008190, 0159: 0x080081EC
- Called by: `vcu_key_sequence_entry_tick`, `vcu_code_nibble_entry_tick`, `vcu_code_digit_entry_tick`, `vcu_level_hold_timer_update`
- Calls: `vcu_gpio_b10_high_b2_low`
- Confidence: medium

## vcu_input_sm_e_tick

**Debounce state machine E on the GPIOB pin-10/pin-2 read, with status bit f92[13]**

Periodic tick of input state machine E, the complement of vcu_input_sm_d_tick. The qualifier vcu_gpio_b10_low_b2_high (0x080089e4) is sampled, so presence means PB10 low and PB2 high. Status bit DAT_20001f92 bit 13 (0x2000) is set on present ticks when the variant DAT_20001fa7 is 4 or 6 and cleared on absent ticks. The state byte is DAT_200021bb, the counters are DAT_200014d4 and DAT_200014d6, and the transition rules match vcu_input_sm_d_tick.

**Notes:** Together with vcu_input_sm_d_tick this reads a two-position switch on PB10/PB2; the switch itself is not named here.

- Addresses by version: 148: 0x080078CC, 14a: 0x08007D08, 14b: 0x08008060, 14e: 0x0800809C, 14f: 0x080080F8, 152: 0x080081BC, 153: 0x08008258, 0159: 0x080082B4
- Called by: `vcu_key_sequence_entry_tick`, `vcu_code_nibble_entry_tick`, `vcu_code_digit_entry_tick`, `vcu_level_hold_timer_update`
- Calls: `vcu_gpio_b10_low_b2_high`
- Confidence: medium

## vcu_key_sequence_entry_tick

**Per-tick key-sequence entry: check debounced key presses against the stored code**

Each tick it runs the four debounce machines (vcu_input_sm_c_tick, vcu_input_sm_b_tick, vcu_input_sm_e_tick, vcu_input_sm_d_tick), then, while the entry-armed flag DAT_20002049 is set, consumes the one-shot press flags DAT_200021C1, DAT_200021B5, DAT_200021BE and DAT_200021BB as keys 1, 2, 3 and 4. Each accepted key is packed as a 4-bit nibble into the accumulator DAT_20002030 and checked against the expected nibble at position (length minus count) of the packed sequence DAT_20002038, where DAT_20002046 is the length; a wrong key ends the entry with result 2. After the last key and a wait past 60 ticks (DAT_20001357), the accumulator is compared with DAT_2000203C: a match sets result 1, copies DAT_20002040 and DAT_20002042 into DAT_20001B96 and DAT_20001B98, raises DAT_20001F54 for vcu_pending_settings_commit and enters app state 4, and a mismatch sets result 2 and app state 1. Every outcome is sent as a 0x73 frame (vcu_ninebot_tx_queue_push, source 0x16, peer 0x3E) carrying the one-byte result in DAT_20002051 (1 accepted, 2 rejected, 3 timed out), and the countdown DAT_2000204A aborts an idle entry with result 3.

**Notes:** Mechanics are read directly from the decompile (high confidence). What the stored code unlocks is not established in this packet. The digit count is mirrored to DAT_20001CEC, which drives the progress bars in vcu_display_frame_render_tick, and the key 2 flag DAT_200021B5 is also read and cleared by vcu_panel_key_report_telemetry_tick, so whichever runs first in a tick consumes the press. Bit 6 of DAT_20001AF0 is a cancel request: when set, the entry is aborted and the bit cleared.

- Addresses by version: 148: 0x08001558, 14a: 0x080015CC, 14b: 0x08001874, 14e: 0x08001874, 14f: 0x080018D0, 152: 0x0800190C, 153: 0x08001928, 0159: 0x0800193C
- Called by: `vcu_slot_193c_alert_tick`
- Calls: `app_set_state`, `vcu_nibble_count_snapshot`, `vcu_input_sm_b_tick`, `vcu_input_sm_c_tick`, `vcu_input_sm_d_tick`, `vcu_input_sm_e_tick`, `vcu_ninebot_tx_queue_push`
- Confidence: medium

## vcu_panel_key_report_telemetry_tick

**Report key presses as 0x56 frames, blink C14/C15, and send three levels every 10 ticks**

Scales three 16-bit readings (app_get_u16_2000329C, _329E and _32A0) by 1/15 when DAT_20001FEB is 1 and by 1/14 otherwise. Each one-shot press flag (DAT_200021B5, DAT_200021C1, DAT_200021B8, DAT_200021BB and DAT_200021BE) is consumed once and reported as a 0x56 frame with sub-command 1, 2, 5, 9 or 10, while keys 2 and 1 also drive PA6 and keys 4 and 3 switch C15 and C14 on and toggle their blink modes. While a blink mode is set, C14 or C15 toggles every 40 ticks, and a 10-tick cycle sends the three scaled levels as 0x56 frames with sub-commands 0x0B, 0x0D and 0x0C at cycle ticks 1, 5 and 10.

**Notes:** The key flags are also read and cleared by vcu_key_sequence_entry_tick; the first of the two to run in a tick consumes a press. The frames use source 0x16 and peer 0x3D and carry 4-byte payloads (the level values are unsigned words). The blink toggle on the C14/C15 pins is written with the output helpers and the argument passed through, as decompiled. Callers are not identified in this packet.

- Addresses by version: 148: 0x08004FB8, 14a: 0x080053A8, 14b: 0x080056D0, 14e: 0x08005708, 14f: 0x08005764, 152: 0x080057BC, 153: 0x080057D4, 0159: 0x08005938
- Called by: `vcu_0159_080047ac`
- Calls: `app_get_u16_2000329e`, `app_get_u16_200032a0`, `app_get_u16_2000329c`, `app_set_state`, `vcu_alert_tone_sequencer`, `vcu_pa6_output_set`, `vcu_level_hold_timer_thunk`, `vcu_gpio_c14_set`, `vcu_gpio_c15_set`, `vcu_can_ef00_message_send`
- Confidence: medium

## vcu_pb14_timed_edge_sequence

**Run the PB14 timed edge-count sequence: 200 and 700 tick windows, 4 edges, timeout to 6**

Periodic state machine on GPIOB pin 14 (0x4000), read through vcu_gpio_pins_all_high into DAT_20001fb8. Each call sets DAT_20001fa8 = 1, then runs vcu_input_sm_c_tick, vcu_fault_warning_evaluate(6), vcu_periodic_100_tick_check and vcu_alert_tone_sequencer. The state is DAT_20001fd1 and the tick counter DAT_200013c2 restarts at each state change. State 0 samples for about 200 ticks, setting bits 2 and 3 of DAT_20001f92 when DAT_20001aee bit 2 is set and DAT_20001f78 bit 0 is clear, then goes to state 1. States 1, 3 and 5 count pin level changes: four changes advance (1 to 2, 3 to 4, 5 to 4) and 300 ticks without that many changes go to state 6. States 2 and 4 hold for about 200 and 700 ticks while sampling the pin, and state 4 ends in state 5. State 6 sets DAT_20001fb4, returns to state 0 and clears DAT_20001fb8.

**Notes:** The purpose of this PB14 handshake or pulse-train check is not established. The states, windows and edge counts are as coded.

- Addresses by version: 148: 0x080090CC, 14a: 0x08009574, 14b: 0x080099F4, 14e: 0x08009A88, 14f: 0x08009BC4, 152: 0x08009DD8, 153: 0x08009ECC, 0159: 0x08009FA4
- Peripheral registers: `GPIOB.CFGLR` (A)
- Called by: `vcu_0159_080047ac`
- Calls: `vcu_alert_tone_sequencer`, `vcu_periodic_100_tick_check`, `vcu_fault_warning_evaluate`, `vcu_input_sm_c_tick`, `vcu_gpio_pins_all_high`
- Confidence: low
