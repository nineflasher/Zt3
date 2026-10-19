# BMS - `watchdog` functions

2 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`LL_IWDG_ReloadCounter`](#ll_iwdg_reloadcounter) | 0x0800A3B8 | Reload the independent watchdog by writing key 0xAAAA to IWDG_KR |
| [`bms_iwdg_start`](#bms_iwdg_start) | 0x0800A354 | Start the independent watchdog: /32 prescaler, reload 4000, wait for sync, then refresh |

## LL_IWDG_ReloadCounter

**Reload the independent watchdog by writing key 0xAAAA to IWDG_KR**

Writes 0xAAAA to IWDG_KR (IWDG base 0x40003000), which restarts the independent watchdog counter. This matches the ST LL_IWDG_ReloadCounter routine exactly. Callers are bms_4168_080082f0 and bms_4168_0800aa5c.

- Addresses by version: 4130: 0x08009358, 4139: 0x08009858, 4148: 0x0800A0A4, 4168: 0x0800A3B8
- Peripheral registers: `IWDG.IWDG_KR` (W)
- Called by: `bms_4168_080082f0`, `bms_pc7_enable_and_settle`
- Confidence: high

## bms_iwdg_start

**Start the independent watchdog: /32 prescaler, reload 4000, wait for sync, then refresh**

Configures and starts the IWDG. It fetches the status object from bms_ram_20000bdc_addr, writes 0xCCCC to IWDG_KR to start the watchdog and 0x5555 to unlock PR, RLR and WINR, and sets IWDG_PR to 3 (divide by 32) and IWDG_RLR to 4000. It polls IWDG_SR for the PVU, RVU and WVU flags for at most 15000 iterations. If the wait times out it sets bit 2 (0x4) in the 16-bit status word at +0x194 of that object, otherwise it clears the bit. It writes 4000 to IWDG_WINR, so the window equals the reload and imposes no early-refresh limit, then reloads the counter with 0xAAAA. With a LSI of about 32 kHz the timeout is roughly 4 s.

**Notes:** The 4 s figure assumes a 32 kHz LSI, which is the STM32G0 nominal value. The bit at +0x194 is written but its meaning is not decoded here.

- Addresses by version: 4130: 0x080092F4, 4139: 0x080097F4, 4148: 0x0800A040, 4168: 0x0800A354
- Peripheral registers: `IWDG.IWDG_KR` (W), `IWDG.IWDG_PR` (W), `IWDG.IWDG_RLR` (W), `IWDG.IWDG_SR` (R), `IWDG.IWDG_WINR` (W)
- Called by: `bms_4168_08008294`, `bms_4168_080082f0`
- Calls: `bms_ram_20000bdc_addr`
- Confidence: high
