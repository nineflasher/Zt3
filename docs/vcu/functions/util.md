# VCU - `util` functions

14 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`soft_timer_poll`](#soft_timer_poll) | 0x0800858C | Service the 5 software timers: fire callbacks whose period has elapsed |
| [`soft_timer_start`](#soft_timer_start) | 0x080085D0 | Configure and arm software timer slot idx with period, one-shot flag and callback |
| [`util_hex_char_to_nibble`](#util_hex_char_to_nibble) | 0x08001B14 | Convert an ASCII hex digit to its value 0..15, 0 for invalid characters |
| [`util_interp_linear_clamp_hi`](#util_interp_linear_clamp_hi) | 0x08001B46 | Linear interpolation between (x0,yB) and (x1,yA), clamped to yA above x1 |
| [`util_load_u32_le`](#util_load_u32_le) | 0x0800DA38 | Read a little-endian 32-bit value from a possibly unaligned byte buffer |
| [`util_map_range_clamp_high`](#util_map_range_clamp_high) | 0x0800F050 | Linear interpolation of x from [in_min,in_max] to [out_min,out_max], clamped at the top |
| [`util_mem_equal`](#util_mem_equal) | 0x080085F0 | Compare two byte buffers of length n, return 1 if equal, 0 if different |
| [`util_store_u32_le`](#util_store_u32_le) | 0x0800DC54 | Write a 32-bit value to four bytes in little-endian order |
| [`vcu_buf_zero`](#vcu_buf_zero) | 0x08001240 | Zero-fill a byte buffer by calling the memset helper with value 0 |
| [`vcu_copy_bytes_src_dst`](#vcu_copy_bytes_src_dst) | 0x08005B7E | Byte-wise copy of param_3 bytes from param_1 to param_2 |
| [`vcu_count_nonzero_nibbles`](#vcu_count_nonzero_nibbles) | 0x08006814 | Count how many of the 8 nibbles of a u32 are nonzero |
| [`vcu_digits4_to_int`](#vcu_digits4_to_int) | 0x08006B00 | Convert four decimal-digit bytes (d0 d1 d2 d3) to a 4-digit integer |
| [`vcu_record_queues_init`](#vcu_record_queues_init) | 0x08007C20 | Reset both 32-entry record queues and zero their 20-byte slots |
| [`vcu_sum_s16_minus_trailer`](#vcu_sum_s16_minus_trailer) | 0x08005914 | Sum an array of s16 and subtract the two s16 words at index 250 and 251 |

## soft_timer_poll

**Service the 5 software timers: fire callbacks whose period has elapsed**

Iterates 5 slots of a 16-byte timer table at 0x20002054 (+0 period u32, +4 last-fire timestamp u32, +8 one-shot flag u8, +9 enabled u8, +12 callback pointer). For every enabled slot, when (tick - last) >= period (tick = DAT_20001350, the millisecond system counter) the slot is re-armed by copying tick into last (periodic, flag==0) or disabled (one-shot, flag!=0), then the callback is invoked if non-NULL. Called from the main loop dispatcher 0x0800d858; slots are configured by soft_timer_start.

**Notes:** Tick unit assumed to be 1 ms; the one-shot/periodic polarity of the +8 byte follows from the code.

- Addresses by version: 148: 0x08007B98, 14a: 0x08007FD4, 14b: 0x0800832C, 14e: 0x0800836C, 14f: 0x080083C8, 152: 0x0800848C, 153: 0x08008528, 0159: 0x0800858C
- Called by: `vcu_0159_0800d858`
- Confidence: medium

## soft_timer_start

**Configure and arm software timer slot idx with period, one-shot flag and callback**

Writes slot param_1 of the 16-byte timer table at 0x20002054: clears enabled byte (+9), zeroes the last-fire timestamp (+4), stores callback param_4 (+12), one-shot flag param_3 (+8) and period param_2 (+0), then sets enabled=1. Because the timestamp starts at 0, the first expiry is relative to tick 0, so the callback may fire immediately if the tick counter is already larger than the period. Pair with soft_timer_poll; no bounds check on the index (0..4 valid). Called from 0x0800d858.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | slot index 0..4 |
| `param_2` | `u32` | period in ticks (ms) |
| `param_3` | `u8` | 0 = periodic, non-zero = one-shot |
| `param_4` | `ptr` | callback function pointer, may be NULL |

**Notes:** Tick unit assumed ms.

- Addresses by version: 148: 0x08007BDC, 14a: 0x08008018, 14b: 0x08008370, 14e: 0x080083B0, 14f: 0x0800840C, 152: 0x080084D0, 153: 0x0800856C, 0159: 0x080085D0
- Called by: `vcu_0159_0800d858`
- Confidence: medium

## util_hex_char_to_nibble

**Convert an ASCII hex digit to its value 0..15, 0 for invalid characters**

Accepts '0'-'9', 'A'-'F' and 'a'-'f'. Digits subtract 0x30, upper-case letters subtract 0x37, lower-case letters subtract 0x57, result masked to 8 bits. Any other character returns 0 (no error indication). Called from vcu_0159_08006d6c, which presumably parses hex text (e.g. an ASCII command or ID string).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | ASCII character |

**Returns** `u32`: nibble value 0..15, 0 if not a hex digit

- Addresses by version: 148: 0x08001730, 14a: 0x080017A4, 14b: 0x08001A4C, 14e: 0x08001A4C, 14f: 0x08001AA8, 152: 0x08001AE4, 153: 0x08001B00, 0159: 0x08001B14
- Called by: `vcu_rx_frame_dispatch`
- Confidence: high

## util_interp_linear_clamp_hi

**Linear interpolation between (x0,yB) and (x1,yA), clamped to yA above x1**

With x=param_1, x0=param_2, x1=param_3, yA=param_4, yB=param_5: if x > x1 returns yA; otherwise returns yB - (yB - yA)*(x - x0)/(x1 - x0) using signed integer arithmetic (division truncates toward zero). So the output goes from yB at x0 to yA at x1 along a straight line, with no clamp below x0 (extrapolates). No guard against x1 == x0, which would divide by zero when x == x1. Single caller vcu_0159_08009240, a numeric sensor/mapping routine that also uses the soft-float helpers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | x input |
| `param_2` | `s32` | x0 start of ramp |
| `param_3` | `s32` | x1 end of ramp |
| `param_4` | `s32` | yA output at and above x1 |
| `param_5` | `s32` | yB output at x0 |

**Returns** `s32`: interpolated value

- Addresses by version: 148: 0x08001762, 14a: 0x080017D6, 14b: 0x08001A7E, 14e: 0x08001A7E, 14f: 0x08001ADA, 152: 0x08001B16, 153: 0x08001B32, 0159: 0x08001B46
- Called by: `vcu_drive_command_update`
- Confidence: high

## util_load_u32_le

**Read a little-endian 32-bit value from a possibly unaligned byte buffer**

Assembles four bytes at the given address into a u32 in little-endian order, using byte loads so there is no alignment requirement. The result is b0 | b1<<8 | b2<<16 | b3<<24. It is the read counterpart of util_store_u32_le (vcu_0159_0800dc54) and is a generic helper for multi-byte fields.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pointer to 4 bytes, little-endian |

**Returns** `u32`: the 32-bit value

- Addresses by version: 0159: 0x0800DA38
- Called by: `vcu_xtea_key_load`, `vcu_xtea_decrypt_inplace`
- Confidence: high

## util_map_range_clamp_high

**Linear interpolation of x from [in_min,in_max] to [out_min,out_max], clamped at the top**

Integer version of the Arduino map() function. If x (param_1) is greater than in_max (param_3) it returns out_max (param_5); otherwise returns (out_max - out_min) * (x - in_min) / (in_max - in_min) + out_min using signed 32-bit division. There is no lower clamp, so x < in_min extrapolates below out_min, and in_max == in_min with x <= in_max would divide by zero. Used from several callers (vcu_0159_08009240, 0800b0c4, 0800e60c), probably to scale sensor/throttle or speed values; the exact use is not determined here.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | x, the input value |
| `param_2` | `s32` | in_min |
| `param_3` | `s32` | in_max (upper clamp) |
| `param_4` | `s32` | out_min |
| `param_5` | `s32` | out_max |

**Returns** `s32`: scaled value

- Addresses by version: 148: 0x0800E02C, 14a: 0x0800E4C8, 14b: 0x0800E958, 14e: 0x0800E9F8, 14f: 0x0800EB44, 152: 0x0800EDEC, 153: 0x0800EEE0, 0159: 0x0800F050
- Called by: `vcu_drive_command_update`, `vcu_0159_0800b0c4`, `lighting_brightness_percent_set`
- Confidence: high

## util_mem_equal

**Compare two byte buffers of length n, return 1 if equal, 0 if different**

Byte-by-byte compare loop with an 8-bit index (so n is effectively limited to 255); returns 1 when all n bytes match (also when n == 0) and 0 on the first mismatch. Note the inverted sense compared with memcmp. Called from 0x080060b8 and 0x08006538, apparently to compare ID/key/header strings.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | buffer A |
| `param_2` | `ptr` | buffer B |
| `param_3` | `u32` | number of bytes, <= 255 |

**Returns** `u32`: 1 = equal, 0 = different

- Addresses by version: 148: 0x08007BFC, 14a: 0x08008038, 14b: 0x08008390, 14e: 0x080083D0, 14f: 0x0800842C, 152: 0x080084F0, 153: 0x0800858C, 0159: 0x080085F0
- Called by: `vcu_0159_080060b8`, `vcu_crypto_key_load`
- Confidence: high

## util_store_u32_le

**Write a 32-bit value to four bytes in little-endian order**

Stores the low byte first, then bytes 1..3 of the value, into the four bytes at the destination. It has no alignment requirement and is the write counterpart of util_load_u32_le (vcu_0159_0800da38). It is used to fill multi-byte fields of outgoing frames.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value to store |
| `param_2` | `ptr` | destination, 4 bytes |

- Addresses by version: 0159: 0x0800DC54
- Called by: `vcu_xtea_decrypt_inplace`
- Confidence: high

## vcu_buf_zero

**Zero-fill a byte buffer by calling the memset helper with value 0**

Clears param_2 bytes starting at param_1 by calling the ARM EABI helper __aeabi_memset (dest, count, value) with value 0. vcu_0159_08001768 uses it to clear its five 32-bit ADC accumulators (20 bytes). There is no bounds check, so the caller must supply at least param_2 bytes.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination buffer |
| `param_2` | `u32` | number of bytes to clear |

- Addresses by version: 148: 0x08001240, 14a: 0x08001240, 14b: 0x08001240, 14e: 0x08001240, 14f: 0x08001240, 152: 0x08001240, 153: 0x08001240, 0159: 0x08001240
- Called by: `vcu_adc_average_16_scans`, `vcu_0159_08001bca`, `vcu_0159_0800261c`, `vcu_0159_080047ac`, `vcu_0159_080057ac`, `vcu_record_queues_init`, `vcu_0159_08009da8`, `vcu_0159_0800ef14`
- Calls: `__aeabi_memset`
- Confidence: high

## vcu_copy_bytes_src_dst

**Byte-wise copy of param_3 bytes from param_1 to param_2**

Simple forward byte loop copying from src (param_1) to dst (param_2). Note the argument order is source first, unlike memcpy. No overlap handling. Called from vcu_0159_08005bb4, 080060b8 and 08009da8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source |
| `param_2` | `ptr` | destination |
| `param_3` | `u32` | number of bytes |

- Addresses by version: 148: 0x0800517E, 14a: 0x0800556A, 14b: 0x08005892, 14e: 0x080058CA, 14f: 0x08005926, 152: 0x0800597E, 153: 0x08005A1A, 0159: 0x08005B7E
- Called by: `vcu_0159_08005bb4`, `vcu_0159_080060b8`, `vcu_0159_08009da8`
- Confidence: high

## vcu_count_nonzero_nibbles

**Count how many of the 8 nibbles of a u32 are nonzero**

Iterates over the 8 hexadecimal digits of param_1 (shift right by 4 each time) and increments a counter for each nibble not equal to 0. Returns the count (0..8). Called from vcu_0159_08007a48.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value whose nibbles are tested |

**Returns** `u8`: number of nonzero nibbles, 0..8

- Addresses by version: 148: 0x08005DE8, 14a: 0x08006208, 14b: 0x08006578, 14e: 0x080065B0, 14f: 0x0800660C, 152: 0x0800668C, 153: 0x08006728, 0159: 0x08006814
- Called by: `vcu_nibble_count_snapshot`
- Confidence: high

## vcu_digits4_to_int

**Convert four decimal-digit bytes (d0 d1 d2 d3) to a 4-digit integer**

Computes ((d0*10 + d1)*10 + d2)*10 + d3 from param_1[0..3], with no subtraction of '0', so the bytes are raw digit values 0..9 (not ASCII), and returns the result sign-extended from 16 bits. Called from vcu_0159_080069b4.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pointer to 4 digit bytes, most significant first |

**Returns** `s32`: value 0..9999

- Addresses by version: 148: 0x08006094, 14a: 0x080064B4, 14b: 0x08006824, 14e: 0x0800685C, 14f: 0x080068B8, 152: 0x0800695C, 153: 0x080069F8, 0159: 0x08006B00
- Called by: `vcu_0159_080069b4`
- Confidence: high

## vcu_record_queues_init

**Reset both 32-entry record queues and zero their 20-byte slots**

Sets the receive ring 0 head and tail (DAT_20002c2c and DAT_20002c30) and the CAN transmit queue read and write indices (DAT_200029a8 and DAT_200029a4) to zero, then zero-fills all 32 slots of 20 bytes at 0x20002C34 (ring 0) and at 0x200029AC (CAN transmit queue) with the zero-fill helper vcu_0159_08001240.

**Notes:** Zero-fill helper vcu_0159_08001240 is not yet described.

- Addresses by version: 148: 0x080071F4, 14a: 0x08007630, 14b: 0x08007994, 14e: 0x080079CC, 14f: 0x08007A28, 152: 0x08007AEC, 153: 0x08007B88, 0159: 0x08007C20
- Called by: `vcu_0159_0800d858`
- Calls: `vcu_buf_zero`
- Confidence: high

## vcu_sum_s16_minus_trailer

**Sum an array of s16 and subtract the two s16 words at index 250 and 251**

Adds up the first param_2 signed 16-bit values of the array at param_1 and returns that sum minus the s16 at byte offset 500 (index 250) and minus the s16 at byte offset 0x1F6 (index 251). It looks like a block integrity check: a 512-byte block of 16-bit words whose last words hold stored check values, the return being 0 when valid. Callers vcu_0159_08005bb4 and vcu_0159_08007d88, which also use vcu_flash_page_count and vcu_copy_bytes_src_dst, so this belongs to the stored-parameter/firmware-image handling code.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | array of s16 words |
| `param_2` | `s32` | number of words to sum |

**Returns** `s32`: sum minus trailer words; 0 expected when consistent

**Notes:** Whether param_2 includes the two trailer words (e.g. 250 vs 252) is decided by callers; purpose is inferred.

- Addresses by version: 148: 0x08004F96, 14a: 0x08005386, 14b: 0x080056AE, 14e: 0x080056E6, 14f: 0x08005742, 152: 0x08005798, 153: 0x080057B0, 0159: 0x08005914
- Called by: `vcu_0159_08005bb4`, `vcu_0159_08007d88`
- Confidence: medium
