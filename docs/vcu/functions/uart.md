# VCU - `uart` functions

13 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`uart_rx_ring0_count`](#uart_rx_ring0_count) | 0x08007C70 | Number of unread entries in the 32-slot receive ring 0 |
| [`uart_rx_ring1_count`](#uart_rx_ring1_count) | 0x08007C8C | Number of unread entries in the 32-slot receive ring 1 |
| [`usart_data_receive`](#usart_data_receive) | 0x0800EFA4 | Read the USART data register (SDK usart_data_receive) |
| [`usart_dma_receiver_enable`](#usart_dma_receiver_enable) | 0x0800EFAA | Enable or disable USART DMA receive request (CTRL3.DMAREN) |
| [`usart_dma_transmitter_enable`](#usart_dma_transmitter_enable) | 0x0800EFB4 | Enable or disable USART DMA transmit request (CTRL3.DMATEN) |
| [`usart_flag_get`](#usart_flag_get) | 0x0800EFC8 | Test whether any given USART STS flag is set (SDK usart_flag_get) |
| [`usart_receiver_enable`](#usart_receiver_enable) | 0x0800F03C | Enable or disable the USART receiver (CTRL1.REN) |
| [`usart_transmitter_enable`](#usart_transmitter_enable) | 0x0800F046 | Enable or disable the USART transmitter (CTRL1.TEN) |
| [`vcu_rx_ring0_pop_record`](#vcu_rx_ring0_pop_record) | 0x08007B58 | Pop one 20-byte record from receive ring 0 into a caller buffer |
| [`vcu_rx_ring0_push_record`](#vcu_rx_ring0_push_record) | 0x08007BB0 | Push one 20-byte record into receive ring 0 if it is not full |
| [`vcu_usart2_pins_init`](#vcu_usart2_pins_init) | 0x08001E7C | Configure PA2 and PA3 as USART2 TX and RX pins |
| [`vcu_usart2_rx_dma_init`](#vcu_usart2_rx_dma_init) | 0x08001F50 | Set up DMA1 channel 6 as the USART2 receive DMA into a 250-byte circular buffer |
| [`vcu_usart2_tx_dma_init`](#vcu_usart2_tx_dma_init) | 0x08001FBC | Set up DMA1 channel 7 as the USART2 transmit DMA from RAM, left disabled |

## uart_rx_ring0_count

**Number of unread entries in the 32-slot receive ring 0**

Computes the fill level of a 32-entry ring buffer: head (DAT_20002c2c, advanced by the producer) minus tail (DAT_20002c30, advanced by the consumer), adding 0x20 when head is behind tail (wrap-around), masked to 16 bits. Result is 0..31. Sibling of the second ring count routine at 0x08007c8c (same code, different head/tail words); both are polled by the communication service routines that drain the rings.

**Returns** `u16`: pending entries, 0..31

**Notes:** That the ring is a UART RX ring is inferred from the layout/size and from the caller (0x08007ad4); the producer is not in this packet.

- Addresses by version: 148: 0x08007244, 14a: 0x08007680, 14b: 0x080079E4, 14e: 0x08007A1C, 14f: 0x08007A78, 152: 0x08007B3C, 153: 0x08007BD8, 0159: 0x08007C70
- Called by: `vcu_0159_08007ad4`
- Confidence: medium

## uart_rx_ring1_count

**Number of unread entries in the 32-slot receive ring 1**

Identical algorithm to uart_rx_ring0_count but on the second ring: head DAT_200029a4 minus tail DAT_200029a8, plus 0x20 when head < tail, masked to 16 bits (0..31). Used by the caller 0x08007b08 to decide whether bytes are waiting to be parsed. Together with uart_rx_ring0_count it forms a pair of per-link RX ring helpers.

**Returns** `u16`: pending entries, 0..31

**Notes:** Ring ownership (which UART/link) not visible here.

- Addresses by version: 148: 0x08007260, 14a: 0x0800769C, 14b: 0x08007A00, 14e: 0x08007A38, 14f: 0x08007A94, 152: 0x08007B58, 153: 0x08007BF4, 0159: 0x08007C8C
- Called by: `vcu_can_tx_pump`
- Confidence: medium

## usart_data_receive

**Read the USART data register (SDK usart_data_receive)**

Matches the Artery SDK usart_data_receive: returns the low 16 bits of the DT register (offset 0x4); reading it also clears RDBF and error flags per the hardware sequence. Called from vcu_0159_08008c98, the USART RX interrupt handler (together with usart_flag_get).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | USART peripheral base (usart_type*) |

**Returns** `u16`: received data (9-bit max, normally a byte)

- Addresses by version: 148: 0x0800DF80, 14a: 0x0800E41C, 14b: 0x0800E8AC, 14e: 0x0800E94C, 14f: 0x0800EA98, 152: 0x0800ED40, 153: 0x0800EE34, 0159: 0x0800EFA4
- Called by: `USART2_IRQHandler`
- Confidence: high

## usart_dma_receiver_enable

**Enable or disable USART DMA receive request (CTRL3.DMAREN)**

Matches the Artery SDK usart_dma_receiver_enable: writes (param_2 & 1) to bit 6 of CTRL3 (offset 0x14). Called with usart_dma_transmitter_enable, usart_transmitter_enable and usart_receiver_enable from vcu_0159_08001ee8, the USART initialisation; the group is the SDK usart driver.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | USART peripheral base (usart_type*) |
| `param_2` | `u32` | 1 = enable, 0 = disable |

- Addresses by version: 148: 0x0800DF86, 14a: 0x0800E422, 14b: 0x0800E8B2, 14e: 0x0800E952, 14f: 0x0800EA9E, 152: 0x0800ED46, 153: 0x0800EE3A, 0159: 0x0800EFAA
- Called by: `vcu_0159_08001ee8`
- Confidence: high

## usart_dma_transmitter_enable

**Enable or disable USART DMA transmit request (CTRL3.DMATEN)**

Matches the Artery SDK usart_dma_transmitter_enable: writes (param_2 & 1) to bit 7 of CTRL3 (offset 0x14). Called from the USART initialisation vcu_0159_08001ee8, alongside usart_dma_receiver_enable.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | USART peripheral base (usart_type*) |
| `param_2` | `u32` | 1 = enable, 0 = disable |

- Addresses by version: 148: 0x0800DF90, 14a: 0x0800E42C, 14b: 0x0800E8BC, 14e: 0x0800E95C, 14f: 0x0800EAA8, 152: 0x0800ED50, 153: 0x0800EE44, 0159: 0x0800EFB4
- Called by: `vcu_0159_08001ee8`
- Confidence: high

## usart_flag_get

**Test whether any given USART STS flag is set (SDK usart_flag_get)**

Matches the Artery SDK usart_flag_get: returns 1 if (USART->sts & flag) is non-zero, else 0; the STS register is at offset 0. Called from the USART RX interrupt handler vcu_0159_08008c98 to check flags such as RDBF/IDLEF/ROERR before reading data with usart_data_receive.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | USART peripheral base (usart_type*) |
| `param_2` | `u32` | flag mask (USART_*_FLAG) |

**Returns** `u32`: 1 if set, 0 otherwise (flag_status)

- Addresses by version: 148: 0x0800DFA4, 14a: 0x0800E440, 14b: 0x0800E8D0, 14e: 0x0800E970, 14f: 0x0800EABC, 152: 0x0800ED64, 153: 0x0800EE58, 0159: 0x0800EFC8
- Called by: `USART2_IRQHandler`
- Confidence: high

## usart_receiver_enable

**Enable or disable the USART receiver (CTRL1.REN)**

Matches the Artery SDK usart_receiver_enable: writes (param_2 & 1) to bit 2 (REN) of CTRL1 (offset 0xC). Called from the USART init vcu_0159_08001ee8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | USART peripheral base (usart_type*) |
| `param_2` | `u32` | 1 = enable, 0 = disable |

- Addresses by version: 148: 0x0800E018, 14a: 0x0800E4B4, 14b: 0x0800E944, 14e: 0x0800E9E4, 14f: 0x0800EB30, 152: 0x0800EDD8, 153: 0x0800EECC, 0159: 0x0800F03C
- Called by: `vcu_0159_08001ee8`
- Confidence: high

## usart_transmitter_enable

**Enable or disable the USART transmitter (CTRL1.TEN)**

Matches the Artery SDK usart_transmitter_enable: writes (param_2 & 1) to bit 3 (TEN) of CTRL1 (offset 0xC). Called from the USART init vcu_0159_08001ee8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | USART peripheral base (usart_type*) |
| `param_2` | `u32` | 1 = enable, 0 = disable |

- Addresses by version: 148: 0x0800E022, 14a: 0x0800E4BE, 14b: 0x0800E94E, 14e: 0x0800E9EE, 14f: 0x0800EB3A, 152: 0x0800EDE2, 153: 0x0800EED6, 0159: 0x0800F046
- Called by: `vcu_0159_08001ee8`
- Confidence: high

## vcu_rx_ring0_pop_record

**Pop one 20-byte record from receive ring 0 into a caller buffer**

If receive ring 0 is not empty (DAT_20002c30 differs from DAT_20002c2c), it copies the 20-byte record at 0x20002C34 + 20 * tail into the buffer argument and advances the tail DAT_20002c30 modulo 32. An empty ring is left alone. The producer is vcu_rx_ring0_push_record.

| Parameter | Type | Description |
|---|---|---|
| `dst` | `ptr` | destination buffer of 20 bytes |

- Addresses by version: 148: 0x0800712C, 14a: 0x08007568, 14b: 0x080078CC, 14e: 0x08007904, 14f: 0x08007960, 152: 0x08007A24, 153: 0x08007AC0, 0159: 0x08007B58
- Called by: `vcu_0159_08007ad4`
- Calls: `__aeabi_memcpy`
- Confidence: high

## vcu_rx_ring0_push_record

**Push one 20-byte record into receive ring 0 if it is not full**

When ring 0 is not full (tail DAT_20002c30 differs from head + 1 modulo 32), it copies 20 bytes from the argument into the slot at 0x20002C34 + 20 * head (head DAT_20002c2c) and advances the head modulo 32. A full ring drops the record without any report. The consumer is vcu_rx_ring0_pop_record.

| Parameter | Type | Description |
|---|---|---|
| `src` | `ptr` | source record of 20 bytes |

**Notes:** Caller vcu_0159_08002904 is outside this packet.

- Addresses by version: 148: 0x08007184, 14a: 0x080075C0, 14b: 0x08007924, 14e: 0x0800795C, 14f: 0x080079B8, 152: 0x08007A7C, 153: 0x08007B18, 0159: 0x08007BB0
- Called by: `CAN1_RX0_IRQHandler`
- Calls: `__aeabi_memcpy`
- Confidence: high

## vcu_usart2_pins_init

**Configure PA2 and PA3 as USART2 TX and RX pins**

Enables the GPIOA clock and configures PA2 (pin mask 0x4) with packed word 0x01080400 and PA3 (mask 0x8) with packed word 0x01001804 through gpio_default_para_init and gpio_init. PA3 gets a pull-up setting (0x18) and PA2 none. These are the standard USART2 pins, and the DMA setup in vcu_0159_08001f50 and vcu_0159_08001fbc targets the USART2 data register at 0x40004404. The mapping is inferred from the pins and their use, not from a name in the code. It is called from vcu_0159_08001ee8.

**Notes:** PA3 is also configured as EXINT line 3 in vcu_0159_080026f0 (vcu_exint3_pa3_init). The two have different callers, so they are presumably not used together.

- Addresses by version: 148: 0x08001A98, 14a: 0x08001B00, 14b: 0x08001DB4, 14e: 0x08001DB4, 14f: 0x08001E10, 152: 0x08001E4C, 153: 0x08001E68, 0159: 0x08001E7C
- Peripheral registers: `GPIOA.CFGLR` (A)
- Called by: `vcu_0159_08001ee8`
- Calls: `crm_periph_clock_enable`, `gpio_default_para_init`, `gpio_init`
- Confidence: medium

## vcu_usart2_rx_dma_init

**Set up DMA1 channel 6 as the USART2 receive DMA into a 250-byte circular buffer**

Configures DMA1 channel 6 (control block 0x4002006C) to receive from USART2.DT (0x40004404) into the 250-byte RAM buffer at 0x20002EB4. It enables the DMA1 clock, resets the channel, and sets peripheral-to-memory direction, a fixed peripheral address, memory increment, byte widths, circular loop mode and high priority, with buffer size 0xFA. It calls dma_init and then dma_channel_enable(1). This is the receive half of the USART2 DMA pair with vcu_0159_08001fbc.

**Notes:** Channel 6 as USART2 RX follows the usual DMA1 request map; it was not checked against the SVD.

- Addresses by version: 148: 0x08001B6C, 14a: 0x08001BD4, 14b: 0x08001E88, 14e: 0x08001E88, 14f: 0x08001EE4, 152: 0x08001F20, 153: 0x08001F3C, 0159: 0x08001F50
- Peripheral registers: `USART2.DT` (A), `DMA1.C6CTRL` (A)
- Called by: `vcu_0159_08001ee8`
- Calls: `crm_periph_clock_enable`, `dma_channel_enable`, `dma_default_para_init`, `dma_init`, `dma_reset`
- Confidence: medium

## vcu_usart2_tx_dma_init

**Set up DMA1 channel 7 as the USART2 transmit DMA from RAM, left disabled**

Configures DMA1 channel 7 (control block 0x40020080) for memory-to-peripheral transfers to USART2.DT (0x40004404), with the source buffer at 0x200030A8. The buffer size is set to 0 here and must be written before each transmit. It uses normal (non-circular) mode, memory increment, byte widths and high priority. It clears the channel 7 transfer-complete flag (0x02000000), then calls dma_channel_enable with 0, so the channel stays disabled until a transmit sets its count and enables it.

**Notes:** Channel 7 as USART2 TX follows the usual DMA1 request map. The flag value is the channel 7 transfer-complete bit in the DMA flag map.

- Addresses by version: 148: 0x08001BD8, 14a: 0x08001C40, 14b: 0x08001EF4, 14e: 0x08001EF4, 14f: 0x08001F50, 152: 0x08001F8C, 153: 0x08001FA8, 0159: 0x08001FBC
- Peripheral registers: `USART2.DT` (A), `DMA1.C7CTRL` (A)
- Called by: `vcu_0159_08001ee8`
- Calls: `crm_periph_clock_enable`, `dma_channel_enable`, `dma_default_para_init`, `dma_flag_clear`, `dma_init`, `dma_reset`
- Confidence: medium
