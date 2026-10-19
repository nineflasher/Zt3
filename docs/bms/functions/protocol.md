# BMS - `protocol` functions

43 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_auth_verify_response`](#bms_auth_verify_response) | 0x08004FEC | Check a 16-byte reply (cmd 0x1D, type 4) against a value computed from the object at 0x20000BCC |
| [`bms_can_cmd_set_handler`](#bms_can_cmd_set_handler) | 0x0800EC04 | Validate CAN commands 0x82, 0x87 and 0xFA, store valid payloads in the state block and reply |
| [`bms_can_status_frame_rx`](#bms_can_status_frame_rx) | 0x0800E2C8 | Decode CAN frames 0x7F0, 0x7F1 and 0x212 and age out the 0x212 status flag after 2000 ticks |
| [`bms_chan_service_all`](#bms_chan_service_all) | 0x0800FEFC | Run the per-object state step for each of N 36-byte channel objects in a table |
| [`bms_comm_await_reply_cmd03`](#bms_comm_await_reply_cmd03) | 0x0800525C | Wait for the command-03 reply: accept into ctx+0x08, retry after 200 ticks, fault after 11 retries |
| [`bms_comm_pool_state_step`](#bms_comm_pool_state_step) | 0x08007DA4 | Advance the message-pool state machine: busy timer, handler dispatch and transitions |
| [`bms_comm_pool_tick_gated_4148`](#bms_comm_pool_tick_gated_4148) | (removed) | Step the 4148 message pool with the bit-5 enable from the state status byte |
| [`bms_comm_pool_tick_with_threshold`](#bms_comm_pool_tick_with_threshold) | 0x08007D48 | Step the message pool and publish the threshold pair in record 0x2C |
| [`bms_comm_req_cmd02`](#bms_comm_req_cmd02) | 0x08005228 | Send command 0x02 with no payload, reset the reply timer, and enter state 2 |
| [`bms_comm_req_cmd04`](#bms_comm_req_cmd04) | 0x080053C8 | Send command 0x04 with no payload, reset the reply timer, and enter state 4 |
| [`bms_comm_req_cmd06`](#bms_comm_req_cmd06) | 0x080052E0 | Send command 0x06 with no payload, reset the reply timer, and enter state 8 |
| [`bms_comm_request_dispatch`](#bms_comm_request_dispatch) | 0x08004DE8 | Pick the next queued link request (0x16, 0x1E, 0x18) and send it, else count the queue down |
| [`bms_comm_send_frame`](#bms_comm_send_frame) | 0x08005128 | Build and send a framed message on USART3: magic, command, count and sequence, payload, CRC-16 |
| [`bms_comm_service_step`](#bms_comm_service_step) | 0x0800E060 | Service the message pool: periodic 14-byte send, two busy timeouts, then dispatch the state handler |
| [`bms_frame_parse_legacy_4139`](#bms_frame_parse_legacy_4139) | (removed) | Byte-wise parser for the 0x5A/0xA5 framed record packet with CRC-16 check (4130/4139) |
| [`bms_frame_parse_legacy_4168`](#bms_frame_parse_legacy_4168) | 0x08007C10 | Byte-wise 0x5A/0xA5 framed-packet parser with CRC-16 check for the 4148/4168 builds |
| [`bms_frame_record_send`](#bms_frame_record_send) | 0x0800FA88 | Send a queued CAN record: 29-bit ID, length byte and payload through the frame sender |
| [`bms_frame_rx_byte`](#bms_frame_rx_byte) | 0x0800E128 | Feed one received byte into the 0x5A 0xA5 framed parser; return 1 when a frame checks out |
| [`bms_frame_send_when_ready`](#bms_frame_send_when_ready) | 0x0800B9A8 | Submit one message, waiting up to 5 time-base ticks for the transmit path to free up |
| [`bms_j1939_tp_rx_dispatch`](#bms_j1939_tp_rx_dispatch) | 0x0800FF22 | Dispatch a received J1939 TP.CM or TP.DT frame to a session, creating one on an RTS |
| [`bms_j1939_tp_session_rx`](#bms_j1939_tp_session_rx) | 0x08010204 | Process a received TP.CM or TP.DT frame for one session: RTS, CTS, EOM ACK, abort and data |
| [`bms_j1939_tp_session_step`](#bms_j1939_tp_session_step) | 0x0800FFEC | Advance one J1939 TP transmit session: send RTS, data frames, and handle its timeouts |
| [`bms_j1939_tpcm_abort_pack`](#bms_j1939_tpcm_abort_pack) | 0x0801066C | Build a J1939 TP.CM connection-abort frame for PGN 0xEF00 into a TX object |
| [`bms_limit_report_cmd08`](#bms_limit_report_cmd08) | 0x080054F8 | Derive a reserve current and send command 0x08 with a limit payload every 500 ticks |
| [`bms_msg_dispatch_request`](#bms_msg_dispatch_request) | 0x0800E9DC | Dispatch incoming BMS requests: data-block requests 4, 5, 6 and control commands of type 3 |
| [`bms_proto_build_reply`](#bms_proto_build_reply) | 0x080062F0 | Build the 0x5A 0xA5 reply frame for a received message and set the reply state |
| [`bms_record_send_multiframe`](#bms_record_send_multiframe) | 0x0800B9F2 | Send a queued record in up to 8-byte frames, advancing its address between frames |
| [`bms_rx_frame_7f0_7f1`](#bms_rx_frame_7f0_7f1) | (removed) | Receive hook for IDs 0x7F0 and 0x7F1: latch one byte-1 bit selected by the module state |
| [`bms_seq_state_reset`](#bms_seq_state_reset) | 0x0800FAA0 | Reset the fault sequence state: sub-state 0, start time, and a nibble snapshot |
| [`bms_syscfg_set_ucpd_strobe`](#bms_syscfg_set_ucpd_strobe) | 0x080028A4 | Replaces SYSCFG.CFGR1 bits 9-10 (UCPD1 and UCPD2 strobe) with the supplied value |
| [`bms_telemetry_block_fill`](#bms_telemetry_block_fill) | (removed) | Fill telemetry block 0 to 10 of the 176-byte frame at 0x20001B90 and write its check word |
| [`bms_telemetry_block_fill_16`](#bms_telemetry_block_fill_16) | 0x0800D76C | Pack telemetry record N (0 to 15) from the BMS state block and stamp it with the time base |
| [`bms_telemetry_sched_11_step`](#bms_telemetry_sched_11_step) | (removed) | Run the 11-record telemetry scheduler: refill and send one due record per call |
| [`bms_telemetry_sched_16_step`](#bms_telemetry_sched_16_step) | 0x0800DDB0 | Run the 16-record telemetry scheduler: pack and send one due record per call |
| [`bms_tp_send_block_4`](#bms_tp_send_block_4) | 0x0800E930 | Send the 20-byte block at 0x20001D9C as a type-4 TP message to the stored peer |
| [`bms_tp_send_block_5`](#bms_tp_send_block_5) | 0x0800E8DC | Send the 64-byte block at 0x20001DB0 as a type-5 TP message to the stored peer |
| [`bms_tp_send_block_6`](#bms_tp_send_block_6) | 0x0800E988 | Send the 64-byte block at 0x20001DF0 as a type-6 TP message to the stored peer |
| [`bms_tp_service_tick`](#bms_tp_service_tick) | 0x0800F8B4 | Run the TP session channel service once each time the time base advances |
| [`bms_tp_session_send`](#bms_tp_session_send) | 0x0800FF8E | Find or allocate the TP slot for a peer key pair, then prepare the transport message in it |
| [`bms_tp_tx_prepare`](#bms_tp_tx_prepare) | 0x080104CC | Build a TP message in a transmit session: 3-byte header, payload, and 16-bit complement trailer |
| [`bms_txq_enqueue`](#bms_txq_enqueue) | 0x0800DF2C | Queue a 9-byte message descriptor and payload into the first free of five pool slots |
| [`bms_txq_init`](#bms_txq_init) | 0x0800DFEC | Reset the five-slot message pool, the queue head and counters, then stamp the periodic timer |
| [`bms_ucpd_clock_irq_setup`](#bms_ucpd_clock_irq_setup) | 0x08002234 | Enables SYSCFG and PWR clocks, prioritises IRQ 4 (RCC_CRS) and sets the UCPD strobes |

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

## bms_can_cmd_set_handler

**Validate CAN commands 0x82, 0x87 and 0xFA, store valid payloads in the state block and reply**

CAN request handler for three commands. A valid payload is copied to the BMS state block at offset 2 times the command byte (0x82 to +0x104, 0x87 to +0x10E, 0xFA to +0x1F4). If the u16 at +2 of the state block differs from param_4, the request is not processed: its header and payload are queued through bms_txq_enqueue as an echo. Command 0x82 needs a 2-byte value from 0x50 to 0x64 (80 to 100) and sets bit 0x80 of the control word at 0x200001C8 when the value changes, while setting bit 0 and bit 1 or 2 of 0x200005C0 (the timer trim flags used by bms_pct_hysteresis_step). Command 0x87 needs a 4-byte packed time with hour and minute fields in range, and sets bit 3 of 0x200005C0 before the check. Command 0xFA needs two bytes that each lie from 91 to 109 and sets bit 4 of 0x200005C0 when the value changes. A payload whose length/2 plus command minus 1 exceeds 255 gets status 7. Replies carry status 0 (ok), 3 (0x82 rejected), 4 (0x87 or 0xFA rejected) or 7, and are sent as an extended CAN frame through bms_can_pack_ext_frame and bms_frame_send_when_ready unless param_6 is 3; an unknown command gets status 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | command byte (for example 0x82, 0x87, 0xFA) |
| `param_2` | `u32` | payload length in bytes |
| `param_3` | `ptr` | payload bytes |
| `param_4` | `u32` | requester word compared with the state block u16 at +2 |
| `param_5` | `u32` | reply field placed in the echo header |
| `param_6` | `s32` | reply mode: 3 suppresses the CAN reply, 0x2C selects reply code 0xAC |

**Notes:** The status numbers are read from the literal values returned to the reply encoder; their wire meaning is not documented here. The reply code 0x05 and 0xAC are the unexplained literals passed to bms_can_pack_ext_frame. The 0x50 to 0x64 and 91 to 109 ranges are read directly from the comparisons; the physical units are not known.

- Addresses by version: 4130: 0x0800D188, 4139: 0x0800D770, 4148: 0x0800E770, 4168: 0x0800EC04
- Called by: `bms_4168_0800f2e0`, `bms_4168_0800f8e0`
- Calls: `memcpy`, `bms_frame_send_when_ready`, `bms_ram_20000bdc_addr`, `bms_ram_200001c8_addr`, `bms_txq_enqueue`, `bms_get_block_200005c0_ptr`, `bms_can_pack_ext_frame`
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
- Called by: `bms_tp_service_tick`
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

## bms_comm_pool_state_step

**Advance the message-pool state machine: busy timer, handler dispatch and transitions**

State machine of the message pool. A zero gate (param_2) resets it: the busy timer 0x200001BA is cleared, bms_app_state_reset runs, bms_comm_service_step sets the send flag at 0x200001B8, and the state byte 0x200001AE becomes 2. A nonzero gate adds param_1 to the time counters 0x20000954 and 0x20000A58 and to the busy timer 0x200001BA, which saturates at 3000 while the not-timed-out flag 0x200001AF tracks it. In state 2 the routine calls bms_comm_service_step and moves on when the flag is set. In any other state it calls the handler selected by index 0x20000A49 (state 1, buffer 0x20000950) or 0x20000B4D (other states, buffer 0x20000A54) from the pointer table at 0x08010800. A handler index of 0 or an odd value, or a set service flag, ends the pass with a transition: the next-state table at 0x080107F7 is used while the reply buffer word at +6 is set (busy), otherwise 0x080107F4 when the byte 0x20000A53 is zero and 0x080107FA when it is not.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | elapsed time since the last call (added to the time counters) |
| `param_2` | `s32` | gate: 0 resets the pool, nonzero steps it |

**Notes:** The next-state tables at 0x080107F4, 0x080107F7 and 0x080107FA and the handler table at 0x08010800 are read from the decompile but not decoded here. The send and frame formats are in bms_comm_service_step and the handlers, not in this packet.

- Addresses by version: 4148: 0x08007A9C, 4168: 0x08007DA4
- Called by: `bms_comm_pool_tick_with_threshold`
- Calls: `bms_app_state_reset`, `bms_comm_service_step`, `bms_reply_buffer_get`
- Confidence: medium

## bms_comm_pool_tick_gated_4148

**Step the 4148 message pool with the bit-5 enable from the state status byte**

Thin 4148 wrapper. It fetches the state block through the accessor at 0x0800BB00 (not described in this packet), takes bit 5 of the byte at +0x194 as a 0 or 1 gate, and calls bms_4168_08007da4 (bms_comm_pool_state_step) with param_1 and that gate. A zero gate resets the message pool and a one gate steps it.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | elapsed time forwarded to the message pool step |

**Notes:** The 4148 image reaches the 4168 family of the pool step, so the pool logic is shared with the 4168 build.

- Addresses by version: 4148: 0x08007A70
- Called by: `bms_4168_08010558`
- Calls: `bms_comm_pool_state_step`, `bms_ram_20000bdc_addr`
- Confidence: high

## bms_comm_pool_tick_with_threshold

**Step the message pool and publish the threshold pair in record 0x2C**

4168 wrapper run once per tick. It calls bms_comm_pool_state_step with param_1 and the bit-5 gate of the state byte at +0x194. It then writes record 0x2C (bms_record12_addr) as two s16 values: state+0x6C when 0x200001AB is 1 or the reply buffer word at +6 (bms_reply_buffer_get) is nonzero, and otherwise 6, followed by that value minus 2 as the hysteresis partner.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | elapsed time forwarded to the message pool step |

**Notes:** The 4139 image writes the same record 0x2C pair in bms_pb11_trigger_sequence_step, so the record is shared by both builds.

- Addresses by version: 4168: 0x08007D48
- Called by: `bms_4168_08010558`
- Calls: `bms_comm_pool_state_step`, `bms_ram_20000bdc_addr`, `bms_record12_addr`, `bms_reply_buffer_get`
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
- Called by: `bms_comm_request_dispatch`, `bms_comm_req_cmd02`, `bms_comm_req_cmd06`, `bms_comm_req_cmd04`, `bms_limit_report_cmd08`
- Calls: `crc16_usb_compute`, `bms_usart3_send_bytes`
- Confidence: high

## bms_comm_service_step

**Service the message pool: periodic 14-byte send, two busy timeouts, then dispatch the state handler**

Called once per service tick. It takes the elapsed ticks since DAT_200025FC from bms_tick_get (an extra tick is subtracted when the time base has wrapped) and, once more than 999 ticks have passed, enqueues a 14-byte message through bms_txq_enqueue with the header 0xB5 0x07 0x06 0x00 and the payload at 0x20002BF0; DAT_200025FC is restamped only if the enqueue succeeded. The busy flag DAT_20002612 is cleared, together with DAT_20002613, when more than 2999 ticks have passed since DAT_20002600; otherwise DAT_20002613 is cleared after 2999 ticks since DAT_20002604. It then calls the handler whose address is in the RAM table at 0x20000614 + 4 * DAT_2000260D, and returns 1 only when that state index is 0 and DAT_20002613 is clear, so 1 means idle. Part of the message pool group.

**Returns** `u32`: 1 when the state index is 0 and DAT_20002613 is clear, else 0

**Notes:** The 1000 and 3000 constants are taken as 1 ms ticks, which is an assumption. The handler table at 0x20000614 is in RAM and is filled elsewhere. The subtract-one on wrap is kept as the compiler produced it and may be an off-by-one.

- Addresses by version: 4148: 0x0800DC04, 4168: 0x0800E060
- Called by: `bms_comm_pool_state_step`
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

## bms_frame_record_send

**Send a queued CAN record: 29-bit ID, length byte and payload through the frame sender**

Queue callback that transmits one record. The low 29 bits of the 32-bit word at param_2 are the CAN identifier, the byte at offset 4 is the length, and the payload starts at offset 5. These go to bms_frame_send_when_ready, and the function returns 1 whatever the send result. It is reached through a queue or pool function pointer, so it has no direct callers in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | unused by this callback |
| `param_2` | `ptr` | queue record: u32 ID word, u8 length at +4, payload from +5 |

**Returns** `u32`: always 1

**Notes:** The return value is a constant 1; whether the caller uses it as done or accepted is not visible here.

- Addresses by version: 4130: 0x0800DD98, 4139: 0x0800E3EC, 4148: 0x0800F5A8, 4168: 0x0800FA88
- Calls: `bms_frame_send_when_ready`
- Confidence: high

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
- Called by: `bms_msg_dispatch_request`, `bms_can_cmd_set_handler`, `bms_fw_upload_handle`, `bms_4168_0800f2e0`, `bms_4168_0800f8e0`, `bms_frame_record_send`
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

## bms_limit_report_cmd08

**Derive a reserve current and send command 0x08 with a limit payload every 500 ticks**

Builds the working limit DAT_200001C2 from the charge limit at state +0x120, replacing it with reply word +0x0C when the reply word +6 is nonzero, flag 0x20000B57 is set and the 0x194 bit 6 is clear (or the +0x11E and +0x11A conditions hold), and halving it when DAT_20000A53 and DAT_20000B57 are both 1. The 32-bit word at the argument's +0x14 packs three fields: bits 0 to 11 cap the limit, bits 12 to 17 are a divisor and bits 18 to 27 cap the limit again, and the cap from +0x10 (12 bits) is scaled by 100000/54370 (0xD462). It divides the limit and the caps by the divisor, keeps the smallest value and stores the product as the reserve DAT_200001C4, which bms_limit_status_update subtracts. When the argument's tick counter at +0x04 exceeds 499 it resets the counter, builds a 4-byte payload with the constant 0x2A7A in the low half and the limit in bits 16 to 27, sends it with bms_comm_send_frame as command 8, and sets the byte at +0xF9 to 10.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | unused |
| `param_2` | `ptr` | limit record: u32 tick counter at +0x04, u32 fields at +0x10 and +0x14, payload word at +0x2C, byte counter +0xFB, state byte +0xF9 |

**Notes:** The 0x2A7A constant is read as a fixed message tag, which is an inference. The divisor and cap semantics come from the bit extraction and are medium confidence. The 0xD462 scale is not identified.

- Addresses by version: 4130: 0x08004CDC, 4139: 0x08004EF8, 4148: 0x080053AC, 4168: 0x080054F8
- Calls: `bms_udiv32`, `bms_comm_send_frame`, `bms_ram_20000bdc_addr`, `bms_reply_buffer_get`
- Confidence: medium

## bms_msg_dispatch_request

**Dispatch incoming BMS requests: data-block requests 4, 5, 6 and control commands of type 3**

Receive-side dispatcher for the BMS request protocol; the first payload byte is the message type. Type 4 queues a 20-byte block: it proceeds only when the u32 from bms_u32_20001348_get is at least the u16 in bytes 1 and 2, stores that u16 and the requester pair, and registers pool type 2 with bms_4168_0800E930 as callback. Type 5 proceeds when the u32 at 0x20001348 is at least the u16 in bytes 3 and 4 and the u16 in bytes 1 and 2 is at most 10, and registers pool type 3 with bms_4168_0800E8DC. Type 6 proceeds when the u32 in bytes 1 to 4 is at most the word from bms_get_word_20001354, and registers pool type 4 with bms_4168_0800E988. Type 3 is a command: 0x81 and 0x89 are time/RTC commands answered through bms_tp_session_send, 0x82 stores a 4-byte value through bms_4168_08009F78 when the length byte is 4, 0x83 registers a pool type 1 entry with no buffer, and 0x84 reads the 0x20001348 word; 0x82, 0x83, 0x84 and any other command are answered with a short extended CAN reply built by bms_can_pack_ext_frame. Messages of other types are dropped.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | requester address; its low byte is stored as the first peer key byte |
| `param_2` | `ptr` | incoming message: byte 0 is the type, the following bytes are the request fields |
| `param_3` | `u32` | reply argument passed to the TP and CAN reply encoders |
| `param_4` | `u32` | requester address; its low byte is stored as the second peer key byte |

**Notes:** Callers bms_4168_0800F2E0 and bms_4168_0800F8E0 are not in this packet. The meaning of bms_4168_08009F78 (the 0x82 store) is not described yet; the 4-byte value matches the packed RTC format of bms_rtc_datetime_pack, so it may set the RTC. The 0x80 to 0x89 status names are not defined in the packet.

- Addresses by version: 4130: 0x0800CF60, 4139: 0x0800D548, 4148: 0x0800E548, 4168: 0x0800E9DC
- Called by: `bms_4168_0800f2e0`, `bms_4168_0800f8e0`
- Calls: `bms_rtc_datetime_pack`, `bms_rtc_set_datetime_packed`, `bms_slot_pool_register`, `bms_frame_send_when_ready`, `bms_u32_20001348_get`, `bms_tp_session_send`, `bms_can_pack_ext_frame`, `bms_get_word_20001354`
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
- Called by: `bms_telemetry_sched_16_step`
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
- Called by: `bms_extflash_probe_and_init`
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
- Called by: `bms_ucpd_clock_irq_setup`
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
- Called by: `bms_telemetry_sched_11_step`
- Calls: `memcpy`, `bms_copy_bytes8`, `bms_rtc_datetime_pack`, `bms_tick_get`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_telemetry_block_fill_16

**Pack telemetry record N (0 to 15) from the BMS state block and stamp it with the time base**

Fills telemetry record param_1 (0 to 15) of the 16-record table at 0x20001C8C (16-byte records: u32 stamp at +0, u16 CAN ID at +4, period byte at +6, 8-byte payload at +7) and writes bms_tick_get into the record's stamp at +0. The payload depends on the record: record 0 takes state bytes +0x118 to +0x11B, +0x1E and +0x1F and the u16 at +0x11E times 10; record 1 writes four ASCII hex digits of the u16 at +0x1C plus bytes +0x26, +0x27, +0xB6 and +0xB7; record 4 converts the eight s16 values at +0x12C to bytes as value+50, with 0xFF for missing, 0xFD below -29 and 0xFE at 121 and above; records 7 and 8 take 8-byte slices of a 14-byte copy of state bytes +4 onward; record 9 stores the packed RTC from bms_rtc_datetime_pack. Records 2, 5, 6 and 10 copy fixed state bytes with constant tags, and records 3, 11, 12, 13, 14 and 15 pack status bitfields and short fields from the state block and the reply buffer (for example, a 0x5AA5 check at +0x108 in record 3).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | record index, 0 to 15; values above 15 match no case but still write the stamp at index param_1 (out of range) |

**Notes:** Per-record byte layouts were read from the decompile and are not all named. The units of the packed values (hours, percent, temperature scale) are inferred from the encodings only. The helper bms_4168_08001246 is treated as a zero-fill, following bms_reply_buffer_get. Case 3 and records 11 to 15 use several bitfield masks that were not decoded bit by bit.

- Addresses by version: 4148: 0x0800D384, 4168: 0x0800D76C
- Called by: `bms_telemetry_sched_16_step`
- Calls: `bms_udiv32`, `memcpy`, `bms_copy_bytes8`, `bms_rtc_datetime_pack`, `bms_tick_get`, `bms_ram_20000bdc_addr`, `bms_reply_buffer_get`
- Confidence: medium

## bms_telemetry_sched_11_step

**Run the 11-record telemetry scheduler: refill and send one due record per call**

Background scheduler for the 11 telemetry records at 0x20001B90 (16 bytes each): u32 stamp at +0, CAN message ID at +4 (0x420, 0x421, 0x310, 0x422, 0x500, 0x423, 0x311, 0x501, 0x502, 0x424, 0x425), period byte at +6 in units of 100 ms (5, 5, 2, 5, 20, 5, 2, 20, 20, 10, 5), and eight payload bytes at +7. State DAT_200004FC: 0 initialises all stamps from bms_tick_get and the table, then moves to 1; 2 waits until bms_tick_timeout_check(DAT_20000500, 2000) expires and then moves to 1; 1 examines one record per call at index DAT_200004FD (wrapping after 10). When the record's period has elapsed it calls bms_telemetry_block_fill for that index, builds a frame of the ID word, bytes 0x00, 0x00, 0x08 and the eight payload bytes, sends it through bms_record_send_multiframe (FUN_0800AFC2 in this build), and advances the index. The frame buffer is zero-filled first with bms_4168_08001246.

**Notes:** The stamp at +0 is not reset here; it is assumed to be written by bms_telemetry_block_fill when the record is packed, which is what makes the period test work. The 'period in 100 ms units' reading relies on the *100 scaling of the threshold and on the 2000 ms timeout in state 2. The state 2 entry point is not set anywhere in this function. FUN_080097E8 (tick source at init) is not in this packet's callee list and is named only by its tick role.

- Addresses by version: 4130: 0x0800C780, 4139: 0x0800CD7C
- Called by: `bms_telemetry_sched_thunk`
- Calls: `bms_telemetry_block_fill`, `bms_mem_zero`, `bms_copy_bytes8`, `bms_tick_get`, `bms_tick_timeout_check`, `bms_record_send_multiframe`
- Confidence: medium

## bms_telemetry_sched_16_step

**Run the 16-record telemetry scheduler: pack and send one due record per call**

Background scheduler for the 16 telemetry records at 0x20001C8C, used by the 4148 and 4168 builds (the 11-record variant is bms_telemetry_sched_11_step). Initialisation (DAT_200005D0 == 0) stamps the table with bms_tick_get, sets CAN IDs 0x420 to 0x425, 0x429, 0x430 to 0x432 and 0x435, sets periods of 500, 500, 200, 500, 2000, 500, 200, 2000, 2000, 1000, 500, 500, 500, 500, 200 and 200 ms, and moves to state 1. State 2 waits for bms_tick_timeout_check(DAT_200005D4, 2000). State 1 examines one record per call at index DAT_200005D1: the index wraps at 12 when the u16 at +6 of the reply buffer is zero (so only records 0 to 11 are scanned), otherwise at 16. For a due record it calls bms_telemetry_block_fill_16 to pack the payload, sends the ID, 0x00, 0x00, DLC 8 and the payload through bms_record_send_multiframe (FUN_0800B9F2 in this build), and advances the index.

**Notes:** The 2000 ms state 2 timeout and the 100 ms period unit follow the *100 scaling and are read from the code. The reply-buffer test at +6 selecting 12 or 16 records is read literally; its meaning (for example a link or session flag) is not identified.

- Addresses by version: 4148: 0x0800D960, 4168: 0x0800DDB0
- Called by: `bms_telemetry_sched_thunk`
- Calls: `bms_mem_zero`, `bms_copy_bytes8`, `bms_tick_get`, `bms_tick_timeout_check`, `bms_record_send_multiframe`, `bms_telemetry_block_fill_16`, `bms_reply_buffer_get`
- Confidence: medium

## bms_tp_send_block_4

**Send the 20-byte block at 0x20001D9C as a type-4 TP message to the stored peer**

Builds a 21-byte message: byte 0 is 4 and the next 20 bytes are copied from 0x20001D9C, with the buffer otherwise zeroed. It is sent through bms_tp_session_send on the TP session at 0x200024C0 with command 0xAB, peer key bytes DAT_200005E2 and DAT_200005E3 (stored by bms_msg_dispatch_request), and length 0x15. It runs as the pool callback that bms_msg_dispatch_request registers for request type 4, and has no direct callers in this packet.

**Notes:** Sub-type 4 and the 0x15 length are read from the code. The meaning of the 20-byte block at 0x20001D9C is not identified.

- Addresses by version: 4130: 0x0800CEB4, 4139: 0x0800D49C, 4148: 0x0800E49C, 4168: 0x0800E930
- Calls: `memcpy`, `bms_tp_session_send`
- Confidence: high

## bms_tp_send_block_5

**Send the 64-byte block at 0x20001DB0 as a type-5 TP message to the stored peer**

Builds a 65-byte message: byte 0 is 5 and the next 64 bytes are copied from 0x20001DB0, inside a zeroed 68-byte buffer. It is sent through bms_tp_session_send on the TP session at 0x200024C0 with command 0xAB, peer key bytes DAT_200005E8 and DAT_200005E9 (stored by bms_msg_dispatch_request), and length 0x41. It has no direct callers in this packet; it runs as the pool callback that bms_msg_dispatch_request registers for request type 5.

**Notes:** Sub-type 5 and the 0x41 length are read from the code. The meaning of the 64-byte block at 0x20001DB0 is not identified.

- Addresses by version: 4130: 0x0800CE60, 4139: 0x0800D448, 4148: 0x0800E448, 4168: 0x0800E8DC
- Calls: `memcpy`, `bms_mem_zero`, `bms_tp_session_send`
- Confidence: high

## bms_tp_send_block_6

**Send the 64-byte block at 0x20001DF0 as a type-6 TP message to the stored peer**

Builds a 65-byte message: byte 0 is 6 and the next 64 bytes are copied from 0x20001DF0, inside a zeroed 68-byte buffer. It is sent through bms_tp_session_send on the TP session at 0x200024C0 with command 0xAB, peer key bytes DAT_200005EE and DAT_200005EF (stored by bms_msg_dispatch_request), and length 0x41. It runs as the pool callback that bms_msg_dispatch_request registers for request type 6, and has no direct callers in this packet.

**Notes:** Sub-type 6 and the 0x41 length are read from the code. The meaning of the 64-byte block at 0x20001DF0 is not identified.

- Addresses by version: 4130: 0x0800CF0C, 4139: 0x0800D4F4, 4148: 0x0800E4F4, 4168: 0x0800E988
- Calls: `memcpy`, `bms_mem_zero`, `bms_tp_session_send`
- Confidence: high

## bms_tp_service_tick

**Run the TP session channel service once each time the time base advances**

Calls bms_tick_timeout_check on DAT_200005DC with a threshold of one tick. When the time base has moved on, it runs bms_chan_service_all on the TP session object at 0x200024C0 and restarts the stamp at DAT_200005DC with bms_tick_get. It acts as a once-per-tick gate for the transport channel loop, so the channel service is never run more than once per tick.

**Notes:** The 1 ms tick rate is assumed from the ms-based timeouts elsewhere in the component. Caller bms_4168_08007F48 is not in this packet.

- Addresses by version: 4130: 0x0800DBC4, 4139: 0x0800E218, 4148: 0x0800F3D4, 4168: 0x0800F8B4
- Called by: `bms_timed_step_sequence_run`
- Calls: `bms_tick_get`, `bms_tick_timeout_check`, `bms_chan_service_all`
- Confidence: high

## bms_tp_session_send

**Find or allocate the TP slot for a peer key pair, then prepare the transport message in it**

Looks up the 36-byte TP slot for the key (param_4, param_5) in the session table at param_1 with bms_slot_table_find, with its fourth argument fixed at 0. If a slot is returned, it calls bms_tp_tx_prepare with the remaining arguments to build a multi-frame TP message, consisting of a 3-byte header, the payload and a 16-bit complement trailer. When no slot is available, the message is dropped. All callers in this packet pass the session object 0x200024C0, message fields 7 and 1, the TP command 0xAB, and a length of 0x41 or 0x15.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TP session object (0x200024C0 in every caller here) |
| `param_2` | `u32` | message field (7 in callers) |
| `param_3` | `u32` | message field (1 in callers) |
| `param_4` | `u32` | first peer key byte |
| `param_5` | `u32` | second peer key byte |
| `param_6` | `u32` | TP command byte (0xAB in callers) |
| `param_7` | `u32` | message field |
| `param_8` | `ptr` | message bytes |
| `param_9` | `u32` | message length in bytes |
| `param_10` | `u32` | flags, 0 in callers |

**Notes:** The meaning of the fourth argument of bms_slot_table_find (fixed at 0) is not stated in the packet and is taken as a no-allocate or default flag. The TP framing is taken from the bms_tp_tx_prepare summary in this packet. The meaning of the message fields 7 and 1 is not identified.

- Addresses by version: 4130: 0x0800E196, 4139: 0x0800E7EA, 4148: 0x0800FA42, 4168: 0x0800FF8E
- Called by: `bms_tp_send_block_5`, `bms_tp_send_block_4`, `bms_tp_send_block_6`, `bms_msg_dispatch_request`, `bms_4168_0800f2e0`
- Calls: `bms_slot_table_find`, `bms_tp_tx_prepare`
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
- Called by: `bms_tp_session_send`
- Calls: `bms_sdiv32`
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
- Called by: `bms_comm_service_step`, `bms_can_cmd_set_handler`, `bms_fw_upload_handle`, `bms_4168_0800f2e0`
- Calls: `memcpy`
- Confidence: high

## bms_txq_init

**Reset the five-slot message pool, the queue head and counters, then stamp the periodic timer**

Initialises the message request pool used by bms_txq_enqueue. For each of the five 20-byte slots at 0x20002B8C it sets the flag to 1 (free), points the slot's first record at 0x20002B14 + 12 * i and its second record at 0x20002B50 + 12 * i, sets the buffer pointers of those records to 128-byte buffers at 0x20002614 + 0x80 * i and 0x20002894 + 0x80 * i, and clears the tag and link words. It then clears the queue head DAT_20002608, the queue count DAT_2000260C, the service state bytes DAT_2000260D to DAT_20002611 and the busy flags DAT_20002612 and DAT_20002613, and stores the current time base from bms_tick_get in DAT_200025FC as the start of the periodic send timer. Part of the message pool group.

- Addresses by version: 4148: 0x0800DB90, 4168: 0x0800DFEC
- Called by: `bms_4168_08010558`
- Calls: `bms_tick_get`
- Confidence: high

## bms_ucpd_clock_irq_setup

**Enables SYSCFG and PWR clocks, prioritises IRQ 4 (RCC_CRS) and sets the UCPD strobes**

Sets APBENR2 bit 0 (SYSCFG clock) and APBENR1 bit 28 (PWR clock), each read back, then calls __NVIC_SetPriority(4, 0) and __NVIC_EnableIRQ(4) for IRQ 4, which the IRQ table names RCC_CRS. Finally it writes 0x600 to SYSCFG CFGR1 through bms_syscfg_set_ucpd_strobe (bms_4168_080028a4), setting both UCPD strobe bits 9 and 10. It has no return value and only bms_4168_080021c4 calls it, so it is probably USB Power Delivery port setup.

**Notes:** The IRQ 4 name comes from the stm32g0b1_irqs.json table. The UCPD purpose is inferred from the strobe bits and the caller.

- Addresses by version: 4130: 0x08002234, 4139: 0x08002234, 4148: 0x08002234, 4168: 0x08002234
- Peripheral registers: `RCC.APBENR1` (RW), `RCC.APBENR2` (RW)
- Called by: `bms_hw_init_systick_prefetch`
- Calls: `__NVIC_EnableIRQ`, `__NVIC_SetPriority`, `bms_syscfg_set_ucpd_strobe`
- Confidence: medium
