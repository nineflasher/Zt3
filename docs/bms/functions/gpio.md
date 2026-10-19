# BMS - `gpio` functions

23 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`HAL_GPIO_DeInit`](#hal_gpio_deinit) | 0x08001F4C | Resets GPIO pins in a mask to analog input and clears their EXTI and AF settings |
| [`HAL_GPIO_Init`](#hal_gpio_init) | 0x0800202C | Configures GPIO pins from a GPIO_InitTypeDef record: mode, pull, speed, AF and EXTI |
| [`LL_GPIO_Init`](#ll_gpio_init) | 0x08002C24 | Configures every pin in an init mask for mode, speed, output type, pull and alternate function |
| [`LL_GPIO_IsInputPinSet`](#ll_gpio_isinputpinset) | 0x08002CD4 | Returns 1 when every pin in the mask reads high in GPIO IDR |
| [`LL_GPIO_ResetOutputPin`](#ll_gpio_resetoutputpin) | 0x08002CE6 | Drives the selected GPIO output pins low by writing the mask to GPIOx BRR |
| [`LL_GPIO_SetOutputPin`](#ll_gpio_setoutputpin) | 0x08002CEA | Drives the selected GPIO output pins high by writing the mask to GPIOx BSRR |
| [`bms_gpio_board_init`](#bms_gpio_board_init) | 0x08008FCC | Board GPIO bring-up: clocks for ports A to D and F, initial output levels, pin modes |
| [`bms_gpio_exti_init`](#bms_gpio_exti_init) | 0x080091F8 | Configure EXTI lines 2, 8 and 12 with their source ports and edges, and enable NVIC IRQ 6 and 7 |
| [`bms_pa12_ready_handshake`](#bms_pa12_ready_handshake) | 0x08009A0C | Pulse PA11 and poll PA12 for a low level; on timeout set *param_1 and return 1 |
| [`bms_pa5_drive_level`](#bms_pa5_drive_level) | 0x0800B8AC | Drive GPIOA pin 5 high for a nonzero argument, low for zero |
| [`bms_pb11_trigger_sequence_step`](#bms_pb11_trigger_sequence_step) | (removed) | Advance the PB11 trigger sequence (phases 0 to 2) and publish record 0x2C thresholds |
| [`bms_pd0_indicator_step`](#bms_pd0_indicator_step) | 0x0800E820 | Drive output PD0 with a blink pattern chosen from flag words, advancing the timer by param_5 |
| [`gpio_pa15_reset`](#gpio_pa15_reset) | 0x08008F20 | Drive GPIOA pin 15 low through BRR |
| [`gpio_pa15_set`](#gpio_pa15_set) | 0x08008F2C | Drive GPIOA pin 15 high through BSRR |
| [`gpio_pa5_reset`](#gpio_pa5_reset) | 0x08009414 | Drive GPIOA pin 5 low through BRR |
| [`gpio_pa5_set`](#gpio_pa5_set) | 0x0800941E | Drive GPIOA pin 5 high through BSRR |
| [`gpio_pb13_15_strap_read`](#gpio_pb13_15_strap_read) | 0x08008F50 | Read PB13, PB14 and PB15 as active-low inputs and return a 3-bit mask |
| [`gpio_pb1_read`](#gpio_pb1_read) | 0x08008F38 | Read the input level of GPIOB pin 1 (1 when high) |
| [`gpio_pb2_read`](#gpio_pb2_read) | 0x08008EE8 | Read the input level of GPIOB pin 2 (1 when high) |
| [`gpio_pb8_reset`](#gpio_pb8_reset) | 0x08008F00 | Drive GPIOB pin 8 low through BRR |
| [`gpio_pb8_set`](#gpio_pb8_set) | 0x08008F10 | Drive GPIOB pin 8 high through BSRR |
| [`gpio_pd0_reset`](#gpio_pd0_reset) | 0x080091E0 | Drive pin 0 of the port at 0x50000C00 low through BRR |
| [`gpio_pd0_set`](#gpio_pd0_set) | 0x080091EC | Drive pin 0 of the port at 0x50000C00 high through BSRR |

## HAL_GPIO_DeInit

**Resets GPIO pins in a mask to analog input and clears their EXTI and AF settings**

For each pin set in the mask param_2 on the port in param_1 (GPIOA to GPIOF map to port codes 0 to 5 by pointer compare): if the SYSCFG EXTICR field for that pin selects this port, it clears the pin's bits in EXTI RTSR1 (0x40021800), FTSR1 (0x40021804), IMR1 (0x40021880) and EMR1 (0x40021884) and clears the EXTICR field. It then sets the pin's MODER field to 0b11 (analog) and clears its AFR nibble and its OSPEEDR, OTYPER and PUPDR bits.

| Parameter | Type | Description |
|---|---|---|
| `port` | `ptr` | param_1, GPIO port register block (GPIO_Type *) |
| `pin_mask` | `u32` | param_2, pins to reset, one bit per pin |

**Notes:** Mirrors ST HAL_GPIO_DeInit. The port code (A=0..F=5) is what the EXTICR fields store.

- Addresses by version: 4130: 0x08001F4C, 4139: 0x08001F4C, 4148: 0x08001F4C, 4168: 0x08001F4C
- Peripheral registers: `EXTI.RTSR1` (RW), `EXTI.FTSR1` (RW), `EXTI.EXTICR1` (RW), `EXTI.IMR1` (RW), `EXTI.EMR1` (RW)
- Called by: `HAL_FDCAN_MspDeInit`
- Confidence: high

## HAL_GPIO_Init

**Configures GPIO pins from a GPIO_InitTypeDef record: mode, pull, speed, AF and EXTI**

Takes a GPIO_InitTypeDef-style record (Pin, Mode, Pull, Speed, Alternate, as 32-bit words) and applies it to the port in param_1 for each pin in the Pin mask, scanning bits from 0 upward. Mode bits 0-1 go into MODER. For output and AF modes (1 or 2) Speed goes to OSPEEDR and the output-type bit (mode bit 4) to OTYPER. PUPDR is written unless the mode is analog, and AFRL/AFRH get the Alternate nibble in AF mode. If mode bit 16 (interrupt) or bit 17 (event) is set, the port code goes into SYSCFG EXTICR, and EXTI RTSR1 and FTSR1 take the rising (bit 20) and falling (bit 21) trigger bits, while IMR1 and EMR1 take the interrupt and event enables.

| Parameter | Type | Description |
|---|---|---|
| `port` | `ptr` | param_1, GPIO port register block (GPIO_Type *) |
| `init` | `ptr` | param_2, GPIO_InitTypeDef-style record: pin mask, mode, pull, speed, alternate |

**Notes:** Mirrors ST HAL_GPIO_Init and its mode encoding (MODE, OTYPE, IT/EVT, RISING/FALLING bits).

- Addresses by version: 4130: 0x0800202C, 4139: 0x0800202C, 4148: 0x0800202C, 4168: 0x0800202C
- Peripheral registers: `EXTI.RTSR1` (RW), `EXTI.FTSR1` (RW), `EXTI.EXTICR1` (RW), `EXTI.IMR1` (RW), `EXTI.EMR1` (RW)
- Called by: `HAL_FDCAN_MspInit`
- Confidence: high

## LL_GPIO_Init

**Configures every pin in an init mask for mode, speed, output type, pull and alternate function**

Per-pin GPIO configuration, as in ST's LL_GPIO_Init, for each bit set in init[0] (the pin mask). For each pin it writes MODER (2 bits, from init[1]) and PUPDR (2 bits, from init[4]). For output or alternate mode (init[1] equal to 1 or 2) it also writes OTYPER (1 bit, init[3]) and OSPEEDR (2 bits, init[2]). For alternate mode (init[1] equal to 2) it writes the 4-bit AF value init[5] to AFRL for pins 0 to 7 or AFRH for pins 8 to 15. Each field is cleared before the new value is ORed in. It returns 0 (SUCCESS).

| Parameter | Type | Description |
|---|---|---|
| `GPIOx` | `ptr` | GPIO port (GPIO_TypeDef pointer) |
| `init` | `ptr` | LL_GPIO_InitTypeDef-style record: Pin, Mode, Speed, OutputType, Pull, Alternate |

**Returns** `u32`: 0 = SUCCESS

- Addresses by version: 4130: 0x08002C24, 4139: 0x08002C24, 4148: 0x08002C24, 4168: 0x08002C24
- Called by: `bms_4168_080082f0`, `bms_adc_hw_init`, `gpio_pb13_15_strap_read`, `bms_gpio_board_init`, `bms_gpio_exti_init`, `bms_i2c_bb_bus_init`, `bms_i2c_bb_bus_release`, `bms_spi1_master_init`, `bms_usart3_comm_init`
- Confidence: high

## LL_GPIO_IsInputPinSet

**Returns 1 when every pin in the mask reads high in GPIO IDR**

Reads GPIOx IDR (offset 0x10) and returns 1 only if all bits of PinMask are set, so a multi-pin mask is an AND test. It has no side effects. It is used by several callers for input level checks.

| Parameter | Type | Description |
|---|---|---|
| `GPIOx` | `ptr` | GPIO port |
| `PinMask` | `u32` | pin bit mask to test |

**Returns** `bool`: true if all pins in the mask are high

- Addresses by version: 4130: 0x08002CD4, 4139: 0x08002CD4, 4148: 0x08002CD4, 4168: 0x08002CD4
- Called by: `bms_i2c_bb_send_bit0`, `bms_i2c_bb_send_bit1`, `bms_i2c_bb_read_byte`, `bms_i2c_bb_write_byte`, `bms_i2c_bb_start`, `bms_i2c_bb_stop`, `bms_pa12_ready_handshake`
- Confidence: high

## LL_GPIO_ResetOutputPin

**Drives the selected GPIO output pins low by writing the mask to GPIOx BRR**

Writes PinMask to GPIOx BRR (offset 0x28). On this part, BRR clears the output latch of each set bit and ignores zero bits, so other pins are not disturbed. The function has no return value and no read-modify-write.

| Parameter | Type | Description |
|---|---|---|
| `GPIOx` | `ptr` | GPIO port |
| `PinMask` | `u32` | pins to drive low |

- Addresses by version: 4130: 0x08002CE6, 4139: 0x08002CE6, 4148: 0x08002CE6, 4168: 0x08002CE6
- Called by: `bms_i2c_bb_send_bit0`, `bms_i2c_bb_send_bit1`, `bms_i2c_bb_read_byte`, `bms_i2c_bb_write_byte`, `bms_i2c_bb_start`, `bms_i2c_bb_stop`, `bms_pa12_ready_handshake`
- Confidence: high

## LL_GPIO_SetOutputPin

**Drives the selected GPIO output pins high by writing the mask to GPIOx BSRR**

Writes PinMask to GPIOx BSRR (offset 0x18). A 1 bit sets the matching output latch and a 0 bit has no effect, so other pins are not disturbed. The function has no return value and no read-modify-write.

| Parameter | Type | Description |
|---|---|---|
| `GPIOx` | `ptr` | GPIO port |
| `PinMask` | `u32` | pins to drive high |

- Addresses by version: 4130: 0x08002CEA, 4139: 0x08002CEA, 4148: 0x08002CEA, 4168: 0x08002CEA
- Called by: `bms_i2c_bb_send_bit0`, `bms_i2c_bb_bus_init`, `bms_i2c_bb_send_bit1`, `bms_i2c_bb_read_byte`, `bms_i2c_bb_write_byte`, `bms_i2c_bb_start`, `bms_i2c_bb_stop`, `bms_pa12_ready_handshake`
- Confidence: high

## bms_gpio_board_init

**Board GPIO bring-up: clocks for ports A to D and F, initial output levels, pin modes**

Enables the RCC.IOPENR clocks for GPIOA, GPIOB, GPIOC, GPIOD and GPIOF, then drives PA5, PA9 and PA15 low, PC7 and PD0 low and PD3 high through the BRR and BSRR registers. It then makes 28 calls to LL_GPIO_Init with pin masks for each port, for example 0x0003 on port A, 0x3B43 on port C and 0x0370 on port D, to set input, output, analog or alternate modes. It is called from bms_4168_08008294 and bms_4168_080082F0 during initialisation and returns nothing. The pin functions are not identified in this packet.

**Notes:** Mode and pull values for each of the 28 calls are set by stack writes between calls; the table is not reproduced here.

- Addresses by version: 4130: 0x08007F6C, 4139: 0x0800846C, 4148: 0x08008CB8, 4168: 0x08008FCC
- Peripheral registers: `RCC.IOPENR` (RW)
- Called by: `bms_peripheral_bringup`, `bms_4168_080082f0`
- Calls: `LL_GPIO_Init`
- Confidence: medium

## bms_gpio_exti_init

**Configure EXTI lines 2, 8 and 12 with their source ports and edges, and enable NVIC IRQ 6 and 7**

Sets analog or input modes for the interrupt input pins from the init masks on ports A, B, C, D and F and drives PA9 high. EXTI line 12 is routed to port B and configured for falling-edge trigger when PB12 reads high at this point, otherwise rising edge. Line 8 is routed to port A with a falling edge, and line 2 is routed to port C with a falling edge, after which its pending bit is cleared through the FPR register. PB12, PA8 and PC2 are switched back to input with their pulls cleared. Finally NVIC IRQ 7 (EXTI4_15) and IRQ 6 (EXTI2_3) are enabled with priority byte 0x80.

**Notes:** Trigger codes are read as LL constants (2 falling, 1 rising), not checked against the header. The IRQ names are the standard G0 vector names and match the brief's IRQ list.

- Addresses by version: 4130: 0x08008198, 4139: 0x08008698, 4148: 0x08008EE4, 4168: 0x080091F8
- Peripheral registers: `EXTI.RPR1` (A), `EXTI.FPR1` (W), `EXTI.EXTICR1` (RW), `EXTI.EXTICR3` (RW), `EXTI.EXTICR4` (RW), `NVIC+0x0` (W), `NVIC+0x304` (RW)
- Called by: `bms_4168_080082f0`
- Calls: `LL_EXTI_Init`, `LL_GPIO_Init`
- Confidence: medium

## bms_pa12_ready_handshake

**Pulse PA11 and poll PA12 for a low level; on timeout set *param_1 and return 1**

Two-pin handshake on GPIOA. It presets the PA12 output latch high through GPIOA.BSRR, clears MODER bits 25:24 to make PA12 an input, then drives PA11 high. After one bms_systick_wait_scaled(1) delay it polls PA12 with LL_GPIO_IsInputPinSet up to 0x9C5 (2501) times. If PA12 reads low, PA11 is driven low, *param_1 is set to 0 and the function returns 0. If the budget runs out, FUN_0800997C is called (not described in this packet), *param_1 is set to 1, PA11 is released and the function returns 1. The reading of PA11 as a request output and PA12 as the peer's ready line is inferred from the sequence.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | status byte written by the routine: 0 when PA12 went low, 1 on timeout |

**Returns** `bool`: 1 on timeout, 0 when PA12 went low within the poll budget

**Notes:** Caller is bms_4168_080097d8. The 2501-poll budget and the PA11/PA12 roles are not confirmed. FUN_0800997C is the timeout path and is outside this packet.

- Addresses by version: 4130: 0x080089AC, 4139: 0x08008EAC, 4148: 0x080096F8, 4168: 0x08009A0C
- Called by: `bms_i2c_bb_write_byte_ack`
- Calls: `LL_GPIO_IsInputPinSet`, `LL_GPIO_ResetOutputPin`, `LL_GPIO_SetOutputPin`, `bms_systick_wait_scaled`, `bms_i2c_bb_stop`
- Confidence: medium

## bms_pa5_drive_level

**Drive GPIOA pin 5 high for a nonzero argument, low for zero**

Thin wrapper that sets the level of GPIOA pin 5. A nonzero argument calls gpio_pa5_set (BSRR) and zero calls gpio_pa5_reset (BRR). It changes no other state.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | nonzero drives PA5 high, zero drives it low |

- Addresses by version: 4130: 0x0800A944, 4139: 0x0800AE7C, 4148: 0x0800B598, 4168: 0x0800B8AC
- Called by: `bms_4168_0800c6dc`
- Calls: `gpio_pa5_reset`, `gpio_pa5_set`
- Confidence: high

## bms_pb11_trigger_sequence_step

**Advance the PB11 trigger sequence (phases 0 to 2) and publish record 0x2C thresholds**

Per-tick sequencer for the PB11 trigger input in the 4139 build (the 4130 build has the same routine). It resets the phase byte at 0x20000117 to 0 and returns unless bit 5 of the state byte at +0x194 is set. Phase 0 calls the dual-bank step with 0 and moves to phase 1. Phase 1 calls the dual-bank step with 1, and when 0x20000112 is 1 it moves to phase 2, starts USART3 TX (bms_usart3_tx_setup), arms EXTI line 11 (bms_exti11_irq_arm) and sets the phase to 2. Every phase-1 pass writes record 0x2C (bms_record12_addr) as two s16 values: state+0x6C when 0x20000113 is 1 otherwise 6, and that value minus 2. Phase 2 waits for bit 10 of the word returned by the accessor at 0x0800B3EC to be set, or for bms_pb11_hold_timer_step to report the latched PB11 hold; it then clears bit 10, disarms EXTI line 11 (bms_exti11_irq_disarm), runs the USART3 RX bring-up bms_4168_0800a574 and returns to phase 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | passed unchanged to the dual-bank step and to the PB11 hold timer |

**Notes:** Call sites are matched to the callee names through the existing 4139 entries (bms_4139_08009b70, bms_4139_08009ba8, bms_4139_08009bdc, bms_4139_08009c78, bms_4139_080072e0). The accessors at 0x0800B3E4 and 0x0800B3EC are not described in this packet, and the meaning of bit 10 is inferred. The USART3 call at the end of phase 2 is the 4168 family name from the callee list, not the 4139 USART3 setup.

- Addresses by version: 4130: 0x08006D38, 4139: 0x08007238
- Called by: `bms_4168_08010558`
- Calls: `bms_4139_dual_bank_step`, `bms_pb11_hold_timer_step`, `bms_exti11_irq_disarm`, `bms_exti11_irq_arm`, `bms_usart3_tx_setup`, `bms_usart3_comm_init`, `bms_ram_20000bdc_addr`, `bms_ram_200001c8_addr`, `bms_record12_addr`
- Confidence: medium

## bms_pd0_indicator_step

**Drive output PD0 with a blink pattern chosen from flag words, advancing the timer by param_5**

Adds param_5 to the timer DAT_20000564 on each call and chooses one of several patterns from the flag words. Pattern 1 (param_2 bit 2, or param_1 bit 5 or 6) has a 2000-tick period and is high from 1000 to 1999; pattern 2 (param_1 bit 3 or 4, param_3 bit 11, or param_2 bit 4) has a 3000-tick period and is high from 1500 to 2999; pattern 3 (param_1 bits 7, 8, 9, 10 or 12) has a 4000-tick period and is high from 2000 to 3999. When none of those match, param_1 bit 2 drives the output high at once, param_1 bit 1 gives a 1000-tick period high from 500 to 999, and otherwise param_4 bit 8 selects solid high or a 200-tick period high from 100 to 199. Each period ends by calling gpio_pd0_reset and clearing the timer, and the solid cases call gpio_pd0_set and clear the timer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | state flags; bits 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 and 12 select patterns |
| `param_2` | `u16` | flag word; bits 2 and 4 select patterns |
| `param_3` | `u32` | flag word; bit 11 selects pattern 2 |
| `param_4` | `s32` | bit 8 chooses the 200-tick pattern over solid high when no other pattern applies |
| `param_5` | `s16` | elapsed ticks added to the timer |

**Notes:** Whether PD0 drives an active-high or active-low LED or buzzer is not established here. The callers are not in this packet, so the meaning of the flag words is unknown. gpio_pd0_set and gpio_pd0_reset are the port-0x50000C00 BSRR and BRR writes described in the packet.

- Addresses by version: 4130: 0x0800CDA4, 4139: 0x0800D38C, 4148: 0x0800E38C, 4168: 0x0800E820
- Called by: `bms_state_snapshot_submit`
- Calls: `gpio_pd0_reset`, `gpio_pd0_set`
- Confidence: medium

## gpio_pa15_reset

**Drive GPIOA pin 15 low through BRR**

Writes 0x8000 to GPIOA.BRR (0x50000028), which resets PA15 atomically and leaves the other port-A pins alone. It is the reset half of gpio_pa15_set. Callers bms_4139_0800be74, bms_4168_08003fcc and bms_4168_0800c96c. The function of the pin is not established.

- Addresses by version: 4130: 0x08007ED4, 4139: 0x080083D4, 4148: 0x08008C20, 4168: 0x08008F20
- Called by: `bms_fault_timers_step`, `bms_4168_0800c96c`
- Confidence: high

## gpio_pa15_set

**Drive GPIOA pin 15 high through BSRR**

Writes 0x8000 to GPIOA.BSRR (0x50000018), which sets PA15 atomically without touching the other port-A pins. It is the set half of gpio_pa15_reset. Callers bms_4139_0800be74 and bms_4168_0800c96c.

- Addresses by version: 4130: 0x08007EE0, 4139: 0x080083E0, 4148: 0x08008C2C, 4168: 0x08008F2C
- Called by: `bms_4168_0800c96c`
- Confidence: high

## gpio_pa5_reset

**Drive GPIOA pin 5 low through BRR**

Writes 0x20 to GPIOA.BRR (0x50000028), which resets PA5 atomically. It is the reset half of gpio_pa5_set. The only caller in the packet is bms_4168_0800b8ac. The pin's function is not established.

- Addresses by version: 4130: 0x080083B4, 4139: 0x080088B4, 4148: 0x08009100, 4168: 0x08009414
- Called by: `bms_pa5_drive_level`
- Confidence: high

## gpio_pa5_set

**Drive GPIOA pin 5 high through BSRR**

Writes 0x20 to GPIOA.BSRR (0x50000018), which sets PA5 atomically. It is the set half of gpio_pa5_reset. The only caller in the packet is bms_4168_0800b8ac.

- Addresses by version: 4130: 0x080083BE, 4139: 0x080088BE, 4148: 0x0800910A, 4168: 0x0800941E
- Called by: `bms_pa5_drive_level`
- Confidence: high

## gpio_pb13_15_strap_read

**Read PB13, PB14 and PB15 as active-low inputs and return a 3-bit mask**

Enables the GPIOB clock (RCC.IOPENR bit 1), configures PB13 to PB15 as inputs with pull-up through LL_GPIO_Init, and samples GPIOB.IDR bits 13 to 15. Bit 0, 1 or 2 of the result is set for each pin that reads low, then the same three pins are reconfigured as analog with no pull. The inputs are probably board straps or jumpers read at start-up; their role is not established in this packet. It is called from bms_4168_080040e4.

**Returns** `u8`: bit i set when PB(13+i) reads low

- Addresses by version: 4130: 0x08007F04, 4139: 0x08008404, 4148: 0x08008C50, 4168: 0x08008F50
- Peripheral registers: `RCC.IOPENR` (RW)
- Called by: `bms_index_debounce_step`
- Calls: `LL_GPIO_Init`
- Confidence: medium

## gpio_pb1_read

**Read the input level of GPIOB pin 1 (1 when high)**

Reads the GPIO input data register at 0x50000410 and returns bit 1 as a bool, true when the pin is high. It is the same read as gpio_pb2_read for a different bit, and it is read-only. Callers bms_4139_0800e4f8 and bms_4168_0800fd7c. What the pin carries is not in this packet.

**Returns** `bool`: true when PB1 is high

**Notes:** Port B at 0x50000400 is inferred from the G0 layout, as in gpio_pb2_read.

- Addresses by version: 4130: 0x08007EEC, 4139: 0x080083EC, 4148: 0x08008C38, 4168: 0x08008F38
- Called by: `bms_4168_0800fd7c`
- Confidence: medium

## gpio_pb2_read

**Read the input level of GPIOB pin 2 (1 when high)**

Reads the GPIO input data register at 0x50000410 and returns bit 2 as a bool, true when the pin is high. The address is GPIOB.IDR on the STM32G0 port layout, where port B is at 0x50000400. It is read-only with no side effects. Callers bms_4139_0800e4f8 and bms_4168_0800fd7c use it as a status input; what the pin carries is not in this packet.

**Returns** `bool`: true when PB2 is high

**Notes:** The port identification (GPIOB at 0x50000400) is inferred from the G0 layout and the offset 0x10 (IDR).

- Addresses by version: 4130: 0x08007E9C, 4139: 0x0800839C, 4148: 0x08008BE8, 4168: 0x08008EE8
- Called by: `bms_4168_0800fd7c`
- Confidence: medium

## gpio_pb8_reset

**Drive GPIOB pin 8 low through BRR**

Writes 0x100 to GPIOB.BRR (0x50000428), which resets PB8 atomically and leaves the other port-B pins alone. The reset and set routines for PB8 and PA15 are paired, and the caller bms_4168_0800c96c calls all four, so they probably drive a set of output control pins. Callers bms_4139_0800be74 and bms_4168_0800c96c. The function of the pin is not established.

**Notes:** Port B at 0x50000400 is inferred from the G0 layout; BRR is offset 0x28.

- Addresses by version: 4130: 0x08007EB4, 4139: 0x080083B4, 4148: 0x08008C00, 4168: 0x08008F00
- Called by: `bms_4168_0800c96c`
- Confidence: medium

## gpio_pb8_set

**Drive GPIOB pin 8 high through BSRR**

Writes 0x100 to GPIOB.BSRR (0x50000418), which sets PB8 atomically without touching the other port-B pins. It is the set half of gpio_pb8_reset. Callers bms_4139_0800be74 and bms_4168_0800c96c.

**Notes:** Port B at 0x50000400 is inferred from the G0 layout; BSRR is offset 0x18.

- Addresses by version: 4130: 0x08007EC4, 4139: 0x080083C4, 4148: 0x08008C10, 4168: 0x08008F10
- Called by: `bms_4168_0800c96c`
- Confidence: medium

## gpio_pd0_reset

**Drive pin 0 of the port at 0x50000C00 low through BRR**

Writes 1 to the BRR register at 0x50000C28 of the port based at 0x50000C00, which resets bit 0 atomically. It is the reset half of gpio_pd0_set. The only caller in the packet is bms_4168_0800e820. The pin's function is not established.

**Notes:** Port identification (0x50000C00 as GPIOD) is inferred from the G0 layout; the pin's function is unknown.

- Addresses by version: 4130: 0x08008180, 4139: 0x08008680, 4148: 0x08008ECC, 4168: 0x080091E0
- Called by: `bms_pd0_indicator_step`
- Confidence: medium

## gpio_pd0_set

**Drive pin 0 of the port at 0x50000C00 high through BSRR**

Writes 1 to the BSRR register at 0x50000C18 of the port based at 0x50000C00, which sets bit 0 atomically. It is the set half of gpio_pd0_reset. Callers bms_4168_080082f0 and bms_4168_0800e820.

**Notes:** Port identification (0x50000C00 as GPIOD) is inferred from the G0 layout, as in gpio_pd0_reset.

- Addresses by version: 4130: 0x0800818C, 4139: 0x0800868C, 4148: 0x08008ED8, 4168: 0x080091EC
- Called by: `bms_4168_080082f0`, `bms_pd0_indicator_step`
- Confidence: medium
