# BLE - `crypto` functions

85 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`AES_GCM_encrypt_C`](#aes_gcm_encrypt_c) | 0x0C05DE8C | AES-GCM encrypt in CTR mode and produce the auth tag (wolfSSL software path, no arg checks) |
| [`GHASH`](#ghash) | 0x0C05DC2C | GCM GHASH over AAD and ciphertext plus the 64-bit length block, output sSz bytes (wolfSSL) |
| [`GMULT`](#gmult) | 0x0C05D828 | GF(2^128) multiply for GHASH: X = X * Y (bitwise, R = 0xE1) |
| [`GetASNInt`](#getasnint) | 0x0C05E3B8 | Parse a DER INTEGER header and strip a leading 0x00 pad byte (wolfSSL GetASNInt) |
| [`GetLength_ex`](#getlength_ex) | 0x0C05E350 | Parse an ASN.1 DER length field (wolfSSL GetLength_ex) |
| [`aes128_encrypt_block`](#aes128_encrypt_block) | 0x0C048FD4 | AES-128 ECB encrypt of one 16-byte block, in place, using an expanded key |
| [`aes128_key_expansion`](#aes128_key_expansion) | 0x0C048F3C | AES-128 key schedule: expand a 16-byte key into 176 bytes of round keys |
| [`ble_crypto_ccm_cbc_mac`](#ble_crypto_ccm_cbc_mac) | 0x0C049288 | AES-128 CBC-MAC over a packet (CCM B0/B1 style blocks), emitting a 4-byte MIC |
| [`btstack_crypto_ccm_next_block`](#btstack_crypto_ccm_next_block) | 0x0C0645EC | Advance an AES-CCM request to its next 16-byte block, finishing it when done |
| [`crc32_compute_poly`](#crc32_compute_poly) | 0x0C02C454 | CRC-32 (reflected, init/xorout 0xffffffff) of a buffer using a table built for a given polynomial |
| [`crc32_make_table`](#crc32_make_table) | 0x0C02C3FC | Build the 256-entry reflected CRC-32 lookup table for a given polynomial |
| [`crypto_tea_cbc_decrypt`](#crypto_tea_cbc_decrypt) | 0x0C036418 | TEA (32-round) decryption of a buffer in place with CBC-style chaining |
| [`fp_add`](#fp_add) | 0x0C061FE8 | Signed big-integer add c = a + b (wolfSSL TFM fp_add) using s_fp_add / s_fp_sub |
| [`fp_add_d`](#fp_add_d) | 0x0C06428C | Add a single 32-bit digit to a big integer magnitude: c = a + b |
| [`fp_addmod_ct`](#fp_addmod_ct) | 0x0C062654 | Constant-time modular addition d = (a + b) mod c for a, b < c |
| [`fp_clear`](#fp_clear) | 0x0C063FEC | Zero a big integer in place (NULL-safe, no return value) |
| [`fp_cmp`](#fp_cmp) | 0x0C0628B4 | Signed comparison of two big integers |
| [`fp_cmp_mag_ct`](#fp_cmp_mag_ct) | 0x0C061E14 | Constant-time magnitude compare of two fp_int digit arrays |
| [`fp_div_2`](#fp_div_2) | 0x0C0623CC | Halve a big integer b = a / 2 by a one-bit right shift from the top digit down (wolfSSL) |
| [`fp_div_2_mod_ct`](#fp_div_2_mod_ct) | 0x0C062450 | Constant-time modular halving c = (a / 2) mod b for 0 <= a < b (wolfSSL fp_div_2_mod_ct) |
| [`fp_lshd`](#fp_lshd) | 0x0C062D08 | Shift a big integer left by whole 32-bit digits |
| [`fp_mod_2d`](#fp_mod_2d) | 0x0C0624E8 | Big integer modulo a power of two: c = a mod 2^b |
| [`fp_montgomery_calc_normalization`](#fp_montgomery_calc_normalization) | 0x0C062940 | Compute a = R mod b (R = 2^(32*used)) for Montgomery normalisation |
| [`fp_mul_2`](#fp_mul_2) | 0x0C0620DC | Double a big integer b = a * 2 by a one-bit left shift across the digits (wolfSSL fp_mul_2) |
| [`fp_mul_2d`](#fp_mul_2d) | 0x0C062D84 | Multiply a big integer by 2^b: c = a << b |
| [`fp_mul_d`](#fp_mul_d) | 0x0C062168 | Multiply a big integer by a single 32-bit digit: c = a * b |
| [`fp_read_radix`](#fp_read_radix) | 0x0C0642F8 | Parse an ASCII number of radix 2..64 (fast path for hex) into a big integer |
| [`fp_read_unsigned_bin`](#fp_read_unsigned_bin) | 0x0C062BAC | Load a big-endian byte string into a big integer |
| [`fp_rshb`](#fp_rshb) | 0x0C062EA8 | Shift a big integer right by x bits in place |
| [`fp_rshd`](#fp_rshd) | 0x0C062E40 | Shift a big integer right by whole 32-bit digits |
| [`fp_sub`](#fp_sub) | 0x0C062068 | Signed big-integer subtract c = a - b (wolfSSL TFM fp_sub) using s_fp_add / s_fp_sub |
| [`fp_submod_ct`](#fp_submod_ct) | 0x0C0625A0 | Constant-time modular subtraction d = (a - b) mod c for a, b < c |
| [`fp_to_unsigned_bin_at_pos`](#fp_to_unsigned_bin_at_pos) | 0x0C062C20 | Append a big integer's bytes (least significant first) at an offset |
| [`get_digit`](#get_digit) | 0x0C0644C8 | Read digit n of a big integer (0 when out of range) |
| [`get_digit_count`](#get_digit_count) | 0x0C0644C0 | Number of used digits in a big integer (NULL-safe) |
| [`mbedtls_sha1_finish_ret`](#mbedtls_sha1_finish_ret) | 0x0C04A9A8 | mbedTLS SHA-1 finish: pad, append 64-bit big-endian bit length, output the 20-byte digest |
| [`mbedtls_sha1_update_ret`](#mbedtls_sha1_update_ret) | 0x0C04A924 | mbedTLS SHA-1 update: absorb input, running the compression on each full 64-byte block |
| [`md5_encode_le_words`](#md5_encode_le_words) | 0x0C0476D8 | Serialise 32-bit words to little-endian bytes (MD5 'Encode') |
| [`md5_final`](#md5_final) | 0x0C047EFC | MD5 'Final': pad the message, append the bit length and write the 16-byte digest |
| [`md5_init`](#md5_init) | 0x0C047E44 | Initialise an MD5 context |
| [`md5_transform`](#md5_transform) | 0x0C047710 | MD5 compression function: process one 64-byte block into the 4-word state |
| [`md5_update`](#md5_update) | 0x0C047E70 | MD5 'Update': absorb a byte string into the context, compressing full 64-byte blocks |
| [`mp_add_d`](#mp_add_d) | 0x0C0642F4 | Thunk to fp_add_d: add a digit to a big integer |
| [`mp_clear`](#mp_clear) | 0x0C064000 | Release a big integer (empty in this build) |
| [`mp_cmp`](#mp_cmp) | 0x0C0640F8 | Signed comparison of two big integers (mp_cmp wrapper) |
| [`mp_cmp_d`](#mp_cmp_d) | 0x0C064184 | Compare a big integer with a single digit |
| [`mp_cond_copy`](#mp_cond_copy) | 0x0C0644E0 | Constant-time conditional copy of a big integer: if (copy) b = a |
| [`mp_copy`](#mp_copy) | 0x0C064234 | Copy a big integer: b = a |
| [`mp_count_bits`](#mp_count_bits) | 0x0C064268 | Bit length of a big integer |
| [`mp_forcezero`](#mp_forcezero) | 0x0C063FD4 | Zero a big integer (used = 0, sign = +, all 96 digit bytes cleared) |
| [`mp_init`](#mp_init) | 0x0C063FB8 | Initialise a big integer to zero (NULL-safe, returns MP_OKAY) |
| [`mp_init_multi`](#mp_init_multi) | 0x0C064004 | Initialise up to six big integers to zero (NULL entries skipped) |
| [`mp_iszero`](#mp_iszero) | 0x0C06425C | Test whether a big integer is zero |
| [`mp_montgomery_setup`](#mp_montgomery_setup) | 0x0C064458 | Compute the Montgomery constant rho = -1/m mod 2^32 |
| [`mp_read_unsigned_bin`](#mp_read_unsigned_bin) | 0x0C06422C | Thunk to fp_read_unsigned_bin: load big-endian bytes into a big integer |
| [`mp_set`](#mp_set) | 0x0C06449C | Set a big integer to a single digit value |
| [`mp_to_unsigned_bin_len`](#mp_to_unsigned_bin_len) | 0x0C0641F4 | Write a big integer as fixed-length big-endian bytes |
| [`mp_unsigned_bin_size`](#mp_unsigned_bin_size) | 0x0C0641B8 | Number of bytes needed for the big integer's magnitude |
| [`s_fp_add`](#s_fp_add) | 0x0C061E70 | Unsigned big-integer add c = \|a\| + \|b\| on 24-digit TFM fp_ints with carry and clamp |
| [`s_fp_sub`](#s_fp_sub) | 0x0C061F2C | Unsigned big-integer subtract c = \|a\| - \|b\| (\|a\| >= \|b\|) on TFM fp_ints, then clamp |
| [`sha1_ctx_init_with_seed`](#sha1_ctx_init_with_seed) | 0x0C0499F0 | Initialise a SHA-1 style context, optionally loading four state words |
| [`sha1_ctx_set_e_word_one`](#sha1_ctx_set_e_word_one) | 0x0C049A20 | Set the word at offset 0x18 of a context to 1 |
| [`sha1_process_block`](#sha1_process_block) | 0x0C049A28 | SHA-1 compression: process one 64-byte block into the five-word state |
| [`sm_c1_build_t1`](#sm_c1_build_t1) | 0x0C04F30C | Build SMP c1 input t1 = (pres \|\| preq \|\| rat \|\| iat) XOR r at 0x2000FDB4 |
| [`sm_c1_xor_p2`](#sm_c1_xor_p2) | 0x0C04F1EC | XOR the 16-byte value at 0x2000FD94 with SMP c1 p2 (0 \|\| ia \|\| ra) |
| [`wc_AesEncrypt`](#wc_aesencrypt) | 0x0C05D4AC | AES single-block encrypt using the 4 x 1 KB T-tables (wolfSSL wc_AesEncrypt) |
| [`wc_AesFree`](#wc_aesfree) | 0x0C05E34C | Free an Aes context (empty in this build) |
| [`wc_AesGcmDecrypt`](#wc_aesgcmdecrypt) | 0x0C05E2F0 | AES-GCM decrypt: verify the auth tag in constant time, then CTR-decrypt (wolfSSL) |
| [`wc_AesGcmSetKey`](#wc_aesgcmsetkey) | 0x0C05DBE0 | Set a 16-byte AES-GCM key: expand the key and compute the GHASH key H = E_K(0^128) |
| [`wc_AesInit`](#wc_aesinit) | 0x0C05E338 | Initialise an Aes context: store heap pointer (device id unused) |
| [`wc_AesSetKeyLocal`](#wc_aessetkeylocal) | 0x0C05D8F8 | AES-128 key expansion into the Aes context (+ inverse key for decrypt) and IV set (wolfSSL) |
| [`wc_HashFree`](#wc_hashfree) | 0x0C060DAC | Free a wc_HashAlg by type: only SHA-256 (type 6) is built in (wolfSSL wc_HashFree) |
| [`wc_HashGetDigestSize`](#wc_hashgetdigestsize) | 0x0C060CE0 | Digest size in bytes for a wolfSSL hash type |
| [`wc_HashInit`](#wc_hashinit) | 0x0C060D0C | Initialise a wolfSSL hash context for a given hash type (SHA-256 only) |
| [`wc_HmacFree`](#wc_hmacfree) | 0x0C06100C | Free an Hmac context: for macType SHA-256 (6) release the inner hash (wolfSSL wc_HmacFree) |
| [`wc_HmacInit`](#wc_hmacinit) | 0x0C060FEC | Zero a 0x118-byte Hmac context and store its heap pointer (wolfSSL wc_HmacInit) |
| [`wc_InitSha256`](#wc_initsha256) | 0x0C061DB0 | Initialise a SHA-256 context |
| [`wc_RNG_TestSeed`](#wc_rng_testseed) | 0x0C061500 | Continuous test on RNG seed: reject repeated adjacent 4-byte blocks |
| [`wc_Sha256Free`](#wc_sha256free) | 0x0C061E10 | Free a SHA-256 context (empty in this build) |
| [`wc_ecc_copy_point`](#wc_ecc_copy_point) | 0x0C05F1D8 | Copy an ecc_point (x, y, z big integers) into another (wolfSSL wc_ecc_copy_point) |
| [`wc_ecc_curve_free`](#wc_ecc_curve_free) | 0x0C05E4E8 | Clear the loaded curve parameters of an ecc_curve_spec according to its load_mask |
| [`wc_ecc_free`](#wc_ecc_free) | 0x0C0601D0 | Release an ecc_key: clear pubkey.x/y/z and force-zero the private scalar k (wolfSSL) |
| [`wc_ecc_init`](#wc_ecc_init) | 0x0C060190 | Zero a 0x1bc-byte ecc_key and init its pubkey.x/y/z and private scalar k (wolfSSL wc_ecc_init) |
| [`wc_ecc_set_curve`](#wc_ecc_set_curve) | 0x0C05E7FC | Select ECC curve parameters for a key by key size or curve id |
| [`wc_ecc_set_rng`](#wc_ecc_set_rng) | 0x0C060BD4 | Attach a random number generator to an ECC key |

## AES_GCM_encrypt_C

**AES-GCM encrypt in CTR mode and produce the auth tag (wolfSSL software path, no arg checks)**

wolfSSL AES_GCM_encrypt_C(aes, out, in, sz, iv, ivSz, authTag, authTagSz, authIn, authInSz). Counter J0: if ivSz == 12 it is iv || 0x00000001, otherwise GHASH(aes, NULL, 0, iv, ivSz, ctr, 16). A copy of J0 is kept; for each full block the 32-bit big-endian counter in the last 4 bytes is incremented (IncrementGcmCounter), the counter block encrypted with wc_AesEncrypt and XORed with the input (word-wise or byte-wise depending on alignment) into out; a final partial block is handled with a memcpy of sz & 0xf bytes. If authTag is non-NULL the tag is GHASH(aes, authIn, authInSz, out, sz, authTag, authTagSz) XOR E_K(J0). Always returns 0; argument validation is done by the caller 0c05e2c0 (the public wc_AesGcmEncrypt). Companion of wc_AesGcmDecrypt.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Aes context with key schedule and H |
| `param_2` | `ptr` | out: ciphertext |
| `param_3` | `ptr` | plaintext |
| `param_4` | `u32` | plaintext length |
| `param_5` | `ptr` | IV / nonce |
| `param_6` | `u32` | IV length (12 = fast path) |
| `param_7` | `ptr` | out: auth tag (NULL = no tag) |
| `param_8` | `u32` | tag length 1..16 |
| `param_9` | `ptr` | additional authenticated data |
| `param_10` | `u32` | AAD length |

**Returns** `s32`: always 0

- Addresses by version: 219: 0x0C05DE8C
- Called by: `ble_219_0c05e2c0`
- Calls: `wc_AesEncrypt`, `GHASH`, `memcpy`
- Confidence: high

## GHASH

**GCM GHASH over AAD and ciphertext plus the 64-bit length block, output sSz bytes (wolfSSL)**

wolfSSL software GHASH(aes, a, aSz, c, cSz, s, sSz) using the subkey H at aes+0x124 and GMULT per block. Starting from x = 0, each full 16-byte block of the AAD is XORed into x (word-wise when 4-byte aligned, byte-wise otherwise) followed by GMULT(x, H); a trailing partial block is zero-padded first. The same is done for the ciphertext c. Then the length block is built big-endian: [aSz*8 as 64-bit][cSz*8 as 64-bit] (the (len >> 29) << 24 terms carry the high bits), XORed in and multiplied once more, and the first sSz bytes of x are memcpy'd to s. Only a and c may be NULL/empty (skipped). Used by AES_GCM_encrypt_C and wc_AesGcmDecrypt both for the tag and for deriving J0 from a non-12-byte IV.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Aes context; H at +0x124 |
| `param_2` | `ptr` | additional authenticated data (may be NULL) |
| `param_3` | `u32` | AAD length in bytes |
| `param_4` | `ptr` | ciphertext (may be NULL) |
| `param_5` | `u32` | ciphertext length in bytes |
| `param_6` | `ptr` | out: hash result |
| `param_7` | `u32` | bytes of the 16-byte result to copy out |

- Addresses by version: 219: 0x0C05DC2C
- Called by: `AES_GCM_encrypt_C`, `wc_AesGcmDecrypt`
- Calls: `GMULT`, `memcpy`
- Confidence: high

## GMULT

**GF(2^128) multiply for GHASH: X = X * Y (bitwise, R = 0xE1)**

Implements the GCM field multiplication from NIST SP 800-38D in the simple shift-and-add form (wolfSSL's static GMULT). Z starts at 0 and V is a copy of X; for each of the 16 bytes of Y, MSB first, if the bit is set Z ^= V, then V is shifted right by one bit across all 16 bytes and, if the bit shifted out (LSB of byte 15) was 1, byte 0 is XORed with the reduction constant 0xE1. After 128 iterations Z is written back over X. Called from the GHASH block update of the AES-GCM implementation.

| Parameter | Type | Description |
|---|---|---|
| `x` | `ptr` | 16-byte GHASH accumulator, multiplicand and result (in place) |
| `y` | `ptr` | 16-byte multiplier (hash subkey H) |

- Addresses by version: 219: 0x0C05D828
- Called by: `GHASH`
- Confidence: high

## GetASNInt

**Parse a DER INTEGER header and strip a leading 0x00 pad byte (wolfSSL GetASNInt)**

wolfSSL GetASNInt with GetASNHeader inlined. Requires input != NULL, idx+1 <= maxIdx and input[idx] == 0x02 (ASN_INTEGER), then GetLength_ex(input, &idx, &len, maxIdx, check=1). On success *len and *inOutIdx (now pointing at the content) are updated; a negative length is returned as-is. If len > 0, the first content byte is 0x00 and len != 1, the padding zero is skipped (idx+1, len-1) and, if the following byte then has its top bit clear, ASN_PARSE_E is returned because the zero was not needed. Returns 0 on success or ASN_PARSE_E (-140 = -0x8c) on any format error. Caller 0c05e420 (ECDSA signature r/s decoding).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DER input buffer |
| `param_2` | `ptr` | in/out u32 index into the buffer |
| `param_3` | `ptr` | out: s32 length of the integer content |
| `param_4` | `u32` | maximum valid index (buffer size) |

**Returns** `s32`: 0 or ASN_PARSE_E (-140)

- Addresses by version: 219: 0x0C05E3B8
- Called by: `ble_219_0c05e420`
- Calls: `GetLength_ex`
- Confidence: high

## GetLength_ex

**Parse an ASN.1 DER length field (wolfSSL GetLength_ex)**

Reads the length octet at input[*inOutIdx]. Short form (<0x80) is the length itself; long form (0x80|n) reads n big-endian bytes (n <= 4, result must be non-negative). Advances *inOutIdx past the length bytes and stores the length in *len (0 when zero). If check is non-zero it also requires inOutIdx + length <= maxIdx. Error codes: -132 (BUFFER_E) when running past maxIdx, -140 (ASN_PARSE_E) for n > 4 or a negative result. The indefinite-length form (0x80) returns 0 after advancing one byte. Used by the DER decoders of the ECC key/signature code.

| Parameter | Type | Description |
|---|---|---|
| `input` | `ptr` | DER buffer |
| `inOutIdx` | `ptr` | in/out: u32 index into the buffer; advanced past the length field |
| `len` | `ptr` | out: s32 decoded length (0 if length is zero) |
| `maxIdx` | `u32` | size of the buffer (upper index bound) |
| `check` | `s32` | non-zero: also verify the content fits within maxIdx |

**Returns** `s32`: decoded length (>= 0) or negative wolfSSL error (-132 BUFFER_E, -140 ASN_PARSE_E)

- Addresses by version: 219: 0x0C05E350
- Called by: `GetASNInt`, `ble_219_0c05e474`
- Confidence: high

## aes128_encrypt_block

**AES-128 ECB encrypt of one 16-byte block, in place, using an expanded key**

Standard byte-oriented AES-128 encryption: initial AddRoundKey, nine rounds of SubBytes (S-box at 0x0C083E20), ShiftRows, MixColumns (GF(2^8) xtime with reduction constant 0x1B) and AddRoundKey, then a final round without MixColumns. param_1 is the 176-byte schedule from ble_219_0c048f3c and param_2 the 16-byte state which is overwritten with the ciphertext. Used by the BLE crypto wrappers (ble_219_0c049288, 0c0493d4, 0c0496a8), e.g. for AES-ECB/CCM-style operations and authentication.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | expanded round keys (176 bytes) |
| `param_2` | `ptr` | 16-byte block, encrypted in place |

- Addresses by version: 219: 0x0C048FD4
- Called by: `ble_crypto_ccm_cbc_mac`, `ble_219_0c0493d4`, `ble_219_0c0496a8`
- Confidence: high

## aes128_key_expansion

**AES-128 key schedule: expand a 16-byte key into 176 bytes of round keys**

Copies the 16-byte key from param_2 to param_1, then generates words 4..43: each new word is the previous word XOR the word four positions back; every fourth word first applies RotWord, SubWord via the AES S-box at 0x0C083E20, and XORs the round constant from the table at 0x0C07482C (0x01,0x02,0x04,...,0x1B,0x36). Output is the 11 round keys (44 words = 176 bytes) at param_1. Called together with ble_219_0c048fd4 from the three AES wrappers ble_219_0c049288, 0c0493d4, 0c0496a8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output: 176-byte expanded key schedule |
| `param_2` | `ptr` | input: 16-byte AES-128 key |

- Addresses by version: 219: 0x0C048F3C
- Called by: `ble_crypto_ccm_cbc_mac`, `ble_219_0c0493d4`, `ble_219_0c0496a8`
- Confidence: high

## ble_crypto_ccm_cbc_mac

**AES-128 CBC-MAC over a packet (CCM B0/B1 style blocks), emitting a 4-byte MIC**

Builds B0 = {0x59, 12 nonce bytes from param_4, 0x00, 0x00, payload_len} where payload_len = param_3 - 3, runs aes128_key_expansion + aes128_encrypt_block on it with key param_1 (X1 = E(K,B0)), then XORs in B1 = {pkt[0], pkt[1], pkt[2], 0 x 13} (the 3 header bytes of the packet at param_2) and encrypts again. The payload starting at pkt+3 is then processed in zero-padded 16-byte chunks: X = E(K, X xor chunk). The first 4 bytes of the final X are written to param_5 as the MIC; the key schedule is recomputed before every block. Flags byte 0x59 encodes Adata=1, M=8, L=2 of CCM, but only 4 MIC bytes are output and the header bytes are used directly instead of a length-prefixed AAD block, so this is a CCM-like authentication tag rather than standard CCM. Callers: the encrypt/decrypt wrappers ble_219_0c0493d4 and 0c0496a8 of the ble_crypto vehicle-authentication group (counter-based nonce, encrypted payload + MIC).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 16-byte AES-128 key |
| `param_2` | `ptr` | packet: 3 header bytes then payload |
| `param_3` | `u8` | total packet length; payload length = param_3 - 3 |
| `param_4` | `ptr` | nonce: 3 x u32 (12 bytes) copied into B0 bytes 1..12 |
| `param_5` | `ptr` | output: 4-byte MIC |

**Notes:** Whether the result is used as a CCM MIC or a plain CBC-MAC tag depends on the wrappers; byte 13 of B0 is always 0 so the effective nonce may be 13 bytes with a zero tail.

- Addresses by version: 219: 0x0C049288
- Called by: `ble_219_0c0493d4`, `ble_219_0c0496a8`
- Calls: `aes128_key_expansion`, `aes128_encrypt_block`, `memcpy`
- Confidence: medium

## btstack_crypto_ccm_next_block

**Advance an AES-CCM request to its next 16-byte block, finishing it when done**

BTstack btstack_crypto.c btstack_crypto_ccm_next_block(ccm, state_when_done). bytes = min(ccm->block_len (u16 at +0x3c), 16); counter (u16 +0x3a) is incremented; input (+0x1c) and output (+0x20) pointers advance by bytes; block_len (+0x3c) and message_len (u16 +0x38) are reduced by bytes. If message_len reaches 0 the state byte at +0x10 becomes 6 (CCM_CALCULATE_S0, compute the final MIC); otherwise state = param_2 and, if the current block_len is now 0, the request is completed via btstack_crypto_done: the head of the pending-operation list btstack_crypto_operations (DAT_20017388) is popped with btstack_linked_list_pop and the request callback at +4 is called with the arg at +8. The engine then continues with the next queued request from the HCI event handler. Layout of btstack_crypto_ccm_t: item +0, callback +4, arg +8, operation +0xc, state +0x10, key +0x14, nonce +0x18, input +0x1c, output +0x20, x_i[16] +0x24, aad_offset +0x34, aad_len +0x36, message_len +0x38, counter +0x3a, block_len +0x3c. No direct callers (reached from the crypto state machine 0c065038 / packet handler 0c064c6c region which belongs to the btstack_crypto group with 0c064ffc random, 0c065038 aes128/ccm, 0c065148 init).

| Parameter | Type | Description |
|---|---|---|
| `ccm` | `ptr` | btstack_crypto_ccm_t request |
| `state_when_done` | `u8` | CCM state to enter when more message bytes remain |

**Notes:** Matches the upstream source line by line (btstack_min(block_len,16), CCM_CALCULATE_S0 = 6, btstack_crypto_done pops btstack_crypto_operations).

- Addresses by version: 219: 0x0C0645EC
- Calls: `btstack_linked_list_pop`, `co_min_u32`
- Confidence: high

## crc32_compute_poly

**CRC-32 (reflected, init/xorout 0xffffffff) of a buffer using a table built for a given polynomial**

Zeroes the 1 KB table at 0x20009484 (memset 0x400), rebuilds it with crc32_make_table(param_3) for the reflected polynomial param_3, then runs the standard table-driven CRC: crc = 0xffffffff; for each byte crc = table[(byte ^ crc) & 0xff] ^ (crc >> 8); returns ~crc. Returns 0 when param_2 <= 0. With polynomial 0xedb88320 this is the usual CRC-32 (zlib). Rebuilding the table on every call makes it slow but reentrant with respect to the polynomial. Single caller 0x0c029414 (bt_app_set_name_and_advdata / vehicle SN handling).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | input bytes |
| `param_2` | `s32` | length in bytes; <= 0 yields 0 |
| `param_3` | `u32` | reflected CRC-32 polynomial passed to crc32_make_table |

**Returns** `u32`: CRC-32 of the buffer, or 0 for an empty buffer

- Addresses by version: 219: 0x0C02C454
- Called by: `ble_219_0c029414`
- Calls: `crc32_make_table`, `memset`
- Confidence: high

## crc32_make_table

**Build the 256-entry reflected CRC-32 lookup table for a given polynomial**

First bit-reverses param_1 over 32 bits (turning e.g. 0x04C11DB7 into the reflected form 0xEDB88320). Then for i = 0..255 computes the classic table entry: eight iterations of c = (c & 1) ? poly ^ (c >> 1) : c >> 1, starting from c = i. Entries are stored at 0x20009484 + 4*i (the loop pre-increments the pointer that starts at DAT_20009480, so the table ends at 0x20009880). Called from the CRC init routine (0x0c02c454), which is used by the firmware-upgrade/verification code.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | CRC-32 polynomial in normal (MSB-first) form, e.g. 0x04C11DB7 |

- Addresses by version: 219: 0x0C02C3FC
- Called by: `crc32_compute_poly`
- Confidence: high

## crypto_tea_cbc_decrypt

**TEA (32-round) decryption of a buffer in place with CBC-style chaining**

Requires param_2 (byte length) to be a multiple of 8, otherwise returns -1. For each 8-byte block it decrypts with standard TEA decryption: 32 rounds, delta 0x9e3779b9 (sum starts at 0xc6ef3720), key words k0..k3 read from param_5[0..3]. If the running byte counter *param_3 is non-zero, the plaintext is XORed with the previous ciphertext block held in the 8-byte chain buffer param_4; the chain buffer is then replaced by the block's ciphertext and *param_3 is advanced by 8. A leading loop over (*param_3 >> 10) and a per-block loop run byte additions on an uninitialised local array whose result is never used (dead code). Returns 0 on success. Caller 0x0c0285ec.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | buffer decrypted in place (length param_2) |
| `param_2` | `u32` | length in bytes, must be a multiple of 8 |
| `param_3` | `ptr` | u32 running byte offset; first block (0) is not chained, advanced by 8 per block |
| `param_4` | `ptr` | 8-byte CBC chaining value (previous ciphertext), updated |
| `param_5` | `ptr` | four 32-bit TEA key words |

**Returns** `s32`: 0 on success, -1 if length not a multiple of 8

**Notes:** Likely used to decrypt firmware-update or config data; the caller context was not examined.

- Addresses by version: 219: 0x0C036418
- Called by: `ble_219_0c0285ec`
- Confidence: high

## fp_add

**Signed big-integer add c = a + b (wolfSSL TFM fp_add) using s_fp_add / s_fp_sub**

wolfSSL fp_add(a, b, c). If the signs are equal: c->sign = a->sign and return s_fp_add(a, b, c). Otherwise it compares magnitudes inline (fp_cmp_mag: by used count, then digits from the most significant down): if |a| < |b| then c->sign = b->sign and s_fp_sub(b, a, c), else c->sign = a->sign and s_fp_sub(a, b, c); these paths return 0. Called by the modular arithmetic helpers 0c062fe4, 0c0634c4, 0c0635ac and the mp_add wrapper 0c064088.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | fp_int a |
| `param_2` | `ptr` | fp_int b |
| `param_3` | `ptr` | fp_int c = a + b |
| `param_4` | `u32` | unused (passed through) |

**Returns** `s32`: 0, or FP_VAL from s_fp_add

- Addresses by version: 219: 0x0C061FE8
- Called by: `ble_219_0c062fe4`, `ble_219_0c0634c4`, `ble_219_0c0635ac`, `ble_219_0c064088`
- Calls: `s_fp_add`, `s_fp_sub`
- Confidence: high

## fp_add_d

**Add a single 32-bit digit to a big integer magnitude: c = a + b**

Copies a to c when the pointers differ (used, sign, 0x60 digit bytes). If b is non-zero it adds b into c->dp[0] and propagates the carry upwards digit by digit (carry = CARRY4 of each addition), returning 0 as soon as the carry is zero. If the carry survives all used digits it is stored as a new top digit (dp[used] = carry, used++); if the carry is still set when the index reaches 24 (FP_SIZE) the function returns -1 (FP_VAL). The sign is not considered, i.e. this is the unsigned digit-add used by fp_read_radix (0c0642f8) and exported as mp_add_d via the thunk 0c0642f4. Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | source fp_int |
| `b` | `u32` | digit to add |
| `c` | `ptr` | destination fp_int (may equal a) |
| `param_4` | `u32` | unused |

**Returns** `s32`: 0 (FP_OKAY) or -1 (FP_VAL) when the carry would need a 25th digit

**Notes:** wolfSSL's reference fp_add_d goes through fp_add with a temporary; this build uses the simpler magnitude-only loop, so negative inputs are handled as magnitudes.

- Addresses by version: 219: 0x0C06428C
- Called by: `mp_add_d`, `fp_read_radix`
- Calls: `memcpy`
- Confidence: medium

## fp_addmod_ct

**Constant-time modular addition d = (a + b) mod c for a, b < c**

wolfSSL TFM fp_addmod_ct(a, b, c, d). First calls s_fp_add(a, b, d) (0c061e70, unsigned digit addition), then mask = all-ones when fp_cmp_mag_ct(d, c, c->used + 1) is not -1 (d >= c), else 0. For i = 0 .. c->used-1 it subtracts (mask & c->dp[i]) plus the running borrow from d->dp[i] (borrow computed from two unsigned compares), then sets d->dp[c->used] = 0, d->used = c->used, d->sign = a->sign and clamps d (a fully zero result gets sign 0). Returns 0 (FP_OKAY). No branch depends on the data, so it is used by the ECC code via the mp_addmod_ct wrapper 0c0640e8. Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | first addend fp_int (< c) |
| `b` | `ptr` | second addend fp_int (< c) |
| `c` | `ptr` | modulus fp_int |
| `d` | `ptr` | result fp_int |

**Returns** `s32`: always 0 (FP_OKAY)

- Addresses by version: 219: 0x0C062654
- Called by: `ble_219_0c0640e8`
- Calls: `fp_cmp_mag_ct`, `s_fp_add`
- Confidence: high

## fp_clear

**Zero a big integer in place (NULL-safe, no return value)**

If a is non-NULL: used = 0, sign = 0 and the 24-digit array (0x60 bytes) cleared with memset; NULL is ignored. Same body as mp_init (0c063fb8) but void. This matches wolfSSL mp_clear(a) { if (a == NULL) return; fp_clear(a); } and is the routine the ECC code calls after every temporary (very many callers: 0c05b724, 0c05e420, 0c05e474, 0c05e4e8, 0c05e868, 0c05eb00, 0c05efc0, 0c05f1b0, 0c05f71c ...). Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | fp_int to clear, or NULL |

**Notes:** Functionally this is wolfSSL's mp_clear; the name mp_clear was already assigned in wave 1 to the empty function 0c064000 (which is more likely mp_free/fp_free), so the inner routine's name fp_clear is used here.

- Addresses by version: 219: 0x0C063FEC
- Called by: `ble_219_0c05b724`, `ble_219_0c05b86c`, `ble_219_0c05bfa4`, `ble_219_0c05e420`, `ble_219_0c05e474`, `wc_ecc_curve_free`, `ble_219_0c05e558`, `ble_219_0c05e868`, `ble_219_0c05eb00`, `ble_219_0c05efc0`, `ble_219_0c05f1b0`, `ble_219_0c05f71c` ...
- Calls: `memset`
- Confidence: medium

## fp_cmp

**Signed comparison of two big integers**

Returns 1 (FP_GT), 0 (FP_EQ) or -1 (FP_LT). If signs differ the positive operand is greater; if both are negative the magnitudes are compared in reverse order; otherwise the magnitudes are compared by digit count first and then digit by digit from the most significant down (fp_cmp_mag). Identical in code to the mp_cmp wrapper at 0x0c0640f8; this copy is used by the fp-level routines 0c062fe4/0c0635ac. wolfSSL TFM fast-math big integer (fp_int): s32 used digit count at +0, s32 sign at +4 (0 = positive, 1 = negative), 32-bit digits dp[24] at +8 (0x68 bytes total, FP_SIZE = 24 digits).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | first fp_int |
| `b` | `ptr` | second fp_int |

**Returns** `s32`: 1 if a > b, 0 if equal, -1 if a < b

- Addresses by version: 219: 0x0C0628B4
- Called by: `ble_219_0c062fe4`, `ble_219_0c0635ac`
- Confidence: high

## fp_cmp_mag_ct

**Constant-time magnitude compare of two fp_int digit arrays**

Compares the lowest n digits of two fp_int values from the most significant digit downwards without data-dependent branches (a mask register tracks 'all higher digits equal so far'). Returns 1 if a > b, 0xFFFFFFFF (-1) if a < b and 0 if equal. Pointers start at dp[n-1] (word index n+1) and walk down. Used inside the Montgomery reduction / modular subtraction (callers 0c0625a0, 0c062654) to avoid timing leaks.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | first fp_int |
| `b` | `ptr` | second fp_int |
| `len` | `s32` | number of 32-bit digits to compare |

**Returns** `s32`: 1 (a > b), -1 (a < b), 0 (equal); 0 if len <= 0

**Notes:** Name from wolfSSL tfm.c fp_cmp_mag_ct; semantics verified by tracing the mask logic.

- Addresses by version: 219: 0x0C061E14
- Called by: `fp_submod_ct`, `fp_addmod_ct`
- Confidence: medium

## fp_div_2

**Halve a big integer b = a / 2 by a one-bit right shift from the top digit down (wolfSSL)**

wolfSSL TFM fp_div_2(a, b). b->used = a->used; starting at digit used-1 each digit is shifted right by one with the previous digit's low bit inserted at bit 31 (the odd '+0x40000001' pointer arithmetic is just dp[used-1]). Digits between the new and old b->used are memset to 0, b->sign = a->sign, then the result is clamped (used reduced past leading zero digits, sign cleared when zero). Callers: 0c0635ac and fp_div_2_mod_ct.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | fp_int a |
| `param_2` | `ptr` | fp_int b = a >> 1 (may alias a) |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | unused |

- Addresses by version: 219: 0x0C0623CC
- Called by: `fp_div_2_mod_ct`, `ble_219_0c0635ac`
- Calls: `memset`
- Confidence: high

## fp_div_2_mod_ct

**Constant-time modular halving c = (a / 2) mod b for 0 <= a < b (wolfSSL fp_div_2_mod_ct)**

wolfSSL TFM fp_div_2_mod_ct(a, b, c). mask = -(a->dp[0] & 1): if a is odd the modulus b is added first so the halving stays exact. For i in 0..b->used-1: c->dp[i] = (a->dp[i] & -(i < a->used)) + (b->dp[i] & mask) + carry, with a carry chain; c->dp[b->used] = final carry, c->used = b->used + 1, c->sign = 0, then clamp. Finally fp_div_2(c, c) shifts right by one. All digit operations are branch-free in the data (constant time) as used by the ECC point arithmetic; called from 0c064498 (the mp_div_2_mod_ct wrapper).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | fp_int a (0 <= a < b) |
| `param_2` | `ptr` | fp_int b (modulus) |
| `param_3` | `ptr` | fp_int c result |

**Returns** `s32`: always 0 (FP_OKAY)

- Addresses by version: 219: 0x0C062450
- Called by: `ble_219_0c064498`
- Calls: `fp_div_2`
- Confidence: high

## fp_lshd

**Shift a big integer left by whole 32-bit digits**

wolfSSL TFM fp_lshd(a, x). If a->used + x > 24 (FP_SIZE) returns -1 (FP_VAL) without touching a. Otherwise sets used = old_used + x, moves the digits upwards from the top (dp[y] = dp[y - x] for y from used-1 down to x), zeroes the lowest x digits with memset, and clamps (reduces used past zero top digits, zero value gets sign 0). Called from fp_mul_2d (0c062d84) and fp_div (0c062fe4). Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | fp_int shifted in place |
| `x` | `s32` | number of digits to shift |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | unused |

**Returns** `s32`: 0 (FP_OKAY) or -1 (FP_VAL) if the result would exceed 24 digits

- Addresses by version: 219: 0x0C062D08
- Called by: `fp_mul_2d`, `ble_219_0c062fe4`
- Calls: `memset`
- Confidence: high

## fp_mod_2d

**Big integer modulo a power of two: c = a mod 2^b**

wolfSSL TFM fp_mod_2d(a, b, c). If b <= 0 the result c is zeroed (used = 0, sign = 0, 96 digit bytes cleared). Otherwise a is copied to c when the pointers differ (used, sign and the 24 digits via memcpy of 0x60 bytes). If b >= 32 * a->used nothing more is done. Otherwise all digits from index b/32 (+1 when b is not a multiple of 32) up to c->used are zeroed with memset, digit b/32 is masked with 0xffffffff >> (32 - b%32), and c is clamped (used reduced past trailing zero digits, sign forced to 0 when the value becomes zero). Called from fp_div_2d (0c062f28). Part of the wolfSSL fast-math (tfm.c) big-integer group: fp_int = s32 used at +0, s32 sign at +4, u32 dp[24] at +8 (0x68 bytes, FP_SIZE = 24 digits).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | source fp_int |
| `b` | `s32` | number of low bits to keep |
| `c` | `ptr` | destination fp_int (may equal a) |

- Addresses by version: 219: 0x0C0624E8
- Called by: `ble_219_0c062f28`
- Calls: `memcpy`, `memset`
- Confidence: high

## fp_montgomery_calc_normalization

**Compute a = R mod b (R = 2^(32*used)) for Montgomery normalisation**

wolfSSL TFM fp_montgomery_calc_normalization(a, b). bits = number of significant bits in b's top digit (loop shifting right; 0 is treated as 32, the decompiler's odd modulo arithmetic is the '% DIGIT_BIT' of fp_count_bits). If b->used > 1, a is set to 2^((used-1)*32 + bits - 1) (inlined fp_2expt: zero a, then if the exponent is below 0x300 = 24*32 set used = exp/32 + 1 and dp[exp/32] = 1 << (exp % 32)); otherwise a = 1 and bits = 1. Then for x = bits-1 .. 31 it doubles a with fp_mul_2(a, a) (0c0620dc; a non-zero return aborts with that error) and subtracts b with s_fp_sub(a, b, a) (0c061f2c) whenever an inlined fp_cmp_mag(a, b) says a >= b (longer used count, or digit-by-digit compare from the top). Returns 0 on success. Called via the mp_montgomery_calc_normalization wrapper 0c064288 by the ECC Montgomery setup. Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | output fp_int receiving R mod b |
| `b` | `ptr` | modulus fp_int |
| `param_3` | `u32` | unused (register noise) |
| `param_4` | `u32` | unused (register noise) |

**Returns** `s32`: 0 (FP_OKAY) or the error returned by fp_mul_2

- Addresses by version: 219: 0x0C062940
- Called by: `ble_219_0c064288`
- Calls: `s_fp_sub`, `fp_mul_2`, `memset`
- Confidence: high

## fp_mul_2

**Double a big integer b = a * 2 by a one-bit left shift across the digits (wolfSSL fp_mul_2)**

wolfSSL TFM fp_mul_2(a, b). Returns FP_VAL (-1) if a->used > 23, or if a->used == 23 and the top bit of dp[23] is set (the source's own overflow guard). Otherwise b->used = a->used and each digit is shifted left by one with the previous digit's top bit carried in; a final carry writes an extra digit 1 and increments b->used. Digits between the new and the old b->used are memset to 0 and b->sign = a->sign. Returns 0. Called from 0c062940 (modular doubling).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | fp_int a |
| `param_2` | `ptr` | fp_int b = 2a (may alias a) |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | unused |

**Returns** `s32`: 0 or FP_VAL (-1) on overflow

- Addresses by version: 219: 0x0C0620DC
- Called by: `fp_montgomery_calc_normalization`
- Calls: `memset`
- Confidence: high

## fp_mul_2d

**Multiply a big integer by 2^b: c = a << b**

wolfSSL TFM fp_mul_2d(a, b, c). Copies a to c when the pointers differ. If b >= 32 it first calls fp_lshd(c, b / 32) and returns its error if non-zero. The remaining b % 32 bits are shifted with a carry loop over c->used digits (dp[i] = (dp[i] << s) + carry; carry = old dp[i] >> (32 - s)); a final non-zero carry becomes a new top digit when used < 24, and if used already equals 24 the function returns -1 (FP_VAL). Afterwards c is clamped. Returns 0 on success. Called from fp_div (0c062fe4). Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | source fp_int |
| `b` | `s32` | number of bits to shift left |
| `c` | `ptr` | destination fp_int (may equal a) |

**Returns** `s32`: 0 (FP_OKAY) or -1 (FP_VAL) on overflow of the 24-digit buffer

- Addresses by version: 219: 0x0C062D84
- Called by: `ble_219_0c062fe4`
- Calls: `fp_lshd`, `memcpy`
- Confidence: high

## fp_mul_d

**Multiply a big integer by a single 32-bit digit: c = a * b**

Copies a's used count and sign to c, then multiplies each digit of a by b with a 64-bit accumulator, storing the low 32 bits and carrying the high word. A final non-zero carry extends c by one digit; if the result would exceed 24 digits (FP_SIZE) it returns -1 (FP_VAL). Digits of c above the new length up to its old length are zeroed, trailing zero digits are trimmed (clamp) and a zero result is forced to a positive sign. wolfSSL TFM fast-math big integer (fp_int): s32 used digit count at +0, s32 sign at +4 (0 = positive, 1 = negative), 32-bit digits dp[24] at +8 (0x68 bytes total, FP_SIZE = 24 digits).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | source fp_int |
| `b` | `u32` | 32-bit multiplier digit |
| `c` | `ptr` | destination fp_int |

**Returns** `s32`: 0 (FP_OKAY) or -1 (FP_VAL) on overflow of the 24-digit buffer

- Addresses by version: 219: 0x0C062168
- Called by: `ble_219_0c062fe4`, `fp_read_radix`
- Confidence: high

## fp_read_radix

**Parse an ASCII number of radix 2..64 (fast path for hex) into a big integer**

wolfSSL TFM fp_read_radix(a, str, radix). a is zeroed first. For radix 16 the inlined fp_read_radix_16 is used: an optional leading '-' sets the sign, then the string is scanned from the end (strlen) and each hex nibble ('0'-'9', 'A'-'F' via -0x37, 'a'-'f' via -0x57) is ORed into dp[k] at bit offset j (j advances by 4, k by one digit every 8 nibbles); an invalid character or more than 24 digits returns -1 (FP_VAL); the result is clamped and the sign applied only when non-zero. For other radices in 2..64: optional '-', then per character: for radix <= 36 lowercase letters are upper-cased using the newlib _ctype_ table at 0x0c0862a9 (class bits & 3 == 2 = _L), the character is looked up in the 64-entry map "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/", parsing stops at the first value >= radix or an unknown character, otherwise a = a * radix (fp_mul_d, 0c062168) + digit (fp_add_d, 0c06428c), propagating their error codes; the sign is set if the result is non-zero. Radix outside 2..64 returns -1. Called by the ECC code (0c05b724, 0c05b86c, 0c05bd30, 0c05e614, 0c060974) to load curve parameters and keys given as hex strings. Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | destination fp_int |
| `str` | `ptr` | NUL-terminated ASCII number, optional leading '-' |
| `radix` | `s32` | number base, 2..64 (16 takes the fast path) |
| `param_4` | `u32` | unused |

**Returns** `s32`: 0 (FP_OKAY), -1 (FP_VAL) for bad radix / bad hex digit / overflow, or an fp_mul_d/fp_add_d error

- Addresses by version: 219: 0x0C0642F8
- Called by: `ble_219_0c05b724`, `ble_219_0c05b86c`, `ble_219_0c05bd30`, `ble_219_0c05e614`, `ble_219_0c060974`
- Calls: `fp_mul_d`, `fp_add_d`, `memset`, `strlen`
- Confidence: high

## fp_read_unsigned_bin

**Load a big-endian byte string into a big integer**

wolfSSL TFM fp_read_unsigned_bin(a, b, c) with the 32-bit little-endian fast path. Zeroes a (sign and 96 digit bytes; used is set below). If c <= 0x60 (96 bytes = 24 digits) then used = (c + 3) / 4 and the c input bytes are copied in reverse into the byte view of dp (byte index c-1 down to 0 while reading b forwards), so a big-endian input lands little-endian in the digits. If c > 96 only the last 96 bytes of b are used and used = 24 (the leading excess is silently dropped). Finally a is clamped (used reduced past zero top digits, sign cleared for 0). Always returns 0. Reached through the thunk 0c06422c (mp_read_unsigned_bin) from the ECC import routines. Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | destination fp_int |
| `b` | `ptr` | big-endian input bytes |
| `c` | `s32` | number of input bytes |

**Returns** `s32`: always 0 (FP_OKAY)

- Addresses by version: 219: 0x0C062BAC
- Called by: `mp_read_unsigned_bin`
- Calls: `memset`
- Confidence: high

## fp_rshb

**Shift a big integer right by x bits in place**

wolfSSL TFM fp_rshb(c, x). Negative x returns immediately. If x >= 32 it first calls fp_rshd(c, x / 32) and keeps x % 32. A zero value returns unchanged. Then it walks the digits from the most significant down: dp[i] = (dp[i] >> x) | (carry << (32 - x)) where carry is the low x bits of the previous (higher) digit (mask ~(-1 << x)). Finally the value is clamped. Called from fp_div_2d (0c062f28) and the mp_rshb wrapper 0c064284. Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `c` | `ptr` | fp_int shifted in place |
| `x` | `s32` | number of bits to shift right |

**Notes:** If x % 32 == 0 after the digit shift the bit loop still runs with a shift of 0, which is harmless.

- Addresses by version: 219: 0x0C062EA8
- Called by: `ble_219_0c062f28`, `ble_219_0c064284`
- Calls: `fp_rshd`
- Confidence: high

## fp_rshd

**Shift a big integer right by whole 32-bit digits**

wolfSSL TFM fp_rshd(a, x). If x >= a->used the value becomes zero (used = 0, sign = 0, all 96 digit bytes cleared with memset). Otherwise digits are moved down (dp[i] = dp[i + x] for i < used - x), the vacated top x digits are zeroed with memset, used is reduced by x and the value is clamped. Called from fp_rshb (0c062ea8), fp_div_2d (0c062f28) and fp_div (0c062fe4). Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | fp_int shifted in place |
| `x` | `s32` | number of digits to shift right |

- Addresses by version: 219: 0x0C062E40
- Called by: `fp_rshb`, `ble_219_0c062f28`, `ble_219_0c062fe4`
- Calls: `memset`
- Confidence: high

## fp_sub

**Signed big-integer subtract c = a - b (wolfSSL TFM fp_sub) using s_fp_add / s_fp_sub**

wolfSSL fp_sub(a, b, c). If the signs differ: c->sign = a->sign and return s_fp_add(a, b, c). If equal, magnitudes are compared inline: when |a| >= |b|, c->sign = a->sign and s_fp_sub(a, b, c); when |a| < |b|, c->sign = !a->sign (positive becomes negative and vice versa) and s_fp_sub(b, a, c). Returns 0 on those paths. Called by 0c062fe4, 0c0635ac, 0c063ce4 and the mp_sub wrapper 0c06408c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | fp_int a |
| `param_2` | `ptr` | fp_int b |
| `param_3` | `ptr` | fp_int c = a - b |

**Returns** `s32`: 0, or FP_VAL from s_fp_add

- Addresses by version: 219: 0x0C062068
- Called by: `ble_219_0c062fe4`, `ble_219_0c0635ac`, `ble_219_0c063ce4`, `ble_219_0c06408c`
- Calls: `s_fp_add`, `s_fp_sub`
- Confidence: high

## fp_submod_ct

**Constant-time modular subtraction d = (a - b) mod c for a, b < c**

wolfSSL TFM fp_submod_ct(a, b, c, d). Computes mask = all-ones when fp_cmp_mag_ct(a, b, c->used + 1) returns -1 (a < b), else 0. Then for i = 0 .. c->used it accumulates d->dp[i] = (i < a->used ? a->dp[i] : 0) + (mask & c->dp[i]) + carry using two CARRY4 tests per digit, stores the final carry in d->dp[c->used + 1], sets d->used = c->used + 2 and d->sign = 0, clamps d, and finally calls s_fp_sub(d, b, d) (0c061f2c; the decompiler shows the b register as extraout_s15). The result is a + (a < b ? c : 0) - b with no branch on the operand values. Always returns 0 (FP_OKAY). Called from the mp_submod_ct wrapper 0c0640e4 used by the ECC point arithmetic. Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | minuend fp_int (< c) |
| `b` | `ptr` | subtrahend fp_int (< c) |
| `c` | `ptr` | modulus fp_int |
| `d` | `ptr` | result fp_int |

**Returns** `s32`: always 0 (FP_OKAY)

**Notes:** The loop also handles the impossible c->used < 0 case by emitting a single digit; the pointer walk starts at dp[0] via pre-increment from word index 1.

- Addresses by version: 219: 0x0C0625A0
- Called by: `ble_219_0c0640e4`
- Calls: `fp_cmp_mag_ct`, `s_fp_sub`
- Confidence: high

## fp_to_unsigned_bin_at_pos

**Append a big integer's bytes (least significant first) at an offset**

Writes b[x++] for every byte of t in little-endian order: for all but the top digit it emits 4 bytes (shift 0,8,16,24), then for the most significant digit it emits bytes until the digit becomes zero. Nothing is written for zero. Returns the new offset x. The caller (0c062c84, fp_to_unsigned_bin) then reverses the buffer to get big-endian output. (Decompiled parameter order is x, t, b.)

| Parameter | Type | Description |
|---|---|---|
| `x` | `u32` | starting offset into the output buffer |
| `t` | `ptr` | source fp_int |
| `b` | `ptr` | output byte buffer |

**Returns** `u32`: offset after the last byte written (x + number of bytes)

**Notes:** The decompiler shows the first and third arguments swapped/typed as pointers; semantics follow wolfSSL's fp_to_unsigned_bin_at_pos(int x, fp_int*, unsigned char*).

- Addresses by version: 219: 0x0C062C20
- Called by: `ble_219_0c062c84`
- Confidence: high

## get_digit

**Read digit n of a big integer (0 when out of range)**

Returns a->dp[n] (word n+2) if a is non-NULL and 0 <= n < used, else 0. wolfSSL's get_digit, used by mp_cond_copy-style constant-time code.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | mp_int or NULL |
| `n` | `s32` | digit index |

**Returns** `u32`: digit value or 0

- Addresses by version: 219: 0x0C0644C8
- Called by: `ble_219_0c05f338`
- Confidence: high

## get_digit_count

**Number of used digits in a big integer (NULL-safe)**

Returns the first word (used) of the mp_int, or 0 when the pointer is NULL. wolfSSL's get_digit_count.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | mp_int or NULL |

**Returns** `s32`: number of used digits, 0 for NULL

- Addresses by version: 219: 0x0C0644C0
- Called by: `ble_219_0c05eb00`, `ble_219_0c05f338`, `ble_219_0c05f830`, `ble_219_0c060974`
- Confidence: high

## mbedtls_sha1_finish_ret

**mbedTLS SHA-1 finish: pad, append 64-bit big-endian bit length, output the 20-byte digest**

Computes high = (total[0] >> 29) | (total[1] << 3) and low = total[0] << 3 and stores them as 8 big-endian bytes on the stack. Padding length is 56-last or 120-last for last = total[0] & 0x3F. Calls mbedtls_sha1_update_ret (ble_219_0c04a924) with the sha1_padding table at 0x0C08400C (0x80 then zeros) and then with the 8 length bytes; if both return 0 the five state words at ctx+8..+0x18 are written big-endian into the 20-byte output param_2. On an error the output is left untouched and nothing is reported (the return value is void here). Caller: mbedtls_sha1_ret (ble_219_0c04aa80).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | mbedtls_sha1_context |
| `param_2` | `ptr` | output: 20-byte SHA-1 digest |

- Addresses by version: 219: 0x0C04A9A8
- Called by: `ble_219_0c04aa80`
- Calls: `mbedtls_sha1_update_ret`
- Confidence: high

## mbedtls_sha1_update_ret

**mbedTLS SHA-1 update: absorb input, running the compression on each full 64-byte block**

mbedtls_sha1_context layout: total[2] (byte count, lo/hi) at +0, state[5] at +8, buffer[64] at +0x1C. Adds len to total[0] with carry into total[1]; if the buffer already holds total[0] & 0x3F bytes and the input completes it, memcpy fills the buffer and sha1_process_block (ble_219_0c049a28, = mbedtls_internal_sha1_process) is run on it; then every remaining whole 64-byte chunk is processed straight from the input, and the tail is memcpy'd into the buffer. Returns 0, or the non-zero result of the block function. Group: mbedtls_sha1_finish_ret (ble_219_0c04a9a8) and the one-shot mbedtls_sha1_ret (ble_219_0c04aa80, which seeds the standard IV 0x67452301..0xC3D2E1F0).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | mbedtls_sha1_context |
| `param_2` | `ptr` | input bytes |
| `param_3` | `u32` | input length in bytes |
| `param_4` | `u32` | unused (register pass-through) |

**Returns** `s32`: 0 on success, else error from the block function

- Addresses by version: 219: 0x0C04A924
- Called by: `mbedtls_sha1_finish_ret`, `ble_219_0c04aa80`
- Calls: `sha1_process_block`, `memcpy`
- Confidence: high

## md5_encode_le_words

**Serialise 32-bit words to little-endian bytes (MD5 'Encode')**

Do-while loop that takes consecutive 32-bit words from param_2 and writes each as four bytes (LSB first) to param_1 until at least param_3 bytes have been produced; because it is a do-while, at least one word is always written and the length is effectively rounded up to a multiple of 4. This is the MD5 'Encode' helper used to write out the state words as the 16-byte digest; its only caller is ble_219_0c047efc (MD5 final).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output byte buffer |
| `param_2` | `ptr` | input array of u32 words |
| `param_3` | `u32` | number of bytes to produce (multiple of 4) |

- Addresses by version: 219: 0x0C0476D8
- Called by: `md5_final`
- Confidence: high

## md5_final

**MD5 'Final': pad the message, append the bit length and write the 16-byte digest**

RFC 1321 MD5Final. Saves the 64-bit bit count ctx[0..1] as 8 little-endian bytes with md5_encode_le_words, computes the padding length so the buffer ends at 56 mod 64 (56-fill if fill < 56, else 120-fill), feeds the PADDING table at 0x0C0747D0 (0x80 followed by zeros) and then the 8 length bytes through md5_update (ble_219_0c047e70), and finally serialises the four state words ctx[2..5] little-endian into the 16-byte digest at param_2. The context is not zeroised afterwards. Callers: the upgrade md5sum verification (ble_219_0c03477c, 0c036868, 0c037588 'upgrade file md5sum error').

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | MD5 context (see md5_update) |
| `param_2` | `ptr` | output: 16-byte digest |

- Addresses by version: 219: 0x0C047EFC
- Called by: `ble_219_0c03477c`, `ble_219_0c036868`, `ble_219_0c037588`
- Calls: `md5_encode_le_words`, `md5_update`
- Confidence: high

## md5_init

**Initialise an MD5 context**

Zeroes the 64-bit bit-count words at ctx[0],ctx[1] and loads the standard MD5 initial values into ctx[2..5]: 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476. Called from ble_219_0c03477c, ble_219_0c036868 and ble_219_0c0369d8 (md5sum computation in the upgrade code).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | MD5 context (6 x u32: count lo/hi, state A..D) |

- Addresses by version: 219: 0x0C047E44
- Called by: `ble_219_0c03477c`, `ble_219_0c036868`, `ble_219_0c0369d8`
- Confidence: high

## md5_transform

**MD5 compression function: process one 64-byte block into the 4-word state**

Fully unrolled 64-step MD5 (RFC 1321, constants such as 0xD76AA478, 0xE8C7B756 ...; rotates 7/12/17/22, 5/9/14/20, 4/11/16/23, 6/10/15/21). param_1 points to the four state words A,B,C,D (a context pointer plus 8 in the surrounding MD5 context); param_2 is the 64-byte input block which is first decoded into sixteen little-endian words on the stack. After the rounds the result is added back into the state in place. Called from the MD5 update routine ble_219_0c047e70. Used by the firmware-upgrade module for the md5sum check.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | state A,B,C,D (4 x u32), updated in place |
| `param_2` | `ptr` | 64-byte message block |

- Addresses by version: 219: 0x0C047710
- Called by: `md5_update`
- Confidence: high

## md5_update

**MD5 'Update': absorb a byte string into the context, compressing full 64-byte blocks**

RFC 1321 MD5Update over a context laid out as ctx[0..1] = 64-bit bit count, ctx[2..5] = state A..D, 64-byte block buffer at +0x18. The current buffer fill is (count & 0x1ff) >> 3; the bit count is advanced by len*8 with carry into the high word (plus len >> 29). If the input completes a block the first part is memcpy'd into the buffer, md5_transform (ble_219_0c047710) is run on the buffer and then directly on each further whole 64-byte chunk of the input; whatever is left is memcpy'd to the start of the buffer. Shorter inputs are only appended to the buffer. Part of the md5_init / md5_update / md5_final group used by the nb_upgrade md5sum check (callers ble_219_0c03477c, 0c036868 and the final routine ble_219_0c047efc); also called from ble_219_0c0285ec.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | MD5 context: count lo/hi, state A..D, 64-byte buffer at +0x18 |
| `param_2` | `ptr` | input bytes |
| `param_3` | `u32` | input length in bytes |
| `param_4` | `u32` | unused (register pass-through to memcpy) |

- Addresses by version: 219: 0x0C047E70
- Called by: `ble_219_0c0285ec`, `ble_219_0c03477c`, `ble_219_0c036868`, `md5_final`
- Calls: `md5_transform`, `memcpy`
- Confidence: high

## mp_add_d

**Thunk to fp_add_d: add a digit to a big integer**

Single branch to fp_add_d (0c06428c): c = a + b for a 32-bit digit b, carry-propagating, -1 (FP_VAL) if a 25th digit would be needed. This is wolfSSL's mp_add_d wrapper; called by the ECC routines 0c05b86c and 0c05f8c4 (e.g. adding 1 to a scalar). Part of the wolfSSL fast-math (tfm.c) big-integer group.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | source mp_int |
| `b` | `u32` | digit to add |
| `c` | `ptr` | destination mp_int |
| `param_4` | `u32` | unused |

**Returns** `s32`: 0 (MP_OKAY) or -1 (MP_VAL) on overflow

- Addresses by version: 219: 0x0C0642F4
- Called by: `ble_219_0c05b86c`, `ble_219_0c05f8c4`
- Calls: `fp_add_d`
- Confidence: high

## mp_clear

**Release a big integer (empty in this build)**

Empty function (single return). With the static TFM fp_int there is no heap storage to free, and the actual wiping is done separately by the forcezero function at 0x0c063fd4. Called after each mp temporary in the ECC scalar multiplication (0c05f8c4).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | fp_int (argument ignored) |

**Notes:** Could be mp_clear or mp_free; both are no-ops for static fp_int.

- Addresses by version: 219: 0x0C064000
- Called by: `ble_219_0c05f8c4`
- Confidence: low

## mp_cmp

**Signed comparison of two big integers (mp_cmp wrapper)**

Same algorithm as fp_cmp: differing signs decide immediately; two negatives compare reversed; otherwise compare used digit counts and then digits from the most significant end. Returns 1 (MP_GT), 0 (MP_EQ), -1 (MP_LT). Heavily used by the ECC point/modular arithmetic (8 callers: 0c05eb00, 0c05f218, 0c05f8c4, 0c05fd18, 0c05ff44 ...). wolfSSL TFM fast-math big integer (fp_int): s32 used digit count at +0, s32 sign at +4 (0 = positive, 1 = negative), 32-bit digits dp[24] at +8 (0x68 bytes total, FP_SIZE = 24 digits).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | first mp_int |
| `b` | `ptr` | second mp_int |

**Returns** `s32`: 1 if a > b, 0 if equal, -1 if a < b

- Addresses by version: 219: 0x0C0640F8
- Called by: `ble_219_0c05eb00`, `ble_219_0c05f218`, `ble_219_0c05f8c4`, `ble_219_0c05fd18`, `ble_219_0c05ff44`, `ble_219_0c0601fc`, `ble_219_0c060828`, `ble_219_0c060974`
- Confidence: high

## mp_cmp_d

**Compare a big integer with a single digit**

If a is zero (used == 0) the result is 0 when b == 0, else -1. If a is negative it is less (-1). If a has more than one digit it is greater (1). Otherwise dp[0] is compared with b giving 1, 0 or -1. Used by ECC code to test values against 1 (e.g. in 0c05f8c4). wolfSSL TFM fast-math big integer (fp_int): s32 used digit count at +0, s32 sign at +4 (0 = positive, 1 = negative), 32-bit digits dp[24] at +8 (0x68 bytes total, FP_SIZE = 24 digits).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | mp_int |
| `b` | `u32` | digit to compare with |

**Returns** `s32`: 1 if a > b, 0 if equal, -1 if a < b

- Addresses by version: 219: 0x0C064184
- Called by: `ble_219_0c05e558`, `ble_219_0c05efc0`, `ble_219_0c05f8c4`
- Confidence: high

## mp_cond_copy

**Constant-time conditional copy of a big integer: if (copy) b = a**

Builds mask = -copy (all ones or zero). Returns -173 if either pointer is NULL. For each digit of a, b->dp[i] is replaced with (a->dp[i] ^ b->dp[i]) & mask ^ b->dp[i] (digits of b above a's used count are masked likewise), and b->used = used_b ^ (mask & (used_a ^ used_b)). No branch depends on the copy flag, which makes it safe for secret-dependent selection in the ECC scalar multiplication (called from 0c05f338 and 0c05f8c4 on the x, y and z coordinates of a point). Sign is not copied.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | source mp_int |
| `copy` | `s32` | 0 or 1: whether to copy |
| `b` | `ptr` | destination mp_int |

**Returns** `s32`: 0 on success, -173 (BAD_FUNC_ARG) on NULL argument

- Addresses by version: 219: 0x0C0644E0
- Called by: `ble_219_0c05f338`, `ble_219_0c05f8c4`
- Confidence: high

## mp_copy

**Copy a big integer: b = a**

wolfSSL mp_copy(a, b) / fp_copy: when the pointers differ it copies used and sign and then the 24 digits (memcpy of 0x60 bytes from +8); copying onto itself is a no-op. Always returns 0 (MP_OKAY). Used by the ECC arithmetic (0c05e558, 0c05e868, 0c05eb00, 0c05f1d8, 0c05f338, 0c05f8c4, 0c05fd18, 0c05ff44, 0c0601fc). Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | source mp_int |
| `b` | `ptr` | destination mp_int |

**Returns** `s32`: always 0 (MP_OKAY)

- Addresses by version: 219: 0x0C064234
- Called by: `ble_219_0c05e558`, `ble_219_0c05e868`, `ble_219_0c05eb00`, `wc_ecc_copy_point`, `ble_219_0c05f338`, `ble_219_0c05f8c4`, `ble_219_0c05fd18`, `ble_219_0c05ff44`, `ble_219_0c0601fc`
- Calls: `memcpy`
- Confidence: high

## mp_count_bits

**Bit length of a big integer**

Returns 0 for used == 0, otherwise (used-1)*32 plus the number of significant bits in the top digit (loop shifting right until zero). Used in ECC (0c05f338, 0c05f8c4, 0c0601fc) for size checks.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | mp_int |

**Returns** `s32`: number of significant bits

- Addresses by version: 219: 0x0C064268
- Called by: `ble_219_0c05f338`, `ble_219_0c05f8c4`, `ble_219_0c0601fc`
- Confidence: high

## mp_forcezero

**Zero a big integer (used = 0, sign = +, all 96 digit bytes cleared)**

Sets used = 0 and sign = 0, then clears the 24-digit dp array byte by byte with an explicit loop (wolfSSL ForceZero style, not optimised to memset) so secret values do not remain on the stack. Called on temporaries holding ECC scalars/keys (callers 0c05f8c4, 0c0600c0, 0c0601d0). wolfSSL TFM fast-math big integer (fp_int): s32 used digit count at +0, s32 sign at +4 (0 = positive, 1 = negative), 32-bit digits dp[24] at +8 (0x68 bytes total, FP_SIZE = 24 digits).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | fp_int to wipe |

**Notes:** Could be fp_zero; the byte-wise loop and the use after secret-dependent computations suggest the ForceZero variant.

- Addresses by version: 219: 0x0C063FD4
- Called by: `ble_219_0c05f8c4`, `ble_219_0c0600c0`, `wc_ecc_free`
- Confidence: medium

## mp_init

**Initialise a big integer to zero (NULL-safe, returns MP_OKAY)**

wolfSSL mp_init(a): if a is non-NULL it performs fp_init/fp_zero - used = 0, sign = 0 and the 24-digit dp array (0x60 bytes) cleared with memset. Returns 0 (MP_OKAY) in both cases. Used by the ECC routines (0c05b724, 0c05b86c, 0c05e420, 0c05f8c4, 0c0600c0 ...) to set up temporaries before arithmetic. Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | mp_int to initialise, or NULL |
| `param_2` | `u32` | unused |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | unused |

**Returns** `s32`: always 0 (MP_OKAY)

- Addresses by version: 219: 0x0C063FB8
- Called by: `ble_219_0c05b724`, `ble_219_0c05b86c`, `ble_219_0c05bfa4`, `ble_219_0c05e420`, `ble_219_0c05e558`, `ble_219_0c05e614`, `ble_219_0c05f8c4`, `ble_219_0c0600c0`, `ble_219_0c0601fc`, `ble_219_0c060974`
- Calls: `memset`
- Confidence: high

## mp_init_multi

**Initialise up to six big integers to zero (NULL entries skipped)**

wolfSSL mp_init_multi(a, b, c, d, e, f): for each of the six pointer arguments that is non-NULL it sets used = 0, sign = 0 and clears the 24-digit array (0x60 bytes) with memset. Always returns 0 (MP_OKAY). Called at the start of the ECC routines that need several temporaries (0c05e868, 0c05eb00, 0c05efc0, 0c05f164, 0c05fd18, 0c060190, 0c0601fc, 0c060828, 0c060ae4). Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | mp_int or NULL |
| `b` | `ptr` | mp_int or NULL |
| `c` | `ptr` | mp_int or NULL |
| `d` | `ptr` | mp_int or NULL |
| `e` | `ptr` | mp_int or NULL |
| `f` | `ptr` | mp_int or NULL |

**Returns** `s32`: always 0 (MP_OKAY)

- Addresses by version: 219: 0x0C064004
- Called by: `ble_219_0c05e868`, `ble_219_0c05eb00`, `ble_219_0c05efc0`, `ble_219_0c05f164`, `ble_219_0c05fd18`, `wc_ecc_init`, `ble_219_0c0601fc`, `ble_219_0c060828`, `ble_219_0c060ae4`
- Calls: `memset`
- Confidence: high

## mp_iszero

**Test whether a big integer is zero**

Returns true when the used-digit count (first word) is 0. Used throughout the ECC arithmetic (callers 0c05eb00, 0c05f218, 0c05fd18 ...).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | mp_int |

**Returns** `bool`: true if a == 0

- Addresses by version: 219: 0x0C06425C
- Called by: `ble_219_0c05eb00`, `ble_219_0c05f218`, `ble_219_0c05fd18`, `ble_219_0c0601fc`, `ble_219_0c060974`
- Confidence: high

## mp_montgomery_setup

**Compute the Montgomery constant rho = -1/m mod 2^32**

Takes dp[0] (at offset 8) of the modulus; if it is even returns -1 (FP_VAL). Otherwise it starts from x = (((b+2)&4)<<1)+b (correct to 4 bits) and applies two Newton iterations x *= 2 - b*x to reach 16 bits, and a further step folded into the final expression to reach 32 bits, then stores rho = -x (mod 2^32) to *rho. Callers are the ECC modular multiply/scalar-mult routines.

| Parameter | Type | Description |
|---|---|---|
| `modulus` | `ptr` | mp_int modulus (must be odd) |
| `rho` | `ptr` | out: u32 Montgomery reduction digit |

**Returns** `s32`: 0 on success, -1 if the modulus is even

- Addresses by version: 219: 0x0C064458
- Called by: `ble_219_0c05b724`, `ble_219_0c05b86c`, `ble_219_0c05f71c`, `ble_219_0c05f8c4`, `ble_219_0c05fb10`, `ble_219_0c05fd18`, `ble_219_0c0601fc`
- Confidence: high

## mp_read_unsigned_bin

**Thunk to fp_read_unsigned_bin: load big-endian bytes into a big integer**

Single branch instruction to fp_read_unsigned_bin (0c062bac): zeroes a, copies up to 96 big-endian bytes into the little-endian digit array (used = (c + 3) / 4, extra leading bytes dropped) and clamps. Returns 0. This is wolfSSL's mp_read_unsigned_bin wrapper, called by the ECC key/point import code (0c05b86c, 0c05e420, 0c05f218, 0c0601fc, 0c060ae4). Part of the wolfSSL fast-math (tfm.c) big-integer group.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | destination mp_int |
| `b` | `ptr` | big-endian input bytes |
| `c` | `s32` | number of input bytes |

**Returns** `s32`: always 0 (MP_OKAY)

- Addresses by version: 219: 0x0C06422C
- Called by: `ble_219_0c05b86c`, `ble_219_0c05e420`, `ble_219_0c05f218`, `ble_219_0c0601fc`, `ble_219_0c060ae4`
- Calls: `fp_read_unsigned_bin`
- Confidence: high

## mp_set

**Set a big integer to a single digit value**

wolfSSL mp_set(a, b) / fp_set: sign = 0, digits dp[1..23] cleared with memset (0x5c bytes from +0xc), dp[0] = b and used = (b != 0). Always returns 0 (MP_OKAY). Used by the ECC routines (0c05bd30, 0c05efc0, 0c05fd18, 0c05ff44, 0c0601fc, 0c060ae4) to initialise constants such as 0 and 1. Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | destination mp_int |
| `b` | `u32` | digit value |

**Returns** `s32`: always 0 (MP_OKAY)

- Addresses by version: 219: 0x0C06449C
- Called by: `ble_219_0c05bd30`, `ble_219_0c05efc0`, `ble_219_0c05fd18`, `ble_219_0c05ff44`, `ble_219_0c0601fc`, `ble_219_0c060ae4`
- Calls: `memset`
- Confidence: high

## mp_to_unsigned_bin_len

**Write a big integer as fixed-length big-endian bytes**

Writes exactly n bytes, filling the output from the last byte backwards: byte k (counting from the least significant) is (dp[k/4] >> (8*(k%4))) & 0xff, so the value is zero-padded on the left. It does not check that the value fits in n bytes (digits above used are zero). Always returns 0. Used to export ECC coordinates/scalars (callers 0c05ba6c, 0c05baf0, 0c05bbcc, 0c05bd30, 0c05c13c).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | source mp_int |
| `out` | `ptr` | output buffer of n bytes |
| `n` | `s32` | number of bytes to write |

**Returns** `s32`: always 0

- Addresses by version: 219: 0x0C0641F4
- Called by: `ble_219_0c05ba6c`, `ble_219_0c05baf0`, `ble_219_0c05bbcc`, `ble_219_0c05bd30`, `ble_219_0c05c13c`
- Confidence: high

## mp_unsigned_bin_size

**Number of bytes needed for the big integer's magnitude**

Computes ceil(bit_length / 8) where the bit length is (used-1)*32 plus the position of the highest set bit in the top digit (the loop shifts the top digit right until zero). Returns 0 for used == 0. This is fp_unsigned_bin_size(a) = (fp_count_bits(a)+7)/8 with fp_count_bits inlined. Called from 0c05fb10.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | mp_int |

**Returns** `s32`: size in bytes

- Addresses by version: 219: 0x0C0641B8
- Called by: `ble_219_0c05fb10`
- Confidence: high

## s_fp_add

**Unsigned big-integer add c = |a| + |b| on 24-digit TFM fp_ints with carry and clamp**

wolfSSL TFM s_fp_add(a, b, c) (fp_int: s32 used +0, s32 sign +4, u32 dp[24] +8). y = max(a->used, b->used), oldused = min(c->used, 24), c->used = y. If y <= 0 the result is zero and the old digits are cleared. Otherwise digits 0..y-1 are added with a carry chain (two CARRY4 terms); a final carry appends digit 1 if y < 24 and bumps used. If the resulting used count is 24 it returns FP_VAL (-1) (overflow of FP_SIZE). Remaining old digits up to oldused are memset to 0 and the number is clamped (leading zero digits dropped; sign kept, or 0 when the value becomes zero). The sign of c is set by the caller (fp_add / fp_sub). Returns FP_OKAY (0).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | fp_int a |
| `param_2` | `ptr` | fp_int b |
| `param_3` | `ptr` | fp_int c = \|a\| + \|b\| (sign preset by caller) |

**Returns** `s32`: 0 or FP_VAL (-1) when 24 digits would be needed

- Addresses by version: 219: 0x0C061E70
- Called by: `fp_add`, `fp_sub`, `fp_addmod_ct`
- Calls: `memset`
- Confidence: high

## s_fp_sub

**Unsigned big-integer subtract c = |a| - |b| (|a| >= |b|) on TFM fp_ints, then clamp**

wolfSSL TFM s_fp_sub(a, b, c). c->used = a->used. For x < b->used: c->dp[x] = a->dp[x] - b->dp[x] - borrow with the borrow recomputed from the two unsigned compares; for b->used <= x < a->used only the borrow is propagated. Digits from a->used up to the old c->used are memset to 0, then fp_clamp drops leading zero digits (sign unchanged, or set to 0 when the result is zero). Caller guarantees |a| >= |b| and sets c->sign; used by fp_add and fp_sub and by the modular helpers 0c0625a0, 0c062940, 0c062a28.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | fp_int a (minuend) |
| `param_2` | `ptr` | fp_int b (subtrahend, \|b\| <= \|a\|) |
| `param_3` | `ptr` | fp_int c result |
| `param_4` | `u32` | unused (leftover register) |

- Addresses by version: 219: 0x0C061F2C
- Called by: `fp_add`, `fp_sub`, `fp_submod_ct`, `fp_montgomery_calc_normalization`, `ble_219_0c062a28`
- Calls: `memset`
- Confidence: high

## sha1_ctx_init_with_seed

**Initialise a SHA-1 style context, optionally loading four state words**

Zeroes the 64-bit length counter ctx[0],ctx[1] and ctx[6] (the fifth state word E, which in ble_219_0c049a28 is stored at offset 0x18). If param_2 is non-NULL, four words are copied from it into ctx[2..5] (the A,B,C,D state words); if NULL those words are left untouched. Unlike plain SHA-1 init this does not write the fixed constants, so the caller supplies the initial vector. Caller: ble_219_0c02bdd0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | hash context (7 x u32: length lo/hi, A,B,C,D,E) |
| `param_2` | `ptr` | optional 4-word initial state (A,B,C,D); NULL to keep existing |

**Notes:** Role of the 4-word seed is unverified; may be a keyed/seeded hash construct.

- Addresses by version: 219: 0x0C0499F0
- Called by: `ble_219_0c02bdd0`
- Confidence: medium

## sha1_ctx_set_e_word_one

**Set the word at offset 0x18 of a context to 1**

Stores 1 in *(u32*)(param_1+0x18). In the SHA-1 context used by ble_219_0c049a28 offset 0x18 is the fifth state word, but this function has no direct callers, so it is more likely a generic 'set flag' method reached through a function-pointer table.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | context pointer |

- Addresses by version: 219: 0x0C049A20
- Confidence: low

## sha1_process_block

**SHA-1 compression: process one 64-byte block into the five-word state**

Fully unrolled 80-round SHA-1 (constants 0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xCA62C1D6; rotl 5 / rotl 30). The state A,B,C,D,E lives at ctx+8,+0xC,+0x10,+0x14,+0x18. The 16 input words at param_2 are byte-swapped (big-endian load) into W[0..15] and the schedule W[t] = rotl1(W[t-3]^W[t-8]^W[t-14]^W[t-16]) is computed on the fly. Results are added back into the state in place and 0 is returned. Called from ble_219_0c04a924 (SHA-1 update/final wrapper).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | hash context; state words at +8..+0x18 |
| `param_2` | `ptr` | 64-byte message block (16 u32 words) |

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C049A28
- Called by: `mbedtls_sha1_update_ret`
- Confidence: high

## sm_c1_build_t1

**Build SMP c1 input t1 = (pres || preq || rat || iat) XOR r at 0x2000FDB4**

Creates the 16-byte p1 on the stack: bytes 0..6 are param_3 and bytes 7..13 are param_2 (both 7-byte Pairing PDUs, copied byte-reversed by co_reverse_copy_7), then byte 14 = param_5 and byte 15 = param_4. It then stores 0x2000FDB4[i] = p1[i] XOR param_1[i] for 16 bytes. This is the first step of SMP c1 (t1 = e(k, r XOR p1), with p1 = pres || preq || rat' || iat'); the AES encryption is performed by a later step. The trace calls with labels 'r' and 't1' are empty stubs.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 16-byte random value r |
| `param_2` | `ptr` | 7-byte Pairing Request PDU (preq), copied to p1[7..13] |
| `param_3` | `ptr` | 7-byte Pairing Response PDU (pres), copied to p1[0..6] |
| `param_4` | `u8` | initiator address type (iat), p1[15] |
| `param_5` | `u8` | responder address type (rat), p1[14] |

**Notes:** Assigning param_2 to preq and param_3 to pres follows the c1 byte order; the argument names are an assumption.

- Addresses by version: 219: 0x0C04F30C
- Called by: `ble_219_0c051eb8`
- Calls: `co_reverse_copy_7`, `util_nop_stub_b`
- Confidence: medium

## sm_c1_xor_p2

**XOR the 16-byte value at 0x2000FD94 with SMP c1 p2 (0 || ia || ra)**

Builds p2 on the stack as 4 zero bytes followed by the 6 bytes at param_1 and the 6 bytes at param_2, then writes param_3[i] = RAM[0x2000FD94+i] XOR p2[i] for i = 0..15. This is the p2 step of the Bluetooth SMP legacy confirm-value function c1 (p2 = padding || initiator address || responder address), applied to the output of an earlier AES-128 step stored at 0x2000FD94. The AES step itself is not in this function, and the trace call 0x0c065ce0 is an empty stub.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 6-byte initiator address (ia) |
| `param_2` | `ptr` | 6-byte responder address (ra) |
| `param_3` | `ptr` | 16-byte output buffer |

**Notes:** Which pointer is ia and which is ra is inferred from the c1 layout.

- Addresses by version: 219: 0x0C04F1EC
- Calls: `util_nop_stub_b`
- Confidence: medium

## wc_AesEncrypt

**AES single-block encrypt using the 4 x 1 KB T-tables (wolfSSL wc_AesEncrypt)**

Encrypts one 16-byte block. The Aes context holds the expanded round keys as u32 key[60] at offset 0 and the round count at offset 0xF0 (param_1[0x3c]); the loop runs rounds/2 double-iterations and is skipped entirely when rounds/2 is not in 1..7. Input words are byte-swapped (big-endian load) and XORed with the first round key, then each round does Te0[s0>>24]^Te1[(s1>>16)&ff]^Te2[(s2>>8)&ff]^Te3[s3&ff]^rk using the table at 0x0c075844 (first entry 0xc66363a5, the standard AES Te0). The final round extracts S-box bytes by masking the same tables (0xff, 0xff00, 0xff0000, 0xff000000), adds the last round key and byte-swaps the four result words into the output block. Used by the AES-GCM code (CTR keystream and H computation).

| Parameter | Type | Description |
|---|---|---|
| `aes` | `ptr` | wolfSSL Aes context: expanded encryption key schedule (u32[60]) followed by the round count at +0xF0 |
| `in_block` | `ptr` | 16-byte plaintext block |
| `out_block` | `ptr` | 16-byte ciphertext output block |

**Notes:** Signature matches wolfSSL wc_AesEncrypt(Aes*, const byte*, byte*); table layout verified against firmware bytes at 0x0c075844.

- Addresses by version: 219: 0x0C05D4AC
- Called by: `wc_AesGcmSetKey`, `AES_GCM_encrypt_C`, `wc_AesGcmDecrypt`
- Confidence: high

## wc_AesFree

**Free an Aes context (empty in this build)**

Empty function (single return). In wolfSSL wc_AesFree only releases async/hardware resources, which are not compiled in here, so nothing needs to be cleared. Called after AES-GCM encrypt/decrypt in the pairing helpers 0c05bf00 and 0c05c13c, mirroring wc_AesInit.

| Parameter | Type | Description |
|---|---|---|
| `aes` | `ptr` | Aes context (argument ignored) |

**Notes:** The callers pass the Aes context in r0; the function ignores it.

- Addresses by version: 219: 0x0C05E34C
- Called by: `ble_219_0c05bf00`, `ble_219_0c05c13c`
- Confidence: medium

## wc_AesGcmDecrypt

**AES-GCM decrypt: verify the auth tag in constant time, then CTR-decrypt (wolfSSL)**

wolfSSL wc_AesGcmDecrypt(aes, out, in, sz, iv, ivSz, authTag, authTagSz, authIn, authInSz) with AES_GCM_decrypt_C inlined. Returns BAD_FUNC_ARG (-173 = 0xffffff53) if aes, iv or authTag is NULL, if sz != 0 with in/out NULL, if authTagSz is not 1..16, or if ivSz == 0. J0 is iv || 00000001 for a 12-byte IV, else GHASH of the IV. It computes T' = GHASH(aes, authIn, authInSz, in, sz, 16 bytes) XOR E_K(J0) and compares authTagSz bytes against authTag with an OR-accumulated constant-time compare; a mismatch returns AES_GCM_AUTH_E (-180 = 0xffffff4c) before any plaintext is written. Then the ciphertext is decrypted block by block (increment the big-endian 32-bit counter, wc_AesEncrypt, XOR) with a memcpy'd partial final block. Returns 0 on success. Called from the ble_crypto wrapper 0c05bf00.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Aes context |
| `param_2` | `ptr` | out: plaintext |
| `param_3` | `ptr` | ciphertext |
| `param_4` | `u32` | ciphertext length |
| `param_5` | `ptr` | IV / nonce |
| `param_6` | `u32` | IV length (must be > 0) |
| `param_7` | `ptr` | expected auth tag |
| `param_8` | `u32` | tag length 1..16 |
| `param_9` | `ptr` | additional authenticated data |
| `param_10` | `u32` | AAD length |

**Returns** `s32`: 0, BAD_FUNC_ARG (-173) or AES_GCM_AUTH_E (-180)

- Addresses by version: 219: 0x0C05E2F0
- Called by: `ble_219_0c05bf00`
- Calls: `wc_AesEncrypt`, `GHASH`, `memcpy`
- Confidence: high

## wc_AesGcmSetKey

**Set a 16-byte AES-GCM key: expand the key and compute the GHASH key H = E_K(0^128)**

wolfSSL wc_AesGcmSetKey, restricted to len == 16. Zeroes a 16-byte IV on the stack, sets aes->keylen (+0xf4) = 16 and aes->rounds (+0xf0) = 10, calls wc_AesSetKeyLocal and, on success, wc_AesEncrypt(aes, zero_block, aes->H) where H lives at aes+0x124; H is the hash subkey later used by GHASH. Returns 0 on success, the key-setup error, or BAD_FUNC_ARG (-173 = -0xad) when len != 16 or aes is NULL. Called by the ble_crypto AES-GCM wrappers 0c05bf00 and 0c05c13c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Aes context (H at +0x124) |
| `param_2` | `ptr` | 16-byte key |
| `param_3` | `u32` | key length; only 16 accepted |

**Returns** `s32`: 0, BAD_FUNC_ARG (-173) or the error from wc_AesSetKeyLocal

- Addresses by version: 219: 0x0C05DBE0
- Called by: `ble_219_0c05bf00`, `ble_219_0c05c13c`
- Calls: `wc_AesEncrypt`, `wc_AesSetKeyLocal`
- Confidence: high

## wc_AesInit

**Initialise an Aes context: store heap pointer (device id unused)**

If the context pointer is NULL returns BAD_FUNC_ARG (-173); otherwise stores param_2 at offset 0x134 of the 312-byte Aes structure (aes->heap) and returns 0. The caller passes heap = 0 and devId = INVALID_DEVID (-2), which this non-async build ignores. Called right before the AES-GCM key is set in the pairing/session encryption helpers (0c05bf00, 0c05c13c).

| Parameter | Type | Description |
|---|---|---|
| `aes` | `ptr` | Aes context (0x138 bytes) to initialise |
| `heap` | `ptr` | heap hint stored at aes+0x134 (NULL in all callers) |

**Returns** `s32`: 0 on success, -173 (BAD_FUNC_ARG) if aes is NULL

**Notes:** Third argument (devId = 0xfffffffe) is passed by the caller but not used by this build.

- Addresses by version: 219: 0x0C05E338
- Called by: `ble_219_0c05bf00`, `ble_219_0c05c13c`
- Confidence: high

## wc_AesSetKeyLocal

**AES-128 key expansion into the Aes context (+ inverse key for decrypt) and IV set (wolfSSL)**

wolfSSL AesSetKeyLocal with wc_AesSetIV inlined. Writes aes->keylen (+0xf4) = keylen and aes->rounds (+0xf0) = keylen/4 + 6, memcpy's the user key into aes->key (+0) and byte-swaps each word (big-endian load). Only keylen == 16 is supported (AES-128, 10 rounds): the expansion loop produces rk[4..43] with rk[i] = rk[i-4] ^ SubWord(RotWord(temp)) ^ rcon, using the S-box bytes extracted from the Te tables at 0x0c075844 and the rcon table at 0x0c0838e4 (first value 0x01000000). If dir == 1 (AES_DECRYPTION) the round-key order is reversed (swap 4-word groups from both ends) and rounds 1..rounds-1 get InvMixColumns applied through the Td tables at 0x0c074844 indexed by Te1 S-box bytes. Finally the IV: if iv is NULL aes->reg (+0xf8, 16 bytes) is zeroed, else copied from iv. Returns 0, or BAD_FUNC_ARG (-173 = 0xffffff53) when keylen is not 16 (or 0).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Aes context: key[60] at +0, rounds +0xf0, keylen +0xf4, reg (IV) +0xf8 |
| `param_2` | `ptr` | user key bytes |
| `param_3` | `u32` | key length in bytes; only 16 accepted |
| `param_4` | `ptr` | 16-byte IV or NULL (zero IV) |
| `param_5` | `s32` | direction: 0 = AES_ENCRYPTION, 1 = AES_DECRYPTION |

**Returns** `s32`: 0 or BAD_FUNC_ARG (-173)

- Addresses by version: 219: 0x0C05D8F8
- Called by: `wc_AesGcmSetKey`
- Calls: `memcpy`
- Confidence: high

## wc_HashFree

**Free a wc_HashAlg by type: only SHA-256 (type 6) is built in (wolfSSL wc_HashFree)**

wolfSSL wc_HashFree(hash, type). NULL hash returns BAD_FUNC_ARG (-173 = 0xffffff53). Switch on the wc_HashType: 6 (WC_HASH_TYPE_SHA256) calls wc_Sha256Free and returns 0; types 3,4,5,7,8,10,11,12,13 (MD5, SHA, SHA224, SHA384, SHA512, SHA3-224/256/384/512) are not compiled in and return HASH_TYPE_E (-232 = 0xffffff18); every other value (NONE, MD2, MD4, MD5_SHA, BLAKE2 ...) returns BAD_FUNC_ARG. Called from 0c060be8 (the wc_Hash wrapper). Sibling of wc_HashInit and wc_HashGetDigestSize.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | wc_HashAlg union |
| `param_2` | `u32` | wc_HashType; 6 = SHA-256 |

**Returns** `s32`: 0, HASH_TYPE_E (-232) or BAD_FUNC_ARG (-173)

- Addresses by version: 219: 0x0C060DAC
- Called by: `ble_219_0c060be8`
- Calls: `wc_Sha256Free`
- Confidence: high

## wc_HashGetDigestSize

**Digest size in bytes for a wolfSSL hash type**

Maps a wc_HashType enum value to its digest length. Only type 6 (WC_HASH_TYPE_SHA256) is compiled in and returns 32 (0x20). Types 1-5 and 7-15 (MD2, MD4, MD5, SHA, SHA-224, SHA-384/512, SHA-3 ...) are known but not built into this image and return -232 (HASH_TYPE_E); anything else returns -173 (BAD_FUNC_ARG). Called by the HKDF wrapper 0c060be8.

| Parameter | Type | Description |
|---|---|---|
| `hash_type` | `u32` | wc_HashType enum value (6 = SHA-256) |

**Returns** `s32`: 32 for SHA-256, -232 for unsupported hash types, -173 for invalid types

- Addresses by version: 219: 0x0C060CE0
- Called by: `ble_219_0c060be8`
- Confidence: high

## wc_HashInit

**Initialise a wolfSSL hash context for a given hash type (SHA-256 only)**

Returns -173 for a NULL context. For hash type 6 (SHA-256) it loads the eight SHA-256 initial values (0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19) into words 0..7, clears the buffer length / length-low / length-high words (indexes 0x18..0x1a) and word 0x1b (heap), and returns 0. Types 3,4,5,7,8,10,11,12,13 return -232 (HASH_TYPE_E, not built in); other types return -173.

| Parameter | Type | Description |
|---|---|---|
| `hash` | `ptr` | wc_HashAlg union / Sha256 context to initialise |
| `hash_type` | `u32` | wc_HashType (6 = SHA-256) |

**Returns** `s32`: 0 on success, -173 or -232 on error

**Notes:** This is the wc_InitSha256 body inlined into the type switch.

- Addresses by version: 219: 0x0C060D0C
- Called by: `ble_219_0c060be8`
- Confidence: high

## wc_HmacFree

**Free an Hmac context: for macType SHA-256 (6) release the inner hash (wolfSSL wc_HmacFree)**

wolfSSL wc_HmacFree(hmac). Does nothing for NULL. If hmac->macType (byte at +0x114) == 6 (WC_SHA256) it calls wc_Sha256Free (an empty function in this build) and, re-checking the same byte, calls it again with the context pointer, which is just the compiler's rendering of the switch and the empty callee; other MAC types are not built in. No memory is zeroed. Called from 0c05c088 after wc_HmacInit/wc_HmacSetKey/wc_HmacUpdate/wc_HmacFinal.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Hmac context (may be NULL) |

- Addresses by version: 219: 0x0C06100C
- Called by: `ble_219_0c05c088`
- Calls: `wc_Sha256Free`
- Confidence: high

## wc_HmacInit

**Zero a 0x118-byte Hmac context and store its heap pointer (wolfSSL wc_HmacInit)**

wolfSSL wc_HmacInit(hmac, heap, devId). Returns BAD_FUNC_ARG (-173 = 0xffffff53) for a NULL context; otherwise memset(hmac, 0, 0x118), hmac->heap (+0x110) = heap and returns 0. devId is ignored (no crypto callbacks built). The macType byte at +0x114 (checked by wc_HmacFree) is thereby cleared. Called from 0c05c088 (the ble_crypto HMAC-SHA256 helper) and paired with wc_HmacFree.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Hmac context (0x118 bytes) |
| `param_2` | `ptr` | heap hint stored at +0x110 |
| `param_3` | `s32` | devId (unused) |

**Returns** `s32`: 0 or BAD_FUNC_ARG (-173)

- Addresses by version: 219: 0x0C060FEC
- Called by: `ble_219_0c05c088`
- Calls: `memset`
- Confidence: high

## wc_InitSha256

**Initialise a SHA-256 context**

Returns -173 (BAD_FUNC_ARG) when the context is NULL. Otherwise loads the SHA-256 IV into digest[0..7] (6a09e667 bb67ae85 3c6ef372 a54ff53a 510e527f 9b05688c 1f83d9ab 5be0cd19), zeroes buffLen, loLen, hiLen (words 0x18..0x1a) and word 0x1b (heap), and returns 0. Called by HMAC, HKDF and DRBG code before hashing.

| Parameter | Type | Description |
|---|---|---|
| `sha256` | `ptr` | wolfSSL Sha256 context (digest[8], buffer[16], buffLen, loLen, hiLen, heap) |

**Returns** `s32`: 0 on success, -173 if sha256 is NULL

- Addresses by version: 219: 0x0C061DB0
- Called by: `ble_219_0c05b984`, `ble_219_0c05ba6c`, `ble_219_0c05bfa4`, `ble_219_0c060de0`, `ble_219_0c061034`, `ble_219_0c061270`
- Confidence: high

## wc_RNG_TestSeed

**Continuous test on RNG seed: reject repeated adjacent 4-byte blocks**

Implements the NIST SP 800-90B style continuous test used by wolfSSL's Hash_DRBG. It walks the seed in 4-byte blocks and compares each block with the next one using an OR-accumulated XOR (constant-time compare); if any two adjacent blocks are identical, or a block has zero length, the result becomes 3 (DRBG_CONT_FIPS_E). Returns 0 when seedSz <= 4 or no repetition was found. Called by the DRBG instantiate/reseed routines (0c061688, 0c061834).

| Parameter | Type | Description |
|---|---|---|
| `seed` | `ptr` | seed/entropy buffer |
| `seed_size` | `u32` | buffer length in bytes |

**Returns** `s32`: 0 = ok (DRBG_SUCCESS), 3 = DRBG_CONT_FIPS_E (repeated block detected)

- Addresses by version: 219: 0x0C061500
- Called by: `ble_219_0c061688`, `ble_219_0c061834`
- Confidence: high

## wc_Sha256Free

**Free a SHA-256 context (empty in this build)**

Empty function (single return). wolfSSL's wc_Sha256Free only has work to do for hardware/async back ends, none of which are built here. Called after each SHA-256 use by HMAC/HKDF/DRBG code.

| Parameter | Type | Description |
|---|---|---|
| `sha256` | `ptr` | Sha256 context (argument ignored) |

**Notes:** Shared empty free hook; could equally be another trivial free function used with SHA-256 contexts.

- Addresses by version: 219: 0x0C061E10
- Called by: `ble_219_0c05b984`, `ble_219_0c05ba6c`, `ble_219_0c05bfa4`, `wc_HashFree`, `ble_219_0c060de0`, `wc_HmacFree`, `ble_219_0c061034`, `ble_219_0c061270`
- Confidence: medium

## wc_ecc_copy_point

**Copy an ecc_point (x, y, z big integers) into another (wolfSSL wc_ecc_copy_point)**

Returns ECC_BAD_ARG_E (-170 = -0xaa) if either point is NULL. Otherwise copies the three fp_int coordinates with the mp_copy routine at 0x0c064234: x at +0, y at +0x68 and z at +0xd0 (each fp_int is 0x68 bytes: used, sign, dp[24]); it stops at the first non-zero result and returns it, else 0. Called from 0c05f338 (ECC point multiplication / cache handling).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source ecc_point |
| `param_2` | `ptr` | destination ecc_point |

**Returns** `s32`: 0, ECC_BAD_ARG_E (-170) or an mp_copy error

- Addresses by version: 219: 0x0C05F1D8
- Called by: `ble_219_0c05f338`
- Calls: `mp_copy`
- Confidence: high

## wc_ecc_curve_free

**Clear the loaded curve parameters of an ecc_curve_spec according to its load_mask**

wolfSSL wc_ecc_curve_free(curve) for a build without USE_ECC_B_PARAM: the struct has dp at +0, mp_int pointers prime +4, Af +8, order +0xc, Gx +0x10, Gy +0x14 and the byte load_mask at +0x24. For each set bit (PRIME 0x01, AF 0x02, ORDER 0x08, GX 0x10, GY 0x20; bit 0x04 for Bf is unused) it calls the mp_int clear routine at 0x0c063fec (mp_clear: used = 0, sign = 0, digits zeroed) on the corresponding big integer, then resets load_mask to 0. NULL curve is ignored. Called at the end of every ECC operation (0c05e614, 0c05fb10, 0c05fd18, 0c05ff44, 0c0600c0, 0c0601fc, 0c060974).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ecc_curve_spec (may be NULL) |

**Notes:** 0x0c063fec is the real mp_clear (the empty 0c064000 named mp_clear in wave 1 is more likely mp_free).

- Addresses by version: 219: 0x0C05E4E8
- Called by: `ble_219_0c05e614`, `ble_219_0c05fb10`, `ble_219_0c05fd18`, `ble_219_0c05ff44`, `ble_219_0c0600c0`, `ble_219_0c0601fc`, `ble_219_0c060974`
- Calls: `fp_clear`
- Confidence: high

## wc_ecc_free

**Release an ecc_key: clear pubkey.x/y/z and force-zero the private scalar k (wolfSSL)**

wolfSSL wc_ecc_free(key). For a non-NULL key it calls the mp_clear routine at 0x0c063fec on pubkey.x (+0x18), pubkey.y (+0x80) and pubkey.z (+0xe8) and then mp_forcezero on the private scalar k at +0x150 so the secret is wiped. Always returns 0 (also for NULL). Counterpart of wc_ecc_init; same six ble_crypto callers plus 0c05ba4c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ecc_key (may be NULL) |

**Returns** `s32`: always 0

- Addresses by version: 219: 0x0C0601D0
- Called by: `ble_219_0c0537b4`, `ble_219_0c05ba4c`, `ble_219_0c05baf0`, `ble_219_0c05bd30`, `ble_219_0c05bfa4`, `ble_219_0c05c13c`
- Calls: `mp_forcezero`, `fp_clear`
- Confidence: high

## wc_ecc_init

**Zero a 0x1bc-byte ecc_key and init its pubkey.x/y/z and private scalar k (wolfSSL wc_ecc_init)**

wolfSSL wc_ecc_init(key) (wc_ecc_init_ex with heap = NULL inlined). Returns BAD_FUNC_ARG (-173 = 0xffffff53) for NULL. memset(key, 0, 0x1bc) then mp_init_multi (routine at 0x0c064004) on &key->k (+0x150), key->pubkey.x (+0x18), .y (+0x80), .z (+0xe8), NULL, NULL; a failure returns MEMORY_E (-125 = 0xffffff83). On success key->heap (+0x14) = NULL and 0 is returned. Layout implied: type +0, idx +4, state +8, flags +0xc, dp +0x10, heap +0x14, pubkey +0x18 (3 x 0x68), k +0x150, rng +0x1b8. Called by the ble_crypto ECDH/ECDSA wrappers (0c0537b4, 0c05baf0, 0c05bd30, 0c05bfa4, 0c05c13c), always paired with wc_ecc_free.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ecc_key to initialise (0x1bc bytes) |

**Returns** `s32`: 0, BAD_FUNC_ARG (-173) or MEMORY_E (-125)

- Addresses by version: 219: 0x0C060190
- Called by: `ble_219_0c0537b4`, `ble_219_0c05baf0`, `ble_219_0c05bd30`, `ble_219_0c05bfa4`, `ble_219_0c05c13c`
- Calls: `mp_init_multi`, `memset`
- Confidence: high

## wc_ecc_set_curve

**Select ECC curve parameters for a key by key size or curve id**

Validates the arguments (keysize <= 0 together with curve_id < 0 gives -173 BAD_FUNC_ARG; keysize > 66 gives -170 ECC_BAD_ARG_E) and returns 0 early if the key already uses a custom curve (key->idx == -1). Otherwise it clears key->idx (+4) and key->dp (+0x10) and scans the ecc_sets table at 0x0c080a18 (stride 0x34 bytes; entry fields size at +0 and curve id at +4; terminated by size == 0; the table holds secp224r1 (28 bytes, id 14) and secp256r1 (32 bytes, id 7)). With curve_id > 0 the entry whose id matches is chosen, otherwise the first entry whose size >= keysize. On a match key->idx is the table index and key->dp points at the entry. No match gives -172 (ECC_CURVE_OID_E).

| Parameter | Type | Description |
|---|---|---|
| `key` | `ptr` | wolfSSL ecc_key (idx at +4, dp at +0x10) |
| `keysize` | `s32` | wanted key size in bytes (<= 66), or <= 0 to select by id |
| `curve_id` | `s32` | ecc_curve_id (e.g. 7 = secp256r1, 14 = secp224r1), or <= 0 to select by size |

**Returns** `s32`: 0 on success, -173/-170/-172 on error

**Notes:** Table contents (28/14, 32/7 entries) verified from firmware bytes; the Find My code uses P-224, the pairing code P-256.

- Addresses by version: 219: 0x0C05E7FC
- Called by: `ble_219_0c0600c0`, `ble_219_0c060ae4`
- Confidence: high

## wc_ecc_set_rng

**Attach a random number generator to an ECC key**

If key is NULL returns -173 (BAD_FUNC_ARG); otherwise stores param_2 at key+0x1b8 (key->rng) and returns 0. The stored RNG is used for blinding/timing resistance and for key generation inside the ECC routines. Called once from the ECDH key-agreement helper 0c05c13c right after generating the ephemeral key.

| Parameter | Type | Description |
|---|---|---|
| `key` | `ptr` | wolfSSL ecc_key |
| `rng` | `ptr` | WC_RNG state to store at key+0x1b8 |

**Returns** `s32`: 0 on success, -173 (BAD_FUNC_ARG) if key is NULL

- Addresses by version: 219: 0x0C060BD4
- Called by: `ble_219_0c05c13c`
- Confidence: high
