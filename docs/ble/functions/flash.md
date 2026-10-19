# BLE - `flash` functions

31 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`flash_region_0x18000_io_cb`](#flash_region_0x18000_io_cb) | 0x0C045CC0 | Stream callback: access up to 64 KB at flash offset 0x18000 through a RAM-patched flash routine |
| [`norflash_apply_dummy_cycles`](#norflash_apply_dummy_cycles) | 0x0C0882A0 | Program the per-device dummy-cycle byte into flash-IP REG_014[23:16] if it is non-zero |
| [`norflash_apply_protect_entry`](#norflash_apply_protect_entry) | 0x0C087CDC | Pick the largest protect-table entry clear of an address range and apply it |
| [`norflash_build_protect_table`](#norflash_build_protect_table) | 0x0C087A34 | Build the table mapping SR block-protect bits to protected address ranges |
| [`norflash_cache_invalidate_range`](#norflash_cache_invalidate_range) | 0x0C087D34 | Invalidate flash cache lines for an address range |
| [`norflash_delay_us`](#norflash_delay_us) | 0x0C0867D0 | Busy-wait a number of microseconds on the down-counting system timer at 0x40003004 |
| [`norflash_erase`](#norflash_erase) | 0x0C088F20 | Erase a 4 KiB, 32 KiB, 64 KiB or whole-chip region of a flash slot at an address |
| [`norflash_erase_checked`](#norflash_erase_checked) | 0x0C087464 | Erase a flash slot range after checking that no erase is suspended |
| [`norflash_erase_range`](#norflash_erase_range) | 0x0C086E08 | Erase a byte range of a flash slot with 4 KiB, 32 KiB or whole-chip erases |
| [`norflash_get_id`](#norflash_get_id) | 0x0C087394 | Copy up to 3 bytes of the detected JEDEC ID of flash device 0/1 into a caller buffer |
| [`norflash_memcpy_thunk`](#norflash_memcpy_thunk) | 0x0C089498 | Tail-call veneer to newlib memcpy used by the flash-id getter |
| [`norflash_page_program`](#norflash_page_program) | 0x0C089064 | Program up to one 256-byte page of a flash slot, with dual or quad input opcodes when enabled |
| [`norflash_post_operation`](#norflash_post_operation) | 0x0C0888D8 | Finish a NOR flash command: re-enter continuous-read mode if enabled, end command mode, restore read clock divider |
| [`norflash_post_operation_alt`](#norflash_post_operation_alt) | 0x0C088928 | Duplicate of norflash_post_operation: re-enter continuous read, clear command mode, restore read divider |
| [`norflash_pre_operation`](#norflash_pre_operation) | 0x0C088858 | Prepare the NOR flash for a command: wait idle, apply the command clock divider, leave continuous-read mode |
| [`norflash_pre_operation_alt`](#norflash_pre_operation_alt) | 0x0C088898 | Duplicate of norflash_pre_operation: wait idle, set command clock divider, exit continuous-read mode |
| [`norflash_probe_protect_layout`](#norflash_probe_protect_layout) | 0x0C087D70 | Probe a flash slot's JEDEC ID and build its block-protect table |
| [`norflash_program_range`](#norflash_program_range) | 0x0C086F38 | Program a byte range of a flash slot page by page, with suspend and resume state |
| [`norflash_read_jedec_id`](#norflash_read_jedec_id) | 0x0C0889D8 | Read up to 3 bytes of the flash JEDEC ID (opcode 0x9F) for a slot into a caller buffer |
| [`norflash_reset`](#norflash_reset) | 0x0C08856C | Wake, soft-reset (0x66/0x99) and re-initialise a NOR flash device and clear its driver state |
| [`norflash_restore_read_config`](#norflash_restore_read_config) | 0x0C088350 | Re-arm continuous read (if the device supports it), release the controller and re-apply dummy cycles |
| [`norflash_sample_delay_calib`](#norflash_sample_delay_calib) | 0x0C088BB8 | Scan the flash-IP sample-delay settings, pick the middle of the window that reads back correctly |
| [`norflash_set_burst_wrap`](#norflash_set_burst_wrap) | 0x0C088474 | Write the flash burst-wrap command (0x77, payload 0x40 or 0x10) and update REG_038 for a slot |
| [`norflash_set_continuous_read`](#norflash_set_continuous_read) | 0x0C0882CC | Enable or disable continuous (XIP mode-byte) read: program read opcode and reset the flash's mode bits |
| [`norflash_set_read_mode`](#norflash_set_read_mode) | 0x0C08866C | Decode and apply a flash read-mode word: read opcode, lane width, continuous read, burst wrap |
| [`norflash_slot_op_locked`](#norflash_slot_op_locked) | 0x0C0873EC | Run a flash slot callback with the flash bracketed and interrupts masked |
| [`norflash_status_reg_op`](#norflash_status_reg_op) | 0x0C089190 | Chip status-register operation: raw write, quad-enable bit, security-register lock bits or block-protect bits |
| [`norflash_status_s0_s7`](#norflash_status_s0_s7) | 0x0C0883A0 | Issue Read Status Register-1 (0x05) and return the status byte from the RX FIFO |
| [`norflash_status_s8_s15`](#norflash_status_s8_s15) | 0x0C0883C8 | Issue Read Status Register-2 (0x35) and return the status byte from the RX FIFO |
| [`norflash_wait_busy_or_suspend`](#norflash_wait_busy_or_suspend) | 0x0C0883F0 | Poll status WIP until the flash is idle; if an IRQ becomes pending, send Program/Erase Suspend (0x75) |
| [`norflash_write_reg`](#norflash_write_reg) | 0x0C088978 | Write-enable, send a register-write command with data bytes, then poll RDSR until WIP clears |

## flash_region_0x18000_io_cb

**Stream callback: access up to 64 KB at flash offset 0x18000 through a RAM-patched flash routine**

Context struct: +0xc current offset, +0x10 pointer to a u16 selector. If *selector == 0 the access targets the non-cacheable flash alias 0x28018000 + offset and offset + length must not exceed 0x10000 (64 KB), otherwise -22 (-EINVAL) is returned; if the selector is non-zero only a zero-length access is accepted (offset + length must be 0). Then calls ble_ram_patch_thunk_20001d38 with (flash id 0, address, param_2 buffer, length, param_4) -- the signature of the BES hal_norflash read/write routines -- advances the offset by length and returns length. No direct callers (used as a function pointer).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | stream context: +0xc offset, +0x10 ptr to u16 selector |
| `param_2` | `ptr` | data buffer |
| `param_3` | `u32` | length in bytes |
| `param_4` | `u32` | passed through to the flash routine |

**Returns** `s32`: bytes transferred, or -22 (-EINVAL) on range violation

**Notes:** Whether the patched routine reads or writes, and what lives at flash offset 0x18000, is unknown.

- Addresses by version: 219: 0x0C045CC0
- Calls: `ble_ram_patch_thunk_20001d38`
- Confidence: low

## norflash_apply_dummy_cycles

**Program the per-device dummy-cycle byte into flash-IP REG_014[23:16] if it is non-zero**

Selects a per-flash-id byte: (&DAT_20003904)[id] when bit 0 of the device flag word at 0x2000390c + id*4 is set, otherwise (&DAT_20003900)[id]. If the byte is zero nothing is done; otherwise norflaship_set_cfg14_byte2 (FUN_0c087838) writes it into bits 16..23 of the flash-IP config register REG_014 (the decompiler drops the argument). Part of the norflash driver state group (per-id tables at 0x200038fc..0x2000391c, reset by norflash_reset ble_219_0c08856c). Callers: ble_219_0c088350, ble_219_0c08866c, ble_219_0c0888d8, ble_219_0c088928.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | flash device id, 0 or 1 |

**Notes:** That REG_014[23:16] is the dummy-cycle count (and that bit 0 of the flag word selects an alternate read mode) is inferred from the surrounding read-mode code, not from documentation.

- Addresses by version: 219: 0x0C0882A0
- Called by: `norflash_restore_read_config`, `norflash_set_read_mode`, `norflash_post_operation`, `norflash_post_operation_alt`
- Calls: `norflaship_set_cfg14_byte2`
- Confidence: low

## norflash_apply_protect_entry

**Pick the largest protect-table entry clear of an address range and apply it**

Works on flash slot 0 only (any other id hangs). If the protect table has entries (count at 0x200038C0), it walks the 3-word entries at 0x200035C0 (SR code, range start, range end). It skips entries that overlap [addr, addr+len) and keeps the largest of the rest, then calls norflash_slot_op_locked (0x0C0873EC) with that entry's SR code. If the call fails it hangs. If no entry qualifies, the initial code 0x7C is left and the function hangs.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash slot id (must be 0) |
| `param_2` | `u32` | start address |
| `param_3` | `u32` | length in bytes |
| `param_4` | `u32` | extra argument, passed through |

**Notes:** The meaning of the SR code and of the entry ordering is inferred from the layout built by norflash_probe_protect_layout.

- Addresses by version: 219: 0x0C087CDC
- Called by: `ble_219_0c088128`
- Calls: `norflash_slot_op_locked`
- Confidence: medium

## norflash_build_protect_table

**Build the table mapping SR block-protect bits to protected address ranges**

Generates, for a NOR flash of size param_2 bytes, an array of 12-byte entries {status_register_value, range_start, range_end} at 0x200035C0 and stores the entry count in 0x200038C0. Entry 0 is {0,0,0} (no protection) and entry 1 is {0x7C,0,size-1} (everything protected). It then loops over the power-of-two block sizes (4 KiB doubling, or 8 KiB when the flag in 0x200038C4[param_1] is set, up to 32 KiB) producing top/bottom-aligned ranges for the BP bits (value n*4), the TB bit 0x40 and the CMP bit 0x4000, as used by SPI NOR status register block protection. The table is later searched to pick the status-register value that protects a given region. Only param_1 == 0 is handled; any other value spins forever. param_1 also indexes the variant flag array at 0x200038C4.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash instance (must be 0, otherwise infinite loop) |
| `param_2` | `u32` | flash size in bytes |

**Notes:** Entry layout read from the stores; semantic interpretation (BP/TB/CMP) is inferred from the 4*n / 0x40 / 0x4000 patterns.

- Addresses by version: 219: 0x0C087A34
- Called by: `norflash_probe_protect_layout`
- Confidence: medium

## norflash_cache_invalidate_range

**Invalidate flash cache lines for an address range**

param_1 selects a flash window: 0 -> addresses in 0x2C000000..0x2FFFFFFF, 1 -> 0x34000000..0x37FFFFFF (any other value spins forever). If the address param_2 is outside the selected window the function returns param_1 and does nothing. For length param_3 > 0xFE0 it writes 1 to 0x07FFA038 (invalidate the whole cache) and returns 0. Otherwise it aligns param_2 down to 32 bytes and, for each 32-byte line up to param_2+param_3, writes the line address to 0x07FFA014 and 1 to 0x07FFA018 (single-line invalidate trigger). Returns 0 on success.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | flash/cache window selector, 0 or 1 |
| `param_2` | `u32` | start address |
| `param_3` | `u32` | length in bytes |

**Returns** `s32`: 0 when handled, param_1 (non-zero) when the address is outside the window

**Notes:** Cache controller registers at 0x07FFA0xx are decompiler-reported (Ghidra PIC warning); peripheral semantics inferred.

- Addresses by version: 219: 0x0C087D34
- Called by: `ble_219_0c088128`
- Confidence: medium

## norflash_delay_us

**Busy-wait a number of microseconds on the down-counting system timer at 0x40003004**

Reads the timer value register 0x40003004, obtains the timer clock from ble_get_ram_var_20003540_div4 (0x20003540 >> 2, treated as Hz) and spins until (start - now) >= param_1 * (clock / 100000) / 10, i.e. param_1 microseconds of timer ticks. The timer counts down so start - now is the elapsed count. Used by the flash driver for the tRES1 wake-up (40 us after 0xAB), reset recovery (200 us after 0x99) and suspend latency (40 us after 0x75): callers ble_219_0c0883f0, ble_219_0c08856c, ble_219_0c088f20, ble_219_0c089064.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | delay in microseconds |

- Addresses by version: 219: 0x0C0867D0
- Peripheral registers: `0x40003004` (R)
- Called by: `norflash_wait_busy_or_suspend`, `norflash_reset`, `norflash_erase`, `norflash_page_program`
- Calls: `ble_get_ram_var_20003540_div4`
- Confidence: medium

## norflash_erase

**Erase a 4 KiB, 32 KiB, 64 KiB or whole-chip region of a flash slot at an address**

Maps the erase kind param_3 to an opcode: 1 = 0x20 (4 KiB sector), 2 = 0x52 (32 KiB block), 3 = 0xD8 (64 KiB block), 4 = 0x60 (chip erase); any other value returns 0xF without touching hardware. If the descriptor capability word has bit 19 set and the cached read mode is mode-based (0x20) or opcode-based quad (0x10), that read mode is left first (REG_014 bit 4 cleared for 0x20, read opcode reset to 0x03 for 0x10) with the descriptor hook at +0x18 called as (slot, 1); a mirror block re-enters the mode after the erase. The sequence is Write Enable (norflaship_send_cmd_byte with 0x06), norflaship_set_reg30_top_byte(address), then the erase opcode with the address shifted into REG_000[31:8] by norflaship_send_cmd_byte. After norflaship_wait_idle, manufacturer byte 0x85 parts get a 400 us delay (norflash_delay_us(400)), then norflash_wait_busy_or_suspend(slot, param_4) polls completion. The mode is restored, REG_004 bit 0 is cleared, and the poll result is returned. This is part of the norflash driver group with norflash_page_program and norflash_set_read_mode.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | flash slot (0 or 1) |
| `param_2` | `u32` | flash address; the top byte goes to REG_030 and the low 24 bits to the command |
| `param_3` | `s32` | erase kind: 1 = 4 KiB, 2 = 32 KiB, 3 = 64 KiB, 4 = whole chip |
| `param_4` | `s32` | suspend-allowed flag passed to norflash_wait_busy_or_suspend |

**Returns** `u32`: 0 = erase finished, 1 = suspended by a pending interrupt, 0xF = invalid erase kind

**Notes:** Opcodes are the standard JEDEC erase commands. The bit-19 mode exit/re-entry and the 0x85 delay gate are inferred from the code shape. 0x85 is the PUYA JEDEC code, unverified. For chip erase the address is still shifted in, which the chip-erase opcode presumably ignores.

- Addresses by version: 219: 0x0C088F20
- Called by: `norflash_erase_range`
- Calls: `norflash_delay_us`, `norflaship_send_cmd_byte`, `norflaship_ctrl_clear_bit0`, `norflaship_wait_idle`, `norflaship_set_cfg14_bit4`, `norflaship_set_reg30_top_byte`, `norflaship_set_reg20_byte2`, `norflash_wait_busy_or_suspend`
- Confidence: medium

## norflash_erase_checked

**Erase a flash slot range after checking that no erase is suspended**

Public erase entry. An id above 1, or an uninitialised slot, hangs in an infinite loop (a trap in the binary). If an erase is already suspended (state byte 0x200035B0[id] non-zero) it returns 10. Otherwise it calls ble_slot_get_field_0x14 (0x0C088520) for its side effect, then norflash_erase_range (0x0C086E08) with a zero extra argument and returns that result.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash slot id (0 or 1) |
| `param_2` | `u32` | start address |
| `param_3` | `u32` | length in bytes |

**Returns** `s32`: result of norflash_erase_range, or 10 when an erase is suspended

**Notes:** The result of ble_slot_get_field_0x14 is not used by this function in the decompile.

- Addresses by version: 219: 0x0C087464
- Called by: `ble_219_0c088128`
- Calls: `norflash_erase_range`, `ble_slot_get_field_0x14`
- Confidence: medium

## norflash_erase_range

**Erase a byte range of a flash slot with 4 KiB, 32 KiB or whole-chip erases**

Checks the start address against the slot size at 0x20003568 + id*0x24 (returns 0x0B if the start is out of range, 0x0C if the length runs past the end) and rounds the start down and the end up to 4 KiB. It calls norflash_pre_operation (0x0C088858), then erases: if the range covers the whole chip it issues one whole-chip norflash_erase (kind 4, 0x0C088F20); otherwise it issues 4 KiB sector erases (kind 1) until the address is 32 KiB aligned, 32 KiB block erases (kind 2) while at least 0x8000 bytes remain, and 4 KiB erases for the tail. norflash_post_operation (0x0C0888D8) runs at the end. If an erase reports 1 (suspended), the progress is saved in 0x20003598[id] (address) and 0x200035A8[id] (remaining length), the state byte at 0x200035B0[id] is set to 2, and the function returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash slot id (0 or 1) |
| `param_2` | `u32` | start address, low 26 bits used |
| `param_3` | `u32` | length in bytes |
| `param_4` | `ptr` | extra argument passed to the flash operations |

**Returns** `s32`: 0 when complete, 1 when suspended with progress saved, 0x0B or 0x0C for a bad range, otherwise the error from the erase

**Notes:** The erase kind mapping (1 = 4 KiB, 2 = 32 KiB, 4 = whole chip) comes from norflash_erase (0x0C088F20).

- Addresses by version: 219: 0x0C086E08
- Called by: `norflash_erase_checked`
- Calls: `norflash_pre_operation`, `norflash_post_operation`, `norflash_erase`
- Confidence: medium

## norflash_get_id

**Copy up to 3 bytes of the detected JEDEC ID of flash device 0/1 into a caller buffer**

BES norflash_drv style accessor. Halts in an infinite loop (assert) if the flash id param_1 > 1. Clamps the length to 3 and copies via FUN_0c089498 (memcpy-like thunk: dst=param_2, src, len) from the per-device context entry at 0x20003550 + id*0x24, offset 1, where the 3-byte JEDEC id (manufacturer, memory type, capacity) was stored by the probe routine. Always returns 0. Called by ble_219_0c087d70.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash device id, 0 or 1 |
| `param_2` | `ptr` | destination buffer for the id bytes |
| `param_3` | `u32` | bytes to copy, clamped to 3 |

**Returns** `u32`: always 0

**Notes:** Assumes FUN_0c089498 is memcpy(dst, src, n); if the argument order were reversed this would be a set-id function.

- Addresses by version: 219: 0x0C087394
- Called by: `norflash_probe_protect_layout`
- Calls: `norflash_memcpy_thunk`
- Confidence: medium

## norflash_memcpy_thunk

**Tail-call veneer to newlib memcpy used by the flash-id getter**

Five-instruction wrapper that forwards its three register arguments unchanged to memcpy (0c0709bc) and returns. The only caller is 0c087394 (hal_norflash_get_id style: copies min(len, 3) JEDEC id bytes from the per-instance flash state at 0x20003551 + id*0x24 into the caller's buffer). Probably a long-branch veneer or patch hook between the flash driver and libc; it adds no logic. The decompiler shows one parameter, but r1 (source) and r2 (length) pass through untouched.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination buffer (r0); r1 = source, r2 = byte count are forwarded unchanged |

- Addresses by version: 219: 0x0C089498
- Called by: `norflash_get_id`
- Calls: `memcpy`
- Confidence: high

## norflash_page_program

**Program up to one 256-byte page of a flash slot, with dual or quad input opcodes when enabled**

Programs one page of a flash slot. Lengths above 256 bytes return 2 immediately. The opcode comes from the cached read-mode word DAT_2000390C[slot]: 0x32 (quad input page program) when lane bit 0x40000 is set, 0xA2 (dual input page program) when 0x20000 is set, otherwise 0x02 (page program). The TX FIFO is cleared and the first chunk is loaded by norflaship_set_len_and_fill_txfifo, which also sets the transfer length; then Write Enable (0x06) is sent, norflaship_set_reg30_top_byte(address) is written, and the program opcode with the address in REG_000[31:8] is issued by norflaship_send_cmd_byte. Remaining data is pushed by repeated norflaship_fill_txfifo calls as FIFO space frees up. After norflaship_wait_idle, manufacturer byte 0x85 parts get a 450 us settle delay (norflash_delay_us(0x1c2)), norflash_wait_busy_or_suspend(slot, param_5) polls completion, REG_004 bit 0 is cleared, and the poll result is returned.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | flash slot (0 or 1) |
| `param_2` | `u32` | page start address (24-bit) |
| `param_3` | `ptr` | source data buffer |
| `param_4` | `u32` | byte count, 0..256 |
| `param_5` | `s32` | suspend-allowed flag passed to norflash_wait_busy_or_suspend |

**Returns** `u32`: 0 = programmed, 1 = suspended by a pending interrupt, 2 = length above 256

**Notes:** 0xA2 as dual input page program is inferred. It is not a JEDEC-standard opcode but several SPI NOR vendors use it. The 0x85 delay is a guess at PUYA parts, and its length check reads the post-loop variable, which is unclear in the decompile.

- Addresses by version: 219: 0x0C089064
- Called by: `norflash_program_range`
- Calls: `norflash_delay_us`, `norflaship_set_len_and_fill_txfifo`, `norflaship_fill_txfifo`, `norflaship_send_cmd_byte`, `norflaship_ctrl_clear_bit0`, `norflaship_wait_idle`, `norflaship_clear_txfifo`, `norflaship_set_reg30_top_byte`, `norflash_wait_busy_or_suspend`
- Confidence: medium

## norflash_post_operation

**Finish a NOR flash command: re-enter continuous-read mode if enabled, end command mode, restore read clock divider**

BES norflash_drv 'post operation' hook run after erase (0c086e08) and program (0c086f38) sequences; the extra arguments at the call sites are register leftovers, the real signature is (id). Calls norflaship_wait_idle, then if the op-mode word 0x2000390c[id] has bit 12 (0x1000, continuous read mode) set it sets REG_004 bit 25 (norflaship_ctrl_set_bit25), writes the chip's 'continuous read enable' mode byte (byte +5 of the flash config record selected via 0x20003908[id] -> pointer table 0x2000306c) into REG_004[11:4] with norflaship_set_ctrl_field_4_11, and waits idle again, so the next memory-mapped read re-arms XIP mode. It then clears REG_004 bit 0 (norflaship_ctrl_clear_bit0, leaves the explicit command/data-phase mode) and calls 0c0882a0, which restores the read-path clock divider (0x20003904[id] when op-mode bit0 standard SPI is set, else 0x20003900[id]) into REG_014[23:16]. Always returns 0. Counterpart of norflash_pre_operation; 0c088928 and 0c088350 are identical clones.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash instance id (0 or 1); indexes 0x20003908 and 0x2000390c |

**Returns** `u32`: always 0

**Notes:** The record table at 0x2000306c is what earlier waves called the 'slot record' (ble_slot_get_* accessors); from this group it is the per-chip NOR flash config entry (3 JEDEC id bytes at +0, crm enable/disable mode bytes at +5/+6, 16-bit fields at +8/+0x0a, supported-mode mask at +0x14, callback at +0x18).

- Addresses by version: 219: 0x0C0888D8
- Called by: `norflash_erase_range`, `norflash_program_range`
- Calls: `norflaship_set_ctrl_field_4_11`, `norflaship_ctrl_set_bit25`, `norflaship_ctrl_clear_bit0`, `norflaship_wait_idle`, `norflash_apply_dummy_cycles`
- Confidence: medium

## norflash_post_operation_alt

**Duplicate of norflash_post_operation: re-enter continuous read, clear command mode, restore read divider**

Byte-for-byte copy of norflash_post_operation (0c0888d8); only caller is 0c0873ec, which uses it together with norflash_pre_operation_alt around the status-register callback (op 4, block protection write). Steps: norflaship_wait_idle; if 0x2000390c[id] bit 12 (continuous read mode) is set, set REG_004 bit 25, put the chip config's crm-enable mode byte (+5 of the record found via 0x20003908[id] and the pointer table 0x2000306c) into REG_004[11:4], wait idle; then norflaship_ctrl_clear_bit0 (leave command mode) and 0c0882a0 (re-program the read clock divider byte 0x20003900/0x20003904[id] into REG_014[23:16]). Returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash instance id (0 or 1); indexes 0x20003908 and 0x2000390c |

**Returns** `u32`: always 0

**Notes:** Identical code to 0c0888d8 and 0c088350.

- Addresses by version: 219: 0x0C088928
- Called by: `norflash_slot_op_locked`
- Calls: `norflaship_set_ctrl_field_4_11`, `norflaship_ctrl_set_bit25`, `norflaship_ctrl_clear_bit0`, `norflaship_wait_idle`, `norflash_apply_dummy_cycles`
- Confidence: medium

## norflash_pre_operation

**Prepare the NOR flash for a command: wait idle, apply the command clock divider, leave continuous-read mode**

BES hal_norflash/norflash_drv style 'pre operation' hook run before erase and program sequences (callers 0c086e08 = erase and 0c086f38 = write; the trailing arguments the decompiler shows at the call sites are register leftovers, the real signature is (id)). Calls norflaship_wait_idle, then if the per-instance byte at 0x200038fc[id] (clock divider used for command/program/erase traffic) is non-zero writes it with norflaship_set_cfg14_byte2 (REG_014[23:16]). It then reads the active op-mode word 0x2000390c[id] (bit layout of the BES HAL_NORFLASH_OP_MODE enum: bit0..5 SPI/fast/dual-out/dual-IO/quad-out/quad-IO, bit12 continuous read, bit14 high performance, bit16..18 page/dual/quad program) and if bit 12 (0x1000, continuous read mode) is set calls 0c0882cc(id, 0), which clears control bit 25, loads the chip's 'continuous read disable' mode byte (chip config +6) and issues a 0xBB/0xEB I/O read so the flash leaves its XIP/continuous-read state before plain commands are sent. Always returns 0; the matching counterpart is norflash_post_operation (0c0888d8). 0c088898 is a byte-identical duplicate used by the status-register path.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash instance id (0 or 1); indexes 0x200038fc and 0x2000390c |

**Returns** `u32`: always 0

**Notes:** The second argument of the norflaship_set_cfg14_byte2 call is dropped by the decompiler; from the load pattern it is the byte 0x200038fc[id]. Divider interpretation of REG_014[23:16] inferred from the three per-mode divider byte arrays (0x200038fc, 0x20003900, 0x20003904).

- Addresses by version: 219: 0x0C088858
- Called by: `norflash_erase_range`, `norflash_program_range`
- Calls: `norflaship_wait_idle`, `norflaship_set_cfg14_byte2`, `norflash_set_continuous_read`
- Confidence: medium

## norflash_pre_operation_alt

**Duplicate of norflash_pre_operation: wait idle, set command clock divider, exit continuous-read mode**

Byte-for-byte copy of norflash_pre_operation (0c088858), emitted separately (compiler clone) for the status-register write path: its only caller is 0c0873ec, which brackets the chip status-register callback (ble_slot_invoke_callback_evt4 -> op 4) with this function and norflash_post_operation_alt (0c088928) inside an IRQ-disabled section. Sequence: norflaship_wait_idle; if the divider byte 0x200038fc[id] is non-zero program it into REG_014[23:16] via norflaship_set_cfg14_byte2; if op-mode word 0x2000390c[id] has bit 12 (0x1000, HAL_NORFLASH_OP_MODE_CONTINUOUS_READ) set call 0c0882cc(id, 0) to take the flash out of continuous-read mode (clear REG_004 bit25, send the chip's crm-disable mode byte from config +6 with a 0xBB dual-I/O or 0xEB quad-I/O read). Returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash instance id (0 or 1); indexes 0x200038fc and 0x2000390c |

**Returns** `u32`: always 0

**Notes:** Identical code to 0c088858; kept as a separate family because it is a distinct function in the image.

- Addresses by version: 219: 0x0C088898
- Called by: `norflash_slot_op_locked`
- Calls: `norflaship_wait_idle`, `norflaship_set_cfg14_byte2`, `norflash_set_continuous_read`
- Confidence: medium

## norflash_probe_protect_layout

**Probe a flash slot's JEDEC ID and build its block-protect table**

Runs once per slot, while the flag at 0x200038C4[id] is clear. It reads the first three JEDEC ID bytes with norflash_get_id (0x0C087394) and selects a block-protect layout. Two manufacturer and type patterns are built inline (0xC8 with 0x40 and capacity code 0x12..0x13, and 0x0B with 0x60 and 0x14), writing 3-word entries (SR code, start, end) at 0x200035C0 and the entry count at 0x200038C0. For other IDs it calls the generic builder norflash_build_protect_table (0x0C087A34) when the capacity lies between 64 KiB and just under 32 MiB. The value that norflash_get_id sets at 0x200038C4 scales the block sizes. Unrecognised sizes return or hang.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash slot id (0 or 1) |
| `param_2` | `u32` | flash capacity in bytes |

**Notes:** The vendor patterns are matched by the decompiled comparisons only, with no datasheet check. The layout of the table entries is inferred.

- Addresses by version: 219: 0x0C087D70
- Calls: `norflash_get_id`, `norflash_build_protect_table`
- Confidence: low

## norflash_program_range

**Program a byte range of a flash slot page by page, with suspend and resume state**

Checks the start address against the slot size at 0x20003568 + id*0x24 (returns 0x0B) and that the length fits (returns 0x0C). It then programs in pieces that stop at page boundaries, each no larger than the page size at 0x2000356C + id*0x24, by calling norflash_page_program (0x0C089064) and advancing the flash address, the source buffer and the remaining length. norflash_pre_operation and norflash_post_operation bracket the loop. A suspended result (1) saves the address, buffer and remaining length in 0x20003598, 0x200035A0 and 0x200035A8 (indexed by id) and sets the state byte at 0x200035B0[id] to 4.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash slot id (0 or 1) |
| `param_2` | `u32` | start address, low 26 bits used |
| `param_3` | `ptr` | source buffer |
| `param_4` | `u32` | length in bytes |
| `param_5` | `u32` | extra argument passed to the page program |

**Returns** `s32`: 0 when complete, 1 when suspended with progress saved, 0x0B or 0x0C for a bad range, otherwise the page-program error

- Addresses by version: 219: 0x0C086F38
- Calls: `norflash_pre_operation`, `norflash_post_operation`, `norflash_page_program`
- Confidence: medium

## norflash_read_jedec_id

**Read up to 3 bytes of the flash JEDEC ID (opcode 0x9F) for a slot into a caller buffer**

Issues the RDID command 0x9F to a flash slot. If the cached read-mode word DAT_2000390C[slot] has continuous read (bit 12) it is turned off with norflash_set_continuous_read(slot, 0), and if the per-slot byte at 0x200038FC is set REG_014[23:16] is reprogrammed by norflaship_set_cfg14_byte2. After norflaship_wait_idle and norflaship_clear_fifos, the command is started with norflaship_send_cmd_ext(slot, 0x9F, 0, n, param_4) where n = min(param_3, 3), then norflaship_wait_fifo_level(n) waits for n bytes in the RX FIFO. The bytes are read one at a time from REG_010 by norflaship_read_rxfifo_byte into param_2[0..n-1]; for a standard RDID these are manufacturer, memory type and capacity. norflash_restore_read_config then re-arms continuous read and dummy cycles. With param_3 == 0 the command is still issued but no bytes are read, and the function always returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | flash slot (0 or 1) |
| `param_2` | `ptr` | destination buffer, at least 3 bytes |
| `param_3` | `u32` | requested byte count, clamped to 3 |
| `param_4` | `u32` | passed as the trailing argument of norflaship_send_cmd_ext |

**Returns** `u32`: always 0

**Notes:** The decompiled call to norflaship_send_cmd_ext has five arguments (slot, 0x9F, 0, n, param_4), while the wave-1 summary lists four. The mapping of n to the length field is taken from the read loop, so the trailing argument is unverified. The byte order of the ID is assumed from the JEDEC RDID convention.

- Addresses by version: 219: 0x0C0889D8
- Calls: `norflaship_read_rxfifo_byte`, `norflaship_send_cmd_ext`, `norflaship_wait_fifo_level`, `norflaship_wait_idle`, `norflaship_clear_fifos`, `norflaship_set_cfg14_byte2`, `norflash_set_continuous_read`, `norflash_restore_read_config`
- Confidence: medium

## norflash_reset

**Wake, soft-reset (0x66/0x99) and re-initialise a NOR flash device and clear its driver state**

BES norflash_drv reset sequence for device id: clear FIFOs, send 0xAB (Release Power-Down), wait 40 us; reset the flash-IP configuration (config REG_014 bits 3/4/5 cleared, REG_040 bits 2..3 cleared, REG_020[7:0] set to 0xEB via the norflaship_set_* thunks), clear ctrl bit 25 (continuous read) and wait idle; fill the TX FIFO with the 4 bytes at DAT_20003068 and send command 0xFF with length 4 (mode-bit reset / exit continuous-read in any width), clear ctrl bit 0 and the RX FIFO; send 0x66 (Enable Reset) and 0x99 (Reset Device), wait 200 us (tRST), then 0xE9 (Exit 4-byte address mode) and clear ctrl bit 0. Finally zeroes the per-id driver state: bytes (&DAT_20003900)[id], (&DAT_20003908)[id] (flash descriptor index), (&DAT_20003904)[id], (&DAT_200038fc)[id], the u32 flag word at 0x2000390c + id*4 and (&DAT_20003914)[id]. No direct callers (reached through the flash open/probe path). Head of the norflash driver state group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | flash device id, 0 or 1 |

**Notes:** Which of the five set_cfg14/reg40/reg20 thunks receives the 0xEB argument is read from the call order (FUN_0c087944), not confirmed.

- Addresses by version: 219: 0x0C08856C
- Calls: `norflash_delay_us`, `norflaship_ctrl_clear_bit25`, `norflaship_set_len_and_fill_txfifo`, `norflaship_send_cmd_byte`, `norflaship_send_cmd_word`, `norflaship_ctrl_clear_bit0`, `norflaship_wait_idle`, `norflaship_clear_fifos`, `norflaship_clear_rxfifo`, `norflaship_set_cfg14_bit5`, `norflaship_set_cfg14_bit4`, `norflaship_set_cfg14_bit3`, `norflaship_set_reg20_byte0`, `norflaship_set_reg40_bits2_3`
- Confidence: medium

## norflash_restore_read_config

**Re-arm continuous read (if the device supports it), release the controller and re-apply dummy cycles**

Waits for the flash IP to go idle, then if bit 12 of the device flag word at 0x2000390c + id*4 is set re-enables continuous read: norflaship_ctrl_set_bit25, programs the continuous-read opcode (descriptor byte +5 via DAT_2000306c[DAT_20003908[id]]) into REG_004[11:4] and waits idle again. Then norflaship_ctrl_clear_bit0 (FUN_0c087774, ends the command phase) and norflash_apply_dummy_cycles (ble_219_0c0882a0). Returns 0. Used after a suspend/resume or a mode switch by ble_219_0c0889d8 to put the controller back into the configured read mode. Part of the norflash driver group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | flash device id |

**Returns** `u32`: always 0

**Notes:** Bit 12 of the flag word is interpreted as 'continuous read currently enabled'; exact meaning not verified.

- Addresses by version: 219: 0x0C088350
- Called by: `norflash_read_jedec_id`
- Calls: `norflaship_set_ctrl_field_4_11`, `norflaship_ctrl_set_bit25`, `norflaship_ctrl_clear_bit0`, `norflaship_wait_idle`, `norflash_apply_dummy_cycles`
- Confidence: low

## norflash_sample_delay_calib

**Scan the flash-IP sample-delay settings, pick the middle of the window that reads back correctly**

BES-style NOR flash sample delay calibration for instance param_1. Reads the clock divider REG_014[23:16] (norflaship_get_cfg14_byte2); 0 means the controller is not set up and -1 is returned. The number of candidates is 4 when the divider is 1 (delay table 0x20003114, 4 bytes) and 11 otherwise (table 0x20003118, 11 bytes). For each candidate i it stores i in 0x20003918[id], writes table[i] into REG_014[15:12] (norflaship_set_cfg14_nibble3) and tests the link according to param_2: mode 0 sends 0x9F (JEDEC Read ID), reads 3 bytes and compares them with the 3 id bytes at the start of the chip's config record (0x2000306c[0x20003908[id]]); mode 1 (only id 0/1, otherwise an endless assert loop) clears the RX FIFO and checks that the memory-mapped word at 0x28000000 (id 0) or 0x30000000 (id 1) equals the BES boot-struct magic 0xBE57EC1C; mode 2 (id 0 only) compares 12 words read from 0x1C0030E4 against a reference pattern starting 0xF0F0F0F0 (0x20003124..0x20003150). It records the first passing index and counts consecutive passes, stopping at the first failure after a pass. With no passing index it returns 1. Otherwise the chosen index is first + count/2, except when exactly 2 passed: with divider 1 it is 1 (or first+1 if first >= 2); with divider 2 the preferred index is 4 if the flag 0x20003914[id] is set else 3, with larger dividers 5, used if it lies in [first, first+1], else first+1. The chosen index is stored in 0x20003918[id] and its table value re-applied to REG_014[15:12]. Returns 0 on success.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash instance id (0 or 1) |
| `param_2` | `u32` | verification method: 0 = JEDEC id, 1 = boot magic 0xBE57EC1C at flash start, other = 48-byte pattern at 0x1C0030E4 |

**Returns** `s32`: 0 = calibrated, 1 = no sample delay worked, -1 = clock divider is 0

**Notes:** Interpretation of REG_014[15:12] as sample delay and [23:16] as divider is inferred from usage. Meaning of the flag byte 0x20003914[id] (biases the choice at divider 2) and of the 0x1C0030E4 pattern region is not established.

- Addresses by version: 219: 0x0C088BB8
- Calls: `norflaship_read_rxfifo_byte`, `norflaship_send_cmd_ext`, `norflaship_wait_fifo_level`, `norflaship_wait_idle`, `norflaship_clear_fifos`, `norflaship_clear_rxfifo`, `norflaship_get_cfg14_byte2`, `norflaship_set_cfg14_nibble3`
- Confidence: medium

## norflash_set_burst_wrap

**Write the flash burst-wrap command (0x77, payload 0x40 or 0x10) and update REG_038 for a slot**

Programs the flash burst-wrap setting with opcode 0x77 (Set Burst with Wrap, used by Winbond/GigaDevice-style SPI NOR parts) and a one-byte payload: 0x40 when param_2 is 0x20 (wrap on) or 0x10 when param_2 is 0 (wrap off); any other param_2 returns immediately. The payload is pushed into the TX FIFO after norflaship_clear_txfifo and norflaship_set_len_and_fill_txfifo, the command goes out as norflaship_send_cmd_byte(0x77, 0), and norflash_wait_busy_or_suspend(slot, 0) polls WIP to completion. For capacities above 16 MiB with manufacturer byte 0xC8 at descriptor offset 0, REG_014 bit 3 is cleared around the command and set again afterwards. REG_038 is then updated: param_2 == 0 clears bit 12, otherwise REG_038[14:13] is programmed from width 0x20 and bit 12 is set, and bit 0 is always set last. This is the only caller path from norflash_set_read_mode (ble_219_0c08866c), part of the norflash driver group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | flash slot (0 or 1) |
| `param_2` | `s32` | 0 = wrap off (payload 0x10), 0x20 = wrap on (payload 0x40), other values ignored |

**Notes:** The 0x77 opcode and the 0x10/0x40 payload meanings are inferred from SPI NOR convention, not verified against a datasheet. The 0xC8 gate for >16 MiB parts is a guess at GigaDevice devices.

- Addresses by version: 219: 0x0C088474
- Called by: `norflash_set_read_mode`
- Calls: `norflaship_set_len_and_fill_txfifo`, `norflaship_send_cmd_byte`, `norflaship_clear_txfifo`, `norflaship_set_cfg14_bit3`, `norflaship_set_cfg38_width_sel`, `norflaship_cfg38_set_bit12`, `norflaship_cfg38_clear_bit12`, `norflaship_cfg38_set_bit0`, `norflash_wait_busy_or_suspend`
- Confidence: medium

## norflash_set_continuous_read

**Enable or disable continuous (XIP mode-byte) read: program read opcode and reset the flash's mode bits**

param_2 != 0: norflaship_ctrl_set_bit25 (continuous-read enable), program the device's continuous-read opcode (byte +5 of the flash descriptor found via DAT_2000306c[DAT_20003908[id]]) into REG_004[11:4] with norflaship_set_ctrl_field_4_11, then norflaship_wait_idle. param_2 == 0: norflaship_ctrl_clear_bit25, program the normal read opcode (descriptor byte +6); if the device flag word 0x2000390c[id] has bit 5 (quad I/O) choose opcode 0xEB, else if bit 3 (dual I/O) 0xBB, else just wait idle and return. For quad/dual devices it clears the RX FIFO, sets the transfer length to 2 and issues the read opcode with operand 0 (norflaship_send_cmd_byte), i.e. a dummy read whose mode byte M7..M0 = 0x00 takes the flash out of continuous-read mode, then clears the RX FIFO and waits idle. Group: norflash driver read-mode control; callers ble_219_0c08866c, ble_219_0c088858, ble_219_0c088898, ble_219_0c0889d8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | flash device id |
| `param_2` | `s32` | non-zero = enable continuous read, 0 = disable and reset mode bits |

**Notes:** REG_004 bit 25 is assumed to be the continuous-read / mode-byte enable; descriptor byte offsets 5/6 are assumed to be the read opcodes with and without continuous mode.

- Addresses by version: 219: 0x0C0882CC
- Called by: `norflash_set_read_mode`, `norflash_pre_operation`, `norflash_pre_operation_alt`, `norflash_read_jedec_id`
- Calls: `norflaship_set_ctrl_field_4_11`, `norflaship_ctrl_clear_bit25`, `norflaship_ctrl_set_bit25`, `norflaship_set_xfer_len`, `norflaship_send_cmd_byte`, `norflaship_wait_idle`, `norflaship_clear_rxfifo`
- Confidence: medium

## norflash_set_read_mode

**Decode and apply a flash read-mode word: read opcode, lane width, continuous read, burst wrap**

Masks the requested mode word param_2 with the device capability word at descriptor +0x14 (descriptor = DAT_2000306c[DAT_20003908[slot]]) and decodes it into a read selector (0x20 quad I/O, 0x10 quad output, 0x08 dual I/O, 0x04 dual output, 0x02 fast read, 0x01 normal read) and a lane width (0x40000 quad, 0x20000 dual, 0x10000 single). Continuous read (0x1000) is honoured only with selector 0x20 or 0x08, and burst wrap (0x4000) only with 0x20; unsupported combinations return 1 without touching hardware. If the normalised word differs from the cached word DAT_2000390C[slot], continuous read is turned off first via norflash_set_continuous_read when the device supports it, REG_014 bits 4 and 5 are cleared, and the new selector is applied: 0x20 sets REG_014 bit 4 (and norflaship_set_reg108(8) when descriptor bit 29 is set), 0x08 sets REG_014 bit 5, and the others write opcode 0x6B, 0x3B, 0x0B or 0x03 into REG_020[23:16]. Continuous read then loads the descriptor byte +5 into REG_004[11:4] with bit 25 set, and a wrap change calls norflash_set_burst_wrap and toggles BLE control bit 1 via ble_hw_ctrl_reg_bit1_set/clear (effective for slot 0 only). The cache is stored, REG_004 bit 0 is cleared, dummy cycles are re-applied, and the function returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | flash slot (0 or 1) |
| `param_2` | `u32` | requested read-mode word: selector in bits 0..5, lane width in 16..18, 0x1000 continuous read, 0x4000 burst wrap |
| `param_3` | `u32` | not used by the decompiled body |
| `param_4` | `u32` | passed through as the trailing argument of norflash_set_continuous_read |

**Returns** `u32`: 0 = mode applied, 1 = unsupported mode combination

**Notes:** Selector-to-opcode mapping follows the standard JEDEC read opcodes. The 0x20/0x08 meanings (quad/dual I/O via REG_014 bits 4/5) agree with the wave-2 notes on norflash_set_continuous_read. The 0x4000 wrap toggle reaches BLE control bit 1 only for slot 0.

- Addresses by version: 219: 0x0C08866C
- Calls: `ble_hw_ctrl_reg_bit1_set`, `ble_hw_ctrl_reg_bit1_clear`, `norflaship_set_ctrl_field_4_11`, `norflaship_ctrl_set_bit25`, `norflaship_ctrl_clear_bit0`, `norflaship_wait_idle`, `norflaship_set_cfg14_bit5`, `norflaship_set_cfg14_bit4`, `norflaship_set_reg20_byte2`, `norflaship_set_reg108`, `norflash_apply_dummy_cycles`, `norflash_set_continuous_read`, `norflash_set_burst_wrap`
- Confidence: medium

## norflash_slot_op_locked

**Run a flash slot callback with the flash bracketed and interrupts masked**

Rejects an id above 1, or a slot whose initialised flag at 0x20003550[id*0x24] is clear, with 0x12. It brackets the slot callback with norflash_pre_operation_alt (0x0C088898) and norflash_post_operation_alt (0x0C088928), with ble_slot_invoke_callback_evt4 (0x0C08915C) in between. Interrupts are masked with disableIRQinterrupts unless the privileged-mode check reports them already masked. In the masked branch it first writes a debug marker, the return address 0x0C08742E and the link register, to 0x20003D78 and 0x20003D7C, clears the marker afterwards and re-enables interrupts. Returns 0 on success or 10 when the callback fails.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash slot id (0 or 1) |
| `param_2` | `u32` | argument passed to the slot callback |

**Returns** `u32`: 0 on success, 10 (0x0A) when the callback fails, 0x12 for a bad id or uninitialised slot

**Notes:** The interpretation of the isIRQinterruptsEnabled result is taken from the branch sense in the code. The debug words suggest a crash-diagnostic marker, which is inferred.

- Addresses by version: 219: 0x0C0873EC
- Called by: `norflash_apply_protect_entry`, `ble_219_0c088128`
- Calls: `norflash_pre_operation_alt`, `norflash_post_operation_alt`, `ble_slot_invoke_callback_evt4`
- Confidence: medium

## norflash_status_reg_op

**Chip status-register operation: raw write, quad-enable bit, security-register lock bits or block-protect bits**

Status register manipulation handler for the NOR flash config layer; it has no direct caller and its (id, op, value) signature matches the callback at offset 0x18 of the chip config record invoked by ble_slot_invoke_callback_evt4 (op 4, from the block-protection path 0c0873ec) and by 0c08866c (op 1, when a quad mode is selected), so it is most likely that callback. It reads the supported-mode mask (ble_slot_get_field_0x14) and treats bits 0x30 (quad output / quad IO) as 'chip has a second status register'. op 0: write value as the raw status word (1 byte, or 2 bytes when quad) with the volatile write enable. Otherwise it reads SR1 with 0x05 (0c0883a0). op 3/4: block protection - mask = ble_slot_get_u16_at_0x08 (low byte for SR1, high byte for SR2), SR1 = (SR1 & ~m) | (value & m); if quad, SR2 is read with 0x35 and merged the same way with value >> 8; op 3 uses 0x06 WREN (non-volatile), op 4 uses 0x50 (volatile). op 1: set (value != 0) or clear bit 1 of SR2 (QE, quad enable, S9) and write both bytes volatile. op 2 (and any other): lock security registers - the 16-bit field ble_slot_get_u16_at_0x0a must have bit 0 set (else return 2); its bits 11:10 select the lock-bit layout 0 = S11..S13 (value < 8), 1 = S10 (value == 1), 2 = S10..S13 (value < 16), 3 = S12..S13 (value < 4), else return 4; an out-of-range value returns 3; the bits are merged into SR2 and written with the non-volatile 0x06 enable. All writes go through norflash_write_reg with opcode 0x01 (WRSR). Returns 0 on success.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash instance id |
| `param_2` | `u32` | operation: 0 raw status write, 1 quad-enable, 2 security register lock, 3 block protect (non-volatile), 4 block protect (volatile) |
| `param_3` | `u32` | value: status word, QE flag, lock-bit mask or block-protect bits (SR1 low byte, SR2 high byte) |

**Returns** `u32`: 0 ok, 2 security registers unsupported, 3 bad lock mask, 4 unknown lock layout

**Notes:** Being the +0x18 config callback is inferred from the signature and the op codes seen at the indirect call sites, not from a resolved pointer. Without quad support ops 1 and 2 degrade to rewriting SR1 unchanged.

- Addresses by version: 219: 0x0C089190
- Calls: `norflash_status_s0_s7`, `norflash_status_s8_s15`, `ble_slot_get_field_0x14`, `ble_slot_get_u16_at_0x0a`, `ble_slot_get_u16_at_0x08`, `norflash_write_reg`
- Confidence: medium

## norflash_status_s0_s7

**Issue Read Status Register-1 (0x05) and return the status byte from the RX FIFO**

Clears both flash-IP FIFOs (norflaship_clear_fifos), starts a transaction with command 0x05 (Read Status Register-1), 0 extra bytes and read length 1 (norflaship_send_cmd_ext), waits until the RX FIFO level reaches 1 (norflaship_wait_fifo_level) and reads the low byte of REG_010 (norflaship_read_rxfifo_byte). Bit 0 of the returned byte is WIP (write in progress), bit 1 WEL. The decompiler shows void but r0 carries the status byte. Sibling of norflash_status_s8_s15 (ble_219_0c0883c8); caller ble_219_0c089190 (status read / write-status path).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash device id |

- Addresses by version: 219: 0x0C0883A0
- Called by: `norflash_status_reg_op`
- Calls: `norflaship_read_rxfifo_byte`, `norflaship_send_cmd_ext`, `norflaship_wait_fifo_level`, `norflaship_clear_fifos`
- Confidence: high

## norflash_status_s8_s15

**Issue Read Status Register-2 (0x35) and return the status byte from the RX FIFO**

Identical to norflash_status_s0_s7 (ble_219_0c0883a0) but sends command 0x35 (Read Status Register-2, bits S8..S15, which holds the QE quad-enable bit on Winbond/GigaDevice parts): clear FIFOs, norflaship_send_cmd_ext(id, 0x35, 0, 1), wait for 1 byte in the RX FIFO, read it from REG_010. Result in r0. Caller ble_219_0c089190.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash device id |

- Addresses by version: 219: 0x0C0883C8
- Called by: `norflash_status_reg_op`
- Calls: `norflaship_read_rxfifo_byte`, `norflaship_send_cmd_ext`, `norflaship_wait_fifo_level`, `norflaship_clear_fifos`
- Confidence: high

## norflash_wait_busy_or_suspend

**Poll status WIP until the flash is idle; if an IRQ becomes pending, send Program/Erase Suspend (0x75)**

Loops reading status register 1 (clear FIFOs, command 0x05 with 1 read byte, wait FIFO level 1, read REG_010): when bit 0 (WIP) is clear returns 0. If param_2 (suspend allowed) is 0 it simply keeps polling. Otherwise, while busy it checks for pending interrupts: when the per-id flag (&DAT_2000391c)[id] is set it calls nvic_any_masked_irq_pending on the 3-word IRQ mask at 0x200038e4 + id*0xc, else ble_scb_irq_pending (any pending exception); as soon as one is pending it clears the FIFOs, issues 0x75 (Program/Erase Suspend) via norflaship_send_cmd_word, waits 40 us (norflash_delay_us(0x28), the suspend latency) and returns 1. Lets the caller service interrupts (e.g. the BT controller) during long erase/program operations. Callers ble_219_0c088474, ble_219_0c088f20, ble_219_0c089064.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | flash device id |
| `param_2` | `s32` | non-zero = allow suspending the operation when an IRQ is pending |

**Returns** `u32`: 0 = operation finished, 1 = operation suspended (status bit 0 still set)

- Addresses by version: 219: 0x0C0883F0
- Called by: `norflash_set_burst_wrap`, `norflash_erase`, `norflash_page_program`
- Calls: `ble_scb_irq_pending`, `nvic_any_masked_irq_pending`, `norflash_delay_us`, `norflaship_read_rxfifo_byte`, `norflaship_send_cmd_word`, `norflaship_send_cmd_ext`, `norflaship_wait_fifo_level`, `norflaship_clear_fifos`
- Confidence: medium

## norflash_write_reg

**Write-enable, send a register-write command with data bytes, then poll RDSR until WIP clears**

Low-level SPI NOR 'write register' helper (BES norflash_drv norflash_write_reg style). If param_2 == 0 it issues opcode 0x06 (WREN, non-volatile write enable) through norflaship_send_cmd_byte, otherwise opcode 0x50 (Volatile Status Register Write Enable) through norflaship_send_cmd_word with length 0. It then resets the TX FIFO (norflaship_clear_txfifo), programs the transfer length and pushes the param_5 bytes at param_4 into the TX FIFO (norflaship_set_len_and_fill_txfifo), and starts the transaction with opcode param_3 and length param_5 (norflaship_send_cmd_word). Finally it loops: clear both FIFOs, send 0x05 (Read Status Register-1) with 1 read byte via norflaship_send_cmd_ext, wait for one RX byte, read it, and repeat while bit 0 (WIP, write in progress) is set. No timeout. Only caller is norflash_status_reg_op (0c089190), which always passes opcode 1 (0x01 Write Status Register) and 1 or 2 data bytes.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash instance id |
| `param_2` | `u32` | 0 = use 0x06 WREN (non-volatile write), non-zero = use 0x50 volatile SR write enable |
| `param_3` | `u32` | register write opcode sent after the write-enable (0x01 WRSR from the only caller) |
| `param_4` | `ptr` | data bytes to send after the opcode |
| `param_5` | `u32` | number of data bytes (1 or 2) |

- Addresses by version: 219: 0x0C088978
- Called by: `norflash_status_reg_op`
- Calls: `norflaship_set_len_and_fill_txfifo`, `norflaship_read_rxfifo_byte`, `norflaship_send_cmd_byte`, `norflaship_send_cmd_word`, `norflaship_send_cmd_ext`, `norflaship_wait_fifo_level`, `norflaship_clear_fifos`, `norflaship_clear_txfifo`
- Confidence: high
