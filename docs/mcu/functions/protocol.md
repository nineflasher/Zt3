# MCU - `protocol` functions

11 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_can_ef00_message_send`](#mcu_can_ef00_message_send) | 0x0800CDD8 | Send a PGN 0xEF00 message: one frame for up to 5 bytes, otherwise start a TP session |
| [`mcu_can_tp_rx_dispatch`](#mcu_can_tp_rx_dispatch) | 0x0800D038 | Route an incoming J1939 TP frame: start a session on RTS, otherwise hand it to the open sessions |
| [`mcu_can_tp_sender_step`](#mcu_can_tp_sender_step) | 0x0800D10A | Advance the J1939 TP sender state machine by one event: RTS, data blocks, CTS wait, end of message |
| [`mcu_can_tp_session_start`](#mcu_can_tp_session_start) | 0x0800D0B0 | Find or allocate a strict pair-table session for a multi-packet send and build its frame |
| [`mcu_can_tp_timeout_tick`](#mcu_can_tp_timeout_tick) | 0x0800B65C | Advance a J1939 TP session timer; on expiry report a timeout and send TP.CM abort |
| [`mcu_frame_build_5aa5_checksum`](#mcu_frame_build_5aa5_checksum) | 0x08006460 | Build a 5A A5 frame: 7-byte header, payload, and a little-endian byte-sum checksum |
| [`mcu_frame_build_checksum16`](#mcu_frame_build_checksum16) | 0x0800D4A8 | Build a framed message with three header bytes, a payload and a 16-bit checksum trailer |
| [`mcu_frame_ring_pop_to_desc`](#mcu_frame_ring_pop_to_desc) | 0x0800AB12 | Hand the next queued 256-byte frame from a 4-slot ring to a descriptor when the channel is ready |
| [`mcu_msg_ring2_enqueue_frames`](#mcu_msg_ring2_enqueue_frames) | 0x0800BC70 | Split a payload into 8-byte CAN records and push them onto message ring 2 |
| [`mcu_state_reset_load_key16`](#mcu_state_reset_load_key16) | 0x08006AE0 | Reset 17 state fields and write the 16-byte ASCII constant AQ5GoxXTs8j3BG2Q to 0x20002054 |
| [`mcu_telemetry_group_get`](#mcu_telemetry_group_get) | 0x0800C6F0 | Return the 8-byte value group for a telemetry request ID, packed into the shared buffer at 0x20000310 |

## mcu_can_ef00_message_send

**Send a PGN 0xEF00 message: one frame for up to 5 bytes, otherwise start a TP session**

Sends a J1939 PGN 0xEF00 proprietary message. Payloads under six bytes go out as one 29-bit frame built by mcu_can_ef00_frame_build (priority 6, header bytes 1, the given header bytes, source and destination addresses), then queued with mcu_can_frame_enqueue. Longer payloads go through mcu_0160_0800d0b0 (mcu_can_tp_session_start) on the session table at 0x200027BC, using the same arguments.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | source address |
| `param_2` | `u32` | destination address |
| `param_3` | `u32` | payload length in bytes |
| `param_4` | `u32` | header byte 1 of the message |
| `param_5` | `u32` | header byte 2 of the message |
| `param_6` | `ptr` | payload source |

**Notes:** The header semantics are not documented in this packet.

- Addresses by version: 12b: 0x0800CABC, 143: 0x0800CD38, 152: 0x0800CD78, 0160: 0x0800CDD8
- Calls: `mcu_can_frame_enqueue`, `mcu_can_tp_session_start`, `mcu_can_ef00_frame_build`
- Confidence: medium

## mcu_can_tp_rx_dispatch

**Route an incoming J1939 TP frame: start a session on RTS, otherwise hand it to the open sessions**

Receive-side dispatcher for J1939 transport-protocol frames (PGN 0xEC00 TP.CM and 0xEB00 TP.DT, group with mcu_can_tp_session_start). For a TP.CM frame whose first data byte is 0x10 (request to send), it asks the accept callback at table +0x08 whether to accept, using the source and destination addresses. If accepted it finds or allocates the receive session with mcu_pair_table_find_or_alloc in mode 1 (lookup or allocate) and passes the frame to mcu_can_tp_session_handle_frame (mcu_0160_0800d1f0). Any other TP.CM or TP.DT frame goes to that handler for every 36-byte session entry in the table, counted at table +0x04. Other PGNs are ignored.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TP table header: entry base +0x00, u16 entry count +0x04, accept callback +0x08, handler callback in the entries |
| `param_2` | `ptr` | received CAN frame: identifier word at +0x00, first data byte at +0x05 |

**Notes:** The callback signatures are taken from the code shape only.

- Addresses by version: 12b: 0x0800CD14, 143: 0x0800CF90, 152: 0x0800CFD8, 0160: 0x0800D038
- Called by: `mcu_0160_0800cd6c`
- Calls: `mcu_pair_table_find_or_alloc`, `mcu_can_tp_session_handle_frame`
- Confidence: medium

## mcu_can_tp_sender_step

**Advance the J1939 TP sender state machine by one event: RTS, data blocks, CTS wait, end of message**

Sender side state machine of a J1939 transport-protocol session for PGN 0xEF00 (group with mcu_can_tp_timeout_tick and mcu_can_tp_rx_dispatch). The state byte at +0x02 selects the action. State 3 builds and sends the TP.CM request to send (mcu_can_tp_rts_frame_build), sets the timer limit to 1250 ms divided by the tick period at +0x14, and moves to state 4 (wait for CTS). States 4, 6, 7, 9 and 10 pass to mcu_0160_0800b65c (the timeout tick). State 5 sends 7-byte TP.DT frames (mcu_can_tp_dt_frame_build) from the offset at +0x0A, paced by the burst counter at +0x1A and the burst size at +0x1C. It moves to state 6 when the block end at +0x12 is reached, or to state 9 (end-of-message wait) when the total length at +0x0C is covered. Frames go out through the send callback at ops +0x0C.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TP sender session: state +0x02, id bytes +0x00 and +0x01, data pointer +0x04, offset +0x0A, total +0x0C, block end +0x12, tick period +0x14, timer +0x16, limit +0x18, burst counter +0x1A, burst size +0x1C |
| `param_2` | `ptr` | operations table: send callback at +0x0C |

**Notes:** Several states (7, 10) only pass to the timeout tick here; their own transitions are in other code.

- Addresses by version: 12b: 0x0800CDE6, 143: 0x0800D062, 152: 0x0800D0AA, 0160: 0x0800D10A
- Called by: `mcu_0160_0800cdcc`
- Calls: `mcu_can_tp_timeout_tick`, `mcu_can_tp_rts_frame_build`, `mcu_can_tp_dt_frame_build`
- Confidence: medium

## mcu_can_tp_session_start

**Find or allocate a strict pair-table session for a multi-packet send and build its frame**

Multi-packet send entry used by mcu_can_ef00_message_send for payloads of six bytes or more (group with mcu_can_tp_rx_dispatch). It finds or allocates a session for the (source, destination) pair with mcu_pair_table_find_or_alloc in strict mode (mode 0, which refuses a reversed duplicate). When it gets a session it passes the arguments to mcu_frame_build_checksum16, which fills the session frame and its repeat count and returns that result; when no session is free it returns 0 and queues nothing.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TP table header (pair table at 0x200027BC) |
| `param_2` | `u32` | service argument, 7 at the call site from mcu_can_ef00_message_send |
| `param_3` | `u32` | argument, 1 at the call site |
| `param_4` | `u32` | source address |
| `param_5` | `u32` | destination address |
| `param_6` | `u32` | header byte 1 |
| `param_7` | `u32` | header byte 2 |
| `param_8` | `ptr` | payload source |
| `param_9` | `u32` | payload length in bytes |
| `param_10` | `s32` | total to cover, passed through; 0 at the call site |

**Returns** `bool`: 1 when the frame was built, 0 when no session was available or a check failed

- Addresses by version: 12b: 0x0800CD8C, 143: 0x0800D008, 152: 0x0800D050, 0160: 0x0800D0B0
- Called by: `mcu_can_ef00_message_send`
- Calls: `mcu_pair_table_find_or_alloc`, `mcu_frame_build_checksum16`
- Confidence: medium

## mcu_can_tp_timeout_tick

**Advance a J1939 TP session timer; on expiry report a timeout and send TP.CM abort**

Timer tick for one J1939 transport-protocol session (group with mcu_can_tp_sender_step and mcu_can_tp_rx_dispatch). It increments the 16-bit timer at session +0x16 and compares it with the limit at +0x18. When the limit is reached it calls the error callback at ops +0x04 (if present) with reason 1 for timeout, builds a TP.CM connection-abort frame for PGN 0xEF00 (mcu_can_tp_abort_frame_build), sends it through the send callback at ops +0x0C, and sets the session state byte at +0x02 to 1, which marks it finished. Before the limit it only advances the counter.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TP session: id bytes at +0x00 and +0x01, state at +0x02, timer +0x16, limit +0x18 |
| `param_2` | `ptr` | operations table: error callback +0x04, send callback +0x0C |

- Addresses by version: 12b: 0x0800B348, 143: 0x0800B5F8, 152: 0x0800B5FC, 0160: 0x0800B65C
- Called by: `mcu_can_tp_sender_step`
- Calls: `mcu_can_tp_abort_frame_build`
- Confidence: high

## mcu_frame_build_5aa5_checksum

**Build a 5A A5 frame: 7-byte header, payload, and a little-endian byte-sum checksum**

Writes a frame into the buffer at param_7: bytes 0x5A and 0xA5, then the payload length, then param_1, param_2, param_4 and param_5, then the payload bytes copied from param_6 starting at byte 7. The checksum is mcu_byte_sum_checksum16 over bytes 2 through 6 plus the payload, which is the length, the four header bytes and the payload, and it is stored little-endian in the last two bytes. The return value is the total frame length, 9 plus the payload length, truncated to 8 bits.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | header byte 3 of the frame |
| `param_2` | `u8` | header byte 4 of the frame |
| `param_3` | `u32` | payload length |
| `param_4` | `u8` | header byte 6 of the frame |
| `param_5` | `u8` | header byte 7 of the frame |
| `param_6` | `ptr` | payload source |
| `param_7` | `ptr` | output buffer |

**Returns** `u8`: total frame length, 9 + payload length

**Notes:** Not the same routine as mcu_frame_build_checksum16 (0x0800D4A8), which uses a three-byte header.

- Addresses by version: 12b: 0x080064D8, 143: 0x08006390, 152: 0x080063C0, 0160: 0x08006460
- Called by: `mcu_req_queue_submit`
- Calls: `mcu_byte_sum_checksum16`
- Confidence: high

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
- Called by: `mcu_can_tp_session_start`
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

## mcu_msg_ring2_enqueue_frames

**Split a payload into 8-byte CAN records and push them onto message ring 2**

Queues an outgoing message on message ring 2 as one 20-byte record per frame of up to 8 data bytes. It does nothing when bit 1 of the flag byte at 0x20000320 is set. A zero-length message becomes one empty record. Otherwise it loops over the payload: each pass sets the identifier word at 0x20001858, the zero index halfword at 0x20001860 and the length byte at 0x20001862 (min of remaining and 8), copies the bytes with __aeabi_memcpy into 0x20001863, and pushes the record with mcu_msg_ring2_push. Frames are dropped by the ring when it is full, so the caller gets no status.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | payload length in bytes, 16-bit arithmetic |
| `param_2` | `u32` | CAN identifier written into every record |
| `param_3` | `ptr` | payload source |

**Notes:** The meaning of flag bit 1 at 0x20000320 (output disabled) is inferred from the early return.

- Addresses by version: 12b: 0x0800B95C, 143: 0x0800BC0C, 152: 0x0800BC10, 0160: 0x0800BC70
- Called by: `mcu_0160_0800dc08`
- Calls: `__aeabi_memcpy`, `mcu_msg_ring2_push`
- Confidence: high

## mcu_state_reset_load_key16

**Reset 17 state fields and write the 16-byte ASCII constant AQ5GoxXTs8j3BG2Q to 0x20002054**

Zeroes 17 RAM fields: nine byte flags and counters at 0x200006B8..0x200006C0, and eight words at 0x200006C4..0x200006E0. It then writes four 32-bit constants to 0x20002054, 0x20002058, 0x2000205C and 0x20002060, which in memory order spell the 16-byte ASCII string AQ5GoxXTs8j3BG2Q. The string looks like a fixed key, password or seed, but this function does not show its use. Called from mcu_0160_0800665c and mcu_0160_0800672c. Present only in the 0160 build.

**Notes:** The constant's use is in another function, probably a comparison or key derivation. Check the callers.

- Addresses by version: 0160: 0x08006AE0
- Called by: `mcu_0160_0800665c`, `mcu_0160_0800672c`
- Confidence: medium

## mcu_telemetry_group_get

**Return the 8-byte value group for a telemetry request ID, packed into the shared buffer at 0x20000310**

Builds the 8-byte reply for a request ID in the shared buffer at 0x20000310 and returns its address. Each ID selects one group: 0x42 takes the 32-bit word at +0x64 of the object at the global 0x2000002C (mcu_get_global_ctx_field_0x64, one call per byte); 0x211 packs a status byte, the clamped speed at 0x20000F48, and a bit from 0x200000EC; 0x210 and 0x212 return fixed values with the 0x20001FEE, FF0, FF4 and FF6 fields; 0x341 and 0x344 return the 0x2000033x and 0x20000340 state words; 0x342 and 0x343 pack the 0x20001FD6 to FDC command words and status bits; 0x401 returns the percent value of the Q15 at 0x20000A50 (mcu_q15_to_percent_s16), a scaled current byte and a clamped mcu_get_cfg_field_0x28 value. Unknown IDs leave the buffer unchanged.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | request ID, 16-bit values such as 0x42, 0x210 to 0x212, 0x341 to 0x344, 0x401 |

**Returns** `ptr`: address of the 8-byte buffer at 0x20000310; its contents depend on the request ID

**Notes:** The meaning of the IDs and of each byte is inferred from the store pattern and the callee summaries; the request ID space is not documented in this packet.

- Addresses by version: 12b: 0x0800C444, 143: 0x0800C68C, 152: 0x0800C690, 0160: 0x0800C6F0
- Calls: `mcu_get_cfg_field_0x28`, `mcu_q15_to_percent_s16`, `mcu_get_global_ctx_field_0x64`
- Confidence: medium
