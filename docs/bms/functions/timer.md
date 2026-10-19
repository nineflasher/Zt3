# BMS - `timer` functions

21 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`LL_TIM_DeInit`](#ll_tim_deinit) | 0x08002E8C | Pulses the RCC reset line of a timer instance (TIM1 to TIM17); returns 1 for other pointers |
| [`LL_TIM_DisableCounter`](#ll_tim_disablecounter) | 0x08002FA4 | Clears TIMx CR1.CEN to stop the timer counter |
| [`LL_TIM_DisableMasterSlaveMode`](#ll_tim_disablemasterslavemode) | 0x08002FAE | Clears SMCR.MSM (bit 7) to turn off master/slave synchronisation |
| [`LL_TIM_EnableARRPreload`](#ll_tim_enablearrpreload) | 0x08002FB8 | Sets CR1.ARPE (bit 7) so auto-reload writes are buffered until the next update |
| [`LL_TIM_EnableCounter`](#ll_tim_enablecounter) | 0x08002FC2 | Sets CR1.CEN (bit 0) to start the timer counter |
| [`LL_TIM_Init`](#ll_tim_init) | 0x08002FCC | Writes prescaler, counter mode, auto-reload, clock division and repetition counter to a timer |
| [`LL_TIM_SetTriggerOutput`](#ll_tim_settriggeroutput) | 0x08003080 | Writes CR2.MMS (bits 4 to 6), the master trigger output selection, of a timer |
| [`SysTick_Config`](#systick_config) | 0x080028B8 | Starts SysTick with the given reload count at lowest priority and enables its interrupt |
| [`bms_counter_1000_tick`](#bms_counter_1000_tick) | 0x0800868C | Count 1000-tick periods into the signed 16-bit counter that 0x2000002C points to |
| [`bms_pb11_hold_timer_step`](#bms_pb11_hold_timer_step) | (removed) | Accumulate time while GPIOB pin 11 is high; latch output past 2000 units, clear when low |
| [`bms_systick_base_set`](#bms_systick_base_set) | 0x08008D4C | Store the SysTick base count used by the busy-wait helpers |
| [`bms_systick_wait_repeat`](#bms_systick_wait_repeat) | 0x08008D58 | Busy-wait param_1 times, each for DAT_20000688 * 1000 SysTick counts |
| [`bms_systick_wait_scaled`](#bms_systick_wait_scaled) | 0x08008DA0 | Busy-wait for param_1 * DAT_20000688 SysTick counts |
| [`bms_tick_get`](#bms_tick_get) | 0x0800A348 | Return the 32-bit time base word at 0x20000678 |
| [`bms_tick_timeout_check`](#bms_tick_timeout_check) | 0x0800A528 | True when (time base - start stamp) reaches the threshold; stores the elapsed value on expiry |
| [`bms_tim6_tim7_start`](#bms_tim6_tim7_start) | 0x0800A3E8 | Configure TIM6 as a polled 10 Hz timer and TIM7 as a 1 kHz update interrupt |
| [`bms_tim6_tim7_stop`](#bms_tim6_tim7_stop) | 0x0800A4B4 | Stop TIM6 and TIM7, reset both timers and disable IRQ 18 |
| [`bms_tim6_tim7_stop_reset`](#bms_tim6_tim7_stop_reset) | (removed) | Stop and reset TIM6 and TIM7: counter disable, then peripheral reset |
| [`bms_tim6_update_flag_poll`](#bms_tim6_update_flag_poll) | 0x0800A3C8 | Return true if TIM6 has an update flag pending, and clear it |
| [`bms_timeout_arm_from_record`](#bms_timeout_arm_from_record) | 0x08005710 | Arm the 0x2000067E countdown from the record at 0x2000133C; set state 0x20001340 from bit 12 |
| [`bms_timer10_poll`](#bms_timer10_poll) | 0x08008254 | Poll a 10-tick periodic timer and arm it when the request byte at 0x20000020 is set |

## LL_TIM_DeInit

**Pulses the RCC reset line of a timer instance (TIM1 to TIM17); returns 1 for other pointers**

Resets one timer by writing a force-reset and then a release-reset to its bit in RCC APBRSTR2 (0x40021030: TIM1 bit 11, TIM14 bit 15, TIM15 bit 16, TIM16 bit 17, TIM17 bit 18) or in RCC APBRSTR1 (0x4002102C: TIM2 bit 0, TIM3 bit 1, TIM4 bit 2, TIM6 bit 4, TIM7 bit 5). It returns 0 (SUCCESS) for a known timer. For any other pointer it returns 1 without touching any register.

| Parameter | Type | Description |
|---|---|---|
| `TIMx` | `ptr` | timer instance (TIM_TypeDef pointer) |

**Returns** `u32`: ErrorStatus: 0 = SUCCESS, 1 = unknown instance

- Addresses by version: 4130: 0x08002E8C, 4139: 0x08002E8C, 4148: 0x08002E8C, 4168: 0x08002E8C
- Peripheral registers: `RCC.APBRSTR1` (RW), `RCC.APBRSTR2` (RW)
- Called by: `bms_tim6_tim7_stop`
- Confidence: high

## LL_TIM_DisableCounter

**Clears TIMx CR1.CEN to stop the timer counter**

Clears CR1 bit 0 (CEN) by read-modify-write and keeps the other CR1 bits, which halts the counter at its current value. It has no other side effects.

| Parameter | Type | Description |
|---|---|---|
| `TIMx` | `ptr` | timer instance; word 0 is CR1 |

- Addresses by version: 4130: 0x08002FA4, 4139: 0x08002FA4, 4148: 0x08002FA4, 4168: 0x08002FA4
- Called by: `bms_tim6_tim7_stop`
- Confidence: high

## LL_TIM_DisableMasterSlaveMode

**Clears SMCR.MSM (bit 7) to turn off master/slave synchronisation**

Clears bit 7 of the word at offset 8 of the timer block (SMCR, master/slave mode MSM) by read-modify-write, which stops the timer from synchronising its trigger output to slave timers. Other SMCR bits are unchanged. It is called only from bms_4168_0800a3e8.

| Parameter | Type | Description |
|---|---|---|
| `TIMx` | `ptr` | timer instance |

- Addresses by version: 4130: 0x08002FAE, 4139: 0x08002FAE, 4148: 0x08002FAE, 4168: 0x08002FAE
- Called by: `bms_tim6_tim7_start`
- Confidence: high

## LL_TIM_EnableARRPreload

**Sets CR1.ARPE (bit 7) so auto-reload writes are buffered until the next update**

ORs 0x80 into CR1 (offset 0), setting ARPE (auto-reload preload enable). With ARPE set, writes to ARR take effect only at the next update event rather than immediately. It is called from bms_4168_0800a3e8.

| Parameter | Type | Description |
|---|---|---|
| `TIMx` | `ptr` | timer instance; word 0 is CR1 |

- Addresses by version: 4130: 0x08002FB8, 4139: 0x08002FB8, 4148: 0x08002FB8, 4168: 0x08002FB8
- Called by: `bms_tim6_tim7_start`
- Confidence: high

## LL_TIM_EnableCounter

**Sets CR1.CEN (bit 0) to start the timer counter**

ORs 1 into CR1 (CEN), which starts the counter from its current CNT value. Other CR1 bits are unchanged. It is called from bms_4168_0800a3e8 as part of timer start-up.

| Parameter | Type | Description |
|---|---|---|
| `TIMx` | `ptr` | timer instance; word 0 is CR1 |

- Addresses by version: 4130: 0x08002FC2, 4139: 0x08002FC2, 4148: 0x08002FC2, 4168: 0x08002FC2
- Called by: `bms_tim6_tim7_start`
- Confidence: high

## LL_TIM_Init

**Writes prescaler, counter mode, auto-reload, clock division and repetition counter to a timer**

Applies an LL_TIM_InitTypeDef-style record to a timer, as ST's LL_TIM_Init does. PSC gets the 16-bit prescaler at offset 0. CR1 DIR and CMS (bits 4 to 6) take the counter mode at offset 4, for TIM1 to TIM4 only. CR1 CKD (bits 8 and 9) takes the clock division at offset 12, for TIM1 to TIM4 and TIM14 to TIM17. ARR takes the auto-reload value at offset 8, and RCR takes the repetition counter at offset 16 for the advanced timers TIM1 and TIM15 to TIM17 only. Finally it sets EGR.UG so that the new PSC and ARR load at once. It always returns 0.

| Parameter | Type | Description |
|---|---|---|
| `TIMx` | `ptr` | timer instance |
| `init` | `ptr` | LL_TIM_InitTypeDef-style record: Prescaler (u16 at 0), CounterMode (4), Autoreload (8), ClockDivision (12), RepetitionCounter (16) |

**Returns** `u32`: ErrorStatus, always 0 (SUCCESS)

- Addresses by version: 4130: 0x08002FCC, 4139: 0x08002FCC, 4148: 0x08002FCC, 4168: 0x08002FCC
- Called by: `bms_tim6_tim7_start`
- Confidence: high

## LL_TIM_SetTriggerOutput

**Writes CR2.MMS (bits 4 to 6), the master trigger output selection, of a timer**

Replaces CR2 (offset 4) bits 4 to 6 (MMS, master mode selection, which chooses the event that drives TRGO) with the argument, leaving other CR2 bits unchanged. The argument is ORed in without masking, so the caller must pass the MMS value already shifted into bits 4 to 6. It is called from bms_4168_0800a3e8.

| Parameter | Type | Description |
|---|---|---|
| `TIMx` | `ptr` | timer instance |
| `trigger_output` | `u32` | MMS value already in bits 4 to 6 |

- Addresses by version: 4130: 0x08003080, 4139: 0x08003080, 4148: 0x08003080, 4168: 0x08003080
- Called by: `bms_tim6_tim7_start`
- Confidence: high

## SysTick_Config

**Starts SysTick with the given reload count at lowest priority and enables its interrupt**

CMSIS SysTick_Config. It returns 1 without touching hardware when ticks - 1 exceeds the 24-bit reload limit 0xFFFFFF. Otherwise it writes SysTick LOAD = ticks - 1, sets the SysTick exception priority to 3 (lowest) by writing 0xC0 into the top byte of SCB SHPR3 (0xE000ED20) and preserving the low 24 bits (including the PendSV priority), clears SysTick VAL, and writes SysTick CTRL = 7 (CLKSOURCE = processor clock, TICKINT = 1, ENABLE = 1). It returns 0 on success.

| Parameter | Type | Description |
|---|---|---|
| `ticks` | `u32` | number of processor clock cycles per tick; 1 to 0x1000000 |

**Returns** `u32`: 0 on success, 1 if ticks is out of range

- Addresses by version: 4130: 0x080028B8, 4139: 0x080028B8, 4148: 0x080028B8, 4168: 0x080028B8
- Peripheral registers: `SysTick+0x0` (W), `SysTick+0x4` (W), `SysTick+0x8` (W), `SCB+0x20` (RW)
- Called by: `bms_4168_080021ec`
- Confidence: high

## bms_counter_1000_tick

**Count 1000-tick periods into the signed 16-bit counter that 0x2000002C points to**

When the request byte at 0x2000001E is set it is cleared and the stamp at 0x20000034 is taken from bms_tick_get. bms_tick_timeout_check then tests for 1000 time-base ticks since the stamp, and on expiry the elapsed value overwrites the stamp word and the request byte is set, so the next call re-takes the stamp. The counter at the pointer in 0x2000002C is incremented on each expiry and reset to 0 instead when the result would be -1. It is called from the main-loop poll bms_4168_08010558.

- Addresses by version: 4130: 0x08007640, 4139: 0x08007B40, 4148: 0x0800838C, 4168: 0x0800868C
- Called by: `bms_4168_08010558`
- Calls: `bms_tick_get`, `bms_tick_timeout_check`
- Confidence: medium

## bms_pb11_hold_timer_step

**Accumulate time while GPIOB pin 11 is high; latch output past 2000 units, clear when low**

Samples GPIOB pin 11 (GPIOB.IDR at 0x50000410, bit 11) on each call. While the pin is high it adds the 16-bit step param_1 to the u16 accumulator at 0x20000596. When the accumulator exceeds 2000 it resets to 0 and sets the output byte at 0x20000595 to 1, and that output stays 1 on later high samples until the pin goes low. A low pin clears the output to 0 but leaves the accumulator intact, so high time adds up across interruptions. The function returns the output byte.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s16` | time step added to the accumulator on each high sample; units not stated in this packet |

**Returns** `u8`: 0 or 1, the latched output byte at 0x20000595

**Notes:** Present in the 4130 and 4139 builds only. The pin's function and the step units are not established here. It is grouped with bms_exti11_irq_disarm, which clears the armed byte at 0x20000594, and the 0x20000594..0x20000596 block. The EXTI line that goes with PB11 is set in SYSCFG EXTICR, which is not visible in this packet.

- Addresses by version: 4130: 0x08009638, 4139: 0x08009B70
- Called by: `bms_4139_08007238`
- Confidence: medium

## bms_systick_base_set

**Store the SysTick base count used by the busy-wait helpers**

Writes param_1 to the RAM word at 0x20000688. That word is the base count multiplied by the busy-wait helpers bms_systick_wait_repeat and bms_systick_wait_scaled, which poll SysTick until the requested number of counts has elapsed. Callers bms_4168_080082f0 and bms_4168_080086d4 set it before they wait. No peripheral access.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | base SysTick count |

- Addresses by version: 4130: 0x08007D00, 4139: 0x08008200, 4148: 0x08008A4C, 4168: 0x08008D4C
- Called by: `bms_4168_080082f0`, `bms_4168_080086d4`
- Confidence: medium

## bms_systick_wait_repeat

**Busy-wait param_1 times, each for DAT_20000688 * 1000 SysTick counts**

Runs param_1 repetitions of a busy-wait. Each repetition polls SysTick->VAL (0xE000E018) until the elapsed count reaches DAT_20000688 * 1000. Elapsed counts come from successive VAL reads: the down-counter difference is added directly, and when VAL has wrapped past the reload value SysTick->LOAD (0xE000E014) the reload is added first, so the wait works across reloads. The loop has no interrupts, sleep or timeout, so it blocks the CPU for the whole duration. The 1000 factor means DAT_20000688 is in thousands of SysTick counts.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | number of repetitions; 0 does nothing |

**Notes:** Callers in the packet: bms_4168_080082bc, bms_4168_080082f0, bms_4168_0800aa5c, bms_4168_0800aae8, bms_4168_0800b314, bms_4168_0800b406, bms_4168_0800b57e. Real time per count depends on the SysTick clock source, which is not in this packet.

- Addresses by version: 4130: 0x08007D0C, 4139: 0x0800820C, 4148: 0x08008A58, 4168: 0x08008D58
- Peripheral registers: `SysTick+0x4` (R), `SysTick+0x8` (R)
- Called by: `bms_4168_080082bc`, `bms_4168_080082f0`, `bms_pc7_enable_and_settle`, `bms_4168_0800aae8`, `bms_4168_0800b314`, `bms_4168_0800b406`, `bms_4168_0800b57e`
- Confidence: high

## bms_systick_wait_scaled

**Busy-wait for param_1 * DAT_20000688 SysTick counts**

A single busy-wait with the same SysTick VAL/LOAD elapsed-count method as bms_systick_wait_repeat, but the target is DAT_20000688 * param_1 counts with no fixed factor. It is the main delay primitive for the timing-sensitive routines in this build; seven callers in the packet use it. The use is probably bit-timed serial signalling or AFE sequencing, which is a guess.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | delay multiplier in DAT_20000688 units |

**Notes:** Callers in the packet: bms_4168_08009428, bms_4168_08009664, bms_4168_08009740, bms_4168_0800982c, bms_4168_080098f0, bms_4168_0800997c, bms_4168_08009a0c. The loop compares the 32-bit target with a 32-bit accumulator, so very large multipliers wrap.

- Addresses by version: 4130: 0x08007D54, 4139: 0x08008254, 4148: 0x08008AA0, 4168: 0x08008DA0
- Peripheral registers: `SysTick+0x4` (R), `SysTick+0x8` (R)
- Called by: `bms_i2c_bb_send_bit0`, `bms_i2c_bb_send_bit1`, `bms_i2c_bb_read_byte`, `bms_i2c_bb_write_byte`, `bms_i2c_bb_start`, `bms_i2c_bb_stop`, `bms_pa12_ready_handshake`
- Confidence: medium

## bms_tick_get

**Return the 32-bit time base word at 0x20000678**

Returns the u32 at RAM 0x20000678. Many callers use it as a time stamp, and bms_tick_timeout_check compares it against stamps, so it is treated as a free-running time base. The code that increments it is not in this packet, so its unit is unknown. Read-only.

**Returns** `u32`: value of the time base at 0x20000678

**Notes:** Callers in the packet include bms_4139_0800c950, bms_4139_0800cd7c, bms_4139_0800cebc and about a dozen bms_4168 functions; the packet's caller list is truncated.

- Addresses by version: 4130: 0x080092E8, 4139: 0x080097E8, 4148: 0x0800A034, 4168: 0x0800A348
- Called by: `bms_event_capture_on_match`, `bms_proto_build_reply`, `bms_nibble_debounce_1s`, `bms_rtc_reset_with_snapshot`, `bms_seq_restart_stamp`, `bms_timer10_poll`, `bms_4168_080082f0`, `bms_counter_1000_tick`, `bms_frame_send_when_ready`, `bms_record_send_multiframe`, `bms_4168_0800d76c`, `bms_4168_0800ddb0` ...
- Confidence: medium

## bms_tick_timeout_check

**True when (time base - start stamp) reaches the threshold; stores the elapsed value on expiry**

Computes an elapsed time from the 32-bit time base at 0x20000678 and the start stamp param_1. If the time base is below the stamp, the elapsed value is computed as base - stamp - 1; otherwise it is base - stamp. If the elapsed value is at least the threshold param_2, it is written to *param_3 and the function returns true. Otherwise it returns false and leaves *param_3 unchanged. It is the common timeout test used by many callers in the packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | start stamp, a value previously read from the time base |
| `param_2` | `u32` | threshold in time-base units |
| `param_3` | `ptr` | output: receives the elapsed value when the threshold is reached |

**Returns** `bool`: true when the elapsed value is at least param_2

**Notes:** The wrap case subtracts one more than a plain unsigned subtraction. This may be a decompiler artifact of a borrow idiom or a real off-by-one; check the disassembly. Callers: bms_4139_0800cd7c, bms_4168_080064a0, bms_4168_08007f48, bms_4168_08008254, bms_4168_080082f0, bms_4168_0800868c, bms_4168_0800b9a8, bms_4168_0800b9f2, bms_4168_0800ddb0, bms_4168_0800e2c8, bms_4168_0800f8b4, bms_4168_0800fabc.

- Addresses by version: 4130: 0x08009490, 4139: 0x080099C8, 4148: 0x0800A214, 4168: 0x0800A528
- Called by: `bms_nibble_debounce_1s`, `bms_4168_08007f48`, `bms_timer10_poll`, `bms_4168_080082f0`, `bms_counter_1000_tick`, `bms_frame_send_when_ready`, `bms_record_send_multiframe`, `bms_4168_0800ddb0`, `bms_can_status_frame_rx`, `bms_4168_0800f8b4`, `bms_fault_record_service`
- Confidence: medium

## bms_tim6_tim7_start

**Configure TIM6 as a polled 10 Hz timer and TIM7 as a 1 kHz update interrupt**

Sets up two basic timers from the 16 MHz clock. It calls a fill helper (FUN_08001246, not described here) on a 20-byte init block, enables the APB1 clocks for TIM6 (0x10) and TIM7 (0x20), and programs TIM6 with PSC 1599 and ARR 999, which gives 10 Hz. TIM6 gets ARR preload, master/slave mode off, reset trigger output, and its update flag cleared before the counter starts. For TIM7 it sets NVIC priority 1 on IRQ 18 and enables that IRQ through NVIC ISER bit 18, then programs PSC 15 and ARR 999 for 1 kHz, sets DIER.UIE to request an update interrupt each millisecond, clears the flag and starts the counter.

**Notes:** The 16 MHz clock is assumed from bms_sysclk_hse_pll_bringup. IRQ 18 is TIM7_LPTIM2 in the STM32G0 vector table, and its handler is not in this packet. FUN_08001246 is not described here.

- Addresses by version: 4130: 0x08009388, 4139: 0x08009888, 4148: 0x0800A0D4, 4168: 0x0800A3E8
- Peripheral registers: `TIM6.CR1` (A), `TIM7.CR1` (A), `TIM7.DIER` (RW), `NVIC+0x0` (AW)
- Called by: `bms_4168_08008294`, `bms_4168_080082f0`
- Calls: `bms_4168_08001246`, `LL_APB1_GRP1_EnableClock`, `bms_request_reset`, `LL_TIM_DisableMasterSlaveMode`, `LL_TIM_EnableARRPreload`, `LL_TIM_EnableCounter`, `LL_TIM_Init`, `LL_TIM_SetTriggerOutput`, `NVIC_SetPriority`
- Confidence: medium

## bms_tim6_tim7_stop

**Stop TIM6 and TIM7, reset both timers and disable IRQ 18**

Undoes bms_tim6_tim7_start. For each of TIM6 and TIM7 it calls LL_TIM_DisableCounter and then LL_TIM_DeInit, which pulses the RCC reset line. It writes 0x40000 to NVIC ICER0 (0xE000E180) to disable IRQ 18, then runs a DSB and an ISB so the disable has taken effect before the function returns.

- Addresses by version: 4139: 0x08009954, 4148: 0x0800A1A0, 4168: 0x0800A4B4
- Peripheral registers: `TIM6.CR1` (A), `TIM7.CR1` (A), `NVIC+0x80` (W)
- Called by: `bms_4168_080082f0`
- Calls: `LL_TIM_DeInit`, `LL_TIM_DisableCounter`
- Confidence: high

## bms_tim6_tim7_stop_reset

**Stop and reset TIM6 and TIM7: counter disable, then peripheral reset**

Calls LL_TIM_DisableCounter and then LL_TIM_DeInit for TIM6, then for TIM7. Each call clears CR1.CEN and pulses the RCC reset line of the timer, returning both to their reset state. No direct caller is in this packet, so it is probably reached from a mode-change path or a callback table.

- Addresses by version: 4130: 0x08009454
- Peripheral registers: `TIM6.CR1` (A), `TIM7.CR1` (A)
- Called by: `bms_4168_080082f0`
- Calls: `LL_TIM_DeInit`, `LL_TIM_DisableCounter`
- Confidence: high

## bms_tim6_update_flag_poll

**Return true if TIM6 has an update flag pending, and clear it**

Checks and clears the TIM6 update flag. It calls bms_request_is_done with the TIM6 instance pointer, which returns bit 0 of the word at offset 0x10 (TIM6_SR, the UIF bit). If that bit is set it calls bms_request_reset, which writes 0xFFFFFFFE to the same word and so clears UIF. The routine returns true only when the flag was set. It is a non-blocking poll, and TIM6 is configured as a 10 Hz timer by bms_tim6_tim7_start.

**Returns** `bool`: true when UIF was set; the flag is cleared by the call

**Notes:** The helpers take the TIM instance pointer as a request block, so the status word is TIM6_SR by address offset.

- Addresses by version: 4130: 0x08009368, 4139: 0x08009868, 4148: 0x0800A0B4, 4168: 0x0800A3C8
- Peripheral registers: `TIM6.CR1` (A)
- Called by: `bms_4168_080082f0`
- Calls: `bms_request_reset`, `bms_request_is_done`
- Confidence: high

## bms_timeout_arm_from_record

**Arm the 0x2000067E countdown from the record at 0x2000133C; set state 0x20001340 from bit 12**

If the record pointer at 0x2000133C is set, it checks the byte at record +1. Value 5 selects a 10000-tick timeout and any other value a 1500-tick one. The value is written as two bytes at 0x2000062A and 0x2000062B (through bms_byte_20000628_addr) and loaded into the countdown at 0x2000067E with bms_u16_2000067e_set. The TIM7 handler, bms_4168_0800367c, decrements that countdown, so the timeout runs at the TIM7 update rate. Then it sets 0x20001340 to 2 when bit 12 of the status word at +0x196 is set, and to 1 otherwise.

**Notes:** The record type and the reason for the 5 versus other choice are not in the packet. The state values 1 and 2 are only set here.

- Addresses by version: 4130: 0x08004EAC, 4139: 0x080050C8, 4148: 0x080055C4, 4168: 0x08005710
- Calls: `bms_u16_2000067e_set`, `bms_byte_20000628_addr`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_timer10_poll

**Poll a 10-tick periodic timer and arm it when the request byte at 0x20000020 is set**

If the one-shot request byte at 0x20000020 is set, it is cleared, the start stamp at 0x2000003C is taken from bms_tick_get, the word at 0x20000028 is set to 10, and the function returns 1. Otherwise bms_tick_timeout_check tests whether 10 time-base ticks have passed since the stamp; on expiry the stamp is re-taken, the elapsed value is stored in 0x20000028, and the function returns 1, else 0. It is called from the main-loop poll bms_4168_08010558.

**Returns** `s32`: 1 when the timer was armed or expired, 0 otherwise

- Addresses by version: 4130: 0x08007208, 4139: 0x08007710, 4148: 0x08007F50, 4168: 0x08008254
- Called by: `bms_4168_08010558`
- Calls: `bms_tick_get`, `bms_tick_timeout_check`
- Confidence: medium
