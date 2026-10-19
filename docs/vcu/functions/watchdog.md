# VCU - `watchdog` functions

5 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`vcu_watchdog_start`](#vcu_watchdog_start) | 0x080028E0 | Start the independent watchdog with divider 256 and reload 1249 (about 8 s at 40 kHz) |
| [`wdt_counter_reload`](#wdt_counter_reload) | 0x0800F0B8 | Feed the independent watchdog (write 0xAAAA to WDT.CMD) |
| [`wdt_divider_set`](#wdt_divider_set) | 0x0800F0C8 | Set the WDT clock prescaler (WDT.DIV[2:0]) |
| [`wdt_register_write_enable`](#wdt_register_write_enable) | 0x0800F0E8 | Unlock or lock write access to WDT DIV/RLD (WDT.CMD key) |
| [`wdt_reload_value_set`](#wdt_reload_value_set) | 0x0800F100 | Set the WDT reload value (write WDT.RLD) |

## vcu_watchdog_start

**Start the independent watchdog with divider 256 and reload 1249 (about 8 s at 40 kHz)**

Configures and starts the independent watchdog. It unlocks register writes (wdt_register_write_enable(1)), sets the prescaler to code 6 (divide by 256, wdt_divider_set), sets the reload value to 0x4E1 = 1249 (wdt_reload_value_set), reloads the counter (wdt_counter_reload), and then writes 0xCCCC to WDT.CMD to start it. The main loop must feed the watchdog afterwards, and vcu_0159_0800d858 calls wdt_counter_reload. It is called from the init sequence vcu_0159_08002060.

**Notes:** The timeout of about 8 s is 1250 x 256 / 40000 and assumes a 40 kHz LSI clock, which is not checked here.

- Addresses by version: 148: 0x0800250C, 14a: 0x08002588, 14b: 0x08002840, 14e: 0x08002840, 14f: 0x0800289C, 152: 0x080028D8, 153: 0x080028F4, 0159: 0x080028E0
- Peripheral registers: `WDT.CMD` (W)
- Called by: `vcu_peripheral_init_sequence`
- Calls: `wdt_counter_reload`, `wdt_divider_set`, `wdt_register_write_enable`, `wdt_reload_value_set`
- Confidence: high

## wdt_counter_reload

**Feed the independent watchdog (write 0xAAAA to WDT.CMD)**

Matches the Artery SDK wdt_counter_reload: writes WDT_CMD_RELOAD (0xAAAA) to the WDT command register, reloading the down-counter from RLD. Called from vcu_0159_080028e0 (watchdog setup) and vcu_0159_0800d858 (likely the periodic main-loop/tick routine that kicks the dog).

- Addresses by version: 148: 0x0800E094, 14a: 0x0800E530, 14b: 0x0800E9C0, 14e: 0x0800EA60, 14f: 0x0800EBAC, 152: 0x0800EE54, 153: 0x0800EF48, 0159: 0x0800F0B8
- Peripheral registers: `WDT.CMD` (W)
- Called by: `vcu_watchdog_start`, `vcu_0159_0800d858`
- Confidence: high

## wdt_divider_set

**Set the WDT clock prescaler (WDT.DIV[2:0])**

Matches the Artery SDK wdt_divider_set: read-modify-write of the DIV register (0x40003004) replacing bits 2:0 with (param_1 & 7); values 0..6 correspond to dividers /4../256 of the LICK clock. Part of the watchdog setup in vcu_0159_080028e0, after wdt_register_write_enable(1).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | divider selector, 0..7 (wdt_division_type) |

- Addresses by version: 148: 0x0800E0A4, 14a: 0x0800E540, 14b: 0x0800E9D0, 14e: 0x0800EA70, 14f: 0x0800EBBC, 152: 0x0800EE64, 153: 0x0800EF58, 0159: 0x0800F0C8
- Peripheral registers: `WDT.DIV` (RW)
- Called by: `vcu_watchdog_start`
- Confidence: high

## wdt_register_write_enable

**Unlock or lock write access to WDT DIV/RLD (WDT.CMD key)**

Matches the Artery SDK wdt_register_write_enable: non-zero argument writes the unlock key 0x5555 to the WDT command register so DIV and RLD can be modified; zero writes 0x0000 to lock them again. Called from watchdog setup vcu_0159_080028e0 around wdt_divider_set and wdt_reload_value_set.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | non-zero = unlock, 0 = lock |

- Addresses by version: 148: 0x0800E0C4, 14a: 0x0800E560, 14b: 0x0800E9F0, 14e: 0x0800EA90, 14f: 0x0800EBDC, 152: 0x0800EE84, 153: 0x0800EF78, 0159: 0x0800F0E8
- Peripheral registers: `WDT.CMD` (W)
- Called by: `vcu_watchdog_start`
- Confidence: high

## wdt_reload_value_set

**Set the WDT reload value (write WDT.RLD)**

Matches the Artery SDK wdt_reload_value_set: stores param_1 into the RLD register (0x40003008); only the low 12 bits are meaningful (0..0xFFF). Must be preceded by wdt_register_write_enable(1). Called from watchdog setup vcu_0159_080028e0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | reload value, 0..0xFFF |

- Addresses by version: 148: 0x0800E0DC, 14a: 0x0800E578, 14b: 0x0800EA08, 14e: 0x0800EAA8, 14f: 0x0800EBF4, 152: 0x0800EE9C, 153: 0x0800EF90, 0159: 0x0800F100
- Peripheral registers: `WDT.RLD` (W)
- Called by: `vcu_watchdog_start`
- Confidence: high
