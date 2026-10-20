# VCU - `adc` functions

14 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`adc_base_config`](#adc_base_config) | 0x0800A96C | Configure ADC scan mode, continuous mode, data alignment and ordinary sequence length |
| [`adc_base_default_para_init`](#adc_base_default_para_init) | 0x0800A998 | Fill adc_base_config_type with defaults (no scan, no repeat, right-aligned, length 1) |
| [`adc_calibration_init`](#adc_calibration_init) | 0x0800A9A6 | Start ADC calibration-register reset (CTRL2.ADCALINIT = 1) |
| [`adc_calibration_init_status_get`](#adc_calibration_init_status_get) | 0x0800A9B0 | Return CTRL2.ADCALINIT (1 while calibration reset is running) |
| [`adc_calibration_start`](#adc_calibration_start) | 0x0800A9BE | Start ADC calibration (CTRL2.ADCAL = 1) |
| [`adc_calibration_status_get`](#adc_calibration_status_get) | 0x0800A9C8 | Return CTRL2.ADCAL (1 while calibration is running) |
| [`adc_dma_mode_enable`](#adc_dma_mode_enable) | 0x0800A9D6 | Enable/disable ADC DMA requests (CTRL2.OCDMAEN) |
| [`adc_enable`](#adc_enable) | 0x0800A9E0 | Enable/disable the ADC (CTRL2.ADCEN) |
| [`adc_ordinary_channel_set`](#adc_ordinary_channel_set) | 0x0800A9EA | Assign a channel to a rank in the ordinary sequence and set its sample time |
| [`adc_ordinary_conversion_trigger_set`](#adc_ordinary_conversion_trigger_set) | 0x0800AA5E | Select the ordinary-channel external trigger and enable/disable it |
| [`adc_ordinary_software_trigger_enable`](#adc_ordinary_software_trigger_enable) | 0x0800AA92 | Start/stop an ordinary conversion by software (CTRL2.OCSWTRG) |
| [`vcu_adc1_scan_init`](#vcu_adc1_scan_init) | 0x08001D5C | Initialise ADC1 for a 5-channel DMA scan, calibrate it, then start conversion |
| [`vcu_adc_analog_pins_init`](#vcu_adc_analog_pins_init) | 0x08001CA8 | Set PA4, PA5, PA7, PB0 and PB1 as analog inputs for ADC1 channels 4, 5, 7, 8 and 9 |
| [`vcu_adc_average_16_scans`](#vcu_adc_average_16_scans) | 0x08001768 | Average 16 ADC scans of 5 channels from the DMA buffer into five 16-bit results |

## adc_base_config

**Configure ADC scan mode, continuous mode, data alignment and ordinary sequence length**

Artery SDK adc_base_config. From a 4-byte adc_base_config_type {sequence_mode, repeat_mode, data_align, ordinary_channel_length}: CTRL1.SQEN (bit 8) <- byte0, CTRL2.RPEN (bit 1) <- byte1, CTRL2.DTALIGN (bit 11) <- byte2, OSQ1.OCLEN (bits 23:20) <- byte3 - 1. Called from the ADC init routine 0x08001d5c. Group of ADC driver calls: adc_base_default_para_init, adc_calibration_*, adc_dma_mode_enable, adc_enable, adc_ordinary_channel_set, adc_ordinary_conversion_trigger_set, adc_ordinary_software_trigger_enable.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base (ADC1) |
| `param_2` | `ptr` | adc_base_config_type |

- Addresses by version: 148: 0x080099E4, 14a: 0x08009EC0, 14b: 0x0800A348, 14e: 0x0800A3DC, 14f: 0x0800A518, 152: 0x0800A798, 153: 0x0800A88C, 0159: 0x0800A96C
- Called by: `vcu_adc1_scan_init`
- Confidence: high

## adc_base_default_para_init

**Fill adc_base_config_type with defaults (no scan, no repeat, right-aligned, length 1)**

Artery SDK adc_base_default_para_init: writes bytes {0,0,0,1} to the config struct (sequence_mode=FALSE, repeat_mode=FALSE, data_align=right, ordinary_channel_length=1). Called from 0x08001d5c before adc_base_config.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | adc_base_config_type to initialise |

- Addresses by version: 148: 0x08009A10, 14a: 0x08009EEC, 14b: 0x0800A374, 14e: 0x0800A408, 14f: 0x0800A544, 152: 0x0800A7C4, 153: 0x0800A8B8, 0159: 0x0800A998
- Called by: `vcu_adc1_scan_init`
- Confidence: high

## adc_calibration_init

**Start ADC calibration-register reset (CTRL2.ADCALINIT = 1)**

Artery SDK adc_calibration_init: sets bit 3 (ADCALINIT) in ADC CTRL2 (offset 0x08). Hardware clears it when the calibration registers are initialised; poll with adc_calibration_init_status_get. Called from 0x08001d5c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |

- Addresses by version: 148: 0x08009A1E, 14a: 0x08009EFA, 14b: 0x0800A382, 14e: 0x0800A416, 14f: 0x0800A552, 152: 0x0800A7D2, 153: 0x0800A8C6, 0159: 0x0800A9A6
- Called by: `vcu_adc1_scan_init`
- Confidence: high

## adc_calibration_init_status_get

**Return CTRL2.ADCALINIT (1 while calibration reset is running)**

Artery SDK adc_calibration_init_status_get: returns 1 if bit 3 of ADC CTRL2 is set, else 0. Polled from 0x08001d5c after adc_calibration_init.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |

**Returns** `u32`: SET(1) / RESET(0)

- Addresses by version: 148: 0x08009A28, 14a: 0x08009F04, 14b: 0x0800A38C, 14e: 0x0800A420, 14f: 0x0800A55C, 152: 0x0800A7DC, 153: 0x0800A8D0, 0159: 0x0800A9B0
- Called by: `vcu_adc1_scan_init`
- Confidence: high

## adc_calibration_start

**Start ADC calibration (CTRL2.ADCAL = 1)**

Artery SDK adc_calibration_start: sets bit 2 (ADCAL) in ADC CTRL2; hardware clears it when calibration completes. Called from 0x08001d5c after the init reset finished.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |

- Addresses by version: 148: 0x08009A36, 14a: 0x08009F12, 14b: 0x0800A39A, 14e: 0x0800A42E, 14f: 0x0800A56A, 152: 0x0800A7EA, 153: 0x0800A8DE, 0159: 0x0800A9BE
- Called by: `vcu_adc1_scan_init`
- Confidence: high

## adc_calibration_status_get

**Return CTRL2.ADCAL (1 while calibration is running)**

Artery SDK adc_calibration_status_get: returns 1 if bit 2 of ADC CTRL2 is set else 0. Polled from 0x08001d5c to wait for calibration to end.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |

**Returns** `u32`: SET(1) / RESET(0)

- Addresses by version: 148: 0x08009A40, 14a: 0x08009F1C, 14b: 0x0800A3A4, 14e: 0x0800A438, 14f: 0x0800A574, 152: 0x0800A7F4, 153: 0x0800A8E8, 0159: 0x0800A9C8
- Called by: `vcu_adc1_scan_init`
- Confidence: high

## adc_dma_mode_enable

**Enable/disable ADC DMA requests (CTRL2.OCDMAEN)**

Artery SDK adc_dma_mode_enable: writes bit 0 of param_2 into bit 8 (OCDMAEN) of ADC CTRL2. Called from 0x08001d5c so the ordinary-channel results are moved by DMA.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |
| `param_2` | `u32` | TRUE/FALSE |

- Addresses by version: 148: 0x08009A4E, 14a: 0x08009F2A, 14b: 0x0800A3B2, 14e: 0x0800A446, 14f: 0x0800A582, 152: 0x0800A802, 153: 0x0800A8F6, 0159: 0x0800A9D6
- Called by: `vcu_adc1_scan_init`
- Confidence: high

## adc_enable

**Enable/disable the ADC (CTRL2.ADCEN)**

Artery SDK adc_enable: writes bit 0 of param_2 into bit 0 (ADCEN) of ADC CTRL2. When already enabled a further set starts an ordinary conversion per the SDK note. Called from 0x08001d5c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |
| `param_2` | `u32` | TRUE/FALSE |

- Addresses by version: 148: 0x08009A58, 14a: 0x08009F34, 14b: 0x0800A3BC, 14e: 0x0800A450, 14f: 0x0800A58C, 152: 0x0800A80C, 153: 0x0800A900, 0159: 0x0800A9E0
- Called by: `vcu_adc1_scan_init`
- Confidence: high

## adc_ordinary_channel_set

**Assign a channel to a rank in the ordinary sequence and set its sample time**

Artery SDK adc_ordinary_channel_set. param_2 is the channel; its 3-bit sample time param_4 goes into SPT2 (offset 0x10, channels 0..9) or SPT1 (offset 0x0C, channel-10..). The 5-bit channel number is written at rank param_3 into OSQ3 (0x34, ranks 1..6), OSQ2 (0x30, ranks 7..12) or OSQ1 (0x2C, ranks 13..16). Called from 0x08001d5c once per scanned channel.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |
| `param_2` | `u32` | channel number 0..15 |
| `param_3` | `u32` | sequence rank 1..16 |
| `param_4` | `s32` | sample-time code 0..7 (1.5..239.5 cycles) |

- Addresses by version: 148: 0x08009A62, 14a: 0x08009F3E, 14b: 0x0800A3C6, 14e: 0x0800A45A, 14f: 0x0800A596, 152: 0x0800A816, 153: 0x0800A90A, 0159: 0x0800A9EA
- Called by: `vcu_adc1_scan_init`
- Confidence: high

## adc_ordinary_conversion_trigger_set

**Select the ordinary-channel external trigger and enable/disable it**

Artery SDK adc_ordinary_conversion_trigger_set. Trigger codes 0..7 clear CTRL2 bit 25 (OCTESEL_H), codes >= 8 set it; the low three bits go to CTRL2 bits 19:17 (OCTESEL_L); param_3 bit 0 goes to CTRL2.OCTEN (bit 20). Called from 0x08001d5c; code 7 (software) enables software-triggered conversions.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |
| `param_2` | `u32` | trigger select (adc_ordinary_trig_select_type), 0..8 |
| `param_3` | `u32` | TRUE/FALSE trigger enable |

- Addresses by version: 148: 0x08009AD6, 14a: 0x08009FB2, 14b: 0x0800A43A, 14e: 0x0800A4CE, 14f: 0x0800A60A, 152: 0x0800A88A, 153: 0x0800A97E, 0159: 0x0800AA5E
- Called by: `vcu_adc1_scan_init`
- Confidence: high

## adc_ordinary_software_trigger_enable

**Start/stop an ordinary conversion by software (CTRL2.OCSWTRG)**

Artery SDK adc_ordinary_software_trigger_enable: writes bit 0 of param_2 into bit 22 (OCSWTRG) of ADC CTRL2. Called from 0x08001d5c to kick off the first (continuous/DMA) conversion.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ADC peripheral base |
| `param_2` | `u32` | TRUE/FALSE |

- Addresses by version: 148: 0x08009B0A, 14a: 0x08009FE6, 14b: 0x0800A46E, 14e: 0x0800A502, 14f: 0x0800A63E, 152: 0x0800A8BE, 153: 0x0800A9B2, 0159: 0x0800AA92
- Called by: `vcu_adc1_scan_init`
- Confidence: high

## vcu_adc1_scan_init

**Initialise ADC1 for a 5-channel DMA scan, calibrate it, then start conversion**

Brings up ADC1 as the 5-channel scan source for the averaging code. It calls vcu_adc_analog_pins_init and vcu_adc_dma_ring_init, enables the ADC1 clock (APB2 bit 9), and sets the ADC clock divider code 2 with crm_adc_clock_div_set. It writes the base configuration 0x05000101 via adc_base_config (scan on, continuous on, right aligned, ordinary length 5), then sets ordinary ranks 1 to 5 to channels 7, 9, 8, 4 and 5. It selects trigger source 7 (adc_ordinary_conversion_trigger_set), enables DMA requests and the ADC, runs calibration reset and calibration while polling both status flags, and starts the first ordinary conversion by software.

**Notes:** Two of the adc_ordinary_channel_set calls show only three arguments in the decompile, so their sample-time argument is not visible here. Trigger source 7 is taken to be the software-start selection.

- Addresses by version: 148: 0x08001978, 14a: 0x080019E0, 14b: 0x08001C94, 14e: 0x08001C94, 14f: 0x08001CF0, 152: 0x08001D2C, 153: 0x08001D48, 0159: 0x08001D5C
- Peripheral registers: `ADC1.STS` (A)
- Called by: `vcu_peripheral_init_sequence`
- Calls: `vcu_adc_dma_ring_init`, `vcu_adc_analog_pins_init`, `adc_base_config`, `adc_base_default_para_init`, `adc_calibration_init`, `adc_calibration_init_status_get`, `adc_calibration_start`, `adc_calibration_status_get`, `adc_dma_mode_enable`, `adc_enable`, `adc_ordinary_channel_set`, `adc_ordinary_conversion_trigger_set`, `adc_ordinary_software_trigger_enable`, `crm_adc_clock_div_set`, `crm_periph_clock_enable`
- Confidence: high

## vcu_adc_analog_pins_init

**Set PA4, PA5, PA7, PB0 and PB1 as analog inputs for ADC1 channels 4, 5, 7, 8 and 9**

Configures the five ADC inputs, PA4 (ADC1 IN4), PA5 (IN5), PA7 (IN7), PB0 (IN8) and PB1 (IN9), which are the channels used by the ADC1 scan in vcu_0159_08001d5c. It enables the IOMUX, GPIOA and GPIOB clocks, then calls gpio_default_para_init and gpio_init for each port. The packed configuration word is built from the register arguments param_3 and param_4, which the caller does not set, so the exact mode is inferred from the channel mapping as analog.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | not used by the routine |
| `param_2` | `u32` | not used by the routine |
| `param_3` | `u32` | packed config word low (register leftover) |
| `param_4` | `u32` | packed config word high (register leftover) |

**Notes:** The mode is inferred, not decoded: the caller passes no arguments, so the config word is whatever the registers hold on entry.

- Addresses by version: 148: 0x080018C4, 14a: 0x0800192C, 14b: 0x08001BE0, 14e: 0x08001BE0, 14f: 0x08001C3C, 152: 0x08001C78, 153: 0x08001C94, 0159: 0x08001CA8
- Peripheral registers: `GPIOA.CFGLR` (A), `GPIOB.CFGLR` (A)
- Called by: `vcu_adc1_scan_init`
- Calls: `crm_periph_clock_enable`, `gpio_default_para_init`, `gpio_init`
- Confidence: medium

## vcu_adc_average_16_scans

**Average 16 ADC scans of 5 channels from the DMA buffer into five 16-bit results**

Averages the ADC1 DMA ring buffer at 0x200032A6 into five 16-bit results at 0x2000329C to 0x200032A4. The buffer holds 16 scans of 5 halfword channels (80 halfwords, filled by the circular DMA set up in vcu_0159_08001c3c). It zeroes five 32-bit stack accumulators, adds every halfword of each channel across all 16 scans (step 5), then stores (sum >> 4), which is the truncated mean, into each result and clears the accumulator. The result index follows the rank order from vcu_0159_08001d5c: channels 7, 9, 8, 4 and 5. It has no direct callers in the harness list, so it runs via a pointer or the main loop.

- Addresses by version: 14f: 0x08001704, 152: 0x0800174C, 153: 0x0800174C, 0159: 0x08001768
- Calls: `vcu_buf_zero`
- Confidence: high
