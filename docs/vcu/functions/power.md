# VCU - `power` functions

5 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`debug_periph_mode_set`](#debug_periph_mode_set) | 0x0800BA94 | Set or clear bits in the DEBUG (DBGMCU) control register (SDK debug_periph_mode_set) |
| [`pwc_battery_powered_domain_access`](#pwc_battery_powered_domain_access) | 0x0800E718 | Enable or disable write access to the battery-powered domain (PWC.CTRL.BPWEN) |
| [`pwc_deep_sleep_mode_enter`](#pwc_deep_sleep_mode_enter) | 0x0800E728 | Enter deep sleep with WFE or WFI, setting and clearing SCB.SCR.SLEEPDEEP |
| [`pwc_voltage_regulate_set`](#pwc_voltage_regulate_set) | 0x0800E754 | Select the voltage regulator mode through PWC.CTRL.VRSEL |
| [`vcu_deferred_system_reset`](#vcu_deferred_system_reset) | 0x08003BC8 | After 20 calls with DAT_20001f52 == 1, trigger a Cortex-M system reset |

## debug_periph_mode_set

**Set or clear bits in the DEBUG (DBGMCU) control register (SDK debug_periph_mode_set)**

ORs param_1 into DEBUG.CTRL (0xE0042004) when param_2 is nonzero, otherwise clears those bits. The bits select peripherals (timers, WDT, ERTC, CAN, I2C) that are frozen while the core is halted in the debugger. Called once from vcu_0159_0800d858 during init. Artery SDK at32f415_debug.c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | DEBUG_*_PAUSE bit mask |
| `param_2` | `s32` | nonzero = set, 0 = clear |

- Addresses by version: 148: 0x0800ABC4, 14a: 0x0800AFB0, 14b: 0x0800B43C, 14e: 0x0800B4D0, 14f: 0x0800B60C, 152: 0x0800B898, 153: 0x0800B98C, 0159: 0x0800BA94
- Peripheral registers: `DEBUG.CTRL` (RW)
- Called by: `vcu_0159_0800d858`
- Confidence: high

## pwc_battery_powered_domain_access

**Enable or disable write access to the battery-powered domain (PWC.CTRL.BPWEN)**

Sets or clears PWC.CTRL bit 8 (BPWEN) with a read-modify-write, leaving the other bits unchanged. While BPWEN is clear, writes to the RTC/ERTC backup registers and the LSE control are blocked. This is the Artery SDK pwc_battery_powered_domain_access and is called before ERTC setup.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | confirm_state: non-zero enables access, zero disables it |

- Addresses by version: 148: 0x0800D700, 14a: 0x0800DB94, 14b: 0x0800E020, 14e: 0x0800E0C0, 14f: 0x0800E20C, 152: 0x0800E4B4, 153: 0x0800E5A8, 0159: 0x0800E718
- Peripheral registers: `PWC.CTRL` (RW)
- Called by: `vcu_0159_0800c960`
- Confidence: high

## pwc_deep_sleep_mode_enter

**Enter deep sleep with WFE or WFI, setting and clearing SCB.SCR.SLEEPDEEP**

Sets SCB.SCR.SLEEPDEEP (bit 2) so the core sleeps in deep-sleep mode, then executes WFE (preceded by SEV, and twice so a pending event is cleared) when the argument is 1, or WFI when it is 0. Other values fall through with no sleep. SLEEPDEEP is cleared again after wake-up so later sleeps are ordinary sleep. This is the Artery SDK pwc_deep_sleep_mode_enter. Its caller is vcu_0159_0800688c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 0 = enter with WFI, 1 = enter with WFE |

- Addresses by version: 148: 0x0800D710, 14a: 0x0800DBA4, 14b: 0x0800E030, 14e: 0x0800E0D0, 14f: 0x0800E21C, 152: 0x0800E4C4, 153: 0x0800E5B8, 0159: 0x0800E728
- Peripheral registers: `SCB+0x10` (RW)
- Called by: `vcu_0159_0800688c`
- Confidence: high

## pwc_voltage_regulate_set

**Select the voltage regulator mode through PWC.CTRL.VRSEL**

Writes bit 0 of PWC.CTRL (VRSEL) to the low bit of the argument, keeping the other bits. The bit selects between the normal and the low-power voltage regulator. This is the Artery SDK pwc_voltage_regulate_set and its caller is vcu_0159_0800688c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | regulator mode: 0 = normal, 1 = low power |

- Addresses by version: 148: 0x0800D73C, 14a: 0x0800DBD0, 14b: 0x0800E05C, 14e: 0x0800E0FC, 14f: 0x0800E248, 152: 0x0800E4F0, 153: 0x0800E5E4, 0159: 0x0800E754
- Peripheral registers: `PWC.CTRL` (RW)
- Called by: `vcu_0159_0800688c`
- Confidence: high

## vcu_deferred_system_reset

**After 20 calls with DAT_20001f52 == 1, trigger a Cortex-M system reset**

If the request byte DAT_20001f52 equals 1, increments the counter DAT_2000134e; once it exceeds 0x13 (i.e. on the 20th call) it executes a DSB, writes SCB->AIRCR (0xE000ED0C) with VECTKEY 0x5FA and SYSRESETREQ (bit 2) while preserving PRIGROUP (mask 0x700), executes another DSB and spins forever until the reset occurs. This is the CMSIS NVIC_SystemReset() sequence preceded by a debounce delay. Used to restart the VCU (e.g. after a configuration/update command); called from the main handler vcu_0159_0800a1d0.

**Notes:** The counter is not cleared when DAT_20001f52 is not 1, so non-consecutive requests also accumulate.

- Addresses by version: 148: 0x08003520, 14a: 0x08003738, 14b: 0x08003A5C, 14e: 0x08003A5C, 14f: 0x08003AB8, 152: 0x08003B1C, 153: 0x08003B3C, 0159: 0x08003BC8
- Peripheral registers: `SCB+0xc` (RW)
- Called by: `vcu_0159_0800a1d0`
- Confidence: high
