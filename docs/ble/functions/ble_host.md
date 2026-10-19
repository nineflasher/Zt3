# BLE - `ble_host` functions

191 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`ad_iterator_get_data`](#ad_iterator_get_data) | 0x0C0645E0 | Pointer to the current AD element's payload |
| [`ad_iterator_get_data_len`](#ad_iterator_get_data_len) | 0x0C0645C8 | Length of the current AD element's data (excluding type) |
| [`ad_iterator_get_data_type`](#ad_iterator_get_data_type) | 0x0C0645D4 | AD type of the current element |
| [`ad_iterator_has_more`](#ad_iterator_has_more) | 0x0C064598 | Check whether a valid AD element remains at the current offset |
| [`ad_iterator_init`](#ad_iterator_init) | 0x0C06458C | Initialise an advertising-data (AD structure) iterator |
| [`ad_iterator_next`](#ad_iterator_next) | 0x0C0645B8 | Advance the AD iterator to the next element |
| [`att_clear_transaction_queue`](#att_clear_transaction_queue) | 0x0C04CE30 | Tell the application to cancel any pending ATT prepared-write transaction |
| [`att_copy_value`](#att_copy_value) | 0x0C04CCD4 | BTstack att_db.c: copy a static attribute value or fetch a dynamic one via att_read_callback |
| [`att_event_forward_class4`](#att_event_forward_class4) | 0x0C04DEF0 | Forward an ATT server event to the hook dispatcher under hook class 4 |
| [`att_is_persistent_ccc`](#att_is_persistent_ccc) | 0x0C04DD40 | BTstack att_db.c: is this handle a Client Characteristic Configuration (UUID 0x2902) attribute |
| [`att_iterator_fetch_next`](#att_iterator_fetch_next) | 0x0C04CC74 | BTstack att_db.c: decode the attribute at it->att_ptr into the iterator and advance |
| [`att_iterator_match_uuid`](#att_iterator_match_uuid) | 0x0C04CD74 | BTstack att_db.c: match the iterator's attribute UUID against a 2- or 16-byte UUID |
| [`att_iterator_match_uuid16`](#att_iterator_match_uuid16) | 0x0C04CD24 | BTstack att_db.c: does the iterator's attribute UUID equal a given 16-bit UUID |
| [`att_prepare_handle_value_indication`](#att_prepare_handle_value_indication) | 0x0C04CE84 | BTstack att_db.c: build an ATT Handle Value Indication (0x1D) PDU |
| [`att_prepare_handle_value_notification`](#att_prepare_handle_value_notification) | 0x0C04CE50 | BTstack att_db.c: build an ATT Handle Value Notification (0x1B) PDU |
| [`att_server_handle_request`](#att_server_handle_request) | 0x0C04CEB8 | Decode one ATT request PDU and build its response (MTU, discovery, read, write) |
| [`att_server_init`](#att_server_init) | 0x0C04EB24 | Initialise the ATT server: GATT database, read and write callbacks, hook and event subscriptions |
| [`att_server_register_packet_handler`](#att_server_register_packet_handler) | 0x0C04EB80 | Store a handler pointer in the global at 0x2000fce4 |
| [`att_server_write_callback`](#att_server_write_callback) | 0x0C04DFB8 | ATT write callback: persist CCC bonds, broadcast commit/cancel, dispatch to attribute handlers |
| [`att_set_db`](#att_set_db) | 0x0C04CDF0 | BTstack att_db.c: install the compiled GATT database after checking its version byte |
| [`att_set_read_callback`](#att_set_read_callback) | 0x0C04CE18 | Register the ATT attribute read callback |
| [`att_validate_security`](#att_validate_security) | 0x0C04CBB4 | Check whether a connection's security level satisfies an ATT attribute's permissions |
| [`bd_addr_cmp`](#bd_addr_cmp) | 0x0C065B24 | Compare two 6-byte Bluetooth device addresses |
| [`bd_addr_copy`](#bd_addr_copy) | 0x0C065B2C | Copy a 6-byte Bluetooth device address |
| [`ble_ctrl_addr_string_slot_store`](#ble_ctrl_addr_string_slot_store) | 0x0C065D1C | Write a BD_ADDR as 'XX:XX:XX:XX:XX:XX' into every all-zero 17-byte slot |
| [`ble_evt_publish`](#ble_evt_publish) | 0x0C04F380 | Publish a link frame: call hook class 4, then every subscriber callback |
| [`ble_evt_source_init`](#ble_evt_source_init) | 0x0C059134 | Register the BLE event run-loop data source and its 16-byte ring buffer |
| [`ble_evt_subscribe`](#ble_evt_subscribe) | 0x0C052B2C | Add a subscriber node to the BLE event list at 0x2000FE9C |
| [`ble_gatt_read_char_value`](#ble_gatt_read_char_value) | 0x0C05ADA4 | Build a GATT characteristic value by selector and copy it out with offset and length |
| [`ble_host_5min_timer_ctrl`](#ble_host_5min_timer_ctrl) | 0x0C05CC70 | Arm or stop the 300-second BLE host timer and set its flag |
| [`ble_host_ctx_clear_2608`](#ble_host_ctx_clear_2608) | 0x0C05481C | Zero the 0x574-byte host state block at 0x20012608 |
| [`ble_host_ctx_reset_b88`](#ble_host_ctx_reset_b88) | 0x0C055570 | Clear the state byte at 0x20012B88 and the 0x80-byte block at 0x20012B8C |
| [`ble_host_env_read_1d8`](#ble_host_env_read_1d8) | 0x0C052DD4 | Return the u32 at +0x1D8 of the BLE host environment, or 0xFFFFFFFF if absent |
| [`ble_host_load_arg_pair`](#ble_host_load_arg_pair) | 0x0C065B0C | Read back the two values saved by ble_host_store_arg_pair |
| [`ble_host_op_allowed`](#ble_host_op_allowed) | 0x0C052E28 | Report whether the BLE host state gate allows starting a new operation |
| [`ble_host_store_arg_pair`](#ble_host_store_arg_pair) | 0x0C065AF8 | Save two values into globals 0x200190b8/0x200190b4 |
| [`ble_host_timer_arm_30s`](#ble_host_timer_arm_30s) | 0x0C04F14C | Re-arm the 30 s run-loop timer at 0x2000FF44 with context param_1 |
| [`ble_host_timer_arm_5min`](#ble_host_timer_arm_5min) | 0x0C0555A8 | Re-arm the 300 s timer at 0x20012C98 and clear the flag byte at 0x20012606 |
| [`ble_host_timer_arm_interval`](#ble_host_timer_arm_interval) | 0x0C0501B0 | Re-arm timer 0x2000FD58 with the interval in DAT_2000FD6C; kick 0x2000FF0C once |
| [`ble_host_timer_cancel_130b0`](#ble_host_timer_cancel_130b0) | 0x0C0573B8 | Remove the run-loop timer source at 0x200130B0 |
| [`ble_host_timer_restart`](#ble_host_timer_restart) | 0x0C059A88 | (Re)arm a BTstack timer source with a new handler and timeout, only when env state byte == 2 |
| [`ble_host_timer_set_enabled`](#ble_host_timer_set_enabled) | 0x0C055524 | Enable or disable the host timer at 0x20012C6C and store the flag at 0x20012B85 |
| [`ble_host_timer_stop_5min`](#ble_host_timer_stop_5min) | 0x0C0555C8 | Remove the 300 s timer source at 0x20012C98 |
| [`ble_host_timers_stop_pair`](#ble_host_timers_stop_pair) | 0x0C0554FC | Remove the two run-loop timer sources at 0x20012C0C and 0x20012C3C |
| [`ble_link_notify_id_addr`](#ble_link_notify_id_addr) | 0x0C04F948 | Send 11-byte frame 0xD6 with the link's identity address type and address |
| [`ble_link_notify_id_flag`](#ble_link_notify_id_flag) | 0x0C04F418 | Send 0xD7 frame with the link's identity address, address type and a flag byte |
| [`ble_link_notify_local`](#ble_link_notify_local) | 0x0C04F584 | Send 11-byte frame 0xD4 with the local address record and the link handle |
| [`ble_link_notify_local_ext`](#ble_link_notify_local_ext) | 0x0C04F3C4 | Send 13-byte frame 0xD5 with the local address record and two extra bytes |
| [`ble_link_notify_pair_addrs`](#ble_link_notify_pair_addrs) | 0x0C04F5CC | Send 20-byte frame with two reversed addresses, a byte, a u16 and a DB index |
| [`ble_link_notify_state`](#ble_link_notify_state) | 0x0C04F4D8 | Send the link state frame (0xC8, 0xC9, 0xCB or 0xCC) selected by byte 0x2000FF5A |
| [`ble_msg_drain_to_host`](#ble_msg_drain_to_host) | 0x0C05AF1C | Drain the inbound 3 KiB ring and pass each message to the upper-layer callback |
| [`ble_msg_enqueue`](#ble_msg_enqueue) | 0x0C05AE14 | Queue a typed message into the 2 KiB outbound ring with lock and filter hooks |
| [`ble_msg_queues_init`](#ble_msg_queues_init) | 0x0C05AD18 | Create the BLE message queues and their run-loop data source |
| [`ble_random_addr_advance`](#ble_random_addr_advance) | 0x0C058170 | Refresh a 6-byte random address field and advance its sequence bytes |
| [`ble_random_bytes_6`](#ble_random_bytes_6) | 0x0C058160 | Fill a 6-byte field with random bytes |
| [`ble_random_static_addr_build`](#ble_random_static_addr_build) | 0x0C0581A8 | Build a random static Bluetooth device address from 6 random bytes |
| [`ble_range_broadcast`](#ble_range_broadcast) | 0x0C04DF64 | Call the default listener, then the +0x10 handler of every range listener |
| [`ble_range_dispatch`](#ble_range_dispatch) | 0x0C04E294 | Call the handler of the range node containing param_2, else the default handler |
| [`ble_range_notify`](#ble_range_notify) | 0x0C04E304 | Send a 7-byte 0xB6 frame to the range listener matching param_3, else the default |
| [`ble_ring_poll_status`](#ble_ring_poll_status) | 0x0C0422D4 | Poll four ring or stream objects of a channel and return a two-bit readiness mask |
| [`ble_sink_init`](#ble_sink_init) | 0x0C04DED8 | Store the sink context pointer and register the class-4 hook handler at 0x0c04de00 |
| [`ble_sink_notify_pair`](#ble_sink_notify_pair) | 0x0C04DF24 | Send a 6-byte 0xB5 frame carrying two u16 values to the sink callback |
| [`bt_bdaddr_is_zero`](#bt_bdaddr_is_zero) | 0x0C05A9C4 | Return true when the 6-byte Bluetooth address is all zeros |
| [`bthost_byte_get_high5_bits`](#bthost_byte_get_high5_bits) | 0x0C04C578 | Return bits 3..7 of the byte pointed to (0 if NULL) |
| [`bthost_byte_get_low3_bits`](#bthost_byte_get_low3_bits) | 0x0C04C570 | Return bits 0..2 of the byte pointed to |
| [`bthost_latch_ctrl_mode_2000fb90`](#bthost_latch_ctrl_mode_2000fb90) | 0x0C04BD0C | Store the controller/host mode byte from ble_ctrl_env_get_mode_or_4 into DAT_2000fb90 |
| [`bthost_link_key_db_tlv_delete_link_key`](#bthost_link_key_db_tlv_delete_link_key) | 0x0C04AC1C | BTstack link-key DB (TLV backend): delete the stored link key for a BD_ADDR |
| [`bthost_link_key_db_tlv_get_instance`](#bthost_link_key_db_tlv_get_instance) | 0x0C04ADE0 | Register the TLV implementation/context and return the link-key DB vtable |
| [`bthost_link_key_db_tlv_get_link_key`](#bthost_link_key_db_tlv_get_link_key) | 0x0C04AC70 | BTstack link-key DB (TLV backend): look up the link key and type for a BD_ADDR |
| [`bthost_link_key_db_tlv_iterator_get_next`](#bthost_link_key_db_tlv_iterator_get_next) | 0x0C04AB90 | Link-key DB iterator: fetch the next stored link key from TLV storage |
| [`bthost_link_key_db_tlv_put_link_key`](#bthost_link_key_db_tlv_put_link_key) | 0x0C04ACE4 | BTstack link-key DB (TLV backend): store a link key, reusing the matching, an empty or the oldest slot |
| [`bthost_set_var_2000fa00`](#bthost_set_var_2000fa00) | 0x0C04BBCC | Store a 32-bit value (probably a callback) in the global at 0x2000fa00 |
| [`bthost_stub_nop_0c04aef8`](#bthost_stub_nop_0c04aef8) | 0x0C04AEF8 | Empty function (immediate return) |
| [`bthost_stub_nop_0c04aefc`](#bthost_stub_nop_0c04aefc) | 0x0C04AEFC | Empty function (immediate return) |
| [`bthost_stub_return_minus1_0c04aef0`](#bthost_stub_return_minus1_0c04aef0) | 0x0C04AEF0 | Stub returning -1 |
| [`bthost_tlv_get_instance`](#bthost_tlv_get_instance) | 0x0C048F34 | Return the pointer to the flash TLV storage vtable |
| [`btstack_hid_get_report_size_for_id`](#btstack_hid_get_report_size_for_id) | 0x0C065288 | Compute the byte size of a HID report from the report descriptor |
| [`btstack_hid_parse_descriptor_item`](#btstack_hid_parse_descriptor_item) | 0x0C065190 | Parse one HID report-descriptor item (short or long) |
| [`btstack_hid_report_id_declared`](#btstack_hid_report_id_declared) | 0x0C0653A0 | Check whether a HID report descriptor contains a Report ID item |
| [`btstack_linked_list_add`](#btstack_linked_list_add) | 0x0C0653EC | Push an item on the head of a linked list unless already present |
| [`btstack_linked_list_add_tail`](#btstack_linked_list_add_tail) | 0x0C065410 | Append an item to the end of a linked list (thunk to the implementation) |
| [`btstack_linked_list_add_tail_impl`](#btstack_linked_list_add_tail_impl) | 0x0C065416 | Append an item at the tail of a linked list unless already present |
| [`btstack_linked_list_empty`](#btstack_linked_list_empty) | 0x0C0653E0 | Test whether a BTstack singly linked list is empty |
| [`btstack_linked_list_get_first_item`](#btstack_linked_list_get_first_item) | 0x0C065450 | Return the first item of a linked list |
| [`btstack_linked_list_iterator_has_next`](#btstack_linked_list_iterator_has_next) | 0x0C06546C | Check whether the linked list iterator has another item |
| [`btstack_linked_list_iterator_init`](#btstack_linked_list_iterator_init) | 0x0C065460 | Initialise a removal-safe linked list iterator |
| [`btstack_linked_list_iterator_next`](#btstack_linked_list_iterator_next) | 0x0C065490 | Return the next item from a linked list iterator |
| [`btstack_linked_list_iterator_remove`](#btstack_linked_list_iterator_remove) | 0x0C0654B4 | Unlink the iterator's current item from its list |
| [`btstack_linked_list_pop`](#btstack_linked_list_pop) | 0x0C065454 | Remove and return the first item of a linked list |
| [`btstack_linked_list_remove`](#btstack_linked_list_remove) | 0x0C06542C | Unlink an item from a singly linked list |
| [`btstack_memory_free_list_push`](#btstack_memory_free_list_push) | 0x0C065558 | Push a freed block onto the global free list at 0x20019088 |
| [`btstack_memory_hci_connection_free`](#btstack_memory_hci_connection_free) | 0x0C0654E4 | Return an hci_connection_t block to its pool free list |
| [`btstack_memory_hci_connection_get`](#btstack_memory_hci_connection_get) | 0x0C0654C4 | Allocate and zero an hci_connection_t from the 3-entry 800-byte pool |
| [`btstack_memory_l2cap_channel_free`](#btstack_memory_l2cap_channel_free) | 0x0C065528 | Return an l2cap_channel_t block to its pool free list |
| [`btstack_memory_l2cap_channel_get`](#btstack_memory_l2cap_channel_get) | 0x0C06550C | Allocate and zero an l2cap_channel_t from the 8-entry 92-byte pool |
| [`btstack_memory_l2cap_service_get`](#btstack_memory_l2cap_service_get) | 0x0C0654F0 | Allocate and zero an l2cap_service_t from the 8-entry 16-byte pool |
| [`btstack_memory_pool_create`](#btstack_memory_pool_create) | 0x0C0656B0 | Build a free list from a contiguous array of fixed-size blocks |
| [`btstack_memory_pool_get`](#btstack_memory_pool_get) | 0x0C0656EC | Pop a block from a memory pool free list |
| [`btstack_memory_service_record_item_get`](#btstack_memory_service_record_item_get) | 0x0C065534 | Allocate and zero a 12-byte SDP service_record_item_t from its 8-entry pool |
| [`btstack_memory_sm_lookup_entry_free`](#btstack_memory_sm_lookup_entry_free) | 0x0C06554C | Return a 12-byte block to the 6-entry pool at 0x2001903c (SM address-resolution entries) |
| [`btstack_ring_buffer_bytes_available`](#btstack_ring_buffer_bytes_available) | 0x0C065728 | Number of bytes stored in a ring buffer |
| [`btstack_ring_buffer_bytes_free`](#btstack_ring_buffer_bytes_free) | 0x0C065768 | Free space in a ring buffer |
| [`btstack_ring_buffer_empty`](#btstack_ring_buffer_empty) | 0x0C065744 | Test whether a ring buffer is empty |
| [`btstack_ring_buffer_init`](#btstack_ring_buffer_init) | 0x0C06570C | Initialise a BTstack ring buffer |
| [`btstack_ring_buffer_read`](#btstack_ring_buffer_read) | 0x0C06580C | Read up to length bytes from a BTstack ring buffer and report the count |
| [`btstack_ring_buffer_reset`](#btstack_ring_buffer_reset) | 0x0C06571C | Reset a ring buffer to empty |
| [`btstack_ring_buffer_write`](#btstack_ring_buffer_write) | 0x0C065784 | Append bytes to a BTstack ring buffer, failing with 7 when they do not fit |
| [`btstack_run_loop_add_data_source`](#btstack_run_loop_add_data_source) | 0x0C065A70 | Dispatch add_data_source via the active run loop |
| [`btstack_run_loop_add_timer`](#btstack_run_loop_add_timer) | 0x0C065AAC | Dispatch add_timer via the active run loop |
| [`btstack_run_loop_dump_timer`](#btstack_run_loop_dump_timer) | 0x0C065AD4 | Dispatch dump_timer via the active run loop |
| [`btstack_run_loop_embedded_add_timer`](#btstack_run_loop_embedded_add_timer) | 0x0C065908 | Insert a timer into the run loop timer list sorted by expiry time |
| [`btstack_run_loop_embedded_dump_timer`](#btstack_run_loop_embedded_dump_timer) | 0x0C0659B0 | Log every pending run loop timer with its index and expiry time |
| [`btstack_run_loop_embedded_init`](#btstack_run_loop_embedded_init) | 0x0C065884 | Reset the embedded run loop lists |
| [`btstack_run_loop_embedded_next_timer_delay_ms`](#btstack_run_loop_embedded_next_timer_delay_ms) | 0x0C065A0C | Milliseconds until the earliest run loop timer expires (-1 if none) |
| [`btstack_run_loop_embedded_poll_data_sources`](#btstack_run_loop_embedded_poll_data_sources) | 0x0C065A2C | Call process() of every data source that has POLL enabled |
| [`btstack_run_loop_embedded_process_timers`](#btstack_run_loop_embedded_process_timers) | 0x0C06595C | Fire every expired timer at the head of the run loop timer list |
| [`btstack_run_loop_embedded_remove_all_timers`](#btstack_run_loop_embedded_remove_all_timers) | 0x0C0658D8 | Unlink every timer from the run loop timer list at 0x200190ac |
| [`btstack_run_loop_enable_data_source_callbacks`](#btstack_run_loop_enable_data_source_callbacks) | 0x0C065A64 | Dispatch enable_data_source_callbacks via the active run loop |
| [`btstack_run_loop_get_time_ms`](#btstack_run_loop_get_time_ms) | 0x0C065AC8 | Dispatch get_time_ms via the active run loop |
| [`btstack_run_loop_get_timer_context`](#btstack_run_loop_get_timer_context) | 0x0C065AA8 | Read the context pointer of a timer source |
| [`btstack_run_loop_init`](#btstack_run_loop_init) | 0x0C065AEC | Select the run loop implementation and initialise it |
| [`btstack_run_loop_remove_data_source`](#btstack_run_loop_remove_data_source) | 0x0C065A7C | Dispatch remove_data_source via the active run loop |
| [`btstack_run_loop_remove_timer`](#btstack_run_loop_remove_timer) | 0x0C065AB8 | Dispatch remove_timer via the active run loop |
| [`btstack_run_loop_remove_timer_thunk`](#btstack_run_loop_remove_timer_thunk) | 0x0C059ABC | Thunk: jump to btstack_run_loop_remove_timer (run-loop vtable slot +0x1c) |
| [`btstack_run_loop_set_data_source_handler`](#btstack_run_loop_set_data_source_handler) | 0x0C065A60 | Set the process callback of a data source |
| [`btstack_run_loop_set_timer`](#btstack_run_loop_set_timer) | 0x0C065A98 | Dispatch set_timer via the active run loop |
| [`btstack_run_loop_set_timer_context`](#btstack_run_loop_set_timer_context) | 0x0C065AA4 | Store a context pointer in a timer source |
| [`btstack_run_loop_set_timer_handler`](#btstack_run_loop_set_timer_handler) | 0x0C065A5C | Set the callback of a timer source |
| [`de_add_data`](#de_add_data) | 0x0C04CAB8 | BTstack sdp_util.c: append a variable-length element (string/UUID128/etc.) to a DE sequence |
| [`de_add_number`](#de_add_number) | 0x0C04CA50 | BTstack sdp_util.c: append a fixed-size numeric element (8/16/32-bit) to a DE sequence |
| [`de_create_sequence`](#de_create_sequence) | 0x0C04C9F4 | BTstack sdp_util.c: start an empty DE_DES sequence with a 16-bit length field |
| [`de_get_data_size`](#de_get_data_size) | 0x0C04C580 | BTstack sdp_util.c: payload size of an SDP data element from its descriptor byte |
| [`de_get_len`](#de_get_len) | 0x0C04C5B8 | BTstack sdp_util.c: total length (header + data) of an SDP data element |
| [`de_get_len_safe`](#de_get_len_safe) | 0x0C04C8DC | BTstack sdp_util.c: element length bounded by the available buffer size, 0 if it does not fit |
| [`de_get_normalized_uuid`](#de_get_normalized_uuid) | 0x0C04C914 | BTstack sdp_util.c: convert a DE_UUID element (16/32/128-bit) into a 128-bit UUID |
| [`de_pop_sequence`](#de_pop_sequence) | 0x0C04CA28 | BTstack sdp_util.c: close a nested sequence by adding its length to the parent's length field |
| [`de_push_sequence`](#de_push_sequence) | 0x0C04CA00 | BTstack sdp_util.c: open a nested DE_DES inside a sequence and return its header pointer |
| [`de_store_descriptor_with_len`](#de_store_descriptor_with_len) | 0x0C04C9CC | BTstack sdp_util.c: write a DE header byte plus its 8/16/32-bit length field |
| [`de_traverse_sequence`](#de_traverse_sequence) | 0x0C04C620 | BTstack sdp_util.c: call a handler for every element of a DE sequence (DE_DES) |
| [`hal_time_ms`](#hal_time_ms) | 0x0C045494 | BTstack run-loop port: current time in milliseconds derived from the FreeRTOS tick count |
| [`hci_add_event_handler`](#hci_add_event_handler) | 0x0C066DBC | Register a packet handler on the event-handler list at env+0x20 |
| [`hci_cmd_pack_format`](#hci_cmd_pack_format) | 0x0C06BC74 | Pack an HCI command payload from a per-opcode format string and argument words |
| [`hci_emit_event`](#hci_emit_event) | 0x0C066004 | Deliver an internal HCI event buffer to every registered event handler |
| [`hci_number_free_acl_slots`](#hci_number_free_acl_slots) | 0x0C0666E4 | Return free ACL packet slots for an address-type class |
| [`hci_power_control_on`](#hci_power_control_on) | 0x0C0661E8 | Power the controller on, run HCI_INIT, and emit event 0x62 when it fails |
| [`hci_release_packet_buffer_thunk`](#hci_release_packet_buffer_thunk) | 0x0C06D5D8 | Thunk: jump to ll_env_clear_flag_170 to release the HCI packet buffer flag |
| [`hci_remove_event_handler`](#hci_remove_event_handler) | 0x0C066DCC | Unregister a packet handler from the event-handler list at env+0x20 |
| [`hci_reserve_packet_buffer`](#hci_reserve_packet_buffer) | 0x0C066BE8 | Reserve the single outgoing packet buffer by setting env+0x170 |
| [`hci_reserve_packet_buffer_thunk`](#hci_reserve_packet_buffer_thunk) | 0x0C06D5D4 | Thunk: jump to the HCI packet-buffer reserve routine at 0x0C066BE8 |
| [`hci_stream_buffer_is_empty`](#hci_stream_buffer_is_empty) | 0x0C045534 | Return true when the 5 KB HCI stream buffer holds no bytes |
| [`hci_stream_buffer_receive_nowait`](#hci_stream_buffer_receive_nowait) | 0x0C045518 | Non-blocking read of up to N bytes from the global HCI stream buffer DAT_2000F2B0 |
| [`hci_transport_h4_rx_advance`](#hci_transport_h4_rx_advance) | 0x0C06C2E0 | Advance the H4 UART receive state machine by the bytes just received |
| [`hid_report_id_status`](#hid_report_id_status) | 0x0C04AF00 | BTstack hid_device.c: classify a HID report ID as VALID (1), INVALID (2) or UNDECLARED (0) |
| [`hid_report_size_valid_body`](#hid_report_size_valid_body) | 0x0C04AF5A | BTstack hid_report_size_valid body (entered after the size!=0 check at 0x0C04AF54) |
| [`l2cap_channel_emit_event_70`](#l2cap_channel_emit_event_70) | 0x0C06C5AC | Emit vendor event 0x70 (26 bytes) describing an L2CAP channel with a sub-code |
| [`l2cap_channel_get_u16_34_by_cid`](#l2cap_channel_get_u16_34_by_cid) | 0x0C06EC54 | Return the u16 at +0x34 of the L2CAP channel with a given local CID |
| [`l2cap_channel_set_context_by_cid`](#l2cap_channel_set_context_by_cid) | 0x0C06F03C | Store a context pointer in the L2CAP channel with a given CID (CIDs 0..0x3F) |
| [`l2cap_channel_timer_teardown`](#l2cap_channel_timer_teardown) | 0x0C06C74C | Timer callback: tear down the L2CAP channel that owns the expired timer |
| [`l2cap_channels_teardown_by_addr`](#l2cap_channels_teardown_by_addr) | 0x0C06C83C | Tear down all L2CAP channels to a peer address, emitting event 0x70 with a code |
| [`l2cap_coc_rx_segment`](#l2cap_coc_rx_segment) | 0x0C06C964 | Consume an LE credit and reassemble one L2CAP credit-based SDU segment |
| [`l2cap_create_channel_entry`](#l2cap_create_channel_entry) | 0x0C06CD00 | Allocate an L2CAP channel from the pool, set its fields and pick a free local CID |
| [`l2cap_register_service`](#l2cap_register_service) | 0x0C06F078 | Register an L2CAP service (PSM, MTU, security) and refresh the env security level |
| [`l2cap_signaling_pdu_build`](#l2cap_signaling_pdu_build) | 0x0C06F12C | Build an L2CAP signalling command PDU from a per-code format string |
| [`le_device_db_tlv_add`](#le_device_db_tlv_add) | 0x0C04ED28 | Insert or update an LE device DB entry (identity address and IRK) in TLV storage |
| [`le_device_db_tlv_check_init`](#le_device_db_tlv_check_init) | 0x0C04ECC0 | Log an error when the LE device DB TLV backend has not been installed |
| [`le_device_db_tlv_configure`](#le_device_db_tlv_configure) | 0x0C04F034 | Install TLV backend and probe which of the 4 device DB slots are populated |
| [`le_device_db_tlv_get_entry`](#le_device_db_tlv_get_entry) | 0x0C04EF9C | Read one 60-byte LE device DB record from TLV storage and unpack its fields |
| [`le_device_db_tlv_init`](#le_device_db_tlv_init) | 0x0C04ECE0 | Empty initialiser of the LE device DB (TLV backed) |
| [`le_device_db_tlv_max_count`](#le_device_db_tlv_max_count) | 0x0C04ECE4 | Return the maximum number of LE device DB entries (4) |
| [`le_device_db_tlv_read_identity`](#le_device_db_tlv_read_identity) | 0x0C04EE74 | Read DB slot N's identity fields: address type, 6-byte address and IRK |
| [`le_device_db_tlv_remove`](#le_device_db_tlv_remove) | 0x0C04ECE8 | Delete LE device DB entry N and its TLV tag |
| [`le_device_db_tlv_remove_by_addr`](#le_device_db_tlv_remove_by_addr) | 0x0C052E70 | Delete the DB entry whose address type and 6-byte address match |
| [`le_device_db_tlv_set_encryption`](#le_device_db_tlv_set_encryption) | 0x0C04EEEC | Overwrite the LTK, EDIV, Rand and key flags of DB slot N in its TLV record |
| [`sdp_attribute_add_length`](#sdp_attribute_add_length) | 0x0C04C89C | Per-attribute callback: add 3 + value length to the running attribute-list size |
| [`sdp_attribute_list_traverse_sequence`](#sdp_attribute_list_traverse_sequence) | 0x0C04C6FC | BTstack sdp_util.c: walk an SDP attribute list as (UINT16 attribute id, value) pairs |
| [`sdp_attribute_write_fragment`](#sdp_attribute_write_fragment) | 0x0C04C780 | Per-attribute callback: write one attribute id and value into a byte-budgeted SDP response |
| [`sdp_get_service_record_handle`](#sdp_get_service_record_handle) | 0x0C04BD98 | Read the 32-bit ServiceRecordHandle (attribute 0x0000) of an SDP record, 0 if absent |
| [`sdp_pattern_uuid_match`](#sdp_pattern_uuid_match) | 0x0C04C680 | Per-UUID callback for a ServiceSearchPattern: fail unless the record contains the UUID |
| [`sdp_record_attribute_list_length`](#sdp_record_attribute_list_length) | 0x0C04CB48 | Total encoded size of the requested attributes of an SDP record |
| [`sdp_record_find_attribute`](#sdp_record_find_attribute) | 0x0C04CB6C | Find an SDP record attribute by 16-bit id and return a pointer to its value element |
| [`sdp_record_matches_pattern`](#sdp_record_matches_pattern) | 0x0C04CB90 | Return true when an SDP record contains every UUID of a ServiceSearchPattern |
| [`sdp_record_write_attribute_list`](#sdp_record_write_attribute_list) | 0x0C04CB10 | Serialize the requested attributes of an SDP record into a byte-budgeted, resumable buffer |
| [`sdp_register_service`](#sdp_register_service) | 0x0C04BDC8 | Register an SDP service record: validate its handle, reject duplicates, link it into the list |
| [`sdp_server_build_service_attribute_response`](#sdp_server_build_service_attribute_response) | 0x0C04BFD0 | Answer an SDP ServiceAttributeRequest for one record handle and an attribute id list |
| [`sdp_server_build_service_search_attribute_response`](#sdp_server_build_service_search_attribute_response) | 0x0C04C144 | Answer an SDP ServiceSearchAttributeRequest with attribute lists for all matching records |
| [`sdp_server_build_service_search_response`](#sdp_server_build_service_search_response) | 0x0C04BE10 | Answer an SDP ServiceSearchRequest with the matching record handles |
| [`sm_device_db_resolve_peer`](#sm_device_db_resolve_peer) | 0x0C04F634 | Match a peer against the LE device DB by address and IRK and report its slot |
| [`sm_init`](#sm_init) | 0x0C052B50 | One-time SM initialisation: run-loop timer, event handlers, default constants, key tables |
| [`sm_link_poll_state`](#sm_link_poll_state) | 0x0C052C7C | Periodic SM poll for the current connection: re-check its identity record and re-arm the timer |
| [`sm_pairing_step_complete`](#sm_pairing_step_complete) | 0x0C050700 | Advance the per-link pairing state machine when one pairing or encryption step completes |
| [`uuid_add_bluetooth_prefix`](#uuid_add_bluetooth_prefix) | 0x0C065CE4 | Expand a 32-bit UUID into a 128-bit Bluetooth Base UUID |

## ad_iterator_get_data

**Pointer to the current AD element's payload**

Returns data + offset + 2, i.e. the address after the length and type bytes. BTstack ad_iterator_get_data.

| Parameter | Type | Description |
|---|---|---|
| `context` | `ptr` | BTstack ad_context_t { u8 *data; u8 offset; u8 length; } |

**Returns** `ptr`: pointer to AD payload

- Addresses by version: 219: 0x0C0645E0
- Called by: `ble_219_0c067248`, `ble_219_0c068da8`
- Confidence: high

## ad_iterator_get_data_len

**Length of the current AD element's data (excluding type)**

Returns data[offset] - 1: the element length byte minus the one-byte AD type. BTstack ad_iterator_get_data_len.

| Parameter | Type | Description |
|---|---|---|
| `context` | `ptr` | BTstack ad_context_t { u8 *data; u8 offset; u8 length; } |

**Returns** `u8`: payload length in bytes

- Addresses by version: 219: 0x0C0645C8
- Called by: `ble_219_0c067248`, `ble_219_0c068da8`
- Confidence: high

## ad_iterator_get_data_type

**AD type of the current element**

Returns data[offset + 1], the AD type byte (e.g. 0x09 complete local name, 0xFF manufacturer data). BTstack ad_iterator_get_data_type.

| Parameter | Type | Description |
|---|---|---|
| `context` | `ptr` | BTstack ad_context_t { u8 *data; u8 offset; u8 length; } |

**Returns** `u8`: AD type

- Addresses by version: 219: 0x0C0645D4
- Called by: `ble_219_0c067248`, `ble_219_0c068da8`
- Confidence: high

## ad_iterator_has_more

**Check whether a valid AD element remains at the current offset**

Returns true if offset+1 < length, the length byte data[offset] is non-zero and data[offset] + offset + 1 <= length (the element fits inside the buffer). Otherwise false. BTstack ad_iterator_has_more.

| Parameter | Type | Description |
|---|---|---|
| `context` | `ptr` | BTstack ad_context_t { u8 *data; u8 offset; u8 length; } |

**Returns** `bool`: true if another well-formed element is available

- Addresses by version: 219: 0x0C064598
- Called by: `ble_219_0c067248`, `ble_219_0c068da8`
- Confidence: high

## ad_iterator_init

**Initialise an advertising-data (AD structure) iterator**

Stores the data pointer at +0, the total length at +5 and clears the current offset at +4 (BTstack ad_context_t { const uint8_t *data; uint8_t offset; uint8_t length; }). Used to walk the length-type-value elements of an advertising / scan response payload.

| Parameter | Type | Description |
|---|---|---|
| `context` | `ptr` | BTstack ad_context_t to fill |
| `ad_len` | `u8` | total length of the AD data in bytes |
| `ad_data` | `ptr` | AD data buffer |

- Addresses by version: 219: 0x0C06458C
- Called by: `ble_219_0c067248`, `ble_219_0c068da8`
- Confidence: high

## ad_iterator_next

**Advance the AD iterator to the next element**

offset += data[offset] + 1, i.e. skip the length byte and its payload (length + type + data). BTstack ad_iterator_next.

| Parameter | Type | Description |
|---|---|---|
| `context` | `ptr` | BTstack ad_context_t { u8 *data; u8 offset; u8 length; } |

- Addresses by version: 219: 0x0C0645B8
- Called by: `ble_219_0c067248`, `ble_219_0c068da8`
- Confidence: high

## att_clear_transaction_queue

**Tell the application to cancel any pending ATT prepared-write transaction**

Calls the registered ATT write callback DAT_2000fccc as callback(con_handle = *(u16*)param_1, attribute_handle = 0, transaction_mode = 3 (cancel), offset 0, buffer NULL, size 0). param_1 is the att_connection_t whose first field is the connection handle. Called from ble_219_0c04e702 when a connection ends or the prepared-write queue is reset.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr:att_connection` | ATT connection; first u16 is the HCI connection handle |

- Addresses by version: 219: 0x0C04CE30
- Called by: `ble_219_0c04e702`
- Confidence: medium

## att_copy_value

**BTstack att_db.c: copy a static attribute value or fetch a dynamic one via att_read_callback**

If it->flags (u16 at +6) has bit 0x100 (ATT_PROPERTY_DYNAMIC) set, returns att_read_callback(con_handle, it->handle, offset, buffer, buffer_size) through the function pointer DAT_2000fcc8 (installed by att_set_read_callback). Otherwise copies co_min_u32(it->value_len - offset, buffer_size) bytes from it->value (+0x14) to buffer with memcpy and returns that count (16-bit). Caller: the ATT PDU handler ble_219_0c04ceb8 (read / read-blob / read-by-type responses).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | att_iterator_t |
| `param_2` | `u16` | offset into the value |
| `param_3` | `ptr` | destination buffer |
| `param_4` | `u16` | buffer size |
| `param_5` | `u16` | hci_con_handle_t passed to the read callback |

**Returns** `u16`: bytes copied, or the read callback's result

- Addresses by version: 219: 0x0C04CCD4
- Called by: `att_server_handle_request`
- Calls: `co_min_u32`, `memcpy`
- Confidence: high

## att_event_forward_class4

**Forward an ATT server event to the hook dispatcher under hook class 4**

Tail-forwards its arguments to the thunk at 0x0c066a4c (the packet lists the final target as ble_219_0c06d5c4, not described here) with the constant class 4, which is the class used by the BLE hook table (ble_sink_init and ble_evt_publish also use class 4). It discards param_2 and passes param_3 and param_4 on. It has no logic of its own. Callers are the ATT packet entry point ble_219_0c04e398 and ble_219_0c04ebc0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | context pass-through |
| `param_2` | `u32` | discarded; replaced by the class constant 4 |
| `param_3` | `u32` | event payload pass-through |
| `param_4` | `u32` | event payload pass-through (also passed as the fifth argument) |

- Addresses by version: 219: 0x0C04DEF0
- Called by: `ble_219_0c04e398`, `ble_219_0c04ebc0`
- Calls: `ble_219_0c06d5c4`
- Confidence: high

## att_is_persistent_ccc

**BTstack att_db.c: is this handle a Client Characteristic Configuration (UUID 0x2902) attribute**

Keeps a one-entry cache: if DAT_2000fcbc (last handle) == handle, returns DAT_2000fcbe (its UUID16) == 0x2902. Otherwise (handle != 0) it walks the db from DAT_2000fcb8 with att_iterator_fetch_next until the handle is found (false if the db ends first), stores the handle in the cache, and if the attribute has a 128-bit UUID (flags & 0x200) caches UUID 0 and returns false; else caches co_read16_le(uuid) and returns whether it is 0x2902. Caller: the att_server write callback ble_219_0c04dfb8, which persists CCC values written with offset 0 and length 2 to the TLV store under tags 'BTC'+n (0x42544300).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | attribute handle |

**Returns** `bool`: true if the attribute is a CCC descriptor

- Addresses by version: 219: 0x0C04DD40
- Called by: `att_server_write_callback`
- Calls: `att_iterator_fetch_next`, `co_read16_le`
- Confidence: high

## att_iterator_fetch_next

**BTstack att_db.c: decode the attribute at it->att_ptr into the iterator and advance**

att_iterator_t layout: att_ptr +0, size u16 +4, flags u16 +6, handle u16 +8, uuid ptr +0xC, value_len u16 +0x10, value ptr +0x14. Reads size = little-endian u16 at att_ptr; if 0 (end-of-db marker) all fields and att_ptr are cleared. Otherwise flags = u16 at +2, handle = u16 at +4, uuid = att_ptr+6; if flags & 0x200 (ATT_PROPERTY_UUID128) the value starts at +22 with value_len = size-22, else at +8 with size-8; finally att_ptr += size. Callers: the ATT request handler ble_219_0c04ceb8 and att_is_persistent_ccc (ble_219_0c04dd40). Group: att_iterator_match_uuid16/att_iterator_match_uuid, att_copy_value, att_set_db.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | att_iterator_t |

- Addresses by version: 219: 0x0C04CC74
- Called by: `att_server_handle_request`, `att_is_persistent_ccc`
- Calls: `co_read16_le`
- Confidence: high

## att_iterator_match_uuid

**BTstack att_db.c: match the iterator's attribute UUID against a 2- or 16-byte UUID**

Returns 0 when it->handle is 0. uuid_len == 2: delegates to att_iterator_match_uuid16 with the little-endian u16. uuid_len == 16 and the db entry is 128-bit (flags & 0x200): memcmp of 16 bytes. Input 128-bit but db 16-bit: the input must be a Bluetooth Base UUID (12-byte memcmp against the table at 0x0C077590 and bytes 14,15 zero), then its u16 at offset 12 is compared with the db UUID16; a non-base UUID returns 0. Caller: the ATT handler ble_219_0c04ceb8 (find-by-type-value, read-by-type, read-by-group-type).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | att_iterator_t |
| `param_2` | `ptr` | UUID bytes (little-endian) |
| `param_3` | `u16` | UUID length: 2 or 16 |
| `param_4` | `u32` | unused register pass-through |

**Returns** `u32`: 1 on match, 0 otherwise

- Addresses by version: 219: 0x0C04CD74
- Called by: `att_server_handle_request`
- Calls: `att_iterator_match_uuid16`, `co_read16_le`, `memcmp`
- Confidence: high

## att_iterator_match_uuid16

**BTstack att_db.c: does the iterator's attribute UUID equal a given 16-bit UUID**

Returns false when it->handle (+8) is 0. For a 16-bit db UUID (flags +6 without 0x200) it compares little-endian u16 at it->uuid with param_2. For a 128-bit db UUID it first checks is_Bluetooth_Base_UUID: memcmp of 12 bytes against the little-endian Bluetooth Base UUID table at 0x0C077590 (FB 34 9B 5F 80 00 00 80 00 10 00 00) and bytes 14,15 == 0; then the short UUID is the u16 at uuid+12. Callers: att_iterator_match_uuid (ble_219_0c04cd74) and the ATT handler ble_219_0c04ceb8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | att_iterator_t |
| `param_2` | `u16` | UUID16 to match |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | unused register pass-through |

**Returns** `bool`: true if the attribute's UUID is this UUID16

- Addresses by version: 219: 0x0C04CD24
- Called by: `att_iterator_match_uuid`, `att_server_handle_request`
- Calls: `co_read16_le`, `memcmp`
- Confidence: high

## att_prepare_handle_value_indication

**BTstack att_db.c: build an ATT Handle Value Indication (0x1D) PDU**

Identical to att_prepare_handle_value_notification except for opcode byte 0x1D (ATT_HANDLE_VALUE_INDICATION): handle little-endian at +1, value memcpy'd to +3 clipped to mtu-3 (mtu = u16 at att_connection+2), return value_len + 3. Caller: att_server_indicate (ble_219_0c04ec18), which also starts the 30 s indication timeout and returns 0x90 (ATT_HANDLE_VALUE_INDICATION_IN_PROGRESS) if one is pending.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr:att_connection` | att_connection_t (mtu u16 at +2) |
| `param_2` | `u16` | attribute handle |
| `param_3` | `ptr` | value bytes |
| `param_4` | `u16` | value length |
| `param_5` | `ptr` | output PDU buffer |

**Returns** `u16`: PDU length = value_len + 3

- Addresses by version: 219: 0x0C04CE84
- Called by: `ble_219_0c04ec18`
- Calls: `co_write16_le`, `co_min_u32`, `memcpy`
- Confidence: high

## att_prepare_handle_value_notification

**BTstack att_db.c: build an ATT Handle Value Notification (0x1B) PDU**

response_buffer[0] = 0x1B (ATT_HANDLE_VALUE_NOTIFICATION), the attribute handle is stored little-endian at +1, and co_min_u32(value_len, att_connection->mtu - 3) bytes of the value are memcpy'd to +3, where mtu is the u16 at att_connection+2. Returns value_len + 3 (16-bit) - note it returns the requested length, not the clipped one, unlike upstream BTstack. Caller: att_server_notify (ble_219_0c04ebc0), which sends it with l2cap_send_prepared_connectionless on the ATT channel 4.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr:att_connection` | att_connection_t (mtu u16 at +2) |
| `param_2` | `u16` | attribute handle |
| `param_3` | `ptr` | value bytes |
| `param_4` | `u16` | value length |
| `param_5` | `ptr` | output PDU buffer |

**Returns** `u16`: PDU length = value_len + 3

- Addresses by version: 219: 0x0C04CE50
- Called by: `ble_219_0c04ebc0`
- Calls: `co_write16_le`, `co_min_u32`, `memcpy`
- Confidence: high

## att_server_handle_request

**Decode one ATT request PDU and build its response (MTU, discovery, read, write)**

The ATT server request dispatcher: it switches on the request opcode at *param_2 and writes the response PDU into param_4, returning its length or 0 for no response. Exchange MTU (0x02) sets the negotiated MTU to max(23, min(client MTU, server MTU)) in param_1[1]. Find Information (0x04), Find By Type Value (0x06), Read By Type (0x08) and Read By Group Type (0x10) walk the attribute database at 0x2000fcb8 with att_iterator_fetch_next and the UUID matchers, emitting uniform-length entries; group types 0x2800 and 0x2801 drive the grouping. Read (0x0a), Read Blob (0x0c) and Read Multiple (0x0e) check READ permission through att_validate_security and copy values with att_copy_value. Write Request (0x12), Prepare Write (0x16), Execute Write (0x18) and Write Command (0x52) work only on dynamic attributes (flag 0x100) and call the write callback at 0x2000fccc with modes 0 write, 1 prepare, 2 commit, 3 cancel and 4 pre-check; prepared-write state lives at 0x2000fcbc..0x2000fcc4. Any other opcode gets an Error Response with code 0x06 (Request Not Supported).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ATT connection context: [1] negotiated MTU, [2] server MTU, flags |
| `param_2` | `ptr` | request PDU (opcode at +0) |
| `param_3` | `u16` | request length in bytes |
| `param_4` | `ptr` | response PDU buffer |

**Returns** `u32`: response PDU length, 0 when no response is sent

**Notes:** Attribute flag bits used: 0x02 read, 0x04 write without response, 0x08 write, 0x100 dynamic (callback-backed), 0x200 128-bit UUID. Error-code mapping follows the ATT spec; the exact per-branch error codes were not all verified. This function is a dispatcher and is part of the ATT server group with att_server_write_callback.

- Addresses by version: 219: 0x0C04CEB8
- Called by: `ble_219_0c04e398`
- Calls: `att_validate_security`, `att_iterator_fetch_next`, `att_copy_value`, `att_iterator_match_uuid16`, `att_iterator_match_uuid`, `co_read16_le`, `co_write16_le`, `co_min_u32`, `co_max_u32`, `util_nop_stub_a`, `memcmp`, `memcpy`
- Confidence: medium

## att_server_init

**Initialise the ATT server: GATT database, read and write callbacks, hook and event subscriptions**

Called once from ble_219_0c059230. It stores the application context (param_2) at 0x2000fce8 and the application callback (param_3) at 0x2000fcec, registers the class-4 sink with ble_sink_init (0x0c04ded8 with 0x0c04e399), installs the compiled GATT database through att_set_db (0x0c04cdf0), and registers the read callback 0x0c04e295 through att_set_read_callback. It also performs two event subscriptions (calls to 0x0c066dbc and 0x0c052b2c, which the packet names ble_evt_subscribe and hci_add_event_handler). Finally it sets the ATT write callback at 0x2000fccc to att_server_write_callback (0x0c04dfb9). Two hook pointers (0x2000fcf4 and 0x2000fd00) are set to the same handler at 0x0c04e6fc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | compiled GATT attribute database |
| `param_2` | `ptr` | application context stored for callbacks |
| `param_3` | `ptr` | application callback stored at 0x2000fcec |

- Addresses by version: 219: 0x0C04EB24
- Called by: `ble_219_0c059230`
- Calls: `att_set_db`, `att_set_read_callback`, `ble_sink_init`, `ble_evt_subscribe`, `hci_add_event_handler`
- Confidence: medium

## att_server_register_packet_handler

**Store a handler pointer in the global at 0x2000fce4**

Single-global setter: DAT_2000fce4 = param_1, located in the att_server.c variable area right after the att_db variables. Matches BTstack's att_server_register_packet_handler (att_client_packet_handler = handler). Called from ble_219_0c059230 at application init.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | packet handler callback |

- Addresses by version: 219: 0x0C04EB80
- Called by: `ble_219_0c059230`
- Confidence: low

## att_server_write_callback

**ATT write callback: persist CCC bonds, broadcast commit/cancel, dispatch to attribute handlers**

Registered as the ATT write callback (0x2000fccc) by att_server_init, and called with a mode in param_3. Modes 2 (commit) and 3 (cancel) broadcast to every entry of the handler list at 0x2000fcf8 and then to the application callback at 0x2000fcec. Mode 4 (pre-check) does the same but returns the first non-zero status. Modes 0 (write) and 1 (prepare) find the list entry whose handle range covers the attribute handle and call its callback, falling back to the application callback. For a plain 2-byte write to a persistent Client Characteristic Configuration (att_is_persistent_ccc), it also stores the CCC value through the bonding storage callbacks: up to 20 tag slots with keys 0x42544300 plus the slot index ('BTC' plus index), each 8-byte record holding a counter, handle, bond index and tag. Store failures are logged as 'att_server.c:%u: Store tag index %u failed' (lines 0x3b0 and 0x3d1).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | connection context (passed to the handlers as the connection handle) |
| `param_2` | `u16` | attribute handle |
| `param_3` | `u32` | mode: 0 write, 1 prepare, 2 execute/commit, 3 cancel, 4 pre-check |
| `param_4` | `u32` | write offset (0 for a plain write) |
| `param_5` | `ptr` | write data |
| `param_6` | `u16` | data length |

**Returns** `u32`: 0 = accepted, otherwise an ATT error code

**Notes:** The mode meanings are inferred from how att_server_handle_request calls the callback. The 8-byte CCC storage record layout is inferred from the stores and reads, and the storage callback table layout (read, write, delete) is inferred.

- Addresses by version: 219: 0x0C04DFB8
- Calls: `att_is_persistent_ccc`, `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`, `ble_host_load_arg_pair`, `co_read16_le`, `ble_ctrl_conn_find_by_handle`, `ble_hook_invoke_indexed`
- Confidence: medium

## att_set_db

**BTstack att_db.c: install the compiled GATT database after checking its version byte**

Ignores NULL. If db[0] != 1 (ATT_DB_VERSION) it logs 'ATT DB version differs, please regenerate .h from .gatt file or update att_db_util.c' (att_db.c:199) via ble_hook_invoke_indexed(2, ...) and keeps the old db. Otherwise the global att_db pointer DAT_2000fcb8 is set to db+1, i.e. the first attribute record (u16 size, u16 flags, u16 handle, uuid, value ...). Called from att_server_init (ble_219_0c04eb24) with the profile data at 0x20004348.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | GATT database blob starting with the version byte |

- Addresses by version: 219: 0x0C04CDF0
- Called by: `att_server_init`
- Calls: `ble_hook_invoke_indexed`
- Confidence: high

## att_set_read_callback

**Register the ATT attribute read callback**

Stores param_1 in DAT_2000fcc8, the att_read_callback pointer of att_db.c (the write callback lives in the next word, 0x2000fccc). Called from ble_219_0c04eb24 (ATT server init).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | att_read_callback_t function pointer |

- Addresses by version: 219: 0x0C04CE18
- Called by: `att_server_init`
- Confidence: medium

## att_validate_security

**Check whether a connection's security level satisfies an ATT attribute's permissions**

BTstack att_db.c security check. param_3 is the attribute iterator whose flags (u16 at +6) hold the read/write permission bits and, in the top nibble, the required encryption key size (stored as size-1). param_2 selects the operation (1 = write, otherwise read) which decides which flag bits form the required level 0..3 (1 encrypted, 2 authenticated, 3 authorized). param_1 is the att_connection_t: encryption_key_size at +7, authenticated at +8, authorized at +9, and a flag at +10 that switches to a variant of the check. Returns the ATT error code: 0x05 insufficient authentication, 0x08 insufficient authorization, 0x0F insufficient encryption, 0x0C insufficient encryption key size, or 0 when allowed. Called from ble_219_0c04ceb8 (attribute read/write handler).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr:att_connection` | ATT connection state (key size, authenticated, authorized) |
| `param_2` | `u32` | operation: 1 = write, else read |
| `param_3` | `ptr` | ATT attribute iterator; flags u16 at +6 |

**Returns** `u8`: ATT error code, 0 = OK

**Notes:** Bit-level mapping inferred from decompilation against att_db.c; the +10 connection flag is believed to be secure-connection state.

- Addresses by version: 219: 0x0C04CBB4
- Called by: `att_server_handle_request`
- Confidence: medium

## bd_addr_cmp

**Compare two 6-byte Bluetooth device addresses**

Calls newlib memcmp on the first 6 bytes of the two address buffers (length constant 6), using the BTstack name bd_addr_cmp. The decompiled function is typed void and drops the result, but the memcmp result is passed through in r0, so callers test it as an ordering (0 when equal). It is used for BD_ADDR matching; the one caller in this packet is not described yet.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | first 6-byte BD_ADDR |
| `b` | `ptr` | second 6-byte BD_ADDR |

**Returns** `s32`: 0 when the addresses are equal, otherwise the memcmp ordering

**Notes:** Decompiler shows void; the return value is inferred from the tail call.

- Addresses by version: 219: 0x0C065B24
- Called by: `l2cap_channels_teardown_by_addr`
- Calls: `memcmp`
- Confidence: medium

## bd_addr_copy

**Copy a 6-byte Bluetooth device address**

BTstack bd_addr_copy(dest, src): copies a u32 followed by a u16 (offset 4), i.e. 6 bytes, from src to dest. Used by HCI/L2CAP/SM when handling connection addresses.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination bd_addr_t |
| `param_2` | `ptr` | source bd_addr_t |

- Addresses by version: 219: 0x0C065B2C
- Called by: `ble_ctrl_conn_alloc_and_register`, `ble_219_0c068da8`, `l2cap_create_channel_entry`
- Confidence: high

## ble_ctrl_addr_string_slot_store

**Write a BD_ADDR as 'XX:XX:XX:XX:XX:XX' into every all-zero 17-byte slot**

Scans a byte array of param_2 bytes at param_1 with a step of 1 byte. Where a 17-byte slot equals the placeholder '00:00:00:00:00:00' (including the NUL, compared with memcmp), it formats the 6-byte address at param_3 as twelve uppercase hex digits separated by colons into the scratch bytes 0x200190BC..0x200190CC, terminates the string at 0x200190CD and copies it into the slot. Scanning then continues 17 bytes further, so consecutive free slots are all filled, and non-matching bytes advance the scan by one. This looks like a text-form address table (the BThost name at env+0x2C uses the same placeholder layout); the caller is not described in this packet.

| Parameter | Type | Description |
|---|---|---|
| `table` | `ptr` | array of 17-byte ASCII address slots |
| `table_len` | `s32` | length of the table in bytes |
| `addr` | `ptr` | 6-byte BD_ADDR to format |

**Notes:** Uses fixed RAM scratch 0x200190BC..0x200190CD. Purpose of the table is not confirmed.

- Addresses by version: 219: 0x0C065D1C
- Called by: `ble_219_0c067248`, `ble_219_0c0674e8`
- Calls: `memcmp`
- Confidence: medium

## ble_evt_publish

**Publish a link frame: call hook class 4, then every subscriber callback**

Calls ble_hook_invoke4(4, 1, frame, len) so the registered 4-argument hook sees the frame (it may first tick a periodic callback). It then walks the subscriber list at DAT_2000fe9c and calls each node's callback at node+4 as callback(4, 0, frame, len). The ble_link_notify_* frame builders use it for all their output.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | frame buffer; byte 0 is the message type, byte 1 the payload length |
| `param_2` | `u32` | frame length in bytes |

- Addresses by version: 219: 0x0C04F380
- Called by: `ble_link_notify_local_ext`, `ble_link_notify_id_flag`, `ble_link_notify_state`, `ble_link_notify_local`, `ble_link_notify_pair_addrs`, `ble_link_notify_id_addr`, `sm_pairing_step_complete`, `ble_219_0c051eb8`, `ble_219_0c051ef0`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`, `ble_hook_invoke4`
- Confidence: high

## ble_evt_source_init

**Register the BLE event run-loop data source and its 16-byte ring buffer**

Initialises the BTstack run-loop data source at 0x20013238 that drives the BLE event pump. The source is removed from the run loop, given the process handler 0x0C058D14, has its callbacks enabled with flag 1, and is added back. It then initialises a BTstack ring buffer at 0x2001324C over 16 bytes of storage at 0x20013260, and creates a 1-count synchronisation object at 0x20013270 through the RTOS wrapper 0x0C042D80.

**Notes:** Handler 0x0C058D14 and wrapper 0x0C042D80 are not described in this packet. The purpose of the ring (16 bytes) is inferred from its size and placement.

- Addresses by version: 219: 0x0C059134
- Called by: `ble_219_0c0592a4`
- Calls: `prvInitialiseMutex`, `btstack_ring_buffer_init`, `btstack_run_loop_set_data_source_handler`, `btstack_run_loop_enable_data_source_callbacks`, `btstack_run_loop_add_data_source`, `btstack_run_loop_remove_data_source`
- Confidence: high

## ble_evt_subscribe

**Add a subscriber node to the BLE event list at 0x2000FE9C**

Thin wrapper around btstack_linked_list_add_tail(&DAT_2000fe9c, param_1), which appends the node unless it is already linked. Subscribers have their callback at node+4, and ble_evt_publish calls each of them. Caller: ble_219_0c04eb24 (not yet described).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | subscriber node; callback at +4 |

- Addresses by version: 219: 0x0C052B2C
- Called by: `att_server_init`
- Calls: `btstack_linked_list_add_tail`
- Confidence: high

## ble_gatt_read_char_value

**Build a GATT characteristic value by selector and copy it out with offset and length**

Read-value provider for a small set of GATT characteristics. param_1 is matched against four u16 IDs at 0x2000430C..0x20004312; when there is no match, selector 0x4A returns a string held at 0x20015E60 and any other selector returns length 0. For a matched ID, param_2 selects the value: 6 gives u16 4 (length 2); 10 loads the 8-byte NV block 0xFA8 (length 8); 12 writes the ASCII name Segway-Ninebot (length 14); 14 loads the 16-byte device name from NV 0xFA6 and, if it equals KickScooter, substitutes Segway KickScooter (length 18), otherwise uses the stored name; 18 gives the NV flag byte 0xFA7 followed by 7 zero bytes (length 8); 20 gives u32 9; 22 gives the packed word at 0x20012CB0; 24 gives u32 0x10000; 26 gives byte 2; 28 gives the state byte from ble_state_407a_read. The value is then copied with co_min_u32 (length - offset, max length) from offset param_3 into param_4 when param_4 is non-null; if the offset is past the end, 0 is returned. The returned count is the bytes copied, or the total length when param_4 is null.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | attribute or characteristic UUID, matched against four u16 IDs at 0x2000430C |
| `param_2` | `s32` | value selector (switch code, for example 6, 10, 12, 14, 18, 20, 22, 24, 26, 28; 0x4A for string) |
| `param_3` | `u32` | read offset into the value |
| `param_4` | `ptr` | output buffer, or null to query the length |
| `param_5` | `u16` | maximum number of bytes to copy |

**Returns** `u32`: bytes copied, or total value length when param_4 is null; 0 on failure or offset past end

**Notes:** The four IDs at 0x2000430C..0x20004312 are not named in this packet, so the mapping to specific GATT characteristics (for example Device Name) is inferred from the string contents and length.

- Addresses by version: 219: 0x0C05ADA4
- Calls: `ble_get_packed_word_12cb0`, `ble_state_407a_read`, `ble_nv_load_8byte_block`, `ble_nv_load_flag_byte`, `ble_nv_load_device_name`, `co_min_u32`, `memcpy`, `memset`, `strlen`, `strncmp`
- Confidence: medium

## ble_host_5min_timer_ctrl

**Arm or stop the 300-second BLE host timer and set its flag**

Controls the 300-second host timer. Argument 1 calls ble_host_timer_arm_5min, which re-arms the timer at 0x20012C98 and clears the flag byte at 0x20012606. Any other value calls ble_host_timer_stop_5min to remove the timer source, then sets the flag at 0x20012606 through ble_set_flag_12606. Always returns 0.

| Parameter | Type | Description |
|---|---|---|
| `cmd` | `s32` | 1 to arm the 5-minute timer; any other value stops it and sets the flag |

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C05CC70
- Called by: `ble_219_0c02a8f8`
- Calls: `ble_set_flag_12606`, `ble_host_timer_arm_5min`, `ble_host_timer_stop_5min`
- Confidence: medium

## ble_host_ctx_clear_2608

**Zero the 0x574-byte host state block at 0x20012608**

Calls memset(0x20012608, 0, 0x574), clearing 1396 bytes. The block's internal layout is not decoded here. It ends at 0x20012B7C, before the state byte at 0x20012B88 and the blocks cleared by ble_host_ctx_reset_b88.

- Addresses by version: 219: 0x0C05481C
- Called by: `ble_219_0c0537b4`, `ble_219_0c053f24`
- Calls: `memset`
- Confidence: high

## ble_host_ctx_reset_b88

**Clear the state byte at 0x20012B88 and the 0x80-byte block at 0x20012B8C**

Zeroes 0x30 bytes at 0x20012B8C, 0x20 bytes at 0x20012BBC and 0x30 bytes at 0x20012BDC (three adjacent sub-blocks that make up 0x80 bytes), then sets the byte at 0x20012B88 to 0. The block ends at 0x20012C0B, where the timer sources cleared by ble_host_timers_stop_pair begin. The individual fields are not decoded.

- Addresses by version: 219: 0x0C055570
- Called by: `ble_219_0c0537b4`
- Calls: `memset`
- Confidence: high

## ble_host_env_read_1d8

**Return the u32 at +0x1D8 of the BLE host environment, or 0xFFFFFFFF if absent**

Calls the environment accessor at 0x0c066554 (not yet named). If it returns a non-NULL pointer, returns the u32 at offset 0x1D8 of that structure; otherwise returns 0xFFFFFFFF. The meaning of the field is not known.

**Returns** `u32`: field value at +0x1D8, or 0xFFFFFFFF when there is no environment

- Addresses by version: 219: 0x0C052DD4
- Called by: `ble_219_0c04e702`
- Calls: `ble_ctrl_conn_find_by_handle`
- Confidence: medium

## ble_host_load_arg_pair

**Read back the two values saved by ble_host_store_arg_pair**

Writes DAT_200190b8 to *param_1 and DAT_200190b4 to *param_2 (pure getter for the pair set at 0x0c065af8). Called from 0x0c04dfb8 and 0x0c04e702 in the host (HCI) code.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | out: value stored in 0x200190b8 |
| `param_2` | `ptr` | out: value stored in 0x200190b4 |

**Notes:** Meaning of the pair (transport/config?) is not confirmed.

- Addresses by version: 219: 0x0C065B0C
- Called by: `att_server_write_callback`, `ble_219_0c04e702`
- Confidence: low

## ble_host_op_allowed

**Report whether the BLE host state gate allows starting a new operation**

Reads the BLE host environment from 0x0c066554 and returns false when it is missing or the byte at +0x1C0 is set. When the state byte at +0x1BE is 3 it returns false for sub-state 3 (+0x1BD); otherwise it compares the sub-state with 0x1A when the flag at +0x1AC is set, or with 0x29 when it is clear. For any other state it returns true unless the state is 4. The function has no side effects, and the state values are not decoded.

**Returns** `bool`: true when a new operation may start

**Notes:** The name describes the gate only; the state machine it guards is not documented here.

- Addresses by version: 219: 0x0C052E28
- Called by: `ble_219_0c04e398`, `ble_219_0c04e702`
- Calls: `ble_ctrl_conn_find_by_handle`
- Confidence: low

## ble_host_store_arg_pair

**Save two values into globals 0x200190b8/0x200190b4**

Stores param_1 into DAT_200190b8 and param_2 into DAT_200190b4. Called once from stack bring-up 0x0c05b67c next to btstack_run_loop_init; the matching getter is 0x0c065b0c. Likely the transport/config pair given to the HCI init, but the meaning is not confirmed.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | first value, saved in 0x200190b8 |
| `param_2` | `u32` | second value, saved in 0x200190b4 |

**Notes:** Purpose guessed from call placement only.

- Addresses by version: 219: 0x0C065AF8
- Called by: `ble_219_0c05b67c`
- Confidence: low

## ble_host_timer_arm_30s

**Re-arm the 30 s run-loop timer at 0x2000FF44 with context param_1**

Removes the timer source at 0x2000FF44 from the BTstack run loop, sets its context to param_1, its callback to 0x0c052474, its timeout to 30000 ms, and adds it back. The callback and the purpose of the 30 s deadline are not named yet. Caller: ble_219_0c051eb8 (not yet described).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | context stored in the timer source |

- Addresses by version: 219: 0x0C04F14C
- Called by: `ble_219_0c051eb8`
- Calls: `btstack_run_loop_set_timer_handler`, `btstack_run_loop_set_timer`, `btstack_run_loop_set_timer_context`, `btstack_run_loop_add_timer`, `btstack_run_loop_remove_timer`
- Confidence: medium

## ble_host_timer_arm_5min

**Re-arm the 300 s timer at 0x20012C98 and clear the flag byte at 0x20012606**

Calls ble_host_timer_restart on the timer source at 0x20012C98 with timeout 300000 ms and callback 0x0c054b94, then sets DAT_20012606 to 0 (the byte accessed by ble_set_flag_12606 and ble_get_flag_12606). The restart only acts when env+0x198 is 2, as for every ble_host_timer_restart call.

- Addresses by version: 219: 0x0C0555A8
- Called by: `ble_219_0c055b90`, `ble_host_5min_timer_ctrl`
- Calls: `ble_host_timer_restart`
- Confidence: high

## ble_host_timer_arm_interval

**Re-arm timer 0x2000FD58 with the interval in DAT_2000FD6C; kick 0x2000FF0C once**

Sets the callback of the timer source at 0x2000FD58 to 0x0c0500d0 and adds it with timeout DAT_2000fd6c (ms), without removing it first. If the flag DAT_2000fd78 is zero, it sets the flag to 1 and, when DAT_2000feb0 is non-zero, removes and re-adds the timer source at 0x2000FF0C with timeout 0 so that it fires at once. The meaning of the flags and of the callback at 0x0c0500d0 is not decoded.

**Notes:** The timer at 0x2000FD58 is added without a prior remove; if it is still pending when this runs, the run loop may see a double add.

- Addresses by version: 219: 0x0C0501B0
- Called by: `ble_219_0c052de8`
- Calls: `btstack_run_loop_set_timer_handler`, `btstack_run_loop_set_timer`, `btstack_run_loop_add_timer`, `btstack_run_loop_remove_timer`
- Confidence: medium

## ble_host_timer_cancel_130b0

**Remove the run-loop timer source at 0x200130B0**

Calls btstack_run_loop_remove_timer_thunk (0x0c059abc) on the timer source at 0x200130B0. The function has no direct callers in the image (entry point, callback or indirect use only), and its matching start function is not in this packet.

- Addresses by version: 219: 0x0C0573B8
- Calls: `btstack_run_loop_remove_timer_thunk`
- Confidence: high

## ble_host_timer_restart

**(Re)arm a BTstack timer source with a new handler and timeout, only when env state byte == 2**

Common timer helper used by 12+ host/app routines. It first reads the controller environment byte at env+0x198 via ble_ctrl_env_get_u8_at_0x198 and returns without doing anything unless it equals 2 (the stack is up/ready). Otherwise it calls btstack_run_loop_remove_timer(timer) so a pending instance is cancelled, btstack_run_loop_set_timer_handler(timer, handler), btstack_run_loop_set_timer(timer, timeout_ms) and btstack_run_loop_add_timer(timer). Example: ble_app_start_deferred_500ms_op arms the timer at 0x200170dc for 500 ms with it. Pairs with btstack_run_loop_remove_timer_thunk (0c059abc) which stops such a timer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | btstack_timer_source_t to arm |
| `param_2` | `u32` | timeout in milliseconds |
| `param_3` | `ptr` | timer callback (void (*)(btstack_timer_source_t*)) |

**Notes:** The meaning of env+0x198 == 2 is inferred from usage (gate for all timer activity); the byte itself is not yet named.

- Addresses by version: 219: 0x0C059A88
- Called by: `ble_219_0c0287ac`, `ble_219_0c028ad4`, `ble_219_0c028c94`, `ble_219_0c02a35c`, `ble_219_0c02b480`, `ble_219_0c053018`, `ble_219_0c055244`, `ble_host_timer_set_enabled`, `ble_host_timer_arm_5min`, `ble_219_0c057d9c`, `ble_219_0c05806c`, `ble_219_0c0593a4` ...
- Calls: `btstack_run_loop_set_timer_handler`, `btstack_run_loop_set_timer`, `btstack_run_loop_add_timer`, `btstack_run_loop_remove_timer`, `ble_ctrl_env_get_u8_at_0x198`
- Confidence: high

## ble_host_timer_set_enabled

**Enable or disable the host timer at 0x20012C6C and store the flag at 0x20012B85**

For a non-zero argument, re-arms the timer source at 0x20012C6C with the timeout in the global DAT_20003FB0 and the callback 0x0c054e1c through ble_host_timer_restart, which only acts when env+0x198 is 2. For zero, it removes that timer source. Either way the low byte of the argument is stored in DAT_20012B85, which ble_get_byte_12b85 reads.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | non-zero to enable, zero to disable |

- Addresses by version: 219: 0x0C055524
- Called by: `ble_219_0c053018`, `ble_219_0c0537b4`
- Calls: `ble_host_timer_restart`, `btstack_run_loop_remove_timer_thunk`
- Confidence: high

## ble_host_timer_stop_5min

**Remove the 300 s timer source at 0x20012C98**

Calls btstack_run_loop_remove_timer_thunk (0x0c059abc) on the timer source at 0x20012C98. This is the stop side of ble_host_timer_arm_5min.

- Addresses by version: 219: 0x0C0555C8
- Called by: `ble_host_5min_timer_ctrl`
- Calls: `btstack_run_loop_remove_timer_thunk`
- Confidence: high

## ble_host_timers_stop_pair

**Remove the two run-loop timer sources at 0x20012C0C and 0x20012C3C**

Calls btstack_run_loop_remove_timer on the timer sources at 0x20012C0C and 0x20012C3C, through the thunk btstack_run_loop_remove_timer_thunk (0x0c059abc). Nothing else is written. The start side of these timers is not in this packet.

- Addresses by version: 219: 0x0C0554FC
- Called by: `ble_219_0c0537b4`
- Calls: `btstack_run_loop_remove_timer_thunk`
- Confidence: high

## ble_link_notify_id_addr

**Send 11-byte frame 0xD6 with the link's identity address type and address**

Sets the link flag byte at +0x35 to 1, takes the address type and 6-byte address from the link (+7, +8) when its DB index is negative or from DB slot N through le_device_db_tlv_read_identity otherwise, and publishes an 11-byte frame: 0xD6, length 9, u16 handle at [2..3], type at [4], reversed address at [5..10]. Compared with ble_link_notify_id_flag (0xD7) it has no trailing flag byte, and it sets +0x35 to 1 instead of 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | link context (see ble_link_notify_id_flag) |

- Addresses by version: 219: 0x0C04F948
- Called by: `sm_pairing_step_complete`, `ble_219_0c051eb8`, `sm_link_poll_state`
- Calls: `le_device_db_tlv_read_identity`, `ble_evt_publish`, `co_write16_le`, `co_reverse_copy_6`
- Confidence: medium

## ble_link_notify_id_flag

**Send 0xD7 frame with the link's identity address, address type and a flag byte**

Clears the link flag byte at +0x35. If the link's DB index (int at +0x30) is negative it uses the link's own address type (+7) and 6-byte address (+8..+13); otherwise it fetches both from DB slot N through le_device_db_tlv_read_identity. The frame is 0xD7, length 10, u16 handle at [2..3], address type at [4], the address reversed at [5..10], and param_2 at [11], published with ble_evt_publish.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | link context: handle +0, address type +7, address +8, DB index +0x30 (int), flag +0x35 |
| `param_2` | `u8` | flag byte sent as the last payload byte |

**Notes:** The decompiled ble_evt_publish call passes no length; 12 bytes is inferred from the length byte (10) plus 2.

- Addresses by version: 219: 0x0C04F418
- Called by: `ble_219_0c051eb8`, `ble_219_0c051ef0`
- Calls: `le_device_db_tlv_read_identity`, `ble_evt_publish`, `co_write16_le`, `co_reverse_copy_6`
- Confidence: medium

## ble_link_notify_local

**Send 11-byte frame 0xD4 with the local address record and the link handle**

Sets the link flag byte at +0x34 to 1 and publishes an 11-byte frame: 0xD4, length 9, the u16 handle at [2..3], the type byte at 0x20010148 at [4], and the 6-byte address at 0x20010149 reversed at [5..10]. It uses the same global record as ble_link_notify_local_ext.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | link context: handle at +0, flag at +0x34 |

- Addresses by version: 219: 0x0C04F584
- Called by: `sm_pairing_step_complete`, `ble_219_0c051eb8`, `sm_link_poll_state`
- Calls: `ble_evt_publish`, `co_write16_le`, `co_reverse_copy_6`
- Confidence: medium

## ble_link_notify_local_ext

**Send 13-byte frame 0xD5 with the local address record and two extra bytes**

Clears the link flag byte at +0x34 and publishes a 13-byte frame: 0xD5, length 11, the link's u16 handle at [2..3], the 1-byte type at 0x20010148 at [4], the 6-byte address at 0x20010149 copied in reverse order to [5..10], then param_2 at [11] and param_3 at [12]. The frame goes out through ble_evt_publish. The meaning of the 0xD5 type and of the two extra bytes is not decoded.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | link context: u16 handle at +0, flag byte at +0x34 |
| `param_2` | `u8` | extra byte at frame[11] |
| `param_3` | `u8` | extra byte at frame[12] |

- Addresses by version: 219: 0x0C04F3C4
- Called by: `ble_219_0c04fc10`, `ble_219_0c051eb8`, `ble_219_0c051ef0`
- Calls: `ble_evt_publish`, `co_write16_le`, `co_reverse_copy_6`
- Confidence: medium

## ble_link_notify_pair_addrs

**Send 20-byte frame with two reversed addresses, a byte, a u16 and a DB index**

Reads the identity address of DB slot param_5 (le_device_db_tlv_read_identity, address only) and builds a 20-byte frame: [0] = param_1, [1] = 0x12 (length 18), u16 param_2 at [2..3], byte param_3 at [4], the 6-byte address param_4 reversed at [5..10], byte [11] left unwritten, the slot address reversed at [12..17], and u16 param_5 at [18..19]. It is published with ble_evt_publish(frame, 20).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | message type byte, frame[0] |
| `param_2` | `u32` | low 16 bits sent at frame[2..3] |
| `param_3` | `u8` | byte sent at frame[4] |
| `param_4` | `ptr` | 6-byte address, reversed into frame[5..10] |
| `param_5` | `u16` | DB slot index; looked up, and echoed at frame[18..19] |

**Notes:** The roles of the two addresses are inferred from the call pattern.

- Addresses by version: 219: 0x0C04F5CC
- Called by: `sm_device_db_resolve_peer`, `sm_pairing_step_complete`
- Calls: `le_device_db_tlv_read_identity`, `ble_evt_publish`, `co_write16_le`, `co_reverse_copy_6`
- Confidence: medium

## ble_link_notify_state

**Send the link state frame (0xC8, 0xC9, 0xCB or 0xCC) selected by byte 0x2000FF5A**

Clears the report flag DAT_2000ff54 and sets the link flag at +0x34 to 1, then switches on the state byte DAT_2000ff5a. States 0, 1/3 and 4 send frames 0xC8, 0xCB and 0xCC (length byte 10, published length 12) with the handle, the link's address type (+7) and reversed address (+8..+13), and set DAT_2000ff54 to 1. State 2 sends frame 0xC9 (length 14, 16 bytes), which adds the flag byte (DAT_2000ff6c != 0) at [11] and a u32 read big-endian from DAT_2000ff5b+12 and stored little-endian at [12..15]. Other states send nothing.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | link context (see ble_link_notify_id_flag) |

**Notes:** State codes are not decoded. The 0xC8/0xCB/0xCC frames declare a 10-byte payload but write 9 bytes; the last byte is left unset.

- Addresses by version: 219: 0x0C04F4D8
- Called by: `ble_219_0c051eb8`
- Calls: `ble_evt_publish`, `co_write16_le`, `co_write32_le`, `co_read32_be`, `co_reverse_copy_6`
- Confidence: medium

## ble_msg_drain_to_host

**Drain the inbound 3 KiB ring and pass each message to the upper-layer callback**

While the inbound ring at 0x200148D4 holds data, it takes the guard at 0x20014884 (100 ms waits, retried on failure), reads a 2-byte length, and reads the payload into a 256-byte stack buffer when the length is below 0xFB. The guard is released on both paths. If the upper-layer receive callback at 0x20015E5C is set, it is called with (type 2, length, payload); oversize messages are dropped.

**Notes:** Only the upper-layer callback signature (type, length, payload) is inferred from the call site.

- Addresses by version: 219: 0x0C05AF1C
- Called by: `ble_219_0c0599d4`
- Calls: `xQueueGenericSend`, `xQueueSemaphoreTake`, `btstack_ring_buffer_empty`, `btstack_ring_buffer_read`
- Confidence: medium

## ble_msg_enqueue

**Queue a typed message into the 2 KiB outbound ring with lock and filter hooks**

Appends a message to the outbound ring at 0x20015538 under the guard at 0x200154E8. It returns 0x41 when bit 0 of the state word at 0x200042F8+4 is clear. For type 2 it first calls the pre-check hook at 0x20014608 and returns 0x46 if that hook reports state below 4 and payload byte 5 is outside 0x5B to 0x5D. The space needed is payload+4 (type 1) or payload+10 (type 2); if the ring lacks space, the whole ring is reset and 0x41 is returned. It waits up to 100 ms for the guard (0x43 on timeout), re-checks space, and for type 2 runs the filter hook at 0x20015F28, which maps the payload into scratch 0x20015D5C; a non-zero return drops the message. The 4-byte header holds the length (payload+6 for type 2) in the low half and the type in the high half, followed by the payload. The guard is released and ble_219_0c05d494 is called to wake the consumer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | message type; 2 selects the extended form with a 6-byte prefix and the filter hook |
| `param_2` | `u32` | payload length |
| `param_3` | `ptr` | payload buffer |

**Returns** `u32`: 0 on success; 0x41 not ready or ring full; 0x43 guard timeout; 0x46 rejected by pre-check hook

**Notes:** Semantics of message types and the 6-byte prefix are not confirmed. Sub-call 0x0C05D494 is not described in this packet.

- Addresses by version: 219: 0x0C05AE14
- Called by: `ble_219_0c028bf0`, `ble_219_0c029c18`, `ble_219_0c029d8c`, `ble_219_0c029df8`, `ble_219_0c02c338`
- Calls: `xQueueGenericSend`, `xQueueSemaphoreTake`, `ble_get_state_ptr_42f8`, `ble_219_0c05d494`, `btstack_ring_buffer_reset`, `btstack_ring_buffer_bytes_free`, `btstack_ring_buffer_write`
- Confidence: medium

## ble_msg_queues_init

**Create the BLE message queues and their run-loop data source**

Creates three guard objects through the RTOS wrapper 0x0C042D80 (count 1) at 0x200154E8, 0x20014884 and 0x20014620, and initialises three BTstack ring buffers. The 2048-byte ring (control struct 0x20015538, storage 0x2001554C, guard 0x200154E8) is the outbound queue used by ble_msg_enqueue. The 3072-byte ring (control 0x200148D4, storage 0x200148E8, guard 0x20014884) is the inbound queue drained by ble_msg_drain_to_host. The 512-byte ring (control 0x20014670, storage 0x20014684, guard 0x20014620) has no user in this packet. It then sets up the run-loop data source at 0x20015D4C with handler 0x0C05AAB8, enables its callbacks and adds it to the run loop.

**Notes:** The consumer of the 512-byte ring and the source handler 0x0C05AAB8 are not described in this packet.

- Addresses by version: 219: 0x0C05AD18
- Called by: `ble_219_0c0592a4`
- Calls: `prvInitialiseMutex`, `btstack_ring_buffer_init`, `btstack_run_loop_set_data_source_handler`, `btstack_run_loop_enable_data_source_callbacks`, `btstack_run_loop_add_data_source`, `btstack_run_loop_remove_data_source`
- Confidence: medium

## ble_random_addr_advance

**Refresh a 6-byte random address field and advance its sequence bytes**

Fills the 6-byte field at param_1 with random bytes through 0x0c045db0, then advances a sequence counter kept in the same field. While the big-endian u16 at bytes 4..5 is below 2001 (0x7D1), it increments byte 4 and stores (byte 5 + 1) OR 0xC2 in byte 5. Otherwise it increments byte 2 and stores (byte 3 + 1) OR 0xC2 in byte 3. The 0xC2 bits look like address-type flags, but the purpose of the counter is not established. Callers: ble_219_0c02a8f8, ble_219_0c02cca8 and ble_219_0c056a50.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 6-byte random address field |

**Notes:** The arithmetic is unusual (increments byte 4 rather than carrying a 16-bit value, OR-ing into the low byte), so the intent may differ from what is described here.

- Addresses by version: 219: 0x0C058170
- Called by: `ble_219_0c02a8f8`, `ble_219_0c02cca8`, `ble_219_0c056a50`
- Calls: `ble_219_0c045db0`
- Confidence: low

## ble_random_bytes_6

**Fill a 6-byte field with random bytes**

Calls the random-byte source at 0x0c045db0 (not analysed in this packet) with length 6 and returns nothing. It has no other logic. Used by the address-generation code paths; callers are ble_219_0c02b158 and ble_219_0c05c2c0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 6-byte destination |

- Addresses by version: 219: 0x0C058160
- Called by: `ble_219_0c02b158`, `ble_gen_static_random_addr`
- Calls: `ble_219_0c045db0`
- Confidence: medium

## ble_random_static_addr_build

**Build a random static Bluetooth device address from 6 random bytes**

Draws 6 random bytes through 0x0c045db0 into a local buffer. Bytes 0..3 are copied unchanged, byte 4 is stored as random+1, and byte 5 as random OR 0xC0. The address is reversed in place with bt_bdaddr_reverse_inplace (0x0c05a9e4) to wire order, and 0xC0 is ORed into the first byte. The two top bits set to 11 mark a static random address. Caller: ble_219_0c056dd0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 6-byte output device address |

- Addresses by version: 219: 0x0C0581A8
- Called by: `ble_219_0c056dd0`
- Calls: `ble_219_0c045db0`, `bt_bdaddr_reverse_inplace`
- Confidence: medium

## ble_range_broadcast

**Call the default listener, then the +0x10 handler of every range listener**

Calls the default listener DAT_2000fce4, when set, as listener(4, 0, param_1, param_2). It then walks the removal-safe list at DAT_2000fcf8 and calls each node's handler at node+0x10 with the same arguments, skipping nodes whose handler is NULL. This is the notify-all counterpart of ble_range_notify, which picks a single node by range.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | forwarded to each listener as its third argument |
| `param_2` | `u32` | forwarded to each listener as its fourth argument |

- Addresses by version: 219: 0x0C04DF64
- Called by: `ble_219_0c04e398`, `ble_219_0c04e702`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: high

## ble_range_dispatch

**Call the handler of the range node containing param_2, else the default handler**

Walks the list at DAT_2000fcf8 and picks the first node whose u16 window [node+4, node+6] contains param_2 (compared as an unsigned 32-bit value). It calls that node's handler at node+8 with all four arguments and returns the result. When no node matches, the default handler DAT_2000fce8 is used, and when the chosen handler is NULL the function returns 0 without calling anything. The +8 slot is a different callback role from the +0x10 slot used by the notify functions.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | forwarded as the first handler argument |
| `param_2` | `u32` | range key, matched against the node windows |
| `param_3` | `u32` | forwarded as the third handler argument |
| `param_4` | `u32` | forwarded as the fourth handler argument |

**Returns** `u32`: result of the selected handler, or 0 when it is NULL

- Addresses by version: 219: 0x0C04E294
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: high

## ble_range_notify

**Send a 7-byte 0xB6 frame to the range listener matching param_3, else the default**

Finds the first node in the list at DAT_2000fcf8 whose u16 window contains param_3, or uses the default listener DAT_2000fce4 when no node matches. If the selected handler (node+0x10 or DAT_2000fce4) is non-NULL, builds a 7-byte frame: byte 0 = 0xB6, byte 1 = 5 (payload length), byte 2 = param_1, bytes 3-4 = param_2 and bytes 5-6 = param_3, both u16 little-endian, then calls handler(4, 0, frame, 7). The two u16 fields are the notified values; their meaning is not decoded.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | sub-type byte at frame[2] |
| `param_2` | `u32` | low 16 bits sent at frame[3..4] |
| `param_3` | `u32` | low 16 bits sent at frame[5..6]; also the range key |

- Addresses by version: 219: 0x0C04E304
- Called by: `ble_219_0c04e398`, `ble_219_0c04e702`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`, `co_write16_le`
- Confidence: high

## ble_ring_poll_status

**Poll four ring or stream objects of a channel and return a two-bit readiness mask**

Takes a channel record: the channel id byte is at +8 and the pointer at +0x10 points to a block whose words at +0x5C, +0x60, +0x64 and +0x68 hold four object pointers, each checked only when non-null. Every check runs inside vPortEnterCritical/vPortExitCritical. The object at +0x5C is tested with 0x0C043338 (bit 0 set when non-zero), the object at +0x60 with 0x0C043364 (bit 1 set when zero), the object at +0x64 with ringbuf_free_space (bit 0 set when free space is non-zero) and the one at +0x68 with ringbuf_is_empty (bit 1 set when not empty). After each check the channel is updated through 0x0C048298(channel, 0 or 1); what that routine stores is left to its own description. Returns the OR of the flags.

| Parameter | Type | Description |
|---|---|---|
| `channel` | `ptr` | channel record; id byte at +8, object block pointer at +0x10 |

**Returns** `u8`: bit 0 and bit 1 readiness flags, 0..3

**Notes:** The meanings of the 0x0C043338 and 0x0C043364 checks and of the 0x0C048298 state write are not established here. The category follows the other BLE host ring helpers.

- Addresses by version: 219: 0x0C0422D4
- Calls: `vPortEnterCritical`, `vPortExitCritical`, `uxQueueSpacesAvailable`, `prvIsQueueEmpty`, `ringbuf_free_space`, `ringbuf_is_empty`, `ble_219_0c048298`
- Confidence: medium

## ble_sink_init

**Store the sink context pointer and register the class-4 hook handler at 0x0c04de00**

Stores param_1 in the global DAT_2000fcd4, the context used by the sink code, then calls FUN_0c06f03c(0x0c04de00, 4) to register the function at 0x0c04de00 for hook class 4. Class 4 is the first argument of every event callback in this packet (ble_evt_publish, ble_range_*, ble_sink_notify_pair). The registration routine 0x0c06f03c is not described yet, so its semantics are inferred from the call shape.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | context pointer kept in DAT_2000fcd4 |

**Notes:** Sink pointer DAT_2000fcdc is only read in this packet; the handler at 0x0c04de00 is not named yet.

- Addresses by version: 219: 0x0C04DED8
- Called by: `att_server_init`
- Calls: `l2cap_channel_set_context_by_cid`
- Confidence: medium

## ble_sink_notify_pair

**Send a 6-byte 0xB5 frame carrying two u16 values to the sink callback**

If the sink pointer DAT_2000fcdc is non-NULL, builds a 6-byte frame: byte 0 = 0xB5 (message type), byte 1 = 4 (payload length), bytes 2-3 = param_1 and bytes 4-5 = param_2, both as u16 little-endian. It then calls the sink as sink(4, param_1, frame, 6). Nothing is sent when the pointer is NULL. The two values are not decoded further (they look like a handle and a value).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | sent as u16 at frame[2..3]; also the second sink argument |
| `param_2` | `u32` | sent as u16 at frame[4..5] |

- Addresses by version: 219: 0x0C04DF24
- Called by: `ble_219_0c04e398`
- Calls: `co_write16_le`
- Confidence: medium

## bt_bdaddr_is_zero

**Return true when the 6-byte Bluetooth address is all zeros**

Builds a 6-byte zero buffer on the stack and returns memcmp(param_1, zeros, 6) == 0. Used by 0c058250, 0c0593a4, 0c059d0c and 0c05a608 to detect an unset/invalid BD_ADDR before using it.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 6-byte BD_ADDR |

**Returns** `bool`: true if all six bytes are 0

- Addresses by version: 219: 0x0C05A9C4
- Called by: `ble_219_0c058250`, `ble_219_0c0593a4`, `ble_219_0c059d0c`, `ble_219_0c05a608`
- Calls: `memcmp`
- Confidence: high

## bthost_byte_get_high5_bits

**Return bits 3..7 of the byte pointed to (0 if NULL)**

Returns *param_1 >> 3, or 0 when param_1 is NULL. Companion getter of ble_219_0c04c570; both are called by ble_219_0c04bd98.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pointer to the packed byte, may be NULL |

**Returns** `u8`: upper 5 bits, 0 if NULL

- Addresses by version: 219: 0x0C04C578
- Called by: `sdp_get_service_record_handle`
- Confidence: medium

## bthost_byte_get_low3_bits

**Return bits 0..2 of the byte pointed to**

Returns *param_1 & 7 (no NULL check). Its only caller, ble_219_0c04bd98, uses it with the companion ble_219_0c04c578, which extracts the upper five bits of the same byte, so the byte is a packed field with a 3-bit part and a 5-bit part (e.g. a type/length style header).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pointer to the packed byte |

**Returns** `u8`: low 3 bits

- Addresses by version: 219: 0x0C04C570
- Called by: `sdp_get_service_record_handle`
- Confidence: medium

## bthost_latch_ctrl_mode_2000fb90

**Store the controller/host mode byte from ble_ctrl_env_get_mode_or_4 into DAT_2000fb90**

One-liner: DAT_2000fb90 (u8) = ble_ctrl_env_get_mode_or_4() (env+0x58, or 4 while the override flag env+0x64 is set). Called only from the host bring-up routine ble_219_0c059230 when its argument is 2, next to other classic-BT host initialisers (ble_219_0c04bd48 which sets DAT_2000fcac = 0x10001 and registers a handler, SDP/HID setup). Nothing in the image reads DAT_2000fb90, so it is probably a leftover configuration latch; ble_219_0c04bb00 (hid_device_init-like) uses the same getter as an argument when registering L2CAP services on PSM 0x11/0x13.

**Notes:** Meaning of the mode byte is not established; see ble_ctrl_env_get_mode_or_4.

- Addresses by version: 219: 0x0C04BD0C
- Called by: `ble_219_0c059230`
- Calls: `ble_ctrl_env_get_mode_or_4`
- Confidence: low

## bthost_link_key_db_tlv_delete_link_key

**BTstack link-key DB (TLV backend): delete the stored link key for a BD_ADDR**

Iterates the four slots with TLV tag 'BTL'+index (0x42544C00 | 0..3), reading each 28-byte link_key_nvm_t {u32 seq_nr; bd_addr[6] at +4; link_key[16] at +10; u16 type at +26} via the btstack_tlv get_tag function (*DAT_2000f8ac)[0] with context DAT_2000f8b0. The first slot whose bd_addr memcmp-equals param_1 is removed with delete_tag ((*DAT_2000f8ac)[2]); if none matches after 4 slots the function returns silently. Slot of the btstack_link_key_db_t vtable at 0x0C07FE88 (no direct callers), source file bthost_link_key_db_tlv.c; siblings get_link_key (ble_219_0c04ac70), put_link_key (ble_219_0c04ace4), iterator_get_next (ble_219_0c04ab90).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | bd_addr (6 bytes) to delete |

- Addresses by version: 219: 0x0C04AC1C
- Calls: `memcmp`
- Confidence: high

## bthost_link_key_db_tlv_get_instance

**Register the TLV implementation/context and return the link-key DB vtable**

Stores the TLV implementation pointer in DAT_2000f8ac and its context in DAT_2000f8b0 (used by the link-key DB functions to read/write tags 'BTL'+index), then returns the address 0x0C07FE88 of the btstack_link_key_db_t function table (open, set_local_bd_addr, close, get/put/delete_link_key, iterator_init/get_next/done). Called from ble_219_0c05b67c during host initialisation.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TLV implementation (btstack_tlv_t vtable) |
| `param_2` | `ptr` | TLV context |

**Returns** `ptr`: pointer to link key DB vtable

- Addresses by version: 219: 0x0C04ADE0
- Called by: `ble_219_0c05b67c`
- Confidence: high

## bthost_link_key_db_tlv_get_link_key

**BTstack link-key DB (TLV backend): look up the link key and type for a BD_ADDR**

Reads TLV tags 'BTL'+0..3 (0x42544C00|i) via get_tag (*DAT_2000f8ac)[0] with context DAT_2000f8b0 into a 28-byte link_key_nvm_t on the stack. On the first entry whose bd_addr at +4 memcmp-matches param_1, the 16-byte link key at +10 is copied to param_2, the u16 link_key_type at +26 to param_3 and 1 is returned. If all four slots are empty or mismatch, 0 is returned and the outputs are untouched. Vtable entry of btstack_link_key_db_t at 0x0C07FE88 (bthost_link_key_db_tlv.c), used by hci.c on link-key requests.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | bd_addr (6 bytes) |
| `param_2` | `ptr` | out: link key (16 bytes) |
| `param_3` | `ptr` | out: link_key_type_t (u16) |

**Returns** `u32`: 1 if found, 0 otherwise

- Addresses by version: 219: 0x0C04AC70
- Calls: `memcmp`
- Confidence: high

## bthost_link_key_db_tlv_iterator_get_next

**Link-key DB iterator: fetch the next stored link key from TLV storage**

Iterator state is a byte index in *param_1 (0..3, max four entries). For each index it calls the TLV get_tag function (*DAT_2000f8ac) with context DAT_2000f8b0, tag 0x42544C00|index ('BTL'+index) and a 28-byte buffer. On the first tag that exists it copies the 6-byte BD_ADDR to param_2, the 16-byte link key to param_3 and the u16 key type to param_4, advances the index and returns 1. If none is found, the index becomes 4 and 0 is returned. This is slot 7 of the BTstack btstack_link_key_db_t vtable at 0x0C07FE88 (hence no direct callers); source file bthost_link_key_db_tlv.c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | iterator state: u8 current index |
| `param_2` | `ptr` | out: bd_addr (6 bytes) |
| `param_3` | `ptr` | out: link key (16 bytes) |
| `param_4` | `ptr` | out: link key type (u16) |

**Returns** `u32`: 1 if an entry was returned, 0 when iteration is finished

- Addresses by version: 219: 0x0C04AB90
- Confidence: high

## bthost_link_key_db_tlv_put_link_key

**BTstack link-key DB (TLV backend): store a link key, reusing the matching, an empty or the oldest slot**

Scans the four 'BTL'+i TLV slots (28-byte link_key_nvm_t, read with (*DAT_2000f8ac)[0] and context DAT_2000f8b0): remembers the tag whose bd_addr equals param_1, the highest seq_nr seen, a tag of an empty slot, and the tag with the lowest seq_nr (oldest). Target tag preference: matching address, else an empty slot, else the oldest entry. It then writes {seq_nr = max+1, bd_addr = param_1, link_key = param_2 (16 bytes), type = param_3} with store_tag (*DAT_2000f8ac)[1]; on failure it logs 'store link key failed' (bthost_link_key_db_tlv.c:142) through ble_hook_invoke_indexed (level 2 = error). Vtable entry of btstack_link_key_db_t at 0x0C07FE88; siblings get/delete_link_key.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | bd_addr (6 bytes) |
| `param_2` | `ptr` | link key (16 bytes) |
| `param_3` | `u16` | link_key_type_t |

- Addresses by version: 219: 0x0C04ACE4
- Calls: `ble_hook_invoke_indexed`, `memcmp`
- Confidence: high

## bthost_set_var_2000fa00

**Store a 32-bit value (probably a callback) in the global at 0x2000fa00**

Trivial setter: DAT_2000fa00 = param_1. Called from ble_219_0c058f00 during setup, so the value is most likely a handler/callback pointer registered with the host stack; exact meaning not determinable here.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value (likely function pointer) to store |

- Addresses by version: 219: 0x0C04BBCC
- Called by: `ble_219_0c058f00`
- Confidence: low

## bthost_stub_nop_0c04aef8

**Empty function (immediate return)**

Single return instruction; no callers, likely a default callback or the 'close' style no-op entry of a vtable.

- Addresses by version: 219: 0x0C04AEF8
- Confidence: medium

## bthost_stub_nop_0c04aefc

**Empty function (immediate return)**

Single return instruction; no callers, likely a default callback / empty vtable entry.

- Addresses by version: 219: 0x0C04AEFC
- Confidence: medium

## bthost_stub_return_minus1_0c04aef0

**Stub returning -1**

Returns 0xFFFFFFFF without side effects. No direct callers; it sits just after the link-key DB code and is most likely an unused/default entry in a callback table that signals 'not available / error'.

**Returns** `s32`: always -1

- Addresses by version: 219: 0x0C04AEF0
- Confidence: low

## bthost_tlv_get_instance

**Return the pointer to the flash TLV storage vtable**

Returns the address 0x0C07FFFC of a constant three-entry function table (btstack_tlv_t: get_tag, store_tag, delete_tag, code at 0x0C048DEC/0x0C048CAC/0x0C048B70). Called from ble_219_0c05b67c, which also calls the link-key DB get_instance, so it is the BTstack TLV (tag-length-value persistent store) implementation handed to the bthost key/device databases.

**Returns** `ptr`: pointer to the TLV implementation vtable

**Notes:** Identification as btstack_tlv_t is inferred from how the link-key and device DB call vtable slots +0 (get) and +8 (delete).

- Addresses by version: 219: 0x0C048F34
- Called by: `ble_219_0c05b67c`
- Confidence: medium

## btstack_hid_get_report_size_for_id

**Compute the byte size of a HID report from the report descriptor**

BTstack btstack_hid_parser.c btstack_hid_get_report_size_for_id(report_id, report_type, descriptor_len, descriptor). Returns 0 for an empty descriptor. Otherwise it walks the descriptor with btstack_hid_parse_descriptor_item (item struct on the stack: s32 value +0, u16 size +4, u8 type +6, u8 tag +7). Global items (type 1): tag 8 Report ID sets the current id; tag 9 Report Count and tag 7 Report Size are recorded only while the current id equals report_id. Main items (type 0) with matching id: tag 8 Input / 9 Output / 0xb Feature add count*size bits to the total when report_type is 1 / 2 / 3 respectively (HID_REPORT_TYPE_INPUT/OUTPUT/FEATURE) and then reset count and size to 0. After each item the descriptor pointer/length advance by item size. Returns (total_bits + 7) / 8 (signed division). Called from hid_device.c (0c04af5a) to size outgoing/incoming reports.

| Parameter | Type | Description |
|---|---|---|
| `report_id` | `s32` | report id to match (0 if the descriptor declares none) |
| `report_type` | `s32` | 1 input, 2 output, 3 feature |
| `hid_descriptor_len` | `u32` | descriptor length in bytes |
| `hid_descriptor` | `ptr` | HID report descriptor bytes |

**Returns** `s32`: report payload size in bytes (0 if not found)

- Addresses by version: 219: 0x0C065288
- Called by: `hid_report_size_valid_body`
- Calls: `btstack_hid_parse_descriptor_item`
- Confidence: high

## btstack_hid_parse_descriptor_item

**Parse one HID report-descriptor item (short or long)**

Fills a hid_descriptor_item_t (item_value u32 at +0, item_size u16 at +4, item_type u8 at +6, item_tag u8 at +7, data_size u8 at +8) from the byte stream. The prefix byte gives the data size via the table {0,1,2,4}[b&3], the item type from bits 3:2 and the tag from bits 7:4. A prefix of 0xFE (type 3, tag 15) is a long item: data size and tag come from the next two bytes and the header is 3 bytes. The little-endian data value is assembled into item_value; for global items (type 1) with tags 1..4 (logical/physical minimum/maximum) the value is sign-extended. If the buffer is shorter than the item, or a long item has more than 4 data bytes, the function returns without completing. Called by the HID device code (0c04af00 and 0c065288/0c0653a0).

| Parameter | Type | Description |
|---|---|---|
| `item` | `ptr` | out: hid_descriptor_item_t (value u32, size u16, type u8, tag u8, data_size u8) |
| `hid_descriptor` | `ptr` | HID report descriptor bytes at the current position |
| `hid_descriptor_len` | `u32` | bytes remaining |

**Notes:** Matches BTstack btstack_hid_parse_descriptor_item.

- Addresses by version: 219: 0x0C065190
- Called by: `hid_report_id_status`, `btstack_hid_get_report_size_for_id`, `btstack_hid_report_id_declared`
- Confidence: high

## btstack_hid_report_id_declared

**Check whether a HID report descriptor contains a Report ID item**

BTstack btstack_hid_parser.c btstack_hid_report_id_declared(descriptor_len, descriptor). Returns 0 for an empty descriptor. Otherwise iterates the items with btstack_hid_parse_descriptor_item (stack item: u16 size +4, u8 type +6, u8 tag +7) and returns 1 as soon as a Global item (type 1) with tag 8 (Report ID) is found; advancing by item size until the length is exhausted returns 0. Called from hid_device.c (0c04afcc) to decide whether reports carry a leading report-id byte.

| Parameter | Type | Description |
|---|---|---|
| `hid_descriptor_len` | `u32` | descriptor length in bytes |
| `hid_descriptor` | `ptr` | HID report descriptor bytes |

**Returns** `s32`: 1 if a Report ID item exists, else 0

- Addresses by version: 219: 0x0C0653A0
- Called by: `ble_219_0c04afcc`
- Calls: `btstack_hid_parse_descriptor_item`
- Confidence: high

## btstack_linked_list_add

**Push an item on the head of a linked list unless already present**

BTstack btstack_linked_list_add(). Walks the list from *param_1 following each item's first word (next pointer); if param_2 is found the list is left unchanged and 0 is returned. Otherwise param_2->next is set to the old head, the head pointer is set to param_2 and 1 is returned. Items embed the next pointer as their first 32-bit word.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | list head cell (btstack_linked_list_t*) |
| `param_2` | `ptr` | item to insert (btstack_linked_item_t*) |

**Returns** `u32`: 1 if inserted, 0 if the item was already in the list

- Addresses by version: 219: 0x0C0653EC
- Called by: `sdp_register_service`, `ble_ctrl_conn_alloc_and_register`, `ble_219_0c06b5a0`, `ble_219_0c06d474`, `l2cap_register_service`
- Confidence: high

## btstack_linked_list_add_tail

**Append an item to the end of a linked list (thunk to the implementation)**

Two-byte thunk that falls into btstack_linked_list_add_tail_impl (0c065416): walks the list from the head cell following each item's first word, returns 0 if the item is already linked, otherwise sets item->next = NULL, stores it in the last next pointer and returns 1. This is the public BTstack btstack_linked_list_add_tail entry used by the crypto queue (0c064ffc, 0c065038 ... on btstack_crypto_operations), SM, HCI, L2CAP (0c06cb3c, 0c06dc56, 0c06ee70) and the run loop (0c065a50).

| Parameter | Type | Description |
|---|---|---|
| `list` | `ptr` | pointer to the list head cell |
| `item` | `ptr` | item whose first word is the next pointer |

**Returns** `s32`: 1 if appended, 0 if the item was already in the list

- Addresses by version: 219: 0x0C065410
- Called by: `ble_219_0c04eb8c`, `ble_evt_subscribe`, `ble_219_0c064ffc`, `ble_219_0c065038`, `ble_219_0c065078`, `ble_219_0c0650c0`, `ble_219_0c065108`, `ble_ctrl_deferred_list_add`, `hci_add_event_handler`, `ble_219_0c06cb3c`, `ble_219_0c06dc56`, `ble_219_0c06ee70`
- Calls: `btstack_linked_list_add_tail_impl`
- Confidence: high

## btstack_linked_list_add_tail_impl

**Append an item at the tail of a linked list unless already present**

Body of BTstack btstack_linked_list_add_tail() (0x0c065410 is a 1-insn thunk that branches here, so Ghidra splits it). Starting at the head cell it steps through the next pointers; reaching a NULL next sets param_2->next = NULL, links param_2 at the end and returns 1. If param_2 is met during the walk it returns 0 and does not modify the list. Used with several fixed global lists such as the one at 0x200190a4.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | list head cell (btstack_linked_list_t*) |
| `param_2` | `ptr` | item to append (btstack_linked_item_t*) |

**Returns** `u32`: 1 if appended, 0 if already linked

**Notes:** The walk compares the successor with the item, so an item that is the very first entry is not detected by the first iteration of the loop; behaviour identical to BTstack for normal use.

- Addresses by version: 219: 0x0C065416
- Called by: `btstack_linked_list_add_tail`
- Confidence: high

## btstack_linked_list_empty

**Test whether a BTstack singly linked list is empty**

BTstack btstack_linked_list_empty(). param_1 points at the list head cell (a pointer to the first item); returns true when that head pointer is NULL. No side effects.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | address of the list head pointer (btstack_linked_list_t*) |

**Returns** `bool`: 1 if the list has no items

- Addresses by version: 219: 0x0C0653E0
- Called by: `ble_219_0c04e398`, `ble_219_0c051eb8`, `ble_219_0c065038`
- Confidence: high

## btstack_linked_list_get_first_item

**Return the first item of a linked list**

BTstack btstack_linked_list_get_first_item(): dereferences the list head cell and returns the first item pointer (NULL when empty).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | list head cell (btstack_linked_list_t*) |

**Returns** `ptr`: first item or NULL

- Addresses by version: 219: 0x0C065450
- Called by: `ble_219_0c065038`
- Confidence: high

## btstack_linked_list_iterator_has_next

**Check whether the linked list iterator has another item**

BTstack btstack_linked_list_iterator_has_next(). If advance_on_next is 0 (nothing consumed yet) the answer is curr != NULL. Otherwise it looks at prev->next; if that still equals curr it takes curr->next instead (handles the current item having been removed), and returns whether the result is non-NULL. Pure query, does not change the iterator.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | iterator (btstack_linked_list_iterator_t*) |

**Returns** `bool`: 1 if another item can be fetched

- Addresses by version: 219: 0x0C06546C
- Called by: `ble_range_broadcast`, `att_server_write_callback`, `ble_range_dispatch`, `ble_range_notify`, `ble_219_0c04e398`, `ble_219_0c04e702`, `ble_evt_publish`, `ble_219_0c051eb8`, `ble_219_0c052de8`, `btstack_run_loop_embedded_remove_all_timers`, `ble_ctrl_update_link_slot_flag`, `ble_ctrl_pending_drain_and_arm_timer` ...
- Confidence: high

## btstack_linked_list_iterator_init

**Initialise a removal-safe linked list iterator**

BTstack btstack_linked_list_iterator_init(). The iterator is {u32 advance_on_next; item *prev; item *curr}. Sets advance_on_next = 0, prev = list head cell address (so prev->next is the head) and curr = *list (first item). Counterparts are iterator_has_next (0x0c06546c), iterator_next (0x0c065490) and iterator_remove (0x0c0654b4).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | iterator struct to initialise (btstack_linked_list_iterator_t*, 12 bytes) |
| `param_2` | `ptr` | list head cell (btstack_linked_list_t*) |

- Addresses by version: 219: 0x0C065460
- Called by: `ble_range_broadcast`, `att_server_write_callback`, `ble_range_dispatch`, `ble_range_notify`, `ble_219_0c04e702`, `ble_evt_publish`, `ble_219_0c052de8`, `btstack_run_loop_embedded_remove_all_timers`, `ble_ctrl_update_link_slot_flag`, `ble_ctrl_pending_drain_and_arm_timer`, `hci_emit_event`, `ble_ctrl_conn_teardown_and_count` ...
- Confidence: high

## btstack_linked_list_iterator_next

**Return the next item from a linked list iterator**

BTstack btstack_linked_list_iterator_next(). On the first call it sets advance_on_next = 1 and returns the current item. Later calls read prev->next: if it still equals curr the iterator advances (prev = curr, next = curr->next); otherwise curr was unlinked by iterator_remove so prev stays and the item after prev is used. Stores the result in curr and returns it (NULL at the end).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | iterator (btstack_linked_list_iterator_t*) |

**Returns** `ptr`: next item or NULL at the end of the list

- Addresses by version: 219: 0x0C065490
- Called by: `ble_range_broadcast`, `att_server_write_callback`, `ble_range_dispatch`, `ble_range_notify`, `ble_219_0c04e398`, `ble_219_0c04e702`, `ble_evt_publish`, `ble_219_0c051eb8`, `ble_219_0c052de8`, `btstack_run_loop_embedded_remove_all_timers`, `ble_ctrl_update_link_slot_flag`, `ble_ctrl_pending_drain_and_arm_timer` ...
- Confidence: high

## btstack_linked_list_iterator_remove

**Unlink the iterator's current item from its list**

BTstack btstack_linked_list_iterator_remove(). Sets curr = curr->next (the old current item's successor), writes it to prev->next, thereby unlinking the item last returned by iterator_next, and clears advance_on_next so the next call re-examines the new current item. Used during list traversals that delete entries.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | iterator (btstack_linked_list_iterator_t*) |

- Addresses by version: 219: 0x0C0654B4
- Called by: `ble_219_0c06cdb8`
- Confidence: high

## btstack_linked_list_pop

**Remove and return the first item of a linked list**

BTstack btstack_linked_list_pop(). Loads the first item; if non-NULL the head cell is advanced to item->next. Returns the popped item (or NULL for an empty list). Also exists as an identical compiler copy at 0x0c0656ec.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | list head cell (btstack_linked_list_t*) |

**Returns** `ptr`: popped item or NULL

- Addresses by version: 219: 0x0C065454
- Called by: `ble_219_0c05d108`, `btstack_crypto_ccm_next_block`, `ble_219_0c065038`
- Confidence: high

## btstack_linked_list_remove

**Unlink an item from a singly linked list**

BTstack btstack_linked_list_remove(). Returns 0 immediately for a NULL item. Otherwise walks from the head cell keeping the predecessor; when predecessor->next == param_2 it sets predecessor->next = param_2->next and returns 1. Returns 0 if the item is not found. Very widely used (timers, connections, data sources) across the host stack.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | list head cell (btstack_linked_list_t*) |
| `param_2` | `ptr` | item to remove (btstack_linked_item_t*) |

**Returns** `u32`: 1 if removed, 0 if not found or item NULL

- Addresses by version: 219: 0x0C06542C
- Called by: `ble_219_0c04e398`, `ble_219_0c051eb8`, `btstack_run_loop_embedded_remove_all_timers`, `btstack_run_loop_embedded_process_timers`, `ble_ctrl_pending_drain_and_arm_timer`, `ble_ctrl_conn_free_and_report_disconnect`, `ble_ctrl_conn_teardown_and_count`, `ble_ctrl_clear_secondary_list`, `hci_remove_event_handler`, `ble_219_0c0674e8`, `ble_219_0c068da8`, `l2cap_channel_timer_teardown` ...
- Confidence: high

## btstack_memory_free_list_push

**Push a freed block onto the global free list at 0x20019088**

Walks the singly linked list headed by the global DAT_20019088 to its end with an empty loop (leftover of the inlined duplicate check in btstack_linked_list_add), then sets *param_1 = DAT_20019088 and DAT_20019088 = param_1, i.e. head-insertion into the free list. Called from the small btstack_memory_*_free wrappers (0x0c0654e4, 0x0c065528, 0x0c06554c) and from two large host functions; interpreted as returning a block to the BTstack static memory pool free list.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | block (first word is next pointer) returned to the free list |

**Notes:** Exact owner of the free list at 0x20019088 (which pool) not determined; the shared list for several free wrappers is odd.

- Addresses by version: 219: 0x0C065558
- Called by: `btstack_memory_hci_connection_free`, `btstack_memory_l2cap_channel_free`, `btstack_memory_sm_lookup_entry_free`, `ble_ctrl_pending_drain_and_arm_timer`, `ble_219_0c0674e8`
- Confidence: medium

## btstack_memory_hci_connection_free

**Return an hci_connection_t block to its pool free list**

BTstack btstack_memory_hci_connection_free(connection): tail-jumps to the shared pool-free routine (0c065558, named btstack_memory_free_list_push in wave 1) with the pool head DAT_20017c64, which walks the list to its end (no-op duplicate check leftover) and head-inserts the block: *block = old head, head = block. The pool (3 x 800 bytes, storage 0x20017c68) is the one hci_connection_t blocks are taken from by 0c0654c4. Called from hci.c when a connection is torn down (0c06637a, 0c0663e8 and the HCI event handler 0c068da8).

| Parameter | Type | Description |
|---|---|---|
| `connection` | `ptr` | hci_connection_t block to release |

**Notes:** The decompiler inlined the callee with the pool head 0x20017c64, which shows that 0c065558 takes the pool as a parameter (btstack_memory_pool_free style) rather than a fixed list at 0x20019088 as described in wave 1.

- Addresses by version: 219: 0x0C0654E4
- Called by: `ble_ctrl_conn_free_and_report_disconnect`, `ble_ctrl_conn_teardown_and_count`, `ble_219_0c068da8`
- Calls: `btstack_memory_free_list_push`
- Confidence: high

## btstack_memory_hci_connection_get

**Allocate and zero an hci_connection_t from the 3-entry 800-byte pool**

BTstack btstack_memory_hci_connection_get(): pops a block from the pool free list at DAT_20017c64 with btstack_memory_pool_get; if one is available it is cleared with memset(block, 0, 800). The pool is created in btstack_memory_init (0c065564) as 3 blocks of 800 bytes (storage at 0x20017c68), so at most 3 ACL/LE connections exist at once. Sole caller is hci.c create_connection_for_bd_addr_and_type (0c066168), which then fills state, timer and address fields. The matching free is 0c0654e4.

**Returns** `ptr`: zeroed hci_connection_t or NULL when all 3 are in use

- Addresses by version: 219: 0x0C0654C4
- Called by: `ble_ctrl_conn_alloc_and_register`
- Calls: `btstack_memory_pool_get`, `memset`
- Confidence: high

## btstack_memory_l2cap_channel_free

**Return an l2cap_channel_t block to its pool free list**

BTstack btstack_memory_l2cap_channel_free(channel): tail-jumps to the shared pool-free routine (0c065558) with pool head DAT_20018b74; the block is head-inserted into the free list (*block = old head, head = block) after a no-op walk to the list end. The pool (8 x 0x5c bytes, storage 0x20018b78) is the one 0c06550c allocates from. Called from l2cap.c channel teardown paths (0c06c74c, 0c06c83c, 0c06cdb8, 0c06d9b0 and the signaling handler 0c06dc56).

| Parameter | Type | Description |
|---|---|---|
| `channel` | `ptr` | l2cap_channel_t block to release |

- Addresses by version: 219: 0x0C065528
- Called by: `l2cap_channel_timer_teardown`, `l2cap_channels_teardown_by_addr`, `ble_219_0c06cdb8`, `ble_219_0c06d9b0`, `ble_219_0c06dc56`
- Calls: `btstack_memory_free_list_push`
- Confidence: high

## btstack_memory_l2cap_channel_get

**Allocate and zero an l2cap_channel_t from the 8-entry 92-byte pool**

BTstack btstack_memory_l2cap_channel_get(): pops a block from the pool free list at DAT_20018b74 with btstack_memory_pool_get and clears it with memset(block, 0, 0x5c). The pool is created in btstack_memory_init (0c065564) as 8 blocks of 0x5c (92) bytes (storage 0x20018b78), i.e. up to 8 simultaneous L2CAP channels (LE CoC / classic). Sole caller is the l2cap.c channel constructor 0c06cd00 (l2cap_create_channel_entry). The matching free is 0c065528.

**Returns** `ptr`: zeroed l2cap_channel_t or NULL when the pool is empty

- Addresses by version: 219: 0x0C06550C
- Called by: `l2cap_create_channel_entry`
- Calls: `btstack_memory_pool_get`, `memset`
- Confidence: high

## btstack_memory_l2cap_service_get

**Allocate and zero an l2cap_service_t from the 8-entry 16-byte pool**

BTstack btstack_memory_l2cap_service_get(): pops a block from the pool free list at DAT_20018e58 with btstack_memory_pool_get and, if non-NULL, zeroes its four 32-bit words (16 bytes: linked item, psm/mtu, packet handler, security level). The pool is created in btstack_memory_init (0c065564) as 8 blocks of 0x10 bytes (storage 0x20018e5c). Sole caller is l2cap_register_service (0c06f078), which logs 'register: no memory for l2cap_service_t' on NULL. The block pointer is returned in r0 although the decompiler shows void.

**Returns** `ptr`: zeroed l2cap_service_t or NULL when the pool is empty (r0)

- Addresses by version: 219: 0x0C0654F0
- Called by: `l2cap_register_service`
- Calls: `btstack_memory_pool_get`
- Confidence: high

## btstack_memory_pool_create

**Build a free list from a contiguous array of fixed-size blocks**

BTstack btstack_memory_pool_create(pool, storage, count, size). Sets *param_1 = NULL. If count > 0 the first block gets next = NULL and becomes the pool head; for each further block (previous + block size) next points at the previous block and the head is moved to the new block, so the head ends at the last block and the chain runs backwards. The inner while loop is a no-op leftover of the inlined duplicate check. Called once at stack start (0x0c065564) for each pool.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pool free list head cell |
| `param_2` | `ptr` | storage array start |
| `param_3` | `s32` | number of blocks |
| `param_4` | `s32` | block size in bytes |

- Addresses by version: 219: 0x0C0656B0
- Called by: `ble_219_0c065564`
- Confidence: high

## btstack_memory_pool_get

**Pop a block from a memory pool free list**

Same code as btstack_linked_list_pop: loads the head block of the pool free list, advances the head to block->next and returns the block (NULL when the pool is exhausted). Called by the btstack_memory_*_get allocation wrappers (0x0c0654c4, 0x0c0654f0, 0x0c06550c, 0x0c065534).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pool free list head cell |

**Returns** `ptr`: free block or NULL if the pool is empty

- Addresses by version: 219: 0x0C0656EC
- Called by: `btstack_memory_hci_connection_get`, `btstack_memory_l2cap_service_get`, `btstack_memory_l2cap_channel_get`, `btstack_memory_service_record_item_get`
- Confidence: high

## btstack_memory_service_record_item_get

**Allocate and zero a 12-byte SDP service_record_item_t from its 8-entry pool**

BTstack btstack_memory_service_record_item_get(): pops a block from the pool free list at DAT_20018fd8 with btstack_memory_pool_get and, if non-NULL, zeroes its three words (linked item, service_record_handle, service_record pointer). The pool is created in btstack_memory_init (0c065564) as 8 blocks of 0xc bytes (storage 0x20018fdc). Sole caller is sdp_register_service (0c04bdc8), which rejects handles below 0x10000 (0x83), duplicates (0x80) and returns 0x56 (BTSTACK_MEMORY_ALLOC_FAILED) when this returns NULL, else stores handle and record pointer at +4/+8 and links the item into the record list at 0x2000fcb4. The pointer is returned in r0 (decompiler shows void).

**Returns** `ptr`: zeroed service_record_item_t or NULL when the pool is empty (r0)

- Addresses by version: 219: 0x0C065534
- Called by: `sdp_register_service`
- Calls: `btstack_memory_pool_get`
- Confidence: high

## btstack_memory_sm_lookup_entry_free

**Return a 12-byte block to the 6-entry pool at 0x2001903c (SM address-resolution entries)**

Tail-jumps to the shared pool-free routine (0c065558) with pool head DAT_2001903c; the block is head-inserted into that free list. btstack_memory_init (0c065564) creates this pool as 6 blocks of 0xc bytes (storage 0x20019040). The only caller is the large security-manager routine 0c051eb8 (sm.c), and the 12-byte size matches BTstack's sm_lookup_entry_t { linked item; u8 address_type; bd_addr_t address }, which sm_address_resolution frees after resolving a peer address. Hence interpreted as btstack_memory_sm_lookup_entry_free.

| Parameter | Type | Description |
|---|---|---|
| `entry` | `ptr` | sm_lookup_entry_t block to release |

**Notes:** Pool identity inferred from block size (12), count (6) and the SM caller; the matching _get wrapper is not in this packet.

- Addresses by version: 219: 0x0C06554C
- Called by: `ble_219_0c051eb8`
- Calls: `btstack_memory_free_list_push`
- Confidence: medium

## btstack_ring_buffer_bytes_available

**Number of bytes stored in a ring buffer**

BTstack btstack_ring_buffer_bytes_available(). If the full flag (+0x10) is set returns size (+4). Otherwise returns last_written - last_read (+0xc minus +8), adding size when negative (wrap).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ring buffer struct |

**Returns** `s32`: bytes currently stored (0..size)

- Addresses by version: 219: 0x0C065728
- Called by: `ble_219_0c05ab04`, `ble_219_0c05ac20`
- Confidence: high

## btstack_ring_buffer_bytes_free

**Free space in a ring buffer**

BTstack btstack_ring_buffer_bytes_free(). Returns 0 when the full flag is set; otherwise read_index - write_index, plus size when write >= read, i.e. size - bytes_available (equal indices mean empty, so size is free).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ring buffer struct |

**Returns** `s32`: free bytes (0..size)

- Addresses by version: 219: 0x0C065768
- Called by: `ble_219_0c028b90`, `ble_msg_enqueue`
- Confidence: high

## btstack_ring_buffer_empty

**Test whether a ring buffer is empty**

BTstack btstack_ring_buffer_empty(). Computes the stored byte count as in bytes_available (full flag set -> size, else write minus read, wrapped) and returns true when it is 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ring buffer struct |

**Returns** `bool`: 1 if no bytes stored

- Addresses by version: 219: 0x0C065744
- Called by: `ble_msg_drain_to_host`
- Confidence: high

## btstack_ring_buffer_init

**Initialise a BTstack ring buffer**

BTstack btstack_ring_buffer_init(). Layout: +0 storage, +4 size, +8 last_read_index, +0xc last_written_index, +0x10 full flag (byte). Stores storage and size, zeroes both indices and the flag. Called when setting up UART and HCI byte queues (e.g. 0x0c059134 with a 16-byte buffer).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ring buffer struct (btstack_ring_buffer_t, 0x14 bytes) |
| `param_2` | `ptr` | backing storage |
| `param_3` | `u32` | storage size in bytes |

- Addresses by version: 219: 0x0C06570C
- Called by: `ble_219_0c0297b0`, `ble_evt_source_init`, `ble_msg_queues_init`
- Confidence: high

## btstack_ring_buffer_read

**Read up to length bytes from a BTstack ring buffer and report the count**

BTstack btstack_ring_buffer_read(ring, buffer, length, number_read). Bytes available are computed inline (size when the full flag at +0x10 is set, else write - read wrapped by size); the count to read is min(length, available) and is stored to *number_read. If non-zero, the first chunk min(size - read_index, count) is memcpy'd from storage + read_index into buffer, the read index advances and wraps to 0 at size, any remainder is copied from the start of storage, and finally the full flag is cleared. Called by the UART/log consumers 0c05ab04, 0c05ac20 and 0c05af1c to drain the queues filled by btstack_ring_buffer_write.

| Parameter | Type | Description |
|---|---|---|
| `ring_buffer` | `ptr` | btstack_ring_buffer_t (0x14 bytes) |
| `buffer` | `ptr` | destination buffer |
| `length` | `u32` | maximum bytes to read |
| `number_read` | `ptr` | out: u32 number of bytes actually read |

- Addresses by version: 219: 0x0C06580C
- Called by: `ble_219_0c05ab04`, `ble_219_0c05ac20`, `ble_msg_drain_to_host`
- Calls: `co_min_u32`, `memcpy`
- Confidence: high

## btstack_ring_buffer_reset

**Reset a ring buffer to empty**

BTstack btstack_ring_buffer_reset(): clears last_read_index (+8), last_written_index (+0xc) and the full flag (+0x10); storage and size are preserved.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ring buffer struct |

- Addresses by version: 219: 0x0C06571C
- Called by: `ble_msg_enqueue`
- Confidence: high

## btstack_ring_buffer_write

**Append bytes to a BTstack ring buffer, failing with 7 when they do not fit**

BTstack btstack_ring_buffer_write(ring, data, length). Layout: +0 storage, +4 size, +8 last_read_index, +0xc last_written_index, +0x10 full flag. Free space is computed inline (0 when full; otherwise read - write, plus size when write >= read). If length exceeds the free space it returns 7 (ERROR_CODE_MEMORY_CAPACITY_EXCEEDED, used in this port instead of BTSTACK_MEMORY_ALLOC_FAILED). A zero length returns 0. Otherwise the first chunk min(size - write_index, length) is memcpy'd at storage + write_index, the write index advances and wraps to 0 when it reaches size, any remainder is memcpy'd to the start of storage, and if the write index now equals the read index the full flag is set. Returns 0 on success. Used by the application-side byte queues: the UART/log sender 0c05ae14 and the mutex-protected writer 0c028b90 (ring at 0x20008aec).

| Parameter | Type | Description |
|---|---|---|
| `ring_buffer` | `ptr` | btstack_ring_buffer_t (0x14 bytes) |
| `data` | `ptr` | bytes to append |
| `data_length` | `u32` | number of bytes |
| `param_4` | `u32` | unused |

**Returns** `s32`: 0 on success, 7 if there is not enough free space

- Addresses by version: 219: 0x0C065784
- Called by: `ble_219_0c028b90`, `ble_msg_enqueue`
- Calls: `co_min_u32`, `memcpy`
- Confidence: high

## btstack_run_loop_add_data_source

**Dispatch add_data_source via the active run loop**

Tail-calls vtable entry +4 of the run loop pointed to by DAT_200190b0, forwarding r0 (the data source).

- Addresses by version: 219: 0x0C065A70
- Called by: `ble_evt_source_init`, `ble_msg_queues_init`
- Confidence: high

## btstack_run_loop_add_timer

**Dispatch add_timer via the active run loop**

Tail-calls vtable entry +0x18 of the run loop at DAT_200190b0, forwarding r0 (timer source).

- Addresses by version: 219: 0x0C065AAC
- Called by: `app_req_timeout_timer_start`, `ble_219_0c04ec18`, `ble_host_timer_arm_30s`, `ble_host_timer_arm_interval`, `ble_219_0c050310`, `sm_pairing_step_complete`, `ble_219_0c051eb8`, `ble_219_0c051ef0`, `sm_link_poll_state`, `ble_219_0c052d30`, `ble_host_timer_restart`, `ble_ctrl_pending_drain_and_arm_timer` ...
- Confidence: high

## btstack_run_loop_dump_timer

**Dispatch dump_timer via the active run loop**

Tail-calls vtable entry +0x24 of the run loop at DAT_200190b0 (debug listing of pending timers). Single caller 0x0c059948.

- Addresses by version: 219: 0x0C065AD4
- Called by: `ble_219_0c059948`
- Confidence: medium

## btstack_run_loop_embedded_add_timer

**Insert a timer into the run loop timer list sorted by expiry time**

bthost_run_loop.c add_timer(ts) for the BTstack embedded run loop; btstack_timer_source_t = { next +0, s32 timeout +4, process +8, context +0xc }. If the list at DAT_200190ac is empty the timer becomes the head with next = NULL. Otherwise it walks the list: when ts->timeout - it->timeout (util_sub_s32, i.e. btstack_time_delta) is negative the timer is linked in front of that item and the function returns, so the list stays ordered by expiry. Reaching the end appends it with next = NULL. If the timer is already in the list it logs 'Timer %p already registered!' (bthost_run_loop.c:73, level 2 via ble_hook_invoke_indexed) and then falls into the generic insert with it->next == ts, which as decompiled links the timer to itself. Called through the run loop vtable (btstack_run_loop_add_timer, 0c065aac), so no direct callers.

| Parameter | Type | Description |
|---|---|---|
| `ts` | `ptr` | btstack_timer_source_t to schedule (timeout at +4 already set) |

**Notes:** The duplicate path looks like a 'break' where upstream BTstack has 'return'; the resulting self-link would corrupt the list, which may be the reason for the error log.

- Addresses by version: 219: 0x0C065908
- Calls: `util_sub_s32`, `ble_hook_invoke_indexed`
- Confidence: high

## btstack_run_loop_embedded_dump_timer

**Log every pending run loop timer with its index and expiry time**

bthost_run_loop.c dump_timer: if the timer list DAT_200190ac is non-empty it walks it and for each timer calls the active run loop's get_time_ms (vtable slot +0x28 of the btstack_run_loop_t pointed to by DAT_200190b0) and logs 'current:[%d] timer %u (%p): timeout %lu' (bthost_run_loop.c:122, level 2 via ble_hook_invoke_indexed) with the current time, a running s16 index, the timer pointer and its timeout (+4). Reached only through the run loop vtable (btstack_run_loop_dump_timer, 0c065ad4). Part of the embedded run loop group.

- Addresses by version: 219: 0x0C0659B0
- Calls: `ble_hook_invoke_indexed`
- Confidence: high

## btstack_run_loop_embedded_init

**Reset the embedded run loop lists**

Run loop init method (reached only through the btstack_run_loop vtable, so no direct callers). Clears three globals: 0x200190a4 (a linked list head, probably the timer list), 0x200190a8 (data source list polled by 0x0c065a2c) and 0x200190ac (trigger/event flag).

**Notes:** Assignment of 0x200190a4 vs 0x200190a8 to timers/data sources inferred from the poll function.

- Addresses by version: 219: 0x0C065884
- Confidence: medium

## btstack_run_loop_embedded_next_timer_delay_ms

**Milliseconds until the earliest run loop timer expires (-1 if none)**

If the timer list DAT_200190ac is empty returns 0xffffffff. Otherwise computes delta = head->timeout (+4) - now (util_sub_s32) and clamps negative values to 0 with the mask trick delta & ~(delta >> 31). Called by the host main loop 0c05d108 right after processing timers to choose the wait time of its event wait (negative -> wait forever or 100 ms, otherwise min(delta, 100) ms depending on DAT_20017284). Part of the bthost_run_loop.c embedded run loop group.

| Parameter | Type | Description |
|---|---|---|
| `now_ms` | `u32` | current run loop time in milliseconds |
| `param_2` | `u32` | unused |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | unused |

**Returns** `u32`: ms until the next timer (>= 0), or 0xffffffff when no timer is pending

- Addresses by version: 219: 0x0C065A0C
- Called by: `ble_219_0c05d108`
- Calls: `util_sub_s32`
- Confidence: high

## btstack_run_loop_embedded_poll_data_sources

**Call process() of every data source that has POLL enabled**

Part of the embedded run loop execute step. Walks the data source list at DAT_200190a8; for each item it caches the next pointer first (so the callback may remove itself), tests bit 0 of the u16 flags at +0xc (DATA_SOURCE_CALLBACK_POLL) and, if set, calls the process function pointer at +8 as process(ds, 1). Returns at the end of the list. Called from the run loop main routine 0x0c05d108.

- Addresses by version: 219: 0x0C065A2C
- Called by: `ble_219_0c05d108`
- Confidence: high

## btstack_run_loop_embedded_process_timers

**Fire every expired timer at the head of the run loop timer list**

bthost_run_loop.c timer execution step, called from the host main loop 0c05d108 with the current time in ms. Loops on the head of DAT_200190ac: if the head's timeout (+4) is 0 it logs 'exception timeout is 0' (bthost_run_loop.c:105, level 2 via ble_hook_invoke_indexed), removes that timer with btstack_linked_list_remove and returns without calling it. Otherwise if timeout - now (util_sub_s32 = btstack_time_delta) is > 0 the head has not expired and, since the list is sorted, the function returns. Expired timers are unlinked and their process callback (+8) is called with the timer pointer; the head is re-read afterwards because callbacks may add or remove timers. Part of the embedded run loop group (0c065908 add, 0c0658d8 remove all, 0c0659b0 dump, 0c065a0c next delay).

| Parameter | Type | Description |
|---|---|---|
| `now_ms` | `u32` | current run loop time in milliseconds |

- Addresses by version: 219: 0x0C06595C
- Called by: `ble_219_0c05d108`
- Calls: `btstack_linked_list_remove`, `util_sub_s32`, `ble_hook_invoke_indexed`
- Confidence: high

## btstack_run_loop_embedded_remove_all_timers

**Unlink every timer from the run loop timer list at 0x200190ac**

Initialises a removal-safe btstack_linked_list_iterator on the timer list head DAT_200190ac and, while has_next, fetches the next timer and removes it with btstack_linked_list_remove. Timer callbacks are not invoked. Part of the BES bthost_run_loop.c port of the BTstack embedded run loop (with 0c065908 add, 0c06595c process, 0c0659b0 dump, 0c065a0c next delay). Single caller is the stack restart routine 0c059180 ('bts restart timer'), which drops all pending timeouts before re-initialising the host.

**Notes:** Contrary to the wave 1 guess for btstack_run_loop_embedded_init, 0x200190ac is the sorted timer list (bthost_run_loop.c), while 0x200190a4 is the deferred-callback queue popped by the main loop 0c05d108.

- Addresses by version: 219: 0x0C0658D8
- Called by: `ble_219_0c059180`
- Calls: `btstack_linked_list_remove`, `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: high

## btstack_run_loop_enable_data_source_callbacks

**Dispatch enable_data_source_callbacks via the active run loop**

Tail-calls function pointer at offset 0xc of the btstack_run_loop vtable whose address is held in DAT_200190b0, forwarding r0/r1 unchanged (ds, callback_types mask; callers pass 1 = POLL).

- Addresses by version: 219: 0x0C065A64
- Called by: `ble_evt_source_init`, `ble_msg_queues_init`
- Confidence: high

## btstack_run_loop_get_time_ms

**Dispatch get_time_ms via the active run loop**

Tail-calls vtable entry +0x28 of the run loop at DAT_200190b0 and returns its result in r0 (system time in milliseconds, used for timer timeouts and timestamps).

**Returns** `u32`: current time in ms (r0 of the callee; decompiler shows void)

**Notes:** Vtable slot assignment taken from the BTstack btstack_run_loop_t layout; entry +0x24 (dump_timer) is a separate wrapper.

- Addresses by version: 219: 0x0C065AC8
- Called by: `ble_219_0c05b5e4`, `ble_ctrl_conn_arm_timeout_timer`, `ble_ctrl_conn_idle_timeout_check`, `ble_ctrl_conn_alloc_and_register`, `ble_219_0c066c2c`, `ble_219_0c068da8`
- Confidence: medium

## btstack_run_loop_get_timer_context

**Read the context pointer of a timer source**

btstack_run_loop_get_timer_context(ts): returns the u32 at offset 0xc, normally fetched at the start of a timer handler.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | timer source |

**Returns** `ptr`: user context set earlier

- Addresses by version: 219: 0x0C065AA8
- Called by: `ble_ctrl_conn_idle_timeout_check`, `ble_ctrl_conn_timer_update_state`
- Confidence: high

## btstack_run_loop_init

**Select the run loop implementation and initialise it**

BTstack btstack_run_loop_init(run_loop): stores the btstack_run_loop vtable pointer in DAT_200190b0, then tail-calls its init method (vtable entry 0), which is btstack_run_loop_embedded_init for this image. Called from the stack bring-up function 0x0c05b67c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | run loop vtable (btstack_run_loop_t*) |

- Addresses by version: 219: 0x0C065AEC
- Called by: `ble_219_0c05b67c`
- Confidence: high

## btstack_run_loop_remove_data_source

**Dispatch remove_data_source via the active run loop**

Calls vtable entry +8 of the run loop at DAT_200190b0 with the incoming r0 (data source); the result of the call is not used.

- Addresses by version: 219: 0x0C065A7C
- Called by: `ble_evt_source_init`, `ble_msg_queues_init`
- Confidence: high

## btstack_run_loop_remove_timer

**Dispatch remove_timer via the active run loop**

Calls vtable entry +0x1c of the run loop at DAT_200190b0 with r0 (timer source); the return value (1 if the timer was removed) is ignored by this wrapper.

- Addresses by version: 219: 0x0C065AB8
- Called by: `app_req_timeout_timer_start`, `ble_219_0c04e398`, `ble_219_0c04e702`, `ble_host_timer_arm_30s`, `ble_219_0c04fc10`, `ble_host_timer_arm_interval`, `ble_219_0c050310`, `sm_pairing_step_complete`, `ble_219_0c051eb8`, `ble_219_0c051ef0`, `sm_link_poll_state`, `ble_219_0c052d30` ...
- Confidence: high

## btstack_run_loop_remove_timer_thunk

**Thunk: jump to btstack_run_loop_remove_timer (run-loop vtable slot +0x1c)**

Single-instruction tail thunk into btstack_run_loop_remove_timer, which dispatches through vtable slot +0x1c of the active run loop at DAT_200190b0 with r0 = timer source. Used by eight host/app routines (0c053018, 0c055268, 0c0554fc, 0c055524, 0c0555c8, 0c0573b8, 0c05952c, 0c059ac0) to cancel a pending timer; it is the stop counterpart of ble_host_timer_restart.

- Addresses by version: 219: 0x0C059ABC
- Called by: `ble_219_0c053018`, `ble_219_0c055268`, `ble_host_timers_stop_pair`, `ble_host_timer_set_enabled`, `ble_host_timer_stop_5min`, `ble_host_timer_cancel_130b0`, `ble_219_0c05952c`, `ble_219_0c059ac0`
- Calls: `btstack_run_loop_remove_timer`
- Confidence: high

## btstack_run_loop_set_data_source_handler

**Set the process callback of a data source**

btstack_run_loop_set_data_source_handler(ds, process): writes param_2 to btstack_data_source_t.process at offset 8 (same store as the timer variant, kept as a separate function). Used e.g. by 0x0c059134 and 0x0c05ad18 to register UART polling handlers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | data source (btstack_data_source_t*) |
| `param_2` | `ptr` | process callback (ds, callback_type) |

- Addresses by version: 219: 0x0C065A60
- Called by: `ble_evt_source_init`, `ble_msg_queues_init`
- Confidence: high

## btstack_run_loop_set_timer

**Dispatch set_timer via the active run loop**

Tail-calls vtable entry +0x14 of the run loop at DAT_200190b0, forwarding r0/r1 (timer source, timeout in ms). Called before add_timer when (re)arming HCI/L2CAP/SM/ATT timers.

- Addresses by version: 219: 0x0C065A98
- Called by: `app_req_timeout_timer_start`, `ble_219_0c04ec18`, `ble_host_timer_arm_30s`, `ble_host_timer_arm_interval`, `ble_219_0c050310`, `sm_pairing_step_complete`, `ble_219_0c051eb8`, `ble_219_0c051ef0`, `sm_link_poll_state`, `ble_219_0c052d30`, `ble_host_timer_restart`, `ble_ctrl_pending_drain_and_arm_timer` ...
- Confidence: high

## btstack_run_loop_set_timer_context

**Store a context pointer in a timer source**

btstack_run_loop_set_timer_context(ts, context): writes param_2 to btstack_timer_source_t.context at offset 0xc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | timer source |
| `param_2` | `ptr` | user context |

- Addresses by version: 219: 0x0C065AA4
- Called by: `ble_host_timer_arm_30s`, `ble_ctrl_conn_arm_timeout_timer`, `ble_ctrl_conn_alloc_and_register`, `ble_219_0c068da8`
- Confidence: high

## btstack_run_loop_set_timer_handler

**Set the callback of a timer source**

btstack_run_loop_set_timer_handler(ts, process): stores param_2 into btstack_timer_source_t.process at offset 8. Very many callers (HCI, L2CAP, SM, ATT timeouts) call it before set_timer/add_timer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | timer source (btstack_timer_source_t*) |
| `param_2` | `ptr` | timer handler function |

- Addresses by version: 219: 0x0C065A5C
- Called by: `app_req_timeout_timer_start`, `ble_219_0c04ec18`, `ble_host_timer_arm_30s`, `ble_host_timer_arm_interval`, `sm_init`, `ble_host_timer_restart`, `ble_ctrl_pending_drain_and_arm_timer`, `ble_ctrl_conn_arm_timeout_timer`, `ble_ctrl_conn_alloc_and_register`, `ble_219_0c0674e8`, `ble_219_0c068da8`, `ble_219_0c06cdb8` ...
- Confidence: high

## de_add_data

**BTstack sdp_util.c: append a variable-length element (string/UUID128/etc.) to a DE sequence**

data_size = co_read16_be(seq,1). If size < 256 a 2-byte header (type << 3 | DE_SIZE_VAR_8, then the length byte) is written at seq+3+data_size, otherwise a 3-byte header (type << 3 | DE_SIZE_VAR_16, big-endian length). If size > 0 the data is memcpy'd right after the header. The sequence length at seq+1 is updated to cover header and data. Caller: HID SDP record builder ble_219_0c04b788 (service name string DE_STRING=4, HID descriptor blob).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DE_DES sequence header |
| `param_2` | `u8` | de_type_t of the new element |
| `param_3` | `u16` | data length |
| `param_4` | `ptr` | data bytes |

- Addresses by version: 219: 0x0C04CAB8
- Called by: `ble_219_0c04b788`
- Calls: `co_read16_be`, `co_write16_be`, `memcpy`
- Confidence: high

## de_add_number

**BTstack sdp_util.c: append a fixed-size numeric element (8/16/32-bit) to a DE sequence**

data_size = co_read16_be(seq,1). Writes the descriptor byte (type << 3) | size_type at seq+3+data_size. For size type 1 (DE_SIZE_16) the value is stored big-endian at seq+4+data_size (element size 3); size type 2 (DE_SIZE_32) stores 32 bits (element size 5); size type 0 (DE_SIZE_8) with a non-NIL type stores one byte (element size 2); any other combination (including DE_NIL) contributes only the 1-byte descriptor. Finally the sequence length at seq+1 is increased by the element size (16-bit arithmetic). Caller: the HID SDP record builder ble_219_0c04b788 (e.g. de_add_number(seq, DE_UINT, DE_SIZE_16, 0x1124), DE_UUID 0x0100, DE_BOOL values).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DE_DES sequence header (VAR_16 length) |
| `param_2` | `u8` | de_type_t |
| `param_3` | `s32` | de_size_t: 0 = 8-bit, 1 = 16-bit, 2 = 32-bit |
| `param_4` | `u32` | value |

- Addresses by version: 219: 0x0C04CA50
- Called by: `ble_219_0c04b788`
- Calls: `co_read16_be`, `co_write16_be`, `co_write32_be`
- Confidence: high

## de_create_sequence

**BTstack sdp_util.c: start an empty DE_DES sequence with a 16-bit length field**

Writes header[0] = 0x36 ((DE_DES=6 << 3) | DE_SIZE_VAR_16=6) and a big-endian length of 0 at header+1 (co_write16_be), i.e. a 3-byte sequence header with no content. The length is later grown by de_add_number / de_add_data / de_pop_sequence. Called at the start of the HID SDP record builder ble_219_0c04b788 (hid_create_sdp_record: service class 0x1124, protocol list L2CAP 0x0100 / HIDP 0x0011, language base 0x656E, attributes 0x0201..0x020x).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | buffer that receives the sequence header |

- Addresses by version: 219: 0x0C04C9F4
- Called by: `ble_219_0c04b788`
- Calls: `co_write16_be`
- Confidence: high

## de_get_data_size

**BTstack sdp_util.c: payload size of an SDP data element from its descriptor byte**

Asserts header != NULL (btstack_assert -> software UDF trap). The size-type field header[0] & 7 selects: 5 (DE_SIZE_VAR_8) -> header[1]; 6 (DE_SIZE_VAR_16) -> big-endian u16 at header+1 (co_read16_be); 7 (DE_SIZE_VAR_32) -> big-endian u32 at header+1; otherwise 1 << size_type (1,2,4,8,16 bytes), except that a DE_NIL element (type field header[0] >> 3 == 0) has size 0. Part of the sdp_util DE (data element) group: de_get_len, de_get_len_safe (caller ble_219_0c04c8dc), de_traverse_sequence, de_add_number/data ...

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DE header byte(s) |

**Returns** `u32`: data size in bytes (without header)

- Addresses by version: 219: 0x0C04C580
- Called by: `de_get_len_safe`
- Calls: `co_read16_be`, `co_read32_be`
- Confidence: high

## de_get_len

**BTstack sdp_util.c: total length (header + data) of an SDP data element**

Returns 0 for a NULL pointer. Size types 0..4: header is 1 byte and the data is 1 << size_type bytes (0 for DE_NIL, i.e. type field header[0]>>3 == 0). DE_SIZE_VAR_8 (5): header[1] + 2; DE_SIZE_VAR_16 (6): co_read16_be(header,1) + 3; DE_SIZE_VAR_32 (7): co_read32_be(header,1) + 5. Equivalent to de_get_header_size + de_get_data_size. Used by the DE traversal and builder helpers (de_traverse_sequence, sdp_attribute_list_traverse_sequence, de_push_sequence, de_pop_sequence) and by the SDP record handling in ble_219_0c04c780/0c04c89c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DE header |

**Returns** `s32`: element length in bytes, 0 for NULL

- Addresses by version: 219: 0x0C04C5B8
- Called by: `de_traverse_sequence`, `sdp_attribute_list_traverse_sequence`, `sdp_attribute_write_fragment`, `sdp_attribute_add_length`, `de_push_sequence`, `de_pop_sequence`
- Calls: `co_read16_be`, `co_read32_be`
- Confidence: high

## de_get_len_safe

**BTstack sdp_util.c: element length bounded by the available buffer size, 0 if it does not fit**

Returns 0 if size == 0. Header size is 1, or 1 + (1 << (size_type-5)) for size types 5..7, and must not exceed size. Then de_get_data_size (ble_219_0c04c580, which asserts the pointer) is called; the result is header + data only if data <= size and header + data <= size, else 0. Used by the SDP server request parsers ble_219_0c04be10 (ServiceSearch), 0c04bfd0 (ServiceAttribute) and 0c04c144 (ServiceSearchAttribute) to validate the incoming search pattern / attribute id list before traversal.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DE header |
| `param_2` | `u32` | bytes available from header |

**Returns** `u32`: element length, or 0 if truncated

- Addresses by version: 219: 0x0C04C8DC
- Called by: `sdp_server_build_service_search_response`, `sdp_server_build_service_attribute_response`, `sdp_server_build_service_search_attribute_response`
- Calls: `de_get_data_size`
- Confidence: high

## de_get_normalized_uuid

**BTstack sdp_util.c: convert a DE_UUID element (16/32/128-bit) into a 128-bit UUID**

Returns 0 for NULL or if the element type (header[0] >> 3) is not 3 (DE_UUID). Size type 1 (DE_SIZE_16): big-endian u16 at +1; size type 2 (DE_SIZE_32): big-endian u32 at +1; either is expanded into the Bluetooth Base UUID with uuid_add_bluetooth_prefix and 1 is returned. Size type 4 (DE_SIZE_128): the 16 bytes at +1 are copied verbatim to param_1 (four unaligned word loads) and 1 is returned. Other size types give 0. No direct callers; used through the SDP traversal callbacks (e.g. the UUID matcher ble_219_0c04c680).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | out: 16-byte UUID128 |
| `param_2` | `ptr` | DE_UUID element |

**Returns** `u32`: 1 on success, 0 if not a UUID element

- Addresses by version: 219: 0x0C04C914
- Calls: `co_read16_be`, `co_read32_be`, `uuid_add_bluetooth_prefix`
- Confidence: high

## de_pop_sequence

**BTstack sdp_util.c: close a nested sequence by adding its length to the parent's length field**

child_len = de_get_len(child) (ble_219_0c04c5b8); parent_len = co_read16_be(parent,1); co_write16_be(parent, 1, parent_len + child_len). Both lengths are handled as 16-bit values. Counterpart of de_push_sequence; called from the HID SDP record builder ble_219_0c04b788 after each nested list is filled.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | parent DE_DES header |
| `param_2` | `ptr` | child DE_DES header previously returned by de_push_sequence |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | unused register pass-through |

- Addresses by version: 219: 0x0C04CA28
- Called by: `ble_219_0c04b788`
- Calls: `de_get_len`, `co_read16_be`, `co_write16_be`
- Confidence: high

## de_push_sequence

**BTstack sdp_util.c: open a nested DE_DES inside a sequence and return its header pointer**

Computes the current length of the parent element with de_get_len (ble_219_0c04c5b8), writes a new 0x36 (DE_DES, VAR_16) header with length 0 at parent + len (co_write16_be) and returns that address. The parent's own length is not changed until de_pop_sequence (ble_219_0c04ca28) is called with the returned child. Called repeatedly by the HID SDP record builder ble_219_0c04b788.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | parent DE_DES header |

**Returns** `ptr`: pointer to the new child sequence header

- Addresses by version: 219: 0x0C04CA00
- Called by: `ble_219_0c04b788`
- Calls: `de_get_len`, `co_write16_be`
- Confidence: high

## de_store_descriptor_with_len

**BTstack sdp_util.c: write a DE header byte plus its 8/16/32-bit length field**

header[0] = (type << 3) | size_type. For size type 5 (DE_SIZE_VAR_8) header[1] = len; for 6 (DE_SIZE_VAR_16) co_write16_be(header,1,len & 0xffff); for 7 (DE_SIZE_VAR_32) co_write32_be(header,1,len); fixed-size types write only the descriptor byte. Callers: the SDP server response builders ble_219_0c04bfd0 and 0c04c144 (attribute lists); the inlined equivalents appear in de_create_sequence, de_push_sequence and de_add_data.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination header |
| `param_2` | `u8` | de_type_t (0 NIL,1 UINT,2 INT,3 UUID,4 STRING,5 BOOL,6 DES,7 DEA,8 URL) |
| `param_3` | `s32` | de_size_t (0..4 fixed 1/2/4/8/16 bytes, 5/6/7 variable 8/16/32-bit length) |
| `param_4` | `u32` | data length for variable size types |

- Addresses by version: 219: 0x0C04C9CC
- Called by: `sdp_server_build_service_attribute_response`, `sdp_server_build_service_search_attribute_response`
- Calls: `co_write16_be`, `co_write32_be`
- Confidence: high

## de_traverse_sequence

**BTstack sdp_util.c: call a handler for every element of a DE sequence (DE_DES)**

Returns unless the element type (header[0] >> 3) is 6 (DE_DES). Skips the header (1 byte, or 1 + (1 << (size_type-5)) for the variable-length size types) and iterates from there to de_get_len(element): for each sub-element it calls handler(element+pos, type, size_type, context) and stops when the handler returns non-zero; otherwise it advances by de_get_len(sub-element). The decompiled call passes a 5th register argument that is just pass-through. Callers: SDP record attribute lookup / service search helpers ble_219_0c04c680, 0c04c780, 0c04c89c and the UUID-in-record matcher ble_219_0c04cb90 (sdp_record_contains_UUID128 style).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DE_DES element |
| `param_2` | `ptr` | de_traversal_callback_t handler(element, type, size, context) returning non-zero to stop |
| `param_3` | `ptr` | opaque context for the handler |
| `param_4` | `u32` | unused register pass-through |

- Addresses by version: 219: 0x0C04C620
- Called by: `sdp_pattern_uuid_match`, `sdp_attribute_write_fragment`, `sdp_attribute_add_length`, `sdp_record_matches_pattern`
- Calls: `de_get_len`
- Confidence: high

## hal_time_ms

**BTstack run-loop port: current time in milliseconds derived from the FreeRTOS tick count**

Reads xTaskGetTickCount(), multiplies by 1000 as a 64-bit value and divides it by 1000 with the 64-bit divide helper 0x0c06fec0 (__udivmoddi4 wrapper), i.e. ticks * 1000 / configTICK_RATE_HZ with a 1 kHz tick, so the result equals the tick count in milliseconds. Single caller is the embedded run-loop execute routine 0x0c05d108, matching BTstack's btstack_run_loop_embedded_get_time_ms() -> hal_time_ms() hook. The decompiler shows no return but the quotient is left in r0/r1.

**Returns** `u32`: milliseconds since scheduler start (low word of the 64-bit quotient)

- Addresses by version: 219: 0x0C045494
- Called by: `ble_219_0c05d108`
- Calls: `xTaskGetTickCount`, `__udivdi3`
- Confidence: medium

## hci_add_event_handler

**Register a packet handler on the event-handler list at env+0x20**

Appends the registration entry to the list at env+0x20 through btstack_linked_list_add_tail (thunk 0x0C065416). hci_emit_event later calls the entry's callback at +4 for every event. The name matches the BTstack function of the same purpose.

| Parameter | Type | Description |
|---|---|---|
| `registration` | `ptr` | packet handler registration; callback at +4 |

- Addresses by version: 219: 0x0C066DBC
- Called by: `att_server_init`, `sm_init`, `ble_219_0c059230`, `ble_219_0c0592a4`, `ble_219_0c065148`, `ble_219_0c06d474`
- Calls: `btstack_linked_list_add_tail`
- Confidence: high

## hci_cmd_pack_format

**Pack an HCI command payload from a per-opcode format string and argument words**

Writes an HCI command into param_1: the u16 opcode from the descriptor at param_2+0 (little-endian), then the payload driven by the format string at param_2+4, one code per argument word (group items take pointers). Codes: '1' u8; '2' or 'H' u16; '3' u24; '4' u32; 'B' 6-byte BD_ADDR reversed; 'D' 8 bytes; 'K' 16 bytes reversed; 'P' 16 bytes; 'Q' 32 bytes reversed; 'A' 31-byte block; 'E' 240-byte block; 'N' string padded with zeros to 248 bytes; 'J' length byte followed by 'V' variable block of that length; '[' ... ']' group repeated a count set by 'a' (the value) or 'b' (popcount of the value). Unknown codes are skipped without consuming an argument. The payload size is stored at param_1[2] and the total byte count including the 3-byte header is returned. Group: HCI and L2CAP packet builders (see l2cap_signaling_pdu_build).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output buffer, at least 3 + payload bytes |
| `param_2` | `ptr` | descriptor: u16 opcode at +0, const u8 *format at +4 |
| `param_3` | `ptr` | u32 argument words, consumed in format order |

**Returns** `u32`: total bytes written, including the 3-byte header (opcode u16 + length byte)

**Notes:** The HCI-command reading comes from the 3-byte header layout (opcode plus parameter length). The 'J'/'V' and '['..']' pairings are read from the decompile. The per-opcode format tables are not in this packet.

- Addresses by version: 219: 0x0C06BC74
- Called by: `ble_219_0c067178`
- Calls: `co_write16_le`, `co_reverse_copy_n`, `co_popcount32`, `memcpy`, `memset`, `strlen`
- Confidence: medium

## hci_emit_event

**Deliver an internal HCI event buffer to every registered event handler**

Walks the event-handler list at env+0x20 (entries added by hci_add_event_handler, callback at entry+4) with the removal-safe iterator. Each callback is called as callback(4, 0, packet, size), where 4 is the HCI event packet type in BTstack and 0 is the channel. The buffer is not copied, so it must remain valid for the synchronous call. Almost every state change in this packet is reported through it, using the internal event codes 0x61, 0x62, 0x73, 0xD8, 0xD9, 0xE0, 0xE1 and 0x6F.

| Parameter | Type | Description |
|---|---|---|
| `packet` | `ptr` | event buffer: code byte, parameter length, parameters |
| `size` | `s32` | buffer length in bytes |

- Addresses by version: 219: 0x0C066004
- Called by: `ble_219_0c052de8`, `ble_ctrl_conn_set_pending_notify`, `ble_ctrl_conn_clear_pending_notify`, `ble_ctrl_conn_idle_timeout_check`, `hci_power_control_on`, `ble_ctrl_conn_key_size_check`, `ble_ctrl_conn_free_and_report_disconnect`, `ble_ctrl_conn_teardown_and_count`, `ble_219_0c06648c`, `ble_219_0c066c2c`, `ble_219_0c066f74`, `ble_219_0c067178` ...
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: high

## hci_number_free_acl_slots

**Return free ACL packet slots for an address-type class**

Computes free host-to-controller packet slots from the buffer totals: the classic ACL total at env+0x178 and the LE total at env+0x17F. Outstanding packets are summed over the connection list from the per-connection byte at +0x194, counted against the classic total for type 0xFD and against the LE total for types below 4. Selector 0xFD returns the classic free count, selector 0 returns the LE free count (or the shared classic count when the LE total is zero), and selector 0xFE is rejected as an unknown address type. Negative results log an error (hci.c lines 0x259, 0x261, 0x268, 0x26F) and return 0.

| Parameter | Type | Description |
|---|---|---|
| `addr_type` | `u8` | address-type selector: 0 for LE, 0xFD for classic, 0xFE rejected |

**Returns** `u16`: number of free packet slots, 0 on error

**Notes:** Selector constants inferred from the code paths. The packet-count byte +0x194 and the buffer totals are inferred from usage.

- Addresses by version: 219: 0x0C0666E4
- Called by: `ble_219_0c052de8`, `ble_ctrl_can_send_le_acl`, `ble_ctrl_can_send_to_handle`, `ble_ctrl_can_send_br_edr_acl`
- Calls: `ble_hook_invoke_indexed`
- Confidence: medium

## hci_power_control_on

**Power the controller on, run HCI_INIT, and emit event 0x62 when it fails**

Calls the power-on hook at control struct env[3]+4 when present; on failure it logs 'POWER_ON failed' (hci.c line 0x12E9) and skips to the failure exit. On success it calls the optional pre-init hook at env[2]+4, then the table entry env[0]+4 with env[1], then HCI_INIT through env[0]+8. If HCI_INIT fails it logs 'HCI_INIT failed, turning Bluetooth off again' (hci.c 0x12FB) and calls the power-off hook env[3]+8. On any failure it emits the 2-byte event 0x62 0x00 with hci_emit_event and returns the failure code; on success it returns 0 without the event.

**Returns** `s32`: 0 on success, otherwise the failing step's nonzero return code

**Notes:** The control structs at env[2] and env[3] are not described; their +4/+8 slots are read as hooks from the code.

- Addresses by version: 219: 0x0C0661E8
- Called by: `ble_219_0c068da8`, `ble_219_0c06b048`
- Calls: `hci_emit_event`, `ble_hook_invoke_indexed`
- Confidence: high

## hci_release_packet_buffer_thunk

**Thunk: jump to ll_env_clear_flag_170 to release the HCI packet buffer flag**

A one-instruction tail jump to 0x0C066C1C (ll_env_clear_flag_170), which writes 0 to the byte at controller env +0x170. It is the release side of hci_reserve_packet_buffer (0x0C066BE8) and performs no check.

**Notes:** Caller 0c04e398.

- Addresses by version: 219: 0x0C06D5D8
- Called by: `ble_219_0c04e398`
- Calls: `ll_env_clear_flag_170`
- Confidence: high

## hci_remove_event_handler

**Unregister a packet handler from the event-handler list at env+0x20**

Unlinks the registration from the event-handler list at env+0x20 with btstack_linked_list_remove. Pair of hci_add_event_handler.

| Parameter | Type | Description |
|---|---|---|
| `registration` | `ptr` | packet handler registration to remove |

- Addresses by version: 219: 0x0C066DCC
- Called by: `ble_219_0c0592a4`
- Calls: `btstack_linked_list_remove`
- Confidence: high

## hci_reserve_packet_buffer

**Reserve the single outgoing packet buffer by setting env+0x170**

If the reserved-buffer byte env+0x170 is clear, it sets it to 1 and returns 1. Otherwise it logs 'hci_reserve_packet_buffer called but buffer already reserved' (hci.c line 0x2F5) and returns 0. The flag is cleared by ll_env_clear_flag_170 and read by ll_env_get_flag_170.

**Returns** `u32`: 1 when the buffer was reserved, 0 when it was already reserved

- Addresses by version: 219: 0x0C066BE8
- Called by: `ble_219_0c06c7ac`, `ble_219_0c06cb3c`, `hci_reserve_packet_buffer_thunk`, `ble_219_0c06d648`, `ble_219_0c06ed64`
- Calls: `ble_hook_invoke_indexed`
- Confidence: high

## hci_reserve_packet_buffer_thunk

**Thunk: jump to the HCI packet-buffer reserve routine at 0x0C066BE8**

A one-instruction tail jump to 0x0C066BE8 (hci_reserve_packet_buffer, named in wave2_batch10). The target sets the byte at controller env +0x170 to 1 and returns 1 when it was 0; otherwise it logs 'hci_reserve_packet_buffer called but buffer already reserved' (hci.c line 757) through ble_hook_invoke_indexed channel 2 and returns 0. The release counterpart is hci_release_packet_buffer_thunk at 0x0C06D5D8.

**Returns** `u32`: 1 when the buffer was claimed, 0 when it was already claimed

**Notes:** The decompiled body shown in the packet is the target at 0x0C066BE8, already described in wave2_batch10. The flag byte at +0x170 is the one read by ll_env_get_flag_170.

- Addresses by version: 219: 0x0C06D5D4
- Called by: `ble_219_0c04e398`, `ble_219_0c04ebc0`, `ble_219_0c04ec18`
- Calls: `hci_reserve_packet_buffer`
- Confidence: high

## hci_stream_buffer_is_empty

**Return true when the 5 KB HCI stream buffer holds no bytes**

Calls ringbuf_used_count on the FreeRTOS stream-buffer handle DAT_2000f2b0 and returns count == 0. The handle is created in the HCI 'intersys' transport open routine 0x0c04542c with xStreamBufferGenericCreateStatic(0x1400 bytes, trigger level 1, storage 0x2000de8c) and is filled by xStreamBufferSend in 0x0c045518. Used by the transport poll routine 0x0c05d40e to decide whether a pending read callback (0x0c05d2f4) must run.

**Returns** `bool`: true if no HCI bytes are buffered

- Addresses by version: 219: 0x0C045534
- Called by: `ble_219_0c05d40e`
- Calls: `ringbuf_used_count`
- Confidence: medium

## hci_stream_buffer_receive_nowait

**Non-blocking read of up to N bytes from the global HCI stream buffer DAT_2000F2B0**

Calls the stream buffer receive routine (0x0C0436F8, xStreamBufferReceive) on the global HCI stream buffer handle DAT_2000F2B0 with a zero timeout, so it returns at once with whatever bytes are present, or 0 when empty. The receive side runs as a consumer; this is the read entry used by the HCI transport.

| Parameter | Type | Description |
|---|---|---|
| `pvRxData` | `ptr` | destination buffer |
| `xBufferLengthBytes` | `u32` | destination size in bytes |

**Returns** `u16`: bytes read

**Notes:** The earlier note on hci_stream_buffer_is_empty (0x0C045534) says this routine fills the buffer through xStreamBufferSend. The decompiled call is to the receive side (prvReadBytesFromBuffer), so that earlier description should be checked.

- Addresses by version: 219: 0x0C045518
- Called by: `ble_219_0c05d2f4`
- Calls: `xStreamBufferReceive`
- Confidence: high

## hci_transport_h4_rx_advance

**Advance the H4 UART receive state machine by the bytes just received**

Called after each receive chunk: the count requested last time (DAT_20019328) is added to the buffer offset DAT_20019448, then state DAT_2001932A selects the next step. State 0 (idle) stops; state 1 reads the H4 packet-type byte at DAT_20019334 and moves to state 2 for event (type 4, 2-byte header), state 3 for ACL (type 2, 4-byte header, u16 length at offset 3, at most 255 bytes) or state 4 for SCO (type 3, 3-byte header, length byte at offset 3); any other type is logged as invalid. State 6 hands the complete packet (type, payload, length) to the upper-layer callback at DAT_2000499C and returns to state 1 expecting one type byte. Each step asks the UART driver (ops table DAT_20019324, slot +0x20) to receive the next N bytes at buffer+offset; errors are logged through ble_hook_invoke_indexed channel 2.

**Notes:** State 5 (ISO header, 14-bit length with bits 8..13 required to be zero) is implemented, but no transition into it appears in this function, since types other than 2, 3 and 4 are rejected. The UART ops table and the upper callback are globals with no names yet. Callers: none direct (invoked from the UART receive path).

- Addresses by version: 219: 0x0C06C2E0
- Calls: `co_read16_le`, `ble_hook_invoke_indexed`
- Confidence: medium

## hid_report_id_status

**BTstack hid_device.c: classify a HID report ID as VALID (1), INVALID (2) or UNDECLARED (0)**

If the single hid_device instance (cid at DAT_2000fa10) matches param_1 and its protocol_mode byte DAT_2000fa2a is 0 (HID_PROTOCOL_MODE_BOOT), report IDs 1 (boot keyboard) and 2 (boot mouse) return HID_REPORT_ID_VALID=1, anything else HID_REPORT_ID_INVALID=2. A cid mismatch logs 'hid_device_in_boot_protocol_mode: could not find hid device instace' (hid_device.c:982) via ble_hook_invoke_indexed and falls through to report-mode handling. In report mode the HID descriptor DAT_2000fa08 of length DAT_2000fa0c is walked with btstack_hid_parse_descriptor_item: a Global item (type 1) with tag 8 (Report ID) equal to param_2 gives 1; if report IDs were declared but none matched, 2; if the descriptor declares no report ID (or is empty), 0. Caller: hid_device SET_REPORT / data handling (ble_219_0c04afcc), together with hid_report_size_valid (ble_219_0c04af54/0c04af5a).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | HID cid |
| `param_2` | `u16` | report ID |

**Returns** `u32`: hid_report_id_status_t: 0 undeclared, 1 valid, 2 invalid

- Addresses by version: 219: 0x0C04AF00
- Called by: `ble_219_0c04afcc`
- Calls: `btstack_hid_parse_descriptor_item`, `ble_hook_invoke_indexed`
- Confidence: high

## hid_report_size_valid_body

**BTstack hid_report_size_valid body (entered after the size!=0 check at 0x0C04AF54)**

Second half of hid_device.c hid_report_size_valid(cid, report_id, report_type, report_size): Ghidra split the function at the point after the 'report_size == 0 -> false' test, so ble_219_0c04af54 is the real entry and falls into this address. In boot protocol mode (DAT_2000fa10 == cid, protocol_mode byte DAT_2000fa2a == 0) report ID 1 (keyboard) needs size >= 8 and report ID 2 (mouse) size >= 1; other IDs are invalid. A cid mismatch logs 'hid_device_in_boot_protocol_mode: could not find hid device instace' (hid_device.c:982) and continues. Otherwise btstack_hid_get_report_size_for_id (ble_219_0c065288) computes the expected size for (report_id, report_type) from the descriptor DAT_2000fa08 / DAT_2000fa0c and the size is valid only if it is non-zero and equals param_4. Group: hid_report_id_status (ble_219_0c04af00), caller ble_219_0c04afcc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | HID cid |
| `param_2` | `s32` | report ID |
| `param_3` | `u32` | hid_report_type_t (1 input, 2 output, 3 feature) |
| `param_4` | `s32` | report size in bytes (non-zero) |

**Returns** `bool`: true if the size is valid for the report

**Notes:** Not a standalone function in the source; it is the tail of ble_219_0c04af54.

- Addresses by version: 219: 0x0C04AF5A
- Called by: `ble_219_0c04af54`
- Calls: `btstack_hid_get_report_size_for_id`, `ble_hook_invoke_indexed`
- Confidence: high

## l2cap_channel_emit_event_70

**Emit vendor event 0x70 (26 bytes) describing an L2CAP channel with a sub-code**

Builds an H4 event with code 0x70 and parameter length 24: byte 2 is the sub-code param_2, bytes 3..8 the byte-reversed peer address at channel +0x26, and u16 values from +0x24, +0x38, the CID at +0x06, +0x30, +0x32, +0x34 and +0x36 at offsets 9, 11, 13, 15, 17, 19 and 21. Byte 23 is bit 15 of the u16 at +0x22, and bytes 24 and 25 are zero. It is sent through ble_hook_invoke4(4, 1, ...) and then to the channel callback at +0x08 with (4, CID, buffer, 26). Group: vendor H4 event emitters; L2CAP channel management.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | L2CAP channel record (CID at +0x06, callback at +0x08, peer address at +0x26) |
| `param_2` | `u8` | sub-code byte written at event offset 2 |

**Notes:** Event code 0x70 is an inference. Callers 0c06c74c (sub-code 0x69), 0c06c83c, 0c06cdb8, 0c06d9b0.

- Addresses by version: 219: 0x0C06C5AC
- Called by: `l2cap_channel_timer_teardown`, `l2cap_channels_teardown_by_addr`, `ble_219_0c06cdb8`, `ble_219_0c06d9b0`
- Calls: `co_write16_le`, `co_reverse_copy_6`, `ble_hook_invoke4`
- Confidence: medium

## l2cap_channel_get_u16_34_by_cid

**Return the u16 at +0x34 of the L2CAP channel with a given local CID**

Returns 0 for CIDs below 0x40 (the dynamic CID range starts there). Otherwise it searches the channel list at 0x2001944C for the channel whose CID at +0x06 equals param_1 and returns its u16 at +0x34, which l2cap_create_channel_entry sets to 0x2A0; it returns 0 when no channel matches. Group: L2CAP channel lookups by CID.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | local CID |

**Returns** `u16`: value at +0x34, or 0

**Notes:** Field +0x34 is a 16-bit parameter, probably an MTU or MPS; the name is not confirmed. Caller not in this packet.

- Addresses by version: 219: 0x0C06EC54
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: medium

## l2cap_channel_set_context_by_cid

**Store a context pointer in the L2CAP channel with a given CID (CIDs 0..0x3F)**

Returns immediately for CIDs above 0x3F. Otherwise it searches the channel list at 0x2001944C for a channel whose CID at +0x06 equals param_2 and stores param_1 at its +0x08 (the callback/context slot). Nothing happens when no channel matches. Group: L2CAP channel lookups by CID.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | context value stored at +0x08 |
| `param_2` | `u32` | CID; only values up to 0x3F are searched |

**Notes:** The range check is the reverse of l2cap_channel_get_u16_34_by_cid (which searches CIDs of 0x40 and above), so the list may also hold fixed-CID records. Not confirmed.

- Addresses by version: 219: 0x0C06F03C
- Called by: `ble_sink_init`, `sm_init`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`
- Confidence: medium

## l2cap_channel_timer_teardown

**Timer callback: tear down the L2CAP channel that owns the expired timer**

Looks up the channel in the L2CAP list at 0x2001944C (state 0, 2 or 5) whose embedded timer at +0x10 equals param_1; returns if none matches. For the match it emits event 0x70 with sub-code 0x69 (l2cap_channel_emit_event_70), unlinks the channel with btstack_linked_list_remove, removes the timer from the run loop with btstack_run_loop_remove_timer, and returns the block to the pool with btstack_memory_l2cap_channel_free. Group: L2CAP channel teardown (with l2cap_channels_teardown_by_addr).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | BTstack timer source embedded at channel +0x10 |

**Notes:** Used as a timer callback; no direct callers in the packet.

- Addresses by version: 219: 0x0C06C74C
- Calls: `btstack_linked_list_remove`, `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`, `btstack_memory_l2cap_channel_free`, `btstack_run_loop_remove_timer`, `l2cap_channel_emit_event_70`
- Confidence: high

## l2cap_channels_teardown_by_addr

**Tear down all L2CAP channels to a peer address, emitting event 0x70 with a code**

First pass: every channel in the L2CAP list (0x2001944C) that is in state 0, 2 or 5 and whose peer address at +0x26 equals the 6-byte address param_1 has sub-state 2 or 3 at +0x20 changed to 0x18 (0x0C065B24 returns 0 on a match). Second pass: while a channel with sub-state 0x18 remains, it emits event 0x70 with sub-code param_2, unlinks the channel, removes its timer at +0x10 from the run loop and frees the block. Channels in other sub-states are kept. Group: L2CAP channel teardown (with l2cap_channel_timer_teardown).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 6-byte BD address to match |
| `param_2` | `u8` | sub-code passed to the event 0x70 (l2cap_channel_emit_event_70) |

**Notes:** 0x0C065B24 is not named in this packet; its use (the loop breaks when it is non-zero) implies it returns 0 for a matching address, like memcmp. Caller: none direct (teardown path).

- Addresses by version: 219: 0x0C06C83C
- Calls: `btstack_linked_list_remove`, `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`, `btstack_memory_l2cap_channel_free`, `btstack_run_loop_remove_timer`, `bd_addr_cmp`, `l2cap_channel_emit_event_70`
- Confidence: medium

## l2cap_coc_rx_segment

**Consume an LE credit and reassemble one L2CAP credit-based SDU segment**

Decrements the remaining-credit counter at channel +0x56; at zero the sub-state at +0x20 becomes 0x12 and the segment is dropped. When fewer than 5 credits remain and the flag byte at +0x58 is set, the counter at +0x54 is reloaded to 5. A PDU of exactly 8 bytes (headers only) is ignored. A segment that starts an SDU reads its u16 SDU length at buffer offset 8, is dropped when it exceeds the channel MTU at +0x32, and otherwise stores the length at +0x44, resets the received count at +0x46 and copies the payload into the SDU buffer at +0x40. Continuation segments are appended at the received offset; when the received count reaches the SDU length, the channel callback at +0x08 is called with (6, id at +0x06, SDU buffer) and +0x44 is cleared. Group: L2CAP LE credit-based flow control.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | channel record (credits at +0x54/+0x56, MTU +0x32, SDU state +0x40..+0x46, callback +0x08) |
| `param_2` | `ptr` | PDU buffer, starting at the HCI ACL header |
| `param_3` | `u32` | PDU length in bytes |
| `param_4` | `u32` | appears only as an extra argument to the 16-bit read; no visible effect |

**Notes:** The first-segment rule assumes the 4-byte ACL and 4-byte L2CAP basic headers precede the SDU length at offset 8. The copy-length argument of the memcpy is not visible in the decompile. Callers are not in this packet.

- Addresses by version: 219: 0x0C06C964
- Called by: `ble_219_0c06dc56`
- Calls: `co_read16_le`, `memcpy`
- Confidence: medium

## l2cap_create_channel_entry

**Allocate an L2CAP channel from the pool, set its fields and pick a free local CID**

Takes a block from the L2CAP channel pool (btstack_memory_l2cap_channel_get) and returns 0 when the pool is empty. It stores param_1 as the context pointer at +0x08, param_2 as the state byte at +0x04, the peer address (param_3) copied to +0x26, param_4 (u8) at +0x2C, param_5 (u16) at +0x38, param_6 (u16 MTU) at +0x32, param_7 (u8) at +0x3A, and the default 0x2A0 (672) at +0x34. A local CID is taken from the counter at 0x200194A4: 0x40 upward, wrapping from 0xFFFE to 0x40, skipping any CID already used in the channel list. The channel gets sub-state 2 at +0x20, unassigned handle 0xFFFF at +0x24, and cleared bytes at +0x22, +0x2D and +0x2E; it is not linked into the list here. Group: L2CAP channel management.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | context pointer stored at +0x08 |
| `param_2` | `u8` | state value stored at +0x04 |
| `param_3` | `ptr` | 6-byte peer BD address, copied to +0x26 |
| `param_4` | `u8` | stored at +0x2C |
| `param_5` | `u16` | stored at +0x38 |
| `param_6` | `u16` | MTU stored at +0x32 |
| `param_7` | `u8` | stored at +0x3A |

**Returns** `ptr`: new channel record, or NULL when the pool is empty

**Notes:** The name matches the wave-1 note on btstack_memory_l2cap_channel_get, which cites this function as the l2cap.c constructor. Callers 0c06dc56, 0c06ee70 (not in this packet). The meaning of the default 0x2A0 at +0x34 is not confirmed.

- Addresses by version: 219: 0x0C06CD00
- Called by: `ble_219_0c06dc56`, `ble_219_0c06ee70`
- Calls: `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`, `btstack_memory_l2cap_channel_get`, `bd_addr_copy`
- Confidence: medium

## l2cap_register_service

**Register an L2CAP service (PSM, MTU, security) and refresh the env security level**

Rejects a PSM already in the service list at 0x200194B0 (logs 'register: PSM %u already registered', l2cap.c line 4814) and returns 0x6B. Otherwise it allocates an l2cap_service_t (btstack_memory_l2cap_service_get; on failure it logs and returns 0x56), stores the PSM at +4, the MTU at +6, the handler context at +8 and the security level at +0x0C, and inserts it at the head of the list with btstack_linked_list_add. It then takes the highest security level over all services (at least 1) and stores it at controller env +0x59 through ble_ctrl_env_set_u8_at_0x59; it returns 0 on success.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | handler / context pointer, stored at +8 |
| `param_2` | `u32` | PSM |
| `param_3` | `u16` | MTU, stored at +6 |
| `param_4` | `u8` | security level, stored at +0x0C |

**Returns** `u32`: 0 on success, 0x6B when the PSM is already registered, 0x56 when out of memory

**Notes:** Matches BTstack l2cap_register_service. Callers 0c04bb00, 0c04bd48.

- Addresses by version: 219: 0x0C06F078
- Called by: `ble_219_0c04bb00`, `ble_219_0c04bd48`
- Calls: `btstack_linked_list_add`, `btstack_linked_list_iterator_init`, `btstack_linked_list_iterator_has_next`, `btstack_linked_list_iterator_next`, `btstack_memory_l2cap_service_get`, `ble_ctrl_env_set_u8_at_0x59`, `ble_hook_invoke_indexed`
- Confidence: high

## l2cap_signaling_pdu_build

**Build an L2CAP signalling command PDU from a per-code format string**

Writes the ACL header (u16 at +0: connection handle param_2 with PB/BC flags param_3 in the top four bits), the L2CAP basic header (length at +4, CID param_4 at +6) and the signalling header (code param_5 at +8, identifier param_6 at +9, data length at +10). The payload layout comes from the format string at table 0x0C082190 indexed by code-1: 'C' writes a list of u16 values read from a pointer until 0xFFFF, 'D' copies a (pointer, length) block, and '2' writes one u16 argument; with an empty format the command is header-only (12 bytes). The length fields are filled in at the end and the total byte count is returned. Group: HCI and L2CAP packet builders (see hci_cmd_pack_format).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output buffer |
| `param_2` | `u16` | ACL connection handle (12 bits) |
| `param_3` | `s16` | packet boundary / broadcast flags (4 bits) |
| `param_4` | `u32` | L2CAP CID |
| `param_5` | `u8` | signalling command code (1-based index into the format table) |
| `param_6` | `u8` | command identifier |
| `param_7` | `ptr` | argument words, consumed in format order |

**Returns** `u32`: total bytes written

**Notes:** Format letters are read from the decompile; the table contents at 0x0C082190 are not in this packet. Callers: ble_219_0c06c7ac (not in this packet).

- Addresses by version: 219: 0x0C06F12C
- Called by: `ble_219_0c06c7ac`
- Calls: `co_write16_le`, `memcpy`
- Confidence: medium

## le_device_db_tlv_add

**Insert or update an LE device DB entry (identity address and IRK) in TLV storage**

Searches the 4 slots (in-use bytes DAT_2000fd04..07) for a used record with the same address type (param_1) and 6-byte address (param_2) and reuses it. Otherwise it takes a free slot and increments the entry count DAT_2000fd10; when all slots are used it overwrites the slot with the smallest sequence number (LRU). The 60-byte record at tag 0x42544400|slot ('BTD'+slot) holds: u32 sequence number at +0 (previous maximum + 1), u32 address type at +4, 6-byte address at +8, 16-byte IRK (param_3) at +14, and zeros at +30..+59 (encryption data cleared). It is written through the backend write function (vtable +4); the in-use byte is set only on success, otherwise 'tag store failed' is logged (le_device_db_tlv.c line 0xe8) and -1 is returned.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | address type, compared with and stored at record +4 |
| `param_2` | `ptr` | 6-byte identity address |
| `param_3` | `ptr` | 16-byte IRK |

**Returns** `s32`: slot index 0..3, or -1 on failure

**Notes:** The IRK name comes from the 16-byte field at +14, which le_device_db_tlv_read_identity returns with the identity address.

- Addresses by version: 219: 0x0C04ED28
- Called by: `sm_device_db_resolve_peer`
- Calls: `util_nop_stub_b`, `ble_hook_invoke_indexed`, `memcmp`, `memset`
- Confidence: medium

## le_device_db_tlv_check_init

**Log an error when the LE device DB TLV backend has not been installed**

Returns at once if the TLV backend pointer DAT_2000fd0c is set. Otherwise it logs '%s:%u: bthost_tlv not initialized' (file le_device_db_tlv.c, line 0x81) through ble_hook_invoke_indexed with level 2, and returns without stopping the caller. The backend is installed by le_device_db_tlv_configure.

- Addresses by version: 219: 0x0C04ECC0
- Called by: `sm_init`, `ble_219_0c059230`
- Calls: `ble_hook_invoke_indexed`
- Confidence: high

## le_device_db_tlv_configure

**Install TLV backend and probe which of the 4 device DB slots are populated**

Stores the TLV implementation pointer (DAT_2000fd0c) and its context (DAT_2000fd08), clears the in-use count (DAT_2000fd10) and the four per-slot flags starting at 0x2000fd04. Then for slots 0..3 calls the backend get callback with tag 0x42544400|slot and a 0x3c-byte buffer; every slot returning exactly 0x3c bytes gets its flag set to 1 and increments the count. Corresponds to BTstack le_device_db_tlv_configure.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | btstack_tlv_t implementation (first word is the get_tag function pointer) |
| `param_2` | `ptr` | TLV context passed back to the callbacks |

- Addresses by version: 219: 0x0C04F034
- Called by: `ble_219_0c05b67c`
- Confidence: high

## le_device_db_tlv_get_entry

**Read one 60-byte LE device DB record from TLV storage and unpack its fields**

Calls the TLV backend get-tag callback (*DAT_2000fd0c)(ctx=DAT_2000fd08, tag='BTD'<<8 | index, buf, 0x3c). If exactly 0x3c bytes were returned, copies the requested fields out of the stack buffer, each only when its output pointer is non-NULL: 16-byte key block at +30 (LTK), u16 at +46 (EDIV), 8-byte at +48 (random number), and four single bytes at +56..+59 (key size, authenticated, authorized, secure-connection flags). On a size mismatch outputs are left untouched. This matches BTstack le_device_db_tlv.c, which stores one record per bonded device under tag 'BTD\0'+index.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | device DB slot index 0..3 (OR-ed into tag 0x42544400) |
| `param_2` | `ptr` | out u16 EDIV, may be NULL |
| `param_3` | `ptr` | out 8-byte random number (rand), may be NULL |
| `param_4` | `ptr` | out 16-byte key (LTK), may be NULL |
| `param_5` | `ptr` | out u32 key size, may be NULL |
| `param_6` | `ptr` | out u32 authenticated flag, may be NULL |
| `param_7` | `ptr` | out u32 authorized flag, may be NULL |
| `param_8` | `ptr` | out u32 secure-connection flag, may be NULL |

**Notes:** Field-to-name mapping inferred from BTstack le_device_db_entry_t layout; the first 30 bytes (IRK/address) are not exported by this function.

- Addresses by version: 219: 0x0C04EF9C
- Called by: `sm_pairing_step_complete`, `ble_219_0c051eb8`, `sm_link_poll_state`
- Confidence: medium

## le_device_db_tlv_init

**Empty initialiser of the LE device DB (TLV backed)**

Single return instruction. In BTstack's le_device_db_tlv.c the init hook performs no work (storage is accessed lazily through the TLV singleton). No direct callers; reached through the le_device_db function interface.

- Addresses by version: 219: 0x0C04ECE0
- Confidence: low

## le_device_db_tlv_max_count

**Return the maximum number of LE device DB entries (4)**

Returns the constant 4, the number of bonded-device slots (tags 'BTD'+index) supported by this build of le_device_db_tlv.c. Called from ble_219_0c04f634, 0c051eb8 and 0c052e70 (security manager).

**Returns** `s32`: 4

- Addresses by version: 219: 0x0C04ECE4
- Called by: `sm_device_db_resolve_peer`, `ble_219_0c051eb8`, `le_device_db_tlv_remove_by_addr`
- Confidence: high

## le_device_db_tlv_read_identity

**Read DB slot N's identity fields: address type, 6-byte address and IRK**

Reads the 60-byte record at tag 0x42544400|slot through the backend read function (vtable +0). If fewer than 60 bytes come back, the buffer is zeroed and the address type is set to 0xFE, the empty-slot marker other DB routines test for. Non-NULL outputs receive the u32 address type from record +4, the 6-byte address from +8..+13 and the 16-byte IRK from +14..+29. This is the identity part of the layout written by le_device_db_tlv_add.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | DB slot index 0..3 |
| `param_2` | `ptr` | out: u32 address type (0xFE for an empty slot) |
| `param_3` | `ptr` | out: 6-byte address, may be NULL |
| `param_4` | `ptr` | out: 16-byte IRK, may be NULL |

- Addresses by version: 219: 0x0C04EE74
- Called by: `ble_link_notify_id_flag`, `ble_link_notify_pair_addrs`, `sm_device_db_resolve_peer`, `ble_link_notify_id_addr`, `ble_219_0c051eb8`, `le_device_db_tlv_remove_by_addr`
- Calls: `memset`
- Confidence: high

## le_device_db_tlv_remove

**Delete LE device DB entry N and its TLV tag**

If the used-flag byte DAT_2000fd04[index] is zero it returns. Otherwise it calls the TLV delete_tag function (vtable at DAT_2000fd0c, slot +8) with context DAT_2000fd08 and tag 0x42544400|index ('BTD'+index), clears the used flag and decrements the entry count DAT_2000fd10. Called from ble_219_0c052e70 (security manager removing a bond).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | device DB index (0..3) |
| `param_2` | `u32` | unused |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | unused |

- Addresses by version: 219: 0x0C04ECE8
- Called by: `le_device_db_tlv_remove_by_addr`
- Confidence: high

## le_device_db_tlv_remove_by_addr

**Delete the DB entry whose address type and 6-byte address match**

Visits DB slots 0 up to le_device_db_tlv_max_count() minus one, reads each slot's identity record (le_device_db_tlv_read_identity) and, for the first slot whose address type equals param_1 and whose address matches param_2 (memcmp of 6 bytes), calls le_device_db_tlv_remove(slot). Empty slots (type 0xFE) never match. Unlike le_device_db_tlv_add it does not check the in-use bytes, and nothing happens when no slot matches.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | address type |
| `param_2` | `ptr` | 6-byte address |

- Addresses by version: 219: 0x0C052E70
- Calls: `le_device_db_tlv_max_count`, `le_device_db_tlv_remove`, `le_device_db_tlv_read_identity`, `memcmp`
- Confidence: high

## le_device_db_tlv_set_encryption

**Overwrite the LTK, EDIV, Rand and key flags of DB slot N in its TLV record**

Reads the 60-byte record for slot param_1 and, only if all 60 bytes come back, rewrites its encryption part and stores it again: 16-byte LTK at +30..+45 (param_4), u16 EDIV at +46..+47 (param_2), 8-byte Rand at +48..+55 (param_3), and four flag bytes at +56..+59 (param_5..param_8). NULL pointers keep the previous LTK or Rand bytes, and the identity fields and sequence number are unchanged. A failed write logs 'Set encryption data failed' (le_device_db_tlv.c line 0x11f) through ble_hook_invoke_indexed.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | DB slot index |
| `param_2` | `u16` | EDIV |
| `param_3` | `ptr` | 8-byte Rand, NULL keeps the old value |
| `param_4` | `ptr` | 16-byte LTK, NULL keeps the old value |
| `param_5` | `u8` | flag byte at record +56 (key size or security flags, not decoded) |
| `param_6` | `u8` | flag byte at record +57 |
| `param_7` | `u8` | flag byte at record +58 |
| `param_8` | `u8` | flag byte at record +59 |

**Notes:** The four flag bytes probably hold key size and authentication bits; that is an inference.

- Addresses by version: 219: 0x0C04EEEC
- Called by: `sm_device_db_resolve_peer`
- Calls: `ble_hook_invoke_indexed`
- Confidence: medium

## sdp_attribute_add_length

**Per-attribute callback: add 3 + value length to the running attribute-list size**

Callback used by sdp_record_attribute_list_length through sdp_attribute_list_traverse_sequence. For an attribute id that is in the requested id list (*param_5, matched with de_traverse_sequence and the comparator at 0x0c04c528), it adds the value element length from de_get_len plus 3 bytes for the DE_UINT16 id element to the 16-bit running total stored at param_5+4. It always returns 0 so the traversal continues. This is the sizing pass that runs before sdp_record_write_attribute_list writes the bytes.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | attribute id |
| `param_2` | `ptr` | value data element |
| `param_3` | `u32` | unused by the body |
| `param_4` | `u32` | unused by the body |
| `param_5` | `ptr` | [0] requested attribute id list, [1] low 16 bits = running byte total |

**Returns** `u32`: always 0 (continue)

- Addresses by version: 219: 0x0C04C89C
- Calls: `de_get_len`, `de_traverse_sequence`
- Confidence: high

## sdp_attribute_list_traverse_sequence

**BTstack sdp_util.c: walk an SDP attribute list as (UINT16 attribute id, value) pairs**

Requires the element to be a DE_DES (type 6); starts after its header and runs to de_get_len(element). Each attribute id must be DE_UINT (type 1) of DE_SIZE_16 (size type 1) or traversal stops; the id is read big-endian at pos+1 and pos advances by 3; if that already reaches the end the loop exits. The handler is then called as handler(attribute_id, value_element, value_type, value_size_type, context) and traversal stops when it returns non-zero, else pos += de_get_len(value). Callers: sdp_get_attribute_value_for_attribute_id style wrappers ble_219_0c04cb10 (with callback 0x0C04C780), 0c04cb48, 0c04cb6c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | attribute list DE_DES |
| `param_2` | `ptr` | sdp_attribute_list_traversal_callback_t handler(id, element, type, size, context) |
| `param_3` | `ptr` | opaque context |

- Addresses by version: 219: 0x0C04C6FC
- Called by: `sdp_record_write_attribute_list`, `sdp_record_attribute_list_length`, `sdp_record_find_attribute`
- Calls: `de_get_len`, `co_read16_be`
- Confidence: high

## sdp_attribute_write_fragment

**Per-attribute callback: write one attribute id and value into a byte-budgeted SDP response**

Callback used by sdp_record_write_attribute_list through sdp_attribute_list_traverse_sequence, once per (id, value) pair in a record. It first checks whether the id is in the requested attribute id list (param_5[3], matched with de_traverse_sequence and the comparator at 0x0c04c528). For a matching attribute it emits the 3-byte id element (DE_UINT16 header 0x09 plus the big-endian id), then copies the value element with memcpy, honouring a resume offset and the bytes still allowed by the budget. The state struct tracks output pointer, skip count, bytes written and bytes remaining. Returns 1 when the budget ran out part-way through (the traversal stops and a continuation is needed) and 0 when the attribute finished or was not requested. Write half of the SDP attribute serializer; the length pass is sdp_attribute_add_length.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | attribute id |
| `param_2` | `ptr` | value data element |
| `param_3` | `u32` | unused by the body |
| `param_4` | `u32` | unused by the body |
| `param_5` | `ptr` | write state: [0] output pointer, [1] skip/offset count, [2] bytes written, [3] attribute id list, [4] remaining budget |

**Returns** `u32`: 1 = budget exhausted mid-attribute, 0 = done or not requested

**Notes:** The state-struct field meanings are inferred from the arithmetic and the traversal call; word offsets are approximate.

- Addresses by version: 219: 0x0C04C780
- Calls: `de_get_len`, `de_traverse_sequence`, `co_write16_be`, `memcpy`
- Confidence: medium

## sdp_get_service_record_handle

**Read the 32-bit ServiceRecordHandle (attribute 0x0000) of an SDP record, 0 if absent**

Looks up attribute 0x0000 (ServiceRecordHandle) in the record's attribute list with sdp_record_find_attribute (0x0c04cb6c). It then requires the value element to be a UINT-type data element of 32-bit size (two small predicates at 0x0c04c578 and 0x0c04c570, whose exact meaning is inferred from the return values 1 and 2) and returns the big-endian u32 payload read at element offset 1 with co_read32_be. Returns 0 when the attribute is missing or has the wrong type. sdp_register_service treats any value below 0x10000 as an invalid handle, so 0 is the failure signal. Part of the SDP record-access group (sdp_record_find_attribute, sdp_record_matches_pattern, sdp_record_attribute_list_length, sdp_record_write_attribute_list).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | SDP service record, DE-encoded attribute list |
| `param_2` | `u32` | unused by the body |
| `param_3` | `u32` | unused by the body |
| `param_4` | `u32` | pass-through to co_read32_be, which ignores it |

**Returns** `u32`: ServiceRecordHandle value, or 0 if not found or not a 32-bit UINT

**Notes:** The packet callee list names bthost_byte_get_low3_bits and bthost_byte_get_high5_bits, but the decompiled body does not call them; the calls are to 0x0c04c578, 0x0c04c570, 0x0c04cb6c and co_read32_be.

- Addresses by version: 219: 0x0C04BD98
- Called by: `sdp_register_service`
- Calls: `bthost_byte_get_low3_bits`, `bthost_byte_get_high5_bits`, `sdp_record_find_attribute`, `co_read32_be`
- Confidence: medium

## sdp_pattern_uuid_match

**Per-UUID callback for a ServiceSearchPattern: fail unless the record contains the UUID**

Invoked by de_traverse_sequence for each element of a ServiceSearchPattern, with the candidate record as context. A DE_UUID element with 16-, 32- or 128-bit payload is normalised to a 128-bit UUID (uuid_add_bluetooth_prefix for the short forms) and searched for in the record's attribute values with de_traverse_sequence and the comparator at 0x0c04c978. If found, it returns 0 so the traversal continues. If not found, or if the element is not a UUID, it clears the result flag at context+4 and returns 1, which stops the traversal and fails the match. Net effect: a record matches only if every UUID in the pattern occurs in it. Used only by sdp_record_matches_pattern.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pattern element (DE header followed by UUID bytes) |
| `param_2` | `u32` | unused by the body |
| `param_3` | `u32` | unused by the body |
| `param_4` | `ptr` | context: [0] = service record pointer, [1] = match result flag |

**Returns** `u32`: 0 = UUID found, continue; 1 = not found or not a UUID, stop

- Addresses by version: 219: 0x0C04C680
- Calls: `de_traverse_sequence`, `co_read16_be`, `co_read32_be`, `uuid_add_bluetooth_prefix`
- Confidence: medium

## sdp_record_attribute_list_length

**Total encoded size of the requested attributes of an SDP record**

Returns the number of bytes that sdp_record_write_attribute_list would emit for the attribute id list param_2 on record param_1. Each matching attribute contributes its 3-byte id element plus the length of its value element. The sum is accumulated by sdp_attribute_list_traverse_sequence with the callback sdp_attribute_add_length (0x0c04c89c), so the result is a 16-bit total. Used to fill the AttributeListsByteCount field before the bytes are written.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | SDP service record |
| `param_2` | `ptr` | requested attribute id list |

**Returns** `u16`: encoded byte count of the matching attributes

- Addresses by version: 219: 0x0C04CB48
- Called by: `sdp_server_build_service_attribute_response`, `sdp_server_build_service_search_attribute_response`
- Calls: `sdp_attribute_list_traverse_sequence`
- Confidence: high

## sdp_record_find_attribute

**Find an SDP record attribute by 16-bit id and return a pointer to its value element**

Walks the attribute list of record param_1 with sdp_attribute_list_traverse_sequence and the id comparator at 0x0c04c518, and returns the value element for attribute id param_2. Returns 0 when the record has no such attribute. Used by sdp_get_service_record_handle with id 0x0000. Member of the SDP record-access group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | SDP service record |
| `param_2` | `u16` | attribute id to find |

**Returns** `ptr`: pointer to the value data element, or 0

- Addresses by version: 219: 0x0C04CB6C
- Called by: `sdp_get_service_record_handle`
- Calls: `sdp_attribute_list_traverse_sequence`
- Confidence: high

## sdp_record_matches_pattern

**Return true when an SDP record contains every UUID of a ServiceSearchPattern**

Walks the ServiceSearchPattern DE sequence param_2 with de_traverse_sequence and the per-UUID callback sdp_pattern_uuid_match (0x0c04c680), using the record as context. The result starts at 1 and is cleared by any failing element, so the function returns true only when every UUID in the pattern is present in the record, which is the BTstack ServiceSearchPattern rule. Used by all three SDP request handlers to select records.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | SDP service record |
| `param_2` | `ptr` | ServiceSearchPattern DE sequence |

**Returns** `bool`: true if the record matches the whole pattern

- Addresses by version: 219: 0x0C04CB90
- Called by: `sdp_server_build_service_search_response`, `sdp_server_build_service_search_attribute_response`
- Calls: `de_traverse_sequence`
- Confidence: high

## sdp_record_write_attribute_list

**Serialize the requested attributes of an SDP record into a byte-budgeted, resumable buffer**

Wrapper around sdp_attribute_list_traverse_sequence that walks the record's attribute list and applies sdp_attribute_write_fragment (0x0c04c780) to each entry. The arguments give the record, the attribute id list, a resume offset, a byte budget, an out-parameter for the number of bytes written, and the output buffer. It returns 1 when the whole list fit and 0 when the traversal stopped at the budget, in which case the caller writes a continuation state. Callers are sdp_server_build_service_attribute_response and sdp_server_build_service_search_attribute_response.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | SDP service record |
| `param_2` | `ptr` | requested attribute id list (DE sequence) |
| `param_3` | `u16` | resume offset within the record's attribute list |
| `param_4` | `u16` | byte budget for this fragment |
| `param_5` | `ptr` | out: u16 number of bytes written |
| `param_6` | `ptr` | output buffer |

**Returns** `u32`: 1 = whole list written, 0 = stopped at the budget

- Addresses by version: 219: 0x0C04CB10
- Called by: `sdp_server_build_service_attribute_response`, `sdp_server_build_service_search_attribute_response`
- Calls: `sdp_attribute_list_traverse_sequence`
- Confidence: medium

## sdp_register_service

**Register an SDP service record: validate its handle, reject duplicates, link it into the list**

Reads the record handle with sdp_get_service_record_handle and returns 0x83 (invalid handle) when it is below 0x10000. It walks the global record list at 0x2000fcb4 and returns 0x80 (already registered) when a record with the same handle exists. Otherwise it takes a 12-byte service_record_item_t from btstack_memory_service_record_item_get (8-entry pool), stores the handle at item+4 and the record pointer at item+8, and pushes the item on the list head with btstack_linked_list_add. Returns 0x56 when the pool is exhausted and 0 on success. Registration only; removal is not in this function. Members of the SDP record-table group: sdp_server_build_service_search_response, sdp_server_build_service_attribute_response and sdp_server_build_service_search_attribute_response all walk the same list.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DE-encoded SDP service record, stored by pointer (not copied) |

**Returns** `u32`: 0 on success, 0x83 invalid handle, 0x80 duplicate handle, 0x56 no free item

**Notes:** Status code names follow BTstack sdp_server.c; the exact code-to-name mapping is inferred.

- Addresses by version: 219: 0x0C04BDC8
- Called by: `ble_219_0c058f00`
- Calls: `sdp_get_service_record_handle`, `btstack_linked_list_add`, `btstack_memory_service_record_item_get`
- Confidence: high

## sdp_server_build_service_attribute_response

**Answer an SDP ServiceAttributeRequest for one record handle and an attribute id list**

Parses the request: transaction id at +1, ParameterLength at +3, ServiceRecordHandle u32 at +5, MaximumAttributeByteCount u16 at +9, AttributeIDList DE sequence from +0x0b. If the handle does not match a record in list 0x2000fcb4, it writes an ErrorResponse (PDU 1) with error 0x0002 (Invalid Service Record Handle). Otherwise it writes a ServiceAttributeResponse (PDU 5): transaction id, ParameterLength, AttributeListByteCount, then the id/value list produced by sdp_record_write_attribute_list cut at the byte budget. The continuation state is 0 when the list completed, or 2 followed by a 16-bit resume offset when it did not. Returns the total PDU length, or 0 for a malformed request. Member of the SDP request-handler group with sdp_server_build_service_search_response.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | SDP ServiceAttributeRequest PDU |
| `param_2` | `u16` | response budget (MTU of the channel) |

**Returns** `u16`: length of the response PDU in 0x2000fb98, 0 if malformed

- Addresses by version: 219: 0x0C04BFD0
- Calls: `de_get_len_safe`, `de_store_descriptor_with_len`, `sdp_record_write_attribute_list`, `sdp_record_attribute_list_length`, `co_read16_be`, `co_read32_be`, `co_write16_be`
- Confidence: medium

## sdp_server_build_service_search_attribute_response

**Answer an SDP ServiceSearchAttributeRequest with attribute lists for all matching records**

Parses the request: ServiceSearchPattern at +5, MaximumAttributeByteCount u16 after it, AttributeIDList after that, then a continuation-state field. For a fresh request it first sums the encoded size of each matching record's attribute list (sdp_record_attribute_list_length, plus 3 bytes per record for its sequence header) and stores that total in the AttributeListsByteCount field at 0x2000fb9f. It then emits one attribute list per matching record with sdp_record_write_attribute_list, resuming from the continuation state when one is present and stopping at the budget (MTU minus 12, capped by MaximumAttributeByteCount). The response is ServiceSearchAttributeResponse (PDU 7) with transaction id, ParameterLength, AttributeListsByteCount, the lists, and a continuation trailer. Malformed requests return 0. Member of the SDP request-handler group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | SDP ServiceSearchAttributeRequest PDU |
| `param_2` | `u16` | response budget (MTU of the channel) |

**Returns** `u16`: length of the response PDU in 0x2000fb98, 0 if malformed

**Notes:** The continuation-state layout (4 bytes: record index and byte offset) is inferred from the code that reads two u16 values at +1 and +3.

- Addresses by version: 219: 0x0C04C144
- Calls: `de_get_len_safe`, `de_store_descriptor_with_len`, `sdp_record_write_attribute_list`, `sdp_record_attribute_list_length`, `sdp_record_matches_pattern`, `co_read16_be`, `co_write16_be`
- Confidence: medium

## sdp_server_build_service_search_response

**Answer an SDP ServiceSearchRequest with the matching record handles**

Parses the request PDU: transaction id at +1, ParameterLength at +3, ServiceSearchPattern DE sequence at +5, MaximumServiceRecordCount u16 right after the pattern, then a continuation-state byte (0, or length 2 followed by a 16-bit resume index). It finds registered records that match the pattern (sdp_record_matches_pattern over list 0x2000fcb4) and writes a ServiceSearchResponse into the global response buffer 0x2000fb98: PDU id 3, transaction id, ParameterLength, TotalServiceRecordCount, CurrentServiceRecordCount, then one raw 32-bit handle per returned record. The count is capped by MaximumServiceRecordCount and by the response budget (roughly (MTU-12)/4 handles); when records remain, a 2-byte resume index is appended as continuation state. Malformed requests return 0 and produce no response. Group: the three SDP request handlers (here, sdp_server_build_service_attribute_response, sdp_server_build_service_search_attribute_response) share the record list and response buffer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | SDP ServiceSearchRequest PDU |
| `param_2` | `u16` | response budget (the ATT/L2CAP MTU of the channel) |

**Returns** `u16`: length of the response PDU in 0x2000fb98, 0 if the request is malformed

- Addresses by version: 219: 0x0C04BE10
- Calls: `de_get_len_safe`, `sdp_record_matches_pattern`, `co_read16_be`, `co_write16_be`, `co_write32_be`
- Confidence: medium

## sm_device_db_resolve_peer

**Match a peer against the LE device DB by address and IRK and report its slot**

Identity-resolves the peer of the connection record param_1. With flag bit 2 of 0x2000ff59 set, it walks the device DB slots (count from le_device_db_tlv_max_count, identity from le_device_db_tlv_read_identity) and compares the stored 16-byte IRK words at 0x20010128..0x20010134 and the 6-byte address at 0x20010149. When the address type at 0x20010148 is zero it scans for an address match instead. If no slot matches, it inserts the entry with le_device_db_tlv_add. On success it sends link frame 0xD3 (address pair and slot index) through ble_link_notify_pair_addrs, sets the connection state byte at +0x0b to 3, and stores the slot index at +0x18. When the key-flag bytes on the connection and flags 0x2000ff6c, 0x2000ff59 indicate it, it also writes encryption info with le_device_db_tlv_set_encryption. Part of the SM identity-resolution path with sm_pairing_step_complete.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | connection record: u16 handle at +0, state at +0x0b, DB index at +0x18, key flags at +0x19..+0x23 |

**Notes:** Mapping of the four helper addresses (0x0c04ece4, 0x0c04ee74, 0x0c04ed28, 0x0c04eeec) to le_device_db_tlv_max_count, le_device_db_tlv_read_identity, le_device_db_tlv_add and le_device_db_tlv_set_encryption follows the packet callee list and is not independently verified.

- Addresses by version: 219: 0x0C04F634
- Called by: `ble_219_0c051eb8`, `ble_219_0c051ef0`
- Calls: `le_device_db_tlv_max_count`, `le_device_db_tlv_add`, `le_device_db_tlv_read_identity`, `le_device_db_tlv_set_encryption`, `ble_link_notify_pair_addrs`, `memcmp`
- Confidence: medium

## sm_init

**One-time SM initialisation: run-loop timer, event handlers, default constants, key tables**

Idempotent: returns at once when 0x2000feb0 is already set. Otherwise it fills two 16-byte byte tables, at 0x2000fed4..0x2000fee3 with (address minus 0x44) and at 0x2000fec4..0x2000fed3 with (address plus 0x5C); the purpose of these tables is unknown. It sets defaults: 0x2000fd79 = 0x0F, 0x2000feb1 = 0x10, 0x2000feb2 = 7, 0x2000fea0 = -1, 0x2000ff08 = 1. It initialises the run-loop timer at 0x2000ff0c with callback 0x0c052ae8 and period 900000 (15 minutes if milliseconds), installs the HCI event handler 0x0c0524f0, and calls le_device_db_tlv_check_init (0x0c065148) and the DB backend init at 0x0c04ecc0. It registers the event handler 0x0c051ef0 for event ids 6 and 7 and clears the pairing state globals. Sets 0x2000feb0 = 1 at the end.

**Notes:** sm_init is a BTstack name; the packet confirms the TLV device DB and timer callees. The 900000 period unit and the byte-table purpose are unverified.

- Addresses by version: 219: 0x0C052B50
- Called by: `ble_219_0c059230`
- Calls: `le_device_db_tlv_check_init`, `ble_219_0c065148`, `btstack_run_loop_set_timer_handler`, `hci_add_event_handler`, `l2cap_channel_set_context_by_cid`
- Confidence: medium

## sm_link_poll_state

**Periodic SM poll for the current connection: re-check its identity record and re-arm the timer**

Looks up the connection record (ble_ctrl_conn_find_by_handle, handle passed in r0) and returns if none is found. When the state byte at +0x1bd is 0 or 0x1a and the mode byte at +0x1be is 3, it reads DB entry at +0x1d8 with le_device_db_tlv_get_entry and, if the entry has a non-zero key field, sets +0x1bd = 0x1B and calls ble_link_notify_id_addr (0x0c04f948) unless flag +0x1dd is set. For mode 4 it sets the same state and calls ble_link_notify_local (0x0c04f584) unless flag +0x1dc is set. Finally, while 0x2000feb0 is set, it removes the run-loop timer 0x2000ff0c, sets it to 0 ms, and adds it again. Only caller: ble_219_0c04e398.

**Notes:** The connection lookup takes its handle in r0, which the decompiler does not show. The meaning of the state and mode bytes is inferred from the transitions.

- Addresses by version: 219: 0x0C052C7C
- Called by: `ble_219_0c04e398`
- Calls: `le_device_db_tlv_get_entry`, `ble_link_notify_local`, `ble_link_notify_id_addr`, `btstack_run_loop_set_timer`, `btstack_run_loop_add_timer`, `btstack_run_loop_remove_timer`, `ble_ctrl_conn_find_by_handle`
- Confidence: low

## sm_pairing_step_complete

**Advance the per-link pairing state machine when one pairing or encryption step completes**

Completion handler for one SM step. param_1 == 1 means success, anything else failure. It takes the pending link from global 0x2000fd84 and clears the pending step code at 0x2000fd8c and the saved timer handle at 0x2000fd90. If a pending link exists with step code 2, it sets the link state byte at +0x15 among the encoded pairing states 0x1B, 0x1C, 0x1D, 0x1E and 0x20, and runs the local/identity notifications (ble_link_notify_local, ble_link_notify_id_addr) or the cleanup helpers, depending on the state and on flags 0x2000ff35 and link+0x03. On success it publishes an 11-byte frame 0xCE (handle, state byte from 0x2000fd7a, 6-byte address copied reversed with co_reverse_copy_6) through ble_evt_publish. On failure it sends frame 0xCF through ble_link_notify_pair_addrs. Pairing-state group with sm_device_db_resolve_peer and sm_link_poll_state.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | step result: 1 = success, otherwise failure |

**Notes:** The meanings of the encoded state values 0x1B to 0x20 and of the step codes are inferred from the transitions, not from a spec. The packet does not show the caller of the state change.

- Addresses by version: 219: 0x0C050700
- Called by: `ble_219_0c051eb8`
- Calls: `le_device_db_tlv_get_entry`, `ble_evt_publish`, `ble_link_notify_local`, `ble_link_notify_pair_addrs`, `ble_link_notify_id_addr`, `btstack_run_loop_set_timer`, `btstack_run_loop_add_timer`, `btstack_run_loop_remove_timer`, `co_write16_le`, `co_reverse_copy_6`
- Confidence: low

## uuid_add_bluetooth_prefix

**Expand a 32-bit UUID into a 128-bit Bluetooth Base UUID**

Writes a 16-byte big-endian UUID into param_1: bytes 0..3 are param_2 MSB first, followed by the constant tail 00 00 10 00 80 00 00 80 5F 9B 34 FB (words 0x100000, 0x80000080, 0xfb349b5f stored little-endian). That yields xxxxxxxx-0000-1000-8000-00805F9B34FB, the Bluetooth Base UUID. Matches BTstack's uuid_add_bluetooth_prefix(); always returns 0 here. Called from the ATT database code (0c04c680, 0c04c914) when comparing/serializing 16/32-bit UUIDs.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 16-byte output buffer |
| `param_2` | `u32` | 16- or 32-bit short UUID value |

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C065CE4
- Called by: `sdp_pattern_uuid_match`, `de_get_normalized_uuid`
- Confidence: high
