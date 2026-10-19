# BMS - `protocol` functions

5 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_frame_parse_legacy_4139`](#bms_frame_parse_legacy_4139) | (removed) | Byte-wise parser for the 0x5A/0xA5 framed record packet with CRC-16 check (4130/4139) |
| [`bms_frame_parse_legacy_4168`](#bms_frame_parse_legacy_4168) | 0x08007C10 | Byte-wise 0x5A/0xA5 framed-packet parser with CRC-16 check for the 4148/4168 builds |
| [`bms_frame_rx_byte`](#bms_frame_rx_byte) | 0x0800E128 | Feed one received byte into the 0x5A 0xA5 framed parser; return 1 when a frame checks out |
| [`bms_j1939_tpcm_abort_pack`](#bms_j1939_tpcm_abort_pack) | 0x0801066C | Build a J1939 TP.CM connection-abort frame for PGN 0xEF00 into a TX object |
| [`bms_syscfg_set_ucpd_strobe`](#bms_syscfg_set_ucpd_strobe) | 0x080028A4 | Replaces SYSCFG.CFGR1 bits 9-10 (UCPD1 and UCPD2 strobe) with the supplied value |

## bms_frame_parse_legacy_4139

**Byte-wise parser for the 0x5A/0xA5 framed record packet with CRC-16 check (4130/4139)**

A state machine in DAT_20000114 consumes one received byte per call. A 0x5A or 0xA5 byte starts a frame and is saved at 0x2000083D. The next byte gives the record count N in its high nibble and the first nibble pair of the 16-bit header word at 0x20000124, and the byte after it completes that word; N = 0 jumps straight to the CRC states. The payload of N*4 bytes is appended to the frame buffer at 0x20000A7C (length in DAT_2000011C) and copied to 0x20000AAE. Two CRC bytes, most significant first, are compared with crc16_usb_compute over the header and payload (reflected poly 0x8005, init 0xFFFF, final complement). On a match, N is capped to 63 and each 4-byte record is stored at 0x20000840 with its byte order reversed, then DAT_20000115 and DAT_20000120 are set to 1; the parser returns to idle in every case once the CRC step is reached.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | received byte, low 8 bits used |
| `param_2` | `u32` | unused |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | passed through unchanged as the last argument of crc16_usb_compute |

**Notes:** Header nibble layout is inferred from the shifts and masks, not from a protocol spec. The meaning of the 16-bit word at 0x20000124 beyond its role as CRC seed/state is not established.

- Addresses by version: 4130: 0x08006C08, 4139: 0x08007108
- Called by: `bms_4168_080036d0`
- Calls: `crc16_usb_compute`
- Confidence: medium

## bms_frame_parse_legacy_4168

**Byte-wise 0x5A/0xA5 framed-packet parser with CRC-16 check for the 4148/4168 builds**

The 4148/4168 counterpart of bms_frame_parse_legacy_4139, with the same states, frame layout and CRC step, using the RAM block at 0x200001AC..0x200001BE (state, counts, CRC word at 0x200001BC, header word at 0x200001BE) and the frame buffer at 0x20000B68. While the mode byte at 0x200001AE equals 2 each byte is handed to bms_frame_rx_byte and the function returns. A valid frame rebuilds 4-byte records at 0x2000092C with reversed byte order and sets DAT_200001AD to 1. The state resets to idle after the CRC step in every case.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | received byte, low 8 bits used |
| `param_2` | `u32` | unused |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | passed through unchanged as the last argument of crc16_usb_compute |

**Notes:** Same protocol reading as the 4139 variant, so its uncertainties apply here too.

- Addresses by version: 4148: 0x08007938, 4168: 0x08007C10
- Called by: `bms_4168_080036d0`
- Calls: `crc16_usb_compute`, `bms_frame_rx_byte`
- Confidence: medium

## bms_frame_rx_byte

**Feed one received byte into the 0x5A 0xA5 framed parser; return 1 when a frame checks out**

This is a byte-at-a-time receive state machine. Its state is DAT_2000260e, the write index is DAT_20000610, the remaining payload count is DAT_20000611, the staged checksum is DAT_20000612, the valid-frame flag is DAT_2000260f, and the frame buffer starts at 0x2000256D. The frame layout as parsed is 0x5A, 0xA5, LEN (accepted only when below 0x81), a fixed 0x06, a byte that must equal byte 1 of the descriptor at *(DAT_20002608 + 4), a byte chosen by byte 0 of that descriptor (0x01 or '*' expects 0xAA, 0x02 or ',' expects 0xAC, 0xB5 expects 0xB5, 0x07 to 0x0A expect 0x0B), then LEN+1 payload bytes and a little-endian 16-bit checksum. The checksum is the one's complement of the 16-bit byte sum of frame bytes 2 through LEN+6, and a frame is accepted when (~sum) & 0xFFFF equals the received word. Any mismatch resets the state to 0, and a good checksum sets DAT_2000260f to 1 and returns 1 for the closing byte.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | received byte |

**Returns** `u32`: 1 when this byte completes a frame whose checksum matches, otherwise 0

**Notes:** The frame layout and the checksum range come from the index arithmetic in the decompile. The byte-0 rule table and the meaning of bytes 3 to 5 are read from constants, so the protocol identity and the meaning of the descriptor are inferred. The only caller is bms_4168_08007c10, and its use of the result is not in this packet.

- Addresses by version: 4148: 0x0800DCD4, 4168: 0x0800E128
- Called by: `bms_frame_parse_legacy_4168`
- Confidence: medium

## bms_j1939_tpcm_abort_pack

**Build a J1939 TP.CM connection-abort frame for PGN 0xEF00 into a TX object**

Writes a fixed 8-byte J1939 TP.CM connection-abort frame into the object at param_3 and returns 1, or 0 when param_3 is null. The identifier is (0x1CEC0000 + param_2 * 0x100) | param_1, masked to 29 bits, so the priority is 7, the PGN is 0xEC00 (TP.CM), the destination address is param_2 in bits 8 to 15 and the source address is param_1 in bits 0 to 7; bit 31 of the old word is kept and bit 29 is forced to 1. The DLC is set to 8. The data bytes are 0xFF (the connection-abort control byte), 0xFF (the abort reason), three reserved 0xFF bytes, and then 0x00 0xEF 0x00, which is PGN 0x00EF00 in little-endian order in data bytes 5 to 7.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | source address, identifier bits 0 to 7 |
| `param_2` | `u8` | destination address, identifier bits 8 to 15 |
| `param_3` | `ptr` | TX object: word 0 identifier, byte 4 DLC, bytes 5 to 12 data |

**Returns** `u32`: 1 when the frame was written, 0 when param_3 is null

**Notes:** The protocol identity rests on the constants: 0x1CEC is TP.CM at priority 7, and control byte 0xFF is a connection abort. The reason byte 0xFF is not one of the usual J1939-21 reason codes, so the intent is uncertain. As in bms_can_pack_ext_frame, the handling of bits 29 and 31 is unconfirmed, and param_1 and param_2 are not limited to 8 bits.

- Addresses by version: 4130: 0x0800E86C, 4139: 0x0800EEC0, 4148: 0x08010120, 4168: 0x0801066C
- Called by: `bms_4168_0800ffec`, `bms_4168_08010204`
- Confidence: medium

## bms_syscfg_set_ucpd_strobe

**Replaces SYSCFG.CFGR1 bits 9-10 (UCPD1 and UCPD2 strobe) with the supplied value**

Read-modify-write of SYSCFG CFGR1 that clears bits 9 and 10 (UCPD1_STROBE and UCPD2_STROBE) with mask 0xFFFFF9FF and then ORs in the argument unchanged. The argument is not masked, so a caller that sets any bit outside 9-10 also writes that bit into CFGR1. It is called only from bms_4168_08002234, which is presumably the USB Power Delivery port setup.

| Parameter | Type | Description |
|---|---|---|
| `strobe_bits` | `u32` | value for CFGR1 bits 9-10; should contain nothing else |

**Notes:** The UCPD association comes from the register names in the SVD. The caller's purpose is not visible in this packet.

- Addresses by version: 4130: 0x080028A4, 4139: 0x080028A4, 4148: 0x080028A4, 4168: 0x080028A4
- Peripheral registers: `SYSCFG.CFGR1` (RW)
- Called by: `bms_4168_08002234`
- Confidence: medium
