# MCU - `dma` functions

7 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`dma_channel_enable`](#dma_channel_enable) | 0x0800C918 | Enable or disable a DMA channel by writing its CCTRL.CHEN bit |
| [`dma_data_number_get`](#dma_data_number_get) | 0x0800C922 | Read the DMA channel's data-number (DTCNT) register, low 16 bits |
| [`dma_default_para_init`](#dma_default_para_init) | 0x0800C928 | Zero an 18-byte DMA init struct to the SDK default values |
| [`dma_init`](#dma_init) | 0x0800C9D4 | Load a DMA channel's control, count and address registers from a dma_init_type record |
| [`dma_reset`](#dma_reset) | 0x0800CA30 | Disable a DMA channel, zero its registers and clear its flags in DMA1.CLR or DMA2.CLR |
| [`mcu_adc1_dma_init`](#mcu_adc1_dma_init) | 0x08001F34 | Starts DMA1 channel 1 as a circular ADC1 ordinary-data to RAM ring transfer |
| [`mcu_dma_channel_start`](#mcu_dma_channel_start) | 0x0800ABDA | Configure and start one DMA channel, then store one context byte |

## dma_channel_enable

**Enable or disable a DMA channel by writing its CCTRL.CHEN bit**

Sets bit 0 (CHEN) of the channel control register, which is the first word of the DMA channel block, to bit 0 of the argument. Matches the SDK dma_channel_enable. Called on the DMA1 channel 1 block at 0x40020008 in other MCU packets. It is part of the DMA group with mcu_0160_0800c922 and mcu_0160_0800c928.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DMA channel block base (CCTRL at offset 0) |
| `param_2` | `u32` | bit 0: 1 = enable, 0 = disable |

- Addresses by version: 12b: 0x0800C620, 143: 0x0800C878, 152: 0x0800C8B8, 0160: 0x0800C918
- Called by: `mcu_adc1_dma_init`, `mcu_dma_channel_start`
- Confidence: high

## dma_data_number_get

**Read the DMA channel's data-number (DTCNT) register, low 16 bits**

Returns the low 16 bits of the channel data-number register at offset 0x04 (DTCNT), which is the number of transfers still to be done. Matches the SDK dma_data_number_get. Called on the DMA1 channel 1 block at 0x40020008 in other MCU packets. DMA group: see mcu_0160_0800c918.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DMA channel block base |

**Returns** `u16`: remaining transfer count

- Addresses by version: 12b: 0x0800C62A, 143: 0x0800C882, 152: 0x0800C8C2, 0160: 0x0800C922
- Called by: `mcu_adc_dma_median5`
- Confidence: high

## dma_default_para_init

**Zero an 18-byte DMA init struct to the SDK default values**

Clears the 18-byte dma_init_type (offsets 0x00..0x11): peripheral and memory base addresses, direction (peripheral to memory), buffer size, peripheral and memory increment enables, data widths (byte), loop mode and priority (low). All of those defaults are zero, so the routine is a zero-fill. Matches the SDK dma_default_para_init. DMA group: see mcu_0160_0800c918. Callers: mcu_0160_08001f34, mcu_0160_0800abda.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DMA init struct to clear (18 bytes) |

- Addresses by version: 12b: 0x0800C630, 143: 0x0800C888, 152: 0x0800C8C8, 0160: 0x0800C928
- Called by: `mcu_adc1_dma_init`, `mcu_dma_channel_start`
- Confidence: high

## dma_init

**Load a DMA channel's control, count and address registers from a dma_init_type record**

SDK dma_init. It clears the DTD (bit 4) and M2M (bit 14) bits of CTRL with mask 0xBFEF and ORs in the direction halfword at record+8. It then writes the channel priority (bits 12-13, from record byte +0x11), memory width (bits 10-11, byte +0x0F), peripheral width (bits 8-9, byte +0x0E), memory increment (bit 7, byte +0x0D), peripheral increment (bit 6, byte +0x0C) and loop/circular mode (bit 5, byte +0x10). The transfer count is the halfword at record+0x0A, the peripheral address is the word at +0x00 and the memory address the word at +0x04. The channel is not enabled here.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DMA channel register block: CTRL at +0, DTCNT at +4, PADDR at +8, MADDR at +12 |
| `param_2` | `ptr` | dma_init_type record: peripheral address +0, memory address +4, direction +8, count +0x0A, see description for the byte fields |

- Addresses by version: 12b: 0x0800C6DC, 143: 0x0800C934, 152: 0x0800C974, 0160: 0x0800C9D4
- Called by: `mcu_adc1_dma_init`, `mcu_dma_channel_start`
- Confidence: high

## dma_reset

**Disable a DMA channel, zero its registers and clear its flags in DMA1.CLR or DMA2.CLR**

SDK dma_reset. It clears CTRL bit 0 (channel enable), then zeroes CTRL, DTCNT, PADDR and MADDR. The channel number is derived from the low byte of the channel block address as ((addr - 8) / 0x14) masked to 6 bits, and a 4-bit group for that channel is cleared through DMA1.CLR (0x40020004) for channels in the DMA1 address range, or DMA2.CLR (0x40020404) for the DMA2 range. Because the index comes from the address, the argument must be the real channel register block.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DMA channel register block (CTRL, DTCNT, PADDR, MADDR) |

- Addresses by version: 12b: 0x0800C738, 143: 0x0800C990, 152: 0x0800C9D0, 0160: 0x0800CA30
- Peripheral registers: `DMA1.CLR` (RW), `DMA2.CLR` (RW)
- Called by: `mcu_adc1_dma_init`, `mcu_dma_channel_start`
- Confidence: high

## mcu_adc1_dma_init

**Starts DMA1 channel 1 as a circular ADC1 ordinary-data to RAM ring transfer**

Enables a peripheral clock (crm_periph_clock_enable with ID 0x00140000), resets DMA1 channel 1 (dma_reset on base 0x40020008) and loads the SDK defaults into a dma_init_type record (dma_default_para_init). The record is filled as: peripheral address 0x4001244C (ADC1 ordinary data register ODT), memory address 0x20000FB4, peripheral to memory, 200 halfwords, peripheral increment off, memory increment on, half-word widths on both sides, circular loop mode, priority 2. The channel is then configured with dma_init and enabled with dma_channel_enable. The ring at 0x20000FB4 holds 40 scans of 5 ADC results each, which mcu_0160_0800249c reads back.

**Notes:** Field meanings of dma_init_type follow the SDK layout as inferred from the stack writes. The clock ID 0x00140000 is an SDK encoding whose target peripheral is not confirmed. A call mcu_ctx_cfg_byte_set(&DMA1, 1) sits between the DMA setup calls. Its argument is the DMA1 register window (0x40020000), but mcu_ctx_cfg_byte_set writes at +0xA0 and +0xA4 of its first argument, so this call looks misidentified and should be checked against the disassembly.

- Addresses by version: 12b: 0x08001F58, 143: 0x08001F94, 152: 0x08001F18, 0160: 0x08001F34
- Peripheral registers: `ADC1.ODT` (A), `DMA1.STS` (A), `DMA1.C1CTRL` (A)
- Called by: `mcu_0160_08002068`
- Calls: `crm_periph_clock_enable`, `dma_channel_enable`, `dma_default_para_init`, `mcu_ctx_cfg_byte_set`, `dma_init`, `dma_reset`
- Confidence: medium

## mcu_dma_channel_start

**Configure and start one DMA channel, then store one context byte**

Sets up and starts a DMA channel. It enables the DMA controller clock (crm_periph_clock_enable with the packed code in param_2), resets the channel (dma_reset), and fills a dma_init_type record that dma_default_para_init has set to defaults: peripheral address = param_1 + 4, memory address = param_4, param_8 as a halfword field (most likely the transfer count), a halfword 0x00FA and several byte flags set to fixed values. It calls dma_init, stores one context byte with mcu_ctx_cfg_byte_set (param_5 context, param_6 index, param_7 value), and enables the channel with dma_channel_enable.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object whose address + 4 is used as the DMA peripheral address |
| `param_2` | `u32` | packed DMA clock code for crm_periph_clock_enable |
| `param_3` | `ptr` | DMA channel register block |
| `param_4` | `u32` | memory (buffer) address |
| `param_5` | `ptr` | context struct for mcu_ctx_cfg_byte_set |
| `param_6` | `u32` | context field index, 1..7 |
| `param_7` | `u32` | value; only the low byte is stored |
| `param_8` | `u16` | transfer count, stored as a halfword in the init record |

**Notes:** Transfer direction and width flags are the record's fixed values; the exact enum values are not decoded here.

- Addresses by version: 12b: 0x0800AA82, 143: 0x0800ACAA, 152: 0x0800AB66, 0160: 0x0800ABDA
- Called by: `mcu_0160_0800a9dc`
- Calls: `crm_periph_clock_enable`, `dma_channel_enable`, `dma_default_para_init`, `mcu_ctx_cfg_byte_set`, `dma_init`, `dma_reset`
- Confidence: medium
