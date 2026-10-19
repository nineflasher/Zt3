# BLE - `fmna` functions

14 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`ble_findmy_ring_status_notify`](#ble_findmy_ring_status_notify) | 0x0C029230 | Send the Find My ring status (0 or 1) to the VCU twice, 5 ticks apart |
| [`ble_fmna_adv_close`](#ble_fmna_adv_close) | 0x0C055268 | Close Find My advertising: remove the timer and run the stop helper |
| [`ble_fmna_adv_offline_ad_build`](#ble_fmna_adv_offline_ad_build) | 0x0C052F28 | Build the 31-byte Apple offline-finding advertisement from a key record and set it as adv data |
| [`ble_fmna_adv_open`](#ble_fmna_adv_open) | 0x0C055244 | Open Find My advertising: run two helpers and arm the 600000-unit timer |
| [`ble_fmna_adv_payload_init`](#ble_fmna_adv_payload_init) | 0x0C052EE4 | Build the Find My advertising data (UUID 0xFD44 service data) and the 'ninebot_fmna' scan response |
| [`ble_fmna_adv_status_ad_build`](#ble_fmna_adv_status_ad_build) | 0x0C052FB0 | Build the 8-byte Apple offline-finding status advertisement and set it as adv data |
| [`ble_fmna_cmd_handler`](#ble_fmna_cmd_handler) | 0x0C02A8F8 | Find My (FMNA) command handler: status reads, ADV_ID, model name, NV records and advertising control |
| [`ble_fmna_debug_cmd_dispatch`](#ble_fmna_debug_cmd_dispatch) | 0x0C055B90 | Dispatch a Find My debug command string selected by its first character |
| [`ble_fmna_found_url_update`](#ble_fmna_found_url_update) | 0x0C054534 | Set one field of the Find My found-URL source and rebuild the lookup URL |
| [`ble_fmna_pair_adv_service`](#ble_fmna_pair_adv_service) | 0x0C0555D4 | Service pair advertising from the 0x20012BE0 block and the 0x304 latch |
| [`ble_fmna_reset_gen_keypair`](#ble_fmna_reset_gen_keypair) | 0x0C0537B4 | Reset host state and generate the P-224 Find My key pair with wolfSSL, returning 0 or an error |
| [`ble_fmna_state_save`](#ble_fmna_state_save) | 0x0C053954 | Assemble the 0x52E-byte Find My state record and store it as NV record 0x4DD; returns 0 or 0xC |
| [`ble_session_msg_build`](#ble_session_msg_build) | 0x0C053E1C | Build the 141-byte session message for tap (0) or bt (1) and encode it |
| [`ble_unlock_auth_cb`](#ble_unlock_auth_cb) | 0x0C029284 | Unlock auth callback: send a folded 16-bit token to the VCU, then wait for the auth event |

## ble_findmy_ring_status_notify

**Send the Find My ring status (0 or 1) to the VCU twice, 5 ticks apart**

Logs 'findmy ring status is %d'. Only the values 0 and 1 are sent: the status goes in the first byte of a 2-byte payload (second byte 0) with command 0x86 and header byte 3 set to 3, through uart_bridge_send_frame. It then waits 5 ticks with vTaskDelay and sends the identical frame again so the VCU receives it twice. Other values are logged and ignored.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | ring status, 0 or 1 is sent |

**Notes:** Callers are ble_219_0c05376c, ble_219_0c0537b4, ble_219_0c055b90 and ble_219_0c05d018.

- Addresses by version: 219: 0x0C029230
- Called by: `ble_slot_mgr_set_ready`, `ble_fmna_reset_gen_keypair`, `ble_fmna_debug_cmd_dispatch`, `ble_host_reset_step`
- Calls: `uart_bridge_send_frame`, `trace_printf`, `vTaskDelay`
- Confidence: high

## ble_fmna_adv_close

**Close Find My advertising: remove the timer and run the stop helper**

Removes the timer source at 0x20012C5C through the btstack_run_loop_remove_timer thunk (thunk_FUN_0c065ab8) and then calls ble_219_0c05c548 (not described yet, presumably the stop action for advertising). This is the counterpart of ble_fmna_adv_open and is called for debug command '2' and for the stop path of command '9'.

- Addresses by version: 219: 0x0C055268
- Called by: `ble_fmna_cmd_handler`, `ble_fmna_debug_cmd_dispatch`, `ble_mode_set_and_persist`, `ble_mode_state_update`
- Calls: `btstack_run_loop_remove_timer_thunk`, `ble_act_stop`
- Confidence: medium

## ble_fmna_adv_offline_ad_build

**Build the 31-byte Apple offline-finding advertisement from a key record and set it as adv data**

Builds the legacy advertisement for Apple offline finding from a 28-byte key record at param_1. Its first byte, with the two top bits forced to 11, plus the next five bytes are cached as the advertising address through ble_peer_bdaddr_cache_set, so the first six bytes are the address and bytes 6 to 27 are the remaining 22 bytes of a P-224 public key. The 27-byte payload at 0x2001016C is laid out as 0x12 0x19 (offline-finding type and length 25), a status byte ((state byte from 0x2000407A << 6) | 0x20), those 22 key bytes copied as 4-byte and 2-byte words, the top two bits of the record's first byte (DAT_20010185), and the hint byte param_2 (DAT_20010186). It is wrapped in a manufacturer-specific element at 0x200170AC (length 0x1E, type 0xFF, company ID 0x004C, Apple) and submitted through 0x0C06B70C with the length kept in DAT_200170CB (31 bytes). The advertising set is reset with 0x0C06B64C first, the parameter bytes 0x200042CA and 0x200042CC are copied from 0x20003FBC, and DAT_20017046 is set to 3.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 28-byte key record: bytes 0-5 are the address, bytes 6-27 the rest of the public key |
| `param_2` | `u8` | hint byte written as the last byte of the offline-finding payload |

**Notes:** The field layout is reasoned from the store offsets and the 0x12 0x19 header. The Apple interpretation (offline finding, P-224 key) is an inference from that layout and from the 0x004C company ID.

- Addresses by version: 219: 0x0C052F28
- Called by: `ble_fmna_pair_adv_service`
- Calls: `ble_peer_bdaddr_cache_set`, `ble_act_stop`, `ble_state_407a_read`, `ble_219_0c06b64c`, `ble_219_0c06b70c`, `memcpy`
- Confidence: medium

## ble_fmna_adv_open

**Open Find My advertising: run two helpers and arm the 600000-unit timer**

Opens Find My advertising for debug command '1' and for the start-pair path of command '9'. It calls ble_219_0c052ee4 and ble_219_0c05c480 (neither described yet), then arms the BTstack timer source at 0x20012C5C through ble_host_timer_restart with timeout 600000 and handler LAB_0C054BB4. The restart helper only arms the timer when the env state byte is 2. If the timeout is in milliseconds the timer is 10 minutes. The matching close routine is ble_fmna_adv_close.

**Notes:** The time unit of the timeout is not confirmed; 600000 is read as milliseconds because the timer source is a BTstack run-loop timer.

- Addresses by version: 219: 0x0C055244
- Called by: `ble_fmna_debug_cmd_dispatch`, `ble_mode_set_and_persist`
- Calls: `ble_fmna_adv_payload_init`, `ble_host_timer_restart`, `ble_act_profile_apply_b`
- Confidence: medium

## ble_fmna_adv_payload_init

**Build the Find My advertising data (UUID 0xFD44 service data) and the 'ninebot_fmna' scan response**

Initialises the Find My (FMNA) advertising configuration. It calls 0x0C05C548, then loads the 8-byte NV record 0xFA8 (ble_nv_load_8byte_block) and the one-byte flag from NV record 0xFA7 (ble_nv_load_flag_byte) into the globals at 0x20010154 to 0x2001015C, stores the state byte from ble_state_407a_read at 0x20010168, and clears DAT_200170AB. The advertising data at 0x2001706C is a 16-bit service UUID list (length 3, type 0x03, UUID 0xFD44) followed by a service data element (length 0x18, type 0x16, UUID 0xFD44) whose payload is copied from the block at 0x20010154 with memcpy; the 0x1D-byte block is submitted through 0x0C06B70C for the advertising set index in DAT_200042C7. The scan response at 0x2001708C is a Complete Local Name element (length 0x10, type 0x09) holding the ASCII string 'ninebot_fmna', submitted through 0x0C06B764. DAT_20017046 is set to 1 to mark the payload as configured. Its only listed caller is 0x0C055244.

**Notes:** The byte count of the memcpy that fills the service-data payload is not visible in the decompile. The 0x1D length is the value passed to 0x0C06B70C.

- Addresses by version: 219: 0x0C052EE4
- Called by: `ble_fmna_adv_open`
- Calls: `ble_act_stop`, `ble_state_407a_read`, `ble_nv_load_8byte_block`, `ble_nv_load_flag_byte`, `ble_219_0c06b70c`, `ble_219_0c06b764`, `memcpy`
- Confidence: medium

## ble_fmna_adv_status_ad_build

**Build the 8-byte Apple offline-finding status advertisement and set it as adv data**

Builds the short Apple manufacturer advertisement used for the offline-finding status when the accessory is not presenting its key. It calls ble_peer_bdaddr_cache_set and sets DAT_20010153 to the top two bits of param_1's first byte. The element at 0x2001704C is length 7, type 0xFF, company 0x004C, then the header bytes 0x12 0x02 and four status bytes at 0x20010150 to 0x20010153: the 0x12 0x02 header, a status byte of (state byte from 0x2000407A << 6) | 0x20 with bit 2 added when ble_get_byte_12b84 is nonzero, and the address bits. The 8-byte block is submitted through 0x0C06B70C after 0x0C06B64C resets the advertising set. The adv parameter bytes 0x200042CA and 0x200042CC are copied from 0x20003FB4, and DAT_20017046 is set to 2. The address argument is the BLE address record at 0x20012B90 when called from ble_slot_cmd_dispatch.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 6-byte BLE address record; only the top two bits of byte 0 are used in the payload |

**Notes:** The stack buffer passed to ble_peer_bdaddr_cache_set (0x0C05C2FC) is not filled in the decompile, probably a decompiler artifact. The cache is written with that buffer's contents.

- Addresses by version: 219: 0x0C052FB0
- Called by: `ble_slot_cmd_dispatch`
- Calls: `ble_get_byte_12b84`, `ble_peer_bdaddr_cache_set`, `ble_act_stop`, `ble_state_407a_read`, `ble_219_0c06b64c`, `ble_219_0c06b70c`, `memcpy`
- Confidence: medium

## ble_fmna_cmd_handler

**Find My (FMNA) command handler: status reads, ADV_ID, model name, NV records and advertising control**

Dispatches Find My and model-name commands by command byte param_5. param_4 selects the operation. Operation 1 is a read and sends back the value for command 0x1D and 0x1E (status words), 0x20, 0x25, 0x36, 0x3A and 0x3B (flags), 0x21 and 0x26 (NV records via ble_nv_load_8byte_block and ble_nv_load_device_name), 0x2A (second half of the name), 0x37 (random address via ble_random_addr_advance), and 0x3C and 0x40 (the ADV_ID block via app_adv_id_block_copy). Operations 2 and 3 are writes: command 0x20 starts or stops FMNA advertising and nearby advertising, logging 'stop_fmna_adv', 'start_nearby_adv', 'adv already open' or 'unpair'; 0x1F (an extra action first when the payload is zero) and 0xA3 both fall through to ble_219_0c041d28(0), the system reboot call used by the upgrade path; 0x21 and 0x26 store an 8-byte or 16-byte NV record; 0x2A writes the second 8-byte half of the name; 0x3C and 0x40 write the ADV_ID through ble_payload_copy_and_schedule; 0x3A and 0x3B change flags; 0xA4 and 0xA5 call ble_219_0c05cfe0 and ble_219_0c05d004. Unknown commands set the result to 1. Replies go to the BT app through ble_219_0c02c338 when param_1 is 1, and otherwise through uart_bridge_send_frame with param_2 and param_3 as the header addresses. Writes with param_4 equal to 2 get a command-5 reply carrying a one-byte result.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | reply channel: 1 means the BT app, any other value means the UART bridge |
| `param_2` | `s32` | address byte used in the reply header; 0x3D and 0x3E are checked for writes |
| `param_3` | `u32` | second address byte used in the reply header |
| `param_4` | `s32` | operation: 1 read, 2 or 3 write |
| `param_5` | `u8` | command byte |
| `param_6` | `u8` | payload length |
| `param_7` | `ptr` | payload |

**Returns** `u32`: 1 when the operation was handled (or the command was unknown), 0 when param_4 is not 1 to 3

**Notes:** Several helpers are undescribed (ble_219_0c05cc28, ble_219_0c05cc70, ble_219_0c05cec4, ble_219_0c05cf1c, ble_219_0c058168, ble_219_0c05cfc8, ble_219_0c05cec8, ble_219_0c05cf10). The 'R'/'SET' log strings name the MODEL_NAME operations. The mapping of the status words is inferred from the callee summaries.

- Addresses by version: 219: 0x0C02A8F8
- Called by: `ble_uart_frame_route`, `ble_vcu_cmd_handle`, `ble_uart_inject_cmd1`, `ble_uart_inject_cmd2`
- Calls: `ble_payload_copy_and_schedule`, `app_adv_id_block_copy`, `app_hook_noop`, `uart_bridge_send_frame`, `ble_uart_frame_enqueue`, `trace_printf`, `ble_boot_mode_set`, `ble_slot_teardown_all`, `ble_slot_mgr_is_ready`, `ble_fmna_adv_close`, `ble_fmna_pair_adv_service`, `ble_app_addr6_store`, `ble_random_addr_advance`, `ble_status_bits_get`, `ble_mode_set_and_persist`, `ble_host_5min_timer_ctrl` ...
- Confidence: medium

## ble_fmna_debug_cmd_dispatch

**Dispatch a Find My debug command string selected by its first character**

Debug and command interpreter for Find My. It logs the string with 'bts_fmna_debug' and switches on the first character. '1' opens advertising (ble_219_0c05cdcc, then ble_fmna_adv_open). '2' closes it (ble_fmna_adv_close, then ble_mode_nv_disable). '3' resets the state machine (ble_219_0c05ce14 and ble_219_0c041d28(0)). '4' writes NV record 0xFAA with a 1-byte invalid marker. '5' calls ble_219_0c029230 (buzzer) when the argument is 0 or 1. '6' handles the PPID and related fields: sub-op 0 prints the 8-byte PPID and, if the argument hex-parses to 8 bytes with ble_util_hex_string_to_bytes, stores it; sub-op 1 gets the category and then sets it from the argument; sub-op 2 stores a model name of up to 15 characters. '7' reads the power level (ble_get_value_407a) and sets two values from the arguments. '9' selects a function: 1 stops advertising when ble_mode_nv_is_inactive is 0 and otherwise starts pair advertising, 2 starts pair advertising, 3 resets the state machine, 4 calls ble_host_timer_arm_5min (logged as 'look up sn') and 5 logs ble_get_flag_12606 as the serial report status.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | NUL-terminated command string; first character is the command |

**Notes:** Command '9' sub-op 4 logs 'look up sn' but calls ble_host_timer_arm_5min, which an earlier wave described as a 300 s timer re-arm; the two descriptions disagree and should be checked. Helpers ble_219_0c05cdcc, ble_219_0c05ce14, ble_219_0c041d28, ble_219_0c029230, ble_219_0c05ce48/ce38/ce74/ce54/cea8/ce98, ble_219_0c05cf04, ble_219_0c05cf1c and ble_219_0c0532dc are not described yet.

- Addresses by version: 219: 0x0C055B90
- Calls: `ble_findmy_ring_status_notify`, `trace_printf`, `ble_boot_mode_set`, `ble_slot_teardown_all`, `ble_get_value_407a`, `ble_get_flag_12606`, `ble_fmna_adv_open`, `ble_fmna_adv_close`, `ble_host_timer_arm_5min`, `ble_fmna_pair_adv_service`, `ble_util_hex_string_to_bytes`, `ble_nv_record_write`, `ble_mode_nv_is_inactive`, `ble_mode_nv_disable`, `ble_mode_nv_enable`, `ble_mode_persist_enabled_alt` ...
- Confidence: medium

## ble_fmna_found_url_update

**Set one field of the Find My found-URL source and rebuild the lookup URL**

param_1 selects the field: 0 stores one byte into 0x2000407A (the b value), 1 copies 16 raw bytes from param_2 to 0x2000408D (the serial, NUL-terminated at 0x2000409D), 2 hex-encodes the 140 bytes at param_2 into the string at 0x20004080 and passes that buffer with length 0x11A to ble_219_0c065c88, and 4 hex-encodes 5 bytes into the same string. The 397-byte URL buffer at 0x20012478 is cleared with memset and filled with 'found.apple.com/accessory?pid=%04x&b=%02x&fv=%08x' from the 16-bit pid at 0x20004078, the byte at 0x2000407A and the 32-bit value at 0x2000407C. It then appends either '&e=%s&op=%s' (the hex string and the string at 0x2000419B) when the slot manager is ready, or '&bt=%s&sr=%s' (the hex string and the serial at 0x2000408D) when it is not.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | field selector: 0, 1, 2 or 4 |
| `param_2` | `ptr` | field value (byte, 16-byte serial, or byte array depending on param_1) |
| `param_3` | `u32` | unused in this function |
| `param_4` | `u32` | passed to the fill helper, value not used by this code path |

**Notes:** The Find My URL format string and its field names are literal firmware strings. The meaning of the 16-byte serial and the 5-byte value in mode 4 are inferred from the printed field names.

- Addresses by version: 219: 0x0C054534
- Called by: `ble_mode_state_update`
- Calls: `ble_slot_mgr_is_ready`, `printf_hexdump`, `memset`, `ble_219_0c071570`, `ble_219_0c0715d8`, `strlen`
- Confidence: medium

## ble_fmna_pair_adv_service

**Service pair advertising from the 0x20012BE0 block and the 0x304 latch**

Scans the 27 bytes from 0x20012BE0 for the first non-zero byte. If one is found it calls ble_219_0c052f28 with the block at 0x20012BE0, the mode byte at 0x20012B95, that byte and the counter at 0x20012B8C. If none is found it zeroes the 4-byte block at 0x20012BC0 and calls ble_219_0c052f28 with that block. Then, if the flag byte at 0x20012605 is set (latched by command 0x304 in ble_app_req_302_handle), it clears the flag and calls ble_219_0c05c480; otherwise it calls ble_219_0c05c320. It always returns 0x2000000. Callers are ble_219_0c02a8f8, ble_fmna_debug_cmd_dispatch and ble_219_0c05cf1c.

**Returns** `u32`: always 0x2000000

**Notes:** The purpose of the 0x20012BE0 block and of the 0x2000000 return code is not confirmed.

- Addresses by version: 219: 0x0C0555D4
- Called by: `ble_fmna_cmd_handler`, `ble_fmna_debug_cmd_dispatch`, `ble_mode_state_update`
- Calls: `ble_fmna_adv_offline_ad_build`, `ble_act_profile_apply_a`, `ble_act_profile_apply_b`, `printf_hexdump`
- Confidence: low

## ble_fmna_reset_gen_keypair

**Reset host state and generate the P-224 Find My key pair with wolfSSL, returning 0 or an error**

Host reset and key generation. It calls the no-op hook 0x0C05CBC0, generates the static random address (ble_host_init_static_random_addr), stops the host timers (ble_host_timers_stop_pair, then ble_host_timer_set_enabled with 0) and sets the slot limit DAT_20003FE8 to 1. When param_1 is nonzero, it first tears down every occupied slot with 0x0C05C850. If the slot-manager marker is 0xA5 it calls 0x0C029230(2); it then clears the marker and persists it to NV record 0xFAB. It resets the host context (ble_host_ctx_reset_b88, ble_host_ctx_clear_2608) and zeroes the 512-byte area at 0x20010224, which holds a wolfSSL ecc_key. It then opens a wolfSSL RNG (0x0C061828), acquires a crypto handle from 0x0C05F1A8 (zero aborts with -1), fills 32 random bytes at 0x200103E0 (0x0C061834), runs wc_ecc_init (0x0C060190) and generates the key with 0x0C0600C0 using keysize 0x1C (28 bytes) and curve id 0x0E. On failure the key is freed with wc_ecc_free and the handle with 0x0C05F1B0; the RNG is freed with 0x0C06156C in every case, and the function returns 0 or the error code.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | nonzero tears down all occupied slots before the reset |
| `param_2` | `u32` | unused by this function |
| `param_3` | `u32` | unused by this function |
| `param_4` | `u32` | unused by this function (passed to the memset call in the decompile) |

**Returns** `s32`: 0 on success; -1 when no crypto handle is available; otherwise the wolfSSL or helper error code

**Notes:** The P-224 identification comes from keysize 0x1C and curve id 0x0E passed to 0x0C0600C0, together with the Find My payload layout in ble_fmna_adv_offline_ad_build. 0x0C0600C0, 0x0C05F1A8, 0x0C05F1B0 and 0x0C029230 are not described in this packet.

- Addresses by version: 219: 0x0C0537B4
- Called by: `ble_host_rx_buf_append`, `ble_host_rx_msg_dispatch`
- Calls: `ble_findmy_ring_status_notify`, `ble_host_init_static_random_addr`, `ble_host_ctx_clear_2608`, `ble_host_timers_stop_pair`, `ble_host_timer_set_enabled`, `ble_host_ctx_reset_b88`, `ble_nv_record_write`, `ble_link_abort_current`, `ble_hook_noop_05cbc0`, `wc_ecc_new_point`, `wc_ecc_del_point`, `wc_ecc_make_key_ex`, `wc_ecc_init`, `wc_ecc_free`, `wc_FreeRng`, `wc_InitRng` ...
- Confidence: medium

## ble_fmna_state_save

**Assemble the 0x52E-byte Find My state record and store it as NV record 0x4DD; returns 0 or 0xC**

Assembles the Find My persistent state record and stores it under NV record id 0x4DD. It exports the public key from the P-224 key at 0x20010224 through 0x0C05BA6C into 0x20010A74 (non-zero aborts), reads the identity block at 0x2001225C through 0x0C05C10C (non-zero aborts) and loads the 8-byte NV record 0xFA8 with ble_nv_load_8byte_block. It then copies 32 bytes of key state from 0x200109E0 to 0x2001150C to 0x2001152B, the 0x400-byte table at 0x20011A10 to 0x2001152C, 16 bytes from 0x20011A00 to 0x2001192C, identity words from 0x2001227C to 0x20012288 into 0x2001193C to 0x20011948, 0x71 bytes from 0x20010A00 into 0x20011958, and a series of identity fields from 0x2001225C to 0x20012278 into 0x200119C9 to 0x200119E5. It also stores the word from ble_get_packed_word_12cb0 (0x0C055604) at 0x20011954 and the NV-loaded words at 0x2001194C and 0x20011950, and then writes the 0x52E-byte record through 0x0C05C13C with id 0x4DD, context 0x20004030 and output buffer 0x20010A94. It returns 0 on success and 0xC when any step fails.

**Returns** `u32`: 0 on success, 0xC when any step fails

**Notes:** The field offsets are taken from the decompile; the meaning of the 0x52E-byte record and of record id 0x4DD is inferred. 0x0C05BA6C, 0x0C05C10C and 0x0C05C13C are not described in this packet.

- Addresses by version: 219: 0x0C053954
- Calls: `ble_get_packed_word_12cb0`, `ble_crypto_sha256_commit`, `ble_rng_get_32`, `ble_crypto_ecdh_seal_p256`, `ble_nv_load_8byte_block`, `memcpy`
- Confidence: low

## ble_session_msg_build

**Build the 141-byte session message for tap (0) or bt (1) and encode it**

param_1 selects an ASCII tag written into the 28-byte block at 0x200122A4 and 0x200122E0: 0 writes 'tap' and 1 writes 'bt' (keeping the byte after it), and any other value restores the previous block, stores the counters and returns 0xC. The 64-bit counter at 0x20012308/0x2001230C is incremented into 0x2001229C/0x200122A0 and copied to 0x200122B8/0x200122BC. The 16-byte value at 0x2001227C is copied to 0x2001228C and to 0x200122A8, the input of the message. ble_219_0c05c088 then computes a 4-byte value over the 28-byte block at 0x2001228C with the key at 0x200122E4 and stores it at 0x200122C0. Finally ble_219_0c05c13c encodes message 0x3C from 0x200122A8 into the 141-byte buffer at 0x20010424 (capacity 0x8D); on failure that buffer is zeroed and 0xC is returned. The 1 mode is requested by the 0x404 command in ble_app_req_406_handle.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | 0 = tap tag, 1 = bt tag, any other value restores state and fails |

**Returns** `u32`: 0 on success, 0xC on failure

**Notes:** Whether 0x200122E0 and 0x200122A4 are one message header or two copies is not confirmed. ble_219_0c05c088 is probably a MAC or check value; the names tap and bt are the literal tags in the code.

- Addresses by version: 219: 0x0C053E1C
- Called by: `ble_app_req_406_handle`
- Calls: `ble_crypto_serial_mac`, `ble_crypto_ecdh_seal_p256`, `memset`
- Confidence: medium

## ble_unlock_auth_cb

**Unlock auth callback: send a folded 16-bit token to the VCU, then wait for the auth event**

Logs 'unlock_auth_cb' and sends VCU command 0x78 with a 2-byte payload that is DAT_200091C0 folded to 16 bits (low half plus high half). It then takes the event object at 0x20008F94 with xQueueSemaphoreTake, up to three attempts of 10 ticks each. On success it sets DAT_20008F79 to 1 and releases the object again with a zero-timeout xQueueGenericSend. If no event arrives in three attempts it returns without setting the flag. DAT_200091C0 is the CRC-32 computed by bt_app_set_name_and_advdata.

**Notes:** The event is signalled by ble_signal_event_8f94 (ble_219_0c02a478), presumably from the VCU reply path. Called from ble_unlock_request_start.

- Addresses by version: 219: 0x0C029284
- Called by: `ble_unlock_request_start`
- Calls: `uart_bridge_send_frame`, `trace_printf`, `xQueueGenericSend`, `xQueueSemaphoreTake`
- Confidence: medium
