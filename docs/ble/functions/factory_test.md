# BLE - `factory_test` functions

3 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`bt_drv_vco_test_start`](#bt_drv_vco_test_start) | 0x0C03DFAC | Start the BT VCO/synthesiser test on a channel: 0xD0220C00 = (channel & 0x7F) \| 0xA0000, then delay |
| [`bt_drv_vco_test_stop`](#bt_drv_vco_test_stop) | 0x0C03DFF4 | Stop the BT VCO test: write 0 to RF channel register 0xD0220C00, then delay |
| [`rf_test_hci_cmd_complete_handler`](#rf_test_hci_cmd_complete_handler) | 0x0C0468B4 | Capture return parameters of RF-test HCI Command Complete events into globals |

## bt_drv_vco_test_start

**Start the BT VCO/synthesiser test on a channel: 0xD0220C00 = (channel & 0x7F) | 0xA0000, then delay**

Enables controller register access if DAT_2000bd58 == 0, increments the nesting counter, writes (param_1 & 0x7F) | 0x000A0000 to the RF channel register 0xD0220C00 (low 7 bits = channel index 0..78, bits 17 and 19 = test/enable flags), waits via ble_ram_patch_thunk_20000570(10) followed by ble_ram_patch_thunk_20000334 (RAM-resident delay pair), decrements the counter and releases access with bes_sysreg_write_08_bit19 if it is back to 0. Caller 0x0c03bd90 is the 'bt vco test start, channel[%d]' factory command handler, which also saves/modifies two RF registers (0x20C1, 0x2024) around it; bt_drv_vco_test_stop undoes it.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | BT channel index (0..78), masked to 7 bits |

- Addresses by version: 219: 0x0C03DFAC
- Called by: `ble_219_0c03bd90`
- Calls: `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: high

## bt_drv_vco_test_stop

**Stop the BT VCO test: write 0 to RF channel register 0xD0220C00, then delay**

Mirror of bt_drv_vco_test_start: enables controller register access if DAT_2000bd58 == 0, increments the counter, writes 0 to 0xD0220C00 (clears the channel and the test flag bits 17/19), delays with ble_ram_patch_thunk_20000570(10) + ble_ram_patch_thunk_20000334, decrements the counter and releases access when it reaches 0. Called from 0x0c03be14, the 'bt vco test stop' factory command handler, which then restores the saved RF registers 0x20C1 and 0x2024.

- Addresses by version: 219: 0x0C03DFF4
- Called by: `ble_219_0c03be14`
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
