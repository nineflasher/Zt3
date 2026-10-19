# BLE - `crypto` functions

202 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`AES_GCM_encrypt_C`](#aes_gcm_encrypt_c) | 0x0C05DE8C | AES-GCM encrypt in CTR mode and produce the auth tag (wolfSSL software path, no arg checks) |
| [`DecodeECC_DSA_Sig`](#decodeecc_dsa_sig) | 0x0C05E474 | Parse a DER ECDSA signature SEQUENCE into its r and s integers |
| [`GHASH`](#ghash) | 0x0C05DC2C | GCM GHASH over AAD and ciphertext plus the 64-bit length block, output sSz bytes (wolfSSL) |
| [`GMULT`](#gmult) | 0x0C05D828 | GF(2^128) multiply for GHASH: X = X * Y (bitwise, R = 0xE1) |
| [`GetASNInt`](#getasnint) | 0x0C05E3B8 | Parse a DER INTEGER header and strip a leading 0x00 pad byte (wolfSSL GetASNInt) |
| [`GetInt`](#getint) | 0x0C05E420 | Parse one ASN.1 DER INTEGER at an index and load it into a big integer |
| [`GetLength_ex`](#getlength_ex) | 0x0C05E350 | Parse an ASN.1 DER length field (wolfSSL GetLength_ex) |
| [`Hash_DRBG_Generate`](#hash_drbg_generate) | 0x0C061270 | Hash_DRBG generate: stream SHA-256 of V with a counter, run a repeat test, then update V |
| [`Hash_DRBG_Instantiate`](#hash_drbg_instantiate) | 0x0C061174 | Instantiate a Hash_DRBG: V = Hash_df(entropy \|\| nonce), C = Hash_df(0x00 \|\| V), counter = 1 |
| [`Hash_DRBG_Reseed`](#hash_drbg_reseed) | 0x0C0611D0 | Reseed a Hash_DRBG: V = Hash_df(0x01 \|\| V \|\| entropy), C = Hash_df(0x00 \|\| V), counter reset to 1 |
| [`Hash_df`](#hash_df) | 0x0C061034 | NIST SP 800-90A Hash_df: derive 55 bytes from two SHA-256 blocks over a counter, tag and two inputs |
| [`Transform_Sha256`](#transform_sha256) | 0x0C061950 | SHA-256 compression: process one 64-byte block into the eight-word state |
| [`aes128_encrypt_block`](#aes128_encrypt_block) | 0x0C048FD4 | AES-128 ECB encrypt of one 16-byte block, in place, using an expanded key |
| [`aes128_key_expansion`](#aes128_key_expansion) | 0x0C048F3C | AES-128 key schedule: expand a 16-byte key into 176 bytes of round keys |
| [`ble_crypto_auth_derive_own_word`](#ble_crypto_auth_derive_own_word) | 0x0C04FA38 | Derive the local auth word as stored word XOR peer word, then send it as request type 0 |
| [`ble_crypto_auth_load_keys`](#ble_crypto_auth_load_keys) | 0x0C050310 | Load the 16-byte auth keys from the key store, set the mode, and fall back to generating one |
| [`ble_crypto_auth_pubkey_begin`](#ble_crypto_auth_pubkey_begin) | 0x0C04F894 | Store a 65-byte key block (X, Y, flag) and start an operation over it with a 16-byte value |
| [`ble_crypto_auth_send_word_type1`](#ble_crypto_auth_send_word_type1) | 0x0C04F9B0 | Send the local 16-bit auth word as request type 1 on the crypto channel |
| [`ble_crypto_auth_start_by_mode`](#ble_crypto_auth_start_by_mode) | 0x0C04FB64 | Start the crypto operation for the current auth mode: type 0 with value 1 (mode 1) or 3 (mode 2) |
| [`ble_crypto_auth_step`](#ble_crypto_auth_step) | 0x0C04F7B8 | Advance the crypto-auth state machine: state 1 starts the address check, state 3 starts the next op |
| [`ble_crypto_auth_store_xor_word`](#ble_crypto_auth_store_xor_word) | 0x0C04FACC | Store peer XOR local as the shared auth word, then send the local word as request type 0 |
| [`ble_crypto_ccm_cbc_mac`](#ble_crypto_ccm_cbc_mac) | 0x0C049288 | AES-128 CBC-MAC over a packet (CCM B0/B1 style blocks), emitting a 4-byte MIC |
| [`ble_crypto_ccm_open_frame`](#ble_crypto_ccm_open_frame) | 0x0C0496A8 | Verify and decrypt a received CCM-style frame, accepting only a counter above the last one |
| [`ble_crypto_ccm_seal_frame`](#ble_crypto_ccm_seal_frame) | 0x0C0493D4 | Encrypt and authenticate an outgoing frame: 3-byte header, CCM-style payload, 4-byte MIC, 2-byte counter |
| [`ble_crypto_diversify`](#ble_crypto_diversify) | 0x0C05BD30 | Diversify a 32-byte secret with a peer P-224 point into a 28-byte value |
| [`ble_crypto_ecdh_seal_p256`](#ble_crypto_ecdh_seal_p256) | 0x0C05C13C | ECDH-P256 seal: ephemeral key, KDF, AES-128-GCM, output ephemeral public key, ciphertext and tag |
| [`ble_crypto_ecdsa_p256_verify`](#ble_crypto_ecdsa_p256_verify) | 0x0C05BFA4 | Verify an ECDSA P-256 signature over the SHA-256 digest of a message |
| [`ble_crypto_init`](#ble_crypto_init) | 0x0C02BDD0 | Copy the vehicle serial number and seed the pairing crypto contexts at startup |
| [`ble_crypto_kdf_connect`](#ble_crypto_kdf_connect) | 0x0C05BCE4 | Two-step key derivation: 'intermediate' then 'connect', producing 16 bytes |
| [`ble_crypto_kdf_update`](#ble_crypto_kdf_update) | 0x0C05BCC0 | Derive 32 bytes from the 32-byte key at param_1 with the label 'update' |
| [`ble_crypto_report_auth_state`](#ble_crypto_report_auth_state) | 0x0C02BF20 | Post the pairing result event 0x0A or 0x0B when any key slot holds a valid key |
| [`ble_crypto_serial_mac`](#ble_crypto_serial_mac) | 0x0C05C088 | HMAC-SHA256 over a message, keyed by a derivation of param_1 with 'SerialNumberProtection' |
| [`ble_crypto_server_secret`](#ble_crypto_server_secret) | 0x0C05BE98 | Derive the 32-byte server shared secret from two 32-byte values |
| [`ble_crypto_session_decrypt`](#ble_crypto_session_decrypt) | 0x0C05BF00 | AES-128-GCM decrypt a pairing-session message whose 16-byte tag is at its end |
| [`ble_crypto_sha256_commit`](#ble_crypto_sha256_commit) | 0x0C05BA6C | SHA-256 over the 28-byte X of ctx+0x150 followed by the 32 bytes at ctx+0x1BC |
| [`ble_crypto_sha256_digest`](#ble_crypto_sha256_digest) | 0x0C05B984 | One-shot SHA-256 of param_1 bytes at param_2 into the 32-byte digest at param_3 |
| [`ble_crypto_try_default_pwd`](#ble_crypto_try_default_pwd) | 0x0C02BE44 | Try each stored 16-byte pairing key against the challenge until one authenticates |
| [`ble_ecc_ctx_release`](#ble_ecc_ctx_release) | 0x0C05BA4C | Release an ECC context: wc_ecc_free, free its temporary point and zero 512 bytes |
| [`ble_ecc_heap_alloc`](#ble_ecc_heap_alloc) | 0x0C05CBA4 | Allocate a block of the given size from the BLE crypto heap pool at DAT_200049A8 |
| [`ble_ecc_heap_free`](#ble_ecc_heap_free) | 0x0C05CBA0 | Release a block to the BLE crypto heap pool at DAT_200049A8 |
| [`ble_ecc_p224_export_derive`](#ble_ecc_p224_export_derive) | 0x0C05BBCC | Export the P-224 point at ctx+0x1FC and derive two 32-byte secrets from its X coordinate |
| [`ble_ecc_point_add_mont`](#ble_ecc_point_add_mont) | 0x0C05B724 | Add two projective ECC points in Montgomery form and write the result to param_1 |
| [`ble_ecc_scalar_base_mult`](#ble_ecc_scalar_base_mult) | 0x0C05B86C | Derive a scalar in 1..n-1 from 36 bytes and multiply the point at param_3 by it |
| [`ble_ecc_share_derive`](#ble_ecc_share_derive) | 0x0C05BAF0 | Import the peer's P-224 point, combine it with the context point and build the 60-byte share record |
| [`ble_rng_get_32`](#ble_rng_get_32) | 0x0C05C10C | Fill 32 bytes at param_1 with random data from a temporary RNG context |
| [`ble_secure_blob_wipe_1k`](#ble_secure_blob_wipe_1k) | 0x0C053EE4 | Clear the 1 KB secure buffer at 0x20011A10 through the wipe helper |
| [`ble_secure_ctx_restore_from_nv`](#ble_secure_ctx_restore_from_nv) | 0x0C053A48 | Verify and unwrap the stored secure context at boot and rebuild its RAM copies |
| [`ble_sha1_mix_pair16`](#ble_sha1_mix_pair16) | 0x0C04920C | SHA-1 over two 16-byte inputs (built-in defaults for NULL), keeping 16 digest bytes |
| [`ble_sha1_oneshot`](#ble_sha1_oneshot) | 0x0C04AA80 | One-shot SHA-1 of a buffer into a 20-byte digest, wiping the context on exit |
| [`ble_sha1_oneshot_thunk`](#ble_sha1_oneshot_thunk) | 0x0C04AAE8 | Thunk: branch to ble_sha1_oneshot at 0x0C04AA80 |
| [`btstack_crypto_aes128_encrypt`](#btstack_crypto_aes128_encrypt) | 0x0C065038 | Queue an AES-128 block encryption (type 1, HCI LE Encrypt) and run the crypto request loop |
| [`btstack_crypto_ccm_next_block`](#btstack_crypto_ccm_next_block) | 0x0C0645EC | Advance an AES-CCM request to its next 16-byte block, finishing it when done |
| [`btstack_crypto_ccm_submit`](#btstack_crypto_ccm_submit) | 0x0C065078 | Queue an AES-CCM request (type 3) and run the crypto job pump |
| [`btstack_crypto_cmac_step`](#btstack_crypto_cmac_step) | 0x0C06464C | Advance the BTstack AES-CMAC (RFC 4493) operation: subkeys, CBC-MAC blocks, final block |
| [`btstack_crypto_ecc_p256_calculate_dhkey`](#btstack_crypto_ecc_p256_calculate_dhkey) | 0x0C065108 | Queue a P-256 ECDH request (remote public key in, shared secret out) |
| [`btstack_crypto_ecc_p256_generate_key`](#btstack_crypto_ecc_p256_generate_key) | 0x0C0650C0 | Queue a P-256 local public-key read and copy the 64-byte result to the caller |
| [`btstack_crypto_random_generate`](#btstack_crypto_random_generate) | 0x0C064FFC | Queue a random-bytes request (type 0, LE Rand) on the crypto list and run it |
| [`crc32_compute_poly`](#crc32_compute_poly) | 0x0C02C454 | CRC-32 (reflected, init/xorout 0xffffffff) of a buffer using a table built for a given polynomial |
| [`crc32_make_table`](#crc32_make_table) | 0x0C02C3FC | Build the 256-entry reflected CRC-32 lookup table for a given polynomial |
| [`crypto_tea_cbc_decrypt`](#crypto_tea_cbc_decrypt) | 0x0C036418 | TEA (32-round) decryption of a buffer in place with CBC-style chaining |
| [`ecc_check_privkey_gen`](#ecc_check_privkey_gen) | 0x0C05FF44 | Check a private key by recomputing k*G and comparing it with the stored public key |
| [`ecc_check_pubkey_order`](#ecc_check_pubkey_order) | 0x0C05F830 | Check that order * Q is the point at infinity (encoded as x = y = 0) for a public key |
| [`ecc_field_inv_fermat`](#ecc_field_inv_fermat) | 0x0C063D2C | Field inverse by Fermat: result = base^(m-2) mod m with an 8-entry run-of-ones table |
| [`ecc_field_inv_fermat_thunk`](#ecc_field_inv_fermat_thunk) | 0x0C0640F4 | Branch-only alias of ecc_field_inv_fermat (base^(m-2) mod m) |
| [`ecc_make_pub_ex`](#ecc_make_pub_ex) | 0x0C05FD18 | Compute the public point k*G for a private key, check its order, and set the key type |
| [`ecc_map_ex`](#ecc_map_ex) | 0x0C05EFC0 | Map a Jacobian point to affine (x*z^-2, y*z^-3, z=1); infinity is encoded as (0, 0, 1) |
| [`ecc_mulmod_ex`](#ecc_mulmod_ex) | 0x0C05F71C | Scalar multiply R = k * P without blinding; optional affine mapping of the result |
| [`ecc_mulmod_ex2`](#ecc_mulmod_ex2) | 0x0C05F8C4 | Blinded scalar multiply R = k * G: k + order blinding, optional RNG, optional affine map |
| [`ecc_mulmod_ex_thunk`](#ecc_mulmod_ex_thunk) | 0x0C05F818 | Branch-only alias of ecc_mulmod_ex; the argument registers pass straight through |
| [`ecc_mulmod_ladder_ct`](#ecc_mulmod_ladder_ct) | 0x0C05F338 | Constant-time Montgomery-ladder scalar multiply over a table of points, optional RNG blinding |
| [`ecc_point_on_curve_check`](#ecc_point_on_curve_check) | 0x0C060828 | Test y^2 == x^3 - 3x + b (mod p) for the point at param 1; returns 0 when it is on the curve |
| [`ecc_point_to_montgomery`](#ecc_point_to_montgomery) | 0x0C05E558 | Convert the X, Y and Z coordinates of a point to Montgomery form |
| [`ecc_projective_add_point`](#ecc_projective_add_point) | 0x0C05EB00 | Add two Jacobian points, R = P + Q, with constant-time field helpers; equal inputs double |
| [`ecc_projective_dbl_point`](#ecc_projective_dbl_point) | 0x0C05E868 | Double a Jacobian point (a = -3 shortcut): out = 2 * in, with constant-time field operations |
| [`ecc_randomize_projective`](#ecc_randomize_projective) | 0x0C05F28C | Re-randomise a point's projective coordinates with a random factor r (Z*=r, X*=r^2, Y*=r^3) |
| [`ecc_shared_secret`](#ecc_shared_secret) | 0x0C05FB10 | ECDH core: X coordinate of (private scalar * peer point) written to the output buffer |
| [`ecc_verify_hash_ex`](#ecc_verify_hash_ex) | 0x0C0601FC | ECDSA verify core: check x(u1*G + u2*Q) mod n against r and set *res |
| [`fp_add`](#fp_add) | 0x0C061FE8 | Signed big-integer add c = a + b (wolfSSL TFM fp_add) using s_fp_add / s_fp_sub |
| [`fp_add_d`](#fp_add_d) | 0x0C06428C | Add a single 32-bit digit to a big integer magnitude: c = a + b |
| [`fp_add_thunk`](#fp_add_thunk) | 0x0C064088 | Branch-only alias of fp_add (signed big-integer addition) |
| [`fp_addmod_ct`](#fp_addmod_ct) | 0x0C062654 | Constant-time modular addition d = (a + b) mod c for a, b < c |
| [`fp_addmod_ct_thunk`](#fp_addmod_ct_thunk) | 0x0C0640E8 | Branch-only alias of fp_addmod_ct (constant-time modular addition) |
| [`fp_clear`](#fp_clear) | 0x0C063FEC | Zero a big integer in place (NULL-safe, no return value) |
| [`fp_cmp`](#fp_cmp) | 0x0C0628B4 | Signed comparison of two big integers |
| [`fp_cmp_mag_ct`](#fp_cmp_mag_ct) | 0x0C061E14 | Constant-time magnitude compare of two fp_int digit arrays |
| [`fp_div`](#fp_div) | 0x0C062FE4 | Divide two fp_ints: quotient c = a / b and remainder d = a mod b (Knuth algorithm D) |
| [`fp_div_2`](#fp_div_2) | 0x0C0623CC | Halve a big integer b = a / 2 by a one-bit right shift from the top digit down (wolfSSL) |
| [`fp_div_2_mod_ct`](#fp_div_2_mod_ct) | 0x0C062450 | Constant-time modular halving c = (a / 2) mod b for 0 <= a < b (wolfSSL fp_div_2_mod_ct) |
| [`fp_div_2_mod_ct_thunk`](#fp_div_2_mod_ct_thunk) | 0x0C064498 | Branch-only alias of fp_div_2_mod_ct (constant-time halving modulo b) |
| [`fp_div_2d`](#fp_div_2d) | 0x0C062F28 | Divide a big integer by 2^b giving quotient and optional remainder |
| [`fp_invmod`](#fp_invmod) | 0x0C0635AC | Modular inverse c = a^-1 mod b (TFM fp_invmod): odd modulus uses binary extended Euclid |
| [`fp_invmod_thunk`](#fp_invmod_thunk) | 0x0C0640F0 | Branch-only alias of fp_invmod (modular inverse c = a^-1 mod b) |
| [`fp_lshd`](#fp_lshd) | 0x0C062D08 | Shift a big integer left by whole 32-bit digits |
| [`fp_mod`](#fp_mod) | 0x0C0634C4 | Modular reduction c = a mod b with the remainder taking the sign of b |
| [`fp_mod_2d`](#fp_mod_2d) | 0x0C0624E8 | Big integer modulo a power of two: c = a mod 2^b |
| [`fp_mod_thunk`](#fp_mod_thunk) | 0x0C0640EC | Branch-only alias of fp_mod (c = a mod b, remainder takes the sign of b) |
| [`fp_montgomery_calc_normalization`](#fp_montgomery_calc_normalization) | 0x0C062940 | Compute a = R mod b (R = 2^(32*used)) for Montgomery normalisation |
| [`fp_montgomery_calc_normalization_thunk`](#fp_montgomery_calc_normalization_thunk) | 0x0C064288 | Branch-only alias of fp_montgomery_calc_normalization (R mod b) |
| [`fp_montgomery_reduce`](#fp_montgomery_reduce) | 0x0C062A28 | Montgomery reduction x = x * R^-1 mod m, word by word, with a final conditional subtract of m |
| [`fp_montgomery_reduce_thunk`](#fp_montgomery_reduce_thunk) | 0x0C064450 | Two-instruction wrapper that calls fp_montgomery_reduce and returns |
| [`fp_mul`](#fp_mul) | 0x0C062218 | Multiply two fp_ints, c = a * b (comba column accumulation); fails when the digit sum exceeds 23 |
| [`fp_mul_2`](#fp_mul_2) | 0x0C0620DC | Double a big integer b = a * 2 by a one-bit left shift across the digits (wolfSSL fp_mul_2) |
| [`fp_mul_2d`](#fp_mul_2d) | 0x0C062D84 | Multiply a big integer by 2^b: c = a << b |
| [`fp_mul_checked`](#fp_mul_checked) | 0x0C064090 | Checked multiply c = a * b: rejects digit sums above 24, then fp_mul and clears stale digits |
| [`fp_mul_comba24`](#fp_mul_comba24) | 0x0C06237C | Fixed-capacity multiply wrapper c = a * b for digit sums up to 24; clears stale digits of c |
| [`fp_mul_d`](#fp_mul_d) | 0x0C062168 | Multiply a big integer by a single 32-bit digit: c = a * b |
| [`fp_mulmod`](#fp_mulmod) | 0x0C06353C | Modular multiply c = a * b mod m for total digit counts up to 24 |
| [`fp_mulmod_thunk`](#fp_mulmod_thunk) | 0x0C0640E0 | Branch-only alias of fp_mulmod (modular multiply c = a * b mod m) |
| [`fp_read_radix`](#fp_read_radix) | 0x0C0642F8 | Parse an ASCII number of radix 2..64 (fast path for hex) into a big integer |
| [`fp_read_unsigned_bin`](#fp_read_unsigned_bin) | 0x0C062BAC | Load a big-endian byte string into a big integer |
| [`fp_rshb`](#fp_rshb) | 0x0C062EA8 | Shift a big integer right by x bits in place |
| [`fp_rshb_thunk`](#fp_rshb_thunk) | 0x0C064284 | Branch-only alias of fp_rshb (in-place right shift by bits) |
| [`fp_rshd`](#fp_rshd) | 0x0C062E40 | Shift a big integer right by whole 32-bit digits |
| [`fp_sqr`](#fp_sqr) | 0x0C062880 | Square wrapper b = a^2: runs fp_sqr_comba and clears stale digits of b above the new used count |
| [`fp_sqr_comba`](#fp_sqr_comba) | 0x0C0626F4 | Square a fp_int, b = a^2, with the comba method that doubles the cross products |
| [`fp_sqr_thunk`](#fp_sqr_thunk) | 0x0C06444C | Branch-only alias of fp_sqr (b = a^2, stale high digits cleared) |
| [`fp_sub`](#fp_sub) | 0x0C062068 | Signed big-integer subtract c = a - b (wolfSSL TFM fp_sub) using s_fp_add / s_fp_sub |
| [`fp_sub_d`](#fp_sub_d) | 0x0C063CE4 | Subtract a 32-bit digit from a big integer: c = a - d |
| [`fp_sub_d_thunk`](#fp_sub_d_thunk) | 0x0C064230 | Branch-only alias of fp_sub_d (c = a - d) |
| [`fp_sub_thunk`](#fp_sub_thunk) | 0x0C06408C | Branch-only alias of fp_sub (signed big-integer subtraction) |
| [`fp_submod_ct`](#fp_submod_ct) | 0x0C0625A0 | Constant-time modular subtraction d = (a - b) mod c for a, b < c |
| [`fp_submod_ct_thunk`](#fp_submod_ct_thunk) | 0x0C0640E4 | Branch-only alias of fp_submod_ct (constant-time modular subtraction) |
| [`fp_to_unsigned_bin`](#fp_to_unsigned_bin) | 0x0C062C84 | Export a fp_int as big-endian bytes: emit little-endian then reverse in place |
| [`fp_to_unsigned_bin_at_pos`](#fp_to_unsigned_bin_at_pos) | 0x0C062C20 | Append a big integer's bytes (least significant first) at an offset |
| [`fp_to_unsigned_bin_thunk`](#fp_to_unsigned_bin_thunk) | 0x0C0641F0 | Branch-only alias of fp_to_unsigned_bin (big-endian export of a big integer) |
| [`get_digit`](#get_digit) | 0x0C0644C8 | Read digit n of a big integer (0 when out of range) |
| [`get_digit_count`](#get_digit_count) | 0x0C0644C0 | Number of used digits in a big integer (NULL-safe) |
| [`hash_drbg_kat_generate`](#hash_drbg_kat_generate) | 0x0C0615C0 | Known-answer self-test: instantiate, generate twice, return the 128-byte second output |
| [`hsm_trng_read_bytes`](#hsm_trng_read_bytes) | 0x0C033328 | Fill a buffer with hardware TRNG bytes, polling the HSM TRNG status register |
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
| [`wc_AesGcmEncrypt`](#wc_aesgcmencrypt) | 0x0C05E2C0 | Validate AES-GCM encrypt arguments, then run the software GCM encrypt |
| [`wc_AesGcmSetKey`](#wc_aesgcmsetkey) | 0x0C05DBE0 | Set a 16-byte AES-GCM key: expand the key and compute the GHASH key H = E_K(0^128) |
| [`wc_AesInit`](#wc_aesinit) | 0x0C05E338 | Initialise an Aes context: store heap pointer (device id unused) |
| [`wc_AesSetKeyLocal`](#wc_aessetkeylocal) | 0x0C05D8F8 | AES-128 key expansion into the Aes context (+ inverse key for decrypt) and IV set (wolfSSL) |
| [`wc_FreeRng`](#wc_freerng) | 0x0C06156C | Wipe and free the Hash_DRBG object of an RNG; returns -199 if the wipe did not zero it |
| [`wc_HashFinal`](#wc_hashfinal) | 0x0C060D80 | Finish a wolfSSL hash of a given type into a digest buffer; only SHA-256 (type 6) is implemented |
| [`wc_HashFree`](#wc_hashfree) | 0x0C060DAC | Free a wc_HashAlg by type: only SHA-256 (type 6) is built in (wolfSSL wc_HashFree) |
| [`wc_HashGetDigestSize`](#wc_hashgetdigestsize) | 0x0C060CE0 | Digest size in bytes for a wolfSSL hash type |
| [`wc_HashInit`](#wc_hashinit) | 0x0C060D0C | Initialise a wolfSSL hash context for a given hash type (SHA-256 only) |
| [`wc_HashUpdate`](#wc_hashupdate) | 0x0C060D3C | Feed bytes into a wolfSSL hash context of a given type; only SHA-256 (type 6) is implemented |
| [`wc_HmacFinal`](#wc_hmacfinal) | 0x0C060F58 | Finish HMAC-SHA-256: H((K ^ opad) \|\| H((K ^ ipad) \|\| message)) written to the output |
| [`wc_HmacFree`](#wc_hmacfree) | 0x0C06100C | Free an Hmac context: for macType SHA-256 (6) release the inner hash (wolfSSL wc_HmacFree) |
| [`wc_HmacInit`](#wc_hmacinit) | 0x0C060FEC | Zero a 0x118-byte Hmac context and store its heap pointer (wolfSSL wc_HmacInit) |
| [`wc_HmacSetKey`](#wc_hmacsetkey) | 0x0C060DE0 | Key an HMAC-SHA-256: build the ipad and opad blocks, hashing keys longer than 64 bytes first |
| [`wc_HmacUpdate`](#wc_hmacupdate) | 0x0C060EF4 | Absorb message bytes into an HMAC-SHA-256; the first update hashes the ipad block |
| [`wc_InitRng`](#wc_initrng) | 0x0C061828 | wolfSSL wc_InitRng(rng): seed and instantiate the RNG with no nonce, discarding the status |
| [`wc_InitSha256`](#wc_initsha256) | 0x0C061DB0 | Initialise a SHA-256 context |
| [`wc_RNG_GenerateBlock`](#wc_rng_generateblock) | 0x0C061834 | Generate up to 65536 random bytes; reseed from the entropy source when the DRBG asks for it |
| [`wc_RNG_TestSeed`](#wc_rng_testseed) | 0x0C061500 | Continuous test on RNG seed: reject repeated adjacent 4-byte blocks |
| [`wc_Sha256Final`](#wc_sha256final) | 0x0C061C80 | Finish SHA-256: pad with 0x80 and bit length, write digest big-endian, reset to IV |
| [`wc_Sha256Free`](#wc_sha256free) | 0x0C061E10 | Free a SHA-256 context (empty in this build) |
| [`wc_Sha256Update`](#wc_sha256update) | 0x0C061B7C | Absorb bytes into a SHA-256 context: fill and transform 64-byte blocks, count bytes in loLen/hiLen |
| [`wc_X963_KDF`](#wc_x963_kdf) | 0x0C060BE8 | ANSI X9.63 KDF: out = Hash(Z \|\| counter \|\| SharedInfo) blocks with a counter from 1 (SHA-256 only) |
| [`wc_ecc_check_key`](#wc_ecc_check_key) | 0x0C060974 | Validate an ECC key: coordinates in range, point on curve, point order, and private scalar range |
| [`wc_ecc_copy_point`](#wc_ecc_copy_point) | 0x0C05F1D8 | Copy an ecc_point (x, y, z big integers) into another (wolfSSL wc_ecc_copy_point) |
| [`wc_ecc_curve_free`](#wc_ecc_curve_free) | 0x0C05E4E8 | Clear the loaded curve parameters of an ecc_curve_spec according to its load_mask |
| [`wc_ecc_curve_load`](#wc_ecc_curve_load) | 0x0C05E614 | Load selected fields of a standard ECC curve into an ecc_curve_spec |
| [`wc_ecc_del_point`](#wc_ecc_del_point) | 0x0C05F1B0 | Zero the three coordinates of an ecc_point and free it (wc_ecc_del_point) |
| [`wc_ecc_free`](#wc_ecc_free) | 0x0C0601D0 | Release an ecc_key: clear pubkey.x/y/z and force-zero the private scalar k (wolfSSL) |
| [`wc_ecc_gen_k`](#wc_ecc_gen_k) | 0x0C05F218 | Draw a random ECC scalar: size+8 RNG bytes read as an integer and reduced modulo the order |
| [`wc_ecc_import_x963_ex`](#wc_ecc_import_x963_ex) | 0x0C060AE4 | Import an ECC public key from an X9.63 uncompressed point (0x04 \|\| X \|\| Y) and validate it |
| [`wc_ecc_init`](#wc_ecc_init) | 0x0C060190 | Zero a 0x1bc-byte ecc_key and init its pubkey.x/y/z and private scalar k (wolfSSL wc_ecc_init) |
| [`wc_ecc_make_key_ex`](#wc_ecc_make_key_ex) | 0x0C0600C0 | Generate an ECC key pair: select the curve, draw k, derive the public point (wc_ecc_make_key_ex) |
| [`wc_ecc_new_point`](#wc_ecc_new_point) | 0x0C05F1A8 | Allocate a new ecc_point with no heap hint (wc_ecc_new_point) |
| [`wc_ecc_new_point_h`](#wc_ecc_new_point_h) | 0x0C05F164 | Allocate and zero an ecc_point (0x138 bytes) and initialise its three fp_ints |
| [`wc_ecc_set_curve`](#wc_ecc_set_curve) | 0x0C05E7FC | Select ECC curve parameters for a key by key size or curve id |
| [`wc_ecc_set_rng`](#wc_ecc_set_rng) | 0x0C060BD4 | Attach a random number generator to an ECC key |
| [`wc_ecc_shared_secret`](#wc_ecc_shared_secret) | 0x0C05FCCC | wc_ecc_shared_secret state machine: validate keys, run the ECDH core, retry on pending |
| [`wc_ecc_verify_hash`](#wc_ecc_verify_hash) | 0x0C060720 | wc_ecc_verify_hash state machine: decode the DER signature, then verify |
| [`wc_rng_seed_instantiate`](#wc_rng_seed_instantiate) | 0x0C061688 | Init an RNG: DRBG known-answer checks, TRNG entropy with a continuous test, then instantiate |

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
- Called by: `wc_AesGcmEncrypt`
- Calls: `wc_AesEncrypt`, `GHASH`, `memcpy`
- Confidence: high

## DecodeECC_DSA_Sig

**Parse a DER ECDSA signature SEQUENCE into its r and s integers**

wolfSSL DecodeECC_DSA_Sig. It requires the first byte to be 0x30 (SEQUENCE tag), reads the SEQUENCE length with GetLength_ex (0x0C05E350) and checks that it fits the buffer. It then decodes two consecutive INTEGERs with GetInt (0x0C05E420), the first into r (param_3) and the second into s (param_4). If anything fails it clears r with fp_clear and returns -171 (0xFFFFFF55). Returns 0 when both integers parse.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DER signature buffer |
| `param_2` | `s32` | buffer length in bytes |
| `param_3` | `ptr` | mp_int r output |
| `param_4` | `ptr` | mp_int s output |

**Returns** `s32`: 0 on success, -171 on malformed input

**Notes:** The wolfSSL identification is inferred from the SEQUENCE plus two INTEGER structure and the argument order.

- Addresses by version: 219: 0x0C05E474
- Called by: `wc_ecc_verify_hash`
- Calls: `GetLength_ex`, `GetInt`, `fp_clear`
- Confidence: medium

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
- Called by: `GetInt`
- Calls: `GetLength_ex`
- Confidence: high

## GetInt

**Parse one ASN.1 DER INTEGER at an index and load it into a big integer**

wolfSSL asn.c GetInt. GetASNInt (0x0C05E3B8) reads the INTEGER header at input[*idx], skips a leading 0x00 pad byte and returns the content length. The destination is then mp_init()ed and the magnitude is loaded big-endian with mp_read_unsigned_bin (reached through a thunk at 0x0C062BAC). On success *idx is advanced by header plus content length and 0 is returned. If the load fails the integer is cleared with fp_clear; the error paths return -142 (ASN parse error) or -110 (mp_init failure). The value is always non-negative because the sign is not decoded.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination mp_int |
| `param_2` | `ptr` | DER input buffer |
| `param_3` | `ptr` | in/out byte index into the input |

**Returns** `s32`: 0 on success, -110 on mp_init failure, -142 on parse or load failure

- Addresses by version: 219: 0x0C05E420
- Called by: `DecodeECC_DSA_Sig`
- Calls: `GetASNInt`, `mp_init`, `fp_clear`, `mp_read_unsigned_bin`
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
- Called by: `GetASNInt`, `DecodeECC_DSA_Sig`
- Confidence: high

## Hash_DRBG_Generate

**Hash_DRBG generate: stream SHA-256 of V with a counter, run a repeat test, then update V**

wolfSSL Hash_DRBG_Generate with a continuous test. It returns 2 (reseed needed) when the reseed counter at +0x00 equals 1000000. Otherwise it produces outLen bytes in 32-byte blocks: each block is SHA-256 of a local copy of V, copied to out (truncated on the last block), and the copy of V is incremented as a 55-byte big-endian number. The continuous test compares the first 32-bit word of each block with the previous one, kept at +0x04. The first repeat sets the flag at +0x76 and costs one extra block, and a second repeat fails with 1. After the output H = SHA-256(0x03 || V) is computed and V := V + H + C + counter (mod 2^440), following the SP 800-90A step, then the reseed counter at +0x00 is incremented. The counter, the previous-block word and the flag live in the same DRBG object that Instantiate and Reseed set up.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DRBG object |
| `param_2` | `ptr` | output buffer |
| `param_3` | `u32` | number of bytes to produce |

**Returns** `u32`: 0 on success, 1 on a hash or continuous-test failure, 2 when a reseed is required

**Notes:** The V update step (V + H + C + counter) is read from the decompile and not checked against a reference. The reseed-required value 1000000 is taken as the wolfSSL reseed interval.

- Addresses by version: 219: 0x0C061270
- Called by: `hash_drbg_kat_generate`, `wc_RNG_GenerateBlock`
- Calls: `wc_Sha256Update`, `wc_Sha256Final`, `wc_InitSha256`, `wc_Sha256Free`, `memcpy`
- Confidence: medium

## Hash_DRBG_Instantiate

**Instantiate a Hash_DRBG: V = Hash_df(entropy || nonce), C = Hash_df(0x00 || V), counter = 1**

wolfSSL Hash_DRBG_Instantiate. It zeroes the 0x78-byte DRBG object. V (55 bytes at +0x08) is derived with Hash_df using tag 0x04 (no tag) over the entropy (param 2 and 3) and the nonce or personalisation string (param 4 and 5). C (55 bytes at +0x3f) is then Hash_df(0x00 || V). The reseed counter at +0x00 is set to 1 and the word at +0x04 (the previous output block for the continuous test) and the flag byte at +0x76 are cleared. Layout of the DRBG object: counter +0, previous block +4, V +8..+62, C +63..+117, flag +118.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DRBG object (0x78 bytes) |
| `param_2` | `ptr` | entropy input |
| `param_3` | `u32` | entropy length |
| `param_4` | `ptr` | nonce or personalisation string, may be NULL |
| `param_5` | `u32` | its length |

**Returns** `u32`: 0 on success, 1 if either Hash_df fails

- Addresses by version: 219: 0x0C061174
- Called by: `hash_drbg_kat_generate`, `wc_rng_seed_instantiate`
- Calls: `Hash_df`, `memset`
- Confidence: high

## Hash_DRBG_Reseed

**Reseed a Hash_DRBG: V = Hash_df(0x01 || V || entropy), C = Hash_df(0x00 || V), counter reset to 1**

wolfSSL Hash_DRBG_Reseed. A new V is computed into a 55-byte temporary as Hash_df with tag 0x01 over the current V and the supplied entropy, then copied into V and the temporary is zeroed. C is recomputed as Hash_df(0x00 || V). The reseed counter at +0x00 is set to 1, the word at +0x04 and the flag byte at +0x76 are cleared.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | DRBG object |
| `param_2` | `ptr` | fresh entropy input |
| `param_3` | `u32` | entropy length |

**Returns** `u32`: 0 on success, 1 if a Hash_df fails

- Addresses by version: 219: 0x0C0611D0
- Called by: `hash_drbg_kat_generate`, `wc_RNG_GenerateBlock`
- Calls: `Hash_df`, `memset`
- Confidence: high

## Hash_df

**NIST SP 800-90A Hash_df: derive 55 bytes from two SHA-256 blocks over a counter, tag and two inputs**

wolfSSL Hash_df from random.c. It produces the 55-byte seed (0x37, 440 bits) in two SHA-256 blocks. Block i (counter byte 1, then 2) hashes the counter, the 4-byte big-endian bit length 0x000001B8 (440), an optional tag byte (param 2, omitted when it equals 0x04), input 1 and, when non-NULL, input 2. Each digest is appended to out: 32 bytes for the first block and the remaining 23 for the second. Each block uses a fresh SHA-256 context (wc_InitSha256, wc_Sha256Update, wc_Sha256Final, wc_Sha256Free). Callers are Hash_DRBG_Instantiate (V with tag 0x04, C with tag 0x00) and Hash_DRBG_Reseed (tag 0x01).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output, 55 bytes |
| `param_2` | `u8` | tag byte; 0x04 means no tag |
| `param_3` | `ptr` | input 1 |
| `param_4` | `u32` | input 1 length |
| `param_5` | `ptr` | input 2, may be NULL |
| `param_6` | `u32` | input 2 length |

**Returns** `bool`: true (1) when any SHA-256 step failed, false (0) on success

- Addresses by version: 219: 0x0C061034
- Called by: `Hash_DRBG_Instantiate`, `Hash_DRBG_Reseed`
- Calls: `wc_Sha256Update`, `wc_Sha256Final`, `wc_InitSha256`, `wc_Sha256Free`, `memcpy`
- Confidence: high

## Transform_Sha256

**SHA-256 compression: process one 64-byte block into the eight-word state**

wolfSSL Transform_Sha256, the SHA-256 block function. It allocates a 256-byte message schedule on the heap (malloc 0x100) and copies the 16 message words from the block (param 2) into it. The schedule is extended to 64 words with sigma0 (rotr7 ^ rotr18 ^ shr3) and sigma1 (rotr17 ^ rotr19 ^ shr10). The 64 rounds use the SHA-256 round constants at 0x0c074668 and keep the eight working variables in a stack array that rotates index by index. At the end the working variables are added to the state (param 1 digest words) and the schedule is freed. The caller has already converted the buffer words to host order.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | SHA-256 context; digest words at +0x00 |
| `param_2` | `ptr` | 64-byte block, words in host order |

**Returns** `s32`: 0 on success, -125 (0xffffff83) if the schedule cannot be allocated

- Addresses by version: 219: 0x0C061950
- Called by: `wc_Sha256Update`, `wc_Sha256Final`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`
- Confidence: high

## aes128_encrypt_block

**AES-128 ECB encrypt of one 16-byte block, in place, using an expanded key**

Standard byte-oriented AES-128 encryption: initial AddRoundKey, nine rounds of SubBytes (S-box at 0x0C083E20), ShiftRows, MixColumns (GF(2^8) xtime with reduction constant 0x1B) and AddRoundKey, then a final round without MixColumns. param_1 is the 176-byte schedule from ble_219_0c048f3c and param_2 the 16-byte state which is overwritten with the ciphertext. Used by the BLE crypto wrappers (ble_219_0c049288, 0c0493d4, 0c0496a8), e.g. for AES-ECB/CCM-style operations and authentication.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | expanded round keys (176 bytes) |
| `param_2` | `ptr` | 16-byte block, encrypted in place |

- Addresses by version: 219: 0x0C048FD4
- Called by: `ble_crypto_ccm_cbc_mac`, `ble_crypto_ccm_seal_frame`, `ble_crypto_ccm_open_frame`
- Confidence: high

## aes128_key_expansion

**AES-128 key schedule: expand a 16-byte key into 176 bytes of round keys**

Copies the 16-byte key from param_2 to param_1, then generates words 4..43: each new word is the previous word XOR the word four positions back; every fourth word first applies RotWord, SubWord via the AES S-box at 0x0C083E20, and XORs the round constant from the table at 0x0C07482C (0x01,0x02,0x04,...,0x1B,0x36). Output is the 11 round keys (44 words = 176 bytes) at param_1. Called together with ble_219_0c048fd4 from the three AES wrappers ble_219_0c049288, 0c0493d4, 0c0496a8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output: 176-byte expanded key schedule |
| `param_2` | `ptr` | input: 16-byte AES-128 key |

- Addresses by version: 219: 0x0C048F3C
- Called by: `ble_crypto_ccm_cbc_mac`, `ble_crypto_ccm_seal_frame`, `ble_crypto_ccm_open_frame`
- Confidence: high

## ble_crypto_auth_derive_own_word

**Derive the local auth word as stored word XOR peer word, then send it as request type 0**

Clears busy and returns when the connection for handle param_1 is absent. It reads the 16-bit peer word from 0x2000FD94 at offset 0xE, big-endian, and sets the local word DAT_200100CE to DAT_200100D0 XOR peer. It zeroes the request block, writes type 0 at 0xC and the local word at 0xE, marks busy, and starts operation 0x0C065038 with output 0x2000FEC4, input 0x2000FFD9, completion callback 0x0C050068 and the connection's +0x1A8 parameter.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | connection handle |

- Addresses by version: 219: 0x0C04FA38
- Calls: `btstack_crypto_aes128_encrypt`, `co_read16_be`, `co_write16_be`, `ble_ctrl_conn_find_by_handle`
- Confidence: medium

## ble_crypto_auth_load_keys

**Load the 16-byte auth keys from the key store, set the mode, and fall back to generating one**

When param_1 is nonzero, it first writes the 16-byte block at 0x2000FEC4 back to the store under tag 0x534D4552 (the bytes 'REMS' in memory order) using the store's put method. It then clears the failure flag DAT_2000FEF4 and reads the 16-byte record for tag 0x534D4952 ('RIMS') into 0x2000FED4. If that read returns 16 bytes, the mode byte DAT_2000FD14 becomes 1 and the second record is attempted (mode 2 when DAT_2000FF40 is set). Otherwise the failure flag is set and operation 0x0C064FFC is started over 0x2000FED4 with callback 0x0C050120. If DAT_2000FEB0 is set, the timer at 0x2000FF0C is re-armed with zero delay.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | nonzero to persist the 0x2000FEC4 record before loading |

**Notes:** Potential defect: the second key record and the constant defaults are loaded through util_nop_stub_b (0x0C065CE0), which the stub annotation describes as a bare return. If so, the copies from 0x0C084200, 0x0C084204 and 0x0C0768A0 do nothing and mode 2 uses an unloaded 0x2000FEE4. Verify the disassembly of 0x0C065CE0 before trusting the key loading.

- Addresses by version: 219: 0x0C050310
- Calls: `btstack_crypto_random_generate`, `btstack_run_loop_set_timer`, `btstack_run_loop_add_timer`, `btstack_run_loop_remove_timer`, `util_nop_stub_b`
- Confidence: medium

## ble_crypto_auth_pubkey_begin

**Store a 65-byte key block (X, Y, flag) and start an operation over it with a 16-byte value**

Copies param_2 (32 bytes) to 0x2000FE00 as X and param_3 (32 bytes) to 0x2000FE20 as Y, writes param_5 into the byte at 0x2000FE40, and records param_1 at DAT_2000FDC8. The resulting 65-byte block is the size of an uncompressed P-256 public key, so this may be the start of an LE Secure Connections key exchange. It arms DAT_2000FDC6, sets the callback at DAT_2000FDCC to 0x0C0503F4, and starts operation 0x0C065078 with the 16-byte value param_4, the key block, the output at DAT_2000FDD0 and completion callback 0x0C04FD4C. The two calls to util_nop_stub_a in the body do nothing.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | context value stored at DAT_2000FDC8 |
| `param_2` | `ptr` | X coordinate, 32 bytes |
| `param_3` | `ptr` | Y coordinate, 32 bytes |
| `param_4` | `ptr` | 16-byte value passed to the operation |
| `param_5` | `u8` | flag byte stored at 0x2000FE40 |

**Notes:** The public-key reading is an inference from the 65-byte size. The roles of the 16-byte value and the flag are not determined. Operation 0x0C065078 is not in this packet.

- Addresses by version: 219: 0x0C04F894
- Called by: `sm_pairing_engine_step`
- Calls: `btstack_crypto_ccm_submit`, `util_nop_stub_a`
- Confidence: low

## ble_crypto_auth_send_word_type1

**Send the local 16-bit auth word as request type 1 on the crypto channel**

Clears the busy byte DAT_2000FDC4 and looks up the connection for handle param_1; it does nothing when the connection is absent. Otherwise it zeroes the 16-byte request block at 0x2000FDB4, writes type 1 at offset 0xC and the local word DAT_200100CE, big-endian, at offset 0xE, marks busy, and starts operation 0x0C065038 with output 0x2000FEC4, input 0x200100EA, completion callback 0x0C050618 and the connection's +0x1A8 parameter. The call to util_nop_stub_b in the body copies nothing.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | connection handle |

**Notes:** The stub call (copy from 0x0C0841F8 to 0x2000FFD9) is a no-op if util_nop_stub_b really is a bare return. See notes on ble_crypto_auth_load_keys.

- Addresses by version: 219: 0x0C04F9B0
- Calls: `btstack_crypto_aes128_encrypt`, `co_write16_be`, `util_nop_stub_b`, `ble_ctrl_conn_find_by_handle`
- Confidence: medium

## ble_crypto_auth_start_by_mode

**Start the crypto operation for the current auth mode: type 0 with value 1 (mode 1) or 3 (mode 2)**

Reads the mode byte DAT_2000FD14, set by ble_crypto_auth_load_keys to 1 or 2. In mode 1, when the busy byte DAT_2000FDC4 is clear, it zeroes the request block, writes type 0 and value 1, and starts operation 0x0C065038 with input 0x2000FEE4 and completion callback 0x0C04FCAC. In mode 2 it writes type 0 and value 3, uses input 0x2000FEB4 and callback 0x0C04FCFC. Both set busy, use output 0x2000FED4, and return 1. Any other mode, or a busy operation, returns 0.

**Returns** `u8`: 1 when an operation was started, 0 otherwise

**Notes:** The meaning of the mode values and of the 16-byte inputs (fee4 and feb4) follows from ble_crypto_auth_load_keys. The mode 2 input (0x2000FEB4) is not loaded by ble_crypto_auth_load_keys, which may leave it unset.

- Addresses by version: 219: 0x0C04FB64
- Called by: `sm_pairing_engine_step`
- Calls: `btstack_crypto_aes128_encrypt`, `co_write16_be`
- Confidence: medium

## ble_crypto_auth_step

**Advance the crypto-auth state machine: state 1 starts the address check, state 3 starts the next op**

The auth state byte DAT_2000FD78 drives the sequence. In state 1 it moves to state 2 and starts an operation (0x0C064FFC) on the 6-byte peer address at DAT_2000FEF8 with completion callback 0x0C04FEE4, returning 1. In state 3, when the busy byte DAT_2000FDC4 is clear, it copies the first three address bytes into the request block at DAT_2000FDC0, marks busy, and starts operation 0x0C065038 with the request block (zeroed at DAT_2000FDB4) and the output at DAT_2000FD94, with callback 0x0C04FE38. Any other state, or a busy operation, returns 0.

**Returns** `u32`: 1 when an operation was started, 0 otherwise

**Notes:** The operations started here (0x0C064FFC, 0x0C065038) are not in this packet. The state numbering is inferred from the transitions in this function.

- Addresses by version: 219: 0x0C04F7B8
- Called by: `sm_pairing_engine_step`
- Calls: `btstack_crypto_random_generate`, `btstack_crypto_aes128_encrypt`
- Confidence: medium

## ble_crypto_auth_store_xor_word

**Store peer XOR local as the shared auth word, then send the local word as request type 0**

Clears busy and returns when the connection for handle param_1 is absent. It reads the peer word from 0x2000FD94 at offset 0xE, big-endian, saves the current local word, and sets DAT_200100D0 to peer XOR local, which the derive step later reads. It zeroes the request block, writes type 0 at 0xC and the saved local word at 0xE, marks busy, and starts operation 0x0C065038 with output 0x2000FEC4, input 0x2000FFD9, completion callback 0x0C04F9B1 (the Thumb entry of ble_crypto_auth_send_word_type1) and the connection's +0x1A8 parameter.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | connection handle |

**Notes:** With ble_crypto_auth_derive_own_word, this forms a two-step XOR exchange of 16-bit words. Its completion path is ble_crypto_auth_send_word_type1.

- Addresses by version: 219: 0x0C04FACC
- Calls: `btstack_crypto_aes128_encrypt`, `co_read16_be`, `co_write16_be`, `ble_ctrl_conn_find_by_handle`
- Confidence: medium

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
- Called by: `ble_crypto_ccm_seal_frame`, `ble_crypto_ccm_open_frame`
- Calls: `aes128_key_expansion`, `aes128_encrypt_block`, `memcpy`
- Confidence: medium

## ble_crypto_ccm_open_frame

**Verify and decrypt a received CCM-style frame, accepting only a counter above the last one**

Inverse of ble_crypto_ccm_seal_frame with the same context; +0x18 holds the last accepted receive counter. It reads the 2-byte big-endian counter from the last two bytes of the frame and handles the 16-bit wrap. A counter above the stored value decrypts the payload, recomputes the 4-byte CBC-MAC, and compares it with the decrypted trailer. The stored counter advances only when the MIC matches. A counter not above the stored value is rejected with a result of 2, which reads as true. A counter of zero takes a separate path: the payload is decrypted with the same constant-block keystream and only the 16-bit sum in the trailer is checked, with no MIC. The header and decrypted payload go to param_4 and the payload length to *param_5.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | crypto context: key pointers, IV, last accepted counter |
| `param_2` | `ptr` | received frame |
| `param_3` | `s32` | received frame length |
| `param_4` | `ptr` | output buffer for header and plaintext |
| `param_5` | `ptr` | receives the payload length |

**Returns** `bool`: false on accept, true on reject (MIC or checksum mismatch, or replayed counter)

**Notes:** Security concern (medium confidence): a frame whose trailing counter is zero is accepted on an unkeyed 16-bit checksum with no MIC. Because the keystream is the same for every chunk, one known plaintext would reveal it. Confirm whether the caller filters counter zero before relying on this function.

- Addresses by version: 219: 0x0C0496A8
- Called by: `ble_rx_data_handler`, `ble_crypto_try_default_pwd`
- Calls: `aes128_key_expansion`, `aes128_encrypt_block`, `ble_sha1_mix_pair16`, `ble_crypto_ccm_cbc_mac`, `memcpy`
- Confidence: medium

## ble_crypto_ccm_seal_frame

**Encrypt and authenticate an outgoing frame: 3-byte header, CCM-style payload, 4-byte MIC, 2-byte counter**

The context holds pointers to two 16-byte keys at +0x00 and +0x04, which ble_sha1_mix_pair16 mixes into a session key; an 8-byte IV at +0x08; and the transmit counter at +0x18, which is incremented for each frame. The 3-byte header is copied through unchanged. With a nonzero counter, the payload is encrypted in 16-byte CCM counter-mode blocks (flags 0x01, the counter, the IV and a block index), and a 4-byte CBC-MAC over the header and plaintext (ble_crypto_ccm_cbc_mac) is XORed with keystream block 0. The output layout is header(3) | ciphertext | MIC(4) | counter(2, big-endian). With a counter of zero, the payload is XORed with AES of one fixed constant block for every 16-byte chunk, and the trailer carries a 16-bit one's-complement sum of the plaintext instead of a MIC.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | crypto context: key pointers, IV, transmit counter |
| `param_2` | `ptr` | input frame: 3-byte header then plaintext |
| `param_3` | `s32` | input frame length including the header |
| `param_4` | `ptr` | output frame buffer |

**Returns** `u32`: output frame length, truncated to 8 bits by the code

**Notes:** Security concern (medium confidence): in the zero-counter path the keystream is AES of the same constant block for every 16-byte chunk, so the keystream repeats across chunks and frames. The integrity check there is an unkeyed 16-bit sum. Check whether any pairing or connection state can produce a zero counter.

- Addresses by version: 219: 0x0C0493D4
- Calls: `aes128_key_expansion`, `aes128_encrypt_block`, `ble_sha1_mix_pair16`, `ble_crypto_ccm_cbc_mac`, `memcpy`
- Confidence: medium

## ble_crypto_diversify

**Diversify a 32-byte secret with a peer P-224 point into a 28-byte value**

Imports the peer's 57-byte P-224 point at param_2 (curve id 14) into a temporary key and validates it. It derives 72 bytes from the 32-byte secret at param_1 with the label 'diversify' (9 bytes) and splits them into two 36-byte scalars. It multiplies the stack point auStack_1C4 by the first scalar (0c05B86C) and the constant point built from curve block +0x1C/+0x20 (Z set to 1 with mp_set) by the second, adds the two with ble_ecc_point_add_mont, and on success exports the X coordinate (28 bytes) to param_3. Temporary points are released on all paths. The purpose is inferred from the label.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 32-byte secret |
| `param_2` | `ptr` | peer public point, 57 bytes |
| `param_3` | `ptr` | 28-byte output (X coordinate) |

**Returns** `s32`: 0 on success, else the first failing status

**Notes:** The curve block pointer is a stack local that the decompile does not show being set; the parameters of the scalar multiplications are read from that layout.

- Addresses by version: 219: 0x0C05BD30
- Called by: `ble_record_a_derive_and_commit`, `ble_record_b_derive_and_commit`
- Calls: `ble_ecc_point_add_mont`, `ble_ecc_scalar_base_mult`, `wc_ecc_new_point`, `wc_ecc_del_point`, `wc_ecc_init`, `wc_ecc_free`, `wc_ecc_check_key`, `wc_ecc_import_x963_ex`, `wc_X963_KDF`, `mp_to_unsigned_bin_len`, `fp_read_radix`, `mp_set`
- Confidence: low

## ble_crypto_ecdh_seal_p256

**ECDH-P256 seal: ephemeral key, KDF, AES-128-GCM, output ephemeral public key, ciphertext and tag**

Requires an output buffer of at least param_2 + 0x51 bytes, otherwise returns -1. It creates an ephemeral P-256 key pair (0c0600C0 make-key with curve 7, RNG attached with 0c060BD4) and computes the ECDH shared secret with the peer's 65-byte public key at param_1 (0c05FCCC, 32 bytes). It derives 32 bytes with 0c060BE8 from the secret and the 130-byte block ephemeral public key || peer public key; the first 16 bytes key AES-128-GCM (0c05DBE0) and the last 16 are the IV. The plaintext (param_3, param_2 bytes) is encrypted to param_5+0x41 with a 16-byte tag appended, and the ephemeral public key is written first as 0x04 || X || Y (65 bytes). *param_4 becomes param_2 + 0x51.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | peer public key, 65 bytes uncompressed P-256 |
| `param_2` | `u32` | plaintext length |
| `param_3` | `ptr` | plaintext |
| `param_4` | `ptr` | in/out: output capacity on entry, total output length on success |
| `param_5` | `ptr` | output: ephemeral public key, ciphertext, tag |

**Returns** `s32`: 0 on success, -1 for a short output buffer, else the first failing status

**Notes:** Called from 0c053954, 0c053A48 and 0c053E1C. The ECIES-style layout is inferred from the buffer offsets and the KDF input length of 0x82.

- Addresses by version: 219: 0x0C05C13C
- Called by: `ble_fmna_state_save`, `ble_secure_ctx_restore_from_nv`, `ble_session_msg_build`
- Calls: `wc_AesGcmSetKey`, `wc_AesGcmEncrypt`, `wc_AesInit`, `wc_AesFree`, `wc_ecc_shared_secret`, `wc_ecc_make_key_ex`, `wc_ecc_init`, `wc_ecc_free`, `wc_ecc_check_key`, `wc_ecc_import_x963_ex`, `wc_ecc_set_rng`, `wc_X963_KDF`, `wc_FreeRng`, `wc_InitRng`, `mp_to_unsigned_bin_len`, `memcpy`
- Confidence: medium

## ble_crypto_ecdsa_p256_verify

**Verify an ECDSA P-256 signature over the SHA-256 digest of a message**

Imports the 65-byte uncompressed P-256 public key at param_1 (curve id 7) into a temporary key and validates it. It hashes the message at param_5 (length param_4) with SHA-256 (init, update 0c061B7C, final 0c061C80) and calls 0c060720 with the signature at param_3 (length param_2), the 32-byte digest and the key, which presumably is wc_ecc_verify_hash. The verification counts only when the result flag equals 1. Returns 0 for a valid signature and -1 otherwise, freeing the key and hash context on every path.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 65-byte uncompressed P-256 public key |
| `param_2` | `u32` | signature length |
| `param_3` | `ptr` | signature |
| `param_4` | `u32` | message length |
| `param_5` | `ptr` | message |

**Returns** `s32`: 0 for a valid signature, -1 for an invalid one or a failure of the verify call

**Notes:** 0c060720 is presumably wc_ecc_verify_hash from its argument shape. Called from 0c053A48.

- Addresses by version: 219: 0x0C05BFA4
- Called by: `ble_secure_ctx_restore_from_nv`
- Calls: `wc_ecc_init`, `wc_ecc_free`, `wc_ecc_verify_hash`, `wc_ecc_check_key`, `wc_ecc_import_x963_ex`, `wc_Sha256Update`, `wc_Sha256Final`, `wc_InitSha256`, `wc_Sha256Free`, `mp_init`, `fp_clear`
- Confidence: medium

## ble_crypto_init

**Copy the vehicle serial number and seed the pairing crypto contexts at startup**

Reads the vehicle record from ble_219_0c059558 and logs 'INFO:ble_crypto_init, vehicle_sn[%s]'. It copies the 14-byte serial (record offset 0x18 to 0x25) to 0x20009404 and NUL-terminates it at 0x20009412, fills the 16-byte seed block at 0x200093F4 with ble_219_0c05b5c0, and initialises two SHA-1 style contexts from that block with sha1_ctx_init_with_seed, at 0x20009414 and 0x20009430. The 16-bit value at record offset 0x24 (the last two serial bytes) is also passed as an argument to the first initialisation. Finally it sets the crypto-ready flag DAT_200092EC to 1, stores the callback address 0x0C02BD44 with ble_cb_slot_15f28_set, and clears DAT_200091D4.

**Notes:** The 16-byte block at 0x200093F4 is the seed used by ble_crypto_try_default_pwd. Whether the u16 argument to the first sha1 init is a length or a counter is unclear. ble_219_0c05b5c0 is a 16-byte fill whose semantics (random or zero) are not known yet.

- Addresses by version: 219: 0x0C02BDD0
- Called by: `btle_connect_status_change`, `ble_app_init_callbacks_nv`, `ble_app_main_init`
- Calls: `btle_connect_status_change`, `trace_printf`, `sha1_ctx_init_with_seed`, `ble_link_table_get_base`, `ble_cb_slot_15f28_set`, `ble_random_fill_seeded`
- Confidence: medium

## ble_crypto_kdf_connect

**Two-step key derivation: 'intermediate' then 'connect', producing 16 bytes**

Derives a 32-byte intermediate from the key at param_1 with the label 'intermediate' (12 bytes) through 0c060BE8. If that succeeds it derives 16 bytes into param_2 from the intermediate with the label 'connect' (7 bytes). No status is returned and the output is left unchanged on the first failure.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 32-byte input key |
| `param_2` | `ptr` | 16-byte output |

**Notes:** Called from 0c053D04.

- Addresses by version: 219: 0x0C05BCE4
- Called by: `ble_record_a_derive_and_commit`
- Calls: `wc_X963_KDF`
- Confidence: high

## ble_crypto_kdf_update

**Derive 32 bytes from the 32-byte key at param_1 with the label 'update'**

Calls the key-derivation helper 0c060BE8 with SHA-256 (type 6), the 32-byte key at param_1, the 6-byte label 'update' and a 32-byte output at param_2. One of the four label-based derivations of the pairing and serial-protection group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 32-byte input key |
| `param_2` | `ptr` | 32-byte output |

**Notes:** Callers: 0c053C94, 0c053CCC, 0c053D04, 0c053DA4. 0c060BE8 is the shared KDF helper of the pairing group and is not described in this packet.

- Addresses by version: 219: 0x0C05BCC0
- Called by: `ble_record_a_reload`, `ble_record_b_reload`, `ble_record_a_derive_and_commit`, `ble_record_b_derive_and_commit`
- Calls: `wc_X963_KDF`
- Confidence: high

## ble_crypto_report_auth_state

**Post the pairing result event 0x0A or 0x0B when any key slot holds a valid key**

Does nothing unless at least one of the key-state bytes at 0x20008FF5, 0x20009006 and 0x20009017 equals '='. Otherwise it reads the authentication-failure byte in ble_get_state_ptr_42f8 + 0x2D and posts event 0x0B through ble_219_0c058a94 when it is not 1, or event 0x0A when it is 1.

**Notes:** The meaning of events 0x0A and 0x0B is not decoded, and ble_219_0c058a94 is not described yet.

- Addresses by version: 219: 0x0C02BF20
- Called by: `ble_rx_data_handler`
- Calls: `ble_get_state_ptr_42f8`, `ble_evt_report_conn_state_02`
- Confidence: medium

## ble_crypto_serial_mac

**HMAC-SHA256 over a message, keyed by a derivation of param_1 with 'SerialNumberProtection'**

Initialises an Hmac context (wc_HmacInit with devId -2) and derives a 32-byte HMAC key from the 32-byte key at param_1 with the label 'SerialNumberProtection' (22 bytes) using 0c060BE8. It sets that key for SHA-256 HMAC (type 6), feeds param_2 bytes from param_3 through wc_HmacUpdate, and writes the 32-byte tag to param_4 with wc_HmacFinal. The context is freed with wc_HmacFree on every path. This is the protection tag for the vehicle serial number.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 32-byte key material |
| `param_2` | `u32` | message length |
| `param_3` | `ptr` | message |
| `param_4` | `ptr` | 32-byte tag output |

**Returns** `s32`: 0 on success, else the first failing status

**Notes:** Called from 0c053E1C. The 'serial number protection' purpose comes from the label string and the brief.

- Addresses by version: 219: 0x0C05C088
- Called by: `ble_session_msg_build`
- Calls: `wc_X963_KDF`, `wc_HmacSetKey`, `wc_HmacUpdate`, `wc_HmacFinal`, `wc_HmacInit`, `wc_HmacFree`
- Confidence: medium

## ble_crypto_server_secret

**Derive the 32-byte server shared secret from two 32-byte values**

Concatenates the 32-byte value at param_1 and the 32-byte value at param_2 into one 64-byte block on the stack and derives 32 bytes into param_3 with 0c060BE8 (SHA-256 type 6), using the label 'ServerSharedSecret' (18 bytes). Part of the pairing key-derivation group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | first 32-byte value |
| `param_2` | `ptr` | second 32-byte value |
| `param_3` | `ptr` | 32-byte output secret |

**Notes:** Called from 0c053A48.

- Addresses by version: 219: 0x0C05BE98
- Called by: `ble_secure_ctx_restore_from_nv`
- Calls: `wc_X963_KDF`
- Confidence: high

## ble_crypto_session_decrypt

**AES-128-GCM decrypt a pairing-session message whose 16-byte tag is at its end**

Rejects an input shorter than 17 bytes or an output capacity below the ciphertext length (returns -1). It derives 32 bytes from the 32-byte key at param_1 with the label 'PairingSession' (14 bytes): bytes 0..15 are the AES-128 key for wc_AesGcmSetKey and bytes 16..31 are the GCM IV. It creates an Aes context (wc_AesInit with devId -2), decrypts the input minus its 16-byte trailing tag with wc_AesGcmDecrypt into param_5, verifies the tag, stores the plaintext length in *param_4 and frees the context.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 32-byte key material |
| `param_2` | `u32` | input length including the 16-byte tag |
| `param_3` | `ptr` | input (ciphertext followed by tag) |
| `param_4` | `ptr` | in/out: output capacity on entry, plaintext length on success |
| `param_5` | `ptr` | plaintext output |

**Returns** `s32`: 0 when the tag verifies, -1 for bad sizes, else the GCM status

**Notes:** The IV source is the second half of the KDF output, which the decompile shows as a separate stack buffer (auStack_160); the byte layout is inferred from the contiguous stack slots. Called from 0c053A48.

- Addresses by version: 219: 0x0C05BF00
- Called by: `ble_secure_ctx_restore_from_nv`
- Calls: `wc_AesGcmSetKey`, `wc_AesGcmDecrypt`, `wc_AesInit`, `wc_AesFree`, `wc_X963_KDF`
- Confidence: medium

## ble_crypto_sha256_commit

**SHA-256 over the 28-byte X of ctx+0x150 followed by the 32 bytes at ctx+0x1BC**

Copies the 32 bytes at context+0x1BC..0x1DB, exports the bignum at context+0x150 as 28 big-endian bytes with 0c0641F4 (mp_to_unsigned_bin_len), and hashes these 60 bytes (28 + 32) with wc_InitSha256, the update 0c061B7C, the final 0c061C80 and wc_Sha256Free. The 32-byte digest goes to param_2. The 60-byte input is the same record that ble_ecc_share_derive writes, so this is the digest of that record.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ECC context |
| `param_2` | `ptr` | 32-byte digest output |

**Returns** `s32`: 0 on success, else the first failing status

**Notes:** Purpose (commitment or confirmation value) is inferred. Called from 0c053954.

- Addresses by version: 219: 0x0C05BA6C
- Called by: `ble_fmna_state_save`
- Calls: `wc_Sha256Update`, `wc_Sha256Final`, `wc_InitSha256`, `wc_Sha256Free`, `mp_to_unsigned_bin_len`
- Confidence: medium

## ble_crypto_sha256_digest

**One-shot SHA-256 of param_1 bytes at param_2 into the 32-byte digest at param_3**

Initialises a SHA-256 context with wc_InitSha256 (0c061DB0), feeds param_1 bytes from param_2 to the unnamed update routine 0c061B7C, finalises into the 32-byte digest at param_3 with 0c061C80 and releases the context with wc_Sha256Free. The update call uses the (context, data, length) order, so param_1 is the length. Returns the first failing status, or the finalisation status.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | message length in bytes |
| `param_2` | `ptr` | message data |
| `param_3` | `ptr` | 32-byte digest output |

**Returns** `s32`: 0 on success, else the initialisation or update status

**Notes:** 0c061B7C and 0c061C80 are presumably wc_Sha256Update and wc_Sha256Final from their call shapes; they are not named in the packet. Called from 0c053A48.

- Addresses by version: 219: 0x0C05B984
- Called by: `ble_secure_ctx_restore_from_nv`
- Calls: `wc_Sha256Update`, `wc_Sha256Final`, `wc_InitSha256`, `wc_Sha256Free`
- Confidence: medium

## ble_crypto_try_default_pwd

**Try each stored 16-byte pairing key against the challenge until one authenticates**

Clears the authentication-failure byte at ble_get_state_ptr_42f8 + 0x2D and walks the three pairing-key slots, each a state byte followed by a 16-byte key (states at 0x20008FF5, 0x20009006 and 0x20009017). For a slot whose state is '=', the key is copied to 0x20009450, the context at 0x20009414 is pointed at that key and at the seed block 0x200093F4, and ble_219_0c0496a8 runs the challenge with its output written to 0x200092F0 and the output length in a local byte. Result 0 routes the output through ble_219_0c02c1e8 with the length as its second argument and returns 0; result 1 sets the failure byte to 1 and moves on; any other result, or an empty slot (status 3), is logged with the attempt count. After the three slots the function returns the status of the last slot tried.

**Returns** `s32`: 0 if a stored key authenticated, otherwise the status of the last slot tried (1 for a mismatch, 3 for an empty slot)

**Notes:** The challenge routine ble_219_0c0496a8 is not described yet, so its status meanings (0, 1, other) are inferred from this caller only. The slot layout and the '=' state marker are inferred from ble_219_0c02b480 and ble_219_0c02bf20. The log name suggests default passwords, but the code tries whatever keys are stored in the three slots.

- Addresses by version: 219: 0x0C02BE44
- Called by: `ble_rx_data_handler`
- Calls: `ble_msg_route_by_key`, `trace_printf`, `ble_crypto_ccm_open_frame`, `ble_get_state_ptr_42f8`
- Confidence: medium

## ble_ecc_ctx_release

**Release an ECC context: wc_ecc_free, free its temporary point and zero 512 bytes**

Calls wc_ecc_free (0c0601D0) on the key object, which takes the key from r0 (the context pointer here), frees the temporary point stored at context+0x1FC through 0c05F1B0 (the release half of the temporary-bignum pool; allocation is 0c05F1A8), and then zeroes the 512 bytes at the context base with memset. The wipe removes private scalars and key material at the end of an ECC operation.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ECC context (0x200+ bytes) |

**Notes:** The argument to 0c0601D0 is implicit in r0 in the decompile.

- Addresses by version: 219: 0x0C05BA4C
- Calls: `wc_ecc_del_point`, `wc_ecc_free`, `memset`
- Confidence: medium

## ble_ecc_heap_alloc

**Allocate a block of the given size from the BLE crypto heap pool at DAT_200049A8**

Thunk that returns 0x0C071080(DAT_200049A8, size), the pool allocation routine (not yet described), for the same pool handle that ble_ecc_heap_free uses. Callers request 0x68 bytes (one fp_int), 0x138 bytes (one ecc_point) or 0x208 bytes (one ecc_curve_spec) and treat a NULL result as MEMORY_E (-0x7D). The block is not zeroed here; callers clear it themselves with memset or mp_init.

| Parameter | Type | Description |
|---|---|---|
| `size` | `u32` | block size in bytes |

**Returns** `ptr`: block, or NULL when the pool is exhausted

- Addresses by version: 219: 0x0C05CBA4
- Called by: `ecc_point_to_montgomery`, `ecc_projective_dbl_point`, `ecc_projective_add_point`, `ecc_map_ex`, `wc_ecc_new_point_h`, `ecc_shared_secret`, `ecc_make_pub_ex`, `ecc_check_privkey_gen`, `wc_ecc_make_key_ex`, `ecc_verify_hash_ex`, `wc_ecc_verify_hash`, `ecc_point_on_curve_check` ...
- Calls: `ble_219_0c07097c`
- Confidence: medium

## ble_ecc_heap_free

**Release a block to the BLE crypto heap pool at DAT_200049A8**

Thunk that calls the pool free routine 0x0C070F40 with the pool handle stored at DAT_200049A8 as the first argument and the block as the second. The ECC routines in this packet release their 0x68-byte fp_int and 0x138-byte ecc_point temporaries through it, usually after zeroing them. The handle is used only by this pair and ble_ecc_heap_alloc, and every observed caller is ECC code, so this is most likely a dedicated ECC heap, although the pool may be shared with other users. 0x0C070F40 itself is not yet described.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | block previously returned by ble_ecc_heap_alloc |

- Addresses by version: 219: 0x0C05CBA0
- Called by: `ecc_point_to_montgomery`, `ecc_projective_dbl_point`, `ecc_projective_add_point`, `ecc_map_ex`, `wc_ecc_new_point_h`, `wc_ecc_del_point`, `ecc_mulmod_ex`, `ecc_check_pubkey_order`, `ecc_mulmod_ex2`, `ecc_shared_secret`, `ecc_make_pub_ex`, `ecc_check_privkey_gen` ...
- Calls: `ble_219_0c07098c`
- Confidence: medium

## ble_ecc_p224_export_derive

**Export the P-224 point at ctx+0x1FC and derive two 32-byte secrets from its X coordinate**

Exports the 28-byte X coordinate of the temporary point at context+0x1FC, then runs the 0c060BE8 key derivation with that X as key over the 64-byte input at context+0x1BC..0x1FB (two 32-byte blocks) to produce 64 bytes. If the derivation succeeds it writes the first 32 bytes to param_3 and the second 32 bytes to param_4, sets param_2[0] = 0x04 and writes X (28 bytes) and Y (28 bytes, point+0x68) after it, giving the 57-byte uncompressed P-224 public point. It has no direct caller in the packet and is reached indirectly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ECC context |
| `param_2` | `ptr` | 57-byte output: uncompressed P-224 point |
| `param_3` | `ptr` | first 32-byte derived secret |
| `param_4` | `ptr` | second 32-byte derived secret |

**Notes:** Unnamed: 0c0641F4 (export), 0c060BE8 (key derivation, SHA-256 type 6). The roles of the two derived halves are not established.

- Addresses by version: 219: 0x0C05BBCC
- Calls: `wc_X963_KDF`, `mp_to_unsigned_bin_len`
- Confidence: medium

## ble_ecc_point_add_mont

**Add two projective ECC points in Montgomery form and write the result to param_1**

Loads the modulus p from the curve block at param_4+0x0C and the constant a from param_4+0x10 as fp_int values (hex, radix 16). It computes R mod p with the normalisation thunk and converts the three 104-byte coordinates of each input point (offsets 0, 0x68, 0xD0) to Montgomery form by multiplying with R. It derives rho = -1/p mod 2^32 with mp_montgomery_setup, adds the points with 0c05EB00 (curve a, modulus p, rho) and, on success, converts the result at param_1 back with the Montgomery reduction 0c05EFC0. Temporary bignums are cleared before return. Called from 0c05BAF0 and 0c05BD30.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output point (three 104-byte fp_int coordinates) |
| `param_2` | `ptr` | first input point P |
| `param_3` | `ptr` | second input point Q |
| `param_4` | `ptr` | curve block: +0x0C modulus p, +0x10 constant a (hex strings) |

**Returns** `s32`: 0 on success, else the first failing status (-1 for a temporary allocation failure)

**Notes:** The operation name (point addition) is inferred from the caller. Unnamed: 0c05EB00, 0c05EFC0, thunk 0c062940, thunk 0c06353C.

- Addresses by version: 219: 0x0C05B724
- Called by: `ble_ecc_share_derive`, `ble_crypto_diversify`
- Calls: `ecc_projective_add_point`, `ecc_map_ex`, `mp_init`, `fp_clear`, `fp_mulmod_thunk`, `fp_montgomery_calc_normalization_thunk`, `fp_read_radix`, `mp_montgomery_setup`
- Confidence: medium

## ble_ecc_scalar_base_mult

**Derive a scalar in 1..n-1 from 36 bytes and multiply the point at param_3 by it**

Imports the 36-byte big-endian value at param_2 into a temporary bignum and loads the curve order n from param_4+0x18 (hex, radix 16). It reduces the value modulo n-1 and adds 1 to get a scalar in 1..n-1; the final +1 is the mp_add_d thunk and the earlier subtract step is an unnamed digit op (medium confidence). It loads the modulus p from param_4+0x0C and the constant a from param_4+0x10, then runs the projective scalar multiplication 0c05F818(scalar, param_3, param_1, a, p, 0). On success it computes rho with mp_montgomery_setup and converts the result out of Montgomery form with 0c05EFC0. Used by the 'diversify' step 0c05BD30.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output point |
| `param_2` | `ptr` | 36-byte big-endian scalar seed |
| `param_3` | `ptr` | base point |
| `param_4` | `ptr` | curve block: +0x0C p, +0x10 a, +0x18 n |

**Returns** `s32`: 0 on success, else the first failing status

**Notes:** The subtract step and the exact reduction rule are inferred from the thunk sequence (sub 1, mod, add 1). Unnamed: 0c05F818 (scalar multiplication), 0c063CE4, 0c0634C4, 0c06428C.

- Addresses by version: 219: 0x0C05B86C
- Called by: `ble_crypto_diversify`
- Calls: `ecc_map_ex`, `ecc_mulmod_ex_thunk`, `mp_init`, `fp_clear`, `fp_mod_thunk`, `mp_read_unsigned_bin`, `fp_sub_d_thunk`, `mp_add_d`, `fp_read_radix`, `mp_montgomery_setup`
- Confidence: medium

## ble_ecc_share_derive

**Import the peer's P-224 point, combine it with the context point and build the 60-byte share record**

Initialises a temporary key and imports the peer's 57-byte uncompressed P-224 point at param_2 (length 0x39, curve id 14) with 0c060AE4, then validates it with 0c060974. It combines the context point at context+0x18 with a stack point through ble_ecc_point_add_mont into the temporary point at context+0x1FC. On success it writes the 28-byte X of context+0x150 to param_3[0..27], copies the 32 bytes at context+0x1BC..0x1DB to param_3[0x1C..0x3B] (a 60-byte record), and stores the 32 bytes at param_2+0x39..0x58 into context+0x1DC..0x1FB. Temporaries are freed on every path. Part of the ECC/pairing group with ble_ecc_p224_export_derive.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ECC context (point at +0x18, temporary point pointer at +0x1FC) |
| `param_2` | `ptr` | peer public point, 57 bytes (0x04 \|\| X28 \|\| Y28) followed by 32 bytes |
| `param_3` | `ptr` | 60-byte output record |

**Returns** `s32`: 0 on success, else the first failing status

**Notes:** Curve identification (P-224) comes from the 0x39 length and curve id 0x0E used on the import. The use of the stack point passed as the second point is not fully resolved in the decompile.

- Addresses by version: 219: 0x0C05BAF0
- Called by: `ble_secure_ctx_restore_from_nv`
- Calls: `ble_ecc_point_add_mont`, `wc_ecc_init`, `wc_ecc_free`, `wc_ecc_check_key`, `wc_ecc_import_x963_ex`, `mp_to_unsigned_bin_len`
- Confidence: medium

## ble_rng_get_32

**Fill 32 bytes at param_1 with random data from a temporary RNG context**

Initialises a 20-byte random-number context with the unnamed 0c061828, generates 32 bytes into param_1 with 0c061834 and releases the context with 0c06156C. Returns the generator status. The call shape (init, generate 32 bytes, free) matches the wolfSSL RNG API, but the names are not confirmed.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 32-byte output buffer |

**Returns** `s32`: 0 on success, else the status of the generator or init

**Notes:** Callers: 0c053954.

- Addresses by version: 219: 0x0C05C10C
- Called by: `ble_fmna_state_save`
- Calls: `wc_FreeRng`, `wc_InitRng`, `wc_RNG_GenerateBlock`
- Confidence: low

## ble_secure_blob_wipe_1k

**Clear the 1 KB secure buffer at 0x20011A10 through the wipe helper**

Calls ble_219_0c05c860 with the buffer at 0x20011A10, length 0x400 and fill value 0. It is the cleanup step reached from ble_219_0c05c8a8 for the 1 KB decrypted output that ble_219_0c053a48 also clears directly. Whether ble_219_0c05c860 is a plain memset or a secure wipe is not confirmed, but the zero fill value suggests a clear.

- Addresses by version: 219: 0x0C053EE4
- Called by: `ble_crypto_nv_store_blob`
- Calls: `ble_transfer_chunks_64`
- Confidence: medium

## ble_secure_ctx_restore_from_nv

**Verify and unwrap the stored secure context at boot and rebuild its RAM copies**

Boot-time restore of the secure link context; it has no direct callers. The record at 0x200122E4 is checked and loaded through ble_219_0c05be98 (its result gates everything), and on success it is saved back as NV record 0xFAF (ble_nv_record_write, 32 bytes). An 80-byte snapshot is then assembled at 0x2001150C: 16 bytes from 0x20011A00, 32 bytes from 0x200109E0 at +0x10 and 32 bytes from 0x2001091D at +0x30. The 0x410-byte blob at 0x2001050D is copied to 0x200115ED and transformed by ble_219_0c05bf00 with the key at 0x200122E4 into a 0x400-byte output at 0x20011A10 (probably decryption with an integrity check); the output is then handled by ble_219_0c05c860, ble_219_0c065c88 and ble_219_0c05c8a8, a second record is loaded by ble_219_0c05baf0 and folded into the snapshot, and the output is memcpy'd to 0x200115BD. Finally ble_219_0c05c13c encodes message 0x4B5 from the snapshot into 0x20011004 (capacity 0x506) using context 0x20004030. The function returns 0 on success and 0xC if any step fails.

**Returns** `u32`: 0 on success, 0xC if any step fails

**Notes:** Callees ble_219_0c05be98, ble_219_0c05b984, ble_219_0c05bfa4, ble_219_0c05bf00, ble_219_0c05baf0, ble_219_0c05c860, ble_219_0c05c8a8, ble_219_0c05c13c and ble_219_0c065c88 are not described yet, so the cipher, the integrity check and the meaning of message ids 0x59 and 0x4B5 are inferred from the call shape only.

- Addresses by version: 219: 0x0C053A48
- Calls: `ble_nv_record_write`, `ble_crypto_sha256_digest`, `ble_ecc_share_derive`, `ble_crypto_server_secret`, `ble_crypto_session_decrypt`, `ble_crypto_ecdsa_p256_verify`, `ble_crypto_ecdh_seal_p256`, `ble_transfer_chunks_64`, `ble_crypto_nv_store_blob`, `printf_hexdump`, `memcpy`
- Confidence: medium

## ble_sha1_mix_pair16

**SHA-1 over two 16-byte inputs (built-in defaults for NULL), keeping 16 digest bytes**

Forms the 32-byte message A || B, where each 16-byte half is the input pointer or, when that pointer is NULL, a built-in constant (words 0x02B8CF97, 0xDE434184, 0x3B2B0056, 0x5D0A7834, the same for both halves). It hashes the message with ble_sha1_oneshot and writes the first 16 bytes of the 20-byte digest to param_3, dropping the last word. The purpose is not identified in this packet; the ble_crypto_* authentication path described in the brief is one candidate to check.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 16-byte input A, or NULL for the built-in constant |
| `param_2` | `ptr` | 16-byte input B, or NULL for the built-in constant |
| `param_3` | `ptr` | 16-byte output |

**Notes:** The SHA-1 identity comes from the mbedTLS calls in the callee. The purpose is low confidence.

- Addresses by version: 219: 0x0C04920C
- Called by: `ble_crypto_ccm_seal_frame`, `ble_crypto_ccm_open_frame`
- Calls: `ble_sha1_oneshot_thunk`
- Confidence: medium

## ble_sha1_oneshot

**One-shot SHA-1 of a buffer into a 20-byte digest, wiping the context on exit**

Clears a 92-byte mbedTLS SHA-1 context with memset and loads the standard IV (0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0). It feeds the input through mbedtls_sha1_update_ret when the length is non-zero and writes the 20-byte digest through mbedtls_sha1_finish_ret. The finish is skipped when the update fails, so the output is then left untouched. The context is zeroed byte by byte before returning.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | input data |
| `param_2` | `s32` | input length in bytes; 0 is allowed |
| `param_3` | `ptr` | 20-byte digest output |

- Addresses by version: 219: 0x0C04AA80
- Called by: `ble_sha1_oneshot_thunk`
- Calls: `mbedtls_sha1_update_ret`, `mbedtls_sha1_finish_ret`, `memset`
- Confidence: high

## ble_sha1_oneshot_thunk

**Thunk: branch to ble_sha1_oneshot at 0x0C04AA80**

A single-instruction branch to ble_sha1_oneshot at 0x0C04AA80; Ghidra shows the target body here. Arguments pass through unchanged, so the behaviour is that of ble_sha1_oneshot. Its only caller in this packet is ble_sha1_mix_pair16.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | input data pointer, as in ble_sha1_oneshot |
| `param_2` | `s32` | input length in bytes |
| `param_3` | `ptr` | 20-byte digest output |

- Addresses by version: 219: 0x0C04AAE8
- Called by: `ble_sha1_mix_pair16`
- Calls: `ble_sha1_oneshot`
- Confidence: high

## btstack_crypto_aes128_encrypt

**Queue an AES-128 block encryption (type 1, HCI LE Encrypt) and run the crypto request loop**

BTstack btstack_crypto_aes128_encrypt. It stores the key pointer at +0x10, plaintext pointer at +0x14, encrypted-output pointer at +0x18, callback at +0x04, argument at +0x08 and type 1 at +0x0C in the request, appends it to the crypto list at 0x20017388, and runs the loop only when the controller state byte is 2. Type 1 reverses the key and plaintext into HCI byte order with co_reverse_copy_16 and sends LE Encrypt (template 0x0C081148). The loop dispatches the head request by type: 0 random, 1 AES, 2 and 3 CMAC (btstack_crypto_cmac_step), 4 local P-256 public key (answered from a cached 64-byte copy at 0x20017304 once the state byte at 0x20017300 reaches 4), 5 ECDH shared secret (template 0x0C081150, two 32-byte halves), and 6 to 8 AES-CCM requests. The CCM sub-states at +0x10 build B0 from the flags, a 13-byte nonce at +0x18 and a 16-bit message length (state 0), absorb the AAD length prefix and data into the CBC-MAC state at +0x24 (state 2), absorb the final partial block (state 4), and build counter blocks A0 or A(i) with a 16-bit counter (states 6 and 8); even states issue the next step and odd states wait for the LE Encrypt result.

| Parameter | Type | Description |
|---|---|---|
| `request` | `ptr` | caller-owned request record (linked-list node) |
| `key` | `ptr` | 16-byte AES key |
| `plaintext` | `ptr` | 16-byte input block |
| `encrypted` | `ptr` | 16-byte output block |
| `callback` | `ptr` | completion callback, called with arg |
| `arg` | `ptr` | argument for the callback |

**Notes:** The argument layout matches the upstream BTstack request. The CCM sub-state meanings and the type 4 and 5 identities are inferred from the block constructions and the HCI template count. The same loop is inlined into ble_219_0c064ffc (btstack_crypto_random_generate). The HCI template identities for 0x0C081148, 0x0C081150 and 0x0C081168 are not decoded in this packet.

- Addresses by version: 219: 0x0C065038
- Called by: `ble_crypto_auth_step`, `ble_crypto_auth_send_word_type1`, `ble_crypto_auth_derive_own_word`, `ble_crypto_auth_store_xor_word`, `ble_crypto_auth_start_by_mode`, `sm_pairing_engine_step`, `btstack_crypto_random_generate`, `btstack_crypto_ccm_submit`, `btstack_crypto_ecc_p256_generate_key`, `btstack_crypto_ecc_p256_calculate_dhkey`
- Calls: `btstack_crypto_cmac_step`, `btstack_linked_list_empty`, `btstack_linked_list_add_tail`, `btstack_linked_list_get_first_item`, `btstack_linked_list_pop`, `co_write16_be`, `co_reverse_copy_16`, `co_min_u32`, `ll_env_is_ready`, `hci_send_cmd_no_status`, `ble_ctrl_env_get_u8_at_0x198`, `memcpy`
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

## btstack_crypto_ccm_submit

**Queue an AES-CCM request (type 3) and run the crypto job pump**

Appends a type-3 request to the BTstack crypto list at DAT_20017388 and then runs the job pump. The request holds the key pointer (+0x10), a u16 message length (+0x14), the nonce pointer (+0x18), the data pointer (+0x1C), the completion callback (+0x04) and its context (+0x08). The pump runs only when env+0x198 equals 2 (ble_ctrl_env_get_u8_at_0x198), no HCI command is in flight (DAT_2001738C clear) and ll_env_is_ready (0x0C066978) is true. It pops the head and switches on the type byte at +0x0C: 0 sends HCI LE Rand (opcode 0x2018), 1 sends HCI LE Encrypt (0x2017) on byte-reversed key and plaintext, 4 and 5 are the P-256 jobs (0x0C0650C0 and 0x0C065108), and 6 to 8 are CCM job steps. Types 2 and 3 latch a CCM job only when the single CCM engine is idle (DAT_200172DC clear): the 16-byte key goes to 0x200172CC, the block count ((length+15)>>4, minimum 1) to 0x200172C8, the accumulator at 0x200172F0 is zeroed and the engine is marked busy; otherwise the active job is continued. The job helper 0x0C06464C is called with the item and is not described here. Within a CCM job the sub-state byte at +0x10 selects the step. State 0 builds B0 = ((M-2)*4 & 0xF8) | (AAD!=0)<<6 | 1, with M at +0x3E, then the 13-byte nonce and the big-endian length at offset 14, and encrypts it. State 2 absorbs the AAD behind a 2-byte big-endian length, then the payload, into the 16-byte CBC-MAC accumulator at +0x24, encrypting each full block. State 4 encrypts the final partial block (accumulator XOR zero-padded data). States 6 and 8 encrypt counter blocks A0 (counter 0) and Ai (counter at +0x3A), each with flags 1, the nonce and a 2-byte counter, to make the MIC and payload keystream. Even sub-states issue an encrypt and odd sub-states (1, 3, 5, 7, 9) wait for its completion, which is handled outside this packet. This is the CCM member of three near-identical copies of the same pump (0x0C0650C0 and 0x0C065108 carry the same dispatch loop). Callers are ble_crypto_auth_pubkey_begin (0x0C04F894) and sm_pairing_engine_step (0x0C051EB8).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | btstack_crypto_ccm_t request, queued on the list at 0x20017388 |
| `param_2` | `ptr` | 16-byte AES key |
| `param_3` | `u16` | message length in bytes |
| `param_4` | `ptr` | 13-byte CCM nonce |
| `param_5` | `ptr` | message data buffer |
| `param_6` | `ptr` | completion callback, stored at +0x04 |
| `param_7` | `ptr` | callback context, stored at +0x08 |

**Notes:** The job type is set to 3 here, and the CCM steps 6 to 8 later reuse the same item. The item's +0x14 field is a u16 length on enqueue but is used as a key pointer by the CCM steps, so the job helper 0x0C06464C must rewrite it. The completion handler that sets DAT_20017300 and advances sub-states is not in this packet. The exact B0 and MIC byte layout is inferred from the code and from the flags formula, and it matches CCM with M=4 and L=2 (BLE link layer).

- Addresses by version: 219: 0x0C065078
- Called by: `ble_crypto_auth_pubkey_begin`, `sm_pairing_engine_step`
- Calls: `btstack_crypto_aes128_encrypt`, `btstack_linked_list_add_tail`, `ble_ctrl_env_get_u8_at_0x198`
- Confidence: medium

## btstack_crypto_cmac_step

**Advance the BTstack AES-CMAC (RFC 4493) operation: subkeys, CBC-MAC blocks, final block**

BTstack AES-CMAC engine, one step per LE Encrypt round trip, with the key at 0x200172CC and the CBC-MAC state at 0x200172F0. The phase byte DAT_200172DC selects the step: phase 1 starts the operation by encrypting the constant block at 0x0C08625C to obtain L = E_K(0), stored in 0x200172E0, and moves to phase 2 to wait; phase 3 absorbs one 16-byte message block as X = E_K(X xor M_i), where M_i comes from a byte callback at request+0x18 when request+0x0C is 2 (otherwise from the buffer that request+0x18 points to), at offset block_index*16 + i; phase 5 handles the final block, deriving K1 = dbl(L) and K2 = dbl(K1) in GF(2^128) with Rb = 0x87, XORing K1 into a full final block or K2 with 0x80 padding into a partial or empty one, and then encrypting. Phases 2, 4 and 6 are waiting for an LE Encrypt result, and the block index at 0x200172C9 is compared against the block count at 0x200172C8 (ceil(length/16)). Three calls to util_nop_stub_b (ble_219_0c065ce0) are empty trace hooks.

| Parameter | Type | Description |
|---|---|---|
| `request` | `ptr` | crypto request record (type, mode, length at +0x14, source at +0x18, callback fields) |

**Notes:** The identification as BTstack's CMAC follows the RFC 4493 structure and the shared btstack_crypto request queue. The phase numbers and the 0x0C08625C zero block are inferred from the code. The completion handler that moves phases 2, 4 and 6 on is outside this packet.

- Addresses by version: 219: 0x0C06464C
- Called by: `btstack_crypto_aes128_encrypt`
- Calls: `co_reverse_copy_16`, `util_nop_stub_b`, `hci_send_cmd_no_status`
- Confidence: medium

## btstack_crypto_ecc_p256_calculate_dhkey

**Queue a P-256 ECDH request (remote public key in, shared secret out)**

Queues a type-5 request holding the remote P-256 public key pointer (param_2, stored at +0x10), the DHKey output pointer (param_3, stored at +0x14), the completion callback (param_4, +0x04) and its context (param_5, +0x08), then runs the shared job pump. The pump sends HCI LE Generate DHKey (opcode 0x2026, template 0x0C081150) with two 32-byte arguments: X at the key pointer and Y at that pointer plus 0x20, and it marks the controller busy. The 32-byte shared secret is written by the completion path, which is not in this packet, so the use of +0x14 is inferred. This is the DHKey member of the same three-copy pump group as 0x0C065078 and 0x0C0650C0, and its only caller in this packet is sm_pdu_rx_handler (0x0C051EF0), the SMP receive path.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | btstack_crypto_ecc_p256_t request |
| `param_2` | `ptr` | remote P-256 public key, 64 bytes (X then Y) |
| `param_3` | `ptr` | 32-byte DHKey output buffer, stored at +0x14 |
| `param_4` | `ptr` | completion callback, stored at +0x04 |
| `param_5` | `ptr` | callback context, stored at +0x08 |

**Notes:** Template 0x0C081150 was decoded from the firmware image as opcode 0x2026, LE Generate DHKey, with format QQ. The public-key layout matches the template's two 32-byte arguments. The DHKey output routing is inferred because the completion handler is not in this packet.

- Addresses by version: 219: 0x0C065108
- Called by: `sm_pdu_rx_handler`
- Calls: `btstack_crypto_aes128_encrypt`, `btstack_linked_list_add_tail`, `ble_ctrl_env_get_u8_at_0x198`
- Confidence: medium

## btstack_crypto_ecc_p256_generate_key

**Queue a P-256 local public-key read and copy the 64-byte result to the caller**

Queues a type-4 request with the output buffer pointer (param_2, stored at +0x10), the completion callback (param_3, +0x04) and its context (param_4, +0x08), then runs the same job pump as 0x0C065078 (the loop is a copy of that one, and 0x0C065108 has the same copy). Before queuing it resets the handshake byte DAT_20017300 from 4 back to 0. When serviced, a DAT_20017300 of 0 is set to 3 and HCI LE Read Local P-256 Public Key (opcode 0x2025, template 0x0C081180, no arguments) is sent. When DAT_20017300 has reached 4, the pump copies the 64-byte X||Y public key from 0x20017304 into the caller's buffer in four 16-byte copies, pops the request and invokes the callback with its context. The shape of the API matches BTstack's btstack_crypto_ecc_p256_generate_key, which is why this name is used. Pump behaviour is the same as in the other two copies, and the caller list contains ble_link_pending_timer_done (0x0C04FC10), sm_pairing_engine_step (0x0C051EB8) and sm_pdu_rx_handler (0x0C051EF0).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | btstack_crypto_ecc_p256_t request |
| `param_2` | `ptr` | 64-byte output buffer for the local P-256 public key (X then Y) |
| `param_3` | `ptr` | completion callback, stored at +0x04 |
| `param_4` | `ptr` | callback context, stored at +0x08 |

**Notes:** Template 0x0C081180 was decoded from the firmware image as opcode 0x2025, LE Read Local P-256 Public Key. The handshake values 3 (command in flight) and 4 (result in 0x20017304) are inferred from the code paths. The completion handler that sets 4 is not in this packet.

- Addresses by version: 219: 0x0C0650C0
- Called by: `ble_link_pending_timer_done`, `sm_pairing_engine_step`, `sm_pdu_rx_handler`
- Calls: `btstack_crypto_aes128_encrypt`, `btstack_linked_list_add_tail`, `ble_ctrl_env_get_u8_at_0x198`
- Confidence: medium

## btstack_crypto_random_generate

**Queue a random-bytes request (type 0, LE Rand) on the crypto list and run it**

BTstack btstack_crypto_random_generate. It records the request as callback at +0x04, argument at +0x08, type 0 at +0x0C, output buffer at +0x10 and byte count (u16) at +0x14, then appends it to the crypto list at 0x20017388 through btstack_linked_list_add_tail_impl (ble_219_0c065416). If ble_ctrl_env_get_u8_at_0x198 returns 2 it runs the request loop, which is inlined here as a copy of the loop in btstack_crypto_aes128_encrypt (ble_219_0c065038). For a type 0 request that loop sends the parameterless HCI command template at 0x0C081168, which is most likely LE Rand (0x2018), and sets the busy byte at 0x2001738C. The loop only dispatches while ll_env_is_ready (ble_219_0c066978) holds and the busy byte is clear.

| Parameter | Type | Description |
|---|---|---|
| `request` | `ptr` | caller-owned request record (linked-list node) |
| `buffer` | `ptr` | output buffer for the random bytes |
| `size` | `u16` | number of random bytes requested |
| `callback` | `ptr` | completion callback, called with arg when the bytes are ready |
| `arg` | `ptr` | argument for the callback |

**Notes:** The signature matches upstream btstack_crypto_random_generate. The LE Rand identification of template 0x0C081168 is an inference, since the template itself is not decoded in this packet. The completion path that fills the buffer is outside this packet.

- Addresses by version: 219: 0x0C064FFC
- Called by: `ble_crypto_auth_step`, `ble_crypto_auth_load_keys`, `sm_pairing_engine_step`, `sm_pdu_rx_handler`, `sm_crypto_done_resume`
- Calls: `btstack_crypto_aes128_encrypt`, `btstack_linked_list_add_tail`, `ble_ctrl_env_get_u8_at_0x198`
- Confidence: medium

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
- Called by: `bt_app_set_name_and_advdata`
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
- Called by: `nb_upgrade_process_cmd`
- Confidence: high

## ecc_check_privkey_gen

**Check a private key by recomputing k*G and comparing it with the stored public key**

wolfSSL-style ecc_check_privkey_gen(key, a, prime). Loads order, Gx and Gy (mask 0x38) with wc_ecc_curve_load, sets a temporary point to (Gx, Gy, 1), and computes R = k * G with ecc_mulmod_ex2 using the key's RNG, then maps R to affine. R's x, y and z are compared with the stored public point (key+0x18, +0x80, +0xE8). A match returns 0 and a mismatch returns ECC_PRIV_KEY_E (-0xD8). Temporaries and the curve context are zeroed and freed on every path.

| Parameter | Type | Description |
|---|---|---|
| `key` | `ptr` | ecc_key with private scalar and stored public point |
| `a` | `ptr` | curve parameter a |
| `prime` | `ptr` | field prime fp_int |

**Returns** `s32`: 0 on match, -0xD8 (ECC_PRIV_KEY_E) on mismatch, -0xAD for NULL key, or a setup error

- Addresses by version: 219: 0x0C05FF44
- Called by: `wc_ecc_check_key`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `wc_ecc_curve_free`, `wc_ecc_curve_load`, `wc_ecc_new_point_h`, `ecc_mulmod_ex2`, `fp_clear`, `mp_cmp`, `mp_copy`, `mp_set`, `memset`
- Confidence: medium

## ecc_check_pubkey_order

**Check that order * Q is the point at infinity (encoded as x = y = 0) for a public key**

Computes order * Q with ecc_mulmod_ex on a temporary point, mapping the result to affine (map flag 1). It returns 0 only when both mapped coordinates are zero, which is the (0, 0) encoding of infinity written by ecc_map_ex; any other result returns ECC_INF_E (-0xD7). A NULL key returns BAD_FUNC_ARG (-0xAD). Only the heap field (key+0x14) is read from the key, and the temporary is zeroed and freed on every path.

| Parameter | Type | Description |
|---|---|---|
| `key` | `ptr` | ecc_key, only its heap field is read |
| `pub` | `ptr` | public point Q |
| `a` | `ptr` | curve parameter a |
| `prime` | `ptr` | field prime fp_int |
| `order` | `ptr` | curve order fp_int |

**Returns** `s32`: 0 when order * Q is infinity, -0xD7 (ECC_INF_E) otherwise, -0xAD for NULL key

- Addresses by version: 219: 0x0C05F830
- Called by: `ecc_make_pub_ex`, `wc_ecc_check_key`
- Calls: `ble_ecc_heap_free`, `wc_ecc_new_point_h`, `ecc_mulmod_ex`, `fp_clear`, `get_digit_count`
- Confidence: high

## ecc_field_inv_fermat

**Field inverse by Fermat: result = base^(m-2) mod m with an 8-entry run-of-ones table**

Computes base^(m-2) mod m with Montgomery products, which is the field inverse when m is prime. It allocates 0x410 bytes (ten 104-byte fp_int slots) through thunk_FUN_0c07097c, copies the base into table slot 0 and fills slots 1 to 7 by square-then-multiply: fp_sqr (ble_219_0c062880), fp_mul_comba24 (ble_219_0c06237c), then fp_montgomery_reduce (ble_219_0c062a28) with mp. Table entry j therefore holds base^(2^(j+1) - 1), so a run of up to eight one-bits in the exponent costs a single multiply. The exponent m - 2 is produced by fp_sub_d (ble_219_0c063ce4) and scanned from its top bit down: each zero bit costs a square, and at the end of each run of ones the matching table entry is multiplied in, with Montgomery reduction after every product. The result is written to the output slot, and the function returns 0, or -2 (0xFFFFFFFE) when the scratch block cannot be allocated. The scan is bounded to 512 exponent bits by a guard of 0x201.

| Parameter | Type | Description |
|---|---|---|
| `base` | `ptr` | value to invert (fp_int, Montgomery form) |
| `modulus` | `ptr` | modulus m (fp_int) |
| `result` | `ptr` | output (fp_int) |
| `mp` | `u32` | Montgomery constant -1/m mod 2^32, passed to fp_montgomery_reduce |

**Returns** `s32`: 0 on success, -2 when the scratch block cannot be allocated

**Notes:** Identity (Fermat inverse with a run-of-ones window) is inferred from the exponent m - 2 and the 2^k - 1 table. Use for the P-256 field prime is an assumption and is not verified in this packet. Operands are assumed to be in Montgomery form (R = 2^(32*used)) because every product is Montgomery-reduced.

- Addresses by version: 219: 0x0C063D2C
- Called by: `ecc_field_inv_fermat_thunk`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `fp_mul_comba24`, `fp_sqr`, `fp_montgomery_reduce`, `fp_sub_d`, `memcpy`, `memset`
- Confidence: medium

## ecc_field_inv_fermat_thunk

**Branch-only alias of ecc_field_inv_fermat (base^(m-2) mod m)**

One-instruction tail branch to ble_219_0c063d2c (ecc_field_inv_fermat). Arguments pass through unchanged.

| Parameter | Type | Description |
|---|---|---|
| `base` | `ptr` | value to invert (fp_int, Montgomery form) |
| `modulus` | `ptr` | modulus m (fp_int) |
| `result` | `ptr` | output (fp_int) |
| `mp` | `u32` | Montgomery constant -1/m mod 2^32 |

**Returns** `s32`: 0 on success, -2 when the scratch block cannot be allocated

- Addresses by version: 219: 0x0C0640F4
- Called by: `ecc_map_ex`
- Calls: `ecc_field_inv_fermat`
- Confidence: high

## ecc_make_pub_ex

**Compute the public point k*G for a private key, check its order, and set the key type**

wolfSSL-style ecc_make_pub_ex(key, curve, pubOut, rng). If no curve context is given it allocates a 0x208-byte ecc_curve_spec and loads prime, a, order, Gx and Gy from key->dp (mask 0x3B). When pubOut is NULL the key's own public point (key+0x18) is used and the key type is set to ECC_PRIVATEKEY_ONLY (3) on entry and to ECC_PRIVATEKEY (2) on exit. The private scalar at key+0x150 must satisfy 0 < k < order, otherwise ECC_PRIV_KEY_E (-0xD8) is returned. pubOut = k * G is then computed with ecc_mulmod_ex2 (RNG blinding), mapped to affine, and checked with ecc_check_pubkey_order. Temporaries are freed on every path. ecc_verify_hash_ex calls it with (key, NULL, NULL) to fill in the public point of a private-only key.

| Parameter | Type | Description |
|---|---|---|
| `key` | `ptr` | ecc_key |
| `curve` | `ptr` | curve context, or NULL to load one |
| `pubOut` | `ptr` | output point, or NULL for key->pubkey |
| `rng` | `ptr` | RNG for blinding |

**Returns** `s32`: 0, -0xD8 (ECC_PRIV_KEY_E) for an out-of-range scalar, or an error from the steps above

- Addresses by version: 219: 0x0C05FD18
- Called by: `wc_ecc_make_key_ex`, `ecc_verify_hash_ex`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `wc_ecc_curve_free`, `wc_ecc_curve_load`, `ecc_map_ex`, `wc_ecc_new_point_h`, `ecc_check_pubkey_order`, `ecc_mulmod_ex2`, `fp_clear`, `mp_init_multi`, `mp_cmp`, `mp_copy`, `mp_iszero`, `mp_montgomery_setup`, `mp_set`, `memset`
- Confidence: medium

## ecc_map_ex

**Map a Jacobian point to affine (x*z^-2, y*z^-3, z=1); infinity is encoded as (0, 0, 1)**

wolfSSL-style affine mapping. If z is zero the point is set to (0, 0, 1), the infinity encoding that ecc_check_pubkey_order tests for. Otherwise, with montgomeryRepr 0 z is first reduced out of Montgomery form and inverted with the modular inverse at 0x0C0635AC; with a non-zero flag the Montgomery-domain inverse at 0x0C063D2C (not yet described) is used instead. With t = z^-1 it computes t2 = t^2, x = x * t2 mod p, t = t * t2 = z^-3, y = y * t mod p, and sets z = 1. Two temporaries are allocated (MEMORY_E on failure) and zeroed before being freed.

| Parameter | Type | Description |
|---|---|---|
| `P` | `ptr` | point, overwritten with its affine form |
| `modulus` | `ptr` | fp_int field modulus |
| `rho` | `u32` | Montgomery reduction digit |
| `montgomeryRepr` | `s32` | 0 when the coordinates are in Montgomery form, non-zero otherwise |

**Returns** `s32`: 0, -0xAA for NULL input, MEMORY_E -0x7D, or an arithmetic error

**Notes:** The meaning of the flag is inferred from which inverse path it selects.

- Addresses by version: 219: 0x0C05EFC0
- Called by: `ble_ecc_point_add_mont`, `ble_ecc_scalar_base_mult`, `ecc_mulmod_ex`, `ecc_mulmod_ex2`, `ecc_shared_secret`, `ecc_make_pub_ex`, `ecc_verify_hash_ex`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `fp_clear`, `mp_init_multi`, `fp_mul_checked`, `fp_mod_thunk`, `fp_invmod_thunk`, `ecc_field_inv_fermat_thunk`, `mp_cmp_d`, `fp_sqr_thunk`, `fp_montgomery_reduce_thunk`, `mp_set`
- Confidence: medium

## ecc_mulmod_ex

**Scalar multiply R = k * P without blinding; optional affine mapping of the result**

wolfSSL-style ecc_mulmod_ex(k, P, R, a, modulus, map, heap). Validates the pointers, creates five table points and one temporary with wc_ecc_new_point, converts P to Montgomery form with ecc_point_to_montgomery, and computes rho with mp_montgomery_setup. It then runs ecc_mulmod_ladder_ct with no RNG and, when map is non-zero, maps R to affine with ecc_map_ex(R, modulus, rho, 0). The table and the temporary are freed with wc_ecc_del_point before returning. The verify path uses it for u1 * G and u2 * Q, and ecc_check_pubkey_order uses it with k = order.

| Parameter | Type | Description |
|---|---|---|
| `k` | `ptr` | scalar fp_int |
| `P` | `ptr` | input point |
| `R` | `ptr` | output point |
| `a` | `ptr` | curve parameter a |
| `modulus` | `ptr` | fp_int field modulus |
| `map` | `s32` | non-zero maps R to affine |
| `heap` | `ptr` | heap hint for temporaries |

**Returns** `s32`: 0, -0xAA for NULL input, MEMORY_E -0x7D, or an arithmetic error

- Addresses by version: 219: 0x0C05F71C
- Called by: `ecc_mulmod_ex_thunk`, `ecc_check_pubkey_order`, `ecc_verify_hash_ex`
- Calls: `ble_ecc_heap_free`, `ecc_point_to_montgomery`, `ecc_map_ex`, `wc_ecc_new_point_h`, `ecc_mulmod_ladder_ct`, `fp_clear`, `mp_montgomery_setup`
- Confidence: medium

## ecc_mulmod_ex2

**Blinded scalar multiply R = k * G: k + order blinding, optional RNG, optional affine map**

wolfSSL-style ecc_mulmod_ex2(k, G, R, a, modulus, order, rng, map, heap). Converts G to Montgomery form, takes rho, and rejects a scalar wider than the order (-0xD9). It computes the blinded scalar k + order, adding the order a second time only when that sum still has the order's bit length, so the ladder always runs over a fixed number of bits. It then calls ecc_mulmod_ladder_ct with the RNG enabling projective blinding. If k is 1 modulo the order the result is replaced by the input point through a constant-time conditional copy. Finally it maps R to affine when map is non-zero and frees its temporaries. Callers are ecc_shared_secret, ecc_make_pub_ex and ecc_check_privkey_gen.

| Parameter | Type | Description |
|---|---|---|
| `k` | `ptr` | private scalar fp_int |
| `G` | `ptr` | input point |
| `R` | `ptr` | output point |
| `a` | `ptr` | curve parameter a |
| `modulus` | `ptr` | fp_int field modulus |
| `order` | `ptr` | curve order fp_int |
| `rng` | `ptr` | RNG for blinding, may be NULL |
| `map` | `s32` | non-zero maps R to affine |
| `heap` | `ptr` | heap hint |

**Returns** `s32`: 0, -0xAA for NULL input, -0xD9 for an over-wide scalar, MEMORY_E, or an arithmetic error

- Addresses by version: 219: 0x0C05F8C4
- Called by: `ecc_shared_secret`, `ecc_make_pub_ex`, `ecc_check_privkey_gen`
- Calls: `ble_ecc_heap_free`, `ecc_point_to_montgomery`, `ecc_map_ex`, `wc_ecc_new_point_h`, `ecc_mulmod_ladder_ct`, `mp_init`, `mp_forcezero`, `fp_clear`, `mp_clear`, `fp_add_thunk`, `mp_cmp`, `mp_cmp_d`, `mp_copy`, `mp_count_bits`, `mp_add_d`, `mp_montgomery_setup` ...
- Confidence: medium

## ecc_mulmod_ex_thunk

**Branch-only alias of ecc_mulmod_ex; the argument registers pass straight through**

Tail-calls ecc_mulmod_ex (0x0C05F71C) without setting up any arguments, so the caller (0x0C05B86C, not yet described) must already hold the argument registers. Like the other *_thunk entries it is a pure branch alias.

- Addresses by version: 219: 0x0C05F818
- Called by: `ble_ecc_scalar_base_mult`
- Calls: `ecc_mulmod_ex`
- Confidence: medium

## ecc_mulmod_ladder_ct

**Constant-time Montgomery-ladder scalar multiply over a table of points, optional RNG blinding**

Core of the scalar multiplication. It copies P into table entry 0, computes entry 1 = 2P with ecc_projective_dbl_point, and copies entries 0 and 1 into entries 3 and 4. When the RNG argument is non-zero, entries 3 and 4 are first randomised with ecc_randomize_projective. It then walks the digits and bits of the scalar from the top; each bit performs one ecc_projective_add_point and conditional copies (mp_cond_copy) that select the accumulator, so the sequence of operations does not depend on the bit values. The top digit is located with get_digit_count of the modulus, and bits are read with get_digit. The final accumulator is written to R, and errors from any step are returned.

| Parameter | Type | Description |
|---|---|---|
| `k` | `ptr` | scalar fp_int |
| `P` | `ptr` | input point, Montgomery form |
| `R` | `ptr` | output point |
| `table` | `ptr` | array of point pointers, entries 0..4 used |
| `a` | `ptr` | curve parameter a |
| `modulus` | `ptr` | fp_int field modulus |
| `rho` | `u32` | Montgomery reduction digit |
| `rng` | `ptr` | RNG for projective blinding, NULL for none |

**Returns** `s32`: 0 or the first error from the point or field operations

**Notes:** The exact ladder update is not traced line by line; the constant-time structure (fixed add plus cond-copy per bit) is what the code shows.

- Addresses by version: 219: 0x0C05F338
- Called by: `ecc_mulmod_ex`, `ecc_mulmod_ex2`
- Calls: `stub_return_zero_0c0360c8`, `ecc_projective_dbl_point`, `ecc_projective_add_point`, `wc_ecc_copy_point`, `ecc_randomize_projective`, `mp_copy`, `mp_count_bits`, `get_digit_count`, `get_digit`, `mp_cond_copy`
- Confidence: medium

## ecc_point_on_curve_check

**Test y^2 == x^3 - 3x + b (mod p) for the point at param 1; returns 0 when it is on the curve**

ECC on-curve test for a short Weierstrass curve with a = -3 (the NIST prime-curve family). Parameter 1 points at the x coordinate of the point and y is the fp_int 0x68 bytes further on, the same layout as pubkey.x/pubkey.y in the ECC key. It computes t1 = y^2 (fp_sqr), t2 = x^2 mod p (fp_mod), t2 = x * t2 through the 3-operand multiply thunk ble_219_0c064090 (not yet described), t1 = t1 - t2 (fp_sub), then adds x three times, which leaves t1 = y^2 - x^3 + 3x. t1 is reduced with fp_mod and normalised into [0, p) by repeated add or subtract of p, then compared with the curve constant b (param 3) using mp_cmp. Two temporaries come from mp_init_multi and are released with fp_clear. Parameter 2 (the a coefficient) is never read because a = -3 is built in.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | point; x fp_int at +0, y fp_int at +0x68 |
| `param_2` | `u32` | curve a coefficient slot; not read (a = -3 is built in) |
| `param_3` | `ptr` | curve constant b as an fp_int |
| `param_4` | `ptr` | field prime p as an fp_int |

**Returns** `s32`: 0 when y^2 == x^3 - 3x + b (mod p); -214 (0xffffff2a) when not equal; -2 on allocation failure, -125 (0xffffff83) if a temporary cannot be allocated

**Notes:** Identity of the test is inferred from the arithmetic (the a = -3 form, the three additions of x, and the final compare with the constant). Callee ble_219_0c064090 is taken to be a 3-operand multiply and is not verified.

- Addresses by version: 219: 0x0C060828
- Called by: `wc_ecc_check_key`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `fp_clear`, `mp_init_multi`, `fp_add_thunk`, `fp_sub_thunk`, `fp_mul_checked`, `fp_mod_thunk`, `mp_cmp`, `fp_sqr_thunk`
- Confidence: medium

## ecc_point_to_montgomery

**Convert the X, Y and Z coordinates of a point to Montgomery form**

Computes t = R mod modulus with fp_montgomery_calc_normalization (0x0C062940, R = 2^(32*used)). For each coordinate (offsets 0, 0x68, 0xD0) of the source point it writes the product with t, reduced modulo the modulus (0x0C06353C), into the destination point. When t equals 1 the three coordinates are plain-copied with mp_copy instead. The temporary t comes from ble_ecc_heap_alloc(0x68) and is freed with ble_ecc_heap_free, and an allocation failure returns MEMORY_E (-0x7D). Used before each ladder run in ecc_mulmod_ex, ecc_mulmod_ex2 and the verify path.

| Parameter | Type | Description |
|---|---|---|
| `src` | `ptr` | source ecc_point in plain form |
| `dst` | `ptr` | destination ecc_point in Montgomery form |
| `modulus` | `ptr` | fp_int modulus |

**Returns** `s32`: 0, MEMORY_E (-0x7D), or the first failing arithmetic result

- Addresses by version: 219: 0x0C05E558
- Called by: `ecc_mulmod_ex`, `ecc_mulmod_ex2`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `mp_init`, `fp_clear`, `fp_mulmod_thunk`, `mp_cmp_d`, `mp_copy`, `fp_montgomery_calc_normalization_thunk`
- Confidence: medium

## ecc_projective_add_point

**Add two Jacobian points, R = P + Q, with constant-time field helpers; equal inputs double**

wolfSSL-style Jacobian addition. If the two operands alias (Q and R the same pointer) they are swapped first. When the operands are the same point (x and y compare equal, with the Z tests passing) it returns ecc_projective_dbl_point(P, R, a, modulus, rho) instead. The general path uses squarings and multiplications with Montgomery reduction, constant-time modular add and subtract (fp_addmod_ct, fp_submod_ct), and zero tests on the Z coordinates (mp_iszero, get_digit_count) to detect the point at infinity and select the other operand. Two temporaries are allocated with ble_ecc_heap_alloc and freed on every path.

| Parameter | Type | Description |
|---|---|---|
| `P` | `ptr` | first input point |
| `Q` | `ptr` | second input point |
| `R` | `ptr` | output point |
| `a` | `ptr` | curve parameter a |
| `modulus` | `ptr` | fp_int field modulus |
| `rho` | `u32` | Montgomery reduction digit |

**Returns** `s32`: 0, or an error code (-0xAA for NULL input, MEMORY_E -0x7D, or an arithmetic error)

**Notes:** Exact formula sequence for the general (non-doubling) case was not traced line by line; the description covers the structure.

- Addresses by version: 219: 0x0C05EB00
- Called by: `ble_ecc_point_add_mont`, `ecc_mulmod_ladder_ct`, `ecc_verify_hash_ex`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `ecc_projective_dbl_point`, `fp_clear`, `mp_init_multi`, `fp_mul_checked`, `fp_submod_ct_thunk`, `fp_addmod_ct_thunk`, `mp_cmp`, `mp_copy`, `mp_iszero`, `fp_sqr_thunk`, `fp_montgomery_reduce_thunk`, `fp_div_2_mod_ct_thunk`, `get_digit_count`
- Confidence: medium

## ecc_projective_dbl_point

**Double a Jacobian point (a = -3 shortcut): out = 2 * in, with constant-time field operations**

wolfSSL-style Jacobian doubling. The input point (X, Y, Z at offsets 0, 0x68, 0xD0) is copied to the output and then computed with the a = -3 sequence: t1 = Z^2, t2 = (X - t1)(X + t1), M = 3 * t2, Z3 = 2 * Y * Z, followed by the X and Y updates. Every multiply is followed by Montgomery reduction with the modulus and rho, and additions, subtractions and halvings use the constant-time helpers fp_addmod_ct, fp_submod_ct and fp_div_2_mod_ct. The curve parameter a (third argument) is not read by the decompiled body, so the routine is correct only for a = -3, which holds for the NIST prime curves. Two temporaries are allocated and freed; NULL input returns ECC_BAD_ARG_E (-0xAA). Called by ecc_projective_add_point when both inputs are the same point and by ecc_mulmod_ladder_ct to form 2P.

| Parameter | Type | Description |
|---|---|---|
| `in` | `ptr` | input point P (X at +0, Y at +0x68, Z at +0xD0) |
| `out` | `ptr` | output point, receives 2P |
| `a` | `ptr` | curve parameter a (not read by the body) |
| `modulus` | `ptr` | fp_int field modulus |
| `rho` | `u32` | Montgomery reduction digit |

**Returns** `s32`: 0, or an error code (-0xAA for NULL input, MEMORY_E -0x7D, or an arithmetic error)

- Addresses by version: 219: 0x0C05E868
- Called by: `ecc_projective_add_point`, `ecc_mulmod_ladder_ct`, `ecc_verify_hash_ex`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `fp_clear`, `mp_init_multi`, `fp_mul_checked`, `fp_submod_ct_thunk`, `fp_addmod_ct_thunk`, `mp_copy`, `fp_sqr_thunk`, `fp_montgomery_reduce_thunk`, `fp_div_2_mod_ct_thunk`
- Confidence: medium

## ecc_randomize_projective

**Re-randomise a point's projective coordinates with a random factor r (Z*=r, X*=r^2, Y*=r^3)**

Draws r with wc_ecc_gen_k (0x0C05F218) into temp2, then multiplies Z by r, computes t1 = r^2 and r = r^3, and multiplies X by r^2 and Y by r^3, with a Montgomery reduction after each product. This is the Coron-style projective blinding that hides intermediate values during the ladder. It runs only when the ladder is given an RNG (see ecc_mulmod_ladder_ct), and a failed random draw returns before any coordinate is touched.

| Parameter | Type | Description |
|---|---|---|
| `rng` | `ptr` | RNG state |
| `size` | `s32` | key size in bytes |
| `point` | `ptr` | ecc_point to re-randomise |
| `modulus` | `ptr` | fp_int field modulus |
| `rho` | `u32` | Montgomery reduction digit |
| `t1` | `ptr` | temporary fp_int |
| `t2` | `ptr` | temporary fp_int, receives r |

**Returns** `s32`: 0 or the error from wc_ecc_gen_k

**Notes:** The bound used when drawing r is uncertain: the decompiled call to 0x0C05F218 passes only three arguments, so the fourth is not known.

- Addresses by version: 219: 0x0C05F28C
- Called by: `ecc_mulmod_ladder_ct`
- Calls: `wc_ecc_gen_k`, `fp_mul_checked`, `fp_sqr_thunk`, `fp_montgomery_reduce_thunk`
- Confidence: medium

## ecc_shared_secret

**ECDH core: X coordinate of (private scalar * peer point) written to the output buffer**

wolfSSL-style ecc_shared_secret(key, point, out, outlen). It loads prime, a and order from key->dp with wc_ecc_curve_load (mask 0x0B), requires an RNG on the key (MISSING_RNG_E, -0xEC, otherwise), and multiplies the private scalar at key+0x150 by the peer point with ecc_mulmod_ex2 (RNG on), then maps the product to affine with ecc_map_ex. The big-endian X coordinate is written right-aligned into out with leading zero padding up to the field size. A too-small out returns BUFFER_E (-0x84), and *outlen is set to the required field size in that case and on success. The other failure paths set *outlen to 0. Temporaries and the curve context are zeroed and freed.

| Parameter | Type | Description |
|---|---|---|
| `key` | `ptr` | private ecc_key (dp at +0x10, rng at +0x1b8, scalar at +0x150) |
| `point` | `ptr` | peer public point |
| `out` | `ptr` | output buffer |
| `outlen` | `ptr` | in: buffer size, out: bytes written (u32) |

**Returns** `s32`: 0, -0xEC (MISSING_RNG_E), -0x84 (BUFFER_E), -0x7D, or an ECC arithmetic error

- Addresses by version: 219: 0x0C05FB10
- Called by: `wc_ecc_shared_secret`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `wc_ecc_curve_free`, `wc_ecc_curve_load`, `ecc_map_ex`, `wc_ecc_new_point_h`, `ecc_mulmod_ex2`, `fp_clear`, `mp_unsigned_bin_size`, `fp_to_unsigned_bin_thunk`, `mp_montgomery_setup`, `memset`
- Confidence: medium

## ecc_verify_hash_ex

**ECDSA verify core: check x(u1*G + u2*Q) mod n against r and set *res**

wolfSSL-style ecc_verify_hash_ex(r, s, hash, hashlen, res, key). *res is cleared first. It rejects r or s that are zero or not below the order (-0x79), reads the digest with fp_read_unsigned_bin and truncates it to the order's bit length, then computes w = s^-1 mod n (0x0C0635AC), u1 = e * w mod n and u2 = r * w mod n. The point R = u1 * G + u2 * Q is formed with two ecc_mulmod_ex calls (G from the curve context, Q = key->pubkey) and ecc_projective_add_point, then mapped to affine with ecc_map_ex. *res is set to 1 when x(R) mod n equals r. A private-only key (type 3) first gets its public point from ecc_make_pub_ex. All temporaries are freed on every path.

| Parameter | Type | Description |
|---|---|---|
| `r` | `ptr` | signature r fp_int |
| `s` | `ptr` | signature s fp_int |
| `hash` | `ptr` | message digest |
| `hashlen` | `s32` | digest length in bytes |
| `res` | `ptr` | output verdict, 1 = valid, 0 = invalid (s32) |
| `key` | `ptr` | ecc_key with public point |

**Returns** `s32`: 0 when the check ran (verdict in *res), -0x79 for out-of-range r or s, or an error code

- Addresses by version: 219: 0x0C0601FC
- Called by: `wc_ecc_verify_hash`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `wc_ecc_curve_free`, `wc_ecc_curve_load`, `ecc_projective_dbl_point`, `ecc_projective_add_point`, `ecc_map_ex`, `wc_ecc_new_point_h`, `ecc_mulmod_ex`, `ecc_make_pub_ex`, `mp_init`, `fp_clear`, `mp_init_multi`, `fp_mulmod_thunk`, `fp_mod_thunk`, `fp_invmod_thunk` ...
- Confidence: medium

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
- Called by: `fp_div`, `fp_mod`, `fp_invmod`, `fp_add_thunk`
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

## fp_add_thunk

**Branch-only alias of fp_add (signed big-integer addition)**

Single-instruction thunk that branches to fp_add at 0x0C061FE8; the decompiled body shown is the target's. Called from ble_219_0c05f8c4 and ble_219_0c060828.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | fp_int a |
| `param_2` | `ptr` | fp_int b |
| `param_3` | `ptr` | fp_int result c |
| `param_4` | `u32` | extra argument passed through to the helper |

**Returns** `s32`: 0 (as the target returns)

- Addresses by version: 219: 0x0C064088
- Called by: `ecc_mulmod_ex2`, `ecc_point_on_curve_check`
- Calls: `fp_add`
- Confidence: high

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
- Called by: `fp_addmod_ct_thunk`
- Calls: `fp_cmp_mag_ct`, `s_fp_add`
- Confidence: high

## fp_addmod_ct_thunk

**Branch-only alias of fp_addmod_ct (constant-time modular addition)**

Single-instruction thunk that branches to fp_addmod_ct at 0x0C062654; the decompiled body shown is the target's. It computes d = (a + b) mod c in constant time. Called from ble_219_0c05e868 and ble_219_0c05eb00.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | fp_int a |
| `param_2` | `ptr` | modulus c, passed through to the helper |
| `param_3` | `ptr` | fp_int b |
| `param_4` | `ptr` | fp_int result d |

**Returns** `s32`: 0 (as the target returns)

- Addresses by version: 219: 0x0C0640E8
- Called by: `ecc_projective_dbl_point`, `ecc_projective_add_point`
- Calls: `fp_addmod_ct`
- Confidence: high

## fp_clear

**Zero a big integer in place (NULL-safe, no return value)**

If a is non-NULL: used = 0, sign = 0 and the 24-digit array (0x60 bytes) cleared with memset; NULL is ignored. Same body as mp_init (0c063fb8) but void. This matches wolfSSL mp_clear(a) { if (a == NULL) return; fp_clear(a); } and is the routine the ECC code calls after every temporary (very many callers: 0c05b724, 0c05e420, 0c05e474, 0c05e4e8, 0c05e868, 0c05eb00, 0c05efc0, 0c05f1b0, 0c05f71c ...). Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | fp_int to clear, or NULL |

**Notes:** Functionally this is wolfSSL's mp_clear; the name mp_clear was already assigned in wave 1 to the empty function 0c064000 (which is more likely mp_free/fp_free), so the inner routine's name fp_clear is used here.

- Addresses by version: 219: 0x0C063FEC
- Called by: `ble_ecc_point_add_mont`, `ble_ecc_scalar_base_mult`, `ble_crypto_ecdsa_p256_verify`, `GetInt`, `DecodeECC_DSA_Sig`, `wc_ecc_curve_free`, `ecc_point_to_montgomery`, `ecc_projective_dbl_point`, `ecc_projective_add_point`, `ecc_map_ex`, `wc_ecc_del_point`, `ecc_mulmod_ex` ...
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
- Called by: `fp_div`, `fp_invmod`
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

## fp_div

**Divide two fp_ints: quotient c = a / b and remainder d = a mod b (Knuth algorithm D)**

TFM fp_div. A zero divisor returns -1 (FP_VAL). When |a| < |b| the quotient is 0 and the remainder is a. Otherwise both operands are normalised by a left shift (fp_mul_2d) so the top divisor digit has its high bit set. The quotient digits are estimated with 64-bit division (__udivdi3), corrected with fp_mul_d, fp_sub and fp_cmp, and the remainder is un-normalised with fp_div_2d. Either output (c or d) may be NULL. A 0x208-byte scratch structure is used. Returns 0 on success, -1 for a zero divisor, -2 on allocation failure.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | dividend a |
| `param_2` | `ptr` | divisor b |
| `param_3` | `ptr` | quotient c, may be NULL |
| `param_4` | `ptr` | remainder d, may be NULL |

**Returns** `s32`: 0 on success; -1 for a zero divisor; -2 on allocation failure

- Addresses by version: 219: 0x0C062FE4
- Called by: `fp_mod`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `fp_add`, `fp_sub`, `fp_mul_d`, `fp_cmp`, `fp_lshd`, `fp_mul_2d`, `fp_rshd`, `fp_div_2d`, `__udivdi3`, `memcpy`, `memset`
- Confidence: high

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
- Called by: `fp_div_2_mod_ct`, `fp_invmod`
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
- Called by: `fp_div_2_mod_ct_thunk`
- Calls: `fp_div_2`
- Confidence: high

## fp_div_2_mod_ct_thunk

**Branch-only alias of fp_div_2_mod_ct (constant-time halving modulo b)**

Single-instruction thunk that branches to fp_div_2_mod_ct at 0x0C062450; the decompiled body shown is the target's. It computes c = (a / 2) mod b for 0 <= a < b: when a is odd it adds b first, then halves the result, in constant time. Called from ble_219_0c05e868 and ble_219_0c05eb00.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | fp_int a |
| `param_2` | `ptr` | modulus b |
| `param_3` | `ptr` | fp_int result c |

**Returns** `s32`: 0 (as the target returns)

- Addresses by version: 219: 0x0C064498
- Called by: `ecc_projective_dbl_point`, `ecc_projective_add_point`
- Calls: `fp_div_2_mod_ct`
- Confidence: high

## fp_div_2d

**Divide a big integer by 2^b giving quotient and optional remainder**

wolfSSL TFM fp_div_2d: c = a >> b and, when d is non-NULL, d = a mod 2^b. For b <= 0 it copies a to c and clears d. Otherwise it copies a to c, computes the remainder with fp_mod_2d (0x0C0624E8) from the original a before shifting, shifts whole 32-bit digits with fp_rshd (0x0C062E40) when b >= 32, shifts the remaining bits with fp_rshb (0x0C062EA8), and trims leading zero digits from the result. Uses newlib memcpy and memset for the copies.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | input fp_int a |
| `param_2` | `u32` | bit count b, signed |
| `param_3` | `ptr` | quotient output c |
| `param_4` | `ptr` | remainder output d, or NULL |

- Addresses by version: 219: 0x0C062F28
- Called by: `fp_div`
- Calls: `fp_mod_2d`, `fp_rshd`, `fp_rshb`, `memcpy`, `memset`
- Confidence: high

## fp_invmod

**Modular inverse c = a^-1 mod b (TFM fp_invmod): odd modulus uses binary extended Euclid**

wolfSSL TFM fp_invmod. Returns -1 when b is negative or zero, or when a is zero. Otherwise it allocates a scratch block through the allocator thunk thunk_FUN_0c07097c (0x270 bytes = six 104-byte fp_int slots when b is odd, 0x340 bytes = eight slots when b is even) and returns -2 if that fails. For an odd modulus it first reduces a with fp_mod (ble_219_0c0634c4) when fp_cmp (ble_219_0c0628b4) reports a >= b, then runs a binary extended Euclid on u = b and v = a mod b: u (or v) is halved with fp_div_2 (ble_219_0c0623cc) while even, and the matching coefficient slots are adjusted by plus or minus b with fp_add and fp_sub until u reaches 0. If the leftover v equals 1, the coefficient in slot 5 is reduced into [0, b) with fp_add and fp_sub and copied to c, and the function returns 0; any other leftover means there is no inverse and it returns -1. The even-modulus branch runs a similar loop over eight slots with the same helpers, and its details are less certain. Scratch memory is zeroed with memset and released through thunk_FUN_0c07098c on every path.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | value to invert (fp_int) |
| `b` | `ptr` | modulus (fp_int), must be positive and nonzero |
| `c` | `ptr` | output (fp_int), receives the inverse in [0, b) |

**Returns** `s32`: 0 on success; -1 for invalid input or when a has no inverse mod b; -2 when the scratch block cannot be allocated

**Notes:** The odd/even split is on b->dp[0] & 1, as in TFM (fp_invmod_slow for an odd modulus). The even branch is identified only by its structure. The packet lists ble_219_0c05cba0 and ble_219_0c05cba4 as callees, but no call to them is visible in this decompile, so they are not described here.

- Addresses by version: 219: 0x0C0635AC
- Called by: `fp_invmod_thunk`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `fp_add`, `fp_sub`, `fp_div_2`, `fp_cmp`, `fp_mod`, `memcpy`, `memset`
- Confidence: medium

## fp_invmod_thunk

**Branch-only alias of fp_invmod (modular inverse c = a^-1 mod b)**

One-instruction tail branch to ble_219_0c0635ac (fp_invmod). Arguments a, b and c pass through unchanged.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | value to invert (fp_int) |
| `b` | `ptr` | modulus (fp_int) |
| `c` | `ptr` | output (fp_int) |

**Returns** `s32`: as fp_invmod: 0, -1 or -2

- Addresses by version: 219: 0x0C0640F0
- Called by: `ecc_map_ex`, `ecc_verify_hash_ex`
- Calls: `fp_invmod`
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
- Called by: `fp_mul_2d`, `fp_div`
- Calls: `memset`
- Confidence: high

## fp_mod

**Modular reduction c = a mod b with the remainder taking the sign of b**

TFM fp_mod. It takes the remainder of a divided by b with fp_div (0c062fe4) into a scratch value. If the remainder's sign matches b's sign it is copied to c. Otherwise b is added to it (fp_add), so the result lies in [0, b) for positive b.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | dividend a |
| `param_2` | `ptr` | modulus b |
| `param_3` | `ptr` | result c |
| `param_4` | `u32` | unused |

**Returns** `s32`: 0 on success; -1 for a zero modulus; -2 on allocation failure

- Addresses by version: 219: 0x0C0634C4
- Called by: `fp_mulmod`, `fp_invmod`, `fp_mod_thunk`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `fp_add`, `fp_div`, `memcpy`, `memset`
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
- Called by: `fp_div_2d`
- Calls: `memcpy`, `memset`
- Confidence: high

## fp_mod_thunk

**Branch-only alias of fp_mod (c = a mod b, remainder takes the sign of b)**

One-instruction tail branch to ble_219_0c0634c4 (fp_mod). The target computes the remainder with fp_div (ble_219_0c062fe4) into a heap temporary, copies it to the output when its sign already matches b, and otherwise adds b with fp_add. Arguments pass through unchanged.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | dividend (fp_int) |
| `b` | `ptr` | modulus (fp_int) |
| `c` | `ptr` | output (fp_int) |
| `param_4` | `u32` | forwarded to the target unchanged |

**Returns** `s32`: as fp_mod: 0 on success, otherwise the failing status

- Addresses by version: 219: 0x0C0640EC
- Called by: `ble_ecc_scalar_base_mult`, `ecc_map_ex`, `wc_ecc_gen_k`, `ecc_verify_hash_ex`, `ecc_point_on_curve_check`
- Calls: `fp_mod`
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
- Called by: `fp_montgomery_calc_normalization_thunk`
- Calls: `s_fp_sub`, `fp_mul_2`, `memset`
- Confidence: high

## fp_montgomery_calc_normalization_thunk

**Branch-only alias of fp_montgomery_calc_normalization (R mod b)**

Single-instruction thunk that branches to fp_montgomery_calc_normalization at 0x0C062940; the decompiled body shown is the target's. It computes a = R mod b, with R = 2^(32 * used digits of b), by repeated doubling and conditional subtraction, for Montgomery normalisation. Called from ble_219_0c05b724 and ble_219_0c05e558.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | fp_int result a |
| `param_2` | `ptr` | modulus b |
| `param_3` | `u32` | unused by the decompiled body |
| `param_4` | `u32` | fallback word used when b is a single digit |

**Returns** `s32`: 0 on success, or the error code from the doubling helper

- Addresses by version: 219: 0x0C064288
- Called by: `ble_ecc_point_add_mont`, `ecc_point_to_montgomery`
- Calls: `fp_montgomery_calc_normalization`
- Confidence: high

## fp_montgomery_reduce

**Montgomery reduction x = x * R^-1 mod m, word by word, with a final conditional subtract of m**

TFM fp_montgomery_reduce. The modulus must have at most 12 digits (384 bits), else -1. It works on a scratch copy of x. For each of the low digits it computes u = x[i] * rho (mod 2^32), where rho = -1/m mod 2^32, and adds u * m shifted by i digits with carry propagation. After all digits the high half is shifted down by the modulus digit count. A final s_fp_sub subtracts m when the result is at least m, comparing from the top digit. Returns 0 on success, -1 for a modulus too big, -2 on allocation failure.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | x, in and out (reduced value) |
| `param_2` | `ptr` | modulus m, at most 12 digits |
| `param_3` | `u32` | rho = -1/m mod 2^32 |

**Returns** `s32`: 0 on success; -1 for a modulus above 12 digits; -2 on allocation failure

- Addresses by version: 219: 0x0C062A28
- Called by: `ecc_field_inv_fermat`, `fp_montgomery_reduce_thunk`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `s_fp_sub`, `memset`
- Confidence: high

## fp_montgomery_reduce_thunk

**Two-instruction wrapper that calls fp_montgomery_reduce and returns**

Calls ble_219_0c062a28 (fp_montgomery_reduce) with whatever the caller left in the argument registers, and returns. It takes no arguments of its own and leaves the callee's result in r0. Its callers in the packet list are ECC code paths.

**Returns** `s32`: the callee's result in r0 (fp_montgomery_reduce: 0, -1 or -2)

**Notes:** The decompile shows an empty argument list, but fp_montgomery_reduce takes three meaningful arguments (x, modulus, mp) that the caller places in r0 to r2.

- Addresses by version: 219: 0x0C064450
- Called by: `ecc_projective_dbl_point`, `ecc_projective_add_point`, `ecc_map_ex`, `ecc_randomize_projective`
- Calls: `fp_montgomery_reduce`
- Confidence: high

## fp_mul

**Multiply two fp_ints, c = a * b (comba column accumulation); fails when the digit sum exceeds 23**

TFM fp_mul in comba form. It requires used(a) + used(b) <= 23, otherwise -1 (FP_VAL), and allocates a 0x68-byte scratch fp_int, returning -2 on allocation failure. Column by column it accumulates 32x32 to 64-bit products with carry propagation, writing one result digit per column. The result sign is the XOR of the operand signs, zero is normalised to positive, and the scratch value is copied into c with memcpy before the scratch is freed. The shared group of big-integer routines (fp_sqr, fp_div and so on) sits next to it.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | operand a |
| `param_2` | `ptr` | operand b |
| `param_3` | `ptr` | destination c |

**Returns** `s32`: 0 on success; -1 when the digit sum exceeds 23; -2 on allocation failure

- Addresses by version: 219: 0x0C062218
- Called by: `fp_mul_comba24`, `fp_mulmod`, `fp_mul_checked`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `memcpy`, `memset`
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
- Called by: `fp_div`
- Calls: `fp_lshd`, `memcpy`
- Confidence: high

## fp_mul_checked

**Checked multiply c = a * b: rejects digit sums above 24, then fp_mul and clears stale digits**

Returns -1 without computing anything when a->used + b->used exceeds 24, the 24-digit capacity of a 104-byte fp_int. Otherwise it calls fp_mul (ble_219_0c062218) to form the product in c, then zeroes the dp digits of c between its new used count and its previous used count so that no stale high digits remain. The return value is fp_mul's status (0 on success).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | multiplicand (fp_int) |
| `b` | `ptr` | multiplier (fp_int) |
| `c` | `ptr` | product output (fp_int) |

**Returns** `s32`: 0 on success, -1 when the digit sum exceeds 24, otherwise fp_mul's status

**Notes:** Same contract as fp_mul_comba24 (ble_219_0c06237c) but without its temporary allocation, so it is likely a second copy of the same wrapper in the binary. The name is chosen to keep names unique.

- Addresses by version: 219: 0x0C064090
- Called by: `ecc_projective_dbl_point`, `ecc_projective_add_point`, `ecc_map_ex`, `ecc_randomize_projective`, `ecc_point_on_curve_check`
- Calls: `fp_mul`
- Confidence: high

## fp_mul_comba24

**Fixed-capacity multiply wrapper c = a * b for digit sums up to 24; clears stale digits of c**

TFM-style fp_mul_comba24 wrapper. It rejects operand digit sums above 24 with -1, multiplies through fp_mul (0c062218), and then zeroes the digits of c above its new used count so no stale digits remain from an earlier, larger value.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | operand a |
| `param_2` | `ptr` | operand b |
| `param_3` | `ptr` | destination c |

**Returns** `s32`: 0 on success; -1 when the digit sum exceeds 24; -2 on allocation failure

**Notes:** The name follows the TFM fixed-size variant with a 24-digit cutoff; the decompile only shows the size guard and the call to fp_mul.

- Addresses by version: 219: 0x0C06237C
- Called by: `ecc_field_inv_fermat`
- Calls: `fp_mul`
- Confidence: medium

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
- Called by: `fp_div`, `fp_read_radix`
- Confidence: high

## fp_mulmod

**Modular multiply c = a * b mod m for total digit counts up to 24**

TFM fp_mulmod. It requires used(a) + used(b) <= 24, otherwise -1. It multiplies a and b into a scratch fp_int with fp_mul (0c062218) and reduces the product modulo m with fp_mod (0c0634c4) into the result. Returns 0 on success.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | operand a |
| `param_2` | `ptr` | operand b |
| `param_3` | `ptr` | modulus m |
| `param_4` | `ptr` | result c |

**Returns** `s32`: 0 on success; -1 when the digit sum exceeds 24; -2 on allocation failure

- Addresses by version: 219: 0x0C06353C
- Called by: `fp_mulmod_thunk`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `fp_mul`, `fp_mod`, `memset`
- Confidence: high

## fp_mulmod_thunk

**Branch-only alias of fp_mulmod (modular multiply c = a * b mod m)**

One-instruction tail branch to ble_219_0c06353c (fp_mulmod). It has no logic of its own and passes all four arguments through unchanged.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | multiplicand (fp_int) |
| `b` | `ptr` | multiplier (fp_int) |
| `m` | `ptr` | modulus (fp_int) |
| `c` | `ptr` | output (fp_int) |

**Returns** `s32`: as fp_mulmod: 0 on success, -1 for a digit sum above 24, -2 on allocation failure

- Addresses by version: 219: 0x0C0640E0
- Called by: `ble_ecc_point_add_mont`, `ecc_point_to_montgomery`, `ecc_verify_hash_ex`
- Calls: `fp_mulmod`
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
- Called by: `ble_ecc_point_add_mont`, `ble_ecc_scalar_base_mult`, `ble_crypto_diversify`, `wc_ecc_curve_load`, `wc_ecc_check_key`
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
- Called by: `fp_div_2d`, `fp_rshb_thunk`
- Calls: `fp_rshd`
- Confidence: high

## fp_rshb_thunk

**Branch-only alias of fp_rshb (in-place right shift by bits)**

Single-instruction thunk that branches to fp_rshb at 0x0C062EA8; the decompiled body shown is the target's. It shifts the big integer right in place by the given number of bits, after whole-digit shifts for counts of 32 or more. Called from ble_219_0c0601fc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | fp_int a, shifted in place |
| `param_2` | `u32` | bit count |

- Addresses by version: 219: 0x0C064284
- Called by: `ecc_verify_hash_ex`
- Calls: `fp_rshb`
- Confidence: high

## fp_rshd

**Shift a big integer right by whole 32-bit digits**

wolfSSL TFM fp_rshd(a, x). If x >= a->used the value becomes zero (used = 0, sign = 0, all 96 digit bytes cleared with memset). Otherwise digits are moved down (dp[i] = dp[i + x] for i < used - x), the vacated top x digits are zeroed with memset, used is reduced by x and the value is clamped. Called from fp_rshb (0c062ea8), fp_div_2d (0c062f28) and fp_div (0c062fe4). Part of the wolfSSL fast-math (tfm.c) big-integer group (fp_int: used +0, sign +4, dp[24] +8).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | fp_int shifted in place |
| `x` | `s32` | number of digits to shift right |

- Addresses by version: 219: 0x0C062E40
- Called by: `fp_rshb`, `fp_div_2d`, `fp_div`
- Calls: `memset`
- Confidence: high

## fp_sqr

**Square wrapper b = a^2: runs fp_sqr_comba and clears stale digits of b above the new used count**

TFM fp_sqr wrapper. The source a is passed through to fp_sqr_comba (0c0626f4) in the first argument register, so the decompile shows it as unused. After squaring it zeroes the digits of b above the new used count, so stale digits from an earlier value are cleared.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source a (passed through to fp_sqr_comba) |
| `param_2` | `ptr` | destination b |

- Addresses by version: 219: 0x0C062880
- Called by: `ecc_field_inv_fermat`, `fp_sqr_thunk`
- Calls: `fp_sqr_comba`
- Confidence: high

## fp_sqr_comba

**Square a fp_int, b = a^2, with the comba method that doubles the cross products**

TFM comba squaring. The result digit count is 2 * used(a), clamped to 23 digits. The routine accumulates each cross product a[i] * a[j] (i < j) once and then doubles the running sum, and adds the diagonal square a[i]^2 in the even columns. The sign of the result is zero (positive). The destination may alias the source, in which case a scratch fp_int is used. Returns 0, or -2 on allocation failure.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source a |
| `param_2` | `ptr` | destination b |

**Returns** `s32`: 0 on success; -2 on allocation failure

- Addresses by version: 219: 0x0C0626F4
- Called by: `fp_sqr`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `memcpy`, `memset`
- Confidence: high

## fp_sqr_thunk

**Branch-only alias of fp_sqr (b = a^2, stale high digits cleared)**

One-instruction tail branch to ble_219_0c062880 (fp_sqr). The target squares the source (param_1) into the destination (param_2) through fp_sqr_comba (ble_219_0c0626f4) and then zeroes the destination digits above its new used count.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | source (fp_int) |
| `b` | `ptr` | destination (fp_int) |

- Addresses by version: 219: 0x0C06444C
- Called by: `ecc_projective_dbl_point`, `ecc_projective_add_point`, `ecc_map_ex`, `ecc_randomize_projective`, `ecc_point_on_curve_check`
- Calls: `fp_sqr`
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
- Called by: `fp_div`, `fp_invmod`, `fp_sub_d`, `fp_sub_thunk`
- Calls: `s_fp_add`, `s_fp_sub`
- Confidence: high

## fp_sub_d

**Subtract a 32-bit digit from a big integer: c = a - d**

Builds a one-digit fp_int holding d in a temporary (used = 1 when d is nonzero, dp[0] = d, sign = 0, and the other 23 digits zeroed with memset), calls fp_sub (ble_219_0c062068) to compute c = a - temp, and frees the temporary. The temporary is 0x68 bytes from the allocator thunk thunk_FUN_0c07097c; if that allocation fails the function returns -2 and c is not touched. Callers pass d = 2 to form modulus - 2, the Fermat exponent used by ecc_field_inv_fermat (ble_219_0c063d2c).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | minuend (fp_int) |
| `d` | `u32` | digit to subtract (0 allowed) |
| `c` | `ptr` | output (fp_int) |

**Returns** `s32`: 0 on success, -2 if the temporary cannot be allocated, otherwise the status returned by fp_sub

**Notes:** Named after TFM fp_sub_d, which is not otherwise present in this build. The decompile passes five arguments to fp_sub; only the three meaningful ones are used here.

- Addresses by version: 219: 0x0C063CE4
- Called by: `ecc_field_inv_fermat`, `fp_sub_d_thunk`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `fp_sub`, `memset`
- Confidence: high

## fp_sub_d_thunk

**Branch-only alias of fp_sub_d (c = a - d)**

One-instruction tail branch to ble_219_0c063ce4 (fp_sub_d). Arguments pass through unchanged. Its caller in the packet list is ble_219_0c05b86c.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | minuend (fp_int) |
| `d` | `u32` | digit to subtract |
| `c` | `ptr` | output (fp_int) |
| `param_4` | `u32` | forwarded to the target unchanged |

**Returns** `s32`: as fp_sub_d: 0, -2 or the status of fp_sub

- Addresses by version: 219: 0x0C064230
- Called by: `ble_ecc_scalar_base_mult`
- Calls: `fp_sub_d`
- Confidence: high

## fp_sub_thunk

**Branch-only alias of fp_sub (signed big-integer subtraction)**

Single-instruction thunk that branches to fp_sub at 0x0C062068; the decompiled body shown is the target's. Called from ble_219_0c060828.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | fp_int a |
| `param_2` | `ptr` | fp_int b |
| `param_3` | `ptr` | fp_int result c |

**Returns** `s32`: 0 (as the target returns)

- Addresses by version: 219: 0x0C06408C
- Called by: `ecc_point_on_curve_check`
- Calls: `fp_sub`
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
- Called by: `fp_submod_ct_thunk`
- Calls: `fp_cmp_mag_ct`, `s_fp_sub`
- Confidence: high

## fp_submod_ct_thunk

**Branch-only alias of fp_submod_ct (constant-time modular subtraction)**

Single-instruction thunk that branches to fp_submod_ct at 0x0C0625A0; the decompiled body shown is the target's. It computes d = (a - b) mod c in constant time. Called from ble_219_0c05e868 and ble_219_0c05eb00.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | fp_int a |
| `param_2` | `ptr` | modulus c, passed through to the helper |
| `param_3` | `ptr` | fp_int b |
| `param_4` | `ptr` | fp_int result d |

**Returns** `s32`: 0 (as the target returns)

- Addresses by version: 219: 0x0C0640E4
- Called by: `ecc_projective_dbl_point`, `ecc_projective_add_point`
- Calls: `fp_submod_ct`
- Confidence: high

## fp_to_unsigned_bin

**Export a fp_int as big-endian bytes: emit little-endian then reverse in place**

TFM fp_to_unsigned_bin. It copies the source into a scratch fp_int, calls fp_to_unsigned_bin_at_pos (0c062c20) to write the magnitude in little-endian order at offset 0 and gets the byte count, then reverses the byte run in place so the output is big-endian. The extra arguments in the decompile are not used by the logic (decompiler artifacts of the memset call). Returns 0, or -2 on allocation failure.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source fp_int |
| `param_2` | `ptr` | output buffer (at least the magnitude byte count) |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | unused |

**Returns** `s32`: 0 on success; -2 on allocation failure

- Addresses by version: 219: 0x0C062C84
- Called by: `fp_to_unsigned_bin_thunk`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `fp_to_unsigned_bin_at_pos`, `memcpy`, `memset`
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
- Called by: `fp_to_unsigned_bin`
- Confidence: high

## fp_to_unsigned_bin_thunk

**Branch-only alias of fp_to_unsigned_bin (big-endian export of a big integer)**

One-instruction tail branch to ble_219_0c062c84 (fp_to_unsigned_bin). The target copies the integer into a heap temporary, exports it with fp_to_unsigned_bin_at_pos (ble_219_0c062c20) at offset 0, reverses the byte string in place to make it big-endian, and frees the temporary.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | integer to export (fp_int) |
| `buf` | `ptr` | output byte buffer, big-endian |
| `param_3` | `u32` | forwarded to the target unchanged |
| `param_4` | `u32` | forwarded to the target unchanged |

**Returns** `s32`: 0 on success, -2 when the temporary cannot be allocated

- Addresses by version: 219: 0x0C0641F0
- Called by: `ecc_shared_secret`
- Calls: `fp_to_unsigned_bin`
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
- Called by: `ecc_mulmod_ladder_ct`
- Confidence: high

## get_digit_count

**Number of used digits in a big integer (NULL-safe)**

Returns the first word (used) of the mp_int, or 0 when the pointer is NULL. wolfSSL's get_digit_count.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | mp_int or NULL |

**Returns** `s32`: number of used digits, 0 for NULL

- Addresses by version: 219: 0x0C0644C0
- Called by: `ecc_projective_add_point`, `ecc_mulmod_ladder_ct`, `ecc_check_pubkey_order`, `wc_ecc_check_key`
- Confidence: high

## hash_drbg_kat_generate

**Known-answer self-test: instantiate, generate twice, return the 128-byte second output**

One-shot Hash_DRBG run used only as the FIPS-style known-answer test in the RNG init and reseed paths (wc_rng_seed_instantiate and wc_RNG_GenerateBlock). It requires entropy (param 4) and an output buffer, and when param 1 is non-zero it also requires the reseed input (param 6). Only a 128-byte request (param 9 == 0x80) is accepted. It allocates a 0x78-byte DRBG, instantiates it from the entropy and the personalisation string (param 2 and 3), optionally reseeds from param 6 and 7, generates once and discards the output, then generates again into out. The DRBG object is wiped, the wipe is verified with an OR-accumulated check, and it is freed. The callers pass an extra argument (0xfffffffe) that the decompiled signature does not declare.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero to run the reseed step |
| `param_2` | `ptr` | personalisation string, may be NULL |
| `param_3` | `u32` | personalisation length |
| `param_4` | `ptr` | entropy input |
| `param_5` | `u32` | entropy length |
| `param_6` | `ptr` | reseed entropy, required when param 1 is non-zero |
| `param_7` | `u32` | reseed entropy length |
| `param_8` | `ptr` | 128-byte output |
| `param_9` | `s32` | output length; must be 128 |

**Returns** `s32`: 0 when the known answer runs cleanly; -1 on any instantiate, reseed or generate failure or a failed wipe check; -173 for bad arguments; -125 on allocation failure

- Addresses by version: 219: 0x0C0615C0
- Called by: `wc_rng_seed_instantiate`, `wc_RNG_GenerateBlock`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `Hash_DRBG_Instantiate`, `Hash_DRBG_Reseed`, `Hash_DRBG_Generate`
- Confidence: high

## hsm_trng_read_bytes

**Fill a buffer with hardware TRNG bytes, polling the HSM TRNG status register**

Waits for hardware semaphore 1 (hal_hwsem_try_lock polled for about 500 timer units), then fills the buffer from the TRNG in chunks. For each chunk it sets the 0x40008000 block run state with hal_block_40008000_set_run(0), polls status register 0x40008104 for a ready nibble (timeout DAT_20003E24, 4 us between polls) and, when the error bits 0x0E are clear, reads up to six 32-bit words from 0x40008114..0x40008128 and copies them out little-endian, with the last partial word copied by memcpy. Error bits make it retry up to 20 times before printing the error. On exit it clears 0x4000812C, writes 0xF to 0x40008108 and 0x40008100 and releases semaphore 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output buffer |
| `param_2` | `s32` | number of bytes to produce |

**Returns** `s32`: 0 on success, -1 on repeated error status, -2 on a ready timeout

**Notes:** The hardware semaphore result is not checked: after the 500-unit wait the code continues even without the lock. The meaning of the 0x40008000 block and of the control writes is inferred from the register accesses. The time source ble_219_0c073b30 and the 500 wait value (ble_219_0c073cb0) are not yet named.

- Addresses by version: 219: 0x0C033328
- Peripheral registers: `0x40008004` (A), `0x40008100` (W), `0x40008104` (R), `0x40008108` (W), `0x40008114` (R), `0x40008118` (R), `0x40008128` (R), `0x4000812c` (RW)
- Called by: `ble_chunked_write_24`
- Calls: `hal_hwsem_try_lock`, `hal_hwsem_unlock`, `hal_sys_timer_delay_us`, `hal_block_40008000_set_run`, `trace_printf`, `memcpy`, `ble_ram_patch_thunk_2000031c`, `ble_ram_patch_thunk_20000570`
- Confidence: medium

## mbedtls_sha1_finish_ret

**mbedTLS SHA-1 finish: pad, append 64-bit big-endian bit length, output the 20-byte digest**

Computes high = (total[0] >> 29) | (total[1] << 3) and low = total[0] << 3 and stores them as 8 big-endian bytes on the stack. Padding length is 56-last or 120-last for last = total[0] & 0x3F. Calls mbedtls_sha1_update_ret (ble_219_0c04a924) with the sha1_padding table at 0x0C08400C (0x80 then zeros) and then with the 8 length bytes; if both return 0 the five state words at ctx+8..+0x18 are written big-endian into the 20-byte output param_2. On an error the output is left untouched and nothing is reported (the return value is void here). Caller: mbedtls_sha1_ret (ble_219_0c04aa80).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | mbedtls_sha1_context |
| `param_2` | `ptr` | output: 20-byte SHA-1 digest |

- Addresses by version: 219: 0x0C04A9A8
- Called by: `ble_sha1_oneshot`
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
- Called by: `mbedtls_sha1_finish_ret`, `ble_sha1_oneshot`
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
- Called by: `nb_upgrade_image_digest`, `nb_upgrade_verify_app_image`, `nb_upgrade_session_finish`
- Calls: `md5_encode_le_words`, `md5_update`
- Confidence: high

## md5_init

**Initialise an MD5 context**

Zeroes the 64-bit bit-count words at ctx[0],ctx[1] and loads the standard MD5 initial values into ctx[2..5]: 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476. Called from ble_219_0c03477c, ble_219_0c036868 and ble_219_0c0369d8 (md5sum computation in the upgrade code).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | MD5 context (6 x u32: count lo/hi, state A..D) |

- Addresses by version: 219: 0x0C047E44
- Called by: `nb_upgrade_image_digest`, `nb_upgrade_verify_app_image`, `nb_upgrade_session_begin`
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
- Called by: `nb_upgrade_process_cmd`, `nb_upgrade_image_digest`, `nb_upgrade_verify_app_image`, `md5_final`
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
- Called by: `ble_ecc_scalar_base_mult`, `ecc_mulmod_ex2`
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
- Called by: `ecc_mulmod_ex2`
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
- Called by: `ecc_projective_add_point`, `wc_ecc_gen_k`, `ecc_mulmod_ex2`, `ecc_make_pub_ex`, `ecc_check_privkey_gen`, `ecc_verify_hash_ex`, `ecc_point_on_curve_check`, `wc_ecc_check_key`
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
- Called by: `ecc_point_to_montgomery`, `ecc_map_ex`, `ecc_mulmod_ex2`
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
- Called by: `ecc_mulmod_ladder_ct`, `ecc_mulmod_ex2`
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
- Called by: `ecc_point_to_montgomery`, `ecc_projective_dbl_point`, `ecc_projective_add_point`, `wc_ecc_copy_point`, `ecc_mulmod_ladder_ct`, `ecc_mulmod_ex2`, `ecc_make_pub_ex`, `ecc_check_privkey_gen`, `ecc_verify_hash_ex`
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
- Called by: `ecc_mulmod_ladder_ct`, `ecc_mulmod_ex2`, `ecc_verify_hash_ex`
- Confidence: high

## mp_forcezero

**Zero a big integer (used = 0, sign = +, all 96 digit bytes cleared)**

Sets used = 0 and sign = 0, then clears the 24-digit dp array byte by byte with an explicit loop (wolfSSL ForceZero style, not optimised to memset) so secret values do not remain on the stack. Called on temporaries holding ECC scalars/keys (callers 0c05f8c4, 0c0600c0, 0c0601d0). wolfSSL TFM fast-math big integer (fp_int): s32 used digit count at +0, s32 sign at +4 (0 = positive, 1 = negative), 32-bit digits dp[24] at +8 (0x68 bytes total, FP_SIZE = 24 digits).

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | fp_int to wipe |

**Notes:** Could be fp_zero; the byte-wise loop and the use after secret-dependent computations suggest the ForceZero variant.

- Addresses by version: 219: 0x0C063FD4
- Called by: `ecc_mulmod_ex2`, `wc_ecc_make_key_ex`, `wc_ecc_free`
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
- Called by: `ble_ecc_point_add_mont`, `ble_ecc_scalar_base_mult`, `ble_crypto_ecdsa_p256_verify`, `GetInt`, `ecc_point_to_montgomery`, `wc_ecc_curve_load`, `ecc_mulmod_ex2`, `wc_ecc_make_key_ex`, `ecc_verify_hash_ex`, `wc_ecc_check_key`
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
- Called by: `ecc_projective_dbl_point`, `ecc_projective_add_point`, `ecc_map_ex`, `wc_ecc_new_point_h`, `ecc_make_pub_ex`, `wc_ecc_init`, `ecc_verify_hash_ex`, `ecc_point_on_curve_check`, `wc_ecc_import_x963_ex`
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
- Called by: `ecc_projective_add_point`, `wc_ecc_gen_k`, `ecc_make_pub_ex`, `ecc_verify_hash_ex`, `wc_ecc_check_key`
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
- Called by: `ble_ecc_point_add_mont`, `ble_ecc_scalar_base_mult`, `ecc_mulmod_ex`, `ecc_mulmod_ex2`, `ecc_shared_secret`, `ecc_make_pub_ex`, `ecc_verify_hash_ex`
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
- Called by: `ble_ecc_scalar_base_mult`, `GetInt`, `wc_ecc_gen_k`, `ecc_verify_hash_ex`, `wc_ecc_import_x963_ex`
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
- Called by: `ble_crypto_diversify`, `ecc_map_ex`, `ecc_make_pub_ex`, `ecc_check_privkey_gen`, `ecc_verify_hash_ex`, `wc_ecc_import_x963_ex`
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
- Called by: `ble_crypto_sha256_commit`, `ble_ecc_share_derive`, `ble_ecc_p224_export_derive`, `ble_crypto_diversify`, `ble_crypto_ecdh_seal_p256`
- Confidence: high

## mp_unsigned_bin_size

**Number of bytes needed for the big integer's magnitude**

Computes ceil(bit_length / 8) where the bit length is (used-1)*32 plus the position of the highest set bit in the top digit (the loop shifts the top digit right until zero). Returns 0 for used == 0. This is fp_unsigned_bin_size(a) = (fp_count_bits(a)+7)/8 with fp_count_bits inlined. Called from 0c05fb10.

| Parameter | Type | Description |
|---|---|---|
| `a` | `ptr` | mp_int |

**Returns** `s32`: size in bytes

- Addresses by version: 219: 0x0C0641B8
- Called by: `ecc_shared_secret`
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
- Called by: `fp_add`, `fp_sub`, `fp_submod_ct`, `fp_montgomery_calc_normalization`, `fp_montgomery_reduce`
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
- Called by: `ble_crypto_init`
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
- Called by: `sm_pairing_engine_step`
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
- Called by: `ble_crypto_session_decrypt`, `ble_crypto_ecdh_seal_p256`
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
- Called by: `ble_crypto_session_decrypt`
- Calls: `wc_AesEncrypt`, `GHASH`, `memcpy`
- Confidence: high

## wc_AesGcmEncrypt

**Validate AES-GCM encrypt arguments, then run the software GCM encrypt**

wolfSSL wc_AesGcmEncrypt argument check. It rejects a NULL context (first argument), a zero IV length (sixth argument) and an authentication tag size outside 12..16 (eighth argument, tested as (size - 12) < 5 unsigned), returning BAD_FUNC_ARG (-173, 0xFFFFFF53). Otherwise it tail-calls the software CTR plus GHASH implementation at 0x0C05DE8C (AES_GCM_encrypt_C), which produces the ciphertext and the authentication tag. The data and IV pointers are not checked here.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | wolfSSL Aes context, must be non-NULL |

**Returns** `s32`: result of the software encrypt, or -173 (BAD_FUNC_ARG) for invalid arguments

**Notes:** The 6th and 8th arguments are read from the stack at offsets 0x4 and 0xC, which the decompiler does not declare. The mapping follows the AAPCS stack layout.

- Addresses by version: 219: 0x0C05E2C0
- Called by: `ble_crypto_ecdh_seal_p256`
- Calls: `AES_GCM_encrypt_C`
- Confidence: medium

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
- Called by: `ble_crypto_session_decrypt`, `ble_crypto_ecdh_seal_p256`
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
- Called by: `ble_crypto_session_decrypt`, `ble_crypto_ecdh_seal_p256`
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

## wc_FreeRng

**Wipe and free the Hash_DRBG object of an RNG; returns -199 if the wipe did not zero it**

wolfSSL wc_FreeRng. A NULL RNG returns -173. If the DRBG pointer at +0x08 is set, the 0x78-byte object is overwritten with zeros, read back and OR-accumulated, which gives -199 (0xffffff39) if any byte is still non-zero. The object is then freed. The DRBG pointer and the status byte at +0x0c are cleared and 0 returned otherwise.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | RNG object |

**Returns** `s32`: 0 on success; -199 if the wipe check fails; -173 for NULL

- Addresses by version: 219: 0x0C06156C
- Called by: `ble_fmna_reset_gen_keypair`, `ble_rng_get_32`, `ble_crypto_ecdh_seal_p256`
- Calls: `ble_ecc_heap_free`
- Confidence: high

## wc_HashFinal

**Finish a wolfSSL hash of a given type into a digest buffer; only SHA-256 (type 6) is implemented**

wolfSSL wc_HashFinal with the same type dispatch as wc_HashUpdate. Type 6 calls wc_Sha256Final (0c061c80), which writes the 32-byte digest to the output and resets the context. A NULL context or NULL output returns -173. Types 3, 4, 5, 7, 8 and 10 to 13 return -232 and other values return -173. It is the finish half of the wc_Hash* group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | hash context |
| `param_2` | `s32` | wc_HashType |
| `param_3` | `ptr` | digest output buffer |

**Returns** `s32`: 0 on success; -173 for bad arguments, -232 for a type that is not built in, or the Sha256Final error

- Addresses by version: 219: 0x0C060D80
- Called by: `wc_X963_KDF`
- Calls: `wc_Sha256Final`
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
- Called by: `wc_X963_KDF`
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
- Called by: `wc_X963_KDF`
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
- Called by: `wc_X963_KDF`
- Confidence: high

## wc_HashUpdate

**Feed bytes into a wolfSSL hash context of a given type; only SHA-256 (type 6) is implemented**

wolfSSL wc_HashUpdate, dispatching on the hash type. Type 6 forwards to wc_Sha256Update (0c061b7c). Types 3, 4, 5, 7, 8 and 10 to 13 return -232 (HASH_TYPE_E) because they are not built in. A NULL context or NULL data pointer, and any other type, return -173. This is the update half of the hash group that also holds wc_HashInit (0c060d0c), wc_HashFinal (0c060d80), wc_HashFree (0c060dac) and wc_HashGetDigestSize (0c060ce0), and it is used by wc_X963_KDF.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | hash context |
| `param_2` | `s32` | wc_HashType |
| `param_3` | `ptr` | input data |
| `param_4` | `u32` | input length |

**Returns** `s32`: 0 on success; -173 for bad arguments or unsupported type, -232 for types not built in, or the Sha256Update error

- Addresses by version: 219: 0x0C060D3C
- Called by: `wc_X963_KDF`
- Calls: `wc_Sha256Update`
- Confidence: high

## wc_HmacFinal

**Finish HMAC-SHA-256: H((K ^ opad) || H((K ^ ipad) || message)) written to the output**

wolfSSL wc_HmacFinal. A non-NULL output is required. If no update has been made yet, the ipad block is absorbed first. The inner hash is finished with wc_Sha256Final into the inner-digest slot (+0xf0, 32 bytes). Because Final resets the context to the IV, the same context then absorbs the opad block (+0xb0, 64 bytes) and the inner digest (+0xf0, 32 bytes) and is finalised into the caller's buffer. The update flag is cleared and 0 returned. A non-SHA-256 type returns -173 and so does a NULL output.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Hmac context |
| `param_2` | `ptr` | output buffer (32 bytes for SHA-256) |

**Returns** `s32`: 0 on success; -173 for NULL output or a non-SHA-256 type, or the underlying SHA-256 error

- Addresses by version: 219: 0x0C060F58
- Called by: `ble_crypto_serial_mac`
- Calls: `wc_Sha256Update`, `wc_Sha256Final`
- Confidence: high

## wc_HmacFree

**Free an Hmac context: for macType SHA-256 (6) release the inner hash (wolfSSL wc_HmacFree)**

wolfSSL wc_HmacFree(hmac). Does nothing for NULL. If hmac->macType (byte at +0x114) == 6 (WC_SHA256) it calls wc_Sha256Free (an empty function in this build) and, re-checking the same byte, calls it again with the context pointer, which is just the compiler's rendering of the switch and the empty callee; other MAC types are not built in. No memory is zeroed. Called from 0c05c088 after wc_HmacInit/wc_HmacSetKey/wc_HmacUpdate/wc_HmacFinal.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Hmac context (may be NULL) |

- Addresses by version: 219: 0x0C06100C
- Called by: `ble_crypto_serial_mac`
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
- Called by: `ble_crypto_serial_mac`
- Calls: `memset`
- Confidence: high

## wc_HmacSetKey

**Key an HMAC-SHA-256: build the ipad and opad blocks, hashing keys longer than 64 bytes first**

wolfSSL wc_HmacSetKey, restricted to SHA-256. The Hmac object (layout: inner SHA-256 context at +0x00, ipad at +0x70, opad at +0xb0, inner digest at +0xf0, macType byte at +0x114, update flag byte at +0x115) is first checked for a previous SHA-256 key (macType == 6), in which case wc_Sha256Free is called. The new type is stored at +0x114 and the update flag cleared. Types outside 3..8 and 10..13 return -173. Then wc_InitSha256 resets the inner context. A key of up to 64 bytes is copied into the ipad block and zero-padded. A longer key is hashed with wc_Sha256Update and wc_Sha256Final to 32 bytes and zero-padded to 64. The ipad block is XORed with 0x36 and the opad block (+0xb0) is filled with key ^ 0x5c. Non-SHA-256 types return -173 after the state reset. The word at +0x110 is also cleared (see notes). This is part of the HMAC group with wc_HmacUpdate, wc_HmacFinal, wc_HmacInit and wc_HmacFree.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Hmac context |
| `param_2` | `s32` | wc_HashType; only 6 (SHA-256) is accepted |
| `param_3` | `ptr` | key bytes |
| `param_4` | `u32` | key length in bytes |

**Returns** `s32`: 0 on success; -173 for bad arguments or a non-SHA-256 type, -125 or the hash error otherwise

**Notes:** The store of zero at +0x110 is a 32-bit write to the word wc_HmacInit uses for the heap pointer. The decompile does not show why wolfSSL clears it here; it may be a leftover field clear that is harmless with a NULL heap. Worth checking against the wolfSSL source.

- Addresses by version: 219: 0x0C060DE0
- Called by: `ble_crypto_serial_mac`
- Calls: `wc_Sha256Update`, `wc_Sha256Final`, `wc_InitSha256`, `wc_Sha256Free`, `memcpy`, `memset`
- Confidence: high

## wc_HmacUpdate

**Absorb message bytes into an HMAC-SHA-256; the first update hashes the ipad block**

wolfSSL wc_HmacUpdate. On the first update after wc_HmacSetKey (update flag at +0x115 == 0) the 64-byte ipad block (+0x70) is absorbed into the inner SHA-256 and the flag is set. For a macType other than 6 it only sets the flag and returns 0 without hashing. For SHA-256 the message bytes are then forwarded to wc_Sha256Update (0c061b7c). A NULL Hmac, or a NULL data pointer with a non-zero length, returns -173.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Hmac context |
| `param_2` | `ptr` | message bytes |
| `param_3` | `u32` | message length |

**Returns** `s32`: 0 on success; -173 for bad arguments, or the Sha256Update error

**Notes:** A zero-initialised Hmac that was never keyed (macType 0) is accepted and produces no error at update time; the error surfaces only in wc_HmacFinal.

- Addresses by version: 219: 0x0C060EF4
- Called by: `ble_crypto_serial_mac`
- Calls: `wc_Sha256Update`
- Confidence: high

## wc_InitRng

**wolfSSL wc_InitRng(rng): seed and instantiate the RNG with no nonce, discarding the status**

wolfSSL wc_InitRng wrapper. It calls the RNG seed-and-instantiate routine ble_219_0c061688 with a NULL nonce and zero length and returns nothing. A caller therefore learns about failure only through the status byte at +0x0c of the RNG object, which is 1 when the RNG is ready.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | RNG object |

- Addresses by version: 219: 0x0C061828
- Called by: `ble_fmna_reset_gen_keypair`, `ble_rng_get_32`, `ble_crypto_ecdh_seal_p256`
- Calls: `wc_rng_seed_instantiate`
- Confidence: high

## wc_InitSha256

**Initialise a SHA-256 context**

Returns -173 (BAD_FUNC_ARG) when the context is NULL. Otherwise loads the SHA-256 IV into digest[0..7] (6a09e667 bb67ae85 3c6ef372 a54ff53a 510e527f 9b05688c 1f83d9ab 5be0cd19), zeroes buffLen, loLen, hiLen (words 0x18..0x1a) and word 0x1b (heap), and returns 0. Called by HMAC, HKDF and DRBG code before hashing.

| Parameter | Type | Description |
|---|---|---|
| `sha256` | `ptr` | wolfSSL Sha256 context (digest[8], buffer[16], buffLen, loLen, hiLen, heap) |

**Returns** `s32`: 0 on success, -173 if sha256 is NULL

- Addresses by version: 219: 0x0C061DB0
- Called by: `ble_crypto_sha256_digest`, `ble_crypto_sha256_commit`, `ble_crypto_ecdsa_p256_verify`, `wc_HmacSetKey`, `Hash_df`, `Hash_DRBG_Generate`
- Confidence: high

## wc_RNG_GenerateBlock

**Generate up to 65536 random bytes; reseed from the entropy source when the DRBG asks for it**

wolfSSL wc_RNG_GenerateBlock. The output must be non-NULL and at most 0x10000 bytes, else -173. The status byte at +0x0c must be 1 (ready), else -199. Hash_DRBG_Generate is called first. When it returns 2 (reseed needed) the reseed path runs: a known-answer check with hash_drbg_kat_generate and reseed input, compared against a flash-resident vector; 36 bytes of entropy from ble_219_0c04585c (not yet described); wc_RNG_TestSeed over that entropy; Hash_DRBG_Reseed with the last 32 bytes; then Hash_DRBG_Generate again. A failed known-answer check sets status 3 and returns -209. Any other generate failure sets status 2 and returns -199.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | RNG object |
| `param_2` | `ptr` | output buffer |
| `param_3` | `u32` | number of bytes, 1..65536 |

**Returns** `s32`: 0 on success; -173 for bad arguments; -199 when the RNG is not ready or generate failed; -209 on a self-test failure

- Addresses by version: 219: 0x0C061834
- Called by: `ble_fmna_reset_gen_keypair`, `ble_rng_get_32`, `wc_ecc_gen_k`
- Calls: `ble_chunked_write_24`, `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `Hash_DRBG_Reseed`, `Hash_DRBG_Generate`, `wc_RNG_TestSeed`, `hash_drbg_kat_generate`
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
- Called by: `wc_rng_seed_instantiate`, `wc_RNG_GenerateBlock`
- Confidence: high

## wc_Sha256Final

**Finish SHA-256: pad with 0x80 and bit length, write digest big-endian, reset to IV**

wolfSSL wc_Sha256Final. It appends 0x80 and zero bytes, then the total length in bits as a 64-bit big-endian value (hiLen * 8 plus loLen >> 29 for the high word, loLen << 3 for the low word), transforms the block, and byte-swaps the eight digest words. The digest is written to param 2 as 32 big-endian bytes. The context is then reset to the SHA-256 IV with buffLen, loLen and hiLen cleared, so the same object can be reused. This Final resetting is what lets wc_HmacFinal reuse the context for the outer hash.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | SHA-256 context |
| `param_2` | `ptr` | 32-byte digest output |

**Returns** `s32`: 0 on success; -173 for NULL pointers; or the transform error

- Addresses by version: 219: 0x0C061C80
- Called by: `ble_crypto_sha256_digest`, `ble_crypto_sha256_commit`, `ble_crypto_ecdsa_p256_verify`, `wc_HashFinal`, `wc_HmacSetKey`, `wc_HmacFinal`, `Hash_df`, `Hash_DRBG_Generate`
- Calls: `Transform_Sha256`, `memset`
- Confidence: high

## wc_Sha256Free

**Free a SHA-256 context (empty in this build)**

Empty function (single return). wolfSSL's wc_Sha256Free only has work to do for hardware/async back ends, none of which are built here. Called after each SHA-256 use by HMAC/HKDF/DRBG code.

| Parameter | Type | Description |
|---|---|---|
| `sha256` | `ptr` | Sha256 context (argument ignored) |

**Notes:** Shared empty free hook; could equally be another trivial free function used with SHA-256 contexts.

- Addresses by version: 219: 0x0C061E10
- Called by: `ble_crypto_sha256_digest`, `ble_crypto_sha256_commit`, `ble_crypto_ecdsa_p256_verify`, `wc_HashFree`, `wc_HmacSetKey`, `wc_HmacFree`, `Hash_df`, `Hash_DRBG_Generate`
- Confidence: medium

## wc_Sha256Update

**Absorb bytes into a SHA-256 context: fill and transform 64-byte blocks, count bytes in loLen/hiLen**

wolfSSL wc_Sha256Update. The 64-byte buffer is at +0x20 and the bytes buffered so far at +0x60. The byte count is kept in loLen (+0x64) with a carry into hiLen (+0x68), in bytes, and converted to bits only at Final. Partial data is copied into the buffer first. When the buffer fills it is byte-swapped in place to big-endian words and Transform_Sha256 (0c061950) runs. Full 64-byte blocks in the input are swapped and transformed directly. The tail goes back into the buffer. A corrupt buffer length returns -132 (BUFFER_E).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | SHA-256 context |
| `param_2` | `ptr` | input data |
| `param_3` | `u32` | input length in bytes |

**Returns** `s32`: 0 on success; -173 for a NULL context or a NULL pointer with non-zero length; -132 for a corrupt buffer length; or the transform error

- Addresses by version: 219: 0x0C061B7C
- Called by: `ble_crypto_sha256_digest`, `ble_crypto_sha256_commit`, `ble_crypto_ecdsa_p256_verify`, `wc_HashUpdate`, `wc_HmacSetKey`, `wc_HmacUpdate`, `wc_HmacFinal`, `Hash_df`, `Hash_DRBG_Generate`
- Calls: `Transform_Sha256`, `memcpy`
- Confidence: high

## wc_X963_KDF

**ANSI X9.63 KDF: out = Hash(Z || counter || SharedInfo) blocks with a counter from 1 (SHA-256 only)**

wolfSSL wc_X963_KDF. The hash type must lie in 4..8 (the wolfSSL SHA-family range), but only SHA-256 (type 6) is built, so the other types fail with -232 from wc_HashInit. The shared secret Z (param 2, length param 3) and the optional SharedInfo (param 4 and 5, skipped when NULL) are hashed after a 4-byte big-endian counter. The counter starts at 0 and is incremented before each block, so the first block uses counter 1. Each digest is copied to the output with memcpy and the last block is truncated. The hash context is a 0x70-byte heap object driven by wc_HashInit, wc_HashUpdate, wc_HashFinal and wc_HashFree.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | hash type (wolfSSL enum; 6 = SHA-256) |
| `param_2` | `ptr` | shared secret Z |
| `param_3` | `u32` | length of Z |
| `param_4` | `ptr` | SharedInfo, may be NULL |
| `param_5` | `u32` | length of SharedInfo |
| `param_6` | `ptr` | output buffer |
| `param_7` | `u32` | requested output length |

**Returns** `s32`: 0 on success; -173 for NULL pointers or zero lengths, -232 for a hash type that is not built in, -125 on allocation failure

- Addresses by version: 219: 0x0C060BE8
- Called by: `ble_ecc_p224_export_derive`, `ble_crypto_kdf_update`, `ble_crypto_kdf_connect`, `ble_crypto_diversify`, `ble_crypto_server_secret`, `ble_crypto_session_decrypt`, `ble_crypto_serial_mac`, `ble_crypto_ecdh_seal_p256`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `wc_HashGetDigestSize`, `wc_HashInit`, `wc_HashUpdate`, `wc_HashFinal`, `wc_HashFree`, `memcpy`
- Confidence: high

## wc_ecc_check_key

**Validate an ECC key: coordinates in range, point on curve, point order, and private scalar range**

wolfSSL-style wc_ecc_check_key. It loads the key's curve (key->dp at +0x10) with wc_ecc_curve_load and mask 0x0b (prime, A, order) into a 0x138-byte pool of three fp_ints, and reads the curve constant b from the ecc_set_type hex string at dp+0x14 into a temporary with fp_read_radix (radix 16). If both x and y have zero digits it returns -215 (point at infinity). If x or y is not less than p it returns -217. Otherwise ble_219_0c060828 (on-curve test with b) must return 0, and the point-order check ble_219_0c05f830 (not yet described) is run with (key, x, A, p, n). For a private key (key->type == 2) the scalar k at +0x150 must be non-zero, non-negative and less than the order n, else -216, and ble_219_0c05ff44 (not yet described) checks the public point against k. The curve spec is released with wc_ecc_curve_free and both temporaries with fp_clear.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ecc_key: type +0, dp +0x10, pubkey x/y/z at +0x18/+0x80/+0xe8, private scalar k at +0x150 |

**Returns** `s32`: 0 when the key is valid; -215, -216, -217 or the failing check's code otherwise; -173 for NULL

**Notes:** The final order and private-key checks are delegated to ble_219_0c05f830 and ble_219_0c05ff44, which are not yet named; their roles are guessed from the wolfSSL structure. The curve-spec field offsets follow wc_ecc_curve_free.

- Addresses by version: 219: 0x0C060974
- Called by: `ble_ecc_share_derive`, `ble_crypto_diversify`, `ble_crypto_ecdsa_p256_verify`, `ble_crypto_ecdh_seal_p256`, `wc_ecc_import_x963_ex`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `wc_ecc_curve_free`, `wc_ecc_curve_load`, `ecc_check_pubkey_order`, `ecc_check_privkey_gen`, `ecc_point_on_curve_check`, `mp_init`, `fp_clear`, `mp_cmp`, `mp_iszero`, `fp_read_radix`, `get_digit_count`, `memset`
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
- Called by: `ecc_mulmod_ladder_ct`
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
- Called by: `wc_ecc_curve_load`, `ecc_shared_secret`, `ecc_make_pub_ex`, `ecc_check_privkey_gen`, `wc_ecc_make_key_ex`, `ecc_verify_hash_ex`, `wc_ecc_check_key`
- Calls: `fp_clear`
- Confidence: high

## wc_ecc_curve_load

**Load selected fields of a standard ECC curve into an ecc_curve_spec**

wolfSSL wc_ecc_curve_load. A NULL curve returns BAD_FUNC_ARG (-173). The spec stores the new curve pointer at +0x00, and if the same curve was already loaded it keeps the fields already present. For each requested field bit in load_mask it takes the next fp_int slot from the pool (slot size 0x68, pool base at +0x18, count at +0x1C, used count at +0x20), runs mp_init on it and parses the curve's hex constant with fp_read_radix(..., 16). The loaded-field mask is stored at +0x24. When the pool is exhausted it returns -170 or -340. Other failures free the spec with wc_ecc_curve_free (0x0C05E4E8) and return -111.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | static curve parameter table (ecc_set_type) |
| `param_2` | `ptr` | out pointer to the ecc_curve_spec |
| `param_3` | `u32` | load_mask, one bit per curve field (prime, A, B, order, Gx, Gy) |

**Returns** `s32`: 0 on success, -173 for a NULL curve, -170 or -340 on pool exhaustion, -111 on load failure

**Notes:** The bit-to-field mapping is inferred from the slot assignments. Bit 2 is not tested by the decompiled branches, so one field may be loaded through a path not seen here.

- Addresses by version: 219: 0x0C05E614
- Called by: `ecc_shared_secret`, `ecc_make_pub_ex`, `ecc_check_privkey_gen`, `wc_ecc_make_key_ex`, `ecc_verify_hash_ex`, `wc_ecc_check_key`
- Calls: `wc_ecc_curve_free`, `mp_init`, `fp_read_radix`
- Confidence: medium

## wc_ecc_del_point

**Zero the three coordinates of an ecc_point and free it (wc_ecc_del_point)**

If the pointer is not NULL, it zeroes the x, y and z fp_ints (offsets 0, 0x68 and 0xD0) with fp_clear (0x0C063FEC) and then frees the block through ble_ecc_heap_free. NULL is ignored. The explicit zeroing matters because mp_clear is empty in this build, so the secret-bearing digits would otherwise survive the free.

| Parameter | Type | Description |
|---|---|---|
| `p` | `ptr` | ecc_point to release, may be NULL |

- Addresses by version: 219: 0x0C05F1B0
- Called by: `ble_fmna_reset_gen_keypair`, `ble_ecc_ctx_release`, `ble_crypto_diversify`
- Calls: `ble_ecc_heap_free`, `fp_clear`
- Confidence: high

## wc_ecc_free

**Release an ecc_key: clear pubkey.x/y/z and force-zero the private scalar k (wolfSSL)**

wolfSSL wc_ecc_free(key). For a non-NULL key it calls the mp_clear routine at 0x0c063fec on pubkey.x (+0x18), pubkey.y (+0x80) and pubkey.z (+0xe8) and then mp_forcezero on the private scalar k at +0x150 so the secret is wiped. Always returns 0 (also for NULL). Counterpart of wc_ecc_init; same six ble_crypto callers plus 0c05ba4c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ecc_key (may be NULL) |

**Returns** `s32`: always 0

- Addresses by version: 219: 0x0C0601D0
- Called by: `ble_fmna_reset_gen_keypair`, `ble_ecc_ctx_release`, `ble_ecc_share_derive`, `ble_crypto_diversify`, `ble_crypto_ecdsa_p256_verify`, `ble_crypto_ecdh_seal_p256`
- Calls: `mp_forcezero`, `fp_clear`
- Confidence: high

## wc_ecc_gen_k

**Draw a random ECC scalar: size+8 RNG bytes read as an integer and reduced modulo the order**

wolfSSL wc_ecc_gen_k(rng, size, k, order). Fills a stack buffer with size+8 random bytes from the RNG routine at 0x0C061834 (not yet described), reads them into k with fp_read_unsigned_bin (0x0C062BAC), and when k >= order reduces it modulo order with 0x0C0634C4. A zero result returns RNG_FAILURE_E (-0x79). The stack buffer is zeroed over its full 80 bytes before returning on every path. The 8 extra bytes keep the bias from the modular reduction small. Used by wc_ecc_make_key_ex and ecc_randomize_projective.

| Parameter | Type | Description |
|---|---|---|
| `rng` | `ptr` | RNG state |
| `size` | `s32` | key size in bytes |
| `k` | `ptr` | output fp_int scalar |
| `order` | `ptr` | curve order fp_int |

**Returns** `s32`: 0, the RNG routine's error code, or -0x79 (RNG_FAILURE_E) when k is zero

- Addresses by version: 219: 0x0C05F218
- Called by: `ecc_randomize_projective`, `wc_ecc_make_key_ex`
- Calls: `wc_RNG_GenerateBlock`, `fp_mod_thunk`, `mp_cmp`, `mp_read_unsigned_bin`, `mp_iszero`
- Confidence: medium

## wc_ecc_import_x963_ex

**Import an ECC public key from an X9.63 uncompressed point (0x04 || X || Y) and validate it**

wolfSSL wc_ecc_import_x963_ex. The input length must be odd (1 + 2 * coordinate size) or -170 is returned. The first byte selects the format: 0x04 is uncompressed, 0x02 and 0x03 (compressed) return -174 because they are not compiled in, anything else returns -140. The coordinate size is (len - 1) / 2. The key is initialised with mp_init_multi on x (+0x18), y (+0x80), z (+0xe8) and the scalar k (+0x150), wc_ecc_set_curve picks the curve from that size and the curve id, key->type (+0) is set to 1 (public key), X and Y are read big-endian with fp_read_unsigned_bin, z is set to 1 with mp_set, and wc_ecc_check_key (0c060974) validates the result. On any failure x, y, z and k are cleared with fp_clear and the error is returned.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | input octet string |
| `param_2` | `u32` | input length in bytes |
| `param_3` | `ptr` | ecc_key to fill |
| `param_4` | `s32` | curve id, or 0 to select by size |

**Returns** `s32`: 0 on success; -173 for NULL, -170 for an odd length, -174 for a compressed point, -140 for an unknown format byte, -125 on allocation failure, or the error from wc_ecc_check_key

- Addresses by version: 219: 0x0C060AE4
- Called by: `ble_ecc_share_derive`, `ble_crypto_diversify`, `ble_crypto_ecdsa_p256_verify`, `ble_crypto_ecdh_seal_p256`
- Calls: `wc_ecc_set_curve`, `wc_ecc_check_key`, `fp_clear`, `mp_init_multi`, `mp_read_unsigned_bin`, `mp_set`
- Confidence: high

## wc_ecc_init

**Zero a 0x1bc-byte ecc_key and init its pubkey.x/y/z and private scalar k (wolfSSL wc_ecc_init)**

wolfSSL wc_ecc_init(key) (wc_ecc_init_ex with heap = NULL inlined). Returns BAD_FUNC_ARG (-173 = 0xffffff53) for NULL. memset(key, 0, 0x1bc) then mp_init_multi (routine at 0x0c064004) on &key->k (+0x150), key->pubkey.x (+0x18), .y (+0x80), .z (+0xe8), NULL, NULL; a failure returns MEMORY_E (-125 = 0xffffff83). On success key->heap (+0x14) = NULL and 0 is returned. Layout implied: type +0, idx +4, state +8, flags +0xc, dp +0x10, heap +0x14, pubkey +0x18 (3 x 0x68), k +0x150, rng +0x1b8. Called by the ble_crypto ECDH/ECDSA wrappers (0c0537b4, 0c05baf0, 0c05bd30, 0c05bfa4, 0c05c13c), always paired with wc_ecc_free.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ecc_key to initialise (0x1bc bytes) |

**Returns** `s32`: 0, BAD_FUNC_ARG (-173) or MEMORY_E (-125)

- Addresses by version: 219: 0x0C060190
- Called by: `ble_fmna_reset_gen_keypair`, `ble_ecc_share_derive`, `ble_crypto_diversify`, `ble_crypto_ecdsa_p256_verify`, `ble_crypto_ecdh_seal_p256`
- Calls: `mp_init_multi`, `memset`
- Confidence: high

## wc_ecc_make_key_ex

**Generate an ECC key pair: select the curve, draw k, derive the public point (wc_ecc_make_key_ex)**

wolfSSL wc_ecc_make_key_ex(rng, keysize, key, curve_id). Sets the key state at +8 to 0, selects the curve by keysize or curve id with wc_ecc_set_curve, initialises the private scalar at key+0x150 with mp_init, and loads a 0x208-byte curve context (mask 0x3B). It draws k with wc_ecc_gen_k over the order and calls ecc_make_pub_ex to derive the public point. On success the key type is set to ECC_PRIVATEKEY (2); on failure the scalar is force-zeroed with mp_forcezero. A NULL rng or key returns BAD_FUNC_ARG (-0xAD) and an allocation failure returns MEMORY_E (-0x7D).

| Parameter | Type | Description |
|---|---|---|
| `rng` | `ptr` | RNG state |
| `keysize` | `s32` | key size in bytes, used when curve_id is not set |
| `key` | `ptr` | ecc_key to fill (0x1bc bytes) |
| `curve_id` | `s32` | ecc_curve_id, or 0 to choose by keysize |

**Returns** `s32`: 0, -0xAD (BAD_FUNC_ARG), -0x7D (MEMORY_E), or the error from curve selection or key generation

- Addresses by version: 219: 0x0C0600C0
- Called by: `ble_fmna_reset_gen_keypair`, `ble_crypto_ecdh_seal_p256`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `wc_ecc_curve_free`, `wc_ecc_curve_load`, `wc_ecc_set_curve`, `wc_ecc_gen_k`, `ecc_make_pub_ex`, `mp_init`, `mp_forcezero`, `memset`
- Confidence: high

## wc_ecc_new_point

**Allocate a new ecc_point with no heap hint (wc_ecc_new_point)**

Calls wc_ecc_new_point_h (0x0C05F164) with a NULL heap hint and returns its result. The result is the new zeroed point, or NULL when the allocation or initialisation fails. It is the usual constructor used by the ECC routines in this packet.

**Returns** `ptr`: new point, or NULL

- Addresses by version: 219: 0x0C05F1A8
- Called by: `ble_fmna_reset_gen_keypair`, `ble_crypto_diversify`
- Calls: `wc_ecc_new_point_h`
- Confidence: high

## wc_ecc_new_point_h

**Allocate and zero an ecc_point (0x138 bytes) and initialise its three fp_ints**

wolfSSL wc_ecc_new_point_h(heap). Allocates 0x138 bytes with ble_ecc_heap_alloc, zeroes them with memset, and calls mp_init_multi on x (+0), y (+0x68) and z (+0xD0). If the initialisation fails the block is released and NULL is returned. The heap argument is accepted but not used, because the BLE pool handle is fixed at DAT_200049A8.

| Parameter | Type | Description |
|---|---|---|
| `heap` | `ptr` | heap hint, ignored |

**Returns** `ptr`: new point, or NULL on allocation or init failure

- Addresses by version: 219: 0x0C05F164
- Called by: `wc_ecc_new_point`, `ecc_mulmod_ex`, `ecc_check_pubkey_order`, `ecc_mulmod_ex2`, `ecc_shared_secret`, `ecc_make_pub_ex`, `ecc_check_privkey_gen`, `ecc_verify_hash_ex`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `mp_init_multi`, `memset`
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
- Called by: `wc_ecc_make_key_ex`, `wc_ecc_import_x963_ex`
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
- Called by: `ble_crypto_ecdh_seal_p256`
- Confidence: high

## wc_ecc_shared_secret

**wc_ecc_shared_secret state machine: validate keys, run the ECDH core, retry on pending**

wolfSSL-style wc_ecc_shared_secret wrapper with a non-blocking state machine. It requires non-NULL out and outlen (BAD_FUNC_ARG -0xAD), a private key type of 2 or 3, and matching curve identity (dp id) between the two keys, otherwise it returns -0xAA. The state word at key+8 selects the step: state 0 or 1 runs ecc_shared_secret with the state set to 1; a WC_PENDING (-0x6C) result leaves the state at 2 so the call can be repeated; state 2 on entry returns 0; any other state returns BAD_STATE_E (-0xC0). Other results reset the state to 0.

| Parameter | Type | Description |
|---|---|---|
| `private_key` | `ptr` | private ecc_key, state word at +8 |
| `public_key` | `ptr` | peer ecc_key |
| `out` | `ptr` | output buffer |
| `outlen` | `ptr` | in/out byte count (u32) |

**Returns** `s32`: 0, -0x6C (WC_PENDING, retry), or an error code (-0xAD, -0xAA, -0xC0, or from ecc_shared_secret)

**Notes:** The exact key-validation conditions were read from the decompiled comparisons and are not fully named.

- Addresses by version: 219: 0x0C05FCCC
- Called by: `ble_crypto_ecdh_seal_p256`
- Calls: `ecc_shared_secret`
- Confidence: medium

## wc_ecc_verify_hash

**wc_ecc_verify_hash state machine: decode the DER signature, then verify**

wolfSSL wc_ecc_verify_hash(sig, siglen, hash, hashlen, res, key) with a state machine in key+8. It rejects NULL sig, hash, res or key (ECC_BAD_ARG_E -0xAA) and allocates two temporary mp_ints for r and s. State 0 or 5 sets the state to 5, clears *res and decodes the DER ECDSA signature into r and s with DecodeECC_DSA_Sig (0x0C05E474); state 6 runs ecc_verify_hash_ex (0x0C0601FC) on r, s, hash, res and key; state 7 returns 0 at once. A WC_PENDING (-0x6C) from a step advances the state so the call can be repeated. A completed run resets the state to 0 and returns 0 with the verdict in *res. Any other state returns BAD_STATE_E (-0xC0).

| Parameter | Type | Description |
|---|---|---|
| `sig` | `ptr` | DER-encoded ECDSA signature |
| `siglen` | `u32` | signature length in bytes |
| `hash` | `ptr` | message digest |
| `hashlen` | `u32` | digest length in bytes |
| `res` | `ptr` | output verdict, 1 = valid, 0 = invalid (s32) |
| `key` | `ptr` | ecc_key, state word at +8 |

**Returns** `s32`: 0 when the check completed (verdict in *res), -0x6C (WC_PENDING), or an error code

- Addresses by version: 219: 0x0C060720
- Called by: `ble_crypto_ecdsa_p256_verify`
- Calls: `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `DecodeECC_DSA_Sig`, `ecc_verify_hash_ex`, `fp_clear`, `memset`
- Confidence: high

## wc_rng_seed_instantiate

**Init an RNG: DRBG known-answer checks, TRNG entropy with a continuous test, then instantiate**

Initialises an RNG object (param 1) in four steps. It stores param 4 at +0x04 and clears the DRBG pointer at +0x08 and the status byte at +0x0c. It runs two known-answer checks with hash_drbg_kat_generate. Each 128-byte result is compared with a flash-resident expected vector using an OR-accumulated XOR. A mismatch sets status 3 and returns -209. Entropy is then read from ble_219_0c04585c (not yet described): 52 bytes, or 36 bytes when a nonce is supplied. The four leading bytes are checked and the whole buffer goes through the continuous test wc_RNG_TestSeed. A 0x78-byte DRBG is allocated and instantiated from the remaining bytes (entropy plus nonce, param 2 and 3). Status values in the RNG object are 1 for ready, 2 for an entropy or instantiate failure (returns -199) and 3 for a self-test or continuous-test failure (returns -209).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | RNG object (status +0x0c, DRBG pointer +0x08, heap +0x04) |
| `param_2` | `ptr` | nonce, may be NULL |
| `param_3` | `u32` | nonce length; must be 0 when param 2 is NULL |
| `param_4` | `u32` | value stored at +0x04 (heap or devId in wolfSSL terms) |

**Returns** `s32`: 0 when the RNG is ready; -199 on an entropy or instantiate failure; -209 on a self-test or continuous-test failure; -173 for bad arguments; -125 on allocation failure

**Notes:** Which argument goes to which wolfSSL field is inferred. The signature matches neither wc_InitRng_ex nor a plain nonce API, so the name is descriptive rather than a library name.

- Addresses by version: 219: 0x0C061688
- Called by: `wc_InitRng`
- Calls: `ble_chunked_write_24`, `ble_ecc_heap_free`, `ble_ecc_heap_alloc`, `Hash_DRBG_Instantiate`, `wc_RNG_TestSeed`, `hash_drbg_kat_generate`
- Confidence: medium
