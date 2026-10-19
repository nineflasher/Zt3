# VCU - `protocol` functions

15 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`can_get_tx_payload_for_id`](#can_get_tx_payload_for_id) | 0x0800B770 | Build the 8-byte CAN payload for a given CAN ID in a static buffer |
| [`proto_session_bind_buffer`](#proto_session_bind_buffer) | 0x0800D32A | Bind a frame buffer and fragment size to a 36-byte protocol session slot |
| [`proto_session_build_frame`](#proto_session_build_frame) | 0x0800D688 | Build a checksummed, fragmented frame for a protocol session into its buffer |
| [`proto_session_find_or_alloc`](#proto_session_find_or_alloc) | 0x0800A676 | Find or allocate a 36-byte session slot for an (a,b) address pair |
| [`proto_session_send`](#proto_session_send) | 0x0800D2F6 | Find or allocate a session for an address pair and build a frame into its buffer |
| [`proto_sessions_init`](#proto_sessions_init) | 0x0800CF54 | Bind five 36-byte protocol session slots to 300-byte buffers and publish the table |
| [`vcu_can_tp_rx_dispatch`](#vcu_can_tp_rx_dispatch) | 0x0800D282 | Route a received J1939 TP.CM or TP.DT frame to the transport session table |
| [`vcu_can_tp_sender_tick`](#vcu_can_tp_sender_tick) | 0x0800D34A | Advance the J1939 TP sender state machine of one session on each timer tick |
| [`vcu_can_tp_session_on_frame`](#vcu_can_tp_session_on_frame) | 0x0800D414 | Process one received TP.CM or TP.DT frame against a J1939 transport session |
| [`vcu_frame_checksum`](#vcu_frame_checksum) | 0x080054D0 | Ones'-complement of the 16-bit sum of bytes (Ninebot-style frame checksum) |
| [`vcu_ninebot_frame_build`](#vcu_ninebot_frame_build) | 0x08008A9E | Build a 9+n byte Ninebot-style frame: 5A A5 LEN SRC DST CMD ARG DATA CKSUM |
| [`vcu_ninebot_tx_queue_push`](#vcu_ninebot_tx_queue_push) | 0x08008BB0 | Build a Ninebot frame into the next free slot of an 8-entry TX ring, drop it when full |
| [`vcu_record_send_chunked`](#vcu_record_send_chunked) | 0x0800AC44 | Submit a byte buffer as a series of up to 8-byte records via FUN_08007bec |
| [`vcu_record_send_short`](#vcu_record_send_short) | 0x0800B088 | Submit one record of up to 8 bytes with tag param_1 and type byte 1 |
| [`vcu_rx_frame_dispatch`](#vcu_rx_frame_dispatch) | 0x08006D6C | Decode one received message record by its 32-bit ID and store its payload fields |

## can_get_tx_payload_for_id

**Build the 8-byte CAN payload for a given CAN ID in a static buffer**

Large if/switch on the CAN identifier param_1. For known IDs it copies fields from application globals into the static 8-byte buffer at 0x2000184c (u16 at +0, u32 at +2, u16 at +6, i.e. four little-endian words) and returns a pointer to that buffer. Handled IDs: 0x100, 0x203, 0x204 (zeros), 0x205 (zeros, only clears word 0, word 1 low half and word 3), 0x209, 0x20a, 0x20b, 0x20c, 0x301, 0x302 (words 0xff00, 0xffffffff, 0xffff), 0x480-0x485 and 0x7f0 (word0 = 0x1e, rest 0). Side effects: 0x301 also copies word0 to DAT_20003358; 0x100 copies word0 to DAT_20003356; 0x20c merges DAT_2000123d into the high byte of DAT_20001fa0 and writes the result back. Unknown IDs leave the buffer unchanged (stale data) and still return its address. No direct callers (invoked through a pointer or table).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 11-bit CAN identifier |

**Returns** `ptr`: pointer to the 8-byte payload buffer at 0x2000184c

**Notes:** Role (TX data provider for periodic/requested CAN frames) is inferred from the ID list and output buffer; the semantic meaning of each source global (speed, battery, etc.) was not resolved. Source globals include 0x20001f90-96 (0x100), 0x20001b68/d08/e62/b62 (0x203), 0x20001cd8-ce0 (0x20a), 0x20001e28/e48/e50/cc4 (0x20b), 0x20001f98-fa0 (0x20c), 0x2000186f-1870/1854/1858 (0x301), 0x20001b84/b88/b78 (0x480), 0x20001b72/b70/b4e/cb6 (0x481), 0x20001ae2/b12 (0x482), 0x20001ad4-ad9 (0x483), 0x20001adc-ae0 (0x484), 0x20001fef/f8e/fee/f8c (0x485).

- Addresses by version: 148: 0x0800A850, 14a: 0x0800AC48, 14b: 0x0800B0D0, 14e: 0x0800B164, 14f: 0x0800B2A0, 152: 0x0800B52C, 153: 0x0800B620, 0159: 0x0800B770
- Confidence: medium

## proto_session_bind_buffer

**Bind a frame buffer and fragment size to a 36-byte protocol session slot**

Initialises one protocol session slot (0x24 bytes): stores the buffer pointer at +4, its capacity (u16) at +8, the fragment size (s16) at +0x14 and param_5 at +0x20, and sets the state byte at +2 to 1 (bound). It returns 0 and writes nothing if any of the buffer pointer, the fragment size or the session pointer is zero, because the fragment size is later used as a divisor. The init routine vcu_0159_0800cf54 calls it for five consecutive slots starting at 0x200022E0, each with a 300-byte buffer at 0x20002394. The field meanings are inferred from the callers and the size arithmetic, so the names are medium confidence.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | protocol session slot (36 bytes) |
| `param_2` | `s32` | fragment (packet) size in bytes, must be non-zero |
| `param_3` | `ptr` | frame buffer, must be non-zero |
| `param_4` | `u16` | frame buffer capacity in bytes |
| `param_5` | `u32` | stored at session +0x20 (passed as 0 by the init code) |

**Returns** `bool`: 1 when the slot was bound, 0 for invalid arguments

**Notes:** The +0x20 field is written but not interpreted in this function.

- Addresses by version: 148: 0x0800C49A, 14a: 0x0800C8E2, 14b: 0x0800CD6E, 14e: 0x0800CE02, 14f: 0x0800CF3E, 152: 0x0800D1CA, 153: 0x0800D2BE, 0159: 0x0800D32A
- Called by: `proto_sessions_init`
- Confidence: medium

## proto_session_build_frame

**Build a checksummed, fragmented frame for a protocol session into its buffer**

Writes a frame into a session buffer: byte 0 = param_3, bytes 1..2 = param_6 and param_7, then the n payload bytes, then a 16-bit checksum (little-endian) equal to the ones' complement of the 16-bit sum of the three header bytes and the payload. It rejects a null buffer or payload, a payload over 0x6F9 (1785) bytes and a buffer smaller than n+5. On success it stores the state 3 at +2, the session bytes param_4 and param_5 at +0 and +1, the frame length n+5 (u16) at +0xC, clears the fragment counter at +0x1A and sets the fragment count at +0x1C to ceil(param_10 / fragment_size), with fragment_size the u16 at +0x14. Its caller vcu_0159_0800d2f6 first gets the session from proto_session_find_or_alloc (vcu_0159_0800a676) and then calls this function. The checksum is the same ones'-complement sum used by vcu_frame_checksum, so it is the protocol's frame check.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | protocol session slot (36 bytes) |
| `param_2` | `u32` | not used in this body |
| `param_3` | `s32` | frame header byte 0 |
| `param_4` | `u8` | stored at session +0 |
| `param_5` | `u8` | stored at session +1 |
| `param_6` | `s32` | frame header byte 1 |
| `param_7` | `s32` | frame header byte 2 |
| `param_8` | `ptr` | payload source |
| `param_9` | `u32` | payload length in bytes, at most 0x6F9 |
| `param_10` | `s32` | total message length used to compute the fragment count |

**Returns** `bool`: 1 when the frame was built, 0 when a check failed

**Notes:** Header byte meanings are not fixed by this code (the caller supplies them). The +0x1C fragment count and the +0x14 fragment size are inferred from the arithmetic and the caller that reads them.

- Addresses by version: 148: 0x0800C7F8, 14a: 0x0800CC40, 14b: 0x0800D0CC, 14e: 0x0800D160, 14f: 0x0800D29C, 152: 0x0800D528, 153: 0x0800D61C, 0159: 0x0800D688
- Called by: `proto_session_send`
- Confidence: medium

## proto_session_find_or_alloc

**Find or allocate a 36-byte session slot for an (a,b) address pair**

param_1 points to a table descriptor {entries pointer; u16 count}; entries are 0x24 bytes with byte0/byte1 = a pair of endpoint ids and byte2 = state (1 = free). With param_4 == 0 it first returns NULL if an in-use entry already holds the reversed pair (e[0]==param_3, e[1]==param_2); otherwise it returns the in-use entry matching (e[0]==param_2, e[1]==param_3); otherwise the first free entry (state==1); otherwise NULL. With param_4 != 0 the reversed-pair check is skipped. Called from 0x0800d282 and 0x0800d2f6 (protocol/session layer).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | table descriptor: [0]=entries base, +4 u16 entry count |
| `param_2` | `u32` | first id byte (matched against entry byte 0) |
| `param_3` | `u32` | second id byte (matched against entry byte 1) |
| `param_4` | `s32` | 0 = also reject if reversed pair active; non-zero = skip that check |

**Returns** `ptr`: matching or free entry, or NULL

**Notes:** Semantics (src/dst addresses? command ids?) inferred from the access pattern only; the entry layout beyond +0..+2 is unknown.

- Addresses by version: 148: 0x080096F2, 14a: 0x08009BCA, 14b: 0x0800A052, 14e: 0x0800A0E6, 14f: 0x0800A222, 152: 0x0800A4A2, 153: 0x0800A596, 0159: 0x0800A676
- Called by: `vcu_can_tp_rx_dispatch`, `proto_session_send`
- Confidence: low

## proto_session_send

**Find or allocate a session for an address pair and build a frame into its buffer**

Send-side entry point of the protocol layer. It calls proto_session_find_or_alloc (vcu_0159_0800a676) with the address pair in param_4 and param_5, with the reversed-pair check enabled, and returns 0 if no slot can be used. Otherwise it passes the session to proto_session_build_frame (vcu_0159_0800d688) with the three header bytes (param_3, param_6, param_7), the payload (param_8, length param_9) and the total message length (param_10), and returns that result.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | session table descriptor |
| `param_2` | `u32` | passed through to the frame builder, unused there |
| `param_3` | `s32` | frame header byte 0 |
| `param_4` | `u8` | first address byte of the session |
| `param_5` | `u8` | second address byte of the session |
| `param_6` | `s32` | frame header byte 1 |
| `param_7` | `s32` | frame header byte 2 |
| `param_8` | `ptr` | payload source |
| `param_9` | `u32` | payload length, at most 0x6F9 |
| `param_10` | `s32` | total message length used for the fragment count |

**Returns** `bool`: 1 = frame built, 0 = no session or the build check failed

- Addresses by version: 148: 0x0800C466, 14a: 0x0800C8AE, 14b: 0x0800CD3A, 14e: 0x0800CDCE, 14f: 0x0800CF0A, 152: 0x0800D196, 153: 0x0800D28A, 0159: 0x0800D2F6
- Called by: `vcu_0159_0800d018`
- Calls: `proto_session_find_or_alloc`, `proto_session_build_frame`
- Confidence: high

## proto_sessions_init

**Bind five 36-byte protocol session slots to 300-byte buffers and publish the table**

Application init of the transport session table. For i = 0..4 it calls proto_session_bind_buffer (vcu_0159_0800d32a) on the slot at 0x200022E0 + i*0x24, with fragment size 1, buffer 0x20002394 + i*300, capacity 300 and extra argument 0. If the callback words DAT_20001838 (block +0x0) and DAT_20001844 (block +0xC) are both set, it stores the table descriptor (entries base 0x200022E0 at 0x20002970, count 5 at 0x20002974) and the callback block address &DAT_20001838 at 0x20002978, then returns 1. Otherwise it returns 0 and leaves the descriptor unset. The callback block is read by vcu_can_tp_rx_dispatch and vcu_can_tp_session_on_frame: +0x0 accept check, +0x4 event, +0x8 message complete, +0xC transmit.

**Returns** `bool`: 1 = table published, 0 = a required callback is missing

**Notes:** The buffer layout is exact (five 300-byte buffers end at 0x20002970). The callback roles are inferred from how the TP code calls them.

- Addresses by version: 148: 0x0800C0C8, 14a: 0x0800C50C, 14b: 0x0800C998, 14e: 0x0800CA2C, 14f: 0x0800CB68, 152: 0x0800CDF4, 153: 0x0800CEE8, 0159: 0x0800CF54
- Called by: `vcu_0159_0800d858`
- Calls: `proto_session_bind_buffer`
- Confidence: medium

## vcu_can_tp_rx_dispatch

**Route a received J1939 TP.CM or TP.DT frame to the transport session table**

Receive dispatcher for J1939 transport protocol frames. It reads the 29-bit CAN ID at param_2, takes PF from ID bits 16..23 and the two low ID bytes as the peer address. Only PF 0xEC (TP.CM) and 0xEB (TP.DT) are handled. A TP.CM request-to-send (control byte 0x10 at frame offset 5) is accepted only if the accept callback (block at param_1[2], function word at +0) returns 1 for that pair; then a session is found or allocated with proto_session_find_or_alloc (vcu_0159_0800a676, reversed-pair check skipped) and the frame goes to vcu_can_tp_session_on_frame (vcu_0159_0800d414). Every other TP.CM or TP.DT frame is offered to each slot of the table in turn, and the session code decides whether it belongs there.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | session table descriptor: entries at +0, u16 count at +4, callback block pointer at +8 |
| `param_2` | `ptr` | received CAN frame: 29-bit ID at +0, data bytes from +5 |

**Notes:** Data bytes start at frame offset 5, inferred from the byte offsets the TP code uses.

- Addresses by version: 148: 0x0800C3F2, 14a: 0x0800C83A, 14b: 0x0800CCC6, 14e: 0x0800CD5A, 14f: 0x0800CE96, 152: 0x0800D122, 153: 0x0800D216, 0159: 0x0800D282
- Called by: `vcu_0159_0800cfac`
- Calls: `proto_session_find_or_alloc`, `vcu_can_tp_session_on_frame`
- Confidence: high

## vcu_can_tp_sender_tick

**Advance the J1939 TP sender state machine of one session on each timer tick**

Tick routine for the transmit side of a transport session. The state byte at session+2 selects the action. State 3 builds a TP.CM RTS (vcu_can_tp_rts_frame_build), sends it through the transmit callback at block+0xC, clears the counters and moves to state 4 with a 0x4E2 (1250) timeout. In state 5 the tick counter at +0x1A counts up to the inter-packet interval at +0x1C; when it expires the next TP.DT is built with vcu_can_tp_dt_frame_build at offset +0x0A and sent, and the offset advances by 7. The state becomes 9 (wait for EOM ACK) once the offset reaches the total size at +0x0C, or 6 (wait for CTS) once it reaches the window end at +0x12; a zero interval sends several packets in one call. States 4, 6, 7, 9 and 10 are passed to the timeout helper vcu_0159_0800a78a (not described in this packet).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | transport session slot (36 bytes) |
| `param_2` | `ptr` | callback block: +0xC transmit callback |

**Notes:** Timeouts are counts divided by the u16 at +0x14 (the fragment size, 1 in proto_sessions_init), so they are read as milliseconds here.

- Addresses by version: 148: 0x0800C4BA, 14a: 0x0800C902, 14b: 0x0800CD8E, 14e: 0x0800CE22, 14f: 0x0800CF5E, 152: 0x0800D1EA, 153: 0x0800D2DE, 0159: 0x0800D34A
- Called by: `vcu_0159_0800d25e`
- Calls: `vcu_can_tp_session_timeout_tick`, `vcu_can_tp_rts_frame_build`, `vcu_can_tp_dt_frame_build`
- Confidence: high

## vcu_can_tp_session_on_frame

**Process one received TP.CM or TP.DT frame against a J1939 transport session**

Frame handler and state machine for one transport session, used on both the receive and the transmit side. Session layout: +0/+1 the peer ID bytes, +2 state, +4 buffer pointer, +8 buffer capacity, +0xA running offset, +0xC total size, +0xE packet sequence, +0x10 packets allowed, +0x12 window end offset, +0x14 fragment divisor, +0x16/+0x18 timer, +0x1A/+0x1C tick and interval, +0x1E running checksum. A control byte 0x10 (RTS) on a free or matching slot checks the size against the capacity and the packet count against (size+6)/7; on a mismatch it sends an abort (vcu_can_tp_abort_frame_build), otherwise it sends a CTS (vcu_can_tp_cts_frame_build) and enters state 10. Control 0x11 (CTS) moves a sender from state 4 or 7 to state 5 with the window taken from the frame, or from state 6 to hold state 7 when zero packets are allowed; 0x13 (EOM ACK) in state 9 completes the sender with a done event (block+0x4, status 3); 0xFF returns the session to idle. A TP.DT (0xEB) in state 10 whose sequence byte is the next expected value copies up to 7 bytes into the buffer and adds the payload bytes, except the last two, into a 16-bit sum, then sets a 750 ms timeout. The last packet compares the trailing little-endian word with the ones' complement of that sum, sends an EOM ACK (vcu_can_tp_eom_ack_frame_build) and calls the message-complete callback (block+0x8) with the length minus 2. A sequence error or checksum mismatch sends an abort and returns the session to idle.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | transport session slot (36 bytes) |
| `param_2` | `ptr` | received CAN frame: 29-bit ID at +0, data bytes from +5 |
| `param_3` | `ptr` | callback block: +0x4 event, +0x8 message complete, +0xC transmit |

**Notes:** Matching: for DT and RTS the frame ID bytes are compared in the same order as the session bytes; for CTS, EOM ACK and abort the order is swapped (the peer answers with source and destination reversed). Callback roles are inferred from how they are called.

- Addresses by version: 148: 0x0800C584, 14a: 0x0800C9CC, 14b: 0x0800CE58, 14e: 0x0800CEEC, 14f: 0x0800D028, 152: 0x0800D2B4, 153: 0x0800D3A8, 0159: 0x0800D414
- Called by: `vcu_can_tp_rx_dispatch`
- Calls: `vcu_can_tp_abort_frame_build`, `vcu_can_tp_cts_frame_build`, `vcu_can_tp_eom_ack_frame_build`
- Confidence: high

## vcu_frame_checksum

**Ones'-complement of the 16-bit sum of bytes (Ninebot-style frame checksum)**

Sums param_2 bytes starting at param_1 into a 16-bit accumulator (wraparound) and returns the bitwise NOT of the sum. This is the typical Ninebot/Xiaomi frame checksum (0xFFFF ^ sum). Called from vcu_0159_08008a9e, a frame build/verify routine. The result is returned as a ushort, low byte then high byte presumably appended to the frame.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | start of data (u8 array) |
| `param_2` | `u32` | number of bytes |

**Returns** `u16`: ~sum of bytes, 16 bit

**Notes:** Which bytes of the frame (e.g. length..data) are included is decided by the caller.

- Addresses by version: 148: 0x08004BC8, 14a: 0x08004F54, 14b: 0x08005258, 14e: 0x08005290, 14f: 0x080052EC, 152: 0x0800534C, 153: 0x08005364, 0159: 0x080054D0
- Called by: `vcu_ninebot_frame_build`
- Confidence: high

## vcu_ninebot_frame_build

**Build a 9+n byte Ninebot-style frame: 5A A5 LEN SRC DST CMD ARG DATA CKSUM**

Serialises one frame into the caller's buffer: bytes 0x5A and 0xA5, then LEN (the payload length), then param_1 and param_2 as the two address bytes, param_4 as the command and param_5 as the argument, followed by len payload bytes copied from param_6. The 16-bit checksum from vcu_frame_checksum (FUN_080054d0) covers bytes 2 through the end of the payload, and is stored little-endian after the payload. The function returns the total frame length, 9 + len, computed with 8-bit wrap-around arithmetic.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | first address byte (frame offset 3) |
| `param_2` | `u8` | second address byte (frame offset 4) |
| `param_3` | `u8` | payload length in bytes, written to frame offset 2 |
| `param_4` | `u8` | command byte (frame offset 5) |
| `param_5` | `u8` | argument byte (frame offset 6) |
| `param_6` | `ptr` | payload source |
| `param_7` | `ptr` | output frame buffer |

**Returns** `u8`: total frame length, 9 + payload length

**Notes:** Frame layout is Ninebot-style as the packet comment suggests; field names are inferred from the byte positions and are not confirmed by a protocol document.

- Addresses by version: 148: 0x0800806A, 14a: 0x080084C6, 14b: 0x0800883E, 14e: 0x0800887E, 14f: 0x080088DA, 152: 0x0800899E, 153: 0x08008A3A, 0159: 0x08008A9E
- Called by: `vcu_ninebot_tx_queue_push`
- Calls: `vcu_frame_checksum`
- Confidence: high

## vcu_ninebot_tx_queue_push

**Build a Ninebot frame into the next free slot of an 8-entry TX ring, drop it when full**

Enqueue operation on a ring object at param_1: +1 is the write index (wraps at 8), +2 the free-slot count, +3 a re-entry guard and +4 a disable flag. Each slot is 0x100 bytes starting at offset +0xc, with its length word at +8. When the guard and the disable flag are both clear, the payload is shorter than 243 bytes and a free slot exists, the frame is built with vcu_ninebot_frame_build into the slot, the length is stored, the write index advances and the free count drops. Otherwise the frame is silently dropped, and the guard is released in both cases.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TX ring object |
| `param_2` | `u8` | first address byte, forwarded to the frame builder |
| `param_3` | `u8` | second address byte, forwarded |
| `param_4` | `u32` | payload length |
| `param_5` | `u8` | command byte |
| `param_6` | `u8` | argument byte |
| `param_7` | `ptr` | payload source |

**Notes:** The slot length word is written as a 32-bit store at +8. Who drains the ring is not in this packet.

- Addresses by version: 148: 0x0800817C, 14a: 0x080085D8, 14b: 0x08008950, 14e: 0x08008990, 14f: 0x080089EC, 152: 0x08008AB0, 153: 0x08008B4C, 0159: 0x08008BB0
- Called by: `vcu_0159_0800193c`, `vcu_0159_08002f30`, `vcu_0159_080031f4`, `vcu_0159_080054ec`, `vcu_0159_08006184`, `vcu_0159_0800683c`, `vcu_0159_08006b24`, `vcu_0159_08007ecc`, `vcu_0159_08008614`, `vcu_0159_08008fe0`
- Calls: `vcu_ninebot_frame_build`
- Confidence: medium

## vcu_record_send_chunked

**Submit a byte buffer as a series of up to 8-byte records via FUN_08007bec**

For a zero length it submits one empty record: the length byte at 0x20002986 and the index byte at 0x20002984 are zeroed, the tag param_2 is stored at 0x2000297c, and FUN_08007bec (record submit, not yet described) is called on that record. For a nonzero length it loops in chunks of at most 8 bytes: each chunk sets the length byte, index 0, the tag, copies the chunk bytes into the payload area at 0x20002987 with __aeabi_memcpy, and submits the record. The record layout (tag at +0, index byte at +8, length byte at +10, payload from +11) is the same as vcu_record_send_short.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | buffer length in bytes |
| `param_2` | `u32` | tag stored in the record header |
| `param_3` | `ptr` | source buffer |

**Notes:** As decompiled, the memcpy source is param_3 on every iteration and the per-chunk offset is not shown, so either the decompile dropped an offset or only the first chunk's bytes are sent for longer buffers. The memcpy byte count is also not visible (presumably the chunk size). Verify in the disassembly before relying on it.

- Addresses by version: 148: 0x08009CBC, 14a: 0x0800A198, 14b: 0x0800A620, 14e: 0x0800A6B4, 14f: 0x0800A7F0, 152: 0x0800AA70, 153: 0x0800AB64, 0159: 0x0800AC44
- Called by: `vcu_0159_08003a7c`, `vcu_0159_0800eac4`
- Calls: `__aeabi_memcpy`, `vcu_can_tx_queue_push`
- Confidence: medium

## vcu_record_send_short

**Submit one record of up to 8 bytes with tag param_1 and type byte 1**

Builds a record on the stack: the tag param_1 at +4, a type byte 1 at +8, a zero byte at +9, the length (param_3 low nibble) at +10, and the payload copied to +11, then calls FUN_08007bec to submit it. Payloads are accepted only when the low nibble of the length is below 9. Latent defect: the copy loop runs for the full param_3 value rather than the masked nibble, so a length of 16 or more whose low nibble is below 9 writes past the 9-byte payload area, and the length field then disagrees with the bytes copied.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | tag stored in the record header |
| `param_2` | `ptr` | payload source |
| `param_3` | `u32` | payload length; only low nibble is recorded and checked |

**Notes:** The first word of the record (uninitialised stack) is not written. The type byte is 1 here and 0 in vcu_record_send_chunked. Check the callers before assuming the overflow is reachable.

- Addresses by version: 148: 0x0800A100, 14a: 0x0800A5DC, 14b: 0x0800AA64, 14e: 0x0800AAF8, 14f: 0x0800AC34, 152: 0x0800AEB4, 153: 0x0800AFA8, 0159: 0x0800B088
- Called by: `vcu_0159_0800d018`, `vcu_0159_0800ef5a`
- Calls: `vcu_can_tx_queue_push`
- Confidence: medium

## vcu_rx_frame_dispatch

**Decode one received message record by its 32-bit ID and store its payload fields**

Takes a pointer to a received record whose first word is the message ID and whose payload begins at byte offset 0x0b. It selects a handler by ID: 0x421 decodes four ASCII hex characters into DAT_20001ae6 through util_hex_char_to_nibble (copied to DAT_20001d60) and stores two 16-bit fields in DAT_20001d6a and DAT_20001ee6; 0x420 stores DAT_20001b5e = value / 10 and copies it to DAT_20001e62 and DAT_20001d08; 0x425 stores the byte DAT_20001f36 and DAT_20001b8a = (DAT_20001f36 - 50) * 10; 0x311 clamps two bytes to DAT_20001fdb and DAT_20001fdc into DAT_20001f9c; 0x3d0 (listed as 0x7f1) sets DAT_2000185e = 500 and bit 0 of DAT_2000185c. Group A IDs 0x341, 0x211, 0x212, 0x342, 0x344 and 0x401 clear the silence timer DAT_2000102c and set the freshness counter DAT_20001868 to 200 with bit 1 of DAT_2000186e cleared; group B IDs (0x310, 0x311, 0x420, 0x421, 0x422-0x425, 0x500, 0x501, 0x502) clear DAT_20001030 and set DAT_2000186a to 200 with bit 2 of DAT_2000186e cleared. Unknown IDs are ignored.

| Parameter | Type | Description |
|---|---|---|
| `record` | `ptr` | received record: 32-bit message ID followed by payload; the payload fields are read at byte offsets 0x0b to 0x12 |

**Notes:** The ID-to-field table is the main content: 0x211 writes DAT_20001f7a from a bit-packed byte and DAT_20001cc6 when the 16-bit value is below 600; 0x212 writes DAT_20001ae4, DAT_20001f78, DAT_2000334c, DAT_20001f7c, the low byte of DAT_20001f80, DAT_20001f7e and DAT_2000334e; 0x310 writes DAT_20001e66, DAT_20001e6e and DAT_20001e50; 0x401 writes DAT_20001f84 and DAT_20001f88; 0x500 writes the eight bytes DAT_20001e70..DAT_20001e7e. The record layout is inferred from the offsets used by the code.

- Addresses by version: 148: 0x08006314, 14a: 0x08006734, 14b: 0x08006A88, 14e: 0x08006AC0, 14f: 0x08006B1C, 152: 0x08006BC8, 153: 0x08006C64, 0159: 0x08006D6C
- Called by: `vcu_0159_08007ad4`
- Calls: `util_hex_char_to_nibble`
- Confidence: medium
