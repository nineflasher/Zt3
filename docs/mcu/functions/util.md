# MCU - `util` functions

98 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_12b_bit4_offset_select`](#mcu_12b_bit4_offset_select) | (removed) | Store the inverted bit 4 flag and add 0x48 to the base when that flag is set |
| [`mcu_12b_select_stack_local_fragment`](#mcu_12b_select_stack_local_fragment) | (removed) | Code fragment (12b build): conditionally replace one caller stack slot with another |
| [`mcu_add_overflow_direction_s32`](#mcu_add_overflow_direction_s32) | 0x08002890 | Report whether a + b would overflow int32 (+1 positive, -1 negative, 0 none) |
| [`mcu_array_max_s32`](#mcu_array_max_s32) | 0x08002946 | Maximum of an int32 array of n elements |
| [`mcu_array_min_s32`](#mcu_array_min_s32) | 0x08002964 | Minimum of an int32 array of n elements |
| [`mcu_bits_and`](#mcu_bits_and) | 0x08002ED2 | Return a & b (bitwise AND of two words) |
| [`mcu_bits_clear`](#mcu_bits_clear) | 0x08002EC8 | *p &= ~mask (clear bits in a word) |
| [`mcu_bits_set`](#mcu_bits_set) | 0x08002ED6 | *p \|= mask (set bits in a word) |
| [`mcu_block200_alloc`](#mcu_block200_alloc) | 0x08007BCE | Allocate one 200-byte block from the 4088-byte first-fit pool at 0x200027CC |
| [`mcu_block_table_load_verified`](#mcu_block_table_load_verified) | 0x08008E30 | Copy a 544-byte block table into RAM and verify its block checksums, up to five attempts |
| [`mcu_byte_sum16_store`](#mcu_byte_sum16_store) | 0x0800CB74 | Sum a byte buffer modulo 2^16 and store the total as a halfword |
| [`mcu_byte_sum_checksum16`](#mcu_byte_sum_checksum16) | 0x08005E60 | 16-bit byte-sum checksum over a buffer, returned as its bitwise complement |
| [`mcu_bytes_equal_n8`](#mcu_bytes_equal_n8) | 0x0800A280 | Compare two byte strings of length n with an 8-bit counter and return 1 if equal |
| [`mcu_callback_slot_dispatch`](#mcu_callback_slot_dispatch) | 0x080089A4 | Call the RAM function pointer in slot 0 or 1 of the two-entry table at 0x20000630 |
| [`mcu_ceil_div_1024`](#mcu_ceil_div_1024) | 0x0800644E | Ceiling of param_1 / 1024: number of 1 KiB units needed for a byte count |
| [`mcu_cfg_gain_108_q15`](#mcu_cfg_gain_108_q15) | 0x08004A0C | Return cfg+0x108 times DAT_200003CC/5.3036 as a Q15 value |
| [`mcu_cfg_gain_10c_q15`](#mcu_cfg_gain_10c_q15) | 0x080049B8 | Return cfg+0x10C times DAT_200003CC/5.3036 as a Q15 value |
| [`mcu_cond_658_and_not_a9a`](#mcu_cond_658_and_not_a9a) | 0x08004AFC | Return 1 if flag 0x20000658 is non-zero and flag 0x20000a9a is zero |
| [`mcu_copy_bytes`](#mcu_copy_bytes) | 0x0800CC68 | Copy a byte block forward, one byte at a time |
| [`mcu_ctx_cfg_byte_set`](#mcu_ctx_cfg_byte_set) | 0x0800C940 | Store one byte into a field of the context config words at +0xA0 and +0xA4 (index 1..7) |
| [`mcu_ctx_clear_field_0x9c`](#mcu_ctx_clear_field_0x9c) | 0x080097AC | Clear the 32-bit field at offset 0x9C of the object |
| [`mcu_ctx_flag4_is_clear`](#mcu_ctx_flag4_is_clear) | 0x08009094 | Return 1 if the byte at offset +0x04 of the object is zero, else 0 |
| [`mcu_ctx_get_field_0x44`](#mcu_ctx_get_field_0x44) | 0x08008F74 | Getter for the 32-bit raw counter at offset 0x44 of the drive context |
| [`mcu_ctx_get_field_0x90`](#mcu_ctx_get_field_0x90) | (removed) | Getter returning the 32-bit field at offset 0x90 of a context struct |
| [`mcu_ctx_get_field_0x9c`](#mcu_ctx_get_field_0x9c) | 0x080097B4 | Getter for the 32-bit field at offset 0x9C of the object |
| [`mcu_ctx_set_field_0x10`](#mcu_ctx_set_field_0x10) | 0x0800CEC8 | Store a 32-bit value at offset 0x10 of a context struct |
| [`mcu_ctx_set_field_0x14`](#mcu_ctx_set_field_0x14) | 0x0800CEC4 | Store a 32-bit value at offset 0x14 of a context struct |
| [`mcu_edge_counter_force_high`](#mcu_edge_counter_force_high) | 0x08009A7A | Load an edge counter with its reload value and force phase and output high |
| [`mcu_edge_counter_init`](#mcu_edge_counter_init) | 0x08009A40 | Initialise an edge counter with limit, reload value and output mode, then enable it |
| [`mcu_edge_counter_reset`](#mcu_edge_counter_reset) | 0x08009A6E | Reset an edge counter to zero with phase and output low, keeping its configuration |
| [`mcu_edge_counter_step`](#mcu_edge_counter_step) | 0x08009954 | Advance a bidirectional phase counter one step and return its selected edge output bit |
| [`mcu_empty_callback`](#mcu_empty_callback) | 0x08006620 | Empty callback: returns immediately |
| [`mcu_fscale_mul_div_a`](#mcu_fscale_mul_div_a) | 0x0800763C | Return p1 * 1088.31 * p2 / p3 in soft-float single precision (tail call) |
| [`mcu_fscale_mul_div_b`](#mcu_fscale_mul_div_b) | 0x0800765C | Return p1 * 1088.31 * p2 / p3 (soft-float single), twin of mcu_fscale_mul_div_a |
| [`mcu_get_cfg_field_0x28`](#mcu_get_cfg_field_0x28) | 0x080046CC | Return the 32-bit field at offset 0x28 of the struct pointed to by DAT_200000f8 |
| [`mcu_get_cfg_field_0x28_q15`](#mcu_get_cfg_field_0x28_q15) | 0x080046D8 | Return field +0x28 of *DAT_200000f8 after a (x * 0x8000) >> 15 round trip |
| [`mcu_get_field_0x0c_ashr_scale`](#mcu_get_field_0x0c_ashr_scale) | 0x0800A588 | Return the s32 field at +0x0c arithmetic-shifted right by the scale byte at +0x32 |
| [`mcu_get_field_0x0c_ashr_scale_thunk1`](#mcu_get_field_0x0c_ashr_scale_thunk1) | 0x0800A56C | Tail-call thunk to mcu_get_field_0x0c_ashr_scale |
| [`mcu_get_field_0x0c_ashr_scale_thunk2`](#mcu_get_field_0x0c_ashr_scale_thunk2) | 0x0800A570 | Second tail-call thunk to mcu_get_field_0x0c_ashr_scale |
| [`mcu_get_field_0x10_ashr_scale`](#mcu_get_field_0x10_ashr_scale) | (removed) | Return the s32 field at +0x10 arithmetic-shifted right by the scale byte at +0x32 |
| [`mcu_get_field_0x18_ashr_scale`](#mcu_get_field_0x18_ashr_scale) | (removed) | Return the s32 field at +0x18 arithmetic-shifted right by the scale byte at +0x32 |
| [`mcu_get_global_ctx_field_0x64`](#mcu_get_global_ctx_field_0x64) | 0x08009088 | Return the 32-bit word at offset 0x64 of the object pointed to by global DAT_2000002C |
| [`mcu_get_param_654_q15`](#mcu_get_param_654_q15) | 0x08004AE4 | Return the byte/halfword at 0x20000654 shifted into Q15 (<< 15) |
| [`mcu_get_u16_field_0x34`](#mcu_get_u16_field_0x34) | 0x0800A818 | Return the u16 field at struct+0x34 |
| [`mcu_get_var_2026`](#mcu_get_var_2026) | 0x08006574 | Getter returning the byte at 0x20002026 |
| [`mcu_get_var_34c_ashr_scale`](#mcu_get_var_34c_ashr_scale) | 0x0800A574 | Return RAM word 0x2000034c arithmetic-shifted right by the scale byte at struct+0x32 |
| [`mcu_get_var_650`](#mcu_get_var_650) | 0x080046F4 | Getter returning the 32-bit RAM variable at 0x20000650 |
| [`mcu_get_var_67c`](#mcu_get_var_67c) | 0x08004AF0 | Getter returning the 32-bit RAM variable at 0x2000067c |
| [`mcu_get_var_f60`](#mcu_get_var_f60) | 0x080021FC | Getter returning the 16-bit RAM value at 0x20000f60 |
| [`mcu_get_word_at_0x6c`](#mcu_get_word_at_0x6c) | 0x080097E4 | Getter returning the 32-bit word at offset 0x6c of a structure |
| [`mcu_get_word_at_0x90`](#mcu_get_word_at_0x90) | 0x08001436 | Getter returning the 32-bit word at offset 0x90 of a structure |
| [`mcu_init_q14_copies_from_200003de`](#mcu_init_q14_copies_from_200003de) | 0x0800727C | Set four RAM words to the byte at 0x200003DE shifted left by 14 (Q14) |
| [`mcu_latched_value_set`](#mcu_latched_value_set) | 0x08009EB8 | Store a 32-bit value and set the valid flag byte at struct+0x04 |
| [`mcu_lpf_asym_update`](#mcu_lpf_asym_update) | 0x08007160 | Enable-gated Q30 low-pass with separate rising and falling coefficients |
| [`mcu_lpf_or_step_tracker_update`](#mcu_lpf_or_step_tracker_update) | 0x080070AC | Update a tracked value: mode 0 asymmetric Q30 low-pass, mode 1 stepped tracker with wrap |
| [`mcu_math_sqrt_fixed`](#mcu_math_sqrt_fixed) | 0x08001CDC | Fixed-point square root via CLZ normalisation, table seed and two Newton rsqrt steps |
| [`mcu_math_sqrt_fixed_v143`](#mcu_math_sqrt_fixed_v143) | (removed) | Fixed-point square root, MCU_12b/143 variant (table at 0x0800da48) |
| [`mcu_mode_bit1_inverted`](#mcu_mode_bit1_inverted) | 0x08004B54 | Return the inverse of bit 1 of mode byte 0x2000065d |
| [`mcu_moving_average6_update`](#mcu_moving_average6_update) | 0x080097BA | Push one sample into a 6-slot running-sum moving average and return the mean |
| [`mcu_msg_ring1_count`](#mcu_msg_ring1_count) | 0x08008D84 | Number of unread records in message ring 1 (write minus read index, modulo 32) |
| [`mcu_msg_ring1_pop`](#mcu_msg_ring1_pop) | 0x08008C08 | Pop one 5-word record from message ring 1 (32 entries at 0x20001B10, consumer index 0x20001B0C) |
| [`mcu_msg_ring1_push`](#mcu_msg_ring1_push) | 0x08008C8C | Append one 5-word record to message ring 1, dropping it when the ring is full |
| [`mcu_msg_ring2_count`](#mcu_msg_ring2_count) | 0x08008DA4 | Number of unread records in message ring 2 (write minus read index, modulo 32) |
| [`mcu_msg_ring2_peek`](#mcu_msg_ring2_peek) | 0x08008C58 | Copy the head record of message ring 2 without advancing its read index |
| [`mcu_msg_ring2_push`](#mcu_msg_ring2_push) | 0x08008CE4 | Append one 5-word record to message ring 2, dropping it when the ring is full |
| [`mcu_msg_rings_init`](#mcu_msg_rings_init) | 0x08008D2C | Clear both 32-entry message rings and their write and read indices |
| [`mcu_nop_stub`](#mcu_nop_stub) | 0x08005008 | Empty function (immediate return) |
| [`mcu_nop_stub_v12b`](#mcu_nop_stub_v12b) | (removed) | Empty stub present only in the MCU_12b build (immediate return) |
| [`mcu_owner_release_if_match`](#mcu_owner_release_if_match) | 0x08005EC8 | Clear the owner word at 0x200003BC if it equals the given id |
| [`mcu_pair_table_find_or_alloc`](#mcu_pair_table_find_or_alloc) | 0x0800B52A | Find or allocate a 36-byte pair-table entry for keys (a, b); mode 0 refuses a reversed (b, a) duplicate |
| [`mcu_q15_div_sat`](#mcu_q15_div_sat) | 0x08001BA0 | Fixed-point divide with Q15 result, saturating: (a << 15) / b |
| [`mcu_q15_mul_sat`](#mcu_q15_mul_sat) | 0x08001C30 | Q15 fixed-point multiply with rounding and saturation: (a*b) >> 15 |
| [`mcu_q16_mul_round`](#mcu_q16_mul_round) | 0x08001410 | Q16 fixed-point multiply with rounding: (a*b + 0x8000) >> 16 |
| [`mcu_q28_mul`](#mcu_q28_mul) | (removed) | Q28 fixed-point multiply: (a*b) >> 28 (truncating) |
| [`mcu_q30_div_sat`](#mcu_q30_div_sat) | 0x08001D6C | Fixed-point divide with Q30 result, saturating: (a << 30) / b |
| [`mcu_q30_lerp`](#mcu_q30_lerp) | 0x0800705C | Q30 blend of two values: a*t + b*(1 - t), with rounded products |
| [`mcu_q30_mul`](#mcu_q30_mul) | 0x08001DFC | Q30 fixed-point multiply: (a*b) >> 30 (truncating) |
| [`mcu_q30_mul_round`](#mcu_q30_mul_round) | 0x08001E0C | Q30 fixed-point multiply with rounding: (a*b + 2^29) >> 30 |
| [`mcu_ratio_110_to_q15`](#mcu_ratio_110_to_q15) | 0x0800CA8C | Return the byte at 0x20001FD3 divided by 110 in Q15, saturated at 1.0 |
| [`mcu_read_be16`](#mcu_read_be16) | 0x080065B8 | Read a big-endian 16-bit value from two bytes |
| [`mcu_read_le32`](#mcu_read_le32) | 0x0800D6A0 | Read a little-endian 32-bit value from four bytes at the pointer |
| [`mcu_rec8_reset_defaults`](#mcu_rec8_reset_defaults) | 0x0800CECC | Reset an 8-byte record to defaults with a 0xFFFF marker and fixed small codes |
| [`mcu_req_queue_submit`](#mcu_req_queue_submit) | 0x0800AD62 | Queue a request into a 4-slot ring of 256-byte request slots when a slot is free and code is below 243 |
| [`mcu_select_stack_local_fragment`](#mcu_select_stack_local_fragment) | 0x08002A20 | Code fragment: pick one of two caller stack slots depending on a third |
| [`mcu_set_byte_field_0x4c`](#mcu_set_byte_field_0x4c) | 0x0800A6B0 | Store a byte at struct+0x4c and return 1 |
| [`mcu_set_request_flags`](#mcu_set_request_flags) | 0x08008968 | Set request flags at 0x20001FC9 and 0x20001FCB to 1 |
| [`mcu_snapshot_copy_if_changed`](#mcu_snapshot_copy_if_changed) | 0x080057E8 | Copy a 7-word record to its shadow when the byte at +0x18 differs or a force flag is set |
| [`mcu_sort_u16_exchange`](#mcu_sort_u16_exchange) | 0x080028C0 | In-place exchange sort of a u16 array, descending when flag is 0, ascending otherwise |
| [`mcu_store_inverted_mask_0x10`](#mcu_store_inverted_mask_0x10) | 0x0800A7F0 | Store the bitwise complement of a word at struct+0x10 |
| [`mcu_store_inverted_word`](#mcu_store_inverted_word) | 0x0800B724 | Store the bitwise complement of the argument into a word |
| [`mcu_swap_u16`](#mcu_swap_u16) | 0x0800CAC4 | Swap two 16-bit values through pointers |
| [`mcu_take_pending_200003ba`](#mcu_take_pending_200003ba) | 0x08006564 | Move the byte at 0x200003BA to 0x200003BB and clear 0x200003BA |
| [`mcu_test_mask_0x10`](#mcu_test_mask_0x10) | 0x0800A81E | Return true if any bit of the mask is set in the word at struct+0x10 |
| [`mcu_track_min_nonzero_u8`](#mcu_track_min_nonzero_u8) | 0x0800A244 | Store a value in RAM byte 0x200003bc if it is smaller than the stored value or the stored value is 0 |
| [`mcu_u16_table_bsearch_desc`](#mcu_u16_table_bsearch_desc) | 0x0800A8D8 | Binary search of a descending u16 table that leaves the bracket index in a register |
| [`mcu_write_le32`](#mcu_write_le32) | 0x0800D924 | Store a 32-bit value as four little-endian bytes |
| [`mcu_xfer_queue_init`](#mcu_xfer_queue_init) | 0x0800CD18 | Arm five 300-byte transfer requests and publish the table when the control pointers are set |
| [`mcu_xfer_request_arm`](#mcu_xfer_request_arm) | 0x0800D0E8 | Arm a transfer request with buffer, length, repeat count and user argument |

## mcu_12b_bit4_offset_select

**Store the inverted bit 4 flag and add 0x48 to the base when that flag is set**

MCU_12b build only. It stores the inverse of bit 4 of param_1 in the flag byte at 0x200006E2 (1 when bit 4 is clear). If that flag is 1 the function returns param_2 + 0x48, otherwise param_2 unchanged. The 0x48 displacement suggests a choice between two layouts of a table or structure depending on a hardware or option bit, but the consumer is not in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value whose bit 4 selects the variant |
| `param_2` | `s32` | base value or offset |

**Returns** `s32`: param_2 plus 0x48 when bit 4 of param_1 is clear, else param_2

- Addresses by version: 12b: 0x0800D6B0
- Called by: `mcu_12b_0800bfd0`
- Confidence: medium

## mcu_12b_select_stack_local_fragment

**Code fragment (12b build): conditionally replace one caller stack slot with another**

Uses the stack frame of its callers (mcu_12b_08002a3c, mcu_12b_08002d0c) without its own frame: if the slot at sp+0xb8 is zero the slot at sp+0xb0 is overwritten with the slot at sp+0x20; the slot at sp+0xb0 is then returned. Outlined common tail of two routines. Equivalent of mcu_0160_08002a20 in the later builds (different frame offsets).

**Returns** `u32`: value of the stack slot at sp+0xb0 after the optional replacement

**Notes:** Fragment that shares the callers' frame.

- Addresses by version: 12b: 0x08002C00
- Called by: `mcu_12b_speed_band_update`, `mcu_12b_speed_lpf_band_update`
- Confidence: low

## mcu_add_overflow_direction_s32

**Report whether a + b would overflow int32 (+1 positive, -1 negative, 0 none)**

Pre-checks a signed 32-bit addition without performing it. Returns 1 if both operands are positive and b > INT_MAX - a (positive overflow), -1 (0xffffffff) if both are negative and a < INT_MIN - b (negative overflow), otherwise 0. Used by mcu_0160_08003c78 (accumulator / integrator saturation logic) to decide when to clamp.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | first addend |
| `param_2` | `s32` | second addend |

**Returns** `s32`: 1 = positive overflow, -1 = negative overflow, 0 = fits

- Addresses by version: 12b: 0x080028B4, 143: 0x080028F0, 152: 0x08002874, 0160: 0x08002890
- Called by: `mcu_0160_08003c78`
- Confidence: high

## mcu_array_max_s32

**Maximum of an int32 array of n elements**

Linear scan: starts with element 0 and keeps the largest of elements 1..n-1. The decompiler dropped the return statement but the running maximum is left in the return register, so the function returns the maximum (for n <= 1 it returns element 0). Called by mcu_0160_08002148. Companion of mcu_array_min_s32 (mcu_0160_08002964).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | int32 array |
| `param_2` | `s32` | number of elements |

**Returns** `s32`: maximum element (implicit in r0)

**Notes:** Return value inferred from register allocation; decompiler shows void.

- Addresses by version: 12b: 0x0800296A, 143: 0x080029A6, 152: 0x0800292A, 0160: 0x08002946
- Called by: `mcu_speed_from_max_u12`
- Confidence: high

## mcu_array_min_s32

**Minimum of an int32 array of n elements**

Linear scan returning the smallest of elements 0..n-1 (decompiler shows void but the running minimum stays in r0). Called by mcu_0160_0800209c. Companion of mcu_array_max_s32 (mcu_0160_08002946).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | int32 array |
| `param_2` | `s32` | number of elements |

**Returns** `s32`: minimum element (implicit in r0)

**Notes:** Return value inferred from register allocation.

- Addresses by version: 12b: 0x08002988, 143: 0x080029C4, 152: 0x08002948, 0160: 0x08002964
- Called by: `mcu_speed_from_period_min`
- Confidence: high

## mcu_bits_and

**Return a & b (bitwise AND of two words)**

Trivial helper returning param_1 & param_2; used by mcu_0160_08004e48, 080061fc and 0800854c to test flag bits. Group with mcu_bits_clear and mcu_bits_set.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value |
| `param_2` | `u32` | mask |

**Returns** `u32`: param_1 & param_2

- Addresses by version: 12b: 0x08003042, 143: 0x08002F3E, 152: 0x08002EC2, 0160: 0x08002ED2
- Called by: `mcu_fault_b1c_mask_any`, `mcu_fault_owner_arbitrate`, `mcu_0160_0800854c`
- Confidence: high

## mcu_bits_clear

***p &= ~mask (clear bits in a word)**

Read-modify-write helper that clears the bits given in mask in the 32-bit word at p. Called from many places (mcu_0160_08005a00, 08005ab0, 08007dc8 and the 12b equivalents) that manage flag/state words; the generated-code style (tiny helper for every bit operation) suggests machine-generated control code. Group with mcu_bits_and and mcu_bits_set.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | u32 word to modify |
| `param_2` | `u32` | mask of bits to clear |

- Addresses by version: 12b: 0x08003038, 143: 0x08002F34, 152: 0x08002EB8, 0160: 0x08002EC8
- Called by: `mcu_bus_threshold_monitor`, `mcu_fb_threshold_monitor`, `mcu_cmd_state_clear`
- Confidence: high

## mcu_bits_set

***p |= mask (set bits in a word)**

Read-modify-write helper that ORs mask into the 32-bit word at p. Called from nine routines (mcu_0160_08005a00, 08005a58, 08005ab0, 08005b3c, 08007364 and the 12b equivalents), all of which set flags in state words. Group with mcu_bits_clear and mcu_bits_and.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | u32 word to modify |
| `param_2` | `u32` | mask of bits to set |

- Addresses by version: 12b: 0x08003046, 143: 0x08002F42, 152: 0x08002EC6, 0160: 0x08002ED6
- Called by: `mcu_bus_threshold_monitor`, `mcu_speed_mismatch_check`, `mcu_fb_threshold_monitor`, `mcu_fault_monitor_update`, `mcu_0160_08007364`
- Confidence: high

## mcu_block200_alloc

**Allocate one 200-byte block from the 4088-byte first-fit pool at 0x200027CC**

Fixed-size 200-byte block allocator. The free list head is the global DAT_2000073C; each free node holds its size in bytes at +0 and the next-node pointer at +4. The first node with size >= 200 is used: an exact 200-byte node is unlinked, a larger node is split and its remainder (size - 200) is re-linked 200 bytes further on. The allocated block's size word is set to 200 and the payload pointer (block + 4) is returned, so the usable payload is 196 bytes. On first use DAT_20000740 is 0, so the pool is initialised as one 0xFF8 (4088) byte node at 0x200027CC and DAT_20000740 is set to 1; afterwards an exhausted pool returns NULL. No locking and no interrupt masking.

**Returns** `ptr`: payload pointer to a 196-byte area, or NULL when no block of 200 bytes is free

**Notes:** The pool's purpose (message or CAN buffers are likely) and the matching free routine are not in this packet. The block size word is written but not read here. Only caller: mcu_0160_08008f34.

- Addresses by version: 12b: 0x08007CAA, 143: 0x08007B9E, 152: 0x08007C26, 0160: 0x08007BCE
- Called by: `mcu_0160_08008f34`
- Confidence: high

## mcu_block_table_load_verified

**Copy a 544-byte block table into RAM and verify its block checksums, up to five attempts**

Copies a 0x220-byte table from the caller's source pointer into RAM at 0x20001D90 with mcu_copy_bytes, then checks it block by block. Each block is a 32-byte window summed with mcu_byte_sum16_store at a 16-byte stride, and the 16-bit sum is compared with the expected halfword in the table at 0x20001F90 (offset 0x200). The first mismatch restarts the copy. The function returns 1 once a full pass verifies and 0 after five failed attempts, so the caller can reject a corrupt table.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source address of the table; not shown in this packet |

**Returns** `bool`: 1 when the table verified, 0 after five failed attempts

**Notes:** The element width and the 16-byte stride are as the decompiler shows them; the windows overlap by half. The 0x20001F90 checksum base agrees with the packet's RAM reference list. Source table identity is not visible here.

- Addresses by version: 12b: 0x08008BE0, 143: 0x08008D7C, 152: 0x08008DBC, 0160: 0x08008E30
- Called by: `mcu_0160_0800b324`
- Calls: `mcu_byte_sum16_store`, `mcu_copy_bytes`
- Confidence: medium

## mcu_byte_sum16_store

**Sum a byte buffer modulo 2^16 and store the total as a halfword**

Adds up param_3 bytes starting at param_1 into a 16-bit accumulator and stores the result as a signed halfword at param_2. A zero length stores 0. The sum is not complemented, unlike mcu_byte_sum_checksum16, so this is the raw checksum body that a caller may complement or compare itself. The accumulator is a short, so the total wraps modulo 2^16 both during accumulation and on storage.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | byte buffer |
| `param_2` | `ptr` | receives the 16-bit sum as a short |
| `param_3` | `u32` | buffer length in bytes |

- Addresses by version: 12b: 0x0800C87C, 143: 0x0800CAD4, 152: 0x0800CB14, 0160: 0x0800CB74
- Called by: `mcu_block_table_load_verified`, `mcu_0160_08009f98`
- Confidence: high

## mcu_byte_sum_checksum16

**16-bit byte-sum checksum over a buffer, returned as its bitwise complement**

Adds the len unsigned bytes of the buffer into a 16-bit accumulator (the sum wraps modulo 65536) and returns the complement of that sum truncated to 16 bits. A zero-length buffer returns 0xFFFF. This is a simple additive checksum, not a CRC: summing the data together with the returned value gives 0xFFFF. Called from mcu_0160_08006460.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | data buffer |
| `param_2` | `u32` | length in bytes |

**Returns** `u16`: complement of the 16-bit byte sum

- Addresses by version: 12b: 0x08005ECC, 143: 0x08005D50, 152: 0x08005DC0, 0160: 0x08005E60
- Called by: `mcu_frame_build_5aa5_checksum`
- Confidence: high

## mcu_bytes_equal_n8

**Compare two byte strings of length n with an 8-bit counter and return 1 if equal**

memcmp-like: walks both strings from the start, returns 0 at the first differing byte, otherwise 1 (also 1 when n is 0). The index is an 8-bit counter (uVar1 = (uVar1 + 1) & 0xff), so for n above 255 the loop never exits on equal data and only mismatches stop it. Lengths 0 to 255 are the only safe use. Callers: mcu_0160_0800665c, mcu_0160_0800b324, mcu_152_08006a7c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | first byte string |
| `param_2` | `ptr` | second byte string |
| `param_3` | `u32` | byte count (use 0 to 255) |

**Returns** `u32`: 1 if the strings are equal, 0 otherwise

- Addresses by version: 12b: 0x0800A010, 143: 0x0800A1C0, 152: 0x0800A20C, 0160: 0x0800A280
- Called by: `mcu_0160_0800665c`, `mcu_0160_0800b324`
- Confidence: high

## mcu_callback_slot_dispatch

**Call the RAM function pointer in slot 0 or 1 of the two-entry table at 0x20000630**

The slot index is read from a stack argument at entry (decompiler symbol in_stack_00000008, passed by the caller on the stack; there is no register argument). For an index below 2 it loads the pointer at 0x20000630 + index*4 and calls it with no arguments. Indexes 2 and above do nothing. Because the table is in RAM, the handlers are installed at run time by code outside this packet.

| Parameter | Type | Description |
|---|---|---|
| `in_stack_00000008` | `u32` | slot index (0 or 1), read from the caller's stack at entry offset +8 |

**Notes:** The fragment shape (stack-passed index, no prototype) suggests a tail-call or shared-code fragment; the handler set is not known. Callers mcu_0160_08005edc, mcu_0160_0800672c, mcu_0160_0800a320.

- Addresses by version: 12b: 0x08008760, 143: 0x080088F0, 152: 0x08008930, 0160: 0x080089A4
- Called by: `mcu_0160_08005edc`, `mcu_0160_0800672c`, `mcu_0160_0800a320`
- Confidence: medium

## mcu_ceil_div_1024

**Ceiling of param_1 / 1024: number of 1 KiB units needed for a byte count**

Returns (value >> 10) plus one if any of the low 10 bits are set, which is ceil(value / 1024). The caller most likely converts a byte count into flash pages, since the AT32F415 erase unit is 1 KiB. Called from mcu_0160_0800cc22.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | byte count |

**Returns** `u32`: number of 1 KiB units, rounded up

**Notes:** The flash-page purpose is an inference from the 1 KiB granularity.

- Addresses by version: 12b: 0x080064C6, 143: 0x0800637E, 152: 0x080063AE, 0160: 0x0800644E
- Called by: `mcu_0160_0800cc22`
- Confidence: high

## mcu_cfg_gain_108_q15

**Return cfg+0x108 times DAT_200003CC/5.3036 as a Q15 value**

Same computation as mcu_cfg_gain_10c_q15: DAT_200003CC is divided by 5.3036 as a Q15 integer, multiplied by a configuration word and shifted right by 15. The only difference is that the word is taken from cfg+0x108 instead of cfg+0x10C, where cfg is the pointer at DAT_200000F8. The only caller in this packet is mcu_0160_0800a320.

**Returns** `u32`: Q15 product of the configuration word and the scaled input

**Notes:** Meaning of cfg+0x108 is not established.

- Addresses by version: 12b: 0x08004898, 143: 0x0800488C, 152: 0x0800496C, 0160: 0x08004A0C
- Called by: `mcu_0160_0800a320`
- Calls: `__aeabi_ddiv`, `__ARM_scalbn`, `__aeabi_d2iz`, `__aeabi_f2d`
- Confidence: medium

## mcu_cfg_gain_10c_q15

**Return cfg+0x10C times DAT_200003CC/5.3036 as a Q15 value**

Converts the f32 value DAT_200003CC to a Q15 integer by dividing it by 5.3036 (the double constant 0x401538A6_13CD503A), done in soft-float double precision: widen with __aeabi_f2d, compute 1/(c/x), which equals x/c, scale by 2^15 and truncate through mcu_0160_0800187e (double to int, not yet described). It multiplies that integer by the 32-bit configuration word at cfg+0x10C, where cfg is the pointer at DAT_200000F8, and returns the product shifted right by 15. Its twin mcu_cfg_gain_108_q15 uses cfg+0x108. Callers include mcu_0160_0800a320, mcu_0160_08004944, mcu_0160_08004db8, mcu_0160_08004e78 and mcu_0160_08008a14.

**Returns** `u32`: Q15 product of the configuration word and the scaled input

**Notes:** The meaning of cfg+0x10C and of DAT_200003CC is not established. The divisor 5.3036 is read from the double constant.

- Addresses by version: 12b: 0x08004844, 143: 0x08004838, 152: 0x08004918, 0160: 0x080049B8
- Called by: `mcu_0160_08004944`, `mcu_0160_08004db8`, `mcu_0160_08004e78`, `mcu_0160_08008a14`, `mcu_0160_0800a320`
- Calls: `__aeabi_ddiv`, `__ARM_scalbn`, `__aeabi_d2iz`, `__aeabi_f2d`
- Confidence: medium

## mcu_cond_658_and_not_a9a

**Return 1 if flag 0x20000658 is non-zero and flag 0x20000a9a is zero**

Boolean combiner of two RAM bytes: true when the configuration/enable byte DAT_20000658 is non-zero and the inhibit byte DAT_20000a9a is zero. Called from mcu_0160_08003f2c and mcu_0160_080047d0.

**Returns** `bool`: 1 if enabled and not inhibited

**Notes:** Semantics of the two flags unknown; assumed enable/inhibit.

- Addresses by version: 12b: 0x0800497C, 143: 0x08004970, 152: 0x08004A5C, 0160: 0x08004AFC
- Called by: `mcu_0160_08003f2c`, `mcu_limit_668_or_default`
- Confidence: medium

## mcu_copy_bytes

**Copy a byte block forward, one byte at a time**

Copies param_3 bytes from param_1 to param_2 in ascending order, one byte per iteration, and returns nothing. A zero count does nothing. The forward copy is only safe when the destination is below the source or the regions do not overlap. It is called from six places across the MCU and 12b builds, including mcu_12b_0800b0a4, so it is a shared utility rather than a protocol routine.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source buffer |
| `param_2` | `ptr` | destination buffer |
| `param_3` | `u32` | number of bytes |

- Addresses by version: 12b: 0x0800C958, 143: 0x0800CBC8, 152: 0x0800CC08, 0160: 0x0800CC68
- Called by: `mcu_0160_08005edc`, `mcu_0160_0800665c`, `mcu_block_table_load_verified`, `mcu_0160_08009f98`, `mcu_0160_0800b324`
- Confidence: high

## mcu_ctx_cfg_byte_set

**Store one byte into a field of the context config words at +0xA0 and +0xA4 (index 1..7)**

Always sets bit 24 of the word at struct+0xA4 (a changed flag that this function never clears), then merges the low byte of the value into one of six byte fields selected by the index: 1 = +0xA0 byte 0, 2 = +0xA0 byte 1, 3 = +0xA0 byte 2, 4 = +0xA0 byte 3, 5 = +0xA4 byte 0, 6 = +0xA4 byte 1, 7 = +0xA4 byte 2. Each write is a read-modify-write that keeps the other bytes and the flag. Any other index only sets the flag. The packet does not show the consumer of these fields, so their individual meanings are unknown; they are presumably per-channel settings of the drive context that are applied to hardware later.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | context struct; config words at +0xA0 and +0xA4, bit 24 of +0xA4 is a changed flag |
| `param_2` | `u32` | field index 1..7; other values only set the flag |
| `param_3` | `u32` | value; only the low byte is stored |

**Notes:** Owning structure and field meanings are not visible in this packet. The bit 24 flag may be a dirty bit for a later apply step.

- Addresses by version: 12b: 0x0800C648, 143: 0x0800C8A0, 152: 0x0800C8E0, 0160: 0x0800C940
- Called by: `mcu_adc1_dma_init`, `mcu_dma_channel_start`
- Confidence: medium

## mcu_ctx_clear_field_0x9c

**Clear the 32-bit field at offset 0x9C of the object**

Stores zero at param_1 + 0x9C. The field is read back by mcu_ctx_get_field_0x9c. Purpose of the field is not shown in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object |

**Notes:** Caller mcu_0160_080031cc is outside this packet.

- Addresses by version: 12b: 0x08009550, 143: 0x080096EC, 152: 0x08009738, 0160: 0x080097AC
- Called by: `mcu_speed_estimate_update`
- Confidence: high

## mcu_ctx_flag4_is_clear

**Return 1 if the byte at offset +0x04 of the object is zero, else 0**

Boolean test of the mode byte at +0x04. The same byte is the flag that mcu_hall_sector_window_update tests (a value of 1 disables the magnitude fault check).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object with byte at +0x04 |

**Returns** `bool`: 1 when the byte is zero

**Notes:** Caller mcu_0160_08003130 is outside this packet.

- Addresses by version: 12b: 0x08008E38, 143: 0x08008FD4, 152: 0x08009020, 0160: 0x08009094
- Called by: `mcu_main_ctx_flag4_clear`
- Confidence: high

## mcu_ctx_get_field_0x44

**Getter for the 32-bit raw counter at offset 0x44 of the drive context**

Returns the 32-bit word at param_1 + 0x44. This is the raw count that mcu_position_rebase captures and mcu_position_multiturn_compute extends into a multi-turn value.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | drive context |

**Returns** `s32`: raw counter value

**Notes:** Caller mcu_0160_08003104 is outside this packet.

- Addresses by version: 12b: 0x08008D24, 143: 0x08008EC0, 152: 0x08008F00, 0160: 0x08008F74
- Called by: `mcu_0160_08003104`
- Confidence: high

## mcu_ctx_get_field_0x90

**Getter returning the 32-bit field at offset 0x90 of a context struct**

Returns *(u32 *)(param_1 + 0x90). Plain accessor on the same large control/context object that mcu_12b_080029ce indexes (offsets 0xa0, 0xbc, 0xbd). No direct callers (called through a pointer table or tail position). Present in the 143 and 152 builds.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | context struct |

**Returns** `u32`: field at +0x90

**Notes:** Field meaning unknown.

- Addresses by version: 143: 0x08002A94, 152: 0x08002A18
- Called by: `mcu_0160_08003f2c`
- Confidence: medium

## mcu_ctx_get_field_0x9c

**Getter for the 32-bit field at offset 0x9C of the object**

Returns the 32-bit word at param_1 + 0x9C, the field cleared by mcu_ctx_clear_field_0x9c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object |

**Returns** `s32`: field value

**Notes:** Caller mcu_0160_080031cc is outside this packet.

- Addresses by version: 12b: 0x08009558, 143: 0x080096F4, 152: 0x08009740, 0160: 0x080097B4
- Called by: `mcu_speed_estimate_update`
- Confidence: high

## mcu_ctx_set_field_0x10

**Store a 32-bit value at offset 0x10 of a context struct**

Plain setter: it writes param_2 to the 32-bit word at param_1 + 0x10. It is the companion of mcu_ctx_set_field_0x14 and is called from the same seven setup callers, so the two fields are configured together.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | context struct |
| `param_2` | `u32` | value to store at +0x10 |

- Addresses by version: 12b: 0x0800CBA4, 143: 0x0800CE20, 152: 0x0800CE68, 0160: 0x0800CEC8
- Called by: `mcu_0160_08006028`, `mcu_gpioc_pin10_follow_flag`, `mcu_hall_dispatch_pc12_output`, `mcu_0160_08007df4`, `mcu_status_drive_pb6_pc11`, `mcu_0160_08008aac`, `mcu_indicator_update`
- Confidence: high

## mcu_ctx_set_field_0x14

**Store a 32-bit value at offset 0x14 of a context struct**

Plain setter: it writes param_2 to the 32-bit word at param_1 + 0x14. It is the counterpart of mcu_ctx_set_field_0x10 and the getters for other context offsets. The packet lists seven callers that configure the context, so the field is a per-context parameter set at setup time.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | context struct |
| `param_2` | `u32` | value to store at +0x14 |

- Addresses by version: 12b: 0x0800CBA0, 143: 0x0800CE1C, 152: 0x0800CE64, 0160: 0x0800CEC4
- Called by: `mcu_0160_08006028`, `mcu_gpioc_pin10_follow_flag`, `mcu_hall_dispatch_pc12_output`, `mcu_0160_08007df4`, `mcu_status_drive_pb6_pc11`, `mcu_0160_08008aac`, `mcu_indicator_update`
- Confidence: high

## mcu_edge_counter_force_high

**Load an edge counter with its reload value and force phase and output high**

Sets count (+0x00) to the reload value (+0x08), phase (+0x0d) to 1 and output (+0x0f) to 1, then returns 1. The next up-step continues from the reload value. The output stays high only until the next mcu_edge_counter_step recomputes it. Callers: mcu_0160_08003784, mcu_0160_08003cc8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | counter structure |

**Returns** `u32`: always 1

- Addresses by version: 12b: 0x0800981E, 143: 0x080099BA, 152: 0x08009A06, 0160: 0x08009A7A
- Called by: `mcu_0160_08003784`, `mcu_limit_chan_cfg_high_seed`
- Confidence: high

## mcu_edge_counter_init

**Initialise an edge counter with limit, reload value and output mode, then enable it**

Succeeds only if both limit (param_2) and reload (param_3) are non-zero. On success it writes count = 0, limit at +0x04, reload at +0x08, the mode byte at +0x0c, phase = 2 and latch = 2 (both undefined, so the first mcu_edge_counter_step emits no edge), output = 0 at +0x0f, and sets the enable byte at +0x10 to 1; it returns 1. On failure it clears the enable byte and returns 0, leaving the structure inert. Companion of mcu_edge_counter_step (mcu_0160_08009954). Callers: mcu_0160_08003784, mcu_0160_08005c0c, mcu_0160_08008998, mcu_12b_08005c80.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | counter structure to initialise |
| `param_2` | `u32` | counter limit (top value), must be non-zero |
| `param_3` | `u32` | reload value loaded on overflow, must be non-zero |
| `param_4` | `u8` | output mode selector 0 to 6, see mcu_edge_counter_step |

**Returns** `u32`: 1 on success, 0 if limit or reload is zero

- Addresses by version: 12b: 0x080097E4, 143: 0x08009980, 152: 0x080099CC, 0160: 0x08009A40
- Called by: `mcu_0160_08003784`, `mcu_0160_08005c0c`, `mcu_pulse_burst_decoder_init`
- Confidence: high

## mcu_edge_counter_reset

**Reset an edge counter to zero with phase and output low, keeping its configuration**

Sets count (+0x00) to 0, phase (+0x0d) to 0 and output (+0x0f) to 0, then returns 1. Limit, reload, mode, latch and enable are not touched, so the counter can be restarted without running mcu_edge_counter_init again. Callers: mcu_0160_08003434, mcu_0160_08003608, mcu_0160_08003664, mcu_0160_08003a0c, mcu_143_08003624, mcu_143_08003910, mcu_143_080052ac.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | counter structure |

**Returns** `u32`: always 1

- Addresses by version: 12b: 0x08009812, 143: 0x080099AE, 152: 0x080099FA, 0160: 0x08009A6E
- Called by: `mcu_edge_pos_track`, `mcu_limit_chan_init_mode6`, `mcu_limit_chan_update_c`, `mcu_limit_chan_cfg_d`
- Confidence: high

## mcu_edge_counter_step

**Advance a bidirectional phase counter one step and return its selected edge output bit**

Steps a counter structure and returns one output bit. Layout: u32 count at +0x00, u32 limit at +0x04, u32 reload at +0x08, u8 mode at +0x0c, u8 phase at +0x0d (0 = low, 1 = high, 2 = not yet defined), u8 last-edge latch at +0x0e, u8 output at +0x0f, u8 enable at +0x10. If the enable byte is 0 it returns 0 and changes nothing. Up-step (direction != 0): count is incremented until it reaches limit; at the limit the phase is set to 1 and count is reloaded from the reload value. Down-step: count is decremented, and when it is already 0 the phase is cleared to 0. The latch is set to 0 on a 0 to 1 phase transition and to 1 on a 1 to 0 transition. Output mode: 1 = phase high, 2 = rising edge, 3 = falling edge, 4 = any edge, 5 = phase high with latch 0, 6 = phase low with latch 1, other = 0. Modes 2 to 4 compare the phase before and after this step; modes 5 and 6 use the updated latch. It is one of a small group with mcu_edge_counter_init, mcu_edge_counter_reset and mcu_edge_counter_force_high, which operate on the same structure. Called from about a dozen motor-control sites (for example mcu_0160_08003434, mcu_0160_08008a14).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | counter structure (layout in description) |
| `param_2` | `s32` | direction: nonzero counts up, zero counts down |

**Returns** `u8`: output bit at struct+0x0f (0 or 1)

**Notes:** The algorithm is clear from the code. The meaning of phase, mode and output in the motor control is a guess.

- Addresses by version: 12b: 0x080096F8, 143: 0x08009894, 152: 0x080098E0, 0160: 0x08009954
- Called by: `mcu_edge_pos_track`, `mcu_0160_08003d2c`, `mcu_0160_08003f2c`, `mcu_digital_input_debounce`, `mcu_drive_state_update`, `mcu_a50_debounce_latch`, `mcu_run_enable_update`, `mcu_speed_mismatch_check`, `mcu_fault_monitor_update`, `mcu_pulse_burst_decode`, `mcu_0160_08008a14`, `mcu_0160_08008aac` ...
- Confidence: medium

## mcu_empty_callback

**Empty callback: returns immediately**

A single return. It is used as a hook or placeholder and is called from mcu_0160_080065f0 and from the 12b build's mcu_12b_0800bfd0. It is most likely an optional callback that is left empty in this firmware.

- Addresses by version: 12b: 0x08006688, 143: 0x08006550, 152: 0x08006580, 0160: 0x08006620
- Called by: `mcu_0160_080065f0`
- Confidence: high

## mcu_fscale_mul_div_a

**Return p1 * 1088.31 * p2 / p3 in soft-float single precision (tail call)**

Multiplies param_1 by the single-precision constant 0x448809F1 (about 1088.31), multiplies by param_2, and divides by param_3, using the soft-float routines __aeabi_fmul and __aeabi_fdiv. The last call is a tail call, so the quotient is returned in r0 even though the decompile shows void. The body is identical to mcu_fscale_mul_div_b at 0x0800765C.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | IEEE-754 single bits |
| `param_2` | `u32` | IEEE-754 single bits |
| `param_3` | `u32` | IEEE-754 single bits |

**Returns** `u32`: IEEE-754 single bits of p1 * 1088.31 * p2 / p3

**Notes:** The purpose of the constant is not identified. Callers: mcu_0160_08004DB8 and mcu_0160_080078F0.

- Addresses by version: 12b: 0x08007728, 143: 0x0800761C, 152: 0x08007694, 0160: 0x0800763C
- Called by: `mcu_0160_08004db8`, `mcu_0160_080078f0`
- Calls: `__aeabi_fmul`, `__aeabi_fdiv`
- Confidence: medium

## mcu_fscale_mul_div_b

**Return p1 * 1088.31 * p2 / p3 (soft-float single), twin of mcu_fscale_mul_div_a**

Same code as mcu_fscale_mul_div_a at 0x0800763C: multiplies param_1 by the constant 0x448809F1, multiplies by param_2, and divides by param_3 with __aeabi_fmul and __aeabi_fdiv. The final divide is a tail call that returns the quotient in r0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | IEEE-754 single bits |
| `param_2` | `u32` | IEEE-754 single bits |
| `param_3` | `u32` | IEEE-754 single bits |

**Returns** `u32`: IEEE-754 single bits of p1 * 1088.31 * p2 / p3

**Notes:** Two identical copies at adjacent addresses, probably one per channel or per build. Callers match mcu_fscale_mul_div_a.

- Addresses by version: 12b: 0x08007748, 143: 0x0800763C, 152: 0x080076B4, 0160: 0x0800765C
- Called by: `mcu_0160_08004db8`, `mcu_0160_080078f0`
- Calls: `__aeabi_fmul`, `__aeabi_fdiv`
- Confidence: medium

## mcu_get_cfg_field_0x28

**Return the 32-bit field at offset 0x28 of the struct pointed to by DAT_200000f8**

DAT_200000f8 holds a pointer to a configuration/state structure; the function returns the word at +0x28. Called from mcu_0160_0800a320 and 0800c6f0. See mcu_0160_080046d8, which reads the same field and passes it through a Q15 multiply by 1.0.

**Returns** `u32`: field at +0x28 of *DAT_200000f8

**Notes:** Struct and field meaning unknown.

- Addresses by version: 12b: 0x08004558, 143: 0x0800454C, 152: 0x0800462C, 0160: 0x080046CC
- Called by: `mcu_0160_0800a320`, `mcu_telemetry_group_get`
- Confidence: medium

## mcu_get_cfg_field_0x28_q15

**Return field +0x28 of *DAT_200000f8 after a (x * 0x8000) >> 15 round trip**

Loads the word at *(DAT_200000f8 + 0x28), multiplies it by 0x8000 in 64 bits and shifts the product right by 15, which is an identity (a Q15 multiply by 1.0 left in by the generated code). Returns the same value as mcu_0160_080046cc but is the variant used by the control routines mcu_0160_08003f2c, 08004e78, 080052bc, 08005424 (and mcu_143_080052ac).

**Returns** `s32`: field at +0x28 (Q15 value)

**Notes:** Identity operation; the code is evidently generated from a fixed-point model.

- Addresses by version: 12b: 0x08004564, 143: 0x08004558, 152: 0x08004638, 0160: 0x080046D8
- Called by: `mcu_0160_08003f2c`, `mcu_0160_08004e78`, `mcu_drive_state_update`, `mcu_neg_limit_flag_update`
- Confidence: medium

## mcu_get_field_0x0c_ashr_scale

**Return the s32 field at +0x0c arithmetic-shifted right by the scale byte at +0x32**

Same pattern as the other scaled getters: returns *(s32 *)(struct + 0x0c) >> (s8)(struct + 0x32). Callers: mcu_0160_08003f2c, mcu_0160_0800a56c, mcu_0160_0800a570, mcu_143_080052ac.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | struct holding the value at +0x0c and the shift count at +0x32 |

**Returns** `s32`: field >> scale

- Addresses by version: 12b: 0x0800A290, 143: 0x0800A4C4, 152: 0x0800A514, 0160: 0x0800A588
- Called by: `mcu_0160_08003f2c`, `mcu_get_field_0x0c_ashr_scale_thunk1`, `mcu_get_field_0x0c_ashr_scale_thunk2`
- Confidence: high

## mcu_get_field_0x0c_ashr_scale_thunk1

**Tail-call thunk to mcu_get_field_0x0c_ashr_scale**

Single branch instruction that tail-calls mcu_0160_0800a588 (mcu_get_field_0x0c_ashr_scale). The target returns the signed 32-bit word at +0x0C of the object, arithmetic-shifted right by the signed count byte at +0x32. This entry is the thunk the caller mcu_0160_080039e0 uses; the decompiler shows the target's body here.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object: s32 value at +0x0C, signed shift count byte at +0x32 |

**Returns** `s32`: the value at +0x0C shifted right by the count at +0x32

- Addresses by version: 152: 0x0800A4F8, 0160: 0x0800A56C
- Called by: `mcu_b90_low_and_enabled`
- Calls: `mcu_get_field_0x0c_ashr_scale`
- Confidence: high

## mcu_get_field_0x0c_ashr_scale_thunk2

**Second tail-call thunk to mcu_get_field_0x0c_ashr_scale**

Single branch instruction, the same shape as mcu_get_field_0x0c_ashr_scale_thunk1, that tail-calls mcu_0160_0800a588. It returns the signed 32-bit word at +0x0C arithmetic-shifted right by the signed count byte at +0x32. The caller here is mcu_0160_08003d2c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object: s32 value at +0x0C, signed shift count byte at +0x32 |

**Returns** `s32`: the value at +0x0C shifted right by the count at +0x32

- Addresses by version: 152: 0x0800A4FC, 0160: 0x0800A570
- Called by: `mcu_0160_08003d2c`
- Calls: `mcu_get_field_0x0c_ashr_scale`
- Confidence: high

## mcu_get_field_0x10_ashr_scale

**Return the s32 field at +0x10 arithmetic-shifted right by the scale byte at +0x32**

Returns *(s32 *)(struct + 0x10) >> (s8)(struct + 0x32), a sign-preserving shift that rescales a stored value by a per-object power of two. The shift count is a signed byte; the Cortex-M ASR-by-register instruction uses only the low byte, so counts of 32 or more return 0 or -1. Present in MCU_12b and MCU_143 only. Called from mcu_143_080052ac.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | struct holding the value at +0x10 and the shift count at +0x32 |

**Returns** `s32`: field >> scale

**Notes:** Which quantity is at +0x10 and its unit are not visible in this packet.

- Addresses by version: 12b: 0x0800A278, 143: 0x0800A4AC
- Called by: `mcu_b90_low_and_enabled`, `mcu_143_080052ac`
- Confidence: high

## mcu_get_field_0x18_ashr_scale

**Return the s32 field at +0x18 arithmetic-shifted right by the scale byte at +0x32**

Same pattern as mcu_get_field_0x10_ashr_scale: returns *(s32 *)(struct + 0x18) >> (s8)(struct + 0x32). Present in MCU_12b and MCU_143 only. Called from mcu_143_080052ac.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | struct holding the value at +0x18 and the shift count at +0x32 |

**Returns** `s32`: field >> scale

- Addresses by version: 12b: 0x0800A284, 143: 0x0800A4B8
- Called by: `mcu_0160_08003d2c`, `mcu_143_080052ac`
- Confidence: high

## mcu_get_global_ctx_field_0x64

**Return the 32-bit word at offset 0x64 of the object pointed to by global DAT_2000002C**

Dereferences the global pointer at 0x2000002C and returns the word at +0x64 of that object. Present in the MCU_152 and MCU_0160 builds only.

**Returns** `u32`: word at +0x64 of the object

**Notes:** The owning object and the meaning of the word are not established in this packet. Caller mcu_0160_0800c6f0.

- Addresses by version: 152: 0x08009014, 0160: 0x08009088
- Called by: `mcu_telemetry_group_get`
- Confidence: medium

## mcu_get_param_654_q15

**Return the byte/halfword at 0x20000654 shifted into Q15 (<< 15)**

Zero-extends DAT_20000654 and shifts it left by 15, converting an integer configuration value into Q15 fixed point. Called from mcu_0160_08003f2c, 0800500c, 08005090, 080051bc (and mcu_12b_08004e74).

**Returns** `s32`: DAT_20000654 * 0x8000

- Addresses by version: 12b: 0x08004970, 143: 0x08004964, 152: 0x08004A44, 0160: 0x08004AE4
- Called by: `mcu_0160_08003f2c`, `mcu_0160_0800500c`, `mcu_fb_lpf_select_update`, `mcu_digital_input_debounce`
- Confidence: high

## mcu_get_u16_field_0x34

**Return the u16 field at struct+0x34**

Getter: returns the 16-bit value at struct+0x34. Called from mcu_0160_08009160.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | structure |

**Returns** `u16`: field at struct+0x34

**Notes:** Field name and meaning are not visible in this packet.

- Addresses by version: 12b: 0x0800A6B4, 143: 0x0800A8E8, 152: 0x0800A7A4, 0160: 0x0800A818
- Called by: `mcu_0160_08009160`
- Confidence: high

## mcu_get_var_2026

**Getter returning the byte at 0x20002026**

Returns the unsigned byte stored at RAM address 0x20002026 unchanged. Called only from mcu_0160_08008a14. It is a pure accessor, so other modules do not touch the variable directly. Its meaning is not known from this function.

**Returns** `u8`: value of 0x20002026

- Addresses by version: 12b: 0x080065DC, 143: 0x080064A4, 152: 0x080064D4, 0160: 0x08006574
- Called by: `mcu_0160_08008a14`
- Confidence: high

## mcu_get_var_34c_ashr_scale

**Return RAM word 0x2000034c arithmetic-shifted right by the scale byte at struct+0x32**

Reads the 32-bit RAM variable at 0x2000034c and returns it shifted right by the signed byte at struct+0x32. It is the global-variable version of mcu_get_field_0x0c_ashr_scale. Present in MCU_152 and MCU_0160 only. Callers: mcu_0160_08003f2c, mcu_0160_080052bc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | scale descriptor; only the shift count at +0x32 is used |

**Returns** `s32`: RAM word at 0x2000034c >> scale

- Addresses by version: 152: 0x0800A500, 0160: 0x0800A574
- Called by: `mcu_0160_08003f2c`, `mcu_drive_state_update`
- Confidence: high

## mcu_get_var_650

**Getter returning the 32-bit RAM variable at 0x20000650**

Returns DAT_20000650. Called from mcu_0160_08003f2c only. Part of a family of getters for parameters stored at 0x2000065x (0x20000654, 0x20000658, 0x20000660 ...) which look like a configuration/status block.

**Returns** `u32`: value of 0x20000650

**Notes:** Meaning of the variable unknown.

- Addresses by version: 12b: 0x08004580, 143: 0x08004574, 152: 0x08004654, 0160: 0x080046F4
- Called by: `mcu_0160_08003f2c`
- Confidence: high

## mcu_get_var_67c

**Getter returning the 32-bit RAM variable at 0x2000067c**

Returns DAT_2000067c unchanged. Only present in the 152 and 0160 builds; called from mcu_0160_08005090.

**Returns** `u32`: value of 0x2000067c

**Notes:** Meaning unknown.

- Addresses by version: 152: 0x08004A50, 0160: 0x08004AF0
- Called by: `mcu_fb_lpf_select_update`
- Confidence: high

## mcu_get_var_f60

**Getter returning the 16-bit RAM value at 0x20000f60**

Returns DAT_20000f60 unchanged (zero-extended 16-bit load). Called only from mcu_0160_0800a90c. Pure accessor used so other modules do not touch the variable directly.

**Returns** `u16`: value of 0x20000f60

**Notes:** Meaning of the variable unknown.

- Addresses by version: 12b: 0x08002220, 143: 0x0800225C, 152: 0x080021E0, 0160: 0x080021FC
- Called by: `mcu_indicator_update`
- Confidence: high

## mcu_get_word_at_0x6c

**Getter returning the 32-bit word at offset 0x6c of a structure**

Returns *(u32 *)(struct + 0x6c) with no check. Same pattern as the other one-word getters in this component (for example mcu_get_word_at_0x90). Called from mcu_0160_0800314c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | structure base pointer |

**Returns** `u32`: word at struct+0x6c

**Notes:** Field meaning is not visible from this function alone.

- Addresses by version: 12b: 0x08009588, 143: 0x08009724, 152: 0x08009770, 0160: 0x080097E4
- Called by: `mcu_position_outlier_reject`
- Confidence: high

## mcu_get_word_at_0x90

**Getter returning the 32-bit word at offset 0x90 of a structure**

Returns *(u32 *)(param_1 + 0x90). Only called from mcu_0160_08003f2c, so param_1 is a context/state structure used by that routine; the field's meaning is unknown from this function alone. Present only in the MCU_0160 build.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | base address of a struct instance |

**Returns** `u32`: field at offset 0x90

**Notes:** Field purpose unknown; name is positional.

- Addresses by version: 0160: 0x08001436
- Called by: `mcu_0160_08003f2c`
- Confidence: medium

## mcu_init_q14_copies_from_200003de

**Set four RAM words to the byte at 0x200003DE shifted left by 14 (Q14)**

Computes (unsigned value at 0x200003DE) << 14 and stores it at 0x2000024C, then copies the same value to 0x20000258, 0x20000230 and 0x2000023C. All four words therefore start equal to the input in Q14 (0x4000 = 1.0 per unit). Present in the 152 and 0160 builds only. Called from mcu_0160_08003784.

**Notes:** The width of the source variable at 0x200003DE is not shown; it is read as an unsigned byte here. Its meaning is unknown.

- Addresses by version: 152: 0x080072D4, 0160: 0x0800727C
- Called by: `mcu_0160_08003784`
- Confidence: medium

## mcu_latched_value_set

**Store a 32-bit value and set the valid flag byte at struct+0x04**

Writes the u32 argument to struct+0x00, sets the byte at struct+0x04 to 1 and returns 1. The flag is probably a 'value present' marker that readers check before using the stored word, following the valid-flag convention used elsewhere in this component (mcu_param_block3_init_checked).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | value holder: u32 value at +0x00, valid byte at +0x04 |
| `param_2` | `u32` | value to store |

**Returns** `u32`: always 1

**Notes:** The meaning of the flag is inferred from the pattern.

- Addresses by version: 12b: 0x08009C5C, 143: 0x08009DF8, 152: 0x08009E44, 0160: 0x08009EB8
- Called by: `mcu_0160_0800729c`
- Confidence: medium

## mcu_lpf_asym_update

**Enable-gated Q30 low-pass with separate rising and falling coefficients**

The input pointer is word 0 of the object and the filtered state is word 1. When the enable byte at +0x1E is set it filters the input with mcu_lpf_q30_step_alt. If the direction-select byte at +0x1C is zero it uses the coefficient in word 2 for all steps; otherwise it uses word 2 when the input is above the state and word 6 when it is not. When the enable byte is zero it copies the input into the state and returns it.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | filter object: word 0 input pointer, word 1 state, word 2 coefficient, word 6 falling coefficient, +0x1C direction select, +0x1E enable |

**Returns** `s32`: filtered state

**Notes:** Same algorithm as the mode-0 path of mcu_lpf_or_step_tracker_update with different offsets. Callers: mcu_0160_08002B64, mcu_12b_08002A3C and mcu_12b_08002D0C.

- Addresses by version: 12b: 0x080072B4, 143: 0x08007188, 152: 0x080071B8, 0160: 0x08007160
- Called by: `mcu_speed_lpf_band_update`
- Calls: `mcu_lpf_q30_step_alt`
- Confidence: high

## mcu_lpf_or_step_tracker_update

**Update a tracked value: mode 0 asymmetric Q30 low-pass, mode 1 stepped tracker with wrap**

The input is read through the pointer in word 0 of the object, and the state is word 1. When the enable byte at +0x22 is zero the input is copied to the state and returned. Mode 0 (byte +0x18 zero) low-passes the input with the Q30 coefficient at +0x08, or with the falling coefficient at +0x1C when the direction flag at +0x20 is set and the input is below the state. Mode 1 is a stepper: when the input is at least the threshold at +0x14 above the state the target is the state plus the step at +0x0C, and when it is at least the threshold below the state the target is the state minus the step, otherwise the target is the state. The target is low-passed toward the input with the coefficient at +0x08, then wrapped by one step (+0x0C) against the limit at +0x10. Any other mode returns 0 without changing the state.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | tracker object: word 0 input pointer, word 1 state, +0x08 coefficient, +0x0C step, +0x10 wrap limit, +0x14 threshold, +0x18 mode, +0x1C falling coefficient, +0x20 direction flag, +0x22 enable |

**Returns** `s32`: updated state, or 0 for an unknown mode

**Notes:** Mode 1 is a guess at a periodic or angle-tracking use: the step and wrap behaviour fits an angle or position unwrapper. Group with mcu_lpf_asym_update, which is the same filter without the stepper.

- Addresses by version: 12b: 0x08007200, 143: 0x080070D4, 152: 0x08007104, 0160: 0x080070AC
- Called by: `mcu_limit_target_b3c_update`, `mcu_0160_08007364`
- Calls: `mcu_lpf_q30_step`
- Confidence: medium

## mcu_math_sqrt_fixed

**Fixed-point square root via CLZ normalisation, table seed and two Newton rsqrt steps**

Returns in r0 roughly sqrt(param_1 * 2^17) (e.g. a Q15 input gives a Q16 result). Normalises the argument with CLZ, seeds 1/sqrt from a 1024-entry table at 0x0800dc20 indexed by the top 10 bits, refines with two Newton-Raphson steps y' = y*(1.5 - 0.5*x*y^2) in 32x32->high-word arithmetic, multiplies by x to get sqrt, applies a 0xb504f334 (1/sqrt2) factor for odd exponents and shifts back with rounding. Inputs <= 0 (CLZ=0 or 32) return 0. param_2 is passed through in r1 for the zero case; r1 is otherwise an auxiliary value and is ignored by callers. Callers: mcu_0160_08005830, 08006f74, 08007364 (magnitude of d/q vectors etc.).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-negative fixed-point value |
| `param_2` | `u32` | unused pass-through |

**Returns** `u64`: low word = sqrt result, high word = scratch

**Notes:** Output scaling derived from the shift constants (+15); the 143/12b variant uses +2 instead.

- Addresses by version: 12b: 0x08001CC0, 143: 0x08001CC0, 152: 0x08001CC0, 0160: 0x08001CDC
- Called by: `mcu_0160_08005830`, `mcu_sqrt_limit_setup_float`, `mcu_0160_08007364`
- Confidence: medium

## mcu_math_sqrt_fixed_v143

**Fixed-point square root, MCU_12b/143 variant (table at 0x0800da48)**

Same algorithm as mcu_0160_08001cdc (CLZ normalise, table seed, two Newton rsqrt iterations, 1/sqrt2 for odd exponent) but the output scale constant is +2 instead of +15 and the seed table is at 0x0800da48, so the result is sqrt(param_1 * 2^30) (a different Q format than the 0160 build). Inputs <= 0 return 0 with param_2 in r1. Single caller mcu_143_0800a580.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-negative fixed-point value |
| `param_2` | `u32` | unused pass-through |

**Returns** `u64`: low word = sqrt result

**Notes:** Scale derived from shift constants only.

- Addresses by version: 12b: 0x08001D6C, 143: 0x08001D60
- Called by: `mcu_pos_tracker_update_v143`
- Confidence: medium

## mcu_mode_bit1_inverted

**Return the inverse of bit 1 of mode byte 0x2000065d**

Returns (~(DAT_2000065d >> 1)) & 1, i.e. 1 when bit 1 of the mode/status byte is clear. Called only from mcu_0160_08003f2c. Companion accessor to mcu_0160_08004b1c (bit 0) and mcu_0160_08005550 (bits 2..4).

**Returns** `u8`: 1 if bit1 clear, else 0

- Addresses by version: 12b: 0x080049D4, 143: 0x080049C8, 152: 0x08004AB4, 0160: 0x08004B54
- Called by: `mcu_0160_08003f2c`
- Confidence: high

## mcu_moving_average6_update

**Push one sample into a 6-slot running-sum moving average and return the mean**

Ring-buffer moving average with six slots. The byte at struct+0x00 is the write index and is advanced as (index + 1) % 6. The sample previously stored in that slot (s32 array at +0x04..+0x1b) is subtracted from the running sum at +0x20, the new sample is added (sum += new - old) and written into the slot. Returns sum / 6 using signed 32-bit division, so the mean is truncated toward zero. The first six outputs are biased by the initial contents of the array and sum, which the caller sets up.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | new sample |
| `param_2` | `ptr` | filter state: u8 index at +0x00, s32 samples[6] at +0x04, s32 running sum at +0x20 |

**Returns** `s32`: mean of the six most recent samples (sum / 6)

**Notes:** The signal being averaged is not visible in this packet; the only caller is mcu_0160_08009160.

- Addresses by version: 12b: 0x0800955E, 143: 0x080096FA, 152: 0x08009746, 0160: 0x080097BA
- Called by: `mcu_0160_08009160`
- Confidence: high

## mcu_msg_ring1_count

**Number of unread records in message ring 1 (write minus read index, modulo 32)**

Returns (DAT_20001B08 - DAT_20001B0C) mod 32: the difference, plus 32 when the read index is ahead of the write index, masked to 16 bits. The result is 0 to 31, since one slot is kept free.

**Returns** `u16`: pending records in ring 1, 0..31

**Notes:** Caller mcu_0160_08008b60 is outside this packet.

- Addresses by version: 12b: 0x08008B34, 143: 0x08008CD0, 152: 0x08008D10, 0160: 0x08008D84
- Called by: `mcu_0160_08008b60`
- Confidence: high

## mcu_msg_ring1_pop

**Pop one 5-word record from message ring 1 (32 entries at 0x20001B10, consumer index 0x20001B0C)**

Ring 1 has 32 records of five 32-bit words (stride 20 bytes) starting at 0x20001B10. The write (producer) index is DAT_20001B08 and the read (consumer) index is DAT_20001B0C. If they differ, the record at the consumer index is copied to the caller's struct (word 0 to +0, word 1 to +4, word 2 to +8, word 3 to +0xC, word 4 to +0x10) and the consumer index is advanced with mask 0x1F. If the ring is empty the caller's struct is left untouched. There is no interrupt masking, so the ring is only safe for one producer and one consumer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination: five 32-bit words |

**Notes:** The record contents (probably CAN or command data) are not identified in this packet. Caller mcu_0160_08008b60 checks the count first (mcu_msg_ring1_count) and is outside this packet.

- Addresses by version: 12b: 0x080089B8, 143: 0x08008B54, 152: 0x08008B94, 0160: 0x08008C08
- Called by: `mcu_0160_08008b60`
- Confidence: high

## mcu_msg_ring1_push

**Append one 5-word record to message ring 1, dropping it when the ring is full**

The ring is full when (DAT_20001B08 + 1) & 0x1F equals the read index DAT_20001B0C (one slot is kept free, so a full ring holds 31 records). If not full, the five words of the source record are stored at the write index: word 0 to 0x20001B10, word 1 to 0x20001B14, word 2 to 0x20001B18, word 3 to 0x20001B1C and word 4 to 0x20001B20, and the write index is advanced with mask 0x1F. When full the record is silently dropped. No interrupt masking.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source record: five 32-bit words |

**Notes:** Only caller in this packet: mcu_0160_080032cc. Drops on full are not reported to the caller.

- Addresses by version: 12b: 0x08008A3C, 143: 0x08008BD8, 152: 0x08008C18, 0160: 0x08008C8C
- Called by: `CAN1_RX0_IRQHandler`
- Confidence: high

## mcu_msg_ring2_count

**Number of unread records in message ring 2 (write minus read index, modulo 32)**

Returns (DAT_20001880 - DAT_20001884) mod 32 with the same logic as mcu_msg_ring1_count, using ring 2's write index DAT_20001880 and read index DAT_20001884. Result 0 to 31.

**Returns** `u16`: pending records in ring 2, 0..31

**Notes:** Caller mcu_0160_08008bb4 is outside this packet.

- Addresses by version: 12b: 0x08008B54, 143: 0x08008CF0, 152: 0x08008D30, 0160: 0x08008DA4
- Called by: `mcu_msg_ring2_tx_step`
- Confidence: high

## mcu_msg_ring2_peek

**Copy the head record of message ring 2 without advancing its read index**

Ring 2 has the same layout as ring 1, with its records starting at 0x20001888 (stride 20 bytes), write index DAT_20001880 and read index DAT_20001884. If the two differ, the record at the read index is copied to the destination: word 0 from 0x20001888, word 1 from 0x2000188C, word 2 from 0x20001890, word 3 from 0x20001894 and word 4 from 0x20001898. Unlike the ring 1 pop, this routine does not advance DAT_20001884, so the caller must do it after use. If the ring is empty the destination is left untouched.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination: five 32-bit words |

**Notes:** The advance of the read index is not in this function. Its caller mcu_0160_08008bb4 is outside this packet; if that caller does not advance DAT_20001884 the head record would be read repeatedly, so it is worth checking.

- Addresses by version: 12b: 0x08008A08, 143: 0x08008BA4, 152: 0x08008BE4, 0160: 0x08008C58
- Called by: `mcu_msg_ring2_tx_step`
- Confidence: high

## mcu_msg_ring2_push

**Append one 5-word record to message ring 2, dropping it when the ring is full**

Same algorithm as mcu_msg_ring1_push on ring 2: write index DAT_20001880, read index DAT_20001884, full when (DAT_20001880 + 1) & 0x1F equals DAT_20001884. Words 0 to 4 of the source record are stored at 0x20001888, 0x2000188C, 0x20001890, 0x20001894 and 0x20001898 for the write index, which is then advanced with mask 0x1F. Records are dropped when full, with no interrupt masking.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source record: five 32-bit words |

**Notes:** Callers mcu_0160_0800bc70 and mcu_0160_0800c294 are outside this packet.

- Addresses by version: 12b: 0x08008A94, 143: 0x08008C30, 152: 0x08008C70, 0160: 0x08008CE4
- Called by: `mcu_msg_ring2_enqueue_frames`, `mcu_can_frame_enqueue`
- Confidence: high

## mcu_msg_rings_init

**Clear both 32-entry message rings and their write and read indices**

Sets the indices of ring 1 (DAT_20001B08 write, DAT_20001B0C read) to 0 and zeroes its 32 five-word records from 0x20001B10. Then does the same for ring 2 (DAT_20001880 write, DAT_20001884 read, records from 0x20001888). Afterwards both rings are empty.

**Notes:** Called from mcu_0160_0800d548, the application main entry reached from app_main_thunk.

- Addresses by version: 12b: 0x08008ADC, 143: 0x08008C78, 152: 0x08008CB8, 0160: 0x08008D2C
- Called by: `mcu_0160_0800d548`
- Confidence: high

## mcu_nop_stub

**Empty function (immediate return)**

Single return instruction; a placeholder or optimised-out hook. Called from mcu_0160_08005090 (probably a call to a feature that is compiled out in this build). Present in the 143, 152 and 0160 builds.

- Addresses by version: 143: 0x08004E68, 152: 0x08004F68, 0160: 0x08005008
- Called by: `mcu_fb_lpf_select_update`
- Confidence: high

## mcu_nop_stub_v12b

**Empty stub present only in the MCU_12b build (immediate return)**

Bare return. It exists only in the MCU_12b build and no function in the packet calls it directly, so it is probably a callback or default slot reached through a pointer. It plays the same role as mcu_nop_stub in the other builds.

**Notes:** The slot it fills is unknown.

- Addresses by version: 12b: 0x0800B0A0
- Called by: `mcu_0160_0800a480`
- Confidence: low

## mcu_owner_release_if_match

**Clear the owner word at 0x200003BC if it equals the given id**

Compare-and-clear on the 32-bit word at 0x200003BC: when it equals param_1 it is set to zero, otherwise it is left unchanged. This is the release half of a single-owner token, where only the owner whose id is stored can release it. Callers are mcu_0160_080061fc and mcu_0160_08007dc8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | owner id to release |

**Notes:** The guarded resource is not identified in this packet.

- Addresses by version: 12b: 0x08005F14, 143: 0x08005DB8, 152: 0x08005E28, 0160: 0x08005EC8
- Called by: `mcu_fault_owner_arbitrate`, `mcu_cmd_state_clear`
- Confidence: medium

## mcu_pair_table_find_or_alloc

**Find or allocate a 36-byte pair-table entry for keys (a, b); mode 0 refuses a reversed (b, a) duplicate**

Searches a table of 36-byte entries (base pointer at table+0x00, u16 count at table+0x04). Entry byte 0 and byte 1 are the two keys, and byte 2 is the state, where 1 means free and any other value means in use. Mode 0 (strict): first scans for an in-use entry with keys reversed (b, a); if one exists it returns NULL. Otherwise it looks for an in-use entry with keys (a, b) and returns it, else the first free entry, else NULL. Non-zero mode skips the reversed check and does only the in-use (a, b) lookup and then the free-entry allocation. The caller fills the returned entry. Callers: mcu_0160_0800d038, mcu_0160_0800d0b0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | table header: entry base pointer at +0x00, u16 entry count at +0x04 |
| `param_2` | `u8` | key a (entry byte 0 on a match) |
| `param_3` | `u8` | key b (entry byte 1 on a match) |
| `param_4` | `s32` | 0 = strict mode with reversed-duplicate refusal; non-zero = lookup or allocate only |

**Returns** `ptr`: pointer to the matching or newly free entry, or NULL

**Notes:** Key meanings are unknown. The exclusion of reversed pairs suggests a bidirectional link table, but this is a guess.

- Addresses by version: 12b: 0x0800B216, 143: 0x0800B4C6, 152: 0x0800B4CA, 0160: 0x0800B52A
- Called by: `mcu_can_tp_rx_dispatch`, `mcu_can_tp_session_start`
- Confidence: medium

## mcu_q15_div_sat

**Fixed-point divide with Q15 result, saturating: (a << 15) / b**

Returns a*2^15/b using sign-magnitude long division in steps: it pre-shifts |a| by up to 14 bits (clz limited), divides, then iterates on the remainder shifting in further fractional bits until 15 total bits are produced, truncating toward zero. Division by zero returns 0x7fffffff; if the quotient would overflow it saturates to 0x7fffffff (same signs) or 0x80000000. Called by many control routines (current/voltage normalisation). Companion of the Q30 variant mcu_0160_08001d6c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | numerator a |
| `param_2` | `s32` | denominator b |

**Returns** `s32`: a/b in Q15, saturated

**Notes:** Q15 scale is inferred from the constant 0xf (15) in the shift logic.

- Addresses by version: 12b: 0x08001B84, 143: 0x08001B84, 152: 0x08001B84, 0160: 0x08001BA0
- Called by: `mcu_ctrl_ramp_limit_update`, `mcu_speed_lpf_band_update`, `mcu_0160_08003c78`, `mcu_0160_08003d2c`, `mcu_0160_08003f2c`, `mcu_target_derate_calc`, `mcu_limit_target_b3c_update`, `mcu_ratio_gain_clamped_q15`, `mcu_dynamic_bound_clamp_update`, `mcu_scaled_ratio_clamp_q15`, `mcu_speed_range_setup_core`, `mcu_pos_tracker_init` ...
- Confidence: medium

## mcu_q15_mul_sat

**Q15 fixed-point multiply with rounding and saturation: (a*b) >> 15**

Computes the signed 64-bit product, shifts right by 15 with round-half-up (bit 14), and saturates to 0x7fffffff / 0x80000000 if the result does not fit in 32 bits (checks (hi >> 14) + 1 >> 1 != 0). Called throughout the FOC/PI code, e.g. from mcu_0160_08001e5a, 08002b64, 0800480c and 080055c4.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | operand a |
| `param_2` | `s32` | operand b |

**Returns** `s32`: (a*b)>>15, saturated

**Notes:** Q-format of the operands is inferred from the shift only.

- Addresses by version: 12b: 0x08001C14, 143: 0x08001C14, 152: 0x08001C14, 0160: 0x08001C30
- Called by: `mcu_cascade_observer_step`, `mcu_speed_lpf_band_update`, `mcu_target_derate_calc`, `mcu_limit_target_b3c_update`, `mcu_speed_range_setup_core`
- Confidence: medium

## mcu_q16_mul_round

**Q16 fixed-point multiply with rounding: (a*b + 0x8000) >> 16**

Forms the signed 64-bit product of the two arguments and returns bits 16..47 of it, plus 1 if bit 15 is set (round half up). Assuming both operands are Q16 (or one Q16 and one integer) the result keeps the Q16 scale. Single caller mcu_0160_08009598, which also uses the Q30 helpers 08001d6c/08001e0c, i.e. part of one fixed-point calculation.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | operand a |
| `param_2` | `s32` | operand b |

**Returns** `s32`: (a*b)>>16, rounded

**Notes:** Q-format of the operands is inferred from the shift only.

- Addresses by version: 12b: 0x08001D50, 143: 0x08001410, 152: 0x08001410, 0160: 0x08001410
- Called by: `mcu_hall_position_update`
- Confidence: medium

## mcu_q28_mul

**Q28 fixed-point multiply: (a*b) >> 28 (truncating)**

Signed 64-bit product shifted right by 28 (low word >> 28 plus high word << 4), no rounding or saturation. Only present in MCU_12b and MCU_143; its single caller is mcu_143_0800a580, which also uses mcu_143_08001d60. The later builds use other Q formats.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | operand a |
| `param_2` | `s32` | operand b |

**Returns** `s32`: (a*b)>>28

**Notes:** Q-format inferred from the shift only.

- Addresses by version: 12b: 0x08001D5C, 143: 0x08001D50
- Called by: `mcu_pos_tracker_update_v143`
- Confidence: medium

## mcu_q30_div_sat

**Fixed-point divide with Q30 result, saturating: (a << 30) / b**

Same long-division scheme as mcu_0160_08001ba0 but producing 30 fractional bits (clz limited to 0x1e). Division by zero returns 0x7fffffff; overflow saturates to 0x7fffffff or 0x80000000 depending on sign agreement; result truncates toward zero. Single caller mcu_0160_08009598.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | numerator a |
| `param_2` | `s32` | denominator b |

**Returns** `s32`: a/b in Q30, saturated

**Notes:** Q30 inferred from the 0x1e constants.

- Addresses by version: 12b: 0x08001DD8, 143: 0x08001DCC, 152: 0x08001D50, 0160: 0x08001D6C
- Called by: `mcu_hall_position_update`
- Confidence: medium

## mcu_q30_lerp

**Q30 blend of two values: a*t + b*(1 - t), with rounded products**

Computes param_1 times t plus param_2 times (0x40000000 - t), where t is the Q30 weight in param_3, using mcu_q30_mul_round for both products. A weight of 0x40000000 gives the first argument and 0 gives the second, up to rounding. Its caller in this packet is mcu_0160_08009598.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | value a |
| `param_2` | `s32` | value b |
| `param_3` | `s32` | Q30 weight t |

**Returns** `s32`: a*t + b*(1 - t), rounded

- Addresses by version: 12b: 0x080071B0, 143: 0x08007084, 152: 0x080070B4, 0160: 0x0800705C
- Called by: `mcu_hall_position_update`
- Calls: `mcu_q30_mul_round`
- Confidence: high

## mcu_q30_mul

**Q30 fixed-point multiply: (a*b) >> 30 (truncating)**

Signed 64-bit product shifted right 30 bits (low word >> 30 plus high word * 4), no rounding. Callers: mcu_0160_08001e5a and mcu_0160_0800767c. The rounding twin is mcu_0160_08001e0c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | operand a |
| `param_2` | `s32` | operand b |

**Returns** `s32`: (a*b)>>30

**Notes:** Q-format inferred from the shift only.

- Addresses by version: 12b: 0x08001E68, 143: 0x08001E5C, 152: 0x08001DE0, 0160: 0x08001DFC
- Called by: `mcu_cascade_observer_step`, `mcu_dq_power_estimate`
- Confidence: medium

## mcu_q30_mul_round

**Q30 fixed-point multiply with rounding: (a*b + 2^29) >> 30**

Like mcu_0160_08001dfc but adds 1 when bit 29 of the low product word is set (round half up). Callers: mcu_0160_08005240, 0800705c, 080093f8 and 08009598.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | operand a |
| `param_2` | `s32` | operand b |

**Returns** `s32`: (a*b)>>30, rounded

**Notes:** Q-format inferred from the shift only.

- Addresses by version: 12b: 0x08001E78, 143: 0x08001E6C, 152: 0x08001DF0, 0160: 0x08001E0C
- Called by: `mcu_0160_08005240`, `mcu_q30_lerp`, `mcu_0160_080093f8`, `mcu_hall_position_update`
- Confidence: medium

## mcu_ratio_110_to_q15

**Return the byte at 0x20001FD3 divided by 110 in Q15, saturated at 1.0**

Converts the byte at 0x20001FD3 to a Q15 fraction of 110, computed as mcu_q15_div_sat of the value shifted left 15 by the constant 0x370000 (which is 110 << 15). Values of 110 and above return 0x8000 (full scale). A zero byte returns 0.

**Returns** `s32`: Q15 value of byte/110, between 0 and 0x8000

**Notes:** The meaning of the scale 110 is not visible in this packet.

- Addresses by version: 12b: 0x0800C794, 143: 0x0800C9EC, 152: 0x0800CA2C, 0160: 0x0800CA8C
- Called by: `mcu_0160_0800adde`
- Calls: `mcu_q15_div_sat`
- Confidence: medium

## mcu_read_be16

**Read a big-endian 16-bit value from two bytes**

Returns (byte[0] << 8) | byte[1], the big-endian reading of the two bytes at param_1. It is used to decode multi-byte protocol fields that are sent most significant byte first. Called from mcu_0160_0800a0f8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pointer to two bytes |

**Returns** `u16`: big-endian value

- Addresses by version: 12b: 0x08006620, 143: 0x080064E8, 152: 0x08006518, 0160: 0x080065B8
- Called by: `mcu_param_record_load`
- Confidence: high

## mcu_read_le32

**Read a little-endian 32-bit value from four bytes at the pointer**

Assembles bytes 0..3 of the buffer into a 32-bit value in little-endian order, using byte loads so no alignment is required. The result is byte0 | byte1 << 8 | byte2 << 16 | byte3 << 24. It is the reader counterpart of mcu_write_le32.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | four bytes, least significant first |

**Returns** `u32`: little-endian 32-bit value

- Addresses by version: 0160: 0x0800D6A0
- Called by: `mcu_xtea_key_load`, `mcu_xtea_decrypt_block`
- Confidence: high

## mcu_rec8_reset_defaults

**Reset an 8-byte record to defaults with a 0xFFFF marker and fixed small codes**

Initialises an 8-byte record: the word at +0 becomes 0x0000FFFF, byte +4 is cleared, byte +5 is set to 4, byte +6 is cleared and byte +7 is set to 1. The 0xFFFF halfword looks like a not-set or invalid marker and the small byte values look like enumerated states, but the record's owner and the meaning of its fields are not visible in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 8-byte record |

**Notes:** The caller mcu_0160_0800c058 is in another packet, so the record's role is inferred only from the default values.

- Addresses by version: 12b: 0x0800CBA8, 143: 0x0800CE24, 152: 0x0800CE6C, 0160: 0x0800CECC
- Called by: `mcu_gpioa_pin_cfg_init`
- Confidence: medium

## mcu_req_queue_submit

**Queue a request into a 4-slot ring of 256-byte request slots when a slot is free and code is below 243**

Four-slot request queue. The object has a busy byte at +0x00 used as a re-entrancy guard (a non-zero byte at +0x02 also refuses), a write index at +0x405 and a free-slot count at +0x406. When the guard is clear, param_4 is below 0xF3 and a slot is free, it calls mcu_0160_08006460 with the forwarded arguments and a pointer to the payload of the slot at 0x100*index + 8, stores the returned word in the slot header at +4, advances the write index modulo 4 and decrements the free count. Otherwise the request is dropped and the guard is cleared.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | queue object: guard +0x00, gate +0x02, write index +0x405, free count +0x406, slots of 0x100 bytes from +0x100 |
| `param_2` | `u32` | forwarded to mcu_0160_08006460 |
| `param_3` | `u32` | forwarded to mcu_0160_08006460 |
| `param_4` | `u32` | request code, accepted when below 0xF3 |
| `param_5` | `u32` | forwarded to mcu_0160_08006460 |
| `param_6` | `u32` | forwarded to mcu_0160_08006460 |
| `param_7` | `u32` | forwarded to mcu_0160_08006460 |

**Notes:** The meaning of the 0xF3 limit and of the callee mcu_0160_08006460 are not visible in this packet.

- Addresses by version: 12b: 0x0800AC0A, 143: 0x0800AE32, 152: 0x0800ACEE, 0160: 0x0800AD62
- Called by: `mcu_0160_0800aa78`
- Calls: `mcu_frame_build_5aa5_checksum`
- Confidence: medium

## mcu_select_stack_local_fragment

**Code fragment: pick one of two caller stack slots depending on a third**

Not a true function: the decompiler shows reads of in_stack_00000030, in_stack_000000c8 and in_stack_000000d0, i.e. it uses the stack frame of its caller (mcu_0160_08002b64) without setting up its own. Logic: if the slot at sp+0xd0 is non-zero return the slot at sp+0xc8, otherwise the slot at sp+0x30. It is a compiler-split tail/outlined block of the enclosing routine. The 12b build has the equivalent mcu_12b_08002c00.

**Returns** `u32`: selected stack-slot value

**Notes:** Outlined fragment sharing its caller's frame; do not treat as a standalone API.

- Addresses by version: 143: 0x08002A80, 152: 0x08002A04, 0160: 0x08002A20
- Called by: `mcu_speed_lpf_band_update`
- Confidence: low

## mcu_set_byte_field_0x4c

**Store a byte at struct+0x4c and return 1**

Writes the u8 argument to struct+0x4c and returns 1, so callers can use it as a success-returning setter. Callers: mcu_0160_08004e78, mcu_0160_08005054.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | structure |
| `param_2` | `u8` | value to store at +0x4c |

**Returns** `u32`: always 1

- Addresses by version: 12b: 0x0800A54C, 143: 0x0800A780, 152: 0x0800A63C, 0160: 0x0800A6B0
- Called by: `mcu_0160_08004e78`, `mcu_0160_08005054`
- Confidence: high

## mcu_set_request_flags

**Set request flags at 0x20001FC9 and 0x20001FCB to 1**

Writes 1 to the two RAM bytes 0x20001FC9 and 0x20001FCB. Byte 0x20001FC8 of the same block is not touched. This looks like a pair of pending-request flags that the main loop or a timer task acts on later.

**Notes:** The reader of these flags is in mcu_0160_0800672c, which is outside this packet.

- Addresses by version: 12b: 0x08008724, 143: 0x080088B4, 152: 0x080088F4, 0160: 0x08008968
- Called by: `mcu_0160_0800672c`
- Confidence: medium

## mcu_snapshot_copy_if_changed

**Copy a 7-word record to its shadow when the byte at +0x18 differs or a force flag is set**

Compares the byte at offset 0x18 of the source record (param_1) with the same byte in the destination (param_2). If they differ, or the RAM force flag at 0x2000066D is non-zero, the seven 32-bit words at offsets 0x00..0x18 are copied from source to destination and the force flag is cleared. Otherwise nothing is written. It is a copy-on-change snapshot, so the destination mirrors the source after any change. The byte at +0x18 acts as the change indicator for the record.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source record, 7 words |
| `param_2` | `ptr` | destination shadow record, 7 words |

**Notes:** Owning subsystem not visible in this packet; only caller is mcu_0160_08004e78.

- Addresses by version: 12b: 0x080057E0, 143: 0x080056E4, 152: 0x08005748, 0160: 0x080057E8
- Called by: `mcu_0160_08004e78`
- Confidence: medium

## mcu_sort_u16_exchange

**In-place exchange sort of a u16 array, descending when flag is 0, ascending otherwise**

Simple O(n^2) exchange sort of n halfword values in place. When the flag is 0 it swaps any pair where the earlier element is smaller, leaving the array in descending order; when the flag is nonzero it swaps where the later element is smaller, giving ascending order. Each swap goes through mcu_swap_u16. Used on five-sample windows for the temporal median in mcu_adc_dma_median5.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | u16 array base |
| `param_2` | `u32` | element count n |
| `param_3` | `s32` | order flag: 0 descending, nonzero ascending |

- Addresses by version: 12b: 0x080028E4, 143: 0x08002920, 152: 0x080028A4, 0160: 0x080028C0
- Called by: `mcu_adc_dma_median5`
- Calls: `mcu_swap_u16`
- Confidence: high

## mcu_store_inverted_mask_0x10

**Store the bitwise complement of a word at struct+0x10**

Writes ~value to the u32 at struct+0x10. Storing the complement means a bit set in the argument reads back as 0 from that word. mcu_test_mask_0x10 (mcu_0160_0800a81e) tests the same word, so the two form a pair. Called from mcu_0160_08009160.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | structure |
| `param_2` | `u32` | mask to store, complemented before the write |

**Notes:** The purpose of the stored mask is not visible in this packet.

- Addresses by version: 12b: 0x0800A68C, 143: 0x0800A8C0, 152: 0x0800A77C, 0160: 0x0800A7F0
- Called by: `mcu_0160_08009160`
- Confidence: high

## mcu_store_inverted_word

**Store the bitwise complement of the argument into a word**

Writes ~value to *p. This is the same operation as mcu_store_inverted_mask_0x10, but with the destination passed directly rather than at a fixed offset. It keeps a mask in complemented form. Called from mcu_0160_08001ee4 and mcu_0160_0800226c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination word |
| `param_2` | `u32` | value to store, complemented before the write |

- Addresses by version: 12b: 0x0800B410, 143: 0x0800B6C0, 152: 0x0800B6C4, 0160: 0x0800B724
- Called by: `mcu_0160_08001ee4`, `mcu_0160_0800226c`
- Confidence: high

## mcu_swap_u16

**Swap two 16-bit values through pointers**

Exchanges the halfwords at both pointers using a temporary variable. It is a generic in-place reordering helper for 16-bit entries, for example when sorting or rotating a table. The callers are not in this packet, so the purpose is inferred from the operation only.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | first u16 operand, read and overwritten |
| `param_2` | `ptr` | second u16 operand, read and overwritten |

- Addresses by version: 12b: 0x0800C7CC, 143: 0x0800CA24, 152: 0x0800CA64, 0160: 0x0800CAC4
- Called by: `mcu_sort_u16_exchange`
- Confidence: high

## mcu_take_pending_200003ba

**Move the byte at 0x200003BA to 0x200003BB and clear 0x200003BA**

Copies the byte at 0x200003BA into 0x200003BB and then zeroes 0x200003BA. This is a snapshot-and-clear: a counter or event flag accumulates in 0x200003BA elsewhere, and the consumer reads the last period's value from 0x200003BB. The variable 0x200003B8 is also address-taken in the wider program but is not touched here. Called from mcu_0160_080085bc.

- Addresses by version: 143: 0x08006494, 152: 0x080064C4, 0160: 0x08006564
- Called by: `mcu_can_rx_command_dispatch`
- Confidence: medium

## mcu_test_mask_0x10

**Return true if any bit of the mask is set in the word at struct+0x10**

Returns ((u32 *)(struct + 0x10) & mask) != 0. It reads the word that mcu_store_inverted_mask_0x10 writes in complemented form, so a true result means a masked bit is 1 in the stored word, which is 0 in the mask as originally given. Called from mcu_0160_08009160.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | structure |
| `param_2` | `u32` | bit mask to test |

**Returns** `bool`: true if any masked bit is set in the stored word

- Addresses by version: 12b: 0x0800A6BA, 143: 0x0800A8EE, 152: 0x0800A7AA, 0160: 0x0800A81E
- Called by: `mcu_0160_08009160`
- Confidence: high

## mcu_track_min_nonzero_u8

**Store a value in RAM byte 0x200003bc if it is smaller than the stored value or the stored value is 0**

Writes the low byte of the argument into the RAM byte at 0x200003bc when the argument is below the current value or the current value is 0. Zero therefore acts as 'no sample yet', but it is also a valid stored value: once a 0 has been stored, the next call always overwrites it. Only 8 bits are stored, so a value above 255 is compared at full width but stored truncated. Callers: mcu_0160_080061fc, mcu_0160_0800b324, mcu_0160_0800d548, mcu_12b_0800b0a4.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | candidate value (only the low 8 bits are stored) |

**Notes:** Meaning of the RAM byte 0x200003bc is not visible in this packet.

- Addresses by version: 12b: 0x08009FD4, 143: 0x0800A184, 152: 0x0800A1D0, 0160: 0x0800A244
- Called by: `mcu_fault_owner_arbitrate`, `mcu_0160_0800b324`, `mcu_0160_0800d548`
- Confidence: high

## mcu_u16_table_bsearch_desc

**Binary search of a descending u16 table that leaves the bracket index in a register**

Bisects a table of n u16 entries (n = param_1 masked to 16 bits) for the position of threshold x = param_3. The bracket starts at low = 0 and high = n - 1, and the loop runs while high - low > 1. At each midpoint it moves low to mid when x <= table[mid], otherwise high to mid. The table is therefore expected to be in descending order, and at the end table[low] >= x > table[high]. The function has no return statement: the decompiler shows void and the final bracket index is left in a register for the caller. Callers: mcu_0160_0800209c, mcu_0160_08002148.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | number of table entries |
| `param_2` | `ptr` | u16 threshold table |
| `param_3` | `u32` | value searched for (compared with the u16 entries) |

**Notes:** Which register holds the result, and what the table represents, could not be determined from this packet.

- Addresses by version: 12b: 0x0800A774, 143: 0x0800A9A8, 152: 0x0800A864, 0160: 0x0800A8D8
- Called by: `mcu_speed_from_period_min`, `mcu_speed_from_max_u12`
- Confidence: medium

## mcu_write_le32

**Store a 32-bit value as four little-endian bytes**

Writes the 32-bit value into four consecutive bytes at the destination, least significant byte first, using byte stores so no alignment is required. It is the writer counterpart of mcu_read_le32.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value to store |
| `param_2` | `ptr` | destination, at least four bytes |

- Addresses by version: 0160: 0x0800D924
- Called by: `mcu_xtea_decrypt_block`
- Confidence: high

## mcu_xfer_queue_init

**Arm five 300-byte transfer requests and publish the table when the control pointers are set**

Arms five transfer request objects of 0x24 bytes starting at 0x2000212C, each with a 300-byte buffer starting at 0x200021E0, through mcu_xfer_request_arm with a repeat count of 1 and user argument 0. If the pointers at 0x200006F0 and 0x200006FC are both non-zero it stores the table in the globals 0x200027BC (base), 0x200027C0 (count 5) and 0x200027C4 (address of the 0x200006F0 control block) and returns 1; otherwise it returns 0 and publishes nothing.

**Returns** `bool`: 1 when the table was published, 0 otherwise

**Notes:** The owner of the control block at 0x200006F0 is not visible in this packet.

- Addresses by version: 12b: 0x0800C9FC, 143: 0x0800CC78, 152: 0x0800CCB8, 0160: 0x0800CD18
- Called by: `mcu_0160_0800d548`
- Calls: `mcu_xfer_request_arm`
- Confidence: medium

## mcu_xfer_request_arm

**Arm a transfer request with buffer, length, repeat count and user argument**

Returns 0 unless the request object, the count and the buffer are all non-zero. On success it stores the buffer pointer at +4, the length halfword at +8 and the count halfword at +0x14, sets the state byte at +2 to 1 (armed or pending) and stores the user argument at +0x20. Nothing is transmitted or copied here, so this only prepares the request for a later service routine. The caller mcu_0160_0800cd18 is in another packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | request object |
| `param_2` | `s16` | count stored at +0x14, must be non-zero |
| `param_3` | `ptr` | buffer, must be non-null |
| `param_4` | `u16` | length stored at +8 |
| `param_5` | `u32` | user argument stored at +0x20 |

**Returns** `bool`: 1 when armed, 0 when an argument is zero or null

**Notes:** The request object's role is not visible here, so the field names are the code's offsets only.

- Addresses by version: 12b: 0x0800CDC4, 143: 0x0800D040, 152: 0x0800D088, 0160: 0x0800D0E8
- Called by: `mcu_xfer_queue_init`
- Confidence: medium
