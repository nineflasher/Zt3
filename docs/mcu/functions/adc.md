# MCU - `adc` functions

17 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`adc_flag_get`](#adc_flag_get) | 0x0800B72A | Test ADC status flags: true when any masked bit of ADC.STS is set |
| [`adc_interrupt_enable`](#adc_interrupt_enable) | 0x0800B738 | Enable or disable ADC interrupt sources in ADC.CTRL1 |
| [`adc_ordinary_channel_set`](#adc_ordinary_channel_set) | 0x0800B752 | Assign a regular ADC channel to a sequence rank and set its sample time |
| [`adc_ordinary_conversion_trigger_set`](#adc_ordinary_conversion_trigger_set) | 0x0800B920 | Select the external trigger for regular conversions and enable it |
| [`adc_ordinary_software_trigger_enable`](#adc_ordinary_software_trigger_enable) | 0x0800B954 | Set or clear the regular-group software start bit (CTRL2.OCSWTRG) |
| [`adc_preempt_channel_length_set`](#adc_preempt_channel_length_set) | 0x0800B95E | Set the injected (preempt) sequence length to 1..4 conversions |
| [`adc_preempt_channel_set`](#adc_preempt_channel_set) | 0x0800B96A | Place a channel in the injected (preempt) sequence and set its sample time |
| [`adc_preempt_conversion_data_get`](#adc_preempt_conversion_data_get) | 0x0800BAC2 | Read the 16-bit injected conversion result (JDT1..JDT4) by index |
| [`adc_preempt_conversion_trigger_set`](#adc_preempt_conversion_trigger_set) | 0x0800BAEE | Select the external trigger for the injected group and enable it |
| [`mcu_adc_apply_scan_cont_config`](#mcu_adc_apply_scan_cont_config) | 0x0800B6A2 | Write scan mode, continuous mode, alignment and sequence length from a 4-byte record into the ADC registers |
| [`mcu_adc_calib_init_busy`](#mcu_adc_calib_init_busy) | 0x0800B6E6 | Return 1 while ADCALINIT (CTRL2 bit 3) is set |
| [`mcu_adc_calibration_busy`](#mcu_adc_calibration_busy) | 0x0800B700 | Return 1 while ADCAL (CTRL2 bit 2) is set |
| [`mcu_adc_config_set_default`](#mcu_adc_config_set_default) | 0x0800B6CE | Fill a 4-byte ADC config record with defaults: no scan, no repeat, right aligned, one conversion |
| [`mcu_adc_set_enable`](#mcu_adc_set_enable) | 0x0800B71A | Set or clear the ADC enable bit ADCEN (CTRL2 bit 0) from bit 0 of the argument |
| [`mcu_adc_set_ordinary_dma`](#mcu_adc_set_ordinary_dma) | 0x0800B710 | Set or clear the ordinary-channel DMA enable (CTRL2 bit 8, OCDMAEN) from bit 0 of the argument |
| [`mcu_adc_start_calibration`](#mcu_adc_start_calibration) | 0x0800B6F6 | Set ADCAL (CTRL2 bit 2) to start A/D calibration |
| [`mcu_adc_start_init_calibration`](#mcu_adc_start_init_calibration) | 0x0800B6DC | Set ADCALINIT (CTRL2 bit 3) to start ADC calibration initialisation |

## adc_flag_get

**Test ADC status flags: true when any masked bit of ADC.STS is set**

Returns true when (STS & flag) is non-zero, where STS is the first word of the ADC register block (offset 0x00). This is the SDK adc_flag_get routine compiled as a bare bit test. The call sites seen in other MCU packets all pass &ADC1 with mask 4, which is STS bit 2 (PCCE, the preempt/injected conversion-end flag). ADC group: see mcu_0160_0800b738 and mcu_0160_0800bac2.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base (ADC1 = 0x40012400) |
| `param_2` | `u32` | flag mask, bit position in ADC.STS (4 = PCCE) |

**Returns** `bool`: true if any masked flag bit is set

**Notes:** Identity from the SDK code shape and the &ADC1,4 call sites; the caller functions themselves were not read.

- Addresses by version: 12b: 0x0800B416, 143: 0x0800B6C6, 152: 0x0800B6CA, 0160: 0x0800B72A
- Called by: `mcu_0160_08001ee4`, `mcu_0160_0800226c`
- Confidence: high

## adc_interrupt_enable

**Enable or disable ADC interrupt sources in ADC.CTRL1**

Read-modify-write of ADC.CTRL1 (offset 0x04): the bits in the mask are set when param_3 == 1 and cleared for any other value. The call site seen is adc_interrupt_enable(&ADC1, 0x80, 1). 0x80 is CTRL1 bit 7 (PCCEIEN), which enables the preempt (injected) conversion-end interrupt. Matches the SDK adc_interrupt_enable. ADC group: see mcu_0160_0800b72a.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |
| `param_2` | `u32` | interrupt enable mask (ADC_xxx_INT bit) |
| `param_3` | `s32` | 1 = enable, any other value = disable |

- Addresses by version: 12b: 0x0800B424, 143: 0x0800B6D4, 152: 0x0800B6D8, 0160: 0x0800B738
- Called by: `mcu_0160_08001fb0`
- Confidence: high

## adc_ordinary_channel_set

**Assign a regular ADC channel to a sequence rank and set its sample time**

Writes the 3-bit sample-time code for the channel into SPT2 (offset 0x10, channels 0..9) or SPT1 (offset 0x0C, channels 10..17). It then writes the 5-bit channel number into the regular sequence register that holds the rank: OSQ3 (0x34) for ranks 1..6, OSQ2 (0x30) for ranks 7..12, OSQ1 (0x2C) for ranks 13..16. Other fields in those registers are kept. Channel or rank values outside those ranges are ignored. The decompiler shows this as two switch statements. Matches the SDK adc_ordinary_channel_set. ADC group: see mcu_0160_0800b72a.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |
| `param_2` | `u32` | channel number 0..17 (ADC_CHANNEL_n) |
| `param_3` | `u32` | regular sequence rank 1..16 |
| `param_4` | `u32` | sample-time code 0..7 (3 bits, ADC_SAMPLETIME_*) |

- Addresses by version: 12b: 0x0800B43E, 143: 0x0800B6EE, 152: 0x0800B6F2, 0160: 0x0800B752
- Called by: `mcu_0160_08002068`
- Confidence: high

## adc_ordinary_conversion_trigger_set

**Select the external trigger for regular conversions and enable it**

Writes ADC.CTRL2 (offset 0x08). The low three bits of the trigger code go to OCTESEL_L (bits 19:17), the high bit (code >= 8) goes to OCTESEL_H (bit 25), and bit 0 of the enable argument goes to OCTEN (bit 20). The other CTRL2 bits are unchanged. Matches the SDK adc_ordinary_conversion_trigger_set. ADC group: see mcu_0160_0800b72a.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |
| `param_2` | `u32` | external trigger code (ADC12_ORDINARY_TRIG_*, 0..15) |
| `param_3` | `u32` | enable: bit 0 = 1 enables the regular-group trigger |

- Addresses by version: 12b: 0x0800B60C, 143: 0x0800B8BC, 152: 0x0800B8C0, 0160: 0x0800B920
- Called by: `mcu_0160_08002068`
- Confidence: high

## adc_ordinary_software_trigger_enable

**Set or clear the regular-group software start bit (CTRL2.OCSWTRG)**

Writes bit 22 (OCSWTRG) of ADC.CTRL2 from bit 0 of the argument. Setting it to 1 starts a regular conversion sequence in software. The routine has no other side effects. Matches the SDK adc_ordinary_software_trigger_enable. Caller: mcu_0160_0800d548. ADC group: see mcu_0160_0800b72a.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |
| `param_2` | `u32` | bit 0 = 1 starts a regular conversion, 0 clears the bit |

- Addresses by version: 12b: 0x0800B640, 143: 0x0800B8F0, 152: 0x0800B8F4, 0160: 0x0800B954
- Called by: `mcu_0160_0800d548`
- Confidence: high

## adc_preempt_channel_length_set

**Set the injected (preempt) sequence length to 1..4 conversions**

Writes ADC.PSQ (offset 0x38) bits 21:20 (PCLEN) with (length - 1) & 3, leaving the other PSQ bits alone. The field stores the length minus one, as in the SDK adc_preempt_channel_length_set. The sequence slots themselves are set by mcu_0160_0800b96a. ADC group: see mcu_0160_0800b72a.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |
| `param_2` | `s32` | injected sequence length 1..4 |

- Addresses by version: 12b: 0x0800B64A, 143: 0x0800B8FA, 152: 0x0800B8FE, 0160: 0x0800B95E
- Called by: `mcu_0160_08001fb0`
- Confidence: high

## adc_preempt_channel_set

**Place a channel in the injected (preempt) sequence and set its sample time**

Sets the sample-time code for the channel in SPT2/SPT1 the same way adc_ordinary_channel_set does. It then computes the injected slot index as rank - PCLEN + 3 (PCLEN is the raw 2-bit field in PSQ bits 21:20). The injected sequence is right-aligned, so the last rank always lands in slot 4. The 5-bit channel number goes into PSQ bits 4:0 (slot 1), 9:5 (slot 2), 14:10 (slot 3) or 19:15 (slot 4). Other index values do nothing. Matches the SDK adc_preempt_channel_set. Callers: mcu_0160_08001fb0, mcu_0160_0800226c, mcu_0160_08002548. ADC group: see mcu_0160_0800b72a.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |
| `param_2` | `u32` | channel number 0..17 |
| `param_3` | `s32` | rank within the injected sequence (1..length) |
| `param_4` | `u32` | sample-time code 0..7 |

- Addresses by version: 12b: 0x0800B656, 143: 0x0800B906, 152: 0x0800B90A, 0160: 0x0800B96A
- Called by: `mcu_0160_08001fb0`, `mcu_0160_0800226c`, `mcu_0160_08002548`
- Confidence: high

## adc_preempt_conversion_data_get

**Read the 16-bit injected conversion result (JDT1..JDT4) by index**

Returns the low 16 bits of the injected data register selected by the index: 0 reads offset 0x3C (PDT1), 1 reads 0x40 (PDT2), 2 reads 0x44 (PDT3), 3 reads 0x48 (PDT4). Any other index returns 0. Matches the SDK adc_preempt_conversion_data_get. Callers: mcu_0160_0800226c, mcu_0160_080025d8. ADC group: see mcu_0160_0800b72a.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |
| `param_2` | `s32` | injected channel index 0..3 |

**Returns** `u16`: injected conversion result, 0..4095 (0 for an invalid index)

- Addresses by version: 12b: 0x0800B7AE, 143: 0x0800BA5E, 152: 0x0800BA62, 0160: 0x0800BAC2
- Called by: `mcu_0160_0800226c`, `mcu_0160_080025d8`
- Confidence: high

## adc_preempt_conversion_trigger_set

**Select the external trigger for the injected group and enable it**

Writes ADC.CTRL2 (offset 0x08). The low three bits of the trigger code go to PCTESEL_L (bits 14:12), the high bit (code >= 8) goes to PCTESEL_H (bit 24), and bit 0 of the enable argument goes to PCTEN (bit 15). Other CTRL2 bits are unchanged. Counterpart of adc_ordinary_conversion_trigger_set for the injected group. Matches the SDK adc_preempt_conversion_trigger_set. Caller: mcu_0160_08001fb0. ADC group: see mcu_0160_0800b72a.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |
| `param_2` | `u32` | external trigger code (0..15) |
| `param_3` | `u32` | enable: bit 0 = 1 enables the injected-group trigger |

- Addresses by version: 12b: 0x0800B7DA, 143: 0x0800BA8A, 152: 0x0800BA8E, 0160: 0x0800BAEE
- Called by: `mcu_0160_08001fb0`
- Confidence: high

## mcu_adc_apply_scan_cont_config

**Write scan mode, continuous mode, alignment and sequence length from a 4-byte record into the ADC registers**

Copies a 4-byte configuration record into an ADC register block whose offsets match ADC1 at 0x40012400. Byte 0 goes to CTRL1 bit 8 (SQEN, sequence/scan mode). Byte 1 goes to CTRL2 bit 1 (RPEN, repeat/continuous). Byte 2 goes to CTRL2 bit 11 (DTALIGN, data alignment). Byte 3 goes to OSQ1 bits 20 to 23 (OCLEN = (byte 3 - 1) & 0xF, the number of ordinary conversions minus one). Each field is written by read-modify-write, leaving other bits unchanged. Called from mcu_0160_08002068.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC register block (layout of ADC1: CTRL1 at +0x04, CTRL2 at +0x08, OSQ1 at +0x2c) |
| `param_2` | `ptr` | 4-byte configuration record: scan, repeat, alignment, conversion count |

**Notes:** Peripheral base is assumed from the register offsets. The bit names come from the ADC1 table in src/zt3re/data/hw/at32f415_registers.json.

- Addresses by version: 12b: 0x0800B38E, 143: 0x0800B63E, 152: 0x0800B642, 0160: 0x0800B6A2
- Called by: `mcu_0160_08002068`
- Confidence: high

## mcu_adc_calib_init_busy

**Return 1 while ADCALINIT (CTRL2 bit 3) is set**

Returns CTRL2 bit 3 (ADCALINIT). The hardware normally clears this bit when calibration initialisation completes, so a 1 means it is still running. Called from mcu_0160_08001fb0, likely to poll for completion (inferred).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC register block (CTRL2 at +0x08) |

**Returns** `bool`: true while ADCALINIT is set

**Notes:** The hardware clear-on-completion behaviour is from the vendor reference, not verified here.

- Addresses by version: 12b: 0x0800B3D2, 143: 0x0800B682, 152: 0x0800B686, 0160: 0x0800B6E6
- Called by: `mcu_0160_08001fb0`
- Confidence: medium

## mcu_adc_calibration_busy

**Return 1 while ADCAL (CTRL2 bit 2) is set**

Returns CTRL2 bit 2 (ADCAL). It should read 1 while calibration runs and 0 once it is done, because the hardware clears the bit. Called from mcu_0160_08001fb0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC register block (CTRL2 at +0x08) |

**Returns** `bool`: true while ADCAL is set

**Notes:** The clear-on-completion behaviour is from the vendor reference, not verified here.

- Addresses by version: 12b: 0x0800B3EC, 143: 0x0800B69C, 152: 0x0800B6A0, 0160: 0x0800B700
- Called by: `mcu_0160_08001fb0`
- Confidence: medium

## mcu_adc_config_set_default

**Fill a 4-byte ADC config record with defaults: no scan, no repeat, right aligned, one conversion**

Writes 0, 0, 0 and 1 into the record: scan off, repeat off, right alignment, and a conversion count of 1. Byte 3 holds the count, and mcu_adc_apply_scan_cont_config stores it minus one in OCLEN. Called from mcu_0160_08002068.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 4-byte configuration record to fill |

- Addresses by version: 12b: 0x0800B3BA, 143: 0x0800B66A, 152: 0x0800B66E, 0160: 0x0800B6CE
- Called by: `mcu_0160_08002068`
- Confidence: high

## mcu_adc_set_enable

**Set or clear the ADC enable bit ADCEN (CTRL2 bit 0) from bit 0 of the argument**

Replaces CTRL2 bit 0 (ADCEN) with bit 0 of the argument, by read-modify-write. It does not wait for the ADC stabilisation time after enabling; any such wait is the caller's job. Called from mcu_0160_08001fb0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC register block (CTRL2 at +0x08) |
| `param_2` | `u32` | enable flag (bit 0 used) |

- Addresses by version: 12b: 0x0800B406, 143: 0x0800B6B6, 152: 0x0800B6BA, 0160: 0x0800B71A
- Called by: `mcu_0160_08001fb0`
- Confidence: high

## mcu_adc_set_ordinary_dma

**Set or clear the ordinary-channel DMA enable (CTRL2 bit 8, OCDMAEN) from bit 0 of the argument**

Replaces CTRL2 bit 8 (OCDMAEN, DMA transfer enable for ordinary channels) with bit 0 of the argument, by read-modify-write. Called from mcu_0160_0800d548, the application main entry, so DMA for ADC conversions is presumably switched on at start-up.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC register block (CTRL2 at +0x08) |
| `param_2` | `u8` | enable flag (bit 0 used) |

- Addresses by version: 12b: 0x0800B3FC, 143: 0x0800B6AC, 152: 0x0800B6B0, 0160: 0x0800B710
- Called by: `mcu_0160_0800d548`
- Confidence: high

## mcu_adc_start_calibration

**Set ADCAL (CTRL2 bit 2) to start A/D calibration**

Sets CTRL2 bit 2 (ADCAL) by OR, which starts the ADC calibration. Completion is checked with mcu_adc_calibration_busy. Called from mcu_0160_08001fb0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC register block (CTRL2 at +0x08) |

- Addresses by version: 12b: 0x0800B3E2, 143: 0x0800B692, 152: 0x0800B696, 0160: 0x0800B6F6
- Called by: `mcu_0160_08001fb0`
- Confidence: high

## mcu_adc_start_init_calibration

**Set ADCALINIT (CTRL2 bit 3) to start ADC calibration initialisation**

Sets bit 3 of the ADC CTRL2 register (ADCALINIT, initialise A/D calibration) at struct+0x08 with a read-modify-write OR, leaving other bits alone. Called from mcu_0160_08001fb0 together with the other mcu_adc_* helpers, so that function is probably the ADC bring-up sequence (inferred).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC register block (CTRL2 at +0x08) |

- Addresses by version: 12b: 0x0800B3C8, 143: 0x0800B678, 152: 0x0800B67C, 0160: 0x0800B6DC
- Called by: `mcu_0160_08001fb0`
- Confidence: high
