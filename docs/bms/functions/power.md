# BMS - `power` functions

1 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`PWR_EnterSTOPMode`](#pwr_enterstopmode) | 0x080022F4 | Selects the PWR LPMS low-power mode, sets SLEEPDEEP and executes WFI or WFE to enter Stop |

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
- Called by: `bms_4168_0800a254`
- Confidence: medium
