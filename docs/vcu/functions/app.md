# VCU - `app` functions

21 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`app_get_u16_2000329c`](#app_get_u16_2000329c) | 0x080017C4 | Getter returning the 16-bit RAM variable at 0x2000329c |
| [`app_get_u16_2000329e`](#app_get_u16_2000329e) | 0x080013EC | Getter returning the 16-bit RAM variable at 0x2000329e |
| [`app_get_u16_200032a0`](#app_get_u16_200032a0) | 0x08001410 | Getter returning the 16-bit RAM variable at 0x200032a0 |
| [`app_get_u16_200032a2`](#app_get_u16_200032a2) | 0x080017D0 | Getter returning the 16-bit RAM variable at 0x200032a2 |
| [`app_get_u16_200032a4`](#app_get_u16_200032a4) | 0x080017DC | Getter returning the 16-bit RAM variable at 0x200032a4 |
| [`app_level_complement_7`](#app_level_complement_7) | 0x08001436 | Return 7 minus the signed byte at offset 2 of a record |
| [`app_set_state`](#app_set_state) | 0x08001B64 | Set the application state byte and reset its sub-step counter when it changes |
| [`app_verify_uid_checksum`](#app_verify_uid_checksum) | 0x08002998 | Check that a two-word record equals the complement of sum and product of three RAM words |
| [`vcu_alarm_edge_trigger`](#vcu_alarm_edge_trigger) | 0x08003254 | Raise alert 4 on the rising edge of DAT_20001f69 or of DAT_20001e68 bit 6 |
| [`vcu_alert_tone_sequencer`](#vcu_alert_tone_sequencer) | 0x08002D64 | Play the alert beep pattern selected by the app state byte DAT_2000101a |
| [`vcu_apply_variant_config`](#vcu_apply_variant_config) | 0x08005DB8 | Build four 16-bit option words from the variant index DAT_20001fa7 and publish them |
| [`vcu_flag_bitmap_expand`](#vcu_flag_bitmap_expand) | 0x080029F4 | Detect changes in three 16-bit flag words and expand set bits into an item index list |
| [`vcu_pa6_output_status_update`](#vcu_pa6_output_status_update) | 0x08002AE0 | Drive PA6 from the output latch and rewrite the mode code in status word DAT_20001f98 |
| [`vcu_pair_pulse_pattern_step`](#vcu_pair_pulse_pattern_step) | 0x0800422C | Run a 60-tick two-output pulse pattern after a change of DAT_20001fb5 |
| [`vcu_runtime_defaults_init`](#vcu_runtime_defaults_init) | 0x0800B294 | Load default runtime status words and mode limits, then apply the variant configuration |
| [`vcu_sanitize_mode_1_to_4`](#vcu_sanitize_mode_1_to_4) | 0x0800686C | Force the byte at param_1 into the range 1..4 (default 1) |
| [`vcu_serial_check_default`](#vcu_serial_check_default) | 0x080066DC | Classify the stored serial string at DAT_20001ad4 against the default '1K1E0000000001' |
| [`vcu_serial_match_set_flag`](#vcu_serial_match_set_flag) | 0x08002F08 | Compare two 14-byte strings and set a flag when they are identical |
| [`vcu_serial_parse_variant_code`](#vcu_serial_parse_variant_code) | 0x08004714 | Decode the variant letter of a '1K1x' serial prefix into DAT_20001fa7 |
| [`vcu_special_mode_gate`](#vcu_special_mode_gate) | 0x080038A4 | Enter and leave special mode stage DAT_20001fd6 after a 300-tick hold |
| [`vcu_standby_entry_timer`](#vcu_standby_entry_timer) | 0x080051E8 | Enter standby after 600 quiet ticks and manage request bit 2 of DAT_20001f92 |

## app_get_u16_2000329c

**Getter returning the 16-bit RAM variable at 0x2000329c**

Returns DAT_2000329c. First element of the five consecutive 16-bit getters (0x2000329c..0x200032a4). Called by vcu_0159_08003594 and vcu_0159_08005938 only. Meaning not determinable from this function; likely a sampled analog input.

**Returns** `u16`: value of DAT_2000329c

**Notes:** Positional name.

- Addresses by version: 148: 0x080013E8, 14a: 0x080013DC, 14b: 0x08001710, 14e: 0x08001710, 14f: 0x0800176C, 152: 0x080017A8, 153: 0x080017A8, 0159: 0x080017C4
- Called by: `vcu_sensor_limit_derate_eval`, `vcu_0159_08005938`
- Confidence: low

## app_get_u16_2000329e

**Getter returning the 16-bit RAM variable at 0x2000329e**

Returns DAT_2000329e unchanged. It sits in a block of five consecutive 16-bit getters (0x2000329c..0x200032a4: vcu_0159_080017c4, 080013ec, 08001410, 080017d0, 080017dc) that expose one 16-bit slot each, which looks like an array of sampled inputs (possibly ADC/DMA results or filtered sensor values) read by the main application loops vcu_0159_08003594, 08005938, 08007ecc and 080088f4, and one build-153 caller. What the value physically measures was not determinable from this function alone.

**Returns** `u16`: value of DAT_2000329e

**Notes:** Name is positional because the semantic of the variable is unknown; rename when the writer of 0x2000329e is annotated.

- Addresses by version: 148: 0x080013D0, 14a: 0x080013C4, 14b: 0x08001410, 14e: 0x08001410, 14f: 0x08001410, 152: 0x080013EC, 153: 0x080013EC, 0159: 0x080013EC
- Called by: `vcu_sensor_limit_derate_eval`, `vcu_0159_08005938`, `vcu_0159_08007ecc`, `vcu_0159_080088f4`
- Confidence: low

## app_get_u16_200032a0

**Getter returning the 16-bit RAM variable at 0x200032a0**

Returns DAT_200032a0. Member of the five-entry 16-bit getter block starting at 0x2000329c (see app_get_u16_2000329e); called by vcu_0159_08003594, 08005938, 08007ecc and 080088f4, always alongside the 0x2000329e getter. Meaning of the value (probably a sampled/filtered analog input) is not established here.

**Returns** `u16`: value of DAT_200032a0

**Notes:** Positional name; rename once the producer of 0x200032a0 is known.

- Addresses by version: 148: 0x080013DC, 14a: 0x080013D0, 14b: 0x08001704, 14e: 0x08001704, 14f: 0x08001760, 152: 0x08001410, 153: 0x08001410, 0159: 0x08001410
- Called by: `vcu_sensor_limit_derate_eval`, `vcu_0159_08005938`, `vcu_0159_08007ecc`, `vcu_0159_080088f4`
- Confidence: low

## app_get_u16_200032a2

**Getter returning the 16-bit RAM variable at 0x200032a2**

Returns DAT_200032a2. Part of the 0x2000329c.. array of 16-bit values. Sole caller is vcu_0159_080042f8, which also calls the next getter (0x200032a4) and the TMR2 output disable routine.

**Returns** `u16`: value of DAT_200032a2

**Notes:** Positional name.

- Addresses by version: 148: 0x080013F4, 14a: 0x080013E8, 14b: 0x0800171C, 14e: 0x0800171C, 14f: 0x08001778, 152: 0x080017B4, 153: 0x080017B4, 0159: 0x080017D0
- Called by: `vcu_0159_080042f8`
- Confidence: low

## app_get_u16_200032a4

**Getter returning the 16-bit RAM variable at 0x200032a4**

Returns DAT_200032a4. Last of the five 16-bit getter functions over 0x2000329c..0x200032a4. Sole caller is vcu_0159_080042f8.

**Returns** `u16`: value of DAT_200032a4

**Notes:** Positional name.

- Addresses by version: 148: 0x08001410, 14a: 0x080013F4, 14b: 0x08001728, 14e: 0x08001728, 14f: 0x08001784, 152: 0x080017C0, 153: 0x080017C0, 0159: 0x080017DC
- Called by: `vcu_0159_080042f8`
- Confidence: low

## app_level_complement_7

**Return 7 minus the signed byte at offset 2 of a record**

Reads the signed char at param_1+2 and returns 7 - that value, i.e. mirrors a 0..7 level or index (for example converting an ascending step number into a descending one). Single caller vcu_0159_080047ac. The record layout and meaning of the field are not visible from this function.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pointer to a record whose byte +2 holds a small level value |

**Returns** `s8`: 7 - record[2]

**Notes:** Purpose guessed from arithmetic only.

- Addresses by version: 148: 0x08004BE2, 14a: 0x08004F6E, 14b: 0x08005272, 14e: 0x080052AA, 14f: 0x08005306, 152: 0x08005366, 153: 0x0800537E, 0159: 0x08001436
- Called by: `vcu_0159_080047ac`
- Confidence: low

## app_set_state

**Set the application state byte and reset its sub-step counter when it changes**

If param_1 differs from the state byte DAT_2000101a, stores the new value (low 8 bits) and zeroes DAT_2000101c (the sub-state / step or timer counter belonging to that state). Setting the same state again is a no-op so the counter keeps running. Called from more than a dozen state handlers (vcu_0159_0800193c, 080029f4, 08002fc0, 08003254, 080032c4, 08003444, 080038a4, 08003c5c, 080046c0, 080047ac, 080051e8, 080054ec ...), so these form the main application state machine and this is its transition primitive.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | new state number |

**Notes:** Whether DAT_2000101c is a step index or a tick counter is not established (written as 0 only).

- Addresses by version: 148: 0x08001780, 14a: 0x080017F4, 14b: 0x08001A9C, 14e: 0x08001A9C, 14f: 0x08001AF8, 152: 0x08001B34, 153: 0x08001B50, 0159: 0x08001B64
- Called by: `vcu_0159_0800193c`, `vcu_flag_bitmap_expand`, `vcu_ready_sequence_step_v14b_0159`, `vcu_alarm_edge_trigger`, `vcu_threshold_alarm_latch`, `vcu_warning_list_rebuild`, `vcu_special_mode_gate`, `vcu_0159_08003c5c`, `vcu_0159_080046c0`, `vcu_0159_080047ac`, `vcu_standby_entry_timer`, `vcu_0159_080054ec` ...
- Confidence: medium

## app_verify_uid_checksum

**Check that a two-word record equals the complement of sum and product of three RAM words**

Computes s = DAT_20001c68 + DAT_20001c6c + DAT_20001c70 and p = DAT_20001c68 * DAT_20001c6c * DAT_20001c70 (32-bit wrap) and returns 1 only if param_1[0] == ~s and param_1[1] == ~p, else 0. The three RAM words are most likely the 96-bit device-ID copied from 0x1FFFF7E8 at startup, and the 8-byte record a stored licence/pairing value, so this is an anti-copy / per-device binding check. Single caller vcu_0159_080054ec (also a state-machine step calling app_set_state).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pointer to two u32 words: ~sum and ~product |

**Returns** `u32`: 1 if both words match, 0 otherwise

**Notes:** That 0x20001c68..70 hold the chip UID is inferred from the brief; not verified in this packet.

- Addresses by version: 148: 0x080025C8, 14a: 0x08002640, 14b: 0x080028F8, 14e: 0x080028F8, 14f: 0x08002954, 152: 0x08002990, 153: 0x080029AC, 0159: 0x08002998
- Called by: `vcu_0159_080054ec`
- Confidence: medium

## vcu_alarm_edge_trigger

**Raise alert 4 on the rising edge of DAT_20001f69 or of DAT_20001e68 bit 6**

Edge detector that starts alert pattern 4 through app_set_state(4). It compares the debounced condition DAT_20001f69 with its previous copy DAT_20001f6c and alerts when the condition becomes 1. When status bit 4 of DAT_20001af2 is set, it also watches bit 6 of DAT_20001e68 through the copy DAT_20001882 and alerts when that bit changes to 1, then returns. When the af2 bit is clear it clears DAT_20001882.

**Notes:** The two edge checks are separate: the f69 check runs first on every call, and the e68 check runs only when af2 bit 4 is set.

- Addresses by version: 148: 0x08002D60, 14a: 0x08002DE8, 14b: 0x080030F8, 14e: 0x080030F8, 14f: 0x08003154, 152: 0x080031C0, 153: 0x080031E0, 0159: 0x08003254
- Called by: `vcu_0159_0800a15c`, `vcu_0159_0800a500`
- Calls: `app_set_state`
- Confidence: medium

## vcu_alert_tone_sequencer

**Play the alert beep pattern selected by the app state byte DAT_2000101a**

Steps the buzzer, a TMR2 channel-1 PWM output started by vcu_0159_08001ba8 and stopped by tmr2_pwm_output_disable, through a pattern chosen by app state byte DAT_2000101a (written by app_set_state). Counter DAT_2000101c advances once per call and the state returns to 0 when a pattern ends. Patterns, in calls (on/off): 1 = one 51-call beep; 2 = two 100-call beeps with a 100-call gap; 3 = one 10-call beep; 4 = two 10-call beeps with a 10-call gap; 5 = three 10-call beeps; 6 = three 100-call beeps; 7 = 20 on, 10 off, then 100 on; 8 = stop (output off, state 0); 0 = idle. If DAT_20002022 or DAT_20002023 is set while bit 11 of DAT_20001aee is set, the state is cleared at once without calling the tone-off routine.

**Notes:** The call period is not established, so the patterns are counted in calls. The buzzer identification is inferred from the single caller of tmr2_pwm_set_frequency and the on/off pattern. The abort branch does not turn the PWM off, so a tone that was sounding may keep sounding; check whether another path stops it. The decompiler shows vcu_0159_08001ba8 and tmr2_pwm_output_disable both with and without an argument (0xaaa), so the argument is not meaningful here.

- Addresses by version: 148: 0x0800290C, 14a: 0x08002990, 14b: 0x08002C48, 14e: 0x08002C48, 14f: 0x08002CA4, 152: 0x08002D10, 153: 0x08002D2C, 0159: 0x08002D64
- Called by: `vcu_0159_08005938`, `vcu_0159_08009fa4`, `vcu_0159_08009fcc`, `vcu_0159_0800a15c`, `vcu_0159_0800a1d0`, `vcu_0159_0800a264`, `vcu_0159_0800a39c`, `vcu_0159_0800a4e8`, `vcu_0159_0800a500`, `vcu_0159_0800a55c`, `vcu_0159_0800a5c8`
- Calls: `vcu_tmr2_ch1_pwm_start`, `tmr2_pwm_output_disable`
- Confidence: medium

## vcu_apply_variant_config

**Build four 16-bit option words from the variant index DAT_20001fa7 and publish them**

Starts from default values (DAT_20001034 = 0x279F, DAT_20001036 = 0xA5A1, DAT_20001038 base 0x83DD, DAT_2000103a with bits 4-5 cleared and bit 1 set) and switches on the variant index DAT_20001fa7 (set by vcu_serial_parse_variant_code, values 0..6, default for other values) to override bit fields in these four words and, for cases 1, 2, 5 and default, to clear bit 12 of DAT_20001aee (case 2 also sets bit 11). Finally the words are copied into the output/shadow words DAT_20001aea, DAT_20001b14, DAT_20001b16 and DAT_20001b18 (4 x u16 = 8 bytes, likely a feature/option mask sent in a protocol frame). Cases 4 and 6 share one configuration, case 3 keeps the defaults. Called from vcu_0159_08009da8 and vcu_0159_0800b294.

**Notes:** Meaning of the individual bits of the four words is unknown; they could be feature enables per model/market variant.

- Addresses by version: 148: 0x080053B8, 14a: 0x080057A4, 14b: 0x08005ACC, 14e: 0x08005B04, 14f: 0x08005B60, 152: 0x08005BB8, 153: 0x08005C54, 0159: 0x08005DB8
- Called by: `vcu_0159_08009da8`, `vcu_runtime_defaults_init`
- Confidence: medium

## vcu_flag_bitmap_expand

**Detect changes in three 16-bit flag words and expand set bits into an item index list**

Watches three 16-bit flag words (current values at DAT_20001CE0, CE2 and CE4). When any of them differs from its last copy (DAT_200022C8, CA and CC), it copies the new values to the last copies and to working words DAT_2000148A, C and E, zeroes the list count DAT_200021E4, sets the pending flag DAT_200022D6, and calls app_set_state(2). While the pending flag is set, it expands each working word into the item list at DAT_200021E8: bit i of the first word adds i+1, of the second adds i+0x11, and of the third adds i+0x21, giving up to 48 items in order. The working words are shifted to zero as they are read, and the pending flag is not cleared here.

**Notes:** The meaning of the flag words and the item numbers is not established in this packet.

- Addresses by version: 148: 0x08002624, 14a: 0x0800269C, 14b: 0x08002954, 14e: 0x08002954, 14f: 0x080029B0, 152: 0x080029EC, 153: 0x08002A08, 0159: 0x080029F4
- Called by: `vcu_0159_0800a15c`, `vcu_0159_0800a1d0`
- Calls: `app_set_state`
- Confidence: medium

## vcu_pa6_output_status_update

**Drive PA6 from the output latch and rewrite the mode code in status word DAT_20001f98**

Per-tick controller for the PA6 output (GPIOA pin 0x40), driven only through vcu_pa6_output_set, and for the 16-bit status word DAT_20001f98. Bits 9-11 of that word hold a 3-bit mode code that is rewritten on each call: 1 (0x200) when debounced condition DAT_20001f69 is active and DAT_20001e68 bit 6 is set, 2 (0x400) while the output latch is set or the variant path keeps the pin high, 3 (0x600) when DAT_20001fec is set or DAT_20001f4f is set with DAT_20001b6e zero, and 4 (0x800) when DAT_20001f4f is set with DAT_20001b6e nonzero. Bit 14 is set from DAT_20001b12 bit 1 (except when DAT_2000123e is 7 or 8) and cleared on most other paths. The output latch DAT_20001340 is set when mode byte DAT_20001fa4 is 4 and DAT_2000123e is not 7, cleared once the condition is gone, and DAT_20001cfa mirrors the pin level. Variant codes DAT_20001fa7 == 2 or 5 take a separate branch that keeps the pin high while DAT_20001f53 is set, and DAT_20001fd4 forces the pin low in the debounced branch.

**Notes:** The load behind PA6 is not identified. The meanings of mode codes 1-4 are inferred from the code paths alone. Callers are not in this packet. The mode field has the same shape in every build, only the RAM addresses differ.

- Addresses by version: 148: 0x08002710, 14a: 0x08002788, 14b: 0x08002A40, 14e: 0x08002A40, 14f: 0x08002A9C, 152: 0x08002AD8, 153: 0x08002AF4, 0159: 0x08002AE0
- Called by: `vcu_0159_0800a15c`, `vcu_0159_0800a1d0`, `vcu_0159_0800a264`, `vcu_0159_0800a500`
- Calls: `vcu_pa6_output_set`
- Confidence: medium

## vcu_pair_pulse_pattern_step

**Run a 60-tick two-output pulse pattern after a change of DAT_20001fb5**

When mode byte DAT_20001fa7 is not 4 or 6 and no inhibit is set (DAT_20002022 or DAT_20002023, or DAT_20001fe8 equal to 10), it watches DAT_20001fb5: a change to a nonzero value while bit 2 of DAT_20001aee is set arms the countdown DAT_20001344 at 60 if bit 14 of DAT_20001af0 is also set, and otherwise cancels it. Each call decrements the countdown and calls vcu_0159_08008a28 and vcu_0159_08008a0c with the same argument: 1 while the remaining count is 41-59 or 1-20, and 0 while it is 21-40 and at 0. The outputs are therefore on for about 39 of 60 calls per trigger.

**Notes:** The two output routines are not described in this packet, so only their arguments are recorded. The trigger source DAT_20001fb5 is set by the EXINT handlers (see vcu_0159_080058ac and vcu_0159_080058f0), which is consistent with a button or switch input, not confirmed.

- Addresses by version: 148: 0x080039AC, 14a: 0x08003D04, 14b: 0x08004044, 14e: 0x08004064, 14f: 0x080040C0, 152: 0x08004124, 153: 0x08004144, 0159: 0x0800422C
- Called by: `vcu_0159_0800a500`, `vcu_0159_0800a55c`, `vcu_0159_0800a5c8`
- Calls: `vcu_gpio_c14_set`, `vcu_gpio_c15_set`
- Confidence: medium

## vcu_runtime_defaults_init

**Load default runtime status words and mode limits, then apply the variant configuration**

Sets the power-on defaults of a block of application words: clears bit 2 of DAT_20001aec, zeroes DAT_20001b76, DAT_20001b96, DAT_20001b98 and DAT_20001b6e, writes 0x5810 to DAT_20001aee and 0x0981 to DAT_20001af0, sets DAT_20001af2 to 2, ORs 3 into DAT_20001b32 and 2 into DAT_20001b12, sets DAT_20001b46 to 5, DAT_20001b48 to 2, DAT_20001b94 and DAT_20001b9c to 1, DAT_20001b68 (operating mode) to 1, DAT_20001b90 to 2, and DAT_20001ba6 and DAT_20001ba8 to 2. It then calls app_apply_mode_limits (FUN_080017e8) and vcu_apply_variant_config (FUN_08005db8), and finally sets DAT_20001fbe to 1, clears DAT_20001c88 and sets DAT_20001f54 to 1.

- Addresses by version: 148: 0x0800A394, 14a: 0x0800A78C, 14b: 0x0800AC14, 14e: 0x0800ACA8, 14f: 0x0800ADE4, 152: 0x0800B064, 153: 0x0800B158, 0159: 0x0800B294
- Called by: `vcu_0159_080031f4`, `vcu_0159_080054ec`
- Calls: `app_apply_mode_limits`, `vcu_apply_variant_config`
- Confidence: high

## vcu_sanitize_mode_1_to_4

**Force the byte at param_1 into the range 1..4 (default 1)**

If *param_1 is not one of 1, 2, 3 or 4, it is replaced by 1. Used to validate a 4-valued setting loaded from stored configuration. Called from vcu_0159_08009da8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pointer to the u8 setting to validate |

- Addresses by version: 148: 0x08005E40, 14a: 0x08006260, 14b: 0x080065D0, 14e: 0x08006608, 14f: 0x08006664, 152: 0x080066E4, 153: 0x08006780, 0159: 0x0800686C
- Called by: `vcu_0159_08009da8`
- Confidence: high

## vcu_serial_check_default

**Classify the stored serial string at DAT_20001ad4 against the default '1K1E0000000001'**

Builds the 14-character template "1K1E0000000001" on the stack and compares it with the string at DAT_20001ad4, character by character. Returns 1 if all 14 characters match (factory default / unprogrammed serial), 2 if a non-alphanumeric character (not 0-9, A-Z, a-z) is found before 14 characters were matched (invalid serial), and 0 if an alphanumeric character differs from the template (a real, different serial). Called from vcu_0159_08005bb4.

**Returns** `u32`: 0 = different valid serial, 1 = equals default template, 2 = invalid (non-alphanumeric) character

**Notes:** Role of the string as a serial number follows from its '1K1' prefix and the sibling parser; return code meanings derived from control flow.

- Addresses by version: 148: 0x08005CB0, 14a: 0x080060D0, 14b: 0x08006440, 14e: 0x08006478, 14f: 0x080064D4, 152: 0x08006554, 153: 0x080065F0, 0159: 0x080066DC
- Called by: `vcu_0159_08005bb4`
- Confidence: medium

## vcu_serial_match_set_flag

**Compare two 14-byte strings and set a flag when they are identical**

Compares param_1 and param_2 byte by byte over exactly 14 bytes (index kept in a u8 loop counter, stops at the first difference). If all 14 bytes match, writes 1 to the global flag DAT_20001f68; otherwise the flag is left untouched (it is never cleared here). The 14-byte length matches the 14-character product/serial string handled by vcu_serial_check_default and vcu_serial_parse_variant_code, so this is most likely a serial-number-equals-stored-copy check. Called from the large configuration/communication routine vcu_0159_08009da8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | first 14-byte buffer |
| `param_2` | `ptr` | second 14-byte buffer |

**Notes:** That the buffers are serial numbers is inferred from the length 14 and the caller, not proven.

- Addresses by version: 148: 0x08002AB0, 14a: 0x08002B34, 14b: 0x08002DEC, 14e: 0x08002DEC, 14f: 0x08002E48, 152: 0x08002EB4, 153: 0x08002ED0, 0159: 0x08002F08
- Called by: `vcu_0159_08009da8`
- Confidence: medium

## vcu_serial_parse_variant_code

**Decode the variant letter of a '1K1x' serial prefix into DAT_20001fa7**

param_1 points to a character string. If it begins with "1K1", the 4th character is mapped to a variant index stored in DAT_20001fa7: 'A'->0, 'E'->1, 'D'->2, 'U'->3, 'Z'->4, 'I'->5, 'G'->6, anything else -> 1. If the prefix is not "1K1" the index is 4. It then sets DAT_20001fa5 = 1 (variant valid/changed) and stores ((DAT_20001b40 >> 8) + 3) & 0xFF into DAT_20001032. The index is consumed by vcu_apply_variant_config to select the feature flag words; both are called from vcu_0159_08009da8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pointer to the serial/model string (at least 4 chars) |

**Notes:** The letters are likely market/region or model variants; exact meaning is a guess. The role of DAT_20001b40>>8 (+3) is unknown.

- Addresses by version: 148: 0x08003D60, 14a: 0x080040B8, 14b: 0x080043F8, 14e: 0x08004424, 14f: 0x08004480, 152: 0x080044E0, 153: 0x080044F8, 0159: 0x08004714
- Called by: `vcu_0159_08009da8`
- Confidence: medium

## vcu_special_mode_gate

**Enter and leave special mode stage DAT_20001fd6 after a 300-tick hold**

Gate for the special mode stage DAT_20001fd6: 0 idle, 1 entered after DAT_20001364 counts past 299 while the gate holds, and 2 when the entry latch DAT_20001359 has cleared. It runs a quiet counter DAT_20001366 that latches DAT_2000135a after more than 100 ticks while DAT_20001cf8 is clear and DAT_20001f4f is low. The gate needs bit 5 of DAT_20001aee set, DAT_20001f66, DAT_20001f64, DAT_20001f63 and DAT_20001f6a all clear, DAT_20001f4f set, DAT_20001f50 clear and DAT_2000135a set, and then sets DAT_20001359 and DAT_20001fd6 = 1, sets DAT_20001d04, sets bits 2 and 3 of DAT_20001f92 and calls app_set_state(4). When the gate fails, the counters and flags clear; stage 2 drops back to 0, clears DAT_20001d04 and bits 2-3 of DAT_20001f92, and calls app_set_state(1). A second path, selected by the one-shot request DAT_20001f71, performs the same entry and exit.

**Notes:** The meaning of stage 1 and stage 2 is not established. On the one-shot DAT_20001f71 path the stop call app_set_state is shown with no argument, so the state written there is unknown.

- Addresses by version: 148: 0x08003218, 14a: 0x08003424, 14b: 0x08003738, 14e: 0x08003738, 14f: 0x08003794, 152: 0x080037FC, 153: 0x0800381C, 0159: 0x080038A4
- Called by: `vcu_0159_0800a1d0`
- Calls: `app_set_state`
- Confidence: medium

## vcu_standby_entry_timer

**Enter standby after 600 quiet ticks and manage request bit 2 of DAT_20001f92**

Tracks the standby request DAT_20001cf6. While DAT_20001f48 is clear and special stage DAT_20001fd6 is 0, it counts DAT_200013a4 when the quiet conditions hold (DAT_20001cf6 clear, bit 0 of DAT_20001f78 clear, DAT_20001b62 below 30, DAT_20001fd5 and DAT_20001f4f clear, mode byte DAT_20001fa4 not 4) and either DAT_20001b38 is below 3 or DAT_20001f70 is set. After more than 600 ticks, or at once when DAT_20001f70 is set, it sets DAT_20001cf6 = 1 and calls app_set_state with the argument not recovered. While DAT_20001cf6 is 1 it leaves standby when DAT_20001f4f is set, the mode byte is 4, DAT_20001b62 exceeds 29 or DAT_20001f70 is set, calling app_set_state(4) and clearing the counter. Bit 2 of DAT_20001f92 is set on the path where DAT_20001b64 is zero and the DAT_20001b62 / 10 versus DAT_20001b38 test fails, and cleared on the other paths; when DAT_20001f48 is set, bit 1 of DAT_20001aec is set.

**Notes:** The app_set_state call that enters standby has no recovered argument. DAT_20001fd9 (a restart request from the ready sequence) is cleared here when DAT_20001f50 is clear. The meaning of DAT_20001f48 is not established.

- Addresses by version: 148: 0x080048AC, 14a: 0x08004C38, 14b: 0x08004F80, 14e: 0x08004FB8, 14f: 0x08005014, 152: 0x08005074, 153: 0x0800508C, 0159: 0x080051E8
- Called by: `vcu_0159_0800a1d0`
- Calls: `app_set_state`
- Confidence: medium
