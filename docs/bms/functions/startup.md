# BMS - `startup` functions

3 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`NVIC_SystemReset`](#nvic_systemreset) | 0x08001444 | Disables interrupts and requests a system reset through SCB AIRCR, then hangs |
| [`Reset_Handler`](#reset_handler) | 0x080010D4 | Cortex-M0+ reset entry: runs three startup routines, then enters the main loop |
| [`bms_call_main_loop`](#bms_call_main_loop) | 0x080010C4 | Thunk that calls the endless BMS main loop bms_4168_08010558 |

## NVIC_SystemReset

**Disables interrupts and requests a system reset through SCB AIRCR, then hangs**

Calls disableIRQinterrupts (CPSID i), issues a data synchronisation barrier, writes 0x05FA0004 to SCB->AIRCR (VECTKEY 0x5FA in the high half, SYSRESETREQ set), issues another barrier and then loops forever while the reset takes effect. This is the CMSIS NVIC_SystemReset sequence with an added interrupt disable. Of its five callers, bms_4168_08008ca0 calls it when an FDCAN configuration step fails, so a failed CAN setup restarts the MCU.

- Addresses by version: 4130: 0x08001444, 4139: 0x08001444, 4148: 0x08001444, 4168: 0x08001444
- Peripheral registers: `SCB+0xc` (W)
- Called by: `bms_4168_08008b98`, `bms_fdcan_add_mask_filter`, `bms_fdcan_filters_start`, `bms_sysclk_hse_pll_bringup`, `bms_sysclk_hsi16_switch`
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
- Called by: `bms_4168_080012ec`
- Confidence: high
