# MCU - `watchdog` functions

5 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_watchdog_feed`](#mcu_watchdog_feed) | 0x08006194 | Refresh the watchdog by writing the 0xAAAA key to WDT.CMD |
| [`mcu_watchdog_start`](#mcu_watchdog_start) | 0x0800B4E8 | Start the independent watchdog with prescaler 128 and reload 0x61A (about 5 s on a 40 kHz LICK) |
| [`wdt_divider_set`](#wdt_divider_set) | 0x0800E3DC | Set the watchdog clock prescaler, WDT.DIV bits 2:0 |
| [`wdt_register_write_enable`](#wdt_register_write_enable) | 0x0800E3FC | Unlock (0x5555) or lock (0x0000) write access to the WDT DIV and RLD registers |
| [`wdt_reload_value_set`](#wdt_reload_value_set) | 0x0800E414 | Write the watchdog reload value to WDT.RLD (offset 0x08) |

## mcu_watchdog_feed

**Refresh the watchdog by writing the 0xAAAA key to WDT.CMD**

Writes the 16-bit refresh key 0xAAAA to the watchdog command register (WDT.CMD), which reloads the watchdog counter so it does not reset the MCU. This is the whole function. Called from mcu_0160_0800d548, the application main loop. Present in the 143, 152 and 0160 builds.

- Addresses by version: 143: 0x080060C4, 152: 0x080060F4, 0160: 0x08006194
- Peripheral registers: `WDT.CMD` (W)
- Called by: `mcu_0160_0800d548`
- Confidence: high

## mcu_watchdog_start

**Start the independent watchdog with prescaler 128 and reload 0x61A (about 5 s on a 40 kHz LICK)**

Initialises and starts the independent watchdog. It unlocks the WDT registers (wdt_register_write_enable with 0x5555), sets the prescaler to WDT_CLK_DIV_128 (code 5 in WDT.DIV), writes the reload value 0x61A (1562) with wdt_reload_value_set, re-locks the registers (0x0000), and writes 0xCCCC (WDT_CMD_ENABLE) to WDT.CMD to start the counter. With a LICK near 40 kHz the timeout is about 5 s.

**Notes:** The LICK frequency is not checked in this packet; the 5 s figure assumes the usual 40 kHz.

- Addresses by version: 143: 0x0800B484, 152: 0x0800B488, 0160: 0x0800B4E8
- Peripheral registers: `WDT.CMD` (W)
- Called by: `mcu_0160_0800d548`
- Calls: `wdt_divider_set`, `wdt_register_write_enable`, `wdt_reload_value_set`
- Confidence: high

## wdt_divider_set

**Set the watchdog clock prescaler, WDT.DIV bits 2:0**

Matches the Artery SDK wdt_divider_set. Read-modify-write of WDT.DIV (0x40003004): bits 2:0 are replaced with param_1 & 7 and the other bits are kept. The register is only writable after the unlock key is written to WDT.CMD (see mcu_0160_0800e3fc). Watchdog setup helper (group of three with wdt_register_write_enable and wdt_reload_value_set, all called from mcu_0160_0800b4e8).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | division code, 3 bits (wdt_division_type) |

**Notes:** The code-to-divide-ratio table is not in the repo register data. Only caller: mcu_0160_0800b4e8, which passes 5.

- Addresses by version: 143: 0x0800E204, 152: 0x0800E29C, 0160: 0x0800E3DC
- Peripheral registers: `WDT.DIV` (RW)
- Called by: `mcu_watchdog_start`
- Confidence: high

## wdt_register_write_enable

**Unlock (0x5555) or lock (0x0000) write access to the WDT DIV and RLD registers**

Matches the Artery SDK wdt_register_write_enable. A non-zero argument writes the unlock key 0x5555 to WDT.CMD so that DIV and RLD can be modified; a zero argument writes 0x0000 to lock them again. Both are plain stores to CMD. The caller mcu_0160_0800b4e8 uses it around wdt_divider_set and wdt_reload_value_set, then writes 0xCCCC to WDT.CMD to start the watchdog (the SDK wdt_enable). Watchdog setup helper (group of three with wdt_register_write_enable and wdt_reload_value_set, all called from mcu_0160_0800b4e8).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | non-zero = unlock, 0 = lock |

**Notes:** Only caller: mcu_0160_0800b4e8.

- Addresses by version: 143: 0x0800E224, 152: 0x0800E2BC, 0160: 0x0800E3FC
- Peripheral registers: `WDT.CMD` (W)
- Called by: `mcu_watchdog_start`
- Confidence: high

## wdt_reload_value_set

**Write the watchdog reload value to WDT.RLD (offset 0x08)**

Matches the Artery SDK wdt_reload_value_set. Stores param_1 into WDT.RLD at 0x40003008 with a full 32-bit write; the register data gives RLD as 12 bits, so only the low 12 bits take effect. It must follow wdt_register_write_enable with a non-zero argument or the write is ignored. Watchdog setup helper (group of three with wdt_register_write_enable and wdt_reload_value_set, all called from mcu_0160_0800b4e8).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | reload value, 0..0xFFF |

**Notes:** Only caller: mcu_0160_0800b4e8, which passes 0x61A (1562).

- Addresses by version: 143: 0x0800E23C, 152: 0x0800E2D4, 0160: 0x0800E414
- Peripheral registers: `WDT.RLD` (W)
- Called by: `mcu_watchdog_start`
- Confidence: high
