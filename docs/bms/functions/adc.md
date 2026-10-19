# BMS - `adc` functions

7 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`LL_ADC_DeInit`](#ll_adc_deinit) | 0x08002910 | Stops and disables the ADC if it is running, then resets its registers to reset values |
| [`LL_ADC_Init`](#ll_adc_init) | 0x08002A44 | Writes ADC CFGR1 resolution, alignment and low-power fields and CFGR2 clock mode while ADC is off |
| [`LL_ADC_REG_Init`](#ll_adc_reg_init) | 0x08002A80 | Writes ADC regular-group trigger, continuous, DMA and overrun settings and channel selection while ADC is off |
| [`bms_adc_deinit`](#bms_adc_deinit) | 0x08008A08 | Stop and reset the ADC through LL_ADC_DeInit |
| [`bms_adc_hw_init`](#bms_adc_hw_init) | 0x08008890 | Bring up the ADC: clocks, PA4 analog pin, PCLK/2 clock mode, sampling time and regulator |
| [`bms_adc_read_mv`](#bms_adc_read_mv) | 0x08008A18 | Read one ADC channel selected from the table at 0x20000674 and return the result in millivolts |
| [`bms_ntc_adc_to_celsius`](#bms_ntc_adc_to_celsius) | 0x0800B8C0 | Convert ADC channel 0 reading to degrees C through a 151-entry lookup table |

## LL_ADC_DeInit

**Stops and disables the ADC if it is running, then resets its registers to reset values**

Deinitialises an ADC instance. If ADEN is set it clears CFGR1 EXTSEL and EXTEN, requests a conversion stop (ADSTP) and waits for it to clear, then sets ADDIS and waits for the hardware to clear it; each wait is a bounded countdown (0x8000 iterations) and a timeout returns 1. If ADEN, ADDIS, ADSTART and ADSTP are all clear, it writes the pending ISR flags back to clear them (mask 0x2B9F), waits up to 0x30000 iterations for CCRDY (ISR bit 13) and clears it, then resets IER, CFGR1, CFGR2, SMPR and CHSELR to their reset values (keeping a few bits the code leaves set), writes 0x0FFF0000 to the three analog watchdog thresholds, and clears the low 7 bits of CALFACT. It returns 0 on success and 1 on timeout or if the ADC is still enabled.

| Parameter | Type | Description |
|---|---|---|
| `ADCx` | `ptr` | ADC instance (ADC_TypeDef pointer) |

**Returns** `u32`: ErrorStatus: 0 = SUCCESS, 1 = ERROR (timeout or ADC still enabled)

**Notes:** The name is inferred from the reset-to-default pattern and the ErrorStatus return; the ST HAL does not reset registers in its ADC deinit, so this matches an LL-style deinit. The 'keeps a few bits' masks (0xFFFFD460 for IER and so on) are not decoded individually.

- Addresses by version: 4130: 0x08002910, 4139: 0x08002910, 4148: 0x08002910, 4168: 0x08002910
- Called by: `bms_adc_deinit`
- Confidence: medium

## LL_ADC_Init

**Writes ADC CFGR1 resolution, alignment and low-power fields and CFGR2 clock mode while ADC is off**

Configures an ADC instance from a 4-word init record, but only when CR.ADEN is clear. If the ADC is enabled it returns 1 and changes nothing. Otherwise it sets CFGR2.CKMODE (bits 31:30) from init[0] and rewrites CFGR1 by clearing RES (bits 4:3), ALIGN (bit 5) and WAIT and AUTOFF (bits 14 and 15) and ORing in the pre-encoded values init[1], init[2] and init[3]. It returns 0 on success.

| Parameter | Type | Description |
|---|---|---|
| `ADCx` | `ptr` | ADC instance (ADC_TypeDef pointer) |
| `init` | `ptr` | 4-word init record: clock mode, resolution, data alignment, low-power bits |

**Returns** `u32`: 0 = SUCCESS; 1 = ADC enabled, nothing written

**Notes:** The LL_ADC_Init name matches the CFGR1 clear mask 0xFFFF3FC7 and the enable check. The 4-word layout and the CKMODE field are inferred from the code, so this is not confirmed against the LL header.

- Addresses by version: 4130: 0x08002A44, 4139: 0x08002A44, 4148: 0x08002A44, 4168: 0x08002A44
- Called by: `bms_adc_hw_init`
- Confidence: medium

## LL_ADC_REG_Init

**Writes ADC regular-group trigger, continuous, DMA and overrun settings and channel selection while ADC is off**

Configures the regular conversion group from a 6-word record and only when ADEN is clear (returns 1 and changes nothing otherwise). It clears the trigger-select, discontinuous, continuous, DMA and overrun fields of CFGR1 with mask 0xFFFEC23C and ORs in init[0], init[2], init[3], init[4] and init[5] for those fields. When CHSELRMOD (CFGR1 bit 21) is set, init[1] is ORed into CHSELR as the regular channel selection. If CHSELRMOD is set and init[1] is 0xF0, the discontinuous bit (init[2]) is left out of the write. It returns 0 on success.

| Parameter | Type | Description |
|---|---|---|
| `ADCx` | `ptr` | ADC instance (ADC_TypeDef pointer) |
| `init` | `ptr` | 6-word regular-group record: trigger, channel or length field, discontinuous, continuous, DMA, overrun |

**Returns** `u32`: 0 = SUCCESS; 1 = ADC enabled, nothing written

**Notes:** The field order and the 0xF0 special case come from the code only. The meaning of init[1] is uncertain: it is written to CHSELR when CHSELRMOD is set, which fits a channel mask better than a length.

- Addresses by version: 4130: 0x08002A80, 4139: 0x08002A80, 4148: 0x08002A80, 4168: 0x08002A80
- Called by: `bms_adc_hw_init`
- Confidence: medium

## bms_adc_deinit

**Stop and reset the ADC through LL_ADC_DeInit**

Calls LL_ADC_DeInit (bms_4168_08002910) on the ADC instance, which stops and disables the ADC if it is running and then resets its registers. Its only caller in this packet is bms_4168_080082f0.

- Addresses by version: 4130: 0x080079BC, 4139: 0x08007EBC, 4148: 0x08008708, 4168: 0x08008A08
- Peripheral registers: `ADC.ADC_ISR` (A)
- Called by: `bms_4168_080082f0`
- Calls: `LL_ADC_DeInit`
- Confidence: high

## bms_adc_hw_init

**Bring up the ADC: clocks, PA4 analog pin, PCLK/2 clock mode, sampling time and regulator**

Enables the GPIOA clock (RCC.IOPENR bit 0) and the ADC clock (RCC.APBENR2 bit 20), selects PCLK as the ADC clock source by clearing CCIPR bits 31:30, and configures PA4 as an analog pin with LL_GPIO_Init. LL_ADC_Init is called with the clock-mode argument 0x40000000 (CFGR2 CKMODE 01, PCLK/2), and LL_ADC_REG_Init is called with the regular-group settings and channel bit 0x1000. The routine clears CFGR2 bits 0 and 29, sets sampling time code 5 (39.5 ADC clock cycles) for SMP1 and SMP2 in SMPR, clears interrupt-enable bits 2 and 3, and sets CR.ADVREGEN (bit 28) to power the regulator. A busy-wait sized from the RAM word at 0x200006A4 runs after the regulator is enabled, and ADC_ISR bit 13 is polled with a SysTick-bounded timeout and cleared by writing 0x2000. The ADC is not enabled or calibrated here; bms_4168_08008a18 does that on first use.

**Notes:** Register bit meanings are taken from the ST G0 reference as used in this code, not checked against the SVD. Sampling time code 5 is 39.5 cycles on G0 by the usual table. The busy-wait length meaning is inferred.

- Addresses by version: 4130: 0x08007844, 4139: 0x08007D44, 4148: 0x08008590, 4168: 0x08008890
- Peripheral registers: `TIM2.CR1` (A), `ADC.ADC_ISR` (ARW), `ADC.ADC_IER` (RW), `ADC.ADC_CR` (RW), `ADC.ADC_CFGR1` (RW), `ADC.ADC_CFGR2` (RW), `ADC.ADC_SMPR` (RW), `ADC.CHSELR_1` (RW), `RCC.IOPENR` (RW), `RCC.APBENR2` (RW), `RCC.CCIPR` (RW), `SysTick+0x0` (R)
- Called by: `bms_4168_08008294`, `bms_4168_080082f0`
- Calls: `bms_udiv32`, `LL_ADC_Init`, `LL_ADC_REG_Init`, `LL_GPIO_Init`
- Confidence: medium

## bms_adc_read_mv

**Read one ADC channel selected from the table at 0x20000674 and return the result in millivolts**

channel_index indexes a 32-bit channel descriptor table at 0x20000674. Bits 26 to 29 of the descriptor are written to the low nibble of CHSELR to select the channel, and the descriptor shifted left by 8 clears the matching SMPR sample-time bits. If CR.ADEN is clear, the routine sets ADVREGEN, waits for the regulator using a busy-wait sized from the RAM word at 0x200006A4, runs calibration (CR.ADCAL) with the CFGR1 low bits held clear, then sets ADEN and waits for ADRDY (ISR bit 0). It then sets ADSTART (CR bit 2), waits for EOC (ISR bit 2) with a SysTick timeout, clears EOC by writing 4, and returns (DR & 0xFFFF) * 3300 / 4095 using bms_udiv32, i.e. millivolts for a 12-bit reading against a 3.3 V reference.

| Parameter | Type | Description |
|---|---|---|
| `channel_index` | `s32` | index into the 4-byte channel descriptor table at 0x20000674 |
| `unused_arg2` | `u32` | unused by the body in the decompile |
| `unused_arg3` | `u32` | unused by the body in the decompile |
| `unused_arg4` | `u32` | unused by the body in the decompile |

**Returns** `u16`: conversion result in millivolts, about 0 to 3300

**Notes:** The 3.3 V reference is inferred from the 3300 multiplier; the 4095 divisor is 12-bit full scale.

- Addresses by version: 4130: 0x080079CC, 4139: 0x08007ECC, 4148: 0x08008718, 4168: 0x08008A18
- Peripheral registers: `ADC.ADC_ISR` (RW), `ADC.ADC_CR` (RW), `ADC.ADC_CFGR1` (RW), `ADC.ADC_SMPR` (RW), `ADC.CHSELR_1` (RW), `ADC.ADC_DR` (R), `SysTick+0x0` (R)
- Called by: `bms_ntc_adc_to_celsius`
- Calls: `bms_udiv32`
- Confidence: medium

## bms_ntc_adc_to_celsius

**Convert ADC channel 0 reading to degrees C through a 151-entry lookup table**

Takes a sample from the helper at 0x08008A18 with argument 0 and returns -30 when the sample is above 3299. Otherwise it forms the ratio (sample * 1000) / (3300 - sample) with the helper at 0x0800113C, which is a divide-with-remainder routine. It then searches the u16 table at flash 0x080108C4 linearly, from entry 1 upward, for the first entry not greater than the ratio. The result is the index minus 30, which covers roughly -30 to +120 C in 1 degree steps. The -30 return for an out-of-range sample is indistinguishable from a real -30 C reading.

**Returns** `s8`: temperature in degrees C, about -30 to +120; -30 also marks an out-of-range sample

**Notes:** The divider and NTC interpretation is inferred from the 3300 constant and the table. The helpers at 0x08008A18 and 0x0800113C are not described in this packet.

- Addresses by version: 4130: 0x0800A958, 4139: 0x0800AE90, 4148: 0x0800B5AC, 4168: 0x0800B8C0
- Called by: `bms_4168_0800c6dc`
- Calls: `bms_4168_0800113c`, `bms_adc_read_mv`
- Confidence: medium
