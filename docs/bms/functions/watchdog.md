# BMS - `watchdog` functions

1 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`LL_IWDG_ReloadCounter`](#ll_iwdg_reloadcounter) | 0x0800A3B8 | Reload the independent watchdog by writing key 0xAAAA to IWDG_KR |

## LL_IWDG_ReloadCounter

**Reload the independent watchdog by writing key 0xAAAA to IWDG_KR**

Writes 0xAAAA to IWDG_KR (IWDG base 0x40003000), which restarts the independent watchdog counter. This matches the ST LL_IWDG_ReloadCounter routine exactly. Callers are bms_4168_080082f0 and bms_4168_0800aa5c.

- Addresses by version: 4130: 0x08009358, 4139: 0x08009858, 4148: 0x0800A0A4, 4168: 0x0800A3B8
- Peripheral registers: `IWDG.IWDG_KR` (W)
- Called by: `bms_4168_080082f0`, `bms_4168_0800aa5c`
- Confidence: high
