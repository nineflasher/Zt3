# MCU - `crypto` functions

5 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_auth_key16_init`](#mcu_auth_key16_init) | (removed) | Clear the 0x200006AC state block and load a 16-byte key from a constant or a fallback |
| [`mcu_tea_decrypt_block`](#mcu_tea_decrypt_block) | (removed) | TEA decryption of one 64-bit block in place: 32 rounds, delta 0x9E3779B9 |
| [`mcu_xtea_decrypt_block`](#mcu_xtea_decrypt_block) | 0x0800D934 | Decrypt one 64-bit XTEA block in place with 32 rounds and a four-word key |
| [`mcu_xtea_decrypt_with_key`](#mcu_xtea_decrypt_with_key) | 0x0800D9A8 | Load a 16-byte XTEA key and decrypt one 64-bit block in place |
| [`mcu_xtea_key_load`](#mcu_xtea_key_load) | 0x0800D674 | Load a 16-byte XTEA key into four little-endian 32-bit words |

## mcu_auth_key16_init

**Clear the 0x200006AC state block and load a 16-byte key from a constant or a fallback**

Clears the state words at 0x200006AC through 0x200006D4, then selects the 16-byte key stored at 0x20002044 through 0x20002050. It compares a hard-coded 16-byte constant with the 16 bytes at flash 0x08001420 using mcu_bytes_equal_n8. The hard-coded constant is stored when the bytes match or when the 16-bit word at 0x20001F54 equals 0x4D43. Otherwise a 16-byte ASCII fallback is stored instead. No caller appears in this packet, so the routine likely runs at startup, and the use of the key is not visible here.

**Notes:** Present in the 12b, 143 and 152 builds. Reading the key as an authentication or identity value is a guess. The constant values are not copied into the documentation.

- Addresses by version: 12b: 0x08006B84, 143: 0x08006A4C, 152: 0x08006A7C
- Called by: `mcu_0160_0800665c`, `mcu_0160_0800672c`
- Calls: `mcu_bytes_equal_n8`
- Confidence: medium

## mcu_tea_decrypt_block

**TEA decryption of one 64-bit block in place: 32 rounds, delta 0x9E3779B9**

Standard TEA decipher. The two words at param_1[0..1] are decrypted in place with the 128-bit key in param_2[0..3]. The round sum starts at 0xC6EF3720 (32 * 0x9E3779B9) and is decremented by 0x9E3779B9 each round for 32 rounds. Each half-update is ((v<<4) + k) ^ (v + sum) ^ ((v>>5) + k'), with key words 2 and 3 for v1 and key words 0 and 1 for v0. Present in the 12b, 143 and 152 builds. There are no direct callers, so it is reached through a pointer or from code outside this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | two u32 words, decrypted in place |
| `param_2` | `ptr` | four u32 key words |

**Notes:** Algorithm is certain. The protocol or storage that uses it is not visible here.

- Addresses by version: 12b: 0x08006C54, 143: 0x08006B28, 152: 0x08006B58
- Called by: `mcu_0160_0800672c`
- Confidence: high

## mcu_xtea_decrypt_block

**Decrypt one 64-bit XTEA block in place with 32 rounds and a four-word key**

Reads the block at param_1 as two little-endian 32-bit words v0 and v1, then runs the 32-round XTEA decryption with delta 0x9E3779B9, starting from sum = 0xC6EF3720 (32 times delta) and subtracting delta each round. In each round v1 is updated with ((v0<<4 ^ v0>>5) + v0) ^ (sum + key[(sum>>11)&3]), sum is decremented by delta, and then v0 is updated with the same mixing function and key[sum&3]. The four key words are read from param_2, and the two result words are written back little-endian to param_1 and param_1+4 through mcu_write_le32. Its delta and round count match mcu_tea_decrypt_block (MCU_152), but the key index depends on sum, which is the XTEA form.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 8-byte block, decrypted in place |
| `param_2` | `ptr` | four u32 key words, as produced by mcu_xtea_key_load |

**Notes:** Check that mcu_tea_decrypt_block (0x08006b58, MCU_152) is not the same routine in a different build, and that the two names are kept separate if they differ.

- Addresses by version: 0160: 0x0800D934
- Called by: `mcu_xtea_decrypt_with_key`
- Calls: `mcu_read_le32`, `mcu_write_le32`
- Confidence: high

## mcu_xtea_decrypt_with_key

**Load a 16-byte XTEA key and decrypt one 64-bit block in place**

Wrapper that copies the 16-byte key at param_2 into a stack array through mcu_xtea_key_load, then decrypts the 8-byte block at param_1 in place through mcu_xtea_decrypt_block. The expanded key stays in the stack frame and is not cleared on return. Its caller mcu_0160_0800672c is not described yet, so the purpose of the decrypted data is unknown.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 8-byte block, decrypted in place |
| `param_2` | `ptr` | 16-byte key |

**Notes:** Leftover key material in the stack frame is a possible concern for a key that is reused.

- Addresses by version: 0160: 0x0800D9A8
- Called by: `mcu_0160_0800672c`
- Calls: `mcu_xtea_key_load`, `mcu_xtea_decrypt_block`
- Confidence: high

## mcu_xtea_key_load

**Load a 16-byte XTEA key into four little-endian 32-bit words**

Copies a 128-bit key from the buffer at param_1 into the four u32 words at param_2, using mcu_read_le32 on the 4-byte groups at offsets 0, 4, 8 and 12 so that the words are key[0]..key[3] in the order XTEA uses. No alignment is required and no key schedule is precomputed. It is the key-preparation step of mcu_xtea_decrypt_with_key, which is its only caller in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 16-byte key, least significant byte of each word first |
| `param_2` | `ptr` | output, four u32 key words |

- Addresses by version: 0160: 0x0800D674
- Called by: `mcu_xtea_decrypt_with_key`
- Calls: `mcu_read_le32`
- Confidence: high
