# VCU - `isr` functions

28 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`BusFault_Handler`](#busfault_handler) | 0x080013FC | Bus fault exception handler: infinite loop |
| [`BusFault_Handler_v148`](#busfault_handler_v148) | (removed) | Bus fault handler in VCU_148: infinite loop |
| [`BusFault_Handler_v148_14a`](#busfault_handler_v148_14a) | (removed) | Bus fault handler in builds 148/14a: infinite loop |
| [`BusFault_Handler_v14b_14f`](#busfault_handler_v14b_14f) | (removed) | Bus fault handler in builds 14b/14e/14f: infinite loop |
| [`CAN1_RX0_IRQHandler`](#can1_rx0_irqhandler) | 0x08002904 | CAN1 RX FIFO 0 interrupt: read one frame when FIFO 0 has a message and dispatch it |
| [`CAN1_SE_IRQHandler`](#can1_se_irqhandler) | 0x08002930 | CAN1 status and error interrupt: latch bus-off, error counters and last error code |
| [`DebugMon_Handler`](#debugmon_handler) | (removed) | Debug monitor exception handler: empty, returns immediately |
| [`DebugMon_Handler_v152_159`](#debugmon_handler_v152_159) | 0x080013FE | Debug monitor exception handler: empty, returns immediately |
| [`Default_Handler`](#default_handler) | 0x080011A2 | Default trap for unused interrupt vectors: spins forever |
| [`ERTC_WKUP_IRQHandler`](#ertc_wkup_irqhandler) | 0x08005874 | ERTC wakeup interrupt: latch the wake event, clear pending bits and count wakeups |
| [`EXINT0_IRQHandler`](#exint0_irqhandler) | (removed) | EXINT line 0 interrupt handler: empty stub |
| [`EXINT0_IRQHandler_v152_159`](#exint0_irqhandler_v152_159) | 0x0800141C | External interrupt line 0 handler: empty stub |
| [`EXINT15_10_IRQHandler`](#exint15_10_irqhandler) | 0x080058AC | EXINT lines 12 and 14: record an input event code and latch DAT_20001fb8 |
| [`EXINT3_IRQHandler`](#exint3_irqhandler) | 0x080058F0 | EXINT line 3 handler: set event code 5 and clear the pending bit |
| [`EXINT9_5_IRQHandler`](#exint9_5_irqhandler) | (removed) | EXINT lines 9..5 shared interrupt handler: empty stub |
| [`EXINT9_5_IRQHandler_v152_159`](#exint9_5_irqhandler_v152_159) | 0x0800141E | External interrupt lines 5..9 handler: empty stub |
| [`HardFault_Handler`](#hardfault_handler) | 0x08005D9A | HardFault exception handler: infinite loop |
| [`MemManage_Handler`](#memmanage_handler) | 0x08006990 | MemManage fault handler: infinite loop |
| [`NMI_Handler`](#nmi_handler) | 0x080069B0 | NMI exception handler: empty, returns immediately |
| [`PendSV_Handler`](#pendsv_handler) | 0x08007AB4 | PendSV exception handler: empty, returns immediately |
| [`SVC_Handler`](#svc_handler) | 0x08007D84 | SVC exception handler: empty (immediate return) |
| [`SysTick_Handler`](#systick_handler) | 0x08008912 | SysTick exception handler: empty (immediate return) |
| [`TMR2_GLOBAL_IRQHandler`](#tmr2_global_irqhandler) | 0x08008988 | TMR2 global interrupt handler: empty (immediate return) |
| [`TMR5_GLOBAL_IRQHandler`](#tmr5_global_irqhandler) | 0x0800898C | TMR5 global interrupt: count overflow events in DAT_20001350 and clear the flag |
| [`USART2_IRQHandler`](#usart2_irqhandler) | 0x08008C98 | USART2 receive interrupt: store the received byte in a 250-byte ring at 0x200019ba |
| [`UsageFault_Handler`](#usagefault_handler) | 0x08009DA4 | UsageFault handler: spin forever |
| [`nvic_irq_enable`](#nvic_irq_enable) | 0x0800DE48 | Set an interrupt's priority from the group setting and enable it in NVIC |
| [`nvic_priority_group_config`](#nvic_priority_group_config) | 0x0800DEC0 | Set the NVIC priority grouping (AIRCR.PRIGROUP) with the VECTKEY write |

## BusFault_Handler

**Bus fault exception handler: infinite loop**

Single b . instruction. A bus fault (bad peripheral/memory access) halts the CPU here until the watchdog or a debugger intervenes. Present in builds 152, 153 and 159, where the fault handlers are separate stubs from the default handler.

- Addresses by version: 152: 0x080013FC, 153: 0x080013FC, 0159: 0x080013FC
- Vector: `BusFault_Handler`
- Confidence: high

## BusFault_Handler_v148

**Bus fault handler in VCU_148: infinite loop**

Single b . trap at 0x0800252e of the VCU_148 image, referenced by the vector table as BusFault_Handler (in this build it is a separate loop stub from the one at 0x0800141e). Hangs the CPU on any bus fault. Behaviourally identical to the BusFault handlers of other builds.

- Addresses by version: 148: 0x0800252E
- Vector: `BusFault_Handler`
- Confidence: high

## BusFault_Handler_v148_14a

**Bus fault handler in builds 148/14a: infinite loop**

Single b . trap used as the BusFault vector in the VCU_148 and VCU_14a images. It is a different physical function (different family) from the BusFault_Handler of builds 152+, which moved because the code layout shifted; behaviour is identical. Halts the CPU on a bus fault.

- Addresses by version: 148: 0x0800141C, 14a: 0x0800141E
- Vector: `BusFault_Handler`
- Confidence: high

## BusFault_Handler_v14b_14f

**Bus fault handler in builds 14b/14e/14f: infinite loop**

Single b . trap at 0x080028be used as BusFault vector in VCU_14b, VCU_14e and VCU_14f. Hangs the CPU on a bus fault; identical in behaviour to the other BusFault_Handler variants, only its address and therefore family differ.

- Addresses by version: 14b: 0x08002862, 14e: 0x08002862, 14f: 0x080028BE
- Vector: `BusFault_Handler`
- Confidence: high

## CAN1_RX0_IRQHandler

**CAN1 RX FIFO 0 interrupt: read one frame when FIFO 0 has a message and dispatch it**

Interrupt handler for CAN1_RX0 (IRQ 20). If the FIFO 0 message-count flag is set (can_flag_get code 9, RF0MN), it reads one frame from FIFO 0 with can_message_receive into a 20-byte stack buffer and calls vcu_0159_08007bb0 with that buffer, which is the CAN frame dispatch routine and is not described yet. Only one frame is taken per interrupt, and a frame still pending raises the interrupt again.

- Addresses by version: 148: 0x08002530, 14a: 0x080025AC, 14b: 0x08002864, 14e: 0x08002864, 14f: 0x080028C0, 152: 0x080028FC, 153: 0x08002918, 0159: 0x08002904
- Vector: `CAN1_RX0_IRQHandler`
- Peripheral registers: `CAN1.MCTRL` (A)
- Calls: `vcu_rx_ring0_push_record`, `can_flag_get`, `can_message_receive`
- Confidence: high

## CAN1_SE_IRQHandler

**CAN1 status and error interrupt: latch bus-off, error counters and last error code**

Interrupt handler for CAN1_SE (IRQ 22). It reads CAN1.ESTS (0x40006418). If the bus-off flag (ESTS bit 2) is set it writes 1 to DAT_2000185B. If the error type record is nonzero (can_flag_get code 4, ESTS bits 6:4), it stores the transmit error counter (bits 23:16) in DAT_2000186F, the receive error counter (bits 31:24) in DAT_20001870, and the last error code (bits 6:4) in DAT_20001858. It then clears status flags 3 and 4 with can_flag_clear. Nothing else in this handler reads those RAM bytes.

**Notes:** The ESTS field layout was checked against the at32f415 register table: REC 31:24, TEC 23:16, ETR 6:4, BOF bit 2.

- Addresses by version: 148: 0x0800255C, 14a: 0x080025D8, 14b: 0x08002890, 14e: 0x08002890, 14f: 0x080028EC, 152: 0x08002928, 153: 0x08002944, 0159: 0x08002930
- Vector: `CAN1_SE_IRQHandler`
- Peripheral registers: `CAN1.MCTRL` (A), `CAN1.ESTS` (R)
- Calls: `can_flag_clear`, `can_flag_get`
- Confidence: high

## DebugMon_Handler

**Debug monitor exception handler: empty, returns immediately**

Cortex-M DebugMonitor exception vector (vector 12). The handler is a single return instruction, so debug monitor events are ignored. Present only in the older builds 148..14f.

- Addresses by version: 148: 0x08004E84, 14a: 0x08005214, 14b: 0x0800553C, 14e: 0x08005574, 14f: 0x080055D0
- Vector: `DebugMon_Handler`
- Confidence: high

## DebugMon_Handler_v152_159

**Debug monitor exception handler: empty, returns immediately**

Single bx lr. The debug monitor exception is not used by the application so the handler does nothing.

- Addresses by version: 152: 0x080013FE, 153: 0x080013FE, 0159: 0x080013FE
- Vector: `DebugMon_Handler`
- Confidence: high

## Default_Handler

**Default trap for unused interrupt vectors: spins forever**

Single instruction infinite loop (b .). The vector table points every unused exception and IRQ slot here; the harness labels it DMA2_Channel6_7_IRQHandler only because that is one of the slots referencing it. If an unexpected interrupt fires the MCU hangs until the watchdog (if enabled) resets it. Same role as the identical loop stubs in the older builds (the BusFault_Handler variants).

- Addresses by version: 148: 0x080011A2, 14a: 0x080011A2, 14b: 0x080011A2, 14e: 0x080011A2, 14f: 0x080011A2, 152: 0x080011A2, 153: 0x080011A2, 0159: 0x080011A2
- Vector: `DMA2_Channel6_7_IRQHandler`
- Confidence: high

## ERTC_WKUP_IRQHandler

**ERTC wakeup interrupt: latch the wake event, clear pending bits and count wakeups**

If ertc_flag_get(0x400) reports the ERTC wakeup flag, it sets the event latch DAT_20001fea to 1, clears the flag with ertc_flag_clear(0x400), clears the EXINT line 22 pending bit with exint_flag_clear(0x400000) and increments the wakeup counter DAT_20001018 (byte). When the flag is clear it does nothing.

- Addresses by version: 148: 0x08004EF0, 14a: 0x080052E0, 14b: 0x08005608, 14e: 0x08005640, 14f: 0x0800569C, 152: 0x080056F8, 153: 0x08005710, 0159: 0x08005874
- Vector: `ERTC_WKUP_IRQHandler`
- Calls: `ertc_flag_clear`, `ertc_flag_get`, `exint_flag_clear`
- Confidence: high

## EXINT0_IRQHandler

**EXINT line 0 interrupt handler: empty stub**

Vector for external interrupt line 0 (EXINT0). The body is a single return and does not clear the EXINT pending bit, so the interrupt is evidently not enabled in practice. Present only in builds 148..14f.

- Addresses by version: 148: 0x08004F28, 14a: 0x08005318, 14b: 0x08005640, 14e: 0x08005678, 14f: 0x080056D4
- Vector: `EXINT0_IRQHandler`
- Confidence: high

## EXINT0_IRQHandler_v152_159

**External interrupt line 0 handler: empty stub**

Single bx lr. The interrupt is not serviced by the 152/153/159 builds, so the handler only returns. Pending flag in EXINT is not cleared, so if the line were enabled it would re-trigger; it is evidently left masked.

- Addresses by version: 152: 0x0800141C, 153: 0x0800141C, 0159: 0x0800141C
- Vector: `EXINT0_IRQHandler`
- Confidence: high

## EXINT15_10_IRQHandler

**EXINT lines 12 and 14: record an input event code and latch DAT_20001fb8**

Line 12 (mask 0x1000) sets the event code DAT_20001fb7 to 2 and clears its pending bit. Line 14 (mask 0x4000) sets DAT_20001fb8 to 1 and, when no event code is pending, sets DAT_20001fb7 to 4, then clears its pending bit and returns. Both lines are tested with exint_flag_get and cleared with exint_flag_clear.

**Notes:** The meaning of the event codes is set by the consumer of DAT_20001fb7, which is not in this packet.

- Addresses by version: 148: 0x08004F2C, 14a: 0x0800531C, 14b: 0x08005644, 14e: 0x0800567C, 14f: 0x080056D8, 152: 0x08005730, 153: 0x08005748, 0159: 0x080058AC
- Vector: `EXINT15_10_IRQHandler`
- Calls: `exint_flag_clear`, `exint_flag_get`
- Confidence: high

## EXINT3_IRQHandler

**EXINT line 3 handler: set event code 5 and clear the pending bit**

If EXINT line 3 (mask 0x8) is pending, it clears the pending bit, zeroes DAT_20001fc6 and sets the event code DAT_20001fb7 to 5. When the line is not pending it does nothing.

- Addresses by version: 148: 0x08004F70, 14a: 0x08005360, 14b: 0x08005688, 14e: 0x080056C0, 14f: 0x0800571C, 152: 0x08005774, 153: 0x0800578C, 0159: 0x080058F0
- Vector: `EXINT3_IRQHandler`
- Calls: `exint_flag_clear`, `exint_flag_get`
- Confidence: high

## EXINT9_5_IRQHandler

**EXINT lines 9..5 shared interrupt handler: empty stub**

Vector for the shared external interrupt of EXINT lines 5-9. The body is a single return and does not clear any pending flag, so it is a placeholder for an unused interrupt. Present only in builds 148..14f.

- Addresses by version: 148: 0x08004F94, 14a: 0x08005384, 14b: 0x080056AC, 14e: 0x080056E4, 14f: 0x08005740
- Vector: `EXINT9_5_IRQHandler`
- Confidence: high

## EXINT9_5_IRQHandler_v152_159

**External interrupt lines 5..9 handler: empty stub**

Single bx lr. The shared EXTI 9..5 vector is not used by this firmware (builds 152, 153, 159), so the handler returns without clearing any pending flag.

- Addresses by version: 152: 0x0800141E, 153: 0x0800141E, 0159: 0x0800141E
- Vector: `EXINT9_5_IRQHandler`
- Confidence: high

## HardFault_Handler

**HardFault exception handler: infinite loop**

Cortex-M HardFault vector. Spins forever; the watchdog (if running) will reset the device, otherwise the MCU hangs. No fault status is saved.

- Addresses by version: 148: 0x0800539A, 14a: 0x08005786, 14b: 0x08005AAE, 14e: 0x08005AE6, 14f: 0x08005B42, 152: 0x08005B9A, 153: 0x08005C36, 0159: 0x08005D9A
- Vector: `HardFault_Handler`
- Confidence: high

## MemManage_Handler

**MemManage fault handler: infinite loop**

Cortex-M MemManage exception vector. Spins forever without saving fault status.

- Addresses by version: 148: 0x08005F3C, 14a: 0x0800635C, 14b: 0x080066CC, 14e: 0x08006704, 14f: 0x08006760, 152: 0x08006804, 153: 0x080068A0, 0159: 0x08006990
- Vector: `MemManage_Handler`
- Confidence: high

## NMI_Handler

**NMI exception handler: empty, returns immediately**

Cortex-M Non-Maskable Interrupt vector. Single return instruction; NMI events (e.g. clock failure detect) are ignored.

- Addresses by version: 148: 0x08005F5C, 14a: 0x0800637C, 14b: 0x080066EC, 14e: 0x08006724, 14f: 0x08006780, 152: 0x08006824, 153: 0x080068C0, 0159: 0x080069B0
- Vector: `NMI_Handler`
- Confidence: high

## PendSV_Handler

**PendSV exception handler: empty, returns immediately**

Cortex-M PendSV vector. A single return instruction; the firmware does not use an RTOS context switch through PendSV.

- Addresses by version: 148: 0x08007088, 14a: 0x080074C4, 14b: 0x08007828, 14e: 0x08007860, 14f: 0x080078BC, 152: 0x08007980, 153: 0x08007A1C, 0159: 0x08007AB4
- Vector: `PendSV_Handler`
- Confidence: high

## SVC_Handler

**SVC exception handler: empty (immediate return)**

Single bx lr instruction. The firmware does not use supervisor calls (no RTOS context switching on SVC), so the vector just returns. Installed in the Cortex-M vector table slot 11.

- Addresses by version: 148: 0x08007358, 14a: 0x08007794, 14b: 0x08007AF8, 14e: 0x08007B30, 14f: 0x08007B8C, 152: 0x08007C50, 153: 0x08007CEC, 0159: 0x08007D84
- Vector: `SVC_Handler`
- Confidence: high

## SysTick_Handler

**SysTick exception handler: empty (immediate return)**

Single bx lr. SysTick is not used as the system time base in this image; the millisecond counter (DAT_20001350) is produced elsewhere, presumably by a hardware timer ISR. Vector table slot 15.

- Addresses by version: 148: 0x08007EDE, 14a: 0x0800833A, 14b: 0x080086B2, 14e: 0x080086F2, 14f: 0x0800874E, 152: 0x08008812, 153: 0x080088AE, 0159: 0x08008912
- Vector: `SysTick_Handler`
- Confidence: high

## TMR2_GLOBAL_IRQHandler

**TMR2 global interrupt handler: empty (immediate return)**

Single bx lr; the vector slot is populated but TMR2 interrupt service does nothing in this firmware (no flag clear), so the interrupt is not enabled in practice.

- Addresses by version: 148: 0x08007F54, 14a: 0x080083B0, 14b: 0x08008728, 14e: 0x08008768, 14f: 0x080087C4, 152: 0x08008888, 153: 0x08008924, 0159: 0x08008988
- Vector: `TMR2_GLOBAL_IRQHandler`
- Confidence: high

## TMR5_GLOBAL_IRQHandler

**TMR5 global interrupt: count overflow events in DAT_20001350 and clear the flag**

Vector handler for TMR5. If the overflow flag (value 1, TMR_OVF_FLAG) is set, as read by tmr_flag_get on TMR5, the handler clears it with tmr_flag_clear and increments the counter at 0x20001350. Nothing else is done, and the counter has no reader in this packet.

**Notes:** Width of the counter at 0x20001350 is not visible in the decompile (it is read and written as one unit).

- Addresses by version: 148: 0x08007F58, 14a: 0x080083B4, 14b: 0x0800872C, 14e: 0x0800876C, 14f: 0x080087C8, 152: 0x0800888C, 153: 0x08008928, 0159: 0x0800898C
- Vector: `TMR5_GLOBAL_IRQHandler`
- Peripheral registers: `TMR5.CTRL1` (A)
- Calls: `tmr_flag_clear`, `tmr_flag_get`
- Confidence: high

## USART2_IRQHandler

**USART2 receive interrupt: store the received byte in a 250-byte ring at 0x200019ba**

Vector handler. When usart_flag_get reports the receive data buffer full flag (0x20), it reads the byte with usart_data_receive and stores it at index DAT_20000004 in the buffer at 0x200019ba, then advances the index with wrap-around at 250 (the last index is 249). Other interrupt causes are not handled here, and reading the data register clears the flag.

- Addresses by version: 148: 0x08008264, 14a: 0x080086C0, 14b: 0x08008A38, 14e: 0x08008A78, 14f: 0x08008AD4, 152: 0x08008B98, 153: 0x08008C34, 0159: 0x08008C98
- Vector: `USART2_IRQHandler`
- Peripheral registers: `USART2.STS` (A)
- Calls: `usart_data_receive`, `usart_flag_get`
- Confidence: high

## UsageFault_Handler

**UsageFault handler: spin forever**

Endless branch-to-self loop. A usage fault (undefined instruction, bad EPSR state, unaligned access if trapped) hangs the CPU until the watchdog (if running) resets the MCU. Vector slot 6.

- Addresses by version: 148: 0x08008F70, 14a: 0x08009414, 14b: 0x08009844, 14e: 0x080098DA, 14f: 0x08009A14, 152: 0x08009C1C, 153: 0x08009CE0, 0159: 0x08009DA4
- Vector: `UsageFault_Handler`
- Confidence: high

## nvic_irq_enable

**Set an interrupt's priority from the group setting and enable it in NVIC**

Encodes the preemption and sub-priority values into one 4-bit priority with the current AIRCR.PRIGROUP setting (preemption bits = min(4, 7 - group), sub-priority bits = the rest), writes it into the top four bits of the priority byte and then enables the IRQ. For negative IRQ numbers (system exceptions) the byte is written to SCB.SHPR at 0xE000ED14; for device IRQs it goes into NVIC IPR at 0xE000E400 and the enable bit is set in the NVIC ISER word (write-1-to-enable, so the write does not disturb other IRQs). This is the Artery SDK nvic_irq_enable. The decompiled code writes the ISER register as a plain store, which is equivalent because the register ignores zero bits.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | IRQ number; negative values select a system exception |
| `param_2` | `u32` | preemption priority |
| `param_3` | `u32` | sub-priority |

- Addresses by version: 148: 0x0800CEA0, 14a: 0x0800D2F4, 14b: 0x0800D780, 14e: 0x0800D820, 14f: 0x0800D96C, 152: 0x0800DBFC, 153: 0x0800DCF0, 0159: 0x0800DE48
- Peripheral registers: `NVIC+0x0` (A), `NVIC.None` (A), `SCB+0xc` (R), `SCB+0x14` (A)
- Called by: `vcu_exint14_pb14_init`, `vcu_exint_pb12_pb14_init`, `vcu_ertc_wakeup_exint_init`, `vcu_tmr5_1khz_tick_init`, `vcu_exint3_pa3_init`, `vcu_can1_init`
- Confidence: high

## nvic_priority_group_config

**Set the NVIC priority grouping (AIRCR.PRIGROUP) with the VECTKEY write**

Reads SCB.AIRCR, replaces PRIGROUP (bits 10..8) with the low three bits of the argument and writes 0x05FA in the VECTKEY field (bits 31..16) so the write is accepted. Changing the group after interrupts have been configured changes how existing priority values are split between preemption and sub-priority. This is the Artery SDK nvic_priority_group_config.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | priority group 0..7 (PRIGROUP value) |

- Addresses by version: 148: 0x0800CF18, 14a: 0x0800D36C, 14b: 0x0800D7F8, 14e: 0x0800D898, 14f: 0x0800D9E4, 152: 0x0800DC74, 153: 0x0800DD68, 0159: 0x0800DEC0
- Peripheral registers: `SCB+0xc` (RW)
- Called by: `vcu_peripheral_init_sequence`
- Confidence: high
