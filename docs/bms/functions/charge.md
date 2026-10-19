# BMS - `charge` functions

1 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_setpoint_window_sample`](#bms_setpoint_window_sample) | 0x0800E478 | Run a window comparator with hysteresis on 30000-tick sampling and restore the control shadows |

## bms_setpoint_window_sample

**Run a window comparator with hysteresis on 30000-tick sampling and restore the control shadows**

Runs a window comparator with hysteresis on two 11-bit limits, every 30000 ticks or at once when bit 3 of DAT_200005C0 is set. Shadow copies of the state block control words at +0x10E and +0x110 live in DAT_200005C8 and DAT_200005CA, and bms_4168_08009d84 supplies a 32-bit measurement; measurement bits 6 to 16 are compared with the setpoint in DAT_200005C8 bits 0 to 10 and with a second limit built from DAT_200005CA bits 0 to 5 and DAT_200005C8 bits 11 to 15, and DAT_200005C2 remembers the side last crossed. The in-window result is written to bit 0 of DAT_200005C1, and bit 5 of DAT_200005C0 is set when bits 1 to 5 of DAT_200005CA equal the top five bits of the measurement. A request on state block +0x194 bit 5 that drops after being seen (latched in DAT_200005C4), or a value below 5 at +0x11E, restores the state block words from the shadows, clears bit 3 of DAT_200005C0 and bit 6 of DAT_200005CA, and sets bit 0 of DAT_200005C1.

**Notes:** The 11-bit field extraction and the 30000-tick window are exact from the decompile. The meaning of the setpoints and of the state block words is not identified. Bit 7 of DAT_200005CA can hold the result at 1 under conditions on DAT_200005C1 and DAT_200005C0, which is not described above. The caller is bms_4168_08008006 and the request handshake is bms_ctrl_request_handshake.

- Addresses by version: 4130: 0x0800CA28, 4139: 0x0800D024, 4148: 0x0800E024, 4168: 0x0800E478
- Called by: `bms_4168_08008006`
- Calls: `bms_rtc_datetime_pack`, `bms_ram_20000bdc_addr`, `bms_ctrl_request_handshake`
- Confidence: medium
