# BMS - `isr` functions

22 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`Default_Handler`](#default_handler) | 0x080010E6 | Default interrupt handler: spins in an endless loop |
| [`EXTI0_1_IRQHandler`](#exti0_1_irqhandler) | 0x08001368 | EXTI line 0 interrupt: latches its rising or falling edge into flag word 0x200001C8 |
| [`EXTI2_3_IRQHandler`](#exti2_3_irqhandler) | 0x080013A0 | EXTI line 2 interrupt: records a falling edge in flag word 0x200001C8 |
| [`EXTI4_15_IRQHandler`](#exti4_15_irqhandler) | 0x080013C8 | EXTI lines 5, 8, 11 and 12 interrupt: flags their edges into 0x200001C8 and clears pending |
| [`HardFault_Handler`](#hardfault_handler) | 0x080028F4 | Hard fault vector that resets the MCU via AIRCR.SYSRESETREQ instead of dumping fault state |
| [`LL_EXTI_Init`](#ll_exti_init) | 0x08002B0C | Programs EXTI line masks, edge triggers and interrupt or event mode from an init record |
| [`NVIC_SetPriority`](#nvic_setpriority) | 0x08003724 | CMSIS NVIC_SetPriority: set the 2-bit priority of an IRQ or system exception |
| [`PendSV_Handler`](#pendsv_handler) | 0x0800343C | PendSV exception handler: returns immediately, does no work |
| [`RCC_CRS_IRQHandler`](#rcc_crs_irqhandler) | 0x08003440 | RCC/CRS interrupt: on HSE ready, bring up HSE/PLL SYSCLK, enable CSS and clear the flag |
| [`RTC_TAMP_IRQHandler`](#rtc_tamp_irqhandler) | 0x08003614 | RTC/TAMP vector: passes the pointer slot at 0x20005D00 to bms_4168_08002542 |
| [`SVC_Handler`](#svc_handler) | 0x08003624 | SVCall exception handler: returns immediately, does no work |
| [`SysTick_Handler`](#systick_handler) | 0x08003662 | SysTick vector: calls bms_counter_accumulate to advance the 32-bit counter at 0x200006A0 |
| [`TIM16_FDCAN_IT0_IRQHandler`](#tim16_fdcan_it0_irqhandler) | 0x0800366C | Shared TIM16 and FDCAN IT0 vector: forward to the FDCAN handle at 0x20005C50 |
| [`TIM7_LPTIM2_IRQHandler`](#tim7_lptim2_irqhandler) | 0x0800367C | TIM7 update vector: clear the flag, advance the 0x20000678 tick, count down two timers |
| [`USART3_4_5_6_LPUART1_IRQHandler`](#usart3_4_5_6_lpuart1_irqhandler) | 0x080036D0 | USART3 vector: on RXNE clear ORE and pass the byte to bms_4168_08007c10; on IDLE clear it |
| [`__NVIC_DisableIRQ`](#__nvic_disableirq) | 0x08002278 | Disables a device interrupt by writing its bit to NVIC ICER at 0xE000E180 |
| [`__NVIC_EnableIRQ`](#__nvic_enableirq) | 0x08002298 | Enables a device interrupt by writing its bit to NVIC ISER at 0xE000E100 |
| [`__NVIC_SetPriority`](#__nvic_setpriority) | 0x080022B0 | Sets the 2-bit priority of a device interrupt (NVIC IPR) or a system exception (SHPR) |
| [`bms_exti11_irq_arm`](#bms_exti11_irq_arm) | (removed) | Route PB11 to EXTI line 11, enable its interrupt and set EXTI4_15 priority |
| [`bms_exti11_irq_disarm`](#bms_exti11_irq_disarm) | (removed) | Disarm EXTI line 11 and its NVIC line EXTI4_15 when the armed byte is set |
| [`bms_nvic_system_reset_plain`](#bms_nvic_system_reset_plain) | 0x0800A2A0 | CMSIS __NVIC_SystemReset body: request a system reset through SCB AIRCR and spin |
| [`exti_disable_lines_2_8_12`](#exti_disable_lines_2_8_12) | 0x080093F0 | Clear EXTI interrupt mask bits for lines 12, 8 and 2 |

## Default_Handler

**Default interrupt handler: spins in an endless loop**

Single infinite loop with no body. The vector table slot labelled CEC_IRQHandler points here, and unimplemented interrupts or faults that land on this default entry halt the core. The handler does not log, disable the source, or reset the MCU. Whether a watchdog recovers the hang is not visible in this function.

**Notes:** The CEC_IRQHandler label is the vector-table name for this slot; the slot is probably an unused IRQ default, not a real CEC handler.

- Addresses by version: 4130: 0x080010E6, 4139: 0x080010E6, 4148: 0x080010E6, 4168: 0x080010E6
- Vector: `CEC_IRQHandler`
- Confidence: high

## EXTI0_1_IRQHandler

**EXTI line 0 interrupt: latches its rising or falling edge into flag word 0x200001C8**

Checks pending bit 0 of EXTI RPR1 (0x4002180C) and FPR1 (0x40021810). For each pending edge it sets flag 0x4 in the 32-bit word at 0x200001C8 (address from bms_ram_200001c8_addr) and clears the pending bit by writing 1 to the EXTI register. Only line 0 is serviced here even though the vector covers lines 0 and 1, and there are no other side effects.

**Notes:** The meaning of flag 0x4 in the word at 0x200001C8 is not established in this packet.

- Addresses by version: 4130: 0x08001368, 4139: 0x08001368, 4148: 0x08001368, 4168: 0x08001368
- Vector: `EXTI0_1_IRQHandler`
- Peripheral registers: `EXTI.RPR1` (RW), `EXTI.FPR1` (RW)
- Calls: `bms_ram_200001c8_addr`
- Confidence: high

## EXTI2_3_IRQHandler

**EXTI line 2 interrupt: records a falling edge in flag word 0x200001C8**

Tests bit 2 of EXTI FPR1 (0x40021810), the falling-edge pending flag of line 2. When it is set, the function ORs 0x100002 (bits 1 and 20) into the word at 0x200001C8 and clears the pending bit by writing 4 to FPR1. Rising edges and line 3 are not handled here.

**Notes:** The meaning of bits 1 and 20 in the flag word is not established in this packet.

- Addresses by version: 4130: 0x080013A0, 4139: 0x080013A0, 4148: 0x080013A0, 4168: 0x080013A0
- Vector: `EXTI2_3_IRQHandler`
- Peripheral registers: `EXTI.FPR1` (RW)
- Calls: `bms_ram_200001c8_addr`
- Confidence: high

## EXTI4_15_IRQHandler

**EXTI lines 5, 8, 11 and 12 interrupt: flags their edges into 0x200001C8 and clears pending**

Services four EXTI lines on the EXTI4_15 vector, each checked against its pending bit and cleared by writing 1 back. The checks run in this order: line 8 falling edge (FPR1 bit 8) and line 5 rising edge (RPR1 bit 5) set 0x100002 in the word at 0x200001C8; line 12 rising edge (RPR1 bit 12) and line 12 falling edge (FPR1 bit 12) set 0x400; line 11 rising edge (RPR1 bit 11) sets 0x400.

- Addresses by version: 4130: 0x080013C8, 4139: 0x080013C8, 4148: 0x080013C8, 4168: 0x080013C8
- Vector: `EXTI4_15_IRQHandler`
- Peripheral registers: `EXTI.RPR1` (RW), `EXTI.FPR1` (RW)
- Calls: `bms_ram_200001c8_addr`
- Confidence: high

## HardFault_Handler

**Hard fault vector that resets the MCU via AIRCR.SYSRESETREQ instead of dumping fault state**

Installed in the HardFault vector, but the body is CMSIS NVIC_SystemReset and not a fault handler. It runs DSB, writes SCB AIRCR = 0x05FA0004 (VECTKEY 0x5FA with SYSRESETREQ set), runs DSB again, and then spins until the reset takes effect. Any hard fault therefore resets the chip, and CFSR and HFSR are never read here. The name is kept because it is the vector slot name.

**Notes:** The AIRCR write is a constant here, so the PRIGROUP-preserving form of NVIC_SystemReset has been simplified. The name comes from the vector table, not from the code.

- Addresses by version: 4130: 0x080028F4, 4139: 0x080028F4, 4148: 0x080028F4, 4168: 0x080028F4
- Vector: `HardFault_Handler`
- Peripheral registers: `SCB+0xc` (W)
- Confidence: high

## LL_EXTI_Init

**Programs EXTI line masks, edge triggers and interrupt or event mode from an init record**

Configures EXTI lines from an LL_EXTI_InitTypeDef-style record: word 0 is the mask for lines 0 to 31, word 1 the mask for lines 32 to 63, and byte 8 is LineCommand (0 disables). For lines 0 to 31, byte 9 selects Mode (0 = interrupt: IMR1 set and EMR1 clear, 1 = event: IMR1 clear and EMR1 set, 2 = both) and byte 10 selects Trigger (1 = rising: RTSR1 set and FTSR1 clear, 2 = falling, 3 = both, 0 = none). Lines 32 to 63 get only the IMR2 and EMR2 bits for their mode, with no edge registers. With LineCommand 0 it clears the lines in IMR1, EMR1, IMR2 and EMR2 and leaves the edge registers alone.

| Parameter | Type | Description |
|---|---|---|
| `init` | `ptr` | EXTI init record: line masks at +0 and +4, LineCommand at +8, Mode at +9, Trigger at +10 |

**Returns** `u32`: error bitmask: 1 = invalid Mode for lines 0-31, 2 = invalid Trigger, 4 = invalid Mode for lines 32-63; 0 = OK

**Notes:** Trigger edges are not programmed for lines 32 to 63 (RTSR2 and FTSR2 are never written), so a line in that range cannot have its edge set through this function.

- Addresses by version: 4130: 0x08002B0C, 4139: 0x08002B0C, 4148: 0x08002B0C, 4168: 0x08002B0C
- Peripheral registers: `EXTI.RTSR1` (RW), `EXTI.FTSR1` (RW), `EXTI.IMR1` (RW), `EXTI.EMR1` (RW), `EXTI.IMR2` (RW), `EXTI.EMR2` (RW)
- Called by: `bms_gpio_exti_init`
- Confidence: high

## NVIC_SetPriority

**CMSIS NVIC_SetPriority: set the 2-bit priority of an IRQ or system exception**

CMSIS-style NVIC_SetPriority for the Cortex-M0+. The priority in param_2 is masked to 2 bits and placed in bits 7:6 of its byte lane (STM32G0 implements __NVIC_PRIO_BITS = 2). For a negative IRQn, meaning a system exception (SVCall -5, PendSV -2, SysTick -1), the byte is written into the SCB SHPR2/SHPR3 word at 0xE000ED1C through a read-modify-write that keeps the other three byte lanes. For IRQn >= 0 the byte goes into the NVIC IPR array at 0xE000E400 with the same read-modify-write. Caller bms_4168_0800a3e8 sets interrupt priorities.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | IRQn: negative for system exceptions, otherwise device IRQ number |
| `param_2` | `u32` | priority; only bits 1:0 are used |

- Addresses by version: 4130: 0x08003724, 4139: 0x08003724, 4148: 0x08003724, 4168: 0x08003724
- Peripheral registers: `NVIC+0x300` (A), `SCB+0x1c` (A)
- Called by: `bms_tim6_tim7_start`
- Confidence: high

## PendSV_Handler

**PendSV exception handler: returns immediately, does no work**

Vector-table entry for the PendSV system exception (exception number -2). The body is a bare return, so this build does no deferred work and no context switch in PendSV. Its priority, when configured, is written by NVIC_SetPriority into the SCB SHPR3 byte.

- Addresses by version: 4130: 0x0800343C, 4139: 0x0800343C, 4148: 0x0800343C, 4168: 0x0800343C
- Vector: `PendSV_Handler`
- Confidence: high

## RCC_CRS_IRQHandler

**RCC/CRS interrupt: on HSE ready, bring up HSE/PLL SYSCLK, enable CSS and clear the flag**

Vector for the RCC and CRS interrupt. It reads the clock interrupt flag register CIFR (0x4002101C) and acts only when HSERDYF (bit 4) is set. In that case it calls bms_sysclk_hse_pll_bringup (bms_4168_0800a130), calls HAL_RCC_EnableCSS (bms_4168_08002334), clears HSERDYIE in CIER (0x40021018 bit 4) so the interrupt does not refire, writes bit 4 to CICR (0x40021020) to clear the flag, and clears bit 31 of the word at the RAM object returned by bms_ram_200001c8_addr. The other CIFR flags, including CSSF and LSECSSF, are not handled here.

**Notes:** Bit 31 of the word at 0x200001C8 is presumably a wait-for-HSE pending flag that other code polls; its meaning is inferred from the clear only. The register bit names come from the register JSON (CIFR bit 4 = HSERDYF).

- Addresses by version: 4130: 0x08003440, 4139: 0x08003440, 4148: 0x08003440, 4168: 0x08003440
- Vector: `RCC_CRS_IRQHandler`
- Peripheral registers: `RCC.CIER` (RW), `RCC.CIFR` (R), `RCC.CICR` (W)
- Calls: `HAL_RCC_EnableCSS`, `bms_sysclk_hse_pll_bringup`, `bms_ram_200001c8_addr`
- Confidence: high

## RTC_TAMP_IRQHandler

**RTC/TAMP vector: passes the pointer slot at 0x20005D00 to bms_4168_08002542**

Vector handler for the RTC and tamper interrupt. It has no logic of its own: it passes the address of the RAM slot at 0x20005D00 to bms_4168_08002542 (not yet described) and returns. The same slot holds a pointer that bms_nibble_debounce_1s dereferences, so the interrupt most likely services the object that slot points to.

**Notes:** Vector name from the STM32G0 IRQ table; the handler is entered only through the vector.

- Addresses by version: 4130: 0x08003614, 4139: 0x08003614, 4148: 0x08003614, 4168: 0x08003614
- Vector: `RTC_TAMP_IRQHandler`
- Calls: `HAL_RTCEx_WakeUpTimerIRQHandler`
- Confidence: high

## SVC_Handler

**SVCall exception handler: returns immediately, does no work**

Vector-table entry for the SVCall system exception (exception number -5). The body is a bare return, so supervisor calls perform no work in this build. Its priority, when configured, is written by NVIC_SetPriority into the SCB SHPR2 byte (bits 31:30 of the word).

- Addresses by version: 4130: 0x08003624, 4139: 0x08003624, 4148: 0x08003624, 4168: 0x08003624
- Vector: `SVC_Handler`
- Confidence: high

## SysTick_Handler

**SysTick vector: calls bms_counter_accumulate to advance the 32-bit counter at 0x200006A0**

Core SysTick exception handler. It calls bms_counter_accumulate (bms_4168_080021b4), which adds the step word at 0x20000698 into the 32-bit counter at 0x200006A0. That counter is the one bms_get_ram_word_200006a0 returns, and bms_rtc_wait_synchro uses it for its 1000-tick timeout. It is a separate time base from the TIM7-driven tick at 0x20000678.

- Addresses by version: 4130: 0x08003662, 4139: 0x08003662, 4148: 0x08003662, 4168: 0x08003662
- Vector: `SysTick_Handler`
- Calls: `bms_counter_accumulate`
- Confidence: high

## TIM16_FDCAN_IT0_IRQHandler

**Shared TIM16 and FDCAN IT0 vector: forward to the FDCAN handle at 0x20005C50**

Vector for the interrupt line shared by TIM16 and FDCAN interrupt 0. It does not test any TIM16 flag. It passes the address of the RAM object at 0x20005C50 to bms_4168_0800185a (not yet described; the FDCAN interrupt dispatcher by its role) and returns, so all FDCAN interrupt work happens in that callee.

**Notes:** Whether 0x20005C50 is the same FDCAN handle that bms_fdcan_handle_init configures is not verified. If TIM16 is ever enabled in this build, its update flag would be ignored here.

- Addresses by version: 4130: 0x0800366C, 4139: 0x0800366C, 4148: 0x0800366C, 4168: 0x0800366C
- Vector: `TIM16_FDCAN_IT0_IRQHandler`
- Calls: `HAL_FDCAN_IRQHandler`
- Confidence: high

## TIM7_LPTIM2_IRQHandler

**TIM7 update vector: clear the flag, advance the 0x20000678 tick, count down two timers**

Runs on each TIM7 update. It tests a status word with bms_request_is_done, passing &TIM7, and if it is set clears it with bms_request_reset (writes 0xFFFFFFFE at offset 0x10). It then increments the 32-bit tick at 0x20000678, which bms_tick_get returns, and decrements the 16-bit countdowns at 0x2000067C and 0x2000067E toward zero. The 0x2000067E countdown is the one bms_timeout_arm_from_record loads, so those timeouts run at the TIM7 update rate.

**Notes:** The wave-1 summaries describe bms_request_is_done and bms_request_reset as request-block helpers, but this call passes &TIM7 and offset 0x10 is TIM7.SR in the timer layout, so the test is most likely SR bit 0 (UIF). Re-check those two helpers against that reading. The width of 0x2000067C is not shown here.

- Addresses by version: 4130: 0x0800367C, 4139: 0x0800367C, 4148: 0x0800367C, 4168: 0x0800367C
- Vector: `TIM7_LPTIM2_IRQHandler`
- Peripheral registers: `TIM7.CR1` (A)
- Calls: `bms_request_reset`, `bms_request_is_done`
- Confidence: medium

## USART3_4_5_6_LPUART1_IRQHandler

**USART3 vector: on RXNE clear ORE and pass the byte to bms_4168_08007c10; on IDLE clear it**

Reads USART3.ISR. If RXNE (bit 5) is set it writes 8 to USART3.ICR, reads one byte from USART3.RDR and passes it to bms_4168_08007c10 (not yet described). The ICR write happens on every RXNE, not only after an overrun. Otherwise, if IDLE (bit 4) is set, it writes 0x10 to ICR to clear IDLE and returns. The handler only moves bytes and clears the two flags; frame assembly must be in bms_4168_08007c10.

**Notes:** ICR bit meanings (ORECF = bit 3, IDLECF = bit 4) follow the ST layout.

- Addresses by version: 4130: 0x080036D0, 4139: 0x080036D0, 4148: 0x080036D0, 4168: 0x080036D0
- Vector: `USART3_4_5_6_LPUART1_IRQHandler`
- Peripheral registers: `USART3.CR1_FIFO_ENABLED` (A), `USART3.ISR_FIFO_ENABLED` (R), `USART3.ICR` (W), `USART3.RDR` (R)
- Calls: `bms_frame_parse_legacy_4168`
- Confidence: high

## __NVIC_DisableIRQ

**Disables a device interrupt by writing its bit to NVIC ICER at 0xE000E180**

CMSIS inline NVIC_DisableIRQ for the Cortex-M0+ core. For IRQn >= 0 it writes 1 << (IRQn & 0x1f) to NVIC ICER[0] (0xE000E180), which clears that interrupt's enable bit, then runs DSB and ISB so the disable has taken effect before returning. Negative IRQn values (core exceptions) are ignored. Only ICER[0] is used, which covers IRQ 0 to 31 as on the STM32G0B1.

| Parameter | Type | Description |
|---|---|---|
| `IRQn` | `s32` | device interrupt number; negative values are ignored |

- Addresses by version: 4130: 0x08002278, 4139: 0x08002278, 4148: 0x08002278, 4168: 0x08002278
- Peripheral registers: `NVIC+0x80` (W)
- Called by: `HAL_FDCAN_MspDeInit`
- Confidence: high

## __NVIC_EnableIRQ

**Enables a device interrupt by writing its bit to NVIC ISER at 0xE000E100**

CMSIS inline NVIC_EnableIRQ for the Cortex-M0+ core. For IRQn >= 0 it writes 1 << (IRQn & 0x1f) to NVIC ISER[0] (the NVIC base 0xE000E100), which sets that interrupt's enable bit. Negative IRQn values are ignored. No barrier is issued, and only the first ISER word is used, which covers IRQ 0 to 31.

| Parameter | Type | Description |
|---|---|---|
| `IRQn` | `s32` | device interrupt number; negative values are ignored |

- Addresses by version: 4130: 0x08002298, 4139: 0x08002298, 4148: 0x08002298, 4168: 0x08002298
- Peripheral registers: `NVIC+0x0` (W)
- Called by: `HAL_FDCAN_MspInit`, `bms_ucpd_clock_irq_setup`, `bms_rtc_wakeup_period_set`
- Confidence: high

## __NVIC_SetPriority

**Sets the 2-bit priority of a device interrupt (NVIC IPR) or a system exception (SHPR)**

CMSIS inline NVIC_SetPriority with __NVIC_PRIO_BITS = 2, so the priority is shifted to the top of the byte (priority << 6); only the low 2 bits of the argument are used and 0 is the highest priority. For IRQn >= 0 it does a read-modify-write of one byte in NVIC IPR (0xE000E400 plus IRQn with the low 2 bits dropped). For negative IRQn it does the same on one byte of SCB SHPR1/2/3 (0xE000ED18 to 0xE000ED20), selecting the register from (IRQn & 0xf) - 8. Other bytes in the word are preserved.

| Parameter | Type | Description |
|---|---|---|
| `IRQn` | `s32` | device interrupt number, or negative system exception number |
| `priority` | `u32` | priority value; only bits 1:0 are used, 0 is highest |

- Addresses by version: 4130: 0x080022B0, 4139: 0x080022B0, 4148: 0x080022B0, 4168: 0x080022B0
- Peripheral registers: `NVIC+0x300` (A), `SCB+0x1c` (A)
- Called by: `HAL_FDCAN_MspInit`, `bms_systick_1khz_start`, `bms_ucpd_clock_irq_setup`, `bms_rtc_wakeup_period_set`
- Confidence: high

## bms_exti11_irq_arm

**Route PB11 to EXTI line 11, enable its interrupt and set EXTI4_15 priority**

Arms the PB11 wake or input interrupt. It sets the EXTI11 source field in EXTI.EXTICR3 (bits 26:24 = 001, port B) by read-modify-write, then calls LL_EXTI_Init with line mask 0x800 and the trailing word 0x00010001, whose mode and edge bits are not decoded here. It writes 0x800 to the EXTI register at 0x40021810, clears MODER11 and PUPDR11 on GPIOB to leave PB11 as an unpulled input, and writes 0x80 into bits 31:24 of NVIC IPR register 0xE000E404, giving IRQ 7 (EXTI4_15 on STM32G0) priority 2. It then sets bit 7 in NVIC ISER to enable IRQ 7 and stores 1 in the RAM flag at 0x20000594. The counterpart is bms_exti11_irq_disarm.

**Notes:** The packet lists the register at 0x40021810 as both EXTI.SWIER1 and EXTI.FPR1, so whether the write triggers or clears line 11 is unresolved. The IRQ 7 mapping is from the STM32G0 vector table, not from the packet's irq list.

- Addresses by version: 4130: 0x080096A4, 4139: 0x08009BDC
- Peripheral registers: `EXTI.SWIER1` (A), `EXTI.FPR1` (W), `EXTI.EXTICR3` (RW), `NVIC+0x0` (W), `NVIC+0x304` (RW)
- Called by: `bms_pb11_trigger_sequence_step`
- Calls: `LL_EXTI_Init`
- Confidence: medium

## bms_exti11_irq_disarm

**Disarm EXTI line 11 and its NVIC line EXTI4_15 when the armed byte is set**

If the armed byte at 0x20000594 is nonzero, it clears the byte, clears EXTI.IMR1 bit 11 (at 0x40021880, the CPU interrupt mask for line 11), and writes 0x80 to NVIC_ICER0 (0xE000E180), which disables NVIC IRQ 7 (EXTI4_15 on STM32G0). It finishes with DSB and ISB barriers so the disable is in effect before return. If the byte is zero, the function does nothing.

**Notes:** Present in the 4130 and 4139 builds only. The NVIC disable stops every EXTI4_15 interrupt, not only line 11, so other lines in that group are affected too. The write that sets the armed byte is elsewhere. Callers: bms_4139_08007238 and bms_4139_0800e4f8.

- Addresses by version: 4130: 0x08009670, 4139: 0x08009BA8
- Peripheral registers: `EXTI.IMR1` (RW), `NVIC+0x80` (W)
- Called by: `bms_pb11_trigger_sequence_step`, `bms_4139_0800e4f8`
- Confidence: high

## bms_nvic_system_reset_plain

**CMSIS __NVIC_SystemReset body: request a system reset through SCB AIRCR and spin**

Runs a DSB, writes 0x05FA0004 to SCB->AIRCR (VECTKEY 0x05FA in the high half and SYSRESETREQ in bit 2), runs another DSB, then loops forever while the reset takes effect. This is the standard CMSIS __NVIC_SystemReset body without any interrupt disable. It never returns.

**Notes:** Same routine as NVIC_SystemReset at bms_4168_08001444 (wave1_batch01), which additionally executes CPSID i first. The library name is already taken there, so this entry uses a unique name. Callers: bms_4168_08003c3c and bms_4168_080082f0.

- Addresses by version: 4130: 0x08009240, 4139: 0x08009740, 4148: 0x08009F8C, 4168: 0x0800A2A0
- Peripheral registers: `SCB+0xc` (W)
- Called by: `bms_4168_08003c3c`, `bms_4168_080082f0`
- Confidence: high

## exti_disable_lines_2_8_12

**Clear EXTI interrupt mask bits for lines 12, 8 and 2**

Clears bits 12, 8 and 2 of EXTI.IMR1 (0x40021880, base 0x40021800 plus offset 0x80), disabling the interrupt for EXTI lines 12, 8 and 2. Each bit is cleared with a separate read-modify-write, so the other mask bits are kept but each step is not atomic. This is equivalent to three LL_EXTI_DisableIT calls. Caller bms_4168_080082f0 uses it to mask the external interrupts before reconfiguring them.

**Notes:** The mask-register offset and bit numbers are certain from the code; the reason for masking is inferred from the single caller.

- Addresses by version: 4130: 0x08008390, 4139: 0x08008890, 4148: 0x080090DC, 4168: 0x080093F0
- Peripheral registers: `EXTI.IMR1` (ARW)
- Called by: `bms_4168_080082f0`
- Confidence: high
