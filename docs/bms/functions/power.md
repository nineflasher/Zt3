# BMS - `power` functions

3 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`PWR_EnterSTOPMode`](#pwr_enterstopmode) | 0x080022F4 | Selects the PWR LPMS low-power mode, sets SLEEPDEEP and executes WFI or WFE to enter Stop |
| [`bms_enter_stop_mode`](#bms_enter_stop_mode) | 0x0800A254 | Enter STOP 0 with WFI through PWR_EnterSTOPMode |
| [`bms_pc7_enable_and_settle`](#bms_pc7_enable_and_settle) | 0x0800AA5C | Drive PC7 high, wait 2000 units, reload the watchdog, wait 1000 more units |

## PWR_EnterSTOPMode

**Selects the PWR LPMS low-power mode, sets SLEEPDEEP and executes WFI or WFE to enter Stop**

Writes PWR.CR1.LPMS (bits 2:0) with 0 when param_1 is 0 and with 1 otherwise, which selects one of the two Stop variants (0 and 1 are the ST HAL STOP0 and STOP1 choices). It then sets SCB SCR.SLEEPDEEP (0xE000ED10 bit 2), executes WFI when stop_entry is 1 and WFE twice otherwise, and clears SLEEPDEEP again after the core wakes. The function does not configure a wake source, so the caller must set up EXTI or RTC wake-up before calling it.

| Parameter | Type | Description |
|---|---|---|
| `lpms_select` | `u32` | 0 selects LPMS = 000 (STOP0), any other value LPMS = 001 (STOP1) |
| `stop_entry` | `u32` | 1 = enter with WFI, any other value = enter with WFE |

**Notes:** The name follows the ST HAL static PWR_EnterSTOPMode pattern (inferred from the body, not from a symbol). The decompile shows two WFE calls with no SEV before them; the HAL pattern is SEV, WFE, WFE, so the SEV is probably elided by the decompiler.

- Addresses by version: 4130: 0x080022F4, 4139: 0x080022F4, 4148: 0x080022F4, 4168: 0x080022F4
- Peripheral registers: `PWR.CR1` (RW), `SCB+0x10` (RW)
- Called by: `bms_enter_stop_mode`
- Confidence: medium

## bms_enter_stop_mode

**Enter STOP 0 with WFI through PWR_EnterSTOPMode**

Calls PWR_EnterSTOPMode(0, 1). Following the HAL convention, the first argument selects LPMS = 0 (STOP 0 with the main regulator) and the second selects WFI as the entry instruction. The core stays in STOP until an enabled interrupt wakes it, and the routine returns after that wake-up. The routine arms no wake source of its own, so the caller must configure one beforehand.

**Notes:** The argument meanings are inferred from the HAL signature, not from the packet. Caller is bms_4168_080082f0.

- Addresses by version: 4130: 0x080091F4, 4139: 0x080096F4, 4148: 0x08009F40, 4168: 0x0800A254
- Called by: `bms_4168_080082f0`
- Calls: `PWR_EnterSTOPMode`
- Confidence: medium

## bms_pc7_enable_and_settle

**Drive PC7 high, wait 2000 units, reload the watchdog, wait 1000 more units**

Enables the device on GPIOC pin 7 and waits for it to settle. It sets GPIOC.BSRR bit 7 (0x80) to drive PC7 high, waits 2000 units through bms_systick_wait_repeat, reloads the independent watchdog with LL_IWDG_ReloadCounter between the two waits, and then waits 1000 more units. If one unit is 1 ms, as DAT_20000688 * 1000 SysTick counts suggests, the total is about 3 s. The device on PC7 is not identified in this packet.

**Notes:** The 1 ms unit size and the GPIOC base address are inferred. The purpose of the device on PC7 is unknown.

- Addresses by version: 4130: 0x08009AF4, 4139: 0x0800A02C, 4148: 0x0800A748, 4168: 0x0800AA5C
- Called by: `bms_4168_080082f0`
- Calls: `bms_systick_wait_repeat`, `LL_IWDG_ReloadCounter`
- Confidence: medium
