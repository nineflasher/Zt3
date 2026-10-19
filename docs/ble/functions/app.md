# BLE - `app` functions

40 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`app_adv_id_block_copy`](#app_adv_id_block_copy) | 0x0C029224 | Copy n bytes out of the global block at 0x20009028 (read as 'ADV_ID' by the status readers) |
| [`app_ble_cmd_fe_rx_stats_update`](#app_ble_cmd_fe_rx_stats_update) | 0x0C029CA8 | Count received 5A A5 ... FE 02 frames and accumulate their byte length |
| [`app_ble_rx_pre_hook_stub`](#app_ble_rx_pre_hook_stub) | 0x0C0291FC | Empty hook that returns 0, called at the start of the BLE data-receive handler |
| [`app_boot_reason_decode`](#app_boot_reason_decode) | 0x0C046884 | Map the BES boot flag word to a small application reset-reason code |
| [`app_dev_ioctl_cmd_101`](#app_dev_ioctl_cmd_101) | 0x0C041E10 | Issue request 0x101 with a 20-byte stack argument on the global device handle DAT_20003EC8, else -EIO |
| [`app_fill_hdr_19_02`](#app_fill_hdr_19_02) | 0x0C02B14C | Write the two bytes 0x19, 0x02 into the buffer passed in |
| [`app_get_scooter_state`](#app_get_scooter_state) | 0x0C02A464 | Return pointer to the application state block at 0x20009288 |
| [`app_get_unique_id16`](#app_get_unique_id16) | 0x0C045AB0 | Fill a 16-byte buffer with the chip/flash unique ID via the RAM-patched reader |
| [`app_gpio_dev_ioctl`](#app_gpio_dev_ioctl) | 0x0C02D5EC | ioctl on the /dev/gpio file descriptor with request 0x1010000 \| param_1 |
| [`app_hook_noop`](#app_hook_noop) | 0x0C029738 | Empty function (single return) |
| [`app_magic_flag_is_set`](#app_magic_flag_is_set) | 0x0C041D10 | Test whether the 0x5a465459 magic flag in DAT_2000018c is armed |
| [`app_magic_flag_set`](#app_magic_flag_set) | 0x0C041CF8 | Set or clear the 0x5a465459 magic flag word depending on param_1==1 |
| [`app_req_timeout_timer_start`](#app_req_timeout_timer_start) | 0x0C02C0B8 | Arm the one-shot BTstack timer at 0x20009460 with a timeout in ms (handler 0x0c02c090) |
| [`app_set_default_cfg_ptr`](#app_set_default_cfg_ptr) | 0x0C02A46C | Store the pointer to a constant table (0x0c082508) into DAT_20009480 |
| [`app_set_word_2000de84`](#app_set_word_2000de84) | 0x0C0454B4 | Store param_1 into the global word DAT_2000de84 |
| [`app_set_word_2000de88`](#app_set_word_2000de88) | 0x0C0454C0 | Store param_1 into the global word DAT_2000de88 |
| [`app_sn_prefix_whitelist_match`](#app_sn_prefix_whitelist_match) | 0x0C02A2E0 | Return 1 if a received serial number starts with a code from the ROM or RAM prefix list |
| [`app_stub_return_zero_0c0454cc`](#app_stub_return_zero_0c0454cc) | 0x0C0454CC | Stub returning 0, only reachable indirectly |
| [`ble_app_arm_4s_deadline`](#ble_app_arm_4s_deadline) | 0x0C05A1D8 | On mode 1: set a 4000-tick deadline, flag 0x200145a9=1 and snapshot the two event counters |
| [`ble_app_get_status_code`](#ble_app_get_status_code) | 0x0C05CC8C | Derive a 0..4 status code from flag bits 7 and 14 of 0x200042fc and the byte at 0x20017046 |
| [`ble_app_start_deferred_500ms_op`](#ble_app_start_deferred_500ms_op) | 0x0C05CB08 | Store an operation (id, mapped type code, args) in 0x200170d0.. and arm a 500 ms timer |
| [`ble_crypto_set_serial_number`](#ble_crypto_set_serial_number) | 0x0C05C888 | Copy up to 16 bytes into the vehicle serial-number buffer at 0x20004980 |
| [`ble_event_window_expire`](#ble_event_window_expire) | 0x0C0582B0 | Expire old entries of the 10-slot event ring and count them into two tallies |
| [`ble_nb_block_copy_in`](#ble_nb_block_copy_in) | 0x0C0567C8 | Copy n bytes from the source into the RAM block at 0x200042E0 |
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
| [`ble_slot_store_and_queue`](#ble_slot_store_and_queue) | 0x0C054298 | Store a (u16, u16) record in the next slot and queue it when a slot is in use |
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
- Called by: `ble_219_0c02a8f8`, `ble_219_0c02cca8`
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
- Called by: `ble_219_0c029df8`
- Confidence: medium

## app_ble_rx_pre_hook_stub

**Empty hook that returns 0, called at the start of the BLE data-receive handler**

Stub that returns 0 with no side effects. It is called first by the BLE application receive handler (0x0c029df8) before the packet is decrypted/dispatched, apparently a placeholder for an optional pre-processing hook; the return value is ignored by the caller.

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C0291FC
- Called by: `ble_219_0c029df8`
- Confidence: high

## app_boot_reason_decode

**Map the BES boot flag word to a small application reset-reason code**

Reads bes_boot_flag_get() (DAT_20000188) and returns: 5 if bit 0 is set; else 1 if bit 1 is set; else, if byte 1 (bits 15..8) equals 1, 4 when bit 16 is set and 3 otherwise; else 0. The application init routine 0x0c0297b0 treats codes 1 and 3 ((code & 0xfd) == 1) specially by setting DAT_20008f6c = 0x13 and DAT_20008f84 = 0, i.e. a reboot caused by the previous firmware (e.g. after an upgrade or software reset) changes the start-up state.

**Returns** `u32`: reset-reason code 0, 1, 3, 4 or 5

**Notes:** Meaning of the individual flag bits is not documented; code values are only known from this decoder and its caller.

- Addresses by version: 219: 0x0C046884
- Called by: `ble_219_0c0297b0`
- Calls: `bes_boot_flag_get`
- Confidence: medium

## app_dev_ioctl_cmd_101

**Issue request 0x101 with a 20-byte stack argument on the global device handle DAT_20003EC8, else -EIO**

If the global descriptor DAT_20003EC8 (an fd/handle from the '/dev/...' device layer, valid when > 0) is open, calls 0x0c0484b4(DAT_20003EC8, 0x101, &buf) where buf is an uninitialised 20-byte stack area and returns its result; otherwise returns -5 (-EIO). The eight small callers 0x0c045d60 ... 0x0c045fa8 are device-control wrappers of the same module. The handle is opened elsewhere by the file-descriptor layer that prints '/dev/%s%d' and 'Unsupport: /dev/%s%d reopen'.

**Returns** `s32`: result of the request, or -5 (0xfffffffb, -EIO) when the handle is not open

**Notes:** 0x0c0484b4 is assumed to be the ioctl-like entry of the LibWhale device layer; command 0x101 and the argument structure are unknown.

- Addresses by version: 219: 0x0C041E10
- Called by: `ble_219_0c045d60`, `ble_219_0c045db0`, `ble_219_0c045e04`, `ble_219_0c045e74`, `ble_219_0c045f04`, `ble_219_0c045f40`, `ble_219_0c045f60`, `ble_219_0c045fa8`
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
- Called by: `ble_219_0c0297b0`
- Confidence: low

## app_get_scooter_state

**Return pointer to the application state block at 0x20009288**

Returns the constant address &DAT_20009288. The returned block is used by the BLE connection-status callback (0x0c0287ac), which sets/clears bit 0 (BLE connected) and bit 3 (classic BT connected) of the word at offset 0x3c, and by four other app routines.

**Returns** `ptr`: pointer to the app state structure (DAT_20009288)

**Notes:** Only the +0x3c connection flags field is seen in this packet's callers.

- Addresses by version: 219: 0x0C02A464
- Called by: `ble_219_0c0287ac`, `ble_219_0c0288dc`, `ble_219_0c028ad4`, `ble_219_0c028c94`, `ble_219_0c029960`
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
- Called by: `ble_219_0c02b158`, `ble_219_0c02cca8`
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
- Called by: `ble_219_0c028c94`
- Calls: `_close`
- Confidence: medium

## app_hook_noop

**Empty function (single return)**

Contains only a return instruction. Called once from 0x0c02a8f8 as a do-nothing callback/hook slot; no state is touched.

- Addresses by version: 219: 0x0C029738
- Called by: `ble_219_0c02a8f8`
- Confidence: high

## app_magic_flag_is_set

**Test whether the 0x5a465459 magic flag in DAT_2000018c is armed**

Returns true when the RAM word DAT_2000018c equals the magic value 0x5a465459, i.e. when app_magic_flag_set(1) was last called. Pure getter, no side effects. Called from ble_219_0c02c49c and ble_219_0c02cca8.

**Returns** `bool`: true if the magic flag is armed

- Addresses by version: 219: 0x0C041D10
- Called by: `ble_219_0c02c49c`, `ble_219_0c02cca8`
- Confidence: medium

## app_magic_flag_set

**Set or clear the 0x5a465459 magic flag word depending on param_1==1**

Writes the magic constant 0x5a465459 (bytes 'Y','T','F','Z' in memory) to the RAM word DAT_2000018c when param_1 == 1, otherwise writes 0. Together with app_magic_flag_is_set it implements a persistent boolean flag held in an early .data word that survives as a magic-value rather than a plain 0/1. The meaning of the flag (probably a boot/factory/mode switch) is not visible from this function; its only caller is ble_219_0c02c49c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 1 = arm the flag; any other value clears it |

**Notes:** Purpose of the flag inferred only from the magic value; not confirmed.

- Addresses by version: 219: 0x0C041CF8
- Called by: `ble_219_0c02c49c`
- Confidence: medium

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
- Called by: `ble_219_0c02a8a0`
- Calls: `btstack_run_loop_set_timer_handler`, `btstack_run_loop_set_timer`, `btstack_run_loop_add_timer`, `btstack_run_loop_remove_timer`
- Confidence: medium

## app_set_default_cfg_ptr

**Store the pointer to a constant table (0x0c082508) into DAT_20009480**

Writes the flash address 0x0c082508 into the RAM pointer DAT_20009480. It is called from the application init routines (0x0c02973c and 0x0c0297b0). Note that the CRC32 table built by crc32_make_table lives at 0x20009484, immediately after this pointer, so the pointer and the table are adjacent globals. The pointed-to data is not interpreted here.

**Notes:** What 0x0c082508 contains (default configuration / token table?) was not examined.

- Addresses by version: 219: 0x0C02A46C
- Called by: `ble_219_0c02973c`, `ble_219_0c0297b0`
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
- Called by: `ble_219_0c02b480`
- Calls: `memcmp`
- Confidence: medium

## app_stub_return_zero_0c0454cc

**Stub returning 0, only reachable indirectly**

Two-instruction function that just returns 0; no direct callers, so it is a default callback/ops-table entry that reports success or 'nothing'.

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C0454CC
- Confidence: high

## ble_app_arm_4s_deadline

**On mode 1: set a 4000-tick deadline, flag 0x200145a9=1 and snapshot the two event counters**

If param_1 == 1 it stores xTaskGetTickCount() + 4000 into DAT_200145ac (a deadline 4 s ahead at the 1 ms tick) and sets the u8 DAT_200145a9 = 1. Then, depending on the flag word at 0x200042fc (state+4): if bit 3 is set DAT_200130ed = state[0x38] (the counter at 0x20004330), and if bit 0 is set DAT_200130ec = state[0x1f] (the counter at 0x20004317), so the current event counts are latched when the window starts. For any other param_1 value it merely rewrites DAT_200145a9 with its previous value (no change). Always returns 0. Called from 0c02b480 together with ble_host_timer_restart.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 1 = start the 4 s window; other values are no-ops |

**Returns** `u32`: always 0

**Notes:** Purpose of the 4 s window (0x200145ac/0x200145a9) is inferred from the constant 4000 and FreeRTOS tick use; the consumer of the deadline is not in this packet.

- Addresses by version: 219: 0x0C05A1D8
- Called by: `ble_219_0c02b480`
- Calls: `xTaskGetTickCount`, `ble_get_state_ptr_42f8`
- Confidence: medium

## ble_app_get_status_code

**Derive a 0..4 status code from flag bits 7 and 14 of 0x200042fc and the byte at 0x20017046**

Reads the flag word at state+4 (0x200042fc). Result starts at 0. If bit 7 is set, result = DAT_20017046 but forced back to 0 unless it is 1, 2 or 3. If bit 14 is set the result is overridden to 4. Called from 0c02a8f8 together with ble_state_407a_copy, ble_flags_bit15_get and ble_flags_bit4_get, which together assemble a status report (probably for the VCU UART protocol).

**Returns** `u32`: 0 (idle/none), 1..3 (from 0x20017046 when flag bit 7), 4 (when flag bit 14)

**Notes:** Semantics of bits 7/14 and of 0x20017046 are not named yet.

- Addresses by version: 219: 0x0C05CC8C
- Called by: `ble_219_0c02a8f8`
- Calls: `ble_get_state_ptr_42f8`
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

## ble_crypto_set_serial_number

**Copy up to 16 bytes into the vehicle serial-number buffer at 0x20004980**

If param_2 > 16 it returns without doing anything; otherwise memcpy(DAT_20004980, param_1, param_2). The 16-byte global at 0x20004980 holds the scooter serial number (default contents "NBNAGBH2053CE905"), which the ble_crypto_* authentication uses together with the password. Called from 0c0296c4 (serial number received from the VCU / configuration). A shorter length does not clear the remaining bytes and no terminator is written.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source bytes (serial number ASCII) |
| `param_2` | `u32` | length, 0..16 |

- Addresses by version: 219: 0x0C05C888
- Called by: `ble_219_0c0296c4`
- Calls: `memcpy`
- Confidence: high

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

## ble_nb_block_copy_in

**Copy n bytes from the source into the RAM block at 0x200042E0**

Calls memcpy(0x200042E0, param_1, param_2) with no size check against the destination. The destination's image bytes start with 4E 42 40 00 00 00 00 BF ('NB@' ...), which suggests a Ninebot-specific configuration record, but its layout is not decoded here. Callers include ble_219_0c029414 (not yet described).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source buffer |
| `param_2` | `u32` | byte count |

- Addresses by version: 219: 0x0C0567C8
- Called by: `ble_219_0c029414`
- Calls: `memcpy`
- Confidence: medium

## ble_nv_load_8byte_block

**Load the 8-byte NV record 0xFA8 into a caller buffer**

Reads 8 bytes from NV record 0xFA8 (partition 2 offset 0x3C5) into dst through ble_nv_record_read. The read result is ignored, so dst is left unchanged on failure. Used by the GATT read path for selector 10.

| Parameter | Type | Description |
|---|---|---|
| `dst` | `ptr` | 8-byte destination buffer |

- Addresses by version: 219: 0x0C05CE48
- Called by: `ble_219_0c0295e0`, `ble_219_0c02a8f8`, `ble_219_0c052ee4`, `ble_219_0c053954`, `ble_219_0c055b90`, `ble_gatt_read_char_value`
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
- Called by: `ble_219_0c0295e0`, `ble_219_0c02a8f8`, `ble_219_0c055b90`, `ble_gatt_read_char_value`
- Calls: `ble_nv_record_read`, `strlen`
- Confidence: high

## ble_nv_load_flag_byte

**Read the one-byte flag from NV record 0xFA7, or 0 on failure**

Reads one byte from NV record 0xFA7 (partition 2 offset 0x12B) through ble_nv_record_read. The local value starts at 0, so a failed read returns 0.

**Returns** `u8`: flag byte, or 0 when the read fails

- Addresses by version: 219: 0x0C05CE74
- Called by: `ble_219_0c0295e0`, `ble_219_0c02a8f8`, `ble_219_0c052ee4`, `ble_219_0c055b90`, `ble_gatt_read_char_value`
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
- Called by: `ble_219_0c02973c`, `ble_219_0c0297b0`
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
- Called by: `ble_link_table_nv_load_trim`, `ble_status_bits_get`, `ble_mode_nv_decode_read`, `ble_mode_nv_is_inactive`, `ble_mode_nv_disable`, `ble_mode_nv_enable`, `ble_nv_load_8byte_block`, `ble_nv_load_flag_byte`, `ble_nv_load_device_name`, `ble_cfg_block_load`, `ble_219_0c05cf1c`
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
- Called by: `ble_219_0c05376c`, `ble_219_0c0537b4`, `ble_219_0c053a48`, `ble_219_0c053d04`, `ble_219_0c053da4`, `ble_219_0c05486c`, `ble_219_0c055b90`, `ble_link_table_remove_index`, `ble_link_table_remove_key`, `ble_link_table_nv_load_trim`, `ble_link_table_reset`, `ble_link_table_save` ...
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
- Called by: `ble_219_0c0295e0`, `ble_219_0c02a8f8`, `ble_219_0c055b90`
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
- Called by: `ble_219_0c0295e0`, `ble_219_0c02a8f8`, `ble_219_0c055b90`
- Calls: `ble_nv_record_write`
- Confidence: high

## ble_nv_store_flag_byte

**Store one flag byte to NV record 0xFA7**

Writes the one-byte value to NV record 0xFA7 (partition 2 offset 0x12B) through ble_nv_record_write. Read back by ble_nv_load_flag_byte.

| Parameter | Type | Description |
|---|---|---|
| `value` | `u8` | flag byte to store |

- Addresses by version: 219: 0x0C05CE54
- Called by: `ble_219_0c0295e0`, `ble_219_0c02a8f8`, `ble_219_0c055b90`
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
- Called by: `ble_219_0c028c94`, `ble_219_0c029200`, `ble_219_0c02a3c4`, `ble_219_0c02b480`
- Calls: `nvdata_ioctl_cmd_0x200`, `nvdata_ioctl_get_buf_0x102`, `nvdata_ioctl_cmd_0x104`, `nvdata_ioctl_unlock_0x103`, `nvdata_ioctl_lock_0x106`, `memcpy`
- Confidence: high

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
- Called by: `ble_219_0c053018`, `ble_219_0c054668`, `ble_219_0c054734`
- Calls: `ble_slot_count_used`, `ble_app_queue_message`, `ble_counter_20012344_step`
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
