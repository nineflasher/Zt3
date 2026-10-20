# BLE - `factory_test` functions

22 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`app_testmode_bt_nonsig_tx`](#app_testmode_bt_nonsig_tx) | 0x0C0469A0 | Test mode: start Bluetooth non-signalling TX from a 10-byte command payload |
| [`ble_factory_test_dispatch_query`](#ble_factory_test_dispatch_query) | 0x0C02CCA8 | Factory-test query commands: read identity, RSSI, stage tag and magic values back to the tool |
| [`ble_factory_test_dispatch_set`](#ble_factory_test_dispatch_set) | 0x0C02C49C | Factory-test set and action commands: enter test mode, RF and HCI tests, VCO, GPIO and writes |
| [`ble_factory_test_init`](#ble_factory_test_init) | 0x0C02D554 | Start the factory-test subsystem: configure channels 0 and 1, open UART1 and create its tasks |
| [`ble_hci_le_enh_rx_test_cmd`](#ble_hci_le_enh_rx_test_cmd) | 0x0C046BFC | Send HCI LE Enhanced Receiver Test (0x2033) with three parameter bytes |
| [`ble_hci_le_enh_tx_test_cmd`](#ble_hci_le_enh_tx_test_cmd) | 0x0C046BBC | Send HCI LE Enhanced Transmitter Test (0x2034) with four parameter bytes |
| [`ble_hci_le_rx_test_cmd`](#ble_hci_le_rx_test_cmd) | 0x0C046B90 | Send HCI LE Receiver Test (0x201D) with one RX channel byte |
| [`ble_hci_le_test_end_cmd`](#ble_hci_le_test_end_cmd) | 0x0C046C34 | Send HCI LE Test End (0x201F), which has no parameters |
| [`ble_hci_le_tx_test_cmd`](#ble_hci_le_tx_test_cmd) | 0x0C046B4C | Send HCI LE Transmitter Test (0x201E) with channel, length and payload type |
| [`ble_nonsig_ble_count_read`](#ble_nonsig_ble_count_read) | 0x0C046C50 | Read the BLE non-signalling test packet counter and reset it when non-zero |
| [`ble_nonsig_bt_result_read`](#ble_nonsig_bt_result_read) | 0x0C046B18 | Read the BT non-signalling test counters into a 3-halfword output and reset them |
| [`ble_rate_test_cmd04_forward`](#ble_rate_test_cmd04_forward) | 0x0C029D8C | Re-frame a rate-test FE 04 frame (six payload bytes) and queue it with ble_msg_enqueue |
| [`ble_recv_rate_test_report`](#ble_recv_rate_test_report) | 0x0C028BF0 | Send the receive-rate test report frame with the RX count and byte total, then reset them |
| [`ble_recv_rate_test_start`](#ble_recv_rate_test_start) | 0x0C029C18 | Parse a rate-test start frame (FE 00), send an acknowledgement and reset the RX counters |
| [`ble_vendor_fc87_send_keyed`](#ble_vendor_fc87_send_keyed) | 0x0C046A58 | Send vendor HCI 0xFC87 for the table record whose key matches request byte 7 |
| [`ble_vendor_fc87_send_test_pattern`](#ble_vendor_fc87_send_test_pattern) | 0x0C046AF0 | Send the fixed vendor HCI 0xFC87 test frame with a 0x55 address field |
| [`bt_drv_ctrl_bringup_rf_test`](#bt_drv_ctrl_bringup_rf_test) | 0x0C046C7C | BT controller bring-up for RF non-signalling test, then three fixed HCI packets |
| [`bt_drv_vco_test_session_start`](#bt_drv_vco_test_session_start) | 0x0C03BD90 | Start a factory VCO test session on one channel, saving and overriding two analog registers |
| [`bt_drv_vco_test_session_stop`](#bt_drv_vco_test_session_stop) | 0x0C03BE14 | End the factory VCO test session and restore the saved analog registers |
| [`bt_drv_vco_test_start`](#bt_drv_vco_test_start) | 0x0C03DFAC | Start the BT VCO/synthesiser test on a channel: 0xD0220C00 = (channel & 0x7F) \| 0xA0000, then delay |
| [`bt_drv_vco_test_stop`](#bt_drv_vco_test_stop) | 0x0C03DFF4 | Stop the BT VCO test: write 0 to RF channel register 0xD0220C00, then delay |
| [`rf_test_hci_cmd_complete_handler`](#rf_test_hci_cmd_complete_handler) | 0x0C0468B4 | Capture return parameters of RF-test HCI Command Complete events into globals |

## app_testmode_bt_nonsig_tx

**Test mode: start Bluetooth non-signalling TX from a 10-byte command payload**

Test-mode command for Bluetooth non-signalling transmit. It logs its own name, runs bt_drv_hci_cmd_post_settle, and builds a 0x20-byte vendor command from a template with constants 0x1CFC8701, 0x0003E800, 0x55555555, 0x00015555 and 0x001B0404. The payload fills in a 16-bit value from bytes 0 and 1, copies the 6-byte address at payload+2 with ble_mem_copy, and sets fields from payload byte 9. Payload byte 8 is matched against the first byte of 27 six-byte records at 0x20003EF0. On a match it fills the template from that record, sends it with bt_drv_hci_cmd_send_wait, and returns 0; without a match it returns 0xFFFFFFFF. A failed copy is logged with line 185.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | command payload: bytes 0 and 1 are a 16-bit field, 2 to 7 the 6-byte address, 8 the record key, 9 a second value |

**Returns** `u32`: 0 when the key matches a record, otherwise 0xFFFFFFFF

**Notes:** The payload field meanings and the record layout are inferred from the decompile and are low confidence. The function name is taken from the string it logs.

- Addresses by version: 219: 0x0C0469A0
- Called by: `ble_factory_test_dispatch_set`
- Calls: `trace_printf`, `ble_mem_copy`, `bt_drv_hci_cmd_send_wait`, `bt_drv_hci_cmd_post_settle`
- Confidence: medium

## ble_factory_test_dispatch_query

**Factory-test query commands: read identity, RSSI, stage tag and magic values back to the tool**

Read-side counterpart of ble_factory_test_dispatch_set, with the same factory-mode gate; replies are 0x66-tagged messages sent with ble_219_0c02e5a4, and the reply type is usually taken from the request payload. Opcode 0x00 copies up to 16 bytes from 0x2000F36C (ble_app_block16_f36c_read, length from payload byte 0), 0x10 returns the 6-byte identity at 0x2000F364 (ble_app_addr6_read), 0x22 returns the 32-bit word at 0x2000F360, 0x33 reads a 40-byte block, and 0x52 and 0xAA check the marker byte at 0x2000F36B and the CAF magic at 0x2000F3B4 (ble_app_marker_o_check, ble_app_magic_caf_check). Opcode 0x58 with 13 bytes copies the ADV_ID block (app_adv_id_block_copy), 0x61 returns a refreshed 6-byte random address (ble_random_addr_advance), 0x26 always answers the constant 0x219, 0x2C returns the u16 at 0x20009898, and 0x4B compares that value with 150 and 450 and replies with the 4-byte tag 'DVT1' (below 150), 'PVT1' (150 to 449) or 'ERR1' when the request byte is 4. Opcode 0x2B samples the RSSI of the connection at DAT_20004338 seven times through bt_drv_reg_op_read_acl_rssi, and 0x57 returns 1 when ble_ram_call_2000110c_arg0 gives at most 0x200000 and 2 otherwise. Opcodes not listed log 'index error' and send nothing.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | factory query frame: +2 payload length, +3 and +4 header bytes, +6 opcode, +8 payload pointer |

**Notes:** Several reads go through ble_app_* callees named by earlier waves (gated by request 0x101). The value of DAT_20009898 and the meaning of the 0x2B sampling (the reply is the byte at DAT_20004330 after sampling) are not confirmed. Opcodes 0x1A, 0x1F and 0x54 call ble_219_0c046b18 and ble_219_0c046c50, which are not described yet.

- Addresses by version: 219: 0x0C02CCA8
- Calls: `app_adv_id_block_copy`, `uart_disp_send_frame`, `trace_printf`, `bt_drv_reg_op_read_acl_rssi`, `app_magic_flag_is_set`, `app_get_unique_id16`, `ble_ram_call_2000110c_arg0`, `ble_app_block16_f36c_read`, `ble_app_addr6_read`, `ble_app_word_f360_read`, `ble_app_block40_f38c_read`, `ble_app_marker_s_check`, `ble_app_marker_o_check`, `ble_app_magic_caf_check`, `ble_nonsig_bt_result_read`, `ble_nonsig_ble_count_read` ...
- Confidence: medium

## ble_factory_test_dispatch_set

**Factory-test set and action commands: enter test mode, RF and HCI tests, VCO, GPIO and writes**

Factory-test command dispatcher, active only while the factory magic is armed (ble_219_0c041d10, app_magic_flag_is_set), and it can enter that mode with opcode 0xEF and payload 1 (app_magic_flag_set(1), reply, 100-tick delay, then ble_219_0c041d28(0)); 0xEF while already armed replies 'duplicate factory test mode'. Writes: opcode 0x00 (14 or 16 bytes, ble_219_0c045d8c) and 0x10 (6 bytes, ble_219_0c045ddc) store identity blocks, 0x58 with 13 bytes calls ble_payload_copy_and_schedule, and 0x29 stores a 6-byte address at 0x20009884 and calls ble_219_0c06b498, while 0x2A logs a 6-byte value and calls ble_219_0c06b8bc with the handle DAT_20004338. RF tests: 0x1E, 0x1F and 0x20 call ble_hci_le_tx_test_cmd (channel below 40, payload type below 8), ble_hci_le_rx_test_cmd and ble_hci_le_test_end_cmd; 0x53 and 0x54 start the BLE TX and RX v2 tests; 0x55 and 0x56 start and stop the VCO test through bt_drv_vco_test_session_start and bt_drv_vco_test_session_stop; 0x23 applies a u16 through bt_drv_rf_2168_field9_set; 0x16 and 0x1A check their bytes against limits and call ble_219_0c0469a0 and ble_vendor_fc87_send_keyed. Opcode 0x50 sets two GPIO bits through ioctl-style calls on DAT_2000988C (requests 0x1010000 and 0x1010001), waits 20 ticks and reads them back, logging 'set PORT_GPIO(0, 0) failed' on mismatch; 0x59 replies, waits 200 ticks and sets the BT100 UART baud rate from a u32 payload through DAT_20009894. Results are sent as 0x66-tagged messages through ble_219_0c02e5a4 with a status byte, unknown opcodes log 'index error' and reply status 0, and opcode 0x25 exits without a reply.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | factory frame: +2 payload length, +3 and +4 header bytes, +6 opcode, +8 payload pointer |

**Notes:** Several callees (ble_219_0c045d8c, ble_219_0c045ddc, ble_219_0c0469a0, ble_219_0c046c50, ble_219_0c06b498) are not described yet. DAT_2000988C is read here, but ble_gpio_dev_open writes DAT_2000989C, so the link between them is unconfirmed. The name _close given to ble_219_0c0484b4 by an earlier wave does not fit its ioctl-style use in this function (requests 0x1010000, 0x100, 0x110). Opcode 0x2A does not set the reply status, so the status it sends is whatever was left in the local.

- Addresses by version: 219: 0x0C02C49C
- Calls: `ble_payload_copy_and_schedule`, `uart_disp_send_frame`, `trace_printf`, `bt_drv_vco_test_session_start`, `bt_drv_vco_test_session_stop`, `bt_drv_rf_2168_field9_set`, `app_magic_flag_set`, `app_magic_flag_is_set`, `ble_boot_mode_set`, `vTaskDelay`, `ble_cfg_set_f36c_bytes`, `ble_cfg_set_bd_addr_checked`, `ble_cfg_set_block40`, `ble_cfg_set_word_f360`, `ble_cfg_set_flag_f36a`, `ble_cfg_set_flag_f36b` ...
- Confidence: medium

## ble_factory_test_init

**Start the factory-test subsystem: configure channels 0 and 1, open UART1 and create its tasks**

Sets peripheral channels 0 and 1 with the 16-bit value 0x0081 through ble_219_0c0456c0. It creates the 'factory_test_task' (stack depth 0x400, priority 2) and 'adc process' (stack depth 0x200, priority 2) tasks with ble_219_0c043d3c (xTaskCreate), calls ble_uart1_open, then creates 'uart_process_task' (stack depth 0x200, priority 1) running ble_uart_process_task, and logs 'factory test init done'.

**Notes:** The task bodies at 0x0C02D1F4 and 0x0C02D224 are not in this packet. The 0x0081 value and the meaning of channels 0 and 1 are not identified. The caller is not visible.

- Addresses by version: 219: 0x0C02D554
- Calls: `ble_uart1_open`, `trace_printf`, `xTaskCreate`, `ble_pin_config_record_apply`
- Confidence: high

## ble_hci_le_enh_rx_test_cmd

**Send HCI LE Enhanced Receiver Test (0x2033) with three parameter bytes**

Sends the 7-byte HCI command 01 33 20 03 p0 p1 p2, which is LE Enhanced Receiver Test (opcode 0x2033): RX_Channel, PHY and Modulation_Index, from the 3-byte request. It runs FUN_0C03BD70 first, then FUN_0C03AC98, and always returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 3 parameter bytes: channel, PHY, modulation index |

**Returns** `s32`: always 0

- Addresses by version: 219: 0x0C046BFC
- Called by: `ble_factory_test_dispatch_set`
- Calls: `bt_drv_hci_cmd_send_wait`, `bt_drv_hci_cmd_post_settle`
- Confidence: high

## ble_hci_le_enh_tx_test_cmd

**Send HCI LE Enhanced Transmitter Test (0x2034) with four parameter bytes**

Sends the 8-byte HCI command 01 34 20 04 followed by the four bytes at param_1, which is LE Enhanced Transmitter Test (opcode 0x2034): TX_Channel, Test_Data_Length, Packet_Payload and PHY, in that order. It runs FUN_0C03BD70 first, then FUN_0C03AC98, and always returns 0. The fourth parameter (PHY) is what distinguishes it from ble_hci_le_tx_test_cmd.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 4 parameter bytes: channel, length, payload, PHY |

**Returns** `s32`: always 0

- Addresses by version: 219: 0x0C046BBC
- Called by: `ble_factory_test_dispatch_set`
- Calls: `bt_drv_hci_cmd_send_wait`, `bt_drv_hci_cmd_post_settle`
- Confidence: high

## ble_hci_le_rx_test_cmd

**Send HCI LE Receiver Test (0x201D) with one RX channel byte**

Sends the 5-byte HCI command 01 1D 20 01 p0, which is LE Receiver Test (opcode 0x201D) with RX_Channel = p0 taken from the 1-byte request. It runs FUN_0C03BD70 first, then FUN_0C03AC98 with length 5, and always returns 0. It is the receive-side counterpart of ble_hci_le_tx_test_cmd.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 1-byte RX channel |

**Returns** `s32`: always 0

- Addresses by version: 219: 0x0C046B90
- Called by: `ble_factory_test_dispatch_set`
- Calls: `bt_drv_hci_cmd_send_wait`, `bt_drv_hci_cmd_post_settle`
- Confidence: high

## ble_hci_le_test_end_cmd

**Send HCI LE Test End (0x201F), which has no parameters**

Sends the 4-byte HCI command 01 1F 20 00, which is LE Test End (opcode 0x201F), through FUN_0C03AC98, and returns 0. Unlike the other test-command senders it does not call FUN_0C03BD70 first. The controller's reply, which carries the received-packet count in the Bluetooth spec, is handled elsewhere.

**Returns** `s32`: always 0

- Addresses by version: 219: 0x0C046C34
- Called by: `ble_factory_test_dispatch_set`
- Calls: `bt_drv_hci_cmd_send_wait`
- Confidence: high

## ble_hci_le_tx_test_cmd

**Send HCI LE Transmitter Test (0x201E) with channel, length and payload type**

Sends the 7-byte HCI command 01 1E 20 03 p0 p1 p2, which is LE Transmitter Test (opcode 0x201E, three parameters): TX_Channel = p0, Length_of_Test_Data = p1 and Packet_Payload = p2, all taken from the 3-byte request in param_1. It runs FUN_0C03BD70 first and clears the test-state word at 0x2000F464 when it is non-zero, then hands the frame to FUN_0C03AC98. It always returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 3-byte request: channel, data length, payload type |

**Returns** `s32`: always 0

**Notes:** The opcode mapping follows the Bluetooth Core LE Test command set. FUN_0C03AC98 (the HCI send) and FUN_0C03BD70 are not yet described.

- Addresses by version: 219: 0x0C046B4C
- Called by: `ble_factory_test_dispatch_set`
- Calls: `bt_drv_hci_cmd_send_wait`, `bt_drv_hci_cmd_post_settle`
- Confidence: high

## ble_nonsig_ble_count_read

**Read the BLE non-signalling test packet counter and reset it when non-zero**

Copies the 16-bit BLE test packet counter at DAT_2000F464 into *param_1, logs 'final ble test cnt:%d', and clears the counter when it is non-zero (read-and-clear). It returns 0, or 0xFFFFFFFF when param_1 is NULL. It is the BLE-side companion of ble_nonsig_bt_result_read.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output for the 16-bit counter |

**Returns** `u32`: 0, or 0xFFFFFFFF for a NULL output

**Notes:** The log call's argument is not visible in the decompile, so the printed value is taken from the output.

- Addresses by version: 219: 0x0C046C50
- Called by: `ble_factory_test_dispatch_query`
- Calls: `trace_printf`
- Confidence: medium

## ble_nonsig_bt_result_read

**Read the BT non-signalling test counters into a 3-halfword output and reset them**

Copies the BT non-signalling test counters into a 3-halfword output: count at DAT_2000F468, head at DAT_2000F46A, and payload length at DAT_2000F46C. It logs 'final bt test result cnt:%d head:%d payload:%d'. When the count is non-zero it clears the count and head word and the payload word (read-and-clear). It returns 0, or 0xFFFFFFFF when the output pointer is NULL.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output: three u16 values (count, head, payload) |

**Returns** `u32`: 0, or 0xFFFFFFFF for a NULL output

**Notes:** The log call's arguments are not visible in the decompile, so the printed values are taken from the output layout.

- Addresses by version: 219: 0x0C046B18
- Called by: `ble_factory_test_dispatch_query`
- Calls: `trace_printf`
- Confidence: medium

## ble_rate_test_cmd04_forward

**Re-frame a rate-test FE 04 frame (six payload bytes) and queue it with ble_msg_enqueue**

Accepts frames with 0xFE at byte 5 and 0x04 at byte 6. It copies payload bytes 7 to 12 and builds a 13-byte frame 5A A5 06 src dst FE 04 followed by those six bytes, with src and dst taken from bytes 4 and 3 of the input (swapped). The frame is queued with ble_msg_enqueue as type 3 and length 0xD, and the function returns 1. Frames that do not match return 0 so the caller can try the next sub-command parser.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | received frame |

**Returns** `u32`: 1 when the frame was an FE 04 frame and was queued, 0 otherwise

**Notes:** The meaning of the six payload bytes is not established.

- Addresses by version: 219: 0x0C029D8C
- Called by: `ble_rx_data_handler`
- Calls: `ble_msg_enqueue`
- Confidence: high

## ble_recv_rate_test_report

**Send the receive-rate test report frame with the RX count and byte total, then reset them**

Builds a 19-byte frame: 5A A5 0A, the source and destination bytes of the incoming frame (swapped), 0xFE 0x03, the 32-bit rx_total_count from 0x20008F5C and rx_bytes from 0x20008F60 (little-endian), and four zero bytes. It queues the frame with ble_msg_enqueue as type 3 and length 0x13, logs 'recv rate test finisged', and clears the statistics block 0x20008F50 to 0x20008F60 used by the rate-test receiver. It is called from ble_rx_data_handler when a 0xFE 0x03 frame arrives.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | received frame, bytes 3 and 4 give the addresses to echo |

**Notes:** The counters are incremented by app_ble_cmd_fe_rx_stats_update (FE 02 frames) and by ble_recv_rate_test_start.

- Addresses by version: 219: 0x0C028BF0
- Called by: `ble_rx_data_handler`
- Calls: `trace_printf`, `ble_msg_enqueue`
- Confidence: high

## ble_recv_rate_test_start

**Parse a rate-test start frame (FE 00), send an acknowledgement and reset the RX counters**

Accepts a frame that starts 5A A5, has 0xFE at byte 5 and 0x00 at byte 6; other frames return 0. The 16-bit response count from bytes 7 and 8 is stored in *param_2, and the function logs 'start recv : got resp count[%d]'. It queues an 8-byte acknowledgement 5A A5 01 src dst FE 00 01 through ble_msg_enqueue as type 3, clears the receive statistics 0x20008F50 to 0x20008F60, and returns 1. The caller then sets DAT_20008F50 to 1 to mark the test as running.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | received frame |
| `param_2` | `ptr:u16` | output: expected response count |

**Returns** `u32`: 1 when the frame was a start frame, 0 otherwise

**Notes:** Source and destination bytes in the acknowledgement are taken from bytes 4 and 3 of the input, swapped.

- Addresses by version: 219: 0x0C029C18
- Called by: `ble_rx_data_handler`
- Calls: `trace_printf`, `ble_msg_enqueue`
- Confidence: high

## ble_vendor_fc87_send_keyed

**Send vendor HCI 0xFC87 for the table record whose key matches request byte 7**

Runs FUN_0C03BD70 and then sends a 32-byte vendor HCI command, opcode 0xFC87 with a 28-byte parameter block, built from the 8-byte request in param_1: byte 0 goes to parameter 6, bytes 1 to 6 (an address) fill parameters 8 to 13, and byte 7 is a key. The key is matched against the first byte of the 27 six-byte records at 0x20003EF0; parameters 15, 16 and 18-19 take that record's byte 2, byte 1 and u16 at +4. The fixed parts are parameters 0-3 = 01 E8 03 00, parameter 7 = 0x02, parameter 14 = 0x01, parameter 17 = 0x04 and parameters 24-27 = 0xFFFFFFFF, with 4-5 and 20-23 zero. A missing key returns -1 without sending; on a match the counters at 0x2000F468 and 0x2000F46C are cleared when set, and the frame goes out through FUN_0C03AC98 with length 32.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 8-byte request: [0] parameter byte, [1..6] address, [7] record key |

**Returns** `s32`: 0 when a matching record was sent, -1 when no record has the key

**Notes:** Field meanings (the 0xFC87 command, the 0x03E8 word, the 27-record table) are inferred from the parameter layout. The constant sibling ble_vendor_fc87_send_test_pattern is the cross-check. FUN_0C03AC98 and FUN_0C03BD70 are not yet described.

- Addresses by version: 219: 0x0C046A58
- Called by: `ble_factory_test_dispatch_set`
- Calls: `ble_mem_copy`, `bt_drv_hci_cmd_send_wait`, `bt_drv_hci_cmd_post_settle`
- Confidence: medium

## ble_vendor_fc87_send_test_pattern

**Send the fixed vendor HCI 0xFC87 test frame with a 0x55 address field**

Takes no input and sends one fixed 32-byte frame: vendor opcode 0xFC87, parameter length 28, and parameters 02 E8 03 00 | 00 00 00 02 | 55 55 55 55 55 55 | 01 01 | 04 04 36 00 | 00 00 00 00 | FF FF FF FF. It is the keyed frame of ble_vendor_fc87_send_keyed with the address field filled with 0x55 bytes, mode byte 0x02 instead of the keyed 0x01, and the table fields set to constants (0x0036 at parameters 18-19). The 0x55 payload and the test-style layout suggest a non-signalling TX or test configuration, which is an inference. It calls only FUN_0C03AC98, without FUN_0C03BD70.

**Returns** `s32`: always 0

**Notes:** Caller is ble_219_0c02c49c, which also calls the keyed sender and the LE test commands.

- Addresses by version: 219: 0x0C046AF0
- Called by: `ble_factory_test_dispatch_set`
- Calls: `bt_drv_hci_cmd_send_wait`
- Confidence: low

## bt_drv_ctrl_bringup_rf_test

**BT controller bring-up for RF non-signalling test, then three fixed HCI packets**

Runs the same opening sequence as bt_drv_ctrl_bringup (link init, callback store, reg-op guard, post_settle, RF regset mode 0, FC77 and FC81 steps, stub). It then sends three fixed HCI packets from ROM at 0x0C076918 (4 bytes), 0x0C07692C (5 bytes) and 0x0C07695C (7 bytes), each followed by a 100-unit delay through the RAM thunks at 0x20000570 and 0x20000334. It finishes by setting DAT_2000BD18 to 1 to mark the test setup as done. Its caller ble_219_0c02c49c is not described here.

**Notes:** The packets are read as the RF test setup from their ROM addresses. Their exact opcodes are not decoded.

- Addresses by version: 219: 0x0C046C7C
- Called by: `ble_factory_test_dispatch_set`
- Calls: `stub_empty_0c03aa3c`, `bt_drv_set_global_2000bd1c`, `bt_drv_hci_cmd_send_wait`, `bt_drv_intersys_link_init_once`, `bt_drv_rf_regset_mode0_select`, `bt_drv_hci_cmd_post_settle`, `bt_drv_vendor_fc77_set_value`, `bt_drv_vendor_fc81_cmd`, `bt_drv_reg_op_env_bde4_clear_flags_thunk`, `bt_drv_reg_op_env_bde4_set_byte18`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## bt_drv_vco_test_session_start

**Start a factory VCO test session on one channel, saving and overriding two analog registers**

Part of the factory VCO test pair with bt_drv_vco_test_session_stop. It returns at once if DAT_2000BD10 is already set; otherwise it sets DAT_2000BD10, saves analog register 0x20C1 into DAT_2000BD0E and 0x2024 into DAT_2000BD0C. It then calls bt_drv_vco_test_start with the channel, clears bit 11 of 0x20C1 and writes bits 7:4 of 0x2024 to 1001b (0x90). The stop function restores the saved values.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | BT channel index, 0..78 |

**Notes:** Called from the factory command handler at 0x0C02C49C, which is outside this packet.

- Addresses by version: 219: 0x0C03BD90
- Called by: `ble_factory_test_dispatch_set`
- Calls: `bt_drv_vco_test_start`, `hal_analogif_reg_read`, `hal_analogif_reg_write`
- Confidence: high

## bt_drv_vco_test_session_stop

**End the factory VCO test session and restore the saved analog registers**

Second half of the factory VCO test pair. If DAT_2000BD10 is set it clears it, calls bt_drv_vco_test_stop to zero RF word 0xD0220C00, and writes the values saved by bt_drv_vco_test_session_start back to analog registers 0x20C1 and 0x2024. It does nothing when no session is active.

**Notes:** Called from 0x0C02C49C, which is outside this packet.

- Addresses by version: 219: 0x0C03BE14
- Called by: `ble_factory_test_dispatch_set`
- Calls: `bt_drv_vco_test_stop`, `hal_analogif_reg_write`
- Confidence: high

## bt_drv_vco_test_start

**Start the BT VCO/synthesiser test on a channel: 0xD0220C00 = (channel & 0x7F) | 0xA0000, then delay**

Enables controller register access if DAT_2000bd58 == 0, increments the nesting counter, writes (param_1 & 0x7F) | 0x000A0000 to the RF channel register 0xD0220C00 (low 7 bits = channel index 0..78, bits 17 and 19 = test/enable flags), waits via ble_ram_patch_thunk_20000570(10) followed by ble_ram_patch_thunk_20000334 (RAM-resident delay pair), decrements the counter and releases access with bes_sysreg_write_08_bit19 if it is back to 0. Caller 0x0c03bd90 is the 'bt vco test start, channel[%d]' factory command handler, which also saves/modifies two RF registers (0x20C1, 0x2024) around it; bt_drv_vco_test_stop undoes it.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | BT channel index (0..78), masked to 7 bits |

- Addresses by version: 219: 0x0C03DFAC
- Called by: `bt_drv_vco_test_session_start`
- Calls: `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: high

## bt_drv_vco_test_stop

**Stop the BT VCO test: write 0 to RF channel register 0xD0220C00, then delay**

Mirror of bt_drv_vco_test_start: enables controller register access if DAT_2000bd58 == 0, increments the counter, writes 0 to 0xD0220C00 (clears the channel and the test flag bits 17/19), delays with ble_ram_patch_thunk_20000570(10) + ble_ram_patch_thunk_20000334, decrements the counter and releases access when it reaches 0. Called from 0x0c03be14, the 'bt vco test stop' factory command handler, which then restores the saved RF registers 0x20C1 and 0x2024.

- Addresses by version: 219: 0x0C03DFF4
- Called by: `bt_drv_vco_test_session_stop`
- Calls: `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: high

## rf_test_hci_cmd_complete_handler

**Capture return parameters of RF-test HCI Command Complete events into globals**

HCI event packet parser used by the factory RF test: param_1[0] = 0x04 (HCI event), [1] = 0x0e (Command Complete), [2] = parameter length, [3] = Num_HCI_Command_Packets, [4..5] = opcode, [6] = status, [7..] = return parameters. For an 18-byte Command Complete whose first two return bytes are non-zero it copies 16 bytes from offset 7 (via the memcpy wrapper 0x0c03aa40) and stores the first 6 into DAT_2000f468 (u32) and DAT_2000f46c (u16) -- the vendor RX-test result that the test command builder 0x0c046a58 (vendor opcode 0xfc87) clears before starting. For a 6-byte Command Complete with a non-zero 2-byte return value (the shape of HCI_LE_Test_End: status + Number_Of_Packets) the u16 is stored in DAT_2000f464, which 0x0c046b4c (HCI_LE_Transmitter_Test, opcode 0x201e) resets before a TX test. Always returns 0; the opcode itself is not checked.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | raw HCI event packet starting with the 0x04 indicator byte |

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C0468B4
- Calls: `ble_mem_copy`
- Confidence: medium
