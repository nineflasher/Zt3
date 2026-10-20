# BMS - `flash` functions

18 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`HAL_FLASHEx_Erase`](#hal_flashex_erase) | 0x08001DBC | Erases flash pages or a bank under a busy lock, reporting the first failing page |
| [`HAL_FLASH_Lock`](#hal_flash_lock) | 0x08001E74 | Sets FLASH.CR.LOCK and returns 1 if the bit still reads 0 afterwards |
| [`HAL_FLASH_Program`](#hal_flash_program) | 0x08001E90 | Programs one double-word or a 256-byte fast row into flash, masking IRQs during the copy |
| [`HAL_FLASH_Unlock`](#hal_flash_unlock) | 0x08001F24 | Unlocks FLASH.CR with the KEY1/KEY2 sequence and returns 1 if it stays locked |
| [`bms_extflash_journal_step`](#bms_extflash_journal_step) | 0x08003A50 | Journal step: write one 660-byte record to external flash, verify it, then rewrite the 12-byte header |
| [`bms_extflash_page_program`](#bms_extflash_page_program) | 0x0800BD88 | Program N bytes into external flash with WREN and command 0x02, split at 256-byte boundaries |
| [`bms_extflash_probe_and_init`](#bms_extflash_probe_and_init) | 0x08008724 | Probe the external SPI flash ID, init the journal, or flag status bit 0x1000 when absent |
| [`bms_extflash_read`](#bms_extflash_read) | 0x0800BB3C | Read N bytes from external SPI flash at a 24-bit address using command 0x03 |
| [`bms_extflash_read_device_id`](#bms_extflash_read_device_id) | 0x0800BB88 | Read the manufacturer and device ID with command 0x90 and return them as a u16 |
| [`bms_extflash_sector_erase`](#bms_extflash_sector_erase) | 0x0800BAA0 | Erase one 4 KB external flash sector with 0x20 after WREN and a ready wait |
| [`bms_extflash_wait_ready`](#bms_extflash_wait_ready) | 0x0800BBC4 | Poll external flash status (0x05) until WIP clears, bounded by the 16-bit word at 0x2000067C |
| [`bms_extflash_wip_poll`](#bms_extflash_wip_poll) | 0x0800BAEC | Read the external flash status once; return 1 while a write is still in progress |
| [`bms_extflash_write_bytes`](#bms_extflash_write_bytes) | 0x0800BC20 | Write bytes to external SPI flash, erasing a 4 KB sector only when target bytes are not 0xFF |
| [`bms_extlog_request_dispatch`](#bms_extlog_request_dispatch) | 0x08005768 | External-flash log dispatcher: init regions, read records, run journal step, append, rewrite header |
| [`bms_flash_erase_program_page`](#bms_flash_erase_program_page) | 0x08008788 | Erase one 2 KB flash page, program it by doubleword and verify, with up to five attempts |
| [`bms_flash_wait_idle_check`](#bms_flash_wait_idle_check) | 0x08001460 | Waits for flash to go idle, clears its error flags, and reports errors or timeouts |
| [`bms_flash_write_bytes`](#bms_flash_write_bytes) | 0x08008DE8 | Write a byte range to internal flash through a 2 KB staging buffer, page by page |
| [`bms_nvm_save_state_snapshot`](#bms_nvm_save_state_snapshot) | 0x08008018 | Save the 512-byte state block to flash at 0x0803F000, retrying up to four times |

## HAL_FLASHEx_Erase

**Erases flash pages or a bank under a busy lock, reporting the first failing page**

Returns 2 (HAL_BUSY) when the lock byte at 0x20005D2C is set. Otherwise it takes the lock and clears the flash error word at 0x20005D30. When the first word of the erase record is 4 it ORs the second word and STRT (bit 16) into FLASH.CR and waits, which looks like a mass-erase start. For the page path it loops over NbPages pages from the first page, writing PNB (bits 3-10), bank bits (selected by whether the bank word equals 4), PER (bit 1) and STRT (bit 16) into CR, then waits with bms_flash_wait_idle_check for up to 1000 ms per page. It stops at the first failure and stores that page in *PageError (preset to 0xFFFFFFFF), clears PER, releases the lock and returns the status.

| Parameter | Type | Description |
|---|---|---|
| `erase` | `ptr` | param_1, erase record: type word, bank word, first page, page count |
| `page_error` | `ptr` | param_2, output: failing page number or 0xFFFFFFFF |

**Returns** `u32`: HAL status: 0 OK, 1 error, 2 busy, 3 timeout

**Notes:** The meaning of the type value 4 and of the bank bits is not established in this packet, so the mass-erase reading is a guess.

- Addresses by version: 4130: 0x08001DBC, 4139: 0x08001DBC, 4148: 0x08001DBC, 4168: 0x08001DBC
- Peripheral registers: `FLASH.ACR` (A), `FLASH.CR` (RW)
- Called by: `bms_flash_erase_program_page`
- Calls: `bms_flash_wait_idle_check`
- Confidence: medium

## HAL_FLASH_Lock

**Sets FLASH.CR.LOCK and returns 1 if the bit still reads 0 afterwards**

Sets bit 31 (LOCK) of FLASH.CR at 0x40022014 by read-modify-write, reads the register back, and returns 1 when LOCK reads 0, meaning the lock did not take. It returns 0 when the bit reads back set. It does not wait on the flash busy flag. Because 1 means failure here, the return value is the reverse of the HAL_OK convention.

**Returns** `bool`: 1 when LOCK still reads 0 (failure), 0 when locked

**Notes:** Name follows ST HAL_FLASH_Lock. The return sense is inverted compared with the HAL status return, so callers must be checked before reusing it.

- Addresses by version: 4130: 0x08001E74, 4139: 0x08001E74, 4148: 0x08001E74, 4168: 0x08001E74
- Peripheral registers: `FLASH.CR` (RW)
- Called by: `bms_flash_erase_program_page`
- Confidence: medium

## HAL_FLASH_Program

**Programs one double-word or a 256-byte fast row into flash, masking IRQs during the copy**

Uses the same busy lock and error word as HAL_FLASHEx_Erase and returns 2 when busy. Type 1 (double-word) sets CR.PG (bit 0), writes the two 32-bit words to the target address and issues a barrier. Any other type sets CR.FSTPG (bit 18), copies 64 words (256 bytes) from the source buffer into flash with interrupts disabled during the copy (PRIMASK is saved when privileged), and waits without a timeout for BSY (bits 16 and 17). Both paths then call bms_flash_wait_idle_check with a 1000 ms timeout, clear the CR bits named by the type value, release the lock and return the status.

| Parameter | Type | Description |
|---|---|---|
| `type` | `u32` | param_1, programming type: 1 double-word, other values fast row |
| `address` | `ptr` | param_2, flash destination address |
| `data_or_src` | `u32` | param_3, first data word for double-word, or source buffer pointer for a fast row |
| `data_hi` | `u32` | param_4, second data word (double-word only) |

**Returns** `u32`: HAL status: 0 OK, 1 error, 2 busy, 3 timeout

**Notes:** In the fast path the final CR write uses the type value (2 or 3) as the clear mask, which clears PER and PG but not FSTPG (bit 18). FSTPG may therefore stay set after a fast row program; check against the reference manual.

- Addresses by version: 4130: 0x08001E90, 4139: 0x08001E90, 4148: 0x08001E90, 4168: 0x08001E90
- Peripheral registers: `FLASH.SR` (R), `FLASH.CR` (RW)
- Called by: `bms_flash_erase_program_page`
- Calls: `bms_flash_wait_idle_check`
- Confidence: medium

## HAL_FLASH_Unlock

**Unlocks FLASH.CR with the KEY1/KEY2 sequence and returns 1 if it stays locked**

If FLASH.CR.LOCK (bit 31) is set, writes KEY1 0x45670123 and then KEY2 0xCDEF89AB to FLASH.KEYR at 0x40022008. It then reads CR back and returns 1 when LOCK is still set (failure) and 0 otherwise. When the flash is already unlocked it writes nothing and returns 0. There is no timeout loop.

**Returns** `u32`: 0 on success (unlocked), 1 if still locked

**Notes:** Name follows the ST HAL routine from its behaviour.

- Addresses by version: 4130: 0x08001F24, 4139: 0x08001F24, 4148: 0x08001F24, 4168: 0x08001F24
- Peripheral registers: `FLASH.KEYR` (W), `FLASH.CR` (R)
- Called by: `bms_flash_erase_program_page`
- Confidence: high

## bms_extflash_journal_step

**Journal step: write one 660-byte record to external flash, verify it, then rewrite the 12-byte header**

A six-state machine stepped once per call from the state byte at 0x20001341. It returns 0 while a flash operation is pending and 1 when the cycle has finished, successfully or after retries are exhausted. State 0 erases the next 4 KB sector when the write pointer 0x20001350 is on a sector boundary, and lowers the sequence counter 0x20001348 by 5 when it is above 2999. State 1 starts a 660-byte (0x294) write of RAM buffer 0x200010A8 to the write pointer. State 2 waits for the write, reads the record back with bms_extflash_read and compares it with bms_memcmp_prefix. On success it advances 0x20001350 by 0x294, or by 0x5B0 when the new offset within the sector would exceed 0xCE3, wraps it to 0x10000 past 0x267FFE, moves the erase-ahead pointer 0x2000134C forward by 0x1000 when the write pointer reaches it, adds 1 to the counter and goes to state 3; on a failed verify it adds 5 to the counter and retries up to three times. States 3 to 5 erase sector 0, write the 12-byte header (counter, erase pointer, write pointer at 0x20001348 to 0x2000134C to 0x20001350) to flash address 0, and read it back, again with up to three retries.

**Returns** `u32`: 0 while busy or waiting; 1 when a cycle has finished (check of the header or record done, or retries used up)

**Notes:** Every record write is followed by a sector-0 erase and header rewrite, so sector 0 wears at the record rate. The helper bms_4168_0800bc20 (external-flash write taking source, flash address and length) is not yet described; it is treated here as a write from its use. The constants 0x10000 and 0x267FFE bound the log region. The meaning of the counter at 0x20001348 is inferred (it moves by 1 on success and by 5 on failure, like a wear or back-off count).

- Addresses by version: 4130: 0x08003A3C, 4139: 0x08003A3C, 4148: 0x08003A50, 4168: 0x08003A50
- Called by: `bms_extlog_request_dispatch`
- Calls: `bms_mem_zero`, `bms_memcmp_prefix`, `bms_extflash_sector_erase`, `bms_extflash_wip_poll`, `bms_extflash_read`, `bms_extflash_write_bytes`
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
- Called by: `bms_extflash_write_bytes`
- Calls: `bms_spi1_transfer_byte`, `bms_extflash_wait_ready`
- Confidence: high

## bms_extflash_probe_and_init

**Probe the external SPI flash ID, init the journal, or flag status bit 0x1000 when absent**

Checks the external flash identity. It reads the manufacturer and device ID with bms_extflash_read_device_id up to three times and accepts 0xC815 or 0x8515. When neither ID is seen it sets bit 12 (0x1000) of the u16 at +0x196 of the state block; otherwise it clears that bit and calls bms_extflash_journal_init. Both paths finish with bms_seq_state_reset.

- Addresses by version: 4130: 0x080076D8, 4139: 0x08007BD8, 4148: 0x08008424, 4168: 0x08008724
- Called by: `bms_4168_08010558`
- Calls: `bms_extflash_journal_init`, `bms_extflash_read_device_id`, `bms_ram_20000bdc_addr`, `bms_seq_state_reset`
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
- Called by: `bms_extflash_journal_step`, `bms_extlog_request_dispatch`, `bms_extflash_journal_init`
- Calls: `bms_spi1_transfer_byte`
- Confidence: high

## bms_extflash_read_device_id

**Read the manufacturer and device ID with command 0x90 and return them as a u16**

Sends the Read Manufacturer/Device ID command 0x90 with PD3 asserted, followed by three zero address bytes, then reads two bytes: the manufacturer ID first and the device ID second. It returns them packed with the manufacturer in the high byte and the device in the low byte. The IDs are not checked against a table here.

**Returns** `u16`: (manufacturer << 8) | device ID

**Notes:** Caller is bms_4168_08008724.

- Addresses by version: 4130: 0x0800AC20, 4139: 0x0800B158, 4148: 0x0800B874, 4168: 0x0800BB88
- Called by: `bms_extflash_probe_and_init`
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
- Called by: `bms_extflash_journal_step`, `bms_extlog_request_dispatch`
- Calls: `bms_spi1_transfer_byte`, `bms_extflash_wait_ready`
- Confidence: medium

## bms_extflash_wait_ready

**Poll external flash status (0x05) until WIP clears, bounded by the 16-bit word at 0x2000067C**

Waits for the external flash to finish an internal write or erase. It starts a retry budget of 500 (0x01F4) at RAM 0x20000628, calls bms_u16_2000067c_set, then loops: it sends RDSR (0x05) with PD3 asserted and reads the status byte, and exits when WIP (bit 0) clears. While WIP stays set, the budget is reloaded from the 16-bit value returned by bms_u16_2000067c_get, so the loop continues as long as that value is nonzero, and a zero budget ends the wait early. DAT_2000062C ends as 1 if the budget is zero at exit and 0 otherwise.

**Notes:** The argument passed to bms_u16_2000067c_set is not recovered from the decompile. The 0x2000067C value is assumed to be a countdown decremented elsewhere, which is not in this packet. Callers include bms_4168_0800baa0 and bms_4168_0800bd88.

- Addresses by version: 4130: 0x0800AC5C, 4139: 0x0800B194, 4148: 0x0800B8B0, 4168: 0x0800BBC4
- Called by: `bms_extflash_sector_erase`, `bms_extflash_write_bytes`, `bms_extflash_page_program`
- Calls: `bms_spi1_transfer_byte`, `bms_u16_2000067c_get`, `bms_u16_2000067c_set`
- Confidence: medium

## bms_extflash_wip_poll

**Read the external flash status once; return 1 while a write is still in progress**

Makes one poll of the external flash busy state. It copies the 16-bit value from bms_u16_2000067e_get into RAM bytes 0x2000062A and 0x2000062B, then sends RDSR (0x05) with PD3 asserted and reads one status byte. It returns 1 only when the WIP bit (bit 0) is set and the saved value is nonzero, meaning keep waiting. When WIP is clear and the saved value is nonzero it clears DAT_2000062C and returns 0. In every other case, including a zero saved value, DAT_2000062C is set to 1 and the routine returns 0.

**Returns** `bool`: 1 while busy with a nonzero saved value, otherwise 0

**Notes:** The meaning of the 16-bit value at 0x2000067E and of the flag at 0x2000062C is not established in this packet.

- Addresses by version: 4130: 0x0800AB84, 4139: 0x0800B0BC, 4148: 0x0800B7D8, 4168: 0x0800BAEC
- Called by: `bms_extflash_journal_step`, `bms_extlog_request_dispatch`
- Calls: `bms_spi1_transfer_byte`, `bms_u16_2000067e_get`
- Confidence: medium

## bms_extflash_write_bytes

**Write bytes to external SPI flash, erasing a 4 KB sector only when target bytes are not 0xFF**

Writes param_3 bytes from param_1 to the 24-bit external flash address param_2, in pieces that stay inside one 4 KB sector. For each piece it reads the current bytes (command 0x03) into a 4 KB staging buffer at 0x20004420. If all of them are 0xFF the piece is programmed directly with bms_extflash_page_program. Otherwise the whole sector is read into the staging buffer, WREN (0x06) and sector erase (0x20) are issued with bms_extflash_wait_ready after each, the new bytes are merged into the buffer, and the full 4 KB sector is reprogrammed. The chip-select GPIO is toggled through 0x50000C18 and 0x50000C28 around each command, and every byte goes through bms_spi1_transfer_byte.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source bytes in RAM |
| `param_2` | `u32` | 24-bit external flash address |
| `param_3` | `u32` | number of bytes |

**Notes:** The chip-select pin is inferred from the bit used on the GPIO writes. The reprogram step is the page program with the full 4 KB buffer, which is split at 256-byte boundaries inside bms_extflash_page_program.

- Addresses by version: 4130: 0x0800ACB8, 4139: 0x0800B1F0, 4148: 0x0800B90C, 4168: 0x0800BC20
- Called by: `bms_extflash_journal_step`, `bms_extlog_request_dispatch`
- Calls: `bms_spi1_transfer_byte`, `bms_extflash_wait_ready`, `bms_extflash_page_program`
- Confidence: medium

## bms_extlog_request_dispatch

**External-flash log dispatcher: init regions, read records, run journal step, append, rewrite header**

Runs once per call and executes the request selected by the op byte at request+1, where the request block pointer is stored at 0x2000133C and holds the argument at +4 and the destination buffer at +8. The op is cancelled (treated as op 0) when the byte at the address from bms_byte_20000628_addr plus 4 is set, or when bit 12 of the state word at 0x196 is set. Op 1 erases sectors 0 and 1 and initialises region A (counter 0x20001348, erase pointer 0x2000134C, write pointer 0x20001350, starting at 0x10000) and region B (0x20001354, 0x20001358, 0x2000135C, starting at 0x280000). Op 2 reads 20 bytes of a logical record (mode 0). Op 3 maps the record number in argument bytes 2 and 3 (mode 0) and reads 64 bytes at that base plus bytes 0 and 1 times 0x40, minus 0x2C. Op 4 reads 64 bytes of the record with a 32-bit number (mode 1). Op 5 runs bms_extflash_journal_step (bms_4168_08003a50) and completes when it returns nonzero. Op 6 appends a 64-byte record from staging RAM 0x20001360 to region B, with sector erase ahead, read-back verification and up to three retries. Op 7 rewrites the 12-byte region-B header at flash 0x1000 (erase, write, verify, up to three retries). Each op sets the status byte DAT_20001340 to 2 when finished and leaves it unchanged while a wait or retry is pending.

**Notes:** Logical record mapping is bms_logical_addr_map. Argument and buffer offsets come from the decompile; the request block layout is inferred from it. The reads in ops 2 to 4 are through bms_extflash_read. The 64-byte records and the staging buffer 0x20001360 are inferred from the copy sizes.

- Addresses by version: 4130: 0x08004F04, 4139: 0x08005120, 4148: 0x0800561C, 4168: 0x08005768
- Calls: `bms_mem_zero`, `bms_memcmp_prefix`, `bms_logical_addr_map`, `bms_extflash_journal_step`, `bms_extflash_sector_erase`, `bms_byte_20000628_addr`, `bms_extflash_wip_poll`, `bms_extflash_read`, `bms_extflash_write_bytes`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_flash_erase_program_page

**Erase one 2 KB flash page, program it by doubleword and verify, with up to five attempts**

Writes a full 2 KB flash page at 0x08000000 + page * 0x800. The page index is checked against the flash size read from FLASHSIZE and PACKAGE_DATA. FLASH.SR is cleared, then flash is unlocked with HAL_FLASH_Unlock (returns 1 if it stays locked). For up to five attempts the page is erased (HAL_FLASHEx_Erase, bms_4168_08001DBC) and the buffer is programmed eight bytes at a time with HAL_FLASH_Program (bms_4168_08001E90). After each doubleword the routine checks an abort flag at 0x20000680 (which increments the error counter at 0x20000682), the ECC double-error bit 30 of FLASH.ECCR (cleared by writing 0x40000000), and reads the doubleword back with bms_memcmp_prefix. Any failure starts the next attempt. On success the flash is locked with HAL_FLASH_Lock and 0 is returned; after five failed attempts 2 is returned.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | page index counted from 0x08000000 in 2 KB steps |
| `param_2` | `ptr` | 2 KB source buffer in RAM |

**Returns** `s32`: 0 on success, 1 for an out-of-range page or a lock or unlock failure, 2 when all five attempts failed

**Notes:** On the return-2 path the decompile shows no HAL_FLASH_Lock call, so flash may be left unlocked; this should be checked. The page size of 2 KB and the bit meanings are taken from the code and the G0 register layout, not from the reference manual.

- Addresses by version: 4130: 0x0800773C, 4139: 0x08007C3C, 4148: 0x08008488, 4168: 0x08008788
- Peripheral registers: `TIM2.CR1` (A), `FLASH.SR` (W), `FLASH.ECCR` (RW), `FLASH.OPTR` (R)
- Called by: `bms_flash_write_bytes`
- Calls: `bms_memcmp_prefix`, `HAL_FLASHEx_Erase`, `HAL_FLASH_Lock`, `HAL_FLASH_Program`, `HAL_FLASH_Unlock`
- Confidence: medium

## bms_flash_wait_idle_check

**Waits for flash to go idle, clears its error flags, and reports errors or timeouts**

Polls FLASH.SR (0x40022010) while busy bits 16 and 17 are set, for up to param_1 ms on the 1 kHz tick (bms_get_ram_word_200006a0). It then writes 0x8C3FB to SR, which clears the EOP and error flags (write one to clear), and tests the earlier SR value against 0xC3FA. If an error bit was set it saves those bits to RAM 0x20005D30 and returns 1. Otherwise it waits up to param_1 ms for SR bit 18 to clear and returns 0, or returns 3 on timeout, following the HAL status codes.

| Parameter | Type | Description |
|---|---|---|
| `timeout_ms` | `u32` | param_1, timeout in milliseconds |

**Returns** `u32`: HAL status: 0 OK, 1 flash error (bits saved at 0x20005D30), 3 timeout

**Notes:** The 1 ms tick is an assumption: bms_get_ram_word_200006a0 is used as the timeout clock throughout this packet, but its own code does not show the unit. SR bit 18 is not named in this packet.

- Addresses by version: 4130: 0x08001460, 4139: 0x08001460, 4148: 0x08001460, 4168: 0x08001460
- Peripheral registers: `FLASH.SR` (RW)
- Called by: `HAL_FLASHEx_Erase`, `HAL_FLASH_Program`
- Calls: `bms_get_ram_word_200006a0`
- Confidence: high

## bms_flash_write_bytes

**Write a byte range to internal flash through a 2 KB staging buffer, page by page**

Read-modify-write of an arbitrary byte range into internal flash. It returns 1 at once when the flag at 0x20000681 is set. Otherwise each affected 2 KB page is staged at 0x20005450. A partial first or last page is copied from flash and overlaid with the new bytes, and whole middle pages are taken from the source. Each staged page is programmed with bms_flash_erase_program_page (0x08008788). The first failure is returned immediately; otherwise 0 is returned after the last page.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | destination flash address |
| `param_2` | `ptr` | source bytes in RAM |
| `param_3` | `u32` | number of bytes |

**Returns** `s32`: 0 on success, 1 when the flag at 0x20000681 blocks writes, otherwise the error from bms_flash_erase_program_page

**Notes:** The decompile calls the page copy with only two arguments, so the 2 KB length of the flash-to-staging copy is inferred. The flag at 0x20000681 is read here only; its setter is not in this packet.

- Addresses by version: 4130: 0x08007D9C, 4139: 0x0800829C, 4148: 0x08008AE8, 4168: 0x08008DE8
- Called by: `bms_nvm_save_state_snapshot`, `bms_fw_upload_handle`
- Calls: `memcpy`, `bms_flash_erase_program_page`
- Confidence: medium

## bms_nvm_save_state_snapshot

**Save the 512-byte state block to flash at 0x0803F000, retrying up to four times**

Runs with interrupts masked. It calls bms_flash_write_bytes (0x08008DE8) with flash address 0x0803F000, source the state block pointer at 0x2000002C, and length 0x200. The write is attempted up to four times, and the first success ends the routine with interrupts restored. After four failures the routine sets bit 14 (0x4000) of the u16 at +0x194 of the state block as a save-failure flag.

**Notes:** The flag bit 0x4000 at +0x194 is the only status left behind; no caller in this packet reads it.

- Addresses by version: 4130: 0x08006FD0, 4139: 0x080074D0, 4148: 0x08007D10, 4168: 0x08008018
- Called by: `bms_4168_08003290`, `bms_4168_08003c3c`, `bms_4168_080082f0`
- Calls: `bms_flash_write_bytes`
- Confidence: high
