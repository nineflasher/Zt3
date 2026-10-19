# MCU - `crypto` functions

1 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_tea_decrypt_block`](#mcu_tea_decrypt_block) | (removed) | TEA decryption of one 64-bit block in place: 32 rounds, delta 0x9E3779B9 |

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
