# BMS - `libc` functions

6 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_mem_fill`](#bms_mem_fill) | 0x08001238 | Fills a byte buffer with one value; argument order is (dst, count, value) |
| [`bms_mem_zero`](#bms_mem_zero) | 0x08001246 | Zero-fills count bytes at dst by calling bms_mem_fill with value 0 |
| [`bms_memcmp_prefix`](#bms_memcmp_prefix) | 0x0800125C | Scans two buffers for a matching prefix; the match length is not returned |
| [`bms_memcpy_args_swap`](#bms_memcpy_args_swap) | 0x08008DD8 | Call memcpy with the first two arguments swapped, passing the length through |
| [`memcpy`](#memcpy) | 0x08001214 | Copies bytes forward, moving whole 32-bit words when both pointers are aligned |
| [`memset`](#memset) | 0x0800124A | Standard memset: fills count bytes at dst with value and returns dst |

## bms_mem_fill

**Fills a byte buffer with one value; argument order is (dst, count, value)**

Writes the byte param_3 to param_2 consecutive addresses starting at param_1, using a count-down loop. A zero count writes nothing. The argument order is pointer, count, value, which is not the memset order, so callers must be checked before assuming memset semantics. Its callers bms_4168_08001246 and bms_4168_0800124a are outside this packet.

| Parameter | Type | Description |
|---|---|---|
| `dst` | `ptr` | param_1, destination buffer |
| `count` | `s32` | param_2, number of bytes; zero writes nothing (a negative value would loop almost 2^32 times) |
| `value` | `u8` | param_3, byte value to store |

- Addresses by version: 4130: 0x08001238, 4139: 0x08001238, 4148: 0x08001238, 4168: 0x08001238
- Called by: `bms_mem_zero`, `memset`
- Confidence: high

## bms_mem_zero

**Zero-fills count bytes at dst by calling bms_mem_fill with value 0**

Thin wrapper: bms_mem_fill (bms_4168_08001238) with the value argument set to 0, so it writes count zero bytes starting at dst. It returns nothing and has no other side effects. bms_4168_080033ce uses it to clear its output before unpacking.

| Parameter | Type | Description |
|---|---|---|
| `dst` | `ptr` | param_1, start of the buffer to clear |
| `count` | `u32` | param_2, number of bytes to clear |

- Addresses by version: 4130: 0x08001246, 4139: 0x08001246, 4148: 0x08001246, 4168: 0x08001246
- Called by: `bms_pack_7bit_string`, `bms_unpack_7bit_string`, `bms_extflash_journal_step`, `bms_4168_08003bf0`, `bms_extlog_request_dispatch`, `bms_session_state_reset`, `bms_state_restore_or_init`, `bms_i2c_bb_bus_init`, `bms_i2c_bb_bus_release`, `bms_tim6_tim7_start`, `bms_4168_0800c80c`, `bms_telemetry_sched_16_step` ...
- Calls: `bms_mem_fill`
- Confidence: high

## bms_memcmp_prefix

**Scans two buffers for a matching prefix; the match length is not returned**

Increments an index while it is below param_3 and the bytes param_1[index] and param_2[index] are equal. This is the loop body of a memcmp-style helper, but the decompiled function has no return value, so the match length is either dropped or read by callers from a register that is not visible here. Six callers are listed in the call graph (bms_4168_08003a50 and others), none analysed in this packet.

| Parameter | Type | Description |
|---|---|---|
| `buf1` | `ptr` | param_1, first buffer |
| `buf2` | `ptr` | param_2, second buffer |
| `max` | `u32` | param_3, maximum number of bytes to compare |

**Notes:** The computed index is never returned in this decompile, so the purpose is inferred from the loop alone; check the callers before relying on it.

- Addresses by version: 4130: 0x0800125C, 4139: 0x0800125C, 4148: 0x0800125C, 4168: 0x0800125C
- Called by: `bms_extflash_journal_step`, `bms_4168_08003c3c`, `bms_extlog_request_dispatch`, `bms_state_restore_or_init`, `bms_flash_erase_program_page`, `bms_fw_upload_handle`
- Confidence: low

## bms_memcpy_args_swap

**Call memcpy with the first two arguments swapped, passing the length through**

Calls memcpy (bms_4168_08001214) with dst as the destination and src as the source, leaving the third argument register untouched, so the length is whatever the caller set. Callers in this packet are bms_4168_08003C3C and bms_4168_08008060.

| Parameter | Type | Description |
|---|---|---|
| `src` | `ptr` | source address |
| `dst` | `ptr` | destination address |

**Notes:** The swap is read from the register order in the wrapper; the length argument is not set here.

- Addresses by version: 4130: 0x08007D8C, 4139: 0x0800828C, 4148: 0x08008AD8, 4168: 0x08008DD8
- Called by: `bms_4168_08003c3c`, `bms_state_restore_or_init`
- Calls: `memcpy`
- Confidence: medium

## memcpy

**Copies bytes forward, moving whole 32-bit words when both pointers are aligned**

Copies param_3 bytes from param_2 to param_1 in increasing address order. If both pointers are 4-byte aligned it copies words while at least four bytes remain, then copies the rest one byte at a time; otherwise it copies bytes only. There is no overlap handling, so a destination above an overlapping source is corrupted. The decompiled routine has no return value, which differs from the newlib memcpy that returns dst.

| Parameter | Type | Description |
|---|---|---|
| `dst` | `ptr` | param_1, destination buffer |
| `src` | `ptr` | param_2, source buffer |
| `n` | `u32` | param_3, byte count |

**Notes:** Named after the C library routine by behaviour; the implementation is custom and not newlib's.

- Addresses by version: 4130: 0x08001214, 4139: 0x08001214, 4148: 0x08001214, 4168: 0x08001214
- Called by: `bms_history_ring_commit`, `bms_state_restore_or_init`, `bms_memcpy_args_swap`, `bms_flash_write_bytes`, `bms_record_queue_pop`, `bms_frame_send_when_ready`, `bms_record_send_multiframe`, `bms_telemetry_block_fill_16`, `bms_txq_enqueue`, `bms_tp_send_block_5`, `bms_tp_send_block_4`, `bms_tp_send_block_6` ...
- Confidence: high

## memset

**Standard memset: fills count bytes at dst with value and returns dst**

Implements C memset(dst, value, count) with the standard argument order. It forwards to bms_mem_fill (bms_4168_08001238) as (dst, count, value), so only the low byte of value is stored, and it returns the destination pointer unchanged. The behaviour is that of memset, so the library name is used.

| Parameter | Type | Description |
|---|---|---|
| `dst` | `ptr` | param_1, destination buffer |
| `value` | `u32` | param_2, fill value (low byte stored) |
| `count` | `u32` | param_3, number of bytes to fill |

**Returns** `ptr`: dst, the original destination pointer

- Addresses by version: 4130: 0x0800124A, 4139: 0x0800124A, 4148: 0x0800124A, 4168: 0x0800124A
- Calls: `bms_mem_fill`
- Confidence: high
