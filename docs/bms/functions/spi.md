# BMS - `spi` functions

4 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`LL_SPI_Disable`](#ll_spi_disable) | 0x0800A0BC | Clear SPI1_CR1.SPE to disable SPI1 |
| [`LL_SPI_Init`](#ll_spi_init) | 0x08002DF4 | Configures an SPI instance from a 10-word init record, only while SPE is clear |
| [`bms_spi1_master_init`](#bms_spi1_master_init) | 0x0800A000 | Enable GPIOB and SPI1 clocks, set PB3-PB5 to AF0, configure SPI1 master mode 0 |
| [`bms_spi1_transfer_byte`](#bms_spi1_transfer_byte) | 0x0800A0CC | Send one byte on SPI1 and return the received byte, with bounded polling waits |

## LL_SPI_Disable

**Clear SPI1_CR1.SPE to disable SPI1**

Clears bit 6 (SPE) of SPI1_CR1 (SPI1 base 0x40013000) with a read-modify-write, disabling the peripheral. This is the ST LL_SPI_Disable operation (CLEAR_BIT on SPI_CR1_SPE) and the code matches it exactly. The routine does not wait for TXE or BSY first, so the caller must have finished the transfer. Its caller in the packet is bms_4168_080082f0.

- Addresses by version: 4130: 0x0800905C, 4139: 0x0800955C, 4148: 0x08009DA8, 4168: 0x0800A0BC
- Peripheral registers: `SPI1.SPI_CR1` (ARW)
- Called by: `bms_4168_080082f0`
- Confidence: high

## LL_SPI_Init

**Configures an SPI instance from a 10-word init record, only while SPE is clear**

Writes an SPI configuration from an LL_SPI_InitTypeDef-style record of 10 words, only when CR1.SPE (bit 6) is clear; if SPI is enabled it returns 1 and writes nothing. CR1 receives init[0], init[1] and init[3] to init[8] ORed in, while the SPE bit and the upper half are kept. CR2 receives the data width from init[2] (which also sets FRXTH when the value is below 0x800, i.e. narrow data) and the NSS output bit from init[5] >> 16 (SSOE). If CRCCalculation (init[8]) is 0x2000, the CRC polynomial init[9] is written to CRCPR. I2SMOD (I2SCFGR bit 11) is cleared so the peripheral runs in SPI mode. It returns 0 on success.

| Parameter | Type | Description |
|---|---|---|
| `SPIx` | `ptr` | SPI instance (SPI_TypeDef pointer) |
| `init` | `ptr` | 10-word LL_SPI_InitTypeDef-style record |

**Returns** `u32`: 0 = SUCCESS; 1 = ERROR (SPI enabled, nothing written)

- Addresses by version: 4130: 0x08002DF4, 4139: 0x08002DF4, 4148: 0x08002DF4, 4168: 0x08002DF4
- Called by: `bms_spi1_master_init`
- Confidence: high

## bms_spi1_master_init

**Enable GPIOB and SPI1 clocks, set PB3-PB5 to AF0, configure SPI1 master mode 0**

Brings up SPI1 as bus master. It enables the GPIOB clock in RCC.IOPENR and reads the register back as a clock-enable delay. It then configures PB3, PB4 and PB5 with LL_GPIO_Init as alternate-function 0 pins (SPI1 SCK, MISO and MOSI), high speed, push-pull, no pull. It sets the SPI1 clock in RCC.APBENR2 and calls LL_SPI_Init with master mode (0x104), 8-bit data (0x700), CPOL 0 and CPHA 0, software NSS (0x200), baud divider DIV2, MSB first, CRC disabled and CRC polynomial 7. It finally clears SPI_CR2 bit 4, sets SPI_CR2 bit 3, and sets SPI_CR1 bit 6 (SPE) to enable the peripheral.

**Notes:** The meaning of the two raw SPI_CR2 bit writes is not confirmed against the SVD. The LL_SPI_InitTypeDef field values are decoded from the stack block.

- Addresses by version: 4130: 0x08008FA0, 4139: 0x080094A0, 4148: 0x08009CEC, 4168: 0x0800A000
- Peripheral registers: `SPI1.SPI_CR1` (ARW), `SPI1.SPI_CR2` (RW), `RCC.IOPENR` (RW), `RCC.APBENR2` (RW)
- Called by: `bms_4168_08008294`, `bms_4168_080082f0`
- Calls: `LL_GPIO_Init`, `LL_SPI_Init`
- Confidence: high

## bms_spi1_transfer_byte

**Send one byte on SPI1 and return the received byte, with bounded polling waits**

Blocking one-byte full-duplex transfer on SPI1. The first loop polls SPI1_SR.TXE (bit 1) and uses param_2 as its counter, giving up when the counter reaches 10000. The byte is then written to SPI1_DR (0x4001300C). The routine waits for BSY (SR bit 7) to clear and then for RXNE (SR bit 0) to set, each bounded by 10000 iterations, and returns the byte read from SPI1_DR. None of the waits report a timeout, so a stuck bus returns whatever DR holds. It has seven callers in the 0x0800BAA0..0x0800BD88 range, which suggests a register-access helper for an external device such as an AFE (inferred).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | byte to transmit |
| `param_2` | `u16` | starting value of the TXE wait counter; pass 0 for a full wait, since a value of 10000 or more skips the TXE wait |

**Returns** `u8`: byte read from SPI1_DR (the received byte, or a stale value on timeout)

**Notes:** Callers: bms_4168_0800baa0, bms_4168_0800baec, bms_4168_0800bb3c, bms_4168_0800bb88, bms_4168_0800bbc4, bms_4168_0800bc20, bms_4168_0800bd88. The reuse of param_2 as the loop counter is how the decompiler shows it; check whether the caller really relies on that starting value.

- Addresses by version: 4130: 0x0800906C, 4139: 0x0800956C, 4148: 0x08009DB8, 4168: 0x0800A0CC
- Peripheral registers: `SPI1.SPI_SR` (R), `SPI1.SPI_DR` (RW)
- Called by: `bms_extflash_sector_erase`, `bms_extflash_wip_poll`, `bms_extflash_read`, `bms_extflash_read_device_id`, `bms_extflash_wait_ready`, `bms_4168_0800bc20`, `bms_extflash_page_program`
- Confidence: high
