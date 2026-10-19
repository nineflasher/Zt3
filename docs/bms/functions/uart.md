# BMS - `uart` functions

5 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`LL_USART_DeInit`](#ll_usart_deinit) | 0x0800308C | Pulses the RCC reset line of a USART instance (USART1 to USART6); returns 1 for other pointers |
| [`bms_usart3_rxne_irq_set`](#bms_usart3_rxne_irq_set) | 0x0800A694 | Enable or disable the USART3 RX FIFO-not-empty interrupt (CR1.RXFNEIE) and return the previous IRQ state |
| [`bms_usart3_send_bytes`](#bms_usart3_send_bytes) | 0x0800A6D0 | Blocking transmit of a byte buffer on USART3, waiting for TC before each TDR write |
| [`bms_usart3_stop`](#bms_usart3_stop) | 0x0800A680 | Disable the USART3 RX-not-empty interrupt and reset USART3 |
| [`bms_usart3_tx_setup`](#bms_usart3_tx_setup) | (removed) | Reset USART3 and set PB10 to alternate function 4 as its output pin |

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
- Called by: `bms_4168_0800a574`, `bms_usart3_stop`
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
- Called by: `bms_4168_08005128`
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
- Called by: `bms_4139_08007238`, `bms_4139_0800e4f8`
- Calls: `LL_GPIO_Init`, `LL_USART_DeInit`, `bms_usart3_rxne_irq_set`
- Confidence: medium
