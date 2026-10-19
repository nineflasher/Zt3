# BLE - `startup` functions

13 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`NVIC_InitVectors`](#nvic_initvectors) | 0x0C046F24 | Relocate the vector table to SRAM 0x20000000 and point VTOR at it |
| [`bes_boot_flag_get`](#bes_boot_flag_get) | 0x0C041CEC | Return the word at DAT_20000188 |
| [`bes_boot_flag_set`](#bes_boot_flag_set) | 0x0C041CE0 | Store a word to DAT_20000188 |
| [`bes_boot_magic_get`](#bes_boot_magic_get) | 0x0C041CD4 | Return the word at 0x2000017c |
| [`bes_boot_magic_is_valid`](#bes_boot_magic_is_valid) | 0x0C041CBC | Check whether the boot magic word at 0x2000017c equals 0x4f42494d |
| [`bes_boot_param_get`](#bes_boot_param_get) | 0x0C041CA8 | Return DAT_20000180 if param_1 == 0, else DAT_20000184 |
| [`ble_analog_chip_init`](#ble_analog_chip_init) | 0x0C03A038 | Boot-time analog and RF bring-up: read variant and OTP, unlock ISPI, program defaults, retune |
| [`ble_chip_variant_probe`](#ble_chip_variant_probe) | 0x0C038D68 | Read the chip variant from OTP and return the high half of SYSREG 0x40080000 |
| [`scb_init_fpu_faults`](#scb_init_fpu_faults) | 0x0C03AB30 | Configure SCB: enable FPU access, trap divide-by-zero, enable fault handlers |
| [`startup_copy_vector_table_to_sram`](#startup_copy_vector_table_to_sram) | 0x0C046EEC | Copy the flash vector table into SRAM at 0x20000000 |
| [`startup_empty_hook`](#startup_empty_hook) | 0x0C03AA8E | Empty function (immediately returns), called during reset sequence |
| [`startup_empty_hook_0c045aac`](#startup_empty_hook_0c045aac) | 0x0C045AAC | Empty function (single return) |
| [`startup_init_main_stack`](#startup_init_main_stack) | 0x0C03AA74 | Reset-time CPU setup: mask IRQs, set MSP/MSPLIM, thread mode and stack selection |

## NVIC_InitVectors

**Relocate the vector table to SRAM 0x20000000 and point VTOR at it**

BES cmsis_nvic.c NVIC_InitVectors(): calls startup_copy_vector_table_to_sram to copy the flash vector table (0x0C028400) to 0x20000000, writes 0x20000000 to SCB->VTOR (0xE000ED08) and executes a DSB so later NVIC_SetVector-style patches of the RAM table take effect. Called from the early board/system init 0x0c045a34 right after .data/.bss setup.

- Addresses by version: 219: 0x0C046F24
- Peripheral registers: `0xe000ed08` (W)
- Called by: `ble_219_0c045a34`
- Calls: `startup_copy_vector_table_to_sram`
- Confidence: high

## bes_boot_flag_get

**Return the word at DAT_20000188**

Returns DAT_20000188 (written by bes_boot_flag_set). Called from ble_219_0c0459fc and ble_219_0c046884.

**Returns** `u32`: value of DAT_20000188

- Addresses by version: 219: 0x0C041CEC
- Called by: `ble_219_0c0459fc`, `app_boot_reason_decode`
- Confidence: medium

## bes_boot_flag_set

**Store a word to DAT_20000188**

Stores param_1 into DAT_20000188, a word in the early-SRAM boot info area read back by bes_boot_flag_get. Called from ble_219_0c03a038.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value to store |

**Notes:** Meaning of the value unknown.

- Addresses by version: 219: 0x0C041CE0
- Called by: `ble_analog_chip_init`
- Confidence: medium

## bes_boot_magic_get

**Return the word at 0x2000017c**

Returns DAT_2000017c unchanged (the boot magic/mode word compared by bes_boot_magic_is_valid). Called from ble_219_0c03a038.

**Returns** `u32`: value of DAT_2000017c

- Addresses by version: 219: 0x0C041CD4
- Called by: `ble_analog_chip_init`
- Confidence: medium

## bes_boot_magic_is_valid

**Check whether the boot magic word at 0x2000017c equals 0x4f42494d**

Returns DAT_2000017c == 0x4f42494d (bytes 'M','I','B','O' little-endian). Called from ble_219_0c045a34.

**Returns** `bool`: true when the magic matches

**Notes:** Meaning of the magic (reboot/boot-mode marker) is inferred.

- Addresses by version: 219: 0x0C041CBC
- Called by: `ble_219_0c045a34`
- Confidence: medium

## bes_boot_param_get

**Return DAT_20000180 if param_1 == 0, else DAT_20000184**

Selects one of two words in the early-SRAM boot/reboot info area (0x20000180 or 0x20000184) by index. Called from ble_219_0c041e38.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | 0 selects 0x20000180, nonzero selects 0x20000184 |

**Returns** `u32`: selected word

**Notes:** Content of the words not known.

- Addresses by version: 219: 0x0C041CA8
- Called by: `ble_219_0c041e38`
- Confidence: medium

## ble_analog_chip_init

**Boot-time analog and RF bring-up: read variant and OTP, unlock ISPI, program defaults, retune**

Boot-time analog and RF bring-up. It first runs ble_analog_cal_0x4059_ramp, then sets DAT_20003D6C to 2 if bit 0 of the saved status nibble (hal_pmu_get_saved_status_nibble) is set, to 4 if only bit 1 is set, and otherwise to the bits 1..3 of register 0x305F mapped to 1, 0x20, 8, 0x10 or 0. It sets DAT_20003D6D when bit 0 of register 0x3061 is clear, caches register 0x305E in DAT_20003D68, and stores a boot record with bes_boot_flag_set unless bes_boot_magic_get returns 0x4F42494D. It reads OTP field 1 through thunk 0x2000067C, checks it with thunk 0x2000065C, and selects a ROM configuration word with hal_chip_select_cfg_word from its top two bits (0 on a failed check). It halts if ble_219_0c040378 returns non-zero, then unlocks the analog ISPI by writing 0xCAFE and 0x5FEE to 0x3000, 0x2000 and 0x1000 with 500-unit settle delays between them. If the measured reference clock differs from the nominal 24 MHz it reloads the synthesiser ratio through ble_rf_synth_load_ratio48, and finally it writes defaults to 0x2159, 0x215A, 0x215B and 0x216E (trim code 4) and clears bits 3..5 of 0x2146.

**Notes:** ble_219_0c040378 is not described in this packet. The meanings of the saved-nibble bits and of the ROM words at 0x0C08607C are inferred.

- Addresses by version: 219: 0x0C03A038
- Called by: `ble_219_0c03ab80`
- Calls: `hal_pmu_get_saved_status_nibble`, `hal_chip_select_cfg_word`, `hal_cmu_get_crystal_freq`, `ble_analog_cal_0x4059_ramp`, `ble_rf_synth_load_ratio48`, `hal_analogif_reg_read`, `hal_analogif_reg_write`, `hal_analogif_check_chip_id`, `bes_boot_magic_get`, `bes_boot_flag_set`, `__udivdi3`, `ble_ram_patch_thunk_2000065c`, `ble_ram_patch_thunk_200005a8`, `ble_ram_patch_thunk_2000022c`, `ble_ram_patch_thunk_200007a8`, `ble_ram_patch_thunk_2000067c` ...
- Confidence: medium

## ble_chip_variant_probe

**Read the chip variant from OTP and return the high half of SYSREG 0x40080000**

Performs a read of register 0x3000 whose result is discarded, then loads the hardware variant into DAT_20003D64 with bes_otp_load_variant and returns the upper 16 bits of peripheral register 0x40080000 from bes_sysreg_read_80000_hi16. It is called from ble_219_0c02ed2c during early chip initialisation.

**Returns** `u32`: bits 31..16 of 0x40080000, zero-extended

**Notes:** Purpose of the discarded 0x3000 read is unclear; it may be a settle or wake read.

- Addresses by version: 219: 0x0C038D68
- Called by: `ble_219_0c02ed2c`
- Calls: `bes_otp_load_variant`, `hal_analogif_reg_read`, `bes_sysreg_read_80000_hi16`
- Confidence: medium

## scb_init_fpu_faults

**Configure SCB: enable FPU access, trap divide-by-zero, enable fault handlers**

Sets CPACR (0xE000ED88) |= 0xF00000 (full access to CP10/CP11, the FPU). In CCR (0xE000ED14) it sets DIV_0_TRP (bit 4) and BFHFNMIGN (bit 10) and clears UNALIGN_TRP (bit 3). In SHCSR (0xE000ED24) it enables UsageFault (bit 18), BusFault (bit 17) and MemManage (bit 16) handlers. Finally it zeroes the system-handler priority bytes at 0xE000ED18/19/1A (MemManage, BusFault, UsageFault) and the byte at 0xE000ED20, i.e. makes them the highest configurable priority. Called once from 0x0c045a34 (OS/system init).

**Notes:** Byte at 0xE000ED20 is zeroed in a SHPR3 byte lane; whether it is DebugMonitor/reserved was not determined.

- Addresses by version: 219: 0x0C03AB30
- Peripheral registers: `0xe000ed14` (RW), `0xe000ed18` (W), `0xe000ed19` (W), `0xe000ed1a` (W), `0xe000ed20` (W), `0xe000ed24` (RW), `0xe000ed88` (RW)
- Called by: `ble_219_0c045a34`
- Confidence: high

## startup_copy_vector_table_to_sram

**Copy the flash vector table into SRAM at 0x20000000**

Word-copy loop that reads consecutive 32-bit words from the vector table inside the RAW4TFT image (header + 0x400, starting at the initial-SP word) and stores them at 0x20000000, 0x20000004, ... It stops after the word that is vector_IRQ75_Handler has been copied, i.e. it relocates the exception table plus 75 IRQ entries to SRAM so handlers can be patched at run time. Called from ble_219_0c046f24 (early startup code).

**Notes:** Source start address is derived from raw4tft_header.padding+0x3cc, which decodes to the vector table at 0x0C028400.

- Addresses by version: 219: 0x0C046EEC
- Called by: `NVIC_InitVectors`
- Confidence: medium

## startup_empty_hook

**Empty function (immediately returns), called during reset sequence**

Contains only a return. It is called from the same reset routine (0x0c028570) as startup_init_main_stack, so it is most likely a placeholder for an optional early-init hook (for example an unused board/clock init) that was left empty in this build.

**Notes:** Purpose as hook is inferred from its sole caller only.

- Addresses by version: 219: 0x0C03AA8E
- Called by: `ble_219_0c028570`
- Confidence: medium

## startup_empty_hook_0c045aac

**Empty function (single return)**

Contains only a return instruction; called once from ble_219_0c028570 as a placeholder hook (e.g. an unimplemented init/optional callback).

- Addresses by version: 219: 0x0C045AAC
- Called by: `ble_219_0c028570`
- Confidence: high

## startup_init_main_stack

**Reset-time CPU setup: mask IRQs, set MSP/MSPLIM, thread mode and stack selection**

Called once from the reset path (0x0c028570). Disables IRQs (CPSID i), and if privileged loads MSP with 0x20080000 (top of the 512 KB SRAM) and sets the main-stack limit MSPLIM to 0x2007ef00 (a 0x1100-byte main/ISR stack). It then sets CONTROL.nPRIV = 0 equivalent via setThreadModePrivileged(1) and, in thread mode, re-writes the stack-select bit (SPSEL) from the current stack in use, followed by an ISB. Always returns 0.

**Returns** `u32`: always 0

**Notes:** The decompiler intrinsics setThreadModePrivileged/setStackMode map to CONTROL register writes; exact CONTROL bit polarity not verified.

- Addresses by version: 219: 0x0C03AA74
- Called by: `ble_219_0c028570`
- Confidence: medium
