# BMS - `uart` functions

7 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`LL_USART_DeInit`](#ll_usart_deinit) | 0x0800308C | Pulses the RCC reset line of a USART instance (USART1 to USART6); returns 1 for other pointers |
| [`bms_usart3_comm_init`](#bms_usart3_comm_init) | 0x0800A574 | Bring up USART3 at 4800 8N1 on PB10/PB11 (AF4), enable IRQ 29 and its RX interrupt |
| [`bms_usart3_rxne_irq_set`](#bms_usart3_rxne_irq_set) | 0x0800A694 | Enable or disable the USART3 RX FIFO-not-empty interrupt (CR1.RXFNEIE) and return the previous IRQ state |
| [`bms_usart3_send_bytes`](#bms_usart3_send_bytes) | 0x0800A6D0 | Blocking transmit of a byte buffer on USART3, waiting for TC before each TDR write |
| [`bms_usart3_stop`](#bms_usart3_stop) | 0x0800A680 | Disable the USART3 RX-not-empty interrupt and reset USART3 |
| [`bms_usart3_tx_setup`](#bms_usart3_tx_setup) | (removed) | Reset USART3 and set PB10 to alternate function 4 as its output pin |
| [`bms_usart_init_from_config`](#bms_usart_init_from_config) | 0x08003140 | Configure a USART from a config record: CR1/CR2/CR3 fields, PRESC and BRR from the peripheral clock |

## LL_USART_DeInit

**Pulses the RCC reset line of a USART instance (USART1 to USART6); returns 1 for other pointers**

Resets one USART by writing a force-reset and then a release-reset to its bit in RCC APBRSTR2 (USART1 is bit 14, at 0x40021030) or RCC APBRSTR1 (USART2 bit 17, USART3 bit 18, USART4 bit 19, USART5 bit 8, USART6 bit 9, at 0x4002102C). It returns 0 (SUCCESS) for a known instance. For any other pointer it returns 1 and writes nothing.

| Parameter | Type | Description |
|---|---|---|
| `USARTx` | `ptr` | USART instance (USART_TypeDef pointer) |

**Returns** `u32`: ErrorStatus: 0 = SUCCESS, 1 = unknown instance

- Addresses by version: 4130: 0x0800308C, 4139: 0x0800308C, 4148: 0x0800308C, 4168: 0x0800308C
- Peripheral registers: `RCC.APBRSTR1` (RW), `RCC.APBRSTR2` (RW)
- Called by: `bms_usart3_stop`
- Confidence: high

## bms_usart3_comm_init

**Bring up USART3 at 4800 8N1 on PB10/PB11 (AF4), enable IRQ 29 and its RX interrupt**

Enables the GPIOB and USART3 clocks, configures PB10 and PB11 as alternate-function 4 pins with LL_GPIO_Init, and sets the priority of IRQ 29 to 0 and enables it through the NVIC enable register. It then programs USART3 with a LL_USART_Init-shaped block: baud 4800 (0x12C0), 8 data bits, 1 stop bit, no parity, TX and RX enabled, no hardware flow control, 16x oversampling. The register writes are bracketed by saving and restoring the interrupt mask, CR1 bit 29 (FIFOEN) and some CR2 and CR3 bits are cleared, the UART is enabled, and the routine waits for the REACK and TEACK acknowledge bits. It finishes with bms_usart3_rxne_irq_set(1).

**Notes:** IRQ 29 is inferred from the enable bit 0x20000000 and the IPR byte cleared at 0xE000E41C; the G0 vector name is the USART3/4/5/6 and LPUART1 line. The LL_USART_Init-shaped callee bms_4168_08003140 is not described in this packet.

- Addresses by version: 4130: 0x080094DC, 4139: 0x08009A14, 4148: 0x0800A260, 4168: 0x0800A574
- Peripheral registers: `USART3.CR1_FIFO_ENABLED` (ARW), `USART3.CR2` (RW), `USART3.CR3` (RW), `USART3.ISR_FIFO_ENABLED` (R), `RCC.IOPENR` (RW), `RCC.APBENR1` (RW), `NVIC+0x0` (W), `NVIC+0x31c` (RW)
- Called by: `bms_peripheral_bringup`, `bms_4168_080082f0`
- Calls: `LL_GPIO_Init`, `bms_usart_init_from_config`, `bms_usart3_rxne_irq_set`
- Confidence: medium

## bms_usart3_rxne_irq_set

**Enable or disable the USART3 RX FIFO-not-empty interrupt (CR1.RXFNEIE) and return the previous IRQ state**

With param_1 == 1 it sets USART3_CR1 bit 5 (RXFNEIE, RX FIFO not empty interrupt enable). With param_1 == 0 it clears the same bit. Any other value returns param_1 with no side effects. In privileged mode the register write is bracketed by isIRQinterruptsEnabled() to save the state, enableIRQinterrupts(1) before the write, and enableIRQinterrupts with the saved bit 0 after it, which is a short interrupt-masked critical section. Unprivileged code skips those calls, so the write is unprotected, and the saved state is reported as 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 1 to enable the RX interrupt, 0 to disable it; other values are a no-op |

**Returns** `u32`: IRQ-enable state saved before the write (0 when unprivileged)

**Notes:** The polarity of enableIRQinterrupts is not clear from the decompiled text: the entry call uses 1 and the restore uses the saved bit, which only makes sense if the argument is an enable flag on one side and a mask on the other. Confirm the helper definitions before relying on the critical-section behavior. The register is the FIFO-mode CR1 view (USART3 base 0x40004800).

- Addresses by version: 4130: 0x080095FC, 4139: 0x08009B34, 4148: 0x0800A380, 4168: 0x0800A694
- Peripheral registers: `USART3.CR1_FIFO_ENABLED` (RW)
- Called by: `bms_usart3_comm_init`, `bms_usart3_stop`
- Confidence: medium

## bms_usart3_send_bytes

**Blocking transmit of a byte buffer on USART3, waiting for TC before each TDR write**

For each of the param_2 bytes it polls USART3_ISR bit 6 (TC, transmission complete) until set, then writes the byte to USART3_TDR (0x40004828). Waiting on TC rather than TXFNF means each byte is fully shifted out before the next is written, so there is no FIFO overlap and throughput is lower. There is no timeout. Its only caller in the packet is bms_4168_08005128.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source buffer of u8 bytes |
| `param_2` | `u32` | number of bytes to send; 0 sends nothing |

- Addresses by version: 4130: 0x0800971C, 4139: 0x08009C54, 4148: 0x0800A3BC, 4168: 0x0800A6D0
- Peripheral registers: `USART3.ISR_FIFO_ENABLED` (R), `USART3.TDR` (W)
- Called by: `bms_comm_send_frame`
- Confidence: high

## bms_usart3_stop

**Disable the USART3 RX-not-empty interrupt and reset USART3**

Turns off USART3 reception and resets the peripheral. It calls bms_usart3_rxne_irq_set(0) to clear CR1.RXFNEIE and then LL_USART_DeInit(USART3), which pulses the RCC reset line. The previous interrupt state returned by the setter is ignored.

- Addresses by version: 4130: 0x080095E8, 4139: 0x08009B20, 4148: 0x0800A36C, 4168: 0x0800A680
- Peripheral registers: `USART3.CR1_FIFO_ENABLED` (A)
- Called by: `bms_4168_080082f0`
- Calls: `LL_USART_DeInit`, `bms_usart3_rxne_irq_set`
- Confidence: high

## bms_usart3_tx_setup

**Reset USART3 and set PB10 to alternate function 4 as its output pin**

Prepares the USART3 TX pin. It calls FUN_08009B34 with 0 (not described in this packet) and then LL_USART_DeInit(USART3). It writes 0x400 to GPIOB.BRR so PB10 is driven low, then calls LL_GPIO_Init on GPIOB with a 6-field init block: pin 0x400, mode field 1, speed 2, push-pull output, pull field 2 (pull-down) and alternate function 4. The field order follows LL_GPIO_InitTypeDef, and the pin is inferred to be USART3_TX from the AF4 selection and the USART3 context.

**Notes:** Callers are bms_4139_08007238 and bms_4139_0800e4f8. The exact meaning of the mode and pull fields and the AF4 pin mapping are inferred from the stack block.

- Addresses by version: 4130: 0x08009740, 4139: 0x08009C78
- Peripheral registers: `USART3.CR1_FIFO_ENABLED` (A)
- Called by: `bms_pb11_trigger_sequence_step`, `bms_4139_0800e4f8`
- Calls: `LL_GPIO_Init`, `LL_USART_DeInit`, `bms_usart3_rxne_irq_set`
- Confidence: medium

## bms_usart_init_from_config

**Configure a USART from a config record: CR1/CR2/CR3 fields, PRESC and BRR from the peripheral clock**

Returns 1 when the USART is already enabled (CR1.UE set). Otherwise it rebuilds CR1 from config words +0x08, +0x10, +0x14 and +0x1C (mask 0xEFFF69F3 clears M0/M1, parity, TE/RE and FIFO-independent mode bits before the config words are OR-ed in), replaces CR2 bits 12-13 (STOP) from +0x0C, and replaces CR3 bits 8-9 (RTSE and CTSE) from +0x18. It fetches the peripheral clock with bms_4168_08002d24 for USART1 (id 3), USART2 (id 0xC) and USART3 (id 0x30), or with bms_4168_08002d0c for USART4 to USART6. When the clock and the baud rate (+0x04) are nonzero, it divides the clock by the prescaler table entry at 0x08010A24 (1, 2, 4, 6, 8, 10, 12, 16, 32, 64, 128, 256, indexed by the +0x00 prescaler code 0 to 11) and computes BRR as the rounded quotient of clock/(divisor*baud) with bms_udiv32. When +0x1C is 0x8000 (CR1.OVER8) the divisor is doubled and BRR is shifted so that BRR[3] is dropped and BRR[2:0] takes the old BRR[3:1]. PRESC is written last from the prescaler code in every path. The routine follows the shape of ST HAL UART_SetConfig.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | USART instance (USART1 to USART6 or another peripheral) |
| `param_2` | `ptr` | USART config record: +0x00 prescaler code (0 to 11), +0x04 baud rate, +0x08 CR1 bits, +0x0C CR2 STOP bits, +0x10 and +0x14 CR1 bits, +0x18 CR3 flow-control bits, +0x1C CR1 bits (0x8000 = OVER8) |

**Returns** `u32`: 0 when the clock and baud checks passed (BRR written); 1 when the USART was already enabled or the instance is not handled

**Notes:** For USART4 to USART6 the clock is returned through bms_4168_08002d0c into auStack_20, but the code then tests local_18, which that path never assigns. The test therefore reads a stale stack value, so BRR for those instances may be computed from garbage. This may be a decompiler artifact; check the disassembly. bms_4168_08002d24 and bms_4168_08002d0c are not yet described.

- Addresses by version: 4130: 0x08003140, 4139: 0x08003140, 4148: 0x08003140, 4168: 0x08003140
- Called by: `bms_usart3_comm_init`
- Calls: `bms_udiv32`, `bms_rcc_get_clock_freqs`, `bms_rcc_periph_clk_get`
- Confidence: medium
