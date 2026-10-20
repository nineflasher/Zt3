# BMS - `app` functions

40 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_app_event_1c_take`](#bms_app_event_1c_take) | 0x080086F8 | Test and clear the one-shot event byte at 0x20000001C |
| [`bms_app_flag_1d_get`](#bms_app_flag_1d_get) | 0x080086EC | Return the byte status flag at 0x20000001D |
| [`bms_app_flag_b57_get`](#bms_app_flag_b57_get) | 0x08007D94 | Return 1 when the byte flag at 0x20000B57 is nonzero |
| [`bms_app_state_reset`](#bms_app_state_reset) | 0x08007EA0 | Clear 24 app state bytes and set defaults (0x200001AA = 2, 0x20000904 = 0x5A) |
| [`bms_app_state_reset_legacy`](#bms_app_state_reset_legacy) | (removed) | Clear the application state block (4130/4139 RAM layout) and set its defaults |
| [`bms_app_value_28_get`](#bms_app_value_28_get) | 0x08008710 | Return the 16-bit value stored at 0x20000028 |
| [`bms_app_value_684_set`](#bms_app_value_684_set) | 0x08008BE0 | Store a 32-bit value at RAM word 0x20000684 |
| [`bms_block_store_u16x7`](#bms_block_store_u16x7) | 0x0800D740 | Copy seven 16-bit words from a source array into RAM at 0x20002BF0 |
| [`bms_byte_200004f4_addr`](#bms_byte_200004f4_addr) | 0x0800C378 | Return the address of the RAM byte at 0x200004F4 |
| [`bms_byte_20000628_addr`](#bms_byte_20000628_addr) | 0x0800BAE4 | Return the address of the RAM byte at 0x20000628 |
| [`bms_byte_2000063e_addr`](#bms_byte_2000063e_addr) | 0x0800B8A4 | Return the address of the RAM byte at 0x2000063E |
| [`bms_chan_bind`](#bms_chan_bind) | 0x0800FECC | Validate a descriptor and bind a channel object to a buffer, a length and that descriptor |
| [`bms_chan_configure`](#bms_chan_configure) | 0x0800FFC6 | Set the extended fields of a channel object and mark it enabled after three nonzero checks |
| [`bms_chan_pool_init`](#bms_chan_pool_init) | 0x0800F288 | Configure five 300-byte channel objects and bind them to the object at 0x200024C0 |
| [`bms_ctrl_request_handshake`](#bms_ctrl_request_handshake) | 0x0800E7B0 | Latch a control request while state bit 0x194.6 is high and consume it on the falling edge |
| [`bms_dispatch_call_current`](#bms_dispatch_call_current) | 0x0800A88C | Call the handler at entry [0x20001340] of the RAM pointer table at 0x20000578 |
| [`bms_dispatch_index_nonzero`](#bms_dispatch_index_nonzero) | 0x0800A87C | Return true when the dispatch index byte at 0x20001340 is nonzero |
| [`bms_extflash_journal_init`](#bms_extflash_journal_init) | 0x0800A7C8 | Reset ten 20-byte slot records, then validate two 12-byte external flash headers |
| [`bms_flag_20001c8a_is_clear`](#bms_flag_20001c8a_is_clear) | 0x0800FB80 | Return 1 when the RAM byte at 0x20001C8A is zero, else 0 |
| [`bms_nop_ce4c`](#bms_nop_ce4c) | 0x0800CE4C | Empty placeholder routine that does nothing |
| [`bms_nop_e8d8`](#bms_nop_e8d8) | 0x0800E8D8 | Empty placeholder routine that does nothing |
| [`bms_ram_200001c8_addr`](#bms_ram_200001c8_addr) | 0x0800BE1C | Return the address of the RAM object at 0x200001C8 |
| [`bms_ram_2000068f_addr`](#bms_ram_2000068f_addr) | 0x08009D6C | Return the address of the RAM byte at 0x2000068F |
| [`bms_ram_20000bdc_addr`](#bms_ram_20000bdc_addr) | 0x0800BE14 | Return the address of the RAM object at 0x20000BDC |
| [`bms_record_queue_flush`](#bms_record_queue_flush) | 0x0800B904 | Empty the 256-entry record queue and set the handler word at 0x20000684 |
| [`bms_record_queue_pop`](#bms_record_queue_pop) | 0x0800B91C | Pop the oldest 24-byte record from the 256-slot queue at 0x20002C18; 0 if empty |
| [`bms_record_set_or_clear`](#bms_record_set_or_clear) | 0x0800E38C | Clear the six-word record at 0x200024CC when param_4 is 0xFFFF, else store its fields |
| [`bms_snapshot_logger_thunk`](#bms_snapshot_logger_thunk) | 0x0800871C | Thunk that runs the snapshot logger tick |
| [`bms_snapshot_logger_tick`](#bms_snapshot_logger_tick) | 0x0800A8A0 | Snapshot logger: every 5000 units capture and queue a record; commit history every 1000 |
| [`bms_state_restore_or_init`](#bms_state_restore_or_init) | 0x08008060 | Restore the state block from flash, or rebuild defaults and identity if the marker is missing |
| [`bms_telemetry_sched_thunk`](#bms_telemetry_sched_thunk) | 0x08007F10 | Thunk that runs the telemetry 16-step scheduler |
| [`bms_u16_2000067c_get`](#bms_u16_2000067c_get) | 0x0800A55C | Return the u16 at RAM 0x2000067C |
| [`bms_u16_2000067c_set`](#bms_u16_2000067c_set) | 0x0800A568 | Store a u16 into RAM 0x2000067C |
| [`bms_u16_2000067e_get`](#bms_u16_2000067e_get) | 0x0800A510 | Return the u16 at RAM 0x2000067E |
| [`bms_u16_2000067e_set`](#bms_u16_2000067e_set) | 0x0800A51C | Store a u16 into RAM 0x2000067E |
| [`bms_u16_20000dfc_addr`](#bms_u16_20000dfc_addr) | 0x0800C6D4 | Return the address of the u16 at RAM 0x20000DFC |
| [`bms_u16x5_block_store`](#bms_u16x5_block_store) | 0x0800BFFC | Copy five u16 values into the 10-byte RAM block at 0x2000051C |
| [`bms_u32_200004dc_addr`](#bms_u32_200004dc_addr) | 0x0800C370 | Return the address of the RAM word at 0x200004DC |
| [`bms_u32_20000dec_addr`](#bms_u32_20000dec_addr) | 0x0800C804 | Return the address of the RAM word at 0x20000DEC |
| [`bms_u32_20001348_get`](#bms_u32_20001348_get) | 0x0800BE24 | Return the u32 at RAM 0x20001348 |

## bms_app_event_1c_take

**Test and clear the one-shot event byte at 0x20000001C**

If the byte at 0x2000001C is nonzero it is cleared and the function returns 1; otherwise it returns 0. This is a fetch-and-clear, so the byte works as a one-shot request flag: whatever sets it (not in this packet) raises the event, and the poll in bms_4168_08010558 consumes it here. The meaning of the event is not established.

**Returns** `bool`: true when the event was pending; the flag is cleared by this call

- Addresses by version: 4130: 0x080076AC, 4139: 0x08007BAC, 4148: 0x080083F8, 4168: 0x080086F8
- Called by: `bms_4168_08010558`
- Confidence: medium

## bms_app_flag_1d_get

**Return the byte status flag at 0x20000001D**

Returns the byte at 0x2000001D without modifying it. It is read by the main-loop poll bms_4168_08010558 together with bms_app_event_1c_take and bms_app_value_28_get, and the three neighbouring RAM words at 0x1C, 0x1D and 0x28 look like one status block. The flag's meaning is not established.

**Returns** `u8`: current flag value

- Addresses by version: 4130: 0x080076A0, 4139: 0x08007BA0, 4148: 0x080083EC, 4168: 0x080086EC
- Called by: `bms_4168_08010558`
- Confidence: medium

## bms_app_flag_b57_get

**Return 1 when the byte flag at 0x20000B57 is nonzero**

Returns true when the byte at 0x20000B57 is nonzero and false otherwise, with no side effects. bms_app_state_reset clears this byte, so it belongs to the application state block. The code that sets it is outside this packet. Callers bms_4168_08004774, bms_4168_0800c96c and bms_4168_0800fb94 use it as a yes or no gate; the flag's meaning is not established.

**Returns** `bool`: true when the flag is set

- Addresses by version: 4148: 0x08007A8C, 4168: 0x08007D94
- Called by: `bms_limit_status_update`, `bms_4168_0800c96c`, `bms_4168_0800fb94`
- Confidence: high

## bms_app_state_reset

**Clear 24 app state bytes and set defaults (0x200001AA = 2, 0x20000904 = 0x5A)**

Zeroes 24 byte-sized RAM variables, 22 of them in the 0x20000A49..0x20000B57 range (including the flag at 0x20000B57 that bms_app_flag_b57_get reads) and two at 0x200001AB and 0x200001AC. It then writes 2 to 0x200001AA and 0x5A (90) to 0x20000904, which are the default values written at reset. The pattern is the same as the legacy layout in bms_app_state_reset_legacy, so this is probably the power-on or fault-recovery reset of the application state block, with 2 as an initial state-machine value. The individual meanings are not confirmed. Callers bms_4168_08007da4 and bms_4168_08010558.

**Notes:** The 2 and 0x5A defaults and the list of cleared variables are certain from the code. Their roles are inferred from the reset pattern and the other families. Shared by the 4148 and 4168 builds.

- Addresses by version: 4148: 0x08007B98, 4168: 0x08007EA0
- Called by: `bms_comm_pool_state_step`, `bms_4168_08010558`
- Confidence: medium

## bms_app_state_reset_legacy

**Clear the application state block (4130/4139 RAM layout) and set its defaults**

Zeroes 22 byte-sized RAM variables, 20 of them in the 0x2000095D..0x20000A69 range and two at 0x20000113 and 0x20000114, then sets 0x20000112 to 2 and 0x20000818 to 0x5a (90). It is the 4130/4139 RAM-layout counterpart of bms_app_state_reset in the 4148/4168 builds: the same pattern and the same default values, at different addresses. The meaning of the individual variables is not established. Caller bms_4139_080072e0.

**Notes:** Probably the same logical function as bms_app_state_reset. Address correspondence inferred from matching writes: 0x20000112 to 0x200001aa, 0x20000113 to 0x200001ab, 0x20000114 to 0x200001ac, 0x20000818 to 0x20000904. The legacy build has no equivalents of 0x20000a53 and 0x20000b57, which the newer layout clears. Kept as a separate family because the address layouts differ.

- Addresses by version: 4130: 0x08006E60, 4139: 0x08007360
- Called by: `bms_4139_dual_bank_step`
- Confidence: medium

## bms_app_value_28_get

**Return the 16-bit value stored at 0x20000028**

Returns the halfword at 0x20000028 without modifying it. It is read in the main-loop poll bms_4168_08010558 alongside the flags at 0x2000001C and 0x2000001D. The stored quantity is not established in this packet.

**Returns** `u16`: current stored value

- Addresses by version: 4130: 0x080076C4, 4139: 0x08007BC4, 4148: 0x08008410, 4168: 0x08008710
- Called by: `bms_4168_08010558`
- Confidence: medium

## bms_app_value_684_set

**Store a 32-bit value at RAM word 0x20000684**

Writes param_1 to the 32-bit RAM word at 0x20000684 and returns nothing. The only caller in the packet is bms_4168_0800b904. What the value means is not established.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value to store |

- Addresses by version: 4130: 0x08007B94, 4139: 0x08008094, 4148: 0x080088E0, 4168: 0x08008BE0
- Called by: `bms_record_queue_flush`
- Confidence: medium

## bms_block_store_u16x7

**Copy seven 16-bit words from a source array into RAM at 0x20002BF0**

Copies param_1[0] through param_1[6] (16-bit each) into the halfwords at 0x20002BF0, 0x20002BF2, 0x20002BF4, 0x20002BF6, 0x20002BF8, 0x20002BFA and 0x20002BFC, so source index i goes to 0x20002BF0 + 2*i. The decompiled assignments are listed out of order, but each source index maps to its own slot. There is no validation and no return value; the only caller in the packet is bms_4168_08004774.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source array of seven u16 values, indexed 0 to 6 |

**Notes:** The destination words are not named in this packet; their use is in the callers. The function does not check the source pointer.

- Addresses by version: 4148: 0x0800D358, 4168: 0x0800D740
- Called by: `bms_limit_status_update`
- Confidence: high

## bms_byte_200004f4_addr

**Return the address of the RAM byte at 0x200004F4**

Returns &DAT_200004f4 as a byte pointer. The object is not identified in this packet. Its only caller, bms_4168_08003cc0, also calls the 0x200004DC and 0x2000051C helpers, so these look like parts of one configuration block set up together (inferred from the shared caller).

**Returns** `ptr`: address of the RAM byte at 0x200004F4

- Addresses by version: 4130: 0x0800B328, 4139: 0x0800B880, 4148: 0x0800C064, 4168: 0x0800C378
- Called by: `bms_profile_select_from_code`
- Confidence: medium

## bms_byte_20000628_addr

**Return the address of the RAM byte at 0x20000628**

Returns &DAT_20000628 so the caller can read or write the byte through the pointer. The byte's role is not established in this packet. Callers: bms_4168_08005710 and bms_4168_08005768.

**Returns** `ptr`: address of the RAM byte at 0x20000628

- Addresses by version: 4130: 0x0800AB7C, 4139: 0x0800B0B4, 4148: 0x0800B7D0, 4168: 0x0800BAE4
- Called by: `bms_timeout_arm_from_record`, `bms_extlog_request_dispatch`
- Confidence: medium

## bms_byte_2000063e_addr

**Return the address of the RAM byte at 0x2000063E**

Returns &DAT_2000063e so the caller can read or write the byte through the pointer. The byte's role is not established in this packet. Caller: bms_4168_08003cc0.

**Returns** `ptr`: address of the RAM byte at 0x2000063E

- Addresses by version: 4130: 0x0800A93C, 4139: 0x0800AE74, 4148: 0x0800B590, 4168: 0x0800B8A4
- Called by: `bms_profile_select_from_code`
- Confidence: medium

## bms_chan_bind

**Validate a descriptor and bind a channel object to a buffer, a length and that descriptor**

Binds a channel object only when every argument passes its check: param_1 (the object) is non-null, param_2 and param_3 are nonzero, and param_4 (the descriptor) is non-null with nonzero words at offsets 0 and 12. On success it stores param_2 as a 32-bit word at object offset 0, param_3 as a 16-bit value at offset 4 and the descriptor pointer at offset 8, then returns 1. On any failed check it returns 0 and writes nothing, so the caller can detect a rejected binding. bms_chan_bind and bms_chan_configure are both called from bms_4168_0800f288 and fill channel objects, so they form a pair of setup routines.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | channel object to fill: offset 0 u32, offset 4 u16, offset 8 pointer |
| `param_2` | `u32` | value stored at offset 0; must be nonzero |
| `param_3` | `u32` | length stored as 16 bits at offset 4; must be nonzero |
| `param_4` | `ptr` | descriptor; non-null, with nonzero words at offsets 0 and 12 |

**Returns** `u32`: 1 when the object is bound, 0 when a check fails

**Notes:** The field meanings of the object are inferred from the stores and checks. The descriptor's contents are only tested here, not used.

- Addresses by version: 4130: 0x0800E0D4, 4139: 0x0800E728, 4148: 0x0800F980, 4168: 0x0800FECC
- Called by: `bms_chan_pool_init`
- Confidence: medium

## bms_chan_configure

**Set the extended fields of a channel object and mark it enabled after three nonzero checks**

Checks that param_1 is non-null and that param_2 and param_3 are nonzero, then fills the channel object: param_3 as a 32-bit word at offset 4, param_4 as a 16-bit value at offset 8, the low 16 bits of param_2 at offset 0x14, a byte flag at offset 2 set to 1 (enabled), and param_5 as a 32-bit word at offset 0x20. It returns 1, or 0 with nothing written when a check fails. Unlike bms_chan_bind it does not look at a descriptor. It is called from bms_4168_0800f288 together with bms_chan_bind.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | channel object to fill |
| `param_2` | `u32` | must be nonzero; low 16 bits stored at offset 0x14 |
| `param_3` | `u32` | must be nonzero; stored at offset 4 as 32 bits |
| `param_4` | `u16` | stored at offset 8 as 16 bits |
| `param_5` | `u32` | stored at offset 0x20 |

**Returns** `u32`: 1 when the object is configured, 0 when a check fails

**Notes:** bms_chan_bind writes offset 4 as 16 bits and offset 8 as a pointer, while this function writes offset 4 as 32 bits and offset 8 as 16 bits. The two may describe different object types, or one of the layouts is wrong; check against the caller bms_4168_0800f288. The meaning of the flag at offset 2 is inferred from the constant 1.

- Addresses by version: 4130: 0x0800E1CE, 4139: 0x0800E822, 4148: 0x0800FA7A, 4168: 0x0800FFC6
- Called by: `bms_chan_pool_init`
- Confidence: medium

## bms_chan_pool_init

**Configure five 300-byte channel objects and bind them to the object at 0x200024C0**

Initialises the channel pool. For each of the five 36-byte channel objects at 0x20001E30 (stride 0x24) it calls bms_chan_configure with the 300-byte buffer at 0x20001EE4 + 300 * i and length 300, then calls bms_chan_bind to bind the object at 0x200024C0 to the array of five channels with descriptor 0x200005F0. It finally stores the time base from bms_tick_get in DAT_200005DC.

**Notes:** The return values of bms_chan_configure and bms_chan_bind are not checked here.

- Addresses by version: 4130: 0x0800D76C, 4139: 0x0800DD54, 4148: 0x0800EDF8, 4168: 0x0800F288
- Called by: `bms_seq_restart_stamp`
- Calls: `bms_tick_get`, `bms_chan_bind`, `bms_chan_configure`
- Confidence: high

## bms_ctrl_request_handshake

**Latch a control request while state bit 0x194.6 is high and consume it on the falling edge**

Tracks a request handshake on bit 6 of the 16-bit word at state block +0x194. While that bit is high DAT_200005C3 is armed to 1. On the next call with the bit low, if DAT_200005C3 is armed, bit 1 (0x02) is set in DAT_200005C1 and bit 3 (0x08) in DAT_200005C0 when bit 7 (0x80) of DAT_200005CA is set, and when bit 8 (0x100) of DAT_200005CA is set that bit is cleared, bit 3 of DAT_200005C0 is set, and the shadow words DAT_200005C8 and DAT_200005CA are written back to the state block at +0x10E and +0x110. DAT_200005C3 is then cleared. Bit 3 of DAT_200005C0 forces bms_setpoint_window_sample to evaluate on its next call. Part of the control group with bms_setpoint_window_sample.

**Notes:** The names of the request bits are not established; the handshake shape is taken from the code paths only.

- Addresses by version: 4130: 0x0800CD34, 4139: 0x0800D31C, 4148: 0x0800E31C, 4168: 0x0800E7B0
- Called by: `bms_setpoint_window_sample`
- Calls: `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_dispatch_call_current

