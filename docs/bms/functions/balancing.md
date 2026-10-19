# BMS - `balancing` functions

1 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_balance_timer_step`](#bms_balance_timer_step) | (removed) | Advance the 30000-tick re-evaluation timer and update state bits 1 and 2 of DAT_20000504 |

## bms_balance_timer_step

**Advance the 30000-tick re-evaluation timer and update state bits 1 and 2 of DAT_20000504**

Advances a 30000-tick re-evaluation timer (DAT_20000510) for the state byte DAT_20000504. While bit 0 (enable) is clear it clears the timer and bit 1. While enabled it accumulates param_1, and when the timer reaches 30000 it restarts the timer and re-evaluates from the 16-bit values in the BMS state block at +0x104 (a percentage in which 100 means full), +0x11E and +0x19C. With bit 1 set it keeps the state while +0x104 is at or below +0x11E and otherwise clears bits 1 and 2; with bit 1 clear it clears bit 1 when the value is exactly 100, sets bit 2 when the value is at or below +0x19C (and bit 1 as well when it is at least 2 below), and clears bits 1 and 2 when it is above +0x19C. Present in the BMS_4130, BMS_4139 and BMS_4148 builds only.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | elapsed ticks since the last call |

**Notes:** The meaning of +0x104, +0x11E, +0x19C and of bits 1 and 2 is inferred from the timing and the comparisons; the function itself does not confirm it. The packet lists the state block accessor as bms_ram_20000bdc_addr, which is FUN_0800bb00 in this build.

- Addresses by version: 4130: 0x0800CC40, 4139: 0x0800D228, 4148: 0x0800E228
- Called by: `bms_4168_08008006`
- Calls: `bms_ram_20000bdc_addr`
- Confidence: medium
