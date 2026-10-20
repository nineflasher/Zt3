# BMS - `rtc` functions

29 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`HAL_RTCEx_DeactivateWakeUpTimer`](#hal_rtcex_deactivatewakeuptimer) | 0x08002348 | Disables the RTC wake-up timer and its interrupt, waiting for WUTWF |
| [`HAL_RTCEx_SetSynchroShift`](#hal_rtcex_setsynchroshift) | 0x080023CA | Writes RTC SHIFTR (add-one-second and sub-second shift) after waiting for SHPF |
| [`HAL_RTCEx_SetWakeUpTimer_IT`](#hal_rtcex_setwakeuptimer_it) | 0x08002470 | Sets the RTC wake-up counter and clock, unmasks EXTI line 19 and enables the interrupt |
| [`HAL_RTCEx_WakeUpTimerIRQHandler`](#hal_rtcex_wakeuptimerirqhandler) | 0x08002542 | RTC wake-up interrupt handler: clears WUTF, runs the event callback, sets READY |
| [`HAL_RTC_GetDate`](#hal_rtc_getdate) | 0x08002564 | Reads RTC_DR and returns weekday, month, date and year, converting BCD to binary when format is 0 |
| [`HAL_RTC_GetTime`](#hal_rtc_gettime) | 0x080025BC | Reads RTC_TR, SSR and PRER and returns hours, minutes, seconds, AM/PM and sub-seconds |
| [`HAL_RTC_Init`](#hal_rtc_init) | 0x08002628 | Initialises the RTC: enters init mode, programs format, output and prescalers, exits init |
| [`HAL_RTC_MspInit`](#hal_rtc_mspinit) | 0x080026CC | Enables the RTC clock (BDCR.RTCEN and APBENR1.RTCAPBEN) when the handle is for the RTC |
| [`HAL_RTC_SetDate`](#hal_rtc_setdate) | 0x08002704 | Writes the RTC date register from a weekday, month, date and year record |
| [`HAL_RTC_SetTime`](#hal_rtc_settime) | 0x080027A4 | Writes the RTC time register from hours, minutes and seconds, plus DST and store bits |
| [`HAL_RTC_WaitForSynchro`](#hal_rtc_waitforsynchro) | 0x08002868 | Clears RSF and waits up to 1000 ms for the RTC shadow registers to resynchronise |
| [`RTC_EnterInitMode`](#rtc_enterinitmode) | 0x0800352C | Sets RTC INIT and waits up to 1000 ms for INITF before RTC registers are written |
| [`bms_epoch_to_tm`](#bms_epoch_to_tm) | 0x08001278 | Converts Unix epoch seconds to an eight-word struct-tm style broken-down time |
| [`bms_epoch_to_tm_20005d48`](#bms_epoch_to_tm_20005d48) | 0x080010F0 | Converts the epoch value at param_1 into the broken-down time block at 0x20005D48 |
| [`bms_packed_datetime_shift_seconds`](#bms_packed_datetime_shift_seconds) | 0x08009E40 | Shift a bit-packed date and time by param_1 seconds through the epoch conversion |
| [`bms_rtc_backup_reset_lse_on`](#bms_rtc_backup_reset_lse_on) | 0x08009BA4 | Pulse the RTC backup-domain reset, clear LSE drive bits, and set LSEON |
| [`bms_rtc_clock_bringup`](#bms_rtc_clock_bringup) | 0x08009A9C | Start the RTC clock: try LSE with a timeout, fall back to LSI, select it, enable RTC |
| [`bms_rtc_datetime_pack`](#bms_rtc_datetime_pack) | 0x08009D84 | Read RTC date and time in binary and pack them into a 4-byte bit-field record |
| [`bms_rtc_fallback_lsi_start`](#bms_rtc_fallback_lsi_start) | 0x08009C4C | Fall back to the LSI clock for the RTC: enable LSI, wait, select it and init the RTC |
| [`bms_rtc_hal_init`](#bms_rtc_hal_init) | 0x08009D08 | Fill the RTC handle (async prescaler 0x7C or 0x7F, sync 0xFF) and call HAL_RTC_Init |
| [`bms_rtc_lse_ready_get`](#bms_rtc_lse_ready_get) | 0x08009BDC | Return the LSE ready flag (RCC.BDCR LSERDY, bit 1) |
| [`bms_rtc_reset_with_snapshot`](#bms_rtc_reset_with_snapshot) | 0x08006514 | Snapshot the RTC time, reset the RTC backup domain and LSE, and set shared state to 3 |
| [`bms_rtc_select_lse_and_start`](#bms_rtc_select_lse_and_start) | 0x08009BEC | Select LSE as the RTC clock in the backup domain and start the RTC |
| [`bms_rtc_set_datetime_packed`](#bms_rtc_set_datetime_packed) | 0x08009F78 | Load the packed date-time record into the RTC with HAL_RTC_SetDate and HAL_RTC_SetTime |
| [`bms_rtc_timestamp_record_start`](#bms_rtc_timestamp_record_start) | 0x080065E0 | Capture the RTC date and time, prepare the record at 0x20001C84 and set its state byte to 2 |
| [`bms_rtc_wait_synchro`](#bms_rtc_wait_synchro) | 0x08003570 | Wait for the RTC register-sync flag (RSF) with a 1000-tick timeout; returns 0 or 3 |
| [`bms_rtc_wakeup_period_set`](#bms_rtc_wakeup_period_set) | 0x0800A6F4 | Arm the RTC wake-up timer for 1 to 31 seconds with RTC_TAMP IRQ priority 1 |
| [`bms_rtc_wakeup_stop`](#bms_rtc_wakeup_stop) | 0x0800A73C | Stop the RTC wake-up timer by calling helper 0x08002348 on the RTC handle |
| [`bms_tm_to_epoch`](#bms_tm_to_epoch) | 0x08001188 | Converts a broken-down time record to Unix epoch seconds and normalises it in place |

## HAL_RTCEx_DeactivateWakeUpTimer

**Disables the RTC wake-up timer and its interrupt, waiting for WUTWF**

Returns 2 (HAL_BUSY) if the lock byte at handle+0x28 is set. Otherwise it takes the lock, sets state BUSY, unlocks RTC write protection with 0xCA then 0x53 (WPR at offset 0x24), and clears CR bit 10 (WUTE) and bit 14 (WUTIE). It waits up to 1000 ms for ICSR bit 2 (WUTWF) to set, relocks write protection with 0xFF, sets state READY and returns 0. On timeout it relocks, sets state TIMEOUT (3) and returns 3.

| Parameter | Type | Description |
|---|---|---|
| `hrtc` | `ptr` | param_1, RTC handle |

**Returns** `u32`: HAL status: 0 OK, 2 busy, 3 timeout

- Addresses by version: 4130: 0x08002348, 4139: 0x08002348, 4148: 0x08002348, 4168: 0x08002348
- Called by: `bms_rtc_wakeup_stop`
- Calls: `bms_get_ram_word_200006a0`
- Confidence: high

## HAL_RTCEx_SetSynchroShift

**Writes RTC SHIFTR (add-one-second and sub-second shift) after waiting for SHPF**

Uses the same busy and write-protection pattern as HAL_RTCEx_DeactivateWakeUpTimer. It waits up to 1000 ms for ICSR bit 3 (SHPF, shift pending) to clear and returns 3 on timeout. If CR bit 4 is clear it writes SHIFTR = param_3 | param_2, then unless CR bit 5 is set it waits for RSF through bms_4168_08002868. Success returns 0 with state READY; a set CR bit 4 or a failed RSF wait sets state ERROR and returns 1.

| Parameter | Type | Description |
|---|---|---|
| `hrtc` | `ptr` | param_1, RTC handle |
| `add1s` | `u32` | param_2, ShiftAdd1S value (bit 31 of SHIFTR) |
| `subfs` | `u32` | param_3, ShiftSubFS sub-second shift value |

**Returns** `u32`: HAL status: 0 OK, 1 error, 3 timeout

**Notes:** Bit numbers follow STM32G0 RTC naming (CR bits 4 and 5, ICSR bit 3 SHPF). The meaning of the bit-4 check is not confirmed.

- Addresses by version: 4130: 0x080023CA, 4139: 0x080023CA, 4148: 0x080023CA, 4168: 0x080023CA
- Called by: `bms_rtc_hal_init`
- Calls: `bms_get_ram_word_200006a0`, `HAL_RTC_WaitForSynchro`
- Confidence: medium

## HAL_RTCEx_SetWakeUpTimer_IT

**Sets the RTC wake-up counter and clock, unmasks EXTI line 19 and enables the interrupt**

After the busy check and write-protection unlock, it clears CR bit 10 (WUTE) and sets SCR bit 2 to clear any stale wake-up flag. Unless ICSR INIT (bit 7) is set, it waits up to 1000 ms for WUTWF (ICSR bit 2) and returns 3 on timeout. It then writes the counter to WUTR (offset 0x14), puts the clock select into CR bits 0-2 from param_3, sets EXTI IMR1 bit 19 (0x40021880) for the RTC wake-up line, and sets CR WUTIE (bit 14) and WUTE (bit 10). It relocks write protection, sets state READY and returns 0.

| Parameter | Type | Description |
|---|---|---|
| `hrtc` | `ptr` | param_1, RTC handle |
| `counter` | `u32` | param_2, wake-up counter value (WUTR) |
| `clock` | `u32` | param_3, wake-up clock select (WUCKSEL) |

**Returns** `u32`: HAL status: 0 OK, 3 timeout

- Addresses by version: 4130: 0x08002470, 4139: 0x08002470, 4148: 0x08002470, 4168: 0x08002470
- Peripheral registers: `RTC.RTC_ICSR` (R), `EXTI.IMR1` (RW)
- Called by: `bms_rtc_wakeup_period_set`
- Calls: `bms_get_ram_word_200006a0`
- Confidence: high

## HAL_RTCEx_WakeUpTimerIRQHandler

**RTC wake-up interrupt handler: clears WUTF, runs the event callback, sets READY**

If the masked flag WUTMF (instance MISR offset 0x50, bit 2) is set, it writes SCR bit 2 to clear the wake-up flag and calls bms_empty_stub (bms_4168_08002540), the weak HAL_RTCEx_WakeUpTimerEventCallback. It then sets the handle state to READY (1) unconditionally. It is called from bms_4168_08003614 in another packet, and the vector is probably RTC_TAMP (IRQ 2).

| Parameter | Type | Description |
|---|---|---|
| `hrtc` | `ptr` | param_1, RTC handle |

- Addresses by version: 4130: 0x08002542, 4139: 0x08002542, 4148: 0x08002542, 4168: 0x08002542
- Called by: `RTC_TAMP_IRQHandler`
- Calls: `bms_empty_stub`
- Confidence: high

## HAL_RTC_GetDate

**Reads RTC_DR and returns weekday, month, date and year, converting BCD to binary when format is 0**

Reads the RTC DR register through the handle (the first handle word points at the RTC peripheral, DR at +4) and writes four bytes to the output record. Byte 0 is the weekday from DR.WDU (bits 13-15), byte 1 is the month from DR.MT and MU (bit 12 and bits 8-11), byte 2 is the day from DR.DT and DU (bits 4-5 and bits 0-3), and byte 3 is the year from DR.YT and YU (bits 20-23 and bits 16-19). When format is 0 (binary) each BCD field is converted as tens * 10 + units. The decompile shows no state or lock check, and the function always returns 0 (HAL_OK).

| Parameter | Type | Description |
|---|---|---|
| `hrtc` | `ptr` | RTC handle; word 0 points at the RTC peripheral |
| `sDate` | `ptr` | output RTC_DateTypeDef record: WeekDay, Month, Date, Year as bytes 0 to 3 |
| `format` | `u32` | 0 = binary output (fields converted from BCD), non-zero = BCD output |

**Returns** `u32`: HAL status; 0 (HAL_OK) on every path in this build

- Addresses by version: 4130: 0x08002564, 4139: 0x08002564, 4148: 0x08002564, 4168: 0x08002564
- Called by: `bms_rtc_datetime_pack`
- Confidence: high

## HAL_RTC_GetTime

**Reads RTC_TR, SSR and PRER and returns hours, minutes, seconds, AM/PM and sub-seconds**

Reads RTC TR through the handle and writes hours (TR bits 16-21), minutes (bits 8-14), seconds (bits 0-6) and the AM/PM flag (bit 22) as bytes 0 to 3 of the output record. It then stores SSR as the 32-bit SubSeconds at +4 and PRER & 0x7FFF as the 32-bit SecondFraction at +8. With format 0 (binary) the hour, minute and second bytes are converted from BCD. It returns 0 and does no state check.

| Parameter | Type | Description |
|---|---|---|
| `hrtc` | `ptr` | RTC handle; word 0 points at the RTC peripheral |
| `sTime` | `ptr` | output RTC_TimeTypeDef record: Hours, Minutes, Seconds, TimeFormat, SubSeconds, SecondFraction |
| `format` | `u32` | 0 = binary output (fields converted from BCD), non-zero = BCD output |

**Returns** `u32`: HAL status; 0 (HAL_OK) on every path in this build

**Notes:** The decompile does not show the read of RTC DR that ST's HAL normally performs after TR to release the shadow registers. This is either a different HAL revision or the read was removed.

- Addresses by version: 4130: 0x080025BC, 4139: 0x080025BC, 4148: 0x080025BC, 4168: 0x080025BC
- Called by: `bms_rtc_datetime_pack`
- Confidence: high

## HAL_RTC_Init

**Initialises the RTC: enters init mode, programs format, output and prescalers, exits init**

Returns 1 for a NULL handle. On first use (state RESET) it clears the lock, stores 0x8800 in handle word 1 and runs HAL_RTC_MspInit (bms_4168_080026cc). It sets state BUSY, unlocks write protection and enters init mode with RTC_EnterInitMode (bms_4168_0800352c). It then rewrites CR from handle words 2, 5 and 7 (hour format, output and output polarity), after clearing those fields, and writes PRER from word 4 (synchronous prescaler) and word 3 (asynchronous prescaler in bits 16 and up). It calls RTC_ExitInitMode (bms_4168_08003570), rebuilds CR bits 29-31 from handle words 6, 8 and 9, relocks, sets READY and returns the first failing status (3 on timeout).

| Parameter | Type | Description |
|---|---|---|
| `hrtc` | `ptr` | param_1, RTC handle with Init fields at words 1 to 9 |

**Returns** `u32`: HAL status: 0 OK, 1 NULL handle, 3 timeout

**Notes:** The handle layout is inferred from offsets only, not from a struct definition. The 0x8800 value stored in word 1 has no clear meaning here.

- Addresses by version: 4130: 0x08002628, 4139: 0x08002628, 4148: 0x08002628, 4168: 0x08002628
- Called by: `bms_rtc_hal_init`
- Calls: `HAL_RTC_MspInit`, `RTC_EnterInitMode`, `bms_rtc_wait_synchro`
- Confidence: medium

## HAL_RTC_MspInit

**Enables the RTC clock (BDCR.RTCEN and APBENR1.RTCAPBEN) when the handle is for the RTC**

If the handle's instance pointer equals the RTC peripheral, it sets RCC BDCR bit 15 (RTCEN) and RCC APBENR1 bit 10 (RTCAPBEN), each by read-modify-write. It then reads APBENR1 back to let the clock enable settle. This is the usual CubeMX HAL_RTC_MspInit body, which expands the __HAL_RCC_RTC_ENABLE macro. For any other instance it does nothing and returns.

| Parameter | Type | Description |
|---|---|---|
| `rtcHandle` | `ptr` | RTC handle; word 0 is the peripheral instance pointer |

**Notes:** The name is inferred from the CubeMX MspInit pattern (instance check followed by RTC clock enable). The clock bits themselves are read directly from the register database.

- Addresses by version: 4130: 0x080026CC, 4139: 0x080026CC, 4148: 0x080026CC, 4168: 0x080026CC
- Peripheral registers: `RCC.APBENR1` (RW), `RCC.BDCR` (RW)
- Called by: `HAL_RTC_Init`
- Confidence: medium

## HAL_RTC_SetDate

**Writes the RTC date register from a weekday, month, date and year record**

Returns 2 when the lock is held. In binary format it first handles a month byte with bit 4 set (month becomes (month & 0xEF) + 10) and converts weekday, month, date and year to BCD with bms_u8_to_bcd (bms_4168_08003514). It sets state BUSY, unlocks write protection, enters init mode through bms_4168_0800352c, writes DR (offset 4) as year << 16 | month << 8 | date | weekday << 13 masked with 0xFFFF3F, and exits init mode through bms_4168_08003570. It relocks, sets READY and returns the first failing status.

| Parameter | Type | Description |
|---|---|---|
| `hrtc` | `ptr` | param_1, RTC handle |
| `sdate` | `ptr` | param_2, date record: weekday, month, date, year bytes |
| `format` | `u32` | param_3, 0 for binary input, non-zero for BCD |

**Returns** `u32`: HAL status: 0 OK, 2 busy, 3 timeout

- Addresses by version: 4130: 0x08002704, 4139: 0x08002704, 4148: 0x08002704, 4168: 0x08002704
- Called by: `bms_rtc_set_datetime_packed`
- Calls: `bms_u8_to_bcd`, `RTC_EnterInitMode`, `bms_rtc_wait_synchro`
- Confidence: high

## HAL_RTC_SetTime

**Writes the RTC time register from hours, minutes and seconds, plus DST and store bits**

Same lock and write-protection sequence as HAL_RTC_SetDate. The TimeFormat byte of the record is cleared when CR bit 6 (12-hour format) is clear, and in binary format hours, minutes and seconds are converted to BCD with bms_u8_to_bcd. After entering init mode through bms_4168_0800352c it writes TR (offset 0) as the packed fields masked with 0x7F7F7F, clears CR bit 18, ORs in the DayLightSaving and StoreOperation words from the record, and exits init mode through bms_4168_08003570. It relocks, sets READY and returns the first failing status.

| Parameter | Type | Description |
|---|---|---|
| `hrtc` | `ptr` | param_1, RTC handle |
| `stime` | `ptr` | param_2, time record: hours, minutes, seconds, TimeFormat, DayLightSaving, StoreOperation |
| `format` | `u32` | param_3, 0 for binary input, non-zero for BCD |

**Returns** `u32`: HAL status: 0 OK, 2 busy, 3 timeout

- Addresses by version: 4130: 0x080027A4, 4139: 0x080027A4, 4148: 0x080027A4, 4168: 0x080027A4
- Called by: `bms_rtc_set_datetime_packed`
- Calls: `bms_u8_to_bcd`, `RTC_EnterInitMode`, `bms_rtc_wait_synchro`
- Confidence: high

## HAL_RTC_WaitForSynchro

**Clears RSF and waits up to 1000 ms for the RTC shadow registers to resynchronise**

Writes ICSR with RSF (bit 5) and INIT (bit 7) cleared, which clears RSF, then polls ICSR until RSF is set. It returns 0 when RSF sets, or 3 when it has not set within 1000 ms by the tick counter. It is called from HAL_RTCEx_SetSynchroShift (bms_4168_080023ca) in this packet.

| Parameter | Type | Description |
|---|---|---|
| `hrtc` | `ptr` | param_1, RTC handle |

**Returns** `u32`: HAL status: 0 OK, 3 timeout

- Addresses by version: 4130: 0x08002868, 4139: 0x08002868, 4148: 0x08002868, 4168: 0x08002868
- Called by: `HAL_RTCEx_SetSynchroShift`
- Calls: `bms_get_ram_word_200006a0`
- Confidence: high

## RTC_EnterInitMode

**Sets RTC INIT and waits up to 1000 ms for INITF before RTC registers are written**

If INITF (ICSR bit 6) is already set nothing is done. Otherwise it sets INIT (ICSR bit 7) and polls INITF; if it stays clear for more than 1000 ms by the tick counter it sets the handle state to TIMEOUT (3) and returns 3. Returns 0 on success. It is called by HAL_RTC_Init, HAL_RTC_SetDate and HAL_RTC_SetTime in this packet, and the matching exit routine is bms_4168_08003570, which is outside this packet.

| Parameter | Type | Description |
|---|---|---|
| `hrtc` | `ptr` | param_1, RTC handle |

**Returns** `u32`: HAL status: 0 OK, 3 timeout

- Addresses by version: 4130: 0x0800352C, 4139: 0x0800352C, 4148: 0x0800352C, 4168: 0x0800352C
- Called by: `HAL_RTC_Init`, `HAL_RTC_SetDate`, `HAL_RTC_SetTime`
- Calls: `bms_get_ram_word_200006a0`
- Confidence: high

## bms_epoch_to_tm

**Converts Unix epoch seconds to an eight-word struct-tm style broken-down time**

Splits the 32-bit epoch at *param_1 with successive bms_udiv32 calls: by 60 for seconds and minutes, by 24 for hours, and by 7 on the day count plus 4 for the weekday (0 is Sunday, since 1970-01-01 was a Thursday). The day count plus 731 (days since 1968-01-01) is divided by 1461 to give a year quotient (tm_year = 68 + quotient) and a day-of-cycle index taken as remainder divided by 4. That index is stored as tm_yday before a one-day correction for non-leap years after February, then month lengths from the table at 0x08010AC0 are subtracted to give tm_mon and the 1-based tm_mday. The output words are sec, min, hour, mday, mon, year-1900, wday, yday, and the function returns param_2.

| Parameter | Type | Description |
|---|---|---|
| `epoch_ptr` | `ptr` | param_1, address of the 32-bit Unix epoch seconds value |
| `out` | `ptr` | param_2, eight-word output record |

**Returns** `ptr`: param_2, the output record

**Notes:** The month length table at 0x08010AC0 and the non-leap correction (which tests the low two bits of the year quotient) are inferred from the code and not checked against test vectors. The division remainders are read from r1 of bms_udiv32, see the notes on bms_sdiv32. This is the inverse of bms_tm_to_epoch (bms_4168_08001188).

- Addresses by version: 4130: 0x08001278, 4139: 0x08001278, 4148: 0x08001278, 4168: 0x08001278
- Called by: `bms_epoch_to_tm_20005d48`, `bms_tm_to_epoch`
- Calls: `bms_udiv32`
- Confidence: medium

## bms_epoch_to_tm_20005d48

**Converts the epoch value at param_1 into the broken-down time block at 0x20005D48**

Thin wrapper around bms_epoch_to_tm (bms_4168_08001278) that passes the RAM block at 0x20005D48 as the output record. param_1 is the address of a 32-bit Unix epoch seconds value and is forwarded unchanged, so the wrapper does no arithmetic itself. Its single caller in this packet is bms_4168_08009e40, which suggests 0x20005D48 holds a cached current date and time.

| Parameter | Type | Description |
|---|---|---|
| `epoch_ptr` | `ptr` | param_1, address of the 32-bit Unix epoch seconds value to convert |

**Notes:** The use of 0x20005D48 as a cached current time is inferred from its one caller, which is outside this packet.

- Addresses by version: 4130: 0x080010F0, 4139: 0x080010F0, 4148: 0x080010F0, 4168: 0x080010F0
- Called by: `bms_packed_datetime_shift_seconds`
- Calls: `bms_epoch_to_tm`
- Confidence: high

## bms_packed_datetime_shift_seconds

**Shift a bit-packed date and time by param_1 seconds through the epoch conversion**

Decodes the bit-packed date-time record at param_2 into a tm structure (seconds in 6 bits, minutes in 6 bits, hours stored as (hour + 8) mod 24 in 5 bits, day in 5 bits, month in 4 bits, year minus 2000 in 6 bits, using the masks in the code). It converts the tm structure to epoch seconds with bms_tm_to_epoch, adds param_1, and converts back through bms_epoch_to_tm_20005d48. It then rewrites the same bit fields from the resulting tm structure, applying the same hour rule. No value is returned.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | offset in seconds added to the date-time |
| `param_2` | `ptr` | four-byte bit-packed date-time record, updated in place |

**Notes:** Bit positions were read by hand from the masks, and the hour encoding was derived from the arithmetic (stored value = (hour + 8) mod 24). The record's use by its callers is not in this packet.

- Addresses by version: 4130: 0x08008DE0, 4139: 0x080092E0, 4148: 0x08009B2C, 4168: 0x08009E40
- Called by: `bms_rtc_timestamp_record_start`
- Calls: `bms_epoch_to_tm_20005d48`, `bms_tm_to_epoch`
- Confidence: medium

## bms_rtc_backup_reset_lse_on

**Pulse the RTC backup-domain reset, clear LSE drive bits, and set LSEON**

Sets PWR.CR1 DBP (bit 8) to allow backup-domain writes, then sets and clears RCC.BDCR BDRST (bit 16), which resets the RTC, its backup registers and the RTC clock selection. It clears LSEDRV (BDCR bits 4:3) and sets LSEON (bit 0) to start the LSE oscillator at default drive. It does not wait for LSERDY, so the caller must poll bms_rtc_lse_ready_get. Called only from bms_4168_08006514.

**Notes:** The reset pulse is what clears the RTC configuration, so the caller must reprogram it afterwards. The reason it is called from bms_4168_08006514 is not in this packet.

- Addresses by version: 4130: 0x08008B44, 4139: 0x08009044, 4148: 0x08009890, 4168: 0x08009BA4
- Peripheral registers: `PWR.CR1` (RW), `RCC.APBENR2` (A), `RCC.BDCR` (RW)
- Called by: `bms_rtc_reset_with_snapshot`
- Confidence: high

## bms_rtc_clock_bringup

**Start the RTC clock: try LSE with a timeout, fall back to LSI, select it, enable RTC**

Brings up the RTC clock source in the RCC backup domain. It first tests RTCSEL (RCC.BDCR bits 9:8). If that already selects LSE (0x100), it sets PWR.CR1 DBP (bit 8) to unlock backup-domain writes, clears LSEDRV (BDCR bits 4:3), sets LSEON, and polls LSERDY (BDCR bit 1) for up to 800000 iterations. On success it selects LSE, pulses BDRST (BDCR bit 16) if the select did not take, sets DAT_20000690 to 1 and goes to the end. Otherwise (LSE not selected, or LSE timed out) it clears LSEON and BDCR bit 5 (LSECSSON), sets LSION (RCC.CSR bit 0), polls LSIRDY (CSR bit 1) up to 0x88000 iterations, stores the timeout result in DAT_20000692, selects LSI (RTCSEL = 0x200) with the same BDRST retry, and clears DAT_20000690. The end sets RTCEN (BDCR bit 15).

**Notes:** Likely defect: the wait counter uVar3 is not reset between the LSE and LSI waits. When LSE was selected and timed out, the counter is already 800000, which is above the LSI bound of 0x88000 (557056). The LSI poll loop then never runs, DAT_20000692 is set to 1 without checking LSIRDY, and LSION is left enabled with no wait. Only the path where RTCSEL was not LSE polls LSI properly. Check the disassembly before relying on the LSI-timeout flag. DAT_20000690 (LSE active) and DAT_20000692 (LSI timeout) are read elsewhere; those readers are not in this packet.

- Addresses by version: 4130: 0x08008A3C, 4139: 0x08008F3C, 4148: 0x08009788, 4168: 0x08009A9C
- Peripheral registers: `PWR.CR1` (RW), `RCC.BDCR` (RW), `RCC.CSR` (RW)
- Called by: `bms_sysclk_hse_pll_bringup`
- Confidence: high

## bms_rtc_datetime_pack

**Read RTC date and time in binary and pack them into a 4-byte bit-field record**

Reads the RTC calendar through HAL_RTC_GetDate and HAL_RTC_GetTime in binary format, using the RTC handle at RAM 0x20005D00. It packs the day of month into bits 0-5 of the output (from the Date byte of the date structure), the month into bits 6-11 (Month byte), the weekday into bits 12-16 (WeekDay byte) and the seconds, masked to 5 bits, into bits 17-21. Hour, minute and AM/PM fields are merged into the upper bytes with the same masking style, but their exact positions are only partly decoded, and the year byte is not packed. The routine writes only the output record.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output record, 4 bytes written as two u16 bit-field words |

**Notes:** Hour, minute and AM/PM bit positions are not fully confirmed. Case 9 of bms_telemetry_block_fill stores this record in the telemetry frame.

- Addresses by version: 4130: 0x08008D24, 4139: 0x08009224, 4148: 0x08009A70, 4168: 0x08009D84
- Called by: `bms_status_event_snapshot`, `bms_history_ring_commit`, `bms_rtc_reset_with_snapshot`, `bms_rtc_timestamp_record_start`, `bms_snapshot_logger_tick`, `bms_telemetry_block_fill_16`, `bms_setpoint_window_sample`, `bms_msg_dispatch_request`
- Calls: `HAL_RTC_GetDate`, `HAL_RTC_GetTime`
- Confidence: medium

## bms_rtc_fallback_lsi_start

**Fall back to the LSI clock for the RTC: enable LSI, wait, select it and init the RTC**

Clears BDCR bit 0 (LSEON), bit 5 and RTCEN, sets PWR_CR1 bit 8 (DBP) to unlock backup writes, pulses the backup-domain reset (BDCR bit 16), then sets RCC_CSR LSION and polls LSIRDY for up to 0x88000 iterations. The timeout result is stored in 0x20000692 and copied to 0x20000694. It then selects LSI (RTCSEL = 0x200), sets RTCEN, clears 0x20000690 so that the 0x7C prescaler is used, and calls bms_4168_08009D08. It returns 1 when the RTC initialises and 0 otherwise.

**Returns** `u32`: 1 when the RTC initialised on LSI, 0 otherwise

**Notes:** The meaning of BDCR bit 5 is not established here. The fallback is entered from bms_4168_080065E0 and bms_4168_080082BC.

- Addresses by version: 4130: 0x08008BEC, 4139: 0x080090EC, 4148: 0x08009938, 4168: 0x08009C4C
- Peripheral registers: `PWR.CR1` (RW), `RCC.APBENR2` (A), `RCC.BDCR` (RW), `RCC.CSR` (RW)
- Called by: `bms_rtc_timestamp_record_start`, `bms_4168_080082bc`
- Calls: `bms_rtc_hal_init`
- Confidence: medium

## bms_rtc_hal_init

**Fill the RTC handle (async prescaler 0x7C or 0x7F, sync 0xFF) and call HAL_RTC_Init**

Fills the RTC handle at 0x20005D00 (the RTC instance first) in HAL layout: hour format 0, asynchronous prescaler 0x7C when 0x20000690 is 0 (LSI) or 0x7F when it is 1 (LSE), synchronous prescaler 0xFF, and output fields zero, with one further field set to 0x40000000. The prescalers give 32768 Hz / 1 Hz on LSE (128 * 256) and 32000 Hz / 1 Hz on a nominal 32 kHz LSI (125 * 256). It calls HAL_RTC_Init (bms_4168_08002628); on failure it clears 0x20000690 and returns 0. On success, in LSE mode only, it calls HAL_RTCEx_SetSynchroShift (bms_4168_080023CA) with 0 and 0x66 and returns 1.

**Returns** `u32`: 1 on success, 0 when HAL_RTC_Init fails

**Notes:** The meaning of the 0x40000000 field and of the 0x66 shift value is not established here.

- Addresses by version: 4130: 0x08008CA8, 4139: 0x080091A8, 4148: 0x080099F4, 4168: 0x08009D08
- Peripheral registers: `TIM2.CR1` (A), `RTC.RTC_TR` (A)
- Called by: `bms_4168_080082bc`, `bms_rtc_select_lse_and_start`, `bms_rtc_fallback_lsi_start`
- Calls: `HAL_RTCEx_SetSynchroShift`, `HAL_RTC_Init`
- Confidence: high

## bms_rtc_lse_ready_get

**Return the LSE ready flag (RCC.BDCR LSERDY, bit 1)**

Reads RCC.BDCR and returns (value & 3) >> 1, which is bit 1, LSERDY, as 0 or 1. It has no side effects and is a plain polling read for LSE readiness. The function has no direct callers in this packet; it is an entry point, callback or indirect call.

**Returns** `u32`: 1 when the LSE oscillator is ready, else 0

- Addresses by version: 4130: 0x08008B7C, 4139: 0x0800907C, 4148: 0x080098C8, 4168: 0x08009BDC
- Peripheral registers: `RCC.BDCR` (R)
- Confidence: high

## bms_rtc_reset_with_snapshot

**Snapshot the RTC time, reset the RTC backup domain and LSE, and set shared state to 3**

Calls bms_4168_08009d84 to store a time value at 0x20001C84, calls bms_rtc_backup_reset_lse_on, which pulses the backup-domain reset and turns LSE on, takes a time-base stamp from bms_tick_get into 0x20001C80, and sets the shared state byte 0x20001C8A to 3. It always returns 0.

**Returns** `u32`: always 0

**Notes:** The reason this path runs is not in the packet. State byte 0x20001C8A is shared with bms_nibble_debounce_1s, which uses values 1 and 2.

- Addresses by version: 4130: 0x08005964, 4139: 0x08005B80, 4148: 0x080063A8, 4168: 0x08006514
- Calls: `bms_rtc_backup_reset_lse_on`, `bms_rtc_datetime_pack`, `bms_tick_get`
- Confidence: medium

## bms_rtc_select_lse_and_start

**Select LSE as the RTC clock in the backup domain and start the RTC**

Clears RTCEN in RCC.BDCR and sets RTCSEL to LSE (0x100). If the select does not take, it pulses BDRST (bit 16) and selects LSE again. It clears the LSE timeout flag at 0x20000692, sets the LSE-in-use flag at 0x20000690 to 1, sets RTCEN and calls bms_4168_08009D08 (RTC init). It returns true when the RTC initialises; on failure bms_4168_08009D08 clears 0x20000690, which tells the caller to fall back to LSI.

**Returns** `bool`: true when the RTC initialised on LSE

**Notes:** The routine assumes LSEON is already set by the caller, since BDCR bit 0 is not written here.

- Addresses by version: 4130: 0x08008B8C, 4139: 0x0800908C, 4148: 0x080098D8, 4168: 0x08009BEC
- Peripheral registers: `RCC.APBENR2` (A), `RCC.BDCR` (RW)
- Calls: `bms_rtc_hal_init`
- Confidence: high

## bms_rtc_set_datetime_packed

**Load the packed date-time record into the RTC with HAL_RTC_SetDate and HAL_RTC_SetTime**

Unpacks the same bit-packed record as bms_packed_datetime_shift_seconds. The date is built as weekday 0, month, day and year (year minus 2000) and the time as hours, minutes and seconds, both in binary format. It calls HAL_RTC_SetDate (bms_4168_08002704) and then HAL_RTC_SetTime (bms_4168_080027A4) on the RTC handle at 0x20005D00. The hour is written as the raw 5-bit field, without the +8 correction that bms_packed_datetime_shift_seconds applies. It returns 1 when both calls return 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | four-byte bit-packed date-time record |

**Returns** `u32`: 1 when both HAL calls succeed, otherwise 0

**Notes:** The raw-hour write may be an inconsistency with the +8 hour encoding used elsewhere; the packed record's convention should be confirmed before relying on it. The weekday is written as 0.

- Addresses by version: 4130: 0x08008F18, 4139: 0x08009418, 4148: 0x08009C64, 4168: 0x08009F78
- Called by: `bms_rtc_timestamp_record_start`, `bms_msg_dispatch_request`
- Calls: `HAL_RTC_SetDate`, `HAL_RTC_SetTime`
- Confidence: medium

## bms_rtc_timestamp_record_start

**Capture the RTC date and time, prepare the record at 0x20001C84 and set its state byte to 2**

Calls bms_rtc_datetime_pack (bms_4168_08009d84), which reads the RTC date and time in binary and packs them into a 4-byte bit-field record. It then calls bms_4168_08009c4c, calls bms_4168_08009e40 with argument 3 and the record at 0x20001C84, and calls bms_4168_08009f78 on that record. It sets the byte at 0x20001C8A to 2 and returns 1. The helpers are not yet described, so the record layout and what argument 3 selects are open.

**Returns** `u32`: always 1

**Notes:** The return value of bms_rtc_datetime_pack is not used here, so the packed record must be stored by the helper itself. The meaning of 2 in the state byte and of argument 3 are inferred.

- Addresses by version: 4130: 0x08005A30, 4139: 0x08005C4C, 4148: 0x08006474, 4168: 0x080065E0
- Calls: `bms_rtc_fallback_lsi_start`, `bms_rtc_datetime_pack`, `bms_packed_datetime_shift_seconds`, `bms_rtc_set_datetime_packed`
- Confidence: low

## bms_rtc_wait_synchro

**Wait for the RTC register-sync flag (RSF) with a 1000-tick timeout; returns 0 or 3**

Waits until the RTC shadow registers are synchronised, the same job as HAL_RTC_WaitForSynchro. param_1 is a handle whose first word is the RTC register base, so RTC_ICSR is at base+0x0C and RTC_CR at base+0x18. The routine clears ICSR bit 7 (INIT) on every call, then clears RSF (ICSR bit 5, a write-0-to-clear flag) and polls until hardware sets it again. Polling is timed against the counter returned by bms_get_ram_word_200006a0; more than 1000 ticks elapsed means timeout, the handle's status byte at +0x29 becomes 3 and the function returns 3. When CR bit 5 is set it is cleared for the wait and set again afterwards, on both the success and timeout paths.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `ptr` | param_1; word 0 is the RTC register base, byte +0x29 receives the status code |

**Returns** `u32`: 0 when RSF was seen, 3 on timeout

**Notes:** Bit names follow the ST RTC layout (ICSR.INIT, ICSR.RSF, CR.BYPSHAD); the code shows only the bit positions, so those labels are medium confidence. The 1000 limit is in counter ticks; whether a tick is 1 ms depends on the SysTick setup, which is not in this packet.

- Addresses by version: 4130: 0x08003570, 4139: 0x08003570, 4148: 0x08003570, 4168: 0x08003570
- Peripheral registers: `RTC.RTC_ICSR` (RW), `RTC.RTC_CR` (RW)
- Called by: `HAL_RTC_Init`, `HAL_RTC_SetDate`, `HAL_RTC_SetTime`
- Calls: `bms_get_ram_word_200006a0`
- Confidence: high

## bms_rtc_wakeup_period_set

**Arm the RTC wake-up timer for 1 to 31 seconds with RTC_TAMP IRQ priority 1**

Sets a periodic RTC wake-up interrupt. The argument is clamped to 1 to 31 (0 becomes 1, values above 31 become 31). The wake-up counter is clamp * 2000 when DAT_20000690 is 0, which suits LSI divided by 16 (about 2 kHz), and clamp << 11 when it is nonzero, which suits LSE divided by 16 (2048 Hz), so the period is about clamp seconds either way. It sets priority 1 (preempt 1, sub 0) on IRQ 2 (RTC_TAMP) through the priority helper at 0x080022B0, enables IRQ 2 through __NVIC_EnableIRQ, and starts the wake-up timer through the helper at 0x08002470 with the RTC handle at 0x20005D00, the counter and clock select 0 (RTCCLK / 16).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | requested period in seconds, clamped to 1 to 31 |

**Notes:** The role of FUN_08002470 is inferred from its arguments and is not described in this packet. The LSE flag at 0x20000690 is taken from its use here only.

- Addresses by version: 4130: 0x0800978C, 4139: 0x08009CC4, 4148: 0x0800A3E0, 4168: 0x0800A6F4
- Called by: `bms_4168_080082f0`
- Calls: `__NVIC_EnableIRQ`, `__NVIC_SetPriority`, `HAL_RTCEx_SetWakeUpTimer_IT`
- Confidence: medium

## bms_rtc_wakeup_stop

**Stop the RTC wake-up timer by calling helper 0x08002348 on the RTC handle**

Calls the helper at 0x08002348 with the RTC handle at 0x20005D00 and does nothing else. The helper is not described in this packet. It is most likely the HAL RTC wake-up deactivation routine, which pairs with bms_rtc_wakeup_period_set, but that is inferred from the single handle argument.

**Notes:** Identity of the helper at 0x08002348 is unconfirmed.

- Addresses by version: 4130: 0x080097D4, 4139: 0x08009D0C, 4148: 0x0800A428, 4168: 0x0800A73C
- Called by: `bms_4168_080082f0`
- Calls: `HAL_RTCEx_DeactivateWakeUpTimer`
- Confidence: low

## bms_tm_to_epoch

**Converts a broken-down time record to Unix epoch seconds and normalises it in place**

Reads a struct-tm style record (word 0 sec, 1 min, 2 hour, 3 mday, 4 month 0-11, 5 year minus 1900). It divides the month count (year*12 + month - 840) by 48 with bms_sdiv32 to get 4-year blocks since 1970, multiplies the block count by 126230400 (1461 days), adds 365 days per whole year inside the block, and adds the lengths of completed months from a byte table at 0x08010AB3. A leap day (86400 s) is added when the month index inside the block is 26 or more, which matches the 1972 leap year of the 1970-based cycle. It then calls bms_epoch_to_tm to rewrite all eight words in normalised form and returns the epoch value.

| Parameter | Type | Description |
|---|---|---|
| `tm` | `ptr` | param_1, struct-tm style record, read and rewritten in normalised form |
| `unused_2` | `u32` | param_2, not used |
| `unused_3` | `u32` | param_3, not used |
| `unused_4` | `u32` | param_4, read into a local and then overwritten, not used |

**Returns** `u32`: Unix epoch seconds

**Notes:** The month length table at 0x08010AB3 is not decoded in this packet, so the day counts are inferred from the code. The leap-day rule assumes the 1970-based 4-year cycle. Pre-1970 inputs go through the unsigned remainder of bms_sdiv32 and are not reliable.

- Addresses by version: 4130: 0x08001188, 4139: 0x08001188, 4148: 0x08001188, 4168: 0x08001188
- Called by: `bms_packed_datetime_shift_seconds`
- Calls: `bms_sdiv32`, `bms_epoch_to_tm`
- Confidence: medium