**Call the handler at entry [0x20001340] of the RAM pointer table at 0x20000578**

Reads the byte at 0x20001340 as an index, multiplies it by 4, and calls the 32-bit function pointer at 0x20000578 plus that offset. The table is in RAM, so the handlers are installed at runtime. There is no bounds check on the index and no return value, so an out-of-range index makes an unbounded indirect call. The decompiler marks the call as an indirect jump treated as a call. Caller: bms_4168_08008778.

**Notes:** Whoever sets the index byte at 0x20001340 and fills the table at 0x20000578 is not in this packet.

- Addresses by version: 4130: 0x08009924, 4139: 0x08009E5C, 4148: 0x0800A578, 4168: 0x0800A88C
- Called by: `bms_dispatch_current_thunk`
- Confidence: high

## bms_dispatch_index_nonzero

**Return true when the dispatch index byte at 0x20001340 is nonzero**

Returns DAT_20001340 != 0 and has no side effects. 0x20001340 is the index that bms_dispatch_call_current uses to choose a handler, so this tells the caller whether the dispatcher is on a non-zero entry. Caller: bms_4168_08008778.

**Returns** `bool`: true when the dispatch index is nonzero

- Addresses by version: 4130: 0x08009914, 4139: 0x08009E4C, 4148: 0x0800A568, 4168: 0x0800A87C
- Called by: `bms_4168_080082f0`
- Confidence: medium

