# VCU - `startup` functions

7 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`Reset_Handler`](#reset_handler) | 0x08001188 | Cortex-M reset vector: system init, C runtime init, then application main |
| [`SystemInit`](#systeminit) | 0x08008914 | Reset CRM to default clocks (HICK) and set VTOR to flash base (Artery SDK SystemInit) |
| [`__scatterload_decompress`](#__scatterload_decompress) | 0x08001710 | Decompress a packed section (literals, zero runs, back-references) into RAM |
| [`app_main_thunk`](#app_main_thunk) | 0x08001178 | Tail-call thunk that jumps to the application main entry FUN_0800d858 |
| [`crt_init_then_main`](#crt_init_then_main) | 0x080016EC | C runtime start: run the two-record init hook table, then call the app main thunk |
| [`crt_init_then_main_v148_14a`](#crt_init_then_main_v148_14a) | (removed) | Builds 148 and 14a start: run init hook table, call app main thunk, then divide loop |
| [`vcu_uid_load`](#vcu_uid_load) | 0x08007CA4 | Read the 96-bit chip unique ID and derive a ones-complement checksum |

## Reset_Handler

**Cortex-M reset vector: system init, C runtime init, then application main**

Reset entry (vector slot 1). Calls FUN_08008914 (clock / system initialisation, SystemInit-like), then FUN_080016ec (C-runtime init that copies/decompresses RAM sections and calls the main thunk), then FUN_0800d858 (application main) as a fallback if the runtime init ever returns. The initial stack pointer comes from vector slot 0 so the decompiler flags that SP may have been set. Startup group: Reset_Handler -> SystemInit-like -> scatter-load runtime -> app_main_thunk -> main.

**Notes:** The roles of FUN_08008914 as SystemInit and FUN_080016ec as scatterload/__main are inferred from order and callers.

- Addresses by version: 148: 0x08001188, 14a: 0x08001188, 14b: 0x08001188, 14e: 0x08001188, 14f: 0x08001188, 152: 0x08001188, 153: 0x08001188, 0159: 0x08001188
- Vector: `Reset_Handler`
- Confidence: high

## SystemInit

**Reset CRM to default clocks (HICK) and set VTOR to flash base (Artery SDK SystemInit)**

Matches the AT32F415 SDK SystemInit: sets CRM.APB1EN.PWCEN, ORs bit 2 into the byte at 0x40007050, clears PWCEN; sets CRM.CTRL.HICKEN and waits for HICKSTBL; selects HICK as SCLK (CRM.CFG &= ~3) and waits for CFG.SCLKSTS==0; clears HEXTEN/HEXTBYPS/CFDEN/PLLEN (CTRL &= 0xFEF2FFFF); then CRM.CFG=0, CRM.PLL=0x1F10, CRM.MISC1=0x100000, CRM.CLKINT=0x9F0000 and SCB->VTOR = 0x08000000 (FLASH_BASE, no offset). No direct caller: reached from the reset/startup code. Note VTOR points to 0x08000000 although the application image starts at 0x08001000.

**Notes:** VTOR value 0x08000000 looks like the SDK default VECT_TAB_OFFSET=0; the app may re-set VTOR later (not seen here).

- Addresses by version: 148: 0x08007EE0, 14a: 0x0800833C, 14b: 0x080086B4, 14e: 0x080086F4, 14f: 0x08008750, 152: 0x08008814, 153: 0x080088B0, 0159: 0x08008914
- Peripheral registers: `0x40007050` (RW), `CRM.CTRL` (RW), `CRM.CFG` (RW), `CRM.CLKINT` (W), `CRM.APB1EN` (RW), `CRM.PLL` (W), `CRM.MISC1` (W), `SCB+0x8` (W)
- Confidence: high

## __scatterload_decompress

**Decompress a packed section (literals, zero runs, back-references) into RAM**

Decompressor used by the Keil/ARM scatter-loader for compressed RW sections (no direct callers; it is invoked through a pointer from the load-region table, hence the indirect call). Each token starts with a header byte: low 3 bits give the literal count + 1 (if zero the next byte is the count), high nibble gives a run length (if zero the next byte supplies it). Literals are copied, then if header bit 3 is set it copies run+2 bytes from dest minus the following offset byte (LZ77 back-reference), otherwise it writes run zero bytes. Loops until dest reaches dst+size. Always returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | compressed input stream |
| `param_2` | `ptr` | output buffer |
| `param_3` | `u32` | number of output bytes to produce |

**Returns** `u32`: always 0

**Notes:** Exact armlink compression scheme name (RLE vs LZ77 variant) not confirmed; token semantics derived directly from the code.

- Addresses by version: 148: 0x08001436, 14a: 0x08001436, 14b: 0x080016AC, 14e: 0x080016AC, 14f: 0x080016AC, 152: 0x080016F4, 153: 0x080016F4, 0159: 0x08001710
- Confidence: medium

## app_main_thunk

**Tail-call thunk that jumps to the application main entry FUN_0800d858**

Two-instruction veneer that just calls FUN_0800d858 and returns. It is called from the C-runtime init routine (vcu_0159_080016ec, the scatter-load / __main equivalent) as the last step, so FUN_0800d858 is the application main(). Reset_Handler also calls FUN_0800d858 directly as a fallback after the runtime init returns. The one indirect call listed by the harness is the branch into main. Part of the startup group together with Reset_Handler and the runtime init.

**Notes:** That 0x0800d858 is main() is inferred from the call order in Reset_Handler and the runtime init, not from a string or symbol.

- Addresses by version: 148: 0x08001178, 14a: 0x08001178, 14b: 0x08001178, 14e: 0x08001178, 14f: 0x08001178, 152: 0x08001178, 153: 0x08001178, 0159: 0x08001178
- Called by: `crt_init_then_main`
- Confidence: medium

## crt_init_then_main

**C runtime start: run the two-record init hook table, then call the app main thunk**

Runtime start called from the reset path after the clocks are set up. It walks the two-entry table at 0x0800F294 to 0x0800F2B4, calling each record as fn(a, b, c) with its three stored arguments. It then calls thunk_FUN_0800d858 (app_main_thunk, the application main entry) and never returns: the decompiler marks the following bad-instruction halt. This routine does not parse a scatter table or copy RAM sections itself, so the earlier description of Reset_Handler as copying RAM sections only holds if the hook records do that work.

**Notes:** Callee names come from the existing app_main_thunk and Reset_Handler annotations. The hook records were not decoded in this packet.

- Addresses by version: 14b: 0x080013DC, 14e: 0x080013DC, 14f: 0x080013DC, 152: 0x080016D0, 153: 0x080016D0, 0159: 0x080016EC
- Calls: `app_main_thunk`
- Confidence: medium

## crt_init_then_main_v148_14a

**Builds 148 and 14a start: run init hook table, call app main thunk, then divide loop**

Present only in builds 148 and 14a, with no direct callers, so it is an entry point reached by pointer or from reset. It runs the two-record hook table at 0x0800E70C, calling each record as fn(a, b, c) with the three stored arguments, the same pattern as vcu_0159_080016ec. It then calls thunk_FUN_0800ce08, which the family map names app_main_thunk. The decompiler shows a 64-bit shift-and-subtract loop after that call, using FUN_080012F4 and FUN_08001312 as shift helpers and returning the quotient in r0:r1 like vcu_0159_080011ac. The operands come from registers the decompiler could not follow, so the loop may be a decompiler artifact.

**Returns** `u64`: loop quotient in r0:r1 (only reached if the main thunk returns)

**Notes:** Open questions: whether thunk_FUN_0800ce08 returns; the names of FUN_080012f4, FUN_08001312 and thunk_FUN_0800ce08 are not established in this packet; the 14a table at 0x0800E70C is not verified against the 0159 table.

- Addresses by version: 148: 0x080013AC, 14a: 0x080013A0
- Calls: `app_main_thunk`, `vcu_udiv64_shift_subtract`
- Confidence: low

## vcu_uid_load

**Read the 96-bit chip unique ID and derive a ones-complement checksum**

Copies the three device-ID words at 0x1FFFF7E8/EC/F0 into DAT_20002004/08/0c and again into DAT_20001c68/6c/70, then stores ~(w2 + w1 + w0) into DAT_20001028 (32-bit wrapping sum, inverted). The result is a per-device value later used by the application (e.g. as a serial/key seed or integrity check). Called once from the start-up/init routine 0x08009da8.

**Notes:** Consumer of 0x20001028 / 0x20001c68.. is outside this packet; 0x20001020 is only address-taken (probably the base of a struct holding the checksum).

- Addresses by version: 148: 0x08007278, 14a: 0x080076B4, 14b: 0x08007A18, 14e: 0x08007A50, 14f: 0x08007AAC, 152: 0x08007B70, 153: 0x08007C0C, 0159: 0x08007CA4
- Called by: `vcu_0159_08009da8`
- Confidence: high
