# VCU - `flash` functions

17 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`flash_fap_status_get`](#flash_fap_status_get) | 0x0800CE78 | Read the flash access-protection (read-out protection) status |
| [`flash_flag_clear`](#flash_flag_clear) | 0x0800CE88 | Clear flash status flags (FLASH.STS) |
| [`flash_halfword_program`](#flash_halfword_program) | 0x0800CE94 | Program one 16-bit flash halfword (CTRL.FPRGM) and wait for the operation to finish |
| [`flash_lock`](#flash_lock) | 0x0800CEB8 | Set FLASH.CTRL.OPLK to lock the flash program/erase controller |
| [`flash_operation_status_get`](#flash_operation_status_get) | 0x0800CEC8 | Return the flash controller status: busy, program error, EPP error or done |
| [`flash_operation_wait_for`](#flash_operation_wait_for) | 0x0800CEF0 | Poll the flash status until the operation ends, or return timeout (4) when the count runs out |
| [`flash_sector_erase`](#flash_sector_erase) | 0x0800CF10 | Erase one flash sector: set CTRL.SECERS, load FLASH.ADDR, start, wait |
| [`flash_unlock`](#flash_unlock) | 0x0800CF3C | Write the two flash unlock keys to FLASH.UNLOCK to enable erase and program |
| [`flash_user_system_data_erase`](#flash_user_system_data_erase) | 0x0800CE0C | Erase the user system data block, then restore the FAP halfword to 0xA5 if allowed |
| [`vcu_config_ab_slot_load`](#vcu_config_ab_slot_load) | 0x08005BB4 | Load the newer valid 512-byte config copy from flash slot A (0x0801F000) or B (0x0801F400) |
| [`vcu_flash_erase_range`](#vcu_flash_erase_range) | 0x08005B40 | Erase a byte range page by page with flash unlocked; returns 1 if all pages erased |
| [`vcu_flash_erase_range_locked`](#vcu_flash_erase_range_locked) | 0x080060A4 | Erase a flash range with interrupts masked; returns 0 on success, 2 on failure |
| [`vcu_flash_page_count`](#vcu_flash_page_count) | 0x08005B2C | Ceiling division of a byte count by 1024 |
| [`vcu_flash_program_verified`](#vcu_flash_program_verified) | 0x08005D58 | Program a halfword buffer to flash, verifying each halfword by readback |
| [`vcu_flash_record_pingpong_save`](#vcu_flash_record_pingpong_save) | 0x08007D88 | Save the 512-byte record to alternating flash half-pages at 0x0801F000 and 0x0801F400 |
| [`vcu_flash_usd_reset_if_unprotected`](#vcu_flash_usd_reset_if_unprotected) | 0x08005B90 | Erase the user system data block if the argument is set and read-out protection is off |
| [`vcu_upgrade_record_store`](#vcu_upgrade_record_store) | 0x080065B4 | Erase and rewrite the 12-byte upgrade record at flash 0x0801F800, interrupts masked |

## flash_fap_status_get

**Read the flash access-protection (read-out protection) status**

AT32 SDK flash_fap_status_get(): returns bit 1 of FLASH.USD (0x4002201c), the FAP flag: 1 when flash access protection is active. Called once by vcu_0159_08005b90 (purpose of the caller not examined).

**Returns** `u32`: 1 if FAP set, else 0

- Addresses by version: 148: 0x0800BFEC, 14a: 0x0800C430, 14b: 0x0800C8BC, 14e: 0x0800C950, 14f: 0x0800CA8C, 152: 0x0800CD18, 153: 0x0800CE0C, 0159: 0x0800CE78
- Peripheral registers: `FLASH.USD` (R)
- Called by: `vcu_flash_usd_reset_if_unprotected`
- Confidence: high

## flash_flag_clear

**Clear flash status flags (FLASH.STS)**

AT32 SDK flash_flag_clear(): writes param_1 to FLASH.STS (0x4002200c); the ODF, PRGMERR and EPPERR flags are write-1-to-clear. Called by vcu_0159_08005b40 (probably a flash program/erase routine).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | FLASH_xxx_FLAG mask (ODF/PRGMERR/EPPERR) |

- Addresses by version: 148: 0x0800BFFC, 14a: 0x0800C440, 14b: 0x0800C8CC, 14e: 0x0800C960, 14f: 0x0800CA9C, 152: 0x0800CD28, 153: 0x0800CE1C, 0159: 0x0800CE88
- Peripheral registers: `FLASH.STS` (W)
- Called by: `vcu_flash_erase_range`
- Confidence: high

## flash_halfword_program

**Program one 16-bit flash halfword (CTRL.FPRGM) and wait for the operation to finish**

AT32 SDK flash_halfword_program(address, data), void variant. It sets CTRL.FPRGM (bit 0), stores the halfword at the flash address (a 16-bit store through param_1), waits with flash_operation_wait_for (vcu_0159_0800cef0) using a count of 0x100000, and clears FPRGM. The wait status is discarded, so a failed program is not reported to the caller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | flash address to program (halfword aligned) |
| `param_2` | `u16` | halfword value to write |

- Addresses by version: 148: 0x0800C008, 14a: 0x0800C44C, 14b: 0x0800C8D8, 14e: 0x0800C96C, 14f: 0x0800CAA8, 152: 0x0800CD34, 153: 0x0800CE28, 0159: 0x0800CE94
- Peripheral registers: `FLASH.CTRL` (RW)
- Called by: `vcu_flash_program_verified`
- Calls: `flash_operation_wait_for`
- Confidence: high

## flash_lock

**Set FLASH.CTRL.OPLK to lock the flash program/erase controller**

Read-modify-write of FLASH.CTRL (0x40022010, FLASH_REG_BASE+0x10) that sets bit 7 (OPLK) and leaves the other control bits unchanged. With OPLK set the controller refuses further erase and program operations until flash_unlock is called again. This is the Artery SDK flash_lock routine, written out as a single OR of the existing register value.

- Addresses by version: 148: 0x0800C02C, 14a: 0x0800C470, 14b: 0x0800C8FC, 14e: 0x0800C990, 14f: 0x0800CACC, 152: 0x0800CD58, 153: 0x0800CE4C, 0159: 0x0800CEB8
- Peripheral registers: `FLASH.PSR` (A), `FLASH.CTRL` (RW)
- Called by: `vcu_flash_erase_range`, `vcu_flash_usd_reset_if_unprotected`, `vcu_flash_program_verified`
- Confidence: high

## flash_operation_status_get

**Return the flash controller status: busy, program error, EPP error or done**

Reads FLASH.STS (0x4002200C) and checks the flags in priority order: OBF (bit 0) gives 0 = FLASH_OPERATE_BUSY, PRGMERR (bit 2) gives 1 = FLASH_PROGRAM_ERROR, EPPERR (bit 4) gives 2 = FLASH_EPP_ERROR, and if none is set the result is 3 = FLASH_OPERATE_DONE. The code returns 0 at once when the busy flag is set. This matches the Artery SDK flash_operation_status_get; the timeout code 4 is not produced here. Called after erase or program operations to wait for completion.

**Returns** `u32`: flash_status_type: 0 busy, 1 program error, 2 EPP error, 3 operate done

- Addresses by version: 148: 0x0800C03C, 14a: 0x0800C480, 14b: 0x0800C90C, 14e: 0x0800C9A0, 14f: 0x0800CADC, 152: 0x0800CD68, 153: 0x0800CE5C, 0159: 0x0800CEC8
- Peripheral registers: `FLASH.STS` (R)
- Called by: `flash_operation_wait_for`
- Confidence: high

## flash_operation_wait_for

**Poll the flash status until the operation ends, or return timeout (4) when the count runs out**

AT32 SDK flash_operation_wait_for(time_out). It calls flash_operation_status_get (vcu_0159_0800cec8) and repeats while the result is 0 (busy) and the countdown is not zero, decrementing the countdown on each poll. It returns the final status: 1 program error, 2 EPP error, 3 operate done, or 4 (FLASH_OPERATE_TIMEOUT) when the countdown reaches zero while the flash is still busy. Callers in this packet pass 0x40000000 for erase and 0x100000 for a halfword program.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | poll count limit (passed in r0; not in the decompiled signature) |

**Returns** `u32`: flash_status_type: 1 program error, 2 EPP error, 3 operate done, 4 timeout

- Addresses by version: 148: 0x0800C064, 14a: 0x0800C4A8, 14b: 0x0800C934, 14e: 0x0800C9C8, 14f: 0x0800CB04, 152: 0x0800CD90, 153: 0x0800CE84, 0159: 0x0800CEF0
- Called by: `flash_user_system_data_erase`, `flash_halfword_program`, `flash_sector_erase`
- Calls: `flash_operation_status_get`
- Confidence: high

## flash_sector_erase

**Erase one flash sector: set CTRL.SECERS, load FLASH.ADDR, start, wait**

AT32 SDK flash_sector_erase(sector_address). It sets CTRL.SECERS (bit 1), writes the sector address to FLASH.ADDR (0x40022014), sets CTRL.ERSTR (bit 6) to start the erase, waits with flash_operation_wait_for (vcu_0159_0800cef0) using a count of 0x40000000, and clears SECERS. The status from the wait is dropped in this build, so the function is void here and an erase failure is not reported.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | address of the flash sector to erase |

- Addresses by version: 148: 0x0800C084, 14a: 0x0800C4C8, 14b: 0x0800C954, 14e: 0x0800C9E8, 14f: 0x0800CB24, 152: 0x0800CDB0, 153: 0x0800CEA4, 0159: 0x0800CF10
- Peripheral registers: `TMR2.CTRL1` (A), `FLASH.CTRL` (RW), `FLASH.ADDR` (W)
- Called by: `vcu_flash_erase_range`
- Calls: `flash_operation_wait_for`
- Confidence: high

## flash_unlock

**Write the two flash unlock keys to FLASH.UNLOCK to enable erase and program**

Writes key1 0x45670123 and then key2 0xCDEF89AB to FLASH.UNLOCK (0x40022004). The controller unlocks only when the keys arrive in that order with no other write in between. This is the Artery SDK flash_unlock routine. It must be called before any flash_sector_erase or program sequence, and flash_lock (vcu_0159_0800ceb8) re-locks.

- Addresses by version: 148: 0x0800C0B0, 14a: 0x0800C4F4, 14b: 0x0800C980, 14e: 0x0800CA14, 14f: 0x0800CB50, 152: 0x0800CDDC, 153: 0x0800CED0, 0159: 0x0800CF3C
- Peripheral registers: `FLASH.PSR` (A), `FLASH.UNLOCK` (W)
- Called by: `vcu_flash_erase_range`, `vcu_flash_usd_reset_if_unprotected`, `vcu_flash_program_verified`
- Confidence: high

## flash_user_system_data_erase

**Erase the user system data block, then restore the FAP halfword to 0xA5 if allowed**

AT32 SDK flash_user_system_data_erase, built with an argument. It writes the two USD unlock keys 0x45670123 and 0xCDEF89AB to FLASH.USD_UNLOCK (0x40022008), waits for CTRL.USDULKS (bit 9), sets CTRL.USDERS (bit 5) and CTRL.ERSTR (bit 6), and waits with flash_operation_wait_for (vcu_0159_0800cef0). If the erase reports done and the argument is 0, it sets CTRL.USDPRGM (bit 4), writes the FAP_RELIEVE_KEY 0xA5 halfword to the user system data at 0x1FFFF800, waits again and clears USDPRGM. USDERS is cleared on every path. Nothing is returned.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | FAP-active flag: 0 = FAP not enabled, so the FAP byte is restored to 0xA5 after the erase; non-zero skips the restore |

**Notes:** The SDK version takes no argument; here the value plays the role of the SDK's flash_fap_status_get() result (0 = FAP not active). The packet lists TMR2.CTRL1 for this function, which is wrong: the 0x40000000 passed to the wait is a timeout count, and no TMR2 register is accessed.

- Addresses by version: 148: 0x0800BF80, 14a: 0x0800C3C4, 14b: 0x0800C850, 14e: 0x0800C8E4, 14f: 0x0800CA20, 152: 0x0800CCAC, 153: 0x0800CDA0, 0159: 0x0800CE0C
- Peripheral registers: `TMR2.CTRL1` (A), `FLASH.USD_UNLOCK` (W), `FLASH.CTRL` (RW)
- Called by: `vcu_flash_usd_reset_if_unprotected`
- Calls: `flash_operation_wait_for`
- Confidence: high

## vcu_config_ab_slot_load

**Load the newer valid 512-byte config copy from flash slot A (0x0801F000) or B (0x0801F400)**

Reads the sequence halfwords at 0x0801F1FE (slot A, into DAT_20001024) and 0x0801F5FE (slot B, into DAT_20001026) and tries the newer copy first. The 512-byte copy is read to RAM at DAT_20001AB4 and checked with vcu_sum_s16_minus_trailer over 256 halfwords against the stored checksum pair in DAT_20001CA8 and DAT_20001CAA. If the newer copy fails it tries the other slot, and if both fail it uses vcu_serial_check_default (vcu_0159_080066DC) to choose a fallback copy to load without the check, or else sets DAT_20001022 to 0 and the first halfword of the buffer to 0xFFFF. A successful load sets DAT_20001022 to the chosen sequence number, and the fallback loads and the recovered-copy path call vcu_0159_08007D88 (not yet described).

**Notes:** The call to vcu_0159_08007D88 is made only on the recovery and fallback paths, not when the first choice verifies. Callers: vcu_0159_08009DA8 (not described).

- Addresses by version: 148: 0x080051B4, 14a: 0x080055A0, 14b: 0x080058C8, 14e: 0x08005900, 14f: 0x0800595C, 152: 0x080059B4, 153: 0x08005A50, 0159: 0x08005BB4
- Called by: `vcu_0159_08009da8`
- Calls: `vcu_sum_s16_minus_trailer`, `vcu_copy_bytes_src_dst`, `vcu_serial_check_default`, `vcu_flash_record_pingpong_save`
- Confidence: high

## vcu_flash_erase_range

**Erase a byte range page by page with flash unlocked; returns 1 if all pages erased**

Unlocks flash, clears the status flags (0x14) and computes the number of 1 KiB pages covering the length with vcu_flash_page_count. It erases pages upward from the start address with flash_sector_erase and stops at the first page whose erase does not return the done status (3), then locks flash again. It returns 1 if every page was erased and 0 otherwise.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash start address of the range |
| `param_2` | `u32` | length of the range in bytes |

**Returns** `u32`: 1 when all pages were erased, 0 when a page erase failed

**Notes:** Callers: vcu_flash_erase_range_locked, vcu_upgrade_record_store and vcu_0159_08007D88 (not yet described).

- Addresses by version: 148: 0x08005140, 14a: 0x0800552C, 14b: 0x08005854, 14e: 0x0800588C, 14f: 0x080058E8, 152: 0x08005940, 153: 0x080059DC, 0159: 0x08005B40
- Called by: `vcu_flash_erase_range_locked`, `vcu_upgrade_record_store`, `vcu_flash_record_pingpong_save`
- Calls: `vcu_flash_page_count`, `flash_flag_clear`, `flash_lock`, `flash_sector_erase`, `flash_unlock`
- Confidence: high

## vcu_flash_erase_range_locked

**Erase a flash range with interrupts masked; returns 0 on success, 2 on failure**

Masks interrupts with the CMSIS __disable_irq operation (shown in the decompile as disableIRQinterrupts), calls vcu_flash_erase_range with the address and length that arrive unchanged in r0 and r1, and returns 2 if that call reports failure or 0 otherwise. It re-enables interrupts before returning, so no interrupt handler runs while the flash is being erased.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash start address, passed through in r0 |
| `param_2` | `u32` | length in bytes, passed through in r1 |

**Returns** `u32`: 0 on success, 2 when a page erase failed

**Notes:** The decompile shows no parameters because the arguments are passed through registers. Caller: vcu_fw_update_frame_handler.

- Addresses by version: 148: 0x080055F8, 14a: 0x08005A18, 14b: 0x08005D70, 14e: 0x08005DA8, 14f: 0x08005E04, 152: 0x08005E84, 153: 0x08005F20, 0159: 0x080060A4
- Called by: `vcu_fw_update_frame_handler`
- Calls: `vcu_flash_erase_range`
- Confidence: high

## vcu_flash_page_count

**Ceiling division of a byte count by 1024**

Returns param_1 >> 10, plus 1 if any of the low 10 bits are set, i.e. ceil(param_1 / 1024). 1 KiB is the AT32F415 flash erase page size, so this converts an image length to the number of pages to erase/program. Called from vcu_0159_08005b40.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | size in bytes |

**Returns** `u32`: number of 1 KiB pages

- Addresses by version: 148: 0x0800512C, 14a: 0x08005518, 14b: 0x08005840, 14e: 0x08005878, 14f: 0x080058D4, 152: 0x0800592C, 153: 0x080059C8, 0159: 0x08005B2C
- Called by: `vcu_flash_erase_range`
- Confidence: high

## vcu_flash_program_verified

**Program a halfword buffer to flash, verifying each halfword by readback**

Unlocks flash, then for each halfword calls flash_halfword_program to write the source value to the destination address, continuing only while the call returns the done status (3) and the flash readback equals the source value. It locks flash again at the end. It returns true only when the full byte count was programmed and verified, counting 2 bytes per halfword.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | flash destination address |
| `param_2` | `ptr` | source buffer of halfwords |
| `param_3` | `u32` | number of bytes to program |

**Returns** `bool`: true when every halfword was programmed and read back equal

**Notes:** Callers: vcu_fw_update_frame_handler (staging writes), vcu_upgrade_record_store and vcu_0159_08007D88 (not described).

- Addresses by version: 148: 0x08005358, 14a: 0x08005744, 14b: 0x08005A6C, 14e: 0x08005AA4, 14f: 0x08005B00, 152: 0x08005B58, 153: 0x08005BF4, 0159: 0x08005D58
- Called by: `vcu_fw_update_frame_handler`, `vcu_upgrade_record_store`, `vcu_flash_record_pingpong_save`
- Calls: `flash_halfword_program`, `flash_lock`, `flash_unlock`
- Confidence: high

## vcu_flash_record_pingpong_save

**Save the 512-byte record to alternating flash half-pages at 0x0801F000 and 0x0801F400**

Saves the 512-byte RAM record at DAT_20001ab4 to flash in two alternating slots. It increments the generation counter DAT_20001022, copies it to DAT_20001cb2, and stores a checksum of the record (vcu_sum_s16_minus_trailer over 256 s16 words, which also subtracts the words at index 250 and 251) in DAT_20001ca8 and DAT_20001caa. With interrupts disabled, an even generation writes to 0x0801F000 and an odd generation to 0x0801F400: each write first calls vcu_0159_08005b40 on the 512-byte target and, only if that succeeds, vcu_0159_08005d58 with the record. The matching generation word DAT_20001024 (even) or DAT_20001026 (odd) is updated only when both calls succeed.

**Notes:** vcu_0159_08005b40 and vcu_0159_08005d58 are not yet described; they are taken to be a flash pre-check and a flash program step from their arguments. The checksum is stored but not written into the record here.

- Addresses by version: 148: 0x0800735C, 14a: 0x08007798, 14b: 0x08007AFC, 14e: 0x08007B34, 14f: 0x08007B90, 152: 0x08007C54, 153: 0x08007CF0, 0159: 0x08007D88
- Called by: `vcu_pending_settings_commit`, `vcu_revolution_stage_tracker`, `vcu_0159_080047ac`, `vcu_0159_080054ec`, `vcu_config_ab_slot_load`, `vcu_crypto_identity_record_init`, `vcu_fw_update_frame_handler`, `vcu_0159_08009da8`
- Calls: `vcu_sum_s16_minus_trailer`, `vcu_flash_erase_range`, `vcu_flash_program_verified`
- Confidence: medium

## vcu_flash_usd_reset_if_unprotected

**Erase the user system data block if the argument is set and read-out protection is off**

When the argument is nonzero and flash_fap_status_get reports a value other than 1 (flash access protection not active), it unlocks flash, calls flash_user_system_data_erase(1) and locks flash again. In every other case it does nothing.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | nonzero to allow the user system data erase |

**Notes:** flash_user_system_data_erase also restores the FAP halfword, so this path can change the read-out protection state. The caller, vcu_0159_0800D858, is not described, so the intent of the erase is not established.

- Addresses by version: 148: 0x08005190, 14a: 0x0800557C, 14b: 0x080058A4, 14e: 0x080058DC, 14f: 0x08005938, 152: 0x08005990, 153: 0x08005A2C, 0159: 0x08005B90
- Called by: `vcu_0159_0800d858`
- Calls: `flash_user_system_data_erase`, `flash_fap_status_get`, `flash_lock`, `flash_unlock`
- Confidence: medium

## vcu_upgrade_record_store

**Erase and rewrite the 12-byte upgrade record at flash 0x0801F800, interrupts masked**

Masks interrupts, erases the one-page record area at 0x0801F800 with vcu_flash_erase_range, and when the erase succeeds programs the 12-byte RAM record DAT_200020D0 to DAT_200020D8 into it with vcu_flash_program_verified. It re-enables interrupts and returns.

**Notes:** The decompile is void, but the caller in vcu_fw_update_frame_handler uses the register left by the last flash call as a success flag, so a failed erase (0) is reported as status 3. Callers: vcu_crypto_identity_record_init and vcu_fw_update_frame_handler.

- Addresses by version: 148: 0x08005B40, 14a: 0x08005F60, 14b: 0x080062B8, 14e: 0x080062F0, 14f: 0x0800634C, 152: 0x080063CC, 153: 0x08006468, 0159: 0x080065B4
- Called by: `vcu_crypto_identity_record_init`, `vcu_fw_update_frame_handler`
- Calls: `vcu_flash_erase_range`, `vcu_flash_program_verified`
- Confidence: high
