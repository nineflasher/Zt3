# MCU - `power` functions

4 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`NVIC_SystemReset`](#nvic_systemreset) | 0x0800A258 | CMSIS NVIC_SystemReset: request a system reset through AIRCR.SYSRESETREQ and spin |
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
- Called by: `mcu_0160_08009f40`
- Confidence: high

## pwc_pvm_level_select

**Select the programmable voltage monitor threshold in PWC.CTRL bits 5..7**

SDK pwc_pvm_level_select. It writes the 3-bit PVM voltage select into bits 5..7 of PWC.CTRL and keeps the other bits. The selection takes effect when the monitor is enabled with pwc_power_voltage_monitor_enable.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | PVM threshold code 0..7 |

- Addresses by version: 12b: 0x0800D6A0, 143: 0x0800D918, 152: 0x0800D9B0, 0160: 0x0800DAF0
- Peripheral registers: `PWC.CTRL` (RW)
- Called by: `mcu_0160_08009f40`
- Confidence: high
