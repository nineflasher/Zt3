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
