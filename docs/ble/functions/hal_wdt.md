# BLE - `hal_wdt` functions

7 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`hal_wdt_irq_enable`](#hal_wdt_irq_enable) | 0x0C03442C | Install watchdog IRQ vector and callback, then enable NVIC IRQ 5 |
| [`hal_wdt_ping`](#hal_wdt_ping) | 0x0C046830 | Reload watchdog 0 if the watchdog has been started |
| [`hal_wdt_set_reload_slot`](#hal_wdt_set_reload_slot) | 0x0C0343F8 | Store watchdog reload slot param_1 as RAM-patch ticks minus one, minimum 1 |
| [`hal_wdt_start`](#hal_wdt_start) | 0x0C034328 | Start the watchdog: unlock, reload, enable reset and interrupt, lock, set started flag |
| [`hal_wdt_stop`](#hal_wdt_stop) | 0x0C034388 | Disable the watchdog counter and clear the running flag |
| [`hal_wdt_task_checkin`](#hal_wdt_task_checkin) | 0x0C0362BC | Mark the running task in the check-in mask; ping the watchdog once all required tasks ran |
| [`hal_wdt_write_load`](#hal_wdt_write_load) | 0x0C0342D4 | Write the stored reload value of watchdog param_1 to the watchdog LOAD register |

## hal_wdt_irq_enable

**Install watchdog IRQ vector and callback, then enable NVIC IRQ 5**

Reads VTOR (0xe000ed08) and copies the handler address from table DAT_20003e28[param_1] into vector slot 0x54 (exception 21 = IRQ 5), issues a DSB, sets NVIC priority byte 0xe000e405 (IRQ5) to 0, clears pending (ICPR 0xe000e280 = 0x20) and enables the interrupt (ISER 0xe000e100 = 0x20). Finally stores the callback param_2 in DAT_2000aad8[param_1]. IRQ 5 is presumed to be the watchdog interrupt, matching the SP805 block used by neighbouring routines.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | index into handler table 0x20003e28 and callback table 0x2000aad8 |
| `param_2` | `ptr` | callback invoked from the watchdog interrupt |

- Addresses by version: 219: 0x0C03442C
- Peripheral registers: `0xe000e100` (W), `0xe000e280` (W), `0xe000e405` (W), `0xe000ed08` (R)
- Called by: `ble_219_0c046838`
- Confidence: medium

## hal_wdt_ping

**Reload watchdog 0 if the watchdog has been started**

If the flag/word DAT_2000aadc is non-zero, calls hal_wdt_write_load(0), which rewrites the stored timeout into the SP805-style LOAD register at 0x40082000 and thereby restarts the countdown. Always returns 0. DAT_2000aadc sits right after the timeout table at 0x2000aad4 and acts as the 'watchdog 0 started' indicator. Callers: 0x0c0362bc and 0x0c041d28 (periodic feed paths).

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C046830
- Called by: `hal_wdt_task_checkin`, `ble_219_0c041d28`
- Calls: `hal_wdt_write_load`
- Confidence: medium

## hal_wdt_set_reload_slot

**Store watchdog reload slot param_1 as RAM-patch ticks minus one, minimum 1**

Passes param_2 to RAM-patch thunk 0x20000570 and stores the result minus one into the reload table DAT_2000AAD4[param_1] (32-bit slots), or 1 when the result is 0 or 1. hal_wdt_write_load copies that slot into the LOAD register (0x40082000) on every reload. Called from ble_219_0c046838 (not described in this packet).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | reload slot index (table has two slots) |
| `param_2` | `u32` | time argument converted by the RAM-patch routine |

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C0343F8
- Called by: `ble_219_0c046838`
- Calls: `ble_ram_patch_thunk_20000570`
- Confidence: medium

## hal_wdt_start

**Start the watchdog: unlock, reload, enable reset and interrupt, lock, set started flag**

Reloads the counter with hal_wdt_write_load first. Then, under a BASEPRI section, it writes the SP805 unlock key 0x1ACCE551 to WDOGLOCK (0x40082C00), writes 3 (INTEN and RESEN) to WDOGCONTROL (0x40082008), writes 1 to WDOGINTCLR (0x4008200C) and writes 1 to 0x40082C00 to lock again. It sets the started flag DAT_2000AADC to 1 and returns the lock register read-back in the high word with 0 in the low word.

**Returns** `u64`: lock register read-back in bits 63..32, zero in bits 31..0

- Addresses by version: 219: 0x0C034328
- Peripheral registers: `0x40082008` (W), `0x4008200c` (W), `0x40082c00` (RW)
- Called by: `ble_219_0c046838`
- Calls: `hal_wdt_write_load`
- Confidence: high

## hal_wdt_stop

**Disable the watchdog counter and clear the running flag**

Runs in a critical section by raising BASEPRI to 0x40; if it was not already 0x40 it records the caller PC and LR in DAT_20003d70/20003d74 (lock-owner debug record) and, when BASEPRI was originally 0, resets DAT_20003d70 to 0xffffffff on exit; the previous BASEPRI is restored. Unlocks 0x40082c00 with 0x1acce551, writes 0 to 0x40082008 (CONTROL: counter and reset disabled), relocks with 1, then clears the running flag DAT_2000aadc. SP805-style watchdog block at 0x40082000: LOAD +0x00, CONTROL +0x08, LOCK +0xc00 (0x1acce551 unlocks).

- Addresses by version: 219: 0x0C034388
- Peripheral registers: `0x40082008` (W), `0x40082c00` (RW)
- Called by: `ble_219_0c03d69c`, `ble_219_0c046838`
- Confidence: medium

## hal_wdt_task_checkin

**Mark the running task in the check-in mask; ping the watchdog once all required tasks ran**

Called from RTOS paths at 0x0C02DC50, 0x0C02EB60, 0x0C0599D4 and 0x0C05D108. It takes the current TCB from xTaskGetCurrentTaskHandle (0x0C04462C). If monitoring is on (DAT_2000BAA4 nonzero) and the TCB lies in the static task table at 0x20004A18..0x20004B99, it sets bit (offset / 0x60) in DAT_2000BAA8. When every required task bit in DAT_2000BAAC is set (tasks in DAT_2000BAB0 are excluded), it calls hal_wdt_ping (0x0C046830) and clears DAT_2000BAA8, so the watchdog is fed only after all monitored tasks have run. The 0x60-byte stride is inferred from the division.

- Addresses by version: 219: 0x0C0362BC
- Called by: `ble_219_0c02dc50`, `ble_219_0c02eb60`, `ble_219_0c0599d4`, `ble_219_0c05d108`
- Calls: `xTaskGetCurrentTaskHandle`, `hal_wdt_ping`
- Confidence: medium

## hal_wdt_write_load

**Write the stored reload value of watchdog param_1 to the watchdog LOAD register**

Runs in a critical section by raising BASEPRI to 0x40; if it was not already 0x40 it records the caller PC and LR in DAT_20003d70/20003d74 (lock-owner debug record) and, when BASEPRI was originally 0, resets DAT_20003d70 to 0xffffffff on exit; the previous BASEPRI is restored. Unlocks the block by writing 0x1acce551 to 0x40082c00, stores the value from table DAT_2000aad4[param_1] into 0x40082000 (LOAD) and relocks by writing 1 to 0x40082c00. SP805-style watchdog block at 0x40082000: LOAD +0x00, CONTROL +0x08, LOCK +0xc00 (0x1acce551 unlocks). Called from the watchdog start/feed routines (0x0c034328, 0x0c046830).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | watchdog index into the timeout table at 0x2000aad4 |

**Notes:** Identification as an SP805 watchdog is based on the 0x1acce551 unlock key and register offsets.

- Addresses by version: 219: 0x0C0342D4
- Peripheral registers: `0x40082000` (W), `0x40082c00` (RW)
- Called by: `hal_wdt_start`, `hal_wdt_ping`
- Confidence: medium
