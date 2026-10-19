# BLE - `bt_controller` functions

69 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
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
| [`bt_drv_intersys_send_saved_iface`](#bt_drv_intersys_send_saved_iface) | 0x0C03EB84 | Send a buffer to the BT core over the intersys link using the interface id saved in DAT_2000be2e, type 0 |
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
| [`bt_drv_rf_apply_config`](#bt_drv_rf_apply_config) | 0x0C03C4BC | Program the BT RF/analog registers 0xD0220Cxx and 0xD0350xxx from a ~0x27-byte config struct |
| [`bt_drv_rf_init`](#bt_drv_rf_init) | 0x0C03CDFC | BT RF bring-up sequence: pre-init, 0xD0350xxx main init, analog defaults, then apply the built-in RF config |
| [`bt_drv_rf_pre_init`](#bt_drv_rf_pre_init) | 0x0C03C930 | First step of RF bring-up: clear/set a few 0xD0220Cxx bits, init 0xD0350xxx, write 0xCAFE0001 to 0x40080020 |
| [`bt_drv_rf_set_reg_c7c_bits13_14`](#bt_drv_rf_set_reg_c7c_bits13_14) | 0x0C03E034 | Write a 2-bit value into field [14:13] of RF register 0xD0220C7C under the register-access guard |
| [`bt_drv_rom_patch_apply_table`](#bt_drv_rom_patch_apply_table) | 0x0C03CEC8 | Install a BT-controller ROM patch table: copy data into BT RAM, then program 64 hardware patch slots |
| [`bt_drv_rom_patch_init`](#bt_drv_rom_patch_init) | 0x0C03CFC0 | Select the ROM patch table by controller metal id, apply it and enable the patch unit (bit 31 of 0xA01FFE00) |
| [`bt_lc_link_setup_patch`](#bt_lc_link_setup_patch) | 0x0C07C7B4 | ROM patch: record a link's 6-byte address in the 9-byte-per-link table at 0xC0004FD0 and start the ROM link setup |
| [`bt_ld_acl_clk_offset_update_patch`](#bt_ld_acl_clk_offset_update_patch) | 0x0C07C04C | ROM patch: adjust an ACL link's clock offset and notify LC tasks of the new ACL/eSCO anchor phase |
| [`bt_ld_acl_sniff_state_patch`](#bt_ld_acl_sniff_state_patch) | 0x0C07D664 | ROM patch: on an ACL link event, promote state byte +0x16b from 1 to 2/3 based on EM control flags, then run ROM handlers |
| [`bt_patch_entry_0c07cdd8`](#bt_patch_entry_0c07cdd8) | 0x0C07CDD8 | Patch trampoline: call bt_lc_link_setup_patch then fall into undecodable bytes |
| [`bt_rfcal_measure_residual_fmt14`](#bt_rfcal_measure_residual_fmt14) | 0x0C03EB98 | RF calibration cost function: set two 14-bit codes in a register, trigger a measurement, average sqrt(I^2+Q^2) |
| [`bt_rfcal_measure_residual_fmt16`](#bt_rfcal_measure_residual_fmt16) | 0x0C03ECC8 | RF calibration cost function variant: 14-bit codes at [13:0]/[29:16], pulses 0xD0350250 bit 31, resets 0xD03300xx |

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

## ble_ram_call_2000110c_arg0

**Call the RAM-resident function at 0x2000110c with argument 0**

Thunk that calls the fixed SRAM address 0x2000110d (0x2000110c with the Thumb bit) with r0 = 0 and returns. Targets code copied or patched into RAM (ROM-patch table), so the actual behaviour is not visible here. Called from ble_219_0c02cca8 and ble_219_0c0459fc.

**Notes:** Target function identity unknown.

- Addresses by version: 219: 0x0C045AC0
- Called by: `ble_219_0c02cca8`, `ble_219_0c0459fc`
- Confidence: medium

## ble_ram_patch_thunk_20000220

**Thunk forwarding param_1 to the code at 0x20000220**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000221 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 10 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073B50
- Called by: `ble_219_0c037d08`, `ble_219_0c03a2a0`, `ble_219_0c03bb70`, `ble_219_0c03cd58`, `bt_drv_rom_patch_init`, `bt_drv_reg_op_addr_table_init`, `ble_219_0c03d69c`, `ble_219_0c03df24`, `ble_219_0c03e49c`, `ble_219_0c03e9fc`
- Confidence: medium

## ble_ram_patch_thunk_2000022c

**Thunk forwarding param_1 to the code at 0x2000022C**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x2000022D (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 8 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073C50
- Called by: `hal_spi_build_hw_cfg`, `bes_clk_measure_hz`, `hal_uart_set_baud_divisor`, `ble_219_0c037b58`, `ble_219_0c038df8`, `ble_219_0c0399b4`, `ble_219_0c03a038`, `ble_219_0c0458a6`
- Confidence: medium

## ble_ram_patch_thunk_20000238

**Thunk forwarding param_1 to the code at 0x20000238**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000239 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 2 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073B60
- Called by: `bes_clk_measure_hz`, `ble_219_0c0399b4`
- Confidence: medium

## ble_ram_patch_thunk_20000244

**Thunk forwarding param_1 to the code at 0x20000244**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000245 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 4 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073C40
- Called by: `bes_iomux_reg0c_set_level`, `ble_219_0c041758`, `bes_iomux_init_level2`, `ble_219_0c0456c0`
- Confidence: medium

## ble_ram_patch_thunk_2000025c

**Thunk forwarding param_1 to the code at 0x2000025C**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x2000025D (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 4 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073BA0
- Called by: `bes_iomux_reg0c_set_level`, `ble_219_0c041758`, `bes_iomux_init_level2`, `ble_219_0c0456c0`
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
- Called by: `hal_i2c_master_send_poll`, `hal_i2c_master_recv_poll`, `ble_219_0c033328`, `bt_drv_reg_op_write_6byte_param`, `bt_drv_reg_op_set_timing_params`, `ble_219_0c03f1f4`, `hal_cmu_pll_enable`
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
- Called by: `hal_gpdma_stop`, `hal_block_40008000_set_run`, `ble_219_0c0384e8`, `ble_219_0c038d8c`, `ble_219_0c039488`, `ble_219_0c039820`, `ble_219_0c03a038`, `ble_219_0c03a8f4`, `ble_219_0c03ac98`, `ble_219_0c03ad44`, `ble_219_0c03bb70`, `ble_219_0c03bccc` ...
- Confidence: medium

## ble_ram_patch_thunk_20000348

**Thunk forwarding param_1 to the code at 0x20000348**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000349 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early RAM-code area, i.e. a routine copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection), so flash code reaches it through this fixed entry point. Behaviour is defined by the RAM target, not by the stub; 8 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073AE0
- Called by: `hal_gpdma_stop`, `ble_219_0c02fb54`, `ble_219_0c038654`, `ble_219_0c039364`, `ble_219_0c039488`, `ble_219_0c039820`, `ble_219_0c03a204`, `hal_cmu_pll_enable`
- Confidence: medium

## ble_ram_patch_thunk_20000534

**Thunk forwarding param_1 to the code at 0x20000534**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000535 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 1 direct caller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073C90
- Called by: `ble_219_0c03ab80`
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
- Called by: `hal_gpdma_stop`, `hal_i2c_master_send_poll`, `hal_i2c_master_recv_poll`, `hal_block_40008000_set_run`, `hal_block_40008000_open`, `ble_219_0c033328`, `hal_wdt_set_reload_slot`, `ble_219_0c0384e8`, `ble_219_0c039488`, `ble_219_0c039820`, `ble_219_0c03a8f4`, `ble_219_0c03ac98` ...
- Confidence: medium

## ble_ram_patch_thunk_200005a8

**Thunk forwarding param_1 to the code at 0x200005A8**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x200005A9 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 8 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073C20
- Called by: `ble_219_0c038d8c`, `ble_219_0c03a038`, `ble_219_0c03ac44`, `bt_rfcal_measure_residual_fmt14`, `bt_rfcal_measure_residual_fmt16`, `hal_cmu_pll_enable`, `hal_cmu_osc_x2_enable`, `hal_cmu_clk_block_8c_enable`
- Confidence: medium

## ble_ram_patch_thunk_200005e8

**Thunk forwarding param_1 to the code at 0x200005e8**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x200005e9 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early RAM-code area, i.e. a routine copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection), so flash code reaches it through this fixed entry point. Behaviour is defined by the RAM target, not by the stub; 1 direct caller (0x0c03f1f4).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073AD0
- Called by: `ble_219_0c03f1f4`
- Confidence: medium

## ble_ram_patch_thunk_20000650

**Thunk forwarding param_1 to the code at 0x20000650**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000651 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 1 direct caller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073C00
- Called by: `ble_219_0c03a2a0`
- Confidence: medium

## ble_ram_patch_thunk_2000065c

**Thunk forwarding param_1 to the code at 0x2000065c**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x2000065d (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early RAM-code area, i.e. a routine copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection), so flash code reaches it through this fixed entry point. Behaviour is defined by the RAM target, not by the stub; 1 direct caller (0x0c03a038).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073B00
- Called by: `ble_219_0c03a038`
- Confidence: medium

## ble_ram_patch_thunk_2000067c

**Thunk forwarding param_1 to the code at 0x2000067C**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x2000067D (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 8 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073C80
- Called by: `ble_219_0c038250`, `bes_otp_load_variant`, `ble_219_0c03a038`, `bes_calib_get_trim_pair`, `ble_219_0c03a2a0`, `ble_219_0c03ba38`, `ble_219_0c03e8f0`, `ble_219_0c03e9ac`
- Confidence: medium

## ble_ram_patch_thunk_20000738

**Thunk forwarding param_1 to the code at 0x20000738**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x20000739 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 2 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073B80
- Called by: `bes_cmu_request_sysclk`, `ble_219_0c0399b4`
- Confidence: medium

## ble_ram_patch_thunk_200007a8

**Thunk forwarding param_1 to the code at 0x200007A8**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x200007A9 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 1 direct caller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073C70
- Called by: `ble_219_0c03a038`
- Confidence: medium

## ble_ram_patch_thunk_200007f4

**Thunk forwarding param_1 to the code at 0x200007f4**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x200007f5 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early RAM-code area, i.e. a routine copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection), so flash code reaches it through this fixed entry point. Behaviour is defined by the RAM target, not by the stub; 3 direct callers (0x0c0328cc, 0x0c032954, 0x0c0460e8).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073AF0
- Called by: `ble_219_0c0328cc`, `hal_spi_dma_rx_start`, `ble_219_0c0460e8`
- Confidence: medium

## ble_ram_patch_thunk_2000081c

**Thunk forwarding param_1 to the code at 0x2000081C**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x2000081D (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 7 direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073BB0
- Called by: `hal_spi_dma_cancel_all`, `ble_219_0c031ea4`, `hal_spi_dma_rx_done_handler`, `hal_spi_dma_tx_done_handler`, `ble_219_0c0328cc`, `hal_spi_dma_rx_start`, `ble_219_0c0460e8`
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
- Called by: `ble_219_0c03ab80`
- Confidence: medium

## ble_ram_patch_thunk_200010a0

**Thunk forwarding param_1 to the code at 0x200010A0**

Trampoline (5 insns) that tail-forwards its single argument (param_1/r0) to the function at hard-coded SRAM address 0x200010A1 (RAM, Thumb bit set) with an indirect call and returns. The 0x2000xxxx target lies in the early .data/RAM-code area, i.e. a function copied or patched into RAM at boot (BES ROM-patch / RAM-resident code redirection table), so this stub lets flash code call RAM-resident routines through fixed entry points. The actual behaviour is defined by the RAM target, which is not part of this stub; 1 direct caller.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opaque argument passed straight through to the target (r0) |

**Notes:** Target function identity unknown from the stub; name derived from the target address.

- Addresses by version: 219: 0x0C073CA0
- Called by: `ble_219_0c03ab80`
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

## bt_drv_intersys_send_saved_iface

**Send a buffer to the BT core over the intersys link using the interface id saved in DAT_2000be2e, type 0**

Forwards to the intersys transmit routine 0x0c031884(iface = DAT_2000be2e, type = 0, data = param_1, len = param_2); that routine queues the message on the per-interface list and raises the MCU-to-BT-core interrupt via 0x400000A0 (bit 2 for interface 0, bit 3 for interface 1). Used by the HCI command sender 0x0c03ac98 when the controller is not yet marked as running (DAT_2000bd06 == 0), followed by a 50-unit delay instead of waiting for a reply.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | data buffer (HCI command packet) |
| `param_2` | `u32` | length in bytes |

**Notes:** DAT_2000be2e is read as a byte/halfword; its initialisation was not seen.

- Addresses by version: 219: 0x0C03EB84
- Called by: `ble_219_0c03ac98`
- Calls: `hal_sysipc_send`
- Confidence: medium

## bt_drv_reg_op_addr_table_init

**Fill the table of BT-controller RAM addresses (0xC000xxxx) used by the bt_drv_reg_op accessors, per metal id**

Sets DAT_2000bd88 = 0xC0000000 (controller RAM base as seen by the MCU) and, depending on the metal id returned by ble_ram_patch_thunk_20000220 (0, 1, other), stores about 40 absolute controller RAM addresses into the pointer block DAT_2000bd4c..DAT_2000be08. These pointers address RivieraWaves/BES environment structures inside the BT core's RAM and are dereferenced by the accessor functions in 0x0c03dd9c..0x0c03e314: e.g. DAT_2000bd68 = per-ACL-link env pointer array (RSSI read), DAT_2000bdb4 = 6-byte parameter location, DAT_2000bdc8 = RSSI/monitor parameter block, DAT_2000bde8 and DAT_2000bd74 = timing parameter blocks, DAT_2000bdec/bdfc/bdf0 = 30-byte RSSI tables, DAT_2000bdd4 = 8-byte table, DAT_2000bdac/DAT_2000be00 = patch-RAM variables (0xC000C8F4/0xC000C8F0 on id 0). Some entries only exist for certain ids (DAT_2000bdb8, DAT_2000bda0 only for id 1; DAT_2000bd78..bd84 and be08 only for ids 1 and >1), the others stay 0 so the accessors fall back to no-ops. Called first thing in the controller start-up routine 0x0c03bb70. Equivalent of the BES SDK bt_drv_reg_op global address initialisation.

**Notes:** Individual structure identities (ld_acl_env, lm_env, rwip_env ...) are inferred only from how the accessors use them.

- Addresses by version: 219: 0x0C03D088
- Called by: `ble_219_0c03bb70`
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
- Called by: `ble_219_0c04696c`, `ble_219_0c046c7c`
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
- Called by: `ble_219_0c04696c`, `ble_219_0c046c7c`
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
- Called by: `ble_219_0c03e314`
- Calls: `ble_mem_copy`, `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_load_rssi_table_b

**Copy the 30-byte table at 0x0c07fde0 into the controller RAM location DAT_2000bdfc**

Same guarded copy as bt_drv_reg_op_load_rssi_table_a, but from flash 0x0c07fde0 to the controller RAM address in DAT_2000bdfc (0xC00043E4 / 0xC00043F0 / 0xC00043E4 per metal id). The table is AC AC AE AE B3 B3 B6 B6 BF BF D7 D7 E8 E8 EC + 15 x 7F, i.e. -84,-84,-82,-82,-77,-77,-74,-74,-65,-65,-41,-41,-24,-24,-20 dBm thresholds with 0x7F fillers. Called from 0x0c03e314 between the a and c loaders.

**Notes:** See bt_drv_reg_op_load_rssi_table_a.

- Addresses by version: 219: 0x0C03E0C8
- Called by: `ble_219_0c03e314`
- Calls: `ble_mem_copy`, `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_load_rssi_table_c

**Copy the 30-byte table at 0x0c07fda0 into the controller RAM location DAT_2000bdf0**

Same guarded copy as bt_drv_reg_op_load_rssi_table_a, but from flash 0x0c07fda0 to the controller RAM address in DAT_2000bdf0 (0xC00043A4 / 0xC00043B0 / 0xC00043A4 per metal id). The table is AB AB AE AE B7 B7 BB BB C1 C1 D8 D8 E9 E9 EA + 15 x 7F, i.e. -85,-85,-82,-82,-73,-73,-69,-69,-63,-63,-40,-40,-23,-23,-22 dBm thresholds with 0x7F fillers. Called from 0x0c03e314.

**Notes:** See bt_drv_reg_op_load_rssi_table_a.

- Addresses by version: 219: 0x0C03E118
- Called by: `ble_219_0c03e314`
- Calls: `ble_mem_copy`, `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_load_table8_bdd4

**Copy the 8-byte RAM table at 0x20003EAC into the controller RAM location DAT_2000bdd4**

Under the register-access guard copies 8 bytes from the .data variable at 0x20003EAC (initial contents FC 00 03 07 0B 10 10 10, loaded from flash 0x0c089afc) to the controller RAM address in DAT_2000bdd4 (0xC0004324 / 0xC0004330 / 0xC0004324 per metal id) via the memcpy wrapper 0x0c03aa40; no-op when the pointer is 0. Because the source lives in RAM it can be modified at run time (e.g. by a factory/NV setting) before the controller is configured. Called from the controller configuration routine 0x0c03e314 after the three RSSI table loaders.

**Notes:** Table meaning unknown (values 0xFC,0,3,7,11,16,16,16 look like a small monotonically increasing index/gain table).

- Addresses by version: 219: 0x0C03E168
- Called by: `ble_219_0c03e314`
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
- Called by: `ble_219_0c02cca8`, `ble_219_0c05a06c`
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
- Called by: `ble_219_0c05a06c`
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
- Called by: `ble_219_0c03bb70`
- Calls: `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_set_rssi_monitor_params

**Fill the controller RAM parameter block DAT_2000bdc8 with RSSI thresholds (-100/-90 dBm) and window counts**

Under the register-access guard writes 22 fields into the structure at DAT_2000bdc8 (0xC00078CC / 0xC000851C / 0xC0009230 per metal id), skipped if the pointer is 0: u8 +0 = 1 (enable), u32 +4 = 80, u32 +8 = 100, u32 +0xC = 5, u32 +0x10 = 0x160 (352), u8 +0x14/+0x15/+0x24 = 3, u8 +0x16/+0x17/+0x25 = 0x9C (-100), u8 +0x18/+0x26 = 0, u32 +0x1C = 80, u32 +0x20 = 100, u8 +0x27/+0x2D = 0xA6 (-90), u16 +0x28 = 80, u16 +0x2A = 200, u8 +0x2C = 1, u16 +0x2E = 20, u16 +0x30 = 800. The repeated -100/-90 bytes look like signed dBm thresholds and the 80/100/200/352/800 values like sample windows or counters. Called from the controller configuration sequence 0x0c03e314. Group: bt_drv_reg_op controller-RAM accessors.

**Notes:** Possibly the AFH channel-assessment or RX AGC/RSSI monitor environment; exact structure unknown.

- Addresses by version: 219: 0x0C03DE90
- Called by: `ble_219_0c03e314`
- Calls: `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`
- Confidence: medium

## bt_drv_reg_op_set_timing_params

**Write slot-timing constants (1250, 625, 500 us, 400, 12, 20) into two controller RAM parameter blocks**

Under the register-access guard (bes_sysreg_write_04_bit19 / bes_sysreg_write_08_bit19 around DAT_2000bd58 == 0) it writes into the structure at DAT_2000bde8 (0xC0007874 / 0xC00084C4 / 0xC00091D8): u32 +0x1C = 0x4E2 (1250), u32 +0x20 = 0, u8 +0x24 = 12, u16 +0x26 = 0x271 (625), u32 +0x28 = 0x01F40271 (u16 625 and u16 500), u8 +0x2C = 1; and into the structure at DAT_2000bd74 (0xC0007770 / 0xC00083B4 / 0xC00090CC): u16 +4 = 400, u8 +6 = 0x14 (20). Both writes are skipped when the respective pointer is 0. The routine timestamps itself with ble_ram_patch_thunk_2000031c before and after and hands the difference to the RAM routine at 0x2000061C. Called from the controller configuration sequence 0x0c03e314. Group: bt_drv_reg_op controller-RAM accessors.

**Notes:** 625/1250 are BT slot / double-slot durations in microseconds, so this looks like sleep/wake-up or scheduling timing (rwip/lld environment); exact field names unknown.

- Addresses by version: 219: 0x0C03DDD8
- Called by: `bt_drv_reg_op_write_6byte_param`, `ble_219_0c03e314`
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
- Called by: `ble_219_0c03e314`
- Calls: `bt_drv_reg_op_set_timing_params`, `bes_sysreg_write_04_bit19`, `bes_sysreg_write_08_bit19`, `ble_ram_patch_thunk_2000031c`
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

## bt_drv_rf_init

**BT RF bring-up sequence: pre-init, 0xD0350xxx main init, analog defaults, then apply the built-in RF config**

Calls bt_drv_rf_pre_init, bes_periph_d035_init_main and bes_analog_init_defaults, then fills a 0x28-byte RF configuration struct on the stack and passes it to bt_drv_rf_apply_config. The struct contents are: bytes 0..1 = 0x01,0x04 (c10 field enable, value 4); word +4 = 0x00010A00 (cfg[4]=0, cfg[5]=0x0A, cfg[6]=1, cfg[7]=0); words +8/+0xC = 0; word +0x10 = 0x00014000 (cfg[0x10]=0, cfg[0x11]=0x40, cfg[0x12]=1); halfword +0x14 = 1 (cfg[0x14]=1, cfg[0x15]=0); +0x18..+0x23 = 0; halfword +0x24 = 0; cfg[0x26] = 3 (clock mode 3). Called from the controller start-up routine 0x0c03bb70 after the ROM patches have been installed. Group: RF bring-up (bt_drv_rf_pre_init / bt_drv_rf_apply_config).

**Notes:** Equivalent of BES btdrv_rf_init; register semantics undocumented.

- Addresses by version: 219: 0x0C03CDFC
- Called by: `ble_219_0c03bb70`
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
- Called by: `ble_219_0c03bb70`
- Calls: `bt_drv_rom_patch_apply_table`, `ble_ram_patch_thunk_20000220`
- Confidence: high

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
- Called by: `ble_219_0c03ee44`, `ble_219_0c03efc0`, `ble_219_0c03f0dc`, `ble_219_0c03f1f4`
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
- Called by: `ble_219_0c03ee44`, `ble_219_0c03f1f4`
- Calls: `w_sqrtf`, `ble_ram_patch_thunk_200005a8`, `ble_ram_patch_thunk_20000334`
- Confidence: medium
