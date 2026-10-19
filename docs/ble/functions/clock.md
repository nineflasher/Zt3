# BLE - `clock` functions

6 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`bes_clk_measure_hz`](#bes_clk_measure_hz) | 0x0C032F0C | Estimate a clock frequency in Hz by timing a counter window of param_1 ms |
| [`bes_cmu_get_sysclk_effective`](#bes_cmu_get_sysclk_effective) | 0x0C032D34 | Return the effective system-clock level: holder request (0 as 3) raised to the floor |
| [`bes_cmu_get_sysclk_request`](#bes_cmu_get_sysclk_request) | 0x0C032D18 | Return the raw clock-level request of the current maximum holder |
| [`bes_cmu_init_periph_pair`](#bes_cmu_init_periph_pair) | 0x0C032EE8 | Bring up two peripheral blocks at 0x40002000 and 0x40003000 and set AON bit 18 |
| [`bes_cmu_request_sysclk`](#bes_cmu_request_sysclk) | 0x0C032C04 | Record one user's system-clock level request (0..7) and apply the new effective level |
| [`hal_cmu_get_freq_name`](#hal_cmu_get_freq_name) | 0x0C032D64 | Map a CMU frequency index (0..7) to its name string |

## bes_clk_measure_hz

**Estimate a clock frequency in Hz by timing a counter window of param_1 ms**

Reads two rates from RAM-patch thunks (0x2000022C into uVar3 and 0x20000238 into uVar4) and forms the reference count uVar4 * ms / 1000 for a window of param_1 ms, where 0 means 10 ms. It runs a timed count through thunk 0x200002CC inside a BASEPRI section with count argument (ms * (uVar3 >> 2)) / 1000 and flag 0x40, then returns (uVar3 / measured) * reference, clamped at zero, using VFP float math. With param_2 == 0 the estimate is rounded to the nearest 1 MHz; with param_2 != 0 the raw estimate is returned, refined through a 64-bit product and helper 0x0C06FEC0 when the timer produced a second count. The meaning of the two thunk rates is inferred from the arithmetic (a 24 MHz class clock and a 32 kHz class reference are plausible but not confirmed).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | measurement window in ms (0 means 10) |
| `param_2` | `u32` | 0 = round to MHz, nonzero = raw or refined estimate |

**Returns** `u32`: estimated frequency in Hz

**Notes:** Thunk targets and helper 0x0C06FEC0 are not named. The 1 MHz rounding is literal in the code.

- Addresses by version: 219: 0x0C032F0C
- Called by: `ble_219_0c0399b4`
- Calls: `__udivdi3`, `ble_ram_patch_thunk_20000238`, `ble_ram_patch_thunk_200002cc`, `ble_ram_patch_thunk_2000022c`
- Confidence: low

## bes_cmu_get_sysclk_effective

**Return the effective system-clock level: holder request (0 as 3) raised to the floor**

When a holder is recorded it takes that holder's request from the table at 0x20003D24, maps 0 to 3, and returns the larger of the result and the floor byte DAT_20003545. With no holder (index 37) it returns the RAM-patch thunk 0x20000934 value unchanged. This is the level that bes_cmu_request_sysclk compares and applies through bes_cmu_set_sysclk_cfg.

**Returns** `u32`: effective system clock level

- Addresses by version: 219: 0x0C032D34
- Called by: `ble_219_0c0399b4`
- Calls: `ble_ram_patch_thunk_20000934`
- Confidence: high

## bes_cmu_get_sysclk_request

**Return the raw clock-level request of the current maximum holder**

Returns the table value of the current maximum holder (DAT_20003544 indexes the byte table at 0x20003D24) without the zero-to-3 mapping or the floor. When no holder is recorded (index 37) it returns the value of RAM-patch thunk 0x20000934 instead. It takes no lock and is the read side of bes_cmu_request_sysclk.

**Returns** `u32`: raw level request 0..7 of the holder, or the thunk value when there is none

- Addresses by version: 219: 0x0C032D18
- Called by: `ble_219_0c0459fc`
- Calls: `ble_ram_patch_thunk_20000934`
- Confidence: high

## bes_cmu_init_periph_pair

**Bring up two peripheral blocks at 0x40002000 and 0x40003000 and set AON bit 18**

Clears bit 9 of CMU register 0x4000005C (bes_cmu_reg5c_clear_bit9), writes 0x82 to 0x40002008, sets bit 10 of 0x4000005C (bes_cmu_reg5c_set_bit10), writes 0x82 to 0x40003008, and then sets bit 18 of 0x4008001C inside a BASEPRI critical section. The 0x82 control value and the two blocks are not documented in this packet, so their purpose is inferred from the sequence as a clock or reset release for two sub-blocks. The only caller in the packet is ble_219_0c03ab80.

- Addresses by version: 219: 0x0C032EE8
- Peripheral registers: `0x40002000` (A), `0x40002008` (W), `0x40003008` (W), `0x4008001c` (RW)
- Called by: `ble_219_0c03ab80`
- Calls: `bes_cmu_reg5c_clear_bit9`, `bes_cmu_reg5c_set_bit10`
- Confidence: medium

## bes_cmu_request_sysclk

**Record one user's system-clock level request (0..7) and apply the new effective level**

Stores the requested level param_2 for user index param_1 (0..36) in the byte table at 0x20003D24 and keeps the index of the maximum requester in DAT_20003544 (37 means none). A request of 0 counts as 3, and the effective level is the larger of the maximum request and the floor byte DAT_20003545. When the effective level changes, bes_cmu_set_sysclk_cfg (0x0C040BC8) applies it; RAM-patch hook 0x20000738 runs before that call when the clock rises and after it when the clock falls. If the previous maximum holder lowers its request the table is rescanned over indices 0..36 for the new maximum. The update runs in a BASEPRI critical section and is the write side of bes_cmu_get_sysclk_request and bes_cmu_get_sysclk_effective.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | user index 0..36 |
| `param_2` | `u32` | requested level 0..7 (0 counts as 3) |

**Returns** `u32`: 0 ok, 1 user index above 36, 2 level above 7

**Notes:** RAM-patch thunk 0x20000934 supplies the value when no holder is recorded; its meaning is not identified.

- Addresses by version: 219: 0x0C032C04
- Called by: `ble_219_0c03ab80`, `ble_219_0c03bb70`
- Calls: `bes_cmu_set_sysclk_cfg`, `ble_ram_patch_thunk_20000934`, `ble_ram_patch_thunk_20000738`
- Confidence: medium

## hal_cmu_get_freq_name

**Map a CMU frequency index (0..7) to its name string**

Returns the entry at index param_1 of the pointer table at 0x0c080924 whose strings are "CMU_FREQ_32K", "CMU_FREQ_6P5M", "CMU_FREQ_13M", "CMU_FREQ_26M", "CMU_FREQ_52M", "CMU_FREQ_78M", "CMU_FREQ_104M", "CMU_FREQ_208M"; returns NULL for index >= 8. Used for trace output of the system clock selection (single caller 0x0c0459fc).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | CMU frequency enum index 0..7 |

**Returns** `ptr`: C string name or NULL

**Notes:** Function name is derived (BES SDK style) - the string table is the evidence.

- Addresses by version: 219: 0x0C032D64
- Called by: `ble_219_0c0459fc`
- Confidence: medium
