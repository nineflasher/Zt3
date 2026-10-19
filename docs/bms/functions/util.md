# BMS - `util` functions

39 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_4139_dual_bank_step`](#bms_4139_dual_bank_step) | (removed) | Advance the active accumulator bank, dispatch its handler and flip banks after an accepted frame |
| [`bms_copy_bytes8`](#bms_copy_bytes8) | 0x08003700 | Copy exactly 8 bytes from source to destination, unrolled |
| [`bms_counter_accumulate`](#bms_counter_accumulate) | 0x080021B4 | Adds the step word at 0x20000698 into the 32-bit counter at 0x200006a0 |
| [`bms_dispatch_current_thunk`](#bms_dispatch_current_thunk) | 0x08008778 | Thunk that runs the current handler through bms_dispatch_call_current |
| [`bms_empty_callback`](#bms_empty_callback) | 0x0800366A | Empty no-op callback (bare return) |
| [`bms_empty_stub`](#bms_empty_stub) | 0x08002540 | Empty stub that returns immediately |
| [`bms_get_200005c1_bit0`](#bms_get_200005c1_bit0) | 0x0800E7A0 | Return bit 0 of the RAM byte at 0x200005C1 |
| [`bms_get_block_200005c0_ptr`](#bms_get_block_200005c0_ptr) | 0x0800E798 | Return the address of the RAM byte at 0x200005C0 |
| [`bms_get_block_20000e58_ptr`](#bms_get_block_20000e58_ptr) | 0x0800CE5C | Return the address of the RAM word at 0x20000E58 |
| [`bms_get_ram_word_200006a0`](#bms_get_ram_word_200006a0) | 0x08002184 | Returns the 32-bit RAM word at 0x200006A0; its purpose is not identified |
| [`bms_get_uid_word0`](#bms_get_uid_word0) | 0x08002190 | Returns word 0 of the 96-bit factory unique device ID |
| [`bms_get_uid_word1`](#bms_get_uid_word1) | 0x0800219C | Returns word 1 of the 96-bit factory unique device ID |
| [`bms_get_uid_word2`](#bms_get_uid_word2) | 0x080021A8 | Returns word 2 of the 96-bit factory unique device ID |
| [`bms_get_uid_word_by_index`](#bms_get_uid_word_by_index) | 0x0800A210 | Return factory UID word 0, 1 or 2 by index; 0 for any other index |
| [`bms_get_word_20001354`](#bms_get_word_20001354) | 0x080106BC | Return the 32-bit RAM word at 0x20001354 |
| [`bms_indirect_nibble_get`](#bms_indirect_nibble_get) | 0x08009D74 | Return the low nibble of the byte that the RAM pointer at 0x20005D00 points to |
| [`bms_lzrle_decompress`](#bms_lzrle_decompress) | 0x08001310 | Decodes a byte-oriented LZ/RLE stream of literals, zero runs and short back-references |
| [`bms_mode_match`](#bms_mode_match) | 0x0800F26E | Return 1 when the state block mode at +2 equals the argument, treating 6 as a wildcard |
| [`bms_noop_hook_08009a98`](#bms_noop_hook_08009a98) | 0x08009A98 | Empty hook: returns immediately with no side effects |
| [`bms_noop_hook_08009a9a`](#bms_noop_hook_08009a9a) | 0x08009A9A | Empty hook: returns immediately with no side effects |
| [`bms_rand_next`](#bms_rand_next) | 0x08001164 | Advances the LCG seed in RAM word 0x200006A8 and returns 31 pseudo-random bits |
| [`bms_record12_addr`](#bms_record12_addr) | 0x0800CE3C | Return the address of 12-byte record N in the table at 0x20000264 |
| [`bms_record_store_from_state`](#bms_record_store_from_state) | 0x08007FC0 | Store selected state-block fields into the record at 0x200024CC through bms_record_set_or_clear |
| [`bms_reply_buffer_get`](#bms_reply_buffer_get) | 0x0800E2A8 | Return the 24-byte reply buffer at 0x20002BFE, clearing it while the busy flag is clear |
| [`bms_request_is_done`](#bms_request_is_done) | 0x08003070 | Returns bit 0 of the request block's status word at offset 0x10 |
| [`bms_request_reset`](#bms_request_reset) | 0x08002E84 | Clears the done bit of a request block by writing 0xFFFFFFFE to its word at offset 0x10 |
| [`bms_rotate_word_bytes`](#bms_rotate_word_bytes) | 0x0800325C | Rotates the 4 bytes at param_1 by (param_2 & 3) positions, as in an AES RotWord step |
| [`bms_seq_restart_stamp`](#bms_seq_restart_stamp) | 0x08007F18 | Restart a timed step sequence: store the start stamp and clear the step word |
| [`bms_set_state_word`](#bms_set_state_word) | 0x08002E78 | Stores its argument into the RAM word at 0x200006A4 |
| [`bms_slot_pool_register`](#bms_slot_pool_register) | 0x0800A74C | Add a tagged entry to a 10-slot pool and append it to a linked list |
| [`bms_slot_table_find`](#bms_slot_table_find) | 0x08005EE4 | Find or allocate a 36-byte slot keyed by an 8-bit pair |
| [`bms_state_ptr_cache_set`](#bms_state_ptr_cache_set) | 0x08007F8C | Cache the address of the BMS state block in the pointer at 0x20000018 |
| [`bms_state_snapshot_submit`](#bms_state_snapshot_submit) | 0x08007F9C | Forward four 16-bit state-block fields and an argument to bms_4168_0800e820 |
| [`bms_tail_call_unnamed_a`](#bms_tail_call_unnamed_a) | 0x08007FFE | Tail-call thunk to bms_4168_0800e748 (not described in this packet) |
| [`bms_tail_call_unnamed_b`](#bms_tail_call_unnamed_b) | 0x08008780 | Tail-call thunk to bms_4168_0800fabc (not described in this packet) |
| [`bms_u8_to_bcd`](#bms_u8_to_bcd) | 0x08003514 | Convert an 8-bit binary value to packed BCD |
| [`bms_udiv32`](#bms_udiv32) | 0x08001110 | Unsigned 32-bit restoring division; returns the quotient |
| [`crc16_usb_compute`](#crc16_usb_compute) | 0x08004DA4 | Bitwise CRC-16, reflected poly 0x8005, init 0xFFFF, final complement |
| [`crc8_msb_compute`](#crc8_msb_compute) | 0x08003626 | CRC-8 over a byte buffer, MSB-first, init 0, polynomial supplied by the caller |

## bms_4139_dual_bank_step

**Advance the active accumulator bank, dispatch its handler and flip banks after an accepted frame**

With reset_request equal to 0 it calls bms_app_state_reset_legacy. Otherwise it adds step to the accumulator of the active bank (0x2000096C when DAT_20000116 is 0, else 0x20000868) and calls the handler taken from a flash function-pointer table at 0x0800F048, indexed by DAT_20000A61 for bank 0 or DAT_2000095D for bank 1, with step and the bank's record address (0x20000968 or 0x20000864). Both accumulators are reset to 0 when they exceed 499. When DAT_20000120 is set (raised by bms_frame_parse_legacy_4139 for an accepted frame), it is cleared and the active bank in DAT_20000116 is toggled.

| Parameter | Type | Description |
|---|---|---|
| `step` | `s32` | increment added to the active accumulator and passed to the handler |
| `reset_request` | `u32` | 0 selects the legacy state reset; nonzero runs the step |

**Notes:** The per-bank handlers in the flash table are not in this packet. The 499 wrap window may be a 500-tick period, which is a guess.

- Addresses by version: 4130: 0x08006DE0, 4139: 0x080072E0
- Called by: `bms_4139_08007238`
- Calls: `bms_app_state_reset_legacy`
- Confidence: medium

## bms_copy_bytes8

**Copy exactly 8 bytes from source to destination, unrolled**

Copies 8 bytes from src to dst one byte at a time, fully unrolled, with no loop, no length argument and no overlap handling. The fixed size of 8 matches a classic CAN payload or a small 8-byte record; the data it moves is not identified in this packet. Several callers in the 4139 and 4168 builds use it, so it is a shared helper for small fixed-size copies.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination, 8 bytes |
| `param_2` | `ptr` | source, 8 bytes |

**Notes:** The 8-byte size is certain; the payload type is a guess.

- Addresses by version: 4130: 0x08003700, 4139: 0x08003700, 4148: 0x08003700, 4168: 0x08003700
- Called by: `bms_4168_0800d76c`, `bms_4168_0800ddb0`, `bms_4168_0800f2e0`
- Confidence: medium

## bms_counter_accumulate

**Adds the step word at 0x20000698 into the 32-bit counter at 0x200006a0**

Leaf routine that does counter += step in place, where the counter is RAM word 0x200006a0 (read-write) and the step is RAM word 0x20000698 (read-only here). The only arithmetic is a 32-bit add, so the counter wraps at 2^32. It is called from bms_4168_08003662, which suggests a periodic time base or an event accumulator, but the packet does not show which.

**Notes:** The meaning of both RAM words and of the caller is not established in this packet; the description only covers the arithmetic.

- Addresses by version: 4130: 0x080021B4, 4139: 0x080021B4, 4148: 0x080021B4, 4168: 0x080021B4
- Called by: `bms_4168_08003662`
- Confidence: low

## bms_dispatch_current_thunk

**Thunk that runs the current handler through bms_dispatch_call_current**

Calls bms_dispatch_call_current (bms_4168_0800a88c), which uses the index byte at 0x20001340 to call a handler from the RAM pointer table at 0x20000578, then returns. It is called from the main-loop poll bms_4168_08010558.

- Addresses by version: 4130: 0x0800772C, 4139: 0x08007C2C, 4148: 0x08008478, 4168: 0x08008778
- Called by: `bms_4168_08010558`
- Calls: `bms_dispatch_call_current`
- Confidence: high

## bms_empty_callback

**Empty no-op callback (bare return)**

The body is a bare return and nothing is read or written. It has no direct callers, so it is reached only through a function pointer or a table that this packet does not resolve. It is most likely a no-op placeholder used as a default or unused hook in a handler or event table.

**Notes:** What the code does is certain; which table or event it is registered in is unknown.

- Addresses by version: 4130: 0x0800366A, 4139: 0x0800366A, 4148: 0x0800366A, 4168: 0x0800366A
- Confidence: medium

## bms_empty_stub

**Empty stub that returns immediately**

The body is a single bx lr with no reads or writes. It is a placeholder that is called for an optional hook or weak callback, so it does nothing by design. The packet's caller address 0x08002542 lies just after this function, so the caller list is probably a split or misaligned entry rather than a real call site.

**Notes:** The purpose is inferred from the empty body and the caller list. Which callback or hook it stands in for cannot be determined from this packet.

- Addresses by version: 4130: 0x08002540, 4139: 0x08002540, 4148: 0x08002540, 4168: 0x08002540
- Called by: `bms_4168_08002542`
- Confidence: low

## bms_get_200005c1_bit0

**Return bit 0 of the RAM byte at 0x200005C1**

Reads the byte at 0x200005C1 and returns its least significant bit, 0 or 1. It is read-only and has no other side effects. Callers are bms_4139_0800be74, bms_4168_08004774 and bms_4168_0800c96c.

**Returns** `u8`: bit 0 of the byte at 0x200005C1, 0 or 1

**Notes:** The meaning of the flag is not visible in this packet.

- Addresses by version: 4130: 0x0800CD24, 4139: 0x0800D30C, 4148: 0x0800E30C, 4168: 0x0800E7A0
- Called by: `bms_4168_08004774`, `bms_4168_0800c96c`
- Confidence: high

## bms_get_block_200005c0_ptr

**Return the address of the RAM byte at 0x200005C0**

Returns the address of the byte at 0x200005C0 without reading or writing it. The byte at 0x200005C1 is the next byte and is read by bms_get_200005c1_bit0, so the two may belong to one small block, though this packet does not prove it. Callers are bms_4130_08005d2c, bms_4139_0800be74, bms_4168_08006730, bms_4168_0800c96c and bms_4168_0800ec04.

**Returns** `ptr`: address of the byte at 0x200005C0

**Notes:** Only the address is certain. The structure of the block is inferred from the adjacent byte.

- Addresses by version: 4130: 0x0800CD1C, 4139: 0x0800D304, 4148: 0x0800E304, 4168: 0x0800E798
- Called by: `bms_state_refresh_scaled`, `bms_4168_0800c96c`, `bms_4168_0800ec04`
- Confidence: high

## bms_get_block_20000e58_ptr

**Return the address of the RAM word at 0x20000E58**

Returns the address of the 16-bit RAM object at 0x20000E58 without reading or writing it. Callers bms_4139_080040e4, bms_4139_08006f08, bms_4168_08004128, bms_4168_08004774 and bms_4168_08007a0c call it to get the object's address, and how they use the object is not visible here.

**Returns** `ptr`: address of the 16-bit word at 0x20000E58

**Notes:** The object's purpose is not visible from this packet. The name is based only on the address.

- Addresses by version: 4130: 0x0800BB00, 4139: 0x0800C0D0, 4148: 0x0800CA74, 4168: 0x0800CE5C
- Called by: `bms_4168_08004128`, `bms_4168_08004774`, `bms_4168_08007a0c`
- Confidence: high

## bms_get_ram_word_200006a0

**Returns the 32-bit RAM word at 0x200006A0; its purpose is not identified**

Returns DAT_200006a0, a RAM word that sits 8 bytes below the LCG seed at 0x200006A8. Nothing in this function shows what the word holds, and the function only reads it. Eight callers, including bms_4168_08001460 and bms_4168_0800352c, are outside this packet, so the meaning must come from them. It is named by address until its role is known.

**Returns** `u32`: raw value of the RAM word at 0x200006A0

- Addresses by version: 4130: 0x08002184, 4139: 0x08002184, 4148: 0x08002184, 4168: 0x08002184
- Called by: `bms_4168_08001460`, `bms_4168_080019d0`, `bms_4168_08002348`, `bms_4168_080023ca`, `bms_4168_08002470`, `bms_4168_08002868`, `bms_4168_0800352c`, `bms_4168_08003570`
- Confidence: low

## bms_get_uid_word0

**Returns word 0 of the 96-bit factory unique device ID**

Returns the UID symbol, the first 32-bit word of the factory-programmed 96-bit unique device ID. On STM32G0 this block is at 0x1FFF7590, which matches the addresses 0x1FFF7594 and 0x1FFF7598 read by the neighbouring getters. It is a read-only function with no side effects. Its caller bms_4168_0800a210 reads all three words.

**Returns** `u32`: unique ID bits 31-0

- Addresses by version: 4130: 0x08002190, 4139: 0x08002190, 4148: 0x08002190, 4168: 0x08002190
- Called by: `bms_get_uid_word_by_index`
- Confidence: high

## bms_get_uid_word1

**Returns word 1 of the 96-bit factory unique device ID**

Reads DAT_1FFF7594, the second 32-bit word of the factory unique device ID (base 0x1FFF7590 on STM32G0). It is a read-only getter with no side effects. Its caller bms_4168_0800a210 reads it together with the other two ID words.

**Returns** `u32`: unique ID bits 63-32

- Addresses by version: 4130: 0x0800219C, 4139: 0x0800219C, 4148: 0x0800219C, 4168: 0x0800219C
- Called by: `bms_get_uid_word_by_index`
- Confidence: high

## bms_get_uid_word2

**Returns word 2 of the 96-bit factory unique device ID**

Reads DAT_1FFF7598, the third 32-bit word of the factory unique device ID (base 0x1FFF7590 on STM32G0). It is a read-only getter with no side effects. Its caller bms_4168_0800a210 reads it together with the other two ID words.

**Returns** `u32`: unique ID bits 95-64

- Addresses by version: 4130: 0x080021A8, 4139: 0x080021A8, 4148: 0x080021A8, 4168: 0x080021A8
- Called by: `bms_get_uid_word_by_index`
- Confidence: high

## bms_get_uid_word_by_index

**Return factory UID word 0, 1 or 2 by index; 0 for any other index**

Dispatches to the three unique-ID word readers. Index 0 returns bms_get_uid_word0, index 1 returns bms_get_uid_word1 and index 2 returns bms_get_uid_word2. Any other index returns 0. It has no side effects.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | word index, 0 to 2 |

**Returns** `u32`: UID word for index 0 to 2, otherwise 0

- Addresses by version: 4130: 0x080091B0, 4139: 0x080096B0, 4148: 0x08009EFC, 4168: 0x0800A210
- Called by: `bms_4168_08003c3c`, `bms_4168_08008060`, `bms_4168_080082f0`
- Calls: `bms_get_uid_word0`, `bms_get_uid_word1`, `bms_get_uid_word2`
- Confidence: high

## bms_get_word_20001354

**Return the 32-bit RAM word at 0x20001354**

Takes no arguments and returns the value of the 32-bit RAM word at 0x20001354. The function is read-only. Its only caller in the packet is bms_4168_0800e9dc, and the code that writes the word is outside this packet.

**Returns** `u32`: value of the RAM word at 0x20001354

**Notes:** The word's meaning is not visible in this packet.

- Addresses by version: 4130: 0x0800E8BC, 4139: 0x0800EF10, 4148: 0x08010170, 4168: 0x080106BC
- Called by: `bms_4168_0800e9dc`
- Confidence: high

## bms_indirect_nibble_get

**Return the low nibble of the byte that the RAM pointer at 0x20005D00 points to**

Loads the pointer stored at RAM 0x20005D00, reads the byte it points to, and returns its low four bits (mask 0xF). There are no writes and no side effects. The pointer's target is not identified in this packet, so the byte is probably a configuration or status field reached through a pointer. Callers: bms_4168_080064a0 and bms_4168_0800faa0.

**Returns** `u32`: 0..15, the low nibble of the pointed-to byte

**Notes:** Byte width is inferred from the masking; the decompiler does not show a type for the pointer target.

- Addresses by version: 4130: 0x08008D14, 4139: 0x08009214, 4148: 0x08009A60, 4168: 0x08009D74
- Called by: `bms_4168_080064a0`, `bms_seq_state_reset`
- Confidence: medium

## bms_lzrle_decompress

**Decodes a byte-oriented LZ/RLE stream of literals, zero runs and short back-references**

Decodes a compressed stream from param_1 into param_2 until param_2 + param_3 is reached. Each token byte has a 3-bit literal field in its low bits (0 means an extension byte follows), a 4-bit length field in its high nibble (0 means an extension byte follows) and bit 3 as a back-reference flag. The decoder copies the literal run, then either copies length+2 bytes from output position minus a one-byte distance (overlapping copies repeat data) or writes length zero bytes. There are no bounds checks on input or output, and the function always returns 0.

| Parameter | Type | Description |
|---|---|---|
| `src` | `ptr` | param_1, compressed input stream, advanced as it is read |
| `dst` | `ptr` | param_2, output buffer, advanced as it is written |
| `out_len` | `s32` | param_3, number of output bytes to produce |

**Returns** `u32`: always 0

**Notes:** The literal count looks biased by one (the do-while copies field-1 bytes), and a zero extension byte would make the literal loop run almost 2^32 times. The format is inferred from the decompile and may be wrong in detail. No caller is analysed in this packet.

- Addresses by version: 4130: 0x08001310, 4139: 0x08001310, 4148: 0x08001310, 4168: 0x08001310
- Confidence: medium

## bms_mode_match

**Return 1 when the state block mode at +2 equals the argument, treating 6 as a wildcard**

Compares the 16-bit mode field at offset 2 of the BMS state block with param_2. It returns 1 when they are equal or when param_2 is 6, which matches any mode, and 0 otherwise. Mode values 5, 6 and 7 are the ones bms_can_status_frame_rx tests on the same field.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | unused by this function |
| `param_2` | `u32` | mode to test; 6 matches any mode |

**Returns** `u32`: 1 on match, 0 otherwise

**Notes:** The packet shows no direct callers; the function is reached through a table or callback.

- Addresses by version: 4130: 0x0800D754, 4139: 0x0800DD3C, 4148: 0x0800EDDE, 4168: 0x0800F26E
- Calls: `bms_ram_20000bdc_addr`
- Confidence: high

## bms_noop_hook_08009a98

**Empty hook: returns immediately with no side effects**

Bare return with no instructions: a placeholder callback that the build leaves empty. Nothing is read or written. It is called from bms_4168_08008294 and bms_4168_080082f0, so its purpose is set by what those callers gate around it, which is not in this packet.

**Notes:** Name carries the address because it is the same empty body as bms_noop_hook_08009a9a and bms_empty_callback.

- Addresses by version: 4130: 0x08008A38, 4139: 0x08008F38, 4148: 0x08009784, 4168: 0x08009A98
- Called by: `bms_4168_08008294`, `bms_4168_080082f0`
- Confidence: high

## bms_noop_hook_08009a9a

**Empty hook: returns immediately with no side effects**

Bare return with no instructions, identical in body to bms_noop_hook_08009a98. Its only caller in the packet is bms_4168_080082f0, which is also a caller of bms_noop_hook_08009a98, so the two are probably alternate slots of one callback sequence (inferred from the caller lists only).

**Notes:** The sequencing claim is an inference from the caller lists.

- Addresses by version: 4130: 0x08008A3A, 4139: 0x08008F3A, 4148: 0x08009786, 4168: 0x08009A9A
- Called by: `bms_4168_080082f0`
- Confidence: high

## bms_rand_next

**Advances the LCG seed in RAM word 0x200006A8 and returns 31 pseudo-random bits**

Linear congruential generator with the classic constants 1103515245 (0x41C64E6D) and 12345 (0x3039): seed = seed * 1103515245 + 12345 modulo 2^32, stored back into DAT_200006a8. The function returns bits 1 to 31 of the new state (seed >> 1). Nothing in this function seeds the generator, so the start value comes from whoever writes DAT_200006a8 elsewhere. The sequence is predictable and must not be used for security purposes.

**Returns** `u32`: pseudo-random value in 0..0x7FFFFFFF

- Addresses by version: 4130: 0x08001164, 4139: 0x08001164, 4148: 0x08001164, 4168: 0x08001164
- Confidence: high

## bms_record12_addr

**Return the address of 12-byte record N in the table at 0x20000264**

Computes base + 12 * index with base 0x20000264 (a multiply by 0xC and an add, with no bounds check) and returns the result as a pointer. It only computes the address and does not read or write memory. Five callers in BMS_4130, BMS_4139 and BMS_4168 use it to reach the entries of this table, so the 12-byte record layout is defined by those callers and not here.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | record index, not range checked |

**Returns** `ptr`: address of the 12-byte record

**Notes:** The decompiled return type is int, but the value is used as an address. The record fields are not visible in this function.

- Addresses by version: 4130: 0x0800BAE0, 4139: 0x0800C0B0, 4148: 0x0800CA54, 4168: 0x0800CE3C
- Called by: `bms_4168_08004488`, `bms_4168_08007d48`
- Confidence: high

## bms_record_store_from_state

**Store selected state-block fields into the record at 0x200024CC through bms_record_set_or_clear**

Reads two 32-bit fields at state+0x1EA and state+0x1EE, a 32-bit field at state+0x1C2 and a 16-bit field at state+0x112 from the block returned by bms_ram_20000bdc_addr, and passes them to bms_record_set_or_clear. That routine writes the six-word record at 0x200024CC, or clears it when the 16-bit argument is 0xFFFF. It is called from the main-loop poll bms_4168_08010558.

**Notes:** The field at +0x1C2 is not 4-byte aligned, so the compiler probably split that access into halfword reads; this is not verified.

- Addresses by version: 4130: 0x08006F78, 4139: 0x08007478, 4148: 0x08007CB8, 4168: 0x08007FC0
- Called by: `bms_4168_08010558`
- Calls: `bms_ram_20000bdc_addr`, `bms_record_set_or_clear`
- Confidence: medium

## bms_reply_buffer_get

**Return the 24-byte reply buffer at 0x20002BFE, clearing it while the busy flag is clear**

When the busy flag DAT_20002612 (used by bms_comm_service_step) is zero it clears the 24-byte buffer at 0x20002BFE through bms_4168_08001246, a two-argument routine that is not described yet, and then returns the buffer address. While the flag is set the buffer is returned unchanged. The buffer begins right after the 14-byte payload at 0x20002BF0 that the periodic send uses. Part of the message pool group.

**Returns** `ptr`: address of the 24-byte buffer at 0x20002BFE

**Notes:** The reason the buffer is left alone while busy is inferred from the flag name and the callers, not stated in the code. bms_4168_08001246 is not identified in this packet.

- Addresses by version: 4148: 0x0800DE54, 4168: 0x0800E2A8
- Called by: `bms_4168_08004774`, `bms_4168_08004a40`, `bms_4168_0800549c`, `bms_4168_080054f8`, `bms_4168_08005fc4`, `bms_4168_080068e8`, `bms_4168_08007704`, `bms_4168_08007d48`, `bms_4168_08007da4`, `bms_4168_0800c018`, `bms_4168_0800c96c`, `bms_4168_0800ce64` ...
- Calls: `bms_4168_08001246`
- Confidence: medium

## bms_request_is_done

**Returns bit 0 of the request block's status word at offset 0x10**

Returns the value of bit 0 of the word at offset 0x10 of the object at param_1, which is 0 or 1. Callers poll it to find out whether the request has completed, using the same word that bms_request_reset clears.

| Parameter | Type | Description |
|---|---|---|
| `req` | `ptr` | request block; the status word is at offset 0x10 |

**Returns** `u32`: bit 0 of the status word: 1 = done, 0 = pending

**Notes:** Reading bit 0 as 'done' is inferred from the reset value 0xFFFFFFFE in bms_request_reset. The name is a guess.

- Addresses by version: 4130: 0x08003070, 4139: 0x08003070, 4148: 0x08003070, 4168: 0x08003070
- Called by: `bms_4168_0800367c`, `bms_tim6_update_flag_poll`
- Confidence: low

## bms_request_reset

**Clears the done bit of a request block by writing 0xFFFFFFFE to its word at offset 0x10**

Writes 0xFFFFFFFE to the word at offset 0x10 of the object at param_1. That clears bit 0, which bms_request_is_done reads as the done flag, and sets all other bits to 1 as a sentinel. It is called from three paths before a request is started or polled.

| Parameter | Type | Description |
|---|---|---|
| `req` | `ptr` | request block; the status word is at offset 0x10 |

**Notes:** The 'request' and 'done' names are guesses from the one-bit read in bms_request_is_done. The structure's other fields are not visible in this packet.

- Addresses by version: 4130: 0x08002E84, 4139: 0x08002E84, 4148: 0x08002E84, 4168: 0x08002E84
- Called by: `bms_4168_0800367c`, `bms_tim6_update_flag_poll`, `bms_tim6_tim7_start`
- Confidence: low

## bms_rotate_word_bytes

**Rotates the 4 bytes at param_1 by (param_2 & 3) positions, as in an AES RotWord step**

Copies the 4-byte word at param_1 into a stack temporary and writes it back rotated: result byte i is original byte (k + i) mod 4, where k = param_2 & 3. With k = 1 this is a one-byte rotation of the word, the same as the RotWord step in AES key expansion, so it may be a helper in a crypto routine. The initial value copied from param_4 is overwritten before use and has no effect.

| Parameter | Type | Description |
|---|---|---|
| `word` | `ptr` | 4-byte buffer rotated in place |
| `rot` | `u32` | rotation count; only bits 1:0 are used |
| `unused` | `u32` | copied into a temporary and then overwritten; no effect |

**Notes:** Whether this is AES RotWord or a generic byte rotate is not visible in this packet. If it is a library routine, the library's name should replace the local one.

- Addresses by version: 4130: 0x0800325C, 4139: 0x0800325C, 4148: 0x0800325C, 4168: 0x0800325C
- Called by: `bms_seed_key_transform`
- Confidence: medium

## bms_seq_restart_stamp

**Restart a timed step sequence: store the start stamp and clear the step word**

Calls bms_4168_0800b904 (not described in this packet), clears the RAM word at 0x200008F4, stores the current time base from bms_tick_get in 0x200008E8, caches the state block pointer in 0x200008F0, clears bit 8 (0x0100) of state+0x196, and calls bms_4168_0800f288 (not described in this packet). It is called from the main-loop poll bms_4168_08010558 and does not wait by itself.

- Addresses by version: 4130: 0x08006ED0, 4139: 0x080073D0, 4148: 0x08007C10, 4168: 0x08007F18
- Called by: `bms_4168_08010558`
- Calls: `bms_tick_get`, `bms_record_queue_flush`, `bms_ram_20000bdc_addr`, `bms_chan_pool_init`
- Confidence: medium

## bms_set_state_word

**Stores its argument into the RAM word at 0x200006A4**

Trivial store of the 32-bit argument into the global at 0x200006A4, which the routine only writes. It is called from bms_4168_0800a130 and bms_4168_0800a2e0, so the word is probably a mode or state selector that those paths set. The meaning of the value is not visible in this packet.

| Parameter | Type | Description |
|---|---|---|
| `value` | `u32` | value to store |

**Notes:** The name is generic because the word's role is unknown. Renaming should wait until the callers in the later waves are documented.

- Addresses by version: 4130: 0x08002E78, 4139: 0x08002E78, 4148: 0x08002E78, 4168: 0x08002E78
- Called by: `bms_sysclk_hse_pll_bringup`, `bms_sysclk_hsi16_switch`
- Confidence: low

## bms_slot_pool_register

**Add a tagged entry to a 10-slot pool and append it to a linked list**

Allocates one of ten 20-byte slots at 0x200013A0 and appends it to a singly linked list headed at 0x2000133C, with the link word at slot+16. The scan takes the first slot whose first byte is nonzero, clears that byte to mark the slot used, and stores the u8 tag at slot+1 and three 32-bit payload words at slot+4, +8 and +12. The list is walked for a node with the same tag; if one is found, the function returns 1 without linking, which leaves the new slot marked used but unreachable. Otherwise the new node is appended, the count at 0x20001344 is incremented, and the function returns 1. It returns 0 when the count is already 10 or no free slot is found.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | tag byte, stored at slot+1 and compared for duplicates |
| `param_2` | `u32` | payload word stored at slot+4 |
| `param_3` | `u32` | payload word stored at slot+8 |
| `param_4` | `u32` | payload word stored at slot+12 |

**Returns** `u32`: 1 on success or duplicate tag, 0 when the pool is full

**Notes:** The duplicate path leaks a pool slot, which is a plausible defect since the slot is never freed. The payload words' meaning is not in this packet. Callers: bms_4168_08005cdc, bms_4168_080082f0, bms_4168_0800a8a0, bms_4168_0800e9dc. The dispatch array at 0x20000578 used by bms_dispatch_call_current is a separate structure.

- Addresses by version: 4130: 0x080097E4, 4139: 0x08009D1C, 4148: 0x0800A438, 4168: 0x0800A74C
- Called by: `bms_4168_08005cdc`, `bms_4168_080082f0`, `bms_4168_0800a8a0`, `bms_4168_0800e9dc`
- Confidence: medium

## bms_slot_table_find

**Find or allocate a 36-byte slot keyed by an 8-bit pair**

Searches a table of 36-byte (0x24) records. param_1 points to a header whose pointer at +0 is the record array and whose u16 at +4 is the record count. Each record has key byte 0, key byte 1, and a state byte at +2 where 1 marks a free slot. With param_4 == 0 (strict mode) the function first returns 0 if the reversed pair (param_3, param_2) is in use, then returns the record keyed (param_2, param_3) if one exists, and otherwise the first free slot. With param_4 != 0 it skips the reversed check and returns the record keyed (param_2, param_3) or the first free slot. It returns a record pointer, or 0 when nothing matches and no slot is free.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | table header: +0 record array pointer, +4 u16 record count |
| `param_2` | `u8` | key byte A |
| `param_3` | `u8` | key byte B |
| `param_4` | `u32` | mode: 0 = strict (reject reversed pair), nonzero = lenient |

**Returns** `ptr`: pointer to the matching or newly free record, or 0

**Notes:** The table most likely maps a link between two 8-bit IDs to a slot; what the IDs are is not in this packet. The state value 1 = free is read from the loops and should be checked against the writers. The record stride 0x24 and the header layout are certain from the code.

- Addresses by version: 4130: 0x08005668, 4139: 0x08005884, 4148: 0x08005D90, 4168: 0x08005EE4
- Called by: `bms_j1939_tp_rx_dispatch`, `bms_4168_0800ff8e`
- Confidence: medium

## bms_state_ptr_cache_set

**Cache the address of the BMS state block in the pointer at 0x20000018**

Stores the value returned by bms_ram_20000bdc_addr in the global pointer at 0x20000018. bms_4168_08007f9c reads that pointer back, so it is a cached base pointer for the state block. Nothing else is written.

- Addresses by version: 4130: 0x08006F44, 4139: 0x08007444, 4148: 0x08007C84, 4168: 0x08007F8C
- Called by: `bms_4168_08010558`
- Calls: `bms_ram_20000bdc_addr`
- Confidence: high

## bms_state_snapshot_submit

**Forward four 16-bit state-block fields and an argument to bms_4168_0800e820**

Reads the cached state block pointer at 0x20000018 and passes the 16-bit fields at offsets 0x124, 0x126, 0x194 and 0x196 together with forward_arg to bms_4168_0800e820, which is not described in this packet. The call shape suggests a snapshot or report of these four fields, but that role is inferred. It is called from the main-loop poll bms_4168_08010558.

| Parameter | Type | Description |
|---|---|---|
| `forward_arg` | `u32` | forwarded unchanged to bms_4168_0800e820 |

- Addresses by version: 4130: 0x08006F54, 4139: 0x08007454, 4148: 0x08007C94, 4168: 0x08007F9C
- Called by: `bms_4168_08010558`
- Calls: `bms_pd0_indicator_step`
- Confidence: low

## bms_tail_call_unnamed_a

**Tail-call thunk to bms_4168_0800e748 (not described in this packet)**

Calls bms_4168_0800e748 with no arguments and returns. It is the only statement in the function and is called from the main-loop poll bms_4168_08010558. The callee is described in another packet.

- Addresses by version: 4130: 0x08006FB6, 4139: 0x080074B6, 4148: 0x08007CF6, 4168: 0x08007FFE
- Called by: `bms_4168_08010558`
- Calls: `bms_soc_band_classify`
- Confidence: high

## bms_tail_call_unnamed_b

**Tail-call thunk to bms_4168_0800fabc (not described in this packet)**

Calls bms_4168_0800fabc with no arguments and returns. The target is described in another packet. It is called from the main-loop poll bms_4168_08010558.

- Addresses by version: 4130: 0x08007734, 4139: 0x08007C34, 4148: 0x08008480, 4168: 0x08008780
- Called by: `bms_4168_08010558`
- Calls: `bms_fault_record_service`
- Confidence: high

## bms_u8_to_bcd

**Convert an 8-bit binary value to packed BCD**

Converts a byte to packed BCD by repeatedly subtracting 10 and counting the tens (the subtraction is kept to 8 bits). The result is the ones digit in the low nibble and the tens count in the high nibble. Correct for inputs 0..159; above 159 the tens count exceeds 15 and is masked to 4 bits, so the result wraps. No globals, registers or memory are touched. Callers bms_4168_08002704 and bms_4168_080027a4 likely format a value for a byte-oriented protocol field.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | binary value, valid range 0..159 |

**Returns** `u8`: packed BCD: tens in bits 7:4, ones in bits 3:0

- Addresses by version: 4130: 0x08003514, 4139: 0x08003514, 4148: 0x08003514, 4168: 0x08003514
- Called by: `bms_4168_08002704`, `bms_4168_080027a4`
- Confidence: high

## bms_udiv32

**Unsigned 32-bit restoring division; returns the quotient**

Bit-serial restoring division for unsigned 32-bit operands, needed because Cortex-M0+ has no hardware divider. For k = 31 down to 0 it tests divisor <= dividend >> k (equivalent to divisor << k <= dividend, without overflow), subtracts divisor << k when the test passes and sets quotient bit k. The local dividend becomes the remainder and is discarded, so only the quotient is returned. With a zero divisor every test passes and the result is 0xFFFFFFFF.

| Parameter | Type | Description |
|---|---|---|
| `dividend` | `u32` | param_1, numerator; the local copy is reduced to the remainder and not returned |
| `divisor` | `u32` | param_2, denominator; zero gives quotient 0xFFFFFFFF |

**Returns** `u32`: floor(param_1 / param_2)

**Notes:** Could be a hand-written replacement for libgcc __aeabi_uidiv; the name is generic, not confirmed.

- Addresses by version: 4130: 0x08001110, 4139: 0x08001110, 4148: 0x08001110, 4168: 0x08001110
- Called by: `bms_4168_0800113c`, `bms_4168_08001278`, `bms_4168_080021ec`, `bms_4168_08003140`, `bms_4168_080034b4`, `bms_4168_0800379c`, `bms_4168_08003868`, `bms_4168_080039e8`, `bms_4168_08004128`, `bms_4168_08004a40`, `bms_4168_080054f8`, `bms_state_refresh_scaled` ...
- Confidence: high

## crc16_usb_compute

**Bitwise CRC-16, reflected poly 0x8005, init 0xFFFF, final complement**

Bitwise CRC-16 over len bytes starting at data. The register starts at 0xFFFF, each byte is XORed into its low half, and then 8 steps shift right and XOR 0xA001 (reflected 0x8005) whenever the LSB is set. The result is complemented (~crc & 0xFFFF). These parameters match CRC-16/USB. CRC-16/MODBUS uses the same polynomial and initial value without the final complement, so the caller's expected form must be checked before reusing it for Modbus frames. No globals, peripherals or memory writes.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | data buffer |
| `param_2` | `u8` | byte count; 0 means none |

**Returns** `u16`: CRC-16 of the buffer, complemented

**Notes:** Callers in the packet: bms_4139_08007108, bms_4168_08005128, bms_4168_08007c10, bms_4168_080106c8. Whether the CRC is CRC-16/USB or a custom variant is inferred from the constants; the frame it protects is not identified here.

- Addresses by version: 4130: 0x08004590, 4139: 0x080047A4, 4148: 0x08004C58, 4168: 0x08004DA4
- Called by: `bms_4168_08005128`, `bms_frame_parse_legacy_4168`, `bms_seed_key_transform`
- Confidence: high

## crc8_msb_compute

**CRC-8 over a byte buffer, MSB-first, init 0, polynomial supplied by the caller**

Computes an 8-bit CRC over len bytes starting at data, with the polynomial passed in poly and an initial value of 0. Bytes are processed MSB first with no reflection and no final XOR. For each bit the CRC is shifted left and XORed with poly when the old bit 7 was set, then XORed with poly again when the data bit is set; this is the standard step crc = (crc << 1) ^ (((crc7 ^ data_bit) != 0) ? poly : 0). Common polynomials for this form are 0x07 (CRC-8/SMBus) and 0x31 (Dallas/Maxim); the caller's choice is not visible in this packet. Only general-purpose registers are used.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | data buffer (byte array) |
| `param_2` | `u8` | number of bytes; 0 means none |
| `param_3` | `u8` | CRC polynomial, normal (non-reflected) form |

**Returns** `u8`: CRC-8 of the buffer

**Notes:** The decompiler shows a void return, but the CRC accumulator is the only live value at exit, so the result is presumably returned in r0; this is unverified. The only caller in the packet is bms_4168_0800b7bc, which would confirm it.

- Addresses by version: 4130: 0x08003626, 4139: 0x08003626, 4148: 0x08003626, 4168: 0x08003626
- Called by: `bms_4168_0800b7bc`
- Confidence: medium
