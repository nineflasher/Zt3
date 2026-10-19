# BLE - `upgrade` functions

21 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`nb_upgrade_begin`](#nb_upgrade_begin) | 0x0C0474B0 | Start a firmware upgrade: notify, open the target, pick the parser state from the image name |
| [`nb_upgrade_check_image_header`](#nb_upgrade_check_image_header) | 0x0C0365A4 | Validate a candidate upgrade image header and derive the backup offset for GZIP images |
| [`nb_upgrade_end`](#nb_upgrade_end) | 0x0C0475D4 | Finish an upgrade: run the finish hook, close the target, clear the 80-byte upgrade state |
| [`nb_upgrade_image_digest`](#nb_upgrade_image_digest) | 0x0C03477C | Parse an upgrade image header (RAIM, RAW or RAW4) and MD5 its payload when a digest is requested |
| [`nb_upgrade_image_parse`](#nb_upgrade_image_parse) | 0x0C047274 | Resumable parser for the firmware image stream: 0x30-byte records, CRC-checked blocks, format tags |
| [`nb_upgrade_init`](#nb_upgrade_init) | 0x0C037A2C | Register the upgrade configuration, load its flash state and mark the module initialised |
| [`nb_upgrade_open_target`](#nb_upgrade_open_target) | 0x0C046FB0 | Open the upgrade target, read its erase and page geometry, rewind and keep it open |
| [`nb_upgrade_packet_info_erase`](#nb_upgrade_packet_info_erase) | 0x0C0367B4 | Invalidate the stored upgrade packet info by erasing its sector when the magic is valid |
| [`nb_upgrade_packet_info_rebuild`](#nb_upgrade_packet_info_rebuild) | 0x0C0366E4 | Rewrite the 28-byte upgrade packet-info record in flash with a fresh CRC16 |
| [`nb_upgrade_print_image_info`](#nb_upgrade_print_image_info) | 0x0C03655C | Print the image name and the platform bytes of the current upgrade image header |
| [`nb_upgrade_process_cmd`](#nb_upgrade_process_cmd) | 0x0C0285EC | Dispatch an NB firmware-upgrade frame: iap begin (7), data (8), verify (9), reboot (10) |
| [`nb_upgrade_resume_load`](#nb_upgrade_resume_load) | 0x0C037798 | Load upgrade packet info and resume records from flash and find the last valid resume point |
| [`nb_upgrade_seek`](#nb_upgrade_seek) | 0x0C047554 | Record the upgrade write offset and seek the open target to it |
| [`nb_upgrade_session_begin`](#nb_upgrade_session_begin) | 0x0C0369D8 | Start an upgrade session: open the target image, reset session state and reply to the peer |
| [`nb_upgrade_session_finish`](#nb_upgrade_session_finish) | 0x0C037588 | Finish an upgrade session: check the file MD5 and the flash image, then report the outcome |
| [`nb_upgrade_session_timeout_check`](#nb_upgrade_session_timeout_check) | 0x0C037970 | Periodic upgrade watchdog: abort a stalled session or report that no data arrived |
| [`nb_upgrade_verify_app_image`](#nb_upgrade_verify_app_image) | 0x0C036868 | Verify the application image on a device: container CRC, then MD5 of the payload |
| [`nb_upgrade_verify_device_image`](#nb_upgrade_verify_device_image) | 0x0C03457C | Check a RAW, RAW4 or GZIP image on a device: header magic, size and payload CRC32 |
| [`nb_upgrade_verify_raw`](#nb_upgrade_verify_raw) | 0x0C034468 | Verify a RAW or RAW4 firmware container: magic, size bound and payload CRC32 |
| [`nb_upgrade_verify_staged_image`](#nb_upgrade_verify_staged_image) | 0x0C034548 | Verify the staged image described by DAT_20003E2C and copy out four header words |
| [`nb_upgrade_write_buffered`](#nb_upgrade_write_buffered) | 0x0C047184 | Write upgrade data in page-sized chunks, erase on block boundaries, pad the final tail with 0xFF |

## nb_upgrade_begin

**Start a firmware upgrade: notify, open the target, pick the parser state from the image name**

Stores 0 in DAT_2000F644 and the expected total size in DAT_2000F648, then calls the progress log in slot 0 of the callback table at DAT_2000F64C ('Begin application update.') and slot 1 with 0. It opens the target with nb_upgrade_open_target, using param_3 or /dev/pflash when param_3 is NULL, and stores the descriptor in DAT_2000F5FC. It reports 'Receiving firmware...' and, if the image name in param_1 is not exactly 'pflash.mImage' but is longer than 8 characters and ends in '.mImage', sets the state to LAB_0C047268 (the streaming parser). Otherwise the state becomes LAB_0C0473EC. It returns 0, or the negative open status.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | image name, checked against 'pflash.mImage' and the '.mImage' suffix |
| `param_2` | `u32` | expected total size, stored in DAT_2000F648 |
| `param_3` | `ptr` | device path, or NULL for /dev/pflash |

**Returns** `s32`: 0 on success, otherwise the negative status from opening the target

**Notes:** The state constant LAB_0C0473EC is the raw writer state, and its role is inferred from the code that sets it after each block. The string checks are read directly from the code.

- Addresses by version: 219: 0x0C0474B0
- Called by: `nb_upgrade_session_begin`
- Calls: `nb_upgrade_open_target`, `strcmp`, `strlen`
- Confidence: medium

## nb_upgrade_check_image_header

**Validate a candidate upgrade image header and derive the backup offset for GZIP images**

Copies the 48-byte candidate header into the working copy at 0x2000BAB4 and maps its magic to a format name. An unknown format or an image larger than the configured maximum (config[0] against the size word at 0x2000BAC0) prints the header through nb_upgrade_print_image_info and returns 0. For a GZIP image with no backup offset configured (config[2] = 0xFFFFFFFF) it derives DAT_2000BAE4, the backup offset, from the page-rounded sum of the header length and payload length fields and the 0x114000 layout, printing 'NOTICE:backup_dev_offset'; it refuses with 'gzip format length not correct' when the result would not fit. Finally it calls the optional validation hook DAT_2000BB8C on the header and returns 1 when the image is accepted, otherwise the hook's result.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | candidate 48-byte image header |

**Returns** `s32`: 1 when valid, 0 when the image cannot be checked or is refused, or the validation hook's non-1 result

**Notes:** The backup-offset constants (0x29000, 0x114000, 0xEB000) come from the decompile without a layout reference; the formula is descriptive. The validation hook at DAT_2000BB8C is set by another module. ble_219_0c0285ec is an outside caller.

- Addresses by version: 219: 0x0C0365A4
- Called by: `nb_upgrade_process_cmd`
- Calls: `bes_image_format_name`, `trace_printf`, `nb_upgrade_print_image_info`, `strncmp`
- Confidence: medium

## nb_upgrade_end

**Finish an upgrade: run the finish hook, close the target, clear the 80-byte upgrade state**

Logs 'Receive firmware done.' through the callback table at DAT_2000F64C. If the finish hook DAT_2000F610 is installed it is called with param_1 and its result becomes the return value, otherwise the return value is 0. The target is then queried with lseek(fd, 0, -1), which is a position query whose result is unused, closed through 0x0C071A60, and the 80-byte block starting at DAT_2000F5FC is zeroed with memset. It finally logs 'Update firmware done.'.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | argument passed to the finish hook |

**Returns** `u32`: result of the finish hook, or 0 when none is installed

**Notes:** The 80-byte zeroing starts at DAT_2000F5FC and covers the descriptor, geometry words, parser state and the seek offset (DAT_2000F644). The meaning of the lseek(fd, 0, -1) query follows fd_lseek and is inferred.

- Addresses by version: 219: 0x0C0475D4
- Called by: `nb_upgrade_session_finish`, `nb_upgrade_session_timeout_check`
- Calls: `memset`, `ble_219_0c071a60`, `ble_219_0c071a80`
- Confidence: high

## nb_upgrade_image_digest

**Parse an upgrade image header (RAIM, RAW or RAW4) and MD5 its payload when a digest is requested**

Reads the 32-bit magic at the image start. For 'RAIM' the hashed length is word 1 plus 8 and the return value is 0; for 'RAW ' and 'RAW4' the length is word 3 and the return value is word 5; any other magic zeroes the digest, magic and length outputs and returns 0. When param_2 is non-null it runs md5_init, then md5_update over the length bytes starting at the header plus word 6, then md5_final into the 16-byte digest. The magic and the length are written to param_3 and param_4 when those are non-null.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | upgrade image header |
| `param_2` | `ptr` | 16-byte MD5 output, optional |
| `param_3` | `ptr` | magic output, optional |
| `param_4` | `ptr` | length output, optional |

**Returns** `u32`: word 5 of a RAW or RAW4 header, or 0 for RAIM and unknown images

**Notes:** Magic words are read as little-endian integers and named from their ASCII bytes. The meaning of header words 1, 3, 5 and 6 is inferred. The length is not checked against the image size before hashing.

- Addresses by version: 219: 0x0C03477C
- Calls: `md5_init`, `md5_update`, `md5_final`
- Confidence: medium

## nb_upgrade_image_parse

**Resumable parser for the firmware image stream: 0x30-byte records, CRC-checked blocks, format tags**

A resumable state machine: each step stores its continuation in DAT_2000F60C and returns to the caller, which feeds the next bytes. It consumes 0x30-byte records. The tag 0x704F6C46 ('FlOp' in memory) copies 48 bytes of header into DAT_2000F614 onward, and the block's CRC is checked with crc32_reflected_table (0x0C0476A0) over DAT_2000F620 bytes against DAT_2000F624. Each block is copied into a buffer from ble_thunk_malloc, its two words are read as start and end offsets (DAT_2000F654 and DAT_2000F658), command 0x101 is issued on the descriptor, and the state moves to the raw writer. The tags 0x43506462 ('bdPC') and 0x55327A62 ('bz2U') install a pair of handlers in DAT_2000F60C and DAT_2000F610 and end the parse, and any other data is passed to nb_upgrade_write_buffered (0x0C047184).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | image stream bytes |
| `param_2` | `s32` | bytes remaining in the stream |
| `param_3` | `u32` | flush flag forwarded to nb_upgrade_write_buffered |

**Returns** `s32`: bytes consumed from the stream, or 0 when a CRC check fails

**Notes:** Lowest-confidence entry of this packet. Tag meanings come from their ASCII bytes and the handler pairs. The 'bz2U' tag suggests a bzip2-style payload, which is not verified. The block-buffer layout and the offset words are inferred. Callees 0x0C0476A0, 0x0C07097C and 0x0C0484B4 are named elsewhere.

- Addresses by version: 219: 0x0C047274
- Calls: `nb_upgrade_write_buffered`, `crc32_reflected_table`, `_close`, `ble_219_0c07097c`, `ble_219_0c07098c`, `memcpy`
- Confidence: low

## nb_upgrade_init

**Register the upgrade configuration, load its flash state and mark the module initialised**

Stores param_1 as the upgrade configuration (DAT_2000BB90) and passes the constant table address 0x0C076FE4 to ble_set_var_2000f64c. It checks that the maximum image size (+0), staging buffer pointer (+0x18) and staging buffer size (+0x1C) are non-zero and that the size is a multiple of 1 KB, printing 'upgrade config argument error' and returning -22 when not. The configuration is kept and nb_upgrade_resume_load runs in both cases, then DAT_2000BC21 is set to 1. A NULL argument returns -22 without changes.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | upgrade configuration: +0 max image size, +4 image device name, +8 backup offset (0xFFFFFFFF none), +0xC info device name, +0x10 info offset, +0x14 info size, +0x18 staging buffer, +0x1C staging size, +0x20 communication timeout, +0x24 no-data timeout, +0x28 error callback |

**Returns** `s32`: 0 when the configuration is accepted, -22 for a NULL or invalid configuration

**Notes:** A caller that ignores the return value runs with a bad configuration, since the config is stored and initialisation still runs. ble_219_0c047634 is treated as ble_set_var_2000f64c; the use of the 0x0C076FE4 table is not verified.

- Addresses by version: 219: 0x0C037A2C
- Called by: `ble_init_cfg_ptr_store`
- Calls: `trace_printf`, `nb_upgrade_resume_load`, `ble_set_var_2000f64c`
- Confidence: high

## nb_upgrade_open_target

**Open the upgrade target, read its erase and page geometry, rewind and keep it open**

Opens the device path param_1 with open(path, 0) through 0x0C071A94; a path that fails to open logs 'Can't open %s' and returns -6. On success it issues command 0x100 on the descriptor through 0x0C0484B4 with param_2 as the output buffer, which receives the two words later stored as DAT_2000F600 (erase-block size) and DAT_2000F604 (write chunk size). It then rewinds with lseek(fd, 0, SEEK_SET) through 0x0C071A80 and returns the descriptor. If the geometry command fails, the negative status is returned without closing the descriptor, so that descriptor leaks.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | NUL-terminated device path, for example /dev/pflash |
| `param_2` | `ptr` | output buffer for the geometry words (DAT_2000F600 and DAT_2000F604 when called from nb_upgrade_begin) |

**Returns** `s32`: open descriptor on success, -6 when open fails, or the negative geometry-command status

**Notes:** Descriptor leak on the geometry-failure path (no close before returning the negative status). The meaning of command 0x100 and the two output words is inferred from how nb_upgrade_write_buffered uses DAT_2000F600 and DAT_2000F604. 0x0C0484B4 is named _close in wave2_batch06, but here it is called with command codes 0x100, 0x101 and 0x110 and looks like an ioctl dispatch. That name should be reviewed in its own packet.

- Addresses by version: 219: 0x0C046FB0
- Called by: `nb_upgrade_begin`
- Calls: `trace_printf`, `_close`, `ble_219_0c071a80`, `ble_219_0c071a94`
- Confidence: medium

## nb_upgrade_packet_info_erase

**Invalidate the stored upgrade packet info by erasing its sector when the magic is valid**

Reads the 28-byte packet-info record at config[4] and logs the start. If its magic is 0x5550 it logs 'need to erase', clears the 0x70-byte resume record buffer at 0x2000BBB0, sets DAT_2000BB88 to 0, sets the record words 0x2000BB94..0x2000BBAC to 0xFFFFFFFF in RAM and erases the sector with fd control command 0x110 (argument = offset / sector size), printing an error if the erase fails. It always releases the device. It is called at session start (protocol 0), at finish and on the error paths.

**Notes:** The RAM words set to 0xFFFFFFFF do not themselves write flash; the erase does.

- Addresses by version: 219: 0x0C0367B4
- Called by: `nb_upgrade_session_begin`, `nb_upgrade_session_finish`
- Calls: `trace_printf`, `_close`, `memset`, `ble_219_0c071a80`, `read`
- Confidence: medium

## nb_upgrade_packet_info_rebuild

**Rewrite the 28-byte upgrade packet-info record in flash with a fresh CRC16**

Fills the packet-info record at 0x2000BB94 (CRC16 at +0, magic 0x5550 at +2, 24-byte body at +4). The body is the file size from the session block (0x2000BCA4) and five words copied from the session descriptor, and the CRC16/CCITT (ble_219_0c047644, over the 26 bytes from the magic) is stored at +0. It erases the info sector (fd control command 0x110 with config[4] divided by the sector size), seeks to config[4] and writes the 28 bytes, then releases the device. It sets DAT_2000BB88 to 0x1C (the resume-chain start) and returns 0 on success or the failing call's result.

**Returns** `s32`: 0 on success; otherwise the nonzero result of the failing erase or write

**Notes:** The meaning of the body words is inferred from the session block layout. The sector size comes from the fd control query in nb_upgrade_resume_load (DAT_2000BAFC).

- Addresses by version: 219: 0x0C0366E4
- Called by: `nb_upgrade_process_cmd`
- Calls: `trace_printf`, `crc16_ccitt_nibble`, `_close`, `ble_219_0c071a80`, `write`
- Confidence: medium

## nb_upgrade_print_image_info

**Print the image name and the platform bytes of the current upgrade image header**

Prints 'image_name:%s,platform:' with the name from bes_image_format_name for the magic at DAT_2000BAB4, then prints the 8 bytes at DAT_2000BAB8 (header offsets +4..+0xB) as '%x(%c)' pairs, stopping early at a NUL byte, and ends with CRLF. Used to show what was found when an image is rejected.

**Notes:** Called by nb_upgrade_check_image_header and by ble_219_0c0285ec (outside this packet).

- Addresses by version: 219: 0x0C03655C
- Called by: `nb_upgrade_process_cmd`, `nb_upgrade_check_image_header`
- Calls: `bes_image_format_name`, `trace_printf`
- Confidence: high

## nb_upgrade_process_cmd

**Dispatch an NB firmware-upgrade frame: iap begin (7), data (8), verify (9), reboot (10)**

Handles one parsed upgrade frame: byte +5 is the command, byte +2 the payload length, byte +6 the packet index and +8 the payload pointer. Command 7 (iap begin, payload length above 3) latches the image size from the first payload word, stores the header fields, reads the 40-byte upgrade block at 0x2000F38C (ble_app_block40_f38c_read) and starts the session through ble_219_0c0369d8. Command 9 passes the first payload word to ble_219_0c037588 and command 10 logs 'upgrade system reboot' and calls ble_219_0c041d28. Command 8 is the data path, valid only in upgrade state 1 or 2: it checks the payload against the total size DAT_2000BC28 and the flash block size, applies a sequence check (a repeated index retransmits the previous ack, a gap is an error) and on the first call validates the 48-byte image header. The header tag selects the mode: tag -0x56 (0xAA) is plain, -0x4456 (0xBBAA) is fixed-key and -0x334456 (0xCCBBAA) is per-device-key. The header is tested as plaintext first, then TEA-CBC decrypted (crypto_tea_cbc_decrypt) with the fixed 128-bit key 0xB21C80FE 0xA641EFD1 0xF53117A4 0xF02468A0 and then with the key at 0x2000BCB9, each time re-validated. In encrypted modes every block is decrypted before it is written, a running byte sum (DAT_2000BC38) is complemented at the end, progress percentages are logged, and a 0x70-byte packet-info record is saved to the pflash handle DAT_2000BAF8 at checkpoints. The status callback at DAT_2000BCCC is called with codes 0 ack, 1 already transferred, 3 decrypt error, 5 index error, 7 data error and 9 not started.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | parsed upgrade frame: +2 payload length, +5 command, +6 packet index, +8 payload pointer |

**Returns** `s32`: bytes accepted for command 8, 0 for other commands, or a negative error code (-0x47, -0x16, -0x8, -0x13)

**Notes:** Large state machine over globals DAT_2000BCxx and DAT_2000BBxx. Decompiler type propagation did not settle, so some field widths are guesses. Undescribed helpers: ble_219_0c0365a4 (header plaintext test), ble_219_0c036418 (TEA-CBC), ble_219_0c0366e4, ble_219_0c0369d8, ble_219_0c037588, ble_219_0c047e70 (running state at 0x2000BC3C) and the pflash seek/read/write helpers at 0x0C071A80, 0x0C071ABC and 0x0C071AD0. The 0x0C0286A4 handler stored at 0x20004BC4 is not analysed here. The meaning of the 0x70-byte record fields is inferred.

- Addresses by version: 219: 0x0C0285EC
- Calls: `trace_printf`, `crypto_tea_cbc_decrypt`, `nb_upgrade_print_image_info`, `nb_upgrade_check_image_header`, `nb_upgrade_packet_info_rebuild`, `nb_upgrade_session_begin`, `nb_upgrade_session_finish`, `ble_boot_mode_set`, `xTaskGetTickCount`, `ble_app_block40_f38c_read`, `nb_upgrade_seek`, `ble_get_var_2000f5fc`, `ble_byte_count_notify`, `crc16_ccitt_nibble`, `md5_update`, `memcpy` ...
- Confidence: medium

## nb_upgrade_resume_load

**Load upgrade packet info and resume records from flash and find the last valid resume point**

Opens the info device (config[3]), reads the sector size with fd control 0x100 and the 28-byte packet-info record at config[4]. If its CRC16 matches (ble_219_0c047644 over 26 bytes from the magic), the magic is 0x5550 and the stored size is within the configured maximum, it walks 0x70-byte resume records from config[4]+0x1C up to config[4]+config[5]. Each record's CRC16 covers the 110 bytes after its CRC word, and the walk stops at the first bad record, leaving DAT_2000BB88 just past the last good one and that record in 0x2000BBB0 (packet index at 0x2000BBB2). With no valid resume record it clears the resume buffer, and an invalid info record is reset in RAM and logged as 'no valid upgrade file info'. The device is released and 'app dflash init complete' is logged. It does nothing when config[3] or config[5] is zero.

**Notes:** Record layouts are inferred from the CRC and offset arithmetic. The CRC16 state pointer at 0x20003E98 is a RAM word used by ble_219_0c047644. Resume is only offered when the stored packet identity matches (see ble_219_0c0369d8).

- Addresses by version: 219: 0x0C037798
- Called by: `nb_upgrade_init`
- Calls: `trace_printf`, `crc16_ccitt_nibble`, `_close`, `memcpy`, `memset`, `ble_219_0c071a80`, `ble_219_0c071a94`, `read`
- Confidence: medium

## nb_upgrade_seek

**Record the upgrade write offset and seek the open target to it**

Stores param_1 in DAT_2000F644 as the current upgrade offset. If the target descriptor DAT_2000F5FC is open (positive), it calls lseek(fd, offset, SEEK_SET) through 0x0C071A80 and returns the new position. With no open target it returns -5 (0xFFFFFFFB).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | absolute byte offset in the target |

**Returns** `s32`: new position from lseek, or -5 when no target is open

- Addresses by version: 219: 0x0C047554
- Called by: `nb_upgrade_process_cmd`, `nb_upgrade_session_begin`
- Calls: `ble_219_0c071a80`
- Confidence: high

## nb_upgrade_session_begin

**Start an upgrade session: open the target image, reset session state and reply to the peer**

Returns -2 when the upgrade module is not initialised (DAT_2000BC21 clear). If a session is already active it calls param_12 with code 6 and returns -16. Otherwise it checks the arguments (non-zero size within the configured maximum, method 0 or 1), returns -22 when they fail, and opens the target image through ble_219_0c0474b0 with the name 'mainApp.mImage', the size and config[1] (default /dev/pflash0). On success it stores the method, size, protocol and callbacks (param_5..param_12 at 0x2000BCB0..0x2000BCCC), clears the 0x7C-byte session block at 0x2000BC24 and the MD5 context, sets the communication and no-data deadlines from config[8] and config[9] and reports status 1 through DAT_2000BB84. Protocol 0 erases the packet info and sends packet 0; protocol 1 sends a 3-byte start reply; protocol 2 compares the stored packet identity and size and either offers resume at the stored packet index with a 7-byte reply or asks for a retransmit from packet 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | method: 0 or 1 (selects the name at 0x0C086044) |
| `param_2` | `u32` | image file size in bytes |
| `param_3` | `u32` | protocol version in the low byte |
| `param_4` | `u32` | stored with the session descriptor |
| `param_5` | `u32` | session parameter stored at 0x2000BCB0 |
| `param_6` | `u32` | session parameter stored at 0x2000BCB4 |
| `param_7` | `u32` | session parameter stored at 0x2000BCB8 |
| `param_8` | `u32` | session parameter stored at 0x2000BCBC |
| `param_9` | `u32` | session parameter stored at 0x2000BCC0 |
| `param_10` | `u32` | session parameter stored at 0x2000BCC4 |
| `param_11` | `u32` | session parameter stored at 0x2000BCC8 |
| `param_12` | `ptr` | response callback (event code, data, length); stored and called on busy and on replies |

**Returns** `s32`: 0 when the session started or resumed; -2 not initialised; -16 busy; -22 bad argument or open failure

**Notes:** Protocol versions 0, 1 and 2 and the reply layouts (3-byte and 7-byte messages) are inferred from the branch structure and not decoded. ble_219_0c0474b0 (image open helper) and ble_219_0c047554 (resume position setup from a block count) are not yet named. Which of the session parameters are needed by the peer is not established.

- Addresses by version: 219: 0x0C0369D8
- Called by: `nb_upgrade_process_cmd`
- Calls: `trace_printf`, `nb_upgrade_packet_info_erase`, `xTaskGetTickCount`, `nb_upgrade_begin`, `nb_upgrade_seek`, `md5_init`, `memcpy`, `memset`
- Confidence: medium

## nb_upgrade_session_finish

**Finish an upgrade session: check the file MD5 and the flash image, then report the outcome**

Valid only in states 1 and 2; otherwise it calls the error callback with 9 and returns -71. It sets state 3 (verifying) and the no-data deadline. If param_1 equals DAT_2000BC38 and the protocol is 2, it finalises the session MD5 (md5_final) and compares it with the 16-byte digest the peer sent at 0x2000BCA9; a mismatch prints both digests and returns -19. It then verifies the flash image with nb_upgrade_verify_app_image. On success it prints 'IAP verify OK', calls the completion callback (0), clears the packet info with nb_upgrade_packet_info_erase, stops the session with ble_219_0c0475d4(1) and reports status 3. On failure it calls the error callback with 8, erases the packet info, stops the session with ble_219_0c0475d4() and reports status 2.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | received packet count or file checksum; compared with DAT_2000BC38 |

**Returns** `s32`: 0 on success; -19 on file digest or checksum error; -71 for a call in the wrong state; otherwise the verify error

**Notes:** Status codes passed to the status callback (1 start, 2 failed or aborted, 3 done) and callback codes 8 and 9 are read from the calls and not from a spec. The meaning of DAT_2000BC38 is not established; ble_219_0c0475d4 is not yet named.

- Addresses by version: 219: 0x0C037588
- Called by: `nb_upgrade_process_cmd`
- Calls: `trace_printf`, `nb_upgrade_packet_info_erase`, `nb_upgrade_verify_app_image`, `stub_empty_0c037584`, `xTaskGetTickCount`, `nb_upgrade_end`, `md5_final`
- Confidence: medium

## nb_upgrade_session_timeout_check

**Periodic upgrade watchdog: abort a stalled session or report that no data arrived**

Runs only when the upgrade module is initialised and configured. If the communication timeout config[8] is set and a session is active (state not 0 or 3) and its deadline DAT_2000BC94 has passed, it logs 'communication timeout', stops the session with ble_219_0c0475d4(), sends status 2 and calls the error callback config[10] with code 1. If the no-data timeout config[9] is set, its deadline DAT_2000BC98 has passed and DAT_20003EA0 is still clear, it logs 'No upgrade data was received', calls config[10] with code 2, sets DAT_20003EA0 and returns.

**Notes:** Callback codes 1 and 2 are the error reason codes passed to config[10]; their meanings are taken from the log text.

- Addresses by version: 219: 0x0C037970
- Calls: `trace_printf`, `xTaskGetTickCount`, `nb_upgrade_end`
- Confidence: medium

## nb_upgrade_verify_app_image

**Verify the application image on a device: container CRC, then MD5 of the payload**

Opens the target device (param_1) and seeks to the backup offset DAT_2000BAE4 to read the 48-byte header. It rejects a size word above the configured maximum and copies the first four header words into the caller's output array. It runs nb_upgrade_verify_device_image (ble_219_0c03457c) for the container CRC; on success it hashes the payload with MD5 (md5_init, md5_update in chunks of config[7] bytes read into config[6], md5_final) and compares the 16-byte digest with the one stored in the header after the payload offset word. A digest mismatch prints both digests and returns -8, a bad header or read returns -5, and a failed open returns -19. The device is released before returning.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | device name string, e.g. /dev/pflash0 |
| `param_2` | `ptr` | output array of four u32 header words |

**Returns** `s32`: 0 on success, -8 on digest or CRC mismatch, -5 on header or read error, -19 when the device cannot be opened

**Notes:** Header field offsets for the payload offset and the stored digest are read from the decompiled local layout and may be off by a word. The MD5 is over the payload length from the header only after the container CRC passes.

- Addresses by version: 219: 0x0C036868
- Called by: `nb_upgrade_session_finish`
- Calls: `nb_upgrade_verify_device_image`, `trace_printf`, `md5_init`, `md5_update`, `md5_final`, `ble_219_0c071a80`, `ble_219_0c071a94`, `read`
- Confidence: medium

## nb_upgrade_verify_device_image

**Check a RAW, RAW4 or GZIP image on a device: header magic, size and payload CRC32**

Reads the 48-byte image header at offset param_2 of device fd param_1. It accepts magic 'RAW4' (0x34574152), 'RAW ' (0x20574152) or 'GZIP' (0x50495A47) and rejects a payload above 0x1D8000 bytes with -5. The payload length is at header +0xC, the expected CRC32 at +0x10 and the payload offset at +0x18 (added to the base offset). The CRC32 (reflected, polynomial 0xEDB88320, initial 0xFFFFFFFF, final inversion) is computed with crc32_reflected_table in 256-byte chunks; for RAW4 images that run past 4 KB the stream is read as the first 4 KB, then one byte per 4 KB boundary, then the tail, the same layout as nb_upgrade_verify_raw. Returns 0 when the CRC matches (~crc equals the stored value), -8 on mismatch, and -5 for a bad magic, an oversize payload or a short read. The device is released with the seek helper using whence 0xFFFFFFFF.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | device fd of the image |
| `param_2` | `u32` | base offset of the image header on the device |

**Returns** `s32`: 0 on match, -8 on CRC mismatch, -5 on bad header, oversize payload or short read

**Notes:** RAW4 streaming coverage (which bytes the CRC includes beyond 4 KB) is low confidence, as for the sibling ble_219_0c034468. GZIP payloads are CRC-checked only; they are not decompressed. The ble_219_0c071a80 seek helper is not yet named.

- Addresses by version: 219: 0x0C03457C
- Called by: `nb_upgrade_verify_app_image`
- Calls: `crc32_reflected_table`, `memset`, `ble_219_0c071a80`, `read`
- Confidence: medium

## nb_upgrade_verify_raw

**Verify a RAW or RAW4 firmware container: magic, size bound and payload CRC32**

Checks the header param_2: magic 0x20574152 ('RAW ') or 0x34574152 ('RAW4') at +0, payload size at +0xC (at most 0x1D8000), expected CRC32 at +0x10 and payload offset at +0x18 from the header. For RAW the reflected CRC32 (polynomial 0xEDB88320, crc32_reflected_table at 0x0C0476A0) is computed over the whole payload in one call. For RAW4 with payload end above 0x1000 the code streams the first 0x1000 bytes, then one byte per 4 KB page boundary, then the tail, all through the same routine. It returns 0 when the CRC matches, -8 on mismatch and -5 for a bad magic or an oversize image, and writes the payload address to *param_1 when that pointer is given.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | optional output: payload start address |
| `param_2` | `ptr` | image header record |

**Returns** `s32`: 0 valid; -8 CRC mismatch; -5 bad magic or size

**Notes:** The RAW4 streaming path passes 0x1000 as the fourth argument of its first call, and the decompiler drops the fourth argument of the in-loop calls. Which bytes the RAW4 CRC covers is therefore uncertain (low confidence on that branch).

- Addresses by version: 219: 0x0C034468
- Called by: `nb_upgrade_verify_staged_image`
- Calls: `crc32_reflected_table`
- Confidence: medium

## nb_upgrade_verify_staged_image

**Verify the staged image described by DAT_20003E2C and copy out four header words**

Upgrade-module wrapper. If the descriptor at DAT_20003E2C has a size (+0xC) of at most 0x1D8000 it calls nb_upgrade_verify_raw on it (0x0C034468), passing param_1 through, and when param_2 is non-NULL it copies descriptor words +4, +8, +0xC and +0x10 into param_2[0..3]. An oversize descriptor returns -5 and copies nothing. Parameters param_3 and param_4 are not used in the body.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | passed through as the payload-address output of the verifier |
| `param_2` | `ptr` | output: four u32 copied from the staged descriptor |
| `param_3` | `u32` | not used |
| `param_4` | `u32` | not used |

**Returns** `s32`: verifier result, or -5 for an oversize descriptor

- Addresses by version: 219: 0x0C034548
- Calls: `nb_upgrade_verify_raw`
- Confidence: medium

## nb_upgrade_write_buffered

**Write upgrade data in page-sized chunks, erase on block boundaries, pad the final tail with 0xFF**

Writes param_2 bytes from param_1 to the open upgrade descriptor DAT_2000F5FC in DAT_2000F604-byte chunks. Before writing, it reads the device position with lseek(fd, 0, SEEK_CUR) through 0x0C071A80. When that position is a multiple of the erase size DAT_2000F600, it issues command 0x110 on the descriptor (through 0x0C0484B4) before the chunk, so the block is prepared first. When param_3 is nonzero (final flush), the trailing partial chunk is copied to a stack buffer, padded with 0xFF to a full chunk and written, so the device always receives whole pages. It returns the number of input bytes handled, or param_2 after a flushed tail.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | image bytes to write |
| `param_2` | `u32` | number of bytes to write |
| `param_3` | `s32` | nonzero to flush and pad the final partial chunk |

**Returns** `u32`: bytes handled from param_1

**Notes:** The position and chunk arithmetic was only partly traced, so the exact return value on error paths is uncertain. Command 0x110 is taken to prepare a block (erase); this is an inference. The offset check on DAT_2000F600 is clear from the code.

- Addresses by version: 219: 0x0C047184
- Called by: `nb_upgrade_image_parse`
- Calls: `_close`, `memcpy`, `memset`, `ble_219_0c071a80`, `write`
- Confidence: medium
