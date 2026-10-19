# VCU - `flash` functions

10 functions.

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
| [`vcu_flash_page_count`](#vcu_flash_page_count) | 0x08005B2C | Ceiling division of a byte count by 1024 |

## flash_fap_status_get

**Read the flash access-protection (read-out protection) status**

AT32 SDK flash_fap_status_get(): returns bit 1 of FLASH.USD (0x4002201c), the FAP flag: 1 when flash access protection is active. Called once by vcu_0159_08005b90 (purpose of the caller not examined).

**Returns** `u32`: 1 if FAP set, else 0

- Addresses by version: 148: 0x0800BFEC, 14a: 0x0800C430, 14b: 0x0800C8BC, 14e: 0x0800C950, 14f: 0x0800CA8C, 152: 0x0800CD18, 153: 0x0800CE0C, 0159: 0x0800CE78
- Peripheral registers: `FLASH.USD` (R)
- Called by: `vcu_0159_08005b90`
- Confidence: high

## flash_flag_clear

**Clear flash status flags (FLASH.STS)**

AT32 SDK flash_flag_clear(): writes param_1 to FLASH.STS (0x4002200c); the ODF, PRGMERR and EPPERR flags are write-1-to-clear. Called by vcu_0159_08005b40 (probably a flash program/erase routine).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | FLASH_xxx_FLAG mask (ODF/PRGMERR/EPPERR) |

- Addresses by version: 148: 0x0800BFFC, 14a: 0x0800C440, 14b: 0x0800C8CC, 14e: 0x0800C960, 14f: 0x0800CA9C, 152: 0x0800CD28, 153: 0x0800CE1C, 0159: 0x0800CE88
- Peripheral registers: `FLASH.STS` (W)
- Called by: `vcu_0159_08005b40`
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
- Called by: `vcu_0159_08005d58`
- Calls: `flash_operation_wait_for`
- Confidence: high

## flash_lock

**Set FLASH.CTRL.OPLK to lock the flash program/erase controller**

Read-modify-write of FLASH.CTRL (0x40022010, FLASH_REG_BASE+0x10) that sets bit 7 (OPLK) and leaves the other control bits unchanged. With OPLK set the controller refuses further erase and program operations until flash_unlock is called again. This is the Artery SDK flash_lock routine, written out as a single OR of the existing register value.

- Addresses by version: 148: 0x0800C02C, 14a: 0x0800C470, 14b: 0x0800C8FC, 14e: 0x0800C990, 14f: 0x0800CACC, 152: 0x0800CD58, 153: 0x0800CE4C, 0159: 0x0800CEB8
- Peripheral registers: `FLASH.PSR` (A), `FLASH.CTRL` (RW)
- Called by: `vcu_0159_08005b40`, `vcu_0159_08005b90`, `vcu_0159_08005d58`
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
- Called by: `vcu_0159_08005b40`
- Calls: `flash_operation_wait_for`
- Confidence: high

## flash_unlock

**Write the two flash unlock keys to FLASH.UNLOCK to enable erase and program**

Writes key1 0x45670123 and then key2 0xCDEF89AB to FLASH.UNLOCK (0x40022004). The controller unlocks only when the keys arrive in that order with no other write in between. This is the Artery SDK flash_unlock routine. It must be called before any flash_sector_erase or program sequence, and flash_lock (vcu_0159_0800ceb8) re-locks.

- Addresses by version: 148: 0x0800C0B0, 14a: 0x0800C4F4, 14b: 0x0800C980, 14e: 0x0800CA14, 14f: 0x0800CB50, 152: 0x0800CDDC, 153: 0x0800CED0, 0159: 0x0800CF3C
- Peripheral registers: `FLASH.PSR` (A), `FLASH.UNLOCK` (W)
- Called by: `vcu_0159_08005b40`, `vcu_0159_08005b90`, `vcu_0159_08005d58`
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
- Called by: `vcu_0159_08005b90`
- Calls: `flash_operation_wait_for`
- Confidence: high

## vcu_flash_page_count

**Ceiling division of a byte count by 1024**

Returns param_1 >> 10, plus 1 if any of the low 10 bits are set, i.e. ceil(param_1 / 1024). 1 KiB is the AT32F415 flash erase page size, so this converts an image length to the number of pages to erase/program. Called from vcu_0159_08005b40.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | size in bytes |

**Returns** `u32`: number of 1 KiB pages

- Addresses by version: 148: 0x0800512C, 14a: 0x08005518, 14b: 0x08005840, 14e: 0x08005878, 14f: 0x080058D4, 152: 0x0800592C, 153: 0x080059C8, 0159: 0x08005B2C
- Called by: `vcu_0159_08005b40`
- Confidence: high
