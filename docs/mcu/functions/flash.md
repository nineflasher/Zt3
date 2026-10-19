# MCU - `flash` functions

7 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`flash_flag_clear`](#flash_flag_clear) | 0x0800CB98 | Clear flash status flags by writing the mask to FLASH.STS |
| [`flash_halfword_program`](#flash_halfword_program) | 0x0800CBA4 | Program one halfword in internal flash: set PG, write, wait, clear PG |
| [`flash_lock`](#flash_lock) | 0x0800CBC8 | Lock the flash program and erase controller by setting FLASH.CTRL.OPLK |
| [`flash_operation_status_get`](#flash_operation_status_get) | 0x0800CBD8 | Report the state of the last flash operation from FLASH.STS |
| [`flash_operation_wait_for`](#flash_operation_wait_for) | 0x0800CC04 | Poll the flash status until it is no longer busy or the poll count runs out |
| [`flash_sector_erase`](#flash_sector_erase) | 0x0800CC80 | Erase the flash sector at an address: set SER, write FLASH.ADDR, start with ERSTRT, wait, clear SER |
| [`flash_unlock`](#flash_unlock) | 0x0800CCAC | Unlock the flash controller with the two-key sequence written to FLASH.UNLOCK |

## flash_flag_clear

**Clear flash status flags by writing the mask to FLASH.STS**

SDK flash_flag_clear. It writes the flag mask to FLASH.STS (0x4002200C). The status flags are cleared by this write, so it is used after a program or erase to acknowledge the operation-done and error flags before the next operation.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash status flag mask |

**Notes:** The packet shows the STS write only in MCU_143, MCU_152 and MCU_0160 builds.

- Addresses by version: 143: 0x0800CAF8, 152: 0x0800CB38, 0160: 0x0800CB98
- Peripheral registers: `FLASH.STS` (W)
- Called by: `mcu_0160_0800cc22`, `mcu_0160_0800ccc4`
- Confidence: high

## flash_halfword_program

**Program one halfword in internal flash: set PG, write, wait, clear PG**

SDK flash_halfword_program. It sets FLASH.CTRL bit 0 (FPRGM), writes the 16-bit value to the address, waits with flash_operation_wait_for(0x100000), and clears FPRGM. This build discards the wait status, so the function returns nothing.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | halfword-aligned flash address |
| `param_2` | `u16` | value to program |

- Addresses by version: 12b: 0x0800C8A0, 143: 0x0800CB04, 152: 0x0800CB44, 0160: 0x0800CBA4
- Peripheral registers: `FLASH.CTRL` (RW)
- Called by: `mcu_0160_0800ccc4`
- Calls: `flash_operation_wait_for`
- Confidence: high

## flash_lock

**Lock the flash program and erase controller by setting FLASH.CTRL.OPLK**

SDK flash_lock. It sets bit 7 (OPLK) of FLASH.CTRL (0x40022010), which locks the program and erase controller so that writes and erases are refused until flash_unlock is run again. Reads of flash are not affected.

- Addresses by version: 12b: 0x0800C8C4, 143: 0x0800CB28, 152: 0x0800CB68, 0160: 0x0800CBC8
- Peripheral registers: `FLASH.PSR` (A), `FLASH.CTRL` (RW)
- Called by: `mcu_0160_0800cc22`, `mcu_0160_0800ccc4`
- Confidence: high

## flash_operation_status_get

**Report the state of the last flash operation from FLASH.STS**

SDK flash_operation_status_get. It reads FLASH.STS (0x4002200C) and checks in this order: OBF (bit 0) set gives 0 (busy), PRGMERR (bit 2) gives 1 (program error), EPPERR (bit 4) gives 2 (erase/program protection error), and if none is set the result is 3 (operation done). A program error therefore wins over a protection error when both are set.

**Returns** `u32`: 0 busy, 1 program error, 2 EPP error, 3 operation done

- Addresses by version: 12b: 0x0800C8D4, 143: 0x0800CB38, 152: 0x0800CB78, 0160: 0x0800CBD8
- Peripheral registers: `FLASH.STS` (R)
- Called by: `flash_operation_wait_for`
- Confidence: high

## flash_operation_wait_for

**Poll the flash status until it is no longer busy or the poll count runs out**

SDK flash_operation_wait_for. It calls flash_operation_status_get repeatedly while the result is FLASH_OPERATE_BUSY (0) and the poll counter is non-zero, decrementing the counter on each poll. It returns the last status, or FLASH_OPERATE_TIMEOUT (4) when the counter reaches zero.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | poll count, passed in r0 by the callers (the decompiler shows the function as taking no argument) |

**Returns** `u32`: flash status: 0 busy, 1 program error, 2 EPP error, 3 done, 4 timeout

- Addresses by version: 12b: 0x0800C900, 143: 0x0800CB64, 152: 0x0800CBA4, 0160: 0x0800CC04
- Called by: `flash_halfword_program`, `flash_sector_erase`
- Calls: `flash_operation_status_get`
- Confidence: high

## flash_sector_erase

**Erase the flash sector at an address: set SER, write FLASH.ADDR, start with ERSTRT, wait, clear SER**

SDK flash_sector_erase. It sets FLASH.CTRL bit 1 (SER), writes the sector address to FLASH.ADDR, sets bit 6 (ERSTRT) to start the erase, waits with flash_operation_wait_for using a large poll count, and clears SER. This build discards the wait status.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | address of the sector to erase |

- Addresses by version: 12b: 0x0800C970, 143: 0x0800CBE0, 152: 0x0800CC20, 0160: 0x0800CC80
- Peripheral registers: `TMR2.CTRL1` (A), `FLASH.CTRL` (RW), `FLASH.ADDR` (W)
- Called by: `mcu_0160_0800cc22`
- Calls: `flash_operation_wait_for`
- Confidence: high

## flash_unlock

**Unlock the flash controller with the two-key sequence written to FLASH.UNLOCK**

SDK flash_unlock. It writes 0x45670123 and then 0xCDEF89AB to FLASH.UNLOCK (0x40022004). The controller clears its lock bit only when the two keys arrive in this order, which is the standard FPEC key pair. Program and erase operations are only accepted after this sequence and until flash_lock is called.

- Addresses by version: 12b: 0x0800C99C, 143: 0x0800CC0C, 152: 0x0800CC4C, 0160: 0x0800CCAC
- Peripheral registers: `FLASH.PSR` (A), `FLASH.UNLOCK` (W)
- Called by: `mcu_0160_0800cc22`, `mcu_0160_0800ccc4`
- Confidence: high
