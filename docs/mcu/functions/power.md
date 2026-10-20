# MCU - `power` functions

5 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`NVIC_SystemReset`](#nvic_systemreset) | 0x0800A258 | CMSIS NVIC_SystemReset: request a system reset through AIRCR.SYSRESETREQ and spin |
| [`mcu_pvm_init`](#mcu_pvm_init) | 0x08009F40 | Set up the PVM on EXINT line 16, select its threshold, enable it and wait for the first event |
| [`pwc_battery_powered_domain_access`](#pwc_battery_powered_domain_access) | 0x0800DAD0 | Enable or disable write access to the battery-powered backup domain |
| [`pwc_power_voltage_monitor_enable`](#pwc_power_voltage_monitor_enable) | 0x0800DAE0 | Enable or disable the programmable voltage monitor in PWC.CTRL |
| [`pwc_pvm_level_select`](#pwc_pvm_level_select) | 0x0800DAF0 | Select the programmable voltage monitor threshold in PWC.CTRL bits 5..7 |

## NVIC_SystemReset

**CMSIS NVIC_SystemReset: request a system reset through AIRCR.SYSRESETREQ and spin**

Same as the CMSIS __NVIC_SystemReset inline in core_cm4.h. When running privileged it runs enableFIQinterrupts(1) (the decompiler's name for the Cortex-M fault/interrupt-mask enable), then DSB, then writes SCB->AIRCR (0xE000ED0C) = 0x05FA0004 | (old AIRCR & 0x700). That is the VECTKEY 0x5FA with SYSRESETREQ set, keeping the PRIGROUP field. It then runs DSB again and loops forever while the reset takes effect. Callers mcu_0160_080065f0, mcu_0160_0800a0b0, mcu_0160_0800a85c and mcu_12b_0800bfd0 suggest it is a deliberate reset path, possibly for fault recovery (inferred).

**Notes:** The exact instruction behind enableFIQinterrupts(1) was not verified; on Cortex-M it is presumably an interrupt or fault mask clear.

- Addresses by version: 12b: 0x08009FE8, 143: 0x0800A198, 152: 0x0800A1E4, 0160: 0x0800A258
- Peripheral registers: `SCB+0xc` (RW)
- Called by: `mcu_0160_080065f0`, `mcu_0160_0800a0b0`, `mcu_0160_0800a85c`
- Confidence: high

## mcu_pvm_init

**Set up the PVM on EXINT line 16, select its threshold, enable it and wait for the first event**

Power-voltage-monitor setup. It enables the PWC clock, configures EXINT line 16 (mask 0x10000, the PVM line) in interrupt mode through an exint_init_type record, selects threshold level 7 with pwc_pvm_level_select and enables the monitor with pwc_power_voltage_monitor_enable. It then polls exint_flag_get on line 16 until the event is pending, with no time limit, clears the flag with exint_flag_clear, and writes 0x2 to 0xE000E280 (NVIC ICPR0 in the ARMv7-M layout), which clears any pending state of IRQ1 (PVM) so that the first real interrupt is not stale.

**Notes:** IRQ1 is PVM in the image's IRQ table (at32f415_irqs.json). The edge code and the level meaning come from packed record values that are not decoded here.

- Addresses by version: 12b: 0x08009CE4, 143: 0x08009E80, 152: 0x08009ECC, 0160: 0x08009F40
- Peripheral registers: `NVIC.None` (W)
- Called by: `mcu_0160_0800325c`
- Calls: `crm_periph_clock_enable`, `exint_flag_clear`, `exint_flag_get`, `exint_init`, `pwc_power_voltage_monitor_enable`, `pwc_pvm_level_select`
- Confidence: medium

## pwc_battery_powered_domain_access

**Enable or disable write access to the battery-powered backup domain**

SDK pwc_battery_powered_domain_access. It sets or clears bit 8 of PWC.CTRL (the battery-powered domain write enable), leaving the other control bits unchanged. Write access must be enabled before the RTC or backup registers can be changed.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `bool` | new state: true enables write access |

- Addresses by version: 12b: 0x0800D680, 143: 0x0800D8F8, 152: 0x0800D990, 0160: 0x0800DAD0
- Peripheral registers: `PWC.CTRL` (RW)
- Called by: `mcu_0160_08006028`
- Confidence: high

## pwc_power_voltage_monitor_enable

**Enable or disable the programmable voltage monitor in PWC.CTRL**

SDK pwc_power_voltage_monitor_enable. It sets or clears bit 4 (PVMEN) of PWC.CTRL, leaving the other bits unchanged. The threshold is chosen separately by pwc_pvm_level_select.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `bool` | new state: true enables the voltage monitor |

- Addresses by version: 12b: 0x0800D690, 143: 0x0800D908, 152: 0x0800D9A0, 0160: 0x0800DAE0
- Peripheral registers: `PWC.CTRL` (RW)
- Called by: `mcu_pvm_init`
- Confidence: high

## pwc_pvm_level_select

**Select the programmable voltage monitor threshold in PWC.CTRL bits 5..7**

SDK pwc_pvm_level_select. It writes the 3-bit PVM voltage select into bits 5..7 of PWC.CTRL and keeps the other bits. The selection takes effect when the monitor is enabled with pwc_power_voltage_monitor_enable.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | PVM threshold code 0..7 |

- Addresses by version: 12b: 0x0800D6A0, 143: 0x0800D918, 152: 0x0800D9B0, 0160: 0x0800DAF0
- Peripheral registers: `PWC.CTRL` (RW)
- Called by: `mcu_pvm_init`
- Confidence: high
