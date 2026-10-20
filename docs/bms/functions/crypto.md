# BMS - `crypto` functions

1 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_seed_key_transform`](#bms_seed_key_transform) | 0x080106C8 | Derive a 16-byte output block from a 16-byte input with a CRC-keyed S-box and column rotations |

## bms_seed_key_transform

**Derive a 16-byte output block from a 16-byte input with a CRC-keyed S-box and column rotations**

Transforms a 16-byte input at param_2 into a 16-byte output at param_1. It computes the CRC-16/USB of the input through crc16_usb_compute and stores it in DAT_200005B8, then XORs the CRC with the byte sum of the input and stores that in DAT_200005BA, taking 2-bit selectors from the mixed value. The input is XORed with a 16-byte constant at 0x08010888, and each byte is then substituted by two nibble lookups in a 64-byte table at 0x08010848 whose rows are chosen by the selectors. The 16 bytes form four 4-byte columns, each rotated by a selector through bms_rotate_word_bytes, and written to the output column by column. The routine reads only flash constants and writes only the output buffer and the two RAM words above.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 16-byte output buffer, written as four 4-byte columns |
| `param_2` | `ptr` | 16-byte input block |

**Notes:** The purpose is not established. It could be a seed-to-key or challenge-response transform, but the routine itself only maps bytes. Its caller bms_4168_08004fec is not in this packet, so the use of the output is unknown.

- Addresses by version: 4130: 0x0800E8C8, 4139: 0x0800EF1C, 4148: 0x0801017C, 4168: 0x080106C8
- Called by: `bms_auth_verify_response`
- Calls: `bms_rotate_word_bytes`, `crc16_usb_compute`
- Confidence: medium
