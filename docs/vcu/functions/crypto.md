# VCU - `crypto` functions

7 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`crc32_ieee_calc`](#crc32_ieee_calc) | 0x0800EF70 | Bitwise CRC-32 (IEEE 802.3, poly 0xEDB88320) over a byte buffer |
| [`vcu_crypto_key_load`](#vcu_crypto_key_load) | 0x08006538 | Load the 16-byte key at RAM 0x200020DC from flash 0x08001440, or the built-in default |
| [`vcu_crypto_state_clear`](#vcu_crypto_state_clear) | (removed) | Zero 18 bytes of key RAM from 0x200020E4, overlapping the last 8 bytes of the key |
| [`vcu_tea_decrypt_block`](#vcu_tea_decrypt_block) | (removed) | TEA decryption of one 64-bit block with a 128-bit key (32 rounds) |
| [`vcu_xtea_decrypt_inplace`](#vcu_xtea_decrypt_inplace) | 0x0800DC64 | XTEA-decrypt one 8-byte block in place with a four-word key, 32 rounds |
| [`vcu_xtea_decrypt_with_key_at`](#vcu_xtea_decrypt_with_key_at) | 0x0800DCD8 | Load a key from memory and XTEA-decrypt the block at a pointer argument |
| [`vcu_xtea_key_load`](#vcu_xtea_key_load) | 0x0800DA0C | Load a 128-bit XTEA key as four little-endian u32 words from memory |

## crc32_ieee_calc

**Bitwise CRC-32 (IEEE 802.3, poly 0xEDB88320) over a byte buffer**

Standard reflected CRC-32 as used by zlib/PNG/Ethernet: starts with 0xFFFFFFFF, XORs each byte into the low bits, then shifts right 8 times applying the polynomial 0xEDB88320 when the low bit is set, and returns the bit-inverted result. No lookup table and does not use the hardware CRC peripheral. Called from vcu_0159_080054ec, likely to verify a stored/received data block (e.g. flash configuration or update image); that purpose is inferred from the caller only.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | buffer to checksum |
| `param_2` | `u32` | length in bytes |

**Returns** `u32`: CRC-32 value (check value for '123456789' is 0xCBF43926)

- Addresses by version: 148: 0x0800DF4C, 14a: 0x0800E3E8, 14b: 0x0800E878, 14e: 0x0800E918, 14f: 0x0800EA64, 152: 0x0800ED0C, 153: 0x0800EE00, 0159: 0x0800EF70
- Called by: `vcu_0159_080054ec`
- Confidence: high

## vcu_crypto_key_load

**Load the 16-byte key at RAM 0x200020DC from flash 0x08001440, or the built-in default**

Clears a block of RAM variables at 0x20001490 to 0x200014b8 (the byte and word values listed in the packet), then compares the built-in 16-byte default key, a constant on the stack, with the 16 bytes at flash 0x08001440 using util_mem_equal. If they match, it copies the default into RAM at 0x200020DC and sets DAT_20001495 to 1; otherwise it copies the flash bytes to 0x200020DC with __aeabi_memcpy and leaves DAT_20001495 at 0. The 128-bit value at 0x200020DC is probably the TEA key used by vcu_153_08006490 (not confirmed in this packet).

**Returns** `u64`: leftover value of the stack copy of the default key (its first 8 bytes); not a meaningful result

**Notes:** The key bytes are deliberately not recorded here. DAT_20001495 = 1 means the default key is in use.

- Addresses by version: 148: 0x08005A90, 14a: 0x08005EB0, 14b: 0x08006208, 14e: 0x08006240, 14f: 0x0800629C, 152: 0x0800631C, 153: 0x080063B8, 0159: 0x08006538
- Called by: `vcu_0159_080060b8`, `vcu_0159_08006184`
- Calls: `__aeabi_memcpy`, `util_mem_equal`
- Confidence: medium

## vcu_crypto_state_clear

**Zero 18 bytes of key RAM from 0x200020E4, overlapping the last 8 bytes of the key**

Calls the zero-fill helper vcu_0159_08001240 (memclr style) for 0x12 bytes at 0x200020E4. That range covers the last 8 bytes of the 16-byte key at 0x200020DC that vcu_crypto_key_load writes, plus 10 bytes after it, so it is probably the key wipe after a decryption step.

**Notes:** The present-in list covers builds 148 to 14f only, so this is probably specific to those builds. The zero-fill helper vcu_0159_08001240 is not described yet; its description in wave 1 is an inference.

- Addresses by version: 148: 0x08005E04, 14a: 0x08006224, 14b: 0x08006594, 14e: 0x080065CC, 14f: 0x08006628
- Called by: `vcu_0159_080047ac`
- Calls: `vcu_buf_zero`
- Confidence: medium

## vcu_tea_decrypt_block

**TEA decryption of one 64-bit block with a 128-bit key (32 rounds)**

Tiny Encryption Algorithm decrypt: v0 = param_1[0], v1 = param_1[1], sum starts at 0xC6EF3720 (= 32 * delta, delta 0x9E3779B9; the code adds 0x61C88647 each round, i.e. subtracts delta). Each of 32 rounds does v1 -= ((v0<<4)+k[2]) ^ (v0+sum) ^ ((v0>>5)+k[3]) then v0 -= ((v1<<4)+k[0]) ^ (v1+sum) ^ ((v1>>5)+k[1]). The result is written back in place. No direct callers in the image (called indirectly or the call was optimised away); not present in the 0159 build.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pointer to two u32 words (the 8-byte block, decrypted in place) |
| `param_2` | `ptr` | pointer to four u32 key words |

**Notes:** Plain TEA (not XTEA): the key index is fixed per half-round, no key schedule on sum. What data it protects is not known from this function.

- Addresses by version: 148: 0x08005B68, 14a: 0x08005F88, 14b: 0x080062E0, 14e: 0x08006318, 14f: 0x08006374, 152: 0x080063F4, 153: 0x08006490
- Called by: `vcu_0159_08006184`
- Confidence: high

## vcu_xtea_decrypt_inplace

**XTEA-decrypt one 8-byte block in place with a four-word key, 32 rounds**

Decrypts the 64-bit block at param_1 in place. It loads the two words with util_load_u32_le, starts with sum 0xC6EF3720 (32 times the delta 0x9E3779B9) and runs 32 rounds of the XTEA decryption schedule: v1 -= (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + key[(sum >> 11) & 3]); then sum -= delta; then v0 -= (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + key[sum & 3]). Both words are stored back with util_store_u32_le (vcu_0159_0800dc54). No alignment is needed.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 8-byte block, decrypted in place |
| `param_2` | `ptr` | four u32 key words |

**Notes:** This is XTEA, not plain TEA. It looks like the same routine as vcu_tea_decrypt_block (vcu_153_08006490, wave 1), but that was not compared here; this family exists only in VCU_0159, so the two are kept as separate families until shown to match.

- Addresses by version: 0159: 0x0800DC64
- Called by: `vcu_xtea_decrypt_with_key_at`
- Calls: `util_load_u32_le`, `util_store_u32_le`
- Confidence: high

## vcu_xtea_decrypt_with_key_at

**Load a key from memory and XTEA-decrypt the block at a pointer argument**

Loads the 16-byte key at param_2 into a local four-word array with vcu_xtea_key_load (vcu_0159_0800da0c), then XTEA-decrypts the 8-byte block at param_1 in place with that array (vcu_xtea_decrypt_inplace, vcu_0159_0800dc64). The other two arguments are copied into the same local array before the load, so the load overwrites them and they have no effect. The 64-bit return value is the first two words of that array after the load, not the decrypted block as far as the code shows. Called from vcu_0159_08006184 (not described in this packet).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 8-byte block to decrypt in place |
| `param_2` | `ptr` | 16-byte key in memory |
| `param_3` | `u32` | copied into the local key array and overwritten by the load |
| `param_4` | `u32` | copied into the local key array and overwritten by the load |

**Returns** `u64`: first two words of the local key array after the load

**Notes:** The return value looks wrong for a decrypt routine. Check the caller at vcu_0159_08006184 before relying on the result.

- Addresses by version: 0159: 0x0800DCD8
- Called by: `vcu_0159_08006184`
- Calls: `vcu_xtea_key_load`, `vcu_xtea_decrypt_inplace`
- Confidence: medium

## vcu_xtea_key_load

**Load a 128-bit XTEA key as four little-endian u32 words from memory**

Reads four consecutive 32-bit little-endian words from the 16 bytes at param_1 with util_load_u32_le (vcu_0159_0800da38) and stores them in the four-word array at param_2. It does not check for null pointers. Used by vcu_xtea_decrypt_with_key_at (vcu_0159_0800dcd8).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 16-byte key in memory |
| `param_2` | `ptr` | output array of four u32 key words |

- Addresses by version: 0159: 0x0800DA0C
- Called by: `vcu_xtea_decrypt_with_key_at`
- Calls: `util_load_u32_le`
- Confidence: high
