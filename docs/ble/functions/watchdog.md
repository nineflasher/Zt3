# BLE - `watchdog` functions

1 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`ble_wdt_enable`](#ble_wdt_enable) | 0x0C046838 | Debug command enable_watchdog: stop when timeout below 2, else start with IRQ 5 callback |

## ble_wdt_enable

**Debug command enable_watchdog: stop when timeout below 2, else start with IRQ 5 callback**

Implements the 'enable_watchdog' command. A reload value below 2 stops the watchdog with hal_wdt_stop and returns 0. Otherwise, if the running flag at 0x2000F45C is not set, it stores the reload value in reload slot 0 with hal_wdt_set_reload_slot, starts the watchdog with hal_wdt_start, installs the watchdog callback on IRQ 5 with hal_wdt_irq_enable, prints 'enable_watchdog', and sets the running flag. A second call while running does nothing and returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | reload value: below 2 disables the watchdog |
| `param_2` | `u32` | unused |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | unused |

**Returns** `u32`: always 0

**Notes:** Callers are ble_219_0c036328 and ble_219_0c036394, which are not described here.

- Addresses by version: 219: 0x0C046838
- Called by: `wdt_task_monitor_register_current`, `wdt_task_monitor_enable`
- Calls: `hal_wdt_start`, `hal_wdt_stop`, `hal_wdt_set_reload_slot`, `hal_wdt_irq_enable`, `trace_printf`
- Confidence: medium
