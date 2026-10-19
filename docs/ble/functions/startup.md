# BLE - `startup` functions

20 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`NVIC_InitVectors`](#nvic_initvectors) | 0x0C046F24 | Relocate the vector table to SRAM 0x20000000 and point VTOR at it |
| [`Reset_Handler`](#reset_handler) | 0x0C028570 | Reset entry: set up the stack, clear .bss, copy .data from flash, run init, then spin |
| [`bes_boot_flag_get`](#bes_boot_flag_get) | 0x0C041CEC | Return the word at DAT_20000188 |
| [`bes_boot_flag_set`](#bes_boot_flag_set) | 0x0C041CE0 | Store a word to DAT_20000188 |
| [`bes_boot_magic_get`](#bes_boot_magic_get) | 0x0C041CD4 | Return the word at 0x2000017c |
| [`bes_boot_magic_is_valid`](#bes_boot_magic_is_valid) | 0x0C041CBC | Check whether the boot magic word at 0x2000017c equals 0x4f42494d |
| [`bes_boot_param_get`](#bes_boot_param_get) | 0x0C041CA8 | Return DAT_20000180 if param_1 == 0, else DAT_20000184 |
| [`ble_analog_chip_init`](#ble_analog_chip_init) | 0x0C03A038 | Boot-time analog and RF bring-up: read variant and OTP, unlock ISPI, program defaults, retune |
| [`ble_boot_early_init`](#ble_boot_early_init) | 0x0C045A34 | Early boot init: copy RAM code, clear state, relocate vectors, check boot magic |
| [`ble_boot_mode_set`](#ble_boot_mode_set) | 0x0C041D28 | Write the boot-mode word at 0x2000017C (0x61447055 or 0), ping the watchdog and restart RF |
| [`ble_boot_notice_log`](#ble_boot_notice_log) | 0x0C0459FC | Log boot notices: flash size, system clock name, and the raw reset reason |
| [`ble_chip_variant_probe`](#ble_chip_variant_probe) | 0x0C038D68 | Read the chip variant from OTP and return the high half of SYSREG 0x40080000 |
| [`ble_hw_init_stage0`](#ble_hw_init_stage0) | 0x0C0459D4 | Early hardware init stage 0: default pin map, GPDMA init, clear IRQ slots 3 and 4 |
| [`ble_soc_bringup_sequence`](#ble_soc_bringup_sequence) | 0x0C03AB80 | SoC bring-up: caches, IOMUX, clock and power, analog init, PLL and clock blocks, progress bits |
| [`bogomips_calibrate`](#bogomips_calibrate) | 0x0C035DA4 | Calibrate the busy-loop speed against SysTick and print the BogoMIPS value |
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
- Called by: `ble_boot_early_init`
- Calls: `startup_copy_vector_table_to_sram`
- Confidence: high

## Reset_Handler

**Reset entry: set up the stack, clear .bss, copy .data from flash, run init, then spin**

Reset vector of the BLE image. It calls startup_init_main_stack (mask IRQs, set MSP and MSPLIM, select thread mode), ble_219_0c045a34 (undescribed here) and startup_empty_hook. It zeroes 0x14B2C bytes of RAM from 0x20004A18 with memset (the .bss) and copies 0xC8C bytes of initialised data from flash 0x0C0899D8 to RAM 0x20003D88 with memcpy (the .data). It then calls ble_219_0c045aac (empty), ble_219_0c047fec (undescribed here, it leads to the application task setup) and ble_219_0c070204 (undescribed, presumably starts the RTOS scheduler). The final infinite loop is reached only if ble_219_0c070204 returns.

**Notes:** Sizes and addresses are literal arguments of the memset and memcpy calls. The role of ble_219_0c070204 and ble_219_0c045a34 is inferred from position only.

- Addresses by version: 219: 0x0C028570
- Vector: `Reset_Handler`
- Calls: `startup_init_main_stack`, `startup_empty_hook`, `ble_boot_early_init`, `startup_empty_hook_0c045aac`, `app_system_init`, `ble_219_0c070204`, `memcpy`, `memset`
- Confidence: high

## bes_boot_flag_get

**Return the word at DAT_20000188**

Returns DAT_20000188 (written by bes_boot_flag_set). Called from ble_219_0c0459fc and ble_219_0c046884.

**Returns** `u32`: value of DAT_20000188

- Addresses by version: 219: 0x0C041CEC
- Called by: `ble_boot_notice_log`, `app_boot_reason_decode`
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
- Called by: `ble_boot_early_init`
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
- Called by: `ble_version_info_print`
- Confidence: medium

## ble_analog_chip_init

**Boot-time analog and RF bring-up: read variant and OTP, unlock ISPI, program defaults, retune**

Boot-time analog and RF bring-up. It first runs ble_analog_cal_0x4059_ramp, then sets DAT_20003D6C to 2 if bit 0 of the saved status nibble (hal_pmu_get_saved_status_nibble) is set, to 4 if only bit 1 is set, and otherwise to the bits 1..3 of register 0x305F mapped to 1, 0x20, 8, 0x10 or 0. It sets DAT_20003D6D when bit 0 of register 0x3061 is clear, caches register 0x305E in DAT_20003D68, and stores a boot record with bes_boot_flag_set unless bes_boot_magic_get returns 0x4F42494D. It reads OTP field 1 through thunk 0x2000067C, checks it with thunk 0x2000065C, and selects a ROM configuration word with hal_chip_select_cfg_word from its top two bits (0 on a failed check). It halts if ble_219_0c040378 returns non-zero, then unlocks the analog ISPI by writing 0xCAFE and 0x5FEE to 0x3000, 0x2000 and 0x1000 with 500-unit settle delays between them. If the measured reference clock differs from the nominal 24 MHz it reloads the synthesiser ratio through ble_rf_synth_load_ratio48, and finally it writes defaults to 0x2159, 0x215A, 0x215B and 0x216E (trim code 4) and clears bits 3..5 of 0x2146.

**Notes:** ble_219_0c040378 is not described in this packet. The meanings of the saved-nibble bits and of the ROM words at 0x0C08607C are inferred.

- Addresses by version: 219: 0x0C03A038
- Called by: `ble_soc_bringup_sequence`
- Calls: `hal_pmu_get_saved_status_nibble`, `hal_chip_select_cfg_word`, `hal_cmu_get_crystal_freq`, `ble_analog_cal_0x4059_ramp`, `ble_rf_synth_load_ratio48`, `hal_analogif_reg_read`, `hal_analogif_reg_write`, `hal_analogif_check_chip_id`, `bes_boot_magic_get`, `bes_boot_flag_set`, `__udivdi3`, `ble_ram_patch_thunk_2000065c`, `ble_ram_patch_thunk_200005a8`, `ble_ram_patch_thunk_2000022c`, `ble_ram_patch_thunk_200007a8`, `ble_ram_patch_thunk_2000067c` ...
- Confidence: medium

## ble_boot_early_init

**Early boot init: copy RAM code, clear state, relocate vectors, check boot magic**

Early boot initialisation. Steps in order: select system mode 1 (bes_sysreg_select_mode1), copy 0x3390 bytes of code and data from flash at 0x0C086648 to RAM at 0x200001C0 (the RAM-resident routines reached through the thunks), issue DSB and ISB, and clear 0x838 bytes of state at 0x20003550. It then calls ble_219_0c03ab80, NVIC_InitVectors (relocates the vector table to SRAM 0x20000000), ble_219_0c03a2a0 and ble_219_0c037d08, and checks the boot magic with bes_boot_magic_is_valid. When that check returns 0 it calls scb_init_fpu_faults and returns 0; otherwise it returns the check result unchanged.

**Returns** `s32`: 0 on success, otherwise the nonzero boot-check result

**Notes:** The polarity of bes_boot_magic_is_valid is unclear: the normal path appears to run when it returns 0, which conflicts with its name. The error path is therefore medium confidence.

- Addresses by version: 219: 0x0C045A34
- Called by: `Reset_Handler`
- Calls: `ble_rf_analog_init`, `ble_rf_radio_init`, `scb_init_fpu_faults`, `ble_soc_bringup_sequence`, `bes_sysreg_select_mode1`, `bes_boot_magic_is_valid`, `NVIC_InitVectors`, `memcpy`, `memset`
- Confidence: medium

## ble_boot_mode_set

**Write the boot-mode word at 0x2000017C (0x61447055 or 0), ping the watchdog and restart RF**

Writes the marker 0x61447055 (bytes 'U','p','D','a') to DAT_2000017C when param_1 is non-zero, or 0 when it is zero. The normal boot check (bes_boot_magic_is_valid) expects 0x4F42494D, so this is a different boot-mode request. The function then pings the watchdog with hal_wdt_ping, raises BASEPRI with rtos_enter_critical and does not release it here, and restarts the RF front end with ble_rf_front_end_start. Returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero writes the 'UpDa' marker 0x61447055 to 0x2000017C, zero clears the word |

**Returns** `s32`: always 0

**Notes:** The 'UpDa' reading as an upgrade request is an inference from the ASCII value. BASEPRI is left at 0x40 on return, so the caller runs with the raised priority unless it restores it.

- Addresses by version: 219: 0x0C041D28
- Called by: `nb_upgrade_process_cmd`, `ble_fmna_cmd_handler`, `ble_vcu_cmd_handle`, `ble_factory_test_dispatch_set`, `ble_fmna_debug_cmd_dispatch`, `ble_bts_task_periodic_check`, `ble_host_stall_watchdog`
- Calls: `ble_rf_front_end_start`, `rtos_enter_critical`, `hal_wdt_ping`
- Confidence: medium

## ble_boot_notice_log

**Log boot notices: flash size, system clock name, and the raw reset reason**

Boot diagnostics. It logs 'NOTICE:chip flash size %d,chip freq:%s' with the value returned by ble_ram_call_2000110c_arg0 (ble_219_0c045AC0) and the name of the current maximum system clock, from bes_cmu_get_sysclk_request and hal_cmu_get_freq_name. It then logs 'NOTICE:reset raw reason:%x' with bes_boot_flag_get. It only logs and has no other side effects.

**Notes:** The annotation of ble_ram_call_2000110c_arg0 says it returns void, but the decompile uses a return value as the flash size. The flash size interpretation depends on that RAM routine.

- Addresses by version: 219: 0x0C0459FC
- Called by: `app_system_init`
- Calls: `bes_cmu_get_sysclk_request`, `hal_cmu_get_freq_name`, `trace_printf`, `bes_boot_flag_get`, `ble_ram_call_2000110c_arg0`
- Confidence: medium

## ble_chip_variant_probe

**Read the chip variant from OTP and return the high half of SYSREG 0x40080000**

Performs a read of register 0x3000 whose result is discarded, then loads the hardware variant into DAT_20003D64 with bes_otp_load_variant and returns the upper 16 bits of peripheral register 0x40080000 from bes_sysreg_read_80000_hi16. It is called from ble_219_0c02ed2c during early chip initialisation.

**Returns** `u32`: bits 31..16 of 0x40080000, zero-extended

**Notes:** Purpose of the discarded 0x3000 read is unclear; it may be a settle or wake read.

- Addresses by version: 219: 0x0C038D68
- Called by: `hal_sysreg_variant_select`
- Calls: `bes_otp_load_variant`, `hal_analogif_reg_read`, `bes_sysreg_read_80000_hi16`
- Confidence: medium

## ble_hw_init_stage0

**Early hardware init stage 0: default pin map, GPDMA init, clear IRQ slots 3 and 4**

Hardware bring-up step that only runs when its argument is 0. It applies the default pin table with ble_pin_config_table_apply(0), initialises both GPDMA controllers with hal_gpdma_init, clears the software IRQ handler slots 3 and 4 with hal_irq_install_handler (NULL handler), and calls ble_219_0c0420d0 (not described here). A non-zero argument returns at once.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | init stage; only 0 does work |

**Notes:** Callers are ble_219_0c0420d0 and ble_219_0c047fec, and this function also calls ble_219_0c0420d0, so the two are mutually linked. That loop is not fully traced.

- Addresses by version: 219: 0x0C0459D4
- Peripheral registers: `0xe000e100` (W), `0xe000e10d` (A), `0xe000e280` (W), `0xe000e40d` (W), `0xe000ed08` (R), `0xe000ed21` (W)
- Called by: `ble_irq13_pool_init`, `app_system_init`
- Calls: `hal_gpdma_init`, `ble_irq13_pool_init`, `ble_pin_config_table_apply`, `hal_irq_install_handler`
- Confidence: medium

## ble_soc_bringup_sequence

**SoC bring-up: caches, IOMUX, clock and power, analog init, PLL and clock blocks, progress bits**

Boot-time SoC bring-up. It enables cache 0 and cache 1 (hal_cache_enable), applies the default and level-2 IOMUX configuration, runs the clock and power register setup, brings up the bes_cmu peripheral pair, and checks the analog chip ID with hal_analogif_check_chip_id. A wrong chip ID sets bit 31 of 0x400000F4 and spins forever. Otherwise it selects the chip variant, runs ble_analog_chip_init, enables the crystal x2 and restarts PLL 0, retries hal_cmu_clk_block_8c_enable until it stops returning -1, and requests system clock level 7 for user 0. Each finished stage sets one bit of 0x400000F4 (bits 1 to 13), so boot progress can be read from that register.

**Notes:** The two stub hooks (hal_init_stub_ret0_a and _b) are also called and do nothing. The thunk at 0x0C073B90, called with argument 3, is not described in this packet.

- Addresses by version: 219: 0x0C03AB80
- Peripheral registers: `0x400000f4` (RW)
- Called by: `ble_boot_early_init`
- Calls: `hal_pmu_save_and_clear_status_nibble`, `hal_cache_enable`, `hal_init_stub_ret0_a`, `hal_init_stub_ret0_b`, `hal_sysreg_variant_select`, `bes_cmu_request_sysclk`, `bes_cmu_init_periph_pair`, `ble_analog_chip_init`, `hal_analogif_check_chip_id`, `bes_cmu_set_sysclk_cfg`, `bes_cmu_stub_return_0`, `hal_cmu_sys_pll_restart`, `bes_cmu_set_rega8_bit21`, `bes_sysreg_write_04_bit4`, `hal_cmu_osc_x2_enable`, `bes_hw_nop_hook` ...
- Confidence: medium

## bogomips_calibrate

**Calibrate the busy-loop speed against SysTick and print the BogoMIPS value**

Times the systick_measure_loop_us busy loop with DAT_20003E90 * 100 iterations, where DAT_20003E90 is a preset loops-per-microsecond estimate, halving the count while the SysTick measurement wraps (returns -1). A zero measurement prints 'failed'. Otherwise DAT_20003E90 becomes the measured loops per microsecond (integer part), DAT_20003E8C becomes 0xFFFFFFFF divided by it (the longest microsecond delay the busy wait can express) and the function prints the rate with two decimals and BogoMIPS as twice the rate, rounded. Output goes to the trace console.

**Notes:** The use of DAT_20003E8C as a delay limit is inferred; its consumers are not in this packet. The meaning of DAT_20003E90 as loops per microsecond is inferred from the printed value.

- Addresses by version: 219: 0x0C035DA4
- Called by: `vTaskStartScheduler`
- Calls: `trace_printf`, `systick_measure_loop_us`
- Confidence: medium

## scb_init_fpu_faults

**Configure SCB: enable FPU access, trap divide-by-zero, enable fault handlers**

Sets CPACR (0xE000ED88) |= 0xF00000 (full access to CP10/CP11, the FPU). In CCR (0xE000ED14) it sets DIV_0_TRP (bit 4) and BFHFNMIGN (bit 10) and clears UNALIGN_TRP (bit 3). In SHCSR (0xE000ED24) it enables UsageFault (bit 18), BusFault (bit 17) and MemManage (bit 16) handlers. Finally it zeroes the system-handler priority bytes at 0xE000ED18/19/1A (MemManage, BusFault, UsageFault) and the byte at 0xE000ED20, i.e. makes them the highest configurable priority. Called once from 0x0c045a34 (OS/system init).

**Notes:** Byte at 0xE000ED20 is zeroed in a SHPR3 byte lane; whether it is DebugMonitor/reserved was not determined.

- Addresses by version: 219: 0x0C03AB30
- Peripheral registers: `0xe000ed14` (RW), `0xe000ed18` (W), `0xe000ed19` (W), `0xe000ed1a` (W), `0xe000ed20` (W), `0xe000ed24` (RW), `0xe000ed88` (RW)
- Called by: `ble_boot_early_init`
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
- Called by: `Reset_Handler`
- Confidence: medium

## startup_empty_hook_0c045aac

**Empty function (single return)**

Contains only a return instruction; called once from ble_219_0c028570 as a placeholder hook (e.g. an unimplemented init/optional callback).

- Addresses by version: 219: 0x0C045AAC
- Called by: `Reset_Handler`
- Confidence: high

## startup_init_main_stack

**Reset-time CPU setup: mask IRQs, set MSP/MSPLIM, thread mode and stack selection**

Called once from the reset path (0x0c028570). Disables IRQs (CPSID i), and if privileged loads MSP with 0x20080000 (top of the 512 KB SRAM) and sets the main-stack limit MSPLIM to 0x2007ef00 (a 0x1100-byte main/ISR stack). It then sets CONTROL.nPRIV = 0 equivalent via setThreadModePrivileged(1) and, in thread mode, re-writes the stack-select bit (SPSEL) from the current stack in use, followed by an ISB. Always returns 0.

**Returns** `u32`: always 0

**Notes:** The decompiler intrinsics setThreadModePrivileged/setStackMode map to CONTROL register writes; exact CONTROL bit polarity not verified.

- Addresses by version: 219: 0x0C03AA74
- Called by: `Reset_Handler`
- Confidence: medium
