# MCU - `hall` functions

4 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_hall_get_transition_status`](#mcu_hall_get_transition_status) | 0x0800915C | Return the hall sector transition status byte at +0x01 |
| [`mcu_hall_sector_transition`](#mcu_hall_sector_transition) | 0x080090A0 | Validate a 60-degree hall sector step from +0x5C to +0x60 and set direction +0x38 to +1 or -1 |
| [`mcu_hall_sector_window_update`](#mcu_hall_sector_window_update) | 0x08008F78 | Set magnitude fault 0x4305 and recompute the expected-sector window bounds at +0x50 and +0x54 |
| [`mcu_hall_state_dispatch`](#mcu_hall_state_dispatch) | 0x08003034 | Dispatch to a per-state handler selected by bits 9..11 of a status word |

## mcu_hall_get_transition_status

**Return the hall sector transition status byte at +0x01**

Getter for byte +0x01 of the object, which mcu_hall_sector_transition sets to 0 for a valid step or to 1..6 for an invalid one.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | drive context |

**Returns** `u8`: transition status

**Notes:** Callers mcu_0160_08005b3c and mcu_12b_08005d30 are outside this packet.

- Addresses by version: 12b: 0x08008F00, 143: 0x0800909C, 152: 0x080090E8, 0160: 0x0800915C
- Called by: `mcu_0160_08005b3c`
- Confidence: high

## mcu_hall_sector_transition

**Validate a 60-degree hall sector step from +0x5C to +0x60 and set direction +0x38 to +1 or -1**

Six sector codes are used: 0, 0x10C15, 0x2182A, 0x3243F, 0x43054 and 0x53C69, i.e. k x 0x10C15 for sectors k = 0..5 (60 degrees each, six per electrical revolution). The status byte +0x01 is cleared first. If the current code (+0x5C) is one of the six and the new code (+0x60) is one of its two neighbours mod 6, the direction halfword +0x38 is set to +1 for a step to the lower index (including 0 to 5) and to -1 for a step to the higher index (including 5 to 0), and the status stays 0. An invalid step leaves +0x38 unchanged and stores k+1 (1..6) in the status byte. A current code outside the six leaves the status at 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | drive context: current sector +0x5C, new sector +0x60, direction +0x38, status byte +0x01 |

**Returns** `u8`: 0 for a valid step, 1..6 (k+1 of the current sector) for an invalid step

**Notes:** The hall sensor interpretation is inferred from the six-state, neighbour-only transitions. Callers mcu_0160_08009160 is outside this packet.

- Addresses by version: 12b: 0x08008E44, 143: 0x08008FE0, 152: 0x0800902C, 0160: 0x080090A0
- Called by: `mcu_0160_08009160`
- Confidence: high

## mcu_hall_sector_window_update

**Set magnitude fault 0x4305 and recompute the expected-sector window bounds at +0x50 and +0x54**

If the flag byte at +0x04 is not 1 and |+0x70| is at least the limit at +0x88, byte +0x05 is set and fault code 0x4305 is stored at +0x58; otherwise both are 0. The window centre is C = +0x5C + +0x48, where +0x5C is the sector code (k x 0x10C15) produced by mcu_hall_sector_transition. The window depends on the direction state +0x38 (a signed halfword): 0 gives [C-10, C+10]; +1 gives [C-0x860A-f, C+f] (upper bound C+0x860B+f when +0x04 is 0); -1 gives [C-f, C+0x860A+f] (lower bound C-0x860B-f when +0x04 is 0), where f is the fault offset in +0x58. Half a sector is 0x860A, so the window covers about 30 degrees either side of the sector edge.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | drive context: flag +0x04, value +0x70, limit +0x88, centre inputs +0x48/+0x5C, direction +0x38, outputs +0x50/+0x54/+0x58 |

**Notes:** The meaning of the fault code 0x4305 and of the value at +0x70 is not established. The window interpretation rests on 0x860A being half of the 0x10C15 sector step. Callers mcu_0160_08009160 and mcu_0160_08009598 are outside this packet.

- Addresses by version: 12b: 0x08008D28, 143: 0x08008EC4, 152: 0x08008F04, 0160: 0x08008F78
- Called by: `mcu_0160_08009160`, `mcu_0160_08009598`
- Confidence: medium

## mcu_hall_state_dispatch

**Dispatch to a per-state handler selected by bits 9..11 of a status word**

Extracts idx = (DAT_20001fda & 0xfff) >> 9 (a 3-bit value 0..7, most likely the Hall-sensor pattern) and calls the function pointer at 0x20000698[idx] (a RAM table of 8 handlers) with argument DAT_20000678 ^ idx, i.e. the bit mask of what changed since the previous state. It then stores the new index (same bit field 9..11 re-extracted) into DAT_20000678 as the previous state. Called from mcu_0160_08007268, an interrupt-level routine. A Hall-commutation/edge interpretation is a guess based on the 3-bit field.

**Notes:** 0x20000698 is address-taken: an 8-entry function-pointer table in RAM. Actual source of 0x20001fda (Hall inputs vs. captured timer value) not shown.

- Addresses by version: 12b: 0x08003114, 143: 0x08003010, 152: 0x08002F94, 0160: 0x08003034
- Called by: `mcu_0160_08007268`
- Confidence: medium