## bms_extflash_journal_init

**Reset ten 20-byte slot records, then validate two 12-byte external flash headers**

Initialises the software state for external-flash journalling. It loops over ten 20-byte slot records starting at RAM 0x200013A0. In each record byte +0 is set to 1, byte +1 is cleared, and the words at +4, +8, +0xC and +0x10 are cleared. It then clears 0x20001340 to 0x20001345 and the word at 0x2000133C. It reads a 12-byte header from external SPI memory at address 0x000000 into 0x20001348 with bms_extflash_read (u32 counter, then two u32 pointers at 0x2000134C and 0x20001350). If the counter exceeds 3000, or either pointer lies outside 0x010000 to 0x267FFF, the RAM copy is reset to counter 0 and both pointers to 0x10000. A second header read from address 0x001000 into 0x20001354 is checked the same way, with a counter limit of 0x4400, pointer range 0x280000 to 0x38FFFF and default 0x280000. Only the RAM copies are reset, not the flash contents.

**Notes:** The meaning of the slot flags and the journal layout are inferred from the field sizes and range checks. Caller chain includes bms_4168_08008724.

- Addresses by version: 4130: 0x08009860, 4139: 0x08009D98, 4148: 0x0800A4B4, 4168: 0x0800A7C8
- Called by: `bms_extflash_probe_and_init`
- Calls: `bms_extflash_read`
- Confidence: medium

