# MCU - `flash` functions

4 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`flash_flag_clear`](#flash_flag_clear) | 0x0800CB98 | Clear flash status flags by writing the mask to FLASH.STS |
| [`flash_lock`](#flash_lock) | 0x0800CBC8 | Lock the flash program and erase controller by setting FLASH.CTRL.OPLK |
| [`flash_operation_status_get`](#flash_operation_status_get) | 0x0800CBD8 | Report the state of the last flash operation from FLASH.STS |
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
- Called by: `mcu_0160_0800cc04`
- Confidence: high

## flash_unlock

**Unlock the flash controller with the two-key sequence written to FLASH.UNLOCK**

SDK flash_unlock. It writes 0x45670123 and then 0xCDEF89AB to FLASH.UNLOCK (0x40022004). The controller clears its lock bit only when the two keys arrive in this order, which is the standard FPEC key pair. Program and erase operations are only accepted after this sequence and until flash_lock is called.

- Addresses by version: 12b: 0x0800C99C, 143: 0x0800CC0C, 152: 0x0800CC4C, 0160: 0x0800CCAC
- Peripheral registers: `FLASH.PSR` (A), `FLASH.UNLOCK` (W)
- Called by: `mcu_0160_0800cc22`, `mcu_0160_0800ccc4`
- Confidence: high
