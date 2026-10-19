# BLE - `util` functions

86 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`SEGGER_RTT_ConfigDownBuffer`](#segger_rtt_configdownbuffer) | 0x0C03FC74 | SEGGER RTT: configure one down buffer entry with a 'terminalN' name |
| [`SEGGER_RTT_ConfigUpBuffer`](#segger_rtt_configupbuffer) | 0x0C03FBF8 | SEGGER RTT: configure one up buffer entry with a 'terminalN' name |
| [`SEGGER_RTT_Init`](#segger_rtt_init) | 0x0C03F9D4 | Initialise the SEGGER RTT control block with one up and one down buffer |
| [`SEGGER_RTT_Read`](#segger_rtt_read) | 0x0C03FB00 | SEGGER RTT: read from a down buffer under the BASEPRI 0x40 lock (wraps SEGGER_RTT_ReadNoLock) |
| [`SEGGER_RTT_ReadNoLock`](#segger_rtt_readnolock) | 0x0C03FA40 | SEGGER RTT: read up to param_3 bytes from down buffer param_1 into param_2 without locking |
| [`SEGGER_RTT_SetTerminal`](#segger_rtt_setterminal) | 0x0C03FCFC | SEGGER RTT: switch the active virtual terminal of up-buffer 0 by sending the 0xFF,<id> escape |
| [`bes_image_format_name`](#bes_image_format_name) | 0x0C034818 | Return a name string for a section image-format magic value |
| [`ble_byte_count_notify`](#ble_byte_count_notify) | 0x0C047588 | Add a byte count to a running total and fire the registered notify callback |
| [`ble_chunked_write_24`](#ble_chunked_write_24) | 0x0C04585C | Write a buffer in 24-byte pieces through ble_219_0c033328; errors -5 or -8 |
| [`ble_clear_flag_2000bd18`](#ble_clear_flag_2000bd18) | 0x0C046CB4 | Clear the byte/word variable at 0x2000bd18 |
| [`ble_clock_realtime_offset_update`](#ble_clock_realtime_offset_update) | 0x0C04014C | Reset (param nonzero) or refresh the REALTIME offset from the monotonic clock |
| [`ble_debug_timestamp_print`](#ble_debug_timestamp_print) | 0x0C03FF38 | Print wall-clock seconds and nanoseconds with the hardware clock value |
| [`ble_get_ram_var_20003540_div4`](#ble_get_ram_var_20003540_div4) | 0x0C0866C0 | Return the global word at 0x20003540 shifted right by 2 |
| [`ble_get_var_2000f5fc`](#ble_get_var_2000f5fc) | 0x0C04757C | Return the 32-bit global at 0x2000f5fc |
| [`ble_mem_copy`](#ble_mem_copy) | 0x0C03AA40 | Wrapper around memcpy that returns 0 |
| [`ble_mem_fill`](#ble_mem_fill) | 0x0C03AA50 | Wrapper around memset that returns 0 |
| [`ble_nvdata0_dev_read_record`](#ble_nvdata0_dev_read_record) | 0x0C041D50 | Read the 120-byte record from /dev/nvdata0 into DAT_2000F354, opening it on first use |
| [`ble_nvdata0_dev_write_record`](#ble_nvdata0_dev_write_record) | 0x0C041DC0 | Write the 120-byte record from DAT_2000F354 to /dev/nvdata0, then issue control command 0x200 |
| [`ble_parse_csv_u8x4`](#ble_parse_csv_u8x4) | 0x0C055634 | Parse up to four comma-separated decimal fields into byte outputs |
| [`ble_parse_u8x3_bdaddr`](#ble_parse_u8x3_bdaddr) | 0x0C05569C | Parse three comma-separated decimal bytes and a trailing Bluetooth address |
| [`ble_pktq_enqueue`](#ble_pktq_enqueue) | 0x0C048A44 | Append a packet to the ble_pktq ring: copy the payload into the next slot |
| [`ble_pktq_init`](#ble_pktq_init) | 0x0C0489E8 | Initialise a packet ring of n+1 descriptor slots and create its recursive mutex |
| [`ble_random_fill_seeded`](#ble_random_fill_seeded) | 0x0C05B5C0 | Fill a buffer with param_2 random bytes from the unnamed generator, seeded by the tick count |
| [`ble_ring_append_with_mark`](#ble_ring_append_with_mark) | 0x0C028B90 | Append a payload to a BTstack ring buffer under a lock, optionally patching one marker byte |
| [`ble_set_var_2000f64c`](#ble_set_var_2000f64c) | 0x0C047634 | Store a 32-bit value in the global at 0x2000f64c, return 0 |
| [`ble_slot_identity_dump`](#ble_slot_identity_dump) | 0x0C05C7B6 | Print 15 bytes of the slot identity block in hex and return 1 |
| [`ble_slot_is_used_2000f4cc`](#ble_slot_is_used_2000f4cc) | 0x0C046F40 | Test whether entry N of the 32-bit table at 0x2000f4cc is non-zero |
| [`ble_stub_nop_0c04628c`](#ble_stub_nop_0c04628c) | 0x0C04628C | Empty function (immediate return) |
| [`ble_stub_nop_0c047f88`](#ble_stub_nop_0c047f88) | 0x0C047F88 | Empty function (immediate return) |
| [`ble_stub_nop_0c047fe8`](#ble_stub_nop_0c047fe8) | 0x0C047FE8 | Empty function (immediate return) |
| [`ble_transfer_chunks_64`](#ble_transfer_chunks_64) | 0x0C05C860 | Feed param_2 bytes from param_1 to 0c065C88 in pieces of at most 64 bytes |
| [`ble_uart_fmt_item`](#ble_uart_fmt_item) | 0x0C033114 | Format one value into a bounded buffer and return the number of bytes kept |
| [`ble_uart_print_values`](#ble_uart_print_values) | 0x0C033150 | Format up to N 1/2/4-byte values into one line and send it to UART0 by polling |
| [`ble_uart_print_values_thunk`](#ble_uart_print_values_thunk) | 0x0C033248 | Branch into ble_uart_print_values (single-instruction thunk, same arguments) |
| [`ble_util_hex_string_to_bytes`](#ble_util_hex_string_to_bytes) | 0x0C05AA80 | Parse n delimiter-separated hex byte fields from a string into a byte array |
| [`bt_bdaddr_from_string`](#bt_bdaddr_from_string) | 0x0C05AA0C | Parse six hex byte fields (e.g. "xx:xx:xx:xx:xx:xx") into a 6-byte address |
| [`bt_bytes_reverse_inplace`](#bt_bytes_reverse_inplace) | 0x0C05AA44 | Reverse len bytes in place via a 6-byte stack temp (generic BD_ADDR byte-order swap) |
| [`co_max_u32`](#co_max_u32) | 0x0C065C7C | Unsigned maximum of two values |
| [`co_min_u32`](#co_min_u32) | 0x0C065C74 | Unsigned minimum of two values |
| [`co_popcount32`](#co_popcount32) | 0x0C065DC0 | Count set bits in a 32-bit word |
| [`co_read16_be`](#co_read16_be) | 0x0C065B94 | Read unaligned big-endian u16 from base+offset |
| [`co_read16_le`](#co_read16_le) | 0x0C065B38 | Read unaligned little-endian u16 from base+offset |
| [`co_read32_be`](#co_read32_be) | 0x0C065BA0 | Read unaligned big-endian u32 from base+offset |
| [`co_read32_le`](#co_read32_le) | 0x0C065B44 | Read unaligned little-endian u32 from base+offset |
| [`co_reverse_copy_16`](#co_reverse_copy_16) | 0x0C065C38 | Copy 16 bytes from src to dst in reversed order |
| [`co_reverse_copy_32`](#co_reverse_copy_32) | 0x0C065C4C | Copy 32 bytes from src to dst in reversed order |
| [`co_reverse_copy_6`](#co_reverse_copy_6) | 0x0C065C60 | Copy 6 bytes from src to dst in reversed order |
| [`co_reverse_copy_7`](#co_reverse_copy_7) | 0x0C065C10 | Copy 7 bytes from src to dst in reversed order |
| [`co_reverse_copy_8`](#co_reverse_copy_8) | 0x0C065C24 | Copy 8 bytes from src to dst in reversed order |
| [`co_reverse_copy_n`](#co_reverse_copy_n) | 0x0C065BF8 | Copy n bytes from src to dst reversed |
| [`co_write16_be`](#co_write16_be) | 0x0C065BBC | Write u16 big-endian to base+offset |
| [`co_write16_le`](#co_write16_le) | 0x0C065B60 | Write u16 little-endian to base+offset |
| [`co_write32_be`](#co_write32_be) | 0x0C065BCC | Write u32 big-endian to base+offset |
| [`co_write32_le`](#co_write32_le) | 0x0C065B70 | Write u32 little-endian to base+offset |
| [`crc16_ccitt_nibble`](#crc16_ccitt_nibble) | 0x0C047644 | Table-driven CRC-16/CCITT (poly 0x1021, MSB first) over a buffer, 4 bits at a time |
| [`crc32_reflected_table`](#crc32_reflected_table) | 0x0C0476A0 | Table-driven reflected CRC-32 (poly 0xEDB88320) over a buffer |
| [`printf_hexdump`](#printf_hexdump) | 0x0C065C88 | Print a buffer as uppercase hex pairs separated by spaces, then a newline |
| [`ringbuf_contig_read_len`](#ringbuf_contig_read_len) | 0x0C043820 | Contiguous readable bytes from the read index to the buffer end or write index |
| [`ringbuf_contig_write_len`](#ringbuf_contig_write_len) | 0x0C0438C0 | Contiguous writable bytes from the write index, keeping one slot free |
| [`ringbuf_free_space`](#ringbuf_free_space) | 0x0C04352C | Free bytes in a circular buffer descriptor (read-1-write modulo size) |
| [`ringbuf_is_empty`](#ringbuf_is_empty) | 0x0C0437E0 | True when the ring's two indices are equal |
| [`ringbuf_is_full_with_reserve`](#ringbuf_is_full_with_reserve) | 0x0C0437F0 | True when free space is at most a reserve (4 bytes if flag bit0 set at +0x1c) |
| [`ringbuf_read_ptr`](#ringbuf_read_ptr) | 0x0C043818 | Address of the current read position (base + read index) |
| [`ringbuf_used_count`](#ringbuf_used_count) | 0x0C043540 | Number of bytes stored in a circular buffer descriptor |
| [`ringbuf_write_ptr`](#ringbuf_write_ptr) | 0x0C0438B8 | Address of the current write position (base + write index) |
| [`segger_rtt_write_blocking`](#segger_rtt_write_blocking) | 0x0C03F97C | SEGGER RTT _WriteBlocking: copy into an up buffer in chunks, spinning until all bytes are stored |
| [`segger_rtt_write_no_check`](#segger_rtt_write_no_check) | 0x0C03F934 | SEGGER RTT _WriteNoCheck: copy param_3 bytes into an up buffer at WrOff with wrap, no free-space check |
| [`segger_rtt_write_overwrite_nolock`](#segger_rtt_write_overwrite_nolock) | 0x0C03FB1C | Write NumBytes into RTT up-buffer n, overwriting the oldest unread data if it does not fit |
| [`stub_empty_0c037584`](#stub_empty_0c037584) | 0x0C037584 | Empty function (immediate return) |
| [`stub_empty_0c0398a8`](#stub_empty_0c0398a8) | 0x0C0398A8 | Empty function (immediate return) |
| [`stub_empty_0c03aa3c`](#stub_empty_0c03aa3c) | 0x0C03AA3C | Empty function (immediate return) |
| [`stub_empty_0c03aa60`](#stub_empty_0c03aa60) | 0x0C03AA60 | Empty function (immediate return) |
| [`stub_return_zero_0c0360c8`](#stub_return_zero_0c0360c8) | 0x0C0360C8 | Stub returning 0 |
| [`stub_return_zero_0c0360cc`](#stub_return_zero_0c0360cc) | 0x0C0360CC | Stub returning 0 |
| [`stub_return_zero_0c065144`](#stub_return_zero_0c065144) | 0x0C065144 | Stub that always returns 0 |
| [`trace_printf`](#trace_printf) | 0x0C035D0C | printf-style trace output into the trace object at 0x20003E30 (three variadic words) |
| [`trace_vprintf_core`](#trace_vprintf_core) | 0x0C035900 | Format a printf-style string to the trace output object, handling %c %d %u %x %p %s and %f |
| [`util_bytes16_to_hex`](#util_bytes16_to_hex) | 0x0C047F48 | Format 16 bytes as 32 lowercase hex characters with a NUL terminator |
| [`util_count_trailing_zeros32`](#util_count_trailing_zeros32) | 0x0C03ABA4 | Count trailing zero bits of a 32-bit word (RBIT + CLZ) |
| [`util_ctz32`](#util_ctz32) | 0x0C036024 | Count trailing zero bits of a 32-bit word (returns 32 for 0) |
| [`util_find_str_in_buf`](#util_find_str_in_buf) | 0x0C028898 | Find a NUL-terminated needle inside the first n bytes of a (non-terminated) buffer |
| [`util_nop_stub_a`](#util_nop_stub_a) | 0x0C065CDC | Empty stub function (returns immediately) |
| [`util_nop_stub_b`](#util_nop_stub_b) | 0x0C065CE0 | Empty stub function (returns immediately) |
| [`util_return_zero_u32`](#util_return_zero_u32) | 0x0C03FEA8 | Stub that returns 0 |
| [`util_return_zero_u64`](#util_return_zero_u64) | 0x0C03FEA0 | Stub that returns 0 in r0/r1 |
| [`util_sub_s32`](#util_sub_s32) | 0x0C065C84 | Return param_1 - param_2 |

## SEGGER_RTT_ConfigDownBuffer

**SEGGER RTT: configure one down buffer entry with a 'terminalN' name**

Same flow as SEGGER_RTT_ConfigUpBuffer for the down direction: initialises RTT on first use, formats 'terminal%d' on the stack, and when the index is below the down-buffer count in DAT_2000BE40 it stores the name, buffer, size, flags and cleared offsets into the down-buffer table. The table is laid out like the up table, starting one entry later (names at 0x2000BE48 plus 24 bytes per index). The update runs in a BASEPRI 0x40 section.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | buffer index |
| `param_2` | `ptr` | buffer memory |
| `param_3` | `u32` | buffer size in bytes |
| `param_4` | `u32` | flags (SEGGER RTT mode bits) |

**Returns** `s32`: index on success, -1 when the index is not below the down-buffer count

**Notes:** One buffer-pointer store is shown by the decompiler with a 12-byte index stride, which does not match the 24-byte stride of the other fields. Check that store against the disassembly. The stack-buffer name has the same dangling-pointer issue as the up variant.

- Addresses by version: 219: 0x0C03FC74
- Calls: `SEGGER_RTT_Init`, `ble_219_0c0715d8`
- Confidence: medium

## SEGGER_RTT_ConfigUpBuffer

**SEGGER RTT: configure one up buffer entry with a 'terminalN' name**

Initialises the RTT control block on first use by calling SEGGER_RTT_Init, then formats 'terminal%d' with the index into a stack buffer. If the index is below the up-buffer count in DAT_2000BE44, it fills that entry of the up-buffer table at 0x2000BFB0 (24-byte entries: name, buffer, size, write offset, read offset, flags), clears both offsets and returns the index. The update runs in a BASEPRI 0x40 section.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | buffer index |
| `param_2` | `ptr` | buffer memory |
| `param_3` | `u32` | buffer size in bytes |
| `param_4` | `u32` | flags (SEGGER RTT mode bits) |

**Returns** `s32`: index on success, -1 when the index is not below the up-buffer count

**Notes:** The name pointer stored in the table is the stack buffer auStack_2c, so it dangles after the function returns. Only the name is affected. The stack buffer is not a string literal as in the upstream SEGGER API.

- Addresses by version: 219: 0x0C03FBF8
- Calls: `SEGGER_RTT_Init`, `ble_219_0c0715d8`
- Confidence: high

## SEGGER_RTT_Init

**Initialise the SEGGER RTT control block with one up and one down buffer**

Fills the control block at 0x2000BE30: ID string 'SEGGER RTT' (bytes 0x47474553 'SEGG', 0x5245 'ER', 0x20, 0x545452 'RTT'), MaxNumUpBuffers = MaxNumDownBuffers = 0xF. Up buffer 0 at 0x2000BE48: name pointer 0x0c07688c (name string in flash), buffer at 0x2000C138, size 0x400, WrOff/RdOff/Flags = 0. Down buffer 0 at 0x2000BFB0: same name, buffer 0x2000C118, size 0x20, offsets/flags 0. Matches SEGGER_RTT_Init / _DoInit from the SEGGER RTT library. Called from the RTT read/write/up-buffer functions (0x0c03fa40, 0x0c03fbf8, 0x0c03fc74, 0x0c03fcfc) as lazy init.

- Addresses by version: 219: 0x0C03F9D4
- Called by: `SEGGER_RTT_ReadNoLock`, `SEGGER_RTT_ConfigUpBuffer`, `SEGGER_RTT_ConfigDownBuffer`, `SEGGER_RTT_SetTerminal`
- Confidence: high

## SEGGER_RTT_Read

**SEGGER RTT: read from a down buffer under the BASEPRI 0x40 lock (wraps SEGGER_RTT_ReadNoLock)**

SEGGER_RTT_LOCK equivalent: if running privileged it saves BASEPRI and sets it to 0x40, calls SEGGER_RTT_ReadNoLock(param_1, param_2, param_3) and restores the saved BASEPRI. The decompiler shows only two forwarded arguments; the third (buffer size, r2) passes through untouched. No direct callers were found (probably used by a debug console / shell task through a function pointer). Matches SEGGER_RTT_Read in SEGGER_RTT.c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | down-buffer index |
| `param_2` | `ptr` | destination buffer |

**Notes:** Return value is really u32 (bytes read) forwarded from SEGGER_RTT_ReadNoLock.

- Addresses by version: 219: 0x0C03FB00
- Calls: `SEGGER_RTT_ReadNoLock`
- Confidence: high

## SEGGER_RTT_ReadNoLock

**SEGGER RTT: read up to param_3 bytes from down buffer param_1 into param_2 without locking**

Lazily initialises the RTT control block (SEGGER_RTT_Init if the ID byte at 0x2000BE30 is 0). Uses the down-buffer array starting at 0x2000BFB0 (24-byte SEGGER_RTT_BUFFER_DOWN entries: pBuffer 0x2000BFB4, SizeOfBuffer 0x2000BFB8, WrOff 0x2000BFBC, RdOff 0x2000BFC0, indexed by param_1 * 6 words). If WrOff < RdOff (data wraps) it first copies min(param_3, SizeOfBuffer - RdOff) bytes from RdOff to the end, resets RdOff to 0 at the end, then copies up to WrOff bytes from the start; otherwise copies min(param_3, WrOff - RdOff) bytes. Updates RdOff and returns the number of bytes read (0 if nothing was available). Called by SEGGER_RTT_Read under the BASEPRI lock; matches SEGGER_RTT_ReadNoLock in SEGGER_RTT.c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | down-buffer index (0 is the only configured one) |
| `param_2` | `ptr` | destination |
| `param_3` | `u32` | destination size |

**Returns** `u32`: bytes copied

- Addresses by version: 219: 0x0C03FA40
- Called by: `SEGGER_RTT_Read`
- Calls: `SEGGER_RTT_Init`, `memcpy`
- Confidence: high

## SEGGER_RTT_SetTerminal

**SEGGER RTT: switch the active virtual terminal of up-buffer 0 by sending the 0xFF,<id> escape**

Identical to SEGGER_RTT_SetTerminal(TerminalId). Lazily runs SEGGER_RTT_Init when acID[0] at 0x2000BE30 is still 0 (the INIT() macro). Rejects TerminalId >= 16, otherwise builds the two-byte escape {0xFF, _aTerminalId[TerminalId]} where _aTerminalId is the string '0123456789ABCDEF'. Under SEGGER_RTT_LOCK (BASEPRI raised to 0x40, old value restored afterwards) it looks at up buffer 0 (0x2000BE48, Flags at 0x2000BE5C): if the mode bits (Flags & 3) are SEGGER_RTT_MODE_BLOCK_IF_FIFO_FULL (2) it stores _ActiveTerminal (byte 0x2000BE2F) and calls _WriteBlocking (0x0c03f97c); otherwise it computes _GetAvailWriteSpace from WrOff/RdOff/SizeOfBuffer (0x2000BE54/58/50) and, if at least 2 bytes are free, stores _ActiveTerminal and calls _WriteNoCheck (0x0c03f934, 2 bytes), else fails. Returns 0 on success, -1 on invalid terminal or full buffer. No direct callers (called from the trace/printf back-end, probably via SEGGER_RTT_TerminalOut-style code).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | TerminalId 0..15 |

**Returns** `s32`: 0 on success, -1 (0xffffffff) if TerminalId >= 16 or the buffer cannot take 2 bytes

**Notes:** 0x0c03f934 = _WriteNoCheck, 0x0c03f97c = _WriteBlocking (SEGGER_RTT.c statics).

- Addresses by version: 219: 0x0C03FCFC
- Calls: `segger_rtt_write_no_check`, `segger_rtt_write_blocking`, `SEGGER_RTT_Init`
- Confidence: high

## bes_image_format_name

**Return a name string for a section image-format magic value**

Maps a 32-bit ASCII magic to a text label: 0x4d494152 ("RAIM") -> "romfs", 0x20574152 ("RAW ") -> "raw", 0x34574152 ("RAW4") -> "raw4k", 0x50495a47 ("GZIP") -> "gzip", anything else -> "unknwon" (sic, typo in firmware). Used by the code at 0x0c03655c/0x0c0365a4 when printing the format of an image/partition record.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | format magic (little-endian four-character tag) |

**Returns** `ptr`: constant C string

**Notes:** Calling context (boot image / romfs section dump) inferred from the labels only.

- Addresses by version: 219: 0x0C034818
- Called by: `nb_upgrade_print_image_info`, `nb_upgrade_check_image_header`
- Confidence: medium

## ble_byte_count_notify

**Add a byte count to a running total and fire the registered notify callback**

If the optional count hook at 0x2000F60C is set, it is called with no arguments and its return value replaces the count. A positive count is added to the 32-bit running total at 0x2000F644, and if the listener record at 0x2000F64C has a callback at +4, the function evaluates total*1000 divided by the value at 0x2000F648 through __divdi3 (FUN_0C06FE20) and then calls that callback with no arguments. The quotient is not used in the decompiled code, so either the division is dead or the decompile is incomplete. The function returns the possibly replaced count.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | not used by the decompiled body |
| `param_2` | `s32` | byte count; replaced by the hook result when the hook is set |

**Returns** `s32`: the count after the optional hook

- Addresses by version: 219: 0x0C047588
- Called by: `nb_upgrade_process_cmd`
- Calls: `__divdi3`
- Confidence: low

## ble_chunked_write_24

**Write a buffer in 24-byte pieces through ble_219_0c033328; errors -5 or -8**

Writes param_2 bytes from param_1 by calling ble_219_0c033328 (not described here) for pieces of at most 0x18 (24) bytes, advancing the offset until the buffer is done. It returns 0 when every piece succeeds. A NULL buffer or zero length returns 0xFFFFFFFB, and a non-zero result from the piece writer stops the loop and returns 0xFFFFFFF8. It does not retry.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | buffer to write |
| `param_2` | `u32` | buffer length in bytes |

**Returns** `u32`: 0 on success, 0xFFFFFFFB for bad arguments, 0xFFFFFFF8 when a piece fails

**Notes:** The device behind ble_219_0c033328 is unknown, so the destination is not described. The two error codes are kept as raw values.

- Addresses by version: 219: 0x0C04585C
- Called by: `ble_host_init_identity_addr`, `wc_rng_seed_instantiate`, `wc_RNG_GenerateBlock`
- Calls: `hsm_trng_read_bytes`
- Confidence: medium

## ble_clear_flag_2000bd18

**Clear the byte/word variable at 0x2000bd18**

Writes 0 to the global DAT_2000bd18 and returns. Called from ble_219_0c02c49c, so it acts as a reset of a state flag/counter owned by that caller; the variable's exact meaning is not visible from this function alone.

- Addresses by version: 219: 0x0C046CB4
- Called by: `ble_factory_test_dispatch_set`
- Confidence: medium

## ble_clock_realtime_offset_update

**Reset (param nonzero) or refresh the REALTIME offset from the monotonic clock**

Companion of clock_settime that maintains the same offset words DAT_2000C5E0 and DAT_2000C5E4. With param_1 nonzero it sets the offset to 0 minus the current monotonic seconds, using the zero-return stub 0x0C03FEA0 as the base, so REALTIME reads zero at this instant. With param_1 zero it reads CLOCK_MONOTONIC through clock_gettime, rounds to the nearest second (adds one when tv_nsec exceeds 500 ms), adds the stored offset and passes the 64-bit result to the zero-return stub 0x0C03FEA8. Its caller is 0x0C047FEC, which is outside this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | nonzero resets the offset so REALTIME restarts at zero; zero refreshes it |

**Notes:** The base value 0 comes from util_return_zero_u64 (0x0C03FEA0). Because 0x0C03FEA8 is also a zero-return stub, the value passed in the zero-parameter branch has no visible effect.

- Addresses by version: 219: 0x0C04014C
- Called by: `app_system_init`
- Calls: `util_return_zero_u64`, `util_return_zero_u32`, `clock_gettime`
- Confidence: medium

## ble_debug_timestamp_print

**Print wall-clock seconds and nanoseconds with the hardware clock value**

Diagnostic timestamp print. It first calls app_cmd_complete_signal, which the other print helpers in this packet also call first, then reads CLOCK_REALTIME through clock_gettime into a two-word local and reads a hardware clock value through util_return_zero_u64. It prints 's.ns: sec.ns, hwclock=..., hw-time=...', where hw-time is the hardware value minus the seconds. Returns 0.

**Returns** `s32`: always 0

**Notes:** util_return_zero_u64 is a stub returning 0 in this image, so hwclock and hw-time print 0 and the seconds value. The second printed field comes from a separate stack slot (local_10), not from the timespec's nanosecond word as the format suggests; check the disassembly.

- Addresses by version: 219: 0x0C03FF38
- Calls: `app_cmd_complete_signal`, `trace_printf`, `util_return_zero_u64`, `clock_gettime`
- Confidence: medium

## ble_get_ram_var_20003540_div4

**Return the global word at 0x20003540 shifted right by 2**

Loads the 32-bit RAM variable at 0x20003540 and returns it logically shifted right by two bits (divide by 4, e.g. a byte count converted to words or a tick prescale). No side effects. Called only from ble_219_0c0867d0. The semantics of the variable are not determinable from this function alone.

**Returns** `u32`: DAT_20003540 >> 2

**Notes:** Variable role unknown; name is descriptive.

- Addresses by version: 219: 0x0C0866C0
- Called by: `norflash_delay_us`
- Confidence: low

## ble_get_var_2000f5fc

**Return the 32-bit global at 0x2000f5fc**

Trivial getter that returns DAT_2000f5fc. Called from ble_219_0c0285ec, which also uses the CRC16 routine, so the value may be a configuration/state word used there.

**Returns** `u32`: value of DAT_2000f5fc

- Addresses by version: 219: 0x0C04757C
- Called by: `nb_upgrade_process_cmd`
- Confidence: medium

## ble_mem_copy

**Wrapper around memcpy that returns 0**

Calls newlib memcpy (0x0C0709BC) as memcpy(param_1, param_3, param_4) and returns 0. param_2 is unused. Eight BLE host and controller callers use it as a copy helper. Its status is always 0, even for zero length.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination |
| `param_2` | `u32` | not used |
| `param_3` | `ptr` | source |
| `param_4` | `u32` | size in bytes |

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C03AA40
- Called by: `bt_drv_hci_cmd_complete_info_rx`, `bt_drv_reg_op_load_rssi_table_a`, `bt_drv_reg_op_load_rssi_table_b`, `bt_drv_reg_op_load_rssi_table_c`, `bt_drv_reg_op_load_table8_bdd4`, `rf_test_hci_cmd_complete_handler`, `app_testmode_bt_nonsig_tx`, `ble_vendor_fc87_send_keyed`
- Calls: `memcpy`
- Confidence: high

## ble_mem_fill

**Wrapper around memset that returns 0**

Calls newlib memset (0x0C070A0A) as memset(param_1, param_3, param_4) and returns 0. param_2 is unused. Its only caller in the packet is ble_219_0c03c070.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination |
| `param_2` | `u32` | not used |
| `param_3` | `u32` | byte value |
| `param_4` | `u32` | size in bytes |

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C03AA50
- Called by: `bt_drv_rf_2168_cal_search`
- Calls: `memset`
- Confidence: high

## ble_nvdata0_dev_read_record

**Read the 120-byte record from /dev/nvdata0 into DAT_2000F354, opening it on first use**

Opens '/dev/nvdata0' with mode 0 on first use and caches the descriptor in DAT_20003EC8. It issues a control call (fd, command 0x101, scratch buffer) through the fd-dispatch helper at 0x0C0484B4; on failure it prints 'Invalid nvdata0 !' and returns that error. It then reads 0x78 (120) bytes into the record at 0x2000F354 and returns 0 when all 120 bytes arrive, -5 otherwise.

**Returns** `s32`: 0 on success, -5 on a short read, a negative value when open or the control call fails

**Notes:** Not the same as ble_nvdata_read_record (ble_219_0c02d784), which is a CRC-checked partition record reader. The helper at 0x0C0484B4 is named _close in wave 2 but is called here with three arguments (fd, command, buffer), so its behaviour as an ioctl-like path should be reviewed. The meaning of command 0x101 is not identified.

- Addresses by version: 219: 0x0C041D50
- Called by: `app_system_init`
- Calls: `trace_printf`, `_close`, `ble_219_0c071a94`, `read`
- Confidence: medium

## ble_nvdata0_dev_write_record

**Write the 120-byte record from DAT_2000F354 to /dev/nvdata0, then issue control command 0x200**

Writes the 0x78-byte record at 0x2000F354 to /dev/nvdata0, opening the device first if the cached descriptor DAT_20003EC8 is not valid (same open as the read routine). A short write returns -5. On success it issues a second control call (fd, command 0x200, 0) through the same helper at 0x0C0484B4 and returns 0x78.

**Returns** `s32`: 0x78 on success, -5 on a short write, a negative value when open fails

**Notes:** This returns 0x78 on success while ble_nvdata0_dev_read_record returns 0, so callers need to check the two conventions. Command 0x200 is probably a commit or sync; not confirmed.

- Addresses by version: 219: 0x0C041DC0
- Called by: `ble_cfg_set_f36c_bytes`, `ble_cfg_set_bd_addr_unchecked`, `ble_cfg_set_block40`, `ble_cfg_set_word_f360`, `ble_cfg_set_flag_f36a`, `ble_cfg_set_flag_f36b`, `ble_cfg_set_word_f3b4`, `ble_cfg_set_bytes_f3b8`
- Calls: `_close`, `ble_219_0c071a94`, `write`
- Confidence: medium

## ble_parse_csv_u8x4

**Parse up to four comma-separated decimal fields into byte outputs**

Tokenises the string in param_1 with strtok-style calls on ',' (ble_219_0c071790, not yet named) and converts each token with atol, storing the low byte into param_2, param_3, param_4 and param_5 in order. param_2 is always written from the first token. Tokens after the fourth are ignored, and it has no direct callers in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | NUL-terminated comma-separated string; modified by the tokenizer |
| `param_2` | `ptr` | output byte for field 0 |
| `param_3` | `ptr` | output byte for field 1 |
| `param_4` | `ptr` | output byte for field 2 |
| `param_5` | `ptr` | output byte for field 3 |

- Addresses by version: 219: 0x0C055634
- Calls: `atol`, `ble_219_0c071790`
- Confidence: medium

## ble_parse_u8x3_bdaddr

**Parse three comma-separated decimal bytes and a trailing Bluetooth address**

Like ble_parse_csv_u8x4, but the fourth field is a Bluetooth device address. The first three tokens are converted with atol into one-byte outputs param_2, param_3 and param_4. The fourth token, when present, is parsed with bt_bdaddr_from_string into the 6-byte output param_5; when it is absent param_5 is zeroed. In both cases ble_hook_noop_05a9c0 is then called with the address, which is an empty hook in this build.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | NUL-terminated comma-separated string; modified by the tokenizer |
| `param_2` | `ptr` | output byte for field 0 |
| `param_3` | `ptr` | output byte for field 1 |
| `param_4` | `ptr` | output byte for field 2 |
| `param_5` | `ptr` | 6-byte Bluetooth device address output |

- Addresses by version: 219: 0x0C05569C
- Calls: `ble_hook_noop_05a9c0`, `bt_bdaddr_from_string`, `atol`, `ble_219_0c071790`
- Confidence: medium

## ble_pktq_enqueue

**Append a packet to the ble_pktq ring: copy the payload into the next slot**

Appends one packet, returning 14 when the payload is longer than the slot size (0x2000F7BC) and 16 when the ring is full (next head equals tail). It takes the ring mutex at 0x2000F7C4 with an infinite timeout, reserves the head slot and advances head with wrap at n, then releases the mutex. The descriptor's cookie word is set to param_3, and the payload is copied into the reserved slot with memcpy outside the lock, after which the length is written to the descriptor. A NULL payload or zero length stores length 0, copies nothing, and still returns 0. The consumer side is not in this packet, so the matching dequeue is unknown.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | payload source, may be NULL |
| `param_2` | `u32` | payload length in bytes |
| `param_3` | `u32` | cookie stored in the descriptor (for example an opaque pointer) |

**Returns** `u32`: 0 on success, 14 if the payload is oversized, 16 if the ring is full

- Addresses by version: 219: 0x0C048A44
- Called by: `ble_evt_post_u16_ctx`, `ble_record_sync_step`, `ble_record_sync_tick`, `ble_evt_post_u16`, `ble_pending_flags_enqueue`
- Calls: `xQueueGiveMutexRecursive`, `xQueueTakeMutexRecursive`, `memcpy`
- Confidence: medium

## ble_pktq_init

**Initialise a packet ring of n+1 descriptor slots and create its recursive mutex**

Sets up the ring used by ble_pktq_enqueue. The buffer at param_3 must be 4-byte aligned (otherwise the function returns 1); it holds n+1 eight-byte descriptors ({u32 cookie, u16 length, 2 pad bytes}) followed by n+1 payload slots of slot_size bytes starting at buffer + 8*(n+1). It records the descriptor base at 0x2000F7B8, the slot base at 0x2000F7B4, the slot size at 0x2000F7BC and n at 0x2000F7BE, sets head (0x2000F7B0) and tail (0x2000F7C0) to 0, then creates the recursive mutex at 0x2000F7C4 with FUN_0C042D80 (type 4, static storage). The creation result is not checked.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | slot size in bytes |
| `param_2` | `s16` | n; the ring has n+1 slots |
| `param_3` | `ptr` | 4-byte aligned storage of at least (8 + slot_size) * (n+1) bytes |
| `param_4` | `u32` | not used by the initialiser; passed through to the mutex creator |

**Returns** `u32`: 0 on success, 1 for a misaligned buffer

- Addresses by version: 219: 0x0C0489E8
- Called by: `ble_host_start`
- Calls: `prvInitialiseMutex`
- Confidence: medium

## ble_random_fill_seeded

**Fill a buffer with param_2 random bytes from the unnamed generator, seeded by the tick count**

Reads the FreeRTOS tick count with xTaskGetTickCount (0c043F1C) and calls the unnamed seed routine 0c071478; the tick value is still in r0 when the seed routine is entered. It then writes param_2 bytes to param_1, one per call to the unnamed generator 0c0714D4. The loop index is an 8-bit counter, so param_2 must be 1..255; a larger count never ends the loop.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output buffer |
| `param_2` | `u32` | number of bytes, 1..255 |

**Notes:** Callers: 0c02BDD0. Whether the generator is cryptographic is not known from this body.

- Addresses by version: 219: 0x0C05B5C0
- Called by: `ble_crypto_init`
- Calls: `xTaskGetTickCount`, `ble_219_0c071478`, `ble_219_0c0714d4`
- Confidence: medium

## ble_ring_append_with_mark

**Append a payload to a BTstack ring buffer under a lock, optionally patching one marker byte**

Takes the lock at 0x20008B00 with a 100-tick timeout (ble_219_0c0430a8) and returns without action if it is not obtained. If param_3 is not 0xFF it writes the fill byte DAT_200092EC at payload offset param_3; when bit 7 of param_3 is set it masks that bit off, does only this marker write and skips the ring append. Otherwise it asks btstack_ring_buffer_bytes_free for ring 0x20008AEC and calls btstack_ring_buffer_write for param_2 bytes from param_1 when they fit, dropping the payload silently when they do not. The lock is released with ble_219_0c042c8c on every path after it was taken.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | payload buffer; source of the ring append and target of the marker byte |
| `param_2` | `u32` | payload length in bytes |
| `param_3` | `u32` | marker offset; 0xFF means no marker, bit 7 set means marker-only write |

**Notes:** The purpose of ring 0x20008AEC and of the marker byte DAT_200092EC is not identified. The lock is inferred to be a take with timeout and ble_219_0c042c8c a give, from their use elsewhere in the packet.

- Addresses by version: 219: 0x0C028B90
- Calls: `xQueueGenericSend`, `xQueueSemaphoreTake`, `btstack_ring_buffer_bytes_free`, `btstack_ring_buffer_write`
- Confidence: medium

## ble_set_var_2000f64c

**Store a 32-bit value in the global at 0x2000f64c, return 0**

Trivial setter: DAT_2000f64c = param_1; always returns 0 (success). Called from ble_219_0c0286e0 and ble_219_0c037a2c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value to store |

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C047634
- Called by: `ble_init_cfg_ptr_store`, `nb_upgrade_init`
- Confidence: medium

## ble_slot_identity_dump

**Print 15 bytes of the slot identity block in hex and return 1**

Gets the slot header block from ble_slot_get_header_ptr (the structure before the slot table at 0x20010188) and copies 16 bytes of it to the buffer whose pointer is in r3 on entry; the decompile shows this as in_r3, not as a normal parameter. A loop then swaps bytes inside the first 8 bytes of that buffer. Bytes 0..14 are printed with %02x through 0c035D0C, followed by a constant string at 0x0C07F24C. Always returns 1.

**Returns** `u32`: always 1

**Notes:** The byte-swap pattern is hard to read from the decompile (the loop index runs over overlapping pairs), so the exact resulting byte order is uncertain. The identity meaning (BD address or serial) is not established.

- Addresses by version: 219: 0x0C05C7B6
- Calls: `trace_printf`, `ble_slot_get_header_ptr`
- Confidence: low

## ble_slot_is_used_2000f4cc

**Test whether entry N of the 32-bit table at 0x2000f4cc is non-zero**

Returns true when the word at DAT_2000f4cc[param_1] is not zero, i.e. an indexed array of pointers/handles/flags is checked for an occupied slot. No bounds check is performed. It has no direct callers (invoked through a function pointer / callback table).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | slot index into the word array at 0x2000f4cc |

**Returns** `bool`: true if the slot is non-zero

- Addresses by version: 219: 0x0C046F40
- Confidence: medium

## ble_stub_nop_0c04628c

**Empty function (immediate return)**

Body is a single return instruction. Called once from ble_219_0c043e70 as a hook/placeholder; it has no side effects.

- Addresses by version: 219: 0x0C04628C
- Called by: `vTaskStartScheduler`
- Confidence: high

## ble_stub_nop_0c047f88

**Empty function (immediate return)**

Single return instruction with no side effects; no direct callers, so it is a default/placeholder callback in a table.

- Addresses by version: 219: 0x0C047F88
- Confidence: high

## ble_stub_nop_0c047fe8

**Empty function (immediate return)**

Single return instruction with no side effects. Called from ble_219_0c043f48 as an empty hook.

- Addresses by version: 219: 0x0C047FE8
- Called by: `xTaskIncrementTick`
- Confidence: high

## ble_transfer_chunks_64

**Feed param_2 bytes from param_1 to 0c065C88 in pieces of at most 64 bytes**

Loops over the buffer in chunks of up to 0x40 bytes, calling the unnamed routine 0c065C88 with each chunk's pointer and length, and advances the pointer. The remaining count is kept as a 16-bit value. A zero length returns at once. 0c065C88 works on RAM objects at 0x20011A10 and 0x20011A50 whose body is not in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | buffer |
| `param_2` | `u32` | byte count, handled as 16 bits |

**Notes:** Callers: 0c053848, 0c053A48, 0c053EE4. The 64-byte chunk size is probably a buffer or FIFO limit (not verified).

- Addresses by version: 219: 0x0C05C860
- Called by: `ble_host_stage_blob`, `ble_secure_ctx_restore_from_nv`, `ble_secure_blob_wipe_1k`
- Calls: `printf_hexdump`
- Confidence: medium

## ble_uart_fmt_item

**Format one value into a bounded buffer and return the number of bytes kept**

Wrapper around the snprintf-style formatter at ble_219_0c071fbc. It passes (buffer, capacity, format) through; the value argument arrives in r3 and is forwarded unchanged because this function does not touch r3. A non-negative would-be length is clamped to capacity-1 when the output was truncated (capacity 0 counts as 1), so the result is always the number of characters stored. A negative formatter result returns 0. ble_uart_print_values uses it to build one line in a shrinking buffer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output buffer |
| `param_2` | `u32` | buffer capacity in bytes |
| `param_3` | `ptr` | format string |

**Returns** `u32`: bytes stored (excluding room for the terminator when truncated), 0 on formatter error

**Notes:** The fourth argument (value) is inferred from the caller passing four arguments and the decompiler showing three. The formatter at 0x0C071FBC is not yet named.

- Addresses by version: 219: 0x0C033114
- Called by: `ble_uart_print_values`
- Calls: `ble_219_0c071fbc`
- Confidence: medium

## ble_uart_print_values

**Format up to N 1/2/4-byte values into one line and send it to UART0 by polling**

Formats an array of values into a 249-byte stack line. The element width is chosen by param_2 (2 = halfword, 4 = word, anything else = byte); each value is formatted with ble_uart_fmt_item using the format string param_1 and the space left in the line (up to 0xFA characters), stopping after param_3 items or when the line is full. A count of 0 produces only a line feed. The line is ended with LF (at byte 250 when the line is full), then every byte is written to UART0 with hal_uart_putc_poll(0, byte), which waits for FIFO space. Returns the number of bytes sent.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | format string applied to each value |
| `param_2` | `u32` | element width code: 2 halfword, 4 word, other byte |
| `param_3` | `u32` | number of items |
| `param_4` | `ptr` | data array |

**Returns** `u32`: bytes sent to the UART (1 for the count 0 case)

**Notes:** The UART is UART0, the trace/console port. Width codes other than 2 and 4 are all treated as bytes.

- Addresses by version: 219: 0x0C033150
- Called by: `ble_uart_print_values_thunk`
- Calls: `ble_uart_fmt_item`, `hal_uart_putc_poll`
- Confidence: medium

## ble_uart_print_values_thunk

**Branch into ble_uart_print_values (single-instruction thunk, same arguments)**

A single branch to 0x0C033150: the decompiler shows the target body under the name thunk_FUN_0c033150, so this address has no logic of its own. It is a second entry point to the UART line printer; the caller in this packet's graph is ble_219_0c03a8f4. The arguments and return value are those of ble_uart_print_values.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | format string |
| `param_2` | `u32` | element width code |
| `param_3` | `u32` | number of items |
| `param_4` | `ptr` | data array |

**Returns** `u32`: passed through from ble_uart_print_values

**Notes:** Thunk. The behaviour is described on ble_219_0c033150.

- Addresses by version: 219: 0x0C033248
- Called by: `ble_ctrl_dump_region`
- Calls: `ble_uart_print_values`
- Confidence: high

## ble_util_hex_string_to_bytes

**Parse n delimiter-separated hex byte fields from a string into a byte array**

Returns -1 if the string or output pointer is NULL. Otherwise for i in 0..n-1 it does out[i] = strtoul(str, &end, 16), then continues after end, skipping one separator character when *end is not NUL. n == 0 is accepted and parses nothing. Returns 0. Same algorithm as bt_bdaddr_from_string with a caller-supplied count; called from 0c055b90 (text command handling, e.g. keys/addresses given as hex strings).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | NUL-terminated input string |
| `param_2` | `ptr` | out: byte array of at least n bytes |
| `param_3` | `u32` | number of bytes to parse |

**Returns** `s32`: 0 on success, -1 on NULL argument

- Addresses by version: 219: 0x0C05AA80
- Called by: `ble_fmna_debug_cmd_dispatch`
- Calls: `strtoul`
- Confidence: high

## bt_bdaddr_from_string

**Parse six hex byte fields (e.g. "xx:xx:xx:xx:xx:xx") into a 6-byte address**

Returns -1 (0xffffffff) if either pointer is NULL. Otherwise it loops exactly six times: strtoul(str, &end, 16) gives the next byte which is stored at out[i]; the scan then resumes at end, skipping one separator character if *end is not NUL (so any single delimiter works, e.g. ':' or '-'). Returns 0 on completion; no validation of the digit count or value range is done. Called from 0c05569c (text/AT style command handling); the fixed count of 6 marks it as a BD_ADDR parser, the generalised n-byte version is ble_util_hex_string_to_bytes.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | NUL-terminated string of hex byte fields |
| `param_2` | `ptr` | out: 6 bytes |

**Returns** `s32`: 0 on success, -1 if a pointer is NULL

- Addresses by version: 219: 0x0C05AA0C
- Called by: `ble_parse_u8x3_bdaddr`
- Calls: `strtoul`
- Confidence: high

## bt_bytes_reverse_inplace

**Reverse len bytes in place via a 6-byte stack temp (generic BD_ADDR byte-order swap)**

Zeroes a 6-byte stack buffer, copies buf[0..len-1] into it back to front (tmp[len-1-i] = buf[i]; the loop end uses len & 0xff) and then memcpy(buf, tmp, len). With len == 0 it just does memcpy(buf, tmp, 0). It is the length-parameterised sibling of bt_bdaddr_reverse_inplace and is called with address data from 0c058458, 0c058520, 0c0585a4 and 0c058980. The temp is only 6 bytes, so a len above 6 would overrun the stack frame.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | buffer to reverse |
| `param_2` | `u32` | number of bytes (expected 6) |

- Addresses by version: 219: 0x0C05AA44
- Called by: `ble_event_report_frame`, `ble_event_stats_report_11`, `ble_link_param_monitor_step`, `ble_host_report_clock_0d`
- Calls: `memcpy`
- Confidence: high

## co_max_u32

**Unsigned maximum of two values**

Returns param_2 if param_1 < param_2, else param_1 (unsigned compare). Plain max() helper.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | first value |
| `param_2` | `u32` | second value |

**Returns** `u32`: larger of the two

- Addresses by version: 219: 0x0C065C7C
- Called by: `att_server_handle_request`, `ble_ctrl_conn_set_pending_notify`
- Confidence: high

## co_min_u32

**Unsigned minimum of two values**

Returns param_2 if param_2 <= param_1, else param_1 (unsigned compare). Plain min() helper, called from many length-limit computations in the stack.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | first value |
| `param_2` | `u32` | second value |

**Returns** `u32`: smaller of the two

- Addresses by version: 219: 0x0C065C74
- Called by: `att_copy_value`, `att_prepare_handle_value_notification`, `att_prepare_handle_value_indication`, `att_server_handle_request`, `ble_gatt_read_char_value`, `btstack_crypto_ccm_next_block`, `btstack_crypto_aes128_encrypt`, `btstack_ring_buffer_write`, `btstack_ring_buffer_read`, `hci_run_general_gap_bredr`, `ble_ctrl_state_machine_step`, `ble_219_0c068da8` ...
- Confidence: high

## co_popcount32

**Count set bits in a 32-bit word**

Classic SWAR population count: sums bits in pairs (0x55555555), nibbles (0x33333333), bytes (0x0f0f0f0f), then 16-bit halves, and returns the total 0..32. The only caller (0c06bc74) most likely counts used channels in a channel map.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | word to count |

**Returns** `s32`: number of set bits, 0..32

- Addresses by version: 219: 0x0C065DC0
- Called by: `hci_cmd_pack_format`
- Confidence: high

## co_read16_be

**Read unaligned big-endian u16 from base+offset**

Returns (base[offset] << 8) | base[offset+1]. Network-order (ATT/L2CAP-style big-endian) 16-bit load, used by many parsers/serializers of byte-swapped fields.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | base pointer |
| `param_2` | `u32` | byte offset |

**Returns** `u16`: value read, big-endian

- Addresses by version: 219: 0x0C065B94
- Called by: `sdp_server_build_service_search_response`, `sdp_server_build_service_attribute_response`, `sdp_server_build_service_search_attribute_response`, `de_get_data_size`, `de_get_len`, `sdp_pattern_uuid_match`, `sdp_attribute_list_traverse_sequence`, `de_get_normalized_uuid`, `de_pop_sequence`, `de_add_number`, `de_add_data`, `ble_crypto_auth_derive_own_word` ...
- Confidence: high

## co_read16_le

**Read unaligned little-endian u16 from base+offset**

Returns (base[offset+1] << 8) | base[offset], i.e. an unaligned little-endian 16-bit load done bytewise. Equivalent of the RivieraWaves co_read16p() helper. Heavily used by the L2CAP/LL PDU parsers (for example the LL_CONNECTION_PARAM_REQ handler reads the interval/latency/timeout fields with it).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | base pointer |
| `param_2` | `u32` | byte offset added to base |

**Returns** `u16`: value read, little-endian

- Addresses by version: 219: 0x0C065B38
- Called by: `att_iterator_fetch_next`, `att_iterator_match_uuid16`, `att_iterator_match_uuid`, `att_server_handle_request`, `att_is_persistent_ccc`, `att_server_write_callback`, `ble_host_att_event_dispatch`, `ble_host_link_event_dispatch`, `sm_pdu_rx_handler`, `ble_adv_addr_restart`, `ble_proto_dispatch_op`, `hci_send_acl_packet_buffer` ...
- Confidence: high

## co_read32_be

**Read unaligned big-endian u32 from base+offset**

Returns b[0]<<24 | b[1]<<16 | b[2]<<8 | b[3] from base+offset using four byte loads.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | base pointer |
| `param_2` | `u32` | byte offset |

**Returns** `u32`: value read, big-endian

- Addresses by version: 219: 0x0C065BA0
- Called by: `sdp_get_service_record_handle`, `sdp_server_build_service_attribute_response`, `de_get_data_size`, `de_get_len`, `sdp_pattern_uuid_match`, `de_get_normalized_uuid`, `ble_link_notify_state`, `sm_pairing_engine_step`
- Confidence: high

## co_read32_le

**Read unaligned little-endian u32 from base+offset**

Returns b[0] | b[1]<<8 | b[2]<<16 | b[3]<<24 from base+offset using four byte loads (unaligned-safe little-endian 32-bit read, like co_read32p). No callers are listed directly in the call graph, so it is probably reached through a table or tail call.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | base pointer |
| `param_2` | `u32` | byte offset |

**Returns** `u32`: value read, little-endian

- Addresses by version: 219: 0x0C065B44
- Confidence: high

## co_reverse_copy_16

**Copy 16 bytes from src to dst in reversed order**

Fixed-size byte-reversal copy: dst[15-i] = src[i] for i in 0..15, implemented as a do-while loop with no length guard. Used to convert between little-endian wire order and big-endian (most-significant-first) order for 16-byte values such as AES keys, LTK/IRK and 128-bit UUIDs. No globals are touched.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source buffer |
| `param_2` | `ptr` | destination buffer (must not overlap) |

- Addresses by version: 219: 0x0C065C38
- Called by: `sm_pairing_engine_step`, `sm_pdu_rx_handler`, `btstack_crypto_cmac_step`, `btstack_crypto_aes128_encrypt`
- Confidence: high

## co_reverse_copy_32

**Copy 32 bytes from src to dst in reversed order**

Fixed-size byte-reversal copy: dst[31-i] = src[i] for i in 0..31, implemented as a do-while loop with no length guard. Used to convert between little-endian wire order and big-endian (most-significant-first) order for 32-byte values such as the P-256 public key coordinates / DH key (LE Secure Connections). No globals are touched.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source buffer |
| `param_2` | `ptr` | destination buffer (must not overlap) |

- Addresses by version: 219: 0x0C065C4C
- Called by: `sm_pairing_engine_step`, `sm_pdu_rx_handler`
- Confidence: medium

## co_reverse_copy_6

**Copy 6 bytes from src to dst in reversed order**

Fixed-size byte-reversal copy: dst[5-i] = src[i] for i in 0..5, implemented as a do-while loop with no length guard. Used to convert between little-endian wire order and big-endian (most-significant-first) order for 6-byte Bluetooth device addresses (BD_ADDR). No globals are touched.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source buffer |
| `param_2` | `ptr` | destination buffer (must not overlap) |

- Addresses by version: 219: 0x0C065C60
- Called by: `ble_host_link_event_dispatch`, `ble_link_notify_local_ext`, `ble_link_notify_id_flag`, `ble_link_notify_state`, `ble_link_notify_local`, `ble_link_notify_pair_addrs`, `ble_link_notify_id_addr`, `sm_pairing_step_complete`, `sm_pairing_engine_step`, `sm_pdu_rx_handler`, `ble_ctrl_conn_set_pending_notify`, `ble_ctrl_conn_clear_pending_notify` ...
- Confidence: high

## co_reverse_copy_7

**Copy 7 bytes from src to dst in reversed order**

Fixed-size byte-reversal copy: dst[6-i] = src[i] for i in 0..6, implemented as a do-while loop with no length guard. Used to convert between little-endian wire order and big-endian (most-significant-first) order for 7-byte values (for example a 6-byte address plus a type byte). No globals are touched.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source buffer |
| `param_2` | `ptr` | destination buffer (must not overlap) |

- Addresses by version: 219: 0x0C065C10
- Called by: `sm_c1_build_t1`
- Confidence: medium

## co_reverse_copy_8

**Copy 8 bytes from src to dst in reversed order**

Fixed-size byte-reversal copy: dst[7-i] = src[i] for i in 0..7, implemented as a do-while loop with no length guard. Used to convert between little-endian wire order and big-endian (most-significant-first) order for 8-byte values such as random numbers, LTKs fragments or 64-bit identifiers. No globals are touched.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source buffer |
| `param_2` | `ptr` | destination buffer (must not overlap) |

- Addresses by version: 219: 0x0C065C24
- Called by: `sm_pairing_engine_step`, `sm_pdu_rx_handler`
- Confidence: high

## co_reverse_copy_n

**Copy n bytes from src to dst reversed**

If param_3 > 0, copies param_3 bytes from param_1 to param_2 in reverse order (dst[n-1-i] = src[i]). Returns immediately for n <= 0. Used to flip endianness of variable-length fields (keys, addresses, UUIDs) when moving them between host and controller byte order.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source buffer |
| `param_2` | `ptr` | destination buffer |
| `param_3` | `s32` | number of bytes |

- Addresses by version: 219: 0x0C065BF8
- Called by: `ble_link_dispatch_peer_addr`, `ble_link_record_peer_addr`, `ble_link_table_prune_by_ctrl`, `ble_link_device_event`, `ble_219_0c068da8`, `hci_cmd_pack_format`
- Confidence: high

## co_write16_be

**Write u16 big-endian to base+offset**

Stores bits 15..8 of param_3 at base[offset] and the low byte at base[(offset+1) & 0xffff] (most-significant byte first).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | base pointer |
| `param_2` | `u32` | byte offset |
| `param_3` | `u16` | value to store |

- Addresses by version: 219: 0x0C065BBC
- Called by: `sdp_server_build_service_search_response`, `sdp_server_build_service_attribute_response`, `sdp_server_build_service_search_attribute_response`, `sdp_attribute_write_fragment`, `de_store_descriptor_with_len`, `de_create_sequence`, `de_push_sequence`, `de_pop_sequence`, `de_add_number`, `de_add_data`, `ble_crypto_auth_send_word_type1`, `ble_crypto_auth_derive_own_word` ...
- Confidence: high

## co_write16_le

**Write u16 little-endian to base+offset**

Stores the low byte of param_3 at base[offset] and bits 15..8 at base[(offset+1) & 0xffff]. The offset of the second byte is truncated to 16 bits, so the helper is meant for offsets inside a small PDU/buffer. Counterpart of co_read16_le (RW co_write16p style).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | base pointer |
| `param_2` | `u32` | byte offset |
| `param_3` | `u16` | value to store |

- Addresses by version: 219: 0x0C065B60
- Called by: `att_prepare_handle_value_notification`, `att_prepare_handle_value_indication`, `att_server_handle_request`, `ble_sink_notify_pair`, `ble_range_notify`, `ble_host_att_event_dispatch`, `ble_host_link_event_dispatch`, `ble_link_notify_local_ext`, `ble_link_notify_id_flag`, `ble_link_notify_state`, `ble_link_notify_local`, `ble_link_notify_pair_addrs` ...
- Confidence: high

## co_write32_be

**Write u32 big-endian to base+offset**

Stores param_3 as four bytes MSB first at base[offset..offset+3]; byte offsets after the first are wrapped with & 0xffff.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | base pointer |
| `param_2` | `u32` | byte offset |
| `param_3` | `u32` | value to store |

- Addresses by version: 219: 0x0C065BCC
- Called by: `sdp_server_build_service_search_response`, `de_store_descriptor_with_len`, `de_add_number`
- Confidence: high

## co_write32_le

**Write u32 little-endian to base+offset**

Stores param_3 as four bytes LSB first at base[offset..offset+3]; each of the byte offsets after the first is computed as (offset+k) & 0xffff. Counterpart of co_read32_le.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | base pointer |
| `param_2` | `u32` | byte offset |
| `param_3` | `u32` | value to store |

- Addresses by version: 219: 0x0C065B70
- Called by: `ble_link_notify_state`
- Confidence: high

## crc16_ccitt_nibble

**Table-driven CRC-16/CCITT (poly 0x1021, MSB first) over a buffer, 4 bits at a time**

Computes a CRC-16 with polynomial 0x1021 using a 16-entry nibble table at 0x0C08097C (entries 0x0000, 0x1021, 0x2042, ...). For each byte the high nibble is processed first, then the low nibble: crc = table[nibble ^ (crc >> 12)] ^ ((crc & 0xFFF) << 4). param_1 optionally points to a context of u16 values: [0] is the initial CRC and [2] (offset 4) is a final XOR value; if NULL both are 0. param_4 is a stride: the data pointer advances by param_4 bytes per step and the remaining length is decremented by param_4 per step (normally 1). Returns xorout ^ crc. Called from five places, including the NB upgrade/UART frame code paths (ble_219_0c0285ec, 0c02d784, 0c02dc50, 0c0366e4, 0c037798).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | optional CRC context: u16 init at +0, u16 xor-out at +4; NULL means 0/0 |
| `param_2` | `ptr` | data buffer |
| `param_3` | `s32` | length in bytes (loop runs while > 0) |
| `param_4` | `s32` | step/stride in bytes (1 for contiguous data) |

**Returns** `u16`: 16-bit CRC (stored in a u32)

- Addresses by version: 219: 0x0C047644
- Called by: `nb_upgrade_process_cmd`, `ble_nvdata_read_record`, `ble_nvdata_write_task`, `nb_upgrade_packet_info_rebuild`, `nb_upgrade_resume_load`
- Confidence: high

## crc32_reflected_table

**Table-driven reflected CRC-32 (poly 0xEDB88320) over a buffer**

Standard byte-wise CRC-32: crc = table[(byte ^ crc) & 0xFF] ^ (crc >> 8) with the 256-entry table at 0x0C074168. param_1 optionally points to a context of two u32 words: [0] initial CRC value, [1] final XOR value (NULL means both 0), so the caller supplies 0xFFFFFFFF/0xFFFFFFFF for the usual IEEE CRC-32. param_4 is a stride: pointer advances by param_4 and the remaining count drops by param_4 per iteration. Returns xorout ^ crc. Used for firmware/IAP image CRC verification and other integrity checks (callers ble_219_0c034468, 0c03457c, 0c047274).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | optional context: u32 init at +0, u32 xor-out at +4; NULL = 0/0 |
| `param_2` | `ptr` | data buffer |
| `param_3` | `s32` | length in bytes |
| `param_4` | `s32` | stride in bytes (normally 1) |

**Returns** `u32`: CRC-32 value

- Addresses by version: 219: 0x0C0476A0
- Called by: `nb_upgrade_verify_raw`, `nb_upgrade_verify_device_image`, `nb_upgrade_image_parse`
- Confidence: high

## printf_hexdump

**Print a buffer as uppercase hex pairs separated by spaces, then a newline**

Prints param_2 bytes from param_1 as uppercase hex pairs separated by spaces, followed by a newline. Each byte is turned into two digits from the table "0123456789ABCDEF" and placed in a 4-byte stack string with a trailing space and NUL. That string is printed through the printf-style logger 0x0C035D0C with format "%s" (the string at 0x0C086184 in the image). Nothing is printed when the count is zero or negative, and a newline string at 0x0C07F24C ends the dump. The routine keeps no state and makes no heap calls. It has nine callers in the BLE host, listed in the packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | bytes to print |
| `param_2` | `s32` | number of bytes; nothing printed when 0 or negative |

**Notes:** The name follows BTstack's printf_hexdump, which matches this behaviour (uppercase, space after each byte, newline at the end). The name is a match by behaviour and not a confirmed symbol. The format string and newline string were read from the firmware image.

- Addresses by version: 219: 0x0C065C88
- Called by: `ble_host_cache_key16`, `ble_host_stage_blob`, `ble_secure_ctx_restore_from_nv`, `ble_record_a_derive_and_commit`, `ble_record_b_derive_and_commit`, `ble_fmna_found_url_update`, `ble_record_sync_step`, `ble_fmna_pair_adv_service`, `ble_transfer_chunks_64`
- Calls: `trace_printf`
- Confidence: high

## ringbuf_contig_read_len

**Contiguous readable bytes from the read index to the buffer end or write index**

With read = [0], write = [1], size = [2]: returns size - read when write < read (data wraps, so only the tail segment is contiguous), else write - read. Used before a single linear copy/DMA from the ring (caller ble_219_0c046380).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ring descriptor: read idx, write idx, size |

**Returns** `s32`: bytes readable without wrapping

- Addresses by version: 219: 0x0C043820
- Called by: `ble_uart_tx_dma_pump`
- Confidence: medium

## ringbuf_contig_write_len

**Contiguous writable bytes from the write index, keeping one slot free**

With read = [0], write = [1], size = [2]: if write < read returns read - 1 - write; otherwise returns size - write, minus 1 when read == 0 (so the buffer never becomes completely full). Used before a linear write/receive into the ring (callers ble_219_0c04264c, ble_219_0c0462c4).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ring descriptor: read idx, write idx, size |

**Returns** `s32`: bytes writable without wrapping

- Addresses by version: 219: 0x0C0438C0
- Called by: `ble_msgq_read_items`, `ble_uart_rx_dma_pump`
- Confidence: medium

## ringbuf_free_space

**Free bytes in a circular buffer descriptor (read-1-write modulo size)**

Circular-buffer helper working on a descriptor {[0]=read index, [1]=write index, [2]=size}. Computes (size + read - 1 - write) and wraps it by subtracting size when result >= size, i.e. the number of bytes that can still be written while always leaving one slot unused. Called by ble_219_0c0422d4 (likely a UART/transport TX or RX path).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ring descriptor: read idx, write idx, size |

**Returns** `u32`: free space in bytes

**Notes:** Field roles (read vs write index) inferred from the formula and the empty test ringbuf_is_empty.

- Addresses by version: 219: 0x0C04352C
- Called by: `ble_ring_poll_status`
- Confidence: medium

## ringbuf_is_empty

**True when the ring's two indices are equal**

Returns descriptor[1] == descriptor[0] (write index equals read index), the empty condition of the circular buffer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ring descriptor: read idx, write idx, size |

**Returns** `bool`: true if no data is buffered

- Addresses by version: 219: 0x0C0437E0
- Called by: `ble_ring_poll_status`, `ble_msgq_read_items`, `ble_uart_rx_dma_pump`
- Confidence: medium

## ringbuf_is_full_with_reserve

**True when free space is at most a reserve (4 bytes if flag bit0 set at +0x1c)**

Computes the free space of the ring as in ringbuf_free_space, then compares it with a reserve: 4 bytes when bit 0 of the byte at descriptor+0x1c is set (some extended-record mode, probably space for a length header), otherwise 0. Returns true when free <= reserve, i.e. no further record can be written. Callers ble_219_0c0424d8 and ble_219_0c046380.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ring descriptor: read idx, write idx, size, ..., flags byte at +0x1c |

**Returns** `bool`: true if the ring is full (within reserve)

**Notes:** Meaning of flag bit 0 is a guess.

- Addresses by version: 219: 0x0C0437F0
- Called by: `ble_msgq_write_items`, `ble_uart_tx_dma_pump`
- Confidence: medium

## ringbuf_read_ptr

**Address of the current read position (base + read index)**

Returns descriptor[6] (buffer base/offset, at +0x18) + descriptor[0] (read index). Used by ble_219_0c046380 to obtain the pointer for consuming data from the ring.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ring descriptor, +0x18 holds buffer base |

**Returns** `ptr`: pointer into the buffer at the read index

- Addresses by version: 219: 0x0C043818
- Called by: `ble_uart_tx_dma_pump`
- Confidence: medium

## ringbuf_used_count

**Number of bytes stored in a circular buffer descriptor**

Computes (size + write - read) and wraps by subtracting size when >= size, on the descriptor {[0]=read, [1]=write, [2]=size}: the count of readable bytes. Caller ble_219_0c045534.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ring descriptor: read idx, write idx, size |

**Returns** `u32`: bytes available to read

- Addresses by version: 219: 0x0C043540
- Called by: `hci_stream_buffer_is_empty`
- Confidence: medium

## ringbuf_write_ptr

**Address of the current write position (base + write index)**

Returns *(param_1+0x18) (buffer base) + *(param_1+4) (write index). Companion of ringbuf_read_ptr; caller ble_219_0c0462c4.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ring descriptor, +0x18 holds buffer base |

**Returns** `ptr`: pointer into the buffer at the write index

- Addresses by version: 219: 0x0C0438B8
- Called by: `ble_uart_rx_dma_pump`
- Confidence: medium

## segger_rtt_write_blocking

**SEGGER RTT _WriteBlocking: copy into an up buffer in chunks, spinning until all bytes are stored**

param_1 is a SEGGER_RTT_BUFFER_UP. Loops: computes the free contiguous space from WrOff to min(end of buffer, RdOff - 1) (handles the wrap-around when RdOff <= WrOff), copies min(remaining, space) bytes with memcpy, advances WrOff (wrapping to 0 at SizeOfBuffer), re-reads RdOff and repeats until all param_3 bytes are written; busy-waits if the host reader has not consumed enough yet. Returns the number of bytes written (= param_3). Used by SEGGER_RTT_SetTerminal when the buffer flags select blocking mode (Flags & 3 == 2, SEGGER_RTT_MODE_BLOCK_IF_FIFO_FULL). Matches the static _WriteBlocking in SEGGER_RTT.c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | SEGGER_RTT_BUFFER_UP ring descriptor |
| `param_2` | `ptr` | source data |
| `param_3` | `u32` | number of bytes |
| `param_4` | `u32` | unused (decompiler artifact) |

**Returns** `u32`: bytes written

- Addresses by version: 219: 0x0C03F97C
- Called by: `SEGGER_RTT_SetTerminal`
- Calls: `memcpy`
- Confidence: high

## segger_rtt_write_no_check

**SEGGER RTT _WriteNoCheck: copy param_3 bytes into an up buffer at WrOff with wrap, no free-space check**

param_1 is a SEGGER_RTT_BUFFER_UP (pBuffer +4, SizeOfBuffer +8, WrOff +0xC, RdOff +0x10). If the bytes fit before the end of the ring (param_3 < SizeOfBuffer - WrOff) a single memcpy to pBuffer + WrOff is done and WrOff += param_3; otherwise it copies the first SizeOfBuffer - WrOff bytes to the end, the remaining bytes to the start of the buffer, and sets WrOff to the remainder. The caller must have verified free space (SEGGER_RTT_SetTerminal 0x0c03fcfc checks RdOff/WrOff before calling it with the 2-byte terminal-switch sequence 0xFF,'0'..'F'). Matches the static _WriteNoCheck in SEGGER_RTT.c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | SEGGER_RTT_BUFFER_UP ring descriptor |
| `param_2` | `ptr` | source data |
| `param_3` | `u32` | number of bytes |
| `param_4` | `u32` | unused (decompiler artifact) |

- Addresses by version: 219: 0x0C03F934
- Called by: `SEGGER_RTT_SetTerminal`
- Calls: `memcpy`
- Confidence: high

## segger_rtt_write_overwrite_nolock

**Write NumBytes into RTT up-buffer n, overwriting the oldest unread data if it does not fit**

Operates on SEGGER RTT up buffer param_1 of the control block initialised by SEGGER_RTT_Init (aUp[] starts at 0x2000BE48, 24-byte entries: pBuffer +4 = 0x2000BE4C, SizeOfBuffer +8 = 0x2000BE50, WrOff +0xC = 0x2000BE54, RdOff +0x10 = 0x2000BE58). First computes the free space exactly like SEGGER's _GetAvailWriteSpace (Size-1 if WrOff==RdOff, RdOff-WrOff-1 if WrOff<RdOff, else Size+RdOff-WrOff-1). If that is smaller than param_3 it advances RdOff by the shortfall (wrapping modulo SizeOfBuffer in a while loop), i.e. the oldest unread bytes are discarded instead of blocking or trimming. Then copies the data with memcpy in chunks: up to Size-WrOff bytes at WrOff, then from offset 0, updating WrOff after each chunk, and always returns param_3. Not a stock SEGGER mode (SKIP/TRIM/BLOCK); no locking is done, callers must hold SEGGER_RTT_LOCK. No direct callers (reached through a function pointer or the trace back-end).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | up-buffer index into _SEGGER_RTT.aUp[] |
| `param_2` | `ptr` | source bytes |
| `param_3` | `u32` | number of bytes to write |

**Returns** `u32`: always param_3 (number of bytes written)

**Notes:** Layout and _GetAvailWriteSpace match SEGGER_RTT.c; the overwrite-oldest policy is a local modification, so the exact original name is unknown.

- Addresses by version: 219: 0x0C03FB1C
- Calls: `memcpy`
- Confidence: medium

## stub_empty_0c037584

**Empty function (immediate return)**

Contains only a return instruction; called from the neighbouring function at 0x0c037588 as an empty hook/placeholder.

- Addresses by version: 219: 0x0C037584
- Called by: `nb_upgrade_session_finish`
- Confidence: high

## stub_empty_0c0398a8

**Empty function (immediate return)**

Contains only a return instruction; called from 0x0c04146c and 0x0c0414ac as an empty hook placeholder.

- Addresses by version: 219: 0x0C0398A8
- Called by: `hal_cmu_aonclk9_user_enable`, `hal_cmu_aonclk9_user_disable`
- Confidence: high

## stub_empty_0c03aa3c

**Empty function (immediate return)**

Contains only a return instruction; called from 0x0c04696c and 0x0c046c7c as an empty hook placeholder.

- Addresses by version: 219: 0x0C03AA3C
- Called by: `bt_drv_ctrl_bringup`, `bt_drv_ctrl_bringup_rf_test`
- Confidence: high

## stub_empty_0c03aa60

**Empty function (immediate return)**

Contains only a return instruction; called from 0x0c03bb70 immediately before the register-write helper at 0x0c03aa64.

- Addresses by version: 219: 0x0C03AA60
- Called by: `bt_drv_rf_bringup`
- Confidence: high

## stub_return_zero_0c0360c8

**Stub returning 0**

Does nothing and returns 0; reached from a callback or hook-table call site at 0x0c05f338 where the default behaviour is success/false.

**Returns** `u32`: always 0

**Notes:** Purpose depends on the call site at 0x0c05f338, not determined here.

- Addresses by version: 219: 0x0C0360C8
- Called by: `ecc_mulmod_ladder_ct`
- Confidence: high

## stub_return_zero_0c0360cc

**Stub returning 0**

Does nothing and returns 0; called from 0x0c02e7d8 as a default hook returning success/false.

**Returns** `u32`: always 0

**Notes:** Purpose depends on the call site at 0x0c02e7d8, not determined here.

- Addresses by version: 219: 0x0C0360CC
- Called by: `uart_disp_rx_process`
- Confidence: high

## stub_return_zero_0c065144

**Stub that always returns 0**

Two-instruction function that returns 0 (constant). Called once from 0c051ef0 (a command/packet handler); looks like an unimplemented optional callback or query that is compiled to a constant.

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C065144
- Called by: `sm_pdu_rx_handler`
- Confidence: medium

## trace_printf

**printf-style trace output into the trace object at 0x20003E30 (three variadic words)**

Variadic wrapper: copies its last three arguments (r1..r3) into a three-word stack array and passes the array with the format string to trace_vprintf_core on the trace object at 0x20003E30. Output goes through the character sink hal_trace_uart0_putc. Only three variadic words are copied, so a conversion that consumes a fourth argument reads stack memory above the copy and prints a wrong value.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | printf format string |
| `param_2` | `u32` | first variadic argument |
| `param_3` | `u32` | second variadic argument |
| `param_4` | `u32` | third variadic argument |

**Notes:** Several callers in this packet pass four variadic arguments, for example the 'dev:%s,offset:%d,size:%d,item_table_size:%d' trace in ble_219_0c02dea8 and the 'NOTICE:IAP verify error ... ret:%d' trace in ble_219_0c037588; the last field of those lines is not reliable. Worth checking whether the wrapper should take a fifth argument.

- Addresses by version: 219: 0x0C035D0C
- Called by: `nb_upgrade_process_cmd`, `btapp_btle_connect_status_change`, `ble_speed_limit_code_check`, `btle_connect_status_change`, `ble_link_status_notify_tick`, `btapp_btle_connect_status_change_enhance`, `ble_recv_rate_test_report`, `ble_app_poll_tick`, `ble_findmy_ring_status_notify`, `ble_unlock_auth_cb`, `ble_device_name_setup`, `bt_app_set_name_and_advdata` ...
- Calls: `trace_vprintf_core`
- Confidence: high

## trace_vprintf_core

**Format a printf-style string to the trace output object, handling %c %d %u %x %p %s and %f**

Walks the format string at param_2 and sends each character through hal_trace_buf_putc into the output object at param_1, whose pending count at +0x56, line buffer at +0x58 and write callback at +0x50 are used to flush. It parses the flags '#', '+', '-' and '0', then a width and an optional precision after a dot, and skips the 'h' and 'l' length modifiers. Arguments come from the va cursor at param_3, which is advanced in place: %d uses trace_fmt_signed, %u, %x, %X and %p (0x and eight hex digits) use trace_fmt_unsigned, %c and %s are written directly, and %f converts the double with __aeabi_d2f, prints the integer part and then the fraction scaled by 10 to the precision, truncating rather than rounding. When the scheduler is running (xTaskGetSchedulerState) the output object is locked with ble_219_0c0431f8 and released with ble_219_0c042df4 before returning the count of characters written, or a negative value when a write callback fails.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output object: pending count +0x56, buffer +0x58, write callback +0x50 |
| `param_2` | `ptr` | format string |
| `param_3` | `ptr` | va_list cursor, advanced in place |

**Returns** `s32`: characters written, negative on a write-callback failure

**Notes:** This is the trace printf used by the BLE firmware, not newlib vfprintf. The %f path truncates instead of rounding. The h and l modifiers are skipped without size distinction.

- Addresses by version: 219: 0x0C035900
- Called by: `trace_printf`
- Calls: `hal_trace_buf_putc`, `trace_fmt_unsigned`, `trace_fmt_signed`, `xQueueGiveMutexRecursive`, `xQueueTakeMutexRecursive`, `xTaskGetSchedulerState`, `__aeabi_d2f`
- Confidence: high

## util_bytes16_to_hex

**Format 16 bytes as 32 lowercase hex characters with a NUL terminator**

Loops over 16 input bytes at param_1 and writes each as two lowercase hex digits with snprintf(dst, 33, '%02x') through 0x0C071570. Each call writes two characters and a NUL at the write position, and the next call overwrites that NUL, so the result is a 32-character string terminated at param_2[32]. param_3 and param_4 are not used by the body; param_4 is passed through as a stray variadic argument to snprintf.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 16 input bytes |
| `param_2` | `ptr` | output buffer, at least 33 bytes |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | unused, passed as an extra snprintf argument |

**Notes:** No caller is in this packet. It is probably used to print 16-byte identifiers or keys as text.

- Addresses by version: 219: 0x0C047F48
- Calls: `ble_219_0c071570`
- Confidence: high

## util_count_trailing_zeros32

**Count trailing zero bits of a 32-bit word (RBIT + CLZ)**

Bit-reverses the input (the decompiler expanded RBIT into per-byte shift/or chains) and then executes CLZ on the result, so it returns the index of the lowest set bit (0..31), or 32 if the input is 0. Used by the controller scheduling code at 0x0c02feec to find the first set bit in a bitmask.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value to examine |

**Returns** `s32`: number of trailing zero bits, 32 for input 0

- Addresses by version: 219: 0x0C03ABA4
- Called by: `hal_gpio_irq_handler`
- Confidence: high

## util_ctz32

**Count trailing zero bits of a 32-bit word (returns 32 for 0)**

Binary-search count of trailing zeros: returns 32 for 0 and 0 when bit0 is set; otherwise tests the low 16/8/4/2 bits in turn, shifting and accumulating the index, and finally subtracts bit0 of the remainder. Result is the zero-based index of the lowest set bit. Sole caller 0x0c02dea8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value |

**Returns** `u32`: number of trailing zeros, 0..32

- Addresses by version: 219: 0x0C036024
- Called by: `nvdata_device_init`
- Confidence: high

## util_find_str_in_buf

**Find a NUL-terminated needle inside the first n bytes of a (non-terminated) buffer**

memmem-style search: returns 0 if param_1 is NULL or strlen(param_3) > param_2; otherwise tries every start offset 0..param_2-strlen(needle) and returns the first pointer for which strncmp(pos, needle, strlen(needle)) == 0, or 0 when nothing matches. The haystack need not be NUL-terminated. Single caller 0x0c0288dc, the 'REMOVE LIMIT SPD CODE' check, which looks for either the fixed string "pWEwvenFz9" or a 10-byte code derived from a 16-bit field (ctx+0x3a) inside a received VCU payload and, on a hit, sends command 0x82 (index 3, value 2) to the VCU via 0x0c02c124.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | haystack buffer (may be NULL) |
| `param_2` | `u32` | number of valid bytes in the haystack |
| `param_3` | `ptr` | NUL-terminated needle string |

**Returns** `ptr`: pointer to the first occurrence inside param_1, or 0 if absent

- Addresses by version: 219: 0x0C028898
- Called by: `ble_speed_limit_code_check`
- Calls: `strlen`, `strncmp`
- Confidence: high

## util_nop_stub_a

**Empty stub function (returns immediately)**

Body is a single return instruction. Likely a compiled-out debug/trace hook or an unused callback placeholder; called from stack functions such as 0c04ceb8, 0c051eb8 and 0c068da8 without effect.

- Addresses by version: 219: 0x0C065CDC
- Called by: `att_server_handle_request`, `ble_crypto_auth_pubkey_begin`, `sm_pairing_engine_step`, `sm_pdu_rx_handler`, `ble_219_0c068da8`
- Confidence: medium

## util_nop_stub_b

**Empty stub function (returns immediately)**

Body is a single return instruction. A second no-op placeholder (distinct address, different callers than util_nop_stub_a), most probably a stubbed-out trace/assert macro in the build.

- Addresses by version: 219: 0x0C065CE0
- Called by: `le_device_db_tlv_add`, `sm_c1_xor_p2`, `sm_c1_build_t1`, `ble_crypto_auth_send_word_type1`, `ble_crypto_auth_load_keys`, `sm_pairing_engine_step`, `btstack_crypto_cmac_step`
- Confidence: medium

## util_return_zero_u32

**Stub that returns 0**

Single move of 0 to r0 and return. Called from 0x0c03ff68 and 0x0c04014c alongside util_return_zero_u64, so it is a stubbed callback returning success/0.

**Returns** `u32`: always 0

**Notes:** Purpose of the callers' hook is unknown.

- Addresses by version: 219: 0x0C03FEA8
- Called by: `clock_settime`, `ble_clock_realtime_offset_update`
- Confidence: medium

## util_return_zero_u64

**Stub that returns 0 in r0/r1**

Contains only a move of 0 into the return registers and a return (declared as 64-bit return by the decompiler, so r1 is probably also 0). Called from 0x0c03ff38 and 0x0c04014c, which also call util_return_zero_u32. Likely a stub of a hook/callback (e.g. an unused lock, tick or hardware-query hook) in the runtime.

**Returns** `u64`: always 0

**Notes:** Purpose of the callers' hook is unknown; may be a stubbed-out lock/unlock or time function.

- Addresses by version: 219: 0x0C03FEA0
- Called by: `ble_debug_timestamp_print`, `ble_clock_realtime_offset_update`
- Confidence: medium

## util_sub_s32

**Return param_1 - param_2**

Two-instruction signed subtraction wrapper. Called from three neighbouring functions (0c065908, 0c06595c, 0c065a0c), probably as a comparator/delta callback (for example comparing timestamps or sort keys); its exact use is not visible from the function itself.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | minuend |
| `param_2` | `s32` | subtrahend |

**Returns** `s32`: param_1 - param_2

- Addresses by version: 219: 0x0C065C84
- Called by: `btstack_run_loop_embedded_add_timer`, `btstack_run_loop_embedded_process_timers`, `btstack_run_loop_embedded_next_timer_delay_ms`
- Confidence: medium
