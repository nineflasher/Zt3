# BMS - `libc` functions

4 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_mem_fill`](#bms_mem_fill) | 0x08001238 | Fills a byte buffer with one value; argument order is (dst, count, value) |
| [`bms_memcmp_prefix`](#bms_memcmp_prefix) | 0x0800125C | Scans two buffers for a matching prefix; the match length is not returned |
| [`bms_memcpy_args_swap`](#bms_memcpy_args_swap) | 0x08008DD8 | Call memcpy with the first two arguments swapped, passing the length through |
| [`memcpy`](#memcpy) | 0x08001214 | Copies bytes forward, moving whole 32-bit words when both pointers are aligned |

## bms_mem_fill

**Fills a byte buffer with one value; argument order is (dst, count, value)**

Writes the byte param_3 to param_2 consecutive addresses starting at param_1, using a count-down loop. A zero count writes nothing. The argument order is pointer, count, value, which is not the memset order, so callers must be checked before assuming memset semantics. Its callers bms_4168_08001246 and bms_4168_0800124a are outside this packet.

| Parameter | Type | Description |
|---|---|---|
| `dst` | `ptr` | param_1, destination buffer |
| `count` | `s32` | param_2, number of bytes; zero writes nothing (a negative value would loop almost 2^32 times) |
| `value` | `u8` | param_3, byte value to store |

- Addresses by version: 4130: 0x08001238, 4139: 0x08001238, 4148: 0x08001238, 4168: 0x08001238
- Called by: `bms_4168_08001246`, `bms_4168_0800124a`
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
- Called by: `bms_4168_08003a50`, `bms_4168_08003c3c`, `bms_4168_08005768`, `bms_4168_08008060`, `bms_4168_08008788`, `bms_4168_0800eddc`
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
- Called by: `bms_4168_08003c3c`, `bms_4168_08008060`
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
- Called by: `bms_4168_08005cdc`, `bms_4168_08008060`, `bms_memcpy_args_swap`, `bms_4168_08008de8`, `bms_record_queue_pop`, `bms_frame_send_when_ready`, `bms_record_send_multiframe`, `bms_4168_0800d76c`, `bms_txq_enqueue`, `bms_4168_0800e8dc`, `bms_4168_0800e930`, `bms_4168_0800e988` ...
- Confidence: high
