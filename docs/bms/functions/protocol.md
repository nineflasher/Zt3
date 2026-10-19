# BMS - `protocol` functions

27 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_auth_verify_response`](#bms_auth_verify_response) | 0x08004FEC | Check a 16-byte reply (cmd 0x1D, type 4) against a value computed from the object at 0x20000BCC |
| [`bms_can_status_frame_rx`](#bms_can_status_frame_rx) | 0x0800E2C8 | Decode CAN frames 0x7F0, 0x7F1 and 0x212 and age out the 0x212 status flag after 2000 ticks |
| [`bms_chan_service_all`](#bms_chan_service_all) | 0x0800FEFC | Run the per-object state step for each of N 36-byte channel objects in a table |
| [`bms_comm_await_reply_cmd03`](#bms_comm_await_reply_cmd03) | 0x0800525C | Wait for the command-03 reply: accept into ctx+0x08, retry after 200 ticks, fault after 11 retries |
| [`bms_comm_req_cmd02`](#bms_comm_req_cmd02) | 0x08005228 | Send command 0x02 with no payload, reset the reply timer, and enter state 2 |
| [`bms_comm_req_cmd04`](#bms_comm_req_cmd04) | 0x080053C8 | Send command 0x04 with no payload, reset the reply timer, and enter state 4 |
| [`bms_comm_req_cmd06`](#bms_comm_req_cmd06) | 0x080052E0 | Send command 0x06 with no payload, reset the reply timer, and enter state 8 |
| [`bms_comm_request_dispatch`](#bms_comm_request_dispatch) | 0x08004DE8 | Pick the next queued link request (0x16, 0x1E, 0x18) and send it, else count the queue down |
| [`bms_comm_send_frame`](#bms_comm_send_frame) | 0x08005128 | Build and send a framed message on USART3: magic, command, count and sequence, payload, CRC-16 |
| [`bms_comm_service_step`](#bms_comm_service_step) | 0x0800E060 | Service the message pool: periodic 14-byte send, two busy timeouts, then dispatch the state handler |
| [`bms_frame_parse_legacy_4139`](#bms_frame_parse_legacy_4139) | (removed) | Byte-wise parser for the 0x5A/0xA5 framed record packet with CRC-16 check (4130/4139) |
| [`bms_frame_parse_legacy_4168`](#bms_frame_parse_legacy_4168) | 0x08007C10 | Byte-wise 0x5A/0xA5 framed-packet parser with CRC-16 check for the 4148/4168 builds |
| [`bms_frame_rx_byte`](#bms_frame_rx_byte) | 0x0800E128 | Feed one received byte into the 0x5A 0xA5 framed parser; return 1 when a frame checks out |
| [`bms_frame_send_when_ready`](#bms_frame_send_when_ready) | 0x0800B9A8 | Submit one message, waiting up to 5 time-base ticks for the transmit path to free up |
| [`bms_j1939_tp_rx_dispatch`](#bms_j1939_tp_rx_dispatch) | 0x0800FF22 | Dispatch a received J1939 TP.CM or TP.DT frame to a session, creating one on an RTS |
| [`bms_j1939_tp_session_rx`](#bms_j1939_tp_session_rx) | 0x08010204 | Process a received TP.CM or TP.DT frame for one session: RTS, CTS, EOM ACK, abort and data |
| [`bms_j1939_tp_session_step`](#bms_j1939_tp_session_step) | 0x0800FFEC | Advance one J1939 TP transmit session: send RTS, data frames, and handle its timeouts |
| [`bms_j1939_tpcm_abort_pack`](#bms_j1939_tpcm_abort_pack) | 0x0801066C | Build a J1939 TP.CM connection-abort frame for PGN 0xEF00 into a TX object |
| [`bms_proto_build_reply`](#bms_proto_build_reply) | 0x080062F0 | Build the 0x5A 0xA5 reply frame for a received message and set the reply state |
| [`bms_record_send_multiframe`](#bms_record_send_multiframe) | 0x0800B9F2 | Send a queued record in up to 8-byte frames, advancing its address between frames |
| [`bms_rx_frame_7f0_7f1`](#bms_rx_frame_7f0_7f1) | (removed) | Receive hook for IDs 0x7F0 and 0x7F1: latch one byte-1 bit selected by the module state |
| [`bms_seq_state_reset`](#bms_seq_state_reset) | 0x0800FAA0 | Reset the fault sequence state: sub-state 0, start time, and a nibble snapshot |
| [`bms_syscfg_set_ucpd_strobe`](#bms_syscfg_set_ucpd_strobe) | 0x080028A4 | Replaces SYSCFG.CFGR1 bits 9-10 (UCPD1 and UCPD2 strobe) with the supplied value |
| [`bms_telemetry_block_fill`](#bms_telemetry_block_fill) | (removed) | Fill telemetry block 0 to 10 of the 176-byte frame at 0x20001B90 and write its check word |
| [`bms_tp_tx_prepare`](#bms_tp_tx_prepare) | 0x080104CC | Build a TP message in a transmit session: 3-byte header, payload, and 16-bit complement trailer |
| [`bms_txq_enqueue`](#bms_txq_enqueue) | 0x0800DF2C | Queue a 9-byte message descriptor and payload into the first free of five pool slots |
| [`bms_txq_init`](#bms_txq_init) | 0x0800DFEC | Reset the five-slot message pool, the queue head and counters, then stamp the periodic timer |

## bms_auth_verify_response

**Check a 16-byte reply (cmd 0x1D, type 4) against a value computed from the object at 0x20000BCC**

Timer-driven check of a challenge reply in the host-link layer. param_1 (elapsed time) is added to the reply timer at +0x00 of the context; past 200 the state at +0xF9 becomes 5 (retry) while fewer than four retries have been used, and 0x0D (fault) otherwise. When a frame is pending (flag 0x200001AD) and its header is command 0x1D with type nibble 4, the four 32-bit words at 0x2000092C..0x2000093B are gathered and bms_4168_080106c8 (not described) computes a 16-byte value from the object at 0x20000BCC. That value is repacked into four 32-bit words and compared with the reply. A match clears the retry byte at +0xFB and sets state +0xF9 to 7. The pending flag is cleared on every pass.

| Parameter | Type | Description |
|---|---|---|
| `elapsed` | `u32` | param_1; time added to the reply timer |
| `ctx` | `ptr` | param_2; link context with state +0xF9, retry +0xFB and timer +0x00 |

**Notes:** This is the authentication core of the link, and the algorithm in bms_4168_080106c8 is not in this packet, so the nature of the 16-byte value (MAC, cipher output or hash) is unknown. The byte-swap repacking is decompiled awkwardly and should be checked against the source.

- Addresses by version: 4130: 0x080047D8, 4139: 0x080049EC, 4148: 0x08004EA0, 4168: 0x08004FEC
- Calls: `bms_seed_key_transform`
- Confidence: medium

## bms_can_status_frame_rx

**Decode CAN frames 0x7F0, 0x7F1 and 0x212 and age out the 0x212 status flag after 2000 ticks**

Handles one received frame whose word 0 is the identifier. For identifiers 0x7F0 and 0x7F1 it takes frame byte 7 shifted right by 2, 3 or 4 according to the 16-bit mode at state block +2 (modes 7, 6 and 5); if bit 0 of that is clear it sets DAT_200005D0 to 1, and otherwise it sets DAT_200005D0 to 2 and stamps DAT_200005D4 with the current tick. For identifier 0x212 it copies bit 0 of frame byte 9 into DAT_20000DDF and stamps DAT_200005D8. For every other identifier it runs bms_tick_timeout_check on DAT_200005D8 with a threshold of 2000 ticks and clears DAT_20000DDF when that expires. It always returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | received frame: 32-bit identifier at +0; the bytes at +7 and +9 are read |

**Returns** `u32`: always 1

**Notes:** The meaning of the three identifiers and of the status flags is not established here. Because the timeout helper overwrites its stamp with the elapsed value on expiry, DAT_200005D8 stays expired until the next 0x212 frame restamps it.

- Addresses by version: 4148: 0x0800DE74, 4168: 0x0800E2C8
- Called by: `bms_4168_080056e8`
- Calls: `bms_tick_get`, `bms_tick_timeout_check`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_chan_service_all

**Run the per-object state step for each of N 36-byte channel objects in a table**

Walks a channel table descriptor: word 0 is the base address of 36-byte objects, the low 16 bits of word 1 are the count, and word 2 is a context pointer passed through. For each index it calls bms_j1939_tp_session_step with the object and the context, and it does nothing when the count is zero.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | table descriptor: +0 base pointer, +4 count (low 16 bits), +8 context pointer |

- Addresses by version: 4130: 0x0800E104, 4139: 0x0800E758, 4148: 0x0800F9B0, 4168: 0x0800FEFC
- Called by: `bms_4168_0800f8b4`
- Calls: `bms_j1939_tp_session_step`
- Confidence: high

## bms_comm_await_reply_cmd03

**Wait for the command-03 reply: accept into ctx+0x08, retry after 200 ticks, fault after 11 retries**

Timer step of the host-link layer for requests such as bms_comm_req_cmd02. It adds param_1 to the reply timer at +0x00; past 200 it sets state +0xF9 to 1 (retry) while the retry byte at +0xFB is below 11, and to 0x0D (fault) otherwise. When a frame is pending (flag 0x200001AD) whose header byte at 0x2000092A is 3 and whose high nibble at 0x2000092B is 1, it stores the four payload bytes at 0x2000092C as a little-endian word into ctx+0x08, clears the retry byte, sets state +0xF9 to 3 (reply received), and sets bit 4 of the u16 at +0x194 of the status object from the 0x20000BDC accessor. The pending flag is cleared on every pass.

| Parameter | Type | Description |
|---|---|---|
| `elapsed` | `u32` | param_1; time added to the reply timer |
| `ctx` | `ptr` | param_2; link context with reply word at +0x08, state +0xF9, retry +0xFB |

**Notes:** The state values 1 and 3 are only set here, and the packet does not show what the caller does with them.

- Addresses by version: 4130: 0x08004A5C, 4139: 0x08004C64, 4148: 0x08005110, 4168: 0x0800525C
- Calls: `bms_ram_20000bdc_addr`
- Confidence: high

## bms_comm_req_cmd02

**Send command 0x02 with no payload, reset the reply timer, and enter state 2**

Request step of the host-link layer. It increments the request counter at +0xFB, zeroes the reply timer at +0x00, sends command 0x02 with no payload through bms_comm_send_frame, and sets the state byte at +0xF9 to 2. The reply is collected by bms_comm_await_reply_cmd03 and timed through the reply timer.

| Parameter | Type | Description |
|---|---|---|
| `unused` | `u32` | param_1; not read by the routine |
| `ctx` | `ptr` | param_2; link context |

**Notes:** The meaning of command 0x02 is not in the packet.

- Addresses by version: 4130: 0x08004A18, 4139: 0x08004C2C, 4148: 0x080050DC, 4168: 0x08005228
- Calls: `bms_comm_send_frame`
- Confidence: high

## bms_comm_req_cmd04

**Send command 0x04 with no payload, reset the reply timer, and enter state 4**

Request step of the host-link layer, the same shape as bms_comm_req_cmd02: it increments the request counter at +0xFB, zeroes the reply timer at +0x00, sends command 0x04 with no payload through bms_comm_send_frame and sets the state byte at +0xF9 to 4. The reply is handled by bms_comm_await_reply_cmd03.

| Parameter | Type | Description |
|---|---|---|
| `unused` | `u32` | param_1; not read by the routine |
| `ctx` | `ptr` | param_2; link context |

**Notes:** The meaning of command 0x04 is not in the packet.

- Addresses by version: 4130: 0x08004BBC, 4139: 0x08004DD8, 4148: 0x0800527C, 4168: 0x080053C8
- Calls: `bms_comm_send_frame`
- Confidence: high

## bms_comm_req_cmd06

**Send command 0x06 with no payload, reset the reply timer, and enter state 8**

Request step of the host-link layer, the same shape as bms_comm_req_cmd02: it increments the request counter at +0xFB, zeroes the reply timer at +0x00, sends command 0x06 with no payload through bms_comm_send_frame and sets the state byte at +0xF9 to 8. The reply is handled by bms_comm_await_reply_cmd03.

| Parameter | Type | Description |
|---|---|---|
| `unused` | `u32` | param_1; not read by the routine |
| `ctx` | `ptr` | param_2; link context |

**Notes:** The meaning of command 0x06 is not in the packet.

- Addresses by version: 4130: 0x08004AD0, 4139: 0x08004CEC, 4148: 0x08005194, 4168: 0x080052E0
- Calls: `bms_comm_send_frame`
- Confidence: high

## bms_comm_request_dispatch

**Pick the next queued link request (0x16, 0x1E, 0x18) and send it, else count the queue down**

Part of the host-link request layer, with bms_comm_send_frame, bms_comm_req_cmd02/04/06 and bms_comm_await_reply_cmd03. When the pending-count byte at +0x101 is zero it sets the state byte at +0xF9 to 9 and returns. Otherwise it bumps the retry byte at +0xFB, zeroes the reply timer word at +0x00 and checks three request flags in order: +0xFC sends command 0x16 with no payload, +0xFE sends command 0x1E with one payload word (the byte at +0xFF, also stored at +0x3C), and +0xFD sends command 0x18 with no payload. Each send sets state +0xF9 to 0x0C. With no request pending it decrements the count at +0x101 and returns.

| Parameter | Type | Description |
|---|---|---|
| `unused` | `u32` | param_1; not read by the routine |
| `ctx` | `ptr` | param_2; link context: state +0xF9, retry +0xFB, timer +0x00, flags +0xFC..+0xFE, count +0x101 |

**Notes:** Command meanings 0x16, 0x18 and 0x1E are not identified in the packet. The state values 9 and 0x0C are the ones this function sets.

- Addresses by version: 4130: 0x080045D4, 4139: 0x080047E8, 4148: 0x08004C9C, 4168: 0x08004DE8
- Calls: `bms_comm_send_frame`
- Confidence: medium

## bms_comm_send_frame

**Build and send a framed message on USART3: magic, command, count and sequence, payload, CRC-16**

Builds the outgoing host-link frame and sends it with bms_usart3_send_bytes. Byte 0 is a magic, 0x5A when DAT_200001AE is 1 and 0xA5 otherwise. Byte 1 is the command (the low byte of param_1). Byte 2 holds the payload word count in its high nibble and the 4-bit sequence number from the context at +0xFA in its low nibble. Then come param_3 payload words, each sent big-endian, then the CRC-16/USB (bms_4168_08004da4) over bytes 1 to the end of the payload, high byte first. The sequence number at +0xFA advances mod 8 after each frame. The header and payload are also mirrored into globals 0x20000904 to 0x2000090E (payload stored little-endian there), with the CRC bytes at 0x20000927-0x20000928.

| Parameter | Type | Description |
|---|---|---|
| `cmd` | `u32` | param_1; command code, used as its low byte |
| `words` | `ptr` | param_2; payload array of 32-bit words |
| `count` | `u32` | param_3; number of payload words |
| `ctx` | `ptr` | param_4; link context whose +0xFA byte holds the sequence number |

**Notes:** Frame layout is read from the stores and the CRC length (count x 4 + 2). The CRC algorithm is in the wave-1 summary of bms_4168_08004da4. The receive side of the same protocol is in bms_proto_build_reply and bms_auth_verify_response.

- Addresses by version: 4130: 0x08004918, 4139: 0x08004B2C, 4148: 0x08004FDC, 4168: 0x08005128
- Called by: `bms_comm_request_dispatch`, `bms_comm_req_cmd02`, `bms_comm_req_cmd06`, `bms_comm_req_cmd04`, `bms_4168_080054f8`
- Calls: `crc16_usb_compute`, `bms_usart3_send_bytes`
- Confidence: high

## bms_comm_service_step

**Service the message pool: periodic 14-byte send, two busy timeouts, then dispatch the state handler**

Called once per service tick. It takes the elapsed ticks since DAT_200025FC from bms_tick_get (an extra tick is subtracted when the time base has wrapped) and, once more than 999 ticks have passed, enqueues a 14-byte message through bms_txq_enqueue with the header 0xB5 0x07 0x06 0x00 and the payload at 0x20002BF0; DAT_200025FC is restamped only if the enqueue succeeded. The busy flag DAT_20002612 is cleared, together with DAT_20002613, when more than 2999 ticks have passed since DAT_20002600; otherwise DAT_20002613 is cleared after 2999 ticks since DAT_20002604. It then calls the handler whose address is in the RAM table at 0x20000614 + 4 * DAT_2000260D, and returns 1 only when that state index is 0 and DAT_20002613 is clear, so 1 means idle. Part of the message pool group.

**Returns** `u32`: 1 when the state index is 0 and DAT_20002613 is clear, else 0

**Notes:** The 1000 and 3000 constants are taken as 1 ms ticks, which is an assumption. The handler table at 0x20000614 is in RAM and is filled elsewhere. The subtract-one on wrap is kept as the compiler produced it and may be an off-by-one.

- Addresses by version: 4148: 0x0800DC04, 4168: 0x0800E060
- Called by: `bms_4168_08007da4`
- Calls: `bms_tick_get`, `bms_txq_enqueue`
- Confidence: medium

## bms_frame_parse_legacy_4139

**Byte-wise parser for the 0x5A/0xA5 framed record packet with CRC-16 check (4130/4139)**

A state machine in DAT_20000114 consumes one received byte per call. A 0x5A or 0xA5 byte starts a frame and is saved at 0x2000083D. The next byte gives the record count N in its high nibble and the first nibble pair of the 16-bit header word at 0x20000124, and the byte after it completes that word; N = 0 jumps straight to the CRC states. The payload of N*4 bytes is appended to the frame buffer at 0x20000A7C (length in DAT_2000011C) and copied to 0x20000AAE. Two CRC bytes, most significant first, are compared with crc16_usb_compute over the header and payload (reflected poly 0x8005, init 0xFFFF, final complement). On a match, N is capped to 63 and each 4-byte record is stored at 0x20000840 with its byte order reversed, then DAT_20000115 and DAT_20000120 are set to 1; the parser returns to idle in every case once the CRC step is reached.

| Parameter | Type | Description |
|---|---|---|
| `rx_byte` | `u32` | received byte, low 8 bits used |
| `unused_arg2` | `u32` | unused |
| `unused_arg3` | `u32` | unused |
| `crc_arg` | `u32` | passed through unchanged as the last argument of crc16_usb_compute |

**Notes:** Header nibble layout is inferred from the shifts and masks, not from a protocol spec. The meaning of the 16-bit word at 0x20000124 beyond its role as CRC seed/state is not established.

- Addresses by version: 4130: 0x08006C08, 4139: 0x08007108
- Called by: `USART3_4_5_6_LPUART1_IRQHandler`
- Calls: `crc16_usb_compute`
- Confidence: medium

## bms_frame_parse_legacy_4168

**Byte-wise 0x5A/0xA5 framed-packet parser with CRC-16 check for the 4148/4168 builds**

The 4148/4168 counterpart of bms_frame_parse_legacy_4139, with the same states, frame layout and CRC step, using the RAM block at 0x200001AC..0x200001BE (state, counts, CRC word at 0x200001BC, header word at 0x200001BE) and the frame buffer at 0x20000B68. While the mode byte at 0x200001AE equals 2 each byte is handed to bms_frame_rx_byte and the function returns. A valid frame rebuilds 4-byte records at 0x2000092C with reversed byte order and sets DAT_200001AD to 1. The state resets to idle after the CRC step in every case.

| Parameter | Type | Description |
|---|---|---|
| `rx_byte` | `u32` | received byte, low 8 bits used |
| `unused_arg2` | `u32` | unused |
| `unused_arg3` | `u32` | unused |
| `crc_arg` | `u32` | passed through unchanged as the last argument of crc16_usb_compute |

**Notes:** Same protocol reading as the 4139 variant, so its uncertainties apply here too.

- Addresses by version: 4148: 0x08007938, 4168: 0x08007C10
- Called by: `USART3_4_5_6_LPUART1_IRQHandler`
- Calls: `crc16_usb_compute`, `bms_frame_rx_byte`
- Confidence: medium

## bms_frame_rx_byte

**Feed one received byte into the 0x5A 0xA5 framed parser; return 1 when a frame checks out**

This is a byte-at-a-time receive state machine. Its state is DAT_2000260e, the write index is DAT_20000610, the remaining payload count is DAT_20000611, the staged checksum is DAT_20000612, the valid-frame flag is DAT_2000260f, and the frame buffer starts at 0x2000256D. The frame layout as parsed is 0x5A, 0xA5, LEN (accepted only when below 0x81), a fixed 0x06, a byte that must equal byte 1 of the descriptor at *(DAT_20002608 + 4), a byte chosen by byte 0 of that descriptor (0x01 or '*' expects 0xAA, 0x02 or ',' expects 0xAC, 0xB5 expects 0xB5, 0x07 to 0x0A expect 0x0B), then LEN+1 payload bytes and a little-endian 16-bit checksum. The checksum is the one's complement of the 16-bit byte sum of frame bytes 2 through LEN+6, and a frame is accepted when (~sum) & 0xFFFF equals the received word. Any mismatch resets the state to 0, and a good checksum sets DAT_2000260f to 1 and returns 1 for the closing byte.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | received byte |

**Returns** `u32`: 1 when this byte completes a frame whose checksum matches, otherwise 0

**Notes:** The frame layout and the checksum range come from the index arithmetic in the decompile. The byte-0 rule table and the meaning of bytes 3 to 5 are read from constants, so the protocol identity and the meaning of the descriptor are inferred. The only caller is bms_4168_08007c10, and its use of the result is not in this packet.

- Addresses by version: 4148: 0x0800DCD4, 4168: 0x0800E128
- Called by: `bms_frame_parse_legacy_4168`
- Confidence: medium

## bms_frame_send_when_ready

**Submit one message, waiting up to 5 time-base ticks for the transmit path to free up**

Builds a small local message block from param_1 and param_3, takes a time stamp with bms_tick_get, and polls the busy check FUN_08008BFC while bms_tick_timeout_check has not expired after 5 ticks. It then calls FUN_08008C14 with the block to submit. A timeout is not reported: the submit is attempted anyway and the routine returns nothing. The block is initialised with memcpy (FUN_08001214) on an argument list not fully recovered from the decompile.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | message word stored into the local block |
| `param_2` | `u32` | not used by the routine |
| `param_3` | `u32` | second message word stored into the local block |

**Notes:** FUN_08008BFC (busy check) and FUN_08008C14 (submit) are not described in this packet, so the send semantics are inferred from the loop shape. Callers include bms_4168_0800e9dc and bms_4168_0800f8e0.

- Addresses by version: 4130: 0x0800AA40, 4139: 0x0800AF78, 4148: 0x0800B694, 4168: 0x0800B9A8
- Called by: `bms_4168_0800e9dc`, `bms_4168_0800ec04`, `bms_4168_0800eddc`, `bms_4168_0800f2e0`, `bms_4168_0800f8e0`, `bms_4168_0800fa88`
- Calls: `memcpy`, `bms_fdcan_tx_fifo_full`, `bms_fdcan_send_frame`, `bms_tick_get`, `bms_tick_timeout_check`
- Confidence: medium

## bms_j1939_tp_rx_dispatch

**Dispatch a received J1939 TP.CM or TP.DT frame to a session, creating one on an RTS**

Handles one received frame whose 32-bit identifier carries the PDU format in byte 2 and the destination and source addresses in bytes 1 and 0. A TP.CM frame (PF 0xEC) with control byte 0x10 (RTS) is offered first to the accept function at the start of the callback table at table+8 with the two addresses; if accepted, bms_slot_table_find returns or allocates the 36-byte session for that address pair and bms_4168_08010204 handles the RTS. Every other TP.CM frame and every TP.DT frame (PF 0xEB) is passed to bms_4168_08010204 for each session in the table, and each session decides whether the frame is for it. This is the receive entry point of the J1939 transport group with bms_j1939_tp_session_step, bms_j1939_tp_session_rx and bms_tp_tx_prepare.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | session table: +0 slot array (36-byte slots), +4 slot count (low 16 bits), +8 callback table pointer |
| `param_2` | `ptr` | received frame: 32-bit identifier at +0, DLC at +4, data from +5 |
| `param_3` | `u32` | unused by this function |
| `param_4` | `u32` | passed to the accept function |

**Notes:** The J1939 TP interpretation (PF 0xEC and 0xEB, control bytes 0x10, 0x11, 0x13, 0xFF, PGN 0xEF00) is from the constants in the code. The accept function's behaviour is in another packet.

- Addresses by version: 4130: 0x0800E12A, 4139: 0x0800E77E, 4148: 0x0800F9D6, 4168: 0x0800FF22
- Called by: `bms_4168_0800f2e0`
- Calls: `bms_slot_table_find`, `bms_j1939_tp_session_rx`
- Confidence: medium

## bms_j1939_tp_session_rx

**Process a received TP.CM or TP.DT frame for one session: RTS, CTS, EOM ACK, abort and data**

Handles one received frame for one 36-byte TP session by state (+2) and control byte. TP.CM frames with PGN 0xEF00 are handled as follows: CTS (0x11) opens the next send window (state 5), a zero-packet CTS puts the sender on hold (state 7 with a 1050-tick timeout), EOM ACK (0x13) completes a send (state 9 to idle, callback reason 3), and abort (0xFF) returns to idle. An RTS (0x10) is accepted when the session is idle or the peer matches; the size is read from data byte 1 only, the packet count from byte 3, and the session answers with a CTS requesting all ceil(size/7) packets and moves to state 10. In state 10 each TP.DT frame with the expected sequence number copies up to seven bytes into the payload at +4 and sums the bytes before the last two; on the last packet the two trailing bytes must equal the complement of that 16-bit sum (little endian), and then the session sends EOM ACK (0x13) and calls the completion callback at +8, otherwise it aborts with bms_j1939_tpcm_abort_pack.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | session object, same layout as bms_j1939_tp_session_step |
| `param_2` | `ptr` | received frame: 32-bit identifier at +0, DLC at +4, data from +5 |
| `param_3` | `ptr` | callback table: +4 event callback (reason 3 = complete), +8 data-complete callback (buffer, length), +0xC transmit function |

**Notes:** Only data byte 1 of an RTS is used as the size, so messages above 255 bytes cannot be received correctly even though the buffer check uses the full capacity at +8. The receive timeout between data frames is 750 ticks. A sequence error, a size or count mismatch, or a checksum failure ends in an abort.

- Addresses by version: 4130: 0x0800E40C, 4139: 0x0800EA60, 4148: 0x0800FCB8, 4168: 0x08010204
- Called by: `bms_j1939_tp_rx_dispatch`
- Calls: `bms_udiv32`, `bms_j1939_tpcm_abort_pack`
- Confidence: medium

## bms_j1939_tp_session_step

**Advance one J1939 TP transmit session: send RTS, data frames, and handle its timeouts**

Runs the transmit side of one 36-byte TP session, switching on the state byte at +2. State 3 builds the RTS (control 0x10, size as 16-bit little endian, ceil(size/7) packets, PGN 0x00EF00) and moves to state 4 to wait for CTS. States 4, 6, 7 and 9 count a timer at +0x16 against the timeout at +0x18, which is 1250 divided by the divisor at +0x14 (1050 in state 7), and on expiry call the callback at offset 4 with reason 1, send an abort through bms_j1939_tpcm_abort_pack, and return to idle. State 5 sends data frames of up to 7 bytes each (sequence number ceil(offset/7)+1, unused bytes 0xFF) from the payload at +4, advances the offset at +0xA, and when the window ends goes to state 6 (waiting for CTS) or, when the message is complete, to state 9 (waiting for the end-of-message ACK). The payload was prepared by bms_tp_tx_prepare with a 16-bit complemented checksum trailer, and the data pacing count is at +0x1C.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | session object: state at +2, peer addresses at +0 and +1, payload pointer at +4, offset at +0xA, size at +0xC, window end at +0x12, packet count at +0x10, timer at +0x16, timeout at +0x18, divisor at +0x14, pacing at +0x1A and +0x1C |
| `param_2` | `ptr` | callback table: +4 event callback (reason 1 = timeout), +0xC transmit function |

**Notes:** For messages of 8 bytes or fewer, state 3 still calls the transmit callback with the frame buffer that was not written on that path, and the identifier keeps its stale 0xA0000000 bits. Only sizes above 8 build a proper RTS. State 1 is idle.

- Addresses by version: 4130: 0x0800E1F4, 4139: 0x0800E848, 4148: 0x0800FAA0, 4168: 0x0800FFEC
- Called by: `bms_chan_service_all`
- Calls: `bms_udiv32`, `bms_j1939_tpcm_abort_pack`
- Confidence: medium

## bms_j1939_tpcm_abort_pack

**Build a J1939 TP.CM connection-abort frame for PGN 0xEF00 into a TX object**

Writes a fixed 8-byte J1939 TP.CM connection-abort frame into the object at param_3 and returns 1, or 0 when param_3 is null. The identifier is (0x1CEC0000 + param_2 * 0x100) | param_1, masked to 29 bits, so the priority is 7, the PGN is 0xEC00 (TP.CM), the destination address is param_2 in bits 8 to 15 and the source address is param_1 in bits 0 to 7; bit 31 of the old word is kept and bit 29 is forced to 1. The DLC is set to 8. The data bytes are 0xFF (the connection-abort control byte), 0xFF (the abort reason), three reserved 0xFF bytes, and then 0x00 0xEF 0x00, which is PGN 0x00EF00 in little-endian order in data bytes 5 to 7.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | source address, identifier bits 0 to 7 |
| `param_2` | `u8` | destination address, identifier bits 8 to 15 |
| `param_3` | `ptr` | TX object: word 0 identifier, byte 4 DLC, bytes 5 to 12 data |

**Returns** `u32`: 1 when the frame was written, 0 when param_3 is null

**Notes:** The protocol identity rests on the constants: 0x1CEC is TP.CM at priority 7, and control byte 0xFF is a connection abort. The reason byte 0xFF is not one of the usual J1939-21 reason codes, so the intent is uncertain. As in bms_can_pack_ext_frame, the handling of bits 29 and 31 is unconfirmed, and param_1 and param_2 are not limited to 8 bits.

- Addresses by version: 4130: 0x0800E86C, 4139: 0x0800EEC0, 4148: 0x08010120, 4168: 0x0801066C
- Called by: `bms_j1939_tp_session_step`, `bms_j1939_tp_session_rx`
- Confidence: medium

## bms_proto_build_reply

**Build the 0x5A 0xA5 reply frame for a received message and set the reply state**

Reads the received message through the pointer at DAT_20002608; its +4 field points to a frame whose byte 0 is the command, bytes 1 to 3 are header bytes, byte 8 is the payload length, and +4 points at the payload. A command is accepted only if it is 1, 2, 7 to 10, 0x2A, 0x2C or 0xB5 and byte 2 equals 6; otherwise the error flag 0x20002611 is set and the state at 0x2000260D becomes 4. Commands 7 to 10 also record bms_tick_get in 0x20002604. The reply is written at 0x200024E4 as 0x5A, 0xA5, the length, bytes 1 to 3, the reply command and the copied payload. Command 1 is answered with 0x2A, command 2 with 0x2C, 0x2A and 0x2C echo themselves, other commands echo the received byte, and command 10 only clears the pending flag 0x20002610.

**Notes:** The 0x5A 0xA5 magic matches bms_comm_send_frame, but the reply carries the length as a plain byte instead of a count nibble. The meaning of the commands is not in the packet. The routine has no direct caller in the packet.

- Addresses by version: 4148: 0x08006184, 4168: 0x080062F0
- Calls: `bms_tick_get`
- Confidence: medium

## bms_record_send_multiframe

**Send a queued record in up to 8-byte frames, advancing its address between frames**

Transmits a record in the bms_record_queue_pop layout: a word at +0, flags at +4 and +5, length at +6 and payload from +7. When param_4 is 1, it loops over the payload in pieces of min(remaining, 8) bytes, copying each piece to a local 8-byte frame buffer with memcpy, waiting for the transmit path as in bms_frame_send_when_ready, and submitting the frame through FUN_08008C14. Between frames the payload pointer advances by 8 and the remaining length drops by 8, and when param_2 is nonzero the word at +0 advances by 4 << (param_3 & 0xFF). The loop stops at the first failed submit or when the length is used up. param_4 of 2 returns success without sending, and any other mode returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | record to send, in the queue record layout |
| `param_2` | `s32` | nonzero: advance the word at +0 between frames |
| `param_3` | `u32` | address step exponent: the step is 4 << param_3 |
| `param_4` | `s32` | mode: 1 sends, 2 succeeds without sending, other values fail |

**Returns** `bool`: 1 when every submitted frame was accepted, otherwise 0

**Notes:** The meaning of the address word at +0 (destination address or ID) is not confirmed. FUN_08008C14 is outside this packet.

- Addresses by version: 4130: 0x0800AA8A, 4139: 0x0800AFC2, 4148: 0x0800B6DE, 4168: 0x0800B9F2
- Called by: `bms_4168_0800ddb0`
- Calls: `memcpy`, `bms_fdcan_tx_fifo_full`, `bms_fdcan_send_frame`, `bms_tick_get`, `bms_tick_timeout_check`
- Confidence: medium

## bms_rx_frame_7f0_7f1

**Receive hook for IDs 0x7F0 and 0x7F1: latch one byte-1 bit selected by the module state**

Receive handler for frames with ID 0x7F0 or 0x7F1 that always returns 1, meaning the frame is consumed. It accepts only frames whose flag byte at +4 is zero and whose DLC at +6 is at least 2, then reads data byte 1 at +7 (same layout as bms_record_queue_pop). The 16-bit state value at +2 of the object from bms_ram_20000bdc_addr selects which bit is tested: state 7 tests bit 2, state 6 tests bit 3 and state 5 tests bit 4, and any other state returns at once. A clear bit sets DAT_200004FC to 1. A set bit sets DAT_200004FC to 2 and stores the result of FUN_080097E8 in DAT_20000500.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | received frame record: ID u32 at +0, flags at +4, DLC at +6, data from +7 |

**Returns** `bool`: always 1: the frame is consumed

**Notes:** No direct caller is in the packet, so the routine is presumably registered as a receive callback. The meaning of the state value and of the 0x7F0/0x7F1 frames is not identified. FUN_080097E8 is outside this packet.

- Addresses by version: 4130: 0x0800C8C0, 4139: 0x0800CEBC
- Called by: `bms_4168_080056e8`
- Calls: `bms_tick_get`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_seq_state_reset

**Reset the fault sequence state: sub-state 0, start time, and a nibble snapshot**

Clears the sub-state index DAT_20001C8A and the byte DAT_20001C89, stamps the start time DAT_20001C78 with bms_tick_get, and loads DAT_20001C88 with the low nibble of the byte addressed by the RAM pointer at 0x20005D00 (bms_indirect_nibble_get). It sets up the state that bms_fault_record_service runs from.

**Notes:** The role of DAT_20001C89 and DAT_20001C88 is not established from this function alone.

- Addresses by version: 4130: 0x0800DDB0, 4139: 0x0800E404, 4148: 0x0800F5C0, 4168: 0x0800FAA0
- Called by: `bms_4168_08008724`
- Calls: `bms_indirect_nibble_get`, `bms_tick_get`
- Confidence: medium

## bms_syscfg_set_ucpd_strobe

**Replaces SYSCFG.CFGR1 bits 9-10 (UCPD1 and UCPD2 strobe) with the supplied value**

Read-modify-write of SYSCFG CFGR1 that clears bits 9 and 10 (UCPD1_STROBE and UCPD2_STROBE) with mask 0xFFFFF9FF and then ORs in the argument unchanged. The argument is not masked, so a caller that sets any bit outside 9-10 also writes that bit into CFGR1. It is called only from bms_4168_08002234, which is presumably the USB Power Delivery port setup.

| Parameter | Type | Description |
|---|---|---|
| `strobe_bits` | `u32` | value for CFGR1 bits 9-10; should contain nothing else |

**Notes:** The UCPD association comes from the register names in the SVD. The caller's purpose is not visible in this packet.

- Addresses by version: 4130: 0x080028A4, 4139: 0x080028A4, 4148: 0x080028A4, 4168: 0x080028A4
- Peripheral registers: `SYSCFG.CFGR1` (RW)
- Called by: `bms_4168_08002234`
- Confidence: medium

## bms_telemetry_block_fill

**Fill telemetry block 0 to 10 of the 176-byte frame at 0x20001B90 and write its check word**

Fills one 16-byte block of the telemetry frame at RAM 0x20001B90. Each block has a 32-bit check word at +0, written last from FUN_080097E8, and data from +7. A switch on param_1 selects the content: blocks 0, 2, 5 and 6 copy 16-bit and 8-bit fields from the state object returned by bms_ram_20000bdc_addr; block 1 writes a 16-bit value as four ASCII hex digits; block 3 packs flag bits into two 16-bit words; block 4 maps eight signed 16-bit values at object +0x12C to bytes (value + 0x32, 0xFF for a sample of 0xFF, 0xFD below -29, and 0xFE at 121 and above); blocks 7 and 8 take 8-byte pieces of a 14-byte staging copy at 0x20001C40 made from object +4; block 9 stores the packed RTC date and time from bms_4168_08009d84; and block 10 writes fields and status bits.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | block index, 0 to 10 |
| `param_2` | `u32` | not used by the routine |
| `param_3` | `u32` | not used by the routine |
| `param_4` | `u32` | not used by the routine |

**Notes:** The check word comes from FUN_080097E8, which is outside this packet. The field-by-field content of blocks 0, 2, 3, 5, 6 and 10 is recorded only at the level of byte offsets.

- Addresses by version: 4130: 0x0800C354, 4139: 0x0800C950
- Called by: `bms_4139_0800cd7c`
- Calls: `memcpy`, `bms_copy_bytes8`, `bms_rtc_datetime_pack`, `bms_tick_get`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_tp_tx_prepare

**Build a TP message in a transmit session: 3-byte header, payload, and 16-bit complement trailer**

Prepares a transmit session object for a message of param_9 payload bytes; it fails unless param_8 is nonnull, param_9 is below 0x6FA and param_9 + 5 fits the buffer capacity at +8. It stores the source and destination addresses from param_4 and param_5, writes the three header bytes param_3, param_6 and param_7, copies the payload from param_8, and appends the 16-bit sum of the header and payload, complemented, in little endian. It sets the total length at +0xC to param_9 + 5, clears the pacing counter at +0x1A, sets the pacing count at +0x1C through bms_4168_0800113c from the value at +0x14 plus param_10 minus 1, and moves the session to state 3 so that bms_j1939_tp_session_step sends the RTS on its next call. Part of the J1939 transport group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | transmit session object with payload buffer pointer at +4 and capacity at +8 |
| `param_2` | `u32` | unused by this function |
| `param_3` | `u8` | first header byte, stored at buffer offset 0 and included in the checksum |
| `param_4` | `u8` | source address, stored at session +0 |
| `param_5` | `u8` | destination address, stored at session +1 |
| `param_6` | `u8` | second header byte, stored at buffer offset 1 and included in the checksum |
| `param_7` | `u8` | third header byte, stored at buffer offset 2 and included in the checksum |
| `param_8` | `ptr` | payload source; must be nonnull |
| `param_9` | `u32` | payload length; must be below 0x6FA |
| `param_10` | `s32` | added to the value at +0x14 (minus one) for the pacing count |

**Returns** `u32`: 1 when the message was prepared, 0 when a check failed

**Notes:** The checksum covers the header and payload, and bms_j1939_tp_session_rx verifies the same sum. The pacing formula's meaning depends on bms_4168_0800113c, which is not yet described.

- Addresses by version: 4130: 0x0800E6D4, 4139: 0x0800ED28, 4148: 0x0800FF80, 4168: 0x080104CC
- Called by: `bms_4168_0800ff8e`
- Calls: `bms_4168_0800113c`
- Confidence: medium

## bms_txq_enqueue

**Queue a 9-byte message descriptor and payload into the first free of five pool slots**

Claims the first pool slot at 0x20002B8C (20-byte stride, five slots) whose flag byte is nonzero, sets the flag to 0, and writes the four header bytes of the descriptor, the length byte (+8) and the payload (copied from the pointer at +4) into the slot's 12-byte record at the pointer stored in slot+4 (records at 0x20002B14, payload buffers at 0x20002614 + 0x80 * slot). The tag param_2 goes to slot+0xC and the slot is appended to the singly linked list headed by DAT_20002608, with the link at slot+0x10, while DAT_2000260C counts the entries. If an entry already in the list has the same header bytes 0 and 3, the new slot is released again (flag 1) and the call returns 0 as a duplicate. Part of the message pool group with bms_txq_init, bms_comm_service_step and bms_reply_buffer_get.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | descriptor: bytes 0 to 3 header, pointer to the payload at +4, length byte at +8 |
| `param_2` | `u32` | tag stored at the slot's +0xC; callers pass a code address (LAB_080039d4_1 in bms_4168_0800e060) |

**Returns** `u32`: 1 when the message was appended; 0 for a duplicate, a full queue (count 5) or no free slot

**Notes:** The length byte is not checked against the 128-byte payload buffer, so a length above 128 overruns into the next buffer. The tag is only stored here; the code that uses it is outside this packet.

- Addresses by version: 4148: 0x0800DAD0, 4168: 0x0800DF2C
- Called by: `bms_comm_service_step`, `bms_4168_0800ec04`, `bms_4168_0800eddc`, `bms_4168_0800f2e0`
- Calls: `memcpy`
- Confidence: high

## bms_txq_init

**Reset the five-slot message pool, the queue head and counters, then stamp the periodic timer**

Initialises the message request pool used by bms_txq_enqueue. For each of the five 20-byte slots at 0x20002B8C it sets the flag to 1 (free), points the slot's first record at 0x20002B14 + 12 * i and its second record at 0x20002B50 + 12 * i, sets the buffer pointers of those records to 128-byte buffers at 0x20002614 + 0x80 * i and 0x20002894 + 0x80 * i, and clears the tag and link words. It then clears the queue head DAT_20002608, the queue count DAT_2000260C, the service state bytes DAT_2000260D to DAT_20002611 and the busy flags DAT_20002612 and DAT_20002613, and stores the current time base from bms_tick_get in DAT_200025FC as the start of the periodic send timer. Part of the message pool group.

- Addresses by version: 4148: 0x0800DB90, 4168: 0x0800DFEC
- Called by: `bms_4168_08010558`
- Calls: `bms_tick_get`
- Confidence: high