## bms_flag_20001c8a_is_clear

**Return 1 when the RAM byte at 0x20001C8A is zero, else 0**

Reads the byte at 0x20001C8A and returns 0 if it is nonzero and 1 if it is zero, so the result is true when the flag is clear. The function is read-only. Its only caller in the packet is bms_4168_080082f0, which also calls bms_nop_e8d8.

**Returns** `u32`: 1 if the flag byte is zero, otherwise 0

**Notes:** The meaning of the flag is not shown here. The name describes only the test.

- Addresses by version: 4130: 0x0800DE90, 4139: 0x0800E4E4, 4148: 0x0800F6A0, 4168: 0x0800FB80
- Called by: `bms_4168_080082f0`
- Confidence: high

## bms_nop_ce4c

**Empty placeholder routine that does nothing**

The body is a bare return with no writes to registers or globals. Its callers are in BMS_4139 and BMS_4168 (bms_4139_08006f08 and bms_4168_08007a0c), so it is most likely the no-op default of an optional hook or callback that these builds do not implement.

**Notes:** The hook it stands in for cannot be identified from this packet. Only the empty body is certain.

- Addresses by version: 4130: 0x0800BAF0, 4139: 0x0800C0C0, 4148: 0x0800CA64, 4168: 0x0800CE4C
- Called by: `bms_4168_08007a0c`
- Confidence: high

