# MCU - `exint` functions

3 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`exint_flag_clear`](#exint_flag_clear) | 0x0800CAD0 | Clear pending EXINT line flags by writing the line mask to EXINT.INTSTS |
| [`exint_flag_get`](#exint_flag_get) | 0x0800CADC | Return true when any of the given EXINT lines has a pending flag |
| [`exint_init`](#exint_init) | 0x0800CAF4 | Configure EXINT lines for interrupt or event mode and an edge, or disable them |

## exint_flag_clear

**Clear pending EXINT line flags by writing the line mask to EXINT.INTSTS**

SDK exint_flag_clear. It writes the caller's line mask to EXINT.INTSTS (0x40010414). The SDK uses this write to acknowledge pending external interrupt lines, so only the lines in the mask are cleared. It is a one-line helper called from the EXINT handler paths in the other callers listed in the packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | EXINT line bit mask (bit n = line n) |

- Addresses by version: 12b: 0x0800C7D8, 143: 0x0800CA30, 152: 0x0800CA70, 0160: 0x0800CAD0
- Peripheral registers: `EXINT.INTSTS` (W)
- Called by: `mcu_0160_0800850c`, `mcu_pvm_init`
- Confidence: high

## exint_flag_get

**Return true when any of the given EXINT lines has a pending flag**

SDK exint_flag_get. It reads EXINT.INTSTS (0x40010414), ANDs it with the line mask and returns whether the result is non-zero. This is an any-line test, not an all-lines test, and a zero mask always returns false.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | EXINT line bit mask |

**Returns** `bool`: true when at least one masked line is pending

- Addresses by version: 12b: 0x0800C7E4, 143: 0x0800CA3C, 152: 0x0800CA7C, 0160: 0x0800CADC
- Peripheral registers: `EXINT.INTSTS` (R)
- Called by: `mcu_0160_0800850c`, `mcu_pvm_init`
- Confidence: high

## exint_init

**Configure EXINT lines for interrupt or event mode and an edge, or disable them**

SDK exint_init, with the EXINT base at 0x40010400. It takes an exint_init_type record: the mode byte at +0 (0 = interrupt, otherwise event), the line mask at +4, the edge byte at +8 (0 = rising, 1 = falling, otherwise both) and the enable byte at +9. The selected lines are first removed from INTEN (0x40010400) and EVTEN (0x40010404) in every case. When enabled, they are added to INTEN or EVTEN, their bits in POLCFG1 (0x40010408, rising) and POLCFG2 (0x4001040C, falling) are cleared, and then the selected edge bits are set again.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | exint_init_type record: mode byte +0, line mask u32 +4, edge byte +8, enable byte +9 |

- Addresses by version: 12b: 0x0800C7FC, 143: 0x0800CA54, 152: 0x0800CA94, 0160: 0x0800CAF4
- Peripheral registers: `EXINT.INTEN` (RW), `EXINT.EVTEN` (RW), `EXINT.POLCFG1` (RW), `EXINT.POLCFG2` (RW)
- Called by: `mcu_pvm_init`
- Confidence: high
