# BLE - `uart_bridge` functions

36 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`ble_app_frame_dispatch_20b`](#ble_app_frame_dispatch_20b) | 0x0C054180 | Dispatch an inbound 0x20B-channel frame to its handler or send status |
| [`ble_app_frame_dispatch_302`](#ble_app_frame_dispatch_302) | 0x0C05420C | Dispatch an inbound 0x302-channel frame to its handler or send status |
| [`ble_app_frame_dispatch_406`](#ble_app_frame_dispatch_406) | 0x0C0540F4 | Dispatch an inbound 0x406-channel frame to the request handler or send status |
| [`ble_app_queue_message`](#ble_app_queue_message) | 0x0C053F74 | Frame an app/UART message and queue it, splitting it when it exceeds the frame limit |
| [`ble_app_req_302_handle`](#ble_app_req_302_handle) | 0x0C054668 | Handle a 0x302-channel command (0x300, 0x301, 0x304) and reply or queue an event |
| [`ble_app_req_406_handle`](#ble_app_req_406_handle) | 0x0C054734 | Handle a 0x406-channel request: answer commands 0x400, 0x401 and 0x404 |
| [`ble_host_rx_buf_append`](#ble_host_rx_buf_append) | 0x0C05482C | Append bytes to the 0x574-byte host receive buffer, calling the overflow handler when full |
| [`ble_host_rx_chunk_handle`](#ble_host_rx_chunk_handle) | 0x0C053F24 | Append one host chunk to the reassembly buffer and dispatch it on the last chunk |
| [`ble_host_rx_msg_dispatch`](#ble_host_rx_msg_dispatch) | 0x0C05486C | Dispatch a completed host message by command word and clear the receive buffer |
| [`ble_msg_route_by_key`](#ble_msg_route_by_key) | 0x0C02C1E8 | Route a BLE message to the handlers registered for its command key, else forward it to the VCU |
| [`ble_slot_cmd_dispatch`](#ble_slot_cmd_dispatch) | 0x0C053018 | Dispatch app control command 0x200-0x209 for slot id param_1 and queue its 0x20B/0x20C/0x20E reply |
| [`ble_token_chunk_rx_7e`](#ble_token_chunk_rx_7e) | 0x0C02B264 | Receive one chunk of the 0x7E chunked token upload and save it after a checksum check |
| [`ble_uart1_open`](#ble_uart1_open) | 0x0C02D4F8 | Allocate the 292-byte UART1 receive buffer and open /dev/uart1 with timeout 100 and buffer 0x120 |
| [`ble_uart_frame_enqueue`](#ble_uart_frame_enqueue) | 0x0C02C338 | Build a 5A A5 UART frame from a message struct and queue it on the outbound ring |
| [`ble_uart_frame_route`](#ble_uart_frame_route) | 0x0C02B42C | Offer one received UART frame to the 0x7E, b1b4 and a8f8 handlers in turn |
| [`ble_uart_inject_cmd1`](#ble_uart_inject_cmd1) | 0x0C02D128 | Log a UART frame and re-dispatch it to ble_219_0c02a8f8 as command 1 |
| [`ble_uart_inject_cmd2`](#ble_uart_inject_cmd2) | 0x0C02D16C | Log a UART frame and re-dispatch it to ble_219_0c02a8f8 as command 2 |
| [`ble_uart_inject_cmd7e`](#ble_uart_inject_cmd7e) | 0x0C02D1B0 | Log a UART frame and feed it to the 0x7E token chunk handler with the command forced to 0x7E |
| [`ble_uart_irq17_handler`](#ble_uart_irq17_handler) | 0x0C0467B8 | UART IRQ17 handler: drain RX FIFO into the instance queue, run the registered callback |
| [`ble_uart_irq18_handler`](#ble_uart_irq18_handler) | 0x0C0467C4 | UART IRQ18 vector entry: same UART IRQ body with context at 0x2000F514 |
| [`ble_uart_irq26_handler`](#ble_uart_irq26_handler) | 0x0C0467D0 | UART IRQ26 vector entry: same UART IRQ body with context at 0x2000F534 |
| [`ble_uart_port_start`](#ble_uart_port_start) | 0x0C046494 | Start UART port 0..2: 115200-baud config, IRQ handler install and RX interrupt enable |
| [`ble_uart_process_task`](#ble_uart_process_task) | 0x0C02D358 | UART1 receive task: reassemble 5A A5 and 55 AA frames and answer the D1x single-UART test |
| [`ble_uart_rx_dma_commit`](#ble_uart_rx_dma_commit) | 0x0C046468 | Commit DMA-received bytes to the UART stream head from ISR and re-arm the receive pump |
| [`ble_uart_rx_dma_pump`](#ble_uart_rx_dma_pump) | 0x0C0462C4 | Keep one UART instance receive DMA running into its stream write side; signal readable |
| [`ble_uart_tx_dma_pump`](#ble_uart_tx_dma_pump) | 0x0C046380 | Keep one UART instance transmit DMA fed from the stream read side; signal writable |
| [`bt_vcu_cmd_wr_process`](#bt_vcu_cmd_wr_process) | 0x0C02A484 | Process a VCU command read (cmd 1) and build the reply from the index using cached or default values |
| [`uart_bridge_queue_init`](#uart_bridge_queue_init) | 0x0C0355C8 | Create a 32-byte static queue and pass it with a fixed id to ble_219_0c0484b4 |
| [`uart_bridge_send_frame`](#uart_bridge_send_frame) | 0x0C02C124 | Build a 5A A5 UART frame with four header bytes, optional payload and checksum, then send it |
| [`uart_bridge_write_channel0`](#uart_bridge_write_channel0) | 0x0C02E758 | Write a buffer to the UART2 fd for channel 0 under the channel mutex and report errors |
| [`uart_disp_get_channel_ctx`](#uart_disp_get_channel_ctx) | 0x0C028790 | Return the UART dispatcher context for channel 0, else NULL |
| [`uart_disp_get_channel_fd`](#uart_disp_get_channel_fd) | 0x0C02E57C | Return the /dev/uart2 file descriptor for channel 0, else -1 |
| [`uart_disp_rx_process`](#uart_disp_rx_process) | 0x0C02E7D8 | Parse 55 AA and 5A A5 frames from the UART RX ring and dispatch them to handlers |
| [`uart_disp_rx_task`](#uart_disp_rx_task) | 0x0C02EB60 | Body of the 'nb uart disp' task: wait for UART data with select and run the RX parser |
| [`uart_disp_send_frame`](#uart_disp_send_frame) | 0x0C02E5A4 | Build a 55 AA or 5A A5 dispatcher frame from a request record and write it to the UART |
| [`uart_disp_start_service`](#uart_disp_start_service) | 0x0C02E420 | Start the UART dispatcher: open /dev/uart2, register stream buffers and spawn its RX task |

## ble_app_frame_dispatch_20b

**Dispatch an inbound 0x20B-channel frame to its handler or send status**

Same structure as ble_app_frame_dispatch_406 for the 0x20B channel (replies carry id 0x20B). Frames shorter than 3 bytes write 0xFFFF0000 into the table at 0x2001231C and send a 4-byte status reply when a slot is in use, returning 1. Type-1 frames are passed to ble_219_0c053018 (not yet described) and return 0. Other frames store (3 << 16) | value in the table and send the 0x20B reply when a slot is in use, returning 0xE in both cases.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | reply context passed to ble_app_queue_message |
| `param_2` | `u32` | frame length |
| `param_3` | `ptr` | frame bytes; byte 0 is the command type |
| `param_4` | `u32` | passed through to the type-1 handler |

**Returns** `u32`: 0 when dispatched to the type-1 handler, 1 for short status frames, 0xE for other frames

- Addresses by version: 219: 0x0C054180
- Called by: `ble_proto_dispatch_op`
- Calls: `ble_slot_cmd_dispatch`, `ble_slot_count_used`, `ble_app_queue_message`, `ble_counter_20012344_step`
- Confidence: medium

## ble_app_frame_dispatch_302

**Dispatch an inbound 0x302-channel frame to its handler or send status**

Same structure as ble_app_frame_dispatch_406 for the 0x302 channel (replies carry id 0x302). Frames shorter than 3 bytes write 0xFFFF0000 into the table at 0x2001231C, send a 4-byte status reply when a slot is in use and return 1. Type-1 frames are handed to ble_app_req_302_handle and return 0. Other frames store (3 << 16) | value in the table, send the 0x302 reply when a slot is in use and return 0xE.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | reply context passed to ble_app_queue_message |
| `param_2` | `u32` | frame length |
| `param_3` | `ptr` | frame bytes; byte 0 is the command type |
| `param_4` | `u32` | passed through to the request handler |

**Returns** `u32`: 0 when dispatched to the request handler, 1 for short status frames, 0xE for other frames

- Addresses by version: 219: 0x0C05420C
- Called by: `ble_proto_dispatch_op`
- Calls: `ble_slot_count_used`, `ble_app_queue_message`, `ble_app_req_302_handle`, `ble_counter_20012344_step`
- Confidence: medium

## ble_app_frame_dispatch_406

**Dispatch an inbound 0x406-channel frame to the request handler or send status**

Frame dispatcher for the 0x406 channel; status replies carry message id 0x406. Frames shorter than 3 bytes are status-only: the entry at index = ble_counter_20012344_step() of the 11-entry table at 0x2001231C is set to 0xFFFF0000, and if any slot is in use (ble_slot_count_used) a 4-byte reply is sent with ble_app_queue_message; the function returns 0xE. For longer frames whose first byte is not 1, the 16-bit value from bytes 1-2 is stored as (3 << 16) | value in the same table entry and sent as the 0x406 reply when a slot is in use; the function returns 1. Frames whose first byte is 1 are passed to ble_app_req_406_handle with the payload, and the function returns 0. The counter at 0x20012344 is the last table entry (index 10).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | reply context passed to ble_app_queue_message |
| `param_2` | `u32` | frame length |
| `param_3` | `ptr` | frame bytes; byte 0 is the command type |
| `param_4` | `u32` | passed through to the request handler |

**Returns** `u32`: 0 when dispatched to the request handler, 1 or 0xE for status frames

**Notes:** The return values of the three ble_app_frame_dispatch_* functions are not uniform: here short frames return 0xE and long non-1 frames return 1, the reverse of ble_app_frame_dispatch_20b and ble_app_frame_dispatch_302 for the status path.

- Addresses by version: 219: 0x0C0540F4
- Called by: `ble_proto_dispatch_op`
- Calls: `ble_slot_count_used`, `ble_app_queue_message`, `ble_app_req_406_handle`, `ble_counter_20012344_step`
- Confidence: medium

## ble_app_queue_message

**Frame an app/UART message and queue it, splitting it when it exceeds the frame limit**

Builds frames in a 0xF7-byte buffer at 0x20012348 (zeroed first with memset). Message codes 0x1FF and 0x6FF use a 1-byte header (0x01) with the payload at +1. Other codes use a 3-byte header: 0x01 followed by the 16-bit message code at +1 (little-endian), and the payload at +3. Payloads larger than the per-frame limit DAT_20004072 are split: the first chunk is queued with ble_app_start_deferred_500ms_op (0x0c05cb08, which stores the operation and arms a 500 ms timer), and the remainder is kept as pending-fragment state in 0x20012310 (code), 0x20012314 (source offset) and 0x20012318 (remaining length). Codes with high byte 0x02 are first checked by ble_slot_mgr_check_flag5 (0x0c0531b8) and dropped when it returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | context passed to the queue operation |
| `param_2` | `u16` | message code |
| `param_3` | `ptr` | payload bytes |
| `param_4` | `u32` | payload length |

**Notes:** The per-frame limit is a u8 global at 0x20004072. Frame-type meaning of codes 0x1FF and 0x6FF is inferred.

- Addresses by version: 219: 0x0C053F74
- Called by: `ble_slot_cmd_dispatch`, `ble_app_frame_dispatch_406`, `ble_app_frame_dispatch_20b`, `ble_app_frame_dispatch_302`, `ble_slot_store_and_queue`
- Calls: `ble_slot_mgr_check_flag5`, `ble_app_start_deferred_500ms_op`, `memcpy`, `memset`
- Confidence: medium

## ble_app_req_302_handle

**Handle a 0x302-channel command (0x300, 0x301, 0x304) and reply or queue an event**

Handles the 16-bit command word in *param_2 on the 0x302 channel. It proceeds only when ble_state_12c81_is_2 is false and ble_slot_test_flag_any on slot param_1 with bit 5 is clear; otherwise it replies with status 0xFFFF. The command is validated with ble_pair_table_lookup against the table at 0x200041A0. Command 0x300, when bit 2 of slot 0xFE is clear, sets that bit with ble_slot_set_flag, queues event 0x0A and replies with status 0; if the bit is set it replies with status 1. Command 0x301, when bit 2 is set, queues event 0x0B and sends no reply; otherwise it replies with status 1. Command 0x304 sets DAT_20012605 to 1, which ble_fmna_pair_adv_service consumes, and replies with status 0. Other commands are dropped without a reply. Replies go through ble_slot_store_and_queue with id 0x302, carrying the command and the status, and a failed lookup replies with the lookup code (3 or 0xFFFF).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | slot or context handle used for the flag tests |
| `param_2` | `ptr` | frame: u16 command word followed by arguments |
| `param_3` | `u32` | frame payload length |

- Addresses by version: 219: 0x0C054668
- Called by: `ble_app_frame_dispatch_302`
- Calls: `ble_slot_test_flag_any`, `ble_slot_set_flag`, `ble_pair_table_lookup`, `ble_slot_store_and_queue`, `ble_state_12c81_is_2`, `ble_evt_post_u16`
- Confidence: medium

## ble_app_req_406_handle

**Handle a 0x406-channel request: answer commands 0x400, 0x401 and 0x404**

Handles requests on the 0x406 channel (frames with type byte 1). The command word is checked with ble_pair_table_lookup against the table at 0x200041AC; on failure it sends an error frame 0x406 carrying the command. Command 0x401 replies with frame 0x403 carrying a 60-byte identity string, read from ROM at 0x0C07462C when the slot manager is not ready and from RAM at 0x2001093D when it is ready. Command 0x400 replies with frame 0x402 carrying a 28-byte block, read from ROM at 0x0C074810 or RAM at 0x20012B90 by the same test. Command 0x404 replies with 0x406 status 1 when flag byte 0x20012606 is set or the slot manager is not ready; otherwise it calls ble_219_0c053e1c(1) (the bt session message) and replies with frame 0x405 carrying 141 bytes. Replies are queued with ble_app_queue_message only when a slot is in use; other commands are ignored.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | reply context passed to ble_app_queue_message |
| `param_2` | `ptr` | frame: u16 command word followed by arguments |
| `param_3` | `u32` | frame payload length |

- Addresses by version: 219: 0x0C054734
- Called by: `ble_app_frame_dispatch_406`
- Calls: `ble_slot_cmd_dispatch`, `ble_slot_mgr_is_ready`, `ble_session_msg_build`, `ble_pair_table_lookup`, `ble_slot_store_and_queue`
- Confidence: medium

## ble_host_rx_buf_append

**Append bytes to the 0x574-byte host receive buffer, calling the overflow handler when full**

Appends param_2 bytes from param_1 to the host receive buffer whose u16 length sits at 0x20012608 and whose payload starts at 0x2001260A (capacity 0x572 bytes; the whole block is 0x574 bytes). If used + param_2 exceeds 0x572 it first calls ble_219_0c0537b4(1) (not yet described, an overflow handler) and re-reads the length, then memcpy's the bytes to the end of the payload and advances the length. Always returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | bytes to append |
| `param_2` | `s32` | number of bytes to append |

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C05482C
- Called by: `ble_host_rx_chunk_handle`
- Calls: `ble_fmna_reset_gen_keypair`, `memcpy`
- Confidence: high

## ble_host_rx_chunk_handle

**Append one host chunk to the reassembly buffer and dispatch it on the last chunk**

Takes the frame length in param_2 and the frame in param_3, whose first byte is a flag (1 marks the last chunk). If the slot manager is not ready (ble_slot_mgr_is_ready returns 0) it returns 0xF. Otherwise the bytes after the flag are appended to the host buffer at 0x20012608 with ble_host_rx_buf_append. When the appended chunk carries the last-chunk flag, a total length under 3 bytes clears the buffer with ble_host_ctx_clear_2608 and returns 0xE; a longer message is dispatched by ble_host_rx_msg_dispatch and the function returns 0. Non-final chunks always return 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | unused in this function |
| `param_2` | `u32` | frame length including the flag byte |
| `param_3` | `ptr` | frame bytes; byte 0 is the last-chunk flag, the rest is payload |

**Returns** `s32`: 0 ok, 0xE short final chunk (buffer cleared), 0xF slot manager not ready

- Addresses by version: 219: 0x0C053F24
- Called by: `ble_proto_dispatch_op`
- Calls: `ble_slot_mgr_is_ready`, `ble_host_ctx_clear_2608`, `ble_host_rx_buf_append`, `ble_host_rx_msg_dispatch`
- Confidence: medium

## ble_host_rx_msg_dispatch

**Dispatch a completed host message by command word and clear the receive buffer**

Consumes the complete message in the host buffer at 0x20012608. The command word is the u16 at 0x2001260A and the body starts at 0x2001260C. The command is checked with ble_pair_table_lookup against the table at 0x200041B8 using the buffer length: command 0x102 accepts lookup codes 0 and 3 and then copies 0x529 bytes to 0x200104B4, writes the 60-byte identity string at 0x2001093D to NV record 0xFB2 (ble_nv_record_write) and queues event 0x0F. Command 0x104 queues event 0x10, and command 0x100 copies 0x91 bytes into the record A area at 0x200109E0 and queues event 0x0E. Other commands do nothing. Commands other than 0x102 require lookup code 0. When the check fails the function calls ble_219_0c0537b4(1) and returns without the final clear; otherwise the 0x574-byte buffer is zeroed with memset.

**Notes:** The 0x0C0537B4 handler is not described yet, so whether it also resets the buffer is unknown. Event numbers 0x0E and 0x0F are not named in other packets yet.

- Addresses by version: 219: 0x0C05486C
- Called by: `ble_host_rx_chunk_handle`
- Calls: `ble_fmna_reset_gen_keypair`, `ble_pair_table_lookup`, `ble_evt_post_u16`, `ble_nv_record_write`, `memcpy`, `memset`
- Confidence: medium

## ble_msg_route_by_key

**Route a BLE message to the handlers registered for its command key, else forward it to the VCU**

Builds the message view used by the handlers (type byte at +2, command byte at +3, 16-bit index at +4 to +5, sub-code at +6, payload pointer at +7) and forms a 24-bit route key from the command byte and the two index bytes. Table A at DAT_20009480 (8-byte entries of key and handler) and table B (12-byte entries of mask, key and handler) are scanned, and every handler whose key matches is called with the message view and param_2; table B matches when key AND mask equals the stored key. If any handler ran the function returns. Otherwise, if ble_get_byte_12eb4 returns 0, the message is wrapped as a 0x66 message and sent to the VCU with ble_219_0c02e5a4, logging 'ERROR:ble to uart send faild[%d]' on failure; if it returns non-zero the message goes to ble_219_0c02a484 instead.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | message struct: +2 type, +3 command, +4 and +5 index, +6 sub-code, +7 payload |
| `param_2` | `u32` | passed unchanged to every matched handler as its third argument |

**Notes:** The table layouts are read from the code, not from a documented struct. The handlers registered in tables A and B are not in this packet. The 0x66-wrapped forward is the same message type that the reply helper ble_219_0c02e5a4 sends elsewhere in the packet.

- Addresses by version: 219: 0x0C02C1E8
- Called by: `ble_rx_data_handler`, `ble_crypto_try_default_pwd`
- Calls: `bt_vcu_cmd_wr_process`, `uart_disp_send_frame`, `trace_printf`, `ble_get_byte_12eb4`
- Confidence: medium

## ble_slot_cmd_dispatch

**Dispatch app control command 0x200-0x209 for slot id param_1 and queue its 0x20B/0x20C/0x20E reply**

Command dispatcher for the app and UART control channel. param_1 is the slot id (0xFE in the helper calls means every slot), param_2 points to the request (u16 command code at +0, u16 argument at +2, a byte at +2 for flags), and param_3 is forwarded to the duplicate lookup. Requests are refused with status 1 unless the slot manager is ready (ble_slot_mgr_is_ready) and the slot has flag bit 5. First, ble_pair_table_lookup checks the command against a 10-entry table at 0x20003FC0; a hit replies with the stored status (0xFFFF becomes command 0). Commands: 0x200 sets flag 2 for the slot and schedules 0x0C055440(10) when no slot has flag 2; 0x201 schedules 0x0C055440(11) when a slot has it; 0x202 sets flag 0 when the byte argument is nonzero (only if no slot has it; then, if the host enable byte 0x20012B85 is set and fewer slots are used than the limit, rebuilds the status advertisement with ble_fmna_adv_status_ad_build and 0x0C05C320, and disables timer 0x20012C6C), or clears flag 0; 0x203 stores the u16 argument times 1000 at 0x200041C8 when it is below 3601 (ble_set_timeout_ms_to_us) and otherwise answers status 4; 0x204 stores a byte at 0x200101E0 when the limit is one and exactly one slot is used; 0x205 checks a time window against 0x20012B8C and 0x200041C4, restarts timer 0x20012C3C through ble_host_timer_restart and sends no reply; 0x206 copies the staging block at 0x20012B8C into the active block (0x20012B88 and 0x20012BDC to 0x20012C08) and replies 0x20E with 4 bytes; 0x207 sets the slot limit DAT_20003FE8 to min(argument, 4) and, for argument 1, tears down the other occupied slots with 0x0C05C850, replying 0x20B only when none were torn down; 0x208 acknowledges; 0x209 replies 0x20C with the OR of the slot flag words, plus 0x40 when another slot has flag 5. Replies go through ble_slot_store_and_queue (0x20B with command and status) or ble_app_queue_message (0x20C and 0x20E frames). Other opcodes do nothing.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | slot id (low byte); 0xFE addresses all slots in the helper calls |
| `param_2` | `ptr` | request record: u16 command code at +0, u16 argument at +2 (byte at +2 for flag commands) |
| `param_3` | `u32` | value forwarded to the duplicate-command lookup |

**Notes:** The helpers 0x0C055440, 0x0C05C320 and 0x0C05C850 take their slot or delay argument implicitly in the decompile. The byte stored by 0x0C053830 for command 0x204 is not visible. The write to 0x200101D8 used as a teardown flag in command 0x207 is an odd location and is inferred.

- Addresses by version: 219: 0x0C053018
- Called by: `ble_app_frame_dispatch_20b`, `ble_app_req_406_handle`
- Calls: `ble_fmna_adv_status_ad_build`, `ble_slot_test_flag`, `ble_slot_test_flag_any`, `ble_slot_set_flag`, `ble_slot_count_used`, `ble_slot_mgr_is_ready`, `ble_ctrl_get_flag_3fe8`, `ble_slot_set_flag_101e0`, `ble_pair_table_lookup`, `ble_app_queue_message`, `ble_slot_store_and_queue`, `ble_set_timeout_ms_to_us`, `ble_evt_post_u16_ctx`, `ble_evt_post_u16`, `ble_host_timer_set_enabled`, `ble_get_byte_12b85` ...
- Confidence: medium

## ble_token_chunk_rx_7e

**Receive one chunk of the 0x7E chunked token upload and save it after a checksum check**

Handles UART command 0x7E, a chunked upload of a blob of at most 0x410 (1040) bytes, and returns 0 for any other command. Chunk index 0 is the start frame: payload byte 0 is an MTU class (1 to 4, which sets the chunk-size code 2, 8, 0x80 or 0x400 in the low halfword of the reply word 0x20009278; other values give status 3), byte 1 must be 1, bytes 2 to 3 carry the sender's checksum and bytes 4 to 7 the total length, which must be below 0x410; the buffer comes from ble_219_0c053884 and is zeroed with memset. Chunk indices 0x40 to 0xFE are data chunks that must arrive in order, starting at 0x40 and incrementing by one per chunk, and each is appended with memcpy. When the last byte arrives the blob is summed as 16-bit bytes, the sum is complemented and compared with the sender's value, and on a match the blob is passed to ble_219_0c05c8a8 (log 'save token err' on failure). The reply is a status word: 0 OK, 1 checksum or save failure, 3 bad start frame or state, 4 out-of-sequence chunk or overflow. The reply goes to the outbound ring through ble_219_0c02c338 when param_1 is 1, otherwise it is sent directly with uart_bridge_send_frame (ble_219_0c02c124) using the request's two address bytes in swapped order.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | reply mode: 1 queues the reply in the outbound ring, any other value sends it straight to UART |
| `param_2` | `u32` | first address byte of the request, placed in the reply's header in swapped position |
| `param_3` | `u32` | second address byte of the request, placed in the reply's header in swapped position |
| `param_4` | `s32` | command byte; only 0x7E is handled |
| `param_5` | `u8` | chunk index: 0 for the start frame, 0x40 to 0xFE for data chunks |
| `param_6` | `u8` | payload length in bytes |
| `param_7` | `ptr` | payload bytes |

**Returns** `s32`: 1 if the command was 0x7E and was consumed (including error statuses), 0 otherwise

**Notes:** The blob's purpose is inferred from the log text 'save token' only. The store routine ble_219_0c05c8a8 and allocator ble_219_0c053884 are not described yet. The checksum is a plain 16-bit byte sum, complemented, although the log text says crc. The log prints only byte 0x20009266 of the sender's value. Whether the reply's high halfword (0x2000927A) is always the computed checksum on the non-final ACKs is not confirmed.

- Addresses by version: 219: 0x0C02B264
- Called by: `ble_uart_frame_route`, `ble_vcu_cmd_handle`, `ble_uart_inject_cmd7e`
- Calls: `uart_bridge_send_frame`, `ble_uart_frame_enqueue`, `trace_printf`, `ble_get_state_ptr_11e10`, `ble_crypto_nv_store_blob`, `memcpy`, `memset`
- Confidence: medium

## ble_uart1_open

**Allocate the 292-byte UART1 receive buffer and open /dev/uart1 with timeout 100 and buffer 0x120**

Allocates 0x124 bytes with ble_219_0c07097c (malloc-like) into DAT_20009890 and opens '/dev/uart1' with flags 0 into DAT_20003E20. On success it issues three ioctl-style driver calls on that descriptor: request 0x22 with argument 0, request 0x14 with 100, and request 0x13 with 0x120. On failure it logs 'open uart1 failed\r\n' and leaves the descriptor negative.

**Notes:** The meanings of the three ioctl requests are not known. The 100 is probably a read timeout in ticks, matching the ring reader in ble_uart_process_task. The descriptor is not checked after the allocation.

- Addresses by version: 219: 0x0C02D4F8
- Called by: `ble_factory_test_init`
- Calls: `trace_printf`, `_close`, `ble_219_0c07097c`, `ble_219_0c071a94`
- Confidence: medium

## ble_uart_frame_enqueue

**Build a 5A A5 UART frame from a message struct and queue it on the outbound ring**

Takes a message struct whose byte 0 is the payload length, bytes 1 to 4 are the four header bytes, and whose pointer at +8 points to the payload. A length of 0xF8 or more returns -22 (0xFFFFFFEA) without queuing anything. Otherwise it writes 5A A5 LEN h1 h2 h3 h4 followed by the payload (copied with memcpy when the length and pointer are non-zero) into a 256-byte stack buffer, and queues LEN + 7 bytes with ble_msg_enqueue (ble_219_0c05ae14) as message class 2. No checksum is appended here, unlike uart_bridge_send_frame, and the enqueue result is returned.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | message struct: +0 payload length, +1 to +4 header bytes, +8 payload pointer |

**Returns** `s32`: enqueue result, or -22 when the length is 0xF8 or more

**Notes:** Callers include the reply paths of ble_219_0c02b264 and ble_219_0c02b1b4, and the message layout matches the one built in ble_219_0c02b264.

- Addresses by version: 219: 0x0C02C338
- Called by: `bts_op_cmd_handle`, `ble_process_autokey`, `bt_vcu_cmd_wr_process`, `ble_fmna_cmd_handler`, `ble_device_info_read_cmd`, `ble_token_chunk_rx_7e`
- Calls: `ble_msg_enqueue`, `memcpy`
- Confidence: high

## ble_uart_frame_route

**Offer one received UART frame to the 0x7E, b1b4 and a8f8 handlers in turn**

Entry point with no direct callers that takes one decoded UART frame in the layout used by ble_uart_frame_enqueue: length at +0, address bytes at +1 and +2, command at +3, index at +4, and the payload pointer at +8. It first offers the frame to ble_token_chunk_rx_7e (ble_219_0c02b264) in reply mode 1. If that handler does not return 1, it calls ble_219_0c02b1b4 and then ble_219_0c02a8f8, both in reply mode 1, without checking their results.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | decoded UART frame: +0 length, +1 and +2 address bytes, +3 command, +4 index, +8 payload pointer |

**Notes:** Frame layout inferred from ble_219_0c02c338 and from the argument order of the callees. The caller of this entry is not in the packet; it is probably a UART receive callback.

- Addresses by version: 219: 0x0C02B42C
- Calls: `ble_fmna_cmd_handler`, `ble_device_info_read_cmd`, `ble_token_chunk_rx_7e`
- Confidence: high

## ble_uart_inject_cmd1

**Log a UART frame and re-dispatch it to ble_219_0c02a8f8 as command 1**

Logs the frame bytes through ble_219_0c035d0c and then calls ble_219_0c02a8f8 with the first (mode) argument taken from frame byte 1, the class from frame byte 3, the command forced to 1, the index from byte 6, and the length and payload from byte 2 and the pointer at +8. It is a thin wrapper with no direct callers in the packet, so it is probably entered from a command table.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | UART frame in the layout of ble_uart_frame_route |

**Notes:** Purpose is unclear. The format string at 0x0C07F200 is not decoded, and the table that registers this entry is not in the packet.

- Addresses by version: 219: 0x0C02D128
- Calls: `ble_fmna_cmd_handler`, `trace_printf`
- Confidence: medium

## ble_uart_inject_cmd2

**Log a UART frame and re-dispatch it to ble_219_0c02a8f8 as command 2**

Logs the frame bytes through ble_219_0c035d0c and then calls ble_219_0c02a8f8 with the first (mode) argument taken from frame byte 1, the class from frame byte 3, the command forced to 2, the index from byte 6, and the length and payload from byte 2 and the pointer at +8. It is a thin wrapper with no direct callers in the packet, so it is probably entered from a command table.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | UART frame in the layout of ble_uart_frame_route |

**Notes:** Sibling of ble_uart_inject_cmd1 that forces command 2. The format string at 0x0C07F250 is not decoded.

- Addresses by version: 219: 0x0C02D16C
- Calls: `ble_fmna_cmd_handler`, `trace_printf`
- Confidence: medium

## ble_uart_inject_cmd7e

**Log a UART frame and feed it to the 0x7E token chunk handler with the command forced to 0x7E**

Logs the frame bytes through ble_219_0c035d0c and then calls ble_219_0c02b264 (ble_token_chunk_rx_7e) with reply mode from frame byte 1, the class from frame byte 3, the command forced to 0x7E, the index from byte 6, and the length and payload from byte 2 and the pointer at +8. The return value is discarded. It is a thin wrapper with no direct callers in the packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | UART frame in the layout of ble_uart_frame_route |

**Notes:** The format string at 0x0C07F2A0 is not decoded. The forced command makes any frame behave as a 0x7E chunk, so this is probably a test or debug path.

- Addresses by version: 219: 0x0C02D1B0
- Calls: `ble_token_chunk_rx_7e`, `trace_printf`
- Confidence: medium

## ble_uart_irq17_handler

**UART IRQ17 handler: drain RX FIFO into the instance queue, run the registered callback**

Interrupt handler for a UART instance whose context is at DAT_2000F510. It reads the instance id from the context, takes the hardware block pointer from the table at 0x0C076844, and reads the status word at +0x40. When the receive status bits 0x50 are set and the instance has a receive queue, it drains the FIFO one byte at a time into that queue with xQueueGenericSendFromISR until bit 4 of the line-status word at +0x18 (FIFO empty) is set. It then signals the event group through ble_evt_read_bits when the queue is not empty, and calls the handler registered at 0x2000AA80 with (id, status). It pends PendSV through ICSR when a task was woken, and stores the last status at +0x44.

**Notes:** The branch structure is complex and partly inferred from the callee summaries. The decompile shows the same body in full for IRQ18 and IRQ26.

- Addresses by version: 219: 0x0C0467B8
- Vector: `IRQ17_Handler`
- Peripheral registers: `0xe000ed04` (W)
- Called by: `ble_uart_irq18_handler`, `ble_uart_irq26_handler`
- Calls: `hal_irq_get_handler_table`, `xQueueGenericSendFromISR`, `prvIsQueueEmpty`, `ble_evt_read_bits`
- Confidence: medium

## ble_uart_irq18_handler

**UART IRQ18 vector entry: same UART IRQ body with context at 0x2000F514**

Interrupt vector entry for IRQ18. The decompile shows the UART IRQ body in full, using the context pointer from DAT_2000F514 instead of DAT_2000F510. The call graph lists ble_219_0c0467b8 as the callee, so this is most likely a short stub that loads its context and branches into the shared body. The shared behaviour is described in ble_uart_irq17_handler.

**Notes:** The stub-to-shared-body reading is inferred from the call graph and the instruction count, not seen directly.

- Addresses by version: 219: 0x0C0467C4
- Vector: `IRQ18_Handler`
- Calls: `ble_uart_irq17_handler`
- Confidence: medium

## ble_uart_irq26_handler

**UART IRQ26 vector entry: same UART IRQ body with context at 0x2000F534**

Interrupt vector entry for IRQ26. The decompile shows the UART IRQ body in full, using the context pointer from DAT_2000F534. The call graph lists ble_219_0c0467b8 as the callee, so this is most likely a short stub that loads its context and branches into the shared body. The shared behaviour is described in ble_uart_irq17_handler.

**Notes:** The stub-to-shared-body reading is inferred from the call graph and the instruction count, not seen directly.

- Addresses by version: 219: 0x0C0467D0
- Vector: `IRQ26_Handler`
- Calls: `ble_uart_irq17_handler`
- Confidence: medium

## ble_uart_port_start

**Start UART port 0..2: 115200-baud config, IRQ handler install and RX interrupt enable**

Starts the UART port whose index is the u16 that param_1+0x10 points to; indexes 3 and above return -19 (-ENODEV). It fills the 24-byte port record at 0x2000F414 + index*0x18 with the four-word line config {0x00030000, 0x00000201, 0x0001C200, 0} (0x1C200 is 115200 baud), stores 0x7C0 at +0x10 and the context pointer param_1 at +0x14, and clears two u16 counters at +4 and +6 of the port descriptor. The config goes to FUN_0C034008, the port's IRQ number is read from the table at 0x0C076850 and installed with hal_irq_install_handler (the context pointer is passed as the handler slot value), and the UART interrupt mask is then written through hal_uart_set_irq_mask. The decompiler does not recover the mask argument, so the value written is unknown.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | request struct; the pointer at +0x10 leads to the port descriptor, whose first u16 is the port index (0..2) |

**Returns** `s32`: 0, or -19 (-ENODEV) for a bad port index

**Notes:** The 115200 baud reading of 0x1C200 is an inference. FUN_0C034008 is not yet described.

- Addresses by version: 219: 0x0C046494
- Calls: `hal_uart_set_irq_mask`, `hal_uart_open`, `hal_irq_install_handler`
- Confidence: medium

## ble_uart_process_task

**UART1 receive task: reassemble 5A A5 and 55 AA frames and answer the D1x single-UART test**

Task body, created by ble_factory_test_init as 'uart_process_task', that never returns. It reads /dev/uart1 into a 288-byte ring at 0x20009890 (count at +0x122, capacity word 0x120 at +0x120) and scans for 5A A5 frames (7-byte fixed part) and 55 AA frames (6-byte fixed part). A frame is accepted only if its 16-bit checksum at the end, stored little-endian, equals the complement of the sum of the bytes from the length byte through the last payload byte; a candidate that fails the check advances the scan by one byte. An accepted frame is compared with the D1x self-test signature 01 3D 23 42 4F 01 that starts at the length byte; a match logs 'd1x single uart test successed' and writes the fixed 10-byte reply 5A A5 01 23 3D 43 4F 01 0B FF, and a mismatch logs 'd1x single uart test, cmd or index failed' and dumps the frame. Consumed bytes are removed by shifting the remainder to the front of the ring.

**Notes:** The task name comes from the string used by ble_factory_test_init. The 55 AA variant is inferred from the 6 instead of 7 fixed bytes. The read timeout of 100 ticks comes from the ioctl-style call in ble_uart1_open. The D1x name is taken from the log strings.

- Addresses by version: 219: 0x0C02D358
- Calls: `trace_printf`, `memcmp`, `memset`, `read`, `write`
- Confidence: medium

## ble_uart_rx_dma_commit

**Commit DMA-received bytes to the UART stream head from ISR and re-arm the receive pump**

Called from the receive-complete path for one UART channel with the byte count that landed. It finds the instance context through the 0x18-byte record at DAT_2000F428 (context at +0x10) and commits the count to the stream head with stream_buffer_commit_head in ISR mode, with no woken-task pointer. It then calls ble_uart_rx_dma_pump in ISR mode to keep the DMA armed.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | channel index selecting the record at 0x2000F428 |
| `param_2` | `u32` | number of bytes received |

- Addresses by version: 219: 0x0C046468
- Calls: `stream_buffer_commit_head`, `ble_uart_rx_dma_pump`
- Confidence: medium

## ble_uart_rx_dma_pump

**Keep one UART instance receive DMA running into its stream write side; signal readable**

Feeds one UART instance's DMA from the write side of its stream buffer. If the instance's record in the 0x18-byte table at 0x2000F420 is active (bit 0 set) and its stream at +0x68 exists, it takes the contiguous free span (ringbuf_contig_write_len). When the instance's DMA is idle (hal_uart_tx_dma_busy is 0), it starts a DMA of that span at the write pointer. When the record's status bit 2 is set and the stream is not empty, it signals the readable event bit with ble_evt_set_index_bit(id, 1) inside a critical section in task context, or calls ble_evt_read_bits(id, 1) in ISR context.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | UART instance context: u16 instance id at +0, stream pointer at +0x68 |
| `param_2` | `s32` | 0 for task context, non-zero for ISR context |

**Notes:** The DMA primitive called here is labelled hal_uart_tx_dma_start in the call graph, but its buffer is the receive-side write pointer. That suggests the labels of hal_uart_tx_dma_start and hal_uart_rx_dma_start are swapped; flagged for review. The even and odd event-bit selectors are read as write-ready and read-ready.

- Addresses by version: 219: 0x0C0462C4
- Called by: `ble_uart_rx_dma_commit`
- Calls: `hal_uart_tx_dma_start`, `hal_uart_tx_dma_busy`, `vPortEnterCritical`, `vPortExitCritical`, `ringbuf_is_empty`, `ringbuf_write_ptr`, `ringbuf_contig_write_len`, `ble_evt_set_index_bit`, `ble_evt_read_bits`
- Confidence: medium

## ble_uart_tx_dma_pump

**Keep one UART instance transmit DMA fed from the stream read side; signal writable**

Feeds one UART instance's DMA from the read side of its stream buffer. If the instance's record in the table at 0x2000F420 has bit 1 set and its stream exists, it takes the contiguous readable span (ringbuf_contig_read_len). When hal_uart_rx_dma_busy is 0, it starts a DMA from the read pointer with hal_uart_rx_dma_start. When the record's status bit 2 is set and the stream is not full with its reserve (ringbuf_is_full_with_reserve), it signals the writable event bit with ble_evt_set_index_bit(id, 0) in task context, inside a critical section, or calls ble_evt_read_bits(id, 0) in ISR context.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | UART instance context: u16 instance id at +0, stream pointer at +0x68 |
| `param_2` | `s32` | 0 for task context, non-zero for ISR context |

**Notes:** This is the transmit-side counterpart of ble_uart_rx_dma_pump. The DMA primitive it calls is labelled hal_uart_rx_dma_start, which is the label swap flagged in ble_uart_rx_dma_pump.

- Addresses by version: 219: 0x0C046380
- Calls: `hal_uart_rx_dma_start`, `hal_uart_rx_dma_busy`, `vPortEnterCritical`, `vPortExitCritical`, `ringbuf_is_full_with_reserve`, `ringbuf_read_ptr`, `ringbuf_contig_read_len`, `ble_evt_set_index_bit`, `ble_evt_read_bits`
- Confidence: medium

## bt_vcu_cmd_wr_process

**Process a VCU command read (cmd 1) and build the reply from the index using cached or default values**

Logs 'bt_vcu_cmd_wr_process' with src, dest, cmd and index. Frames with byte 2 equal to 9 and byte 3 equal to 1 are handled first: index 0x28 replies with the 16-byte ECU part number at 0x200092D8 (ble_app_block16_f36c_read) and length 0x14, and index 3 replies with 0xFFFF. For other command-1 frames it acts only when the RX state DAT_200092EC is 4, then chooses the reply by index: 0x10 reads 14 bytes from the app block (ble_app_block16_f3b8_read, length 0x15), 0x1A and 0x20 reply with two bytes 0x1810, 0x1B with two zero bytes, 0x1D with 0x1810, 0x67 with 0x0300 and 0xB2 with 0xFFFF, 0x1C, 0x22, 0x24, 0x25, 0x26 and 0x7B with one byte, 0x29 with 21 bytes, 0xF0 with the byte 0x01 and length 0x15, and every other index in range builds a 12-byte reply from a stack-local array. Each reply is sent with ble_219_0c02c338 as a record of length, dest, src, type 4, index and payload pointer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | received VCU frame: +1 src, +2 dest, +3 cmd, +4 index, +5 onward payload |

**Notes:** The reply defaults are constants in the decompile and their meaning is not established. The 12-byte default path uses a stack cache that is zero-initialised and filled from a few locals, so its output is mostly constant. Undescribed: ble_219_0c02c338 (the common reply sender).

- Addresses by version: 219: 0x0C02A484
- Called by: `ble_msg_route_by_key`
- Calls: `ble_uart_frame_enqueue`, `trace_printf`, `ble_app_block16_f36c_read`, `ble_app_block16_f3b8_read`, `memset`
- Confidence: medium

## uart_bridge_queue_init

**Create a 32-byte static queue and pass it with a fixed id to ble_219_0c0484b4**

Creates a static queue of 32 one-byte items with ble_219_0c042ba0, using the storage at 0x20005478 and the queue structure at 0x20005428, then passes the handle with the global at 0x2000B520 and the constant 0x11 to ble_219_0c0484b4 and returns that call's result. The packet names ble_219_0c0484b4 _close, but this call passes three arguments, so that name is doubtful. The most likely role is a receive or event queue for the UART bridge, which is not verified. It has no direct callers.

**Returns** `s32`: result of ble_219_0c0484b4

**Notes:** ble_219_0c0484b4 is named _close in earlier waves. The constant 0x11 and the global at 0x2000B520 are not identified; the owner of that callee's entry should review it.

- Addresses by version: 219: 0x0C0355C8
- Calls: `prvInitialiseNewQueue`, `xStreamBufferGenericCreateStatic`, `_close`
- Confidence: low

## uart_bridge_send_frame

**Build a 5A A5 UART frame with four header bytes, optional payload and checksum, then send it**

Builds the frame in a 256-byte stack buffer: bytes 0 and 1 are 5A A5, byte 2 is the length param_1, bytes 3 to 6 are the four header bytes param_2 to param_5 and, for a non-zero length, the payload is copied from param_6 to offset 7. The checksum is the 16-bit ones-complement of the sum of bytes 2 through length+6, stored little-endian after the payload, which makes the frame length+9 bytes long. The frame is written to channel 0 through ble_219_0c02e758 (uart_bridge_write_channel0). A length of 0xFFFB wraps the checksum offset, and the function then sends a 4-byte frame 5A A5 FF FF; a length above 247 overruns the 256-byte buffer because nothing checks length+9 against it.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | payload length in bytes |
| `param_2` | `u8` | header byte 1, stored at frame offset 3 |
| `param_3` | `u8` | header byte 2, stored at frame offset 4 |
| `param_4` | `u8` | header byte 3, stored at frame offset 5 |
| `param_5` | `u8` | header byte 4, stored at frame offset 6 |
| `param_6` | `ptr` | payload source |

**Notes:** The mapping of the four header bytes onto src, dest, cmd and index is inferred from the brief and not confirmed by a sender. The overrun for lengths above 247 is a real bound issue in this code.

- Addresses by version: 219: 0x0C02C124
- Called by: `btapp_btle_connect_status_change`, `ble_speed_limit_code_check`, `ble_link_status_notify_tick`, `ble_app_poll_tick`, `ble_findmy_ring_status_notify`, `ble_unlock_auth_cb`, `bts_op_cmd_handle`, `ble_vcu_wakeup_retry`, `ble_fmna_cmd_handler`, `ble_device_info_read_cmd`, `ble_token_chunk_rx_7e`, `ble_vcu_cmd_handle`
- Calls: `uart_bridge_write_channel0`, `memset`
- Confidence: high

## uart_bridge_write_channel0

**Write a buffer to the UART2 fd for channel 0 under the channel mutex and report errors**

Does nothing unless param_1 is 0, the buffer is non-null and the length is non-zero, and returns 0 in those cases. It gets the dispatcher context from uart_disp_get_channel_ctx and returns -5 when that is missing or the file descriptor in DAT_20009D10 is not positive. It takes the mutex at context+8 with a 100-tick timeout (ble_219_0c0430a8) and returns -16 if it is not obtained; otherwise it calls newlib write for the full length, releases the mutex, and returns -16 when fewer bytes were written.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | channel index; only 0 is handled |
| `param_2` | `ptr` | data buffer |
| `param_3` | `s32` | byte count |

**Returns** `s32`: 0 when done or ignored; -5 no context or bad fd; -16 lock timeout or short write

**Notes:** The descriptor is presumably the /dev/uart2 fd returned by uart_disp_get_channel_fd in earlier waves, which is not verified in this packet.

- Addresses by version: 219: 0x0C02E758
- Called by: `uart_bridge_send_frame`
- Calls: `uart_disp_get_channel_ctx`, `xQueueGenericSend`, `xQueueSemaphoreTake`, `write`
- Confidence: high

## uart_disp_get_channel_ctx

**Return the UART dispatcher context for channel 0, else NULL**

Returns &DAT_20003db8 when param_1 == 0 and NULL for any other value; the dispatcher has only a single channel. Called from the 'Uart dispatcher: start service' routine (0x0c02e420) and three sibling routines in the same module, which pass the returned block (+8) to a registration call. The structure layout is not visible in this function.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | channel index; only 0 is valid |

**Returns** `ptr`: pointer to the channel-0 context at 0x20003db8 or NULL

**Notes:** Context struct contents unknown; role inferred from the callers' strings ('Uart dispatcher', '/dev/uart2').

- Addresses by version: 219: 0x0C028790
- Called by: `uart_disp_start_service`, `uart_disp_send_frame`, `uart_bridge_write_channel0`, `uart_disp_rx_process`
- Confidence: medium

## uart_disp_get_channel_fd

**Return the /dev/uart2 file descriptor for channel 0, else -1**

Returns -1 if param_1 != 0. Otherwise returns DAT_20009d10 (the descriptor stored by the UART dispatcher start routine 0x0c02e420 after opening '/dev/uart2'), or -1 if that value is not positive (port never opened). No direct callers; it is used as a callback/ops-table entry.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | channel index; only 0 is valid |

**Returns** `s32`: file descriptor (>0) or -1

**Notes:** Used via function pointer, so the exact consumer is unknown.

- Addresses by version: 219: 0x0C02E57C
- Confidence: medium

## uart_disp_rx_process

**Parse 55 AA and 5A A5 frames from the UART RX ring and dispatch them to handlers**

Called with 0 from the RX task. It reads pending UART bytes into the channel RX ring (buffer at context+0x58, capacity at +0x5C, fill at +0x5E) and, when the RX idle timer DAT_20009D3D is armed, marks state DAT_20009D3C = 2 and sets the deadline DAT_20009D34. It scans for frame starts 0x55 0xAA (type 'e', header 6 bytes) and 0x5A 0xA5 (type 'f', header 7 bytes); a frame is taken only when all of it is in the ring and its checksum matches, otherwise one byte is skipped and the resync counter DAT_20009D24 is incremented. A good frame is passed as a header record {type, length, src, dest, cmd} plus the raw frame and length: to the override handler DAT_20009D14 if set; otherwise, for keys 0xFC01, 0xFC04, 0xFD02, 0xFD05 and 0xFE03, to handler DAT_20009D44; otherwise to every entry of the 8-byte table at 0x0C073ED0 whose 3-byte (src, dest, cmd) key matches, and every masked entry of the 12-byte table at 0x0C073EFC. Frames with no handler print the 'not find chn' trace. Consumed bytes are removed by shifting the ring and fill is updated. Returns the argument when it is non-zero.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | 0 starts a processing pass; a non-zero value is returned unchanged |

**Returns** `s32`: param_1 when non-zero, otherwise 0

**Notes:** Handler table entry layouts are inferred from the pointer arithmetic. For 55 AA frames there is no src byte, so src is 0. Calls to the stub at 0x0C0360CC (stub_return_zero_0c0360cc) are no-ops. The idle-timeout interaction is medium confidence.

- Addresses by version: 219: 0x0C02E7D8
- Called by: `uart_disp_rx_task`
- Calls: `uart_disp_get_channel_ctx`, `trace_printf`, `stub_return_zero_0c0360cc`, `xTaskGetTickCount`, `read`
- Confidence: medium

## uart_disp_rx_task

**Body of the 'nb uart disp' task: wait for UART data with select and run the RX parser**

Registers the task with the watchdog monitor (wdt_task_monitor_register_current) and then loops forever. Each pass rebuilds a read set from the single-entry fd list at 0x20009D10, calls hal_wdt_task_checkin and waits in ble_fd_select (on the BLE event group) for readable data. If the RX idle timer is armed and its deadline DAT_20009D34 has passed, it sets DAT_20009D3C = 1, calls the idle callback DAT_20009D38(0) when registered and re-arms the deadline from DAT_20009D30 (ms). When the channel fd is readable it calls uart_disp_rx_process(0). The task never returns.

**Notes:** The select timeout block is zero as decompiled (local_40+2); the value 50000 written at local_40[4] is not read by that call, so the wait length is up to ble_fd_select. Medium confidence on that point.

- Addresses by version: 219: 0x0C02EB60
- Calls: `uart_disp_rx_process`, `trace_printf`, `hal_wdt_task_checkin`, `wdt_task_monitor_register_current`, `vTaskDelete`, `xTaskGetTickCount`, `ble_fd_select`
- Confidence: medium

## uart_disp_send_frame

**Build a 55 AA or 5A A5 dispatcher frame from a request record and write it to the UART**

param_1 is a request record: byte 0 is the frame type ('e' selects the 55 AA frame, any other value the 5A A5 frame; 'd' is rejected), byte 1 the channel (must be 0), byte 2 the payload length and bytes 3..6 header bytes; the payload pointer is at +8. A 55 AA frame is 55 AA len h0 h1 h2 payload csum_lo csum_hi (len+8 bytes) and carries request bytes 4..6 as header; a 5A A5 frame is 5A A5 len h0..h3 payload csum (len+9 bytes). The 16-bit checksum is the ones complement of the byte sum from the length byte through the last payload byte, stored low byte first. The frame is built in the channel TX buffer (capacity at context+4), the context mutex (context+8) is taken with a 100-tick timeout, the frame is written to fd DAT_20009D10 and a short write returns -16. The channel-0 TX counter at 0x20009D2C (stride 0x18) is incremented and the mutex released with xQueueGenericSend.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | request record: +0 frame type char, +1 channel (0 only), +2 payload length, +3..+6 header bytes, +8 payload pointer |

**Returns** `s32`: 0 on success; -5 for an unknown frame type, no channel context or no fd; -16 on lock timeout or short write; 0 silently for a non-zero channel or a frame that does not fit the TX buffer

**Notes:** The silent return 0 cases (non-zero channel, TX buffer too small) cannot be told apart by the caller. The 'e' (55 AA) and other (5A A5) frame types match the receive side in ble_219_0c02e7d8, which names 55 AA 'e' and 5A A5 'f'.

- Addresses by version: 219: 0x0C02E5A4
- Called by: `ble_msg_route_by_key`, `ble_factory_test_dispatch_set`, `ble_factory_test_dispatch_query`
- Calls: `uart_disp_get_channel_ctx`, `trace_printf`, `xQueueGenericSend`, `xQueueSemaphoreTake`, `memcpy`, `write`
- Confidence: high

## uart_disp_start_service

**Start the UART dispatcher: open /dev/uart2, register stream buffers and spawn its RX task**

Creates the dispatcher's plain mutex (prvInitialiseMutex type 1) at channel context+8 when the context exists. It opens /dev/uart2 with flags 0x4006 and configures it through the fd control entry: ioctl 0x100 with 0x1C200 (115200 baud), two 0x120-byte stream buffers (xStreamBufferGenericCreateStatic, trigger level 1) passed with ioctl 0x1D and 0x1E, then ioctl 0x1C and 0x19. The fd is stored in DAT_20009D10, the single channel fd used by the rest of the dispatcher. The RX task 'nb uart disp' is created with xTaskCreateStatic at entry 0x0C02EB61 (Thumb address of ble_219_0c02eb60), 0x200 words of stack at 0x20009D48, TCB at 0x20004A78 and priority 4; it is created even if the open failed.

**Returns** `u32`: always 0

**Notes:** The meaning of ioctl commands 0x19, 0x1C, 0x1D and 0x1E and of the stream buffers is inferred from argument shapes. When the open fails DAT_20009D10 stays -1 and the RX loop has no fd to wait on.

- Addresses by version: 219: 0x0C02E420
- Calls: `uart_disp_get_channel_ctx`, `trace_printf`, `prvInitialiseNewQueue`, `prvInitialiseMutex`, `xStreamBufferGenericCreateStatic`, `xTaskCreateStatic`, `_close`, `ble_219_0c071a94`
- Confidence: medium
