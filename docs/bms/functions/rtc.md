# BMS - `rtc` functions

6 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`HAL_RTC_GetDate`](#hal_rtc_getdate) | 0x08002564 | Reads RTC_DR and returns weekday, month, date and year, converting BCD to binary when format is 0 |
| [`HAL_RTC_GetTime`](#hal_rtc_gettime) | 0x080025BC | Reads RTC_TR, SSR and PRER and returns hours, minutes, seconds, AM/PM and sub-seconds |
| [`HAL_RTC_MspInit`](#hal_rtc_mspinit) | 0x080026CC | Enables the RTC clock (BDCR.RTCEN and APBENR1.RTCAPBEN) when the handle is for the RTC |
| [`bms_rtc_backup_reset_lse_on`](#bms_rtc_backup_reset_lse_on) | 0x08009BA4 | Pulse the RTC backup-domain reset, clear LSE drive bits, and set LSEON |
| [`bms_rtc_clock_bringup`](#bms_rtc_clock_bringup) | 0x08009A9C | Start the RTC clock: try LSE with a timeout, fall back to LSI, select it, enable RTC |
| [`bms_rtc_lse_ready_get`](#bms_rtc_lse_ready_get) | 0x08009BDC | Return the LSE ready flag (RCC.BDCR LSERDY, bit 1) |

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
- Called by: `bms_4168_08009d84`
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
- Called by: `bms_4168_08009d84`
- Confidence: high

## HAL_RTC_MspInit

**Enables the RTC clock (BDCR.RTCEN and APBENR1.RTCAPBEN) when the handle is for the RTC**

If the handle's instance pointer equals the RTC peripheral, it sets RCC BDCR bit 15 (RTCEN) and RCC APBENR1 bit 10 (RTCAPBEN), each by read-modify-write. It then reads APBENR1 back to let the clock enable settle. This is the usual CubeMX HAL_RTC_MspInit body, which expands the __HAL_RCC_RTC_ENABLE macro. For any other instance it does nothing and returns.

| Parameter | Type | Description |
|---|---|---|
| `rtcHandle` | `ptr` | RTC handle; word 0 is the peripheral instance pointer |

**Notes:** The name is inferred from the CubeMX MspInit pattern (instance check followed by RTC clock enable). The clock bits themselves are read directly from the register database.

- Addresses by version: 4130: 0x080026CC, 4139: 0x080026CC, 4148: 0x080026CC, 4168: 0x080026CC
- Peripheral registers: `RCC.APBENR1` (RW), `RCC.BDCR` (RW)
- Called by: `bms_4168_08002628`
- Confidence: medium

## bms_rtc_backup_reset_lse_on

**Pulse the RTC backup-domain reset, clear LSE drive bits, and set LSEON**

Sets PWR.CR1 DBP (bit 8) to allow backup-domain writes, then sets and clears RCC.BDCR BDRST (bit 16), which resets the RTC, its backup registers and the RTC clock selection. It clears LSEDRV (BDCR bits 4:3) and sets LSEON (bit 0) to start the LSE oscillator at default drive. It does not wait for LSERDY, so the caller must poll bms_rtc_lse_ready_get. Called only from bms_4168_08006514.

**Notes:** The reset pulse is what clears the RTC configuration, so the caller must reprogram it afterwards. The reason it is called from bms_4168_08006514 is not in this packet.

- Addresses by version: 4130: 0x08008B44, 4139: 0x08009044, 4148: 0x08009890, 4168: 0x08009BA4
- Peripheral registers: `PWR.CR1` (RW), `RCC.APBENR2` (A), `RCC.BDCR` (RW)
- Called by: `bms_4168_08006514`
- Confidence: high

## bms_rtc_clock_bringup

**Start the RTC clock: try LSE with a timeout, fall back to LSI, select it, enable RTC**

Brings up the RTC clock source in the RCC backup domain. It first tests RTCSEL (RCC.BDCR bits 9:8). If that already selects LSE (0x100), it sets PWR.CR1 DBP (bit 8) to unlock backup-domain writes, clears LSEDRV (BDCR bits 4:3), sets LSEON, and polls LSERDY (BDCR bit 1) for up to 800000 iterations. On success it selects LSE, pulses BDRST (BDCR bit 16) if the select did not take, sets DAT_20000690 to 1 and goes to the end. Otherwise (LSE not selected, or LSE timed out) it clears LSEON and BDCR bit 5 (LSECSSON), sets LSION (RCC.CSR bit 0), polls LSIRDY (CSR bit 1) up to 0x88000 iterations, stores the timeout result in DAT_20000692, selects LSI (RTCSEL = 0x200) with the same BDRST retry, and clears DAT_20000690. The end sets RTCEN (BDCR bit 15).

**Notes:** Likely defect: the wait counter uVar3 is not reset between the LSE and LSI waits. When LSE was selected and timed out, the counter is already 800000, which is above the LSI bound of 0x88000 (557056). The LSI poll loop then never runs, DAT_20000692 is set to 1 without checking LSIRDY, and LSION is left enabled with no wait. Only the path where RTCSEL was not LSE polls LSI properly. Check the disassembly before relying on the LSI-timeout flag. DAT_20000690 (LSE active) and DAT_20000692 (LSI timeout) are read elsewhere; those readers are not in this packet.

- Addresses by version: 4130: 0x08008A3C, 4139: 0x08008F3C, 4148: 0x08009788, 4168: 0x08009A9C
- Peripheral registers: `PWR.CR1` (RW), `RCC.BDCR` (RW), `RCC.CSR` (RW)
- Called by: `bms_4168_0800a130`
- Confidence: high

## bms_rtc_lse_ready_get

**Return the LSE ready flag (RCC.BDCR LSERDY, bit 1)**

Reads RCC.BDCR and returns (value & 3) >> 1, which is bit 1, LSERDY, as 0 or 1. It has no side effects and is a plain polling read for LSE readiness. The function has no direct callers in this packet; it is an entry point, callback or indirect call.

**Returns** `u32`: 1 when the LSE oscillator is ready, else 0

- Addresses by version: 4130: 0x08008B7C, 4139: 0x0800907C, 4148: 0x080098C8, 4168: 0x08009BDC
- Peripheral registers: `RCC.BDCR` (R)
- Confidence: high
