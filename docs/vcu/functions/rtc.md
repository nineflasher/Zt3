# VCU - `rtc` functions

19 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`ertc_date_set`](#ertc_date_set) | 0x0800C9D8 | Write the ERTC date register from year, month, day and weekday, with BCD year, month and day |
| [`ertc_divider_set`](#ertc_divider_set) | 0x0800CA4C | Write the ERTC prescaler: async divider (7 bits) and sync divider (15 bits) |
| [`ertc_flag_clear`](#ertc_flag_clear) | 0x0800CA84 | Clear ERTC status flags while preserving the IMEN bit |
| [`ertc_flag_get`](#ertc_flag_get) | 0x0800CAA0 | Test an ERTC status flag |
| [`ertc_hour_mode_set`](#ertc_hour_mode_set) | 0x0800CAB4 | Set the ERTC 12/24-hour mode bit (CTRL.HM) inside an init-mode window |
| [`ertc_init_mode_enter`](#ertc_init_mode_enter) | 0x0800CAE4 | Enter ERTC init mode (set STS.IMEN) and poll INITF with a 0x6C0000 timeout |
| [`ertc_init_mode_exit`](#ertc_init_mode_exit) | 0x0800CB14 | Leave ERTC initialisation mode |
| [`ertc_interrupt_enable`](#ertc_interrupt_enable) | 0x0800CB24 | Enable or disable ERTC interrupt sources: tamper interrupt in TAMP, the rest in CTRL |
| [`ertc_num_to_bcd`](#ertc_num_to_bcd) | 0x0800CB6C | Convert a number 0..99 to packed BCD |
| [`ertc_reset`](#ertc_reset) | 0x0800CB84 | Reset all ERTC registers to power-on values inside an init-mode window |
| [`ertc_wait_flag`](#ertc_wait_flag) | 0x0800CC70 | Poll an ERTC status flag until it reaches the wanted state, 0x360000 polls at most |
| [`ertc_wait_update`](#ertc_wait_update) | 0x0800CC98 | Wait until the ERTC calendar registers are synchronised |
| [`ertc_wakeup_clock_set`](#ertc_wakeup_clock_set) | 0x0800CCC8 | Select the wakeup timer clock (CTRL bits 2:0, WATCLK) under write protection |
| [`ertc_wakeup_counter_set`](#ertc_wakeup_counter_set) | 0x0800CCE8 | Write the 16-bit wakeup timer reload value (ERTC.WAT) under write protection |
| [`ertc_wakeup_enable`](#ertc_wakeup_enable) | 0x0800CD08 | Enable or disable the ERTC wakeup timer (CTRL.WATEN), waiting for WATWF on disable |
| [`ertc_write_protect_disable`](#ertc_write_protect_disable) | 0x0800CD38 | Unlock ERTC register write protection |
| [`ertc_write_protect_enable`](#ertc_write_protect_enable) | 0x0800CD48 | Lock ERTC register write protection |
| [`rtc_day_of_year`](#rtc_day_of_year) | (removed) | Day-of-year from year, month, day with leap-year correction |
| [`rtc_days_between_dates`](#rtc_days_between_dates) | (removed) | Number of days from calendar date 1 to date 2 (Gregorian), 0 if date 2 is in an earlier year |

## ertc_date_set

**Write the ERTC date register from year, month, day and weekday, with BCD year, month and day**

Matches the SDK ertc_date_set. It converts year, month and date with ertc_num_to_bcd, lifts write protection, enters init mode through FUN_0800cae4 (ertc_init_mode_enter, not yet described) and returns 0 if that fails. It writes ERTC.DATE as year<<16 | (month&0x1f)<<8 | (date&0x3f) | (weekday&7)<<13, exits init mode, waits for calendar synchronisation with ertc_wait_update when CTRL bit 5 (DREN) is clear, re-locks write protection and returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | year, 0..99 |
| `param_2` | `u8` | month, 1..12 |
| `param_3` | `u8` | day of month |
| `param_4` | `u8` | weekday, 0..7 |

**Returns** `u32`: 1 on success, 0 when init mode could not be entered

- Addresses by version: 148: 0x0800BB4C, 14a: 0x0800BF90, 14b: 0x0800C41C, 14e: 0x0800C4B0, 14f: 0x0800C5EC, 152: 0x0800C878, 153: 0x0800C96C, 0159: 0x0800C9D8
- Peripheral registers: `ERTC.DATE` (AW), `ERTC.CTRL` (R)
- Called by: `vcu_0159_0800c960`
- Calls: `ertc_init_mode_enter`, `ertc_init_mode_exit`, `ertc_num_to_bcd`, `ertc_wait_update`, `ertc_write_protect_disable`, `ertc_write_protect_enable`
- Confidence: high

## ertc_divider_set

**Write the ERTC prescaler: async divider (7 bits) and sync divider (15 bits)**

Matches the SDK ertc_divider_set(div_a, div_b). It lifts write protection, enters init mode through FUN_0800cae4 and returns 0 if that fails. It writes the async divider into ERTC.DIV bits 16..22 and the sync divider into bits 0..14, exits init mode, re-locks write protection and returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | async divider (diva), 7 bits used |
| `param_2` | `u16` | sync divider (divb), 15 bits used |

**Returns** `u32`: 1 on success, 0 when init mode could not be entered

**Notes:** The decompile takes the async divider from register r3 (extraout_r3), a decompiler artefact of the call sequence; the SDK source takes it from the first argument, so the mapping above follows the SDK.

- Addresses by version: 148: 0x0800BBC0, 14a: 0x0800C004, 14b: 0x0800C490, 14e: 0x0800C524, 14f: 0x0800C660, 152: 0x0800C8EC, 153: 0x0800C9E0, 0159: 0x0800CA4C
- Peripheral registers: `ERTC.DIV` (ARW)
- Called by: `vcu_0159_0800c960`
- Calls: `ertc_init_mode_enter`, `ertc_init_mode_exit`, `ertc_write_protect_disable`, `ertc_write_protect_enable`
- Confidence: high

## ertc_flag_clear

**Clear ERTC status flags while preserving the IMEN bit**

AT32 SDK ertc_flag_clear(): writes ERTC.STS = ~(param_1 | 0x80) | (STS & 0x80). The flag bits are cleared by writing 0 to them; all other bits are written as 1 (no effect) and bit 7 (init mode enable) is written back unchanged. Called from vcu_0159_08005874 (likely the RTC alarm/wakeup IRQ handler, not verified).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | ERTC_xxx_FLAG mask to clear |

- Addresses by version: 148: 0x0800BBF8, 14a: 0x0800C03C, 14b: 0x0800C4C8, 14e: 0x0800C55C, 14f: 0x0800C698, 152: 0x0800C924, 153: 0x0800CA18, 0159: 0x0800CA84
- Peripheral registers: `ERTC.STS` (ARW)
- Called by: `ERTC_WKUP_IRQHandler`
- Confidence: high

## ertc_flag_get

**Test an ERTC status flag**

AT32 SDK ertc_flag_get(): returns 1 if any bit of ERTC.STS selected by param_1 is set, else 0. Called by vcu_0159_08005874.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | ERTC_xxx_FLAG mask |

**Returns** `u32`: 1 if set, 0 if clear

- Addresses by version: 148: 0x0800BC14, 14a: 0x0800C058, 14b: 0x0800C4E4, 14e: 0x0800C578, 14f: 0x0800C6B4, 152: 0x0800C940, 153: 0x0800CA34, 0159: 0x0800CAA0
- Peripheral registers: `ERTC.STS` (R)
- Called by: `ERTC_WKUP_IRQHandler`, `ertc_wait_flag`
- Confidence: high

## ertc_hour_mode_set

**Set the ERTC 12/24-hour mode bit (CTRL.HM) inside an init-mode window**

AT32 SDK ertc_hour_mode_set. Disables write protection, enters ERTC init mode through ertc_init_mode_enter (vcu_0159_0800cae4), writes CTRL bit 6 (HM, hour format) from the low bit of the mode argument, leaves init mode with ertc_init_mode_exit and re-enables write protection. The mode is not in the decompiled signature: the value is carried in r3 (extraout_r3). If init mode cannot be entered it returns 0 and CTRL is left unchanged. Called from the ERTC set-time path vcu_0159_0800c960.

**Returns** `u32`: 1 = SUCCESS, 0 = ERROR (init mode not entered)

**Notes:** Mode argument read from r3; SDK type is ertc_hour_mode_set_type.

- Addresses by version: 148: 0x0800BC28, 14a: 0x0800C06C, 14b: 0x0800C4F8, 14e: 0x0800C58C, 14f: 0x0800C6C8, 152: 0x0800C954, 153: 0x0800CA48, 0159: 0x0800CAB4
- Peripheral registers: `ERTC.CTRL` (ARW)
- Called by: `vcu_0159_0800c960`
- Calls: `ertc_init_mode_enter`, `ertc_init_mode_exit`, `ertc_write_protect_disable`, `ertc_write_protect_enable`
- Confidence: high

## ertc_init_mode_enter

**Enter ERTC init mode (set STS.IMEN) and poll INITF with a 0x6C0000 timeout**

AT32 SDK ertc_init_mode_enter. If the init-mode flag STS bit 6 (IMF, INITF) is already set it returns 1 at once. Otherwise it writes 0xFFFFFFFF to ERTC.STS, which sets the init-mode enable bit 7 (IMEN), and polls IMF for up to 0x6C0000 iterations. On timeout it re-enables write protection and returns 0. Every ERTC calendar, divider, hour-mode and reset routine goes through this gate; callers are vcu_0159_0800c960, 0800c9d8, 0800ca4c, 0800cab4 and 0800cb84.

**Returns** `u32`: 1 = SUCCESS (init mode active), 0 = ERROR (timed out)

- Addresses by version: 148: 0x0800BC58, 14a: 0x0800C09C, 14b: 0x0800C528, 14e: 0x0800C5BC, 14f: 0x0800C6F8, 152: 0x0800C984, 153: 0x0800CA78, 0159: 0x0800CAE4
- Peripheral registers: `ERTC.STS` (ARW)
- Called by: `vcu_0159_0800c960`, `ertc_date_set`, `ertc_divider_set`, `ertc_hour_mode_set`, `ertc_reset`
- Calls: `ertc_write_protect_enable`
- Confidence: high

## ertc_init_mode_exit

**Leave ERTC initialisation mode**

AT32 SDK ertc_init_mode_exit(): writes 0xFFFFFF7F to ERTC.STS, which clears the init-mode enable bit (bit 7) and writes 1 (no effect) to all flag bits. Called at the end of the ERTC set-time/date/calendar routines (vcu_0159_0800c960, 0800c9d8, 0800ca4c, 0800cab4).

- Addresses by version: 148: 0x0800BC88, 14a: 0x0800C0CC, 14b: 0x0800C558, 14e: 0x0800C5EC, 14f: 0x0800C728, 152: 0x0800C9B4, 153: 0x0800CAA8, 0159: 0x0800CB14
- Peripheral registers: `ERTC.STS` (W)
- Called by: `vcu_0159_0800c960`, `ertc_date_set`, `ertc_divider_set`, `ertc_hour_mode_set`
- Confidence: high

## ertc_interrupt_enable

**Enable or disable ERTC interrupt sources: tamper interrupt in TAMP, the rest in CTRL**

AT32 SDK ertc_interrupt_enable(source, new_state). Disables write protection, then if the source mask contains ERTC_TP_INT (0x04) it sets or clears TAMP bit 2 (TPIEN). The remaining source bits are OR-ed into or cleared from ERTC.CTRL, which holds the alarm, wakeup and timestamp interrupt enables (ALAIEN bit 12, ALBIEN bit 13, WATIEN bit 14, TSIEN bit 15). Write protection is re-enabled afterwards. Only the masked bits change, so STS flags are not touched.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | interrupt source mask (ERTC_xxx_INT); 0x04 selects the tamper interrupt |
| `param_2` | `bool` | confirm_state: non-zero enables, zero disables |

**Notes:** The decompiler takes the arguments from r2 and r3 after the write-protect call (extraout_r2, extraout_r3); these are read as the SDK source and state arguments.

- Addresses by version: 148: 0x0800BC98, 14a: 0x0800C0DC, 14b: 0x0800C568, 14e: 0x0800C5FC, 14f: 0x0800C738, 152: 0x0800C9C4, 153: 0x0800CAB8, 0159: 0x0800CB24
- Peripheral registers: `ERTC.CTRL` (ARW), `ERTC.TAMP` (RW)
- Called by: `vcu_0159_080024ec`
- Calls: `ertc_write_protect_disable`, `ertc_write_protect_enable`
- Confidence: high

## ertc_num_to_bcd

**Convert a number 0..99 to packed BCD**

AT32 SDK ertc_num_to_bcd(): returns (param_1 % 10) | ((param_1 / 10 & 0xf) << 4). Used by the set-time and set-date routines (vcu_0159_0800c960, 0800c9d8) before writing the ERTC TIME/DATE registers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | binary value 0..99 |

**Returns** `u32`: BCD byte, tens in bits 7:4

- Addresses by version: 148: 0x0800BCE0, 14a: 0x0800C124, 14b: 0x0800C5B0, 14e: 0x0800C644, 14f: 0x0800C780, 152: 0x0800CA0C, 153: 0x0800CB00, 0159: 0x0800CB6C
- Called by: `vcu_0159_0800c960`, `ertc_date_set`
- Confidence: high

## ertc_reset

**Reset all ERTC registers to power-on values inside an init-mode window**

AT32 SDK ertc_reset. Disables write protection, clears CTRL, enters init mode (vcu_0159_0800cae4), then writes the reset values: TIME 0, DATE 0x2101 (year 00, January 1, weekday 1), CTRL 0, DIV 0x007F00FF (async divider 128, sync divider 256), WAT 0xFFFF, and zero for CCAL, ALA, ALB, TADJ, SCAL, TAMP, ALASBS, ALBSBS and STS. It then waits for the calendar update with ertc_wait_update (vcu_0159_0800cc98) and re-enables write protection. If init mode cannot be entered it returns 0 after clearing only CTRL.

**Returns** `u32`: 1 = SUCCESS, 0 = ERROR

- Addresses by version: 148: 0x0800BCF8, 14a: 0x0800C13C, 14b: 0x0800C5C8, 14e: 0x0800C65C, 14f: 0x0800C798, 152: 0x0800CA24, 153: 0x0800CB18, 0159: 0x0800CB84
- Peripheral registers: `ERTC.TIME` (W), `ERTC.DATE` (W), `ERTC.CTRL` (W), `ERTC.STS` (AW), `ERTC.DIV` (W), `ERTC.WAT` (AW), `ERTC.CCAL` (W), `ERTC.ALA` (W), `ERTC.ALB` (W), `ERTC.TADJ` (W), `ERTC.SCAL` (W), `ERTC.TAMP` (W), `ERTC.ALASBS` (W), `ERTC.ALBSBS` (W)
- Called by: `vcu_0159_0800c960`
- Calls: `ertc_init_mode_enter`, `ertc_wait_update`, `ertc_write_protect_disable`, `ertc_write_protect_enable`
- Confidence: high

## ertc_wait_flag

**Poll an ERTC status flag until it reaches the wanted state, 0x360000 polls at most**

AT32 SDK ertc_wait_flag(flag, status) as built here. It calls ertc_flag_get (vcu_0159_0800caa0) in a loop while the result equals the expected value and returns 1 once it differs. The countdown starts at 0x360000 (ERTC_TIMEOUT); on expiry it re-enables write protection and returns 0. The only caller in this packet, vcu_0159_0800cd08 (ertc_wakeup_enable), passes flag 4 (STS.WATWF, the wakeup-register write-allowed flag) and value 0, so it waits until WATWF is set.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | ERTC_xxx_FLAG mask (4 = WATWF) |
| `param_2` | `u32` | flag value to wait out of: 0 = wait until set, 1 = wait until clear |

**Returns** `u32`: 1 = flag reached the wanted state, 0 = timed out

**Notes:** The expected value is read from r3 in the decompile (extraout_r3).

- Addresses by version: 148: 0x0800BDE4, 14a: 0x0800C228, 14b: 0x0800C6B4, 14e: 0x0800C748, 14f: 0x0800C884, 152: 0x0800CB10, 153: 0x0800CC04, 0159: 0x0800CC70
- Called by: `ertc_wakeup_enable`
- Calls: `ertc_flag_get`, `ertc_write_protect_enable`
- Confidence: high

## ertc_wait_update

**Wait until the ERTC calendar registers are synchronised**

AT32 SDK ertc_wait_update(): clears the UPDF flag (bit 5) in ERTC.STS by writing ~(UPDF | 0x80) | (STS & 0x80), then polls UPDF up to 0x6c0000 times. Returns 1 when the flag came up, 0 on timeout. Called by vcu_0159_0800c960, 0800c9d8 and 0800cb84 before reading/after writing calendar registers.

**Returns** `u32`: 1 = SUCCESS, 0 = timed out (ERROR)

- Addresses by version: 148: 0x0800BE0C, 14a: 0x0800C250, 14b: 0x0800C6DC, 14e: 0x0800C770, 14f: 0x0800C8AC, 152: 0x0800CB38, 153: 0x0800CC2C, 0159: 0x0800CC98
- Peripheral registers: `ERTC.STS` (RW)
- Called by: `vcu_0159_0800c960`, `ertc_date_set`, `ertc_reset`
- Confidence: high

## ertc_wakeup_clock_set

**Select the wakeup timer clock (CTRL bits 2:0, WATCLK) under write protection**

AT32 SDK ertc_wakeup_clock_set(clock). Disables write protection, replaces CTRL bits 2..0 (the wakeup clock select field WATCLK) with the low three bits of the argument, keeps the other CTRL bits and re-enables write protection. The SDK does not poll any flag before the write, and neither does this code.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | wakeup clock select code 0..7 (ertc_wakeup_clock_type) |

- Addresses by version: 148: 0x0800BE3C, 14a: 0x0800C280, 14b: 0x0800C70C, 14e: 0x0800C7A0, 14f: 0x0800C8DC, 152: 0x0800CB68, 153: 0x0800CC5C, 0159: 0x0800CCC8
- Peripheral registers: `ERTC.CTRL` (ARW)
- Called by: `vcu_0159_080024ec`
- Calls: `ertc_write_protect_disable`, `ertc_write_protect_enable`
- Confidence: high

## ertc_wakeup_counter_set

**Write the 16-bit wakeup timer reload value (ERTC.WAT) under write protection**

AT32 SDK ertc_wakeup_counter_set(counter). Disables write protection, replaces the low 16 bits of ERTC.WAT (0x40002814) with the argument, keeps the upper half and re-enables write protection. Like the SDK, it does not poll WATWF before writing.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | wakeup counter reload value 0..65535 |

- Addresses by version: 148: 0x0800BE5C, 14a: 0x0800C2A0, 14b: 0x0800C72C, 14e: 0x0800C7C0, 14f: 0x0800C8FC, 152: 0x0800CB88, 153: 0x0800CC7C, 0159: 0x0800CCE8
- Peripheral registers: `ERTC.WAT` (ARW)
- Called by: `vcu_0159_080024ec`
- Calls: `ertc_write_protect_disable`, `ertc_write_protect_enable`
- Confidence: high

## ertc_wakeup_enable

**Enable or disable the ERTC wakeup timer (CTRL.WATEN), waiting for WATWF on disable**

AT32 SDK ertc_wakeup_enable(new_state). Disables write protection, writes CTRL bit 10 (WATEN) from the argument and, when disabling, waits for STS.WATWF with ertc_wait_flag (vcu_0159_0800cc70). If that wait times out the function returns 0 without re-locking write protection, because ertc_wait_flag has already re-enabled it on its timeout path. On success it re-enables write protection and returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `bool` | confirm_state: 1 enables the wakeup timer, 0 disables it |

**Returns** `u32`: 1 = SUCCESS, 0 = ERROR (WATWF wait timed out)

- Addresses by version: 148: 0x0800BE7C, 14a: 0x0800C2C0, 14b: 0x0800C74C, 14e: 0x0800C7E0, 14f: 0x0800C91C, 152: 0x0800CBA8, 153: 0x0800CC9C, 0159: 0x0800CD08
- Peripheral registers: `ERTC.CTRL` (ARW)
- Called by: `vcu_0159_080024ec`
- Calls: `ertc_wait_flag`, `ertc_write_protect_disable`, `ertc_write_protect_enable`
- Confidence: high

## ertc_write_protect_disable

**Unlock ERTC register write protection**

AT32 SDK ertc_write_protect_disable(): writes the key sequence 0xCA then 0x53 to ERTC.WP (0x40002824). Called at the beginning of every ERTC write routine (vcu_0159_0800c960, 0800c9d8, 0800ca4c, 0800cab4, 0800cb24, 0800cb84, 0800ccc8, 0800cce8, 0800cd08) and paired with ertc_write_protect_enable.

- Addresses by version: 148: 0x0800BEAC, 14a: 0x0800C2F0, 14b: 0x0800C77C, 14e: 0x0800C810, 14f: 0x0800C94C, 152: 0x0800CBD8, 153: 0x0800CCCC, 0159: 0x0800CD38
- Peripheral registers: `ERTC.WP` (AW)
- Called by: `vcu_0159_0800c960`, `ertc_date_set`, `ertc_divider_set`, `ertc_hour_mode_set`, `ertc_interrupt_enable`, `ertc_reset`, `ertc_wakeup_clock_set`, `ertc_wakeup_counter_set`, `ertc_wakeup_enable`
- Confidence: high

## ertc_write_protect_enable

**Lock ERTC register write protection**

AT32 SDK ertc_write_protect_enable(): writes 0xFF to ERTC.WP (0x40002824), re-enabling write protection of the ERTC registers. Called at the end of the ERTC configuration routines (and on timeout paths).

- Addresses by version: 148: 0x0800BEBC, 14a: 0x0800C300, 14b: 0x0800C78C, 14e: 0x0800C820, 14f: 0x0800C95C, 152: 0x0800CBE8, 153: 0x0800CCDC, 0159: 0x0800CD48
- Peripheral registers: `ERTC.WP` (W)
- Called by: `vcu_0159_0800c960`, `ertc_date_set`, `ertc_divider_set`, `ertc_hour_mode_set`, `ertc_init_mode_enter`, `ertc_interrupt_enable`, `ertc_reset`, `ertc_wait_flag`, `ertc_wakeup_clock_set`, `ertc_wakeup_counter_set`, `ertc_wakeup_enable`
- Confidence: high

## rtc_day_of_year

**Day-of-year from year, month, day with leap-year correction**

Computes table[month-1] + day + leap, where table is the 12-entry word array at 0x0800f0ec (cumulative days before each month, assumed) and leap = 1 only when month >= 3 and the year is a Gregorian leap year (divisible by 4, and not a century unless divisible by 400). Returns a 64-bit value whose low word is the day number and whose high word is just param_1 echoed back (decompiler artifact). Present only in builds up to VCU_153; its single caller vcu_153_0800ba2c is in the date/time conversion code.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | full year, e.g. 2024 |
| `param_2` | `s32` | month 1..12 |
| `param_3` | `s32` | day of month 1..31 |

**Returns** `u32`: day of year (1..366); low word of a 64-bit return

**Notes:** Name and intent inferred from the arithmetic; the table contents at 0x0800f0ec were not dumped here. Missing from VCU_0159, so the date logic was removed or inlined in that build.

- Addresses by version: 148: 0x0800AB70, 14a: 0x0800AF68, 14b: 0x0800B3F4, 14e: 0x0800B488, 14f: 0x0800B5C4, 152: 0x0800B850, 153: 0x0800B944
- Called by: `rtc_days_between_dates`
- Confidence: medium

## rtc_days_between_dates

**Number of days from calendar date 1 to date 2 (Gregorian), 0 if date 2 is in an earlier year**

Computes the day count between two dates. Each date's day-of-year is taken from rtc_day_of_year (FUN_0800b944). In the same year the result is the plain day-of-year difference, which is negative if date 2 is earlier. For later years the result is the remaining days in the first year (365, or 366 when the first year is a leap year, per the Gregorian rule), plus the day-of-year of date 2, plus 365 for each full year between them, plus one for each leap year strictly between the two years. Years before the first date return 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | year of date 1 |
| `param_2` | `u32` | month of date 1 |
| `param_3` | `u32` | day of date 1 |
| `param_4` | `s32` | year of date 2 |
| `param_5` | `u32` | month of date 2 |
| `param_6` | `u32` | day of date 2 |

**Returns** `s32`: days from date 1 to date 2

- Addresses by version: 148: 0x0800AC64, 14a: 0x0800B050, 14b: 0x0800B4DC, 14e: 0x0800B570, 14f: 0x0800B6AC, 152: 0x0800B938, 153: 0x0800BA2C
- Called by: `vcu_0159_08004594`
- Calls: `rtc_day_of_year`
- Confidence: high
