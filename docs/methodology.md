# Methodology

How the firmware set is analysed, and why the pipeline is shaped the way it is.  Every step below is
a `zt3` subcommand (see `README.md`), so the whole analysis can be rebuilt from `firmware/` alone.

## 1. Identification of the targets

| Component | Chip | Evidence |
|---|---|---|
| VCU (8 builds) | Artery AT32F415, Cortex-M4F | owner-confirmed; vector table matches `startup_at32f415.s` with 0 mismatches (92 slots, 21 reserved); all 19 referenced peripheral windows explained by the AT32F415 SVD; Thumb-2 integer code, no VFP use |
| MCU (4 builds) | Artery AT32F415 | same 92-slot vector pattern, 0 mismatches; reads `DEBUG->IDCODE` and compares with Artery's `0x700301C5`; ADC1/CAN1/TMR3/TMR4 handlers touch the matching bases |
| BMS (4 builds) | STM32G0B1-class, Cortex-M0+ | pure ARMv6-M (no 32-bit ALU encodings); 47-slot vector table matches `startup_stm32g0b1xx.s`; EXTI at `0x40021800`, GPIO on IOPORT `0x50000000`, FDCAN1/2 + message RAM at `0x4000B400`; image needs >64 KiB flash |
| BLE (1 build) | Bestechnic BES Bluetooth SoC, ARMv8-M (Cortex-M33 class) | `msr msplim`, `bxns`; `RAW4TFT` container header with MD5 of the payload (verified); pointer clustering puts the image at `0x0C028000`; strings name the BES SDK, BTstack, wolfSSL, FreeRTOS |

All MCU/VCU/BMS images are application images loaded at `0x08001000`; the 4 KiB below is a bootloader
that is not part of the dumps.  Loading them at `0x08000000` (the naive choice) decodes as garbage:
the vector table's handler addresses only land on `push {.., lr}` prologues at the +0x1000 offset.

## 2. Pipeline

```
firmware/*.bin ─ import ─► ghidra_project/ ─ match ─► analysis/matches/   (Ghidra Version Tracking)
                   │                        ─ export ─► analysis/export/   (functions, globals, tables, strings)
                   │                        ─ decompile ─► analysis/decomp/ (local cache)
                   └ data/hw (SVD-derived register structs, vector names)
analysis/{export,matches} ─ families ─► analysis/families/   (one id per logical function/variable across versions)
families + decomp ─ plan ─► analysis/work/<comp>/wave<N>_batch<M>.md   (work packets for annotation agents)
agents ─► annotations/<comp>/...  ─ validate / lint / check ─► apply (Ghidra) / docs (markdown)
```

* **import** relocates the image, builds the memory map, types the vector table and seeds a function at
  every handler before auto-analysis; then parses the vendor register header into the program so decompiled
  code shows `GPIOA->ODR`-style accesses.
* **match** runs Ghidra's Auto Version Tracking (exact bytes/instructions/mnemonics, duplicate-function and
  reference correlators) for adjacent versions and for every version against the newest.
* **families** merges those matches into one family per logical function.  VT leaves the smallest
  functions (median 3 instructions) unmatched, so a second, order-preserving pass aligns the remaining
  functions between the matched anchors (longest common subsequence on normalised instruction hashes).
  Variables and flash tables are aligned through matched functions: the k-th memory reference of two
  matched functions is the same variable.  A rebuild keeps previously issued ids.
* **plan** orders families bottom-up through the call graph (leaf functions first) so every packet shows
  the already-written summaries of its callees.
* **doctor** is the gate that keeps all of this honest: ownership (`MANIFEST.toml`), freshness stamps,
  orphan detection, literal/link checks in the docs.

## 3. Annotation rules

See `docs/annotation-guide.md`.  Descriptions are written once per family and applied to every version.
Every entry carries a confidence; `zt3 lint` refuses raw key or secret bytes in annotation text.
