# MCU - `timer` functions

21 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_busy_wait_systick_counts`](#mcu_busy_wait_systick_counts) | 0x080061A6 | Busy-wait until SysTick has counted down param_1 counts |
| [`mcu_timed_hold_countdown`](#mcu_timed_hold_countdown) | 0x08005E7C | One-shot 0x567-count hold timer: started by request flag 0x20001FC8, run down per call |
| [`mcu_timeout_tick_v12b`](#mcu_timeout_tick_v12b) | (removed) | Advance the MCU_12b 100-tick timeout counter and set flag DAT_20001F8A at saturation |
| [`mcu_timeout_tick_v143`](#mcu_timeout_tick_v143) | (removed) | Advance the MCU_143 100-tick timeout counter, decade counter and saturating byte counter |
| [`mcu_timeout_tick_v152`](#mcu_timeout_tick_v152) | (removed) | Advance the MCU_152 100-tick timeout counter and the level field in status halfword 0x20001FCE |
| [`mcu_tmr_iden_c2ien_set`](#mcu_tmr_iden_c2ien_set) | 0x0800E224 | Enable or disable the channel 2 compare interrupt (IDEN.C2IEN, bit 2) |
| [`mcu_tmr_iden_c3ien_set`](#mcu_tmr_iden_c3ien_set) | 0x0800E22E | Enable or disable the channel 3 compare interrupt (IDEN.C3IEN, bit 3) |
| [`mcu_tmr_swevt_trgswtr_set`](#mcu_tmr_swevt_trgswtr_set) | 0x0800E1A2 | Set or clear the software trigger event bit SWEVT.TRGSWTR (bit 6) |
| [`systick_clock_source_config`](#systick_clock_source_config) | 0x0800DBEC | Select the SysTick clock source: AHB clock undivided or AHB clock divided by 8 |
| [`tmr_32_bit_function_enable`](#tmr_32_bit_function_enable) | 0x0800DD98 | Set or clear CTRL1.PMEN (Plus Mode Enable, bit 10) on TMR2 and TMR5 only |
| [`tmr_base_init`](#tmr_base_init) | 0x0800DDB2 | Load the timer period (PR) and prescaler (DIV) and force an update event |
| [`tmr_channel1_input_select`](#tmr_channel1_input_select) | 0x0800DE1A | Set CTRL2.C1INSEL (bit 7), the source selection for the channel 1 input |
| [`tmr_clock_source_div_set`](#tmr_clock_source_div_set) | 0x0800DE9A | Set CTRL1.CLKDIV (bits 9:8), the clock divider of the timer |
| [`tmr_cnt_dir_set`](#tmr_cnt_dir_set) | 0x0800DEA4 | Set CTRL1.CNT_DIR (bits 6:4): counting direction and center-aligned mode |
| [`tmr_counter_enable`](#tmr_counter_enable) | 0x0800DEAE | Start or stop the timer counter through CTRL1.TMREN (bit 0) |
| [`tmr_flag_clear`](#tmr_flag_clear) | 0x0800DEB8 | Clear interrupt status flags by writing the inverted mask to ISTS |
| [`tmr_flag_get`](#tmr_flag_get) | 0x0800DEBE | Return true if any of the masked TMR interrupt status flags is set |
| [`tmr_interrupt_enable`](#tmr_interrupt_enable) | 0x0800DFF8 | Set or clear TMR interrupt and DMA enable bits in IDEN |
| [`tmr_overflow_request_source_set`](#tmr_overflow_request_source_set) | 0x0800E11E | Set CTRL1.OVFS (bit 2): overflow event source selection |
| [`tmr_sub_mode_select`](#tmr_sub_mode_select) | 0x0800E132 | Select the slave (subordinate) mode, STCTRL.SMSEL bits 2:0 |
| [`tmr_trigger_input_select`](#tmr_trigger_input_select) | 0x0800E13C | Select the slave trigger input source, STCTRL.STIS bits 6:4 |

## mcu_busy_wait_systick_counts

**Busy-wait until SysTick has counted down param_1 counts**

Polls the SysTick current-value register (SYST_CVR, 0xE000E018) and accumulates the decrease between successive reads. When a read is larger than the previous one the counter has wrapped, so 0xFFFFFF is added, which assumes a 24-bit reload. The loop exits once the accumulated count reaches param_1, so the argument is in SysTick clock cycles, not microseconds. It runs at least one iteration even for a zero argument. Callers are mcu_0160_0800226c, mcu_0160_08007df4 and mcu_0160_0800d548.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | wait length in SysTick counts |

- Addresses by version: 12b: 0x08006220, 143: 0x080060D6, 152: 0x08006106, 0160: 0x080061A6
- Peripheral registers: `SysTick+0x8` (R)
- Called by: `mcu_0160_0800226c`, `mcu_0160_08007df4`, `mcu_0160_0800d548`
- Confidence: high

## mcu_timed_hold_countdown

**One-shot 0x567-count hold timer: started by request flag 0x20001FC8, run down per call**

When the request byte at 0x20001FC8 is set, the routine loads the countdown 0x20000644 with 0x567 (1383), clears the request and sets the active byte 0x2000066C. While active, each call decrements the countdown; once it is below 1 the active and request bytes are both cleared. The hold therefore lasts about 1383 calls of the caller's tick, plus one. Called from mcu_0160_0800a320.

**Notes:** The period of the calling tick is not visible here, so the real-time length is unknown. The purpose of the hold is a guess.

- Addresses by version: 12b: 0x08005EE8, 143: 0x08005D6C, 152: 0x08005DDC, 0160: 0x08005E7C
- Called by: `mcu_0160_0800a320`
- Confidence: high

## mcu_timeout_tick_v12b

**Advance the MCU_12b 100-tick timeout counter and set flag DAT_20001F8A at saturation**

Counts DAT_200003B4 up to 100, one step per call. At 100 the counter stays there and the byte DAT_20001F8A is set to 1 on every call. This build has no decade or overflow counter. It is the same timeout pattern as mcu_timeout_tick_v143 and mcu_timeout_tick_v152.

**Notes:** Consumer of DAT_20001F8A is outside this packet. The 12b build is the only one with DAT_20001F8A.

- Addresses by version: 12b: 0x08007ED0
- Called by: `mcu_0160_0800a480`
- Confidence: medium

## mcu_timeout_tick_v143

**Advance the MCU_143 100-tick timeout counter, decade counter and saturating byte counter**

Per-call tick of a timeout. Counter DAT_200003AC counts up to 100; on every 10th count the decade counter DAT_20000324 is incremented. At 100 the counter stays saturated, DAT_20001FAA is set to 1 (timeout flag), and the overflow counter DAT_20000326 increments on every further call. Independently, the byte DAT_200003AE increments as a saturating 8-bit counter that stops at 0xFF. The 100-count saturation suggests a heartbeat or message-loss timeout of about 100 ticks (the tick period is not shown in this packet).

**Notes:** Timeout purpose is inferred from the 100-count saturation. The consumer of DAT_20001FAA is outside this packet.

- Addresses by version: 143: 0x08007DC4
- Called by: `mcu_0160_0800a480`
- Confidence: medium

## mcu_timeout_tick_v152

**Advance the MCU_152 100-tick timeout counter and the level field in status halfword 0x20001FCE**

Same timeout pattern as mcu_timeout_tick_v143 on DAT_200003B0: the counter saturates at 100, the decade counter DAT_20000330 steps every 10 counts, DAT_20001FC2 is set on saturation and the overflow counter DAT_20000332 increments while saturated, and the byte DAT_200003B2 is an 8-bit saturating counter. While saturated, DAT_20000634 counts timed-out ticks up to 0x189C (6300). Bits 9..11 of the status halfword DAT_20001FCE are a 3-bit level: after 300 timed-out ticks the level is forced to 2 (0x400) on every 100th tick unless it already is 2, and the level field is cleared when the 6300 cap is reached. The counter DAT_20000634 is reset to 0 as soon as the timeout counter is below saturation.

**Notes:** The meaning of the level field (escalation of a fault or timeout severity) is inferred from the write pattern only.

- Addresses by version: 152: 0x08007E4C
- Called by: `mcu_0160_0800a480`
- Confidence: medium

## mcu_tmr_iden_c2ien_set

**Enable or disable the channel 2 compare interrupt (IDEN.C2IEN, bit 2)**

Read-modify-write of bit 2 (C2IEN) of the interrupt/DMA enable register IDEN (offset 0x0C) with param_2 & 1, keeping the other bits. It is a single-bit update, not the mask-based SDK tmr_interrupt_enable. It is one of the setup steps in mcu_0160_0800ac52, which calls it with 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | 1 = enable, 0 = disable |

**Notes:** Only caller: mcu_0160_0800ac52.

- Addresses by version: 12b: 0x0800DDF0, 143: 0x0800E04C, 152: 0x0800E0E4, 0160: 0x0800E224
- Called by: `mcu_0160_0800ac52`
- Confidence: high

## mcu_tmr_iden_c3ien_set

**Enable or disable the channel 3 compare interrupt (IDEN.C3IEN, bit 3)**

Read-modify-write of bit 3 (C3IEN) of the interrupt/DMA enable register IDEN (offset 0x0C) with param_2 & 1, keeping the other bits. Same pattern as mcu_0160_0800e224 for channel 3; it is called from mcu_0160_0800ac52 with 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | 1 = enable, 0 = disable |

**Notes:** Only caller: mcu_0160_0800ac52.

- Addresses by version: 12b: 0x0800DDFA, 143: 0x0800E056, 152: 0x0800E0EE, 0160: 0x0800E22E
- Called by: `mcu_0160_0800ac52`
- Confidence: high

## mcu_tmr_swevt_trgswtr_set

**Set or clear the software trigger event bit SWEVT.TRGSWTR (bit 6)**

Read-modify-write of bit 6 (TRGSWTR) of the software event register SWEVT (offset 0x14) with param_2 & 1, keeping the other bits. Writing 1 requests a software trigger event, as the register data describes it. Unlike the SDK tmr_event_sw_trigger, which ORs a mask into SWEVT, this writes one bit and so can also write 0. It is one of the setup steps in mcu_0160_0800ac52.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | 1 = request software trigger event, 0 = write 0 to the bit |

**Notes:** Only caller: mcu_0160_0800ac52.

- Addresses by version: 12b: 0x0800DD6E, 143: 0x0800DFCA, 152: 0x0800E062, 0160: 0x0800E1A2
- Called by: `mcu_0160_0800ac52`
- Confidence: high

## systick_clock_source_config

**Select the SysTick clock source: AHB clock undivided or AHB clock divided by 8**

Sets SysTick.CTRL bit 2 (CLKSOURCE) when param_1 equals 4 (SYSTICK_CLOCK_SOURCE_AHBCLK_NODIV) and clears it for any other value, which selects the AHB clock divided by 8 (SYSTICK_CLOCK_SOURCE_AHBCLK_DIV8 = 0). The update is a read-modify-write, so the ENABLE and TICKINT bits are kept. This is the Artery SDK routine systick_clock_source_config. It is called from mcu_0160_0800c8f8 with 4 just before the SysTick counter is started.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | clock source: 4 = AHB clock without divider, 0 = AHB clock divided by 8 |

- Addresses by version: 12b: 0x0800D7B8, 143: 0x0800DA14, 152: 0x0800DAAC, 0160: 0x0800DBEC
- Peripheral registers: `SysTick+0x0` (RW)
- Called by: `mcu_0160_0800c8f8`
- Confidence: high

## tmr_32_bit_function_enable

**Set or clear CTRL1.PMEN (Plus Mode Enable, bit 10) on TMR2 and TMR5 only**

Matches the Artery SDK tmr_32_bit_function_enable. Only TMR2 and TMR5, the two 32-bit timers, are affected: for them bit 10 of CTRL1 is replaced with param_2 & 1 by a read-modify-write that keeps the other control bits. For any other timer pointer the function does nothing. Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer (TMR2 or TMR5 are the only ones acted on) |
| `param_2` | `u32` | confirm_state: 1 = enable, 0 = disable |

**Notes:** The repo register data only names CTRL1 bit 10 'Plus Mode Enable'; the hardware effect of PMEN is not documented in the repo. Only caller: mcu_0160_08009800.

- Addresses by version: 12b: 0x0800D964, 143: 0x0800DBC0, 152: 0x0800DC58, 0160: 0x0800DD98
- Called by: `mcu_0160_08009800`
- Confidence: high

## tmr_base_init

**Load the timer period (PR) and prescaler (DIV) and force an update event**

Matches the Artery SDK tmr_base_init. param_2 is written to the period register PR (offset 0x2C) and param_3 to the prescaler register DIV (offset 0x28). It then sets SWEVT.OVFSWTR (bit 0 of offset 0x14), which generates an update event so the new values are loaded into the shadow registers at once. The counter is started separately with tmr_counter_enable. The TMR4 setup at mcu_0160_08003060 passes PR = 999 and DIV = 0x8F (143). Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | period value (PR, auto-reload) |
| `param_3` | `u32` | prescaler value (DIV) |

- Addresses by version: 12b: 0x0800D97E, 143: 0x0800DBDA, 152: 0x0800DC72, 0160: 0x0800DDB2
- Called by: `mcu_0160_08003060`, `mcu_0160_08009800`, `mcu_0160_0800a6b8`
- Confidence: high

## tmr_channel1_input_select

**Set CTRL2.C1INSEL (bit 7), the source selection for the channel 1 input**

Matches the Artery SDK tmr_channel1_input_select. Read-modify-write of bit 7 of CTRL2 (offset 0x04) with param_2 & 1. The register data calls the bit 'C1IN selection'; what each value connects is not given in the repo register data. Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | connection select (1 bit, tmr_channel1_input_connected_type) |

**Notes:** Only caller: mcu_0160_08009800.

- Addresses by version: 12b: 0x0800D9E6, 143: 0x0800DC42, 152: 0x0800DCDA, 0160: 0x0800DE1A
- Called by: `mcu_0160_08009800`
- Confidence: high

## tmr_clock_source_div_set

**Set CTRL1.CLKDIV (bits 9:8), the clock divider of the timer**

Matches the Artery SDK tmr_clock_source_div_set. Read-modify-write of the 2-bit field at bits 9:8 of the first word of the block (CTRL1 for a TMR) with param_2 & 3, keeping the other bits. In the usual timer design this divider sets the clock used by dead-time generation and the input filters; the repo register data only says 'Clock divider', so that use is not confirmed here. Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer (first word is CTRL1) |
| `param_2` | `u32` | division code 0..3 (tmr_clock_division_type) |

**Notes:** Callers: mcu_0160_08003060, mcu_0160_08009800.

- Addresses by version: 12b: 0x0800DA66, 143: 0x0800DCC2, 152: 0x0800DD5A, 0160: 0x0800DE9A
- Called by: `mcu_0160_08003060`, `mcu_0160_08009800`
- Confidence: high

## tmr_cnt_dir_set

**Set CTRL1.CNT_DIR (bits 6:4): counting direction and center-aligned mode**

Matches the Artery SDK tmr_cnt_dir_set. Read-modify-write of the 3-bit CNT_DIR field at bits 6:4 of CTRL1 (OWCDIR at bit 4, TWCMSEL at bits 6:5 in the register data) with param_2 & 7; other CTRL1 bits are kept. The value selects up, down or one of the center-aligned counting modes (tmr_count_mode_type). Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | counting mode, 3 bits (tmr_count_mode_type) |

**Notes:** Callers: mcu_0160_08003060, mcu_0160_08009800, mcu_0160_0800a6b8.

- Addresses by version: 12b: 0x0800DA70, 143: 0x0800DCCC, 152: 0x0800DD64, 0160: 0x0800DEA4
- Called by: `mcu_0160_08003060`, `mcu_0160_08009800`, `mcu_0160_0800a6b8`
- Confidence: high

## tmr_counter_enable

**Start or stop the timer counter through CTRL1.TMREN (bit 0)**

Matches the Artery SDK tmr_counter_enable. Read-modify-write of bit 0 (TMREN) of CTRL1 with param_2 & 1, keeping the other bits. This is the switch that starts or stops the counter after the base and channel setup. Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | confirm_state: non-zero starts the counter, zero stops it |

**Notes:** Callers: mcu_0160_08003060, mcu_0160_08009800, mcu_0160_0800a6b8.

- Addresses by version: 12b: 0x0800DA7A, 143: 0x0800DCD6, 152: 0x0800DD6E, 0160: 0x0800DEAE
- Called by: `mcu_0160_08003060`, `mcu_0160_08009800`, `mcu_0160_0800a6b8`
- Confidence: high

## tmr_flag_clear

**Clear interrupt status flags by writing the inverted mask to ISTS**

Matches the Artery SDK tmr_flag_clear. Stores ~param_2 into the interrupt status register ISTS (offset 0x10) with a plain store, not a read-modify-write. ISTS flags are cleared by writing 0, so only the bits set in the mask are cleared; the other bits are written as 1 and have no effect. The TMR4 global interrupt handler mcu_0160_0800a85c is one of the callers. Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | mask of status flags to clear |

**Notes:** Callers: mcu_0160_08009800, mcu_0160_0800a85c.

- Addresses by version: 12b: 0x0800DA84, 143: 0x0800DCE0, 152: 0x0800DD78, 0160: 0x0800DEB8
- Called by: `mcu_0160_08009800`, `mcu_0160_0800a85c`
- Confidence: high

## tmr_flag_get

**Return true if any of the masked TMR interrupt status flags is set**

Matches the Artery SDK tmr_flag_get. Reads ISTS (offset 0x10) and returns whether (ISTS & param_2) is non-zero, so it is true when any masked flag is set. It does not clear anything; clearing is done with tmr_flag_clear. It is called from the TMR4 global interrupt handler mcu_0160_0800a85c, which polls the timer status flags. Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | mask of status flags to test |

**Returns** `bool`: true if any masked flag bit is set

**Notes:** Only caller: mcu_0160_0800a85c.

- Addresses by version: 12b: 0x0800DA8A, 143: 0x0800DCE6, 152: 0x0800DD7E, 0160: 0x0800DEBE
- Called by: `mcu_0160_0800a85c`
- Confidence: high

## tmr_interrupt_enable

**Set or clear TMR interrupt and DMA enable bits in IDEN**

Matches the Artery SDK tmr_interrupt_enable. With param_3 == 1, param_2 is ORed into the interrupt/DMA enable register IDEN (offset 0x0C); with param_3 == 0 those bits are cleared; any other value leaves IDEN unchanged. The mask uses the TMR_*_INT bits of IDEN, for example bit 0 OVFIEN, bit 1 C1IEN, bit 2 C2IEN and bit 3 C3IEN. Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | interrupt mask (TMR_*_INT bits) |
| `param_3` | `u32` | 1 = enable, 0 = disable (confirm_state) |

**Notes:** Callers: mcu_0160_08003060, mcu_0160_08009800.

- Addresses by version: 12b: 0x0800DBC4, 143: 0x0800DE20, 152: 0x0800DEB8, 0160: 0x0800DFF8
- Called by: `mcu_0160_08003060`, `mcu_0160_08009800`
- Confidence: high

## tmr_overflow_request_source_set

**Set CTRL1.OVFS (bit 2): overflow event source selection**

Matches the Artery SDK tmr_overflow_request_source_set. Read-modify-write of bit 2 (OVFS) of CTRL1 with param_2 & 1, keeping the other bits. The register data only names it 'Overflow event source'; the usual meaning is that when it is set, only counter overflow generates the overflow event. Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer (first word is CTRL1) |
| `param_2` | `u32` | 1 = counter overflow only (confirm_state) |

**Notes:** Only caller: mcu_0160_08009800.

- Addresses by version: 12b: 0x0800DCEA, 143: 0x0800DF46, 152: 0x0800DFDE, 0160: 0x0800E11E
- Called by: `mcu_0160_08009800`
- Confidence: high

## tmr_sub_mode_select

**Select the slave (subordinate) mode, STCTRL.SMSEL bits 2:0**

Matches the Artery SDK tmr_sub_mode_select. Read-modify-write of bits 2:0 (SMSEL) of STCTRL (offset 0x08) with param_2 & 7, which selects the slave-mode behaviour of the timer. The code-to-mode table is not in the repo register data. Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | slave mode code, 3 bits (tmr_sub_mode_select_type) |

**Notes:** Only caller: mcu_0160_08009800.

- Addresses by version: 12b: 0x0800DCFE, 143: 0x0800DF5A, 152: 0x0800DFF2, 0160: 0x0800E132
- Called by: `mcu_0160_08009800`
- Confidence: high

## tmr_trigger_input_select

**Select the slave trigger input source, STCTRL.STIS bits 6:4**

Matches the Artery SDK tmr_trigger_input_select. Read-modify-write of bits 6:4 (STIS) of STCTRL (offset 0x08) with param_2 & 7. STIS picks which internal trigger input feeds the slave controller; the mapping from code to trigger source is not in the repo register data. Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | trigger input select, 3 bits (sub_tmr_input_sel_type) |

**Notes:** Only caller: mcu_0160_08009800.

- Addresses by version: 12b: 0x0800DD08, 143: 0x0800DF64, 152: 0x0800DFFC, 0160: 0x0800E13C
- Called by: `mcu_0160_08009800`
- Confidence: high
