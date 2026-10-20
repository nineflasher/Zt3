# VCU - `dma` functions

12 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`dma_channel_enable`](#dma_channel_enable) | 0x0800C838 | Enable or disable a DMA channel (CTRL.CHEN, bit 0) |
| [`dma_data_number_get`](#dma_data_number_get) | 0x0800C842 | Read the remaining transfer count of a DMA channel (DTCNT) |
| [`dma_data_number_set`](#dma_data_number_set) | 0x0800C848 | Set the transfer count of a DMA channel (DTCNT) |
| [`dma_default_para_init`](#dma_default_para_init) | 0x0800C84C | Fill a dma_init_type structure with the SDK default DMA settings |
| [`dma_flag_clear`](#dma_flag_clear) | 0x0800C864 | Clear DMA interrupt/status flags (DMA1.CLR or DMA2.CLR) |
| [`dma_flag_get`](#dma_flag_get) | 0x0800C884 | Test a DMA status flag (DMA1.STS or DMA2.STS) |
| [`dma_init`](#dma_init) | 0x0800C8A8 | Configure a DMA channel from a dma_init_type structure |
| [`dma_reset`](#dma_reset) | 0x0800C904 | Reset a DMA channel registers and clear its flags |
| [`vcu_adc_dma_ring_init`](#vcu_adc_dma_ring_init) | 0x08001C3C | Set up DMA1 channel 1 as a circular ADC1 result buffer of 80 halfwords |
| [`vcu_dma_ring_drain`](#vcu_dma_ring_drain) | 0x08008C1C | Copy bytes received since the last call from a 250-byte DMA ring into a buffer |
| [`vcu_dma_tx_queue_service`](#vcu_dma_tx_queue_service) | 0x08005704 | Start the next queued DMA transmit record when DMA1 channel 7 is free |
| [`vcu_dma_tx_start`](#vcu_dma_tx_start) | 0x08005754 | Re-arm DMA1 channel 7 with a new memory address and count if the last transfer completed |

## dma_channel_enable

**Enable or disable a DMA channel (CTRL.CHEN, bit 0)**

AT32 SDK dma_channel_enable(): rewrites bit 0 of the channel control register pointed to by param_1 with (param_2 & 1), leaving other bits untouched. Called by the three DMA channel setup routines (vcu_0159_08001c3c, 08001f50, 08001fbc) and by 08005754 together with dma_reset/dma_init.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | dma_channel_type* (DMAx_CHANNELy base, its CTRL register is at offset 0) |
| `param_2` | `u32` | TRUE enables, FALSE disables |

- Addresses by version: 148: 0x0800B9AC, 14a: 0x0800BDF0, 14b: 0x0800C27C, 14e: 0x0800C310, 14f: 0x0800C44C, 152: 0x0800C6D8, 153: 0x0800C7CC, 0159: 0x0800C838
- Called by: `vcu_adc_dma_ring_init`, `vcu_usart2_rx_dma_init`, `vcu_usart2_tx_dma_init`, `vcu_dma_tx_start`
- Confidence: high

## dma_data_number_get

**Read the remaining transfer count of a DMA channel (DTCNT)**

AT32 SDK dma_data_number_get(): returns the 16-bit DTCNT register (offset +4) of the DMA channel at param_1. Used by vcu_0159_08008c1c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | dma_channel_type* |

**Returns** `u16`: remaining number of data items

- Addresses by version: 148: 0x0800B9B6, 14a: 0x0800BDFA, 14b: 0x0800C286, 14e: 0x0800C31A, 14f: 0x0800C456, 152: 0x0800C6E2, 153: 0x0800C7D6, 0159: 0x0800C842
- Called by: `vcu_dma_ring_drain`
- Confidence: high

## dma_data_number_set

**Set the transfer count of a DMA channel (DTCNT)**

AT32 SDK dma_data_number_set(): stores param_2 into DTCNT (offset +4) of the DMA channel at param_1. Called from 08005754 to restart a transfer; the channel should be disabled while it is written.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | dma_channel_type* |
| `param_2` | `u16` | number of data items to transfer |

- Addresses by version: 148: 0x0800B9BC, 14a: 0x0800BE00, 14b: 0x0800C28C, 14e: 0x0800C320, 14f: 0x0800C45C, 152: 0x0800C6E8, 153: 0x0800C7DC, 0159: 0x0800C848
- Called by: `vcu_dma_tx_start`
- Confidence: high

## dma_default_para_init

**Fill a dma_init_type structure with the SDK default DMA settings**

AT32 SDK dma_default_para_init(): zeroes the 0x14-byte dma_init_type: peripheral_base_addr (+0), memory_base_addr (+4), direction (+8, 0 = peripheral to memory), buffer_size (+0xa), peripheral_inc_enable (+0xc), memory_inc_enable (+0xd), peripheral_data_width (+0xe, byte), memory_data_width (+0xf, byte), loop_mode_enable (+0x10) and priority (+0x11, low). Called before dma_init by the three DMA setup routines vcu_0159_08001c3c, 08001f50 and 08001fbc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | dma_init_type* to initialise |

- Addresses by version: 148: 0x0800B9C0, 14a: 0x0800BE04, 14b: 0x0800C290, 14e: 0x0800C324, 14f: 0x0800C460, 152: 0x0800C6EC, 153: 0x0800C7E0, 0159: 0x0800C84C
- Called by: `vcu_adc_dma_ring_init`, `vcu_usart2_rx_dma_init`, `vcu_usart2_tx_dma_init`
- Confidence: high

## dma_flag_clear

**Clear DMA interrupt/status flags (DMA1.CLR or DMA2.CLR)**

AT32 SDK dma_flag_clear(): flag values above 0x10000000 identify DMA2 flags and are written, with the marker nibble stripped (& 0x0fffffff), to DMA2.CLR (0x40020404); otherwise the value is written straight to DMA1.CLR (0x40020004). Writing a 1 clears the corresponding global/full/half/error flag.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | DMAx_GLn/FDTn/HDTn/DTERRn_FLAG mask |

- Addresses by version: 148: 0x0800B9D8, 14a: 0x0800BE1C, 14b: 0x0800C2A8, 14e: 0x0800C33C, 14f: 0x0800C478, 152: 0x0800C704, 153: 0x0800C7F8, 0159: 0x0800C864
- Peripheral registers: `DMA1.CLR` (W), `DMA2.CLR` (W)
- Called by: `vcu_usart2_tx_dma_init`, `vcu_dma_tx_start`
- Confidence: high

## dma_flag_get

**Test a DMA status flag (DMA1.STS or DMA2.STS)**

AT32 SDK dma_flag_get(): chooses DMA1.STS when param_1 <= 0x10000000, else DMA2.STS, and returns whether any bit selected by param_1 is set. (The DMA2 flag masks contain a 0x10000000 marker bit that never matches real status bits, since it is only used for selection.)

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | DMAx_xxn_FLAG mask |

**Returns** `bool`: true if flag set

- Addresses by version: 148: 0x0800B9F8, 14a: 0x0800BE3C, 14b: 0x0800C2C8, 14e: 0x0800C35C, 14f: 0x0800C498, 152: 0x0800C724, 153: 0x0800C818, 0159: 0x0800C884
- Peripheral registers: `DMA1.STS` (R), `DMA2.STS` (R)
- Called by: `vcu_dma_tx_start`
- Confidence: high

## dma_init

**Configure a DMA channel from a dma_init_type structure**

AT32 SDK dma_init(): masks CTRL with 0xbfef (clears DTD and M2M), ORs in the direction, then inserts priority (CTRL[13:12]), memory width ([11:10]), peripheral width ([9:8]), memory increment (bit 7), peripheral increment (bit 6) and loop mode (bit 5), and loads DTCNT (+4), PADDR (+8) and MADDR (+0xc) from buffer_size, peripheral_base_addr and memory_base_addr. The channel is not enabled here; see dma_channel_enable. Called by vcu_0159_08001c3c, 08001f50 and 08001fbc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | dma_channel_type* to configure |
| `param_2` | `ptr` | dma_init_type* with the settings |

- Addresses by version: 148: 0x0800BA1C, 14a: 0x0800BE60, 14b: 0x0800C2EC, 14e: 0x0800C380, 14f: 0x0800C4BC, 152: 0x0800C748, 153: 0x0800C83C, 0159: 0x0800C8A8
- Called by: `vcu_adc_dma_ring_init`, `vcu_usart2_rx_dma_init`, `vcu_usart2_tx_dma_init`
- Confidence: high

## dma_reset

**Reset a DMA channel registers and clear its flags**

AT32 SDK dma_reset(): clears CTRL.CHEN, then zeroes CTRL, DTCNT, PADDR and MADDR, and ORs 0xF << (4 * channel_index) into DMA1.CLR (0x40020004) or DMA2.CLR (0x40020404) to clear that channel's four flags. The channel index is derived from the register address ((addr & 0xff) - 8) / 0x14 and the controller from (addr & 0x4ff) < 0x408 / < 0x488. Called by vcu_0159_08001c3c, 08001f50 and 08001fbc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | dma_channel_type* |

- Addresses by version: 148: 0x0800BA78, 14a: 0x0800BEBC, 14b: 0x0800C348, 14e: 0x0800C3DC, 14f: 0x0800C518, 152: 0x0800C7A4, 153: 0x0800C898, 0159: 0x0800C904
- Peripheral registers: `DMA1.CLR` (RW), `DMA2.CLR` (RW)
- Called by: `vcu_adc_dma_ring_init`, `vcu_usart2_rx_dma_init`, `vcu_usart2_tx_dma_init`
- Confidence: high

## vcu_adc_dma_ring_init

**Set up DMA1 channel 1 as a circular ADC1 result buffer of 80 halfwords**

Initialises DMA1 channel 1 to move ADC1 conversion results from the ADC1 data register (0x4001244C) into the RAM buffer at 0x200032A6 in circular mode. It enables the DMA1 clock (AHBEN bit 0), resets the channel, loads dma_default_para_init, and then sets peripheral-to-memory direction, a fixed peripheral address, memory increment, halfword widths on both sides, circular loop mode and medium priority, with buffer size 0x50 (16 scans of 5 channels). It calls dma_init and then dma_channel_enable(1), so the channel runs from this point.

**Notes:** The field values follow the dma_init_type offsets documented on the existing dma_default_para_init annotation.

- Addresses by version: 148: 0x08001858, 14a: 0x080018C0, 14b: 0x08001B74, 14e: 0x08001B74, 14f: 0x08001BD0, 152: 0x08001C0C, 153: 0x08001C28, 0159: 0x08001C3C
- Peripheral registers: `ADC1.ODT` (A), `DMA1.C1CTRL` (A)
- Called by: `vcu_adc1_scan_init`
- Calls: `crm_periph_clock_enable`, `dma_channel_enable`, `dma_default_para_init`, `dma_init`, `dma_reset`
- Confidence: high

## vcu_dma_ring_drain

**Copy bytes received since the last call from a 250-byte DMA ring into a buffer**

Given a DMA channel handle (param_2) and a ring index (param_3, 0 or 1), the bytes written so far are 250 minus the remaining count from dma_data_number_get. Each new byte is copied from the ring at 0x20002eb4 + index*0xfa to the caller's buffer, advancing the per-ring read index (u16 at 0x200018b8 + index*2) and wrapping after 249. The function returns the number of bytes copied; a write position of 250 (counter at zero) is treated as no new data, as is a read index already equal to the write position.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination buffer; needs room for up to 249 bytes |
| `param_2` | `ptr` | DMA channel handle passed to dma_data_number_get |
| `param_3` | `s32` | ring index, 0 or 1 |

**Returns** `u16`: bytes copied, 0..249

**Notes:** The 250-byte ring size and the two-ring layout come from the constants in the decompile. The 250 to 0 quirk means a counter that has just reloaded is not drained on that call.

- Addresses by version: 148: 0x080081E8, 14a: 0x08008644, 14b: 0x080089BC, 14e: 0x080089FC, 14f: 0x08008A58, 152: 0x08008B1C, 153: 0x08008BB8, 0159: 0x08008C1C
- Called by: `vcu_0159_08008a44`
- Calls: `dma_data_number_get`
- Confidence: medium

## vcu_dma_tx_queue_service

**Start the next queued DMA transmit record when DMA1 channel 7 is free**

Service function for an 8-slot transmit queue of 256-byte records. Read index DAT_20000008 wraps at 8, and write index DAT_20000009 is set elsewhere. If the queue is not empty and neither the hold flag DAT_2000000b nor the re-entry guard DAT_2000000c is set, it sets the guard, calls vcu_dma_tx_start with the data at 0x20000014 + 256 * read index and its 16-bit length at 0x20000010 + 256 * read index, and on success advances the read index and counts sent records in DAT_2000000a. The guard is cleared at the end, so a record that could not be started stays queued and is retried on the next call.

**Notes:** Callers are not in this packet. The queue layout is read from the code and no names for it exist in wave 1.

- Addresses by version: 148: 0x08004DDC, 14a: 0x0800516C, 14b: 0x08005494, 14e: 0x080054CC, 14f: 0x08005528, 152: 0x08005588, 153: 0x080055A0, 0159: 0x08005704
- Called by: `vcu_0159_0800d858`
- Calls: `vcu_dma_tx_start`
- Confidence: high

## vcu_dma_tx_start

**Re-arm DMA1 channel 7 with a new memory address and count if the last transfer completed**

Starts a transfer on DMA1 channel 7 (registers at 0x40020080). It returns 0 without doing anything while the busy flag DAT_200018a4 is set and the transfer-complete flag for channel 7 (0x02000000 in the DMA1 status register, read through dma_flag_get) is still clear. Otherwise it sets the busy flag, clears the flag with dma_flag_clear, disables the channel with dma_channel_enable(0), writes the memory address to C7MADDR (0x4002008C), loads the transfer count with dma_data_number_set and enables the channel again. It returns 1 once the channel is re-armed.

| Parameter | Type | Description |
|---|---|---|
| `buffer_addr` | `u32` | memory address written to DMA1 channel 7 MADDR |
| `count` | `u16` | transfer count loaded into DTCNT |

**Returns** `u32`: 1 when the channel was started, 0 when the previous transfer is still running

**Notes:** The peripheral address and transfer direction are set elsewhere, not in this function.

- Addresses by version: 148: 0x08004E2C, 14a: 0x080051BC, 14b: 0x080054E4, 14e: 0x0800551C, 14f: 0x08005578, 152: 0x080055D8, 153: 0x080055F0, 0159: 0x08005754
- Peripheral registers: `DMA1.C7CTRL` (A), `DMA1.C7MADDR` (W)
- Called by: `vcu_dma_tx_queue_service`
- Calls: `dma_channel_enable`, `dma_data_number_set`, `dma_flag_clear`, `dma_flag_get`
- Confidence: high
