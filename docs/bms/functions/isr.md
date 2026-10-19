# BMS - `isr` functions

13 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`Default_Handler`](#default_handler) | 0x080010E6 | Default interrupt handler: spins in an endless loop |
| [`HardFault_Handler`](#hardfault_handler) | 0x080028F4 | Hard fault vector that resets the MCU via AIRCR.SYSRESETREQ instead of dumping fault state |
| [`LL_EXTI_Init`](#ll_exti_init) | 0x08002B0C | Programs EXTI line masks, edge triggers and interrupt or event mode from an init record |
| [`NVIC_SetPriority`](#nvic_setpriority) | 0x08003724 | CMSIS NVIC_SetPriority: set the 2-bit priority of an IRQ or system exception |
| [`PendSV_Handler`](#pendsv_handler) | 0x0800343C | PendSV exception handler: returns immediately, does no work |
| [`SVC_Handler`](#svc_handler) | 0x08003624 | SVCall exception handler: returns immediately, does no work |
| [`__NVIC_DisableIRQ`](#__nvic_disableirq) | 0x08002278 | Disables a device interrupt by writing its bit to NVIC ICER at 0xE000E180 |
| [`__NVIC_EnableIRQ`](#__nvic_enableirq) | 0x08002298 | Enables a device interrupt by writing its bit to NVIC ISER at 0xE000E100 |
| [`__NVIC_SetPriority`](#__nvic_setpriority) | 0x080022B0 | Sets the 2-bit priority of a device interrupt (NVIC IPR) or a system exception (SHPR) |
| [`bms_exti11_irq_arm`](#bms_exti11_irq_arm) | (removed) | Route PB11 to EXTI line 11, enable its interrupt and set EXTI4_15 priority |
| [`bms_exti11_irq_disarm`](#bms_exti11_irq_disarm) | (removed) | Disarm EXTI line 11 and its NVIC line EXTI4_15 when the armed byte is set |
| [`bms_nvic_system_reset_plain`](#bms_nvic_system_reset_plain) | 0x0800A2A0 | CMSIS __NVIC_SystemReset body: request a system reset through SCB AIRCR and spin |
| [`exti_disable_lines_2_8_12`](#exti_disable_lines_2_8_12) | 0x080093F0 | Clear EXTI interrupt mask bits for lines 12, 8 and 2 |

## Default_Handler

**Default interrupt handler: spins in an endless loop**

Single infinite loop with no body. The vector table slot labelled CEC_IRQHandler points here, and unimplemented interrupts or faults that land on this default entry halt the core. The handler does not log, disable the source, or reset the MCU. Whether a watchdog recovers the hang is not visible in this function.

**Notes:** The CEC_IRQHandler label is the vector-table name for this slot; the slot is probably an unused IRQ default, not a real CEC handler.

- Addresses by version: 4130: 0x080010E6, 4139: 0x080010E6, 4148: 0x080010E6, 4168: 0x080010E6
- Vector: `CEC_IRQHandler`
- Confidence: high

## HardFault_Handler

**Hard fault vector that resets the MCU via AIRCR.SYSRESETREQ instead of dumping fault state**

Installed in the HardFault vector, but the body is CMSIS NVIC_SystemReset and not a fault handler. It runs DSB, writes SCB AIRCR = 0x05FA0004 (VECTKEY 0x5FA with SYSRESETREQ set), runs DSB again, and then spins until the reset takes effect. Any hard fault therefore resets the chip, and CFSR and HFSR are never read here. The name is kept because it is the vector slot name.

**Notes:** The AIRCR write is a constant here, so the PRIGROUP-preserving form of NVIC_SystemReset has been simplified. The name comes from the vector table, not from the code.

- Addresses by version: 4130: 0x080028F4, 4139: 0x080028F4, 4148: 0x080028F4, 4168: 0x080028F4
- Vector: `HardFault_Handler`
- Peripheral registers: `SCB+0xc` (W)
- Confidence: high

## LL_EXTI_Init

**Programs EXTI line masks, edge triggers and interrupt or event mode from an init record**

Configures EXTI lines from an LL_EXTI_InitTypeDef-style record: word 0 is the mask for lines 0 to 31, word 1 the mask for lines 32 to 63, and byte 8 is LineCommand (0 disables). For lines 0 to 31, byte 9 selects Mode (0 = interrupt: IMR1 set and EMR1 clear, 1 = event: IMR1 clear and EMR1 set, 2 = both) and byte 10 selects Trigger (1 = rising: RTSR1 set and FTSR1 clear, 2 = falling, 3 = both, 0 = none). Lines 32 to 63 get only the IMR2 and EMR2 bits for their mode, with no edge registers. With LineCommand 0 it clears the lines in IMR1, EMR1, IMR2 and EMR2 and leaves the edge registers alone.

| Parameter | Type | Description |
|---|---|---|
| `init` | `ptr` | EXTI init record: line masks at +0 and +4, LineCommand at +8, Mode at +9, Trigger at +10 |

**Returns** `u32`: error bitmask: 1 = invalid Mode for lines 0-31, 2 = invalid Trigger, 4 = invalid Mode for lines 32-63; 0 = OK

**Notes:** Trigger edges are not programmed for lines 32 to 63 (RTSR2 and FTSR2 are never written), so a line in that range cannot have its edge set through this function.

- Addresses by version: 4130: 0x08002B0C, 4139: 0x08002B0C, 4148: 0x08002B0C, 4168: 0x08002B0C
- Peripheral registers: `EXTI.RTSR1` (RW), `EXTI.FTSR1` (RW), `EXTI.IMR1` (RW), `EXTI.EMR1` (RW), `EXTI.IMR2` (RW), `EXTI.EMR2` (RW)
- Called by: `bms_gpio_exti_init`
- Confidence: high

## NVIC_SetPriority

**CMSIS NVIC_SetPriority: set the 2-bit priority of an IRQ or system exception**

CMSIS-style NVIC_SetPriority for the Cortex-M0+. The priority in param_2 is masked to 2 bits and placed in bits 7:6 of its byte lane (STM32G0 implements __NVIC_PRIO_BITS = 2). For a negative IRQn, meaning a system exception (SVCall -5, PendSV -2, SysTick -1), the byte is written into the SCB SHPR2/SHPR3 word at 0xE000ED1C through a read-modify-write that keeps the other three byte lanes. For IRQn >= 0 the byte goes into the NVIC IPR array at 0xE000E400 with the same read-modify-write. Caller bms_4168_0800a3e8 sets interrupt priorities.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | IRQn: negative for system exceptions, otherwise device IRQ number |
| `param_2` | `u32` | priority; only bits 1:0 are used |

- Addresses by version: 4130: 0x08003724, 4139: 0x08003724, 4148: 0x08003724, 4168: 0x08003724
- Peripheral registers: `NVIC+0x300` (A), `SCB+0x1c` (A)
- Called by: `bms_tim6_tim7_start`
- Confidence: high

## PendSV_Handler

**PendSV exception handler: returns immediately, does no work**

Vector-table entry for the PendSV system exception (exception number -2). The body is a bare return, so this build does no deferred work and no context switch in PendSV. Its priority, when configured, is written by NVIC_SetPriority into the SCB SHPR3 byte.

- Addresses by version: 4130: 0x0800343C, 4139: 0x0800343C, 4148: 0x0800343C, 4168: 0x0800343C
- Vector: `PendSV_Handler`
- Confidence: high

## SVC_Handler

**SVCall exception handler: returns immediately, does no work**

Vector-table entry for the SVCall system exception (exception number -5). The body is a bare return, so supervisor calls perform no work in this build. Its priority, when configured, is written by NVIC_SetPriority into the SCB SHPR2 byte (bits 31:30 of the word).

- Addresses by version: 4130: 0x08003624, 4139: 0x08003624, 4148: 0x08003624, 4168: 0x08003624
- Vector: `SVC_Handler`
- Confidence: high

## __NVIC_DisableIRQ

**Disables a device interrupt by writing its bit to NVIC ICER at 0xE000E180**

CMSIS inline NVIC_DisableIRQ for the Cortex-M0+ core. For IRQn >= 0 it writes 1 << (IRQn & 0x1f) to NVIC ICER[0] (0xE000E180), which clears that interrupt's enable bit, then runs DSB and ISB so the disable has taken effect before returning. Negative IRQn values (core exceptions) are ignored. Only ICER[0] is used, which covers IRQ 0 to 31 as on the STM32G0B1.

| Parameter | Type | Description |
|---|---|---|
| `IRQn` | `s32` | device interrupt number; negative values are ignored |

- Addresses by version: 4130: 0x08002278, 4139: 0x08002278, 4148: 0x08002278, 4168: 0x08002278
- Peripheral registers: `NVIC+0x80` (W)
- Called by: `bms_4168_08001bf4`
- Confidence: high

## __NVIC_EnableIRQ

**Enables a device interrupt by writing its bit to NVIC ISER at 0xE000E100**

CMSIS inline NVIC_EnableIRQ for the Cortex-M0+ core. For IRQn >= 0 it writes 1 << (IRQn & 0x1f) to NVIC ISER[0] (the NVIC base 0xE000E100), which sets that interrupt's enable bit. Negative IRQn values are ignored. No barrier is issued, and only the first ISER word is used, which covers IRQ 0 to 31.

| Parameter | Type | Description |
|---|---|---|
| `IRQn` | `s32` | device interrupt number; negative values are ignored |

- Addresses by version: 4130: 0x08002298, 4139: 0x08002298, 4148: 0x08002298, 4168: 0x08002298
- Peripheral registers: `NVIC+0x0` (W)
- Called by: `bms_4168_08001c24`, `bms_4168_08002234`, `bms_rtc_wakeup_period_set`
- Confidence: high

## __NVIC_SetPriority

**Sets the 2-bit priority of a device interrupt (NVIC IPR) or a system exception (SHPR)**

CMSIS inline NVIC_SetPriority with __NVIC_PRIO_BITS = 2, so the priority is shifted to the top of the byte (priority << 6); only the low 2 bits of the argument are used and 0 is the highest priority. For IRQn >= 0 it does a read-modify-write of one byte in NVIC IPR (0xE000E400 plus IRQn with the low 2 bits dropped). For negative IRQn it does the same on one byte of SCB SHPR1/2/3 (0xE000ED18 to 0xE000ED20), selecting the register from (IRQn & 0xf) - 8. Other bytes in the word are preserved.

| Parameter | Type | Description |
|---|---|---|
| `IRQn` | `s32` | device interrupt number, or negative system exception number |
| `priority` | `u32` | priority value; only bits 1:0 are used, 0 is highest |

- Addresses by version: 4130: 0x080022B0, 4139: 0x080022B0, 4148: 0x080022B0, 4168: 0x080022B0
- Peripheral registers: `NVIC+0x300` (A), `SCB+0x1c` (A)
- Called by: `bms_4168_08001c24`, `bms_4168_080021ec`, `bms_4168_08002234`, `bms_rtc_wakeup_period_set`
- Confidence: high

## bms_exti11_irq_arm

**Route PB11 to EXTI line 11, enable its interrupt and set EXTI4_15 priority**

Arms the PB11 wake or input interrupt. It sets the EXTI11 source field in EXTI.EXTICR3 (bits 26:24 = 001, port B) by read-modify-write, then calls LL_EXTI_Init with line mask 0x800 and the trailing word 0x00010001, whose mode and edge bits are not decoded here. It writes 0x800 to the EXTI register at 0x40021810, clears MODER11 and PUPDR11 on GPIOB to leave PB11 as an unpulled input, and writes 0x80 into bits 31:24 of NVIC IPR register 0xE000E404, giving IRQ 7 (EXTI4_15 on STM32G0) priority 2. It then sets bit 7 in NVIC ISER to enable IRQ 7 and stores 1 in the RAM flag at 0x20000594. The counterpart is bms_exti11_irq_disarm.

**Notes:** The packet lists the register at 0x40021810 as both EXTI.SWIER1 and EXTI.FPR1, so whether the write triggers or clears line 11 is unresolved. The IRQ 7 mapping is from the STM32G0 vector table, not from the packet's irq list.

- Addresses by version: 4130: 0x080096A4, 4139: 0x08009BDC
- Peripheral registers: `EXTI.SWIER1` (A), `EXTI.FPR1` (W), `EXTI.EXTICR3` (RW), `NVIC+0x0` (W), `NVIC+0x304` (RW)
- Called by: `bms_4139_08007238`
- Calls: `LL_EXTI_Init`
- Confidence: medium

## bms_exti11_irq_disarm

**Disarm EXTI line 11 and its NVIC line EXTI4_15 when the armed byte is set**

If the armed byte at 0x20000594 is nonzero, it clears the byte, clears EXTI.IMR1 bit 11 (at 0x40021880, the CPU interrupt mask for line 11), and writes 0x80 to NVIC_ICER0 (0xE000E180), which disables NVIC IRQ 7 (EXTI4_15 on STM32G0). It finishes with DSB and ISB barriers so the disable is in effect before return. If the byte is zero, the function does nothing.

**Notes:** Present in the 4130 and 4139 builds only. The NVIC disable stops every EXTI4_15 interrupt, not only line 11, so other lines in that group are affected too. The write that sets the armed byte is elsewhere. Callers: bms_4139_08007238 and bms_4139_0800e4f8.

- Addresses by version: 4130: 0x08009670, 4139: 0x08009BA8
- Peripheral registers: `EXTI.IMR1` (RW), `NVIC+0x80` (W)
- Called by: `bms_4139_08007238`, `bms_4139_0800e4f8`
- Confidence: high

## bms_nvic_system_reset_plain

**CMSIS __NVIC_SystemReset body: request a system reset through SCB AIRCR and spin**

Runs a DSB, writes 0x05FA0004 to SCB->AIRCR (VECTKEY 0x05FA in the high half and SYSRESETREQ in bit 2), runs another DSB, then loops forever while the reset takes effect. This is the standard CMSIS __NVIC_SystemReset body without any interrupt disable. It never returns.

**Notes:** Same routine as NVIC_SystemReset at bms_4168_08001444 (wave1_batch01), which additionally executes CPSID i first. The library name is already taken there, so this entry uses a unique name. Callers: bms_4168_08003c3c and bms_4168_080082f0.

- Addresses by version: 4130: 0x08009240, 4139: 0x08009740, 4148: 0x08009F8C, 4168: 0x0800A2A0
- Peripheral registers: `SCB+0xc` (W)
- Called by: `bms_4168_08003c3c`, `bms_4168_080082f0`
- Confidence: high

## exti_disable_lines_2_8_12

**Clear EXTI interrupt mask bits for lines 12, 8 and 2**

Clears bits 12, 8 and 2 of EXTI.IMR1 (0x40021880, base 0x40021800 plus offset 0x80), disabling the interrupt for EXTI lines 12, 8 and 2. Each bit is cleared with a separate read-modify-write, so the other mask bits are kept but each step is not atomic. This is equivalent to three LL_EXTI_DisableIT calls. Caller bms_4168_080082f0 uses it to mask the external interrupts before reconfiguring them.

**Notes:** The mask-register offset and bit numbers are certain from the code; the reason for masking is inferred from the single caller.

- Addresses by version: 4130: 0x08008390, 4139: 0x08008890, 4148: 0x080090DC, 4168: 0x080093F0
- Peripheral registers: `EXTI.IMR1` (ARW)
- Called by: `bms_4168_080082f0`
- Confidence: high
