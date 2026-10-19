# MCU - `can` functions

15 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`can_base_init`](#can_base_init) | 0x0800BB22 | Initialize CAN control and loopback bits in freeze mode, returns success flag |
| [`can_baudrate_set`](#can_baudrate_set) | 0x0800BBE2 | Program CAN bit timing (BTMG): prescaler, resync width, BS1, BS2 |
| [`can_default_para_init`](#can_default_para_init) | 0x0800BDC0 | Zero the 7-byte CAN base init struct to reset defaults |
| [`can_filter_init`](#can_filter_init) | 0x0800BDD2 | Configure one CAN acceptance filter bank: scale, mode, FIFO, ID/mask words |
| [`can_flag_clear`](#can_flag_clear) | 0x0800BF14 | Clear one CAN status flag by writing its write-1-to-clear bit |
| [`can_flag_get`](#can_flag_get) | 0x0800BF84 | Test a CAN status flag selected by SDK flag code, returns 1 when set |
| [`can_interrupt_enable`](#can_interrupt_enable) | 0x0800C0B8 | Set or clear CAN interrupt-enable bits in CAN.INTEN |
| [`can_message_receive`](#can_message_receive) | 0x0800C0CE | Read one frame from a CAN RX FIFO mailbox into a struct and release the slot |
| [`can_message_transmit`](#can_message_transmit) | 0x0800C182 | Load a CAN frame into the first empty transmit mailbox and request transmission |
| [`mcu_can_ef00_frame_build`](#mcu_can_ef00_frame_build) | 0x0800D6B6 | Build a 29-bit PGN 0xEF00 CAN frame with three header bytes and up to five payload bytes |
| [`mcu_can_tp_abort_frame_build`](#mcu_can_tp_abort_frame_build) | 0x0800D72A | Build a J1939 TP.CM connection-abort frame for PGN 0xEF00 |
| [`mcu_can_tp_cts_frame_build`](#mcu_can_tp_cts_frame_build) | 0x0800D768 | Build a J1939 TP.CM clear-to-send frame (control 0x11) for PGN 0xEF00 |
| [`mcu_can_tp_dt_frame_build`](#mcu_can_tp_dt_frame_build) | 0x0800D880 | Build one J1939 TP.DT data frame for PGN 0xEF00 from a 7-byte aligned message offset |
| [`mcu_can_tp_eom_ack_frame_build`](#mcu_can_tp_eom_ack_frame_build) | 0x0800D7C4 | Build a J1939 TP.CM end-of-message acknowledgment (control 0x13) for PGN 0xEF00 |
| [`mcu_can_tp_rts_frame_build`](#mcu_can_tp_rts_frame_build) | 0x0800D820 | Build a J1939 TP.CM request-to-send (control 0x10) for a multi-packet PGN 0xEF00 message |

## can_base_init

**Initialize CAN control and loopback bits in freeze mode, returns success flag**

Implements the SDK can_base_init sequence on the CAN block. It sets MCTRL.FZEN (bit 0) and polls MSTS.FZC (bit 0) for freeze acknowledge, with a 0xFFFF-iteration timeout. It then writes MCTRL bits from the init struct: TTCEN (bit 7), AEBOEN (bit 6, automatic bus-off recovery), AEDEN (bit 5, automatic doze exit), PRSFEN (bit 4, no retransmission on failure), MDRSEL (bit 3), MMSSR (bit 2), and clears DZEN (bit 1). The mode byte sets BTMG LBEN (bit 30) and LOEN (bit 31). Freeze mode is then left and FZC is polled to clear. Part of the CAN group: mcu_0160_0800bbe2 (baud rate), mcu_0160_0800bdc0 (struct zeroing), mcu_0160_0800bdd2 (filters).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base (CAN1 = 0x40006400) |
| `param_2` | `ptr` | 7-byte base init struct: byte 0 mode, bytes 1..6 the control flags |

**Returns** `u32`: 1 on success, 0 on freeze/unfreeze timeout

- Addresses by version: 12b: 0x0800B80E, 143: 0x0800BABE, 152: 0x0800BAC2, 0160: 0x0800BB22
- Called by: `mcu_0160_08003368`
- Confidence: high

## can_baudrate_set

**Program CAN bit timing (BTMG): prescaler, resync width, BS1, BS2**

Enters freeze mode and waits for FZC, then writes BTMG (offset 0x1C). BRP = (baudrate_div - 1) & 0xFFF goes to bits 11:0, RSAW (SJW) 2 bits go to bits 25:24 from struct byte 2, BTS1 4 bits to bits 19:16 from byte 3, and BTS2 3 bits to bits 22:20 from byte 4. The divider is a u16 at struct offset 0. Freeze mode is then left and FZC is polled. Matches the SDK can_baudrate_set. Part of the CAN group: see mcu_0160_0800bb22.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base |
| `param_2` | `ptr` | baud rate struct: u16 divider at 0, then RSAW, BTS1, BTS2 bytes |

**Returns** `u32`: 1 on success, 0 on freeze/unfreeze timeout

- Addresses by version: 12b: 0x0800B8CE, 143: 0x0800BB7E, 152: 0x0800BB82, 0160: 0x0800BBE2
- Called by: `mcu_0160_08003368`
- Confidence: high

## can_default_para_init

**Zero the 7-byte CAN base init struct to reset defaults**

Clears bytes 0..6 of the CAN base init struct: mode selection, TTC, automatic bus-off recovery, automatic doze exit, retransmission rule, overflow discard rule and send order. All-zero is the SDK default (normal communicate mode, FALSE for every flag, first-received discard, send by ID). Matches the SDK can_default_para_init. Part of the CAN group: see mcu_0160_0800bb22. Caller: mcu_0160_08003368.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN base init struct (7 bytes) |

- Addresses by version: 12b: 0x0800BAAC, 143: 0x0800BD5C, 152: 0x0800BD60, 0160: 0x0800BDC0
- Called by: `mcu_0160_08003368`
- Confidence: high

## can_filter_init

**Configure one CAN acceptance filter bank: scale, mode, FIFO, ID/mask words**

Sets FCTRL.FCS to enter filter configuration, then for the bank number in struct byte 3: clears its activation bit in FACFG (0x21C), packs the id/mask halfwords at struct bytes 6..13 into FB[n].FFDB1 and FFDB2 (base 0x240 + 8n) using the 16-bit layout (four halfwords) when byte 4 is 0 and the 32-bit layout (two words) otherwise, sets FSCFG (0x20C) for 32-bit scale or clears it for 16-bit, sets FMCFG (0x204) for ID-list mode (byte 1 = 1) or clears it for ID-mask mode, sets FRF (0x214) for FIFO 1 (byte 2 = 1) or clears it for FIFO 0, and finally sets or clears FACFG from byte 0. FCS is cleared at the end. Matches the SDK can_filter_init. Part of the CAN group: see mcu_0160_0800bb22. Caller: mcu_0160_08003368.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base |
| `param_2` | `ptr` | filter struct: byte 0 activate, 1 mode, 2 FIFO, 3 bank 0..13, 4 scale, bytes 6..13 id/mask halfwords |

**Notes:** Byte offsets are read from the decompile. The SDK field names for the halfwords are not confirmed beyond the packing order.

- Addresses by version: 12b: 0x0800BABE, 143: 0x0800BD6E, 152: 0x0800BD72, 0160: 0x0800BDD2
- Called by: `mcu_0160_08003368`
- Confidence: high

## can_flag_clear

**Clear one CAN status flag by writing its write-1-to-clear bit**

Switches on the SDK CAN_*_FLAG code. Each case writes a constant to one status register, which clears the flag: MSTS (offset 0x04) for the error flags and EOIF (value 4), with ETR also zeroing ESTS (0x18); TSTS (0x08) for the TM0, TM1 and TM2 transmit-complete flags (bits 0, 8 and 16, or 0x10101 for all three); RF0R (0x0C) and RF1R (0x10) for the FIFO full and overrun flags. Codes 0x0F and 0x10 write MSTS bits 3 and 4. Unknown codes do nothing. Matches the SDK can_flag_clear. Part of the CAN group: see mcu_0160_0800bb22.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base |
| `param_2` | `u32` | flag code (SDK CAN_*_FLAG value) |

**Notes:** Case-to-bit mapping follows the decompile. Not every case was checked against the SDK flag constants.

- Addresses by version: 12b: 0x0800BC00, 143: 0x0800BEB0, 152: 0x0800BEB4, 0160: 0x0800BF14
- Called by: `mcu_0160_080032f8`
- Confidence: high

## can_flag_get

**Test a CAN status flag selected by SDK flag code, returns 1 when set**

Switches on the SDK CAN_*_FLAG code and tests one bit: ESTS bits 0, 1 and 2 (EAF, EPF, BOF); ESTS bits 6:4 for ETR (any non-zero last error code); MSTS bit 2 for EOIF; TSTS bit 0, 8 or 16 for TM0, TM1 or TM2 transmit complete; RF0 and RF1 bits 1:0 (pending message count), 3 (full) and 4 (overrun); MSTS bit 3 (code 0x0F); MSTS bit 1 or 4 (code 0x10); and TSTS bits 26..28 (code 0x11, any transmit mailbox empty). It returns 1 if the selected bit is set and 0 otherwise. Matches the SDK can_flag_get. Part of the CAN group: see mcu_0160_0800bb22.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base |
| `param_2` | `u32` | flag code (SDK CAN_*_FLAG value) |

**Returns** `bool`: true if the selected flag is set

**Notes:** Case-to-bit mapping follows the decompile. The meaning of MSTS bits 1, 3 and 4 is not confirmed against the SDK flag names.

- Addresses by version: 12b: 0x0800BC70, 143: 0x0800BF20, 152: 0x0800BF24, 0160: 0x0800BF84
- Called by: `mcu_0160_080032cc`, `mcu_0160_080032f8`
- Confidence: high

## can_interrupt_enable

**Set or clear CAN interrupt-enable bits in CAN.INTEN**

Read-modify-write of CAN.INTEN (offset 0x14). The mask is ORed in when the new-state argument is non-zero and cleared otherwise. Matches the SDK can_interrupt_enable. Part of the CAN group: see mcu_0160_0800bb22.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base |
| `param_2` | `u32` | interrupt enable mask (CAN_*_INT) |
| `param_3` | `s32` | new state: non-zero enables, zero disables |

- Addresses by version: 12b: 0x0800BDA4, 143: 0x0800C054, 152: 0x0800C058, 0160: 0x0800C0B8
- Called by: `mcu_0160_08003368`
- Confidence: high

## can_message_receive

**Read one frame from a CAN RX FIFO mailbox into a struct and release the slot**

Selects the RX mailbox at 0x1B0 for FIFO 0 or 0x1C0 for FIFO 1 (fifo index * 0x10). It decodes the ID word RXMI (+0): IDE (bit 2) and RTR (bit 1) become struct flags, the standard ID is bits 31:21, and the extended ID is bits 31:3. The DLC (bits 3:0) and filter match index FMI (bits 15:8) come from RXMDT (+4). The eight data bytes come from RXMDL (+8) and RXMDH (+0xC). Finally RFOM (bit 5) is written to RF0R (0x0C) or RF1R (0x10) to release the slot. Matches the SDK can_message_receive, without the return value.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base |
| `param_2` | `u32` | RX FIFO number 0 or 1 |
| `param_3` | `ptr` | receive message struct filled with ID, flags, DLC, FMI and 8 data bytes |

- Addresses by version: 12b: 0x0800BDBA, 143: 0x0800C06A, 152: 0x0800C06E, 0160: 0x0800C0CE
- Called by: `mcu_0160_080032cc`
- Confidence: high

## can_message_transmit

**Load a CAN frame into the first empty transmit mailbox and request transmission**

Picks the first empty transmit mailbox by testing TSTS bit 26 (TME0), bit 27 (TME1) and bit 28 (TME2). If none is empty it does nothing. The chosen mailbox at 0x180 + 0x10*n is filled from the struct: an 11-bit standard ID (u16 at offset 0) goes to bits 31:21 when the IDE byte (offset 8) is 0, otherwise the 32-bit word at offset 4 goes to the extended ID (<<3); RTR comes from byte 9; the DLC from byte 10 (TDTR bits 3:0); and the eight data bytes (offsets 11..18) go to TDLR and TDHR. The last step sets TXRQ (bit 0). Matches the SDK can_message_transmit, except that this build returns void and does not report the mailbox number.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base |
| `param_2` | `ptr` | transmit message struct: ID, IDE, RTR, DLC and 8 data bytes |

- Addresses by version: 12b: 0x0800BE6E, 143: 0x0800C11E, 152: 0x0800C122, 0160: 0x0800C182
- Called by: `mcu_0160_08008bb4`
- Confidence: high

## mcu_can_ef00_frame_build

**Build a 29-bit PGN 0xEF00 CAN frame with three header bytes and up to five payload bytes**

Fills a software CAN frame (word 0 = 29-bit identifier, byte 4 = DLC, bytes 5..12 = data). The identifier is priority << 26 | destination << 8 | source, masked to 29 bits, then ORed with 0x00EF0000 (PDU1 format 0xEF, the proprietary-A PGN 0xEF00) and 0x20000000 (bit 29, set as the extended-identifier marker). Bit 31 of the old word is preserved. The DLC is payload + 3, the three header bytes go to data bytes 0..2 and the payload follows from data byte 3. The call fails when priority is 8 or more, when the payload is 6 bytes or longer, or when a pointer is null. The TP functions below use the same identifier scheme for multi-packet transfers on this channel.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | CAN priority 0..7 |
| `param_2` | `u8` | data byte 0 (header) |
| `param_3` | `u32` | source address (ID bits 0..7) |
| `param_4` | `u32` | destination address (ID bits 8..15) |
| `param_5` | `u8` | data byte 1 (header) |
| `param_6` | `u8` | data byte 2 (header) |
| `param_7` | `ptr` | payload source |
| `param_8` | `u32` | payload length 0..5 |
| `param_9` | `ptr` | output CAN frame struct |

**Returns** `bool`: 1 on success, 0 on bad arguments

**Notes:** The header byte semantics are not known from this function alone. The VCU twin annotation vcu_can_ef00_frame_build describes the same routine.

- Addresses by version: 12b: 0x0800D354, 143: 0x0800D5CC, 152: 0x0800D614, 0160: 0x0800D6B6
- Called by: `mcu_0160_0800cdd8`
- Confidence: medium

## mcu_can_tp_abort_frame_build

**Build a J1939 TP.CM connection-abort frame for PGN 0xEF00**

Builds an 8-byte J1939 TP.CM frame. The identifier is 0x20EC0000 | destination << 8 | source (PF 0xEC = TP.CM, bit 29 set, no priority bits). The data is FF FF FF FF FF 00 EF 00: control byte 0xFF (connection abort), reason 0xFF, reserved bytes 0xFF, and the aborted PGN 0x00EF00 in bytes 5..7. It is used when a multi-packet transfer on the proprietary channel must stop.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | source address (ID bits 0..7) |
| `param_2` | `u32` | destination address (ID bits 8..15) |
| `param_3` | `ptr` | output CAN frame struct |

**Returns** `bool`: 1 on success, 0 when the frame pointer is null

**Notes:** The VCU twin annotation vcu_can_tp_abort_frame_build describes the identifier as 0x18EC (priority 6). This MCU code does not set the priority bits, so the identifier here is 0x20EC.... The difference should be checked against the binary.

- Addresses by version: 12b: 0x0800D3C8, 143: 0x0800D640, 152: 0x0800D688, 0160: 0x0800D72A
- Called by: `mcu_0160_0800b65c`, `mcu_0160_0800d1f0`
- Confidence: medium

## mcu_can_tp_cts_frame_build

**Build a J1939 TP.CM clear-to-send frame (control 0x11) for PGN 0xEF00**

Builds the TP.CM clear-to-send frame with the same identifier scheme as the abort frame. Data bytes: 0x11, the number of packets the receiver accepts now (param_3), the next packet number expected (param_4), 0xFF, 0xFF, then the PGN bytes 00 EF 00. The receiver sends it to start or resume a multi-packet transfer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | source address (ID bits 0..7) |
| `param_2` | `u32` | destination address (ID bits 8..15) |
| `param_3` | `u8` | number of packets the receiver accepts now |
| `param_4` | `u8` | next packet number expected |
| `param_5` | `ptr` | output CAN frame struct |

**Returns** `bool`: 1 on success, 0 when the frame pointer is null

- Addresses by version: 12b: 0x0800D406, 143: 0x0800D67E, 152: 0x0800D6C6, 0160: 0x0800D768
- Called by: `mcu_0160_0800d1f0`
- Confidence: medium

## mcu_can_tp_dt_frame_build

**Build one J1939 TP.DT data frame for PGN 0xEF00 from a 7-byte aligned message offset**

Builds one TP.DT frame with identifier 0x20EB0000 | destination << 8 | source. Data byte 0 is the sequence number (offset / 7) + 1, computed as (offset + 6) / 7 + 1, followed by payload bytes: the byte count is min(*remaining, 7), copied from the message, and the rest of the data bytes are filled with 0xFF. The count is written back to *remaining. The offset must be a multiple of 7 or the call fails. The decompiled loop bounds look off by one: the copy loop runs count + 1 times and the padding loop starts at the last copied payload byte, so that byte is overwritten with 0xFF, and a full 7-byte chunk also writes one byte past the frame data. The VCU twin annotation reports the same pattern. Verify against the disassembly before relying on exact byte counts. On success the low word of the return value is 1; the high word holds an unclear count or 0xFF.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | source address (ID bits 0..7) |
| `param_2` | `u32` | destination address (ID bits 8..15) |
| `param_3` | `u32` | byte offset of this chunk in the message, must be a multiple of 7 |
| `param_4` | `ptr` | message source at the chunk offset |
| `param_5` | `ptr` | in/out u16: bytes remaining; clamped to 7 and written back |
| `param_6` | `ptr` | output CAN frame struct |

**Returns** `bool`: 1 on success in the low word, 0 on bad arguments

**Notes:** The sequence number formula matches the TP.DT convention (1-based packet number). The byte-count and padding arithmetic is uncertain, see description.

- Addresses by version: 12b: 0x0800D520, 143: 0x0800D798, 152: 0x0800D7E0, 0160: 0x0800D880
- Called by: `mcu_0160_0800d10a`
- Confidence: low

## mcu_can_tp_eom_ack_frame_build

**Build a J1939 TP.CM end-of-message acknowledgment (control 0x13) for PGN 0xEF00**

Builds the TP.CM end-of-message acknowledgment. Data bytes: 0x13, the total message size in bytes little-endian (bytes 1..2), the number of data packets (size + 6) / 7 = ceil(size / 7) in byte 3, 0xFF in byte 4, then the PGN bytes 00 EF 00. The receiver sends it after the last data packet arrives.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | source address (ID bits 0..7) |
| `param_2` | `u32` | destination address (ID bits 8..15) |
| `param_3` | `u32` | total message size in bytes |
| `param_4` | `ptr` | output CAN frame struct |

**Returns** `bool`: 1 on success, 0 when the frame pointer is null

- Addresses by version: 12b: 0x0800D464, 143: 0x0800D6DC, 152: 0x0800D724, 0160: 0x0800D7C4
- Called by: `mcu_0160_0800d1f0`
- Confidence: medium

## mcu_can_tp_rts_frame_build

**Build a J1939 TP.CM request-to-send (control 0x10) for a multi-packet PGN 0xEF00 message**

Builds the TP.CM request-to-send for a message longer than 8 bytes. Data bytes: 0x10, total size in bytes little-endian (bytes 1..2), the number of data packets (size + 6) / 7 in byte 3, 0xFF in byte 4 (no limit on packets per CTS) and the PGN bytes 00 EF 00. The call fails when the size is 8 or less or the pointer is null, because such messages go in a single frame.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | source address (ID bits 0..7) |
| `param_2` | `u32` | destination address (ID bits 8..15) |
| `param_3` | `u32` | total message size in bytes, must be more than 8 |
| `param_4` | `ptr` | output CAN frame struct |

**Returns** `bool`: 1 on success, 0 when the size is 8 or less or the pointer is null

- Addresses by version: 12b: 0x0800D4C0, 143: 0x0800D738, 152: 0x0800D780, 0160: 0x0800D820
- Called by: `mcu_0160_0800d10a`
- Confidence: medium
