# BMS - `fdcan` functions

24 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`HAL_FDCAN_ActivateNotification`](#hal_fdcan_activatenotification) | 0x080014CC | Enables FDCAN interrupt sources and routes their groups to interrupt lines 0 and 1 |
| [`HAL_FDCAN_AddMessageToTxFifoQ`](#hal_fdcan_addmessagetotxfifoq) | 0x080015C4 | Writes one frame into the next Tx FIFO slot in message RAM and requests transmission |
| [`HAL_FDCAN_ConfigFilter`](#hal_fdcan_configfilter) | 0x0800168C | Writes one standard or extended acceptance filter element into message RAM |
| [`HAL_FDCAN_ConfigGlobalFilter`](#hal_fdcan_configglobalfilter) | 0x080016F0 | Sets the global filter (RXGFC) actions for non-matching and remote frames |
| [`HAL_FDCAN_ErrorCallback`](#hal_fdcan_errorcallback) | 0x08001754 | Empty weak FDCAN error callback, invoked by the FDCAN interrupt dispatcher |
| [`HAL_FDCAN_GetRxMessage`](#hal_fdcan_getrxmessage) | 0x08001758 | Reads one received frame from RX FIFO0 or FIFO1 and releases its element |
| [`HAL_FDCAN_GetTxFifoFreeLevel`](#hal_fdcan_gettxfifofreelevel) | 0x0800184C | Returns the Tx FIFO free level from TXFQS, masked to bits 0-2 |
| [`HAL_FDCAN_Start`](#hal_fdcan_start) | 0x08001CF6 | Starts FDCAN: requires READY, clears CCCR.INIT and moves the state to BUSY |
| [`HAL_FDCAN_Stop`](#hal_fdcan_stop) | 0x08001D22 | Stops FDCAN: sets CCCR.INIT, handles clock-stop acknowledge, re-enables configuration change |
| [`bms_can_pack_ext_frame`](#bms_can_pack_ext_frame) | 0x080105FC | Pack a 29-bit extended CAN frame (ID, DLC, 3 header bytes, payload) into a TX buffer |
| [`bms_fdcan_add_mask_filter`](#bms_fdcan_add_mask_filter) | 0x08008C64 | Add one FDCAN mask filter to RX FIFO 0, resetting the MCU if HAL rejects it |
| [`bms_fdcan_cb_ir_100`](#bms_fdcan_cb_ir_100) | 0x08001DB2 | Empty FDCAN callback for IR flag 0x100 (bit 8), receives the cancelled-buffer mask |
| [`bms_fdcan_cb_ir_1c00`](#bms_fdcan_cb_ir_1c00) | 0x08001DB6 | Empty FDCAN interrupt hook for IR flags 0x1C00 (bits 10-12) |
| [`bms_fdcan_cb_ir_200`](#bms_fdcan_cb_ir_200) | 0x08001DB8 | Empty FDCAN interrupt hook for IR flag 0x200 (bit 9) |
| [`bms_fdcan_cb_ir_2000`](#bms_fdcan_cb_ir_2000) | 0x08001DB0 | Empty FDCAN interrupt hook for IR flag 0x2000 (bit 13) |
| [`bms_fdcan_cb_ir_38`](#bms_fdcan_cb_ir_38) | 0x08001CF4 | Empty FDCAN interrupt hook for IR flags 0x38 (bits 3-5) |
| [`bms_fdcan_cb_ir_40`](#bms_fdcan_cb_ir_40) | 0x08001858 | Empty FDCAN interrupt hook for IR flag 0x40 (bit 6) |
| [`bms_fdcan_cb_ir_80`](#bms_fdcan_cb_ir_80) | 0x08001DB4 | Empty FDCAN callback for IR flag 0x80 (bit 7), receives the completed-buffer mask |
| [`bms_fdcan_cb_ir_8000`](#bms_fdcan_cb_ir_8000) | 0x08001DAE | Empty FDCAN interrupt hook for IR flag 0x8000 (bit 15) |
| [`bms_fdcan_cb_ir_e0000`](#bms_fdcan_cb_ir_e0000) | 0x08001756 | Empty FDCAN interrupt hook for IR bits 17-19 (mask 0xE0000) |
| [`bms_fdcan_filters_start`](#bms_fdcan_filters_start) | 0x08008CA0 | Set up FDCAN1 filters, reject unmatched frames, start FDCAN and enable RX FIFO 0 interrupts |
| [`bms_fdcan_send_frame`](#bms_fdcan_send_frame) | 0x08008C14 | Build an FDCAN Tx header from a frame record and queue it in the Tx FIFO |
| [`bms_fdcan_tx_fifo_full`](#bms_fdcan_tx_fifo_full) | 0x08008BFC | Return 1 when the FDCAN1 Tx FIFO has no free element, else 0 |
| [`fdcan2_is_bus_off`](#fdcan2_is_bus_off) | 0x08008C8C | Return 1 when FDCAN2 is bus-off (FDCAN_PSR.BO set) |

## HAL_FDCAN_ActivateNotification

**Enables FDCAN interrupt sources and routes their groups to interrupt lines 0 and 1**

param_1 is the FDCAN handle: instance pointer at +0x00, state byte at +0x5C, error code word at +0x60. The call is rejected unless the state is READY (1) or BUSY (2); it then sets error bit 0x2 and returns 1. Otherwise it ORs param_2 into the IE register (+0x54). Bits 0-2, 3-5, 6-8, 9-12, 13-15, 16-17 and 18-23 of param_2 form seven groups matching the seven ILS bits: for each group with a bit set, ILE bit 0 is set when that ILS bit is clear and ILE bit 1 when it is set, enabling interrupt line 0 or 1. Bit 7 of param_2 ORs param_3 (buffer mask) into TXBTIE and bit 8 into TXBCIE. Returns 0 on success.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `ptr` | param_1, FDCAN handle |
| `ie_mask` | `u32` | param_2, interrupt sources to enable (IE bits); bits 7 and 8 also select buffer-level enables |
| `buffer_mask` | `u32` | param_3, Tx buffer bits written to TXBTIE/TXBCIE when bits 7/8 are set |

**Returns** `u32`: 0 on success, 1 when the state is not READY or BUSY

**Notes:** Named after the ST HAL routine by its role (state check, IE register, ILS/ILE routing). The bit-to-group mapping and the bit 7/8 buffer-mask encoding are read from this code, not from ST flag definitions, so verify before relying on the exact flag meanings.

- Addresses by version: 4130: 0x080014CC, 4139: 0x080014CC, 4148: 0x080014CC, 4168: 0x080014CC
- Called by: `bms_fdcan_filters_start`
- Confidence: medium

## HAL_FDCAN_AddMessageToTxFifoQ

**Writes one frame into the next Tx FIFO slot in message RAM and requests transmission**

Requires state BUSY (2), else sets error 0x8. Returns error 0x200 when the TXFQS queue-full flag is set. The put index comes from TXFQS bits 16-17, and the 0x48-byte element is written at handle+0x54 + index*0x48: T0 holds the identifier (standard IDs shifted to bits 18-28, extended IDs with XTD bit 30), RTR and ESI from pre-shifted header words; T1 holds the message marker (bits 24-31), EFC, FDF, BRS and DLC<<16. The payload is packed four bytes at a time into little-endian words, reading whole words from the payload pointer even when the DLC length is not a multiple of 4, with the length taken from the table at flash 0x08010A14. Finally TXBAR is set to 1<<index to request sending, the same mask is stored at handle+0x58, and 0 is returned.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `ptr` | param_1, FDCAN handle |
| `header` | `ptr` | param_2, 9-word Tx header: identifier, id type, frame type, DLC<<16, ESI, BRS, FDF, EFC, message marker (HAL FDCAN_TxHeaderTypeDef order) |
| `data` | `ptr` | param_3, payload bytes |

**Returns** `u32`: 0 on success, 1 on bad state or full queue

**Notes:** Name follows the ST HAL routine from its behaviour and header layout. Only put-index bits 16-17 are used, so this build supports at most four Tx queue slots. The table at 0x08010A14 is the DLC-to-length map (0..8 bytes, then 12, 16, 20, 24, 32, 48, 64).

- Addresses by version: 4130: 0x080015C4, 4139: 0x080015C4, 4148: 0x080015C4, 4168: 0x080015C4
- Called by: `bms_fdcan_send_frame`
- Confidence: high

## HAL_FDCAN_ConfigFilter

**Writes one standard or extended acceptance filter element into message RAM**

Accepts state READY or BUSY, else sets error 0x2. The filter descriptor (IdType, FilterIndex, FilterType, FilterConfig, FilterID1, FilterID2, in that order) selects the element. A standard filter (IdType 0) writes one word at the standard-filter RAM base (handle+0x40) + index*4, with SFID2 in bits 0-10, SFEC in bits 27-29, SFT in bits 30-31 and SFID1 in bits 16-26. Otherwise it writes two words at the extended-filter RAM base (handle+0x44) + index*8: EFID1 with EFEC in bits 29-31, then EFID2 with EFT in bits 30-31. The index is not range-checked, and the function returns 0 on success.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `ptr` | param_1, FDCAN handle |
| `filter` | `ptr` | param_2, 6-word filter descriptor (HAL FDCAN_FilterTypeDef order) |

**Returns** `u32`: 0 on success, 1 on bad state

**Notes:** Name follows the ST HAL routine from its behaviour and descriptor layout.

- Addresses by version: 4130: 0x0800168C, 4139: 0x0800168C, 4148: 0x0800168C, 4168: 0x0800168C
- Called by: `bms_fdcan_add_mask_filter`
- Confidence: high

## HAL_FDCAN_ConfigGlobalFilter

**Sets the global filter (RXGFC) actions for non-matching and remote frames**

Requires state READY (1); otherwise sets error 0x4 and returns 1. It rewrites the low six bits of RXGFC at +0x80: ANFS = param_2 (bits 4-5, non-matching standard frames), ANFE = param_3 (bits 2-3, non-matching extended frames), RRFS = param_4 (bit 1, reject remote standard) and RRFE = param_5 (bit 0, reject remote extended). Bits 6-31 of RXGFC are kept. Returns 0 on success.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `ptr` | param_1, FDCAN handle |
| `non_matching_std` | `u32` | param_2, action code for non-matching standard frames |
| `non_matching_ext` | `u32` | param_3, action code for non-matching extended frames |
| `reject_remote_std` | `u32` | param_4, 1 to reject remote standard frames |
| `reject_remote_ext` | `u32` | param_5, 1 to reject remote extended frames |

**Returns** `u32`: 0 on success, 1 when not READY

**Notes:** Name follows the ST HAL routine from its behaviour.

- Addresses by version: 4130: 0x080016F0, 4139: 0x080016F0, 4148: 0x080016F0, 4168: 0x080016F0
- Called by: `bms_fdcan_filters_start`
- Confidence: high

## HAL_FDCAN_ErrorCallback

**Empty weak FDCAN error callback, invoked by the FDCAN interrupt dispatcher**

The body is a bare return, so the callback does nothing in this image. The FDCAN interrupt dispatcher bms_4168_0800185a calls it at the end of its run whenever the accumulated error code at handle+0x60 is non-zero. The dispatcher sets those error bits from IR flags 0xF10000 (bits 16 and 20-23) and from IR bit 14 (error 0x80). The name follows the ST HAL callback that is called at the same point.

**Notes:** The HAL callback name is inferred from the dispatcher's call position, not from a symbol.

- Addresses by version: 4130: 0x08001754, 4139: 0x08001754, 4148: 0x08001754, 4168: 0x08001754
- Called by: `bms_4168_0800185a`
- Confidence: medium

## HAL_FDCAN_GetRxMessage

**Reads one received frame from RX FIFO0 or FIFO1 and releases its element**

Requires state BUSY (else error 0x8). RxLocation 0x40 selects FIFO0 and any other value selects FIFO1. If the FIFO fill level (RXF0S or RXF1S bits 0-3) is zero it returns error 0x100. Otherwise it takes the get index (bits 8-9) and reads the 0x48-byte element at handle+0x48 (FIFO0) or handle+0x4C (FIFO1) plus index*0x48. The header words are split into identifier, id type (raw bit 30), RTR (raw bit 29), ESI (raw bit 31), DLC (bits 16-19, kept shifted), BRS and FDF (raw bits 20 and 21), a 16-bit receive timestamp, the filter index (bits 24-30) and the matching-frame flag (bit 31). It then copies the DLC-sized payload from element+8, writes the get index to RXF0A (0x94) or RXF1A (0x9C) to release the element, and returns 0.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `ptr` | param_1, FDCAN handle |
| `rx_location` | `u32` | param_2, 0x40 for FIFO0, otherwise FIFO1 |
| `header` | `ptr` | param_3, output array of 10 words (HAL FDCAN_RxHeaderTypeDef order) |
| `data` | `ptr` | param_4, output payload buffer |

**Returns** `u32`: 0 on success, 1 on bad state or empty FIFO

**Notes:** Name follows the ST HAL routine from its behaviour and header layout. Header fields keep their raw bit positions, so id type and flags are not normalised to 0/1.

- Addresses by version: 4130: 0x08001758, 4139: 0x08001758, 4148: 0x08001758, 4168: 0x08001758
- Called by: `bms_4168_08001c90`
- Confidence: high

## HAL_FDCAN_GetTxFifoFreeLevel

**Returns the Tx FIFO free level from TXFQS, masked to bits 0-2**

Returns TXFQS & 7, the TFFL free-entry count. The mask keeps only three bits, although the field is six bits wide, so the result is correct only for queues of up to seven entries. It is a pure register read with no side effects. Its caller bms_4168_08008bfc is outside this packet.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `ptr` | param_1, FDCAN handle |

**Returns** `u32`: free Tx FIFO entries (0..7 as masked)

**Notes:** The narrow mask is probably deliberate given the four-slot queue seen in HAL_FDCAN_AddMessageToTxFifoQ, but that is not confirmed.

- Addresses by version: 4130: 0x0800184C, 4139: 0x0800184C, 4148: 0x0800184C, 4168: 0x0800184C
- Called by: `bms_fdcan_tx_fifo_full`
- Confidence: high

## HAL_FDCAN_Start

**Starts FDCAN: requires READY, clears CCCR.INIT and moves the state to BUSY**

Requires state READY (1); otherwise sets error 0x4 and returns 1. On success it sets the state to BUSY (2), clears CCCR bit 0 (INIT) so the node joins the bus, clears the error code at +0x60 and returns 0. The function does not poll for INIT to clear, since the decompile has no wait loop.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `ptr` | param_1, FDCAN handle |

**Returns** `u32`: 0 on success, 1 when not READY

**Notes:** Name follows the ST HAL routine from its behaviour.

- Addresses by version: 4130: 0x08001CF6, 4139: 0x08001CF6, 4148: 0x08001CF6, 4168: 0x08001CF6
- Called by: `bms_fdcan_filters_start`
- Confidence: high

## HAL_FDCAN_Stop

**Stops FDCAN: sets CCCR.INIT, handles clock-stop acknowledge, re-enables configuration change**

Requires state BUSY (else error 0x8). It sets CCCR.INIT (bit 0) and polls about 11 times for hardware to acknowledge it, then clears CCCR.CSR (bit 4, clock-stop request) and polls CSA (bit 3) for about 11 more iterations. A timeout in either loop sets error 0x1, moves the state to ERROR (3) and returns 1. On success it sets CCCR.CCE (bit 1), clears the Tx request mask at handle+0x58, sets the state to READY (1) and returns 0.

| Parameter | Type | Description |
|---|---|---|
| `handle` | `ptr` | param_1, FDCAN handle |

**Returns** `u32`: 0 on success, 1 on bad state or timeout

**Notes:** Its caller bms_4168_08001732 calls this and then clears interrupt line enables ILE bits 0-1, sets the error code to 0 and the state to RESET, which looks like HAL_FDCAN_DeInit.

- Addresses by version: 4130: 0x08001D22, 4139: 0x08001D22, 4148: 0x08001D22, 4168: 0x08001D22
- Called by: `bms_4168_08001732`
- Confidence: high

## bms_can_pack_ext_frame

**Pack a 29-bit extended CAN frame (ID, DLC, 3 header bytes, payload) into a TX buffer**

Writes one extended-identifier frame into the buffer at param_9. The 32-bit identifier word becomes ((param_1 << 26) | (param_4 << 8) | param_3) & 0x1FFFFFFF, ORed with 0xEF0000 and with bit 29 (0x20000000), and bit 31 of the old word is kept. Byte 4 is set to param_8 + 3, which counts three header bytes (param_2, param_5 and param_6 at bytes 5 to 7) plus param_8 payload bytes copied from param_7 to bytes 8 onward. It returns 1 on success; if param_7 or param_9 is null, param_8 is 6 or more, or param_1 is 8 or more, it returns 0 with nothing written. The priority in bits 26 to 28 and the fixed 0xEF byte in bits 16 to 23 match a J1939-style 29-bit identifier, which is an inference from the constants.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | priority, 0 to 7, placed in identifier bits 26 to 28 |
| `param_2` | `u8` | header byte, written to data byte 0 (offset 5) |
| `param_3` | `u32` | identifier term ORed in unshifted; not limited to 8 bits |
| `param_4` | `u32` | identifier term shifted left 8 (bits 8 to 15) |
| `param_5` | `u8` | header byte, written to data byte 1 (offset 6) |
| `param_6` | `u8` | header byte, written to data byte 2 (offset 7) |
| `param_7` | `ptr` | payload source, at least param_8 bytes |
| `param_8` | `u32` | payload length, 0 to 5 |
| `param_9` | `ptr` | TX buffer element: word 0 identifier, byte 4 length, bytes 5 to 12 data |

**Returns** `u32`: 1 when the frame was packed, 0 when a check fails

**Notes:** Byte 4 holds a length (payload + 3), not the FDCAN T1 DLC field, so this is a custom or simplified buffer layout. The meanings of identifier bit 29 and bit 31 are not confirmed. The J1939 reading is inferred from the constants and has not been checked against a real message from the image. param_3 is not limited to 8 bits, so values of 256 or more overlap param_4's field.

- Addresses by version: 4130: 0x0800E7FA, 4139: 0x0800EE4E, 4148: 0x080100B0, 4168: 0x080105FC
- Called by: `bms_4168_0800e9dc`, `bms_4168_0800ec04`, `bms_4168_0800f2e0`, `bms_4168_0800f8e0`
- Confidence: medium

## bms_fdcan_add_mask_filter

**Add one FDCAN mask filter to RX FIFO 0, resetting the MCU if HAL rejects it**

Builds a HAL_FDCAN_FilterTypeDef on the stack with IdType from param_2, FilterIndex from param_3, FilterType set to MASK (2), FilterConfig set to store matches in RX FIFO 0 (1), FilterID1 from param_4 and FilterID2 from param_5 used as the mask. It then calls HAL_FDCAN_ConfigFilter on the handle in param_1. A nonzero status calls NVIC_SystemReset, so a rejected filter restarts the board. It is called five times by bms_4168_08008ca0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | FDCAN handle (0x20005C50 in the caller) |
| `param_2` | `u32` | ID type: 0 standard, 0x40000000 extended |
| `param_3` | `u32` | filter index |
| `param_4` | `u32` | FilterID1, the identifier to match |
| `param_5` | `u32` | FilterID2, the mask |

- Addresses by version: 4130: 0x08007C18, 4139: 0x08008118, 4148: 0x08008964, 4168: 0x08008C64
- Called by: `bms_fdcan_filters_start`
- Calls: `NVIC_SystemReset`, `HAL_FDCAN_ConfigFilter`
- Confidence: high

## bms_fdcan_cb_ir_100

**Empty FDCAN callback for IR flag 0x100 (bit 8), receives the cancelled-buffer mask**

The body is a bare return. The FDCAN dispatcher bms_4168_0800185a calls it when IR and IE have bit 8 (0x100) set, passing TXBCF AND TXBCIE, which are the Tx buffers whose cancellation finished and whose interrupt is enabled. It writes 0x100 back to IR first. In ST HAL terms this is the Tx buffer abort callback, but the bit-8 meaning differs from the RM0444 numbering (HPM), so the mapping is unverified.

**Notes:** The mask argument comes from the dispatcher; the empty body ignores it. The probable ST callback is HAL_FDCAN_TxBufferAbortCallback.

- Addresses by version: 4130: 0x08001DB2, 4139: 0x08001DB2, 4148: 0x08001DB2, 4168: 0x08001DB2
- Called by: `bms_4168_0800185a`
- Confidence: medium

## bms_fdcan_cb_ir_1c00

**Empty FDCAN interrupt hook for IR flags 0x1C00 (bits 10-12)**

The body is a bare return. The FDCAN dispatcher bms_4168_0800185a calls it with IR AND IE AND 0x1C00 after writing those bits back to IR. In RM0444 numbering bits 10-12 are TCF, TFE and TEFN (transmission cancelled, Tx FIFO empty, TX event FIFO new entry), which is the likely meaning and is not verified.

**Notes:** The dispatcher passes the masked flags as an argument that this empty body ignores.

- Addresses by version: 4130: 0x08001DB6, 4139: 0x08001DB6, 4148: 0x08001DB6, 4168: 0x08001DB6
- Called by: `bms_4168_0800185a`
- Confidence: medium

## bms_fdcan_cb_ir_200

**Empty FDCAN interrupt hook for IR flag 0x200 (bit 9)**

The body is a bare return. The FDCAN dispatcher bms_4168_0800185a calls it when both IR and IE have bit 9 (0x200) set, after clearing the bit through IR. In RM0444 numbering bit 9 is TC (transmission completed), which is the likely meaning and is not verified.

- Addresses by version: 4130: 0x08001DB8, 4139: 0x08001DB8, 4148: 0x08001DB8, 4168: 0x08001DB8
- Called by: `bms_4168_0800185a`
- Confidence: medium

## bms_fdcan_cb_ir_2000

**Empty FDCAN interrupt hook for IR flag 0x2000 (bit 13)**

The body is a bare return. The FDCAN dispatcher bms_4168_0800185a calls it when both IR and IE have bit 13 (0x2000) set, after clearing the bit through IR. In RM0444 numbering bit 13 is TEFW (TX event FIFO watermark), which is the likely meaning and is not verified.

- Addresses by version: 4130: 0x08001DB0, 4139: 0x08001DB0, 4148: 0x08001DB0, 4168: 0x08001DB0
- Called by: `bms_4168_0800185a`
- Confidence: medium

## bms_fdcan_cb_ir_38

**Empty FDCAN interrupt hook for IR flags 0x38 (bits 3-5)**

The body is a bare return. The FDCAN dispatcher bms_4168_0800185a calls it with the masked IR/IE value for bits 3-5 (0x38) after clearing those IR bits. In RM0444 numbering this group is RF0L, RF1N and RF1W (FIFO0 message lost, FIFO1 new message, FIFO1 watermark), which is the likely meaning and is not verified.

- Addresses by version: 4130: 0x08001CF4, 4139: 0x08001CF4, 4148: 0x08001CF4, 4168: 0x08001CF4
- Called by: `bms_4168_0800185a`
- Confidence: medium

## bms_fdcan_cb_ir_40

**Empty FDCAN interrupt hook for IR flag 0x40 (bit 6)**

The body is a bare return. The FDCAN dispatcher bms_4168_0800185a calls it when both IR and IE have bit 6 (0x40) set, after writing 0x40 back to IR to clear it. In the RM0444 numbering bit 6 is RF1F (RX FIFO 1 full), which is the likely meaning, but this image's IR layout is not verified.

- Addresses by version: 4130: 0x08001858, 4139: 0x08001858, 4148: 0x08001858, 4168: 0x08001858
- Called by: `bms_4168_0800185a`
- Confidence: medium

## bms_fdcan_cb_ir_80

**Empty FDCAN callback for IR flag 0x80 (bit 7), receives the completed-buffer mask**

The body is a bare return. The FDCAN dispatcher bms_4168_0800185a calls it when IR and IE have bit 7 (0x80) set, passing TXBTO AND TXBTIE, the Tx buffers that finished transmitting with their interrupt enabled. It writes 0x80 back to IR first. This matches the ST HAL Tx buffer completion callback, but the bit-7 meaning is taken from the dispatcher's use only.

**Notes:** The mask argument is ignored by the empty body. The probable ST callback is HAL_FDCAN_TxBufferCompleteCallback.

- Addresses by version: 4130: 0x08001DB4, 4139: 0x08001DB4, 4148: 0x08001DB4, 4168: 0x08001DB4
- Called by: `bms_4168_0800185a`
- Confidence: medium

## bms_fdcan_cb_ir_8000

**Empty FDCAN interrupt hook for IR flag 0x8000 (bit 15)**

The body is a bare return. The FDCAN dispatcher bms_4168_0800185a calls it when both IR and IE have bit 15 (0x8000) set, after writing that bit back to IR to clear it. In RM0444 numbering bit 15 is TEFL (TX event FIFO element lost), which is the likely meaning and is not verified.

- Addresses by version: 4130: 0x08001DAE, 4139: 0x08001DAE, 4148: 0x08001DAE, 4168: 0x08001DAE
- Called by: `bms_4168_0800185a`
- Confidence: medium

## bms_fdcan_cb_ir_e0000

**Empty FDCAN interrupt hook for IR bits 17-19 (mask 0xE0000)**

The body is a bare return. The FDCAN dispatcher bms_4168_0800185a calls it with the masked IR/IE flags for bits 17-19 (0xE0000) after writing those bits back to IR to clear them. The name is derived from the mask; the RM0444 numbering for these bits (MRAF, TOO, DRX) is the likely meaning and is not verified against this image.

**Notes:** Probably a HAL error-status or timeout callback. The dispatcher passes the flag mask as an argument that this empty body ignores.

- Addresses by version: 4130: 0x08001756, 4139: 0x08001756, 4148: 0x08001756, 4168: 0x08001756
- Called by: `bms_4168_0800185a`
- Confidence: medium

## bms_fdcan_filters_start

**Set up FDCAN1 filters, reject unmatched frames, start FDCAN and enable RX FIFO 0 interrupts**

Installs five mask filters through bms_fdcan_add_mask_filter: extended IDs 0x070000 with mask 0x3F0000 (index 0) and 0xEB0000 with mask 0xF80000 (index 4), and standard IDs 0x7F0 with mask 0xFFE (index 1), 0x720 exact (index 2) and 0x212 exact (index 3). HAL_FDCAN_ConfigGlobalFilter then rejects non-matching standard and extended frames and sends remote frames to the filters instead of rejecting them. HAL_FDCAN_Start starts the peripheral, and HAL_FDCAN_ActivateNotification enables the RX FIFO 0 new-message interrupt, routed to interrupt line 0. Each HAL failure calls NVIC_SystemReset.

**Notes:** The meaning of the IDs (which message IDs these are) is not established in this packet.

- Addresses by version: 4130: 0x08007C54, 4139: 0x08008154, 4148: 0x080089A0, 4168: 0x08008CA0
- Peripheral registers: `TIM2.CR1` (A)
- Called by: `bms_4168_080082bc`, `bms_4168_080082f0`
- Calls: `NVIC_SystemReset`, `HAL_FDCAN_ActivateNotification`, `HAL_FDCAN_ConfigGlobalFilter`, `HAL_FDCAN_Start`, `bms_fdcan_add_mask_filter`
- Confidence: high

## bms_fdcan_send_frame

**Build an FDCAN Tx header from a frame record and queue it in the Tx FIFO**

Reads a frame record at param_1: the 16-bit byte count at +0 becomes DataLength (count shifted left 16 in the header word at 0x20005CC0), a nonzero 32-bit word at +4 sets IdType to extended (0x40000000 at 0x20005CB8), a nonzero word at +8 sets TxFrameType to remote (0x20000000 at 0x20005CBC), and the 32-bit word at +12 becomes Identifier at 0x20005CB4. The remaining header fields at 0x20005CC4 to 0x20005CD4 are cleared and the payload starts at +16 of the record. HAL_FDCAN_AddMessageToTxFifoQ queues the frame on the handle at 0x20005C50, and the function returns true when HAL accepts it.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | frame record: byte count at +0, extended flag at +4, remote flag at +8, identifier at +12, payload from +16 |

**Returns** `bool`: true when HAL_FDCAN_AddMessageToTxFifoQ succeeded

**Notes:** The header layout is inferred from the staging addresses 0x20005CB4 to 0x20005CD4 and the HAL field order. The flag values match HAL constants as read from the code.

- Addresses by version: 4130: 0x08007BC8, 4139: 0x080080C8, 4148: 0x08008914, 4168: 0x08008C14
- Peripheral registers: `TIM2.CR1` (A)
- Called by: `bms_4168_0800b9a8`, `bms_4168_0800b9f2`
- Calls: `HAL_FDCAN_AddMessageToTxFifoQ`
- Confidence: medium

## bms_fdcan_tx_fifo_full

**Return 1 when the FDCAN1 Tx FIFO has no free element, else 0**

Calls HAL_FDCAN_GetTxFifoFreeLevel on the FDCAN handle at 0x20005C50 and returns 0 when the free level is nonzero, otherwise 1. Its callers are bms_4168_0800b9a8 and bms_4168_0800b9f2, which are the transmit paths, so a return of 1 means the FIFO is full.

**Returns** `bool`: true when the Tx FIFO has no free element

- Addresses by version: 4130: 0x08007BB0, 4139: 0x080080B0, 4148: 0x080088FC, 4168: 0x08008BFC
- Called by: `bms_4168_0800b9a8`, `bms_4168_0800b9f2`
- Calls: `HAL_FDCAN_GetTxFifoFreeLevel`
- Confidence: high

## fdcan2_is_bus_off

**Return 1 when FDCAN2 is bus-off (FDCAN_PSR.BO set)**

Reads FDCAN2.FDCAN_PSR (0x40006844, offset 0x44 from the FDCAN2 block at 0x40006800) and returns 1 when bit 7, the BO (bus-off) status flag, is set, otherwise 0. It is read-only and has no side effects. The only caller in the packet is bms_4168_080082f0.

**Returns** `bool`: true when the FDCAN2 protocol status reports bus-off

**Notes:** The PSR bit layout is from the standard FDCAN register map; the FDCAN2 base is inferred from the address.

- Addresses by version: 4130: 0x08007C40, 4139: 0x08008140, 4148: 0x0800898C, 4168: 0x08008C8C
- Peripheral registers: `FDCAN2.FDCAN_PSR` (R)
- Called by: `bms_4168_080082f0`
- Confidence: high
