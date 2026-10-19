# BMS - `flash` functions

2 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`HAL_FLASH_Lock`](#hal_flash_lock) | 0x08001E74 | Sets FLASH.CR.LOCK and returns 1 if the bit still reads 0 afterwards |
| [`HAL_FLASH_Unlock`](#hal_flash_unlock) | 0x08001F24 | Unlocks FLASH.CR with the KEY1/KEY2 sequence and returns 1 if it stays locked |

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
