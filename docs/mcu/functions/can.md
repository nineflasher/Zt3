# MCU - `can` functions

22 functions.

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
| [`mcu_can1_reset_pulse`](#mcu_can1_reset_pulse) | 0x0800C278 | Pulse the CAN1 peripheral reset line: assert, then release |
| [`mcu_can_ef00_frame_build`](#mcu_can_ef00_frame_build) | 0x0800D6B6 | Build a 29-bit PGN 0xEF00 CAN frame with three header bytes and up to five payload bytes |
| [`mcu_can_frame_enqueue`](#mcu_can_frame_enqueue) | 0x0800C294 | Queue one classic CAN frame of up to 8 data bytes on message ring 2 |
| [`mcu_can_init`](#mcu_can_init) | 0x08003368 | Initialise CAN1: bus clock, bit timing, six accept-all filters, NVIC and interrupts |
| [`mcu_can_rx_command_dispatch`](#mcu_can_rx_command_dispatch) | 0x080085BC | Dispatch a received command frame to its handler by message ID |
| [`mcu_can_rx_frame_forward`](#mcu_can_rx_frame_forward) | 0x0800E18C | Forward a received CAN frame's 29-bit identifier, DLC and data to the CAN handler |
| [`mcu_can_tp_abort_frame_build`](#mcu_can_tp_abort_frame_build) | 0x0800D72A | Build a J1939 TP.CM connection-abort frame for PGN 0xEF00 |
| [`mcu_can_tp_cts_frame_build`](#mcu_can_tp_cts_frame_build) | 0x0800D768 | Build a J1939 TP.CM clear-to-send frame (control 0x11) for PGN 0xEF00 |
| [`mcu_can_tp_dt_frame_build`](#mcu_can_tp_dt_frame_build) | 0x0800D880 | Build one J1939 TP.DT data frame for PGN 0xEF00 from a 7-byte aligned message offset |
| [`mcu_can_tp_eom_ack_frame_build`](#mcu_can_tp_eom_ack_frame_build) | 0x0800D7C4 | Build a J1939 TP.CM end-of-message acknowledgment (control 0x13) for PGN 0xEF00 |
| [`mcu_can_tp_rts_frame_build`](#mcu_can_tp_rts_frame_build) | 0x0800D820 | Build a J1939 TP.CM request-to-send (control 0x10) for a multi-packet PGN 0xEF00 message |
| [`mcu_can_tp_session_handle_frame`](#mcu_can_tp_session_handle_frame) | 0x0800D1F0 | Advance one J1939 TP.CM/TP.DT session for PGN 0xEF00 by one received frame |
| [`mcu_msg_ring2_tx_step`](#mcu_msg_ring2_tx_step) | 0x08008BB4 | Send the head record of message ring 2 on a free CAN1 mailbox, one frame per call |

## can_base_init

**Initialize CAN control and loopback bits in freeze mode, returns success flag**

Implements the SDK can_base_init sequence on the CAN block. It sets MCTRL.FZEN (bit 0) and polls MSTS.FZC (bit 0) for freeze acknowledge, with a 0xFFFF-iteration timeout. It then writes MCTRL bits from the init struct: TTCEN (bit 7), AEBOEN (bit 6, automatic bus-off recovery), AEDEN (bit 5, automatic doze exit), PRSFEN (bit 4, no retransmission on failure), MDRSEL (bit 3), MMSSR (bit 2), and clears DZEN (bit 1). The mode byte sets BTMG LBEN (bit 30) and LOEN (bit 31). Freeze mode is then left and FZC is polled to clear. Part of the CAN group: mcu_0160_0800bbe2 (baud rate), mcu_0160_0800bdc0 (struct zeroing), mcu_0160_0800bdd2 (filters).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base (CAN1 = 0x40006400) |
| `param_2` | `ptr` | 7-byte base init struct: byte 0 mode, bytes 1..6 the control flags |

**Returns** `u32`: 1 on success, 0 on freeze/unfreeze timeout

- Addresses by version: 12b: 0x0800B80E, 143: 0x0800BABE, 152: 0x0800BAC2, 0160: 0x0800BB22
- Called by: `mcu_can_init`
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
- Called by: `mcu_can_init`
- Confidence: high

## can_default_para_init

**Zero the 7-byte CAN base init struct to reset defaults**

Clears bytes 0..6 of the CAN base init struct: mode selection, TTC, automatic bus-off recovery, automatic doze exit, retransmission rule, overflow discard rule and send order. All-zero is the SDK default (normal communicate mode, FALSE for every flag, first-received discard, send by ID). Matches the SDK can_default_para_init. Part of the CAN group: see mcu_0160_0800bb22. Caller: mcu_0160_08003368.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN base init struct (7 bytes) |

- Addresses by version: 12b: 0x0800BAAC, 143: 0x0800BD5C, 152: 0x0800BD60, 0160: 0x0800BDC0
- Called by: `mcu_can_init`
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
- Called by: `mcu_can_init`
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
- Called by: `CAN1_SE_IRQHandler`
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
- Called by: `CAN1_RX0_IRQHandler`, `CAN1_SE_IRQHandler`
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
- Called by: `mcu_can_init`
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
- Called by: `CAN1_RX0_IRQHandler`
- Confidence: high

## can_message_transmit

**Load a CAN frame into the first empty transmit mailbox and request transmission**

Picks the first empty transmit mailbox by testing TSTS bit 26 (TME0), bit 27 (TME1) and bit 28 (TME2). If none is empty it does nothing. The chosen mailbox at 0x180 + 0x10*n is filled from the struct: an 11-bit standard ID (u16 at offset 0) goes to bits 31:21 when the IDE byte (offset 8) is 0, otherwise the 32-bit word at offset 4 goes to the extended ID (<<3); RTR comes from byte 9; the DLC from byte 10 (TDTR bits 3:0); and the eight data bytes (offsets 11..18) go to TDLR and TDHR. The last step sets TXRQ (bit 0). Matches the SDK can_message_transmit, except that this build returns void and does not report the mailbox number.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base |
| `param_2` | `ptr` | transmit message struct: ID, IDE, RTR, DLC and 8 data bytes |

- Addresses by version: 12b: 0x0800BE6E, 143: 0x0800C11E, 152: 0x0800C122, 0160: 0x0800C182
- Called by: `mcu_msg_ring2_tx_step`
- Confidence: high

## mcu_can1_reset_pulse

**Pulse the CAN1 peripheral reset line: assert, then release**

Asserts and then releases the CAN1 peripheral reset bit (APB1RST bit 25, packed code 0x100019) through crm_periph_reset. The CAN1 controller registers are cleared by the pulse. It is called from the peripheral setup sequence mcu_0160_0800dc08.

- Addresses by version: 12b: 0x0800BF64, 143: 0x0800C214, 152: 0x0800C218, 0160: 0x0800C278
- Called by: `mcu_0160_0800dc08`
- Calls: `crm_periph_reset`
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
- Called by: `mcu_can_ef00_message_send`
- Confidence: medium

## mcu_can_frame_enqueue

**Queue one classic CAN frame of up to 8 data bytes on message ring 2**

Builds a 20-byte ring record for one CAN frame and pushes it onto message ring 2 with mcu_msg_ring2_push (group with mcu_msg_ring2_tx_step). Lengths of 8 or less store the identifier, set the flag byte to 1, store the DLC in the low nibble of the length byte and copy the data. Longer lengths are dropped and the 32-bit counter at 0x20000340 is incremented instead.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | CAN identifier |
| `param_2` | `ptr` | payload source |
| `param_3` | `u32` | data length; lengths 0..8 are queued |

**Notes:** The decompiler puts the identifier one word after the pointer that it passes to the push routine. This disagrees with the layout in mcu_msg_ring2_enqueue_frames, so the exact record offsets are uncertain.

- Addresses by version: 12b: 0x0800BF80, 143: 0x0800C230, 152: 0x0800C234, 0160: 0x0800C294
- Called by: `mcu_can_ef00_message_send`, `mcu_can_rx_frame_forward`
- Calls: `mcu_msg_ring2_push`
- Confidence: medium

## mcu_can_init

**Initialise CAN1: bus clock, bit timing, six accept-all filters, NVIC and interrupts**

Runs once at startup to bring up CAN1. It calls mcu_0160_0800c058 (not yet described), enables a bus clock through crm_periph_clock_enable with peripheral id 0x1C0019 (presumably CAN1), and builds a 7-byte base configuration on the stack with all bytes zero except byte 3, which is 1, then passes it to can_base_init (freeze mode and control/loopback bits). Bit timing is programmed with can_baudrate_set using prescaler 9, resync width 1, BS1 10 and BS2 3, which is 14 time quanta per bit; the bit rate itself depends on the APB1 clock, which is not in this packet. Filter banks 0 to 5 are each configured with can_filter_init, activated, with all ID and mask words zero so every frame is accepted. It then sets NVIC priorities for IRQ 0x16 (CAN1_SE, preempt 2, sub 0) and IRQ 0x14 (CAN1_RX0, preempt 1, sub 0), and enables interrupt bits 0x2, 0x400, 0x800 and 0x8000 through can_interrupt_enable.

**Notes:** Interrupt bit 0x2 is FIFO 0 message-pending, confirmed by the INTEN field names. 0x400, 0x800 and 0x8000 are taken to be bus-off, error type change and error by analogy with the bxCAN layout. The 0x1C0019 id and the byte-3 field are SDK-level assumptions.

- Addresses by version: 12b: 0x08003444, 143: 0x08003344, 152: 0x080032C8, 0160: 0x08003368
- Peripheral registers: `CAN1.MCTRL` (A)
- Called by: `mcu_0160_0800325c`, `mcu_0160_0800dc08`
- Calls: `can_base_init`, `can_baudrate_set`, `can_default_para_init`, `can_filter_init`, `mcu_gpioa_pin_cfg_init`, `can_interrupt_enable`, `crm_periph_clock_enable`, `nvic_irq_enable`
- Confidence: medium

## mcu_can_rx_command_dispatch

**Dispatch a received command frame to its handler by message ID**

Reads the message ID word at the start of the frame (param_1), the payload length byte at +0x0A and the payload at +0x0B. It handles IDs 0x482, 0x100, 0x20C, 0x310, 0x311, 0x485, 0x486, 0x7F0 and 0x7F1, and most handlers call mcu_cmd_state_clear first. The 0x100 frame copies its payload into the block at 0x20001FD2, bumps the 32-bit counter at 0x2000062C (split into halfwords at 0x20001F1C and 0x20001F1E), updates the saturating counter 0x200003BE from bit 0x10 of 0x20001FD4, and passes the first payload byte to mcu_sample_history3_rise_detect. The 0x20C frame copies its payload into 0x20001FDA, the status word read by mcu_hall_dispatch_pc12_output and mcu_status_drive_pb6_pc11. The 0x311 frame stores its 16-bit value divided by 10 at 0x200003E6, limited to 33 to 42 with a default of 40. The 0x485 frame stores a u16 at +0x0F divided by 32768 and a byte at +0x11 divided by 10 as floats, and the 0x486 frame stores two bytes. Frames 0x7F0 and 0x7F1 count heartbeats in 0x20000628 and copy bit 0x2 of their first payload byte into bit 1 of 0x20000320. Most handled frames refresh a timeout word of 200 ticks, set in 0x2000032C, 0x20000332 or 0x20000322.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | received frame record: message ID word at +0, payload length at +0x0A, payload at +0x0B |

**Notes:** The frame layout is inferred from the handler offsets. The bus is probably CAN, since the MCU receives from the VCU over CAN1. Group with mcu_cmd_state_clear and mcu_take_pending_200003ba.

- Addresses by version: 12b: 0x08008378, 143: 0x080084B4, 152: 0x080085A4, 0160: 0x080085BC
- Called by: `mcu_0160_08003376`
- Calls: `__aeabi_memcpy`, `__ARM_scalbnf`, `__aeabi_ui2f`, `__aeabi_fdiv`, `mcu_take_pending_200003ba`, `mcu_cmd_state_clear`, `mcu_sample_history3_rise_detect`
- Confidence: medium

## mcu_can_rx_frame_forward

**Forward a received CAN frame's 29-bit identifier, DLC and data to the CAN handler**

Receive-callback adapter that unpacks the CAN frame struct: the 29-bit extended identifier is the low 29 bits of the first word (mask 0x1FFFFFFF), the DLC is the byte at offset 4, and the data begins at offset 5. It calls mcu_0160_0800c294 with (identifier, data pointer, DLC) and returns 1 unconditionally. The function does no filtering or dispatch itself; the handler behind mcu_0160_0800c294 is documented in its own packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | not used by this function |
| `param_2` | `ptr` | received CAN frame: identifier word at +0, DLC at +4, data at +5 |

**Returns** `u32`: always 1

**Notes:** The DLC is passed as a signed char, so a DLC byte above 127 reaches the callee as a negative value.

- Addresses by version: 12b: 0x0800DD58, 143: 0x0800DFB4, 152: 0x0800E04C, 0160: 0x0800E18C
- Calls: `mcu_can_frame_enqueue`
- Confidence: high

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
- Called by: `mcu_can_tp_timeout_tick`, `mcu_can_tp_session_handle_frame`
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
- Called by: `mcu_can_tp_session_handle_frame`
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
- Called by: `mcu_can_tp_sender_step`
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
- Called by: `mcu_can_tp_session_handle_frame`
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
- Called by: `mcu_can_tp_sender_step`
- Confidence: medium

## mcu_can_tp_session_handle_frame

**Advance one J1939 TP.CM/TP.DT session for PGN 0xEF00 by one received frame**

One step of a J1939 multi-packet transport session for the proprietary PGN 0xEF00, called once per received frame for one 36-byte session record selected by the caller mcu_0160_0800d038. The frame's first word holds SA in byte 0, DA (PS field) in byte 1 and PF in byte 2; the TP.CM control byte is data byte 0 at frame offset 5, and the PGN is accepted only when data bytes 5..7 are 00 EF 00. Receiver role: an RTS (control 0x10) from an idle session or from the same peer is accepted when the size (data byte 1 only) is at most the buffer capacity at session+0x08 and the packet count (data byte 3) equals ceil(size/7); the session then sends a CTS for all packets with next packet 1, enters state 10 and arms a 1250 ms timeout, otherwise it sends an abort and goes idle. Each in-sequence TP.DT (PF 0xEB, sequence number = previous + 1) copies min(remaining, 7) payload bytes into the buffer at session+0x04, adds every byte below size-2 into a 16-bit running sum at session+0x1e and re-arms a 750 ms timeout; an out-of-sequence DT sends an abort. After the last byte the final two bytes, read little-endian, must equal the one's complement of that sum: on success an EOM ACK is sent and the message callback receives size-2 bytes, on mismatch an abort is sent. Sender role: in state 6 a zero-count CTS holds the session in state 7 with a 1050 ms timeout, while a non-zero CTS in state 4 or 7 sets the next packet, the byte offset (next-1)*7 and the burst end at session+0x12 and enters state 5; an EOM ACK received in state 9 at the matching offset returns the session to idle and calls the completion callback with status 3, and an abort (control 0xFF) from the peer returns it to idle without a callback.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TP session record, 36 bytes (layout in notes); state at +0x02, buffer pointer at +0x04 |
| `param_2` | `ptr` | received CAN frame: 32-bit identifier word at +0, DLC byte at +4, data bytes at +5..+12 |
| `param_3` | `ptr` | callback table: +0x04 transfer complete(session, byte0, byte1, status), +0x08 message delivered(session, byte0, byte1, buffer, length), +0x0c transmit frame(session, frame) |

**Notes:** Session layout (inferred from accesses): +0x00 peer address byte, +0x01 own address byte, +0x02 state (1 = idle, 10 = receiving data, 9 = all data sent and waiting for EOM ACK, 6 = RTS sent and waiting for CTS, 7 = held after a zero-count CTS, 5 = sending a burst, 4 = role not identified), +0x04 buffer pointer, +0x08 u16 buffer capacity, +0x0a u16 byte offset, +0x0c u16 total message size, +0x0e u16 last sequence number, +0x10 u16 total packets (RTS) or next packet (CTS), +0x12 u16 burst end offset, +0x14 u16 time base (ms per tick, inferred), +0x16 u16 cleared at session start (purpose unknown), +0x18 s16 timeout countdown in ticks (decremented outside this function), +0x1e u16 running checksum. The 36-byte stride is taken from the caller. Open points: (1) only data byte 1 of the TP.CM size is read, so messages above 255 bytes cannot be expressed; this needs checking against the disassembly. (2) In state 6 this branch ignores a CTS with a non-zero packet count, so either another path handles the first CTS or the state is reached differently. (3) The timeout values are computed as 1250, 1050 and 750 divided by session+0x14 with no zero check. (4) The meaning of states 4 and 9 is inferred because they are set outside this function. (5) The 750, 1050 and 1250 ms values match the J1939-21 T1, T4 and T2/T3 magnitudes; the mapping to those names is not confirmed. (6) The completion callback at +0x04 is null-checked, the message callback at +0x08 is null-checked, the transmit callback at +0x0c is not.

- Addresses by version: 12b: 0x0800CECC, 143: 0x0800D148, 152: 0x0800D190, 0160: 0x0800D1F0
- Called by: `mcu_can_tp_rx_dispatch`
- Calls: `mcu_can_tp_abort_frame_build`, `mcu_can_tp_cts_frame_build`, `mcu_can_tp_eom_ack_frame_build`
- Confidence: medium

## mcu_msg_ring2_tx_step

**Send the head record of message ring 2 on a free CAN1 mailbox, one frame per call**

Drains one record per call from message ring 2, the 32-entry ring of 20-byte records with the write index at 0x20001880 and the read index at 0x20001884 (group with mcu_msg_ring2_push, mcu_msg_ring2_peek and mcu_msg_ring2_count). It returns 0 at once when the ring is empty. If CAN1.MSTS bit 8 (CUSS, the unit is still sending) is set it leaves the ring alone and returns the pending count. Otherwise it peeks the head record, passes it to can_message_transmit on CAN1, and advances the read index modulo 32 only when that call did not return 4, the code's no-free-mailbox result.

**Returns** `u16`: 0 if the ring was empty on entry, otherwise the number of records still queued after the attempt

**Notes:** The name CUSS for MSTS bit 8 is from the SVD header; the meaning of the return value 4 is taken from the code.

- Addresses by version: 12b: 0x08008964, 143: 0x08008B00, 152: 0x08008B40, 0160: 0x08008BB4
- Peripheral registers: `CAN1.MCTRL` (A), `CAN1.MSTS` (R)
- Called by: `mcu_0160_0800a0b0`
- Calls: `mcu_msg_ring2_peek`, `mcu_msg_ring2_count`, `can_message_transmit`
- Confidence: high
