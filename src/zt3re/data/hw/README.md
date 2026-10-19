# Hardware register layouts for Ghidra

Peripheral register-layout C headers and peripheral base maps for the two chip
families in the scooter firmware:

| Files                        | Family                          | Used by               |
|------------------------------|---------------------------------|-----------------------|
| `stm32f1.h`, `peripherals_stm32f1.json` | STM32F103xB, Cortex-M3 (GD32F103 clone) | MCU and VCU boards |
| `stm32f0.h`, `peripherals_stm32f0.json` | STM32F0 (F091 superset), Cortex-M0     | BMS board          |

## Sources

All layouts were derived mechanically from upstream public headers (fetched with
`curl` from raw.githubusercontent.com), not re-typed:

- `STMicroelectronics/cmsis_device_f1` `Include/stm32f103xb.h`
- `STMicroelectronics/cmsis_device_f0` `Include/stm32f091xc.h` (all F0 structs) and
  `Include/stm32f072xb.h` (only `USB_TypeDef`, which the F091 header lacks)
- `ARM-software/CMSIS_5` `CMSIS/Core/Include/core_cm3.h` and `core_cm0.h`

The conversion removed `__IO/__I/__O/__IOM/__IM/__OM/volatile/const`, `#include`s and
`#if` alternatives (the `#if` branch was kept; for `SCnSCB_Type` that is `ACTLR`
present, `__CM3_REV >= 0x200`), and flattened the `ITM_Type.PORT` union into
`uint32_t PORT[32]`. Member names, order, reserved padding and array sizes are
unchanged, so offsets are byte-identical to CMSIS. Instance base addresses in the
JSON were evaluated from the `*_BASE` / `#define X ((T *) ...)` macros in the same
headers.

## Header conventions (Ghidra `CParser`)

- Fundamental typedefs at the top: `uint8_t`, `uint16_t`, `uint32_t` (no `#include`).
- Plain `typedef struct { ... } NAME_TypeDef;`, no `volatile`, no unions, no bitfields,
  explicit array sizes. Core structs are named `*_Type` as in CMSIS (`SCB_Type`, ...).
- Every member has a `/* 0xNNN */` byte-offset comment; each struct ends with a
  `/* sizeof = 0x.. */` comment.
- Reserved padding keeps its CMSIS name (`RESERVED0[88]`, ...).
- Parse with Ghidra's `CParserUtils.parseHeaderFiles(...)` into a
  `StandAloneDataTypeManager` (note the capital "A" in Ghidra 12.x).

## JSON conventions

Each file is an array sorted by `base` of
`{"name", "base", "size", "type", "description"}`:

