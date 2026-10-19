# BLE - `factory_test` functions

12 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`ble_hci_le_enh_rx_test_cmd`](#ble_hci_le_enh_rx_test_cmd) | 0x0C046BFC | Send HCI LE Enhanced Receiver Test (0x2033) with three parameter bytes |
| [`ble_hci_le_enh_tx_test_cmd`](#ble_hci_le_enh_tx_test_cmd) | 0x0C046BBC | Send HCI LE Enhanced Transmitter Test (0x2034) with four parameter bytes |
| [`ble_hci_le_rx_test_cmd`](#ble_hci_le_rx_test_cmd) | 0x0C046B90 | Send HCI LE Receiver Test (0x201D) with one RX channel byte |
| [`ble_hci_le_test_end_cmd`](#ble_hci_le_test_end_cmd) | 0x0C046C34 | Send HCI LE Test End (0x201F), which has no parameters |
| [`ble_hci_le_tx_test_cmd`](#ble_hci_le_tx_test_cmd) | 0x0C046B4C | Send HCI LE Transmitter Test (0x201E) with channel, length and payload type |
| [`ble_vendor_fc87_send_keyed`](#ble_vendor_fc87_send_keyed) | 0x0C046A58 | Send vendor HCI 0xFC87 for the table record whose key matches request byte 7 |
| [`ble_vendor_fc87_send_test_pattern`](#ble_vendor_fc87_send_test_pattern) | 0x0C046AF0 | Send the fixed vendor HCI 0xFC87 test frame with a 0x55 address field |
| [`bt_drv_vco_test_session_start`](#bt_drv_vco_test_session_start) | 0x0C03BD90 | Start a factory VCO test session on one channel, saving and overriding two analog registers |
| [`bt_drv_vco_test_session_stop`](#bt_drv_vco_test_session_stop) | 0x0C03BE14 | End the factory VCO test session and restore the saved analog registers |
| [`bt_drv_vco_test_start`](#bt_drv_vco_test_start) | 0x0C03DFAC | Start the BT VCO/synthesiser test on a channel: 0xD0220C00 = (channel & 0x7F) \| 0xA0000, then delay |
| [`bt_drv_vco_test_stop`](#bt_drv_vco_test_stop) | 0x0C03DFF4 | Stop the BT VCO test: write 0 to RF channel register 0xD0220C00, then delay |
| [`rf_test_hci_cmd_complete_handler`](#rf_test_hci_cmd_complete_handler) | 0x0C0468B4 | Capture return parameters of RF-test HCI Command Complete events into globals |

## ble_hci_le_enh_rx_test_cmd

**Send HCI LE Enhanced Receiver Test (0x2033) with three parameter bytes**

Sends the 7-byte HCI command 01 33 20 03 p0 p1 p2, which is LE Enhanced Receiver Test (opcode 0x2033): RX_Channel, PHY and Modulation_Index, from the 3-byte request. It runs FUN_0C03BD70 first, then FUN_0C03AC98, and always returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 3 parameter bytes: channel, PHY, modulation index |

**Returns** `s32`: always 0

- Addresses by version: 219: 0x0C046BFC
- Called by: `ble_219_0c02c49c`
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
- Called by: `ble_219_0c02c49c`
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
- Called by: `ble_219_0c02c49c`
- Calls: `bt_drv_hci_cmd_send_wait`, `bt_drv_hci_cmd_post_settle`
- Confidence: high

## ble_hci_le_test_end_cmd

**Send HCI LE Test End (0x201F), which has no parameters**

Sends the 4-byte HCI command 01 1F 20 00, which is LE Test End (opcode 0x201F), through FUN_0C03AC98, and returns 0. Unlike the other test-command senders it does not call FUN_0C03BD70 first. The controller's reply, which carries the received-packet count in the Bluetooth spec, is handled elsewhere.

**Returns** `s32`: always 0

- Addresses by version: 219: 0x0C046C34
- Called by: `ble_219_0c02c49c`
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
- Called by: `ble_219_0c02c49c`
- Calls: `bt_drv_hci_cmd_send_wait`, `bt_drv_hci_cmd_post_settle`
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
- Called by: `ble_219_0c02c49c`
- Calls: `ble_mem_copy`, `bt_drv_hci_cmd_send_wait`, `bt_drv_hci_cmd_post_settle`
- Confidence: medium

## ble_vendor_fc87_send_test_pattern

**Send the fixed vendor HCI 0xFC87 test frame with a 0x55 address field**

Takes no input and sends one fixed 32-byte frame: vendor opcode 0xFC87, parameter length 28, and parameters 02 E8 03 00 | 00 00 00 02 | 55 55 55 55 55 55 | 01 01 | 04 04 36 00 | 00 00 00 00 | FF FF FF FF. It is the keyed frame of ble_vendor_fc87_send_keyed with the address field filled with 0x55 bytes, mode byte 0x02 instead of the keyed 0x01, and the table fields set to constants (0x0036 at parameters 18-19). The 0x55 payload and the test-style layout suggest a non-signalling TX or test configuration, which is an inference. It calls only FUN_0C03AC98, without FUN_0C03BD70.

**Returns** `s32`: always 0

**Notes:** Caller is ble_219_0c02c49c, which also calls the keyed sender and the LE test commands.

- Addresses by version: 219: 0x0C046AF0
- Called by: `ble_219_0c02c49c`
- Calls: `bt_drv_hci_cmd_send_wait`
- Confidence: low

## bt_drv_vco_test_session_start

**Start a factory VCO test session on one channel, saving and overriding two analog registers**

Part of the factory VCO test pair with bt_drv_vco_test_session_stop. It returns at once if DAT_2000BD10 is already set; otherwise it sets DAT_2000BD10, saves analog register 0x20C1 into DAT_2000BD0E and 0x2024 into DAT_2000BD0C. It then calls bt_drv_vco_test_start with the channel, clears bit 11 of 0x20C1 and writes bits 7:4 of 0x2024 to 1001b (0x90). The stop function restores the saved values.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | BT channel index, 0..78 |

**Notes:** Called from the factory command handler at 0x0C02C49C, which is outside this packet.

- Addresses by version: 219: 0x0C03BD90
- Called by: `ble_219_0c02c49c`
- Calls: `bt_drv_vco_test_start`, `hal_analogif_reg_read`, `hal_analogif_reg_write`
- Confidence: high

## bt_drv_vco_test_session_stop

**End the factory VCO test session and restore the saved analog registers**

Second half of the factory VCO test pair. If DAT_2000BD10 is set it clears it, calls bt_drv_vco_test_stop to zero RF word 0xD0220C00, and writes the values saved by bt_drv_vco_test_session_start back to analog registers 0x20C1 and 0x2024. It does nothing when no session is active.

**Notes:** Called from 0x0C02C49C, which is outside this packet.

- Addresses by version: 219: 0x0C03BE14
- Called by: `ble_219_0c02c49c`
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
