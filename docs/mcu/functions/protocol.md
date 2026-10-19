# MCU - `protocol` functions

3 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_frame_build_checksum16`](#mcu_frame_build_checksum16) | 0x0800D4A8 | Build a framed message with three header bytes, a payload and a 16-bit checksum trailer |
| [`mcu_frame_ring_pop_to_desc`](#mcu_frame_ring_pop_to_desc) | 0x0800AB12 | Hand the next queued 256-byte frame from a 4-slot ring to a descriptor when the channel is ready |
| [`mcu_state_reset_load_key16`](#mcu_state_reset_load_key16) | 0x08006AE0 | Reset 17 state fields and write the 16-byte ASCII constant AQ5GoxXTs8j3BG2Q to 0x20002054 |

## mcu_frame_build_checksum16

**Build a framed message with three header bytes, a payload and a 16-bit checksum trailer**

Validates the object, the payload pointer, the payload length (below 0x6FA) and the capacity (payload + 5 must fit the halfword at +8). It sets the state byte at +2 to 3 and copies param_4 and param_5 into object bytes +0 and +1. The frame buffer at +4 receives byte 0 = param_3, byte 1 = param_6, byte 2 = param_7, then the payload, then a 16-bit trailer equal to the complement of (param_3 + param_6 + param_7 + sum of payload bytes), stored little-endian. The frame length (payload + 5) is stored as a halfword at +0x0C and the counter at +0x1A is cleared. The repeat count at +0x1C is ceil(param_10 / period), where period is the halfword at +0x14. Param_2 is not used.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | frame object: buffer pointer +4, capacity u16 +8, state +2, length +0x0C, period u16 +0x14, counter +0x1A, repeat count +0x1C |
| `param_2` | `u32` | not used |
| `param_3` | `u8` | header byte 0 (also a checksum term) |
| `param_4` | `u8` | stored at object byte +0 |
| `param_5` | `u8` | stored at object byte +1 |
| `param_6` | `u8` | header byte 1 (also a checksum term) |
| `param_7` | `u8` | header byte 2 (also a checksum term) |
| `param_8` | `ptr` | payload source, must be non-null |
| `param_9` | `u32` | payload length in bytes, below 0x6FA |
| `param_10` | `s32` | total to cover, divided by the period to give the repeat count |

**Returns** `bool`: 1 when the frame was built, 0 when a check failed

**Notes:** The meaning of the header bytes and of object bytes +0 and +1 is not visible in this packet. The period is assumed non-zero because it is used as a divisor.

- Addresses by version: 12b: 0x0800D184, 143: 0x0800D400, 152: 0x0800D448, 0160: 0x0800D4A8
- Called by: `mcu_0160_0800d0b0`
- Confidence: medium

## mcu_frame_ring_pop_to_desc

**Hand the next queued 256-byte frame from a 4-slot ring to a descriptor when the channel is ready**

Service step for a 4-entry frame ring inside a context structure. A busy guard at context +0x00 and +0x02 makes it return at once if either byte is set; otherwise it sets +0x02. If the descriptor's pending bit (bit 0 of desc word 0) is set, it first checks bit (4 * channel - 3) of status word 0. If that bit is clear it clears the busy flag and returns. If it is set, it sets the same bit in status word 1 as a latch and clears the descriptor's pending bit. Then, if the ring's read index (+0x404) differs from its write index (+0x405), it resets the 32-bit idle counter at +0x604, points desc word 3 at slot+8 and desc word 1 at the slot length (slot+4; each slot is 0x100 bytes), sets the pending bit, advances the read index modulo 4 and increments the count at +0x406. Otherwise, if the descriptor is not pending, it increments the 32-bit idle counter at +0x604 and saturates it at 20 (0x14). It then clears the busy flag and returns.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | unused by the decompiled body |
| `param_2` | `ptr` | status words: word 0 = live input bits, word 1 = latched bits |
| `param_3` | `ptr` | ring context: busy flags at +0x00/+0x02, 4 slots of 0x100 bytes from +0x08, indices at +0x404/+0x405, count +0x406, idle counter +0x604 |
| `param_4` | `ptr` | descriptor: word 0 bit 0 = pending, word 1 = length, word 3 = data pointer |
| `param_5` | `s32` | channel number; selects bit (4 * channel - 3) of the status words |

**Notes:** The mechanism is clear from the code. The purpose (a transmit or receive frame ring, and what the status bits mean) is inferred.

- Addresses by version: 12b: 0x0800A9BA, 143: 0x0800ABE2, 152: 0x0800AA9E, 0160: 0x0800AB12
- Called by: `mcu_0160_0800a0b0`
- Confidence: medium

## mcu_state_reset_load_key16

**Reset 17 state fields and write the 16-byte ASCII constant AQ5GoxXTs8j3BG2Q to 0x20002054**

Zeroes 17 RAM fields: nine byte flags and counters at 0x200006B8..0x200006C0, and eight words at 0x200006C4..0x200006E0. It then writes four 32-bit constants to 0x20002054, 0x20002058, 0x2000205C and 0x20002060, which in memory order spell the 16-byte ASCII string AQ5GoxXTs8j3BG2Q. The string looks like a fixed key, password or seed, but this function does not show its use. Called from mcu_0160_0800665c and mcu_0160_0800672c. Present only in the 0160 build.

**Notes:** The constant's use is in another function, probably a comparison or key derivation. Check the callers.

- Addresses by version: 0160: 0x08006AE0
- Called by: `mcu_0160_0800665c`, `mcu_0160_0800672c`
- Confidence: medium
