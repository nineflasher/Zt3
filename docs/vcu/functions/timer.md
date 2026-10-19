# VCU - `timer` functions

24 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`delay_ms`](#delay_ms) | 0x0800BAB0 | Blocking millisecond delay using SysTick |
| [`delay_us`](#delay_us) | 0x0800BB00 | Blocking microsecond delay using SysTick |
| [`systick_clock_source_config`](#systick_clock_source_config) | 0x0800EA74 | Select the SysTick clock source: core clock (no divide) or core clock / 8 |
| [`tmr2_pwm_output_disable`](#tmr2_pwm_output_disable) | 0x08001BBC | Clear TMR2 capture/compare enable bit 0 to turn the channel-1 output off |
| [`tmr2_pwm_set_frequency`](#tmr2_pwm_set_frequency) | 0x08001B78 | Start TMR2 channel 1 PWM at a given frequency (Hz) with 3/4 compare value |
| [`tmr_base_init`](#tmr_base_init) | 0x0800EDB4 | Set the timer period (PR) and prescaler (DIV) and force an update event |
| [`tmr_channel_value_set`](#tmr_channel_value_set) | 0x0800EDC2 | Write a timer channel compare value (C1DT..C4DT) selected by channel number |
| [`tmr_cnt_dir_set`](#tmr_cnt_dir_set) | 0x0800EDE2 | Set the timer counting direction (CTRL1.CNT_DIR, bits 6..4) |
| [`tmr_counter_enable`](#tmr_counter_enable) | 0x0800EDEC | Start or stop the timer counter through CTRL1.TMREN (bit 0) |
| [`tmr_flag_clear`](#tmr_flag_clear) | 0x0800EDF6 | Clear timer interrupt status flags by writing the inverted mask to ISTS |
| [`tmr_flag_get`](#tmr_flag_get) | 0x0800EDFC | Test whether any of the given TMR status flags is set (SDK tmr_flag_get) |
| [`tmr_interrupt_enable`](#tmr_interrupt_enable) | 0x0800EE0A | Set or clear TMR interrupt-enable bits (SDK tmr_interrupt_enable) |
| [`tmr_output_channel_config`](#tmr_output_channel_config) | 0x0800EE22 | Configure a TMR output-compare channel from a tmr_output_config_type (SDK) |
| [`tmr_output_default_para_init`](#tmr_output_default_para_init) | 0x0800EEF8 | Zero all seven fields of a tmr_output_config_type (SDK) |
| [`tmr_output_enable`](#tmr_output_enable) | 0x0800EF0A | Set or clear the TMR main output enable (BRK.OEN) bit (SDK) |
| [`vcu_alert_tone_start_if_idle`](#vcu_alert_tone_start_if_idle) | 0x08006AE0 | Start the tone with argument 0xAAA only while the TMR2 channel 1 output is off |
| [`vcu_systick_resume`](#vcu_systick_resume) | 0x0800EAB0 | Restore the SysTick enable bit from the value saved by vcu_systick_suspend |
| [`vcu_systick_suspend`](#vcu_systick_suspend) | 0x0800EA90 | Save the SysTick enable bit to RAM and stop the SysTick counter |
| [`vcu_systick_timebase_init`](#vcu_systick_timebase_init) | 0x08002030 | Select the core clock for SysTick and derive the ticks-per-us and ticks-per-ms globals |
| [`vcu_tmr2_ch1_pwm_init`](#vcu_tmr2_ch1_pwm_init) | 0x08001BCA | Configure the TMR2 base and channel-1 PWM output, then start the counter |
| [`vcu_tmr2_ch1_pwm_start`](#vcu_tmr2_ch1_pwm_start) | 0x08001BA8 | Program TMR2 channel 1 PWM frequency, then enable the channel 1 output |
| [`vcu_tmr2_pwm_pa0_bringup`](#vcu_tmr2_pwm_pa0_bringup) | 0x08001E6C | Bring up PA0 and then the TMR2 channel-1 PWM output |
| [`vcu_tmr2_pwm_pa0_bringup_14a`](#vcu_tmr2_pwm_pa0_bringup_14a) | (removed) | Bring up PA0 and the TMR2 channel-1 PWM base in the 14a build |
| [`vcu_tmr5_1khz_tick_init`](#vcu_tmr5_1khz_tick_init) | 0x0800261C | Start TMR5 as a 1 kHz overflow interrupt tick (PR 143, DIV 999, IRQ 50) |

## delay_ms

**Blocking millisecond delay using SysTick**

Loops over chunks of at most 50 ms (0x32): loads SysTick LOAD (0xE000E014) with ticks_per_ms * n (ticks_per_ms = byte-wide global at 0x200018b4, set by the delay init), clears VAL, sets ENABLE, spins until COUNTFLAG (bit16) is set, then disables SysTick and clears VAL. The remaining count is masked to 16 bits. Standard Artery delay_ms pattern; callers vcu_0159_08003f40 and vcu_0159_08006184. Reconfigures SysTick, so it conflicts with any use of SysTick as a periodic tick at the same time.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | delay in milliseconds (up to 65535) |

**Notes:** The SysTick tick-per-ms factor (0x200018b4) is initialised elsewhere (vcu_0159 wave1_batch01 area); that it is used to count 1 ms while another path uses SysTick as the system tick is not checked.

- Addresses by version: 148: 0x0800ABE0, 14a: 0x0800AFCC, 14b: 0x0800B458, 14e: 0x0800B4EC, 14f: 0x0800B628, 152: 0x0800B8B4, 153: 0x0800B9A8, 0159: 0x0800BAB0
- Peripheral registers: `SysTick+0x0` (RW), `SysTick+0x4` (W), `SysTick+0x8` (W)
- Called by: `vcu_fault_warning_evaluate`, `vcu_fw_update_frame_handler`
- Confidence: medium

## delay_us

**Blocking microsecond delay using SysTick**

Loads SysTick LOAD with ticks_per_us * param_1 (ticks_per_us is the global at 0x200018b0), clears VAL, enables SysTick, spins until COUNTFLAG (bit16) is set, then disables it and clears VAL. No chunking, so param_1 must fit the 24-bit counter at the configured tick rate. Artery delay_us pattern; sole caller vcu_0159_0800688c (likely a bit-banged peripheral). Companion of delay_ms.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | delay in microseconds |

**Notes:** Name chosen from the Artery delay.c convention; global names for 0x200018b0/0x200018b4 are not annotated in this packet.

- Addresses by version: 148: 0x0800AC30, 14a: 0x0800B01C, 14b: 0x0800B4A8, 14e: 0x0800B53C, 14f: 0x0800B678, 152: 0x0800B904, 153: 0x0800B9F8, 0159: 0x0800BB00
- Peripheral registers: `SysTick+0x0` (RW), `SysTick+0x4` (W), `SysTick+0x8` (W)
- Called by: `vcu_deep_sleep_enter_and_restore`
- Confidence: medium

## systick_clock_source_config

**Select the SysTick clock source: core clock (no divide) or core clock / 8**

Sets SysTick.CTRL bit 2 (CLKSOURCE) when the argument is SYSTICK_CLOCK_SOURCE_AHBCLK_NODIV (4) and clears it for any other value, which selects the AHB clock divided by 8. This is the Artery SDK systick_clock_source_config Its caller is vcu_0159_08002030.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | clock source: 4 = AHB without divider, 0 = AHB divided by 8 |

- Addresses by version: 148: 0x0800DA54, 14a: 0x0800DEF0, 14b: 0x0800E37C, 14e: 0x0800E41C, 14f: 0x0800E568, 152: 0x0800E810, 153: 0x0800E904, 0159: 0x0800EA74
- Peripheral registers: `SysTick+0x0` (RW)
- Called by: `vcu_systick_timebase_init`
- Confidence: high

## tmr2_pwm_output_disable

**Clear TMR2 capture/compare enable bit 0 to turn the channel-1 output off**

Read-modify-write of the register at 0x40000020 (TMR2.CCTRL): clears bit 0 (C1EN), disabling the channel 1 compare output while leaving the counter running. Counterpart of tmr2_pwm_set_frequency (the enable bit is set elsewhere, presumably in the caller of that routine). Called from vcu_0159_08002d64, 080042f8, 08006b24 and 0800a39c.

**Notes:** Harness decoded the register as TMR2.CCTRL; buzzer/tone output is a guess from the paired frequency routine.

- Addresses by version: 148: 0x080017D8, 14a: 0x08001410, 14b: 0x08001AF4, 14e: 0x08001AF4, 14f: 0x08001B50, 152: 0x08001B8C, 153: 0x08001BA8, 0159: 0x08001BBC
- Peripheral registers: `TMR2.CTRL1` (A), `TMR2.CCTRL` (RW)
- Called by: `vcu_alert_tone_sequencer`, `vcu_c14_c15_pulse_sequencer`, `vcu_ninebot_rx_cmd_handle`, `vcu_0159_0800a39c`
- Confidence: medium

## tmr2_pwm_set_frequency

**Start TMR2 channel 1 PWM at a given frequency (Hz) with 3/4 compare value**

Clears TMR2.CTRL1.TMREN (bit 0) to stop the counter, writes period PR (0x4000002C) = 1000000 / param_1 and channel-1 compare C1DT (0x40000034) = PR - PR/4 (75% of the period), resets the counter CVAL (0x40000024) to 0 and re-enables the timer. The period arithmetic assumes the timer counts at 1 MHz (prescaler set elsewhere), so param_1 is a frequency in Hz; param_1 = 0 would divide by zero. Looks like a buzzer / tone generator; sole caller is vcu_0159_08001ba8, and vcu_0159_08001bbc switches the output off. Output enable is separate (TMR2.CCTRL).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | output frequency in Hz (timer assumed 1 MHz) |

**Notes:** Buzzer use and the 1 MHz timer clock are inferred; duty polarity depends on the TMR2 channel mode set at init.

- Addresses by version: 148: 0x08001794, 14a: 0x08001808, 14b: 0x08001AB0, 14e: 0x08001AB0, 14f: 0x08001B0C, 152: 0x08001B48, 153: 0x08001B64, 0159: 0x08001B78
- Peripheral registers: `TMR2.CTRL1` (RW), `TMR2.CVAL` (W), `TMR2.PR` (W), `TMR2.C1DT` (W)
- Called by: `vcu_tmr2_ch1_pwm_start`
- Confidence: medium

## tmr_base_init

**Set the timer period (PR) and prescaler (DIV) and force an update event**

Writes the period register at offset 0x2C and the prescaler register at 0x28 of the timer block, then sets SWEVT.OVFSWTR (bit 0 of offset 0x14), which generates an update event so the new values load into the shadow registers at once. This is the Artery SDK tmr_base_init. The timer must still be started with tmr_counter_enable.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | timer peripheral base (TMRx) |
| `param_2` | `u32` | period value (PR, auto-reload) |
| `param_3` | `u32` | prescaler value (DIV) |

- Addresses by version: 148: 0x0800DD90, 14a: 0x0800E22C, 14b: 0x0800E6BC, 14e: 0x0800E75C, 14f: 0x0800E8A8, 152: 0x0800EB50, 153: 0x0800EC44, 0159: 0x0800EDB4
- Called by: `vcu_tmr2_ch1_pwm_init`, `vcu_tmr5_1khz_tick_init`
- Confidence: high

## tmr_channel_value_set

**Write a timer channel compare value (C1DT..C4DT) selected by channel number**

Stores the value into the capture/compare register of the chosen channel: 0 selects C1DT (offset 0x34), 2 selects C2DT (0x38), 4 selects C3DT (0x3C) and 6 selects C4DT (0x40). The codes are the TMR_SELECT_CHANNEL_n values, and the complementary variants (1, 3, 5) are not handled, so they do nothing. This is the Artery SDK tmr_channel_value_set.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | timer peripheral base (TMRx) |
| `param_2` | `u32` | channel code: 0 = channel 1, 2 = channel 2, 4 = channel 3, 6 = channel 4 |
| `param_3` | `u32` | compare value |

- Addresses by version: 148: 0x0800DD9E, 14a: 0x0800E23A, 14b: 0x0800E6CA, 14e: 0x0800E76A, 14f: 0x0800E8B6, 152: 0x0800EB5E, 153: 0x0800EC52, 0159: 0x0800EDC2
- Called by: `vcu_tmr2_ch1_pwm_init`
- Confidence: high

## tmr_cnt_dir_set

**Set the timer counting direction (CTRL1.CNT_DIR, bits 6..4)**

Writes the three-bit CNT_DIR field (bits 6..4 of CTRL1) to the low three bits of the argument, leaving the other control bits unchanged. The value selects up, down or center-aligned counting. This is the Artery SDK tmr_cnt_dir_set.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | timer peripheral base (TMRx) |
| `param_2` | `u32` | counting mode (tmr_count_mode_type) |

- Addresses by version: 148: 0x0800DDBE, 14a: 0x0800E25A, 14b: 0x0800E6EA, 14e: 0x0800E78A, 14f: 0x0800E8D6, 152: 0x0800EB7E, 153: 0x0800EC72, 0159: 0x0800EDE2
- Called by: `vcu_tmr2_ch1_pwm_init`, `vcu_tmr5_1khz_tick_init`
- Confidence: high

## tmr_counter_enable

**Start or stop the timer counter through CTRL1.TMREN (bit 0)**

Sets or clears bit 0 (TMREN) of CTRL1 with a read-modify-write that keeps the other bits. This is the Artery SDK tmr_counter_enable and it is the last step of timer start-up after tmr_base_init and the channel setup.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | timer peripheral base (TMRx) |
| `param_2` | `u32` | confirm_state: non-zero starts the counter, zero stops it |

- Addresses by version: 148: 0x0800DDC8, 14a: 0x0800E264, 14b: 0x0800E6F4, 14e: 0x0800E794, 14f: 0x0800E8E0, 152: 0x0800EB88, 153: 0x0800EC7C, 0159: 0x0800EDEC
- Called by: `vcu_tmr2_ch1_pwm_init`, `vcu_tmr5_1khz_tick_init`
- Confidence: high

## tmr_flag_clear

**Clear timer interrupt status flags by writing the inverted mask to ISTS**

Stores ~flag in the interrupt status register at offset 0x10. ISTS is rc_w0: a 0 written to a bit clears that flag, and a 1 leaves the flag unchanged, so only the bits in the mask are cleared. This is the Artery SDK tmr_flag_clear. Its callers are not visible in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | timer peripheral base (TMRx) |
| `param_2` | `u32` | mask of status flags to clear |

- Addresses by version: 148: 0x0800DDD2, 14a: 0x0800E26E, 14b: 0x0800E6FE, 14e: 0x0800E79E, 14f: 0x0800E8EA, 152: 0x0800EB92, 153: 0x0800EC86, 0159: 0x0800EDF6
- Called by: `TMR5_GLOBAL_IRQHandler`
- Confidence: high

## tmr_flag_get

**Test whether any of the given TMR status flags is set (SDK tmr_flag_get)**

Matches the Artery SDK tmr_flag_get: returns true when (tmr->ists & flag) != 0, where ists is the interrupt status register at offset 0x10 of the timer block. Does not clear anything. Only caller is vcu_0159_0800898c, presumably a timer update/overflow ISR checking TMR_OVF_FLAG or similar. Part of the vendor timer driver group (tmr_*) at 0x0800ede0..0800ef0a.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR peripheral base (tmr_type*) |
| `param_2` | `u32` | flag mask (TMR_*_FLAG bits) |

**Returns** `bool`: true if any masked flag bit is set

- Addresses by version: 148: 0x0800DDD8, 14a: 0x0800E274, 14b: 0x0800E704, 14e: 0x0800E7A4, 14f: 0x0800E8F0, 152: 0x0800EB98, 153: 0x0800EC8C, 0159: 0x0800EDFC
- Called by: `TMR5_GLOBAL_IRQHandler`
- Confidence: high

## tmr_interrupt_enable

**Set or clear TMR interrupt-enable bits (SDK tmr_interrupt_enable)**

Matches the Artery SDK tmr_interrupt_enable: with param_3 == 1 ORs param_2 into the IDEN register (offset 0xC); with param_3 == 0 clears those bits; any other value leaves the register unchanged. Called from vcu_0159_0800261c, the timer init code.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR peripheral base (tmr_type*) |
| `param_2` | `u32` | interrupt mask (TMR_*_INT bits) |
| `param_3` | `u32` | 1 = enable, 0 = disable (confirm_state) |

- Addresses by version: 148: 0x0800DDE6, 14a: 0x0800E282, 14b: 0x0800E712, 14e: 0x0800E7B2, 14f: 0x0800E8FE, 152: 0x0800EBA6, 153: 0x0800EC9A, 0159: 0x0800EE0A
- Called by: `vcu_tmr5_1khz_tick_init`
- Confidence: high

## tmr_output_channel_config

**Configure a TMR output-compare channel from a tmr_output_config_type (SDK)**

Matches the Artery SDK tmr_output_channel_config. param_2 is the channel select value (0,2,4,6 for CH1..CH4, i.e. 2*channel index). param_3 points to a 7-byte tmr_output_config_type: [0] oc_mode, [1] oc_idle_state, [2] occ_idle_state, [3] oc_polarity, [4] occ_polarity, [5] oc_output_state, [6] occ_output_state. It writes the idle-state bits into CTRL2 (bits 8+ch and 9+ch), writes the OC mode (3 bits) into CM1 (offset 0x18) or CM2 (0x1C) at bit 4 or 12, and then sets polarity and enable bits in CCTRL (offset 0x20) at bit positions 2*ch..2*ch+3. Called from the PWM timer init vcu_0159_08001bca (together with tmr_output_default_para_init and tmr_output_enable).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR peripheral base (tmr_type*) |
| `param_2` | `u32` | channel select, 0/2/4/6 for CH1..CH4 |
| `param_3` | `ptr` | tmr_output_config_type, 7 byte fields |

**Notes:** The decompile does not clear the CxC bit (SDK sets c1c = FALSE); register masks match the SDK otherwise.

- Addresses by version: 148: 0x0800DDFE, 14a: 0x0800E29A, 14b: 0x0800E72A, 14e: 0x0800E7CA, 14f: 0x0800E916, 152: 0x0800EBBE, 153: 0x0800ECB2, 0159: 0x0800EE22
- Called by: `vcu_tmr2_ch1_pwm_init`
- Confidence: high

## tmr_output_default_para_init

**Zero all seven fields of a tmr_output_config_type (SDK)**

Matches the Artery SDK tmr_output_default_para_init: clears the 7 byte-wide members (oc_mode, idle states, polarities, output enables) so the struct is in the default state before the caller fills in selected fields and passes it to tmr_output_channel_config. Called from vcu_0159_08001bca.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | tmr_output_config_type to clear (7 bytes) |

- Addresses by version: 148: 0x0800DED4, 14a: 0x0800E370, 14b: 0x0800E800, 14e: 0x0800E8A0, 14f: 0x0800E9EC, 152: 0x0800EC94, 153: 0x0800ED88, 0159: 0x0800EEF8
- Called by: `vcu_tmr2_ch1_pwm_init`
- Confidence: high

## tmr_output_enable

**Set or clear the TMR main output enable (BRK.OEN) bit (SDK)**

Matches the Artery SDK tmr_output_enable: read-modify-write of the BRK register (offset 0x44) bit 15 (OEN) with (param_2 & 1). Needed on advanced timers (TMR1) for PWM outputs to appear on the pins. Called from the PWM setup vcu_0159_08001bca.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR peripheral base (tmr_type*) |
| `param_2` | `u32` | 1 = enable outputs, 0 = disable |

- Addresses by version: 148: 0x0800DEE6, 14a: 0x0800E382, 14b: 0x0800E812, 14e: 0x0800E8B2, 14f: 0x0800E9FE, 152: 0x0800ECA6, 153: 0x0800ED9A, 0159: 0x0800EF0A
- Called by: `vcu_tmr2_ch1_pwm_init`
- Confidence: high

## vcu_alert_tone_start_if_idle

**Start the tone with argument 0xAAA only while the TMR2 channel 1 output is off**

Reads TMR2.CCTRL (register at 0x40000020) and, when bit 0 (channel 1 compare output enable) is clear, calls vcu_0159_08001ba8 with 0xaaa to start the tone. When the output is already enabled it does nothing. Called from vcu_0159_080042f8, which is outside this packet.

- Addresses by version: 148: 0x08006074, 14a: 0x08006494, 14b: 0x08006804, 14e: 0x0800683C, 14f: 0x08006898, 152: 0x0800693C, 153: 0x080069D8, 0159: 0x08006AE0
- Peripheral registers: `TMR2.CCTRL` (R)
- Called by: `vcu_c14_c15_pulse_sequencer`
- Calls: `vcu_tmr2_ch1_pwm_start`
- Confidence: high

## vcu_systick_resume

**Restore the SysTick enable bit from the value saved by vcu_systick_suspend**

ORs the saved byte DAT_200018AC into SysTick.CTRL, so the counter restarts only when it was enabled before vcu_systick_suspend. It never clears ENABLE, so a call without a prior suspend leaves the counter unchanged. This is the second half of the suspend and resume group.

- Addresses by version: 148: 0x0800DA90, 14a: 0x0800DF2C, 14b: 0x0800E3B8, 14e: 0x0800E458, 14f: 0x0800E5A4, 152: 0x0800E84C, 153: 0x0800E940, 0159: 0x0800EAB0
- Peripheral registers: `SCnSCB+0x0` (A), `SysTick+0x0` (RW)
- Called by: `vcu_deep_sleep_enter_and_restore`
- Confidence: high

## vcu_systick_suspend

**Save the SysTick enable bit to RAM and stop the SysTick counter**

Copies SysTick.CTRL bit 0 (ENABLE) into the RAM byte DAT_200018AC and then clears ENABLE. All three callers of the suspend, resume and deep-sleep routines list vcu_0159_0800688c, so this is most likely part of a sleep sequence (medium). vcu_systick_resume (vcu_0159_0800eab0) restores the saved state, and the pair forms a two-function suspend and resume group.

- Addresses by version: 148: 0x0800DA70, 14a: 0x0800DF0C, 14b: 0x0800E398, 14e: 0x0800E438, 14f: 0x0800E584, 152: 0x0800E82C, 153: 0x0800E920, 0159: 0x0800EA90
- Peripheral registers: `SCnSCB+0x0` (A), `SysTick+0x0` (RW)
- Called by: `vcu_deep_sleep_enter_and_restore`
- Confidence: high

## vcu_systick_timebase_init

**Select the core clock for SysTick and derive the ticks-per-us and ticks-per-ms globals**

Sets SysTick to count the core clock with no divider (systick_clock_source_config with code 4) and derives the time-base globals used by delay_us and delay_ms. DAT_200018B0 becomes the core clock in MHz (the frequency in Hz at 0x200018BC divided by 1,000,000), and DAT_200018B4 becomes the ticks per millisecond (MHz times 1000). The core clock frequency must already be stored at 0x200018BC when this runs. It is called from the init sequence vcu_0159_08002060.

- Addresses by version: 148: 0x08001C4C, 14a: 0x08001CB4, 14b: 0x08001F68, 14e: 0x08001F68, 14f: 0x08001FC4, 152: 0x08002000, 153: 0x0800201C, 0159: 0x08002030
- Called by: `vcu_peripheral_init_sequence`
- Calls: `systick_clock_source_config`
- Confidence: high

## vcu_tmr2_ch1_pwm_init

**Configure the TMR2 base and channel-1 PWM output, then start the counter**

Zeroes a 20-byte local, enables the TMR2 clock (CRM id 0x1C0000) and reads the clock frequencies. It programs TMR2 with tmr_base_init(TMR2, PR 1, DIV 143), giving a 1 MHz count on a 144 MHz timer clock, sets the count direction to up, and fills a tmr_output_config_type with oc_mode 6 (PWM mode A), oc_idle_state 0, oc_polarity 0 and oc_output_state 1 (enabled). It then configures channel 1 with that struct, writes the channel-1 compare value, enables the main output (BRK.OEN) and starts the counter. The result is an idle PWM tone output on TMR2 channel 1 (the buzzer), which tmr2_pwm_set_frequency retunes later.

**Notes:** The 144 MHz timer clock is inferred from the 1 MHz count that tmr2_pwm_set_frequency assumes together with DIV 143. The compare-value argument of tmr_channel_value_set is not visible in the decompile. Callers: vcu_tmr2_pwm_pa0_bringup.

- Addresses by version: 148: 0x080017E6, 14b: 0x08001B02, 14e: 0x08001B02, 14f: 0x08001B5E, 152: 0x08001B9A, 153: 0x08001BB6, 0159: 0x08001BCA
- Peripheral registers: `TMR2.CTRL1` (A)
- Called by: `vcu_tmr2_pwm_pa0_bringup`
- Calls: `vcu_buf_zero`, `crm_clocks_freq_get`, `crm_periph_clock_enable`, `tmr_base_init`, `tmr_channel_value_set`, `tmr_cnt_dir_set`, `tmr_counter_enable`, `tmr_output_channel_config`, `tmr_output_default_para_init`, `tmr_output_enable`
- Confidence: medium

## vcu_tmr2_ch1_pwm_start

**Program TMR2 channel 1 PWM frequency, then enable the channel 1 output**

Starts the TMR2 channel 1 PWM output. It calls tmr2_pwm_set_frequency (vcu_0159_08001b78), which programs the period and the 3/4 compare value, then sets TMR2 CCTRL bit 0 (C1EN, channel 1 enable) with a read-modify-write, leaving the other channel bits unchanged. The packet's register reference TMR2.CTRL1 is wrong for this offset: 0x40000020 is TMR2.CCTRL. Callers are vcu_0159_08002d64, vcu_0159_08006ae0 and vcu_0159_08006b24.

**Notes:** The register offset was checked against the at32f415 register table: CCTRL is at 0x20 and C1EN is bit 0.

- Addresses by version: 148: 0x080017C4, 14a: 0x08001838, 14b: 0x08001AE0, 14e: 0x08001AE0, 14f: 0x08001B3C, 152: 0x08001B78, 153: 0x08001B94, 0159: 0x08001BA8
- Peripheral registers: `TMR2.CTRL1` (A), `TMR2.CCTRL` (RW)
- Called by: `vcu_alert_tone_sequencer`, `vcu_alert_tone_start_if_idle`, `vcu_ninebot_rx_cmd_handle`
- Calls: `tmr2_pwm_set_frequency`
- Confidence: high

## vcu_tmr2_pwm_pa0_bringup

**Bring up PA0 and then the TMR2 channel-1 PWM output**

Calls vcu_gpio_pa0_init, which configures PA0 (the default TMR2 channel-1 pin) first, and then vcu_tmr2_ch1_pwm_init, which sets up the TMR2 timer and its channel-1 PWM output. Together they are the full bring-up of the buzzer output path before any tone is requested.

**Notes:** Called from vcu_peripheral_init_sequence. The 14a build has the same two steps as vcu_tmr2_pwm_pa0_bringup_14a.

- Addresses by version: 148: 0x08001A88, 14b: 0x08001DA4, 14e: 0x08001DA4, 14f: 0x08001E00, 152: 0x08001E3C, 153: 0x08001E58, 0159: 0x08001E6C
- Called by: `vcu_peripheral_init_sequence`
- Calls: `vcu_tmr2_ch1_pwm_init`, `vcu_gpio_pa0_init`
- Confidence: high

## vcu_tmr2_pwm_pa0_bringup_14a

**Bring up PA0 and the TMR2 channel-1 PWM base in the 14a build**

Calls the PA0 setup first, then zeroes a 20-byte local, enables the TMR2 clock (CRM id 0x1C0000), reads the clock frequencies and programs TMR2 with PR 1 and DIV 143, which counts at 1 MHz on a 144 MHz timer clock. It sets up the channel-1 output as PWM mode A (mode code 6) with the output enabled, writes the channel-1 compare value, enables the main output (BRK.OEN) and starts the counter. The tone frequency is written later by tmr2_pwm_set_frequency, which sets PR to 1000000 divided by the frequency.

**Notes:** This is the 14a copy of the 0159 bring-up split into vcu_tmr2_pwm_pa0_bringup (PA0 step) and vcu_tmr2_ch1_pwm_init (TMR2 step), both inlined here. The leading call FUN_08001AB4 is taken to be the PA0 routine vcu_gpio_pa0_init, because the packet lists that routine as a callee; this image's address was not checked. The third argument of tmr_channel_value_set is not visible in the decompile, so the compare value written is whatever the register held.

- Addresses by version: 14a: 0x08001AF0
- Peripheral registers: `TMR2.CTRL1` (A)
- Called by: `vcu_peripheral_init_sequence`
- Calls: `vcu_buf_zero`, `vcu_gpio_pa0_init`, `crm_clocks_freq_get`, `crm_periph_clock_enable`, `tmr_base_init`, `tmr_channel_value_set`, `tmr_cnt_dir_set`, `tmr_counter_enable`, `tmr_output_channel_config`, `tmr_output_default_para_init`, `tmr_output_enable`
- Confidence: medium

## vcu_tmr5_1khz_tick_init

**Start TMR5 as a 1 kHz overflow interrupt tick (PR 143, DIV 999, IRQ 50)**

Zeroes a 20-byte local, enables the TMR5 clock (CRM id 0x1C0003) and reads the clock frequencies. It calls tmr_base_init(TMR5, PR 143, DIV 999), sets the count direction to up, enables the overflow interrupt and enables NVIC IRQ 50 (TMR5_GLOBAL) with preemption priority 1 and sub-priority 0, then starts the counter. With a 144 MHz timer clock, 144e6 divided by (1000 times 144) is 1 kHz, and the overflow handler TMR5_GLOBAL_IRQHandler (vcu_0159_0800898C) counts those overflows.

**Notes:** The 1 kHz rate depends on the 144 MHz timer clock inferred from the TMR2 setup, not on a stated clock value. Only the overflow count is kept by the handler (DAT_20001350), so this is the application's periodic timebase source.

- Addresses by version: 148: 0x08002248, 14a: 0x080022B8, 14b: 0x0800257C, 14e: 0x0800257C, 14f: 0x080025D8, 152: 0x08002614, 153: 0x08002630, 0159: 0x0800261C
- Peripheral registers: `TMR5.CTRL1` (A)
- Called by: `vcu_peripheral_init_sequence`
- Calls: `vcu_buf_zero`, `crm_clocks_freq_get`, `crm_periph_clock_enable`, `nvic_irq_enable`, `tmr_base_init`, `tmr_cnt_dir_set`, `tmr_counter_enable`, `tmr_interrupt_enable`
- Confidence: medium
