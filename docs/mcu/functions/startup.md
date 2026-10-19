# MCU - `startup` functions

5 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`Reset_Handler`](#reset_handler) | 0x08001188 | Cortex-M reset vector: system init, C runtime init, then application main |
| [`SystemInit`](#systeminit) | 0x0800A2AC | CMSIS SystemInit: reset the CRM clock tree to HICK, clear PLL and clock flags, set VTOR |
| [`__scatterload_decompress`](#__scatterload_decompress) | 0x08001ABC | Decompress a packed section (literals, zero runs, back-references) into RAM |
| [`app_main_thunk`](#app_main_thunk) | 0x08001178 | Tail-call thunk that jumps to the application main entry FUN_0800d548 |
| [`mcu_read_device_identity`](#mcu_read_device_identity) | 0x08008EA4 | Copy the 96-bit UID to RAM, check DBGMCU IDCODE against 0x700301C5 and store a UID checksum |

## Reset_Handler

**Cortex-M reset vector: system init, C runtime init, then application main**

Reset entry placed in vector slot 1. Calls FUN_0800a2ac (SystemInit-style clock/vector setup), then FUN_08001a98 (Keil __main/scatter-load: copies and decompresses initialised data, zeroes BSS), and finally FUN_0800d548 (application main). The last call is only reached if the scatter-load routine returns; it never returns in normal operation. Identical structure to the VCU Reset_Handler.

- Addresses by version: 12b: 0x08001188, 143: 0x08001188, 152: 0x08001188, 0160: 0x08001188
- Vector: `Reset_Handler`
- Confidence: high

## SystemInit

**CMSIS SystemInit: reset the CRM clock tree to HICK, clear PLL and clock flags, set VTOR**

Same as SystemInit in libraries/cmsis/cm4/device_support/system_at32f415.c, including its PWC prologue. Steps: enable the PWC clock (CRM APB1EN bit 28, PWCEN), set bit 2 of the byte at 0x40007050 (an address outside the PWC block in the repo SVD, not named), then disable the PWC clock. Then CRM->CTRL |= HICKEN and wait for HICKSTBL; select HICK as system clock (CFG.SCLKSEL = 0) and wait for SCLKSTS = 0; clear HEXTEN, HEXTBYPS, CFDEN and PLLEN (CTRL &= ~0x010D0000); set CFG = 0; PLL = 0x1F10; MISC1 = 0x00100000; and CLKINT = 0x009F0000 to clear the stability and CFD flags. Finally SCB->VTOR = 0x08000000 (flash base, no vector offset). Called from Reset_Handler (mcu_0160_08001188).

**Notes:** VTOR is set to 0x08000000. The MCU brief places the application at 0x08001000 behind a 4 KiB bootloader, so unless a vector offset is applied elsewhere the active vector table is the one at 0x08000000. Worth checking against the bootloader layout.

- Addresses by version: 12b: 0x0800A03C, 143: 0x0800A1EC, 152: 0x0800A238, 0160: 0x0800A2AC
- Peripheral registers: `0x40007050` (RW), `CRM.CTRL` (RW), `CRM.CFG` (RW), `CRM.CLKINT` (W), `CRM.APB1EN` (RW), `CRM.PLL` (W), `CRM.MISC1` (W), `SCB+0x8` (W)
- Called by: `mcu_0160_0800d548`
- Confidence: high

## __scatterload_decompress

**Decompress a packed section (literals, zero runs, back-references) into RAM**

ARM/Keil scatter-load decompressor, reached through the load-region table by function pointer (so it has no direct caller). Each token starts with a control byte: low 3 bits = literal count+1 (0 means the count is in the next byte), high nibble = run length (0 means next byte); the literals are copied first. If bit 3 is set the token ends with a copy of (run+2) bytes from the already-written output at distance given by the next byte (LZ77 back-reference), otherwise it emits run zero bytes. Loops until param_2 reaches param_2_start+param_3 and returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | compressed source stream |
| `param_2` | `ptr` | destination in RAM |
| `param_3` | `u32` | decompressed length in bytes |

**Returns** `u32`: always 0

**Notes:** Same algorithm as the VCU image's __scatterload_decompress.

- Addresses by version: 12b: 0x08001AA0, 143: 0x08001AA0, 152: 0x08001AA0, 0160: 0x08001ABC
- Confidence: high

## app_main_thunk

**Tail-call thunk that jumps to the application main entry FUN_0800d548**

Two-instruction veneer that branches to FUN_0800d548, the application main routine that is also the third call in Reset_Handler. It is called from the C-runtime scatter-load routine (mcu_0160_08001a98, the __main equivalent) once RAM sections are initialised. Same role as the VCU image's app_main_thunk.

- Addresses by version: 12b: 0x08001178, 143: 0x08001178, 152: 0x08001178, 0160: 0x08001178
- Called by: `mcu_0160_08001a98`
- Confidence: high

## mcu_read_device_identity

**Copy the 96-bit UID to RAM, check DBGMCU IDCODE against 0x700301C5 and store a UID checksum**

Copies the three UID words at 0x1FFFF7E8, 0x1FFFF7EC and 0x1FFFF7F0 to 0x20001FBC, 0x20001FC0 and 0x20001FC4, and again to 0x20001F44, 0x20001F48 and 0x20001F4C. It stores the expected IDCODE 0x700301C5 at 0x20001FB4 and reads DEBUG.DEBUG_IDCODE (0xE0042000) into 0x20001FB0; halfword 0x20001E1C becomes 1 when the read value equals 0x700301C5, otherwise 0. Finally it writes the bitwise NOT of the UID word sum, ~(uid0 + uid1 + uid2), to 0x200003B0. That word is the timeout counter of the MCU_152 build, so the value is used as a seed or check value for the device.

**Notes:** The IDCODE check confirms the expected Artery part. Why the UID checksum is stored in the timeout counter word is not explained by this packet (medium confidence on that point).

- Addresses by version: 12b: 0x08008C54, 143: 0x08008DF0, 152: 0x08008E30, 0160: 0x08008EA4
- Peripheral registers: `DEBUG.DEBUG_IDCODE` (R)
- Called by: `mcu_0160_0800b324`
- Confidence: high
