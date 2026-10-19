# BLE - `ble_controller` functions

193 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`ble_active_idx_clear_if_match`](#ble_active_idx_clear_if_match) | 0x0C05C92C | Reset 0x20004992 to 0xff if it equals param_1 |
| [`ble_active_idx_get`](#ble_active_idx_get) | 0x0C05CAFC | Return the byte at 0x20004992 |
| [`ble_active_idx_set`](#ble_active_idx_set) | 0x0C05C920 | Store the byte at 0x20004992 |
| [`ble_cb_slot_130dc_set`](#ble_cb_slot_130dc_set) | 0x0C05844C | Store a value (likely a callback pointer) into global 0x200130dc |
| [`ble_cb_slot_14600_set`](#ble_cb_slot_14600_set) | 0x0C059EE8 | Store a 32-bit value into global 0x20014600 |
| [`ble_cb_slot_14604_set`](#ble_cb_slot_14604_set) | 0x0C059EF4 | Store a 32-bit value into global 0x20014604 |
| [`ble_cb_slot_14608_set`](#ble_cb_slot_14608_set) | 0x0C059F1C | Store the callback pointer used by ble_event_count_reached_check |
| [`ble_cb_slot_1460c_set`](#ble_cb_slot_1460c_set) | 0x0C059F00 | Store a 32-bit value into global 0x2001460c |
| [`ble_cb_slot_15e5c_set`](#ble_cb_slot_15e5c_set) | 0x0C05ADFC | Store a 32-bit value into global 0x20015e5c |
| [`ble_cb_slot_15f28_set`](#ble_cb_slot_15f28_set) | 0x0C05AE08 | Store a 32-bit value into global 0x20015f28 |
| [`ble_cfg_block_load`](#ble_cfg_block_load) | 0x0C05CEC8 | Load the 1040-byte configuration block from NV partition 1 and return its first 16 bytes |
| [`ble_conn_select_link_and_fill_info`](#ble_conn_select_link_and_fill_info) | 0x0C05A8A0 | Make link_id the active link, fill a 14-byte info record from its table entry + own BD_ADDR |
| [`ble_counter_20012344_step`](#ble_counter_20012344_step) | 0x0C05CB88 | Increment the counter at 0x20012344 and reset it to 0 if below 11 |
| [`ble_ctrl_can_send_br_edr_acl`](#ble_ctrl_can_send_br_edr_acl) | 0x0C066A64 | Return true when classic (BR/EDR) ACL packets can be sent now |
| [`ble_ctrl_can_send_le_acl`](#ble_ctrl_can_send_le_acl) | 0x0C0669A8 | Return true when LE ACL packets can be sent now |
| [`ble_ctrl_can_send_to_handle`](#ble_ctrl_can_send_to_handle) | 0x0C0669D8 | Return true when the connection with a given handle has free ACL slots |
| [`ble_ctrl_clear_pairing_flags`](#ble_ctrl_clear_pairing_flags) | 0x0C04F0A4 | Zero a group of seven single-byte flag/state variables |
| [`ble_ctrl_clear_secondary_list`](#ble_ctrl_clear_secondary_list) | 0x0C066D84 | Unlink every entry of the secondary list at env+0x224 without freeing them |
| [`ble_ctrl_conn_addr_class_by_handle`](#ble_ctrl_conn_addr_class_by_handle) | 0x0C06B92C | Classify a connection's address-type byte into a small class (by handle) |
| [`ble_ctrl_conn_alloc_and_register`](#ble_ctrl_conn_alloc_and_register) | 0x0C066168 | Allocate a connection record for a peer address and link it into the connection list |
| [`ble_ctrl_conn_arm_timeout_timer`](#ble_ctrl_conn_arm_timeout_timer) | 0x0C065F6C | Re-arm a connection deadline timer for (node+0x50 + 6 - now) milliseconds |
| [`ble_ctrl_conn_check_flags_0x60`](#ble_ctrl_conn_check_flags_0x60) | 0x0C06B218 | Return true when a connection's flags at +0x10 have both bits 0x20 and 0x40 set |
| [`ble_ctrl_conn_clear_pending_notify`](#ble_ctrl_conn_clear_pending_notify) | 0x0C0660C0 | Clear connection pending bits and emit event 0xE1/0x09 with a status byte |
| [`ble_ctrl_conn_find_by_addr`](#ble_ctrl_conn_find_by_addr) | 0x0C066588 | Find the connection record for a peer address and address type |
| [`ble_ctrl_conn_find_by_handle`](#ble_ctrl_conn_find_by_handle) | 0x0C066554 | Find the connection record whose handle (u16 at +0x0A) equals the argument |
| [`ble_ctrl_conn_free_and_report_disconnect`](#ble_ctrl_conn_free_and_report_disconnect) | 0x0C06637A | Unlink and free a connection, emitting event 0xD9/0x07 when bit 15 is set |
| [`ble_ctrl_conn_get_flag_bit4`](#ble_ctrl_conn_get_flag_bit4) | 0x0C06B274 | Return bit 4 (0x10) of a connection's flags at +0x10, or 0 for an unknown handle |
| [`ble_ctrl_conn_get_level_by_handle`](#ble_ctrl_conn_get_level_by_handle) | 0x0C06B2FC | Return the link security tier (0..4) of a connection looked up by handle |
| [`ble_ctrl_conn_get_state_by_handle`](#ble_ctrl_conn_get_state_by_handle) | 0x0C06B984 | Return the state byte at +0x0D of a connection looked up by handle (0xFF if unknown) |
| [`ble_ctrl_conn_has_pending_flag`](#ble_ctrl_conn_has_pending_flag) | 0x0C0665D4 | Return 1 when the connection with a handle has a pending bit (0x400 or 0x800) set |
| [`ble_ctrl_conn_idle_timeout_check`](#ble_ctrl_conn_idle_timeout_check) | 0x0C06611C | Timer callback: after 10 s since node+0x7C emit event 0x73 with the handle |
| [`ble_ctrl_conn_iter_init`](#ble_ctrl_conn_iter_init) | 0x0C066544 | Initialise a removal-safe iterator over the connection list at env+0x14 |
| [`ble_ctrl_conn_key_size_check`](#ble_ctrl_conn_key_size_check) | 0x0C066280 | Apply the encryption key size check and set the connection status for event 0xD8/0x03 |
| [`ble_ctrl_conn_set_pending_notify`](#ble_ctrl_conn_set_pending_notify) | 0x0C066040 | Set connection pending bit 0x400 or 0x800 and emit event 0xE0/0x0A |
| [`ble_ctrl_conn_teardown_and_count`](#ble_ctrl_conn_teardown_and_count) | 0x0C0663E8 | Stop a connection's timers, unlink and free it, then emit event 0x61 with the count |
| [`ble_ctrl_conn_timer_update_state`](#ble_ctrl_conn_timer_update_state) | 0x0C066B74 | Timer callback: set the connection state byte +0x56 and flush the deferred event |
| [`ble_ctrl_deferred_list_add`](#ble_ctrl_deferred_list_add) | 0x0C065A50 | Append an item to the global deferred list whose head is at 0x200190A4 |
| [`ble_ctrl_env_get_addr_type_and_addr_a`](#ble_ctrl_env_get_addr_type_and_addr_a) | 0x0C066D34 | Get own address type and 6-byte device address (variant using type flag at env+0x1DC) |
| [`ble_ctrl_env_get_addr_type_and_addr_b`](#ble_ctrl_env_get_addr_type_and_addr_b) | 0x0C066D5C | Get own address type and 6-byte device address (variant using type flag at env+0x218) |
| [`ble_ctrl_env_get_flag_bit6_at_0x18e`](#ble_ctrl_env_get_flag_bit6_at_0x18e) | 0x0C066D20 | Return bit 6 of the flag byte at env+0x18E (0 or 1) |
| [`ble_ctrl_env_get_mode_or_4`](#ble_ctrl_env_get_mode_or_4) | 0x0C066EE4 | Return env+0x58 unless the flag at env+0x64 is set, in which case return 4 |
| [`ble_ctrl_env_get_public_addr`](#ble_ctrl_env_get_public_addr) | 0x0C066F60 | Copy the 6-byte public device address from env+0x38 |
| [`ble_ctrl_env_get_u16_at_0x17a`](#ble_ctrl_env_get_u16_at_0x17a) | 0x0C066D10 | Return the 16-bit field at offset 0x17A of the controller environment struct |
| [`ble_ctrl_env_get_u16_at_0x56`](#ble_ctrl_env_get_u16_at_0x56) | 0x0C066F2C | Return the 16-bit field at env+0x56 |
| [`ble_ctrl_env_get_u8_at_0x198`](#ble_ctrl_env_get_u8_at_0x198) | 0x0C06BAC0 | Return the byte at env+0x198 (widely used state byte) |
| [`ble_ctrl_env_get_u8_at_0x40`](#ble_ctrl_env_get_u8_at_0x40) | 0x0C066F1C | Return the byte at env+0x40 |
| [`ble_ctrl_env_get_u8_at_0x46`](#ble_ctrl_env_get_u8_at_0x46) | 0x0C067168 | Return the byte at env+0x46 |
| [`ble_ctrl_env_get_u8_at_0x5a`](#ble_ctrl_env_get_u8_at_0x5a) | 0x0C066ED4 | Return the byte at env+0x5A |
| [`ble_ctrl_env_get_u8_at_0x64`](#ble_ctrl_env_get_u8_at_0x64) | 0x0C066F0C | Return the byte at env+0x64 (override flag used by 0c066ee4) |
| [`ble_ctrl_env_set_callbacks_and_notify`](#ble_ctrl_env_set_callbacks_and_notify) | 0x0C066EBC | Store callback table pointer at env+8 and invoke its second entry with env+4 |
| [`ble_ctrl_env_set_iface_and_init`](#ble_ctrl_env_set_iface_and_init) | 0x0C066DE8 | Store interface table pointer at env+0x10 and call its first entry |
| [`ble_ctrl_env_set_peer_addr`](#ble_ctrl_env_set_peer_addr) | 0x0C066F3C | Store a 6-byte address, type and valid flag at env+0x230..0x237 |
| [`ble_ctrl_env_set_u8_at_0x42`](#ble_ctrl_env_set_u8_at_0x42) | 0x0C067148 | Set the byte at env+0x42 |
| [`ble_ctrl_env_set_u8_at_0x45`](#ble_ctrl_env_set_u8_at_0x45) | 0x0C067158 | Set the byte at env+0x45 |
| [`ble_ctrl_env_set_u8_at_0x59`](#ble_ctrl_env_set_u8_at_0x59) | 0x0C066EFC | Set the byte at env+0x59 |
| [`ble_ctrl_flush_deferred_event`](#ble_ctrl_flush_deferred_event) | 0x0C066B20 | Send the deferred 0x6F event once the controller is idle and a link slot is free |
| [`ble_ctrl_get_data_len_or_default`](#ble_ctrl_get_data_len_or_default) | 0x0C06EE60 | Return the configured 16-bit length DAT_2001949c, or 251 if it is 0 |
| [`ble_ctrl_get_flag_3fe8`](#ble_ctrl_get_flag_3fe8) | 0x0C053824 | Return byte global 0x20003fe8 |
| [`ble_ctrl_get_max_data_len`](#ble_ctrl_get_max_data_len) | 0x0C06EE5C | Return the constant 251 (0xFB) |
| [`ble_ctrl_get_sanitized_setting_20004344`](#ble_ctrl_get_sanitized_setting_20004344) | 0x0C0581F0 | Return the byte at 0x20004344, forcing it to 0x0e unless it is 0x0e or 0x10 |
| [`ble_ctrl_iface_iterate_dispatch`](#ble_ctrl_iface_iterate_dispatch) | 0x0C06662C | Iterate the interface table's items and pass each one to its handler |
| [`ble_ctrl_iface_probe_and_start`](#ble_ctrl_iface_probe_and_start) | 0x0C06C298 | Call ops[1]; if it returns 0, set start flags and call ops[8](buf, 1) |
| [`ble_ctrl_noop_callback`](#ble_ctrl_noop_callback) | 0x0C06C1E4 | Empty function used as a no-op callback |
| [`ble_ctrl_opcode_in_set`](#ble_ctrl_opcode_in_set) | 0x0C06CA0C | Return 1 if opcode param_1 is in a fixed set and flag bit 15 of param_2 is clear |
| [`ble_ctrl_pending_drain_and_arm_timer`](#ble_ctrl_pending_drain_and_arm_timer) | 0x0C065EF8 | Free every entry of the list at env+0x1E8 and arm the 1000 ms timer at env+0x19C |
| [`ble_ctrl_set_flag_3fac`](#ble_ctrl_set_flag_3fac) | 0x0C052B44 | Store a byte configuration value into global 0x20003fac |
| [`ble_ctrl_set_flag_fdc5`](#ble_ctrl_set_flag_fdc5) | 0x0C052B38 | Store a byte configuration value into global 0x2000fdc5 |
| [`ble_ctrl_set_key_dist_flags`](#ble_ctrl_set_key_dist_flags) | 0x0C04F848 | Translate two key-distribution bitmasks into controller-internal flag bytes |
| [`ble_ctrl_store_keys_and_addrs`](#ble_ctrl_store_keys_and_addrs) | 0x0C04F0C8 | Copy three 16-byte keys and three short address/info blobs into controller globals |
| [`ble_ctrl_update_link_slot_flag`](#ble_ctrl_update_link_slot_flag) | 0x0C065E20 | Recompute the link-slot-available flag at env+0x220 from the connection list |
| [`ble_ctx_get_base_20014580`](#ble_ctx_get_base_20014580) | 0x0C059F5C | Return the address of the context structure at 0x20014580 |
| [`ble_deferred_list_post`](#ble_deferred_list_post) | 0x0C05D08C | Post one item to the deferred list under the mutex and signal the worker event |
| [`ble_event_count_reached_check`](#ble_event_count_reached_check) | 0x0C05A11C | Check whether enough events have been counted and report which kind via *param_1 |
| [`ble_event_counters_clear`](#ble_event_counters_clear) | 0x0C059F28 | Zero the four counter/flag bytes at 0x20004317, 0x2000431d, 0x20004318, 0x2000431c |
| [`ble_event_thresholds_refresh_from_link`](#ble_event_thresholds_refresh_from_link) | 0x0C05A1AC | Recompute both event-count thresholds (0x2000432f, 0x20004316) from the link table entry |
| [`ble_flag_20017114_get`](#ble_flag_20017114_get) | 0x0C05CF10 | Return the byte at 0x20017114 |
| [`ble_flag_20017114_set`](#ble_flag_20017114_set) | 0x0C05CF04 | Store the byte at 0x20017114 |
| [`ble_flags_bit15_get`](#ble_flags_bit15_get) | 0x0C05CFD0 | Return bit 15 of the flag word at 0x200042fc |
| [`ble_flags_bit4_get`](#ble_flags_bit4_get) | 0x0C05CFF4 | Return bit 4 of the flag word at 0x200042fc |
| [`ble_flags_clear`](#ble_flags_clear) | 0x0C058150 | Clear mask bits in the flag word at 0x200042fc |
| [`ble_flags_set`](#ble_flags_set) | 0x0C058140 | OR a mask into the flag word at 0x200042fc |
| [`ble_gen_static_random_addr`](#ble_gen_static_random_addr) | 0x0C05C2C0 | Generate a 6-byte static random device address into the output buffer |
| [`ble_get_byte_12b84`](#ble_get_byte_12b84) | 0x0C055518 | Return byte global 0x20012b84 |
| [`ble_get_byte_12b85`](#ble_get_byte_12b85) | 0x0C055558 | Return byte global 0x20012b85 |
| [`ble_get_byte_12eb4`](#ble_get_byte_12eb4) | 0x0C0567BC | Return byte global 0x20012eb4 |
| [`ble_get_flag_12606`](#ble_get_flag_12606) | 0x0C054728 | Return byte flag 0x20012606 |
| [`ble_get_packed_word_12cb0`](#ble_get_packed_word_12cb0) | 0x0C055604 | Return 32-bit global 0x20012cb0 |
| [`ble_get_state_ptr_11e10`](#ble_get_state_ptr_11e10) | 0x0C053884 | Return address of the object at 0x20011e10 |
| [`ble_get_state_ptr_42f8`](#ble_get_state_ptr_42f8) | 0x0C0571CC | Return address of the object at 0x200042f8 |
| [`ble_get_value_407a`](#ble_get_value_407a) | 0x0C054524 | Output byte global 0x2000407a when index is 0 |
| [`ble_get_word_13074`](#ble_get_word_13074) | 0x0C058134 | Return 32-bit global 0x20013074 |
| [`ble_get_word_41cc`](#ble_get_word_41cc) | 0x0C055564 | Return 32-bit global 0x200041cc |
| [`ble_hook_invoke4`](#ble_hook_invoke4) | 0x0C06C0C0 | Call the registered 4-argument hook, optionally ticking a periodic callback first |
| [`ble_hook_invoke_indexed`](#ble_hook_invoke_indexed) | 0x0C06C138 | Call hook table entry 2 for channel idx (<3) if that channel is enabled |
| [`ble_hook_noop_05a9c0`](#ble_hook_noop_05a9c0) | 0x0C05A9C0 | Empty hook, returns immediately |
| [`ble_hook_noop_05cba8`](#ble_hook_noop_05cba8) | 0x0C05CBA8 | Empty hook, returns immediately |
| [`ble_hook_noop_05cbc0`](#ble_hook_noop_05cbc0) | 0x0C05CBC0 | Empty hook, returns immediately |
| [`ble_hook_noop_05cec4`](#ble_hook_noop_05cec4) | 0x0C05CEC4 | Empty hook, returns immediately |
| [`ble_hook_table_register`](#ble_hook_table_register) | 0x0C06C090 | Install the hook table and reset the hook period counter |
| [`ble_iface_exchange_tables`](#ble_iface_exchange_tables) | 0x0C06C44C | Save the peer interface table pointer and return the local interface table |
| [`ble_link_get_byte_200134a4`](#ble_link_get_byte_200134a4) | 0x0C0591E4 | Return the byte at 0x200134a4 |
| [`ble_link_param_monitor_step`](#ble_link_param_monitor_step) | 0x0C0585A4 | Run one link-parameter monitor step and emit a 27-byte status record to the host |
| [`ble_link_table_alloc_slot`](#ble_link_table_alloc_slot) | 0x0C05976C | Find the link record for a key, or the first free slot among slots 0 to 3 |
| [`ble_link_table_find_by_addr`](#ble_link_table_find_by_addr) | 0x0C059830 | Find the link table entry whose 6-byte address at +12 equals param_1 |
| [`ble_link_table_find_by_key`](#ble_link_table_find_by_key) | 0x0C0597F0 | Find the table entry whose key byte matches and return its pointer |
| [`ble_link_table_find_index_by_key`](#ble_link_table_find_index_by_key) | 0x0C059884 | Return the index of the table entry with the given key, or 0xff |
| [`ble_link_table_get_base`](#ble_link_table_get_base) | 0x0C059558 | Return the address of the link/connection table base at 0x200134bc |
| [`ble_link_table_nv_load_trim`](#ble_link_table_nv_load_trim) | 0x0C0596C8 | Reload the link table from NV, free unused slots and save if changed |
| [`ble_link_table_prune_by_ctrl`](#ble_link_table_prune_by_ctrl) | 0x0C05A4A8 | Reconcile the link table with the controller address list through LL hooks |
| [`ble_link_table_remove_index`](#ble_link_table_remove_index) | 0x0C059560 | Remove the link-table record at an index and persist the table |
| [`ble_link_table_remove_key`](#ble_link_table_remove_key) | 0x0C0595EC | Remove link-table records that carry a given key and persist the table |
| [`ble_link_table_reset`](#ble_link_table_reset) | 0x0C059724 | Clear the link table to empty and save it to NV |
| [`ble_link_table_save`](#ble_link_table_save) | 0x0C059754 | Save the link table to NV record 0xFB3 and return 1 |
| [`ble_link_table_write_at0`](#ble_link_table_write_at0) | 0x0C05822C | Copy up to 24 bytes to the start of the current link entry and commit |
| [`ble_link_table_write_at18`](#ble_link_table_write_at18) | 0x0C058208 | Copy up to 24 bytes into the current link entry at offset 0x18 and commit |
| [`ble_listener_broadcast_event`](#ble_listener_broadcast_event) | 0x0C06C4C0 | Send an event buffer to the hook and to every listener in the list at 0x20019450 |
| [`ble_mode_nv_decode_read`](#ble_mode_nv_decode_read) | 0x0C05CD10 | Read the NV mode byte and decode it to a 0-3 mode value |
| [`ble_mode_nv_disable`](#ble_mode_nv_disable) | 0x0C05CD84 | Set the NV mode byte to its off value, or to 0xFD for other values |
| [`ble_mode_nv_enable`](#ble_mode_nv_enable) | 0x0C05CDCC | Set the NV mode byte to 1, or to 3 when it was another value |
| [`ble_mode_nv_encode_write`](#ble_mode_nv_encode_write) | 0x0C05CCD8 | Encode a 0-3 mode value to the NV mode byte and write it |
| [`ble_mode_nv_is_inactive`](#ble_mode_nv_is_inactive) | 0x0C05CD4C | Return 0 when the NV mode byte is 1 or 3, otherwise 1 |
| [`ble_pack_version_nibbles`](#ble_pack_version_nibbles) | 0x0C0555DC | OR the three nibble bytes into the 24-bit packed word at 0x20012cb0 |
| [`ble_pair_table_lookup`](#ble_pair_table_lookup) | 0x0C053EF4 | Look up a 16-bit key in an array of {key,value} u16 pairs and compare the value |
| [`ble_peer_bdaddr_cache_set`](#ble_peer_bdaddr_cache_set) | 0x0C05C2FC | Cache a 6-byte address at 0x20004977 and mark it valid |
| [`ble_pending_param_store`](#ble_pending_param_store) | 0x0C05A9A4 | Latch a parameter pair and set a valid flag when param_1 == 2, else clear the flag |
| [`ble_rom_ptr_table_get_0c07ffac`](#ble_rom_ptr_table_get_0c07ffac) | 0x0C05D48C | Return the address of the pointer table at 0x0c07ffac |
| [`ble_rom_ptr_table_get_0c0800b4`](#ble_rom_ptr_table_get_0c0800b4) | 0x0C05D4A4 | Return the address of the pointer table at 0x0c0800b4 |
| [`ble_rom_table_get_0c07fe00`](#ble_rom_table_get_0c07fe00) | 0x0C05B71C | Return the address of the constant data block at 0x0c07fe00 |
| [`ble_rom_table_get_0c0810e0`](#ble_rom_table_get_0c0810e0) | 0x0C05B670 | Return the address of the constant data block at 0x0c0810e0 |
| [`ble_rssi_filter_update`](#ble_rssi_filter_update) | 0x0C059B60 | Outlier-clamp and Kalman-filter a 5-sample signed RSSI window, return the mean |
| [`ble_set_flag_12606`](#ble_set_flag_12606) | 0x0C054710 | Set byte flag 0x20012606 to 1 |
| [`ble_set_indexed_word_1307c`](#ble_set_indexed_word_1307c) | 0x0C0571B0 | Store a 32-bit value in the 4-entry u32 array at 0x2001307c |
| [`ble_set_mode_14_or_16`](#ble_set_mode_14_or_16) | 0x0C0581E0 | Store 0x10 if param_1 is 0x10, otherwise 0x0e, into byte 0x20004344 |
| [`ble_set_timeout_ms_to_us`](#ble_set_timeout_ms_to_us) | 0x0C05527C | Store param_1 * 1000 into 0x200041c8 |
| [`ble_set_word_1308c`](#ble_set_word_1308c) | 0x0C0571A4 | Store 32-bit value into global 0x2001308c |
| [`ble_set_word_130d4`](#ble_set_word_130d4) | 0x0C0571C0 | Store 32-bit value into global 0x200130d4 |
| [`ble_slot_count_used`](#ble_slot_count_used) | 0x0C05341C | Count slots in the 4-entry table whose id byte is not 0xff |
| [`ble_slot_expiry_scan`](#ble_slot_expiry_scan) | 0x0C0534E0 | Scan the slot table against the tick count; the result is always 0 |
| [`ble_slot_get_field_0x14`](#ble_slot_get_field_0x14) | 0x0C088520 | Return the 32-bit field at offset 0x14 of the slot record selected by an index-mapped id |
| [`ble_slot_get_header_ptr`](#ble_slot_get_header_ptr) | 0x0C053764 | Return address of the structure at 0x20010188 preceding the slot table |
| [`ble_slot_get_u16_at_0x08`](#ble_slot_get_u16_at_0x08) | 0x0C088550 | Return the 16-bit field at offset 0x08 of the slot record selected by an index-mapped id |
| [`ble_slot_get_u16_at_0x0a`](#ble_slot_get_u16_at_0x0a) | 0x0C088538 | Return the 16-bit field at offset 0x0a of the slot record selected by an index-mapped id |
| [`ble_slot_invoke_callback_evt4`](#ble_slot_invoke_callback_evt4) | 0x0C08915C | Call the slot's registered callback (offset 0x18) with event code 4, return 0 or -1 if none |
| [`ble_slot_mgr_check_flag5`](#ble_slot_mgr_check_flag5) | 0x0C0531B8 | When the slot manager is ready, run the flag-5 test for slot param_1 (or all slots) |
| [`ble_slot_mgr_is_ready`](#ble_slot_mgr_is_ready) | 0x0C0537A0 | Check that the slot manager marker byte equals 0xa5 |
| [`ble_slot_set_flag`](#ble_slot_set_flag) | 0x0C053390 | Set or clear a bit in the flag word of the slot with a given id |
| [`ble_slot_set_flag_101e0`](#ble_slot_set_flag_101e0) | 0x0C053830 | Store a byte into global 0x200101e0 |
| [`ble_slot_test_flag`](#ble_slot_test_flag) | 0x0C0531D0 | Test whether a bit is set in the flag word of the slot with a given id |
| [`ble_slot_test_flag_any`](#ble_slot_test_flag_any) | 0x0C05328C | Test flag bit param_2 on one slot, or on each slot until one reports set |
| [`ble_state_12c81_is_2`](#ble_state_12c81_is_2) | 0x0C055230 | Check whether state byte 0x20012c81 equals 2 |
| [`ble_state_407a_copy`](#ble_state_407a_copy) | 0x0C05CFC8 | Copy the state byte 0x2000407a to *param_1 (ble_get_value_407a with index 0) |
| [`ble_state_407a_read`](#ble_state_407a_read) | 0x0C05C778 | Return the state byte at 0x2000407a (via ble_get_value_407a index 0) |
| [`ble_state_cb_register`](#ble_state_cb_register) | 0x0C059F0C | Install a callback into one of four notification slots at 0x20014610 |
| [`ble_state_change_notify`](#ble_state_change_notify) | 0x0C059E9C | Update the state byte at 0x20004970 and notify the registered callbacks |
| [`ble_state_is_0x102`](#ble_state_is_0x102) | 0x0C05A198 | Test whether the state word at 0x200145b0 equals 0x102 |
| [`ble_state_is_0x110`](#ble_state_is_0x110) | 0x0C059390 | Test whether the 32-bit state word at 0x200145b0 equals 0x110 |
| [`ble_status_bits_get`](#ble_status_bits_get) | 0x0C05CBC4 | Compose a 4-bit BLE status mask from object flags, slot state, timer flag and mode |
| [`ble_thunk_call_0c03aafc`](#ble_thunk_call_0c03aafc) | 0x0C089478 | Thin wrapper that calls a function at fixed address 0x0c03aafc (Thumb) with its argument |
| [`ble_thunk_call_0c03ab18`](#ble_thunk_call_0c03ab18) | 0x0C089488 | Thin wrapper that calls a function at fixed address 0x0c03ab18 (Thumb) with its argument |
| [`ble_thunk_call_0c0401b0`](#ble_thunk_call_0c0401b0) | 0x0C089468 | Thin wrapper that forwards its single argument to FUN_0c0401b0 |
| [`ble_thunk_call_0c040290`](#ble_thunk_call_0c040290) | 0x0C0894A8 | Thin wrapper that forwards its single argument to FUN_0c040290 |
| [`ble_unpack_version_nibbles`](#ble_unpack_version_nibbles) | 0x0C055610 | Split a 16-bit value into four nibble bytes at 0x20012cac..caf |
| [`bt_bdaddr_reverse_inplace`](#bt_bdaddr_reverse_inplace) | 0x0C05A9E4 | Reverse the byte order of a 6-byte Bluetooth device address in place |
| [`bt_drv_set_global_2000bd1c`](#bt_drv_set_global_2000bd1c) | 0x0C03AC8C | Store a 32-bit value into global DAT_2000bd1c |
| [`ll_conn_params_in_range`](#ll_conn_params_in_range) | 0x0C066508 | Check requested connection parameters against allowed range |
| [`ll_env_clear_flag_170`](#ll_env_clear_flag_170) | 0x0C066C1C | Clear byte at controller env offset 0x170 |
| [`ll_env_get_flag_170`](#ll_env_get_flag_170) | 0x0C066BD8 | Return byte at controller env offset 0x170 |
| [`ll_env_get_u16_196`](#ll_env_get_u16_196) | 0x0C066CF4 | Return u16 at controller env offset 0x196 |
| [`ll_env_get_u32_68`](#ll_env_get_u32_68) | 0x0C066D04 | Return u32 at controller env offset 0x68 |
| [`ll_env_get_u32_68_plus8`](#ll_env_get_u32_68_plus8) | 0x0C06D5C8 | Return the u32 at controller env +0x68 plus 8 |
| [`ll_env_has_free_slot`](#ll_env_has_free_slot) | 0x0C066A94 | Check whether another link slot is available |
| [`ll_env_init`](#ll_env_init) | 0x0C066DFC | Initialise the link-layer environment and register the HCI packet handler |
| [`ll_env_is_ready`](#ll_env_is_ready) | 0x0C066978 | Check whether controller env permits the operation |
| [`ll_env_reset_defaults`](#ll_env_reset_defaults) | 0x0C065E8C | Reset link-layer environment runtime fields to defaults |
| [`ll_env_run_stop_hooks`](#ll_env_run_stop_hooks) | 0x0C065DF8 | Invoke controller hooks then clear status byte 0x198 |
| [`ll_get_conn_param_range`](#ll_get_conn_param_range) | 0x0C0664E8 | Copy 12-byte connection-parameter acceptance range |
| [`ll_hook_call_0x14`](#ll_hook_call_0x14) | 0x0C066618 | Call optional external hook at table offset 0x14 |
| [`ll_hook_call_0x18`](#ll_hook_call_0x18) | 0x0C066698 | Call optional external hook at table offset 0x18 |
| [`ll_hook_call_0x1c`](#ll_hook_call_0x1c) | 0x0C0666B0 | Call optional external hook at table offset 0x1c |
| [`ll_hook_call_0x20`](#ll_hook_call_0x20) | 0x0C0666D0 | Call optional external hook at table offset 0x20 |
| [`ll_link_check_flag_or_state_by_key`](#ll_link_check_flag_or_state_by_key) | 0x0C06BBB8 | Test a link record found by key: flag byte at +0x1C2, or state 7 or 8 |
| [`ll_link_emit_event_78`](#ll_link_emit_event_78) | 0x0C06C504 | Emit vendor event 0x78 for a link and move matching L2CAP channel sub-states |
| [`ll_link_emit_event_79`](#ll_link_emit_event_79) | 0x0C06C710 | Send a 4-byte vendor event 0x79 with a u16 handle to a callback and the hook |
| [`ll_link_emit_event_7d`](#ll_link_emit_event_7d) | 0x0C06C684 | Emit vendor event 0x7D (23 bytes) with a sub-code and link parameters |
| [`ll_link_emit_event_code_handle`](#ll_link_emit_event_code_handle) | 0x0C06C648 | Send a 4-byte H4 event whose code is param_2 and whose parameter is the record id |
| [`ll_link_get_byte_1cb_by_key`](#ll_link_get_byte_1cb_by_key) | 0x0C06BC24 | Return the byte at +0x1CB of a link record found by key when two flags are set |
| [`ll_link_get_ext_byte_by_key`](#ll_link_get_ext_byte_by_key) | 0x0C06BADC | Look up a link record by key and return one of its status bytes |
| [`ll_link_get_flag_by_key`](#ll_link_get_flag_by_key) | 0x0C06BB3C | Return a flag from a link record found by key, depending on its class byte |
| [`ll_link_get_level`](#ll_link_get_level) | 0x0C065FBC | Classify a link/device record into level 0..4 |
| [`ll_link_notify_event_72`](#ll_link_notify_event_72) | 0x0C06C460 | Send a 16-byte vendor event 0x72 with link parameters to the hook and the link callback |
| [`lm_env_defaults_init`](#lm_env_defaults_init) | 0x0C03E4C8 | Initialise controller default parameters in two small RAM tables |
| [`lm_get_state_9bit`](#lm_get_state_9bit) | 0x0C03E480 | Return the low 9 bits of global DAT_20003ec0 |
| [`thumb2_encode_b_w`](#thumb2_encode_b_w) | 0x0C03CE68 | Build the 32-bit Thumb-2 B.W (T4) branch instruction from a site address and a target |

## ble_active_idx_clear_if_match

**Reset 0x20004992 to 0xff if it equals param_1**

Compares the byte DAT_20004992 with param_1 and, when equal, writes 0xff (the 'none' marker). Used to release the stored active index when the matching link goes away. No direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | index/handle to release |

- Addresses by version: 219: 0x0C05C92C
- Confidence: medium

## ble_active_idx_get

**Return the byte at 0x20004992**

Trivial getter returning the stored active link index (0xff means none). No direct callers.

**Returns** `u8`: stored index, 0xff if none

- Addresses by version: 219: 0x0C05CAFC
- Confidence: medium

## ble_active_idx_set

**Store the byte at 0x20004992**

Writes param_1 to the 8-bit global DAT_20004992. This global is cleared to 0xff (invalid) by ble_active_idx_clear_if_match and read by ble_active_idx_get, so it holds a link/connection index or handle. No direct callers (invoked indirectly).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | index/handle to store |

- Addresses by version: 219: 0x0C05C920
- Confidence: medium

## ble_cb_slot_130dc_set

**Store a value (likely a callback pointer) into global 0x200130dc**

Trivial setter: writes param_1 to the 32-bit global DAT_200130dc. It is called only from ble_219_0c0297b0, which also registers several other slots (0x20014600/04/08/0c/10.., 0x20015e5c), so the value is most likely a callback function pointer installed during init.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value/callback pointer to store |

- Addresses by version: 219: 0x0C05844C
- Called by: `ble_219_0c0297b0`
- Confidence: medium

## ble_cb_slot_14600_set

**Store a 32-bit value into global 0x20014600**

Trivial setter: writes param_1 to the 32-bit global at 0x20014600. Value (likely a callback pointer) to store. Called from ble_219_0c0297b0 (a registration/init routine that also programs several sibling slots).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | Value (likely a callback pointer) to store |

- Addresses by version: 219: 0x0C059EE8
- Called by: `ble_219_0c0297b0`
- Confidence: medium

## ble_cb_slot_14604_set

**Store a 32-bit value into global 0x20014604**

Trivial setter: writes param_1 to the 32-bit global at 0x20014604. Value (likely a callback pointer) to store. Called from ble_219_0c0297b0 (a registration/init routine that also programs several sibling slots).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | Value (likely a callback pointer) to store |

- Addresses by version: 219: 0x0C059EF4
- Called by: `ble_219_0c0297b0`
- Confidence: medium

## ble_cb_slot_14608_set

**Store the callback pointer used by ble_event_count_reached_check**

Writes param_1 to the 32-bit global DAT_20014608. That global is called as a function in ble_219_0c05a11c with a pointer to a small stack buffer which it fills in, so param_1 is a callback taking a pointer to an info structure. Callers: ble_219_0c02973c and ble_219_0c0297b0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | callback function pointer |

- Addresses by version: 219: 0x0C059F1C
- Called by: `ble_219_0c02973c`, `ble_219_0c0297b0`
- Confidence: medium

## ble_cb_slot_1460c_set

**Store a 32-bit value into global 0x2001460c**

Trivial setter: writes param_1 to the 32-bit global at 0x2001460c. Value (likely a callback pointer) to store. Called from ble_219_0c0297b0 (a registration/init routine that also programs several sibling slots).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | Value (likely a callback pointer) to store |

- Addresses by version: 219: 0x0C059F00
- Called by: `ble_219_0c0297b0`
- Confidence: medium

## ble_cb_slot_15e5c_set

**Store a 32-bit value into global 0x20015e5c**

Trivial setter: writes param_1 to the 32-bit global at 0x20015e5c. Value (likely a callback pointer) to store. Called from ble_219_0c02973c and ble_219_0c0297b0 (a registration/init routine that also programs several sibling slots).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | Value (likely a callback pointer) to store |

- Addresses by version: 219: 0x0C05ADFC
- Called by: `ble_219_0c02973c`, `ble_219_0c0297b0`
- Confidence: medium

## ble_cb_slot_15f28_set

**Store a 32-bit value into global 0x20015f28**

Trivial setter: writes param_1 to the 32-bit global at 0x20015f28. Value (likely a callback pointer) to store. Called from ble_219_0c02bdd0 (a registration/init routine that also programs several sibling slots).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | Value (likely a callback pointer) to store |

- Addresses by version: 219: 0x0C05AE08
- Called by: `ble_219_0c02bdd0`
- Confidence: medium

## ble_cfg_block_load

**Load the 1040-byte configuration block from NV partition 1 and return its first 16 bytes**

Zeroes the RAM object returned by ble_get_state_ptr_11e10 (at 0x20011E10, 0x410 bytes) with memset, then reads the 1040-byte configuration block from NV record 0x1389 (partition 1, offset 0) into it. It then copies the first 16 bytes of the object to out, which is likely a 128-bit key such as an identity key (unconfirmed).

| Parameter | Type | Description |
|---|---|---|
| `out` | `ptr` | 16-byte output buffer |

**Notes:** The meaning of the first 16 bytes is a guess. The return value of the NV read is ignored.

- Addresses by version: 219: 0x0C05CEC8
- Called by: `ble_219_0c02a8f8`
- Calls: `ble_get_state_ptr_11e10`, `ble_nv_record_read`, `memset`
- Confidence: medium

## ble_conn_select_link_and_fill_info

**Make link_id the active link, fill a 14-byte info record from its table entry + own BD_ADDR**

Fetches the local public address (ble_ctrl_env_get_public_addr into a 6-byte stack buffer, then bt_bdaddr_reverse_inplace), looks the link up with ble_link_table_find_by_key(param_1) and writes (u8)param_1 to DAT_200042f8 (byte 0 of the shared state object = current link id). If no entry: DAT_20004300 = 0 and the u16 at 0x2000432e (clearing threshold 0x2000432f) = 0. If found: out[0] = (out[0] & 0xfc) | (entry[5] & 1) | ((entry[6] & 1) << 1), out[1] = entry[4], out[2..7] = entry[0xc..0x11] (6 bytes, presumably the peer address), DAT_20004316 = entry[2] + (3 - entry[3]) * 8 when entry[2] != 0 (same threshold formula as ble_event_thresholds_refresh_from_link) and DAT_20004300 = entry[5] (the byte that gates ble_event_count_reached_check). In both cases out[8..13] = the reversed own address. Caller: 0c029960.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | link key/id (low byte stored in 0x200042f8) |
| `param_2` | `ptr` | out: 14-byte record (flags, type byte, 6-byte peer addr, 6-byte own addr) |

**Notes:** Field meanings of the 0x14-byte link entry (bytes 4,5,6 and the 6 bytes at +0xc) are inferred; the record layout is factual.

- Addresses by version: 219: 0x0C05A8A0
- Called by: `ble_219_0c029960`
- Calls: `ble_link_table_find_by_key`, `bt_bdaddr_reverse_inplace`, `ble_ctrl_env_get_public_addr`
- Confidence: medium

## ble_counter_20012344_step

**Increment the counter at 0x20012344 and reset it to 0 if below 11**

Increments the global DAT_20012344 and, if the result is less than 0xb, sets it back to 0, exactly as decompiled. The condition looks inverted for a wrap-at-11 counter, so either the decompiler mangled the comparison or the counter semantics are unusual. Called from the four similar functions ble_219_0c0540f4, 0c054180, 0c05420c and 0c054298.

**Notes:** Condition may be a decompilation artifact (unsigned vs signed compare); verify against disassembly.

- Addresses by version: 219: 0x0C05CB88
- Called by: `ble_219_0c0540f4`, `ble_219_0c054180`, `ble_219_0c05420c`, `ble_slot_store_and_queue`
- Confidence: low

## ble_ctrl_can_send_br_edr_acl

**Return true when classic (BR/EDR) ACL packets can be sent now**

Same gating as ble_ctrl_can_send_le_acl (the flag at env+0x5C and the table+0x14 check with argument 2), but queries hci_number_free_acl_slots with the classic selector 0xFD.

**Returns** `bool`: true when a classic ACL packet can be queued

- Addresses by version: 219: 0x0C066A64
- Called by: `ble_219_0c06cb3c`
- Calls: `hci_number_free_acl_slots`
- Confidence: high

## ble_ctrl_can_send_le_acl

**Return true when LE ACL packets can be sent now**

Returns false when the byte at env+0x5C is set. Otherwise it requires the readiness check at table+0x14 (called with 2) to succeed or be absent, then returns whether hci_number_free_acl_slots(0) is non-zero, i.e. free LE slots exist.

**Returns** `bool`: true when an LE ACL packet can be queued

- Addresses by version: 219: 0x0C0669A8
- Called by: `ble_219_0c04de00`, `ble_219_0c06cb3c`
- Calls: `hci_number_free_acl_slots`
- Confidence: high

## ble_ctrl_can_send_to_handle

**Return true when the connection with a given handle has free ACL slots**

Runs the readiness check at table+0x14 (argument 2), then searches the connection list for the handle and returns hci_number_free_acl_slots(record address type) != 0. If the handle is unknown it logs 'hci_number_free_acl_slots: handle 0x%04x not in connection list' (hci.c line 0x281) and returns false.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `u16` | connection handle |

**Returns** `bool`: true when that connection can take another packet

- Addresses by version: 219: 0x0C0669D8
- Called by: `ble_219_0c066a4c`, `ble_219_0c066c2c`, `ble_219_0c0674e8`, `ble_219_0c06d5dc`, `ble_219_0c06ed64`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`, `hci_number_free_acl_slots`, `ble_hook_invoke_indexed`
- Confidence: high

## ble_ctrl_clear_pairing_flags

**Zero a group of seven single-byte flag/state variables**

Writes 0 to bytes at 0x2000ffe9, 0x2000ff55, 0x2000ff6b, 0x2000ff5b, 0x2000ff5f, 0x2000ff63 and 0x2000ff67. These sit next to the key-distribution bytes set by the sibling setters (0x2000ff56/58) and are probably per-pairing state. Called once from the same init routine (ble_219_0c051eb8) that loads the keys and address structures.

**Notes:** Exact meaning of each cleared byte unknown.

- Addresses by version: 219: 0x0C04F0A4
- Called by: `ble_219_0c051eb8`
- Confidence: low

## ble_ctrl_clear_secondary_list

**Unlink every entry of the secondary list at env+0x224 without freeing them**

Walks the list at env+0x224 with the removal-safe iterator and unlinks each entry with btstack_linked_list_remove. The entries are not returned to any pool, so this only empties the list. That list is separate from the connection list (env+0x14) and the event-handler list (env+0x20).

- Addresses by version: 219: 0x0C066D84
- Calls: `btstack_linked_list_remove`, `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: high

## ble_ctrl_conn_addr_class_by_handle

**Classify a connection's address-type byte into a small class (by handle)**

Looks up the connection by handle and maps its address-type byte at +0xC. 0xFC gives 2, 0x00 and 0x01 (LE public and random) give 3, 0x02..0xFB give 0, 0xFD gives 1, and 0xFE and 0xFF give 0. Returns 0 when no connection has that handle. The class names are inferred from the sentinel values and are not confirmed.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `u16` | connection handle |

**Returns** `u8`: class 0..3 as described

- Addresses by version: 219: 0x0C06B92C
- Called by: `ble_219_0c04e702`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: medium

## ble_ctrl_conn_alloc_and_register

**Allocate a connection record for a peer address and link it into the connection list**

Takes a zeroed hci_connection block from btstack_memory_hci_connection_get (800-byte pool). It sets the state byte +0x3C to 3, the address-type byte +0xC from the argument, the handle +0xA to 0xFFFF (unassigned), +0xD to 0xFF, +0x28 and +0x36 to 0xFFFF, +0x57 to 0xFF, +0x1A2 to 0xFF, clears the flags at +0x10 and +0x68, and copies the peer address to +4 with bd_addr_copy. It stores the current time at +0x7C, installs handler 0x0C06611C and context = the record on the +0x6C timer (not started here), and appends the record to the list at env+0x14. Returns the record, or NULL when the pool is empty.

| Parameter | Type | Description |
|---|---|---|
| `addr` | `ptr` | 6-byte peer BD_ADDR |
| `addr_type` | `u8` | address type stored at +0xC |

**Returns** `ptr`: new connection record, or NULL when the pool is exhausted

- Addresses by version: 219: 0x0C066168
- Called by: `ble_219_0c066f74`, `ble_219_0c068da8`, `ble_219_0c06b498`, `ble_219_0c06b4bc`
- Calls: `btstack_linked_list_add`, `btstack_memory_hci_connection_get`, `btstack_run_loop_set_timer_handler`, `btstack_run_loop_set_timer_context`, `btstack_run_loop_get_time_ms`, `bd_addr_copy`
- Confidence: medium

## ble_ctrl_conn_arm_timeout_timer

**Re-arm a connection deadline timer for (node+0x50 + 6 - now) milliseconds**

Reads the run-loop time, then picks the timer embedded in the connection record: the one at +0x6C when bit 0 of byte +0x54 is set, otherwise the one at +0x58. The chosen timer is removed, set to fire after (value at +0x50 + 6 - now) milliseconds, given the 16-bit handle at +0x0A as its context, and given handler 0x0C066B74 (ble_ctrl_conn_timer_update_state), then added to the run loop. The +0x6C timer is created in ble_ctrl_conn_alloc_and_register with the node pointer as context, so using the handle here is inconsistent for that timer.

| Parameter | Type | Description |
|---|---|---|
| `conn` | `ptr` | connection record |

**Notes:** The +6 offset and the meaning of +0x50 are unconfirmed. Context type mismatch on the +0x6C timer should be checked.

- Addresses by version: 219: 0x0C065F6C
- Called by: `ble_219_0c068da8`
- Calls: `btstack_run_loop_set_timer_handler`, `btstack_run_loop_set_timer`, `btstack_run_loop_set_timer_context`, `btstack_run_loop_add_timer`, `btstack_run_loop_remove_timer`, `btstack_run_loop_get_time_ms`
- Confidence: medium

## ble_ctrl_conn_check_flags_0x60

**Return true when a connection's flags at +0x10 have both bits 0x20 and 0x40 set**

Returns false unless the env byte at 0x18E has bit 3 set and the env byte at 0x41 is non-zero. Under those conditions it looks up the connection by handle and returns whether (node+0x10 & 0x60) == 0x60. Returns false when no connection has that handle.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `u16` | connection handle |

**Returns** `bool`: true when both flag bits are set

**Notes:** Meaning of the two flag bits and the env gating bytes is not confirmed.

- Addresses by version: 219: 0x0C06B218
- Called by: `ble_219_0c06c8f4`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: medium

## ble_ctrl_conn_clear_pending_notify

**Clear connection pending bits and emit event 0xE1/0x09 with a status byte**

Clears node+0x17 and the 0xC00 pending field of node+0x68, then emits an 11-byte event E1 09: the u16 handle at +2, the reversed peer address at +4..+9 and the status byte at +10. When the status is nonzero and bit 15 of node+0x10 is set, that bit is cleared, bit 10 (0x400) is set and the status is stored at node+0x14 for later use.

| Parameter | Type | Description |
|---|---|---|
| `conn` | `ptr` | connection record |
| `status` | `s32` | status byte reported in the event |

**Notes:** Use of node+0x14 after the deferred path is not visible in this packet.

- Addresses by version: 219: 0x0C0660C0
- Called by: `ble_219_0c0674e8`, `ble_219_0c068da8`
- Calls: `co_write16_le`, `co_reverse_copy_6`, `hci_emit_event`
- Confidence: medium

## ble_ctrl_conn_find_by_addr

**Find the connection record for a peer address and address type**

Walks the connection list at env+0x14 and returns the first record whose address-type byte at +0xC equals param_2 and whose 6-byte address at +4 matches param_1 (memcmp of 6 bytes). Returns NULL when no record matches. Used to look a peer up before its handle is known.

| Parameter | Type | Description |
|---|---|---|
| `addr` | `ptr` | 6-byte BD_ADDR |
| `addr_type` | `u8` | address type to match |

**Returns** `ptr`: matching connection record, or NULL

- Addresses by version: 219: 0x0C066588
- Called by: `ble_219_0c066f74`, `ble_219_0c068c98`, `ble_219_0c068da8`, `ble_219_0c06ee70`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`, `memcmp`
- Confidence: high

## ble_ctrl_conn_find_by_handle

**Find the connection record whose handle (u16 at +0x0A) equals the argument**

Walks the connection list at env+0x14 with the iterator and returns the first record whose u16 handle at +0x0A equals the argument. Returns NULL when no record matches. The decompiled output is typed void with a bare return, but the matching node is left in r0 by the iterator-next call, so this is treated as a pointer-returning lookup.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `u16` | connection handle |

**Returns** `ptr`: matching connection record, or NULL

**Notes:** Return value inferred from the register flow; the decompile does not show it.

- Addresses by version: 219: 0x0C066554
- Called by: `att_server_write_callback`, `ble_219_0c04e398`, `ble_219_0c04e702`, `ble_219_0c04eb8c`, `ble_219_0c04ebc0`, `ble_219_0c04ec18`, `ble_219_0c04f9b0`, `ble_219_0c04fa38`, `ble_219_0c04facc`, `ble_219_0c051eb8`, `ble_219_0c051ef0`, `sm_link_poll_state` ...
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: medium

## ble_ctrl_conn_free_and_report_disconnect

**Unlink and free a connection, emitting event 0xD9/0x07 when bit 15 is set**

Copies the peer address and handle, unlinks the record from the connection list at env+0x14 (btstack_linked_list_remove) and returns it to the pool (btstack_memory_hci_connection_free). If bit 15 of node+0x10 was set it emits a 9-byte event D9 07: the reason byte, then the peer address reversed. Finally, when the reason is 5 and the interface table at env+0x10 has an entry at +0x14, it calls that entry with the address.

| Parameter | Type | Description |
|---|---|---|
| `conn` | `ptr` | connection record |
| `reason` | `u8` | disconnect reason byte |

**Notes:** Reason 5 is treated as a special case by the code; its HCI meaning is not confirmed.

- Addresses by version: 219: 0x0C06637A
- Called by: `ble_219_0c066370`
- Calls: `btstack_linked_list_remove`, `btstack_memory_hci_connection_free`, `co_reverse_copy_6`, `hci_emit_event`
- Confidence: medium

## ble_ctrl_conn_get_flag_bit4

**Return bit 4 (0x10) of a connection's flags at +0x10, or 0 for an unknown handle**

Looks up the connection by handle and returns (node+0x10 & 0x1F) >> 4, which is 1 when bit 0x10 is set and 0 otherwise. Other flag bits are masked out. Returns 0 when no connection has that handle.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `u16` | connection handle |

**Returns** `u8`: 0 or 1

**Notes:** The meaning of bit 0x10 is not confirmed.

- Addresses by version: 219: 0x0C06B274
- Called by: `ble_219_0c06dc56`, `ble_219_0c06ee70`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: medium

## ble_ctrl_conn_get_level_by_handle

**Return the link security tier (0..4) of a connection looked up by handle**

Looks up the connection by handle and applies the same classification as ll_link_get_level (0x0C065FBC): 0 when the record is missing, when the status bits (node+0x68 & 0x3000) are not both set, or when the key size at +0x16 is below the minimum at env+0x52. Otherwise the tier comes from the state word at +0x28: 5 and 0 give 3, 8 gives 3 when the key size is below 16 and 4 otherwise, and any other state gives 2.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `u16` | connection handle |

**Returns** `u8`: tier 0 (not eligible), 2, 3 or 4

- Addresses by version: 219: 0x0C06B2FC
- Called by: `ble_219_0c06c8f4`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: high

## ble_ctrl_conn_get_state_by_handle

**Return the state byte at +0x0D of a connection looked up by handle (0xFF if unknown)**

Looks up the connection by handle and returns the byte at its +0x0D offset, which ble_ctrl_conn_alloc_and_register initialises to 0xFF. Returns 0xFF when no connection has that handle, so 0xFF means unset or unknown to callers. ble_ctrl_update_link_slot_flag compares this byte with 1.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `u16` | connection handle |

**Returns** `u8`: state byte, 0xFF when the handle is unknown

- Addresses by version: 219: 0x0C06B984
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: high

## ble_ctrl_conn_has_pending_flag

**Return 1 when the connection with a handle has a pending bit (0x400 or 0x800) set**

Looks up the connection by handle (u16 at +0x0A) and returns 1 if (node+0x68 & 0x0C00) is non-zero, otherwise 0. It also returns 0 when no connection has that handle. The 0x0C00 field is the pending state written by ble_ctrl_conn_set_pending_notify and cleared by ble_ctrl_conn_clear_pending_notify.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `u16` | connection handle |

**Returns** `u16`: 1 when a pending bit is set, otherwise 0

- Addresses by version: 219: 0x0C0665D4
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: high

## ble_ctrl_conn_idle_timeout_check

**Timer callback: after 10 s since node+0x7C emit event 0x73 with the handle**

Runs as the handler of the connection's +0x6C timer; the context is the connection pointer. If the u32 timestamp at node+0x7C plus 10000 ms is earlier than the current run-loop time, and the global byte DAT_200190CE is zero, it emits a 4-byte event 0x73 0x02 followed by the u16 handle at +2 via hci_emit_event. The timestamp is written at allocation by ble_ctrl_conn_alloc_and_register. The meaning of event 0x73 and of DAT_200190CE is not confirmed.

**Notes:** Event size is taken as 4 from the layout (code, length 2, handle); the decompile shows only one argument.

- Addresses by version: 219: 0x0C06611C
- Calls: `btstack_run_loop_get_timer_context`, `btstack_run_loop_get_time_ms`, `co_write16_le`, `hci_emit_event`
- Confidence: medium

## ble_ctrl_conn_iter_init

**Initialise a removal-safe iterator over the connection list at env+0x14**

Wrapper that calls btstack_linked_list_iterator_init on the connection list head at env+0x14, filling the caller's iterator storage (12 bytes in most callers). Callers then use btstack_linked_list_iterator_has_next and _next to walk the connections.

| Parameter | Type | Description |
|---|---|---|
| `iter` | `ptr` | iterator storage supplied by the caller |

- Addresses by version: 219: 0x0C066544
- Called by: `ble_219_0c04e398`, `ble_219_0c051eb8`, `ble_219_0c06ca80`, `ble_219_0c06cdb8`
- Calls: `btstack_linked_list_iterator_init`
- Confidence: high

## ble_ctrl_conn_key_size_check

**Apply the encryption key size check and set the connection status for event 0xD8/0x03**

Stores the negotiated key size in node+0x16 and sets flag 0x2000 in node+0x68. Until bit 0x1000 of node+0x68 is set, it only maintains the connection flags: bit 15 of node+0x10 turns into pending 0x400 with status 0x2F, otherwise bits 0x3 and 0x800 are set. Once 0x1000 is set, a key size below the minimum at env+0x52 gives status 0, and otherwise the status depends on the state word at +0x28 and the key size (0x3 or 0x4 for states 0, 5 and 8, 0x2 for other states). A non-zero status is sent as event 0xD8 0x03 with the handle, cleared node+0x17 first, unless bit 15 turns it into a pending state.

| Parameter | Type | Description |
|---|---|---|
| `conn` | `ptr` | connection record |
| `key_size` | `u8` | negotiated encryption key size in bytes |

**Notes:** Status values 0/2/3/4 and the 0x2F (insufficient security) pending path are read from the code; their protocol meaning is inferred. Minimum key size default 7 is set in ll_env_init.

- Addresses by version: 219: 0x0C066280
- Called by: `ble_219_0c068da8`
- Calls: `co_write16_le`, `hci_emit_event`
- Confidence: medium

## ble_ctrl_conn_set_pending_notify

**Set connection pending bit 0x400 or 0x800 and emit event 0xE0/0x0A**

If the 0xC00 pending field of node+0x68 is clear, it sets 0x400 (param 0) or 0x800 (param nonzero). When bit 12 of node+0x10 is clear it also sets node+0x17 to the larger of its current value and the byte at env+0x59 (co_max_u32). It then emits a 12-byte event E0 0A: the u16 handle at +2 (little-endian), the peer address reversed at +4..+9, the parameter byte at +10 and the bool from bit 12 at +11, via hci_emit_event. Nothing is emitted when a pending bit is already set.

| Parameter | Type | Description |
|---|---|---|
| `conn` | `ptr` | connection record |
| `kind` | `s32` | 0 selects pending bit 0x400, nonzero selects 0x800; also written as the event parameter byte |

**Notes:** Event 0xE0 subtype 0x0A semantics are not confirmed.

- Addresses by version: 219: 0x0C066040
- Called by: `ble_219_0c068da8`
- Calls: `co_write16_le`, `co_reverse_copy_6`, `co_max_u32`, `hci_emit_event`
- Confidence: medium

## ble_ctrl_conn_teardown_and_count

**Stop a connection's timers, unlink and free it, then emit event 0x61 with the count**

Removes both the +0x58 and +0x6C timers from the run loop, unlinks the record from env+0x14 and frees it. It then counts the connections still on the list and emits the 3-byte event 61 01 count via hci_emit_event. If the removed record's address-type byte is 0xFC and the interface table has an entry at +0x24, it calls that entry with the u16 at env+0x1D2 and the number of 0xFC-type connections still present, which is a tail call in the binary.

| Parameter | Type | Description |
|---|---|---|
| `conn` | `ptr` | connection record |

**Notes:** 0xFC is treated as an LE connection type by the code; this packet does not name it.

- Addresses by version: 219: 0x0C0663E8
- Called by: `ble_219_0c06648c`, `ble_219_0c0674e8`, `ble_219_0c068da8`
- Calls: `btstack_linked_list_remove`, `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`, `btstack_memory_hci_connection_free`, `btstack_run_loop_remove_timer`, `hci_emit_event`
- Confidence: medium

## ble_ctrl_conn_timer_update_state

**Timer callback: set the connection state byte +0x56 and flush the deferred event**

Runs as the handler of the connection's +0x58 timer, with the 16-bit handle as context. It finds the connection by handle in env+0x14 and sets node+0x56 to 1. It changes that to 2 when the u16 at env+0x1D2 AND 3 is not 3 and the byte at env+0x17D is below 0x7B (123). It then calls ble_ctrl_flush_deferred_event.

**Notes:** Meaning of the values 1 and 2 at +0x56 is not confirmed.

- Addresses by version: 219: 0x0C066B74
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`, `btstack_run_loop_get_timer_context`, `ble_ctrl_flush_deferred_event`
- Confidence: medium

## ble_ctrl_deferred_list_add

**Append an item to the global deferred list whose head is at 0x200190A4**

Thin thunk to the list append routine 0x0C065416 (btstack_linked_list_add_tail_impl). It appends its single argument to the list whose head pointer lives at the RAM global DAT_200190A4, a list separate from the controller environment at DAT_200190D0. The consumer of that list is not present in this packet, so the purpose is inferred from the placement only. The wrapper exists to keep the call site short.

| Parameter | Type | Description |
|---|---|---|
| `item` | `ptr` | list node to append (linked item with next pointer at +0) |

**Notes:** Consumer of the list at 0x200190A4 is unknown; name reflects only the placement.

- Addresses by version: 219: 0x0C065A50
- Called by: `ble_deferred_list_post`
- Calls: `btstack_linked_list_add_tail`
- Confidence: medium

## ble_ctrl_env_get_addr_type_and_addr_a

**Get own address type and 6-byte device address (variant using type flag at env+0x1DC)**

Writes the byte at env+0x1dc to *param_1 (address type: 0 selects the public address). If it is 0 the 6-byte address at env+0x38 (u32 + u16, the public BD_ADDR) is copied to param_2, otherwise the 6-byte address at env+0x1dd..0x1e2 (the alternate/random address) is copied. Used by the caller 0c051eb8, which is an advertising/scan related routine. Env is the controller environment struct pointed to by the RAM pointer DAT_200190d0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | out: address type byte (0 = public, nonzero = random/other) |
| `param_2` | `ptr` | out: 6-byte Bluetooth device address buffer |

**Notes:** Interpretation as public vs random address type is inferred from the 6-byte layout.

- Addresses by version: 219: 0x0C066D34
- Called by: `ble_219_0c051eb8`
- Confidence: medium

## ble_ctrl_env_get_addr_type_and_addr_b

**Get own address type and 6-byte device address (variant using type flag at env+0x218)**

Same as ble_ctrl_env_get_addr_type_and_addr_a except that the type byte is read from env+0x218 instead of env+0x1dc: it is stored to *param_1 and, when zero, the public address at env+0x38 (4+2 bytes) is returned in param_2, otherwise the alternate address at env+0x1dd (4+2 bytes). No direct callers (referenced through a function-pointer table). Env is the controller environment struct pointed to by the RAM pointer DAT_200190d0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | out: address type byte |
| `param_2` | `ptr` | out: 6-byte device address buffer |

**Notes:** Likely the second role/instance counterpart of the 0c066d34 getter.

- Addresses by version: 219: 0x0C066D5C
- Confidence: medium

## ble_ctrl_env_get_flag_bit6_at_0x18e

**Return bit 6 of the flag byte at env+0x18E (0 or 1)**

Reads the byte at +0x18e of the controller environment struct pointed to by the RAM pointer DAT_200190d0, masks it with 0x7f and shifts right by 6, which yields just bit 6 (0 or 1). Pure getter without side effects. Always called together with ble_ctrl_env_get_u16_at_0x56 (0c066f2c) from 0c06ca3c, 0c06caf4 and 0c06ed64.

**Returns** `u32`: 0 or 1, bit 6 of env+0x18e

**Notes:** Semantics of the bit unknown.

- Addresses by version: 219: 0x0C066D20
- Called by: `ble_219_0c06ca3c`, `ble_219_0c06caf4`, `ble_219_0c06ed64`
- Confidence: low

## ble_ctrl_env_get_mode_or_4

**Return env+0x58 unless the flag at env+0x64 is set, in which case return 4**

If the byte at env+0x64 of the controller environment struct pointed to by the RAM pointer DAT_200190d0 is zero the function returns the byte at env+0x58; otherwise it returns the constant 4. Looks like a state/mode getter with an override while a flag (see ble_ctrl_env_get_u8_at_0x64) is active. Callers: 04bb00, 04bd0c, 06ee70.

**Returns** `u8`: env+0x58 or 4

**Notes:** Semantics unknown.

- Addresses by version: 219: 0x0C066EE4
- Called by: `ble_219_0c04bb00`, `bthost_latch_ctrl_mode_2000fb90`, `ble_219_0c06ee70`
- Confidence: low

## ble_ctrl_env_get_public_addr

**Copy the 6-byte public device address from env+0x38**

Copies the u32 at env+0x38 and the u16 at env+0x3c of the controller environment struct pointed to by the RAM pointer DAT_200190d0 into the 6-byte buffer param_1. This is the controller's local Bluetooth device address (BD_ADDR). Called from 0c051eb8 and 0c05a8a0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | out: 6-byte address buffer |

- Addresses by version: 219: 0x0C066F60
- Called by: `ble_219_0c051eb8`, `ble_conn_select_link_and_fill_info`
- Confidence: medium

## ble_ctrl_env_get_u16_at_0x17a

**Return the 16-bit field at offset 0x17A of the controller environment struct**

Getter: loads the pointer DAT_200190d0 and returns the halfword at +0x17a of the controller environment struct pointed to by the RAM pointer DAT_200190d0. No side effects. Called from 0c06d698 together with another env getter (0c067168). The field's meaning is not evidenced in this packet (possibly a connection/link parameter such as an interval or handle).

**Returns** `u16`: value of env+0x17a

**Notes:** Meaning of the field unknown; name is positional.

- Addresses by version: 219: 0x0C066D10
- Called by: `ble_219_0c06d698`
- Confidence: low

## ble_ctrl_env_get_u16_at_0x56

**Return the 16-bit field at env+0x56**

Getter returning the halfword at +0x56 of the controller environment struct pointed to by the RAM pointer DAT_200190d0. Always paired with ble_ctrl_env_get_flag_bit6_at_0x18e by callers 0c06ca3c, 0c06caf4 and 0c06ed64.

**Returns** `u16`: value of env+0x56

- Addresses by version: 219: 0x0C066F2C
- Called by: `ble_219_0c06ca3c`, `ble_219_0c06caf4`, `ble_219_0c06ed64`
- Confidence: low

## ble_ctrl_env_get_u8_at_0x198

**Return the byte at env+0x198 (widely used state byte)**

Getter returning the byte at +0x198 of the controller environment struct pointed to by the RAM pointer DAT_200190d0. It has eight callers (0c051eb8, 0c05806c, 0c059a88 and the clustered 0c064ffc..0c065108 routines), so it is probably a frequently tested state/role/mode byte.

**Returns** `u8`: value of env+0x198

- Addresses by version: 219: 0x0C06BAC0
- Called by: `ble_219_0c051eb8`, `ble_219_0c05806c`, `ble_host_timer_restart`, `ble_219_0c064ffc`, `ble_219_0c065038`, `ble_219_0c065078`, `ble_219_0c0650c0`, `ble_219_0c065108`
- Confidence: low

## ble_ctrl_env_get_u8_at_0x40

**Return the byte at env+0x40**

Getter returning the byte at +0x40 of the controller environment struct pointed to by the RAM pointer DAT_200190d0, directly next to the 6-byte public address field at env+0x38. Called from 0c06cdb8.

**Returns** `u8`: value of env+0x40

- Addresses by version: 219: 0x0C066F1C
- Called by: `ble_219_0c06cdb8`
- Confidence: low

## ble_ctrl_env_get_u8_at_0x46

**Return the byte at env+0x46**

Getter returning the byte at +0x46 of the controller environment struct pointed to by the RAM pointer DAT_200190d0. Called from 0c06d698.

**Returns** `u8`: value of env+0x46

- Addresses by version: 219: 0x0C067168
- Called by: `ble_219_0c06d698`
- Confidence: low

## ble_ctrl_env_get_u8_at_0x5a

**Return the byte at env+0x5A**

Simple getter returning the byte at +0x5a of the controller environment struct pointed to by the RAM pointer DAT_200190d0. Called from 0c06c8f4.

**Returns** `u8`: value of env+0x5a

**Notes:** Field meaning unknown.

- Addresses by version: 219: 0x0C066ED4
- Called by: `ble_219_0c06c8f4`
- Confidence: low

## ble_ctrl_env_get_u8_at_0x64

**Return the byte at env+0x64 (override flag used by 0c066ee4)**

Getter returning the byte at +0x64 of the controller environment struct pointed to by the RAM pointer DAT_200190d0; the same byte selects the constant-4 path in ble_ctrl_env_get_mode_or_4. Called from 0c06dc56.

**Returns** `u8`: value of env+0x64

- Addresses by version: 219: 0x0C066F0C
- Called by: `ble_219_0c06dc56`
- Confidence: low

## ble_ctrl_env_set_callbacks_and_notify

**Store callback table pointer at env+8 and invoke its second entry with env+4**

Writes param_1 into env+8 of the controller environment struct pointed to by the RAM pointer DAT_200190d0. If param_1 is non-NULL and its entry at +4 is non-NULL, that callback is invoked with the value stored at env+4 as the only argument. Called from the registration function 0c05b67c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | callback table (entry at +4 = notify callback taking env+4) or NULL |

- Addresses by version: 219: 0x0C066EBC
- Called by: `ble_219_0c05b67c`
- Confidence: medium

## ble_ctrl_env_set_iface_and_init

**Store interface table pointer at env+0x10 and call its first entry**

Stores param_1 into env+0x10 of the controller environment struct pointed to by the RAM pointer DAT_200190d0; if non-NULL, treats it as a table of function pointers and calls entry 0 (typically an init/open callback) with no arguments. Called once from the large interface-registration function 0c05b67c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | table of function pointers (entry 0 = init callback) or NULL |

- Addresses by version: 219: 0x0C066DE8
- Called by: `ble_219_0c05b67c`
- Confidence: medium

## ble_ctrl_env_set_peer_addr

**Store a 6-byte address, type and valid flag at env+0x230..0x237**

Copies the 6-byte address at *param_1 (u32 + u16) to env+0x231..0x236 of the controller environment struct pointed to by the RAM pointer DAT_200190d0, sets the byte env+0x237 to 1 (valid flag) and stores param_2 at env+0x230 (address type). Called from 0c058250.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pointer to 6-byte device address |
| `param_2` | `u8` | address type |

**Notes:** Role of the address (peer/white-list/resolving entry) not confirmed.

- Addresses by version: 219: 0x0C066F3C
- Called by: `ble_219_0c058250`
- Confidence: medium

## ble_ctrl_env_set_u8_at_0x42

**Set the byte at env+0x42**

Setter storing param_1 into +0x42 of the controller environment struct pointed to by the RAM pointer DAT_200190d0. Called from 0c058250 along with ble_ctrl_env_set_u8_at_0x45 and ble_ctrl_env_set_peer_addr.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | new value |

- Addresses by version: 219: 0x0C067148
- Called by: `ble_219_0c058250`
- Confidence: low

## ble_ctrl_env_set_u8_at_0x45

**Set the byte at env+0x45**

Setter storing param_1 into +0x45 of the controller environment struct pointed to by the RAM pointer DAT_200190d0. Called from 0c058250.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | new value |

- Addresses by version: 219: 0x0C067158
- Called by: `ble_219_0c058250`
- Confidence: low

## ble_ctrl_env_set_u8_at_0x59

**Set the byte at env+0x59**

Setter: stores param_1 into +0x59 of the controller environment struct pointed to by the RAM pointer DAT_200190d0. Called from 0c06f078 (which also uses the indexed hook dispatcher 0c06c138).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | new value |

**Notes:** Semantics unknown.

- Addresses by version: 219: 0x0C066EFC
- Called by: `l2cap_register_service`
- Confidence: low

## ble_ctrl_flush_deferred_event

**Send the deferred 0x6F event once the controller is idle and a link slot is free**

When the deferred-event byte env+0x186 is set, the reserved-buffer byte env+0x170 is clear and ll_env_has_free_slot() succeeds, it clears env+0x186, builds the 2-byte event 0x6F 0x00 and passes it to ble_hook_invoke4 with packet type 4 and channel 1. It then calls the env callback at env+0x1C with (4, 0, buffer, 2).

**Notes:** Event 0x6F semantics are not confirmed. The env+0x1C callback is not identified.

- Addresses by version: 219: 0x0C066B20
- Called by: `ble_ctrl_conn_timer_update_state`, `ble_219_0c068da8`
- Calls: `ll_env_has_free_slot`, `ble_hook_invoke4`
- Confidence: medium

## ble_ctrl_get_data_len_or_default

**Return the configured 16-bit length DAT_2001949c, or 251 if it is 0**

Reads the halfword DAT_2001949c and returns it, substituting 0xfb (251, the maximum LE data length) when it is zero. Called from 0c04e702.

**Returns** `s16`: configured length or 251

**Notes:** Whether it is tx or rx octets is not confirmed.

- Addresses by version: 219: 0x0C06EE60
- Called by: `ble_219_0c04e702`
- Confidence: medium

## ble_ctrl_get_flag_3fe8

**Return byte global 0x20003fe8**

Trivial getter returning DAT_20003fe8. Called only from the large routine ble_219_0c053018. Purpose of the value not determinable here.

**Returns** `u8`: current value

- Addresses by version: 219: 0x0C053824
- Called by: `ble_219_0c053018`
- Confidence: low

## ble_ctrl_get_max_data_len

**Return the constant 251 (0xFB)**

Returns 0xfb = 251, the maximum LE data PDU payload length allowed by Bluetooth 4.2+ data length extension. No side effects; no direct callers (used as a callback).

**Returns** `u32`: 251

- Addresses by version: 219: 0x0C06EE5C
- Confidence: medium

## ble_ctrl_get_sanitized_setting_20004344

**Return the byte at 0x20004344, forcing it to 0x0e unless it is 0x0e or 0x10**

Reads the 8-bit global at 0x20004344. If its value is neither 0x0e nor 0x10 it is overwritten with the default 0x0e, then the (possibly corrected) value is returned. Acts as a validated getter for a two-valued configuration byte (14 or 16); the meaning (possibly a length/power/mode selector) is not evident from this function alone. Called from ble_219_0c056a50.

**Returns** `u8`: 0x0e or 0x10

**Notes:** Semantics of the 0x0e/0x10 setting not determined.

- Addresses by version: 219: 0x0C0581F0
- Called by: `ble_219_0c056a50`
- Confidence: low

## ble_ctrl_iface_iterate_dispatch

**Iterate the interface table's items and pass each one to its handler**

Uses the interface table at env+0x10 as a generic iterator. It calls table+0x18 to initialise an iterator (auStack_2c); if that succeeds it loops, calling table+0x1C to fetch the next item into two output buffers and table+0x14 with the item for each one, and stops when table+0x1C returns 0. It finishes with table+0x20 on the iterator. If initialisation fails it logs 'could not initialize iterator' at hci.c line 0x210. Which items are visited is not visible in this packet.

**Notes:** Slot meanings of the interface table are inferred from the call pattern only.

- Addresses by version: 219: 0x0C06662C
- Calls: `ble_hook_invoke_indexed`
- Confidence: medium

## ble_ctrl_iface_probe_and_start

**Call ops[1]; if it returns 0, set start flags and call ops[8](buf, 1)**

Calls the function at offset 4 of the interface table whose pointer is DAT_20019324. If that call returns 0, it clears DAT_20019448, sets the flag bytes DAT_2001932a and DAT_20019328 to 1, calls the function at offset 0x20 of the table with (&DAT_20019334, 1) and finally sets DAT_2001944a = 1. Returns the first call's result. No direct callers (used via a pointer table).

**Returns** `s32`: result of ops[1](); 0 means the start sequence was executed

**Notes:** Table identity unknown; may be an init/open style routine of a peripheral driver.

- Addresses by version: 219: 0x0C06C298
- Confidence: low

## ble_ctrl_noop_callback

**Empty function used as a no-op callback**

Consists of a single return instruction; it takes no arguments and has no side effects. It has no direct callers and is presumably stored in a function-pointer table as a placeholder.

- Addresses by version: 219: 0x0C06C1E4
- Confidence: high

## ble_ctrl_opcode_in_set

**Return 1 if opcode param_1 is in a fixed set and flag bit 15 of param_2 is clear**

If bit 15 of param_2 is clear, a switch on param_1 returns 1 for the values 2, 3, 4, 6, 8, 9, 10, 11, 14, 0x14, 0x17 and 0x18, otherwise (or when bit 15 is set) it returns 0. The value set resembles a list of control-PDU/command opcodes, but this is not confirmed. No direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | opcode or message id |
| `param_2` | `u32` | flags; bit 15 must be clear (only low 16 bits examined) |

**Returns** `u32`: 1 if the opcode is in the set, else 0

**Notes:** Opcode meaning (LL control vs LMP vs internal message) unknown.

- Addresses by version: 219: 0x0C06CA0C
- Confidence: low

## ble_ctrl_pending_drain_and_arm_timer

**Free every entry of the list at env+0x1E8 and arm the 1000 ms timer at env+0x19C**

Walks the list at env+0x1E8 with the removal-safe iterator, unlinks each entry and returns it to the global free pool with btstack_memory_free_list_push. It then stores the u16 0x3F03 at env+0x198 (state byte 3 at +0x198) and initialises the timer embedded at env+0x19C: period 1000 ms, handler 0x0C068D6C, then adds it to the run loop. The result is a reset of a pending-item queue followed by a one-second timer; the timer's purpose is not confirmed.

**Notes:** Callback 0x0C068D6C is named LAB_0c068d6c in the decompile and is not described here.

- Addresses by version: 219: 0x0C065EF8
- Called by: `ble_219_0c06b048`
- Calls: `btstack_linked_list_remove`, `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`, `btstack_memory_free_list_push`, `btstack_run_loop_set_timer_handler`, `btstack_run_loop_set_timer`, `btstack_run_loop_add_timer`
- Confidence: medium

## ble_ctrl_set_flag_3fac

**Store a byte configuration value into global 0x20003fac**

Trivial setter: DAT_20003fac = param_1. Called from ble_219_0c059230 together with the setter for 0x2000fdc5; purpose of the variable unknown.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | new value |

- Addresses by version: 219: 0x0C052B44
- Called by: `ble_219_0c059230`
- Confidence: low

## ble_ctrl_set_flag_fdc5

**Store a byte configuration value into global 0x2000fdc5**

Trivial setter: DAT_2000fdc5 = param_1. Called from the same configuration routine (ble_219_0c059230) as the setter for 0x20003fac. Meaning of the value is not evident from this function.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | new value |

- Addresses by version: 219: 0x0C052B38
- Called by: `ble_219_0c059230`
- Confidence: low

## ble_ctrl_set_key_dist_flags

**Translate two key-distribution bitmasks into controller-internal flag bytes**

Clears 0x2000ff58, 0x2000ff59 and 0x2000ff57. For param_2 (bit0 -> 0x03, bit1 -> OR 0x0c, bit2 -> OR 0x10) builds 0x2000ff58; for param_1 with the same mapping builds 0x2000ff56. The bit0/1/2 layout matches the SMP key distribution field (EncKey, IdKey, Sign), expanded into 2-bit groups plus a 1-bit group. param_1 is likely the initiator and param_2 the responder distribution.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | key distribution bitmask (bit0 enc, bit1 id, bit2 sign) -> stored at 0x2000ff56 |
| `param_2` | `u32` | key distribution bitmask -> stored at 0x2000ff58 |

**Notes:** Initiator/responder assignment is a guess.

- Addresses by version: 219: 0x0C04F848
- Called by: `ble_219_0c051eb8`
- Confidence: low

## ble_ctrl_store_keys_and_addrs

**Copy three 16-byte keys and three short address/info blobs into controller globals**

Copies param_1, param_2 and param_3 (16 bytes each) to 0x2000fe00, 0x2000fe10 and 0x2000fe20. Then copies a 3-byte item (u16 + u8) from param_4 to 0x2000fe30, and two 7-byte items (u32 + u16 + u8, written with unaligned stores) from param_5 and param_6 to 0x2000fe33 and 0x2000fe3a. The 7-byte items look like address-type + 6-byte BD_ADDR records and the 16-byte items like IRK/LTK/CSRK style keys, but this is inferred from sizes only.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 16-byte key #1 source |
| `param_2` | `ptr` | 16-byte key #2 source |
| `param_3` | `ptr` | 16-byte key #3 source |
| `param_4` | `ptr` | 3-byte source |
| `param_5` | `ptr` | 7-byte source (probably address) |
| `param_6` | `ptr` | 7-byte source (probably address) |

**Notes:** Semantic naming speculative; layout of copies is certain.

- Addresses by version: 219: 0x0C04F0C8
- Called by: `ble_219_0c051eb8`
- Confidence: low

## ble_ctrl_update_link_slot_flag

**Recompute the link-slot-available flag at env+0x220 from the connection list**

When bit 2 of the env byte at 0x21F is clear, it clears the bool at env+0x220 and returns. Otherwise it walks the connection list at env+0x14 and counts nodes whose state byte +0xE is 4, whose byte +0xD is 1 and whose address-type/class byte +0xC is below 4. The bool at env+0x220 is set to (count < the limit byte at env+0x221). The bit-2 gate is set elsewhere and its owner is not described in this packet.

**Notes:** Meaning of bytes +0xC/+0xD/+0xE is inferred from the comparisons only.

- Addresses by version: 219: 0x0C065E20
- Called by: `ble_219_0c068da8`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: medium

## ble_ctx_get_base_20014580

**Return the address of the context structure at 0x20014580**

Returns the constant pointer &DAT_20014580 (RAM structure beginning at 0x20014580; the neighbouring globals 0x20014600..0x20014620 are callback slots). Called from ble_219_0c056a50, ble_219_0c056dd0 and ble_219_0c0585a4.

**Returns** `ptr`: pointer to 0x20014580

- Addresses by version: 219: 0x0C059F5C
- Called by: `ble_219_0c056a50`, `ble_219_0c056dd0`, `ble_link_param_monitor_step`
- Confidence: low

## ble_deferred_list_post

**Post one item to the deferred list under the mutex and signal the worker event**

Waits forever (timeout 0xFFFFFFFF) for the mutex at 0x20017180, appends the item with ble_ctrl_deferred_list_add, releases the mutex, and signals the worker event at 0x20017184 through the RTOS wrapper 0x0C04291C.

| Parameter | Type | Description |
|---|---|---|
| `item` | `ptr` | list node to append |

**Notes:** The consumer of the deferred list is not in this packet. Wrapper 0x0C0430A8 (wait) and 0x0C042C8C (release) are inferred from use.

- Addresses by version: 219: 0x0C05D08C
- Calls: `xEventGroupSetBits`, `xQueueGenericSend`, `xQueueSemaphoreTake`, `ble_ctrl_deferred_list_add`
- Confidence: medium

## ble_event_count_reached_check

**Check whether enough events have been counted and report which kind via *param_1**

Gated by bits 0 and 3 of the flags byte at 0x200042fc (returns 0 if both clear) and by a non-zero byte at 0x20004300. If flag bit 3 is set and threshold 0x2000432f is non-zero and <= counter 0x20004330, it sets *param_1=0 and returns 1. Otherwise it calls the callback in 0x20014608 with a small stack buffer, then (only if flag bit 0 is set) requires byte 3 of that buffer to equal 4 and threshold 0x20004316 non-zero and <= counter 0x20004317, in which case *param_1=1 and it returns 1. In every other case it returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | out: byte set to 0 or 1 identifying which condition was met |

**Returns** `u32`: 1 if a threshold has been reached, else 0

**Notes:** Purpose of the two threshold/counter pairs (possibly link-quality or sniff/sleep event counting) is a guess.

- Addresses by version: 219: 0x0C05A11C
- Called by: `ble_219_0c028c94`, `ble_219_0c02a8a0`, `ble_219_0c02b480`, `ble_219_0c05a224`
- Confidence: low

## ble_event_counters_clear

**Zero the four counter/flag bytes at 0x20004317, 0x2000431d, 0x20004318, 0x2000431c**

Clears the four 8-bit globals DAT_20004317, DAT_2000431d, DAT_20004318 and DAT_2000431c. 0x20004317 is the running counter compared against threshold 0x20004316 in ble_event_count_reached_check; the others appear to be sibling counters/flags. No direct callers (entry point or invoked via pointer).

- Addresses by version: 219: 0x0C059F28
- Confidence: medium

## ble_event_thresholds_refresh_from_link

**Recompute both event-count thresholds (0x2000432f, 0x20004316) from the link table entry**

Looks up the link entry with ble_link_table_find_by_key (r0 is passed through unchanged from the caller, 0c029960, so the key is the caller's first argument). If an entry exists it computes scale = (3 - entry[3]) * 8 (entry[3] is a 0..3 index, giving 24/16/8/0) and stores two u8 thresholds: DAT_2000432f = entry[1] + scale and DAT_20004316 = entry[2] + scale. These are the thresholds that ble_event_count_reached_check compares against the running counters 0x20004330 and 0x20004317 (flag bit 3 and flag bit 0 paths). Both globals live inside the shared state object at 0x200042f8 (+0x37 and +0x1e). Part of the link/event-counting group with ble_conn_select_link_and_fill_info and ble_app_arm_4s_deadline.

**Notes:** Decompiler shows no parameter; the key byte is whatever the caller left in r0. What entry[1..3] physically represent (e.g. per-link counts and a rate index) is not known.

- Addresses by version: 219: 0x0C05A1AC
- Called by: `ble_219_0c029960`
- Calls: `ble_link_table_find_by_key`
- Confidence: medium

## ble_flag_20017114_get

**Return the byte at 0x20017114**

Trivial getter returning the 8-bit global DAT_20017114 written by ble_flag_20017114_set. Called from ble_219_0c02a8f8.

**Returns** `u8`: stored value

- Addresses by version: 219: 0x0C05CF10
- Called by: `ble_219_0c02a8f8`
- Confidence: medium

## ble_flag_20017114_set

**Store the byte at 0x20017114**

Trivial setter writing param_1 to the 8-bit global DAT_20017114. Its getter is ble_flag_20017114_get; the setter is called from ble_219_0c055b90 and the getter from ble_219_0c02a8f8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | value to store |

- Addresses by version: 219: 0x0C05CF04
- Called by: `ble_219_0c055b90`
- Confidence: medium

## ble_flags_bit15_get

**Return bit 15 of the flag word at 0x200042fc**

Returns (DAT_200042fc & 0xffff) >> 15, i.e. 0 or 1 for flag bit 15 of the shared state object's flag word (set/cleared by ble_flags_set/ble_flags_clear). One of the status getters called from 0c02a8f8.

**Returns** `u32`: 0 or 1

- Addresses by version: 219: 0x0C05CFD0
- Called by: `ble_219_0c02a8f8`
- Calls: `ble_get_state_ptr_42f8`
- Confidence: high

## ble_flags_bit4_get

**Return bit 4 of the flag word at 0x200042fc**

Returns (DAT_200042fc & 0x1f) >> 4, i.e. 0 or 1 for flag bit 4 of the state object's flag word. Companion of ble_flags_bit15_get; called from the status reporter 0c02a8f8.

**Returns** `u32`: 0 or 1

- Addresses by version: 219: 0x0C05CFF4
- Called by: `ble_219_0c02a8f8`
- Calls: `ble_get_state_ptr_42f8`
- Confidence: high

## ble_flags_clear

**Clear mask bits in the flag word at 0x200042fc**

DAT_200042fc &= ~param_1. Counterpart of ble_flags_set; 8 callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | bits to clear |

- Addresses by version: 219: 0x0C058150
- Called by: `ble_219_0c0567d8`, `ble_219_0c0593a4`, `ble_219_0c05952c`, `ble_219_0c059ac0`, `ble_219_0c05a608`, `ble_219_0c05c3e8`, `ble_219_0c05c548`, `ble_219_0c05cfe0`
- Confidence: medium

## ble_flags_set

**OR a mask into the flag word at 0x200042fc**

DAT_200042fc |= param_1. Not interrupt-protected. Called from ble_219_0c05c320, 0c05c3e8, 0c05c480 and 0c05cfe0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | bits to set |

- Addresses by version: 219: 0x0C058140
- Called by: `ble_219_0c05c320`, `ble_219_0c05c3e8`, `ble_219_0c05c480`, `ble_219_0c05cfe0`
- Confidence: medium

## ble_gen_static_random_addr

**Generate a 6-byte static random device address into the output buffer**

Fills 6 bytes through 0x0C058160 (a random or stored-value source not described in this packet), sets the top two bits (OR 0xC0) of the most significant byte, which is the static random address marker, and reverses the bytes. The result is most-significant byte first in the output buffer.

| Parameter | Type | Description |
|---|---|---|
| `out` | `ptr` | 6-byte output buffer for the address |

**Notes:** The byte order of the address as stored elsewhere and the source of the random bytes are unconfirmed.

- Addresses by version: 219: 0x0C05C2C0
- Called by: `ble_219_0c052ec0`
- Calls: `ble_random_bytes_6`
- Confidence: medium

## ble_get_byte_12b84

**Return byte global 0x20012b84**

Trivial getter for DAT_20012b84, called from ble_219_0c052fb0.

**Returns** `u8`: current value

- Addresses by version: 219: 0x0C055518
- Called by: `ble_219_0c052fb0`
- Confidence: low

## ble_get_byte_12b85

**Return byte global 0x20012b85**

Trivial getter for DAT_20012b85 (the byte after 0x20012b84), called from ble_219_0c053018.

**Returns** `u8`: current value

- Addresses by version: 219: 0x0C055558
- Called by: `ble_219_0c053018`
- Confidence: low

## ble_get_byte_12eb4

**Return byte global 0x20012eb4**

Trivial getter for DAT_20012eb4, called from ble_219_0c02c1e8.

**Returns** `u8`: current value

- Addresses by version: 219: 0x0C0567BC
- Called by: `ble_219_0c02c1e8`
- Confidence: low

## ble_get_flag_12606

**Return byte flag 0x20012606**

Returns DAT_20012606, the flag set by ble_set_flag_12606.

**Returns** `u8`: flag value

- Addresses by version: 219: 0x0C054728
- Called by: `ble_219_0c055b90`, `ble_status_bits_get`
- Confidence: low

## ble_get_packed_word_12cb0

**Return 32-bit global 0x20012cb0**

Getter for DAT_20012cb0, the packed word built by ble_pack_version_nibbles. Called from ble_219_0c02b158, ble_219_0c053954 and ble_219_0c05ada4.

**Returns** `u32`: packed value

- Addresses by version: 219: 0x0C055604
- Called by: `ble_219_0c02b158`, `ble_219_0c053954`, `ble_gatt_read_char_value`
- Confidence: low

## ble_get_state_ptr_11e10

**Return address of the object at 0x20011e10**

Returns constant &DAT_20011e10; callers access fields through it. Nothing else is done.

**Returns** `ptr`: pointer to 0x20011e10

- Addresses by version: 219: 0x0C053884
- Called by: `ble_219_0c02b264`, `ble_cfg_block_load`
- Confidence: low

## ble_get_state_ptr_42f8

**Return address of the object at 0x200042f8**

Returns constant &DAT_200042f8. Very widely used (12+ callers) as the accessor of a shared controller state structure; the u32 at +4 (0x200042fc) is a flag word manipulated by ble_flags_set/ble_flags_clear.

**Returns** `ptr`: pointer to 0x200042f8

- Addresses by version: 219: 0x0C0571CC
- Called by: `ble_219_0c028b50`, `ble_219_0c029df8`, `ble_219_0c02be44`, `ble_219_0c02bf20`, `ble_219_0c0558ec`, `ble_219_0c0569a0`, `ble_link_param_monitor_step`, `ble_219_0c058980`, `ble_219_0c058a0c`, `ble_219_0c058a64`, `ble_219_0c058a94`, `ble_219_0c058b48` ...
- Confidence: medium

## ble_get_value_407a

**Output byte global 0x2000407a when index is 0**

If param_1 == 0, writes DAT_2000407a to *param_2; otherwise does nothing (so non-zero indices leave the output untouched).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | index, only 0 supported |
| `param_2` | `ptr` | out byte |

- Addresses by version: 219: 0x0C054524
- Called by: `ble_219_0c055b90`, `ble_state_407a_read`, `ble_state_407a_copy`
- Confidence: low

## ble_get_word_13074

**Return 32-bit global 0x20013074**

Trivial getter for DAT_20013074, called from ble_219_0c059948.

**Returns** `u32`: current value

- Addresses by version: 219: 0x0C058134
- Called by: `ble_219_0c059948`
- Confidence: low

## ble_get_word_41cc

**Return 32-bit global 0x200041cc**

Trivial getter for DAT_200041cc, called from ble_219_0c0534e0.

**Returns** `u32`: current value

- Addresses by version: 219: 0x0C055564
- Called by: `ble_slot_expiry_scan`
- Confidence: low

## ble_hook_invoke4

**Call the registered 4-argument hook, optionally ticking a periodic callback first**

Does nothing unless the hook table pointer DAT_20019314 is non-NULL, table[1] is non-NULL and the enable byte DAT_20019320 is set. If the period DAT_20019318 is positive, the counter DAT_2001931c is compared with it: when counter >= period and table[0] is non-NULL the counter is cleared and table[0]() is called; afterwards the counter is incremented. It then tail-calls table[1](param_1..param_4). Used from a dozen or more call sites across the controller, so it behaves like a trace/log or event-notify entry point.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | hook argument 1 |
| `param_2` | `u32` | hook argument 2 |
| `param_3` | `u32` | hook argument 3 |
| `param_4` | `u32` | hook argument 4 |

**Notes:** Purpose (logging vs profiling) is a guess.

- Addresses by version: 219: 0x0C06C0C0
- Called by: `ble_evt_publish`, `ble_219_0c052de8`, `ble_ctrl_flush_deferred_event`, `ble_219_0c066f74`, `ble_219_0c0674e8`, `ble_219_0c068da8`, `ll_link_notify_event_72`, `ble_listener_broadcast_event`, `l2cap_channel_emit_event_70`, `ll_link_emit_event_code_handle`, `ll_link_emit_event_7d`, `ll_link_emit_event_79` ...
- Confidence: medium

## ble_hook_invoke_indexed

**Call hook table entry 2 for channel idx (<3) if that channel is enabled**

Requires DAT_20019314 non-NULL, param_1 < 3, the per-index enable byte at DAT_20004998[param_1] non-zero and table[2] (offset 8) non-NULL; then calls table[2](param_1, param_2). Otherwise returns silently. Has a very large number of callers (04ace4, 04af00, 04bc2c, 04cdf0 ...), so likely a per-category trace/event notification.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | channel/category index, must be < 3 |
| `param_2` | `u32` | argument passed through to the hook |

**Notes:** Purpose of the 3 channels unknown.

- Addresses by version: 219: 0x0C06C138
- Called by: `bthost_link_key_db_tlv_put_link_key`, `hid_report_id_status`, `hid_report_size_valid_body`, `ble_219_0c04bc2c`, `att_set_db`, `att_server_write_callback`, `ble_219_0c04e398`, `ble_219_0c04ec18`, `le_device_db_tlv_check_init`, `le_device_db_tlv_add`, `le_device_db_tlv_set_encryption`, `ble_219_0c052de8` ...
- Confidence: medium

## ble_hook_noop_05a9c0

**Empty hook, returns immediately**

Single-instruction function (bx lr) with no side effects. It is called from about ten places across the controller code, so it is most likely a stubbed-out debug/trace or optional-feature hook.

- Addresses by version: 219: 0x0C05A9C0
- Called by: `ble_219_0c05569c`, `ble_219_0c057178`, `ble_219_0c0572c0`, `ble_219_0c0573c4`, `ble_219_0c05741c`, `ble_219_0c0593a4`, `ble_link_table_prune_by_ctrl`, `ble_219_0c05a53c`, `ble_219_0c05a608`, `ble_219_0c05a804`
- Confidence: medium

## ble_hook_noop_05cba8

**Empty hook, returns immediately**

Single-instruction function (bx lr) with no effect. Its only caller is ble_219_0c053d04; likely a stubbed optional callback or debug hook.

- Addresses by version: 219: 0x0C05CBA8
- Called by: `ble_219_0c053d04`
- Confidence: medium

## ble_hook_noop_05cbc0

**Empty hook, returns immediately**

Single-instruction function (bx lr) with no effect. Its only caller is ble_219_0c0537b4; likely a stubbed optional callback or debug hook.

- Addresses by version: 219: 0x0C05CBC0
- Called by: `ble_219_0c0537b4`
- Confidence: medium

## ble_hook_noop_05cec4

**Empty hook, returns immediately**

Single-instruction function (bx lr) with no effect. Its only caller is ble_219_0c02a8f8; likely a stubbed optional callback or debug hook.

- Addresses by version: 219: 0x0C05CEC4
- Called by: `ble_219_0c02a8f8`
- Confidence: medium

## ble_hook_table_register

**Install the hook table and reset the hook period counter**

Initialises the global hook state: DAT_2001931c (call counter) = 0, DAT_20019318 (period) = -1 (periodic callback disabled), DAT_20019314 (hook table pointer) = param_1 and DAT_20019320 (enable flag) = 1. Called once from 0c0592a4. The table holds three function pointers used by ble_hook_invoke4 and ble_hook_invoke_indexed.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | hook table: [0] periodic callback, [1] main hook(a,b,c,d), [2] indexed hook(idx,arg) |

**Notes:** Table layout inferred from its two consumers; likely a debug/trace or profiling hook.

- Addresses by version: 219: 0x0C06C090
- Called by: `ble_219_0c0592a4`
- Confidence: medium

## ble_iface_exchange_tables

**Save the peer interface table pointer and return the local interface table**

Stores param_1 into DAT_20019324 (the table used by ble_ctrl_iface_probe_and_start) and returns the address of the constant ops table at 0x0c0816d4. Called from the registration function 0c05b67c, which is a series of such get/exchange calls, so this is one module's interface hand-shake.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | interface table provided by the other module |

**Returns** `ptr`: pointer to this module's constant interface table (0x0c0816d4)

- Addresses by version: 219: 0x0C06C44C
- Called by: `ble_219_0c05b67c`
- Confidence: medium

## ble_link_get_byte_200134a4

**Return the byte at 0x200134a4**

Trivial getter returning the 8-bit global DAT_200134a4, located just before the 0x200134bc link/connection table. Its purpose is not clear from the code; sole caller is ble_219_0c0598b8.

**Returns** `u8`: value of DAT_200134a4

- Addresses by version: 219: 0x0C0591E4
- Called by: `ble_219_0c0598b8`
- Confidence: low

## ble_link_param_monitor_step

**Run one link-parameter monitor step and emit a 27-byte status record to the host**

Evaluates one parameter sample for a link and reports the outcome. param_1 bits 0-5 select the event: 1 stores the 16-bit value in param_2 as the pending pair at 0x200130F1 and sets mode 8, 2 sets mode 9, other codes keep the mode; bit 6 is copied into the link context byte at +0x28. The working record at 0x200130E0 (27 bytes) is filled from the state object at 0x200042F8 (key byte +0, flags word +4, limit bytes +0x1E and +0x37, byte +8), from the link record returned by ble_link_table_find_by_key (its byte +5 = 1 means active), and from the optional hook at 0x20014608. The sample is classified into a state byte at 0x200130F3: 1 = neither flag bit 0 nor bit 3 set, 2 = signed value outside the limits selected by those flags, 3 = accumulator above 4000, 4 = link record byte zero, 6 = mode 8 with value below 500, 8 = context bit 6 set. Two signed fields are compared against the limits and stored as deltas, the 16-bit fields are byte-swapped with bt_bytes_reverse_inplace, and ble_pending_param_store latches the state. Fields are converted from offset binary by subtracting 0x80. For states 1 and 2 the host callback at 0x200130DC receives the record with length 0x1B and event 0x94; state 2 also appends the record to a 10-slot ring at 0x20013120 and calls 0x0C0582B0(1). Other states send event 0x14. Finally the working record is reset with the default 5000 (0x1388) in 0x200130F1. clock_gettime(CLOCK_MONOTONIC) is called but its result does not feed the visible logic.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | event code: low 6 bits select the sample type (1, 2 or other), bit 6 is a context flag |
| `param_2` | `u16` | 16-bit parameter, stored as the pending pair when param_1 & 0x3F == 1 |

**Notes:** The decompiled code aliases 0x200130F0..F3 (the state byte at F3 is the top byte of the 4-byte accumulator at F0), and the stack byte local_3a is only set through the hook, so state meanings are inferred from the stores and may be off. The sub-call 0x0C0582B0(1) is not described in this packet. Limit semantics for states 2 and 3 are medium confidence.

- Addresses by version: 219: 0x0C0585A4
- Called by: `ble_219_0c02c090`
- Calls: `clock_gettime`, `ble_get_state_ptr_42f8`, `ble_event_window_expire`, `ble_link_table_find_by_key`, `ble_ctx_get_base_20014580`, `ble_pending_param_store`, `bt_bytes_reverse_inplace`
- Confidence: medium

## ble_link_table_alloc_slot

**Find the link record for a key, or the first free slot among slots 0 to 3**

Looks up key param_1 among the active link records (count at 0x200134EC, key at +0 of each 20-byte record). When found, it sets *param_2 = 1 and returns the record index. Otherwise it returns the first of slots 0 to 3 whose key is 0xFF, with *param_2 = 0, or 0 when no slot is free. If the count is above 4 the table is treated as corrupt: it is reset, saved, *param_2 is set to 0 and 0 is returned. Only four slots are allocatable; the fifth record is used as a shift buffer by the removal functions.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | key to find; 0xFF skips the search and goes straight to the free-slot scan |
| `param_2` | `ptr` | out flag: 1 when an existing record matched, 0 when a slot was chosen |

**Returns** `u8`: record index 0 to 3, or 0 when no slot is free

**Notes:** Two further undefined arguments in the decompiled signature are unused in the body.

- Addresses by version: 219: 0x0C05976C
- Called by: `ble_219_0c05741c`
- Calls: `ble_nv_record_write`
- Confidence: medium

## ble_link_table_find_by_addr

**Find the link table entry whose 6-byte address at +12 equals param_1**

Reads the entry count byte at 0x200134EC and returns NULL if it is zero. Otherwise it compares the 6 bytes at param_1 (memcmp) with the 6 bytes at +12 of each 20-byte entry, starting at 0x200134ED with stride 20, and returns the base of the first matching entry or NULL. It scans the same table as ble_link_table_find_by_key, which matches the byte at +0 instead.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 6-byte address to find |

**Returns** `ptr`: base of the matching 20-byte entry, or NULL

**Notes:** The address offset +12 comes from the scan start 0x200134F9 = entry base + 12; the entry stride is inferred from the pointer arithmetic.

- Addresses by version: 219: 0x0C059830
- Called by: `ble_219_0c0573c4`, `ble_219_0c05741c`, `ble_219_0c05a224`, `ble_219_0c05a53c`
- Calls: `memcmp`
- Confidence: medium

## ble_link_table_find_by_key

**Find the table entry whose key byte matches and return its pointer**

Looks up param_1 in the table at 0x200134bc: the count is the byte at 0x200134ec; if zero returns NULL. Otherwise it scans entries (stride 0x14 bytes starting at 0x200134ed) comparing the first byte of each entry (offset 0x31 from the table base) with param_1 and returns &entry (0x200134ed + 20*i) on a match, or NULL when none matches. Heavily used (callers in many modules).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | key byte to search for (e.g. link/connection id) |

**Returns** `ptr`: pointer to the matching 20-byte entry, or NULL

**Notes:** Key is likely a link/connection handle or index.

- Addresses by version: 219: 0x0C0597F0
- Called by: `ble_219_0c029960`, `ble_219_0c02b480`, `ble_219_0c0572c0`, `ble_219_0c057d9c`, `ble_link_param_monitor_step`, `ble_219_0c058a0c`, `ble_219_0c058b48`, `ble_219_0c058c40`, `ble_219_0c058c90`, `ble_219_0c0593a4`, `ble_219_0c05952c`, `ble_219_0c059ac0` ...
- Confidence: medium

## ble_link_table_find_index_by_key

**Return the index of the table entry with the given key, or 0xff**

Same linear scan as ble_link_table_find_by_key (count at 0x200134ec, 20-byte entries from 0x200134ed, key = first byte) but returns the zero-based index (masked to 8 bits) of the first matching entry, or 0xff if the table is empty or no entry matches. Only caller is ble_219_0c057d9c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | key byte to search for |

**Returns** `u8`: entry index, or 0xff if not found

- Addresses by version: 219: 0x0C059884
- Called by: `ble_219_0c057d9c`
- Confidence: medium

## ble_link_table_get_base

**Return the address of the link/connection table base at 0x200134bc**

Returns the constant pointer &DAT_200134bc. The structure at this address has a 0x30-byte header; the entry count byte lives at 0x200134ec and the 20-byte entries start at 0x200134ed (first byte of each entry is a lookup key, see ble_link_table_find_by_key). Called from ten functions including ble_219_0c056a50, ble_219_0c0572c0 and ble_219_0c05a91c.

**Returns** `ptr`: pointer to the table base

**Notes:** Interpretation as a connection/link table is inferred from the access pattern.

- Addresses by version: 219: 0x0C059558
- Called by: `ble_219_0c02bdd0`, `ble_219_0c056a50`, `ble_219_0c056dd0`, `ble_219_0c0572c0`, `ble_219_0c05741c`, `ble_219_0c057d9c`, `ble_link_table_write_at18`, `ble_link_table_write_at0`, `ble_link_table_prune_by_ctrl`, `ble_219_0c05a91c`
- Confidence: medium

## ble_link_table_nv_load_trim

**Reload the link table from NV, free unused slots and save if changed**

Reads the 153-byte link table block from NV record 0xFB3 with ble_nv_record_read and returns 0x41 if the read fails. If fewer than four records are in use (count < 4), every slot from index count to 3 whose key byte is not 0xFF is set to 0xFF. The table is written back with ble_nv_record_write when anything changed. Returns 0 otherwise.

**Returns** `u32`: 0 on success, 0x41 when the NV read fails

- Addresses by version: 219: 0x0C0596C8
- Called by: `ble_219_0c02973c`, `ble_219_0c0297b0`
- Calls: `ble_nv_record_write`, `ble_nv_record_read`
- Confidence: medium

## ble_link_table_prune_by_ctrl

**Reconcile the link table with the controller address list through LL hooks**

Clears a 112-byte controller context at 0x20014580, then enumerates a list of device addresses through the LL hook entries at table offsets 0x18, 0x1C and 0x20. If the start hook fails, the link table is reset. For each enumerated address, the 6 bytes are reversed with co_reverse_copy_n and compared with the address stored in each link record (at record +0x0C), scanning from the last used record down to index 0. A match calls the no-op hook ble_hook_noop_05a9c0 and removes that record with ble_link_table_remove_index. When the count is 0 or above 4 the table is reset with ble_link_table_reset.

**Notes:** The meaning of the three hook offsets as start, next and end is inferred from their use in the loop. Matching records are removed, which implies the enumerated list is a block list or a list of entries to drop, but this is not confirmed.

- Addresses by version: 219: 0x0C05A4A8
- Called by: `ble_219_0c059230`
- Calls: `ble_link_table_get_base`, `ble_link_table_remove_index`, `ble_link_table_reset`, `ble_hook_noop_05a9c0`, `co_reverse_copy_n`, `ll_hook_call_0x18`, `ll_hook_call_0x1c`, `ll_hook_call_0x20`, `memcmp`, `memset`
- Confidence: medium

## ble_link_table_remove_index

**Remove the link-table record at an index and persist the table**

Removes record param_1 (0 to 3) from the link table: 5 records of 20 bytes starting at 0x200134ED, with the record count byte at 0x200134EC and key byte +0 equal to 0xFF when free. If the index is the last used slot, the record is zeroed and its key set to 0xFF. Otherwise the following records are moved down with memmove and the vacated last slot gets key 0xFF. The table is then written to NV record 0xFB3 with ble_nv_record_write (153 bytes from 0x200134BC). Indexes above 3 are ignored and nothing happens when the count is zero.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | record index to remove, 0 to 3 |

- Addresses by version: 219: 0x0C059560
- Called by: `ble_link_table_prune_by_ctrl`
- Calls: `ble_nv_record_write`, `memmove`
- Confidence: high

## ble_link_table_remove_key

**Remove link-table records that carry a given key and persist the table**

Scans the link table for records whose key byte at +0 equals param_1 and removes them: each match is compacted out with memmove and its vacated slot is marked 0xFF. The count byte at 0x200134EC is decremented once for the first match, then the scan continues until its index passes the count. The table is saved once with ble_nv_record_write (record 0xFB3, 153 bytes) at the end. Nothing is written if no record matches.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | key byte to match (record +0) |

**Notes:** The count is decremented only once even when more than one record is removed, so behaviour with duplicate keys is not certain.

- Addresses by version: 219: 0x0C0595EC
- Called by: `ble_219_0c05a53c`, `ble_219_0c05a804`
- Calls: `ble_nv_record_write`, `memmove`
- Confidence: medium

## ble_link_table_reset

**Clear the link table to empty and save it to NV**

Sets the count byte at 0x200134EC to 0, clears all five 20-byte records starting at 0x200134ED (so every key byte becomes 0x00, not 0xFF), and writes the 153-byte table to NV record 0xFB3 through ble_nv_record_write. It is the recovery path when the table cannot be trusted, for example when the controller enumeration fails or the count is out of range.

**Notes:** Cleared slots have key 0x00, while the free marker used by ble_link_table_alloc_slot is 0xFF. Free-slot allocation only inspects slots 0 to 3, so a cleared key 0 is harmless only while the count is 0.

- Addresses by version: 219: 0x0C059724
- Called by: `ble_link_table_prune_by_ctrl`
- Calls: `ble_nv_record_write`
- Confidence: high

## ble_link_table_save

**Save the link table to NV record 0xFB3 and return 1**

Writes the 153-byte link table block at 0x200134BC to NV record 0xFB3 with ble_nv_record_write and ignores the byte count it returns. The function always returns the constant 1. Ten callers in the connection and bond code call it after changing the table.

**Returns** `u32`: always 1

**Notes:** The return value appears to be a success flag that is not derived from the write.

- Addresses by version: 219: 0x0C059754
- Called by: `ble_219_0c029960`, `ble_219_0c05741c`, `ble_link_table_write_at18`, `ble_link_table_write_at0`, `ble_219_0c0593a4`, `ble_219_0c05952c`, `ble_219_0c059ac0`, `ble_219_0c059d0c`, `ble_219_0c05a224`, `ble_219_0c05a608`
- Calls: `ble_nv_record_write`
- Confidence: high

## ble_link_table_write_at0

**Copy up to 24 bytes to the start of the current link entry and commit**

Same as ble_link_table_write_at18 (0x0c058208) except that the copy destination is the start of the entry returned by ble_link_table_get_base, not offset 0x18. It also calls ble_219_0c059754 to commit, and returns 0x41 for a length of 0x19 or more.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source bytes |
| `param_2` | `u32` | length in bytes (must be below 0x19) |

**Returns** `u32`: 0 on success, 0x41 when the length is out of range

- Addresses by version: 219: 0x0C05822C
- Called by: `ble_219_0c0292f0`
- Calls: `ble_link_table_get_base`, `ble_link_table_save`, `memcpy`
- Confidence: medium

## ble_link_table_write_at18

**Copy up to 24 bytes into the current link entry at offset 0x18 and commit**

Gets the current link table entry from ble_link_table_get_base (0x0c059558, table base 0x200134BC), copies param_2 bytes from param_1 to entry+0x18 with memcpy, and calls ble_219_0c059754 (not described in this packet) to commit the change. Returns 0x41 without copying when the length is 0x19 or more, so the field holds at most 24 bytes.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source bytes |
| `param_2` | `u32` | length in bytes (must be below 0x19) |

**Returns** `u32`: 0 on success, 0x41 when the length is out of range

- Addresses by version: 219: 0x0C058208
- Called by: `ble_219_0c0292f0`
- Calls: `ble_link_table_get_base`, `ble_link_table_save`, `memcpy`
- Confidence: medium

## ble_listener_broadcast_event

**Send an event buffer to the hook and to every listener in the list at 0x20019450**

Calls ble_hook_invoke4(4, 1, param_1, param_2) so the global hook sees the event, then walks the listener list at 0x20019450 and calls each item's callback at +4 with (4, 0, param_1, param_2). The second argument differs between the two paths (1 for the hook, 0 for listeners), which looks like a broadcast marker. Used to fan out the vendor event 0x78 built by ll_link_emit_event_78. Group: vendor H4 event emitters.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | event buffer |
| `param_2` | `u32` | event length in bytes |

**Notes:** Listener items are BTstack-style list records with the callback at +0x04. Callers 0c06c504, 0c06dc56.

- Addresses by version: 219: 0x0C06C4C0
- Called by: `ll_link_emit_event_78`, `ble_219_0c06dc56`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`, `ble_hook_invoke4`
- Confidence: medium

## ble_mode_nv_decode_read

**Read the NV mode byte and decode it to a 0-3 mode value**

Reads the mode byte from NV record 0xFA9 with ble_nv_record_read and decodes it: 0xEB gives 0, 1 gives 1, 3 gives 3, and any other byte gives 2. A failed read leaves 0xFF, which also decodes to 2. This is the inverse of ble_mode_nv_encode_write for the values 0, 1 and 3.

**Returns** `u8`: decoded mode, 0 to 3

- Addresses by version: 219: 0x0C05CD10
- Called by: `ble_219_0c02a8f8`
- Calls: `ble_nv_record_read`
- Confidence: medium

## ble_mode_nv_disable

**Set the NV mode byte to its off value, or to 0xFD for other values**

Reads the NV mode byte (record 0xFA9). If it is 0xEB or 1 it is written back as 0xEB, otherwise it is written as 0xFD. This is the off transition paired with ble_mode_nv_enable.

**Notes:** Reading 0xEB as off and 0xFD as a non-off error state is inferred from the encoding in ble_mode_nv_encode_write.

- Addresses by version: 219: 0x0C05CD84
- Called by: `ble_219_0c055b90`, `ble_219_0c05cf1c`
- Calls: `ble_nv_record_write`, `ble_nv_record_read`
- Confidence: medium

## ble_mode_nv_enable

**Set the NV mode byte to 1, or to 3 when it was another value**

Reads the NV mode byte (record 0xFA9). If it is 0xEB or 1, it is written as 1, otherwise as 3. Together with ble_mode_nv_disable it toggles between the 0xEB/1 and 3/0xFD families.

**Notes:** The meaning of mode 1 versus mode 3 is not established in this packet.

- Addresses by version: 219: 0x0C05CDCC
- Called by: `ble_219_0c055b90`, `ble_219_0c05cf1c`
- Calls: `ble_nv_record_write`, `ble_nv_record_read`
- Confidence: medium

## ble_mode_nv_encode_write

**Encode a 0-3 mode value to the NV mode byte and write it**

Encodes the mode into one byte and writes it to NV record 0xFA9 (partition 2 +0x12A): 0 is stored as 0xEB, 1 and 3 are stored as themselves, and any other value is stored as 0xFD. The write goes through ble_nv_record_write.

| Parameter | Type | Description |
|---|---|---|
| `mode` | `s32` | mode value, expected 0, 1 or 3 |

- Addresses by version: 219: 0x0C05CCD8
- Called by: `ble_219_0c02a8f8`
- Calls: `ble_nv_record_write`
- Confidence: medium

## ble_mode_nv_is_inactive

**Return 0 when the NV mode byte is 1 or 3, otherwise 1**

Reads the NV mode byte from record 0xFA9 (0xFF on read failure) and returns 0 when it is 1 or 3, and 1 for any other value including 0xEB. It is a boolean gate on the same byte that ble_status_bits_get reads for bit 3.

**Returns** `u32`: 0 when mode byte is 1 or 3; 1 otherwise

- Addresses by version: 219: 0x0C05CD4C
- Called by: `ble_219_0c02a8f8`, `ble_219_0c055b90`, `ble_219_0c05c320`, `ble_219_0c05c3e8`, `ble_219_0c05c480`
- Calls: `ble_nv_record_read`
- Confidence: medium

## ble_pack_version_nibbles

**OR the three nibble bytes into the 24-bit packed word at 0x20012cb0**

Computes DAT_20012cb0 |= DAT_20012caf | (DAT_20012cad << 16) | (DAT_20012cae << 8), combining the nibble values stored by ble_unpack_version_nibbles into a packed value. The old contents are ORed in, not cleared. No direct callers (indirect entry), and the nibble at 0x20012cac is not used.

**Notes:** Likely a Bluetooth version/revision or class-of-device style value; unconfirmed.

- Addresses by version: 219: 0x0C0555DC
- Confidence: low

## ble_pair_table_lookup

**Look up a 16-bit key in an array of {key,value} u16 pairs and compare the value**

Iterates up to param_4 entries (count effectively limited to 8-bit arithmetic) of 4-byte records {u16 key, u16 value} starting at param_3. On the first entry whose key equals param_1, returns 0 if its value equals param_2 and 3 otherwise. If no key matches (or count is 0) returns 0xffff. Looks like a handle/value validation helper where 0=OK, 3=mismatch, 0xffff=not found.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | key to find |
| `param_2` | `u32` | expected value |
| `param_3` | `ptr` | array of {u16 key, u16 value} |
| `param_4` | `s32` | number of entries |

**Returns** `u32`: 0 match, 3 value mismatch, 0xffff key not found

**Notes:** Return code semantics (3 = error status) inferred.

- Addresses by version: 219: 0x0C053EF4
- Called by: `ble_219_0c053018`, `ble_219_0c054668`, `ble_219_0c054734`, `ble_219_0c05486c`
- Confidence: medium

## ble_peer_bdaddr_cache_set

**Cache a 6-byte address at 0x20004977 and mark it valid**

Copies 6 bytes from param_1 (a 4-byte word followed by a 2-byte halfword) to the unaligned RAM bytes 0x20004977..0x2000497c and sets the valid flag at 0x20004976 to 1. The data looks like a Bluetooth device address; callers ble_219_0c052ec0, ble_219_0c052f28 and ble_219_0c052fb0 are likely HCI/LL command handlers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pointer to a 6-byte address (u32 + u16) |

- Addresses by version: 219: 0x0C05C2FC
- Called by: `ble_219_0c052ec0`, `ble_219_0c052f28`, `ble_219_0c052fb0`
- Confidence: medium

## ble_pending_param_store

**Latch a parameter pair and set a valid flag when param_1 == 2, else clear the flag**

If param_1 is not 2, clears the flag byte at 0x200145f8. If it is 2, stores param_2 into the 32-bit slot 0x200145f4, param_3 into byte 0x200145f9, and sets the flag at 0x200145f8 to 1. Only caller is ble_219_0c0585a4, which presumably consumes the latched values later.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | event/mode selector; only the value 2 latches the data |
| `param_2` | `u32` | 32-bit value to latch |
| `param_3` | `u8` | byte value to latch |

- Addresses by version: 219: 0x0C05A9A4
- Called by: `ble_link_param_monitor_step`
- Confidence: low

## ble_rom_ptr_table_get_0c07ffac

**Return the address of the pointer table at 0x0c07ffac**

Returns the constant address 0x0c07ffac (symbol PTR_LAB_0c05d1f0_1_0c07ffac), a table of code pointers in the flash image. Pure accessor used by ble_219_0c05b67c.

**Returns** `ptr`: pointer to the table at 0x0c07ffac

- Addresses by version: 219: 0x0C05D48C
- Called by: `ble_219_0c05b67c`
- Confidence: low

## ble_rom_ptr_table_get_0c0800b4

**Return the address of the pointer table at 0x0c0800b4**

Returns the constant address 0x0c0800b4 (symbol PTR_LAB_0c05d3a4_1_0c0800b4), a table of code pointers in the flash image. Pure accessor used by ble_219_0c05b67c.

**Returns** `ptr`: pointer to the table at 0x0c0800b4

- Addresses by version: 219: 0x0C05D4A4
- Called by: `ble_219_0c05b67c`
- Confidence: low

## ble_rom_table_get_0c07fe00

**Return the address of the constant data block at 0x0c07fe00**

Returns the constant pointer &DAT_0c07fe00 (flash read-only data). Pure address accessor used by ble_219_0c05b67c, which also uses the neighbouring pointer-table accessors at 0x0c05d48c and 0x0c05d4a4.

**Returns** `ptr`: pointer to flash data at 0x0c07fe00

- Addresses by version: 219: 0x0C05B71C
- Called by: `ble_219_0c05b67c`
- Confidence: low

## ble_rom_table_get_0c0810e0

**Return the address of the constant data block at 0x0c0810e0**

Returns the constant pointer &DAT_0c0810e0, an address inside the flash image (read-only data). Pure address accessor, used by ble_219_0c0592a4 to reach that table; its contents were not analysed here.

**Returns** `ptr`: pointer to flash data at 0x0c0810e0

- Addresses by version: 219: 0x0C05B670
- Called by: `ble_219_0c0592a4`
- Confidence: low

## ble_rssi_filter_update

**Outlier-clamp and Kalman-filter a 5-sample signed RSSI window, return the mean**

Smooths a window of five signed 8-bit samples (RSSI-like) for one channel. When the first sample is nonzero, it computes the mean and standard deviation of all five with soft-float arithmetic, and replaces samples more than two standard deviations from the mean of the nonzero samples with that nonzero mean. It then runs one scalar Kalman update on the newest sample: K = (P+Q)/(P+Q+R), x = x + K(z - x), P = (1-K)(P+Q). The per-channel state (x, P, K) is at 0x20004948 for channel 0 or 0x20004960 for channel 1; the shared process noise Q is at 0x2000495C and measurement noise R at 0x20004958, copied to 0x20014570 and 0x20014574 for inspection. The filtered value is written back to byte 4 of the window. The return value is the mean of the nonzero samples at positions 2 to 4, as a signed byte.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 5-byte signed sample window; byte 4 is the newest sample and is overwritten with the filtered value |
| `param_2` | `u32` | channel: 0 selects state at 0x20004948, nonzero selects state at 0x20004960 |

**Returns** `s32`: mean of nonzero samples at positions 2 to 4, as a signed byte; 0 if none are nonzero

**Notes:** The sigma threshold uses a truncated integer standard deviation. The sqrt routine at 0x0C06F220 and the float-to-int conversion at 0x0C06FD30 are inferred from call shape. Q and R are labelled as process and measurement noise from the Kalman form, which is a medium-confidence reading.

- Addresses by version: 219: 0x0C059B60
- Called by: `ble_219_0c059f64`
- Calls: `ble_219_0c06f220`, `__aeabi_dadd`, `__aeabi_f2d`, `__aeabi_dmul`, `__aeabi_d2iz`, `__aeabi_d2f`
- Confidence: medium

## ble_set_flag_12606

**Set byte flag 0x20012606 to 1**

Writes 1 to DAT_20012606. Paired with ble_get_flag_12606; called from ble_219_0c05cc70.

- Addresses by version: 219: 0x0C054710
- Called by: `ble_host_5min_timer_ctrl`
- Confidence: low

## ble_set_indexed_word_1307c

**Store a 32-bit value in the 4-entry u32 array at 0x2001307c**

If param_2 < 4, writes param_1 to the u32 at 0x2001307c + param_2*4; out-of-range indices are ignored silently. Called from the configuration routines ble_219_0c02973c and ble_219_0c0297b0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value to store |
| `param_2` | `u32` | array index 0..3 |

- Addresses by version: 219: 0x0C0571B0
- Called by: `ble_219_0c02973c`, `ble_219_0c0297b0`
- Confidence: medium

## ble_set_mode_14_or_16

**Store 0x10 if param_1 is 0x10, otherwise 0x0e, into byte 0x20004344**

Normalises the argument: anything other than 0x10 becomes 0x0e, then writes the low byte to DAT_20004344. So the variable can only hold 16 or 14. Called from the configuration routines ble_219_0c02973c and ble_219_0c0297b0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | requested value; only 0x10 is preserved |

**Notes:** Meaning of 14/16 unknown (could be a length or size selector).

- Addresses by version: 219: 0x0C0581E0
- Called by: `ble_219_0c02973c`, `ble_219_0c0297b0`
- Confidence: low

## ble_set_timeout_ms_to_us

**Store param_1 * 1000 into 0x200041c8**

Multiplies the argument by 1000 and writes it to DAT_200041c8; the factor suggests a milliseconds to microseconds conversion of a timing parameter. Called from ble_219_0c053018.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | value in ms (presumed) |

**Notes:** Unit interpretation guessed from the 1000 multiplier.

- Addresses by version: 219: 0x0C05527C
- Called by: `ble_219_0c053018`
- Confidence: low

## ble_set_word_1308c

**Store 32-bit value into global 0x2001308c**

Trivial setter: DAT_2001308c = param_1. Called from ble_219_0c02973c and ble_219_0c0297b0 (configuration routines).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | new value |

- Addresses by version: 219: 0x0C0571A4
- Called by: `ble_219_0c02973c`, `ble_219_0c0297b0`
- Confidence: low

## ble_set_word_130d4

**Store 32-bit value into global 0x200130d4**

Trivial setter: DAT_200130d4 = param_1; called from ble_219_0c0297b0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | new value |

- Addresses by version: 219: 0x0C0571C0
- Called by: `ble_219_0c0297b0`
- Confidence: low

## ble_slot_count_used

**Count slots in the 4-entry table whose id byte is not 0xff**

Walks the four 16-byte slots at 0x20010198 and counts those whose byte at +12 differs from 0xff (the free marker). Returns the count 0..4. Used by several callers deciding whether any slot/connection is active.

**Returns** `u8`: number of used slots, 0..4

- Addresses by version: 219: 0x0C05341C
- Called by: `ble_219_0c053018`, `ble_219_0c0540f4`, `ble_219_0c054180`, `ble_219_0c05420c`, `ble_slot_store_and_queue`
- Confidence: high

## ble_slot_expiry_scan

**Scan the slot table against the tick count; the result is always 0**

Reads the tick count through xTaskGetTickCount, then walks the 4-entry table at 0x20010198 (16-byte entries: a 64-bit value at +0..+7, id byte at +12). Free entries (id 0xFF) are skipped, as are entries whose id has flag 5 set (for id 0xFE, when any slot has it). For the rest it compares a 64-bit sum of the entry value and the word from ble_get_word_41cc with the tick count; the exact 64-bit comparison is hard to read in the decompile. Only calls are visible, no memory is written, and the function returns 0 on every path.

**Returns** `u32`: always 0

**Notes:** The intended expiry result is not visible in this build, so the purpose is inferred from the table layout.

- Addresses by version: 219: 0x0C0534E0
- Calls: `xTaskGetTickCount`, `ble_slot_test_flag`, `ble_get_word_41cc`
- Confidence: low

## ble_slot_get_field_0x14

**Return the 32-bit field at offset 0x14 of the slot record selected by an index-mapped id**

Looks up param_1 in the byte map at 0x20003908 to get a slot number, uses it to index the pointer table at 0x2000306c (4 bytes per entry), and returns the 32-bit word at offset 0x14 of the record that pointer addresses. There is no null or range check on the id or the pointer. Called from 0c087464 and 0c089190, which appear to be a registration/dispatch layer keyed by a small id (probably a link, task or channel id). The meaning of the field is not established from this function alone; it could be a context or handle value.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | logical id (index into byte map at 0x20003908) |

**Returns** `u32`: word at offset 0x14 of the selected slot record

**Notes:** Struct layout inferred only from field accessors (+8 u16, +0xa u16, +0x14 u32, +0x18 callback); owning subsystem unconfirmed.

- Addresses by version: 219: 0x0C088520
- Called by: `ble_219_0c087464`, `norflash_status_reg_op`
- Confidence: medium

## ble_slot_get_header_ptr

**Return address of the structure at 0x20010188 preceding the slot table**

Returns constant &DAT_20010188, the 16 bytes immediately before the slot table at 0x20010198. No other work.

**Returns** `ptr`: pointer to 0x20010188

- Addresses by version: 219: 0x0C053764
- Called by: `ble_219_0c05c7b6`
- Confidence: medium

## ble_slot_get_u16_at_0x08

**Return the 16-bit field at offset 0x08 of the slot record selected by an index-mapped id**

Maps param_1 through the byte table at 0x20003908 to a slot index, loads the record pointer from the table at 0x2000306c (4 bytes per entry), and returns the halfword at offset 0x08 of that record. No bounds or null checks are made. Its only caller is 0c089190, which also uses the +0x0a and +0x14 accessors. Likely a size, length or handle parameter of the slot.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | logical id (index into byte map at 0x20003908) |

**Returns** `u16`: halfword at offset 0x08 of the slot record

**Notes:** Semantics of the field not established.

- Addresses by version: 219: 0x0C088550
- Called by: `norflash_status_reg_op`
- Confidence: medium

## ble_slot_get_u16_at_0x0a

**Return the 16-bit field at offset 0x0a of the slot record selected by an index-mapped id**

Maps param_1 through the byte table at 0x20003908 to a slot index, loads the record pointer from the table at 0x2000306c (4 bytes per entry), and returns the halfword at offset 0x0a of that record. No bounds or null checks are made. Its only caller is 0c089190, which also reads the sibling field at +8 and the +0x14 word through the sibling accessors, so these are probably parameters (for example a length, size or handle) of the registered slot.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | logical id (index into byte map at 0x20003908) |

**Returns** `u16`: halfword at offset 0x0a of the slot record

**Notes:** Semantics of the field not established.

- Addresses by version: 219: 0x0C088538
- Called by: `norflash_status_reg_op`
- Confidence: medium

## ble_slot_invoke_callback_evt4

**Call the slot's registered callback (offset 0x18) with event code 4, return 0 or -1 if none**

Resolves param_1 through the byte map at 0x20003908 and the pointer table at 0x2000306c to a slot record, then reads the function pointer at offset 0x18. If it is non-null it is called as cb(param_1, 4, param_2, cb, param_4) and the function returns 0. The fifth argument position is filled with the callback pointer itself, which is probably a decompiler artefact of register reuse, so the real callback arguments are most likely (id, event=4, param_2, ...). If no callback is registered it returns 0xFFFFFFFF. param_3 is unused. Called from 0c0873ec.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | logical id used to select the slot and passed as first callback argument |
| `param_2` | `u32` | passed through as the third callback argument |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | passed through as an extra callback argument |

**Returns** `s32`: 0 if a callback was invoked, -1 if no callback is registered

**Notes:** Event code 4 meaning unknown. The callback argument list is uncertain because of register-reuse artefacts.

- Addresses by version: 219: 0x0C08915C
- Called by: `ble_219_0c0873ec`
- Confidence: medium

## ble_slot_mgr_check_flag5

**When the slot manager is ready, run the flag-5 test for slot param_1 (or all slots)**

Calls ble_slot_mgr_is_ready() and returns at once if it is 0. Otherwise it calls ble_slot_test_flag_any(param_1, 5) and ignores its result. The function has no return value, so it acts only through the side effects of the flag test, if any.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | slot id; 0xFE selects all slots |

- Addresses by version: 219: 0x0C0531B8
- Called by: `ble_app_queue_message`
- Calls: `ble_slot_test_flag_any`, `ble_slot_mgr_is_ready`
- Confidence: medium

## ble_slot_mgr_is_ready

**Check that the slot manager marker byte equals 0xa5**

Returns (DAT_200101d9 == 0xa5), the byte directly after the slot table; 0xa5 looks like an initialised/valid magic written by the setup code. Widely used (8 callers) as a guard before touching the slot data.

**Returns** `bool`: true when the marker is 0xa5

**Notes:** Interpretation of 0xa5 as 'initialised' is inferred.

- Addresses by version: 219: 0x0C0537A0
- Called by: `ble_219_0c02a8f8`, `ble_219_0c053018`, `ble_slot_mgr_check_flag5`, `ble_219_0c053f24`, `ble_219_0c054534`, `ble_219_0c054734`, `ble_status_bits_get`, `ble_219_0c05cf1c`
- Confidence: medium

## ble_slot_set_flag

**Set or clear a bit in the flag word of the slot with a given id**

Same 4-entry, 16-byte-stride table at 0x20010198 as ble_slot_test_flag. Returns without action if param_1 is 0xff or no slot has that id at +12. Otherwise, if param_3 is non-zero ORs 1 << (param_2 & 0xff) into the slot's flag word (+8), else clears that bit. Not interrupt-protected.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | slot id (0xff = invalid) |
| `param_2` | `u32` | bit number |
| `param_3` | `s32` | non-zero to set, zero to clear |

- Addresses by version: 219: 0x0C053390
- Called by: `ble_219_0c053018`, `ble_219_0c054668`
- Confidence: medium

## ble_slot_set_flag_101e0

**Store a byte into global 0x200101e0**

Trivial setter: DAT_200101e0 = param_1, a variable located just after the slot table and its 0xa5 marker. Called from ble_219_0c053018.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | new value |

- Addresses by version: 219: 0x0C053830
- Called by: `ble_219_0c053018`
- Confidence: low

## ble_slot_test_flag

**Test whether a bit is set in the flag word of the slot with a given id**

The module keeps a 4-entry table of 16-byte slots at 0x20010198..0x200101d8; byte +12 of each slot is an id (0xff means unused) and the u32 at +8 is a flag/bitmask word. Returns false immediately for id 0xff, then scans the table for a slot whose id equals param_1 (a redundant second scan repeats the search to find its index) and returns whether bit (param_2 & 0xff) of that slot's flag word is set. Returns false if no slot matches.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | slot id (0xff = invalid) |
| `param_2` | `u32` | bit number to test |

**Returns** `bool`: true if the bit is set

**Notes:** Slot table is probably per-connection or per-activity state; not confirmed.

- Addresses by version: 219: 0x0C0531D0
- Called by: `ble_219_0c053018`, `ble_slot_test_flag_any`, `ble_slot_expiry_scan`
- Confidence: medium

## ble_slot_test_flag_any

**Test flag bit param_2 on one slot, or on each slot until one reports set**

For a specific slot id (not 0xFE) it calls ble_slot_test_flag(id, bit) and returns without using the result. For id 0xFE it walks the 4-entry table at 0x20010198 (16-byte entries, id byte at +12) and calls ble_slot_test_flag(entry_id, bit) on each entry, stopping at the first call that returns true. The function returns nothing; free entries (id 0xFF) are rejected inside ble_slot_test_flag.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | slot id, or 0xFE for all slots |
| `param_2` | `u32` | flag bit number |

- Addresses by version: 219: 0x0C05328C
- Called by: `ble_219_0c053018`, `ble_slot_mgr_check_flag5`, `ble_219_0c054668`, `ble_219_0c0553d0`
- Calls: `ble_slot_test_flag`
- Confidence: medium

## ble_state_12c81_is_2

**Check whether state byte 0x20012c81 equals 2**

Returns (DAT_20012c81 == 2). Called from ble_219_0c054668; the byte is presumably a state/mode enum value.

**Returns** `bool`: true when the byte equals 2

- Addresses by version: 219: 0x0C055230
- Called by: `ble_219_0c054668`
- Confidence: low

## ble_state_407a_copy

**Copy the state byte 0x2000407a to *param_1 (ble_get_value_407a with index 0)**

Tail-calls ble_get_value_407a(0, param_1), which writes DAT_2000407a into the byte at param_1. Pointer-output variant of ble_state_407a_read, used by the status reporter 0c02a8f8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | out: 1 byte |

- Addresses by version: 219: 0x0C05CFC8
- Called by: `ble_219_0c02a8f8`
- Calls: `ble_get_value_407a`
- Confidence: high

## ble_state_407a_read

**Return the state byte at 0x2000407a (via ble_get_value_407a index 0)**

Zeroes a local byte, calls ble_get_value_407a(0, &local) which copies DAT_2000407a into it, and returns the byte. A plain getter used by 0c052ee4, 0c052f28, 0c052fb0 and 0c05ada4 to test the current value of that state/mode byte; ble_state_407a_copy is the pointer-output variant.

**Returns** `u8`: current value of DAT_2000407a

- Addresses by version: 219: 0x0C05C778
- Called by: `ble_219_0c052ee4`, `ble_219_0c052f28`, `ble_219_0c052fb0`, `ble_gatt_read_char_value`
- Calls: `ble_get_value_407a`
- Confidence: high

## ble_state_cb_register

**Install a callback into one of four notification slots at 0x20014610**

Bounds-checks param_2 < 4 and, if valid, stores param_1 into the pointer array at 0x20014610 at index param_2; out-of-range indexes are silently ignored. The array is traversed by ble_state_change_notify. Called from ble_219_0c0297b0 during init.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | callback function pointer |
| `param_2` | `u32` | slot index 0..3 |

- Addresses by version: 219: 0x0C059F0C
- Called by: `ble_219_0c0297b0`
- Confidence: medium

## ble_state_change_notify

**Update the state byte at 0x20004970 and notify the registered callbacks**

Ignores param_1 values 2 and 3 and any value equal to the current state in DAT_20004970. Otherwise stores the new state and walks the four-entry callback array at 0x20014610..0x20014620: for param_1==1 each non-NULL callback is invoked with argument 1, for param_1==0 each is invoked with argument 2. Callbacks are installed with ble_state_cb_register. No direct callers (invoked via function pointer / event).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | new state: 0 or 1 (2 and 3 are ignored) |

**Notes:** Likely a BT enable/disable (or link up/down) event fan-out; exact event not confirmed.

- Addresses by version: 219: 0x0C059E9C
- Confidence: medium

## ble_state_is_0x102

**Test whether the state word at 0x200145b0 equals 0x102**

Returns true when the 32-bit global at 0x200145b0 equals 0x102. Sibling of ble_state_is_0x110 and used by the same callers (ble_219_0c0572c0, ble_219_0c0573c4, ble_219_0c05741c).

**Returns** `bool`: 1 if _DAT_200145b0 == 0x102

**Notes:** Meaning of the 0x102/0x110 values unknown.

- Addresses by version: 219: 0x0C05A198
- Called by: `ble_219_0c0572c0`, `ble_219_0c0573c4`, `ble_219_0c05741c`
- Confidence: medium

## ble_state_is_0x110

**Test whether the 32-bit state word at 0x200145b0 equals 0x110**

Returns true when the global at 0x200145b0 (read as a 32-bit word) equals 0x110. Companion of ble_219_0c05a198 which tests the same word against 0x102. Used by ble_219_0c0572c0, ble_219_0c0573c4 and ble_219_0c05741c as a mode/variant check.

**Returns** `bool`: 1 if _DAT_200145b0 == 0x110

**Notes:** The word looks like a configuration/chip-variant or state code; exact meaning unknown.

- Addresses by version: 219: 0x0C059390
- Called by: `ble_219_0c0572c0`, `ble_219_0c0573c4`, `ble_219_0c05741c`
- Confidence: medium

## ble_status_bits_get

**Compose a 4-bit BLE status mask from object flags, slot state, timer flag and mode**

Builds a status mask. Bit 0 is set when flag 0x80 in the word at 0x200042F8+4 is set and the byte at 0x20017046 equals 1. Bit 1 is set when ble_slot_mgr_is_ready reports ready. Bit 2 is set when the global flag at 0x20012606 is clear. Bit 3 is set when the mode byte in NV record 0xFA9 is 1 or 3 (0xEB and failed reads, which leave 0xFF, do not count).

**Returns** `u8`: status bitmask, bits 0 to 3

- Addresses by version: 219: 0x0C05CBC4
- Called by: `ble_219_0c028c94`, `ble_219_0c02a8f8`
- Calls: `ble_slot_mgr_is_ready`, `ble_get_flag_12606`, `ble_get_state_ptr_42f8`, `ble_nv_record_read`
- Confidence: medium

## ble_thunk_call_0c03aafc

**Thin wrapper that calls a function at fixed address 0x0c03aafc (Thumb) with its argument**

Casts the constant 0x0c03aafd to a function pointer and calls it with param_1. Bit 0 set means a Thumb entry, so the target is 0x0c03aafc. This is outside the analysed function list, so it is probably a ROM-resident or patched routine. The only caller is 0c086754, which also calls the neighbouring wrapper 0c089488 (target 0x0c03ab18). They look like paired start/stop or enable/disable calls.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | argument forwarded unchanged |

**Notes:** Target 0x0c03aafc is not in the function list; function purpose unknown.

- Addresses by version: 219: 0x0C089478
- Called by: `hal_sys_timer_calc_loop_ticks`
- Confidence: low

## ble_thunk_call_0c03ab18

**Thin wrapper that calls a function at fixed address 0x0c03ab18 (Thumb) with its argument**

Casts the constant 0x0c03ab19 to a function pointer and calls it with param_1. Bit 0 set means a Thumb entry, so the target is 0x0c03ab18. This is outside the analysed function list, so it is probably a ROM-resident or patched routine. The only caller is 0c086754, which also calls the neighbouring wrapper 0c089478. They look like paired calls on the same object.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | argument forwarded unchanged |

**Notes:** Target 0x0c03ab18 is not in the function list; function purpose unknown.

- Addresses by version: 219: 0x0C089488
- Called by: `hal_sys_timer_calc_loop_ticks`
- Confidence: low

## ble_thunk_call_0c0401b0

**Thin wrapper that forwards its single argument to FUN_0c0401b0**

Calls the function at 0x0c0401b0 with param_1 and returns. That target is 210 bytes, calls three helpers at 0x0c0326a8/c4/e8 and writes globals around 0x20003d70..0x20003d80. The tiny wrapper is probably a patch or ROM-redirect veneer. The decompiler flags one indirect call here, so the real target may be resolved through a literal or table. Called from 0c086b04 and 0c086c30, which also call the sibling wrapper 0c0894a8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | argument forwarded unchanged |

**Notes:** Purpose of the target unknown. Probably forms a pair with ble_219_0c0894a8 in the callers (for example enter/exit or start/stop).

- Addresses by version: 219: 0x0C089468
- Called by: `analogif_reg30b7_channel_read`, `analogif_reg3037_3048_config`
- Confidence: low

## ble_thunk_call_0c040290

**Thin wrapper that forwards its single argument to FUN_0c040290**

Calls the function at 0x0c040290 with param_1 and returns. That target is 220 bytes, calls helpers at 0x0c0326a8/c4 and 0x0c0418e0/f4, and writes the same globals (0x20003d70..0x20003d80) as the target of the sibling wrapper 0c089468. The tiny wrapper is probably a patch or ROM-redirect veneer. The decompiler flags one indirect call. Called from 0c086b04 and 0c086c30 together with 0c089468.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | argument forwarded unchanged |

**Notes:** Purpose of the target unknown. Probably pairs with ble_219_0c089468.

- Addresses by version: 219: 0x0C0894A8
- Called by: `analogif_reg30b7_channel_read`, `analogif_reg3037_3048_config`
- Confidence: low

## ble_unpack_version_nibbles

**Split a 16-bit value into four nibble bytes at 0x20012cac..caf**

Stores bits 15..12 of param_1 to DAT_20012cac, bits 11..8 to DAT_20012cad, bits 7..4 to DAT_20012cae and bits 3..0 to DAT_20012caf (each as a separate byte). Called from ble_219_0c0297b0 during configuration.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 16-bit value, e.g. a packed BCD-like version number |

- Addresses by version: 219: 0x0C055610
- Called by: `ble_219_0c0297b0`
- Confidence: low

## bt_bdaddr_reverse_inplace

**Reverse the byte order of a 6-byte Bluetooth device address in place**

Copies the six bytes at param_1 in reverse order into a local buffer and then writes the 6 bytes back over the original (a 4-byte + 2-byte store), converting between little- and big-endian BD_ADDR representations. Equivalent to BTstack's reverse_bd_addr but operating in place. Called from ble_219_0c0581a8 and ble_219_0c05a8a0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pointer to a 6-byte BD_ADDR, modified in place |

- Addresses by version: 219: 0x0C05A9E4
- Called by: `ble_random_static_addr_build`, `ble_conn_select_link_and_fill_info`
- Confidence: high

## bt_drv_set_global_2000bd1c

**Store a 32-bit value into global DAT_2000bd1c**

Trivial setter: DAT_2000bd1c = param_1. Called from two routines in the 0x0c0469xx/0x0c046cxx region (controller/driver code). The meaning of the variable is unknown; it is only written here in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value stored in DAT_2000bd1c |

**Notes:** Semantics of DAT_2000bd1c not determined from this function alone; name is positional.

- Addresses by version: 219: 0x0C03AC8C
- Called by: `ble_219_0c04696c`, `ble_219_0c046c7c`
- Confidence: low

## ll_conn_params_in_range

**Check requested connection parameters against allowed range**

param_1 points to six u16 limits: [0] and [1] bound the interval, [2],[3] bound latency, [4],[5] bound the supervision timeout. Returns true only if lim[0] <= param_2 and param_3 <= lim[1] (interval min/max), lim[2] <= param_4 <= lim[3] (slave latency), and lim[4] <= param_5 <= lim[5] (timeout). In the caller (LL_CONNECTION_PARAM_REQ, opcode 0x12) param_2..5 are the u16 fields read at PDU offsets 4,6,8,10, and a false result sets reject-reason byte 4 in the link record.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | six u16 limits obtained from ll_get_conn_param_range |
| `param_2` | `u16` | requested minimum interval |
| `param_3` | `u16` | requested maximum interval |
| `param_4` | `u16` | requested slave latency |
| `param_5` | `u16` | requested supervision timeout |

**Returns** `bool`: true if all parameters are within limits

- Addresses by version: 219: 0x0C066508
- Called by: `ble_219_0c06dc56`
- Confidence: medium

## ll_env_clear_flag_170

**Clear byte at controller env offset 0x170**

Writes 0 to *(u8 *)(DAT_200190d0 + 0x170). Setter counterpart of ll_env_get_flag_170. Callers: 05806c and 06d5d8.

- Addresses by version: 219: 0x0C066C1C
- Called by: `ble_219_0c05806c`, `hci_release_packet_buffer_thunk`
- Confidence: medium

## ll_env_get_flag_170

**Return byte at controller env offset 0x170**

Returns *(u8 *)(DAT_200190d0 + 0x170). This byte is cleared by ll_env_clear_flag_170 and ll_env_reset_defaults, and tested by ll_env_is_ready (non-zero blocks it). Callers: 05806c, 06d5dc, 06ed64.

**Returns** `u8`: flag value

- Addresses by version: 219: 0x0C066BD8
- Called by: `ble_219_0c05806c`, `ble_219_0c06d5dc`, `ble_219_0c06ed64`
- Confidence: medium

## ll_env_get_u16_196

**Return u16 at controller env offset 0x196**

Returns *(u16 *)(DAT_200190d0 + 0x196). Simple getter; sole caller is 0c06cdb8. Field meaning unknown.

**Returns** `u16`: value of env field at +0x196

- Addresses by version: 219: 0x0C066CF4
- Called by: `ble_219_0c06cdb8`
- Confidence: low

## ll_env_get_u32_68

**Return u32 at controller env offset 0x68**

Returns *(u32 *)(DAT_200190d0 + 0x68). Simple getter used by 0c06c7ac, 06cb3c, 06d5c8, 06d5dc, 06d648, 06ed64. Field meaning unknown.

**Returns** `u32`: value of env field at +0x68

- Addresses by version: 219: 0x0C066D04
- Called by: `ble_219_0c06c7ac`, `ble_219_0c06cb3c`, `ll_env_get_u32_68_plus8`, `ble_219_0c06d5dc`, `ble_219_0c06d648`, `ble_219_0c06ed64`
- Confidence: low

## ll_env_get_u32_68_plus8

**Return the u32 at controller env +0x68 plus 8**

Calls ll_env_get_u32_68 (0x0C066D04) and returns its value plus 8. The +8 suggests the value at env+0x68 is a pointer and the caller wants the address of a sub-field at offset 8 of that object.

**Returns** `u32`: env+0x68 value plus 8

**Notes:** Meaning of env+0x68 is unknown. Callers 0c04e398, 0c04ebc0, 0c04ec18.

- Addresses by version: 219: 0x0C06D5C8
- Called by: `ble_219_0c04e398`, `ble_219_0c04ebc0`, `ble_219_0c04ec18`
- Calls: `ll_env_get_u32_68`
- Confidence: low

## ll_env_has_free_slot

**Check whether another link slot is available**

With env = DAT_200190d0: first, if the callback table at env[0] has a function at offset 0x14, calls it with 3 and returns false if it returns 0. If the string pointed to by table[0] begins with 'H','2' the function returns byte env+0x187. Otherwise it walks the linked list at env[5] (each node: next pointer at +0). If byte env+0x17e is 0 it counts nodes whose byte +0xc is 0xfc and byte +0x56 is non-zero; if it is non-zero it sums byte +0x194 over nodes whose byte +0xc is 0xfc and compares against byte env+0x17c, returning false when the sum exceeds it and otherwise using the difference. Returns count > 0 (or remaining capacity > 0). Sole caller is 0c066b20.

**Returns** `bool`: true if at least one slot/resource remains

**Notes:** Looks like a connection/resource availability check but the node type 0xfc and the 'H2' string are not understood.

- Addresses by version: 219: 0x0C066A94
- Called by: `ble_ctrl_flush_deferred_event`
- Confidence: low

## ll_env_init

**Initialise the link-layer environment and register the HCI packet handler**

Points DAT_200190D0 at the 0x240-byte environment at DAT_200190D4 and clears it with memset. It stores the transport table (param_1) at env+0x00 and the context (param_2) at env+0x04, then installs the HCI packet handler 0x0C068DA8 through table+0x10. Defaults set here: the state byte at +0x198 = 0, bytes +0x58 = 2 and +0x5A = 4, the minimum encryption key size at +0x52 = 7, the LE connection-parameter ranges at +0x1EC/+0x1F0/+0x1F4 (interval 6..3200, latency 0..500, supervision timeout 10..3200), the local name pointer at +0x2C ('BThost 00:00:00:00:00:00'), and several capability words. It then calls ll_env_reset_defaults.

| Parameter | Type | Description |
|---|---|---|
| `transport` | `ptr` | transport/callback table; entry +0x10 sets the packet handler |
| `context` | `ptr` | opaque context stored at env+0x04 |

**Notes:** Parameter ranges are read as BLE spec units (1.25 ms, 10 ms) from the values. The packet handler 0x0C068DA8 is not described in this packet.

- Addresses by version: 219: 0x0C066DFC
- Called by: `ble_219_0c05b67c`
- Calls: `ll_env_reset_defaults`, `memset`
- Confidence: medium

## ll_env_is_ready

**Check whether controller env permits the operation**

With env = DAT_200190d0: returns false if byte env+0x170 is non-zero. Otherwise, if the callback table at env[0] has a function at offset 0x14 it must return non-zero when called with argument 1 (otherwise false); if no such function exists the check passes. When all checks pass, returns (byte env+0x177 != 0). Used as a gate in 0c051eb8, 065038, 067178, 0674e8 and 06cdb8.

**Returns** `bool`: true when allowed and flag at +0x177 is set

**Notes:** Names of the flags at env+0x170 and +0x177 not known; the 0x170 byte is also cleared by ll_env_clear_flag_170.

- Addresses by version: 219: 0x0C066978
- Called by: `ble_219_0c051eb8`, `ble_219_0c065038`, `ble_219_0c067178`, `ble_219_0c0674e8`, `ble_219_0c06cdb8`
- Confidence: low

## ll_env_reset_defaults

**Reset link-layer environment runtime fields to defaults**

With env = DAT_200190d0: sets env+0x5c = 0x9e8b33 (0x9e8b33 is the Bluetooth General Inquiry Access Code LAP), zeroes env+0x14 (word), bytes at 0x170, 0x1d5, 0x46, word 0x1dd, half 0x1e1, byte 0x1e3, clears bit1 of byte 0x21f, sets env+0x50 = 0x6000 and env+0x48 = 0x9f. If bit0 of the old 0x21f byte was set it sets bit2 of byte 0x1f8, and if word 0x1fc is non-zero it sets bit0 of byte 0x1f8. Called from 0c066dfc and 0c0674e8 (init/reset paths).

**Notes:** 0x9e8b33 is the Bluetooth general inquiry access code LAP (GIAC), which hints this env also covers BR/EDR; field roles beyond that are guesses.

- Addresses by version: 219: 0x0C065E8C
- Called by: `ll_env_init`, `ble_219_0c0674e8`
- Confidence: medium

## ll_env_run_stop_hooks

**Invoke controller hooks then clear status byte 0x198**

Uses env = DAT_200190d0 (link-layer/controller environment pointer). Calls the function at offset 0xc of the callback table pointed to by env[0]; then, if env[3] (offset 0xc) is non-NULL and the object it points to has a non-NULL function pointer at offset 8, calls that as well. Finally clears the byte at env+0x198. Looks like a stop/reset sequence: notify the registered handlers and clear a state flag. Called from 0c0674e8, 0c068da8, 0c06b048.

**Notes:** Exact meaning of env offsets 0xc and 0x198 not determined; semantics inferred from structure only.

- Addresses by version: 219: 0x0C065DF8
- Called by: `ble_219_0c0674e8`, `ble_219_0c068da8`, `ble_219_0c06b048`
- Confidence: low

## ll_get_conn_param_range

**Copy 12-byte connection-parameter acceptance range**

Copies three words from the controller environment (DAT_200190d0 + 0x1ec, 0x1f0, 0x1f4) into the 12-byte buffer at param_1. The 12 bytes are six u16 limits that ll_conn_params_in_range() consumes. Used by the LL_CONNECTION_PARAM_REQ handler (0c06dc56, control opcode 0x12).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 12-byte output buffer (6 x u16) |

- Addresses by version: 219: 0x0C0664E8
- Called by: `ble_219_0c06dc56`
- Confidence: medium

## ll_hook_call_0x14

**Call optional external hook at table offset 0x14**

If the pointer at DAT_200190d0+0x10 (an external callback table) is non-NULL, tail-calls the function pointer at offset 0x14 of that table with no arguments; otherwise returns. The decompiler could not recover the indirect jump. Callers: 05741c, 05a53c, 05a804, 06d9b0.

- Addresses by version: 219: 0x0C066618
- Called by: `ble_219_0c05741c`, `ble_219_0c05a53c`, `ble_219_0c05a804`, `ble_219_0c06d9b0`
- Confidence: medium

## ll_hook_call_0x18

**Call optional external hook at table offset 0x18**

If the table pointer at DAT_200190d0+0x10 is non-NULL and its function pointer at offset 0x18 is non-NULL, tail-calls it and returns its result; otherwise returns 0.

**Returns** `u32`: hook result, or 0 if absent

- Addresses by version: 219: 0x0C066698
- Called by: `ble_link_table_prune_by_ctrl`
- Confidence: medium

## ll_hook_call_0x1c

**Call optional external hook at table offset 0x1c**

If the table pointer at DAT_200190d0+0x10 is non-NULL, tail-calls the (unchecked) function pointer at offset 0x1c and returns its result; otherwise returns 0.

**Returns** `u32`: hook result, or 0 if no table

- Addresses by version: 219: 0x0C0666B0
- Called by: `ble_link_table_prune_by_ctrl`
- Confidence: medium

## ll_hook_call_0x20

**Call optional external hook at table offset 0x20**

If the table pointer at DAT_200190d0+0x10 is non-NULL, tail-calls the function pointer at offset 0x20 with no arguments; otherwise returns. Sibling of ll_hook_call_0x14/0x18/0x1c; all four are called from the same area (0c05a4a8, 0c05741c ...).

- Addresses by version: 219: 0x0C0666D0
- Called by: `ble_link_table_prune_by_ctrl`
- Confidence: medium

## ll_link_check_flag_or_state_by_key

**Test a link record found by key: flag byte at +0x1C2, or state 7 or 8**

Finds the link record in the env+0x14 list whose u16 key at +0x0A equals param_1 and returns false when there is none. For class byte at +0x0C below 2 it returns true when the flag byte at +0x1C0 is set and the byte at +0x1C2 is non-zero. For larger class values it returns true only when (class + 4) truncated to a byte is 0 or 1 and the u16 at +0x28 minus 7 is below 2, i.e. the state is 7 or 8. Group: link-record accessors by key (ll_link_*_by_key).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | record key (+0x0A) to match |

**Returns** `bool`: true when the selected flag or state test holds

**Notes:** Same class-byte caveat as ll_link_get_flag_by_key. Caller 0c04e702.

- Addresses by version: 219: 0x0C06BBB8
- Called by: `ble_219_0c04e702`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: medium

## ll_link_emit_event_78

**Emit vendor event 0x78 for a link and move matching L2CAP channel sub-states**

Sets the record's state byte at +0x318 to 5, then builds an 8-byte H4 event (code 0x78, length 6) from the u16 values at record +0x0A, +0x31A and +0x31C and broadcasts it with ble_listener_broadcast_event. It then walks the L2CAP channel list at 0x2001944C and, for each channel in state 0, 2 or 5 whose u16 at +0x24 equals the record's +0x0A, changes sub-state 7 at +0x20 to 0x11 and sub-state 8 to 0x0E; other channels are untouched. Group: vendor H4 event emitters.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | connection record: key at +0x0A, fields at +0x31A and +0x31C, state byte at +0x318 |

**Notes:** Event code 0x78 and the meaning of sub-states 7, 8, 0x0E and 0x11 are inferred. Caller 0c06dc56.

- Addresses by version: 219: 0x0C06C504
- Called by: `ble_219_0c06dc56`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`, `co_write16_le`, `ble_listener_broadcast_event`
- Confidence: medium

## ll_link_emit_event_79

**Send a 4-byte vendor event 0x79 with a u16 handle to a callback and the hook**

Builds [0x79][length 2][u16 param_2, little-endian], passes it to ble_hook_invoke4(4, 1, ...) and then calls the caller-supplied callback param_1 with (4, handle, buffer). Unlike ll_link_emit_event_code_handle the callback arrives as an argument rather than from a record. Group: vendor H4 event emitters.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | callback (function pointer) invoked with (4, handle, buffer) |
| `param_2` | `u32` | handle value written into the event |

**Notes:** The callback call shows three arguments in the decompile; the length argument is not visible. Caller 0c06cb3c.

- Addresses by version: 219: 0x0C06C710
- Called by: `ble_219_0c06cb3c`
- Calls: `co_write16_le`, `ble_hook_invoke4`
- Confidence: medium

## ll_link_emit_event_7d

**Emit vendor event 0x7D (23 bytes) with a sub-code and link parameters**

Builds an H4 event with code 0x7D and parameter length 21: byte 2 is the sub-code param_2, byte 3 the record byte at +0x2C, bytes 4..9 the byte-reversed peer address at +0x26, byte 12 bit 15 of the u16 at +0x22, and u16 values from +0x24, +0x38, +0x06, +0x30, +0x32 and +0x34 at offsets 10, 13, 15, 17, 19 and 21. The 23-byte event goes through ble_hook_invoke4(4, 1, ...) and to the record callback at +0x08. Group: vendor H4 event emitters.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | link record |
| `param_2` | `u8` | sub-code at event offset 2 |

**Notes:** Event code 0x7D is an inference from the layout. Callers 0c06cdb8, 0c06dc56.

- Addresses by version: 219: 0x0C06C684
- Called by: `ble_219_0c06cdb8`, `ble_219_0c06dc56`
- Calls: `co_write16_le`, `co_reverse_copy_6`, `ble_hook_invoke4`
- Confidence: medium

## ll_link_emit_event_code_handle

**Send a 4-byte H4 event whose code is param_2 and whose parameter is the record id**

Builds [code = param_2][length 2][u16 record id at +0x06, little-endian], passes it to ble_hook_invoke4(4, 1, ...) and then to the record callback at +0x08 with (4, id, buffer, 4). It is the generic single-handle notifier for link events. Group: vendor H4 event emitters.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | link record (id at +0x06, callback at +0x08) |
| `param_2` | `u8` | H4 event code |

**Notes:** The decompiled hook and callback calls show three arguments; length 4 is taken from the built buffer (2 + 2). Callers 0c06cb3c, 0c06cdb8, 0c06d9b0, 0c06dc56, 0c06ebec.

- Addresses by version: 219: 0x0C06C648
- Called by: `ble_219_0c06cb3c`, `ble_219_0c06cdb8`, `ble_219_0c06d9b0`, `ble_219_0c06dc56`, `ble_219_0c06ebec`
- Calls: `co_write16_le`, `ble_hook_invoke4`
- Confidence: medium

## ll_link_get_byte_1cb_by_key

**Return the byte at +0x1CB of a link record found by key when two flags are set**

Finds the link record in the env+0x14 list whose u16 key at +0x0A equals param_1. It returns the byte at +0x1CB only when the flag byte at +0x1C0 and the byte at +0x1C1 are both non-zero; otherwise it returns 0, including when no record matches. Read-only. Group: link-record accessors by key (ll_link_*_by_key).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | record key (+0x0A) to match |

**Returns** `u8`: byte at +0x1CB, or 0

**Notes:** Field meaning at +0x1CB is unknown. Callers 0c04e398, 0c06dc56.

- Addresses by version: 219: 0x0C06BC24
- Called by: `ble_219_0c04e398`, `ble_219_0c06dc56`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: medium

## ll_link_get_ext_byte_by_key

**Look up a link record by key and return one of its status bytes**

Walks the link list at controller env +0x14 (head via DAT_200190D0) and returns the first record whose u16 key at +0x0A equals param_1, or 0 when none matches. Which byte is returned depends on the record's class byte at +0x0C: for class below 4 it returns the byte at +0x1C3 when the flag byte at +0x1C0 is non-zero (else 0); for class 4 or more it returns the byte at +0x16 when bit 0x2000 of the u16 at +0x68 is set (else 0). Read-only. Group: link-record accessors by key (ll_link_*_by_key).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | key to match against the record's u16 at +0x0A (likely a connection handle) |

**Returns** `u16`: selected record byte (0..255), or 0 when not found or not selected

**Notes:** Meaning of the class byte at +0x0C and of fields +0x16, +0x1C0, +0x1C3 and +0x68 is not established; the branch structure comes from the decompile. Callers 0c04e702, 0c06c8f4, 0c06dc56.

- Addresses by version: 219: 0x0C06BADC
- Called by: `ble_219_0c04e702`, `ble_219_0c06c8f4`, `ble_219_0c06dc56`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: medium

## ll_link_get_flag_by_key

**Return a flag from a link record found by key, depending on its class byte**

Finds the link record in the env+0x14 list whose u16 key at +0x0A equals param_1 and returns 0 when there is none. For class byte at +0x0C below 2 it returns 1 when the flag byte at +0x1C0 is set and the byte at +0x1C1 is non-zero, else 0. For larger class values it returns 0 unless (class + 4) truncated to a byte is 0 or 1; then it returns 1 when the u16 at +0x28 is 5 or 8, else 0. Group: link-record accessors by key (ll_link_*_by_key).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | record key (+0x0A) to match |

**Returns** `u32`: 1 or 0

**Notes:** The (class + 4) test makes the class 2..4 branch always return 0 for unsigned classes, so the class field is either signed or the decompiler folded a comparison. Treat the class >= 2 branch as unverified. When state 5 is seen the result is a leftover loop variable that equals 1. Caller 0c04e702, 0c06dc56.

- Addresses by version: 219: 0x0C06BB3C
- Called by: `ble_219_0c04e702`, `ble_219_0c06dc56`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: medium

## ll_link_get_level

**Classify a link/device record into level 0..4**

Returns 0 if param_1 is NULL. Otherwise requires (u16 at +0x68 & 0x3000) == 0x3000 and byte +0x16 >= byte at DAT_200190d0+0x52 (a configured threshold), else 0. Then switches on the s16 at +0x28: value 5 -> 3; value 8 -> 3 if byte +0x16 < 0x10 else 4; value 0 -> 3; any other value -> 2. Result is a small ranking (0 = not eligible, 2..4 = tiers). Callers 0c068da8 and 0c06b374 use it as a selection/priority criterion.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | link/connection record, may be NULL |

**Returns** `u32`: 0 = not eligible, 2, 3 or 4

**Notes:** Semantics of the +0x16/+0x28/+0x68 fields are unknown; this is a structural description only.

- Addresses by version: 219: 0x0C065FBC
- Called by: `ble_219_0c068da8`, `ble_219_0c06b374`
- Confidence: low

## ll_link_notify_event_72

**Send a 16-byte vendor event 0x72 with link parameters to the hook and the link callback**

Builds an H4 event: code 0x72, parameter length 14, the 6-byte peer address at record +0x26 (byte-reversed) at offset 2, and four u16 values from +0x24, +0x38, the record id at +0x06 and +0x30 at offsets 8, 10, 12 and 14. It is passed to ble_hook_invoke4 with (4, 1, buffer, 16), then to the record callback at +0x08 with (4, id, buffer, 16). Group: vendor H4 event emitters (codes 0x70..0x7D).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | link record: u16 id at +0x06, callback pointer at +0x08, peer address at +0x26 |

**Notes:** Event code and field meanings are inferred from the packet layout only. Callers 0c06c8f4, 0c06dc56.

- Addresses by version: 219: 0x0C06C460
- Called by: `ble_219_0c06c8f4`, `ble_219_0c06dc56`
- Calls: `co_write16_le`, `co_reverse_copy_6`, `ble_hook_invoke4`
- Confidence: medium

## lm_env_defaults_init

**Initialise controller default parameters in two small RAM tables**

Writes constants to an 8-byte table at 0x20003EAC..0x20003EB3 (0xFD, 0, 2, 6, 8, 8, 8, 8) and to a record at 0x2000BE0C..0x2000BE20 (be0c=0x100, be12=4, be15=8, be16=0x0608, be18=0x02060408, be1c=0xFD000002, low byte of be20=0xFD). The repeated values 8, 6 and 0xFD look like default packet-type/length or feature capability limits of a link-manager environment. Called once from 0x0c03e9fc (controller init).

**Notes:** The structure semantics are unknown; the name is a guess based on its init-time role.

- Addresses by version: 219: 0x0C03E4C8
- Called by: `bt_drv_rf_analog_bringup`
- Confidence: low

## lm_get_state_9bit

**Return the low 9 bits of global DAT_20003ec0**

Returns DAT_20003ec0 & 0x1FF as a 16-bit value. The 9-bit mask suggests a Bluetooth-controller counter/index or a clock-offset like field (the BT clock slot counter is 9 bits in some places), but the variable is only read here. Called by 0x0c03c070.

**Returns** `u16`: DAT_20003ec0 masked with 0x1FF

**Notes:** Meaning of DAT_20003ec0 not determined.

- Addresses by version: 219: 0x0C03E480
- Called by: `ble_219_0c03c070`
- Confidence: low

## thumb2_encode_b_w

**Build the 32-bit Thumb-2 B.W (T4) branch instruction from a site address and a target**

Computes offset = (target & ~1) - ((site + 4) & ~1) and encodes it as a wide unconditional branch: first halfword 0xF000 | S<<10 | imm10 in the low 16 bits and second halfword 0x9000 | J1<<13 | J2<<11 | imm11 in the high 16 bits (J1/J2 derived as NOT(I XOR S) from offset bits 23/22). The result can be stored directly as a little-endian 32-bit word at the patch site. Used by 0x0c03cec8 which installs ROM/flash code patches by overwriting a function entry with a branch to a new routine.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | address of the instruction being replaced |
| `param_2` | `u32` | branch destination address |

**Returns** `u32`: 32-bit encoded B.W instruction (first halfword in low 16 bits)

- Addresses by version: 219: 0x0C03CE68
- Called by: `bt_drv_rom_patch_apply_table`
- Confidence: high
