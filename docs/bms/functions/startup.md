# BMS - `startup` functions

7 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`NVIC_SystemReset`](#nvic_systemreset) | 0x08001444 | Disables interrupts and requests a system reset through SCB AIRCR, then hangs |
| [`Reset_Handler`](#reset_handler) | 0x080010D4 | Cortex-M0+ reset entry: runs three startup routines, then enters the main loop |
| [`bms_call_main_loop`](#bms_call_main_loop) | 0x080010C4 | Thunk that calls the endless BMS main loop bms_4168_08010558 |
| [`bms_hw_init_systick_prefetch`](#bms_hw_init_systick_prefetch) | 0x080021C4 | Enables flash prefetch, starts the 1 kHz SysTick at lowest priority, then runs UCPD setup |
| [`bms_peripheral_bringup`](#bms_peripheral_bringup) | 0x08008294 | Bring up IWDG, GPIO, ADC, TIM6/7, I2C, FDCAN, USART3 and SPI1 in turn |
| [`bms_startup_init_unpack`](#bms_startup_init_unpack) | 0x080012EC | Startup: runs two init-table hooks, then LZ-unpacks a stream before main |
| [`bms_vtor_reset_cause_latch`](#bms_vtor_reset_cause_latch) | 0x0800A260 | Set VTOR to 0x08001000, latch reset-cause flags into RAM, then call bms_hw_init_systick_prefetch |

## NVIC_SystemReset

**Disables interrupts and requests a system reset through SCB AIRCR, then hangs**

Calls disableIRQinterrupts (CPSID i), issues a data synchronisation barrier, writes 0x05FA0004 to SCB->AIRCR (VECTKEY 0x5FA in the high half, SYSRESETREQ set), issues another barrier and then loops forever while the reset takes effect. This is the CMSIS NVIC_SystemReset sequence with an added interrupt disable. Of its five callers, bms_4168_08008ca0 calls it when an FDCAN configuration step fails, so a failed CAN setup restarts the MCU.

- Addresses by version: 4130: 0x08001444, 4139: 0x08001444, 4148: 0x08001444, 4168: 0x08001444
- Peripheral registers: `SCB+0xc` (W)
- Called by: `bms_fdcan_nominal_500k_setup`, `bms_fdcan_add_mask_filter`, `bms_fdcan_filters_start`, `bms_sysclk_hse_pll_bringup`, `bms_sysclk_hsi16_switch`
- Confidence: high

## Reset_Handler

**Cortex-M0+ reset entry: runs three startup routines, then enters the main loop**

Reset vector target. It calls bms_4168_0800366a, then bms_4168_080012ec, then bms_4168_08010558 (the endless main loop), in that order. It has no inline .data copy or .bss clear of its own, so that work is presumed to be inside the first two callees. The decompiler warns that it may set the stack pointer, which is normal for a reset vector.

**Notes:** The roles of bms_4168_0800366a and bms_4168_080012ec are inferred from call order only; bms_4168_080012ec reaches the main loop through bms_call_main_loop.

- Addresses by version: 4130: 0x080010D4, 4139: 0x080010D4, 4148: 0x080010D4, 4168: 0x080010D4
- Vector: `Reset_Handler`
- Confidence: high

## bms_call_main_loop

**Thunk that calls the endless BMS main loop bms_4168_08010558**

A two-instruction stub: it calls bms_4168_08010558 and returns. The decompiler names it thunk_FUN_08010558, so the toolchain emitted a separate entry for the same target. Its only direct caller in this packet's call graph is bms_4168_080012ec, which therefore reaches the main loop through this address. The target never returns, so this stub does not return in practice either.

**Notes:** Behaviour of bms_4168_08010558 is taken from its own decompile in another packet (wave4), not verified here.

- Addresses by version: 4130: 0x080010C4, 4139: 0x080010C4, 4148: 0x080010C4, 4168: 0x080010C4
- Called by: `bms_startup_init_unpack`
- Confidence: high

## bms_hw_init_systick_prefetch

**Enables flash prefetch, starts the 1 kHz SysTick at lowest priority, then runs UCPD setup**

Sets bit 8 (PRFTEN) in the flash ACR register (the FLASH base word), then calls bms_systick_1khz_start (bms_4168_080021ec) with priority 3, the lowest. If that succeeds it calls bms_ucpd_clock_irq_setup (bms_4168_08002234) and ignores its result. The return value is true when the SysTick start failed, so the caller can treat it as an init error.

**Returns** `bool`: 1 when the SysTick could not be started

- Addresses by version: 4130: 0x080021C4, 4139: 0x080021C4, 4148: 0x080021C4, 4168: 0x080021C4
- Peripheral registers: `FLASH.ACR` (RW)
- Called by: `bms_vtor_reset_cause_latch`
- Calls: `bms_systick_1khz_start`, `bms_ucpd_clock_irq_setup`
- Confidence: high

## bms_peripheral_bringup

**Bring up IWDG, GPIO, ADC, TIM6/7, I2C, FDCAN, USART3 and SPI1 in turn**

Board initialisation run after the clock setup. In call order it calls bms_iwdg_start, bms_gpio_board_init, bms_adc_hw_init, bms_tim6_tim7_start, bms_i2c_bb_bus_init, bms_4168_08008B98 (FDCAN handle init), bms_4168_0800A574 (USART3 bring-up), bms_noop_hook_08009A98 and bms_spi1_master_init. Nothing is passed or returned, and each step depends on the clock set up earlier in the boot path.

**Notes:** The order is taken from the call sites in the decompile, and the names come from the existing entries for each address.

- Addresses by version: 4130: 0x08007248, 4139: 0x08007750, 4148: 0x08007F90, 4168: 0x08008294
- Called by: `bms_4168_08010558`
- Calls: `bms_adc_hw_init`, `bms_fdcan_nominal_500k_setup`, `bms_gpio_board_init`, `bms_i2c_bb_bus_init`, `bms_noop_hook_08009a98`, `bms_spi1_master_init`, `bms_iwdg_start`, `bms_tim6_tim7_start`, `bms_usart3_comm_init`
- Confidence: high

## bms_startup_init_unpack

**Startup: runs two init-table hooks, then LZ-unpacks a stream before main**

Walks a two-entry init table at 0x08010ACC and calls each entry's function pointer with its three argument words (the entries are probably block copy and fill operations). It then calls thunk_FUN_08010558 (bms_call_main_loop) and uses the return value as the compressed-stream pointer. The stream is decoded with the token format of bms_lzrle_decompress (bms_4168_08001310): a literal run, then a back-reference or a zero run, with extension bytes. Output goes from the RAM output pointer (shown as 0 in the decompile, probably the RAM base 0x20000000 named in the packet's RAM references) until the end pointer, and the function returns 0.

**Returns** `u32`: always 0

**Notes:** Two sources conflict: bms_call_main_loop (wave1) says its target never returns, yet this function uses the thunk's return value as a stream pointer and continues. Reset_Handler (wave1) calls this function before the main loop, which supports the decode being real. The decompiled output pointer starts at address 0. Verify the thunk target at bms_4168_08010558 before trusting either reading.

- Addresses by version: 4130: 0x080012EC, 4139: 0x080012EC, 4148: 0x080012EC, 4168: 0x080012EC
- Calls: `bms_call_main_loop`
- Confidence: low

## bms_vtor_reset_cause_latch

**Set VTOR to 0x08001000, latch reset-cause flags into RAM, then call bms_hw_init_systick_prefetch**

Sets the vector table offset SCB.VTOR to 0x08001000, the application image above the 4 KB bootloader. It then sets RAM flags from the RCC reset status register: 0x2000068C when SFTRSTF (bit 28) is set, 0x2000068D when IWDGRSTF (bit 29) is set, and 0x2000068E when PINRSTF (bit 26) is set. The flags are set to 1 here and never cleared, and the routine ends by calling bms_hw_init_systick_prefetch.

**Notes:** The bit positions follow the usual STM32G0 RCC_CSR layout, not a checked reference. Clearing of the reset flags is presumably done in bms_hw_init_systick_prefetch.

- Addresses by version: 4130: 0x08009200, 4139: 0x08009700, 4148: 0x08009F4C, 4168: 0x0800A260
- Peripheral registers: `RCC.CSR` (R), `SCB+0x8` (W)
- Called by: `bms_4168_080082f0`, `bms_system_clock_setup`
- Calls: `bms_hw_init_systick_prefetch`
- Confidence: high
