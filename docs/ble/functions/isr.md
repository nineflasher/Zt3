# BLE - `isr` functions

14 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`Default_Handler`](#default_handler) | 0x0C035F90 | Fallback exception handler: dump fault registers and halt |
| [`HardFault_Handler`](#hardfault_handler) | 0x0C035FA8 | HardFault handler: dump fault state to trace UART and halt |
| [`NMI_Handler`](#nmi_handler) | 0x0C046EE8 | Non-maskable interrupt handler: spin forever |
| [`SysTick_Handler`](#systick_handler) | 0x0C03F674 | FreeRTOS xPortSysTickHandler: under BASEPRI mask call xTaskIncrementTick and pend PendSV if a switch is needed |
| [`ble_scb_irq_pending`](#ble_scb_irq_pending) | 0x0C0866F8 | True if the Cortex-M SCB ICSR VECTPENDING field is non-zero |
| [`hal_dma0_irq_handler`](#hal_dma0_irq_handler) | 0x0C04555C | IRQ3 vector: dispatch pending channel interrupts of DMA controller 0 (0x40120000) |
| [`hal_dma1_irq_handler`](#hal_dma1_irq_handler) | 0x0C04556C | IRQ4 vector: dispatch pending channel interrupts of DMA controller 1 (0x40130000) |
| [`hal_gpio_irq_handler`](#hal_gpio_irq_handler) | 0x0C02FEEC | GPIO interrupt service: ack both 32-pin banks and call the per-pin handler table at 0x2000a638 |
| [`hal_i2c_irq_handler`](#hal_i2c_irq_handler) | 0x0C0302F4 | Shared I2C ISR: for every instance whose IRQ is active, read status, handle TX abort and call its callback |
| [`hal_irq_install_handler`](#hal_irq_install_handler) | 0x0C046F54 | Store a callback in the IRQ handler table at 0x2000f4cc and enable the interrupt |
| [`hal_irq_remove_handler`](#hal_irq_remove_handler) | 0x0C046F7C | Disable an interrupt and clear its slot in the IRQ handler table at 0x2000f4cc |
| [`hal_sysipc_tx_done_irq_handler`](#hal_sysipc_tx_done_irq_handler) | 0x0C0314F0 | IPC transmit-complete ISR: ack 0x400000a0 bits 23/24, run tx-done callbacks, send the next queued message |
| [`nvic_any_masked_irq_pending`](#nvic_any_masked_irq_pending) | 0x0C086710 | Return 1 if any IRQ in a bitmask is both enabled and pending in the NVIC |
| [`rtos_svc_handler`](#rtos_svc_handler) | 0x0C03F910 | SVC exception handler: on SVC #2 switch to the first task using PSP and jump into it |

## Default_Handler

**Fallback exception handler: dump fault registers and halt**

Selects the stacked exception frame by EXC_RETURN bit2 (MSP or PSP), clears the 0x100-byte buffer at 0x2000b9a4 with memset, copies SCB registers SHCSR/CFSR/HFSR/MMFAR/BFAR/AFSR (0xe000ed24..ed3c) to 0x2000b9f0..ba04 and the stacked R0-R3, R12, LR, PC, xPSR to 0x2000ba08..ba24. It then prints "start backtrace:\r\n" byte-wise via the trace UART putc (0x0c045ac8), formats "pc:0x%x,lr:0x%x \r\n" with the stacked PC/LR using the snprintf at 0x0c071570 and prints that, calls the crash-dump routine 0x0c0476a0 (&0x0c0809a4, 0x2000b9ac, 0x78, 1), and spins forever. Installed on vector slot 13 (reserved); the body is identical to HardFault_Handler.

- Addresses by version: 219: 0x0C035F90
- Vector: `Reserved_13`
- Confidence: high

## HardFault_Handler

**HardFault handler: dump fault state to trace UART and halt**

Selects the stacked exception frame by EXC_RETURN bit2 (MSP or PSP), clears the 0x100-byte buffer at 0x2000b9a4 with memset, copies SCB registers SHCSR/CFSR/HFSR/MMFAR/BFAR/AFSR (0xe000ed24..ed3c) to 0x2000b9f0..ba04 and the stacked R0-R3, R12, LR, PC, xPSR to 0x2000ba08..ba24. It then prints "start backtrace:\r\n" byte-wise via the trace UART putc (0x0c045ac8), formats "pc:0x%x,lr:0x%x \r\n" with the stacked PC/LR using the snprintf at 0x0c071570 and prints that, calls the crash-dump routine 0x0c0476a0 (&0x0c0809a4, 0x2000b9ac, 0x78, 1), and spins forever.

- Addresses by version: 219: 0x0C035FA8
- Vector: `HardFault_Handler`
- Confidence: high

## NMI_Handler

**Non-maskable interrupt handler: spin forever**

Cortex-M NMI vector target. It is an empty infinite loop, so any NMI hangs the core until the watchdog (if enabled) resets the chip.

- Addresses by version: 219: 0x0C046EE8
- Vector: `NMI_Handler`
- Confidence: high

## SysTick_Handler

**FreeRTOS xPortSysTickHandler: under BASEPRI mask call xTaskIncrementTick and pend PendSV if a switch is needed**

SysTick exception vector. Saves/raises BASEPRI with rtos_enter_critical, calls xTaskIncrementTick (0x0c043f48, which advances the tick count, moves expired delayed tasks to the ready lists and returns non-zero when a context switch is required); if it returns non-zero writes 0x10000000 (PENDSVSET) to ICSR (0xE000ED04), then restores BASEPRI with rtos_exit_critical. Tick period is 1 ms (see vPortSetupTimerInterrupt).

- Addresses by version: 219: 0x0C03F674
- Vector: `SysTick_Handler`
- Peripheral registers: `0xe000e000` (A), `0xe000ed04` (W)
- Calls: `rtos_enter_critical`, `rtos_exit_critical`, `xTaskIncrementTick`
- Confidence: high

## ble_scb_irq_pending

**True if the Cortex-M SCB ICSR VECTPENDING field is non-zero**

Reads SCB->ICSR (0xE000ED04) and returns whether bits [20:12] (mask 0x1FF000, VECTPENDING) are non-zero, i.e. whether any exception/interrupt is pending to be taken. Read-only, no side effects. Called from ble_219_0c0883f0, probably an idle/sleep or critical-section path that checks for pending interrupts before entering low power.

**Returns** `bool`: true if an exception is pending

**Notes:** Caller context (low-power check) is inferred.

- Addresses by version: 219: 0x0C0866F8
- Peripheral registers: `0xe000ed04` (R)
- Called by: `norflash_wait_busy_or_suspend`
- Confidence: high

## hal_dma0_irq_handler

**IRQ3 vector: dispatch pending channel interrupts of DMA controller 0 (0x40120000)**

Exception vector IRQ3_Handler. Reads the PL08x-style DMACIntStatus register at 0x40120000 (controller 0, AUDMA in BES naming) and for each of the 8 channels whose bit is set calls hal_gpdma_chan_irq_handler(0, channel), which clears the TC/error flags and runs the registered callback. Returns the last callback result or 3 if no channel was pending (value unused by the NVIC). Companion of hal_dma1_irq_handler.

**Returns** `u32`: last hal_gpdma_chan_irq_handler result, 3 if nothing was pending

**Notes:** The harness lists RAM 0x2000f4d8 (= handler table 0x2000f4cc + 3*4) as read; the decompiled body does not show it.

- Addresses by version: 219: 0x0C04555C
- Vector: `IRQ3_Handler`
- Calls: `hal_gpdma_chan_irq_handler`
- Confidence: high

## hal_dma1_irq_handler

**IRQ4 vector: dispatch pending channel interrupts of DMA controller 1 (0x40130000)**

Exception vector IRQ4_Handler, identical to hal_dma0_irq_handler but for the second PL08x-style controller: reads DMACIntStatus at 0x40130000 (GPDMA in BES naming) and calls hal_gpdma_chan_irq_handler(1, channel) for every set bit of channels 0..7. Returns the last callback result or 4 when nothing was pending.

**Returns** `u32`: last hal_gpdma_chan_irq_handler result, 4 if nothing was pending

**Notes:** Listed RAM read 0x2000f4dc (= handler table 0x2000f4cc + 4*4) is not visible in the decompiled body.

- Addresses by version: 219: 0x0C04556C
- Vector: `IRQ4_Handler`
- Calls: `hal_gpdma_chan_irq_handler`
- Confidence: high

## hal_gpio_irq_handler

**GPIO interrupt service: ack both 32-pin banks and call the per-pin handler table at 0x2000a638**

Reads the pending pin-interrupt words of the two GPIO banks with bes_gpio_read_status_words(buf, 2) (via thunk 0x0c041b5c); if that returned fewer than two words, the missing word is read directly from the bank's raw interrupt status register (base from table 0x0c080fec[bank] + 0x44; for bank 1 that is 0x40088044). For each bank (DesignWare APB GPIO at 0x40081000 and 0x40088000) it writes the word to the end-of-interrupt register (+0x4c) to acknowledge, then loops over set bits with util_count_trailing_zeros32: the bit must be below the bank's pin count from byte table 0x0c080ff4 (else assert loop); pin number = bit + 32*bank; if the handler pointer DAT_2000a638[pin] is non-NULL it is called, and a non-zero return sets a 'context switch needed' flag. Finally rtos_port_yield_from_isr(flag) pends PendSV if any handler asked for it. No direct callers: installed as the GPIO interrupt vector. Shares the pin handler table with the GPIO IRQ registration code.

**Notes:** Register identification (+0x44 RAW_INTSTATUS, +0x4c PORTA_EOI) follows the DesignWare apb_gpio layout.

- Addresses by version: 219: 0x0C02FEEC
- Peripheral registers: `0x40081000` (A), `0x4008104c` (W), `0x40088000` (A), `0x40088044` (R), `0x4008804c` (W)
- Calls: `util_count_trailing_zeros32`, `thunk_bes_gpio_read_status_words`, `rtos_port_yield_from_isr`
- Confidence: high

## hal_i2c_irq_handler

**Shared I2C ISR: for every instance whose IRQ is active, read status, handle TX abort and call its callback**

Iterates over the six I2C instances described by the 12-byte ROM records at 0x0c081abc (+0 register base, +10 IRQ number; instance 0 uses IRQ 14, instance 1 IRQ 29). For each instance with a non-negative IRQ it tests the NVIC Interrupt Active Bit Register (0xe000e300 + 4*(irq>>5), bit irq&31); if the IRQ is active it reads the callback DAT_2000a6cc[inst] (6 pointers at 0x2000a6cc..0x2000a6e3), reads IC_RAW_INTR_STAT (base+0x34), calls hal_i2c_check_tx_abort(base) to detect/clear a TX abort, and if the callback is non-NULL calls callback(inst, raw_status & 0xffff, abort_result). Observed register bases include 0x40005000, 0x40006000 and 0x40060000 (DesignWare I2C). No direct callers: it is the I2C interrupt entry used for all instances; the callbacks continue the interrupt-mode task state machine (hal_i2c_task_done_handler / hal_i2c_task_start_next).

**Notes:** The decompiler renders the IRQ byte table as the string "\x1d" (0x0c081ad2); the handler relies on IABR to find which instance interrupted.

- Addresses by version: 219: 0x0C0302F4
- Peripheral registers: `0x40005000` (A), `0x40005034` (R), `0x40006000` (A), `0x40006034` (R), `0x40060000` (A), `0x40060034` (R), `0xe000e300` (R), `0xe000e308` (R)
- Calls: `hal_i2c_check_tx_abort`
- Confidence: high

## hal_irq_install_handler

**Store a callback in the IRQ handler table at 0x2000f4cc and enable the interrupt**

Inside vPortEnterCritical/vPortExitCritical (0x0c03f640/0x0c03f65c): nvic_clear_pending_irq(irq), writes param_2 into the 4-byte slot 0x2000f4cc + irq*4 of a software handler table, then nvic_set_default_priority_and_enable_irq(irq) (priority 0x60). Returns 0. The table is separate from the RAM vector table; the common IRQ trampolines look the handler up by IRQ number. Counterpart of hal_irq_remove_handler. Callers: peripheral open routines 0x0c0300d0, 0x0c0315d8 (HCI intersys), 0x0c031810, 0x0c045250, 0x0c0459d4, 0x0c046494.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | IRQ number (NVIC external interrupt index) |
| `param_2` | `ptr` | handler function pointer |

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C046F54
- Called by: `ble_219_0c0300d0`, `ble_219_0c0315d8`, `ble_219_0c031810`, `ble_219_0c045250`, `ble_219_0c0459d4`, `ble_219_0c046494`
- Calls: `nvic_clear_pending_irq`, `nvic_set_default_priority_and_enable_irq`, `vPortEnterCritical`, `vPortExitCritical`
- Confidence: medium

## hal_irq_remove_handler

**Disable an interrupt and clear its slot in the IRQ handler table at 0x2000f4cc**

Inside vPortEnterCritical/vPortExitCritical: nvic_disable_irq(irq) and writes 0 into the handler slot 0x2000f4cc + irq*4. Inverse of hal_irq_install_handler. No direct callers (used through a function pointer or by peripheral close paths).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | IRQ number |

- Addresses by version: 219: 0x0C046F7C
- Calls: `nvic_disable_irq`, `vPortEnterCritical`, `vPortExitCritical`
- Confidence: medium

## hal_sysipc_tx_done_irq_handler

**IPC transmit-complete ISR: ack 0x400000a0 bits 23/24, run tx-done callbacks, send the next queued message**

For IPC channel 0 and 1 it tests register 0x400000a0 (bit 23 for channel 0, bit 24 for channel 1); when set it writes 1 (ch0) or 2 (ch1) to 0x400000a4 to acknowledge, then walks the list of sent message nodes whose head is DAT_2000a9cc[ch] (node: +0 next, +4 type byte 0/1 (assert if >1), +8 and +0xc payload words, +0x10 in-use byte): for each node it calls the tx-done callback DAT_2000aa54[ch*2 + type](node[0xc], node[8]) if registered and clears the in-use byte. If the pending list DAT_2000aa4c[ch] is empty it clears the head and the channel-busy byte DAT_2000a98c[ch]; when the global busy flag DAT_2000a988 is set and both channel busy bytes (0x2000a98c, 0x2000a98d) are now clear it calls pm_busy_mask_clear_bit(0) and clears DAT_2000a988 (IPC no longer vetoes sleep). Otherwise it moves the pending list to the head, empties it, and raises the doorbell by writing 4 (ch0) or 8 (ch1) to 0x400000a0 (read back to flush). No direct callers: reached from the IPC interrupt vector installed by hal_sysipc_rx_irq_setup (0x0c0314bc). Counterpart of hal_sysipc_send, which builds the nodes and the lists.

**Notes:** Identification as the Bestechnic inter-core IPC (hal_sysipc / hal_mcu2bt) follows the wave-1 hal_sysipc_* naming; register bit semantics of 0x400000a0/a4 are inferred from usage.

- Addresses by version: 219: 0x0C0314F0
- Peripheral registers: `0x400000a0` (RW), `0x400000a4` (W)
- Calls: `pm_busy_mask_clear_bit`
- Confidence: medium

## nvic_any_masked_irq_pending

**Return 1 if any IRQ in a bitmask is both enabled and pending in the NVIC**

Clamps the word count param_2 to at most 3 (returns 0 immediately if it is 0), then for each word i ANDs NVIC_ISER[i] (0xE000E100+4i, enable set), NVIC_ICPR[i] (0xE000E280+4i, reads pending state) and the caller-supplied mask word param_1[i]. Returns 1 on the first non-zero result, else 0. Used (from 0x0c0883f0) to check whether a wake-up/interrupt of interest is already pending, e.g. before entering sleep; covers IRQ 0..95.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | array of u32 IRQ mask words (bit n of word i = IRQ 32*i+n) |
| `param_2` | `u32` | number of mask words to test, clamped to 3 |

**Returns** `u32`: 1 if an enabled and pending IRQ matches the mask, else 0

- Addresses by version: 219: 0x0C086710
- Peripheral registers: `0xe000e100` (R), `0xe000e104` (R), `0xe000e280` (R), `0xe000e284` (R)
- Called by: `norflash_wait_busy_or_suspend`
- Confidence: high

## rtos_svc_handler

**SVC exception handler: on SVC #2 switch to the first task using PSP and jump into it**

Selects MSP or PSP from EXC_RETURN bit 2, reads the stacked PC (frame+0x18) and checks that the SVC immediate byte at PC-2 equals 2; otherwise returns. For SVC 2 it sets CPACR (0xE000ED88) |= 0xF00000 (FPU access), FPCCR (0xE000EF34) |= 0xC0000000 (ASPEN/LSPEN lazy FP stacking), loads the TCB pointer from *DAT_2000cb8c, sets PSPLIM from TCB[0], switches thread mode to PSP, sets PSP = TCB + 0x28 and then calls the function pointer stored in TCB[1] with (PSP, 2), which restores the context and enters the first task. Vector-table entry SVC_Handler.

**Notes:** Decompiler could not fully recover the final indirect jump; exact role of TCB[1] (context-restore routine) is inferred.

- Addresses by version: 219: 0x0C03F910
- Vector: `SVC_Handler`
- Confidence: medium