## bms_nop_e8d8

**Empty placeholder routine that does nothing**

The body is a bare return; it writes nothing and returns no value. Its only caller in the packet is bms_4168_080082f0, which also calls bms_flag_20001c8a_is_clear, so it is probably a no-op hook or callback slot.

**Notes:** The hook it stands in for cannot be identified from this packet. It has the same shape as bms_nop_ce4c, and the two may be different hook slots.

- Addresses by version: 4130: 0x0800CE5C, 4139: 0x0800D444, 4148: 0x0800E444, 4168: 0x0800E8D8
- Called by: `bms_4168_080082f0`
- Confidence: high

## bms_ram_200001c8_addr

**Return the address of the RAM object at 0x200001C8**

Returns &DAT_200001c8 for pointer access. The object's width is unknown. It is called from many sites, including bms_4130_08005d2c and bms_4139_08007238, which probably makes it a shared state block; this is not established in the packet.

**Returns** `ptr`: address of the RAM object at 0x200001C8

**Notes:** The packet's caller list is truncated.

- Addresses by version: 4130: 0x0800AEB4, 4139: 0x0800B3EC, 4148: 0x0800BB08, 4168: 0x0800BE1C
- Called by: `EXTI0_1_IRQHandler`, `EXTI2_3_IRQHandler`, `EXTI4_15_IRQHandler`, `bms_4168_08003290`, `RCC_CRS_IRQHandler`, `bms_soc_main_step`, `bms_charge_integrate_step`, `bms_state_restore_or_init`, `bms_protect_dwell_flags_update`, `bms_meas_interp_filter_dispatch`, `bms_4168_0800c80c`, `bms_4168_0800c96c` ...
- Confidence: medium

## bms_ram_2000068f_addr

**Return the address of the RAM byte at 0x2000068F**

Returns &DAT_2000068f so the caller can read or write the byte through the pointer. The byte is next to 0x20000690, the LSE-active flag written by bms_rtc_clock_bringup, and next to 0x2000068C..0x2000068E, the three flags read by bms_fault_class_get. Nothing in this packet shows what 0x2000068F holds. Callers: bms_4168_080064a0 and bms_4168_0800fabc.

**Returns** `ptr`: address of the RAM byte at 0x2000068F

**Notes:** Width and role unknown; the decompiler shows an untyped pointer.

