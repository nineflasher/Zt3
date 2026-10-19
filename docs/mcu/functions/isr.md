# MCU - `isr` functions

16 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`BusFault_Handler`](#busfault_handler) | 0x080032C8 | Cortex-M BusFault exception handler: infinite loop |
| [`BusFault_Handler_v12b`](#busfault_handler_v12b) | (removed) | Bus fault handler in MCU_12b: infinite loop |
| [`DebugMon_Handler`](#debugmon_handler) | 0x080061A4 | Debug monitor exception handler: empty, returns immediately |
| [`DebugMon_Handler_v12b`](#debugmon_handler_v12b) | (removed) | Debug monitor exception handler in MCU_12b: empty, returns immediately |
| [`Default_Handler`](#default_handler) | 0x080011A2 | Default trap for unused interrupt vectors: spins forever |
| [`MemManage_Handler`](#memmanage_handler) | 0x08007BA0 | MemManage fault handler: infinite loop |
| [`NMI_Handler`](#nmi_handler) | 0x08007BCC | Non-maskable interrupt handler: returns immediately |
| [`PendSV_Handler`](#pendsv_handler) | 0x0800119E | PendSV exception handler: infinite loop |
| [`SVC_Handler`](#svc_handler) | 0x08009A88 | SVC exception handler: empty, returns immediately |
| [`SysTick_Handler`](#systick_handler) | 0x0800A2AA | SysTick exception handler: empty, returns immediately |
| [`UsageFault_Handler`](#usagefault_handler) | 0x0800B320 | UsageFault exception handler: infinite loop |
| [`mcu_irq_disable_thunk`](#mcu_irq_disable_thunk) | 0x08006B68 | Disable interrupts by calling disableIRQinterrupts (critical-section entry) |
| [`mcu_irq_enable_thunk`](#mcu_irq_enable_thunk) | 0x08006B6C | Enable interrupts by calling enableIRQinterrupts (critical-section exit) |
| [`nvic_irq_enable`](#nvic_irq_enable) | 0x0800DA14 | Set the preempt and sub priority of an IRQ with the current group, then enable it |
| [`nvic_priority_group_config`](#nvic_priority_group_config) | 0x0800DA98 | Set the NVIC priority grouping in SCB->AIRCR with the VECTKEY |
| [`nvic_vector_table_set`](#nvic_vector_table_set) | 0x0800DABC | Set the vector table base in SCB->VTOR with 128-byte offset alignment |

## BusFault_Handler

**Cortex-M BusFault exception handler: infinite loop**

Vector table handler for BusFault; spins forever (b .), so a bus error hangs the CPU until the independent watchdog resets it. No logging or recovery. Present in the 143, 152 and 0160 builds (shared with other fault handlers that loop in the same manner).

- Addresses by version: 143: 0x080032A4, 152: 0x08003228, 0160: 0x080032C8
- Vector: `BusFault_Handler`
- Confidence: high

## BusFault_Handler_v12b

**Bus fault handler in MCU_12b: infinite loop**

Single branch-to-self trap in the MCU_12b build, installed in the BusFault vector slot. A bus error therefore hangs the CPU until the watchdog resets it. Other builds have the equivalent handler at a different address.

- Addresses by version: 12b: 0x080013FE
- Vector: `BusFault_Handler`
- Confidence: high

## DebugMon_Handler

**Debug monitor exception handler: empty, returns immediately**

Handler for the Cortex-M DebugMonitor vector in the 143, 152 and 0160 builds. The body is a single return, so debug monitor events are ignored. The 12b build has the same stub at another address under the name DebugMon_Handler_v12b.

- Addresses by version: 143: 0x080060D4, 152: 0x08006104, 0160: 0x080061A4
- Vector: `DebugMon_Handler`
- Confidence: high

## DebugMon_Handler_v12b

**Debug monitor exception handler in MCU_12b: empty, returns immediately**

Empty handler for the DebugMonitor exception vector in the MCU_12b build: it contains only a return. Other builds put the same stub at a different address.

- Addresses by version: 12b: 0x0800141E
- Vector: `DebugMon_Handler`
- Confidence: high

## Default_Handler

**Default trap for unused interrupt vectors: spins forever**

Single branch-to-self shared by all vector-table slots that have no real handler (the packet lists it under the DMA2_Channel6_7 slot but many slots point at this address). Only PVM, ADC1, CAN1_RX0, CAN1_SE, TMR3 and TMR4 have real handlers on the MCU, so any other interrupt locks the CPU here. Same as VCU Default_Handler.

- Addresses by version: 12b: 0x080011AA, 143: 0x080011A2, 152: 0x080011A2, 0160: 0x080011A2
- Vector: `DMA2_Channel6_7_IRQHandler`
- Confidence: high

## MemManage_Handler

**MemManage fault handler: infinite loop**

Cortex-M MemManage exception vector. The body is a bare infinite loop with no fault status saved, so a memory-protection fault halts the core until the watchdog resets it.

- Addresses by version: 12b: 0x08007C7C, 143: 0x08007B70, 152: 0x08007BF8, 0160: 0x08007BA0
- Vector: `MemManage_Handler`
- Confidence: high

## NMI_Handler

**Non-maskable interrupt handler: returns immediately**

Cortex-M NMI vector target. The body is a bare return, so NMI is acknowledged by doing nothing; no clock, watchdog or fault register is touched. Reached only through the vector table, no direct callers.

- Addresses by version: 12b: 0x08007CA8, 143: 0x08007B9C, 152: 0x08007C24, 0160: 0x08007BCC
- Vector: `NMI_Handler`
- Confidence: high

## PendSV_Handler

**PendSV exception handler: infinite loop**

Empty trap: the body is a single branch-to-self, so a PendSV exception hangs the core (until the watchdog resets it). The firmware does not use an RTOS context switch, so PendSV is never expected to fire.

- Addresses by version: 12b: 0x080011A6, 143: 0x0800119E, 152: 0x0800119E, 0160: 0x0800119E
- Vector: `PendSV_Handler`
- Confidence: high

## SVC_Handler

**SVC exception handler: empty, returns immediately**

Cortex-M SVCall vector target whose body is a bare return, so an svc instruction does nothing. Its presence in all four builds suggests the SVC slot is an unused default stub.

- Addresses by version: 12b: 0x0800982C, 143: 0x080099C8, 152: 0x08009A14, 0160: 0x08009A88
- Vector: `SVC_Handler`
- Confidence: high

## SysTick_Handler

**SysTick exception handler: empty, returns immediately**

Cortex-M SysTick vector target with a bare return, so the core SysTick interrupt does nothing. The time base must come from elsewhere; the MCU brief lists TMR3 and TMR4 as the active timer interrupts.

- Addresses by version: 12b: 0x0800A03A, 143: 0x0800A1EA, 152: 0x0800A236, 0160: 0x0800A2AA
- Vector: `SysTick_Handler`
- Confidence: high

## UsageFault_Handler

**UsageFault exception handler: infinite loop**

Cortex-M UsageFault vector target that spins forever. A usage fault (undefined instruction, unaligned access, or divide by zero when trapping is enabled) hangs the MCU until a reset, for example from the watchdog if it is enabled.

- Addresses by version: 12b: 0x0800B0A2, 143: 0x0800B330, 152: 0x0800B2C0, 0160: 0x0800B320
- Vector: `UsageFault_Handler`
- Confidence: high

## mcu_irq_disable_thunk

**Disable interrupts by calling disableIRQinterrupts (critical-section entry)**

A two-instruction wrapper that calls the vendor-named routine disableIRQinterrupts, which masks the global interrupt enable (PRIMASK set, cpsid i). It is the entry half of a critical section. Called from mcu_0160_080031cc and mcu_0160_080061e8. The body of disableIRQinterrupts is not in this packet, so the PRIMASK mechanism is inferred from its name.

- Addresses by version: 12b: 0x08006CBC, 143: 0x08006B90, 152: 0x08006BC0, 0160: 0x08006B68
- Called by: `mcu_0160_080031cc`, `mcu_0160_080061e8`
- Confidence: high

## mcu_irq_enable_thunk

**Enable interrupts by calling enableIRQinterrupts (critical-section exit)**

A two-instruction wrapper that calls the vendor-named routine enableIRQinterrupts, which clears the global interrupt mask (PRIMASK, cpsie i). It is the exit half of the critical section opened by mcu_irq_disable_thunk. Called from mcu_0160_080031cc and mcu_0160_080061f6. The body of enableIRQinterrupts is not in this packet.

- Addresses by version: 12b: 0x08006CC0, 143: 0x08006B94, 152: 0x08006BC4, 0160: 0x08006B6C
- Called by: `mcu_0160_080031cc`, `mcu_0160_080061f6`
- Confidence: high

## nvic_irq_enable

**Set the preempt and sub priority of an IRQ with the current group, then enable it**

SDK nvic_irq_enable. It encodes the two priorities with the CMSIS NVIC_EncodePriority rule for the current group in SCB->AIRCR bits 8..10: preempt bits = min(4, 7 - group), sub bits = 0 when group + 4 < 7, else group - 3. The encoded value goes into the top four bits of the priority byte. For device interrupts the byte is IPR at 0xE000E400 + IRQn, and the enable bit is then set in NVIC ISER. For negative IRQn (system handlers) the byte goes into the SHP array instead and nothing is enabled.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | IRQn; negative values address system exception priorities |
| `param_2` | `u32` | preempt priority |
| `param_3` | `u32` | sub priority |

- Addresses by version: 12b: 0x0800D5C4, 143: 0x0800D83C, 152: 0x0800D8D4, 0160: 0x0800DA14
- Peripheral registers: `NVIC+0x0` (A), `NVIC.None` (A), `SCB+0xc` (R), `SCB+0x14` (A)
- Called by: `mcu_0160_08003368`, `mcu_0160_080065c4`, `mcu_0160_0800d548`
- Confidence: high

## nvic_priority_group_config

**Set the NVIC priority grouping in SCB->AIRCR with the VECTKEY**

SDK nvic_priority_group_config. It writes SCB->AIRCR (0xE000ED0C) as the existing value with mask 0xF8FF, the group (0..7) in bits 8..10, and the VECTKEY 0x05FA in the upper half. It sets how later priority values split into preempt and sub bits, so it is normally called once at startup before nvic_irq_enable.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | priority group 0..7 |

- Addresses by version: 12b: 0x0800D648, 143: 0x0800D8C0, 152: 0x0800D958, 0160: 0x0800DA98
- Peripheral registers: `SCB+0xc` (RW)
- Called by: `mcu_0160_080065c4`
- Confidence: high

## nvic_vector_table_set

**Set the vector table base in SCB->VTOR with 128-byte offset alignment**

SDK nvic_vector_table_set. It writes SCB->VTOR (0xE000ED08) as base | (offset & 0x1FFFFF80). The offset is aligned to 128 bytes, and the base argument selects the memory region. It relocates the vector table, for example to the application after the 4 KiB bootloader at 0x08001000.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | region base, for example the flash or RAM base |
| `param_2` | `u32` | offset within the region |

- Addresses by version: 12b: 0x0800D66C, 143: 0x0800D8E4, 152: 0x0800D97C, 0160: 0x0800DABC
- Peripheral registers: `SCB+0x8` (W)
- Called by: `mcu_0160_0800d548`
- Confidence: high
