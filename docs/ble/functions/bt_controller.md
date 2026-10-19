# BLE - `bt_controller` functions

111 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`ble_ctrl_dump_region`](#ble_ctrl_dump_region) | 0x0C03A8F4 | Hex-dump a memory region to the log in 100-byte lines, labelled by region id |
| [`ble_ctrl_sysreg_pulse_bit19`](#ble_ctrl_sysreg_pulse_bit19) | 0x0C04554C | Assert and release bit 19 of the sysreg pair around the controller state word |
| [`ble_flash_patch_thunk_a000e528`](#ble_flash_patch_thunk_a000e528) | 0x0C07DAD0 | Thunk forwarding param_1 to the code at 0xA000E528 |
| [`ble_flash_patch_thunk_a0022c48`](#ble_flash_patch_thunk_a0022c48) | 0x0C07D9F0 | Thunk forwarding param_1 to the code at 0xA0022C48 |
| [`ble_flash_patch_thunk_a0033f74`](#ble_flash_patch_thunk_a0033f74) | 0x0C07DE10 | Thunk forwarding param_1 to the code at 0xA0033F74 |
| [`ble_flash_patch_thunk_a003460c`](#ble_flash_patch_thunk_a003460c) | 0x0C07DDD0 | Thunk forwarding param_1 to the code at 0xA003460C |
| [`ble_flash_patch_thunk_a0074c98`](#ble_flash_patch_thunk_a0074c98) | 0x0C07DE30 | Thunk forwarding param_1 to the code at 0xA0074C98 |
| [`ble_flash_patch_thunk_a007cd24`](#ble_flash_patch_thunk_a007cd24) | 0x0C07DA60 | Thunk forwarding param_1 to the code at 0xA007CD24 |
| [`ble_flash_patch_thunk_a007d4b0`](#ble_flash_patch_thunk_a007d4b0) | 0x0C07DAE0 | Thunk forwarding param_1 to the code at 0xA007D4B0 |
| [`ble_flash_patch_thunk_a007fbac`](#ble_flash_patch_thunk_a007fbac) | 0x0C07D860 | Thunk forwarding param_1 to the code at 0xA007FBAC |
| [`ble_flash_patch_thunk_a007fc0c`](#ble_flash_patch_thunk_a007fc0c) | 0x0C07DE00 | Thunk forwarding param_1 to the code at 0xA007FC0C |
| [`ble_flash_patch_thunk_a0083c2c`](#ble_flash_patch_thunk_a0083c2c) | 0x0C07D840 | Thunk forwarding param_1 to the code at 0xA0083C2C |
| [`ble_hwtimer_guard_restart`](#ble_hwtimer_guard_restart) | 0x0C03AC44 | Restart the BLE guard hwtimer DAT_2000BD14 with a 9000-unit timeout, marking busy bit 31 |
| [`ble_ram_call_2000110c_arg0`](#ble_ram_call_2000110c_arg0) | 0x0C045AC0 | Call the RAM-resident function at 0x2000110c with argument 0 |
| [`ble_ram_patch_thunk_20000220`](#ble_ram_patch_thunk_20000220) | 0x0C073B50 | Thunk forwarding param_1 to the code at 0x20000220 |
| [`ble_ram_patch_thunk_2000022c`](#ble_ram_patch_thunk_2000022c) | 0x0C073C50 | Thunk forwarding param_1 to the code at 0x2000022C |
| [`ble_ram_patch_thunk_20000238`](#ble_ram_patch_thunk_20000238) | 0x0C073B60 | Thunk forwarding param_1 to the code at 0x20000238 |
| [`ble_ram_patch_thunk_20000244`](#ble_ram_patch_thunk_20000244) | 0x0C073C40 | Thunk forwarding param_1 to the code at 0x20000244 |
| [`ble_ram_patch_thunk_2000025c`](#ble_ram_patch_thunk_2000025c) | 0x0C073BA0 | Thunk forwarding param_1 to the code at 0x2000025C |
| [`ble_ram_patch_thunk_200002cc`](#ble_ram_patch_thunk_200002cc) | 0x0C073BE0 | Thunk forwarding param_1 to the code at 0x200002CC |
| [`ble_ram_patch_thunk_2000031c`](#ble_ram_patch_thunk_2000031c) | 0x0C073B30 | Thunk forwarding param_1 to the code at 0x2000031c |
| [`ble_ram_patch_thunk_20000328`](#ble_ram_patch_thunk_20000328) | 0x0C073B70 | Thunk forwarding param_1 to the code at 0x20000328 |
| [`ble_ram_patch_thunk_20000334`](#ble_ram_patch_thunk_20000334) | 0x0C073CC0 | Thunk forwarding param_1 to the code at 0x20000334 |
| [`ble_ram_patch_thunk_20000348`](#ble_ram_patch_thunk_20000348) | 0x0C073AE0 | Thunk forwarding param_1 to the code at 0x20000348 |
| [`ble_ram_patch_thunk_20000534`](#ble_ram_patch_thunk_20000534) | 0x0C073C90 | Thunk forwarding param_1 to the code at 0x20000534 |
| [`ble_ram_patch_thunk_20000554`](#ble_ram_patch_thunk_20000554) | 0x0C073BC0 | Thunk forwarding param_1 to the code at 0x20000554 |
| [`ble_ram_patch_thunk_20000570`](#ble_ram_patch_thunk_20000570) | 0x0C073CB0 | Thunk forwarding param_1 to the code at 0x20000570 |
| [`ble_ram_patch_thunk_200005a8`](#ble_ram_patch_thunk_200005a8) | 0x0C073C20 | Thunk forwarding param_1 to the code at 0x200005A8 |
| [`ble_ram_patch_thunk_200005e8`](#ble_ram_patch_thunk_200005e8) | 0x0C073AD0 | Thunk forwarding param_1 to the code at 0x200005e8 |
| [`ble_ram_patch_thunk_20000650`](#ble_ram_patch_thunk_20000650) | 0x0C073C00 | Thunk forwarding param_1 to the code at 0x20000650 |
| [`ble_ram_patch_thunk_2000065c`](#ble_ram_patch_thunk_2000065c) | 0x0C073B00 | Thunk forwarding param_1 to the code at 0x2000065c |
| [`ble_ram_patch_thunk_2000067c`](#ble_ram_patch_thunk_2000067c) | 0x0C073C80 | Thunk forwarding param_1 to the code at 0x2000067C |
| [`ble_ram_patch_thunk_20000738`](#ble_ram_patch_thunk_20000738) | 0x0C073B80 | Thunk forwarding param_1 to the code at 0x20000738 |
| [`ble_ram_patch_thunk_200007a8`](#ble_ram_patch_thunk_200007a8) | 0x0C073C70 | Thunk forwarding param_1 to the code at 0x200007A8 |
| [`ble_ram_patch_thunk_200007f4`](#ble_ram_patch_thunk_200007f4) | 0x0C073AF0 | Thunk forwarding param_1 to the code at 0x200007f4 |
| [`ble_ram_patch_thunk_2000081c`](#ble_ram_patch_thunk_2000081c) | 0x0C073BB0 | Thunk forwarding param_1 to the code at 0x2000081C |
| [`ble_ram_patch_thunk_20000934`](#ble_ram_patch_thunk_20000934) | 0x0C073B40 | Thunk forwarding param_1 to the code at 0x20000934 |
| [`ble_ram_patch_thunk_20000f34`](#ble_ram_patch_thunk_20000f34) | 0x0C073BF0 | Thunk forwarding param_1 to the code at 0x20000F34 |
| [`ble_ram_patch_thunk_2000106c`](#ble_ram_patch_thunk_2000106c) | 0x0C073B90 | Thunk forwarding param_1 to the code at 0x2000106C |
| [`ble_ram_patch_thunk_200010a0`](#ble_ram_patch_thunk_200010a0) | 0x0C073CA0 | Thunk forwarding param_1 to the code at 0x200010A0 |
| [`ble_ram_patch_thunk_20001c10`](#ble_ram_patch_thunk_20001c10) | 0x0C073B10 | Thunk forwarding param_1 to the code at 0x20001c10 |
| [`ble_ram_patch_thunk_20001ca0`](#ble_ram_patch_thunk_20001ca0) | 0x0C073B20 | Thunk forwarding param_1 to the code at 0x20001ca0 |
| [`ble_ram_patch_thunk_20001d38`](#ble_ram_patch_thunk_20001d38) | 0x0C073BD0 | Thunk forwarding param_1 to the code at 0x20001D38 |
| [`ble_ram_patch_thunk_20001d7c`](#ble_ram_patch_thunk_20001d7c) | 0x0C073C10 | Thunk forwarding param_1 to the code at 0x20001D7C |
| [`bt_ctrl_crash_dump`](#bt_ctrl_crash_dump) | 0x0C03D69C | Log the BT controller crash record: ROM and patch versions, fault and stack registers, BT errors |
| [`bt_ctrl_crash_dump_irq_safe`](#bt_ctrl_crash_dump_irq_safe) | 0x0C03DD80 | Run the BT crash dump with IRQs masked and memory barriers around it |
| [`bt_drv_analog_init_20f2_variant`](#bt_drv_analog_init_20f2_variant) | 0x0C03E49C | On the variant path, clear analog 0x20F2 and 0x20F3 and set 0x20F4 to 0x7C |
| [`bt_drv_analog_reg200f_set_1`](#bt_drv_analog_reg200f_set_1) | 0x0C03E490 | Write value 1 to analog register 0x200F |
| [`bt_drv_ctrl_bringup`](#bt_drv_ctrl_bringup) | 0x0C04696C | BT controller bring-up sequence A: link init, callback, RF regset, vendor FC77 and FC81 |
| [`bt_drv_ctrl_param_load_all`](#bt_drv_ctrl_param_load_all) | 0x0C03E314 | Load the controller RSSI, timing and table parameters and set the RF mode field |
| [`bt_drv_digital_assert_check`](#bt_drv_digital_assert_check) | 0x0C03DF24 | Check BT digital error status and the crash-record word; log and return 1 on assert |
| [`bt_drv_hci_cmd_complete_info_rx`](#bt_drv_hci_cmd_complete_info_rx) | 0x0C03BFBC | Command Complete hook that copies a 16-byte vendor response into RAM at 0x2000BD38 |
| [`bt_drv_hci_cmd_post_settle`](#bt_drv_hci_cmd_post_settle) | 0x0C03BD70 | Send the fixed 4-byte HCI packet at 0x0C076914 and wait 350 units |
| [`bt_drv_hci_cmd_send_wait`](#bt_drv_hci_cmd_send_wait) | 0x0C03AC98 | Send an HCI packet to the BT core and poll a reply flag with a timeout |
| [`bt_drv_hci_evt_conn_state_hook`](#bt_drv_hci_evt_conn_state_hook) | 0x0C03BCCC | HCI event hook for Connection Complete and Disconnection Complete state changes |
| [`bt_drv_hci_vendor_cmd_send`](#bt_drv_hci_vendor_cmd_send) | 0x0C03BE50 | Build an H4 HCI command from opcode, length and parameters, then send it |
| [`bt_drv_intersys_link_init_once`](#bt_drv_intersys_link_init_once) | 0x0C03ACF0 | One-time BT-core link setup: set the controller-running flag and register callbacks |
| [`bt_drv_intersys_send_saved_iface`](#bt_drv_intersys_send_saved_iface) | 0x0C03EB84 | Send a buffer to the BT core over the intersys link using the interface id saved in DAT_2000be2e, type 0 |
| [`bt_drv_pending_action_poll`](#bt_drv_pending_action_poll) | 0x0C03C034 | Service two pending flags: resend the 350-unit HCI step and call 0x0C044D90 |
| [`bt_drv_reg_op_addr_table_init`](#bt_drv_reg_op_addr_table_init) | 0x0C03D088 | Fill the table of BT-controller RAM addresses (0xC000xxxx) used by the bt_drv_reg_op accessors, per metal id |
| [`bt_drv_reg_op_env_bde4_clear_flags`](#bt_drv_reg_op_env_bde4_clear_flags) | 0x0C03DD9C | Zero byte 0 and byte 0x36 of the controller RAM structure at DAT_2000bde4 under the register-access guard |
| [`bt_drv_reg_op_env_bde4_clear_flags_thunk`](#bt_drv_reg_op_env_bde4_clear_flags_thunk) | 0x0C03D028 | Thunk (1 insn) to bt_drv_reg_op_env_bde4_clear_flags |
| [`bt_drv_reg_op_env_bde4_set_byte18`](#bt_drv_reg_op_env_bde4_set_byte18) | 0x0C03DE58 | Store a byte at offset 0x18 of the controller RAM structure DAT_2000bde4 under the register-access guard |
| [`bt_drv_reg_op_get_patch_var_bdac`](#bt_drv_reg_op_get_patch_var_bdac) | 0x0C03E1B8 | Read the 32-bit controller RAM variable pointed to by DAT_2000bdac (0 if unavailable) |
| [`bt_drv_reg_op_load_rssi_table_a`](#bt_drv_reg_op_load_rssi_table_a) | 0x0C03E078 | Copy the 30-byte table at 0x0c07fdc0 into the controller RAM location DAT_2000bdec |
| [`bt_drv_reg_op_load_rssi_table_b`](#bt_drv_reg_op_load_rssi_table_b) | 0x0C03E0C8 | Copy the 30-byte table at 0x0c07fde0 into the controller RAM location DAT_2000bdfc |
| [`bt_drv_reg_op_load_rssi_table_c`](#bt_drv_reg_op_load_rssi_table_c) | 0x0C03E118 | Copy the 30-byte table at 0x0c07fda0 into the controller RAM location DAT_2000bdf0 |
| [`bt_drv_reg_op_load_table8_bdd4`](#bt_drv_reg_op_load_table8_bdd4) | 0x0C03E168 | Copy the 8-byte RAM table at 0x20003EAC into the controller RAM location DAT_2000bdd4 |
| [`bt_drv_reg_op_read_acl_rssi`](#bt_drv_reg_op_read_acl_rssi) | 0x0C03E264 | Return the signed RSSI byte (+0x152) of the BT ACL link environment for a connection handle |
| [`bt_drv_reg_op_read_ble_rssi`](#bt_drv_reg_op_read_ble_rssi) | 0x0C03E2C0 | Return the signed byte at +9 of the 12-byte BLE RX-monitor entry for a BLE link index |
| [`bt_drv_reg_op_set_patch_var_be00`](#bt_drv_reg_op_set_patch_var_be00) | 0x0C03E1F0 | Write a 32-bit value to the controller RAM variable pointed to by DAT_2000be00 |
| [`bt_drv_reg_op_set_rssi_monitor_params`](#bt_drv_reg_op_set_rssi_monitor_params) | 0x0C03DE90 | Fill the controller RAM parameter block DAT_2000bdc8 with RSSI thresholds (-100/-90 dBm) and window counts |
| [`bt_drv_reg_op_set_timing_params`](#bt_drv_reg_op_set_timing_params) | 0x0C03DDD8 | Write slot-timing constants (1250, 625, 500 us, 400, 12, 20) into two controller RAM parameter blocks |
| [`bt_drv_reg_op_write_6byte_param`](#bt_drv_reg_op_write_6byte_param) | 0x0C03D02C | Copy a 6-byte constant (u32 + u16) into the controller RAM location DAT_2000bdb4 and report the elapsed time |
| [`bt_drv_rf_0x2018_from_cfg_mode`](#bt_drv_rf_0x2018_from_cfg_mode) | 0x0C03E8F0 | Set the low 6 bits of analog 0x2018 from a 2-bit mode in calibration record 0x0C |
| [`bt_drv_rf_0x2058_fields_remap`](#bt_drv_rf_0x2058_fields_remap) | 0x0C03E66C | Remap two 7-bit fields of analog 0x2058 into 0x202E and set bits 13:11 of 0x202D |
| [`bt_drv_rf_0x208f_field_from_cfg`](#bt_drv_rf_0x208f_field_from_cfg) | 0x0C03E9AC | Copy bits 11:9 of calibration record 0x0C into analog 0x208F bits 6:4 |
| [`bt_drv_rf_2168_cal_search`](#bt_drv_rf_2168_cal_search) | 0x0C03C070 | Closed-loop search that tunes the 9-bit field of analog 0x2168 until the RF cal error is zero |
| [`bt_drv_rf_2168_field9_set`](#bt_drv_rf_2168_field9_set) | 0x0C03E454 | Set the 9-bit field of analog register 0x2168 and refresh its shadow |
| [`bt_drv_rf_2168_update_from_src`](#bt_drv_rf_2168_update_from_src) | 0x0C03E5DC | Update the 9-bit field of analog 0x2168 from an external measurement or a fallback value |
| [`bt_drv_rf_analog_bringup`](#bt_drv_rf_analog_bringup) | 0x0C03E9FC | RF analog front-end bring-up: init tables, LUT registers, config record and register sets |
| [`bt_drv_rf_apply_cfg_record`](#bt_drv_rf_apply_cfg_record) | 0x0C03E51C | Apply the RAM config record at 0x2000BE0C-0x2000BE20 to the RF lookup registers |
| [`bt_drv_rf_apply_config`](#bt_drv_rf_apply_config) | 0x0C03C4BC | Program the BT RF/analog registers 0xD0220Cxx and 0xD0350xxx from a ~0x27-byte config struct |
| [`bt_drv_rf_bringup`](#bt_drv_rf_bringup) | 0x0C03BB70 | BT RF bring-up: clock level 4, RF init and calibration chain, ISR channel and IPC setup |
| [`bt_drv_rf_dc_iq_cal_run`](#bt_drv_rf_dc_iq_cal_run) | 0x0C03B8D4 | Run the RF DC/IQ calibration sweep inside a save and restore of RF and analog state |
| [`bt_drv_rf_gain_ratio_rescale`](#bt_drv_rf_gain_ratio_rescale) | 0x0C03AD44 | Rescale about 30 analog gain bit-fields by a power ratio read from register 0x2144 |
| [`bt_drv_rf_init`](#bt_drv_rf_init) | 0x0C03CDFC | BT RF bring-up sequence: pre-init, 0xD0350xxx main init, analog defaults, then apply the built-in RF config |
| [`bt_drv_rf_pre_init`](#bt_drv_rf_pre_init) | 0x0C03C930 | First step of RF bring-up: clear/set a few 0xD0220Cxx bits, init 0xD0350xxx, write 0xCAFE0001 to 0x40080020 |
| [`bt_drv_rf_reg_lo6_from_lut`](#bt_drv_rf_reg_lo6_from_lut) | 0x0C03E388 | Write the table code for a float setting into bits 5:0 of analog register 0x2049+index |
| [`bt_drv_rf_reg_mid6_from_lut`](#bt_drv_rf_reg_mid6_from_lut) | 0x0C03E3E8 | Write the table code for a float setting into bits 11:6 of analog register 0x2049+index |
| [`bt_drv_rf_regset_capture`](#bt_drv_rf_regset_capture) | 0x0C03E7D0 | Save the two analog register sets used by bt_drv_rf_regset_select |
| [`bt_drv_rf_regset_mode0_select`](#bt_drv_rf_regset_mode0_select) | 0x0C03BC74 | Call the RF register-set selector with mode 0 |
| [`bt_drv_rf_regset_select`](#bt_drv_rf_regset_select) | 0x0C03E844 | Switch analog 0x221D, 0x221E and the low byte of 0x2235 to saved set 0 or 1 |
| [`bt_drv_rf_set_reg_c7c_bits13_14`](#bt_drv_rf_set_reg_c7c_bits13_14) | 0x0C03E034 | Write a 2-bit value into field [14:13] of RF register 0xD0220C7C under the register-access guard |
| [`bt_drv_rf_tx_power_trim_apply`](#bt_drv_rf_tx_power_trim_apply) | 0x0C03BA38 | Apply the signed TX power trim from calibration record 7 to power and gain registers |
| [`bt_drv_rfcal_timer_run`](#bt_drv_rfcal_timer_run) | 0x0C03BE8C | Create the rfcal timer on first use, then start it or run one RF calibration cycle |
| [`bt_drv_rom_patch_apply_table`](#bt_drv_rom_patch_apply_table) | 0x0C03CEC8 | Install a BT-controller ROM patch table: copy data into BT RAM, then program 64 hardware patch slots |
| [`bt_drv_rom_patch_init`](#bt_drv_rom_patch_init) | 0x0C03CFC0 | Select the ROM patch table by controller metal id, apply it and enable the patch unit (bit 31 of 0xA01FFE00) |
| [`bt_drv_vendor_ctrl_init_cmds`](#bt_drv_vendor_ctrl_init_cmds) | 0x0C03CD58 | Send the BES vendor controller-init commands 0xFC71, the 0xFCxx record table and 0xFCC3 |
| [`bt_drv_vendor_fc77_set_value`](#bt_drv_vendor_fc77_set_value) | 0x0C03CE14 | Store a byte in DAT_20003EB4 and send vendor command 0xFC77 with an 8-byte block |
| [`bt_drv_vendor_fc81_cmd`](#bt_drv_vendor_fc81_cmd) | 0x0C03CE38 | Send vendor command 0xFC81 with an 8-byte block and wait one unit |
| [`bt_lc_link_setup_patch`](#bt_lc_link_setup_patch) | 0x0C07C7B4 | ROM patch: record a link's 6-byte address in the 9-byte-per-link table at 0xC0004FD0 and start the ROM link setup |
| [`bt_ld_acl_clk_offset_update_patch`](#bt_ld_acl_clk_offset_update_patch) | 0x0C07C04C | ROM patch: adjust an ACL link's clock offset and notify LC tasks of the new ACL/eSCO anchor phase |
| [`bt_ld_acl_sniff_state_patch`](#bt_ld_acl_sniff_state_patch) | 0x0C07D664 | ROM patch: on an ACL link event, promote state byte +0x16b from 1 to 2/3 based on EM control flags, then run ROM handlers |
| [`bt_patch_entry_0c07cdd8`](#bt_patch_entry_0c07cdd8) | 0x0C07CDD8 | Patch trampoline: call bt_lc_link_setup_patch then fall into undecodable bytes |
| [`bt_rfcal_dc_iq_sweep_all_bands`](#bt_rfcal_dc_iq_sweep_all_bands) | 0x0C03F1F4 | DC offset and IQ calibration sweep: coarse-to-fine I and Q search per band, table store |
| [`bt_rfcal_measure_residual_fmt14`](#bt_rfcal_measure_residual_fmt14) | 0x0C03EB98 | RF calibration cost function: set two 14-bit codes in a register, trigger a measurement, average sqrt(I^2+Q^2) |
| [`bt_rfcal_measure_residual_fmt16`](#bt_rfcal_measure_residual_fmt16) | 0x0C03ECC8 | RF calibration cost function variant: 14-bit codes at [13:0]/[29:16], pulses 0xD0350250 bit 31, resets 0xD03300xx |
| [`bt_rfcal_search_i_fmt14`](#bt_rfcal_search_i_fmt14) | 0x0C03EFC0 | Refine the I code on register 0xD0350250 with fmt14 residual probes, Q fixed |
| [`bt_rfcal_search_i_fmt16`](#bt_rfcal_search_i_fmt16) | 0x0C03EE44 | Refine the I code of a band calibration point using fmt16 residual probes |
| [`bt_rfcal_search_q_fmt14`](#bt_rfcal_search_q_fmt14) | 0x0C03F0DC | Refine the Q code on register 0xD0350250 with fmt14 residual probes, I fixed |

## ble_ctrl_dump_region

**Hex-dump a memory region to the log in 100-byte lines, labelled by region id**

Prints a banner for the region (controller, mcu, em_area1 or em_area2), then the bytes as lines of up to 100 bytes. Each line starts with dump_line=N and is produced by the byte formatter at 0x0C033150 (format %02x, element size 1). The routine waits 100 units before the first line and 50 units after each line, using the paired RAM-patch thunks. An unknown region id with a zero length prints nothing, and with a non-zero length it prints only the lines. Called from bt_ctrl_crash_dump.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | start address of the region |
| `param_2` | `u32` | length in bytes |
| `param_3` | `u32` | region id: 0 controller RAM, 1 MCU, 2 em_area1, 3 em_area2 |

**Notes:** The byte formatter at 0x0C033150 is not described in this packet.

- Addresses by version: 219: 0x0C03A8F4
- Called by: `bt_ctrl_crash_dump`
- Calls: `ble_uart_print_values_thunk`, `trace_printf`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: high

## ble_ctrl_sysreg_pulse_bit19

**Assert and release bit 19 of the sysreg pair around the controller state word**

Calls ble_219_0c03bb70 (not described here), then reads the controller state word DAT_2000BD58. When that word is zero it asserts bit 19 of 0x40080004 through bes_sysreg_write_04_bit19, stores state code 0x14 through the pointer in DAT_2000BDA0 when that pointer is set, and if the state word is still zero afterwards it releases bit 19 of 0x40080008 through bes_sysreg_write_08_bit19. When the state word is non-zero it only stores 0x14 through DAT_2000BDA0 and returns.

**Notes:** The bit-19 set and clear pair is described from the callee summaries. The meaning of DAT_2000BD58, the pointer DAT_2000BDA0 and state code 0x14 are not established.

- Addresses by version: 219: 0x0C04554C
- Called by: `ble_host_controller_init`
- Calls: `bt_drv_rf_bringup`, `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: low

## ble_flash_patch_thunk_a000e528

**Thunk forwarding param_1 to the code at 0xA000E528**

Single-instruction-sequence trampoline (5 insns: load literal, BLX/BX, return). It forwards its one argument (param_1, passed through in r0) to the function at 0xA000E529 (0xA0000000-based alias of the flash/ROM image, Thumb bit set) via an indirect call and returns whatever that routine does (decompiler shows void). The target is a hard-coded constant in the 0xA0000000 window, so this is a link-time/ROM-patch jump stub into the Bestechnic code region rather than ordinary application logic. The purpose of the target is not recoverable from this stub alone; it is called from the BT controller code region near 0x0c07c000-0x0c07d700 (1 direct caller).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C07DAD0
- Called by: `bt_lc_link_setup_patch`
- Confidence: medium

## ble_flash_patch_thunk_a0022c48

**Thunk forwarding param_1 to the code at 0xA0022C48**

Single-instruction-sequence trampoline (5 insns: load literal, BLX/BX, return). It forwards its one argument (param_1, passed through in r0) to the function at 0xA0022C49 (0xA0000000-based alias of the flash/ROM image, Thumb bit set) via an indirect call and returns whatever that routine does (decompiler shows void). The target is a hard-coded constant in the 0xA0000000 window, so this is a link-time/ROM-patch jump stub into the Bestechnic code region rather than ordinary application logic. The purpose of the target is not recoverable from this stub alone; it is called from the BT controller code region near 0x0c07c000-0x0c07d700 (1 direct caller).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C07D9F0
- Called by: `bt_ld_acl_sniff_state_patch`
- Confidence: medium

## ble_flash_patch_thunk_a0033f74

**Thunk forwarding param_1 to the code at 0xA0033F74**

Single-instruction-sequence trampoline (5 insns: load literal, BLX/BX, return). It forwards its one argument (param_1, passed through in r0) to the function at 0xA0033F75 (0xA0000000-based alias of the flash/ROM image, Thumb bit set) via an indirect call and returns whatever that routine does (decompiler shows void). The target is a hard-coded constant in the 0xA0000000 window, so this is a link-time/ROM-patch jump stub into the Bestechnic code region rather than ordinary application logic. The purpose of the target is not recoverable from this stub alone; it is called from the BT controller code region near 0x0c07c000-0x0c07d700 (1 direct caller).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C07DE10
- Called by: `bt_ld_acl_sniff_state_patch`
- Confidence: medium

## ble_flash_patch_thunk_a003460c

**Thunk forwarding param_1 to the code at 0xA003460C**

Single-instruction-sequence trampoline (5 insns: load literal, BLX/BX, return). It forwards its one argument (param_1, passed through in r0) to the function at 0xA003460D (0xA0000000-based alias of the flash/ROM image, Thumb bit set) via an indirect call and returns whatever that routine does (decompiler shows void). The target is a hard-coded constant in the 0xA0000000 window, so this is a link-time/ROM-patch jump stub into the Bestechnic code region rather than ordinary application logic. The purpose of the target is not recoverable from this stub alone; it is called from the BT controller code region near 0x0c07c000-0x0c07d700 (1 direct caller).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C07DDD0
- Called by: `bt_ld_acl_sniff_state_patch`
- Confidence: medium

## ble_flash_patch_thunk_a0074c98

**Thunk forwarding param_1 to the code at 0xA0074C98**

Single-instruction-sequence trampoline (5 insns: load literal, BLX/BX, return). It forwards its one argument (param_1, passed through in r0) to the function at 0xA0074C99 (0xA0000000-based alias of the flash/ROM image, Thumb bit set) via an indirect call and returns whatever that routine does (decompiler shows void). The target is a hard-coded constant in the 0xA0000000 window, so this is a link-time/ROM-patch jump stub into the Bestechnic code region rather than ordinary application logic. The purpose of the target is not recoverable from this stub alone; it is called from the BT controller code region near 0x0c07c000-0x0c07d700 (1 direct caller).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C07DE30
- Called by: `bt_lc_link_setup_patch`
- Confidence: medium

## ble_flash_patch_thunk_a007cd24

**Thunk forwarding param_1 to the code at 0xA007CD24**

Single-instruction-sequence trampoline (5 insns: load literal, BLX/BX, return). It forwards its one argument (param_1, passed through in r0) to the function at 0xA007CD25 (0xA0000000-based alias of the flash/ROM image, Thumb bit set) via an indirect call and returns whatever that routine does (decompiler shows void). The target is a hard-coded constant in the 0xA0000000 window, so this is a link-time/ROM-patch jump stub into the Bestechnic code region rather than ordinary application logic. The purpose of the target is not recoverable from this stub alone; it is called from the BT controller code region near 0x0c07c000-0x0c07d700 (1 direct caller).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C07DA60
- Called by: `bt_ld_acl_clk_offset_update_patch`
- Confidence: medium

## ble_flash_patch_thunk_a007d4b0

**Thunk forwarding param_1 to the code at 0xA007D4B0**

Single-instruction-sequence trampoline (5 insns: load literal, BLX/BX, return). It forwards its one argument (param_1, passed through in r0) to the function at 0xA007D4B1 (0xA0000000-based alias of the flash/ROM image, Thumb bit set) via an indirect call and returns whatever that routine does (decompiler shows void). The target is a hard-coded constant in the 0xA0000000 window, so this is a link-time/ROM-patch jump stub into the Bestechnic code region rather than ordinary application logic. The purpose of the target is not recoverable from this stub alone; it is called from the BT controller code region near 0x0c07c000-0x0c07d700 (1 direct caller).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C07DAE0
- Called by: `bt_ld_acl_sniff_state_patch`
- Confidence: medium

## ble_flash_patch_thunk_a007fbac

**Thunk forwarding param_1 to the code at 0xA007FBAC**

Single-instruction-sequence trampoline (5 insns: load literal, BLX/BX, return). It forwards its one argument (param_1, passed through in r0) to the function at 0xA007FBAD (0xA0000000-based alias of the flash/ROM image, Thumb bit set) via an indirect call and returns whatever that routine does (decompiler shows void). The target is a hard-coded constant in the 0xA0000000 window, so this is a link-time/ROM-patch jump stub into the Bestechnic code region rather than ordinary application logic. The purpose of the target is not recoverable from this stub alone; it is called from the BT controller code region near 0x0c07c000-0x0c07d700 (1 direct caller).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C07D860
- Called by: `bt_ld_acl_clk_offset_update_patch`
- Confidence: medium

## ble_flash_patch_thunk_a007fc0c

**Thunk forwarding param_1 to the code at 0xA007FC0C**

Single-instruction-sequence trampoline (5 insns: load literal, BLX/BX, return). It forwards its one argument (param_1, passed through in r0) to the function at 0xA007FC0D (0xA0000000-based alias of the flash/ROM image, Thumb bit set) via an indirect call and returns whatever that routine does (decompiler shows void). The target is a hard-coded constant in the 0xA0000000 window, so this is a link-time/ROM-patch jump stub into the Bestechnic code region rather than ordinary application logic. The purpose of the target is not recoverable from this stub alone; it is called from the BT controller code region near 0x0c07c000-0x0c07d700 (1 direct caller).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C07DE00
- Called by: `bt_ld_acl_clk_offset_update_patch`
- Confidence: medium

## ble_flash_patch_thunk_a0083c2c

**Thunk forwarding param_1 to the code at 0xA0083C2C**

Single-instruction-sequence trampoline (5 insns: load literal, BLX/BX, return). It forwards its one argument (param_1, passed through in r0) to the function at 0xA0083C2D (0xA0000000-based alias of the flash/ROM image, Thumb bit set) via an indirect call and returns whatever that routine does (decompiler shows void). The target is a hard-coded constant in the 0xA0000000 window, so this is a link-time/ROM-patch jump stub into the Bestechnic code region rather than ordinary application logic. The purpose of the target is not recoverable from this stub alone; it is called from the BT controller code region near 0x0c07c000-0x0c07d700 (1 direct caller).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C07D840
- Called by: `bt_ld_acl_clk_offset_update_patch`
- Confidence: medium

## ble_hwtimer_guard_restart

**Restart the BLE guard hwtimer DAT_2000BD14 with a 9000-unit timeout, marking busy bit 31**

Marks busy-mask bit 31 (DAT_2000AA6C) with pm_busy_mask_set_bit(31), then stops hwtimer DAT_2000BD14 with hwtimer_stop. It converts (bes_hw_get_const_4000() + 500) * 2 = 9000 through ble_ram_patch_thunk_200005a8, keeps that value in DAT_2000BD20 and restarts the same hwtimer with it through hwtimer_start. It takes no arguments and has no direct callers in this packet.

**Notes:** The meaning of busy bit 31 and of the 9000-unit timeout is inferred. The thunk 0x200005A8 returns a tick-count value.

- Addresses by version: 219: 0x0C03AC44
- Calls: `pm_busy_mask_set_bit`, `bes_hw_get_const_4000`, `hwtimer_start`, `hwtimer_stop`, `ble_ram_patch_thunk_200005a8`
- Confidence: medium

## ble_ram_call_2000110c_arg0

**Call the RAM-resident function at 0x2000110c with argument 0**

Thunk that calls the fixed SRAM address 0x2000110d (0x2000110c with the Thumb bit) with r0 = 0 and returns. Targets code copied or patched into RAM (ROM-patch table), so the actual behaviour is not visible here. Called from ble_219_0c02cca8 and ble_219_0c0459fc.

**Notes:** Target function identity unknown.

- Addresses by version: 219: 0x0C045AC0
- Called by: `ble_factory_test_dispatch_query`, `ble_boot_notice_log`
- Confidence: medium

## ble_ram_patch_thunk_20000220

**Thunk forwarding param_1 to the code at 0x20000220**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000221 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 10 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073B50
- Called by: `ble_rf_analog_init`, `ble_rf_radio_init`, `bt_drv_rf_bringup`, `bt_drv_vendor_ctrl_init_cmds`, `bt_drv_rom_patch_init`, `bt_drv_reg_op_addr_table_init`, `bt_ctrl_crash_dump`, `bt_drv_digital_assert_check`, `bt_drv_analog_init_20f2_variant`, `bt_drv_rf_analog_bringup`
- Confidence: medium

## ble_ram_patch_thunk_2000022c

**Thunk forwarding param_1 to the code at 0x2000022C**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x2000022D (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 8 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073C50
- Called by: `hal_spi_build_hw_cfg`, `bes_clk_measure_hz`, `hal_uart_set_baud_divisor`, `ble_rf_synth_retune`, `ble_rf_synth_set_freq_ratio`, `ble_rf_osc_trim_calibrate`, `ble_analog_chip_init`, `hal_i2c_open_internal`
- Confidence: medium

## ble_ram_patch_thunk_20000238

**Thunk forwarding param_1 to the code at 0x20000238**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000239 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 2 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073B60
- Called by: `bes_clk_measure_hz`, `ble_rf_osc_trim_calibrate`
- Confidence: medium

## ble_ram_patch_thunk_20000244

**Thunk forwarding param_1 to the code at 0x20000244**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000245 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 4 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073C40
- Called by: `bes_iomux_reg0c_set_level`, `hal_pinmux_apply_table`, `bes_iomux_init_level2`, `ble_pin_config_record_apply`
- Confidence: medium

## ble_ram_patch_thunk_2000025c

**Thunk forwarding param_1 to the code at 0x2000025C**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x2000025D (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 4 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073BA0
- Called by: `bes_iomux_reg0c_set_level`, `hal_pinmux_apply_table`, `bes_iomux_init_level2`, `ble_pin_config_record_apply`
- Confidence: medium

## ble_ram_patch_thunk_200002cc

**Thunk forwarding param_1 to the code at 0x200002CC**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x200002CD (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 1 direct caller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073BE0
- Called by: `bes_clk_measure_hz`
- Confidence: medium

## ble_ram_patch_thunk_2000031c

**Thunk forwarding param_1 to the code at 0x2000031c**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x2000031d (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early RAM-code area, i.e. a routine copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection), so flash code reaches it through this fixed entry point. Behaviour is defined by the RAM target, not by the stub; 7 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073B30
- Called by: `hal_i2c_master_send_poll`, `hal_i2c_master_recv_poll`, `hsm_trng_read_bytes`, `bt_drv_reg_op_write_6byte_param`, `bt_drv_reg_op_set_timing_params`, `bt_rfcal_dc_iq_sweep_all_bands`, `hal_cmu_pll_enable`
- Confidence: medium

## ble_ram_patch_thunk_20000328

**Thunk forwarding param_1 to the code at 0x20000328**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000329 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 1 direct caller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073B70
- Called by: `rtos_run_time_counter_get`
- Confidence: medium

## ble_ram_patch_thunk_20000334

**Thunk forwarding param_1 to the code at 0x20000334**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000335 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; at least 12 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073CC0
- Called by: `hal_gpdma_stop`, `hal_block_40008000_set_run`, `ble_analog_cal_0x4059_trigger`, `ble_rf_synth_load_ratio48`, `ble_rf_mode_switch`, `ble_rf_front_end_start`, `ble_analog_chip_init`, `ble_ctrl_dump_region`, `bt_drv_hci_cmd_send_wait`, `bt_drv_rf_gain_ratio_rescale`, `bt_drv_rf_bringup`, `bt_drv_hci_evt_conn_state_hook` ...
- Confidence: medium

## ble_ram_patch_thunk_20000348

**Thunk forwarding param_1 to the code at 0x20000348**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000349 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early RAM-code area, i.e. a routine copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection), so flash code reaches it through this fixed entry point. Behaviour is defined by the RAM target, not by the stub; 8 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073AE0
- Called by: `hal_gpdma_stop`, `hal_analogif_chan_start`, `ble_analog_cal_0x4059_ramp`, `ble_rf_power_ramp_step`, `ble_rf_mode_switch`, `ble_rf_front_end_start`, `ble_rf_block4_enable`, `hal_cmu_pll_enable`
- Confidence: medium

## ble_ram_patch_thunk_20000534

**Thunk forwarding param_1 to the code at 0x20000534**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000535 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 1 direct caller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073C90
- Called by: `ble_soc_bringup_sequence`
- Confidence: medium

## ble_ram_patch_thunk_20000554

**Thunk forwarding param_1 to the code at 0x20000554**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000555 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 3 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073BC0
- Called by: `vPortSetupTimerInterrupt`, `rtos_systick_sub_tick_ns`, `systick_measure_loop_us`
- Confidence: medium

## ble_ram_patch_thunk_20000570

**Thunk forwarding param_1 to the code at 0x20000570**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000571 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; at least 12 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073CB0
- Called by: `hal_gpdma_stop`, `hal_i2c_master_send_poll`, `hal_i2c_master_recv_poll`, `hal_block_40008000_set_run`, `hal_block_40008000_open`, `hsm_trng_read_bytes`, `hal_wdt_set_reload_slot`, `ble_analog_cal_0x4059_trigger`, `ble_rf_mode_switch`, `ble_rf_front_end_start`, `ble_ctrl_dump_region`, `bt_drv_hci_cmd_send_wait` ...
- Confidence: medium

## ble_ram_patch_thunk_200005a8

**Thunk forwarding param_1 to the code at 0x200005A8**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x200005A9 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 8 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073C20
- Called by: `ble_rf_synth_load_ratio48`, `ble_analog_chip_init`, `ble_hwtimer_guard_restart`, `bt_rfcal_measure_residual_fmt14`, `bt_rfcal_measure_residual_fmt16`, `hal_cmu_pll_enable`, `hal_cmu_osc_x2_enable`, `hal_cmu_clk_block_8c_enable`
- Confidence: medium

## ble_ram_patch_thunk_200005e8

**Thunk forwarding param_1 to the code at 0x200005e8**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x200005e9 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early RAM-code area, i.e. a routine copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection), so flash code reaches it through this fixed entry point. Behaviour is defined by the RAM target, not by the stub; 1 direct caller (0x0c03f1f4).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073AD0
- Called by: `bt_rfcal_dc_iq_sweep_all_bands`
- Confidence: medium

## ble_ram_patch_thunk_20000650

**Thunk forwarding param_1 to the code at 0x20000650**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000651 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 1 direct caller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073C00
- Called by: `ble_rf_radio_init`
- Confidence: medium

## ble_ram_patch_thunk_2000065c

**Thunk forwarding param_1 to the code at 0x2000065c**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x2000065d (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early RAM-code area, i.e. a routine copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection), so flash code reaches it through this fixed entry point. Behaviour is defined by the RAM target, not by the stub; 1 direct caller (0x0c03a038).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073B00
- Called by: `ble_analog_chip_init`
- Confidence: medium

## ble_ram_patch_thunk_2000067c

**Thunk forwarding param_1 to the code at 0x2000067C**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x2000067D (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 8 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073C80
- Called by: `ble_rf_irq_setup`, `bes_otp_load_variant`, `ble_analog_chip_init`, `bes_calib_get_trim_pair`, `ble_rf_radio_init`, `bt_drv_rf_tx_power_trim_apply`, `bt_drv_rf_0x2018_from_cfg_mode`, `bt_drv_rf_0x208f_field_from_cfg`
- Confidence: medium

## ble_ram_patch_thunk_20000738

**Thunk forwarding param_1 to the code at 0x20000738**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000739 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 2 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073B80
- Called by: `bes_cmu_request_sysclk`, `ble_rf_osc_trim_calibrate`
- Confidence: medium

## ble_ram_patch_thunk_200007a8

**Thunk forwarding param_1 to the code at 0x200007A8**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x200007A9 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 1 direct caller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073C70
- Called by: `ble_analog_chip_init`
- Confidence: medium

## ble_ram_patch_thunk_200007f4

**Thunk forwarding param_1 to the code at 0x200007f4**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x200007f5 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early RAM-code area, i.e. a routine copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection), so flash code reaches it through this fixed entry point. Behaviour is defined by the RAM target, not by the stub; 3 direct callers (0x0c0328cc, 0x0c032954, 0x0c0460e8).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073AF0
- Called by: `hal_spi_bus1_transfer`, `hal_spi_dma_rx_start`, `ble_spi_read_locked`
- Confidence: medium

## ble_ram_patch_thunk_2000081c

**Thunk forwarding param_1 to the code at 0x2000081C**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x2000081D (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 7 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073BB0
- Called by: `hal_spi_dma_cancel_all`, `hal_spi_close_user`, `hal_spi_dma_rx_done_handler`, `hal_spi_dma_tx_done_handler`, `hal_spi_bus1_transfer`, `hal_spi_dma_rx_start`, `ble_spi_read_locked`
- Confidence: medium

## ble_ram_patch_thunk_20000934

**Thunk forwarding param_1 to the code at 0x20000934**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000935 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early RAM-code area, i.e. a routine copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection), so flash code reaches it through this fixed entry point. Behaviour is defined by the RAM target, not by the stub; 3 direct callers (0x0c032c04, 0x0c032d18, 0x0c032d34).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073B40
- Called by: `bes_cmu_request_sysclk`, `bes_cmu_get_sysclk_request`, `bes_cmu_get_sysclk_effective`
- Confidence: medium

## ble_ram_patch_thunk_20000f34

**Thunk forwarding param_1 to the code at 0x20000F34**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000F35 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 1 direct caller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073BF0
- Called by: `app_get_unique_id16`
- Confidence: medium

## ble_ram_patch_thunk_2000106c

**Thunk forwarding param_1 to the code at 0x2000106C**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x2000106D (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 1 direct caller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073B90
- Called by: `ble_soc_bringup_sequence`
- Confidence: medium

## ble_ram_patch_thunk_200010a0

**Thunk forwarding param_1 to the code at 0x200010A0**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x200010A1 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 1 direct caller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073CA0
- Called by: `ble_soc_bringup_sequence`
- Confidence: medium

## ble_ram_patch_thunk_20001c10

**Thunk forwarding param_1 to the code at 0x20001c10**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20001c11 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early RAM-code area, i.e. a routine copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection), so flash code reaches it through this fixed entry point. Behaviour is defined by the RAM target, not by the stub; no direct caller (used via function pointer).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073B10
- Confidence: medium

## ble_ram_patch_thunk_20001ca0

**Thunk forwarding param_1 to the code at 0x20001ca0**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20001ca1 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early RAM-code area, i.e. a routine copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection), so flash code reaches it through this fixed entry point. Behaviour is defined by the RAM target, not by the stub; no direct caller (used via function pointer).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073B20
- Confidence: medium

## ble_ram_patch_thunk_20001d38

**Thunk forwarding param_1 to the code at 0x20001D38**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20001D39 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 1 direct caller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073BD0
- Called by: `flash_region_0x18000_io_cb`
- Confidence: medium

## ble_ram_patch_thunk_20001d7c

**Thunk forwarding param_1 to the code at 0x20001D7C**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20001D7D (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; no direct callers (likely invoked through a function pointer/table).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073C10
- Confidence: medium

## bt_ctrl_crash_dump

**Log the BT controller crash record: ROM and patch versions, fault and stack registers, BT errors**

Prints the BT controller crash report. When the nesting counter DAT_2000BD58 is zero it holds the BT core with bes_sysreg_write_04_bit19. It prints the ROM metal id and patch version from DAT_2000BDF4, then the commit id and patch date for metal id 0, 1 or other (three fixed string records). It prints the saved registers R0-R8, SL, FP, IP, SP and the SP+0 to SP+64 words, then PSP, MSP and the Cortex-M fault registers CFSR, BFAR, HFSR, ICSR, AIRCR, SCR, CCR, SHCSR, AFSR and MMFAR. The snapshot is read from words at 0xC0004050 to 0xC00040FC, with a different offset layout for chip variant 0 and 1 than for 2 and up. It then prints the BT error registers 0xD0220460, 0xD0220860 and 0xD0220428, 0xD0330050, 0xD0330054, 0xD03300A0, 0xD03300A4, 0x400000A0, 0x400000A4 and the controller RAM base. With a non-zero argument it dumps controller RAM and the 0xD0210000 block through ble_ctrl_dump_region. It ends with 'BT crash dump complete!', decrements DAT_2000BD58 and releases the hold with bes_sysreg_write_08_bit19 when the counter reaches zero.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero also dumps controller RAM (DAT_2000BD88, 0x10000 bytes) and the block at 0xD0210000 (0x10000 bytes) |

**Notes:** The choice of layout by the variant thunk 0x0C073B50 is inferred from the comparisons; the two layouts are not documented here.

- Addresses by version: 219: 0x0C03D69C
- Peripheral registers: `0x40000000` (A), `0x400000a0` (R), `0x400000a4` (R)
- Called by: `bt_ctrl_crash_dump_irq_safe`, `ble_bts_task_periodic_check`
- Calls: `hal_wdt_stop`, `trace_printf`, `ble_ctrl_dump_region`, `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`, `ble_ram_patch_thunk_20000220`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: high

## bt_ctrl_crash_dump_irq_safe

**Run the BT crash dump with IRQs masked and memory barriers around it**

Wrapper that masks interrupts with disableIRQinterrupts, runs DSB and ISB, calls bt_ctrl_crash_dump, and then re-enables interrupts with DSB and ISB. No caller is visible in this image, so it is probably reached from a fault or assert hook through a pointer.

**Notes:** It calls bt_ctrl_crash_dump with no argument. The RAM-dump flag therefore comes from whatever value is in r0 at entry, so the RAM dump may not run here.

- Addresses by version: 219: 0x0C03DD80
- Calls: `bt_ctrl_crash_dump`
- Confidence: high

## bt_drv_analog_init_20f2_variant

**On the variant path, clear analog 0x20F2 and 0x20F3 and set 0x20F4 to 0x7C**

Calls the RAM routine at 0x20000220 as a flag test. When the result is nonzero it writes 0 to analog registers 0x20F2 and 0x20F3 and 0x7C to 0x20F4 through hal_analogif_reg_write. Otherwise it returns without touching the registers. It is called from 0x0C03BB70, which is outside this packet.

**Notes:** The flag at 0x20000220 is also tested by bt_drv_vendor_ctrl_init_cmds and bt_drv_rf_analog_bringup, so it is a chip or variant selector. Its exact meaning is not established.

- Addresses by version: 219: 0x0C03E49C
- Called by: `bt_drv_rf_bringup`
- Calls: `hal_analogif_reg_write`, `ble_ram_patch_thunk_20000220`
- Confidence: medium

## bt_drv_analog_reg200f_set_1

**Write value 1 to analog register 0x200F**

Writes the constant 1 to analog register 0x200F through hal_analogif_reg_write. That is also the first register in the list that bt_drv_rf_dc_iq_cal_run saves and programs. It is called from 0x0C03C070, which is outside this packet.

- Addresses by version: 219: 0x0C03E490
- Called by: `bt_drv_rf_2168_cal_search`
- Calls: `hal_analogif_reg_write`
- Confidence: high

## bt_drv_ctrl_bringup

**BT controller bring-up sequence A: link init, callback, RF regset, vendor FC77 and FC81**

Controller bring-up, always returns 0. It runs bt_drv_intersys_link_init_once, stores the Thumb callback address 0x0C0468B5 with bt_drv_set_global_2000bd1c, calls thunk_FUN_0c03dd9c and bt_drv_reg_op_env_bde4_set_byte18(0), then bt_drv_hci_cmd_post_settle, bt_drv_rf_regset_mode0_select, bt_drv_vendor_fc77_set_value(0) and bt_drv_vendor_fc81_cmd. It ends with an empty stub. Its caller ble_219_0c0592a4 is the controller state machine, which is not described here.

**Returns** `u32`: always 0

**Notes:** The same opening sequence is shared with bt_drv_ctrl_bringup_rf_test. The target of thunk_FUN_0c03dd9c is not named in the call graph.

- Addresses by version: 219: 0x0C04696C
- Called by: `ble_host_start`
- Calls: `stub_empty_0c03aa3c`, `bt_drv_set_global_2000bd1c`, `bt_drv_intersys_link_init_once`, `bt_drv_rf_regset_mode0_select`, `bt_drv_hci_cmd_post_settle`, `bt_drv_vendor_fc77_set_value`, `bt_drv_vendor_fc81_cmd`, `bt_drv_reg_op_env_bde4_clear_flags_thunk`, `bt_drv_reg_op_env_bde4_set_byte18`
- Confidence: medium

## bt_drv_ctrl_param_load_all

**Load the controller RSSI, timing and table parameters and set the RF mode field**

Loads the controller parameter set in a fixed order. If DAT_2000BDB4 is nonzero it writes the 6-byte constant at 0x0C07691C; it then loads the three RSSI tables (bt_drv_reg_op_load_rssi_table_a, _b and _c), the 8-byte table at 0x20003EAC (bt_drv_reg_op_load_table8_bdd4), the RSSI monitor block (bt_drv_reg_op_set_rssi_monitor_params) and the slot-timing block (bt_drv_reg_op_set_timing_params). It sets RF field 14:13 to 1 through the thunk at 0x0C03BE88. Finally, when the register-access guard DAT_2000BD58 is zero it toggles the sysreg gate (0x0C0413F0 on, 0x0C041430 off), and in both paths it sets byte +0x28 of the structure at DAT_2000BDF8 to 1 when that pointer is set.

**Notes:** The order follows the decompile. The configuration meaning of the 0xD0220C7C field is not known.

- Addresses by version: 219: 0x0C03E314
- Called by: `bt_drv_rf_bringup`
- Calls: `bes_rf_set_mode_bits`, `bt_drv_reg_op_write_6byte_param`, `bt_drv_reg_op_set_timing_params`, `bt_drv_reg_op_set_rssi_monitor_params`, `bt_drv_reg_op_load_rssi_table_a`, `bt_drv_reg_op_load_rssi_table_b`, `bt_drv_reg_op_load_rssi_table_c`, `bt_drv_reg_op_load_table8_bdd4`, `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_digital_assert_check

**Check BT digital error status and the crash-record word; log and return 1 on assert**

Reads IP_ERRORTYPESTAT at 0xD0220460 and ignores bit 6. If any other bit is set it logs 'BT_DRV:digital assert,error code=0x%x' and returns 1. Otherwise it reads the crash-record word at 0xC0004050 or 0xC0004060 (selected by chip variant) and reports an assert when that word is non-zero and not 0x42. It keeps the same nesting counter DAT_2000BD58 as bt_ctrl_crash_dump and uses the same bes_sysreg_write_04_bit19 and bes_sysreg_write_08_bit19 hold-and-release pair.

**Returns** `s32`: 0 when no digital assert is latched, 1 when one is reported

**Notes:** The 0x42 expected value and the variant selection are read from the comparisons only.

- Addresses by version: 219: 0x0C03DF24
- Called by: `ble_bts_task_periodic_check`
- Calls: `trace_printf`, `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`, `ble_ram_patch_thunk_20000220`
- Confidence: medium

## bt_drv_hci_cmd_complete_info_rx

**Command Complete hook that copies a 16-byte vendor response into RAM at 0x2000BD38**

Runs with the IPC RX interrupt for channel 0 disabled (0x0C031848(0) before the work and 0x0C031808(0) after it). If the packet is an HCI event (indicator 0x04) with event code 0x0E (Command Complete), parameter length 0x12 and a nonzero halfword at offset 7, it copies 16 bytes from offset 7 into RAM at 0x2000BD38 through ble_mem_copy and sets DAT_2000BD33 = 1. It returns its second argument in every case, so it works as a pass-through filter in the host event path.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | H4 event packet |
| `param_2` | `u32` | value passed through unchanged |

**Returns** `u32`: Returns param_2 in every case.

**Notes:** Reached indirectly as a callback, so there are no direct callers. The meaning of the 16-byte response is not known.

- Addresses by version: 219: 0x0C03BFBC
- Calls: `hal_isr_chan_disable`, `hal_sysipc_rx_irq_disable`, `ble_mem_copy`
- Confidence: medium

## bt_drv_hci_cmd_post_settle

**Send the fixed 4-byte HCI packet at 0x0C076914 and wait 350 units**

Sends the four-byte packet stored at ROM 0x0C076914 through bt_drv_hci_cmd_send_wait and then waits 350 delay units (0x15E) with the RAM delay pair, which gives the controller time to apply it. It is a fixed step in controller sequencing: the pending-action poll at 0x0C03C034 calls it, and so do routines at 0x0C0469xx and 0x0C046Cxx.

**Notes:** The packet contents are not visible in this packet, so the opcode is not identified.

- Addresses by version: 219: 0x0C03BD70
- Called by: `bt_drv_pending_action_poll`, `bt_drv_ctrl_bringup`, `app_testmode_bt_nonsig_tx`, `ble_vendor_fc87_send_keyed`, `ble_hci_le_tx_test_cmd`, `ble_hci_le_rx_test_cmd`, `ble_hci_le_enh_tx_test_cmd`, `ble_hci_le_enh_rx_test_cmd`, `bt_drv_ctrl_bringup_rf_test`
- Calls: `bt_drv_hci_cmd_send_wait`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## bt_drv_hci_cmd_send_wait

**Send an HCI packet to the BT core and poll a reply flag with a timeout**

Sends the HCI packet at param_1 (param_2 bytes) to the BT controller core and is the common send path for the vendor command group (bt_drv_hci_vendor_cmd_send, bt_drv_hci_cmd_post_settle, the event hooks). While the controller-running flag DAT_2000BD06 is clear it hands the buffer to bt_drv_intersys_send_saved_iface, waits one 50-unit delay and returns without waiting for a reply. Once the flag is set it clears DAT_20003EA4, queues the packet with hal_sysipc_send(channel 0, type 0) and polls every 50 delay units for up to 201 iterations until DAT_20003EA4 or the ready flag DAT_2000BD18 becomes nonzero. It returns no status, so a timeout is silent and the caller continues.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | HCI packet buffer, H4 indicator byte first |
| `param_2` | `u32` | packet length in bytes |

**Notes:** Who sets DAT_20003EA4 is outside this packet. The 201-iteration bound is the literal 0xC9 in the decompile.

- Addresses by version: 219: 0x0C03AC98
- Called by: `bt_drv_hci_evt_conn_state_hook`, `bt_drv_hci_cmd_post_settle`, `bt_drv_hci_vendor_cmd_send`, `bt_drv_rfcal_timer_run`, `app_testmode_bt_nonsig_tx`, `ble_vendor_fc87_send_keyed`, `ble_vendor_fc87_send_test_pattern`, `ble_hci_le_tx_test_cmd`, `ble_hci_le_rx_test_cmd`, `ble_hci_le_enh_tx_test_cmd`, `ble_hci_le_enh_rx_test_cmd`, `ble_hci_le_test_end_cmd` ...
- Calls: `hal_sysipc_send`, `bt_drv_intersys_send_saved_iface`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## bt_drv_hci_evt_conn_state_hook

**HCI event hook for Connection Complete and Disconnection Complete state changes**

Callback for incoming HCI event packets that does nothing unless the ready flag DAT_2000BD18 is nonzero. For a Connection Complete event (indicator 0x04, event 0x03, length 11, status 0) it sends the 5-byte buffer at 0x0C076924 through bt_drv_hci_cmd_send_wait, waits 20 units and sets DAT_20003EA8 = 1. For a Disconnection Complete event (event 0x05, length 4, status 0) it sends the buffer at 0x0C07692C, waits 20 units, sets DAT_2000BD18 = 1 and sets DAT_20003EA8 = 2. Other events are ignored, so this is a small two-state connection tracker in the host-side event path.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | H4 event packet: indicator, event code, parameter length, status |

**Notes:** Reached only indirectly as a callback, so there are no direct callers. The length of the 0x0C07692C send is not visible in this decompile; another packet (wave4_batch05) passes 5 for the same buffer.

- Addresses by version: 219: 0x0C03BCCC
- Calls: `bt_drv_hci_cmd_send_wait`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## bt_drv_hci_vendor_cmd_send

**Build an H4 HCI command from opcode, length and parameters, then send it**

Builds a command in a 256-byte stack buffer: byte 0 is 0x01 (H4 command indicator), bytes 1 and 2 are the opcode, byte 3 is the parameter length, and the parameters are copied from param_3 with newlib memcpy when the length is nonzero. It then calls bt_drv_hci_cmd_send_wait with length param_2 + 4. The opcodes used across the vendor group are BES vendor commands in the 0xFCxx range: 0xFC71, 0xFC77, 0xFC81 and 0xFCC3.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | HCI opcode, sent little-endian |
| `param_2` | `u8` | parameter length in bytes |
| `param_3` | `ptr` | parameter block, copied only when the length is nonzero |

- Addresses by version: 219: 0x0C03BE50
- Called by: `bt_drv_vendor_ctrl_init_cmds`, `bt_drv_vendor_fc77_set_value`, `bt_drv_vendor_fc81_cmd`
- Calls: `bt_drv_hci_cmd_send_wait`, `memcpy`
- Confidence: high

## bt_drv_intersys_link_init_once

**One-time BT-core link setup: set the controller-running flag and register callbacks**

Runs its body only once: while DAT_2000BD06 is zero it sets the flag to 1 and registers two callbacks (code labels at 0x0C03BD44 and 0x0C03ABB0) through 0x0C0315D8(0, 0, cb_a, cb_b, 0). If that registration returns 0 it calls 0x0C031808, which is probably the IRQ-enable counterpart of hal_sysipc_rx_irq_disable. Later calls do nothing. DAT_2000BD06 is the flag that bt_drv_hci_cmd_send_wait tests to choose between the intersys and IPC send paths.

**Notes:** 0x0C0315D8 and 0x0C031808 are not described yet. The meaning of the two callbacks is open.

- Addresses by version: 219: 0x0C03ACF0
- Called by: `bt_drv_ctrl_bringup`, `bt_drv_ctrl_bringup_rf_test`
- Calls: `hal_isr_chan_register`, `hal_isr_chan_disable`
- Confidence: medium

## bt_drv_intersys_send_saved_iface

**Send a buffer to the BT core over the intersys link using the interface id saved in DAT_2000be2e, type 0**

Forwards to the intersys transmit routine 0x0c031884(iface = DAT_2000be2e, type = 0, data = param_1, len = param_2); that routine queues the message on the per-interface list and raises the MCU-to-BT-core interrupt via 0x400000A0 (bit 2 for interface 0, bit 3 for interface 1). Used by the HCI command sender 0x0c03ac98 when the controller is not yet marked as running (DAT_2000bd06 == 0), followed by a 50-unit delay instead of waiting for a reply.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | data buffer (HCI command packet) |
| `param_2` | `u32` | length in bytes |

**Notes:** DAT_2000be2e is read as a byte/halfword; its initialisation was not seen.

- Addresses by version: 219: 0x0C03EB84
- Called by: `bt_drv_hci_cmd_send_wait`
- Calls: `hal_sysipc_send`
- Confidence: medium

## bt_drv_pending_action_poll

**Service two pending flags: resend the 350-unit HCI step and call 0x0C044D90**

Periodic poll for two pending actions. If DAT_2000BD32 is set it runs bt_drv_hci_cmd_post_settle, waits 200 delay units and clears the flag. If DAT_2000BD34 is nonzero it calls 0x0C044D90 with DAT_2000BD34, 3, 0, 0 and 0. It is called from 0x0C03C070, which is outside this packet.

**Notes:** 0x0C044D90 is not described yet, so the action behind DAT_2000BD34 is open.

- Addresses by version: 219: 0x0C03C034
- Called by: `bt_drv_rf_2168_cal_search`
- Calls: `bt_drv_hci_cmd_post_settle`, `xTimerGenericCommand`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## bt_drv_reg_op_addr_table_init

**Fill the table of BT-controller RAM addresses (0xC000xxxx) used by the bt_drv_reg_op accessors, per metal id**

Sets DAT_2000bd88 = 0xC0000000 (controller RAM base as seen by the MCU) and, depending on the metal id returned by ble_ram_patch_thunk_20000220 (0, 1, other), stores about 40 absolute controller RAM addresses into the pointer block DAT_2000bd4c..DAT_2000be08. These pointers address RivieraWaves/BES environment structures inside the BT core's RAM and are dereferenced by the accessor functions in 0x0c03dd9c..0x0c03e314: e.g. DAT_2000bd68 = per-ACL-link env pointer array (RSSI read), DAT_2000bdb4 = 6-byte parameter location, DAT_2000bdc8 = RSSI/monitor parameter block, DAT_2000bde8 and DAT_2000bd74 = timing parameter blocks, DAT_2000bdec/bdfc/bdf0 = 30-byte RSSI tables, DAT_2000bdd4 = 8-byte table, DAT_2000bdac/DAT_2000be00 = patch-RAM variables (0xC000C8F4/0xC000C8F0 on id 0). Some entries only exist for certain ids (DAT_2000bdb8, DAT_2000bda0 only for id 1; DAT_2000bd78..bd84 and be08 only for ids 1 and >1), the others stay 0 so the accessors fall back to no-ops. Called first thing in the controller start-up routine 0x0c03bb70. Equivalent of the BES SDK bt_drv_reg_op global address initialisation.

**Notes:** Individual structure identities (ld_acl_env, lm_env, rwip_env ...) are inferred only from how the accessors use them.

- Addresses by version: 219: 0x0C03D088
- Called by: `bt_drv_rf_bringup`
- Calls: `ble_ram_patch_thunk_20000220`
- Confidence: high

## bt_drv_reg_op_env_bde4_clear_flags

**Zero byte 0 and byte 0x36 of the controller RAM structure at DAT_2000bde4 under the register-access guard**

If the nesting counter DAT_2000bd58 is 0 it enables controller register access with bes_sysreg_write_04_bit19 (BES BT_DRV_REG_OP_CLK_ENB equivalent), then, if DAT_2000bde4 is non-NULL (0xC0007800 / 0xC0008444 / 0xC0009144 per metal id), writes 0 to offset 0 and offset 0x36 of that structure; finally, if the counter is still 0, it releases access with bes_sysreg_write_08_bit19. Reached through the 1-instruction thunk bt_drv_reg_op_env_bde4_clear_flags_thunk from the factory/RF test entry sequences. Group: bt_drv_reg_op controller-RAM accessors (shared enable/disable pattern around DAT_2000bd58).

**Notes:** Structure identity unknown.

- Addresses by version: 219: 0x0C03DD9C
- Called by: `bt_drv_reg_op_env_bde4_clear_flags_thunk`
- Calls: `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_env_bde4_clear_flags_thunk

**Thunk (1 insn) to bt_drv_reg_op_env_bde4_clear_flags**

Single branch to 0x0c03dd9c; the decompiler inlines the target: under the controller register-access guard (enable via bes_sysreg_write_04_bit19 when nesting counter DAT_2000bd58 is 0, disable via bes_sysreg_write_08_bit19 afterwards) it zeroes byte 0 and byte 0x36 of the controller RAM structure pointed to by DAT_2000bde4 (0xC0007800 / 0xC0008444 / 0xC0009144 per metal id). Called from the two factory/RF test entry sequences 0x0c04696c and 0x0c046c7c right before bt_drv_reg_op_env_bde4_set_byte18(0).

**Notes:** Identity of the structure at DAT_2000bde4 unknown (some controller environment, flags cleared when entering test mode).

- Addresses by version: 219: 0x0C03D028
- Called by: `bt_drv_ctrl_bringup`, `bt_drv_ctrl_bringup_rf_test`
- Calls: `bt_drv_reg_op_env_bde4_clear_flags`
- Confidence: medium

## bt_drv_reg_op_env_bde4_set_byte18

**Store a byte at offset 0x18 of the controller RAM structure DAT_2000bde4 under the register-access guard**

If DAT_2000bd58 == 0 enables controller register access (bes_sysreg_write_04_bit19); if DAT_2000bde4 is non-NULL writes param_1 to byte +0x18 of that structure; if the counter is 0 releases access (bes_sysreg_write_08_bit19). Both factory/RF test entry sequences (0x0c04696c, 0x0c046c7c) call it with 0 immediately after bt_drv_reg_op_env_bde4_clear_flags_thunk. Group: bt_drv_reg_op controller-RAM accessors.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | value stored at +0x18 (0 from both callers) |

**Notes:** Field meaning unknown; probably disables some controller feature for test mode.

- Addresses by version: 219: 0x0C03DE58
- Called by: `bt_drv_ctrl_bringup`, `bt_drv_ctrl_bringup_rf_test`
- Calls: `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_get_patch_var_bdac

**Read the 32-bit controller RAM variable pointed to by DAT_2000bdac (0 if unavailable)**

Under the register-access guard (enable when DAT_2000bd58 == 0, release afterwards) returns *DAT_2000bdac, or 0 when the pointer is NULL. The pointer is 0xC000C8F4 for metal id 0 and 0xC000C4D8 for id 1 and is not set for other ids; these addresses lie in the patch-code area of controller RAM, so the value is a variable maintained by the ROM patches. No direct callers (probably used through a table or by debug/test code). Group: bt_drv_reg_op controller-RAM accessors.

**Returns** `u32`: value of the patch variable, 0 if no pointer

**Notes:** Semantic of the variable unknown.

- Addresses by version: 219: 0x0C03E1B8
- Calls: `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_load_rssi_table_a

**Copy the 30-byte table at 0x0c07fdc0 into the controller RAM location DAT_2000bdec**

Under the register-access guard (enable when DAT_2000bd58 == 0, counter incremented around the copy, release when it returns to 0) copies 0x1E bytes from flash 0x0c07fdc0 to the controller RAM address in DAT_2000bdec (0xC00043C4 / 0xC00043D0 / 0xC00043C4 per metal id) using the memcpy wrapper 0x0c03aa40; does nothing if the pointer is 0. The table is A5 A5 A8 A8 AE AE B2 B2 B8 B8 D1 D1 E2 E2 EC followed by 15 x 7F: as signed bytes -91,-91,-88,-88,-82,-82,-78,-78,-72,-72,-47,-47,-30,-30,-20 and 0x7F fillers, i.e. an ascending list of RSSI thresholds in dBm (per RX gain step). One of three sibling loaders (tables a/b/c at 0x0c07fdc0/0x0c07fde0/0x0c07fda0) called in sequence from the controller configuration routine 0x0c03e314.

**Notes:** Interpretation as an RX gain / RSSI threshold table is inferred from the values; which link type (BT/BLE) each of the three tables serves is unknown.

- Addresses by version: 219: 0x0C03E078
- Called by: `bt_drv_ctrl_param_load_all`
- Calls: `ble_mem_copy`, `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_load_rssi_table_b

**Copy the 30-byte table at 0x0c07fde0 into the controller RAM location DAT_2000bdfc**

Same guarded copy as bt_drv_reg_op_load_rssi_table_a, but from flash 0x0c07fde0 to the controller RAM address in DAT_2000bdfc (0xC00043E4 / 0xC00043F0 / 0xC00043E4 per metal id). The table is AC AC AE AE B3 B3 B6 B6 BF BF D7 D7 E8 E8 EC + 15 x 7F, i.e. -84,-84,-82,-82,-77,-77,-74,-74,-65,-65,-41,-41,-24,-24,-20 dBm thresholds with 0x7F fillers. Called from 0x0c03e314 between the a and c loaders.

**Notes:** See bt_drv_reg_op_load_rssi_table_a.

- Addresses by version: 219: 0x0C03E0C8
- Called by: `bt_drv_ctrl_param_load_all`
- Calls: `ble_mem_copy`, `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_load_rssi_table_c

**Copy the 30-byte table at 0x0c07fda0 into the controller RAM location DAT_2000bdf0**

Same guarded copy as bt_drv_reg_op_load_rssi_table_a, but from flash 0x0c07fda0 to the controller RAM address in DAT_2000bdf0 (0xC00043A4 / 0xC00043B0 / 0xC00043A4 per metal id). The table is AB AB AE AE B7 B7 BB BB C1 C1 D8 D8 E9 E9 EA + 15 x 7F, i.e. -85,-85,-82,-82,-73,-73,-69,-69,-63,-63,-40,-40,-23,-23,-22 dBm thresholds with 0x7F fillers. Called from 0x0c03e314.

**Notes:** See bt_drv_reg_op_load_rssi_table_a.

- Addresses by version: 219: 0x0C03E118
- Called by: `bt_drv_ctrl_param_load_all`
- Calls: `ble_mem_copy`, `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_load_table8_bdd4

**Copy the 8-byte RAM table at 0x20003EAC into the controller RAM location DAT_2000bdd4**

Under the register-access guard copies 8 bytes from the .data variable at 0x20003EAC (initial contents FC 00 03 07 0B 10 10 10, loaded from flash 0x0c089afc) to the controller RAM address in DAT_2000bdd4 (0xC0004324 / 0xC0004330 / 0xC0004324 per metal id) via the memcpy wrapper 0x0c03aa40; no-op when the pointer is 0. Because the source lives in RAM it can be modified at run time (e.g. by a factory/NV setting) before the controller is configured. Called from the controller configuration routine 0x0c03e314 after the three RSSI table loaders.

**Notes:** Table meaning unknown (values 0xFC,0,3,7,11,16,16,16 look like a small monotonically increasing index/gain table).

- Addresses by version: 219: 0x0C03E168
- Called by: `bt_drv_ctrl_param_load_all`
- Calls: `ble_mem_copy`, `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_read_acl_rssi

**Return the signed RSSI byte (+0x152) of the BT ACL link environment for a connection handle**

Under the register-access guard looks up the per-link environment pointer array at DAT_2000bd68 (0xC00057FC / 0xC000579C / 0xC0006480 per metal id), indexed by (param_1 - 0x80) * 4 (ACL connection handles start at 0x80, so this converts handle to link id), and if both the array pointer and the entry are non-NULL returns the sign-extended byte at offset 0x152 of the link structure; otherwise 0. Callers treat the result as a dBm value: the factory test command 0x2B samples it seven times and prints it, and 0x0c05a06c accumulates negative results into an RSSI sum/count pair for link-quality statistics. Companion of bt_drv_reg_op_read_ble_rssi.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | ACL connection handle (0x80 + link id) |

**Returns** `s32`: RSSI in dBm (sign-extended s8), 0 if not available

**Notes:** No bounds check on the link id. Equivalent of BES bt_drv_reg_op_read_rssi_in_dbm; the field offset 0x152 inside ld_acl_env is not verified.

- Addresses by version: 219: 0x0C03E264
- Called by: `ble_factory_test_dispatch_query`, `ble_rssi_sample_poll`
- Calls: `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_read_ble_rssi

**Return the signed byte at +9 of the 12-byte BLE RX-monitor entry for a BLE link index**

Under the register-access guard reads the table pointed to by DAT_2000bdb8 (only set for metal id 1: 0xC000C3A8, so 0 is returned on other chips) and returns the sign-extended byte at param_1 * 12 + 9; 0 if the table pointer is NULL. The caller 0x0c05a06c uses the result exactly like bt_drv_reg_op_read_acl_rssi (negative values accumulated into an RSSI sum/count for the BLE link), so this is the BLE per-connection RSSI readout. Companion of bt_drv_reg_op_read_acl_rssi.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | BLE link / activity index |

**Returns** `s32`: RSSI in dBm (sign-extended s8), 0 if not available

**Notes:** Table identity (12-byte entries) inferred; equivalent of BES bt_drv_reg_op_read_ble_rssi_in_dbm.

- Addresses by version: 219: 0x0C03E2C0
- Called by: `ble_rssi_sample_poll`
- Calls: `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_set_patch_var_be00

**Write a 32-bit value to the controller RAM variable pointed to by DAT_2000be00**

Under the register-access guard stores param_1 to *DAT_2000be00 when that pointer is non-NULL (0xC000C8F0 for metal id 0, 0xC000C4D4 for id 1, unset otherwise). The controller start-up routine 0x0c03bb70 calls it with 1 only when the metal id is below 2, right after the controller configuration, so it acts as an enable flag for a feature implemented by the ROM patches. Group: bt_drv_reg_op controller-RAM accessors.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value written (1 from the only caller) |

**Notes:** Which patch feature the flag enables is unknown.

- Addresses by version: 219: 0x0C03E1F0
- Called by: `bt_drv_rf_bringup`
- Calls: `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_set_rssi_monitor_params

**Fill the controller RAM parameter block DAT_2000bdc8 with RSSI thresholds (-100/-90 dBm) and window counts**

Under the register-access guard writes 22 fields into the structure at DAT_2000bdc8 (0xC00078CC / 0xC000851C / 0xC0009230 per metal id), skipped if the pointer is 0: u8 +0 = 1 (enable), u32 +4 = 80, u32 +8 = 100, u32 +0xC = 5, u32 +0x10 = 0x160 (352), u8 +0x14/+0x15/+0x24 = 3, u8 +0x16/+0x17/+0x25 = 0x9C (-100), u8 +0x18/+0x26 = 0, u32 +0x1C = 80, u32 +0x20 = 100, u8 +0x27/+0x2D = 0xA6 (-90), u16 +0x28 = 80, u16 +0x2A = 200, u8 +0x2C = 1, u16 +0x2E = 20, u16 +0x30 = 800. The repeated -100/-90 bytes look like signed dBm thresholds and the 80/100/200/352/800 values like sample windows or counters. Called from the controller configuration sequence 0x0c03e314. Group: bt_drv_reg_op controller-RAM accessors.

**Notes:** Possibly the AFH channel-assessment or RX AGC/RSSI monitor environment; exact structure unknown.

- Addresses by version: 219: 0x0C03DE90
- Called by: `bt_drv_ctrl_param_load_all`
- Calls: `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_set_timing_params

**Write slot-timing constants (1250, 625, 500 us, 400, 12, 20) into two controller RAM parameter blocks**

Under the register-access guard (bes_sysreg_write_04_bit19 / bes_sysreg_write_08_bit19 around DAT_2000bd58 == 0) it writes into the structure at DAT_2000bde8 (0xC0007874 / 0xC00084C4 / 0xC00091D8): u32 +0x1C = 0x4E2 (1250), u32 +0x20 = 0, u8 +0x24 = 12, u16 +0x26 = 0x271 (625), u32 +0x28 = 0x01F40271 (u16 625 and u16 500), u8 +0x2C = 1; and into the structure at DAT_2000bd74 (0xC0007770 / 0xC00083B4 / 0xC00090CC): u16 +4 = 400, u8 +6 = 0x14 (20). Both writes are skipped when the respective pointer is 0. The routine timestamps itself with ble_ram_patch_thunk_2000031c before and after and hands the difference to the RAM routine at 0x2000061C. Called from the controller configuration sequence 0x0c03e314. Group: bt_drv_reg_op controller-RAM accessors.

**Notes:** 625/1250 are BT slot / double-slot durations in microseconds, so this looks like sleep/wake-up or scheduling timing (rwip/lld environment); exact field names unknown.

- Addresses by version: 219: 0x0C03DDD8
- Called by: `bt_drv_reg_op_write_6byte_param`, `bt_drv_ctrl_param_load_all`
- Calls: `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`, `ble_ram_patch_thunk_2000031c`
- Confidence: medium

## bt_drv_reg_op_write_6byte_param

**Copy a 6-byte constant (u32 + u16) into the controller RAM location DAT_2000bdb4 and report the elapsed time**

Takes a timestamp via ble_ram_patch_thunk_2000031c, then under the register-access guard (bes_sysreg_write_04_bit19 when DAT_2000bd58 == 0, bes_sysreg_write_08_bit19 at the end) writes *param_1 (u32) and *(u16*)(param_1+4) to the controller RAM address held in DAT_2000bdb4 (0xC0004284 / 0xC0004290 / 0xC00042A4 by metal id). Finally it takes a second timestamp and passes the difference to the RAM-resident routine at 0x2000061C (a timing/trace hook). The only caller, the controller configuration routine 0x0c03e314, passes the flash constant at 0x0c07691c = 28 04 20 03 90 01 (u16 view: 0x0428=1064, 0x0320=800, 0x0190=400). Group: bt_drv_reg_op controller-RAM accessors.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 6-byte source (u32 followed by u16) |

**Notes:** Whether the 6 bytes are a BD address or three u16 parameters (400 and 800 also appear in the timing / RSSI parameter writers) is not known.

- Addresses by version: 219: 0x0C03D02C
- Called by: `bt_drv_ctrl_param_load_all`
- Calls: `bt_drv_reg_op_set_timing_params`, `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`, `ble_ram_patch_thunk_2000031c`
- Confidence: medium

## bt_drv_rf_0x2018_from_cfg_mode

**Set the low 6 bits of analog 0x2018 from a 2-bit mode in calibration record 0x0C**

Reads calibration record 0x0C through the RAM routine at 0x2000067C and forms a 2-bit mode from bit 0 and bit 6 of the record. Mode 2 sets the low 6 bits of analog 0x2018 to 0x26, mode 3 sets them to 0x3F, mode 1 sets them to 0x18, and any other mode uses 0x12. The upper bits are kept. It is a step of bt_drv_rf_analog_bringup.

**Notes:** The calibration record index and the meaning of the mode are not established.

- Addresses by version: 219: 0x0C03E8F0
- Called by: `bt_drv_rf_analog_bringup`
- Calls: `hal_analogif_reg_read`, `hal_analogif_reg_write`, `ble_ram_patch_thunk_2000067c`
- Confidence: medium

## bt_drv_rf_0x2058_fields_remap

**Remap two 7-bit fields of analog 0x2058 into 0x202E and set bits 13:11 of 0x202D**

Sets bit 0 of analog 0x20C4 and puts RF word 0xD0220C00 into test state 0x000A0028 (channel 40) with a 1-unit delay. It splits analog 0x2058 into a low 7-bit field and a 7-bit field at bits 13:7. Field values 0x75 to 0x7F are scaled as value * 0.8 + 0.5 (truncated) and other values are kept. The two results go into 0x202E, bits 13:11 of 0x202D are set, bit 0 of 0x20C4 is cleared and the RF word is restored.

**Notes:** The meaning of the 0x2058 fields and the 0.8 scale are not known, so the purpose is a guess. The second read of 0x2058 is discarded. The 0x20C4 bit and the 0x202D and 0x202E registers are not identified.

- Addresses by version: 219: 0x0C03E66C
- Called by: `bt_drv_rf_analog_bringup`
- Calls: `hal_analogif_reg_read`, `hal_analogif_reg_write`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: low

## bt_drv_rf_0x208f_field_from_cfg

**Copy bits 11:9 of calibration record 0x0C into analog 0x208F bits 6:4**

Reads calibration record 0x0C through the RAM routine at 0x2000067C. If bits 11:9 of the record are all zero it returns without a write. Otherwise it replaces bits 6:4 of analog register 0x208F with the 3-bit value of bits 11:9 and keeps the other bits. It runs only on the variant path of bt_drv_rf_analog_bringup.

- Addresses by version: 219: 0x0C03E9AC
- Called by: `bt_drv_rf_analog_bringup`
- Calls: `hal_analogif_reg_read`, `hal_analogif_reg_write`, `ble_ram_patch_thunk_2000067c`
- Confidence: medium

## bt_drv_rf_2168_cal_search

**Closed-loop search that tunes the 9-bit field of analog 0x2168 until the RF cal error is zero**

Drives the RF calibration search. It clears the sample history at 0x2000BD2C (6 bytes), sets analog 0x200F to 1 (bt_drv_analog_reg200f_set_1), starts one run with bt_drv_rfcal_timer_run(1), and waits up to 17 times 500 units for DAT_2000BD33 to flag a finished sample. Each sample gives a signed error in DAT_2000BD3E, and the current 9-bit field is read back through lm_get_state_9bit. The first trial step is 2 units; later steps are sized from the slope of the last two samples (scaled by 500). Each trial is written with bt_drv_rf_2168_field9_set. A small error (under about 3 units) reached a second time ends the search, which returns 0 when fewer than five trials were used and -1 otherwise. Timeouts, sample timeouts and a budget of about ten steps return -1. Every exit calls bt_drv_pending_action_poll and stores the final value through param_1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | receives the final 16-bit field value on every exit |

**Returns** `s32`: 0 when the error converges within the step budget, -1 on timeout or budget exhaustion

**Notes:** The sample flags and error values are produced by the RF calibration event path, which is outside this packet. Calling the search a bisection or secant method is an inference from the step logic.

- Addresses by version: 219: 0x0C03C070
- Calls: `ble_mem_fill`, `bt_drv_rfcal_timer_run`, `bt_drv_pending_action_poll`, `bt_drv_rf_2168_field9_set`, `lm_get_state_9bit`, `bt_drv_analog_reg200f_set_1`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## bt_drv_rf_2168_field9_set

**Set the 9-bit field of analog register 0x2168 and refresh its shadow**

Replaces bits 8:0 of the cached word DAT_20003EC0 with param_1 & 0x1FF and keeps bits 15:9. It writes the cached word to analog register 0x2168 and copies it to the shadow DAT_20003EBE. The other 0x2168 writers in the RF group (bt_drv_rf_2168_update_from_src) use the same cache.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | new value; bits 8:0 used |

- Addresses by version: 219: 0x0C03E454
- Called by: `ble_factory_test_dispatch_set`, `bt_drv_rf_2168_cal_search`
- Calls: `hal_analogif_reg_write`
- Confidence: high

## bt_drv_rf_2168_update_from_src

**Update the 9-bit field of analog 0x2168 from an external measurement or a fallback value**

When DAT_2000BE0C is zero it reads a status from 0x0C045F04 and, if that equals 1 and 0x0C045E04(&value) returns 0, sets the 9-bit field to value & 0x1FF and waits one unit. When the status check fails it uses the constant 0x7F. When DAT_2000BE0C is nonzero it uses DAT_2000BE0E & 0x1FF instead. Every path writes analog register 0x2168 and copies the cached word to DAT_20003EBE.

**Notes:** 0x0C045E04 and 0x0C045F04 are not described yet, so the source of the value is open.

- Addresses by version: 219: 0x0C03E5DC
- Called by: `bt_drv_rf_analog_bringup`
- Calls: `hal_analogif_reg_write`, `ble_app_word_f360_read`, `ble_app_marker_s_check`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## bt_drv_rf_analog_bringup

**RF analog front-end bring-up: init tables, LUT registers, config record and register sets**

Full analog bring-up of the BT radio and the head of the RF group. It reads the variant flag from 0x20000220 and clears the low nibble of analog 0x20E9 (with a 1-unit delay), writes 0x2002 = 0x1717, then runs the ROM list at 0x0C083BE8 of 6-byte records (register at +6, value at +8, optional 1-unit delay flag at +10), each preceded by a dummy read. It writes 0x208F = 0x9F52, or 0x9F42 with a delay and bt_drv_rf_0x208f_field_from_cfg on the variant path, and calls bt_drv_rf_0x2018_from_cfg_mode. It then clears the config record at 0x2000BE0C-0x2000BE20 and calls lm_env_defaults_init, bt_drv_rf_apply_cfg_record, bt_drv_rf_0x2058_fields_remap and bt_drv_rf_2168_update_from_src. Next it sets bit 3 and then bits 4 and 5 of analog 0x227D, runs the ROM list at 0x0C083AA8 (starting with 0x027D = 0x0378), and calls bt_drv_rf_regset_capture and bt_drv_rf_regset_select with mode 0.

**Returns** `u32`: Always 0.

**Notes:** The contents of the two ROM lists are not visible here. The variant flag decides the 0x208F value and the extra step.

- Addresses by version: 219: 0x0C03E9FC
- Called by: `bt_drv_rf_bringup`
- Calls: `lm_env_defaults_init`, `bt_drv_rf_apply_cfg_record`, `bt_drv_rf_2168_update_from_src`, `bt_drv_rf_0x2058_fields_remap`, `bt_drv_rf_regset_capture`, `bt_drv_rf_regset_select`, `bt_drv_rf_0x2018_from_cfg_mode`, `bt_drv_rf_0x208f_field_from_cfg`, `hal_analogif_reg_read`, `hal_analogif_reg_write`, `ble_ram_patch_thunk_20000220`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## bt_drv_rf_apply_cfg_record

**Apply the RAM config record at 0x2000BE0C-0x2000BE20 to the RF lookup registers**

Spins forever if DAT_2000BE0D is zero, which means the record is not initialised. Otherwise it passes seven record bytes to bt_drv_rf_reg_lo6_from_lut for indices 0 to 6 (analog registers 0x2049 to 0x204F, values from 0x2000BE1F, BE1D, BE1B, BE19, BE17, BE15 and BE12) and six bytes to bt_drv_rf_reg_mid6_from_lut for indices 0 to 5 (bits 11:6 of the same registers, values from 0x2000BE20, BE1E, BE1C, BE1A, BE18 and BE16). It is the apply step at the end of the RF bring-up group.

**Notes:** The record is filled by lm_env_defaults_init and cleared by bt_drv_rf_analog_bringup. DAT_2000BE0D is nonzero after lm_env_defaults_init.

- Addresses by version: 219: 0x0C03E51C
- Called by: `bt_drv_rf_analog_bringup`
- Calls: `bt_drv_rf_reg_lo6_from_lut`, `bt_drv_rf_reg_mid6_from_lut`
- Confidence: medium

## bt_drv_rf_apply_config

**Program the BT RF/analog registers 0xD0220Cxx and 0xD0350xxx from a ~0x27-byte config struct**

Applies a packed RF configuration structure to the undocumented BT transceiver block. With a NULL pointer it only sets bit 17 of 0xD0220C8C and returns. Otherwise: bes_analog_set_c10_field(cfg[0], cfg[1]); cfg[4] goes to bit 0 of 0xD0220C8C and selects the upper halfword of 0xD0220C0C (0x2837 if cfg[4]==0, else 0x2827); cfg[6] (0/1/other) clears bit 28 of 0xD0220C8C, sets it, or leaves it; bes_rf_synth_config_by_mode() is called; cfg[7] drives bit 31 of 0xD0220C90 and, when set together with non-zero u32 fields at +8/+0xC and cfg[6]==1, loads 0xD0220CC4 = cfg+0xC and 0xD0220CC8 = cfg+8 (otherwise 0xD0220CC8 is rewritten with its old value or cfg+0xC); cfg[5] & 0x7F goes to field [30:24] of 0xD0220C90; cfg[0x10]==0 clears bit 24 of 0xD0350228 and writes cfg[0x12] to field [7:4] of 0xD0350368, else writes cfg[0x11] & 0x7F to field [22:16] of 0xD0350228 and sets bit 24; cfg[0x14] -> bit 16 of 0xD0220C18; cfg[0x15] -> bit 14 of 0xD0220C80 plus 0xD0220C40/C44 = u32 at +0x18/+0x1C and 0xD0220C48 |= u32 at +0x20; cfg[0x24] -> bit 24 of 0xD0220C18 and field [30:24] of 0xD0220C90 = 0x66; cfg[0x25] -> clear bit 25 of 0xD0220C18 or call bes_analog_clock_mode_config(cfg[0x26]). Finally bit 17 of 0xD0220C8C is set (looks like a 'config done/latch' bit). Part of the RF bring-up group with bt_drv_rf_pre_init and bt_drv_rf_init, which builds the struct (bytes 01 04 | 00 0A 01 00 | 0 | 0 | 00 40 01 00 | 01 00 | 0 | 0 | 0 | 00 00 03).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | RF config struct (bytes/words at the offsets listed), or NULL |

**Notes:** 0xD0220Cxx is the BT RF transceiver bank (0xD0220C00 low 7 bits = channel index in the VCO test and the DC calibration); the meaning of the individual fields is not documented.

- Addresses by version: 219: 0x0C03C4BC
- Called by: `bt_drv_rf_init`
- Calls: `bes_analog_clock_mode_config`, `bes_rf_synth_config_by_mode`, `bes_analog_set_c10_field`
- Confidence: medium

## bt_drv_rf_bringup

**BT RF bring-up: clock level 4, RF init and calibration chain, ISR channel and IPC setup**

Runs the BT RF bring-up with system clock user 4 held at level 4 and released at the end. It calls the RF chain bt_drv_reg_op_addr_table_init, ble_rf_block4_enable(1), bt_drv_rf_init, bt_drv_rf_analog_bringup, bt_drv_rf_tx_power_trim_apply, bt_drv_rf_dc_iq_cal_run, bt_drv_rf_gain_ratio_rescale and bes_periph_d033_config, with a 10-unit wait after the early setup. On its first call it registers an ISR channel with hal_isr_chan_register(0, 0, handler, handler, 0), using handlers at 0x0C03BD44 and 0x0C03ABB0, and disables it with hal_isr_chan_disable when registration succeeds. It then loads the vendor controller init commands and parameter records. If the chip variant (thunk 0x0C073B50) is below 2 it sets the patch variable (bt_drv_reg_op_set_patch_var_be00), allocates two pool nodes with rtos_pool_node_alloc_init and enables IPC channel 1 (hal_sysipc_rx_irq_setup). If this call registered the ISR channel it closes it with hal_sysipc_close(0).

**Notes:** The handlers at 0x0C03BD44, 0x0C03ABB0, 0x0C03ABBC, 0x0C03AC45 and 0x0C03ABC4 are not described in this packet.

- Addresses by version: 219: 0x0C03BB70
- Called by: `ble_ctrl_sysreg_pulse_bit19`, `ble_host_start`
- Calls: `hal_isr_chan_register`, `hal_sysipc_close`, `hal_isr_chan_disable`, `hal_sysipc_rx_irq_setup`, `bes_cmu_request_sysclk`, `ble_rf_block4_enable`, `stub_empty_0c03aa60`, `hal_ext_ctrl_write_d0702000`, `bt_drv_rf_gain_ratio_rescale`, `bt_drv_rf_dc_iq_cal_run`, `bt_drv_rf_tx_power_trim_apply`, `bes_periph_d033_config`, `bt_drv_vendor_ctrl_init_cmds`, `bt_drv_rf_init`, `bt_drv_rom_patch_init`, `bt_drv_reg_op_addr_table_init` ...
- Confidence: medium

## bt_drv_rf_dc_iq_cal_run

**Run the RF DC/IQ calibration sweep inside a save and restore of RF and analog state**

Saves 11 analog registers (address list in ROM at 0x0C0768F8, first entry 0x200F) and nine RF or controller words (0xD0350334, 0xD0350248, 0xD035002C, 0xD0350028, 0xD0340020, 0xD0330058, 0xD0330060, 0xD0330064, 0xD0220C00). It then writes the ROM list at 0x0C0768A4 (its first entry sets 0x200F = 0x0030), loads 0xD0340020 = 0x030E01C0, 0xD0350028 = 0x013F0012, 0xD035002C = 3 and 0xD0220C00 = 0x800A0027 (test word for channel 39), sets bit 23 of 0xD0350334 and clears bit 31 of 0xD0350250. It runs bt_rfcal_dc_iq_sweep_all_bands and then restores everything it saved, so it is the wrapper that makes the sweep safe to run from the controller init path.

**Notes:** The purpose of the individual register writes is inferred from the calibration context. Bit 31 of 0xD0350250 is cleared here and set again by the sweep itself.

- Addresses by version: 219: 0x0C03B8D4
- Called by: `bt_drv_rf_bringup`
- Calls: `bt_rfcal_dc_iq_sweep_all_bands`, `hal_analogif_reg_read`, `hal_analogif_reg_write`
- Confidence: medium

## bt_drv_rf_gain_ratio_rescale

**Rescale about 30 analog gain bit-fields by a power ratio read from register 0x2144**

Saves analog registers 0x20B8 and 0x2172 and RF word 0xD0220C00, then puts the radio in a test state (0xD0220C00 = 0x000A0080, 0x20B8 = 0x7C00, bits 4 and 5 of 0x2172 set, with delays of 1 to 10 units). It reads the 16-bit power word at 0x2144 and only when bit 15 is set takes its low 14 bits divided by 8257.0 as a ratio, falling back to 1.0 for some range and FP-status cases. Each analog bit-field in about 23 registers from 0x2027 to 0x213C is read, divided by the ratio, rounded and clamped to nonnegative, then written back. The saved registers are restored at the end, so the routine is a self-contained gain-compensation step in the same RF group as bt_drv_rf_analog_bringup.

**Notes:** The 8257.0 scale, the field layout and the meaning of the 0x2144 word are not confirmed, so the purpose is a guess from the code shape. The final write to 0x213C overwrites the ratio variable but nothing reads it afterwards. If bit 15 of the word is clear, no field is changed.

- Addresses by version: 219: 0x0C03AD44
- Called by: `bt_drv_rf_bringup`
- Calls: `hal_analogif_reg_read`, `hal_analogif_reg_write`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: low

## bt_drv_rf_init

**BT RF bring-up sequence: pre-init, 0xD0350xxx main init, analog defaults, then apply the built-in RF config**

Calls bt_drv_rf_pre_init, bes_periph_d035_init_main and bes_analog_init_defaults, then fills a 0x28-byte RF configuration struct on the stack and passes it to bt_drv_rf_apply_config. The struct contents are: bytes 0..1 = 0x01,0x04 (c10 field enable, value 4); word +4 = 0x00010A00 (cfg[4]=0, cfg[5]=0x0A, cfg[6]=1, cfg[7]=0); words +8/+0xC = 0; word +0x10 = 0x00014000 (cfg[0x10]=0, cfg[0x11]=0x40, cfg[0x12]=1); halfword +0x14 = 1 (cfg[0x14]=1, cfg[0x15]=0); +0x18..+0x23 = 0; halfword +0x24 = 0; cfg[0x26] = 3 (clock mode 3). Called from the controller start-up routine 0x0c03bb70 after the ROM patches have been installed. Group: RF bring-up (bt_drv_rf_pre_init / bt_drv_rf_apply_config).

**Notes:** Equivalent of BES btdrv_rf_init; register semantics undocumented.

- Addresses by version: 219: 0x0C03CDFC
- Called by: `bt_drv_rf_bringup`
- Calls: `bt_drv_rf_apply_config`, `bes_analog_init_defaults`, `bt_drv_rf_pre_init`, `bes_periph_d035_init_main`
- Confidence: medium

## bt_drv_rf_pre_init

**First step of RF bring-up: clear/set a few 0xD0220Cxx bits, init 0xD0350xxx, write 0xCAFE0001 to 0x40080020**

Clears bits [22:21] of 0xD0220C04, sets field [6:0] of 0xD0220C14 to 6, sets bit 3 of 0xD03300A0 and bit 30 of 0xD0220C38, then calls bes_periph_d035_init_small. After that call it stores the magic word 0xCAFE0001 (loaded into r0 before the call and evidently preserved by the callee) into 0x40080020, sets bit 28 of 0xD0220C18 (the decompiler shows this as base-in-r1 + 0xC18, i.e. the 0xD0220000 base left over from the callee) and finally sets bit 9 of 0x400800E8. Called first in bt_drv_rf_init, before bes_periph_d035_init_main and bes_analog_init_defaults.

**Notes:** The 0xCAFE0001 / 0x40080020 write and the bit-28 write rely on register contents surviving the call to 0x0c03c87c; the decompiler output is confused here, so verify against the disassembly. 0x40080000 is the same AON/CMU-like block whose bit-19 enable/disable registers guard controller register access.

- Addresses by version: 219: 0x0C03C930
- Peripheral registers: `0x40080020` (W), `0x400800e8` (RW)
- Called by: `bt_drv_rf_init`
- Calls: `bes_periph_d035_init_small`
- Confidence: medium

## bt_drv_rf_reg_lo6_from_lut

**Write the table code for a float setting into bits 5:0 of analog register 0x2049+index**

Converts param_2 to float and searches an 8-byte-record table at ROM 0x0C0857F0 for it, returning the 16-bit code of the matching record (zero when nothing matches). The scan starts from the key 16.0 and runs until 0x0C085888. It then replaces bits 5:0 of analog register (0x2049 + param_1) with that code by read-modify-write and keeps the other bits. It is the low-field half of the RF lookup helpers together with bt_drv_rf_reg_mid6_from_lut and bt_drv_rf_apply_cfg_record.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | field index; analog register is 0x2049 + index |
| `param_2` | `s32` | setting, converted to float before the lookup |

**Notes:** Table layout is inferred from the scan loop: the float at +8 of each record is the key that selects the record after it, and the last matching record wins. The meaning of the setting is not known.

- Addresses by version: 219: 0x0C03E388
- Called by: `bt_drv_rf_apply_cfg_record`
- Calls: `hal_analogif_reg_read`, `hal_analogif_reg_write`
- Confidence: medium

## bt_drv_rf_reg_mid6_from_lut

**Write the table code for a float setting into bits 11:6 of analog register 0x2049+index**

For param_1 below 6 it runs the same lookup as bt_drv_rf_reg_lo6_from_lut on param_2 and writes the 16-bit code into bits 11:6 of analog register (0x2049 + param_1), keeping the other bits. For param_1 of 6 or more it enters an endless loop and never returns. It is the mid-field companion of bt_drv_rf_reg_lo6_from_lut.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | field index, 0..5 valid |
| `param_2` | `s32` | setting, converted to float before the lookup |

**Notes:** The endless loop is a trap for an out-of-range index, not a delay.

- Addresses by version: 219: 0x0C03E3E8
- Called by: `bt_drv_rf_apply_cfg_record`
- Calls: `hal_analogif_reg_read`, `hal_analogif_reg_write`
- Confidence: medium

## bt_drv_rf_regset_capture

**Save the two analog register sets used by bt_drv_rf_regset_select**

Reads analog 0x221D, 0x221E, 0x2220 and 0x2221 into RAM words DAT_2000BE22, DAT_2000BE24, DAT_2000BE28 and DAT_2000BE2A, and reads 0x2235 twice, storing its low byte in DAT_2000BE26 and its high byte in DAT_2000BE2C. Set 0 therefore holds (BE22, BE24, BE26) and set 1 holds (BE28, BE2A, BE2C). bt_drv_rf_regset_select writes those values back to 0x221D, 0x221E and the low byte of 0x2235.

- Addresses by version: 219: 0x0C03E7D0
- Called by: `bt_drv_rf_analog_bringup`
- Calls: `hal_analogif_reg_read`
- Confidence: medium

## bt_drv_rf_regset_mode0_select

**Call the RF register-set selector with mode 0**

Wrapper that calls bt_drv_rf_regset_select with a single argument of 0 (the decompile shows no second argument). Its callers 0x0C04696C and 0x0C046C7C are controller state-machine paths outside this packet.

**Notes:** The set index is the second argument of bt_drv_rf_regset_select, which the decompile does not show here, so the set actually selected is not confirmed.

- Addresses by version: 219: 0x0C03BC74
- Called by: `bt_drv_ctrl_bringup`, `bt_drv_ctrl_bringup_rf_test`
- Calls: `bt_drv_rf_regset_select`
- Confidence: medium

## bt_drv_rf_regset_select

**Switch analog 0x221D, 0x221E and the low byte of 0x2235 to saved set 0 or 1**

Returns at once if the requested index equals the current index held in DAT_20003EBC. Otherwise it stores the index and, with mode 0, writes the saved 0x221D and 0x221E values for that set and merges the saved byte into the low byte of 0x2235. Set 0 uses BE22, BE24 and BE26, set 1 uses BE28, BE2A and BE2C (see bt_drv_rf_regset_capture). An index other than 0 or 1 returns without writing.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | mode gate: must be 0, any other value spins forever |
| `param_2` | `u32` | register set index, 0 or 1 |

**Notes:** Both callers in this packet (0x0C03BC74 and 0x0C03E9FC) pass only one argument, so the set index they select is not visible in the decompile. The index is stored before the mode check.

- Addresses by version: 219: 0x0C03E844
- Called by: `bt_drv_rf_regset_mode0_select`, `bt_drv_rf_analog_bringup`
- Calls: `hal_analogif_reg_read`, `hal_analogif_reg_write`
- Confidence: medium

## bt_drv_rf_set_reg_c7c_bits13_14

**Write a 2-bit value into field [14:13] of RF register 0xD0220C7C under the register-access guard**

If DAT_2000bd58 == 0 enables controller register access with bes_sysreg_write_04_bit19, does a read-modify-write of 0xD0220C7C setting bits [14:13] = param_1 (the value is shifted by 13 without masking), and releases access with bes_sysreg_write_08_bit19 if the counter is 0. The controller configuration sequence 0x0c03e314 calls it with 1 through the 1-instruction thunk 0x0c03be88. Part of the 0xD0220Cxx RF register group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 2-bit field value (1 from the only caller) |

**Notes:** Field meaning unknown.

- Addresses by version: 219: 0x0C03E034
- Called by: `bes_rf_set_mode_bits`
- Calls: `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_rf_tx_power_trim_apply

**Apply the signed TX power trim from calibration record 7 to power and gain registers**

Reads calibration record 7 through the RAM routine at 0x2000067C into a 16-bit value and decodes three 3-bit sign-magnitude fields at bits 2:0, 6:4 and 10:8, where a set sign bit (3, 7 or 11) means positive. If bit 12 is set the result is the average of the three fields divided by 3, otherwise it is the first field alone, rounded half away from zero. A positive result is subtracted from five 6-bit power fields (the first in 0xD0350308, the rest at addresses listed in ROM at 0x0C0768D0). A negative result instead adds 1 + 2*|v| to the 5-bit gain index in bits 8:4 of analog register 0x20CC, and zero changes nothing.

**Notes:** The meaning of calibration record 7 and the names of the power registers are not known. The sign convention comes from the bit tests: a clear sign bit negates the field.

- Addresses by version: 219: 0x0C03BA38
- Called by: `bt_drv_rf_bringup`
- Calls: `hal_analogif_reg_read`, `hal_analogif_reg_write`, `ble_ram_patch_thunk_2000067c`
- Confidence: medium

## bt_drv_rfcal_timer_run

**Create the rfcal timer on first use, then start it or run one RF calibration cycle**

Creates the 'rfcal_timer' FreeRTOS software timer on first use (period 0x5DC ticks, no auto-reload, callback = this function). The start path, taken when param_1 is 0 and DAT_2000BD48 is clear, sets DAT_2000BD48 and sends a 32-byte vendor HCI command (packet bytes 01 87 FC 1C, opcode 0xFC87) through bt_drv_hci_cmd_send_wait, changes the timer period to 300 ticks and starts it at the current tick. The calibration path clears DAT_2000BD48, sends an HCI Reset (bytes 01 03 0C 00) and the same vendor command with different parameters, ORs 0x55 into the low byte of register 0xD0210100 and clears its upper 24 bits, and sets the period to 0x5DC and restarts the timer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | 0 starts the timer when no run is pending; non-zero runs one calibration cycle (this function is also the timer callback) |

**Notes:** The opcodes are read from the packet bytes and are consistent with HCI Reset (0x0C03) and a BES vendor command (0xFC87). The timer callback argument is inferred.

- Addresses by version: 219: 0x0C03BE8C
- Called by: `bt_drv_rf_2168_cal_search`
- Calls: `trace_printf`, `bt_drv_hci_cmd_send_wait`, `xTaskGetTickCount`, `xTimerCreate`, `xTimerGenericCommand`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## bt_drv_rom_patch_apply_table

**Install a BT-controller ROM patch table: copy data into BT RAM, then program 64 hardware patch slots**

param_1 points to a patch table (selected per metal id by bt_drv_rom_patch_init). Layout: 64 records of 3 words {type, rom_site, value} at +0; word +0x300 = number of copy records, word +0x304 = number of memset records, copy records {dst, src, len_flags} from +0x308, memset records {dst, len} after them. Phase 1 (copy records): if bit 31 of len_flags is clear, memcpy_newlib_aligned_16(dst, table + src, len) copies a blob from the table into controller RAM (0xC000xxxx as seen by the MCU); if bit 31 is set the record is an immediate of 1, 2 or 4 bytes (3 or >4 traps in an endless loop) and the src word itself is memcpy'd to dst (used e.g. to install function pointers such as 0xC0009511 at 0xC00045A4). Phase 2: memset(dst, 0, len) for each memset record. Phase 3: walks the 64 slot records and the hardware patch unit at 0xA01FFE00 (address slots) / 0xA01FFF00 (data slots), 4 bytes per slot, stopping at 0xA0200000. type 1 = code patch: address slot = (rom_site | 1) + 0x60000000 (i.e. the ROM offset with the Thumb bit) and data slot = thumb2_encode_b_w(rom_site & ~1, (value & ~1) + 0xE0200000), a B.W from the ROM site to the replacement routine in BT RAM (0xC000xxxx MCU view == 0xA02xxxxx BT-core view); type 2 = data patch: data slot = value verbatim (e.g. 0xBF00BF00 = two NOPs), address slot as above; type 0 = slot skipped. param_2 (table size) is not used. Group: ROM patching (bt_drv_rom_patch_init, thumb2_encode_b_w).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | patch table in flash (0x0c078270 / 0x0c07ba80 / 0x0c07e0b4) |
| `param_2` | `u32` | table size in bytes (unused) |
| `param_3` | `u32` | unused (decompiler artifact) |
| `param_4` | `u32` | unused (decompiler artifact) |

**Notes:** Table A (0x0c078270, 0x3810 bytes) has 8 copy + 1 memset records; table B (0x0c07ba80) 6 + 1; table C (0x0c07e0b4) 3 + 1.

- Addresses by version: 219: 0x0C03CEC8
- Called by: `bt_drv_rom_patch_init`
- Calls: `memcpy_newlib_aligned_16`, `thumb2_encode_b_w`, `memcpy`, `memset`
- Confidence: high

## bt_drv_rom_patch_init

**Select the ROM patch table by controller metal id, apply it and enable the patch unit (bit 31 of 0xA01FFE00)**

Reads the BT controller metal id through ble_ram_patch_thunk_20000220 (the same call steers bt_drv_reg_op_addr_table_init) and calls bt_drv_rom_patch_apply_table with table 0x0c078270 (0x3810 bytes) for id 0, 0x0c07ba80 (0x2634 bytes) for id 1, or 0x0c07e0b4 (0xFAC bytes) for any other id. Afterwards it sets bit 31 of 0xA01FFE00, the global enable of the hardware ROM patch unit. Called from the controller start-up sequence 0x0c03bb70 after a 10-unit delay (string 'BT rom: 1306: metal id=%d,patch version=%08x' elsewhere confirms the metal-id scheme).

- Addresses by version: 219: 0x0C03CFC0
- Called by: `bt_drv_rf_bringup`
- Calls: `bt_drv_rom_patch_apply_table`, `ble_ram_patch_thunk_20000220`
- Confidence: high

## bt_drv_vendor_ctrl_init_cmds

**Send the BES vendor controller-init commands 0xFC71, the 0xFCxx record table and 0xFCC3**

Controller init step made of vendor commands. It builds a 16-byte 0xFC71 block from bes_hw_get_const_4000 (three copies of 4000 + 200, then 0x0203, 4000, 1 and 0) and sends it through bt_drv_hci_vendor_cmd_send. It then walks a ROM table of 12-byte records (opcode at +2, parameter length at +4, parameter pointer at +8), sending each with a 20-unit delay. Last it sends opcode 0xFCC3 with a 37-byte block at 0x0C07F078, or a 40-byte block at 0x0C07F0A0 when the RAM routine at 0x20000220 returns nonzero, followed by a 1-unit delay.

**Notes:** As decompiled, the table loop exits after the first record because its end test compares the pointer with the start address, so only one record may be sent. That is possibly a decompiler artefact. The 4000 constant and the fields of the 0xFC71 block are not identified.

- Addresses by version: 219: 0x0C03CD58
- Called by: `bt_drv_rf_bringup`
- Calls: `bt_drv_hci_vendor_cmd_send`, `bes_hw_get_const_4000`, `ble_ram_patch_thunk_20000220`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## bt_drv_vendor_fc77_set_value

**Store a byte in DAT_20003EB4 and send vendor command 0xFC77 with an 8-byte block**

Stores param_1 in DAT_20003EB4, sends vendor opcode 0xFC77 with an 8-byte parameter block through bt_drv_hci_vendor_cmd_send, and waits one delay unit. It is one of the small vendor-setting writes called from the controller state machine (with bt_drv_vendor_fc81_cmd).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | value cached in DAT_20003EB4 |

**Notes:** The parameter block is not visible in the decompile, so it is whatever the caller left in the third argument register. Callers are 0x0C04696C and 0x0C046C7C.

- Addresses by version: 219: 0x0C03CE14
- Called by: `bt_drv_ctrl_bringup`, `bt_drv_ctrl_bringup_rf_test`
- Calls: `bt_drv_hci_vendor_cmd_send`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## bt_drv_vendor_fc81_cmd

**Send vendor command 0xFC81 with an 8-byte block and wait one unit**

Sends vendor opcode 0xFC81 with an 8-byte parameter block through bt_drv_hci_vendor_cmd_send, then waits one delay unit. It is the companion of bt_drv_vendor_fc77_set_value in the same controller state-machine callers.

**Notes:** The parameter block pointer is not visible in the decompile. Callers are 0x0C04696C and 0x0C046C7C.

- Addresses by version: 219: 0x0C03CE38
- Called by: `bt_drv_ctrl_bringup`, `bt_drv_ctrl_bringup_rf_test`
- Calls: `bt_drv_hci_vendor_cmd_send`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## bt_lc_link_setup_patch

**ROM patch: record a link's 6-byte address in the 9-byte-per-link table at 0xC0004FD0 and start the ROM link setup**

Handler patch taking a message/parameter block: byte 0 = link index, bytes 1..6 = a 6-byte value (BD address layout: u32 + u16), u16 at +7, data at +0xc. It fills entry link*9 of the table at 0xC0004FD0: u32 at +0 and u16 at +4 copied from the block, byte +6 = 7, byte +7 = 1. Then calls FUN_0c07de30(link, &entry) and FUN_0c07dad0(link, 1, addr_lo, addr_hi, 0, 0, u16 at +7, global DAT_c0004fc2, block+0xc) (ROM thunks to 0xA000E528 / 0xA0074C98) and finally jumps into ROM code at 0xA0039830 with the link index. Invoked from the trampoline ble_219_0c07cdd8. Belongs to the BES ROM-patch group of the BT controller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | parameter block: [0]=link index, [1..6]=address, [7..8]=u16, [0xc..]=payload |

**Notes:** Purpose of the 9-byte table and constants 7/1 is unknown; address 0xC0004FD0 is in the controller's RAM data area.

- Addresses by version: 219: 0x0C07C7B4
- Called by: `bt_patch_entry_0c07cdd8`
- Calls: `ble_flash_patch_thunk_a000e528`, `ble_flash_patch_thunk_a0074c98`
- Confidence: low

## bt_ld_acl_clk_offset_update_patch

**ROM patch: adjust an ACL link's clock offset and notify LC tasks of the new ACL/eSCO anchor phase**

RivieraWaves BT link-driver patch operating on the ACL link environment table at 0xC000579C (ld_acl_env[link_id], word per link). When param_6 is set it rebases the link's 28-bit clock offset (env+0xfc) by (env+0xa4 - param_4) & 0xfffffff (env+0xa4 holds the last anchor/sync clock, param_4 the new clock). If the link is in state 3 (env+0xd8) and either the global flag at FUN_0c07da60()+0x20 or env+0xd6 is clear, it allocates kernel message 0x650 (ke_msg_alloc thunk FUN_0c07d860, dest task (link_id<<8)|1, src 0xff, 2-byte payload), fills it with clk_off mod (2 * interval at env+0x104) and sends it (ke_msg_send thunk FUN_0c07de00); a zero interval triggers the assert hook FUN_0c07d840(0xc000c2aa, 0xa5). It then scans the two synchronous-link entries at 0xC00057B8 (ld_sco_env[2]) whose byte +0x5a equals link_id, rebases their 28-bit anchor (+0x40) the same way and sends message 0x651 with 4-byte payload {u8 from +0x5b, u16 anchor mod (2 * interval byte at +0x56)}. Part of the ld_acl/ld_sco patch group of the BES ROM Bluetooth controller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | ACL link index into ld_acl_env |
| `param_2` | `ptr` | forwarded to ke_msg_alloc (unused by the logic) |
| `param_3` | `u32` | forwarded to ke_msg_alloc (unused by the logic) |
| `param_4` | `s32` | new reference clock (half-slots) used to rebase offsets |
| `param_5` | `u32` | unused |
| `param_6` | `bool` | non-zero = apply the clock rebase and send notifications |

**Notes:** Field meanings of the ld_acl_env / ld_sco_env structures and the message ids 0x650/0x651 are inferred from the arithmetic only; the ROM thunk targets are undocumented.

- Addresses by version: 219: 0x0C07C04C
- Calls: `ble_flash_patch_thunk_a0083c2c`, `ble_flash_patch_thunk_a007fbac`, `ble_flash_patch_thunk_a007cd24`, `ble_flash_patch_thunk_a007fc0c`
- Confidence: low

## bt_ld_acl_sniff_state_patch

**ROM patch: on an ACL link event, promote state byte +0x16b from 1 to 2/3 based on EM control flags, then run ROM handlers**

Wraps its body between FUN_0c07dae0(0xd,3,8,1) and FUN_0c07dae0(0xd,3,8,0) (a diagnostic/profiling toggle in ROM, thunk 0xA0022C48). If ld_acl_env[link] (0xC000579C + link*4) exists it reads the current clock via FUN_0c07d9f0 (ROM thunk) and a 16-bit control word from exchange memory at 0xD0217892 + DAT_c0005415*0x18 (24-byte EM control-structure table indexed by a global byte). When the link's byte +0x16b == 1 and bit 0 of that word is clear, the byte becomes 2 if bits 0x42 are clear, else 3. It then calls FUN_0c07ddd0(link, clock, 1) and FUN_0c07de10(link, clock) (ROM thunks 0xA003460C / 0xA0033F74) to continue the ROM's link-driver processing. Part of the ld_acl ROM-patch group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | ACL link index |

**Notes:** Meaning of state values 1/2/3 at env+0x16b (likely a sniff/role-switch sub-state) is a guess.

- Addresses by version: 219: 0x0C07D664
- Calls: `ble_flash_patch_thunk_a0022c48`, `ble_flash_patch_thunk_a007d4b0`, `ble_flash_patch_thunk_a003460c`, `ble_flash_patch_thunk_a0033f74`
- Confidence: low

## bt_patch_entry_0c07cdd8

**Patch trampoline: call bt_lc_link_setup_patch then fall into undecodable bytes**

Entry stub with no direct callers (reached from a ROM patch/jump table). It calls bt_lc_link_setup_patch (ble_219_0c07c7b4) with the incoming registers and then Ghidra hits bad instruction data, i.e. the continuation is either a literal pool or a branch back into ROM that the decompiler could not follow. Treat as part of the BT controller ROM-patch group.

- Addresses by version: 219: 0x0C07CDD8
- Calls: `bt_lc_link_setup_patch`
- Confidence: low

## bt_rfcal_dc_iq_sweep_all_bands

**DC offset and IQ calibration sweep: coarse-to-fine I and Q search per band, table store**

Measures the DC offset and IQ codes of the transmit path. Stage 1 sweeps the I code from -200 to 200 in steps of 50 with Q at 0 on register 0xD0350250 (bt_rfcal_measure_residual_fmt14), clears bit 23 of 0xD0350334, refines Q and repeats the sweep and refinement while the residual stays above 200. Stage 2 runs for each of three bands with register 0xD0310034, 0xD031009C or 0xD0310104, frequency word 0xD0350248 (0xBF8E39, 0xC24E90, 0xC50EE6) and channel word 0xD0220C00 (channels 13, 39 and 65). It uses bt_rfcal_measure_residual_fmt16 with a threshold of 100 and runs a coarse I sweep, I refinement and, when needed, a Q sweep, Q refinement and I refinement again. Each channel's packed (I, Q) pair is stored with bes_pack_two_14bit_fields in the table at 0xD0310000 (26, 26 and 27 entries, 79 channels in total). At the end it sets bit 31 of 0xD0350250 and reports the elapsed time through the RAM routine at 0x200005E8. It is the core of the RF calibration group, called from bt_drv_rf_dc_iq_cal_run.

**Notes:** The 0x0C03ECC8 and 0x0C03EB98 names follow the existing annotations (fmt16 and fmt14). The packed 14-bit I and Q codes stored in the table are consistent with the codes measured here. The argument list of the Q refinement call is discussed in bt_rfcal_search_q_fmt14.

- Addresses by version: 219: 0x0C03F1F4
- Called by: `bt_drv_rf_dc_iq_cal_run`
- Calls: `bt_rfcal_measure_residual_fmt14`, `bt_rfcal_measure_residual_fmt16`, `bt_rfcal_search_i_fmt16`, `bes_pack_two_14bit_fields`, `bt_rfcal_search_i_fmt14`, `bt_rfcal_search_q_fmt14`, `ble_ram_patch_thunk_200005e8`, `ble_ram_patch_thunk_2000031c`
- Confidence: medium

## bt_rfcal_measure_residual_fmt14

**RF calibration cost function: set two 14-bit codes in a register, trigger a measurement, average sqrt(I^2+Q^2)**

Repeats param_4 times: writes param_2 & 0x3FFF into bits [13:0] and param_3 & 0x3FFF into bits [27:14] of the register *param_1 (two read-modify-writes), delays 1 unit via ble_ram_patch_thunk_200005a8 + ble_ram_patch_thunk_20000334, sets bit 30 of 0xD0350334 (start capture), delays 400 units, then reads the 22-bit signed accumulators in 0xD0350338 (I) and 0xD035033C (Q): the low 22 bits are sign-extended from bit 21, rounded toward zero by adding 7 for negatives and divided by 8 (>>3). It accumulates sqrt(I^2 + Q^2) (via VSQRT, or the newlib sqrtf error path 0x0c06f288 for a negative argument) and finally returns the mean over param_4 runs as float. Used by the DC-offset/IQ calibration sweep 0x0c03f1f4 (with param_1 = 0xD0350250) and its refinement helper 0x0c03ee44, which minimise this residual over a grid of -200..200 step 50 followed by a binary search. Sibling of bt_rfcal_measure_residual_fmt16.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | register receiving the two packed 14-bit codes (e.g. 0xD0350250) |
| `param_2` | `u32` | code for bits [13:0] (I offset) |
| `param_3` | `u32` | code for bits [27:14] (Q offset) |
| `param_4` | `s32` | number of measurements to average (1..4) |

**Returns** `f32`: mean residual magnitude

**Notes:** Register 0xD0350334/338/33C are an undocumented capture block of the BT PHY; the 'DC offset' reading comes from the search structure of the caller.

- Addresses by version: 219: 0x0C03EB98
- Called by: `bt_rfcal_search_i_fmt16`, `bt_rfcal_search_i_fmt14`, `bt_rfcal_search_q_fmt14`, `bt_rfcal_dc_iq_sweep_all_bands`
- Calls: `w_sqrtf`, `ble_ram_patch_thunk_200005a8`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## bt_rfcal_measure_residual_fmt16

**RF calibration cost function variant: 14-bit codes at [13:0]/[29:16], pulses 0xD0350250 bit 31, resets 0xD03300xx**

Same measurement loop as bt_rfcal_measure_residual_fmt14 but per iteration it first clears bit 31 of 0xD0350250, writes param_2 & 0x3FFF into bits [13:0] and param_3 & 0x3FFF into bits [29:16] of *param_1, delays 1 unit, writes 0xD0330058 = 0x800030, 0xD0330060 = 0xD0330064 = 0xFFFFFFFF, sets bit 31 of 0xD0350250 again and bit 30 of 0xD0350334, delays 400 units and then evaluates the I/Q accumulators 0xD0350338/0xD035033C exactly as the sibling (22-bit sign extension, /8, sqrt(I^2+Q^2)). Returns the mean over param_4 runs. Used by the per-band DC-offset calibration in 0x0c03f1f4 with param_1 = 0xD0310034 / 0xD031009C / 0xD0310104 (band entries of the 79-channel table at 0xD0310000) while 0xD0350248 and 0xD0220C00 are set to the band's frequency word and channel 13/39/65; also by the search helper 0x0c03ee44.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | register receiving the packed codes |
| `param_2` | `u32` | code for bits [13:0] |
| `param_3` | `u32` | code for bits [29:16] |
| `param_4` | `s32` | number of measurements to average |

**Returns** `f32`: mean residual magnitude

**Notes:** The 0xD03300xx writes look like resetting a capture/counter block before each sample.

- Addresses by version: 219: 0x0C03ECC8
- Called by: `bt_rfcal_search_i_fmt16`, `bt_rfcal_dc_iq_sweep_all_bands`
- Calls: `w_sqrtf`, `ble_ram_patch_thunk_200005a8`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## bt_rfcal_search_i_fmt14

**Refine the I code on register 0xD0350250 with fmt14 residual probes, Q fixed**

Bracketing search for the I code (bits 13:0) of 0xD0350250 with the Q code fixed at param_2, using bt_rfcal_measure_residual_fmt14. It probes centre minus and plus the half-width and the midpoint, with one measurement per probe (three once the bracket is under 17 codes). It narrows the bracket toward the lower residual until it is a few codes wide and then re-measures the stored best with three averages. Results go to *param_4 and *param_5 and the best code is returned. It is the I step of the 0xD0350250 sweep in bt_rfcal_dc_iq_sweep_all_bands.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | centre I code |
| `param_2` | `s16` | fixed Q code, placed in bits 27:14 |
| `param_3` | `s32` | search half-width in codes |
| `param_4` | `ptr` | out: best I code as s32 |
| `param_5` | `ptr` | in/out: best residual as f32 |

**Returns** `s32`: Best I code.

- Addresses by version: 219: 0x0C03EFC0
- Called by: `bt_rfcal_dc_iq_sweep_all_bands`
- Calls: `bt_rfcal_measure_residual_fmt14`
- Confidence: medium

## bt_rfcal_search_i_fmt16

**Refine the I code of a band calibration point using fmt16 residual probes**

Searches the I code (bits 13:0) of the register at param_1 while the Q code is held at param_3, using bt_rfcal_measure_residual_fmt16. It probes the centre minus 50, the centre plus 50 and the midpoint, with two measurements per probe (four once the bracket is under 8 codes). It then repeatedly probes the midpoint and keeps the side with the lower residual until the bracket is only a few codes wide. The best code and residual are written to *param_4 and *param_5. If the last probe was not the best, it re-measures the stored best with bt_rfcal_measure_residual_fmt14 at three averages and keeps the better result. It is the I refinement step of bt_rfcal_dc_iq_sweep_all_bands.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | register that receives the packed codes, such as 0xD0310034 |
| `param_2` | `s32` | centre I code; probes sit at centre plus or minus 50 |
| `param_3` | `s16` | fixed Q code |
| `param_4` | `ptr` | out: best I code as s32 |
| `param_5` | `ptr` | in/out: best residual as f32 |

**Returns** `s32`: Best I code.

- Addresses by version: 219: 0x0C03EE44
- Called by: `bt_rfcal_dc_iq_sweep_all_bands`
- Calls: `bt_rfcal_measure_residual_fmt14`, `bt_rfcal_measure_residual_fmt16`
- Confidence: medium

## bt_rfcal_search_q_fmt14

**Refine the Q code on register 0xD0350250 with fmt14 residual probes, I fixed**

Same bracketing search as bt_rfcal_search_i_fmt14, but the varied code is Q (bits 27:14 of 0xD0350250) and the I code is fixed at param_2. It probes centre minus and plus the half-width and the midpoint, with one measurement per probe (three under 17 codes), narrows toward the lower residual and re-measures the stored best with three averages. Results go to *param_4 and *param_5 and the best Q code is returned. It is the Q step of the 0xD0350250 sweep.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | centre Q code |
| `param_2` | `s16` | fixed I code, placed in bits 13:0 |
| `param_3` | `s32` | search half-width in codes |
| `param_4` | `ptr` | out: best Q code as s32 |
| `param_5` | `ptr` | in/out: best residual as f32 |

**Returns** `s32`: Best Q code.

**Notes:** In bt_rfcal_dc_iq_sweep_all_bands the decompiled call to this function passes six values, including a float, to a five-parameter prototype. The centre (0) and half-width (50) used there are inferred from the call pattern.

- Addresses by version: 219: 0x0C03F0DC
- Called by: `bt_rfcal_dc_iq_sweep_all_bands`
- Calls: `bt_rfcal_measure_residual_fmt14`
- Confidence: medium