- Addresses by version: 4130: 0x08008D0C, 4139: 0x0800920C, 4148: 0x08009A58, 4168: 0x08009D6C
- Called by: `bms_nibble_debounce_1s`, `bms_fault_record_service`
- Confidence: medium

## bms_ram_20000bdc_addr

**Return the address of the RAM object at 0x20000BDC**

Returns &DAT_20000bdc. The object's width and role are not shown, since the decompiler gives no type for it. It has many callers across the 4130, 4139 and 4168 builds, which suggests a block shared between the firmware images (inferred from the caller count).

**Returns** `ptr`: address of the RAM object at 0x20000BDC

**Notes:** Callers include bms_4130_08004410, bms_4130_08005d2c, bms_4130_08006830 and bms_4139_08004618, among others; the packet's list is truncated.

- Addresses by version: 4130: 0x0800AEAC, 4139: 0x0800B3E4, 4148: 0x0800BB00, 4168: 0x0800BE14
- Called by: `bms_limit_status_update`, `bms_remaining_time_4168`, `bms_comm_await_reply_cmd03`, `bms_status_bit4_from_reply`, `bms_limit_report_cmd08`, `bms_timeout_arm_from_record`, `bms_extlog_request_dispatch`, `bms_status_event_snapshot`, `bms_history_ring_commit`, `bms_status_latch_step`, `bms_state_refresh_scaled`, `bms_soc_main_step` ...
- Confidence: medium

## bms_record_queue_flush

**Empty the 256-entry record queue and set the handler word at 0x20000684**

Discards every queued record. It copies the write index at 0x20004418 into the read index at 0x2000441A, so the queue reads as empty, and then stores the code address of LAB_08005A6C into RAM word 0x20000684 through bms_app_value_684_set. That word is presumably a handler pointer called by the queue consumer, but the consumer is not in this packet.

**Notes:** Caller is bms_4168_08007f18. The use of the pointer at 0x20000684 is inferred.

- Addresses by version: 4130: 0x0800A99C, 4139: 0x0800AED4, 4148: 0x0800B5F0, 4168: 0x0800B904
- Called by: `bms_seq_restart_stamp`
- Calls: `bms_app_value_684_set`
- Confidence: medium

## bms_record_queue_pop

**Pop the oldest 24-byte record from the 256-slot queue at 0x20002C18; 0 if empty**

Dequeues one record. The queue has 256 slots of 24 bytes at 0x20002C18, which end at the write index 0x20004418, and the read index at 0x2000441A wraps after 255. If the indexes are equal it returns 0. Otherwise it reads the six u32 fields of the slot, clears them, advances the read index, and writes the output record at param_1: field 3 at +0, a bool from field 1 at +4, a bool from field 2 at +5, the length byte from field 0 at +6, and up to 8 payload bytes copied from fields 4 and 5 to +7 with memcpy. The output layout (ID at +0, flags at +4 and +5, DLC at +6, data at +7) matches what bms_rx_frame_7f0_7f1 reads, so the queue holds received frames.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output frame record, at least 15 bytes |

**Returns** `bool`: 1 when a record was dequeued, 0 when the queue was empty

**Notes:** The length byte is not clamped to 8 before memcpy, so a corrupted slot can copy more than the payload field holds. The producer is not in this packet.

- Addresses by version: 4130: 0x0800A9B4, 4139: 0x0800AEEC, 4148: 0x0800B608, 4168: 0x0800B91C
- Called by: `bms_event_capture_on_match`
- Calls: `memcpy`
- Confidence: medium

## bms_record_set_or_clear

**Clear the six-word record at 0x200024CC when param_4 is 0xFFFF, else store its fields**

When param_4 is 0xFFFF, all six 32-bit words from 0x200024CC to 0x200024E0 are zeroed, which clears the record. Otherwise param_3 is stored at 0x200024D4, param_2 at 0x200024E0 and param_1 at 0x200024DC, and the low 16 bits of param_4 go into the low halfword of 0x200024D0 while its high halfword is kept. The words at 0x200024CC and 0x200024D8 are not written on the store path. There is no return value and no other side effect; the callers are bms_4168_08007fc0 and bms_4168_0800f8e0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value stored at 0x200024DC |
| `param_2` | `u32` | value stored at 0x200024E0 |
| `param_3` | `u32` | value stored at 0x200024D4 |
| `param_4` | `u32` | 0xFFFF clears the record; otherwise the low 16 bits are stored at 0x200024D0 |

**Notes:** The meaning of each field is unknown. The 0xFFFF sentinel is the only evidence of how the record is used, and the name is a guess.

- Addresses by version: 4130: 0x0800C93C, 4139: 0x0800CF38, 4148: 0x0800DF38, 4168: 0x0800E38C
- Called by: `bms_record_store_from_state`, `bms_4168_0800f8e0`
- Confidence: medium

## bms_snapshot_logger_thunk

**Thunk that runs the snapshot logger tick**

Calls bms_snapshot_logger_tick (0x0800A8A0) with no explicit arguments and returns. It is one of the main-loop periodic calls and keeps no state of its own.

**Notes:** The decompile shows no arguments, which suggests a tail call that passes the caller's registers through. If so, param_1 and param_2 of the logger come from the main loop and not from this thunk.