- `base`/`size` are integers; `size` is `sizeof(type)` (the struct footprint, not the
  peripheral's address window), or the real byte length for untyped regions.
- `type` is a TypeDef/Type name from the matching header, or `null` for raw regions
  (UID, FLASHSIZE, USB packet memory).
- Optional extra key `overlaps` lists other entries whose byte ranges intersect. These
  are deliberate CMSIS overlays; when applying types in Ghidra apply only one side:
  - F1/F0 `NVIC_Type` (0xE04 / 0x320 long) spans `SCB` and `CoreDebug` (F1).
  - F0 `DMA_TypeDef` includes the channel area as `RESERVED0[40]`; apply
    `DMA1_ChannelN` entries on top of (or instead of) the `DMA1` struct. Same for DMA2.
  - F0 `SYSCFG_TypeDef.RESERVED1[25]` covers `COMP1`/`COMP2` (`COMP_CSR` at +0x1C).
- Deliberately omitted: F1 `ADC12_COMMON` (CMSIS places `ADC_Common_TypeDef` on top of
  ADC1 at `0x40012400`), and the F0 legacy aliases `COMP`, `ADC`, `DAC`, `COMP12_COMMON`.
  `ADC_Common_TypeDef` is still defined in both headers. F0 `ADC1_COMMON` is at
  `0x40012708`.
- Per-instance availability on F0 is noted in `description` (F091 is the superset;
  e.g. USART5-8 and DMA2 are F091-only; `USB`/`USB_PMA` come from the F072 header and
  are absent on F091; `CAN` is absent on F051).

## Verification

`verify_headers.py` parses both headers with Ghidra and asserts struct sizes and key
member offsets against a table, checks every JSON `type` exists, `size` equals
`sizeof(type)`, names are unique, undeclared overlaps do not exist, and spot-checks
base addresses:

```
GHIDRA_INSTALL_DIR=/opt/ghidra_12.1.4_PUBLIC /opt/zt3-venv/bin/python \
    src/zt3re/data/hw/verify_headers.py [-v]
```

Known sizes worth remembering (from CMSIS, not guesses): F1 `TIM_TypeDef` is 0x54
(includes `OR` at 0x50), `CAN_TypeDef` is 0x2B0 (the CAN window is 0x400 but the last
filter bank register ends at 0x2B0), `RCC_TypeDef` F1 0x28, F0 0x38.

## GD32 clone caveats (from memory, not verified against GD manuals)

These headers describe the ST parts. GD32 clones keep the same base addresses and,
for most peripherals, the same register offsets, but differ in details:

- GD32F103 vs STM32F103: GPIO/AFIO/EXTI/TIM/USART/SPI/I2C/ADC/DMA/CAN/BKP/RTC/IWDG/WWDG/
  CRC offsets are believed identical. Likely differences: flash controller (FMC) wait
  states / page size / extra bits, GD-only RCC registers beyond 0x28 (e.g. an
  `RCC_ADDCTL` near 0xC0, absent from `RCC_TypeDef`), `DBGMCU->IDCODE` value, and bit
  semantics of I2C/ADC. USB device and CAN share SRAM as on ST.
- For an F0-class BMS that is actually a GD32 part, treat `stm32f0.h` as authoritative
  for ST F0 only; re-check RCC, FMC, ADC and USART against the GD32 user manual if
  decompiled offsets look off.


## Artery AT32

The STM32F1 / STM32F0 files above were an early guess. Identification result: `VCU` and `MCU`
= Artery AT32F415 (Cortex-M4F), `BMS` = STM32G0B1-class (G0B1/G0C1, Cortex-M0+). Evidence:
the zero ("reserved") slots of the VCU/MCU vector tables match the 92-slot table of
`startup_at32f415.s` exactly (21 reserved IRQ slots, 0 mismatches; AT32F413 has 10, F403A 19),
the MCU compares `DEBUG->IDCODE` (0xE0042000) with 0x700301C5, and the BMS vector table
(47 slots, reserved slots 4-10/12/13 only) equals `startup_stm32g0b1xx.s` with every literal-pool
peripheral base (EXTI 0x40021800, GPIO 0x50000000.., FDCAN1/2 0x40006400/0x40006800, SRAMCAN
0x4000B400, USART6 0x40013C00, ...) inside the G0B1 memory map. The vendor-SVD-generated files
below describe those parts and supersede `stm32f1.*` / `stm32f0.*` for these boards (which stay
in the tree, untouched).

| Files                                                                 | Chip                          | Boards    |
|-----------------------------------------------------------------------|-------------------------------|-----------|
| `at32f415.h`, `peripherals_at32f415.json`, `at32f415_registers.json`, `at32f415_irqs.json`, `at32f415_core.json` | Artery AT32F415, Cortex-M4F (150 MHz) | VCU, MCU |
| `stm32g0b1.h`, `peripherals_stm32g0b1.json`, `stm32g0b1_registers.json`, `stm32g0b1_irqs.json`, `stm32g0b1_core.json` | STM32G0B1 (G0B1/G0C1 class), Cortex-M0+ | BMS      |

### Sources and licences

Everything is generated by `tools/svd2hw.py` from the vendor CMSIS-SVD files, which are
copied unmodified into `svd/` together with the vendor startup file and the `IRQn_Type` enum
(`svd/SOURCES.md` lists upstream path, commit, md5 and licence of each input):

- `svd/AT32F415xx_v2.svd` - ArteryTek `AT32F415_Firmware_Library`
  (`utilities/.../at32_ide/SVD/AT32F415xx_v2.svd`, commit `773f887`), BSD-3-Clause
  (`svd/LICENSE.ArteryTek-BSD-3-Clause`; the SVD itself carries ARM's BSD-style header).
- `svd/STM32G0B1.svd` - ST's SVD v1.8 via `modm-io/cmsis-svd-stm32` (commit `e79021a`),
  Apache-2.0 (`svd/LICENSE.STMicroelectronics-Apache-2.0`, notice kept in the file).
- Cortex-M4F / M0+ core structs: flattened from ARM CMSIS (`core_cm4.h`, `core_cm0plus.h`),
  the same text as the core section of `stm32f1.h` / `stm32f0.h` plus `MPU_Type`/`FPU_Type`
  (M4) and `VTOR`/`MPU_Type` (M0+).

The Zt3 repository has no top-level `LICENSE` file; the three upstream licences are
permissive redistribution licences (BSD-3-Clause, Apache-2.0), so redistributing the
SVD copies with their licence texts is allowed.

### Regenerate

```
python3 tools/svd2hw.py --chip at32f415     # reads svd/AT32F415xx_v2.svd + svd/startup_at32f415.s + svd/at32f415_irqn.h
python3 tools/svd2hw.py --chip stm32g0b1    # reads svd/STM32G0B1.svd   + svd/startup_stm32g0b1xx.s + svd/stm32g0b1_irqn.h
python3 tools/svd2hw.py --selftest          # synthetic SVD: derivedFrom, dim arrays, clusters, 8/16-bit regs, aliases
```

Stdlib only (`xml.etree`). Other parts: `--svd X --chip NAME --core {m4f,m0plus}
[--irq-header H] [--startup S] [--out-dir D]`. The output is deterministic.

### File formats

- `<chip>.h` - same conventions as above (`uint8_t/uint16_t/uint32_t` typedefs, plain
  `typedef struct`, `/* 0xNNN */` offsets, `/* sizeof = 0x.. */`), one struct per distinct
  register layout. Struct names: `<GROUP>_Type` when several instances share one layout
  (`GPIO_Type`, `USART_Type`, `DMA_Type`), else the first instance's name (`TMR1_Type`,
  `ADC1_Type`, `TIM2_Type` for TIM2/3/4). Members are the SVD register names; a `PERIPH_`
  prefix carried by >= 70 % of a peripheral's registers (ST SVDs: `ADC_ISR`, `TIM1_CR1`) is
  stripped in the header only. Core structs keep their CMSIS names (`SysTick_Type`, `NVIC_Type`,
  `SCB_Type`, ...). `RESERVEDn` is padding.
- `peripherals_<chip>.json` - `[{name, base, size, type, description, source, block, group?,
  derivedFrom?, interrupts?, overlaps?}]` sorted by `base`; `size` is `sizeof(type)`,
  `block` the SVD address-block span, `source` is `svd`, `core` (SysTick/NVIC/SCB/MPU/...) or
  `extra` (regions not in the SVD: STM32G0 `UID`, `FLASHSIZE`, `PACKAGE_DATA`,
  `SRAMCAN_FDCAN1/2`). `overlaps` marks deliberate overlays (apply only one side in Ghidra).
- `<chip>_registers.json` - `{peripheral: {base, description, group, type, derivedFrom?,
  registers:[{name, offset, size, access, reset, description, member, in_struct, alias_of?,
  alternate_of?, fields:[{name, bitOffset, bitWidth, description, access?, enums?}]}]}}`.
  `name` is the SVD name, `member` the C member expression (`CTRL1`, `EXTICR[2]`), `offset`
  is relative to the peripheral base. Derived peripherals repeat the full register list.
- `<chip>_irqs.json` - `[{number, exception (= number + 16), name, description, handler,
  svd_name?, header_name?, peripherals?, sources, startup_reserved?}]`. `name` comes from the
  vendor startup file (so `<name>_IRQHandler` is the vector-table symbol), then the vendor
  header, then the SVD.
- `<chip>_core.json` - vector-table layout from the vendor startup file: `vector_table_slots`
  (AT32F415: 92, STM32G0B1: 47), `reserved_irq_numbers` and per-slot `name`/`reserved`.

### Caveats

- **Alias registers are not struct members** (the first/primary one is kept; the SVD
  "alternate" ones are listed in the registers JSON with `"in_struct": false` and
  `alias_of`): AT32F415 `TMR1/2/3/9/10.CM1_INPUT/CM2_INPUT` (vs `*_OUTPUT`),
  `USB_OTG_GLOBAL.GRXSTSR_Host` (vs `GRXSTSR_Device`), `GNPTXFSIZ` (vs `DIEPTXF0`);
  STM32G0B1 `TIMx.CCMRn_Input`, `TIM2.CNT_ALTERNATE5`, `ADC.CHSELR_1`, `USART1.CR1/ISR_FIFO_DISABLED`,
  `LPUART1.CR1/ISR_disabled`. Use the registers JSON to comment the dropped name.
- STM32G0B1 `SPI_Type` (and a few others) use the SVD's 16-bit register size, so members are
  `uint16_t` separated by 2 bytes of padding (sizeof 0x22, not CMSIS' 0x24).
- Overlays by design: CMSIS `NVIC_Type` (M4: 0xE04 bytes) spans `SCB`, `MPU` and `CoreDebug`;
  STM32G0B1 `SYSCFG` (0x100) contains `VREFBUF` (0x40010030) in its reserved hole.
- The AT32F415 SVD has an `NVIC` pseudo-peripheral at 0xE000E000 (ISER0/ICER0/.../IPR14); it is
  not a struct (the core structs cover it) but is kept in the registers JSON (`"core": true`).
- IRQ numbers: the AT32F415 SVD disagrees with the vendor header/startup (`ACC` = 72 and
  `OTGFS` = 77 in the SVD, but 72-74 are reserved in `startup_at32f415.s` and `OTGFS1` = 67,
  `OTGFS1_WKUP` = 42 exist only in the header). The header/startup numbers win; the SVD-only
  entries are flagged with `sources: ["svd"]`.
- STM32G0B1 SVD gaps: `DMAMUX` lists 7 request channels (device has 12), `DMA2` is derived
  from `DMA1` (7 channels), there is no AES/RNG (G0C1 only) and no SCB/NVIC. Per-instance
  register names of derived peripherals are inherited (e.g. `TIM3` shows `TIM2` registers even
  though TIM3 is 16-bit).
- `FDCAN2` is derived from `FDCAN1`, so its struct also covers `FDCAN_CONFIG`/`CKDIV` at +0x100,
  but the real `FDCAN_CONFIG` block exists once, at `0x40006500`.
- Memory-mapped data not in the SVDs (AT32F415 UID/flash-size/user-system-data areas) is not
  listed; the AT32F415 vendor library does not publish those addresses.

### Verification

`verify_artery.py` parses both headers with Ghidra (`CParserUtils`, `StandAloneDataTypeManager`),
asserts ~250 + ~220 hand-written struct sizes/member offsets, cross-checks *every* register of
the registers JSON against the parsed struct member offsets, asserts JSON `type`/`size`/overlap
rules and ~110 well-known base addresses, checks IRQ numbers and vector-table size, checks that
the zero (reserved) vector slots of all 12 VCU/MCU and 4 BMS images in `firmware/` equal the
reserved slots of the chip description, and runs `svd2hw.py --selftest`:

```
GHIDRA_INSTALL_DIR=/opt/ghidra_12.1.4_PUBLIC /opt/zt3-venv/bin/python \
    src/zt3re/data/hw/verify_artery.py [-v]
```
