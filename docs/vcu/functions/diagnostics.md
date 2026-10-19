# VCU - `diagnostics` functions

15 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`vcu_error_code_clear`](#vcu_error_code_clear) | 0x08005394 | Clear error code from active slot and bit i-1 of the 48-bit error bitmap |
| [`vcu_error_code_clear_if_current`](#vcu_error_code_clear_if_current) | 0x08005380 | Clear the active error code DAT_2000123c when it equals the given code |
| [`vcu_error_state_reset`](#vcu_error_state_reset) | 0x080053EC | Zero the active error code, DAT_20001b66 and the 3-word error bitmap |
| [`vcu_fault_0f_update`](#vcu_fault_0f_update) | 0x080029D0 | Update the displayed fault code 0x0F for a state: clear it, or store it when the state is 3 |
| [`vcu_fault_alert_repeat`](#vcu_fault_alert_repeat) | 0x080065DC | Repeat alert 4 every 300 ticks for fault 15 and alert 1 about every 1000 ticks for fault 9 |
| [`vcu_fault_code_set`](#vcu_fault_code_set) | 0x0800846C | Store a fault code (1..48) in DAT_2000123c and latch bit code-1 in a 3x16-bit bitmap |
| [`vcu_fault_code_store`](#vcu_fault_code_store) | 0x08008460 | Store the current fault code byte without updating the fault bitmap |
| [`vcu_fault_codes_4_5_eval`](#vcu_fault_codes_4_5_eval) | 0x08002D18 | Set or clear fault codes 4 and 5 from the reading in DAT_20001f36 |
| [`vcu_fault_warning_evaluate`](#vcu_fault_warning_evaluate) | 0x08003F40 | Per-tick evaluator that sets or clears warning and fault codes from sensor and message state |
| [`vcu_nibble_count_snapshot`](#vcu_nibble_count_snapshot) | 0x08007A48 | Snapshot the packed 32-bit counter word and count its nonzero hex nibbles |
| [`vcu_threshold_alarm_latch`](#vcu_threshold_alarm_latch) | 0x080032C4 | Latch a threshold alarm: alert 4 once while DAT_20001e62 is over its limit |
| [`vcu_warning_code_clear`](#vcu_warning_code_clear) | 0x08005434 | Clear warning code from active slot and bit (code-10) of the warning bitmap |
| [`vcu_warning_code_set`](#vcu_warning_code_set) | 0x080084BC | Record a warning code keeping the lowest non-zero one; latch it in a bitmap |
| [`vcu_warning_list_rebuild`](#vcu_warning_list_rebuild) | 0x08003444 | Rebuild the active warning code list when the four-word warning bitmap changes |
| [`vcu_warning_state_reset`](#vcu_warning_state_reset) | 0x08005410 | Zero the active warning code, DAT_20001b64 and the 4-word warning bitmap |

## vcu_error_code_clear

**Clear error code from active slot and bit i-1 of the 48-bit error bitmap**

First clears the active error code DAT_2000123c if it equals param_1. Then for codes 1..48 (param_1 != 0 and < 0x31) clears bit (param_1-1) in a 48-bit pending-error set spread over three u16 words: bits 0-15 in DAT_20001ce0, 16-31 in DAT_20001ce2 and 32-47 in DAT_20001ce4. Out-of-range codes only affect the active slot. Paired with vcu_warning_code_clear which does the same for codes 10..57 in DAT_20001cd8..cde and DAT_2000123d; reset together by vcu_error_state_reset. Callers: vcu_0159_08002d18, vcu_0159_08003f40.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | error code, 1..48 (0 and larger values ignored for the bitmap) |

**Notes:** Which of the two bitmap groups is 'error' versus 'warning' is a guess; both are fault-code sets.

- Addresses by version: 148: 0x08004A9C, 14a: 0x08004E28, 14b: 0x0800512C, 14e: 0x08005164, 14f: 0x080051C0, 152: 0x08005220, 153: 0x08005238, 0159: 0x08005394
- Called by: `vcu_fault_codes_4_5_eval`, `vcu_fault_warning_evaluate`
- Confidence: medium

## vcu_error_code_clear_if_current

**Clear the active error code DAT_2000123c when it equals the given code**

If the currently displayed/active error code DAT_2000123c equals param_1 it is set to 0. Does not touch the error bitmap (vcu_error_code_clear does that). Called from vcu_0159_080029d0 and vcu_0159_08003f40.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | error code to retire |

**Notes:** Interpretation of DAT_2000123c as an error code is inferred from the sibling functions with 48-bit bitmaps.

- Addresses by version: 148: 0x08004A88, 14a: 0x08004E14, 14b: 0x08005118, 14e: 0x08005150, 14f: 0x080051AC, 152: 0x0800520C, 153: 0x08005224, 0159: 0x08005380
- Called by: `vcu_fault_0f_update`, `vcu_fault_warning_evaluate`
- Confidence: medium

## vcu_error_state_reset

**Zero the active error code, DAT_20001b66 and the 3-word error bitmap**

Writes 0 to DAT_2000123c (active code), DAT_20001b66 and the three bitmap words DAT_20001ce0, DAT_20001ce2 and DAT_20001ce4 used by vcu_error_code_clear. Called from vcu_0159_0800a39c together with vcu_warning_state_reset, vcu_aux_flags_reset and the other clear helpers, i.e. a global reset of fault state.

**Notes:** DAT_20001b66 is probably a mirror of the active error code or a count; unknown.

- Addresses by version: 148: 0x08004AE4, 14a: 0x08004E70, 14b: 0x08005174, 14e: 0x080051AC, 14f: 0x08005208, 152: 0x08005268, 153: 0x08005280, 0159: 0x080053EC
- Called by: `vcu_0159_0800a39c`
- Confidence: medium

## vcu_fault_0f_update

**Update the displayed fault code 0x0F for a state: clear it, or store it when the state is 3**

Maintains fault code 0x0F as the displayed code. If bit 11 of DAT_20001AEC is set, it clears the displayed code if it is 0x0F (vcu_error_code_clear_if_current) and returns. Otherwise, if param_1 is not 3, it also clears the displayed 0x0F. Only when param_1 is 3 and bit 11 is clear does it store 0x0F as the current fault code without touching the bitmap (vcu_fault_code_store). Callers are vcu_0159_0800a15c, vcu_0159_0800a1d0, vcu_0159_0800a264, vcu_0159_0800a39c and vcu_0159_0800a5c8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | state argument; 3 means store the code |

**Notes:** The meaning of fault code 0x0F and of bit 11 of DAT_20001AEC is unknown; the function is described for its effect on the displayed code.

- Addresses by version: 148: 0x08002600, 14a: 0x08002678, 14b: 0x08002930, 14e: 0x08002930, 14f: 0x0800298C, 152: 0x080029C8, 153: 0x080029E4, 0159: 0x080029D0
- Called by: `vcu_0159_0800a15c`, `vcu_0159_0800a1d0`, `vcu_state2_periodic_tick`, `vcu_0159_0800a39c`, `vcu_0159_0800a5c8`
- Calls: `vcu_error_code_clear_if_current`, `vcu_fault_code_store`
- Confidence: medium

## vcu_fault_alert_repeat

**Repeat alert 4 every 300 ticks for fault 15 and alert 1 about every 1000 ticks for fault 9**

Runs while the warning code DAT_2000123d is zero and the fault code DAT_2000123c is nonzero. Counter DAT_20001486 counts those ticks; each time it reaches a multiple of 300 it resets, and if the fault is 15 it calls app_set_state(4). For fault 9 it uses the countdown DAT_20001482, loaded with 1000 and decremented per tick, and calls app_set_state(1) when it reaches zero. A change of the warning code (last value in DAT_2000147d) clears DAT_2000147c and DAT_20001480, and while a warning is active DAT_20001486 is held at 0. When DAT_20001f48 is set, the counters are cleared.

**Notes:** The alert numbers follow from the app_set_state values used here. DAT_20001f48 is not identified.

- Addresses by version: 148: 0x08005BC8, 14a: 0x08005FE8, 14b: 0x08006340, 14e: 0x08006378, 14f: 0x080063D4, 152: 0x08006454, 153: 0x080064F0, 0159: 0x080065DC
- Called by: `vcu_0159_0800a1d0`
- Calls: `app_set_state`
- Confidence: medium

## vcu_fault_code_set

**Store a fault code (1..48) in DAT_2000123c and latch bit code-1 in a 3x16-bit bitmap**

Writes (u8)param_1 to DAT_2000123c. If 1 <= param_1 <= 0x30 it sets bit (param_1-1) of a 48-bit active-fault bitmap spread across DAT_20001ce0 (codes 1..16), DAT_20001ce2 (17..32) and DAT_20001ce4 (33..48). Codes of 0 or above 48 only update the code byte. Bits are never cleared here; callers (0x08002d18, 0x08003f40) clear the bitmap elsewhere. Group: vcu_fault_code_store / vcu_fault_code_set / vcu_warning_code_set.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | fault code, 1..48 (0 = none) |

**Notes:** Naming as faults (vs. errors) is a guess; the clear path is not in this packet.

- Addresses by version: 148: 0x08007A80, 14a: 0x08007EBC, 14b: 0x08008214, 14e: 0x08008254, 14f: 0x080082B0, 152: 0x08008374, 153: 0x08008410, 0159: 0x0800846C
- Called by: `vcu_fault_codes_4_5_eval`, `vcu_fault_warning_evaluate`
- Confidence: medium

## vcu_fault_code_store

**Store the current fault code byte without updating the fault bitmap**

Writes param_1 to the byte DAT_2000123c (the latest fault/error code) and does nothing else. vcu_fault_code_set does the same store and additionally latches the code in a 48-bit bitmap; this variant is used by callers (0x080029d0, 0x08003f40) that only want to overwrite or clear the displayed code. Part of the fault/warning code group with vcu_fault_code_set and vcu_warning_code_set.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | fault code, 0 = none |

**Notes:** Role as 'fault' code inferred from the 1..48 range handled by the sibling that sets bitmap bits.

- Addresses by version: 148: 0x08007A74, 14a: 0x08007EB0, 14b: 0x08008208, 14e: 0x08008248, 14f: 0x080082A4, 152: 0x08008368, 153: 0x08008404, 0159: 0x08008460
- Called by: `vcu_fault_0f_update`, `vcu_fault_warning_evaluate`
- Confidence: medium

## vcu_fault_codes_4_5_eval

**Set or clear fault codes 4 and 5 from the reading in DAT_20001f36**

Maps the byte DAT_20001f36 (the 0x425 message field, see vcu_rx_frame_dispatch) onto two fault codes. The sentinel value 0x5aa5 returns at once. With sVar1 = value - 50, fault code 4 is set through vcu_fault_code_set when sVar1 is at least 60 (value 110 or more) and otherwise cleared through vcu_error_code_clear. Fault code 5 is set when sVar1 is below -12 (value below 38) and otherwise cleared. There is no hysteresis, so both codes follow the reading on every call.

**Notes:** The unit of DAT_20001f36 is not established. The 0x425 handler derives DAT_20001b8a = (value - 50) * 10 from the same byte, which suggests a temperature-like reading with a 50 offset.

- Addresses by version: 148: 0x080028C0, 14a: 0x08002944, 14b: 0x08002BFC, 14e: 0x08002BFC, 14f: 0x08002C58, 152: 0x08002CC4, 153: 0x08002CE0, 0159: 0x08002D18
- Called by: `vcu_0159_0800a15c`, `vcu_0159_0800a1d0`
- Calls: `vcu_error_code_clear`, `vcu_fault_code_set`
- Confidence: medium

## vcu_fault_warning_evaluate

**Per-tick evaluator that sets or clears warning and fault codes from sensor and message state**

Runs every tick and sets or clears codes through vcu_warning_code_set/clear, vcu_fault_code_set/store and vcu_error_code_clear. Silence timers DAT_2000102c (capped at 500) and DAT_20001030 (capped at 1500) and the fault-duration counter DAT_2000102e (capped at 4000, counting while DAT_2000123e is 2 or 3) are advanced here. Warnings 14, 15 and 16 follow the channel 1, 2 and 3 flags from vcu_sensor_limit_derate_eval, warning 10 is set when DAT_2000102c reaches 300, fault 21 when DAT_20001030 reaches 500, and fault 9 is stored after DAT_20001b62 / 10 exceeds DAT_20001032 for more than 100 ticks. When DAT_2000102e reaches 1500 it stores fault 25 and, once per latch in DAT_2000147e, pulses GPIOA pin 0x1000 low for 1000 ms (gpio_bits_reset, delay_ms, gpio_bits_set), which blocks the tick. Fault 34 is set for DAT_20001f7e of 0xfd or 0xfe, fault 40 after 100 ticks at DAT_20001f7e of 196 or more, and fault 41 for DAT_20001f84 of 156 or more (not 0xfd or 0xfe). Warnings 11, 13, 18, 24, 55 and 56 come from the byte DAT_20001f80, warning 30 from bits 3 and 12 of DAT_20001e6a and DAT_20001e68, and warning 35 from DAT_2000123e == 3 with DAT_20001f68. Finally DAT_20001b64 and DAT_20001b66 copy the warning and fault codes when DAT_2000123e is nonzero.

**Notes:** The 1000 ms pulse blocks the caller for a full second once per latch. Which physical circuit PA12 drives is not established. Code 9 uses vcu_fault_code_store and not the bitmap set, so it is not latched. The 0xfd and 0xfe values in DAT_20001f7e set fault 34, while the same values in DAT_20001f84 are excluded from fault 41; they look like error sentinels from the sender.

- Addresses by version: 148: 0x0800377C, 14a: 0x08003AB4, 14b: 0x08003DD4, 14e: 0x08003DD4, 14f: 0x08003E30, 152: 0x08003E94, 153: 0x08003EB4, 0159: 0x08003F40
- Peripheral registers: `GPIOA.CFGLR` (A)
- Called by: `vcu_pb14_timed_edge_sequence`, `vcu_0159_0800a15c`, `vcu_0159_0800a1d0`, `vcu_state2_periodic_tick`, `vcu_0159_0800a55c`, `vcu_0159_0800a5c8`
- Calls: `vcu_error_code_clear_if_current`, `vcu_error_code_clear`, `vcu_warning_code_clear`, `vcu_fault_code_store`, `vcu_fault_code_set`, `vcu_warning_code_set`, `delay_ms`, `gpio_bits_reset`, `gpio_bits_set`
- Confidence: medium

## vcu_nibble_count_snapshot

**Snapshot the packed 32-bit counter word and count its nonzero hex nibbles**

Clears the counters DAT_20002044, DAT_20002047, DAT_2000202d, DAT_20002030, DAT_2000202e and DAT_20002050, packs DAT_20001b96 (low half) and DAT_20001b98 (high half) into the 32-bit word DAT_20002034, and then sets DAT_20002046 to vcu_count_nonzero_nibbles of a 32-bit value. When DAT_20002049 is set it counts the nibbles of DAT_20002038 and sets the timer DAT_2000204a to 3000; otherwise it calls the count routine with no argument, so the value it counts is whatever the register holds. It finally clears DAT_20001cec and DAT_2000204c.

**Notes:** The argument of the no-flag call is not recovered; the packed word is the likely value. The meanings of the packed words are not established.

- Addresses by version: 148: 0x08007034, 14a: 0x08007458, 14b: 0x080077BC, 14e: 0x080077F4, 14f: 0x08007850, 152: 0x08007914, 153: 0x080079B0, 0159: 0x08007A48
- Called by: `vcu_key_sequence_entry_tick`, `vcu_0159_080047ac`, `vcu_code_nibble_entry_tick`, `vcu_code_digit_entry_tick`, `vcu_state2_periodic_tick`
- Calls: `vcu_count_nonzero_nibbles`
- Confidence: medium

## vcu_threshold_alarm_latch

**Latch a threshold alarm: alert 4 once while DAT_20001e62 is over its limit**

Compares DAT_20001e62 (the frame 0x420 value divided by 10, see vcu_rx_frame_dispatch) with the low byte of DAT_20001e48 (frame 0x423 field) and with 100. When DAT_20001e62 is below 100 and below that limit, it clears the step bytes DAT_20001878 and DAT_20001879 and the flag DAT_20001fec. Otherwise it sets DAT_20001cc4 = 3 and DAT_20001fec = 1, sets DAT_20001fbc once, and runs a two-step latch: the first call calls app_set_state(4) and moves DAT_20001878 from 0 to 1, a second call moves it to 2, and later calls return without a new alert.

**Notes:** The meaning of DAT_20001e62 (frame 0x420 value / 10) and DAT_20001e48 (frame 0x423 field) is taken from vcu_rx_frame_dispatch. The unit is not established.

- Addresses by version: 14a: 0x08002E58, 14b: 0x08003168, 14e: 0x08003168, 14f: 0x080031C4, 152: 0x08003230, 153: 0x08003250, 0159: 0x080032C4
- Called by: `vcu_0159_0800a15c`, `vcu_state0_periodic_tick_v0159`
- Calls: `app_set_state`
- Confidence: medium

## vcu_warning_code_clear

**Clear warning code from active slot and bit (code-10) of the warning bitmap**

Clears the active code DAT_2000123d if it equals param_1. For codes 10..57 (9 < param_1 < 0x3a) the bit index idx = param_1 - 10 is cleared in a bitmap of u16 words: idx 0-15 in DAT_20001cd8, 16-31 in cda, 32-47 in cdc, 48-63 in cde (the last word is reachable only for idx >= 48, which the range check prevents, so it is effectively dead). Sibling of vcu_error_code_clear with a different code range and storage. Callers: vcu_0159_08003f40, vcu_0159_0800a500.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | warning code, 10..57 |

**Notes:** Code range 10..57 suggests the warning numbering is offset from the error numbering; unverified.

- Addresses by version: 148: 0x08004B2C, 14a: 0x08004EB8, 14b: 0x080051BC, 14e: 0x080051F4, 14f: 0x08005250, 152: 0x080052B0, 153: 0x080052C8, 0159: 0x08005434
- Called by: `vcu_fault_warning_evaluate`, `vcu_state0_periodic_tick_v0159`
- Confidence: medium

## vcu_warning_code_set

**Record a warning code keeping the lowest non-zero one; latch it in a bitmap**

Keeps DAT_2000123d as the current warning code: if it is already non-zero and smaller than param_1 it is retained (lowest number = highest priority), otherwise it is set to param_1. When param_1 < 10 and the resulting code is 0 the whole bitmap (DAT_20001cd8/cda/cdc/cde) is cleared; codes 1..9 set no bit. For 10 <= param_1 < 0x3a the index n = param_1-10 sets bit n%16 in cd8 (n 0..15), cda (16..31) or cdc (32..47); the cde branch (n 48..63) is unreachable with the < 0x3a bound. Called by 0x08003f40, 0x08008cc0 and 0x0800a500; part of the fault/warning code group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | warning code; 0 clears the bitmap if no code is held, 10..57 map to bitmap bits 0..47 |

**Notes:** Semantic labelling (warning, priority rule) inferred from the min-keeping logic only.

- Addresses by version: 148: 0x08007AC8, 14a: 0x08007F04, 14b: 0x0800825C, 14e: 0x0800829C, 14f: 0x080082F8, 152: 0x080083BC, 153: 0x08008458, 0159: 0x080084BC
- Called by: `vcu_fault_warning_evaluate`, `vcu_speed_mode_snapshot_update`, `vcu_state0_periodic_tick_v0159`
- Confidence: medium

## vcu_warning_list_rebuild

**Rebuild the active warning code list when the four-word warning bitmap changes**

Compares the four 16-bit words of the warning bitmap at DAT_20001cd8..DAT_20001cde with a cached copy at DAT_200022ce..DAT_200022d4. On any change it copies the new words, clears the list count DAT_200021e6, sets the rebuild flag DAT_200022d8 and calls app_set_state(2) (alert 2) if any word is nonzero. When the flag is set it rebuilds a byte list at DAT_20002248: one entry per set bit, with word 0 giving codes 10-25, word 1 giving 26-41, word 2 giving 42-57 and word 3 giving 58-73. Warning code n is bit n - 10 of the bitmap (see vcu_warning_code_clear).

**Notes:** Each word is tested with 0 < word on a signed value, so a word with bit 15 set is skipped entirely, and codes 25, 41, 57 and 73 would be missing from the list. Entries are written through a byte pointer, so each code is stored as one byte.

- Addresses by version: 148: 0x08002EE0, 14a: 0x08002FD4, 14b: 0x080032E8, 14e: 0x080032E8, 14f: 0x08003344, 152: 0x080033B0, 153: 0x080033D0, 0159: 0x08003444
- Called by: `vcu_0159_0800a15c`, `vcu_0159_0800a1d0`
- Calls: `app_set_state`
- Confidence: high

## vcu_warning_state_reset

**Zero the active warning code, DAT_20001b64 and the 4-word warning bitmap**

Writes 0 to DAT_2000123d (active code), DAT_20001b64 and the four u16 bitmap words DAT_20001cd8, cda, cdc and cde used by vcu_warning_code_clear. Called from vcu_0159_0800a39c together with vcu_error_state_reset.

**Notes:** Error vs warning naming is a guess.

- Addresses by version: 148: 0x08004B08, 14a: 0x08004E94, 14b: 0x08005198, 14e: 0x080051D0, 14f: 0x0800522C, 152: 0x0800528C, 153: 0x080052A4, 0159: 0x08005410
- Called by: `vcu_0159_0800a39c`
- Confidence: medium