- Addresses by version: 4130: 0x080076D0, 4139: 0x08007BD0, 4148: 0x0800841C, 4168: 0x0800871C
- Called by: `bms_4168_08010558`
- Calls: `bms_snapshot_logger_tick`
- Confidence: medium

## bms_snapshot_logger_tick

**Snapshot logger: every 5000 units capture and queue a record; commit history every 1000**

Called every tick with the elapsed time in param_1. A zero param_2 resets the 5000-unit accumulator at 0x20000570. Otherwise the accumulator advances by param_1, and at 5000 the routine captures a record at 0x20001360 to 0x20001395: the RTC date-time from bms_rtc_datetime_pack, 13 u16 words from state+0x140, the current at +0x11A, six low bytes from the u16 words at +0x12C to +0x13C, bytes at +0x11E and +0x19C, u32 words from +0x124 and +0x194, two u16 words at +0x13C and +0x13E, and bytes at +0x180 and +0x1D2. The record is registered in the 10-slot pool with bms_slot_pool_register under tag 6. A separate 1000-unit accumulator at 0x20000574 triggers bms_history_ring_commit. Each call ends with bms_status_event_snapshot(param_1).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | elapsed time since the previous call |
| `param_2` | `s32` | mode: 0 resets the 5000-unit accumulator, otherwise the accumulator advances |
| `param_3` | `u32` | not used in this routine |
| `param_4` | `u32` | scratch word; overwritten with the RTC pack result |

**Notes:** The record field layout is taken from the offsets read in the decompile and has no names of its own here. The reset in the mode 0 case clears only the 5000-unit accumulator.

- Addresses by version: 4130: 0x08009938, 4139: 0x08009E70, 4148: 0x0800A58C, 4168: 0x0800A8A0
- Called by: `bms_snapshot_logger_thunk`
- Calls: `bms_status_event_snapshot`, `bms_history_ring_commit`, `bms_rtc_datetime_pack`, `bms_slot_pool_register`, `bms_ram_20000bdc_addr`
- Confidence: medium

## bms_state_restore_or_init

**Restore the state block from flash, or rebuild defaults and identity if the marker is missing**

Boot-time routine. It points the state block at 0x2000002C and the status word at 0x200001C8 (bms_ram_200001c8_addr), and copies the 512-byte block back from flash 0x0803F000 with bms_memcpy_args_swap. It clamps the u16 scale fields at +0xAE and +0x1E0 to 1000 when they are outside 800 to 1000, sets bit 25 of the status word and bit 5 of +0x196, and loads three factory UID words (bms_get_uid_word_by_index 0 to 2) into 0x200008F8, 0x200008FC and 0x20000900. If the marker 0x5A5A at +0x1FE is present and the 12 bytes at +0x186 match the UID words (bms_memcmp_prefix), the restored block is kept; a mismatch clears bit 25 and sets bit 7. Otherwise the block is cleared with bms_mem_zero, a 16-character identity built from the constants 0x3130305A, 0x32303041, 0x41314133 and 0x31303030 (ASCII Z001A0023A1A0001 in memory order) is packed to 14 bytes with bms_pack_7bit_string and copied to +0x02, ten ascending default u16 values from 3474 to 4150 are written at +0x2A to +0x3D, the UID copy is written at +0x186, the marker 0x5A5A is stored, and bit 7 is set. Both paths then write the model code 0x4168 at +0x1C and defaults (+0x00 = 0, +0x18 = 4, +0x20 = 13, +0x22 = 0x01E0, +0x24 = 6, +0x11C = 100, +0x1F4 = 0x6464), clear bit 4 of +0x196 and bit 7 and 8 of +0x126, call bms_index_debounce_step, call bms_4168_08003CC0 (not described here) and set bit 5 of +0x1D4.

**Notes:** The identity string order and the 7-bit packing are inferred from the constants and the callee name. The later write of 7 to the u16 at +0x02 overwrites the first two identity bytes; this may be a bug or intended, and should be checked. Field meanings beyond the model code and the 0x11C capacity value are not established here.

- Addresses by version: 4130: 0x08007018, 4139: 0x08007518, 4148: 0x08007D58, 4168: 0x08008060
- Called by: `bms_4168_08010558`
- Calls: `memcpy`, `bms_mem_zero`, `bms_memcmp_prefix`, `bms_pack_7bit_string`, `bms_profile_select_from_code`, `bms_index_debounce_step`, `bms_memcpy_args_swap`, `bms_get_uid_word_by_index`, `bms_ram_20000bdc_addr`, `bms_ram_200001c8_addr`
- Confidence: medium

## bms_telemetry_sched_thunk

**Thunk that runs the telemetry 16-step scheduler**

Tail-call wrapper with no state of its own. It calls bms_telemetry_sched_16_step (0x0800DDB0) and returns, and the main loop calls it as one of its periodic services.

- Addresses by version: 4130: 0x08006EC8, 4139: 0x080073C8, 4148: 0x08007C08, 4168: 0x08007F10
- Called by: `bms_4168_08010558`
- Calls: `bms_telemetry_sched_16_step`
- Confidence: high

## bms_u16_2000067c_get

**Return the u16 at RAM 0x2000067C**

