# BMS - `flash` functions

8 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`HAL_FLASH_Lock`](#hal_flash_lock) | 0x08001E74 | Sets FLASH.CR.LOCK and returns 1 if the bit still reads 0 afterwards |
| [`HAL_FLASH_Unlock`](#hal_flash_unlock) | 0x08001F24 | Unlocks FLASH.CR with the KEY1/KEY2 sequence and returns 1 if it stays locked |
| [`bms_extflash_page_program`](#bms_extflash_page_program) | 0x0800BD88 | Program N bytes into external flash with WREN and command 0x02, split at 256-byte boundaries |
| [`bms_extflash_read`](#bms_extflash_read) | 0x0800BB3C | Read N bytes from external SPI flash at a 24-bit address using command 0x03 |
| [`bms_extflash_read_device_id`](#bms_extflash_read_device_id) | 0x0800BB88 | Read the manufacturer and device ID with command 0x90 and return them as a u16 |
| [`bms_extflash_sector_erase`](#bms_extflash_sector_erase) | 0x0800BAA0 | Erase one 4 KB external flash sector with 0x20 after WREN and a ready wait |
| [`bms_extflash_wait_ready`](#bms_extflash_wait_ready) | 0x0800BBC4 | Poll external flash status (0x05) until WIP clears, bounded by the 16-bit word at 0x2000067C |
| [`bms_extflash_wip_poll`](#bms_extflash_wip_poll) | 0x0800BAEC | Read the external flash status once; return 1 while a write is still in progress |

## HAL_FLASH_Lock

**Sets FLASH.CR.LOCK and returns 1 if the bit still reads 0 afterwards**

Sets bit 31 (LOCK) of FLASH.CR at 0x40022014 by read-modify-write, reads the register back, and returns 1 when LOCK reads 0, meaning the lock did not take. It returns 0 when the bit reads back set. It does not wait on the flash busy flag. Because 1 means failure here, the return value is the reverse of the HAL_OK convention.

**Returns** `bool`: 1 when LOCK still reads 0 (failure), 0 when locked

**Notes:** Name follows ST HAL_FLASH_Lock. The return sense is inverted compared with the HAL status return, so callers must be checked before reusing it.

- Addresses by version: 4130: 0x08001E74, 4139: 0x08001E74, 4148: 0x08001E74, 4168: 0x08001E74
- Peripheral registers: `FLASH.CR` (RW)
- Called by: `bms_4168_08008788`
- Confidence: medium

## HAL_FLASH_Unlock

**Unlocks FLASH.CR with the KEY1/KEY2 sequence and returns 1 if it stays locked**

If FLASH.CR.LOCK (bit 31) is set, writes KEY1 0x45670123 and then KEY2 0xCDEF89AB to FLASH.KEYR at 0x40022008. It then reads CR back and returns 1 when LOCK is still set (failure) and 0 otherwise. When the flash is already unlocked it writes nothing and returns 0. There is no timeout loop.

**Returns** `u32`: 0 on success (unlocked), 1 if still locked

**Notes:** Name follows the ST HAL routine from its behaviour.

- Addresses by version: 4130: 0x08001F24, 4139: 0x08001F24, 4148: 0x08001F24, 4168: 0x08001F24
- Peripheral registers: `FLASH.KEYR` (W), `FLASH.CR` (R)
- Called by: `bms_4168_08008788`
- Confidence: high

## bms_extflash_page_program

**Program N bytes into external flash with WREN and command 0x02, split at 256-byte boundaries**

Writes param_3 bytes from the RAM buffer param_1 to external flash at address param_2. Each piece is the smaller of the remaining length and the distance to the next 256-byte boundary. For each piece it sends WREN (0x06), then PAGE PROGRAM (0x02) with the 24-bit address and the data bytes, all with PD3 asserted, then waits for completion with bms_extflash_wait_ready. The buffer and address advance by the piece length until the count is used up. The routine does not read back or verify the data, and it does not check the status register for program errors.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source data buffer in RAM |
| `param_2` | `u32` | 24-bit destination flash address |
| `param_3` | `u32` | byte count |

**Notes:** Caller bms_4168_0800bc20 is not described in this packet. The 256-byte page size is the standard value for this command family.

- Addresses by version: 4130: 0x0800AE20, 4139: 0x0800B358, 4148: 0x0800BA74, 4168: 0x0800BD88
- Called by: `bms_4168_0800bc20`
- Calls: `bms_spi1_transfer_byte`, `bms_extflash_wait_ready`
- Confidence: high

## bms_extflash_read

**Read N bytes from external SPI flash at a 24-bit address using command 0x03**

Reads param_3 bytes starting at the 24-bit address param_2 into the buffer at param_1. It asserts PD3, sends READ DATA (0x03), then sends the address bytes from bits 23:16, 15:8 and 7:0, and clocks out 0xFF per byte, storing each received byte through a 16-bit index. PD3 is released at the end. The routine does not check the WIP bit or the bus status before reading.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination buffer |
| `param_2` | `u32` | 24-bit flash address; the upper byte is ignored |
| `param_3` | `u32` | byte count; values above 0xFFFF never terminate the loop |

**Notes:** Callers in the packet use a count of 12. A count of 0x10000 or more makes the 16-bit index wrap, so the loop never exits, which is a latent hang.

- Addresses by version: 4130: 0x0800ABD4, 4139: 0x0800B10C, 4148: 0x0800B828, 4168: 0x0800BB3C
- Called by: `bms_4168_08003a50`, `bms_4168_08005768`, `bms_extflash_journal_init`
- Calls: `bms_spi1_transfer_byte`
- Confidence: high

## bms_extflash_read_device_id

**Read the manufacturer and device ID with command 0x90 and return them as a u16**

Sends the Read Manufacturer/Device ID command 0x90 with PD3 asserted, followed by three zero address bytes, then reads two bytes: the manufacturer ID first and the device ID second. It returns them packed with the manufacturer in the high byte and the device in the low byte. The IDs are not checked against a table here.

**Returns** `u16`: (manufacturer << 8) | device ID

**Notes:** Caller is bms_4168_08008724.

- Addresses by version: 4130: 0x0800AC20, 4139: 0x0800B158, 4148: 0x0800B874, 4168: 0x0800BB88
- Called by: `bms_4168_08008724`
- Calls: `bms_spi1_transfer_byte`
- Confidence: high

## bms_extflash_sector_erase

**Erase one 4 KB external flash sector with 0x20 after WREN and a ready wait**

Erases the 4 KB sector whose index is the low 12 bits of param_1. It asserts the chip select on PD3 (GPIOD BRR bit 3 low, BSRR bit 3 high to release), and sends WREN (0x06), then waits with bms_extflash_wait_ready. It then sends the sector-erase command 0x20 followed by a 24-bit address built as sector << 12, using the bytes sector >> 4, (sector & 0xF) << 4 and 0. The command set matches the W25Q-style SPI NOR family, but the part is not identified in the packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | sector index; only the low 12 bits are used |

**Notes:** PD3 as the chip select is inferred from the GPIOD base address. Callers are bms_4168_08003a50 and bms_4168_08005768.

- Addresses by version: 4130: 0x0800AB38, 4139: 0x0800B070, 4148: 0x0800B78C, 4168: 0x0800BAA0
- Called by: `bms_4168_08003a50`, `bms_4168_08005768`
- Calls: `bms_spi1_transfer_byte`, `bms_extflash_wait_ready`
- Confidence: medium

## bms_extflash_wait_ready

**Poll external flash status (0x05) until WIP clears, bounded by the 16-bit word at 0x2000067C**

Waits for the external flash to finish an internal write or erase. It starts a retry budget of 500 (0x01F4) at RAM 0x20000628, calls bms_u16_2000067c_set, then loops: it sends RDSR (0x05) with PD3 asserted and reads the status byte, and exits when WIP (bit 0) clears. While WIP stays set, the budget is reloaded from the 16-bit value returned by bms_u16_2000067c_get, so the loop continues as long as that value is nonzero, and a zero budget ends the wait early. DAT_2000062C ends as 1 if the budget is zero at exit and 0 otherwise.

**Notes:** The argument passed to bms_u16_2000067c_set is not recovered from the decompile. The 0x2000067C value is assumed to be a countdown decremented elsewhere, which is not in this packet. Callers include bms_4168_0800baa0 and bms_4168_0800bd88.

- Addresses by version: 4130: 0x0800AC5C, 4139: 0x0800B194, 4148: 0x0800B8B0, 4168: 0x0800BBC4
- Called by: `bms_extflash_sector_erase`, `bms_4168_0800bc20`, `bms_extflash_page_program`
- Calls: `bms_spi1_transfer_byte`, `bms_u16_2000067c_get`, `bms_u16_2000067c_set`
- Confidence: medium

## bms_extflash_wip_poll

**Read the external flash status once; return 1 while a write is still in progress**

Makes one poll of the external flash busy state. It copies the 16-bit value from bms_u16_2000067e_get into RAM bytes 0x2000062A and 0x2000062B, then sends RDSR (0x05) with PD3 asserted and reads one status byte. It returns 1 only when the WIP bit (bit 0) is set and the saved value is nonzero, meaning keep waiting. When WIP is clear and the saved value is nonzero it clears DAT_2000062C and returns 0. In every other case, including a zero saved value, DAT_2000062C is set to 1 and the routine returns 0.

**Returns** `bool`: 1 while busy with a nonzero saved value, otherwise 0

**Notes:** The meaning of the 16-bit value at 0x2000067E and of the flag at 0x2000062C is not established in this packet.

- Addresses by version: 4130: 0x0800AB84, 4139: 0x0800B0BC, 4148: 0x0800B7D8, 4168: 0x0800BAEC
- Called by: `bms_4168_08003a50`, `bms_4168_08005768`
- Calls: `bms_spi1_transfer_byte`, `bms_u16_2000067e_get`
- Confidence: medium
