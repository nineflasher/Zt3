# VCU - `exint` functions

8 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`exint_default_para_init`](#exint_default_para_init) | 0x0800CD54 | Set an exint_init_type to the SDK defaults |
| [`exint_flag_clear`](#exint_flag_clear) | 0x0800CD64 | Clear external-interrupt pending flags (EXINT.INTSTS) |
| [`exint_flag_get`](#exint_flag_get) | 0x0800CD70 | Test external-interrupt pending flag(s) |
| [`exint_init`](#exint_init) | 0x0800CD88 | Configure an external-interrupt/event line |
| [`exint_interrupt_enable`](#exint_interrupt_enable) | 0x0800CDF0 | Enable or disable the interrupt for EXINT lines |
| [`vcu_exint14_pb14_init`](#vcu_exint14_pb14_init) | 0x080020A4 | Route PB14 to EXINT line 14 as a falling-edge interrupt on EXINT15_10, store a probe result |
| [`vcu_exint3_pa3_init`](#vcu_exint3_pa3_init) | 0x080026F0 | Route PA3 to EXINT line 3 as a falling-edge interrupt on EXINT3 (IRQ 9) |
| [`vcu_exint_pb12_pb14_init`](#vcu_exint_pb12_pb14_init) | 0x080021C4 | Route PB12 and PB14 to EXINT lines 12 and 14 as falling-edge interrupts on EXINT15_10 |

## exint_default_para_init

**Set an exint_init_type to the SDK defaults**

AT32 SDK exint_default_para_init(): writes line_mode (+0) = 1 (EXINT_LINE_EVENT), line_select (+4) = 0 (none), line_polarity (+8) = 1 (falling edge) and line_enable (+9) = FALSE. Called before exint_init by vcu_0159_080020a4, 080021c4, 080024ec and 080026f0 (the external-interrupt line setup routines).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | exint_init_type* to initialise |

- Addresses by version: 148: 0x0800BEC8, 14a: 0x0800C30C, 14b: 0x0800C798, 14e: 0x0800C82C, 14f: 0x0800C968, 152: 0x0800CBF4, 153: 0x0800CCE8, 0159: 0x0800CD54
- Called by: `vcu_exint14_pb14_init`, `vcu_exint_pb12_pb14_init`, `vcu_0159_080024ec`, `vcu_exint3_pa3_init`
- Confidence: high

## exint_flag_clear

**Clear external-interrupt pending flags (EXINT.INTSTS)**

AT32 SDK exint_flag_clear(): writes param_1 to EXINT.INTSTS (0x40010414); writing a 1 clears the pending bit of that line. Called from vcu_0159_08005874, 080058ac and 080058f0 (probably EXINT/RTC interrupt handlers) and in setup routines (080020a4, 080026f0).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | bit mask of EXINT lines (EXINT_LINE_n) |

- Addresses by version: 148: 0x0800BED8, 14a: 0x0800C31C, 14b: 0x0800C7A8, 14e: 0x0800C83C, 14f: 0x0800C978, 152: 0x0800CC04, 153: 0x0800CCF8, 0159: 0x0800CD64
- Peripheral registers: `EXINT.INTSTS` (W)
- Called by: `vcu_exint14_pb14_init`, `vcu_exint3_pa3_init`, `ERTC_WKUP_IRQHandler`, `EXINT15_10_IRQHandler`, `EXINT3_IRQHandler`
- Confidence: high

## exint_flag_get

**Test external-interrupt pending flag(s)**

AT32 SDK exint_flag_get(): returns whether EXINT.INTSTS & param_1 is non-zero. Called from vcu_0159_080058ac and 080058f0 (probably EXINT interrupt handlers).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | bit mask of EXINT lines |

**Returns** `bool`: true if any selected line is pending

- Addresses by version: 148: 0x0800BEE4, 14a: 0x0800C328, 14b: 0x0800C7B4, 14e: 0x0800C848, 14f: 0x0800C984, 152: 0x0800CC10, 153: 0x0800CD04, 0159: 0x0800CD70
- Peripheral registers: `EXINT.INTSTS` (R)
- Called by: `EXINT15_10_IRQHandler`, `EXINT3_IRQHandler`
- Confidence: high

## exint_init

**Configure an external-interrupt/event line**

AT32 SDK exint_init(): reads the exint_init_type (line_mode +0, line_select +4, line_polarity +8, line_enable +9). Always clears the selected lines in EXINT.INTEN and EXINT.EVTEN; if line_enable is set it sets them in INTEN (mode 0 = interrupt) or EVTEN (mode != 0 = event), clears them in POLCFG1/POLCFG2 and then sets POLCFG1 for rising (0), POLCFG2 for falling (1), or both for any other value. Called from vcu_0159_080020a4, 080021c4, 080024ec and 080026f0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | exint_init_type*: {u8 mode; u32 line_select@4; u8 polarity@8; u8 enable@9} |

- Addresses by version: 148: 0x0800BEFC, 14a: 0x0800C340, 14b: 0x0800C7CC, 14e: 0x0800C860, 14f: 0x0800C99C, 152: 0x0800CC28, 153: 0x0800CD1C, 0159: 0x0800CD88
- Peripheral registers: `EXINT.INTEN` (RW), `EXINT.EVTEN` (RW), `EXINT.POLCFG1` (RW), `EXINT.POLCFG2` (RW)
- Called by: `vcu_exint14_pb14_init`, `vcu_exint_pb12_pb14_init`, `vcu_0159_080024ec`, `vcu_exint3_pa3_init`
- Confidence: high

## exint_interrupt_enable

**Enable or disable the interrupt for EXINT lines**

AT32 SDK exint_interrupt_enable(): if param_2 == 1 sets the bits of param_1 in EXINT.INTEN, otherwise clears them. Called by vcu_0159_080026f0 and vcu_0159_0800688c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | bit mask of EXINT lines |
| `param_2` | `s32` | 1 = enable, anything else = disable |

- Addresses by version: 148: 0x0800BF64, 14a: 0x0800C3A8, 14b: 0x0800C834, 14e: 0x0800C8C8, 14f: 0x0800CA04, 152: 0x0800CC90, 153: 0x0800CD84, 0159: 0x0800CDF0
- Peripheral registers: `EXINT.INTEN` (RW)
- Called by: `vcu_exint3_pa3_init`, `vcu_0159_0800688c`
- Confidence: high

## vcu_exint14_pb14_init

**Route PB14 to EXINT line 14 as a falling-edge interrupt on EXINT15_10, store a probe result**

Configures a group of GPIO pins (PB2, PB10 to PB14, PF6, PA1) and routes PB14 to external interrupt line 14 with gpio_exint_line_config(GPIOB, 14). It sets line 14 as an interrupt on the falling edge with exint_init, clears its pending flag with exint_flag_clear, and enables the EXINT15_10 IRQ (number 40) with nvic_irq_enable. It finally stores the result of vcu_0159_08007a9c in DAT_20001FEB, which is not described yet.

**Notes:** Falling edge follows the exint_init polarity encoding (value 1). The meaning of the stored value depends on vcu_0159_08007a9c, which is not in this packet.

- Addresses by version: 148: 0x08001CBC, 14a: 0x08001D24, 14b: 0x08002004, 14e: 0x08002004, 14f: 0x08002060, 152: 0x0800209C, 153: 0x080020B8, 0159: 0x080020A4
- Peripheral registers: `GPIOA.CFGLR` (A), `GPIOB.CFGLR` (A), `GPIOF.CFGLR` (A)
- Called by: `vcu_0159_080013f8`
- Calls: `vcu_pa1_input_high`, `crm_periph_clock_enable`, `exint_default_para_init`, `exint_flag_clear`, `exint_init`, `gpio_default_para_init`, `gpio_exint_line_config`, `gpio_init`, `nvic_irq_enable`
- Confidence: medium

## vcu_exint3_pa3_init

**Route PA3 to EXINT line 3 as a falling-edge interrupt on EXINT3 (IRQ 9)**

Configures PA3 (mask 0x8) as an input with a pull-up (0x18) through gpio_init, and routes it to EXINT line 3 with gpio_exint_line_config(GPIOA, 3). It sets line 3 as an interrupt on the falling edge with exint_init, enables the line in INTEN with exint_interrupt_enable, clears its pending flag, and enables IRQ 9 (EXINT3) with priority 1. It is called from vcu_0159_0800688c.

**Notes:** PA3 is also USART2 RX in vcu_0159_08001e7c. The two have different callers, so they are presumably not used together.

- Addresses by version: 148: 0x08002328, 14a: 0x08002398, 14b: 0x08002650, 14e: 0x08002650, 14f: 0x080026AC, 152: 0x080026E8, 153: 0x08002704, 0159: 0x080026F0
- Peripheral registers: `GPIOA.CFGLR` (A)
- Called by: `vcu_0159_0800688c`
- Calls: `crm_periph_clock_enable`, `exint_default_para_init`, `exint_flag_clear`, `exint_init`, `exint_interrupt_enable`, `gpio_default_para_init`, `gpio_exint_line_config`, `gpio_init`, `nvic_irq_enable`
- Confidence: medium

## vcu_exint_pb12_pb14_init

**Route PB12 and PB14 to EXINT lines 12 and 14 as falling-edge interrupts on EXINT15_10**

Configures the pins PB2, PB10, PB11, PB12, PB13, PB14 and PA1 with gpio_default_para_init and gpio_init, giving PB14 a pull-up setting (0x18). It routes PB12 and PB14 to EXINT lines 12 and 14 with gpio_exint_line_config(GPIOB, 12) and (GPIOB, 14), sets both lines as falling-edge interrupts with exint_init (line mask 0x5000), and enables the EXINT15_10 IRQ (number 40) with nvic_irq_enable. It does not clear pending flags. It is called from vcu_0159_0800688c.

**Notes:** This routine and vcu_0159_080020a4 both configure PB14 for EXINT14; they have different callers and the one that runs is determined by the caller.

- Addresses by version: 148: 0x08001DD0, 14a: 0x08001E48, 14b: 0x08002124, 14e: 0x08002124, 14f: 0x08002180, 152: 0x080021BC, 153: 0x080021D8, 0159: 0x080021C4
- Peripheral registers: `GPIOA.CFGLR` (A), `GPIOB.CFGLR` (A)
- Called by: `vcu_0159_0800688c`
- Calls: `crm_periph_clock_enable`, `exint_default_para_init`, `exint_init`, `gpio_default_para_init`, `gpio_exint_line_config`, `gpio_init`, `nvic_irq_enable`
- Confidence: medium
