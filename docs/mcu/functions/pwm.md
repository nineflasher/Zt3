# MCU - `pwm` functions

13 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_pwm_outputs_set_enable`](#mcu_pwm_outputs_set_enable) | 0x08008594 | Enable or disable the main and complementary outputs of TMR1 channels 1-3 from flag +0x2E5 |
| [`mcu_pwm_trigger_and_clamp_select`](#mcu_pwm_trigger_and_clamp_select) | 0x08005F08 | Choose the TMR1 C4 trigger compare value and the three-phase clamp code from six inputs |
| [`mcu_tmr1_pwm_outputs_enable`](#mcu_tmr1_pwm_outputs_enable) | 0x08007BA4 | Set TMR1 CH1-3 compare values to 0x1193 and enable channels 1-3 and their complementary outputs |
| [`mcu_tmr_output_channel_setup`](#mcu_tmr_output_channel_setup) | 0x0800DECC | Configure one TMR output channel (polarity, output mode, enable) from a 4-byte record |
| [`mcu_tmr_swevt_brkswtr_set`](#mcu_tmr_swevt_brkswtr_set) | 0x0800E1AC | Set or clear the software brake event bit SWEVT.BRKSWTR (bit 7) |
| [`tmr_brkdt_config`](#tmr_brkdt_config) | 0x0800DDC0 | Write the TMR break and dead-time register (BRK) from a 7-byte configuration record |
| [`tmr_brkdt_default_para_init`](#tmr_brkdt_default_para_init) | 0x0800DE08 | Zero the seven fields of a tmr_brkdt_config_type record (default dead-time and brake setup) |
| [`tmr_channel_enable`](#tmr_channel_enable) | 0x0800DE24 | Enable or disable one output channel or its complementary output in CCTRL |
| [`tmr_channel_value_set`](#tmr_channel_value_set) | 0x0800DE7A | Write the compare value of channel 1 to 4 (C1DT..C4DT) selected by channel code |
| [`tmr_output_channel_config`](#tmr_output_channel_config) | 0x0800E012 | Configure a TMR output channel (idle states, output mode, polarity, enables) from a 7-byte record |
| [`tmr_output_default_para_init`](#tmr_output_default_para_init) | 0x0800E102 | Zero the seven fields of a tmr_output_config_type (default output channel setup) |
| [`tmr_output_enable`](#tmr_output_enable) | 0x0800E114 | Set or clear the main output enable (BRK.OEN, bit 15) of the TMR |
| [`tmr_repetition_counter_set`](#tmr_repetition_counter_set) | 0x0800E128 | Write the 8-bit repetition counter value (RPR, offset 0x30) |

## mcu_pwm_outputs_set_enable

**Enable or disable the main and complementary outputs of TMR1 channels 1-3 from flag +0x2E5**

Reads-modifies-writes TMR1.CCTRL at 0x40012C20. If the byte at param_1+0x2E5 is non-zero it ORs mask 0x555 (C1EN, C1CEN, C2EN, C2CEN, C3EN, C3CEN, bits 0,2,4,6,8,10), otherwise it ANDs with 0xFFFFFAAA, clearing the same six bits. The polarity bits (C1P, C1CP, C2P, C2CP, C3P, C3CP) and channel-4 bits are left unchanged. This is the output-enable gate for the three motor phases, using the complementary PWM of TMR1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | drive context; enable byte at +0x2E5 |

**Notes:** Mapping of the three channels to motor phases is inferred from the three-channel pattern.

- Addresses by version: 12b: 0x08008350, 143: 0x0800848C, 152: 0x0800857C, 0160: 0x08008594
- Peripheral registers: `TMR1.CCTRL` (RW)
- Called by: `mcu_0160_08007364`, `mcu_0160_0800a7f8`
- Confidence: high

## mcu_pwm_trigger_and_clamp_select

**Choose the TMR1 C4 trigger compare value and the three-phase clamp code from six inputs**

Classifies the first three arguments into a mode in DAT_20000070 and writes a compare value to DAT_20000074 through tmr_channel_value_set(&TMR1, 6, value), which is channel 4 (C4DT at 0x40). For p3 at most 510 the mode depends on p2 minus p3 and p1 minus p2 against 0x3FD: mode 0 with value 10 when all three are close, mode 1 with value p2 + 0x208 when p1 is far from p2, and mode 2 with value p3 + 0x208 when p2 is far from p3. For p3 above 510 it is mode 3 with value 10, because the value p3 - 500 is always above the clamp of 10 in that range. The minimum of p4, p5 and p6 selects a clamp code in DAT_20000071 (0x11 for p4, 0x22 for p5, 0x33 for p6). DAT_20000072 is 0xAA in mode 0, 0 in modes 2 and 3, and 1, 2 or 3 in mode 1 depending on the order of the other two arguments.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | phase or sector quantity A, compared with B in the mode test |
| `param_2` | `s32` | phase or sector quantity B |
| `param_3` | `s32` | magnitude that selects the mode (values above 510 give mode 3) |
| `param_4` | `s32` | first clamp input, compared for the minimum |
| `param_5` | `s32` | second clamp input |
| `param_6` | `s32` | third clamp input |

**Notes:** The physical meaning of the six inputs is inferred from the arithmetic (phase or sector quantities in timer counts). The 0x208 and 0x3FD constants are used literally. The caller is mcu_0160_08009a8c.

- Addresses by version: 12b: 0x08005F94, 143: 0x08005E38, 152: 0x08005E68, 0160: 0x08005F08
- Peripheral registers: `TMR1.CTRL1` (A)
- Called by: `mcu_0160_08009a8c`
- Calls: `tmr_channel_value_set`
- Confidence: medium

## mcu_tmr1_pwm_outputs_enable

**Set TMR1 CH1-3 compare values to 0x1193 and enable channels 1-3 and their complementary outputs**

Writes 0x1193 (4499) to TMR1.C1DT, C2DT and C3DT (0x40012C34, 0x40012C38, 0x40012C3C), so all three PWM channels start at the same duty. It then ORs 0x555 into TMR1.CCTRL (0x40012C20), which sets bits 0, 2, 4, 6, 8 and 10, the output-enable and complementary-enable bits of channels 1 to 3, with polarity left at active-high. The result is three-phase complementary PWM on the motor bridge. Dead-time is not set here. Called from mcu_0160_0800226c.

**Notes:** Register writes are certain. The bit names follow the usual timer layout and the duty period is not visible here.

- Addresses by version: 12b: 0x08007C80, 143: 0x08007B74, 152: 0x08007BFC, 0160: 0x08007BA4
- Peripheral registers: `TMR1.CCTRL` (ARW), `TMR1.C1DT` (W), `TMR1.C2DT` (W), `TMR1.C3DT` (W)
- Called by: `mcu_0160_0800226c`
- Confidence: high

## mcu_tmr_output_channel_setup

**Configure one TMR output channel (polarity, output mode, enable) from a 4-byte record**

Application routine, not an SDK function. record[0] selects the channel with the same codes as the SDK: 0, 2, 4 or 6 for CH1..CH4, and any other value makes it return without writing. record[1] bit 0 is the polarity CxP and bit 1 the complementary polarity CxCP (CH1 to CH3 only). record[2] bits 1:0 are written to the channel-configure field CxC, and record[3] bits 3:0 to the output control CxOCTRL (3 bits) plus CxOSEN. param_3 bit 0 is CxOIEN (output immediately enable) and bit 1 is CxOBEN (output buffer enable). Finally the main enable CxEN is set in CCTRL, and the complementary enable CxCEN is left unchanged. The CCTRL, CM1/CM2 and CxOIEN/CxOBEN bit positions follow the TMR register data for each channel.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `ptr` | 4-byte channel record: [0] channel code, [1] polarities, [2] CxC, [3] output control and OSEN |
| `param_3` | `u32` | bit 0 = output immediately enable (OIEN), bit 1 = output buffer enable (OBEN) |

**Notes:** Only caller: mcu_0160_08009800. Differs from the SDK tmr_output_channel_config (mcu_0160_0800e012): it writes CxC from the record instead of clearing it, and it does not set the idle states or CxCEN.

- Addresses by version: 12b: 0x0800DA98, 143: 0x0800DCF4, 152: 0x0800DD8C, 0160: 0x0800DECC
- Called by: `mcu_0160_08009800`
- Confidence: high

## mcu_tmr_swevt_brkswtr_set

**Set or clear the software brake event bit SWEVT.BRKSWTR (bit 7)**

Read-modify-write of bit 7 (BRKSWTR) of the software event register SWEVT (offset 0x14) with param_2 & 1, keeping the other bits. Writing 1 requests a software brake event (register data: 'Brake event triggered by software'), so the brake logic acts as if the brake input had fired. It is one of the setup steps in mcu_0160_0800ac52, which calls it with 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | 1 = request software brake event, 0 = write 0 to the bit |

**Notes:** The bit position is certain. How the break logic reacts to it depends on the BRK configuration that is not visible in this packet. Only caller: mcu_0160_0800ac52.

- Addresses by version: 12b: 0x0800DD78, 143: 0x0800DFD4, 152: 0x0800E06C, 0160: 0x0800E1AC
- Called by: `mcu_0160_0800ac52`
- Confidence: medium

## tmr_brkdt_config

**Write the TMR break and dead-time register (BRK) from a 7-byte configuration record**

Matches the Artery SDK tmr_brkdt_config. Each field is written with its own read-modify-write of BRK (offset 0x44). The 7-byte tmr_brkdt_config_type record at param_2 is laid out as: byte 0 = dead-time value DTC (BRK bits 7:0, full byte), byte 1 = BRKV brake input polarity (bit 13), byte 2 = WPC write-protect level (bits 9:8, 2 bits), byte 3 = AOEN automatic output enable (bit 14), byte 4 = FCSOEN (bit 11), byte 5 = FCSODIS (bit 10), byte 6 = BRKEN brake enable (bit 12). The main output enable OEN (bit 15) is not changed here; it belongs to tmr_output_enable. Part of the TMR helper group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `ptr` | tmr_brkdt_config_type record (7 bytes, layout in description) |

**Notes:** Only caller: mcu_0160_0800a6b8.

- Addresses by version: 12b: 0x0800D98C, 143: 0x0800DBE8, 152: 0x0800DC80, 0160: 0x0800DDC0
- Called by: `mcu_0160_0800a6b8`
- Confidence: high

## tmr_brkdt_default_para_init

**Zero the seven fields of a tmr_brkdt_config_type record (default dead-time and brake setup)**

Matches the Artery SDK tmr_brkdt_default_para_init. It clears the 7-byte record at param_1, which gives dead-time 0, brake polarity active-low (enum value 0), write protection off, and automatic output, frozen-state and brake enables all FALSE. The caller fills in the fields it needs and passes the record to tmr_brkdt_config (mcu_0160_0800ddc0).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | tmr_brkdt_config_type record to clear (7 bytes) |

**Notes:** The seven-byte zeroing body is identical to mcu_0160_0800e102 (tmr_output_default_para_init), so the two records cannot be told apart from the code alone. Only caller: mcu_0160_0800a6b8.

- Addresses by version: 12b: 0x0800D9D4, 143: 0x0800DC30, 152: 0x0800DCC8, 0160: 0x0800DE08
- Called by: `mcu_0160_0800a6b8`
- Confidence: high

## tmr_channel_enable

**Enable or disable one output channel or its complementary output in CCTRL**

Matches the Artery SDK tmr_channel_enable. param_2 is a TMR_SELECT_CHANNEL code: 0 = C1EN (CCTRL bit 0), 1 = C1CEN (bit 2), 2 = C2EN (bit 4), 3 = C2CEN (bit 6), 4 = C3EN (bit 8), 5 = C3CEN (bit 10), 6 = C4EN (bit 12); any other value does nothing. The selected bit is replaced with param_3 & 1 by a read-modify-write of CCTRL (offset 0x20). Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | channel code 0..6 (0 = CH1, 1 = CH1 complementary, ... 6 = CH4) |
| `param_3` | `u32` | confirm_state: 1 = enable, 0 = disable |

**Notes:** Callers: mcu_0160_08003060, mcu_0160_0800a6b8.

- Addresses by version: 12b: 0x0800D9F0, 143: 0x0800DC4C, 152: 0x0800DCE4, 0160: 0x0800DE24
- Called by: `mcu_0160_08003060`, `mcu_0160_0800a6b8`
- Confidence: high

## tmr_channel_value_set

**Write the compare value of channel 1 to 4 (C1DT..C4DT) selected by channel code**

Matches the Artery SDK tmr_channel_value_set. param_2 selects the data register: 0 = C1DT (offset 0x34), 2 = C2DT (0x38), 4 = C3DT (0x3C), 6 = C4DT (0x40). Complementary codes 1, 3 and 5 are not handled, and any other value does nothing. The value is stored as a plain 32-bit write; on advanced timers the field is 16 bits wide, so only the low 16 bits take effect. Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | channel code: 0 = channel 1, 2 = channel 2, 4 = channel 3, 6 = channel 4 |
| `param_3` | `u32` | compare value |

**Notes:** Callers: mcu_0160_080030f4, mcu_0160_08005f08, mcu_0160_0800a6b8.

- Addresses by version: 12b: 0x0800DA46, 143: 0x0800DCA2, 152: 0x0800DD3A, 0160: 0x0800DE7A
- Called by: `mcu_tmr4_ch4_compare_clear`, `mcu_pwm_trigger_and_clamp_select`, `mcu_0160_0800a6b8`
- Confidence: high

## tmr_output_channel_config

**Configure a TMR output channel (idle states, output mode, polarity, enables) from a 7-byte record**

Matches the Artery SDK tmr_output_channel_config. param_2 is the channel code 0, 2, 4 or 6 for CH1..CH4, and param_3 points to a 7-byte tmr_output_config_type: [0] oc_mode (3 bits, into CM1 or CM2 at bits 6:4 for CH1/CH3 or 14:12 for CH2/CH4), [1] oc_idle_state (CTRL2 bit 8 + code), [2] occ_idle_state (CTRL2 bit 9 + code), [3] oc_polarity (CCTRL bit 2*code+1), [4] occ_polarity (bit 2*code+3), [5] oc_output_state (CxEN, bit 2*code) and [6] occ_output_state (CxCEN, bit 2*code+2). Each of these fields is written, so the output-enable bits are set or cleared from the record. For CH4 the complementary polarity and enable fields land in reserved CCTRL bits 14 and 15. Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | channel code: 0 = CH1, 2 = CH2, 4 = CH3, 6 = CH4 |
| `param_3` | `ptr` | tmr_output_config_type record (7 bytes, layout in description) |

**Notes:** The decompile does not clear the CxC channel-configure bits, which the SDK sets to FALSE. Callers: mcu_0160_08003060, mcu_0160_0800a6b8.

- Addresses by version: 12b: 0x0800DBDE, 143: 0x0800DE3A, 152: 0x0800DED2, 0160: 0x0800E012
- Called by: `mcu_0160_08003060`, `mcu_0160_0800a6b8`
- Confidence: high

## tmr_output_default_para_init

**Zero the seven fields of a tmr_output_config_type (default output channel setup)**

Matches the Artery SDK tmr_output_default_para_init. It clears the 7-byte record at param_1: output mode OFF (0), idle states FALSE, polarities ACTIVE_HIGH (0) and output enables FALSE. The caller fills in the fields it needs and passes the record to tmr_output_channel_config (mcu_0160_0800e012). Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | tmr_output_config_type record to clear (7 bytes) |

**Notes:** Same body as mcu_0160_0800de08 (tmr_brkdt_default_para_init). Callers: mcu_0160_08003060, mcu_0160_0800a6b8.

- Addresses by version: 12b: 0x0800DCCE, 143: 0x0800DF2A, 152: 0x0800DFC2, 0160: 0x0800E102
- Called by: `mcu_0160_08003060`, `mcu_0160_0800a6b8`
- Confidence: high

## tmr_output_enable

**Set or clear the main output enable (BRK.OEN, bit 15) of the TMR**

Matches the Artery SDK tmr_output_enable. Read-modify-write of bit 15 (OEN) of the BRK register (offset 0x44) with param_2 & 1. This is the master output switch; it is separate from the per-channel enables in CCTRL. Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | 1 = enable outputs, 0 = disable |

**Notes:** Only caller: mcu_0160_0800a6b8.

- Addresses by version: 12b: 0x0800DCE0, 143: 0x0800DF3C, 152: 0x0800DFD4, 0160: 0x0800E114
- Called by: `mcu_0160_0800a6b8`
- Confidence: high

## tmr_repetition_counter_set

**Write the 8-bit repetition counter value (RPR, offset 0x30)**

Matches the Artery SDK tmr_repetition_counter_set. Replaces bits 7:0 of RPR (offset 0x30) with param_2 & 0xFF and keeps the upper bits. RPR sets how many counter periods pass between update events. Part of the TMR register-helper group in this packet (mcu_0160_0800dd98 to mcu_0160_0800e22e).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TMR base pointer |
| `param_2` | `u32` | repetition value, 0..255 |

**Notes:** Only caller: mcu_0160_0800a6b8.

- Addresses by version: 12b: 0x0800DCF4, 143: 0x0800DF50, 152: 0x0800DFE8, 0160: 0x0800E128
- Called by: `mcu_0160_0800a6b8`
- Confidence: high
