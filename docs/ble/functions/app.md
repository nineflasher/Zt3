# BLE - `app` functions

83 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`app_adv_id_block_copy`](#app_adv_id_block_copy) | 0x0C029224 | Copy n bytes out of the global block at 0x20009028 (read as 'ADV_ID' by the status readers) |
| [`app_ble_cmd_fe_rx_stats_update`](#app_ble_cmd_fe_rx_stats_update) | 0x0C029CA8 | Count received 5A A5 ... FE 02 frames and accumulate their byte length |
| [`app_ble_rx_pre_hook_stub`](#app_ble_rx_pre_hook_stub) | 0x0C0291FC | Empty hook that returns 0, called at the start of the BLE data-receive handler |
| [`app_boot_reason_decode`](#app_boot_reason_decode) | 0x0C046884 | Map the BES boot flag word to a small application reset-reason code |
| [`app_cmd_complete_signal`](#app_cmd_complete_signal) | 0x0C0354CC | Clear the command-busy byte at 0x2000AB5C and give the completion object at DAT_2000AB08 |
| [`app_dev_ioctl_cmd_101`](#app_dev_ioctl_cmd_101) | 0x0C041E10 | Issue request 0x101 with a 20-byte stack argument on the global device handle DAT_20003EC8, else -EIO |
| [`app_fill_hdr_19_02`](#app_fill_hdr_19_02) | 0x0C02B14C | Write the two bytes 0x19, 0x02 into the buffer passed in |
| [`app_get_scooter_state`](#app_get_scooter_state) | 0x0C02A464 | Return pointer to the application state block at 0x20009288 |
| [`app_get_unique_id16`](#app_get_unique_id16) | 0x0C045AB0 | Fill a 16-byte buffer with the chip/flash unique ID via the RAM-patched reader |
| [`app_gpio_dev_ioctl`](#app_gpio_dev_ioctl) | 0x0C02D5EC | ioctl on the /dev/gpio file descriptor with request 0x1010000 \| param_1 |
| [`app_hook_noop`](#app_hook_noop) | 0x0C029738 | Empty function (single return) |
| [`app_magic_flag_is_set`](#app_magic_flag_is_set) | 0x0C041D10 | Test whether the 0x5a465459 magic flag in DAT_2000018c is armed |
| [`app_magic_flag_set`](#app_magic_flag_set) | 0x0C041CF8 | Set or clear the 0x5a465459 magic flag word depending on param_1==1 |
| [`app_process_cmd_task_start`](#app_process_cmd_task_start) | 0x0C0354E8 | Create the 'process command' task with 0x200 stack words at priority 1 and store its handle |
| [`app_process_cmd_task_start_thunk`](#app_process_cmd_task_start_thunk) | 0x0C02878C | Branch into app_process_cmd_task_start (thunk to ble_219_0c0354e8) |
| [`app_req_timeout_timer_start`](#app_req_timeout_timer_start) | 0x0C02C0B8 | Arm the one-shot BTstack timer at 0x20009460 with a timeout in ms (handler 0x0c02c090) |
| [`app_set_default_cfg_ptr`](#app_set_default_cfg_ptr) | 0x0C02A46C | Store the pointer to a constant table (0x0c082508) into DAT_20009480 |
| [`app_set_word_2000de84`](#app_set_word_2000de84) | 0x0C0454B4 | Store param_1 into the global word DAT_2000de84 |
| [`app_set_word_2000de88`](#app_set_word_2000de88) | 0x0C0454C0 | Store param_1 into the global word DAT_2000de88 |
| [`app_sn_prefix_whitelist_match`](#app_sn_prefix_whitelist_match) | 0x0C02A2E0 | Return 1 if a received serial number starts with a code from the ROM or RAM prefix list |
| [`app_stub_return_zero_0c0454cc`](#app_stub_return_zero_0c0454cc) | 0x0C0454CC | Stub returning 0, only reachable indirectly |
| [`app_system_init`](#app_system_init) | 0x0C047FEC | One-time BLE application bring-up: init sub-systems, start the command task, create the init task |
| [`ble_app_addr6_read`](#ble_app_addr6_read) | 0x0C045DB0 | Return the 6-byte identity at 0x2000F364 (u32 + u16), gated by request 0x101 |
| [`ble_app_addr6_store`](#ble_app_addr6_store) | 0x0C058168 | Store the 6-byte identity at param_1 through the app block writer ble_219_0c045ddc |
| [`ble_app_arm_4s_deadline`](#ble_app_arm_4s_deadline) | 0x0C05A1D8 | On mode 1: set a 4000-tick deadline, flag 0x200145a9=1 and snapshot the two event counters |
| [`ble_app_block16_f36c_read`](#ble_app_block16_f36c_read) | 0x0C045D60 | Copy up to 16 bytes of the app block at 0x2000F36C, gated by request 0x101 |
| [`ble_app_block16_f3b8_read`](#ble_app_block16_f3b8_read) | 0x0C045FA8 | Copy up to 16 bytes of the app block at 0x2000F3B8, gated by request 0x101 |
| [`ble_app_block40_f38c_read`](#ble_app_block40_f38c_read) | 0x0C045E74 | Copy the 40-byte app block at 0x2000F38C..0x2000F3B3, gated by request 0x101 |
| [`ble_app_get_status_code`](#ble_app_get_status_code) | 0x0C05CC8C | Derive a 0..4 status code from flag bits 7 and 14 of 0x200042fc and the byte at 0x20017046 |
| [`ble_app_init_callbacks_nv`](#ble_app_init_callbacks_nv) | 0x0C02973C | Early app init: register BLE callbacks, trim the link table, load the NV block and set the name |
| [`ble_app_magic_caf_check`](#ble_app_magic_caf_check) | 0x0C045F60 | Check the 32-bit magic 0x00464143 ('CAF') at 0x2000F3B4, gated by request 0x101 |
| [`ble_app_main_init`](#ble_app_main_init) | 0x0C0297B0 | Main BLE app init: identity, callbacks, default FMNA token, NV block, and the 500 ms app poll timer |
| [`ble_app_marker_o_check`](#ble_app_marker_o_check) | 0x0C045F40 | Report whether the marker byte at 0x2000F36B is 'o', gated by request 0x101 |
| [`ble_app_marker_s_check`](#ble_app_marker_s_check) | 0x0C045F04 | Report whether the marker byte at 0x2000F36A is 'S', gated by request 0x101 |
| [`ble_app_poll_tick`](#ble_app_poll_tick) | 0x0C028C94 | 500 ms app poll: VCU wake retries, NV save, power-off countdown, 15-minute battery poll |
| [`ble_app_start_deferred_500ms_op`](#ble_app_start_deferred_500ms_op) | 0x0C05CB08 | Store an operation (id, mapped type code, args) in 0x200170d0.. and arm a 500 ms timer |
| [`ble_app_word_f360_read`](#ble_app_word_f360_read) | 0x0C045E04 | Read the 32-bit word at 0x2000F360, gated by request 0x101 (length must be 4) |
| [`ble_crypto_nv_store_blob`](#ble_crypto_nv_store_blob) | 0x0C05C8A8 | Store a blob in NV record 0x1389 and write the validity marker 0xEA to record 0xFAA |
| [`ble_crypto_set_serial_number`](#ble_crypto_set_serial_number) | 0x0C05C888 | Copy up to 16 bytes into the vehicle serial-number buffer at 0x20004980 |
| [`ble_device_info_init`](#ble_device_info_init) | 0x0C02B158 | Fill the BLE identity block at 0x200091E8 with a code, model 0x219, address, unique ID and serial |
| [`ble_device_info_read_cmd`](#ble_device_info_read_cmd) | 0x0C02B1B4 | Read a slice of the BLE identity block at 0x200091E8 and reply on the app or UART channel |
| [`ble_device_name_setup`](#ble_device_name_setup) | 0x0C0292F0 | Set the BLE advertising name from the serial number and a per-model name template |
| [`ble_event_window_expire`](#ble_event_window_expire) | 0x0C0582B0 | Expire old entries of the 10-slot event ring and count them into two tallies |
| [`ble_get_bluetooth_pn`](#ble_get_bluetooth_pn) | 0x0C0296C4 | Read the 14-character Bluetooth part number from app block 0x2000F3B8 and store it as the serial |
| [`ble_init_cfg_ptr_store`](#ble_init_cfg_ptr_store) | 0x0C0286E0 | Init step: run ble_219_0c037a2c on the .data base, then store a flash config pointer |
| [`ble_log_data_send`](#ble_log_data_send) | 0x0C05AB04 | Send one type-4 log record from ring 0x20014670 to the state handle |
| [`ble_log_print_timestamped`](#ble_log_print_timestamped) | 0x0C05B5E4 | Format a log line into a 256-byte buffer and print it with an hh:mm:ss.mmm stamp |
| [`ble_log_typed_send`](#ble_log_typed_send) | 0x0C05AC20 | Send one log record from ring 0x20015538 with opcode 0x31, 0x39 or 0x3E by type |
| [`ble_nb_block_copy_in`](#ble_nb_block_copy_in) | 0x0C0567C8 | Copy n bytes from the source into the RAM block at 0x200042E0 |
| [`ble_nv_identity_init`](#ble_nv_identity_init) | 0x0C0295E0 | Validate the NV identity records (PPID, model name, category flag) and write defaults if bad |
| [`ble_nv_load_8byte_block`](#ble_nv_load_8byte_block) | 0x0C05CE48 | Load the 8-byte NV record 0xFA8 into a caller buffer |
| [`ble_nv_load_device_name`](#ble_nv_load_device_name) | 0x0C05CEA8 | Read the 16-byte device name from NV record 0xFA6 and return its length |
| [`ble_nv_load_flag_byte`](#ble_nv_load_flag_byte) | 0x0C05CE74 | Read the one-byte flag from NV record 0xFA7, or 0 on failure |
| [`ble_nv_read_block_1c5`](#ble_nv_read_block_1c5) | 0x0C05B0F4 | Read the 512-byte block at NV partition 2 offset 0x1C5 |
| [`ble_nv_record_read`](#ble_nv_record_read) | 0x0C05B380 | Read a record from its NV partition offset by record id |
| [`ble_nv_record_write`](#ble_nv_record_write) | 0x0C05B138 | Write a record to its NV partition offset by record id, then commit |
| [`ble_nv_store_8byte_block`](#ble_nv_store_8byte_block) | 0x0C05CE38 | Store an 8-byte block to NV record 0xFA8 (length must be 8) |
| [`ble_nv_store_device_name`](#ble_nv_store_device_name) | 0x0C05CE98 | Store a device name of up to 16 bytes in NV record 0xFA6 |
| [`ble_nv_store_flag_byte`](#ble_nv_store_flag_byte) | 0x0C05CE54 | Store one flag byte to NV record 0xFA7 |
| [`ble_nv_write_block_1c5`](#ble_nv_write_block_1c5) | 0x0C05B0A8 | Write up to 512 bytes into NV partition 2 at offset 0x1C5, then commit |
| [`ble_nvdata_init`](#ble_nvdata_init) | 0x0C02D724 | Create the 5-entry request queue and the 'nvdata' task (0x100 stack words, priority 3) |
| [`ble_process_autokey`](#ble_process_autokey) | 0x0C02A3C4 | Store the autokey record in the NV block and switch the RX state to 3 |
| [`ble_proto_dispatch_op`](#ble_proto_dispatch_op) | 0x0C05CA80 | Dispatch protocol sub-opcodes 0x1F and 0x20..0x29 to their handlers, always return 0 |
| [`ble_record_a_derive_and_commit`](#ble_record_a_derive_and_commit) | 0x0C053D04 | Reload record A, derive its 28-byte and 16-byte blocks and commit them to NV |
| [`ble_record_a_reload`](#ble_record_a_reload) | 0x0C053C94 | Reload the 32-byte record at 0x200101E4 from its backing store into RAM |
| [`ble_record_b_derive_and_commit`](#ble_record_b_derive_and_commit) | 0x0C053DA4 | Reload record B, derive its 28-byte block, bump its counter and commit to NV |
| [`ble_record_b_reload`](#ble_record_b_reload) | 0x0C053CCC | Reload the 32-byte record at 0x20010204 from its backing store into RAM |
| [`ble_record_sync_step`](#ble_record_sync_step) | 0x0C055330 | Advance the record A sync step: derive record A, sync record B, post a kick |
| [`ble_record_sync_tick`](#ble_record_sync_tick) | 0x0C0553D0 | Run one record sync step, latch slot 0xFE flag bit 5 and post event 2 |
| [`ble_slot_store_and_queue`](#ble_slot_store_and_queue) | 0x0C054298 | Store a (u16, u16) record in the next slot and queue it when a slot is in use |
| [`ble_speed_limit_code_check`](#ble_speed_limit_code_check) | 0x0C0288DC | Check received bytes for the speed-limit removal token and acknowledge it with frame 0x82 |
| [`ble_unlock_record_get`](#ble_unlock_record_get) | 0x0C02A430 | Log the autokey and seat-key unlock records and return the record block address |
| [`ble_unlock_request_start`](#ble_unlock_request_start) | 0x0C02A8A0 | Start an unlock request when state bit 1 is set: arm a 5 s timeout and run the auth callback |
| [`ble_vcu_cmd_handle`](#ble_vcu_cmd_handle) | 0x0C02B480 | Dispatch class 9 and 0x16 command frames to their unlock, pairing, telemetry and ack handlers |
| [`ble_vcu_wakeup_retry`](#ble_vcu_wakeup_retry) | 0x0C02A35C | Timer step that re-sends a VCU wake request up to three times while the VCU is in low power |
| [`ble_version_info_print`](#ble_version_info_print) | 0x0C041E38 | Print the version and build records for Application, LibWhale, Miniboot and LibWhale in Miniboot |
| [`bt_app_set_name_and_advdata`](#bt_app_set_name_and_advdata) | 0x0C029414 | Pick the vendor adv-data entry for the serial number, set the 8-byte identity and CRC-32 |
| [`nvdata_device_init`](#nvdata_device_init) | 0x0C02DEA8 | Open one nvdata device, build its item index and locate the newest valid item |
| [`nvdata_ioctl_cmd_0x104`](#nvdata_ioctl_cmd_0x104) | 0x0C02D6CC | Send ioctl 0x104 (no argument) to /dev/nvdata<idx>, issued after an update before flush |
| [`nvdata_ioctl_cmd_0x200`](#nvdata_ioctl_cmd_0x200) | 0x0C02D688 | Send ioctl 0x200 (no argument) to /dev/nvdata<idx>, used last in a write sequence (flush) |
| [`nvdata_ioctl_get_buf_0x102`](#nvdata_ioctl_get_buf_0x102) | 0x0C02D6A4 | ioctl 0x102 on /dev/nvdata<idx>: return the driver's RAM buffer pointer for the partition |
| [`nvdata_ioctl_lock_0x106`](#nvdata_ioctl_lock_0x106) | 0x0C02D704 | ioctl 0x106 with an argument on /dev/nvdata<idx>; returns -5 if the partition is not open |
| [`nvdata_ioctl_unlock_0x103`](#nvdata_ioctl_unlock_0x103) | 0x0C02D6E8 | ioctl 0x103 with an argument on /dev/nvdata<idx>; callers pass 0 after finishing buffer access |

## app_adv_id_block_copy

**Copy n bytes out of the global block at 0x20009028 (read as 'ADV_ID' by the status readers)**

memcpy(param_1, &DAT_20009028, param_2): copies the first param_2 bytes of the global block starting at 0x20009028 into the caller's buffer. The two callers are the vehicle/FMNA status reader 0x0c02a8f8 (cases 0x3c/0x40, logging 'R ADV_ID len=%d' and copying 13 bytes) and the factory command handler 0x0c02cca8 (case 0x58, copying 13 bytes when the payload byte is 0x0d). The same region (records of 13 bytes from 0x20009029) is scanned by app_sn_prefix_whitelist_match, so the block is a 13-byte advertising identifier followed by the RAM serial-prefix list.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination buffer |
| `param_2` | `u32` | number of bytes to copy (callers use 13) |

**Notes:** The exact layout of the 0x20009028 block (13-byte ADV_ID vs. 13-byte record list starting one byte later) is inferred from the callers only.

- Addresses by version: 219: 0x0C029224
- Called by: `ble_fmna_cmd_handler`, `ble_factory_test_dispatch_query`
- Calls: `memcpy`
- Confidence: medium

## app_ble_cmd_fe_rx_stats_update

**Count received 5A A5 ... FE 02 frames and accumulate their byte length**

Checks that the packet in param_1 starts with the Ninebot frame header 0x5A 0xA5 and that byte[5] (command) == 0xFE and byte[6] == 0x02. On a match it increments DAT_20008f5c (total frames) and DAT_20008f58 (frames in the current burst) and adds param_2 (packet length) to DAT_20008f60 (total bytes). The BLE receive handler (0x0c029df8) then compares DAT_20008f58 with an expected count (DAT_20008f54) parsed from a request and, when equal, sends an 'FE' reply frame and resets DAT_20008f58, so this looks like a BLE throughput/packet-count test helper.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | decrypted BLE/UART frame (byte[0]=0x5A, byte[1]=0xA5, byte[5]=cmd, byte[6]=sub-cmd) |
| `param_2` | `u32` | frame length in bytes |

**Notes:** Purpose (throughput test) inferred from the counter comparison in the caller, not from strings.

- Addresses by version: 219: 0x0C029CA8
- Called by: `ble_rx_data_handler`
- Confidence: medium

## app_ble_rx_pre_hook_stub

**Empty hook that returns 0, called at the start of the BLE data-receive handler**

Stub that returns 0 with no side effects. It is called first by the BLE application receive handler (0x0c029df8) before the packet is decrypted/dispatched, apparently a placeholder for an optional pre-processing hook; the return value is ignored by the caller.

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C0291FC
- Called by: `ble_rx_data_handler`
- Confidence: high

## app_boot_reason_decode

**Map the BES boot flag word to a small application reset-reason code**

Reads bes_boot_flag_get() (DAT_20000188) and returns: 5 if bit 0 is set; else 1 if bit 1 is set; else, if byte 1 (bits 15..8) equals 1, 4 when bit 16 is set and 3 otherwise; else 0. The application init routine 0x0c0297b0 treats codes 1 and 3 ((code & 0xfd) == 1) specially by setting DAT_20008f6c = 0x13 and DAT_20008f84 = 0, i.e. a reboot caused by the previous firmware (e.g. after an upgrade or software reset) changes the start-up state.

**Returns** `u32`: reset-reason code 0, 1, 3, 4 or 5

**Notes:** Meaning of the individual flag bits is not documented; code values are only known from this decoder and its caller.

- Addresses by version: 219: 0x0C046884
- Called by: `ble_app_main_init`
- Calls: `bes_boot_flag_get`
- Confidence: medium

## app_cmd_complete_signal

**Clear the command-busy byte at 0x2000AB5C and give the completion object at DAT_2000AB08**

Writes zero to the byte at 0x2000AB5C and gives the object whose handle is DAT_2000AB08 through ble_219_0c042c8c with (handle, 0, 0). It is the completion step after a command, presumably waking the task that waits on that object. Four callers share it: ble_219_0c0360d4, ble_219_0c03ff38, ble_219_0c041e38 and ble_219_0c048040.

**Notes:** The object at DAT_2000AB08 is presumed to be the semaphore or queue that the process command task waits on.

- Addresses by version: 219: 0x0C0354CC
- Called by: `wdt_task_monitor_cli`, `ble_debug_timestamp_print`, `ble_version_info_print`, `fd_dump_open_files`
- Calls: `xQueueGenericSend`
- Confidence: medium

## app_dev_ioctl_cmd_101

**Issue request 0x101 with a 20-byte stack argument on the global device handle DAT_20003EC8, else -EIO**

If the global descriptor DAT_20003EC8 (an fd/handle from the '/dev/...' device layer, valid when > 0) is open, calls 0x0c0484b4(DAT_20003EC8, 0x101, &buf) where buf is an uninitialised 20-byte stack area and returns its result; otherwise returns -5 (-EIO). The eight small callers 0x0c045d60 ... 0x0c045fa8 are device-control wrappers of the same module. The handle is opened elsewhere by the file-descriptor layer that prints '/dev/%s%d' and 'Unsupport: /dev/%s%d reopen'.

**Returns** `s32`: result of the request, or -5 (0xfffffffb, -EIO) when the handle is not open

**Notes:** 0x0c0484b4 is assumed to be the ioctl-like entry of the LibWhale device layer; command 0x101 and the argument structure are unknown.

- Addresses by version: 219: 0x0C041E10
- Called by: `ble_app_block16_f36c_read`, `ble_app_addr6_read`, `ble_app_word_f360_read`, `ble_app_block40_f38c_read`, `ble_app_marker_s_check`, `ble_app_marker_o_check`, `ble_app_magic_caf_check`, `ble_app_block16_f3b8_read`
- Calls: `_close`
- Confidence: low

## app_fill_hdr_19_02

**Write the two bytes 0x19, 0x02 into the buffer passed in**

Stores 0x19 at param_1[0] and 0x02 at param_1[1]. Called once from the app init routine (0x0c0297b0) with a 4-byte stack buffer. The pair equals 0x0219 little-endian, which matches the image tag BLE_219, so it may be a 2-byte firmware/protocol version, but this is a guess.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination buffer of at least 2 bytes |

**Notes:** Meaning of 0x0219 is speculative (possibly firmware version 2.19).

- Addresses by version: 219: 0x0C02B14C
- Called by: `ble_app_main_init`
- Confidence: low

## app_get_scooter_state

**Return pointer to the application state block at 0x20009288**

Returns the constant address &DAT_20009288. The returned block is used by the BLE connection-status callback (0x0c0287ac), which sets/clears bit 0 (BLE connected) and bit 3 (classic BT connected) of the word at offset 0x3c, and by four other app routines.

**Returns** `ptr`: pointer to the app state structure (DAT_20009288)

**Notes:** Only the +0x3c connection flags field is seen in this packet's callers.

- Addresses by version: 219: 0x0C02A464
- Called by: `btapp_btle_connect_status_change`, `ble_speed_limit_code_check`, `ble_link_status_notify_tick`, `ble_app_poll_tick`, `bts_op_cmd_handle`
- Confidence: medium

## app_get_unique_id16

**Fill a 16-byte buffer with the chip/flash unique ID via the RAM-patched reader**

Calls the ROM-patch thunk ble_ram_patch_thunk_20000f34 with (0, param_1, 0x10) and returns 0x10. The argument pattern (device id 0, destination, 16 bytes) matches hal_norflash_get_unique_id(HAL_FLASH_ID_0, buf, 16) of the BES SDK, i.e. the 16-byte flash unique ID. The device-info builder 0x0c02b158 stores the result at 0x200091f2 next to the version word and the serial string, and the VCU-protocol dispatcher 0x0c02cca8 (command 0x2d) compares its first byte with a received byte.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 16-byte destination buffer |

**Returns** `u32`: always 16 (bytes written)

**Notes:** The patched RAM routine itself is not visible; the unique-ID interpretation is inferred from the argument shape.

- Addresses by version: 219: 0x0C045AB0
- Called by: `ble_device_info_init`, `ble_factory_test_dispatch_query`
- Calls: `ble_ram_patch_thunk_20000f34`
- Confidence: medium

## app_gpio_dev_ioctl

**ioctl on the /dev/gpio file descriptor with request 0x1010000 | param_1**

Calls the VFS ioctl dispatcher 0x0c0484b4 with the file descriptor stored in DAT_2000989c (set by 0x0c02d5d4 = open("/dev/gpio", 0)), the request code param_1 | 0x01010000 and the argument param_2. The dispatcher maps fd 3..48 to an object in the table at 0x2000f6d8 and jumps to its ops entry at +0xc; an invalid fd sets errno = 9 (EBADF) and returns -1. Single caller: the periodic application tick 0x0c028c94, which issues request 0x500 with a boolean taken from bit 0 of a vehicle-state word, i.e. it drives a GPIO output (an indicator/enable line) each tick.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | gpio ioctl sub-command (caller uses 0x500); ORed with 0x1010000 |
| `param_2` | `u32` | ioctl argument (caller passes 0/1) |

**Notes:** Meaning of request 0x500 inside the gpio driver was not examined.

- Addresses by version: 219: 0x0C02D5EC
- Called by: `ble_app_poll_tick`
- Calls: `_close`
- Confidence: medium

## app_hook_noop

**Empty function (single return)**

Contains only a return instruction. Called once from 0x0c02a8f8 as a do-nothing callback/hook slot; no state is touched.

- Addresses by version: 219: 0x0C029738
- Called by: `ble_fmna_cmd_handler`
- Confidence: high

## app_magic_flag_is_set

**Test whether the 0x5a465459 magic flag in DAT_2000018c is armed**

Returns true when the RAM word DAT_2000018c equals the magic value 0x5a465459, i.e. when app_magic_flag_set(1) was last called. Pure getter, no side effects. Called from ble_219_0c02c49c and ble_219_0c02cca8.

**Returns** `bool`: true if the magic flag is armed

- Addresses by version: 219: 0x0C041D10
- Called by: `ble_factory_test_dispatch_set`, `ble_factory_test_dispatch_query`
- Confidence: medium

## app_magic_flag_set

**Set or clear the 0x5a465459 magic flag word depending on param_1==1**

Writes the magic constant 0x5a465459 (bytes 'Y','T','F','Z' in memory) to the RAM word DAT_2000018c when param_1 == 1, otherwise writes 0. Together with app_magic_flag_is_set it implements a persistent boolean flag held in an early .data word that survives as a magic-value rather than a plain 0/1. The meaning of the flag (probably a boot/factory/mode switch) is not visible from this function; its only caller is ble_219_0c02c49c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 1 = arm the flag; any other value clears it |

**Notes:** Purpose of the flag inferred only from the magic value; not confirmed.

- Addresses by version: 219: 0x0C041CF8
- Called by: `ble_factory_test_dispatch_set`
- Confidence: medium

## app_process_cmd_task_start

**Create the 'process command' task with 0x200 stack words at priority 1 and store its handle**

Calls ble_219_0c043cfc with the task entry 0x0C034F0C, the name 'process command', a stack depth of 0x200 words, no task parameter, priority 1, the static stack buffer at 0x2000ACC0 and the static TCB at 0x2000B4C0. The returned handle is stored in DAT_2000ABA0. It always returns 0 and does not check the creation result.

**Returns** `u32`: always 0

**Notes:** The callee is assumed to be xTaskCreateStatic from its seven arguments. The task body at 0x0C034F0C is not part of this packet. ble_219_0c02878c is a branch to this function.

- Addresses by version: 219: 0x0C0354E8
- Called by: `app_process_cmd_task_start_thunk`
- Calls: `xTaskCreateStatic`
- Confidence: high

## app_process_cmd_task_start_thunk

**Branch into app_process_cmd_task_start (thunk to ble_219_0c0354e8)**

Single-instruction thunk: the decompiler shows the body of ble_219_0c0354e8 under the name thunk_FUN_0c0354e8, so this address is a branch into that function and has no logic of its own. It is a second entry point to the 'process command' task creation and is reached from ble_219_0c047fec. The return value is whatever the target returns, which is always 0.

**Returns** `u32`: always 0, passed through from the target

**Notes:** Thunk. The behaviour is described on ble_219_0c0354e8.

- Addresses by version: 219: 0x0C02878C
- Called by: `app_system_init`
- Calls: `app_process_cmd_task_start`
- Confidence: high

## app_req_timeout_timer_start

**Arm the one-shot BTstack timer at 0x20009460 with a timeout in ms (handler 0x0c02c090)**

Removes the btstack_timer_source_t at 0x20009460 from the run loop (btstack_run_loop_remove_timer), sets its handler to 0x0c02c090, sets the timeout to param_1 ms (btstack_run_loop_set_timer) and adds it again (btstack_run_loop_add_timer), so a running timer is restarted. The handler 0x0c02c090 reports the pending request code DAT_20008f69 & 0x7f with the 16-bit value DAT_20008f6a | DAT_20008f6b << 8 through 0x0c0585a4 and then clears those three bytes. The only caller 0x0c02a8a0 starts it with 5000 ms when it records a new pending request (DAT_20008f69 = code | 0x80), i.e. this is a 5 s response timeout for a request forwarded to the VCU/host. param_2..param_4 are unused (decompiler artefacts).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | timeout in milliseconds |
| `param_2` | `u32` | unused |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | unused |

**Notes:** What 0x0c0585a4 does with the pending code was not examined; 'request timeout' is inferred from the caller.

- Addresses by version: 219: 0x0C02C0B8
- Called by: `ble_unlock_request_start`
- Calls: `btstack_run_loop_set_timer_handler`, `btstack_run_loop_set_timer`, `btstack_run_loop_add_timer`, `btstack_run_loop_remove_timer`
- Confidence: medium

## app_set_default_cfg_ptr

**Store the pointer to a constant table (0x0c082508) into DAT_20009480**

Writes the flash address 0x0c082508 into the RAM pointer DAT_20009480. It is called from the application init routines (0x0c02973c and 0x0c0297b0). Note that the CRC32 table built by crc32_make_table lives at 0x20009484, immediately after this pointer, so the pointer and the table are adjacent globals. The pointed-to data is not interpreted here.

**Notes:** What 0x0c082508 contains (default configuration / token table?) was not examined.

- Addresses by version: 219: 0x0C02A46C
- Called by: `ble_app_init_callbacks_nv`, `ble_app_main_init`
- Confidence: low

## app_set_word_2000de84

**Store param_1 into the global word DAT_2000de84**

Plain setter: DAT_2000de84 = param_1. No direct callers, so it is invoked through a function-pointer table (an ops/config setter). The consumer and meaning of the stored value are not determined here.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value to store |

**Notes:** Likely paired with app_set_word_2000de88; purpose unknown.

- Addresses by version: 219: 0x0C0454B4
- Confidence: low

## app_set_word_2000de88

**Store param_1 into the global word DAT_2000de88**

Plain setter: DAT_2000de88 = param_1. Indirect-call only; sibling of app_set_word_2000de84.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value to store |

- Addresses by version: 219: 0x0C0454C0
- Confidence: low

## app_sn_prefix_whitelist_match

**Return 1 if a received serial number starts with a code from the ROM or RAM prefix list**

Two passes with memcmp. Pass 1 (only if the count byte DAT_20003e1d is non-zero): walks DAT_20003e1d records of 13 bytes starting at ROM 0x0c080dd5 (entries such as '0TDC','0VDD','Z02K','Z03W' followed by 'NC..'); the code length is 3 if record[3] == 0 else 4, and a match sets the result to 1 (all records are still scanned). If any matched, returns 1. Pass 2: walks the 30 RAM records of 13 bytes from 0x20009029 to 0x200091af, considering only records whose byte[4] is 'N' and byte[5] is 'B' or 'C', with the same 3/4-byte compare. Returns 1 when any record matched, else 0. Called from the VCU command handler 0x0c02b480 (command 0x10, 'check reveived sn is valid') to decide whether the received 14-byte vehicle SN is acceptable before 'set sn'. Only param_1 is used; the other parameters are decompiler artefacts of the 3-argument memcmp.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | received serial-number bytes (first 3..4 compared) |
| `param_2` | `u32` | unused |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | unused |

**Returns** `s32`: 1 if a list entry matches, 0 otherwise

**Notes:** Record layout (13 bytes: 3/4-char code, then 'N' + 'B'/'C' + ...) is inferred from the compare logic and the ROM strings near 0x0c080e7e; the role as an SN prefix whitelist comes from the caller's debug strings.

- Addresses by version: 219: 0x0C02A2E0
- Called by: `ble_vcu_cmd_handle`
- Calls: `memcmp`
- Confidence: medium

## app_stub_return_zero_0c0454cc

**Stub returning 0, only reachable indirectly**

Two-instruction function that just returns 0; no direct callers, so it is a default callback/ops-table entry that reports success or 'nothing'.

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C0454CC
- Confidence: high

## app_system_init

**One-time BLE application bring-up: init sub-systems, start the command task, create the init task**

Runs the bring-up sequence for the BLE application: 0x0C0459D4(0), 0x0C035D30(), 0x0C041D50(), ble_clock_realtime_offset_update(1) to reset the realtime offset, 0x0C036394(1), 0x0C0459FC(), app_process_cmd_task_start (0x0C0354E8), and 0x0C0286E0(). It then creates the FreeRTOS task named 'init' at entry 0x0C047F8C with stack depth 0x400 and priority 5 through 0x0C043D3C, calls 0x0C043E70(), and returns 0. The task entry at 0x0C047F8C is not in this packet.

**Returns** `u32`: always 0

**Notes:** The 0x0C043D3C call is identified as a task-create call from its arguments (name string, depth, priority). The meaning of the calls to 0x0C0459D4, 0x0C036394 and 0x0C043E70 is not clear from this packet.

- Addresses by version: 219: 0x0C047FEC
- Called by: `Reset_Handler`
- Calls: `ble_init_cfg_ptr_store`, `app_process_cmd_task_start_thunk`, `console_init`, `wdt_task_monitor_enable`, `ble_clock_realtime_offset_update`, `ble_nvdata0_dev_read_record`, `xTaskCreate`, `vTaskStartScheduler`, `ble_hw_init_stage0`, `ble_boot_notice_log`
- Confidence: medium

## ble_app_addr6_read

**Return the 6-byte identity at 0x2000F364 (u32 + u16), gated by request 0x101**

Gated copy of a 6-byte value: the u32 at 0x2000F364 goes to output bytes 0-3 and the u16 at 0x2000F368 to bytes 4-5. The first step is the app device request 0x101 (FUN_0C041E10), whose error is returned if it fails, and a length other than 6 returns -EINVAL. The 4+2 byte layout matches a Bluetooth device address, so the block is probably the controller's own address; this is inferred from size and layout only. Callers are at 0x0C02CCA8, 0x0C058160, 0x0C058170, 0x0C0581A8 and 0x0C058250.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 6-byte output buffer |
| `param_2` | `s32` | requested length, must be 6 |

**Returns** `s32`: 0 on success, -22 for a length other than 6, or the ioctl error

- Addresses by version: 219: 0x0C045DB0
- Called by: `ble_factory_test_dispatch_query`, `ble_random_bytes_6`, `ble_random_addr_advance`, `ble_random_static_addr_build`, `ble_host_init_identity_addr`
- Calls: `app_dev_ioctl_cmd_101`
- Confidence: medium

## ble_app_addr6_store

**Store the 6-byte identity at param_1 through the app block writer ble_219_0c045ddc**

Two-instruction wrapper that calls ble_219_0c045ddc (not yet described) with param_1 and length 6. Its caller ble_219_0c02a8f8 is outside this batch. Within the identity code of ble_host_init_identity_addr, ble_219_0c045ddc is the counterpart of ble_app_addr6_read, so this stores a 6-byte device identity into the app block.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 6-byte identity address to store |

**Notes:** The write-side meaning of ble_219_0c045ddc is inferred from how ble_host_init_identity_addr uses it, not from its own body.

- Addresses by version: 219: 0x0C058168
- Called by: `ble_fmna_cmd_handler`
- Calls: `ble_cfg_set_bd_addr_checked`
- Confidence: medium

## ble_app_arm_4s_deadline

**On mode 1: set a 4000-tick deadline, flag 0x200145a9=1 and snapshot the two event counters**

If param_1 == 1 it stores xTaskGetTickCount() + 4000 into DAT_200145ac (a deadline 4 s ahead at the 1 ms tick) and sets the u8 DAT_200145a9 = 1. Then, depending on the flag word at 0x200042fc (state+4): if bit 3 is set DAT_200130ed = state[0x38] (the counter at 0x20004330), and if bit 0 is set DAT_200130ec = state[0x1f] (the counter at 0x20004317), so the current event counts are latched when the window starts. For any other param_1 value it merely rewrites DAT_200145a9 with its previous value (no change). Always returns 0. Called from 0c02b480 together with ble_host_timer_restart.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 1 = start the 4 s window; other values are no-ops |

**Returns** `u32`: always 0

**Notes:** Purpose of the 4 s window (0x200145ac/0x200145a9) is inferred from the constant 4000 and FreeRTOS tick use; the consumer of the deadline is not in this packet.

- Addresses by version: 219: 0x0C05A1D8
- Called by: `ble_vcu_cmd_handle`
- Calls: `xTaskGetTickCount`, `ble_get_state_ptr_42f8`
- Confidence: medium

## ble_app_block16_f36c_read

**Copy up to 16 bytes of the app block at 0x2000F36C, gated by request 0x101**

Reads a 16-byte RAM block at 0x2000F36C after first issuing the app device request 0x101 (app_dev_ioctl_cmd_101, FUN_0C041E10); a non-zero ioctl result is returned unchanged. A requested length above 16 returns -EINVAL (-0x16) without copying, and otherwise the requested bytes are copied with memcpy. The 16-byte bound comes from the 0x11 comparison, and the block contents are not identified here. Callers are at 0x0C02A484, 0x0C02B158 and 0x0C02CCA8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination buffer |
| `param_2` | `u32` | number of bytes requested, 0..16 |

**Returns** `s32`: 0 on success, -22 (-EINVAL) for a length above 16, or the ioctl error (-EIO)

- Addresses by version: 219: 0x0C045D60
- Called by: `bt_vcu_cmd_wr_process`, `ble_device_info_init`, `ble_factory_test_dispatch_query`
- Calls: `app_dev_ioctl_cmd_101`, `memcpy`
- Confidence: medium

## ble_app_block16_f3b8_read

**Copy up to 16 bytes of the app block at 0x2000F3B8, gated by request 0x101**

Same pattern as ble_app_block16_f36c_read: the app device request 0x101 (FUN_0C041E10) must succeed, a length above 16 returns -EINVAL, and otherwise the requested bytes are copied from 0x2000F3B8 with memcpy. The 16-byte bound is inferred from the 0x11 comparison. Six callers use it: 0x0C0292F0, 0x0C029414, 0x0C0296C4, 0x0C02A484, 0x0C02B480 and 0x0C056A50.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination buffer |
| `param_2` | `u32` | bytes requested, 0..16 |

**Returns** `s32`: 0 on success, -22 for a length above 16, or the ioctl error

- Addresses by version: 219: 0x0C045FA8
- Called by: `ble_device_name_setup`, `bt_app_set_name_and_advdata`, `ble_get_bluetooth_pn`, `bt_vcu_cmd_wr_process`, `ble_vcu_cmd_handle`, `ble_adv_set_a_apply_mode`
- Calls: `app_dev_ioctl_cmd_101`, `memcpy`
- Confidence: medium

## ble_app_block40_f38c_read

**Copy the 40-byte app block at 0x2000F38C..0x2000F3B3, gated by request 0x101**

Gated snapshot of a 40-byte RAM block: ten consecutive 32-bit words from 0x2000F38C to 0x2000F3B0 are copied in order into the caller's buffer, after the app device request 0x101 (FUN_0C041E10) has succeeded. A length other than 0x28 returns -EINVAL. The whole region is read as one unit, which suggests a fixed-size record, but its field layout is not identified here. The 0x2000F3B4 word read by ble_app_magic_caf_check sits directly after this block.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 40-byte output buffer |
| `param_2` | `s32` | requested length, must be 40 |

**Returns** `s32`: 0 on success, -22 for a wrong length, or the ioctl error

- Addresses by version: 219: 0x0C045E74
- Called by: `nb_upgrade_process_cmd`, `ble_factory_test_dispatch_query`
- Calls: `app_dev_ioctl_cmd_101`
- Confidence: medium

## ble_app_get_status_code

**Derive a 0..4 status code from flag bits 7 and 14 of 0x200042fc and the byte at 0x20017046**

Reads the flag word at state+4 (0x200042fc). Result starts at 0. If bit 7 is set, result = DAT_20017046 but forced back to 0 unless it is 1, 2 or 3. If bit 14 is set the result is overridden to 4. Called from 0c02a8f8 together with ble_state_407a_copy, ble_flags_bit15_get and ble_flags_bit4_get, which together assemble a status report (probably for the VCU UART protocol).

**Returns** `u32`: 0 (idle/none), 1..3 (from 0x20017046 when flag bit 7), 4 (when flag bit 14)

**Notes:** Semantics of bits 7/14 and of 0x20017046 are not named yet.

- Addresses by version: 219: 0x0C05CC8C
- Called by: `ble_fmna_cmd_handler`
- Calls: `ble_get_state_ptr_42f8`
- Confidence: medium

## ble_app_init_callbacks_nv

**Early app init: register BLE callbacks, trim the link table, load the NV block and set the name**

Registers the stack hooks: the pre-check hook at 0x0C028A78 with ble_cb_slot_14608_set, mode 14 with ble_set_mode_14_or_16, the RX handler 0x0C029DF9 (ble_rx_data_handler) with ble_cb_slot_15e5c_set, the connect status callbacks at indexes 2 and 0 (btle_connect_status_change, btapp_btle_connect_status_change) and the enhanced connect-status callback 0x0C028B51. It then trims the link table from NV (ble_link_table_nv_load_trim), reads the 512-byte NV block at offset 0x1C5 into 0x20008D50 (ble_nv_read_block_1c5) and copies its first 0x1DA bytes to 0x20008FE4. It sets the advertising name with bt_app_set_name_and_advdata, runs ble_219_0c0592a4(2) and ble_219_0c02bdd0 (both undescribed here), and calls app_set_default_cfg_ptr.

**Notes:** The callers of this function are not in this packet. Its callback set is a subset of the one in ble_app_main_init.

- Addresses by version: 219: 0x0C02973C
- Calls: `bt_app_set_name_and_advdata`, `app_set_default_cfg_ptr`, `ble_crypto_init`, `ble_set_word_1308c`, `ble_set_indexed_word_1307c`, `ble_set_mode_14_or_16`, `ble_host_start`, `ble_link_table_nv_load_trim`, `ble_cb_slot_14608_set`, `ble_cb_slot_15e5c_set`, `ble_nv_read_block_1c5`, `memcpy`
- Confidence: medium

## ble_app_magic_caf_check

**Check the 32-bit magic 0x00464143 ('CAF') at 0x2000F3B4, gated by request 0x101**

Returns true when the word at 0x2000F3B4 equals 0x00464143, which reads 'C', 'A', 'F', 0 in memory. The app device request 0x101 (FUN_0C041E10) runs first, and false is returned if it fails. The word sits directly after the 40-byte block of ble_app_block40_f38c_read, so it is probably that block's validity tag; this is an inference.

**Returns** `bool`: true when the gate passes and the magic matches

- Addresses by version: 219: 0x0C045F60
- Called by: `ble_factory_test_dispatch_query`, `ble_host_start`
- Calls: `app_dev_ioctl_cmd_101`
- Confidence: medium

## ble_app_main_init

**Main BLE app init: identity, callbacks, default FMNA token, NV block, and the 500 ms app poll timer**

Runs the full application init in order. It writes the 0x19 0x02 header with app_fill_hdr_19_02, calls ble_219_0c055610(0x108) (undescribed), then ble_nv_identity_init, ble_get_bluetooth_pn, mode 14, ble_device_info_init and the RX handler. It registers the connect status callbacks and several more hooks (0x0C02913C, 0x0C028F80, 0x0C028EAC, 0x0C028FE4, 0x0C029068, 0x0C028A64), sets the speed-limit RX hook DAT_200091E4 to 0x0C0288DD, and stores two more callbacks at DAT_200091D8 and DAT_200091DC. It logs 'set_fmna_default_token' and copies the 0xD2-byte default Find My token from flash 0x0C0822C0. It then reads and copies the NV block as in ble_app_init_callbacks_nv, sets the advertising name, signals the event object at 0x20008F94 (ble_signal_event_8f94), and sets DAT_20008F6C and DAT_20008F84 when the status returned by ble_219_0c046884 is 1 or 3. Last it creates the 'app poll timer' (FreeRTOS software timer, 500 ms, auto-reload, handler 0x0C028C95 = ble_app_poll_tick) and starts it.

**Notes:** The undescribed callbacks at 0x0C02913C, 0x0C028F80, 0x0C028EAC, 0x0C028FE4, 0x0C029068 and 0x0C028A64 are only listed, not analysed. The FreeRTOS timer creation call is shown as FUN_0c044c7c and is presumed to be xTimerCreate.

- Addresses by version: 219: 0x0C0297B0
- Calls: `bt_app_set_name_and_advdata`, `ble_nv_identity_init`, `ble_get_bluetooth_pn`, `app_set_default_cfg_ptr`, `ble_signal_event_8f94`, `app_fill_hdr_19_02`, `ble_device_info_init`, `ble_crypto_init`, `ble_gpio_dev_open`, `trace_printf`, `prvInitialiseMutex`, `xTaskGetTickCount`, `xTimerCreate`, `xTimerGenericCommand`, `app_boot_reason_decode`, `ble_host_stage_blob` ...
- Confidence: medium

## ble_app_marker_o_check

**Report whether the marker byte at 0x2000F36B is 'o', gated by request 0x101**

Returns true when the byte at 0x2000F36B equals the ASCII character 'o' (0x6F). The app device request 0x101 (FUN_0C041E10) runs first, and false is returned if it fails. It is the second of the two marker characters at 0x2000F36A/0x2000F36B tested by ble_app_marker_s_check, which probably tag a valid app-side record; that role is a guess.

**Returns** `bool`: true when the gate passes and the byte is 'o'

- Addresses by version: 219: 0x0C045F40
- Called by: `ble_factory_test_dispatch_query`
- Calls: `app_dev_ioctl_cmd_101`
- Confidence: medium

## ble_app_marker_s_check

**Report whether the marker byte at 0x2000F36A is 'S', gated by request 0x101**

Returns true when the byte at 0x2000F36A equals the ASCII character 'S' (0x53). The app device request 0x101 (FUN_0C041E10) runs first, and false is returned if it fails. This byte and the byte at 0x2000F36B ('o', tested by ble_app_marker_o_check) are two single-character markers that probably tag a valid app-side record; that role is a guess.

**Returns** `bool`: true when the gate passes and the byte is 'S'

- Addresses by version: 219: 0x0C045F04
- Called by: `ble_factory_test_dispatch_query`, `bt_drv_rf_2168_update_from_src`
- Calls: `app_dev_ioctl_cmd_101`
- Confidence: medium

## ble_app_poll_tick

**500 ms app poll: VCU wake retries, NV save, power-off countdown, 15-minute battery poll**

Callback of the 500 ms auto-reload software timer 'app poll timer' created by ble_app_main_init. It increments the tick counter DAT_200091E0 on every call. It sends VCU command 0x1C with payload 2 up to three times (counter DAT_200092D0). When DAT_20008F7B is set it runs ble_219_0c05a91c(1, 0), clears the header fields of the 0x20008FE4 block and 0x33 bytes at 0x20008FF5, writes 0x1DA bytes of the block to NV with ble_nv_write_block_1c5, and clears the flag. On even ticks, while DAT_20009280 is zero, it sends command 0x10 with payload 0x0E, waits 5 ticks with vTaskDelay, and sends 0x1C again. When DAT_20008F73 is set it runs the VCU power-off step (log 'vcu power off', command 0x1C, timer 0x20009254 re-armed) using DAT_20003E1C as a countdown. When ble_status_bits_get is non-zero and the tick counter is in 0x707 to 0x709 it sends command 0x55 with payload 2 to ask for the battery level; 0x707 to 0x709 is 1800 ticks, which is 15 minutes at 500 ms, and the counter wraps at 0x709. Every tick it drives the GPIO with app_gpio_dev_ioctl(0x500, BLE connected bit). Finally, when DAT_20008F7A is set it polls the unlock state for three ticks and sends command 0x7B with payload 1 ('open unlock state') or 0 ('dis-open unlock state').

**Notes:** The 500 ms period and 1800-tick cycle come from the timer creation and the tick constants. The meaning of VCU commands 0x1C, 0x10, 0x55 and 0x7B is inferred from their payloads and log messages.

- Addresses by version: 219: 0x0C028C94
- Calls: `app_get_scooter_state`, `uart_bridge_send_frame`, `app_gpio_dev_ioctl`, `trace_printf`, `vTaskDelay`, `ble_host_timer_restart`, `ble_event_count_reached_check`, `ble_link_table_release`, `ble_nv_write_block_1c5`, `ble_status_bits_get`, `memset`
- Confidence: medium

## ble_app_start_deferred_500ms_op

**Store an operation (id, mapped type code, args) in 0x200170d0.. and arm a 500 ms timer**

Saves a pending operation in a global context block: DAT_200170d0 = param_1 (u16 id), DAT_200170d4 = param_3, DAT_200170d8 = (u16)param_4 and DAT_200170d2 = a code derived from the high byte of *param_2: if *param_2 == 0x1ff it is first replaced in place by the default/current value DAT_20012310; then 0x1xx -> 0x1f, 0x2xx -> 0x22, 0x3xx -> 0x25, 0x4xx -> 0x28, anything else -> 0. Finally ble_host_timer_restart(&DAT_200170dc, 500, 0x0c05c90c|1) schedules the handler at 0x0c05c90c to run 500 ms later with that context. Always returns 0. Called from 0c053f74.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | operation id, stored at 0x200170d0 |
| `param_2` | `ptr` | in/out u16 selector; 0x1ff is replaced by DAT_20012310; high byte picks the code |
| `param_3` | `u32` | stored verbatim at 0x200170d4 |
| `param_4` | `u32` | low 16 bits stored at 0x200170d8 |

**Returns** `u32`: always 0

**Notes:** What the selector (0x1xx..0x4xx) and the 0x1f/0x22/0x25/0x28 codes (step 3) represent is unknown; the timer handler 0x0c05c90c is not in this packet.

- Addresses by version: 219: 0x0C05CB08
- Called by: `ble_app_queue_message`
- Calls: `ble_host_timer_restart`
- Confidence: low

## ble_app_word_f360_read

**Read the 32-bit word at 0x2000F360, gated by request 0x101 (length must be 4)**

Gated read of the 32-bit RAM word at 0x2000F360 into the caller's pointer. The app device request 0x101 (FUN_0C041E10) runs first and its error is returned on failure, and the call is rejected with -EINVAL unless the length is exactly 4. The word is only read here; the code that writes it is elsewhere and its meaning is not established. Callers are at 0x0C02CCA8 and 0x0C03E5DC.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output u32 |
| `param_2` | `s32` | requested length, must be 4 |

**Returns** `s32`: 0 on success, -22 for a wrong length, or the ioctl error

- Addresses by version: 219: 0x0C045E04
- Called by: `ble_factory_test_dispatch_query`, `bt_drv_rf_2168_update_from_src`
- Calls: `app_dev_ioctl_cmd_101`
- Confidence: low

## ble_crypto_nv_store_blob

**Store a blob in NV record 0x1389 and write the validity marker 0xEA to record 0xFAA**

Clears the validity flag DAT_200170CD and calls the unnamed 0c053EE4, then writes param_2 bytes from param_1 to NV record 0x1389 with ble_nv_record_write. If all bytes were written it writes the one-byte marker 0xEA to NV record 0xFAA, sets DAT_200170CD to 1, notifies through 0c055440(0x11) and returns 0. Otherwise it clears the flag, notifies with the same call and returns 0x0C.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | blob to store |
| `param_2` | `u32` | blob length |

**Returns** `u32`: 0 when the blob and marker were written, 0x0C when the write fell short

**Notes:** The blob is probably the protected serial-number or pairing secret; record meanings are inferred. Record 0x1389 is not described in this packet.

- Addresses by version: 219: 0x0C05C8A8
- Called by: `ble_token_chunk_rx_7e`, `ble_secure_ctx_restore_from_nv`
- Calls: `ble_secure_blob_wipe_1k`, `ble_evt_post_u16`, `ble_nv_record_write`
- Confidence: medium

## ble_crypto_set_serial_number

**Copy up to 16 bytes into the vehicle serial-number buffer at 0x20004980**

If param_2 > 16 it returns without doing anything; otherwise memcpy(DAT_20004980, param_1, param_2). The 16-byte global at 0x20004980 holds the scooter serial number (default contents "NBNAGBH2053CE905"), which the ble_crypto_* authentication uses together with the password. Called from 0c0296c4 (serial number received from the VCU / configuration). A shorter length does not clear the remaining bytes and no terminator is written.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source bytes (serial number ASCII) |
| `param_2` | `u32` | length, 0..16 |

- Addresses by version: 219: 0x0C05C888
- Called by: `ble_get_bluetooth_pn`
- Calls: `memcpy`
- Confidence: high

## ble_device_info_init

**Fill the BLE identity block at 0x200091E8 with a code, model 0x219, address, unique ID and serial**

Takes the packed word from ble_get_packed_word_12cb0 (global 0x20012CB0) and stores a 16-bit code at 0x200091E8, whose high byte is bits 19:16 and whose low byte is bits 11:8 and 3:0 of that word. It writes the constant 0x219 (the BLE_219 image id) at 0x200091EA and fills the 6-byte field at 0x200091EC through ble_219_0c058160. The chip unique ID goes to the 16 bytes at 0x200091F2 via app_get_unique_id16, a 16-byte value from ble_219_0c045d60 goes to 0x20009202, and the 16-byte vehicle serial string literal at 0x20004980 is copied to 0x20009212 with memcpy. The whole block spans 0x200091E8 to 0x20009221.

**Notes:** The 6-byte field at 0x200091EC is probably the Bluetooth device address, which is not verified. The meaning of the packed code and of the 16-byte value from ble_219_0c045d60 is unknown.

- Addresses by version: 219: 0x0C02B158
- Called by: `ble_app_main_init`, `ble_device_info_read_cmd`
- Calls: `app_get_unique_id16`, `ble_app_block16_f36c_read`, `ble_get_packed_word_12cb0`, `ble_random_bytes_6`, `memcpy`
- Confidence: high

## ble_device_info_read_cmd

**Read a slice of the BLE identity block at 0x200091E8 and reply on the app or UART channel**

Only the read operation (param_4 equal to 1) does anything. It refreshes the identity block with ble_device_info_init. If param_5 plus half the requested length is below 0x1E, it sends the slice starting at offset param_5 with the length taken from *param_6 to the BT app (param_1 equal to 1, through ble_219_0c02c338) or through uart_bridge_send_frame. A request for offset 0x50 always sends the fixed reply 0x90. An offset that is too large logs 'ERROR: read data len too large' when param_5 is below 0x1D and returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | reply channel: 1 means the BT app, any other value means the UART bridge |
| `param_2` | `u32` | address byte used in the reply header |
| `param_3` | `u32` | second address byte used in the reply header |
| `param_4` | `s32` | operation, only 1 (read) is handled |
| `param_5` | `u8` | offset into the identity block |
| `param_6` | `ptr:u8` | pointer to the requested length byte |

**Returns** `u32`: 1 when a reply was sent, 0 otherwise

**Notes:** The meaning of the halved length check is taken from the arithmetic. The fixed 0x90 reply at offset 0x50 is not explained by the packet.

- Addresses by version: 219: 0x0C02B1B4
- Called by: `ble_uart_frame_route`, `ble_vcu_cmd_handle`
- Calls: `ble_device_info_init`, `uart_bridge_send_frame`, `ble_uart_frame_enqueue`, `trace_printf`
- Confidence: medium

## ble_device_name_setup

**Set the BLE advertising name from the serial number and a per-model name template**

Reads the 16-byte vehicle serial number from app block 0x2000F3B8 (ble_app_block16_f3b8_read) and logs it. If its first word is 0xFFFFFFFF or 0 it uses the default '1K1E9999999999' and writes that back with ble_219_0c045fd4 (undescribed). It stores 15 serial bytes into the link table at offset 0x18 (ble_link_table_write_at18). It then builds the name from one of four templates chosen by param_1: 1 and 3 copy 0x18 bytes from flash tables at 0x0C077724 and 0x0C077738; 2 uses an inline binary prefix followed by the text 'way E-bi' and 'ke'; any other value uses an inline 0x16-byte template. Four serial-derived bytes are placed at the end of the name (offset 0x11 to 0x13 depending on the template). The name is logged as bt_app_set_name and written to the link table at offset 0 with ble_link_table_write_at0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | name template selector: 1, 2, 3, or any other value for the default template |

**Notes:** The flash templates at 0x0C077724 and 0x0C077738 and the binary prefix bytes are not decoded. The exact offsets of the serial-derived bytes are read from the decompile and may be off by one.

- Addresses by version: 219: 0x0C0292F0
- Called by: `bt_app_set_name_and_advdata`
- Calls: `trace_printf`, `ble_app_block16_f3b8_read`, `ble_cfg_set_bytes_f3b8`, `ble_link_table_write_at18`, `ble_link_table_write_at0`
- Confidence: medium

## ble_event_window_expire

**Expire old entries of the 10-slot event ring and count them into two tallies**

Works on a ring of ten 27-byte records: a flag byte at offset 0 (value 9 marks one event kind, anything else the other) and a 32-bit timestamp at offset 0x13. The reference time is the monotonic clock (FUN_0c03feac with id 4, when param_1 is 0), otherwise the timestamp of the record at the head index 0x20013235. Starting at the tail index 0x2001311F, it walks entries that are at least 300 time units older than the reference. Each expired entry increments the tally at 0x2001322F (flag 9) or 0x200130FC (other), records the first expired timestamp in 0x20013230 or 0x20013100, and decrements the pending count at 0x20013234. It stops at the first younger entry and commits the new tail index. Only caller: ble_219_0c0585a4.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 0 = use the current clock as the reference; otherwise use the head entry timestamp |

**Notes:** The 300 threshold unit is presumably milliseconds. The meaning of the two tallies is not established from this function alone.

- Addresses by version: 219: 0x0C0582B0
- Called by: `ble_link_param_monitor_step`
- Calls: `clock_gettime`
- Confidence: medium

## ble_get_bluetooth_pn

**Read the 14-character Bluetooth part number from app block 0x2000F3B8 and store it as the serial**

Reads 14 bytes from app block 0x2000F3B8 into offset 2 of a 16-byte buffer (ble_app_block16_f3b8_read). Each byte must be a digit or an upper-case letter other than I and O. On success the first two bytes are set to 'N' and 'B' (0x4E 0x42), the 16-byte result is stored as the vehicle serial number with ble_crypto_set_serial_number, and the function returns 0. A bad byte or a failed read logs 'get_bluetooth_pn err.' and returns 1.

**Returns** `u32`: 0 on success, 1 when the part number is missing or malformed

**Notes:** The 'NB' prefix is written as a constant. Called from ble_app_main_init.

- Addresses by version: 219: 0x0C0296C4
- Called by: `ble_app_main_init`
- Calls: `trace_printf`, `ble_app_block16_f3b8_read`, `ble_crypto_set_serial_number`
- Confidence: high

## ble_init_cfg_ptr_store

**Init step: run ble_219_0c037a2c on the .data base, then store a flash config pointer**

Calls ble_219_0c037a2c (undescribed here) with the .data base address 0x20003D88 and then calls ble_set_var_2000f64c with the address of the flash constant at 0x0C076FD8. As a result the global at 0x2000F64C holds the address of that constant table. It is called from ble_219_0c047fec during startup and returns nothing.

**Notes:** The purpose of the table at 0x0C076FD8 and of ble_219_0c037a2c is not established in this packet.

- Addresses by version: 219: 0x0C0286E0
- Called by: `app_system_init`
- Calls: `nb_upgrade_init`, `ble_set_var_2000f64c`
- Confidence: medium

## ble_log_data_send

**Send one type-4 log record from ring 0x20014670 to the state handle**

Takes the log semaphore 0x20014620 with a 100-tick timeout and logs 'ble_log_data_send sem timeout' when it fails. It reads a 4-byte record header from the 0x20014670 ring: the low 16 bits are the payload length and byte 2 is the record type. Records shorter than 252 bytes are read in full and the semaphore is given back; a read that returns a different length logs 'read real data len not match'. Type-4 records are sent with the unnamed 0c04EBC0 (opcode 0x44) to the handle at state+0x12 unless that handle is 0xFF; other types are consumed without sending. When more than 4 bytes remain it stores its own entry (0x0C05AB05) in DAT_20015F30 as a continuation marker and, if bit 16 of DAT_200042FC is set, calls 0c04EB8C to notify. Records of 252 bytes or more are drained in 251-byte pieces and logged as 'data too large'.

**Notes:** Unnamed: 0c04EBC0 (message send with handle, opcode, payload, length), 0c04EB8C (notify), 0c035D0C (debug print). The header layout and opcode 0x44 are read from the code; the purpose of the channel is inferred from the strings.

- Addresses by version: 219: 0x0C05AB04
- Calls: `trace_printf`, `xQueueGenericSend`, `xQueueSemaphoreTake`, `ble_host_att_queue_send`, `ble_host_att_send_notification`, `ble_get_state_ptr_42f8`, `btstack_ring_buffer_bytes_available`, `btstack_ring_buffer_read`
- Confidence: medium

## ble_log_print_timestamped

**Format a log line into a 256-byte buffer and print it with an hh:mm:ss.mmm stamp**

Formats param_2 (format string) with the argument param_3 into the 256-byte static buffer at 0x20015F44 through the unnamed formatter 0c071FBC. It reads the current time from btstack_run_loop_get_time_ms, splits it into hours (seconds / 3600), minutes, seconds and milliseconds, and prints '[%02u:%02u:%02u.%03u] ' followed by 'LOG -- %s' through 0c035D0C. param_1 is not used in the body. The shared buffer makes it non-reentrant.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | unused in this body |
| `param_2` | `ptr` | printf-style format string |
| `param_3` | `u32` | first format argument; further variadic arguments are not visible in the decompile |

**Notes:** 0c071FBC and 0c035D0C are unnamed here. The stamp layout is read from the format string.

- Addresses by version: 219: 0x0C05B5E4
- Calls: `trace_printf`, `btstack_run_loop_get_time_ms`, `ble_219_0c071fbc`
- Confidence: medium

## ble_log_typed_send

**Send one log record from ring 0x20015538 with opcode 0x31, 0x39 or 0x3E by type**

Works like ble_log_data_send on its own ring 0x20015538 and semaphore 0x200154E8 (100-tick take). The record type in byte 2 of the 4-byte header picks the message opcode: type 2 gives 0x31, type 1 gives 0x39, type 3 gives 0x3E; other types are dropped after the semaphore is given back. The payload goes to the handle at state+0x10 through 0c04EBC0. When more than 4 bytes remain it sets DAT_20015F3C to its own entry (0x0C05AC21) and, if bit 0 of DAT_200042FC is set, calls 0c04EB8C with the handle. Records of 252 bytes or more are drained and not sent.

**Notes:** Opcode mapping and header layout are read from the code. The meaning of the three opcodes is not established.

- Addresses by version: 219: 0x0C05AC20
- Calls: `xQueueGenericSend`, `xQueueSemaphoreTake`, `ble_host_att_queue_send`, `ble_host_att_send_notification`, `ble_get_state_ptr_42f8`, `btstack_ring_buffer_bytes_available`, `btstack_ring_buffer_read`
- Confidence: medium

## ble_nb_block_copy_in

**Copy n bytes from the source into the RAM block at 0x200042E0**

Calls memcpy(0x200042E0, param_1, param_2) with no size check against the destination. The destination's image bytes start with 4E 42 40 00 00 00 00 BF ('NB@' ...), which suggests a Ninebot-specific configuration record, but its layout is not decoded here. Callers include ble_219_0c029414 (not yet described).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source buffer |
| `param_2` | `u32` | byte count |

- Addresses by version: 219: 0x0C0567C8
- Called by: `bt_app_set_name_and_advdata`
- Calls: `memcpy`
- Confidence: medium

## ble_nv_identity_init

**Validate the NV identity records (PPID, model name, category flag) and write defaults if bad**

Loads the 8-byte PPID record from NV 0xFA8, the 16-byte device name from NV 0xFA6 and the category flag from NV 0xFA7 (ble_nv_load_8byte_block, ble_nv_load_device_name, ble_nv_load_flag_byte). A PPID whose first word is 0xFFFFFFFF or 0 is logged as 'ppid err', a name with the same first-word test is logged as 'model name err', and a flag outside 0x86 and 0x87 is logged as 'category name err'. If all three are valid the function returns without writing. Otherwise it writes the defaults: device name 'KickScooter' padded to 16 bytes (ble_nv_store_device_name), the 8-byte identity DC D4 64 E9 BC CE 4E 89 (ble_nv_store_8byte_block), and the flag 0x87 (ble_nv_store_flag_byte).

**Notes:** The record IDs come from the callee summaries. The default name string is the literal 'KickScooter' in the decompile. Called from ble_app_main_init.

- Addresses by version: 219: 0x0C0295E0
- Called by: `ble_app_main_init`
- Calls: `trace_printf`, `ble_nv_store_8byte_block`, `ble_nv_load_8byte_block`, `ble_nv_store_flag_byte`, `ble_nv_load_flag_byte`, `ble_nv_store_device_name`, `ble_nv_load_device_name`
- Confidence: high

## ble_nv_load_8byte_block

**Load the 8-byte NV record 0xFA8 into a caller buffer**

Reads 8 bytes from NV record 0xFA8 (partition 2 offset 0x3C5) into dst through ble_nv_record_read. The read result is ignored, so dst is left unchanged on failure. Used by the GATT read path for selector 10.

| Parameter | Type | Description |
|---|---|---|
| `dst` | `ptr` | 8-byte destination buffer |

- Addresses by version: 219: 0x0C05CE48
- Called by: `ble_nv_identity_init`, `ble_fmna_cmd_handler`, `ble_fmna_adv_payload_init`, `ble_fmna_state_save`, `ble_fmna_debug_cmd_dispatch`, `ble_gatt_read_char_value`
- Calls: `ble_nv_record_read`
- Confidence: high

## ble_nv_load_device_name

**Read the 16-byte device name from NV record 0xFA6 and return its length**

Reads 16 bytes from NV record 0xFA6 (partition 2 offset 0x3CD) into buf through ble_nv_record_read, then returns strlen of buf as a byte. The caller must provide a zeroed or NUL-terminated buffer, since strlen can run past 16 bytes if no terminator is present. The GATT read path zeroes 40 bytes before calling.

| Parameter | Type | Description |
|---|---|---|
| `buf` | `ptr` | destination buffer, at least 17 bytes, zeroed by the caller |

**Returns** `u8`: strlen of the stored name, truncated to a byte

- Addresses by version: 219: 0x0C05CEA8
- Called by: `ble_nv_identity_init`, `ble_fmna_cmd_handler`, `ble_fmna_debug_cmd_dispatch`, `ble_gatt_read_char_value`
- Calls: `ble_nv_record_read`, `strlen`
- Confidence: high

## ble_nv_load_flag_byte

**Read the one-byte flag from NV record 0xFA7, or 0 on failure**

Reads one byte from NV record 0xFA7 (partition 2 offset 0x12B) through ble_nv_record_read. The local value starts at 0, so a failed read returns 0.

**Returns** `u8`: flag byte, or 0 when the read fails

- Addresses by version: 219: 0x0C05CE74
- Called by: `ble_nv_identity_init`, `ble_fmna_cmd_handler`, `ble_fmna_adv_payload_init`, `ble_fmna_debug_cmd_dispatch`, `ble_gatt_read_char_value`
- Calls: `ble_nv_record_read`
- Confidence: high

## ble_nv_read_block_1c5

**Read the 512-byte block at NV partition 2 offset 0x1C5**

Locks NV partition 2 (ioctl 0x106), copies 512 bytes from the RAM image at offset 0x1C5 into the caller buffer, and unlocks with 0x103 (argument 0). It issues no commit ioctls, so it is a read-only operation.

| Parameter | Type | Description |
|---|---|---|
| `dst` | `ptr` | destination buffer of at least 512 bytes |

**Returns** `u32`: 0 on success; 1 when the partition buffer is not available

- Addresses by version: 219: 0x0C05B0F4
- Called by: `ble_app_init_callbacks_nv`, `ble_app_main_init`
- Calls: `nvdata_ioctl_get_buf_0x102`, `nvdata_ioctl_unlock_0x103`, `nvdata_ioctl_lock_0x106`, `memcpy`
- Confidence: high

## ble_nv_record_read

**Read a record from its NV partition offset by record id**

Read counterpart of ble_nv_record_write with the same record-id-to-offset map. It locks the partition (0x106), copies length bytes from the partition RAM image into dst, and unlocks (0x103) without the commit ioctls. It returns true only when a mapped partition is not open. Unknown ids return false and leave dst untouched.

| Parameter | Type | Description |
|---|---|---|
| `record_id` | `u32` | record id, same map as ble_nv_record_write |
| `length` | `u32` | byte count to read |
| `dst` | `ptr` | destination buffer |

**Returns** `bool`: true when the partition is not open, false otherwise

- Addresses by version: 219: 0x0C05B380
- Called by: `ble_link_table_nv_load_trim`, `ble_status_bits_get`, `ble_mode_nv_decode_read`, `ble_mode_nv_is_inactive`, `ble_mode_nv_disable`, `ble_mode_nv_enable`, `ble_nv_load_8byte_block`, `ble_nv_load_flag_byte`, `ble_nv_load_device_name`, `ble_cfg_block_load`, `ble_mode_state_update`
- Calls: `nvdata_ioctl_get_buf_0x102`, `nvdata_ioctl_unlock_0x103`, `nvdata_ioctl_lock_0x106`, `memcpy`
- Confidence: high

## ble_nv_record_write

**Write a record to its NV partition offset by record id, then commit**

Maps a record id to an NV partition and offset, locks the partition with ioctl 0x106, copies length bytes from src into the partition RAM image, unlocks with 0x103 and commits with 0x104 and 0x200. Known ids: 0xFA6 partition 2 +0x3CD (device name, up to 16 bytes); 0xFA7 +0x12B (one-byte flag); 0xFA8 +0x3C5 (8-byte block); 0xFA9 +0x12A (one-byte mode byte); 0xFAA +0x129; 0xFAB +0x128; 0xFAC (default) +0; 0xFAD..0xFB2 +0x3C, +0x5C, +0x7C, +0x9C, +0xCC, +0xEC; 0xFB3 +0x12C (link table block); 0x1388 +0x1C5 (512-byte block); 0x1389 partition 1 offset 0 (1040-byte configuration block). Unknown ids return 0 and touch nothing. It returns length on success, or 0 when the partition is not open.

| Parameter | Type | Description |
|---|---|---|
| `record_id` | `u32` | record id, for example 0xFA6..0xFB3, 0x1388 or 0x1389 |
| `length` | `u32` | byte count to write |
| `src` | `ptr` | source buffer |

**Returns** `u32`: bytes written, or 0 for an unknown id or closed partition

**Notes:** The meaning of most record ids is inferred from their use by callers, not confirmed. Partition numbers 1 and 2 come from the ioctl argument.

- Addresses by version: 219: 0x0C05B138
- Called by: `ble_slot_mgr_set_ready`, `ble_fmna_reset_gen_keypair`, `ble_secure_ctx_restore_from_nv`, `ble_record_a_derive_and_commit`, `ble_record_b_derive_and_commit`, `ble_host_rx_msg_dispatch`, `ble_fmna_debug_cmd_dispatch`, `ble_link_table_remove_index`, `ble_link_table_remove_key`, `ble_link_table_nv_load_trim`, `ble_link_table_reset`, `ble_link_table_save` ...
- Calls: `nvdata_ioctl_cmd_0x200`, `nvdata_ioctl_get_buf_0x102`, `nvdata_ioctl_cmd_0x104`, `nvdata_ioctl_unlock_0x103`, `nvdata_ioctl_lock_0x106`, `memcpy`
- Confidence: high

## ble_nv_store_8byte_block

**Store an 8-byte block to NV record 0xFA8 (length must be 8)**

Writes the 8-byte block at src to NV record 0xFA8 (partition 2 offset 0x3C5) through ble_nv_record_write. It does nothing unless len equals 8. This is read back by ble_nv_load_8byte_block.

| Parameter | Type | Description |
|---|---|---|
| `src` | `ptr` | 8-byte source block |
| `len` | `s32` | must be 8 |

- Addresses by version: 219: 0x0C05CE38
- Called by: `ble_nv_identity_init`, `ble_fmna_cmd_handler`, `ble_fmna_debug_cmd_dispatch`
- Calls: `ble_nv_record_write`
- Confidence: high

## ble_nv_store_device_name

**Store a device name of up to 16 bytes in NV record 0xFA6**

Writes len bytes from name to NV record 0xFA6 (partition 2 offset 0x3CD) through ble_nv_record_write. Names longer than 16 bytes are rejected by doing nothing. The stored value is read back by ble_nv_load_device_name and used by the GATT device name path.

| Parameter | Type | Description |
|---|---|---|
| `name` | `ptr` | name bytes |
| `len` | `u32` | byte count, at most 16 |

- Addresses by version: 219: 0x0C05CE98
- Called by: `ble_nv_identity_init`, `ble_fmna_cmd_handler`, `ble_fmna_debug_cmd_dispatch`
- Calls: `ble_nv_record_write`
- Confidence: high

## ble_nv_store_flag_byte

**Store one flag byte to NV record 0xFA7**

Writes the one-byte value to NV record 0xFA7 (partition 2 offset 0x12B) through ble_nv_record_write. Read back by ble_nv_load_flag_byte.

| Parameter | Type | Description |
|---|---|---|
| `value` | `u8` | flag byte to store |

- Addresses by version: 219: 0x0C05CE54
- Called by: `ble_nv_identity_init`, `ble_fmna_cmd_handler`, `ble_fmna_debug_cmd_dispatch`
- Calls: `ble_nv_record_write`
- Confidence: high

## ble_nv_write_block_1c5

**Write up to 512 bytes into NV partition 2 at offset 0x1C5, then commit**

Copies len bytes (at most 0x200) from src into the RAM image of NV partition 2 at offset 0x1C5. It locks the partition with ioctl 0x106, copies, unlocks with 0x103 (argument 0), then issues the commit sequence 0x104 and 0x200 (flush). It returns len on success, or 0 when the length is too large or the partition is not open. This is the same block as NV record id 0x1388 in ble_nv_record_write.

| Parameter | Type | Description |
|---|---|---|
| `src` | `ptr` | source buffer |
| `len` | `u32` | byte count, at most 0x200 |

**Returns** `u32`: bytes written, or 0 on failure

- Addresses by version: 219: 0x0C05B0A8
- Called by: `ble_app_poll_tick`, `ble_payload_copy_and_schedule`, `ble_process_autokey`, `ble_vcu_cmd_handle`
- Calls: `nvdata_ioctl_cmd_0x200`, `nvdata_ioctl_get_buf_0x102`, `nvdata_ioctl_cmd_0x104`, `nvdata_ioctl_unlock_0x103`, `nvdata_ioctl_lock_0x106`, `memcpy`
- Confidence: high

## ble_nvdata_init

**Create the 5-entry request queue and the 'nvdata' task (0x100 stack words, priority 3)**

Creates a static queue of five 4-byte items with ble_219_0c042ba0 and stores the handle in DAT_20009CBC. The packet names that callee prvInitialiseNewQueue, but its five-argument form matches xQueueGenericCreateStatic. It then creates the static task named 'nvdata' through ble_219_0c043cfc with entry 0x0C02DC50, a stack depth of 0x100 words, priority 3, stack buffer 0x200098A8 and TCB 0x20004A18, and stores the handle in DAT_200098A4. It always returns 0 and checks neither creation result.

**Returns** `u32`: always 0

**Notes:** ble_219_0c043cfc is assumed to be xTaskCreateStatic from its seven arguments. The 'nvdata' name suggests non-volatile storage, but the worker body is not in this packet.

- Addresses by version: 219: 0x0C02D724
- Calls: `prvInitialiseNewQueue`, `xTaskCreateStatic`
- Confidence: medium

## ble_process_autokey

**Store the autokey record in the NV block and switch the RX state to 3**

Logs 'process_autokey' and sends a fixed 5-byte reply 00 04 3E 5C 01 through ble_219_0c02c338. It then copies the autokey fields from 0x20009450, 0x20009454, 0x20009458 and 0x2000945C into the 0x1DA-byte block at 0x20008FE4 (type byte 0x3D plus the four words) and writes that block to NV with ble_nv_write_block_1c5. It finally sets the RX state DAT_200092EC to 3 (autokey pending), so that ble_rx_data_handler routes the next data frame to ble_219_0c02be44.

**Notes:** The meaning of the 0x3D type byte and of the four words is inferred from the copy.

- Addresses by version: 219: 0x0C02A3C4
- Called by: `ble_vcu_cmd_handle`
- Calls: `ble_uart_frame_enqueue`, `trace_printf`, `ble_nv_write_block_1c5`
- Confidence: medium

## ble_proto_dispatch_op

**Dispatch protocol sub-opcodes 0x1F and 0x20..0x29 to their handlers, always return 0**

A switch on the sub-opcode in param_2: 0x1F calls 0c053F24 with param_6 and param_5; 0x22 calls 0c054180, 0x25 calls 0c05420C and 0x28 calls 0c0540F4 with the sub-code 9 (0x28 - 0x1F) and param_4. The group 0x20, 0x23, 0x26 and 0x29 calls the unnamed 0c065B38 with the payload pointer and 0, which releases or acknowledges it. Other values do nothing. Returns 0 on every path.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | context passed to the handlers |
| `param_2` | `s32` | sub-opcode |
| `param_3` | `u32` | unused in this body |
| `param_4` | `u32` | passed to the 0x28 handler |
| `param_5` | `ptr` | payload pointer |
| `param_6` | `u16` | 16-bit argument passed to the 0x1F, 0x22, 0x25 and 0x28 handlers |

**Returns** `u32`: always 0

**Notes:** The protocol is not identified in this packet; the 0x1F..0x29 step pattern suggests message families with per-family handlers. No direct callers in the packet.

- Addresses by version: 219: 0x0C05CA80
- Calls: `ble_host_rx_chunk_handle`, `ble_app_frame_dispatch_406`, `ble_app_frame_dispatch_20b`, `ble_app_frame_dispatch_302`, `co_read16_le`
- Confidence: low

## ble_record_a_derive_and_commit

**Reload record A, derive its 28-byte and 16-byte blocks and commit them to NV**

Reloads record A at 0x200101E4 (ble_219_0c05bcc0) and, on success, derives a 28-byte block at 0x20012B90 from it with ble_219_0c05bd30 (parameter block 0x20012220). On success the 32-bit generation counter at 0x20012B8C is incremented, the 28-byte block is passed through ble_219_0c065c88, and a 16-byte block at 0x20012BAC is derived with ble_219_0c05bce4 and passed through ble_219_0c065c88 and ble_219_0c053740. Record A is then written to NV 0xFAD (ble_nv_record_write, 32 bytes) and the 48-byte composite [counter, 28-byte block, 16-byte block] starting at 0x20012B8C is written to NV 0xFB0. The empty hook ble_hook_noop_05cba8 runs last and the function returns 0; any failed step returns 0xC without writing NV.

**Returns** `u32`: 0 on success, 0xC if a reload or derive step fails (no NV write)

**Notes:** Helpers ble_219_0c05bd30, ble_219_0c05bce4, ble_219_0c065c88 and ble_219_0c053740 are not described yet; the meaning of the 28-byte and 16-byte blocks is inferred from where they are stored.

- Addresses by version: 219: 0x0C053D04
- Called by: `ble_record_sync_step`
- Calls: `ble_host_cache_key16`, `ble_nv_record_write`, `ble_crypto_kdf_update`, `ble_crypto_kdf_connect`, `ble_crypto_diversify`, `ble_hook_noop_05cba8`, `printf_hexdump`
- Confidence: medium

## ble_record_a_reload

**Reload the 32-byte record at 0x200101E4 from its backing store into RAM**

Reads the 32-byte record through ble_219_0c05bcc0, which takes the record address and returns the content in a caller buffer. Only when that read returns 0 are the eight words copied into the RAM copy at 0x200101E4..0x20010200; on failure the RAM copy is left unchanged. The function writes the 8 global words and returns 0, or 0xC on read failure. The backing store behind ble_219_0c05bcc0 is not described yet.

**Returns** `u32`: 0 on success, 0xC if the read fails

- Addresses by version: 219: 0x0C053C94
- Calls: `ble_crypto_kdf_update`
- Confidence: medium

## ble_record_b_derive_and_commit

**Reload record B, derive its 28-byte block, bump its counter and commit to NV**

Reloads record B at 0x20010204 (ble_219_0c05bcc0) and derives a 28-byte block at 0x20012BC0 from it with ble_219_0c05bd30 (parameter block 0x20012220). On success the 32-bit counter at 0x20012BBC is incremented, the block is passed through ble_219_0c065c88, and two NV records are written: record B itself to 0xFAE (ble_nv_record_write, 32 bytes) and the 32-byte composite [counter, 28-byte block] to 0xFB1. Returns 0 on success and 0xC if the reload or the derive step fails, with no NV write on failure.

**Returns** `u32`: 0 on success, 0xC if the reload or derive step fails

- Addresses by version: 219: 0x0C053DA4
- Called by: `ble_record_sync_step`
- Calls: `ble_nv_record_write`, `ble_crypto_kdf_update`, `ble_crypto_diversify`, `printf_hexdump`
- Confidence: medium

## ble_record_b_reload

**Reload the 32-byte record at 0x20010204 from its backing store into RAM**

Same pattern as ble_record_a_reload for the second 32-byte record at 0x20010204..0x20010220: read through ble_219_0c05bcc0 into a stack buffer and copy the eight words into RAM only when the read returns 0. Returns 0 on success and 0xC on read failure, with the RAM copy untouched on failure. The helper ble_219_0c05bcc0 is shared with the record A reload and is not described yet.

**Returns** `u32`: 0 on success, 0xC if the read fails

- Addresses by version: 219: 0x0C053CCC
- Calls: `ble_crypto_kdf_update`
- Confidence: medium

## ble_record_sync_step

**Advance the record A sync step: derive record A, sync record B, post a kick**

Scheduled sync step. It copies the target generation from 0x20012C7C to 0x20012B7C, calls ble_219_0c043f1c, runs ble_record_a_derive_and_commit, calls ble_219_0c043f1c again, and passes 0x20012B90 to ble_219_0c065c88. It returns early, without posting, unless the record A generation at 0x20012B8C now equals the target. When the state byte at 0x20012C80 is 2, the word at 0x20012B88 is cleared and the 48-byte block at 0x20012BDC is zeroed. It then computes page = generation / 0x60 + 1; if the record B counter at 0x20012BBC is below page it runs ble_record_b_derive_and_commit and sets the counter to page. Finally it calls ble_219_0c043f1c, passes the 4-byte block at 0x20012BC0 to ble_219_0c065c88 and posts a zero-length packet with handler LAB_0C054904 through ble_pktq_enqueue.

**Notes:** The meaning of ble_219_0c043f1c (called around the record work) and of the 96-byte page size is inferred from the arithmetic only.

- Addresses by version: 219: 0x0C055330
- Called by: `ble_record_sync_tick`
- Calls: `xTaskGetTickCount`, `ble_pktq_enqueue`, `ble_record_a_derive_and_commit`, `ble_record_b_derive_and_commit`, `printf_hexdump`, `memset`
- Confidence: medium

## ble_record_sync_tick

**Run one record sync step, latch slot 0xFE flag bit 5 and post event 2**

Periodic tick entry; it has no direct callers. It calls ble_219_0c043f1c, runs ble_record_sync_step, stores the result of ble_slot_test_flag_any(0xFE, 5) in byte 0x20012B84, and posts the 16-bit value 2 through ble_pktq_enqueue with the same completion handler LAB_0C0554F4 used by ble_evt_post_u16.

- Addresses by version: 219: 0x0C0553D0
- Calls: `xTaskGetTickCount`, `ble_pktq_enqueue`, `ble_slot_test_flag_any`, `ble_record_sync_step`
- Confidence: medium

## ble_slot_store_and_queue

**Store a (u16, u16) record in the next slot and queue it when a slot is in use**

Gets the slot index from ble_counter_20012344_step (0x0c05cb88). Writes the two u16 arguments into the 4-entry table at 0x2001231C, 4 bytes per entry (param_3 at +0, param_4 at +2). If ble_slot_count_used (0x0c05341c) reports a non-zero count, it queues the 4-byte record as a message with code param_1 through ble_app_queue_message (0x0c053f74), using param_2 as the context. Callers: ble_219_0c053018, ble_219_0c054668 and ble_219_0c054734.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | message code used when queueing |
| `param_2` | `u32` | context passed to ble_app_queue_message |
| `param_3` | `u16` | first value, stored at +0 of the slot entry |
| `param_4` | `u16` | second value, stored at +2 of the slot entry |

- Addresses by version: 219: 0x0C054298
- Called by: `ble_slot_cmd_dispatch`, `ble_app_req_302_handle`, `ble_app_req_406_handle`
- Calls: `ble_slot_count_used`, `ble_app_queue_message`, `ble_counter_20012344_step`
- Confidence: medium

## ble_speed_limit_code_check

**Check received bytes for the speed-limit removal token and acknowledge it with frame 0x82**

Installed as the RX hook at DAT_200091E4 by ble_app_main_init, so it runs on received data. It does nothing when bit 1 of the u16 at state+0x38 is set. If the u16 at state+0x3A is zero it searches the buffer (util_find_str_in_buf) for the fixed 10-character token 'pWEwvenFz9'. Otherwise it derives a 10-byte token from that u16: byte 0 is the low byte plus 0x48, followed by seven bytes from the high byte plus the constants 0x45, 0x91, 0xE0, 0x37, 0x8E, 0xDD, 0x2F, and then two more bytes (high byte plus 0x7B and high byte minus 0x41), the token being NUL terminated. When the token is found it sends frame 0x82 with the payload 0x02 to the VCU through uart_bridge_send_frame and logs 'REMOVE LIMIT SPD CODE SEND'. The non-zero branch also logs the derived token and the received bytes in hex.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | received buffer, searched for the token |
| `param_2` | `u32` | length of the received buffer in bytes |

**Notes:** The token derivation is read directly from the arithmetic. What the token protects (the speed limiter, its challenge) is inferred from the log strings only.

- Addresses by version: 219: 0x0C0288DC
- Calls: `util_find_str_in_buf`, `app_get_scooter_state`, `uart_bridge_send_frame`, `trace_printf`
- Confidence: medium

## ble_unlock_record_get

**Log the autokey and seat-key unlock records and return the record block address**

Logs two unlock records with their times. The first is the autokey index (byte 0 of 0x200092A8) with the time stored at 0x20009298, and the second is the seat-key index (byte 1 of 0x200092A8) with the time at 0x200092A0. It returns &DAT_20009298, the start of the 16-byte unlock record block, so the caller can read or copy it. No state is changed.

**Returns** `ptr`: pointer to the unlock record block at 0x20009298

**Notes:** Times are logged with %ld from 32-bit words, so the time fields are probably 8 bytes each.

- Addresses by version: 219: 0x0C02A430
- Calls: `trace_printf`
- Confidence: medium

## ble_unlock_request_start

**Start an unlock request when state bit 1 is set: arm a 5 s timeout and run the auth callback**

Returns 0 unless bit 1 of the state byte at 0x20009288 is set. If the pending word at 0x20008F69 is zero it stores param_1 OR 0x80 there and arms a one-shot 5000 ms timeout with app_req_timeout_timer_start. It then calls ble_event_count_reached_check. If the event threshold is not reached it returns 0. Otherwise it sets bit 6 (0x40) of 0x20008F69 and calls ble_unlock_auth_cb. The function always returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | request source tag, OR-ed with 0x80 into the pending word |

**Returns** `u32`: always 0

**Notes:** The return value is always 0 regardless of the unlock outcome.

- Addresses by version: 219: 0x0C02A8A0
- Called by: `ble_vcu_cmd_handle`
- Calls: `ble_unlock_auth_cb`, `app_req_timeout_timer_start`, `ble_event_count_reached_check`
- Confidence: high

## ble_vcu_cmd_handle

**Dispatch class 9 and 0x16 command frames to their unlock, pairing, telemetry and ack handlers**

Command dispatcher for two frame classes passed in param_1: class 9 (commands 0x58, 0x5E, 0x5F, 0x75) and class 0x16 (commands 0x66, 0x02 and 0x03, 0x04, 0x05, 0x7A, 0x7B), with the index byte selecting the sub-command. Before the class switch it offers the frame to ble_token_chunk_rx_7e in reply mode 2, then to ble_219_0c02b1b4 and ble_219_0c02a8f8, and returns true as soon as one of them consumes it. The pairing material written by 0x5E index 3 is 48 bytes, three 16-byte keys stored after a one-byte state at 0x20008FF5, 0x20009006 and 0x20009017, where '=' marks a valid key; a key equal to 16 ASCII zeros is cleared with ble_219_0c05a91c, and the 474-byte block at 0x20008FE4 is committed with ble_nv_write_block_1c5. Class 0x16 command 0x04 stores telemetry words (indices 0x40, 0x7D and 0xE0 into 0x20009290, 0x2000928C and 0x2000928E, the VCU state word at 0x20009288 with index 0x1C, and a battery byte mapped to level 3 below 20, 2 below 50, 1 below 80 and 0 otherwise), and index 0x10 validates a 14-byte serial with app_sn_prefix_whitelist_match, compares it with the stored copy and writes it with ble_219_0c045fd4 at most once (RAM flag 0x20009280). Power and unlock (command 0x02 or 0x03, index 0x51) take a sub-command from payload byte 0: 0 power off, 1 power on (arms a 5-unit timer with ble_host_timer_restart and handler 0x0C02A35D), 2 pre-power-on (checks link state and unlock conditions), 3 read the VCU serial; autokey (index 0x61, bit 0x20 of a u16) and seat (index 0x1D, bit 0x4000) record xTaskGetTickCount timestamps and arm ble_app_arm_4s_deadline. Replies are UART frames sent with ble_219_0c02c124, and the class 0x16 command 0x05 acknowledgements clear pending-request flags under the semaphore at 0x20008F94.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | frame class: 9 or 0x16; other values fall through and return false |
| `param_2` | `u32` | address byte passed to the sub-handlers |
| `param_3` | `u32` | command byte |
| `param_4` | `u32` | index byte, the sub-command or request code |
| `param_5` | `u8` | payload length in bytes |
| `param_6` | `ptr` | payload bytes |

**Returns** `bool`: true if the frame was consumed (handled or acknowledged), false otherwise

**Notes:** Uncertain points: on the class 9 command 0x75 path the code stores a byte (bVar1) that is not assigned on that path in the decompile, likely a decompiler artifact. The meanings of the unlock flags (0x20008F7A, 0x20008F71, 0x20008F72) are inferred from names only. The log 'All Bluetooth connections have been disconnected' is printed when a link entry with state 1 is found and DAT_200092C4 bits 0x9 are clear, which contradicts the text. The class 9 index 1 copy of 16 bytes into 0x200092B0 has no length check. The battery thresholds are probably state-of-charge percent but this is not confirmed.

- Addresses by version: 219: 0x0C02B480
- Calls: `app_sn_prefix_whitelist_match`, `ble_process_autokey`, `ble_unlock_request_start`, `ble_fmna_cmd_handler`, `ble_device_info_read_cmd`, `ble_token_chunk_rx_7e`, `uart_bridge_send_frame`, `trace_printf`, `ble_boot_mode_set`, `xQueueGenericSend`, `xQueueSemaphoreTake`, `xTaskGetTickCount`, `ble_app_block16_f3b8_read`, `ble_cfg_set_bytes_f3b8`, `ble_link_table_find_by_key`, `ble_host_timer_restart` ...
- Confidence: medium

## ble_vcu_wakeup_retry

**Timer step that re-sends a VCU wake request up to three times while the VCU is in low power**

When the retry count at 0x200092D2 is not 3 and DAT_20008F70 is zero, it sends VCU command 0x1C with payload 2 through uart_bridge_send_frame, increments the retry count, logs 'Wake up low power to get vcu status' and re-arms the timer at 0x20009254 with itself as handler and period 5. Otherwise it clears the retry count and DAT_20008F70, which ends the sequence.

**Notes:** The log format has a %d for the count but the call passes no argument, so the decompile is missing it.

- Addresses by version: 219: 0x0C02A35C
- Calls: `uart_bridge_send_frame`, `trace_printf`, `ble_host_timer_restart`
- Confidence: medium

## ble_version_info_print

**Print the version and build records for Application, LibWhale, Miniboot and LibWhale in Miniboot**

Prints a version table framed by separator lines. It calls app_cmd_complete_signal first. For each of four components it prints the component name followed by 'Build' and 'Version' from a record: the Application record at 0x0C076FF0 and the LibWhale record at 0x0C082270, then, for Miniboot and LibWhale in Miniboot, the records returned by bes_boot_param_get (DAT_20000180 and DAT_20000184). A missing record prints 'Unknown'. The build field is read from record offset +8 and the version from +4.

**Returns** `u32`: always 0

**Notes:** Which literal belongs to which record is not confirmed. The strings referenced here include '1.9.175((ZT3PRO_V0.2.1.8_20240815w33_hotfix)...)' and '2024-08-15 06:26:32'.

- Addresses by version: 219: 0x0C041E38
- Calls: `app_cmd_complete_signal`, `trace_printf`, `bes_boot_param_get`
- Confidence: medium

## bt_app_set_name_and_advdata

**Pick the vendor adv-data entry for the serial number, set the 8-byte identity and CRC-32**

Reads the 16-byte serial number with ble_app_block16_f3b8_read, using the same '1K1E9999999999' fallback as ble_device_name_setup. It then searches the flash table at 0x0C080DD4 (13-byte entries: index byte, 4-byte prefix, 8-byte identity; the count is DAT_20003E1D) with memcmp, comparing 3 or 4 prefix bytes depending on the fourth prefix byte. On a match it logs the advertising payload and copies the 8-byte identity into 0x200042E0 with ble_nb_block_copy_in. If nothing matches it searches the RAM copy at 0x20009028 (up to 30 entries) the same way, but only for entries whose first two identity bytes are 'N' and 'B' or 'N' and 'C'. The matched entry's index byte, if non-zero, is passed to ble_device_name_setup. Finally DAT_200091C0 is set to the CRC-32 of serial bytes 2 to 13 with the non-standard polynomial 0x4E494E45 (crc32_compute_poly). If no entry matches it only logs 'vendor adv data is null'.

**Notes:** The DAT_200091C0 value is consumed by ble_unlock_auth_cb. The table layout is read from the stride of 13 and the offsets used in the log format.

- Addresses by version: 219: 0x0C029414
- Called by: `ble_app_init_callbacks_nv`, `ble_app_main_init`
- Calls: `ble_device_name_setup`, `crc32_compute_poly`, `trace_printf`, `ble_app_block16_f3b8_read`, `ble_cfg_set_bytes_f3b8`, `ble_nb_block_copy_in`, `memcmp`
- Confidence: medium

## nvdata_device_init

**Open one nvdata device, build its item index and locate the newest valid item**

Initialises one nvdata device (index 0..3, read through the u16 that param_1+0x10 points to) from a 0x18-byte device table at 0x0C082D0C: path at +0, area offset at +4, area size at +8, item size at +0xE, state pointer at +0x10 and mode flag at +0x14. It opens the path, creates a recursive mutex in the state block (state+4, prvInitialiseMutex type 4) and keeps the fd at state+0x54. Mode 0 scans every item slot (size / item size) with ble_219_0c02d784 and keeps the valid item with the highest 14-bit serial, compared modulo 16384. Mode non-zero first sizes a bitmap index from the sector geometry (ioctl 0x100), then checks the 0x55AAAA55 magic at the area start and binary-searches 4-byte index words with util_ctz32 to find the newest item; if the magic or that item is missing it falls back to a scan and, failing that, rebuilds the index. Results: state+0x56 is the current index (-1 if none), state+0x58 the serial (low 14 bits), and param_1+0xC receives the index. Returns 0, or -19 for a bad device index or a failed open.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | request record: +0x0C receives the current item index, +0x10 points to the u16 device index, +0x14 receives the state pointer |

**Returns** `s32`: 0 on success, -19 (-ENODEV) for a device index above 3 or a failed open

**Notes:** Mode-flag semantics, the bitmap bit meaning and the rebuild path are inferred from the code, not from hardware. ble_219_0c02d870, ble_219_0c02db00 and ble_219_0c071a80 (device seek/lock helper) are not yet named. The prvInitialiseMutex result is not checked.

- Addresses by version: 219: 0x0C02DEA8
- Calls: `ble_nvdata_read_record`, `ble_nvdata_sector_header_write`, `ble_nvdata_slot_mark_used`, `trace_printf`, `util_ctz32`, `prvInitialiseMutex`, `xQueueGiveMutexRecursive`, `xQueueTakeMutexRecursive`, `_close`, `ble_219_0c071a80`, `ble_219_0c071a94`, `read`, `write`
- Confidence: medium

## nvdata_ioctl_cmd_0x104

**Send ioctl 0x104 (no argument) to /dev/nvdata<idx>, issued after an update before flush**

Reads the fd byte at DAT_2000989c + 3 + param_1 (fds of /dev/nvdata1..3 at 0x200098a0..) and, if non-zero, calls the VFS ioctl dispatcher 0x0c0484b4(fd, 0x104, 0); no-op otherwise. In the writers 0x0c05b0a8 and 0x0c05b138 it is always called right after nvdata_ioctl_unlock_0x103 and right before nvdata_ioctl_cmd_0x200, and never in the read-only path 0x0c05b0f4, so it most likely marks the partition image dirty / recomputes its checksum before the flush.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | nvdata partition index (1..3) |

**Notes:** Semantics inferred from call order only.

- Addresses by version: 219: 0x0C02D6CC
- Called by: `ble_nv_write_block_1c5`, `ble_nv_record_write`
- Calls: `_close`
- Confidence: low

## nvdata_ioctl_cmd_0x200

**Send ioctl 0x200 (no argument) to /dev/nvdata<idx>, used last in a write sequence (flush)**

Reads the file descriptor byte at DAT_2000989c + 3 + param_1 (the fds of /dev/nvdata1..3 opened by 0x0c02d604 and stored at 0x200098a0..0x200098a2) and, if non-zero, calls the VFS ioctl dispatcher 0x0c0484b4(fd, 0x200, 0). Does nothing when the partition was not opened. Part of the nvdata access group with nvdata_ioctl_lock_0x106, nvdata_ioctl_get_buf_0x102, nvdata_ioctl_unlock_0x103 and nvdata_ioctl_cmd_0x104: writers (0x0c05b0a8, 0x0c05b138) run lock -> get_buf -> memcpy into the buffer -> unlock -> 0x104 -> 0x200, so 0x200 is most likely 'flush the RAM copy to flash'.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | nvdata partition index (1..3) |

**Notes:** Command semantics (flush/sync) inferred only from the call order in the writers; the nvdata driver itself was not examined.

- Addresses by version: 219: 0x0C02D688
- Called by: `ble_nv_write_block_1c5`, `ble_nv_record_write`
- Calls: `_close`
- Confidence: low

## nvdata_ioctl_get_buf_0x102

**ioctl 0x102 on /dev/nvdata<idx>: return the driver's RAM buffer pointer for the partition**

Looks up the fd byte at DAT_2000989c + 3 + param_1 (fds of /dev/nvdata1..3 at 0x200098a0..). If it is non-zero, calls the VFS ioctl dispatcher 0x0c0484b4(fd, 0x102, &out) and returns the 32-bit value the driver wrote into out; returns 0 when the partition is not open. All callers (0x0c05b0a8, 0x0c05b0f4, 0x0c05b138, 0x0c05b380) use the result as a base pointer for memcpy at fixed offsets (+0x3c, +0x5c, ..., +0x1c5, +0x3c5), so the value is the address of the partition's in-RAM image. Used between nvdata_ioctl_lock_0x106 and nvdata_ioctl_unlock_0x103.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | nvdata partition index (1..3) |

**Returns** `ptr`: pointer to the partition's RAM image, or 0 if not opened

**Notes:** Command number meaning inferred from how the callers use the returned value.

- Addresses by version: 219: 0x0C02D6A4
- Called by: `ble_nv_write_block_1c5`, `ble_nv_read_block_1c5`, `ble_nv_record_write`, `ble_nv_record_read`
- Calls: `_close`
- Confidence: medium

## nvdata_ioctl_lock_0x106

**ioctl 0x106 with an argument on /dev/nvdata<idx>; returns -5 if the partition is not open**

Reads the fd byte at DAT_2000989c + 3 + param_1 (fds of /dev/nvdata1..3 at 0x200098a0..). If non-zero, returns the result of the VFS ioctl dispatcher 0x0c0484b4(fd, 0x106, param_2); otherwise returns 0xfffffffb (-5, EIO-style error). All callers invoke it first with param_2 = 0xffffffff (looks like 'wait forever') before nvdata_ioctl_get_buf_0x102 and finish with nvdata_ioctl_unlock_0x103(idx, 0), so 0x106 is most likely 'acquire the partition with timeout'. Callers: 0x0c05b0a8 (write 0x1da-byte record at +0x1c5), 0x0c05b0f4 (read 0x200 bytes from +0x1c5), 0x0c05b138 and 0x0c05b380 (field-wise read/write of partition 2, and partition 1 for id 0x1389).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | nvdata partition index (1..3) |
| `param_2` | `u32` | ioctl argument; callers pass 0xffffffff |

**Returns** `s32`: ioctl result, or -5 (0xfffffffb) when the partition is not open

**Notes:** Lock semantics inferred from call order only; the only certain facts are the fd lookup and the command number.

- Addresses by version: 219: 0x0C02D704
- Called by: `ble_nv_write_block_1c5`, `ble_nv_read_block_1c5`, `ble_nv_record_write`, `ble_nv_record_read`
- Calls: `_close`
- Confidence: low

## nvdata_ioctl_unlock_0x103

**ioctl 0x103 with an argument on /dev/nvdata<idx>; callers pass 0 after finishing buffer access**

Reads the fd byte at DAT_2000989c + 3 + param_1 (fds of /dev/nvdata1..3 at 0x200098a0..) and, if non-zero, calls the VFS ioctl dispatcher 0x0c0484b4(fd, 0x103, param_2); no-op otherwise. Every caller (0x0c05b0a8, 0x0c05b0f4, 0x0c05b138, 0x0c05b380) issues it with param_2 = 0 after it is done copying to or from the buffer obtained with nvdata_ioctl_get_buf_0x102, and after having taken the partition with nvdata_ioctl_lock_0x106(idx, -1); it therefore looks like the release/unlock counterpart of 0x106.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | nvdata partition index (1..3) |
| `param_2` | `u32` | ioctl argument (callers pass 0) |

**Notes:** Lock/unlock pairing of 0x106/0x103 is inferred from call order only.

- Addresses by version: 219: 0x0C02D6E8
- Called by: `ble_nv_write_block_1c5`, `ble_nv_read_block_1c5`, `ble_nv_record_write`, `ble_nv_record_read`
- Calls: `_close`
- Confidence: low