Returns the halfword at RAM 0x2000067C. Its setter is bms_u16_2000067c_set. The role of this halfword is not established in this packet. Caller: bms_4168_0800bbc4.

**Returns** `u16`: value of the halfword at 0x2000067C

- Addresses by version: 4130: 0x080094C4, 4139: 0x080099FC, 4148: 0x0800A248, 4168: 0x0800A55C
- Called by: `bms_extflash_wait_ready`
- Confidence: medium

## bms_u16_2000067c_set

**Store a u16 into RAM 0x2000067C**

Stores param_1 as a 16-bit value at RAM 0x2000067C, the halfword read by bms_u16_2000067c_get. The role of the halfword is not established in this packet. Caller: bms_4168_0800bbc4.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | value to store |

- Addresses by version: 4130: 0x080094D0, 4139: 0x08009A08, 4148: 0x0800A254, 4168: 0x0800A568
- Called by: `bms_extflash_wait_ready`
- Confidence: medium

## bms_u16_2000067e_get

**Return the u16 at RAM 0x2000067E**

Returns the halfword at RAM 0x2000067E. Its setter is bms_u16_2000067e_set. The role of this halfword is not established in this packet; it sits in the 0x2000067C..0x2000067F block with the 0x2000067C pair. Caller: bms_4168_0800baec.

**Returns** `u16`: value of the halfword at 0x2000067E

- Addresses by version: 4130: 0x08009478, 4139: 0x080099B0, 4148: 0x0800A1FC, 4168: 0x0800A510
- Called by: `bms_extflash_wip_poll`
- Confidence: medium

## bms_u16_2000067e_set

**Store a u16 into RAM 0x2000067E**

Stores param_1 as a 16-bit value at RAM 0x2000067E, the halfword read by bms_u16_2000067e_get. The role of the halfword is not established in this packet. Caller: bms_4168_08005710.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | value to store |

- Addresses by version: 4130: 0x08009484, 4139: 0x080099BC, 4148: 0x0800A208, 4168: 0x0800A51C
- Called by: `bms_timeout_arm_from_record`
- Confidence: medium

## bms_u16_20000dfc_addr

**Return the address of the u16 at RAM 0x20000DFC**

Returns &DAT_20000dfc as a 16-bit pointer so the caller can read or write the halfword. The object is not identified in this packet. Callers: bms_4139_08006f08, bms_4168_08005ab0, bms_4168_08007a0c and bms_4168_080082f0.

**Returns** `ptr`: address of the u16 at 0x20000DFC

- Addresses by version: 4130: 0x0800B684, 4139: 0x0800BBDC, 4148: 0x0800C3C0, 4168: 0x0800C6D4
- Called by: `bms_status_event_snapshot`, `bms_4168_08007a0c`, `bms_4168_080082f0`
- Confidence: medium

## bms_u16x5_block_store

**Copy five u16 values into the 10-byte RAM block at 0x2000051C**

Copies the five halfwords of the source array param_1 to RAM at 0x2000051C, 0x2000051E, 0x20000520, 0x20000522 and 0x20000524, element i going to 0x2000051C + 2i. It is a plain sequence of halfword moves with no size or bounds checks on the source. Caller: bms_4168_08003cc0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source array of five u16 values |

- Addresses by version: 4130: 0x0800B074, 4139: 0x0800B5CC, 4148: 0x0800BCE8, 4168: 0x0800BFFC
- Called by: `bms_profile_select_from_code`
- Confidence: high

## bms_u32_200004dc_addr

**Return the address of the RAM word at 0x200004DC**

Returns &DAT_200004dc as a 32-bit pointer so the caller can read or write the word. The object is not identified in this packet. Caller: bms_4168_08003cc0.

**Returns** `ptr`: address of the RAM word at 0x200004DC

- Addresses by version: 4130: 0x0800B320, 4139: 0x0800B878, 4148: 0x0800C05C, 4168: 0x0800C370
- Called by: `bms_profile_select_from_code`
- Confidence: medium

## bms_u32_20000dec_addr

**Return the address of the RAM word at 0x20000DEC**

Returns &DAT_20000dec as a 32-bit pointer so the caller can read or write the word. The object is not identified in this packet. Caller: bms_4168_08003fcc.

**Returns** `ptr`: address of the RAM word at 0x20000DEC

- Addresses by version: 4130: 0x0800B7B4, 4139: 0x0800BD0C, 4148: 0x0800C4F0, 4168: 0x0800C804
- Called by: `bms_fault_timers_step`
- Confidence: medium

## bms_u32_20001348_get

**Return the u32 at RAM 0x20001348**

Returns DAT_20001348. In this packet it is read only by bms_4168_0800e9dc. The neighbouring words are the dispatch index at 0x20001340 (bms_dispatch_index_nonzero, bms_dispatch_call_current) and the pool count at 0x20001344 (bms_slot_pool_register). The role of 0x20001348 is not established here.

**Returns** `u32`: value of the word at 0x20001348

- Addresses by version: 4130: 0x0800AEBC, 4139: 0x0800B3F4, 4148: 0x0800BB10, 4168: 0x0800BE24
- Called by: `bms_msg_dispatch_request`
- Confidence: medium
