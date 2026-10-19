# VCU - `libc` functions

18 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`__ARM_scalbnf`](#__arm_scalbnf) | 0x080012BA | Soft-float scale: add an integer to the exponent of a float (ldexpf style) |
| [`__aeabi_d2iz`](#__aeabi_d2iz) | 0x08001348 | Soft-float convert double to signed 32-bit integer, truncating toward zero |
| [`__aeabi_dadd`](#__aeabi_dadd) | 0x08001450 | Soft-float double-precision add or subtract with exponent alignment and rounding |
| [`__aeabi_f2d`](#__aeabi_f2d) | 0x08001386 | Soft-float widen single-precision float to double-precision (r0:r1 pair) |
| [`__aeabi_f2iz`](#__aeabi_f2iz) | 0x080012EE | Soft-float convert single-precision float to signed int, truncating toward zero |
| [`__aeabi_f2uiz`](#__aeabi_f2uiz) | 0x08001320 | Soft-float convert float magnitude to unsigned int, truncating |
| [`__aeabi_fmul`](#__aeabi_fmul) | 0x08001256 | Soft-float IEEE-754 single precision multiply (no FPU) |
| [`__aeabi_i2f`](#__aeabi_i2f) | (removed) | Soft-float convert signed 32-bit integer to single-precision float (VCU_14a build) |
| [`__aeabi_i2f_v148_159`](#__aeabi_i2f_v148_159) | 0x080012D2 | Soft-float convert signed 32-bit integer to IEEE-754 single, round to nearest even |
| [`__aeabi_lasr`](#__aeabi_lasr) | 0x0800159E | 64-bit arithmetic shift right (lo, hi, shift) |
| [`__aeabi_llsl`](#__aeabi_llsl) | 0x080013AC | 64-bit logical shift left (lo, hi, shift) |
| [`__aeabi_llsr`](#__aeabi_llsr) | 0x080013CA | 64-bit logical shift right (lo, hi, shift) |
| [`__aeabi_memcpy`](#__aeabi_memcpy) | 0x0800120E | Forward memory copy: word-wise if both pointers 4-byte aligned, else bytewise |
| [`__aeabi_memset`](#__aeabi_memset) | 0x08001232 | Fill a byte buffer with a constant value (dest, count, value argument order) |
| [`__aeabi_ui2f`](#__aeabi_ui2f) | 0x080012E4 | Soft-float convert unsigned 32-bit integer to single-precision float |
| [`fp64_round_pack`](#fp64_round_pack) | 0x0800164E | Soft-float double normalise, round to nearest even and pack for the add routine |
| [`memset`](#memset) | 0x08001244 | C library memset: fill n bytes at dst with c and return dst |
| [`vcu_udiv64_shift_subtract`](#vcu_udiv64_shift_subtract) | 0x080011AC | 64-bit unsigned divide returning the quotient by 64-step shift and subtract |

## __ARM_scalbnf

**Soft-float scale: add an integer to the exponent of a float (ldexpf style)**

If the magnitude of param_1 is non-zero, checks that the biased exponent plus param_2 stays positive (-exp < n) and returns param_1 + (param_2 << 23), i.e. multiplies by 2^param_2 by adjusting the exponent field directly. Otherwise (result would underflow) returns 0; zero input is returned unchanged. No overflow or NaN/Inf checking. Called from vcu_0159_08009240 together with the other soft-float helpers. Different function from the VCU_14a function at the same address (which is int-to-float).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | float bits |
| `param_2` | `s32` | power-of-two exponent adjustment |

**Returns** `u32`: param_1 * 2^param_2 as float bits

**Notes:** Name is a best guess among ARM library helpers (scalbnf/ldexpf); behaviour is certain.

- Addresses by version: 14b: 0x080012BA, 14e: 0x080012BA, 14f: 0x080012BA, 152: 0x080012BA, 153: 0x080012BA, 0159: 0x080012BA
- Called by: `vcu_drive_command_update`
- Confidence: medium

## __aeabi_d2iz

**Soft-float convert double to signed 32-bit integer, truncating toward zero**

Converts an IEEE-754 double (low word param_1, high word param_2) to int32 with truncation toward zero. The biased exponent is bits 30:20 of the high word. Exponents below 0x3FF (|x| < 1) give 0. For 0x3FF <= e < 0x434 the 53-bit mantissa (implicit one at bit 20 of the high word) is shifted right by 0x433 - e to get the integer part. For e >= 0x434 the low mantissa word is shifted left by e - 0x433 with no saturation. A set sign bit negates the result. There is no NaN or overflow handling.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | double low word |
| `param_2` | `u32` | double high word |

**Returns** `s32`: truncated integer

- Addresses by version: 14b: 0x08001316, 14e: 0x08001316, 14f: 0x08001316, 152: 0x08001348, 153: 0x08001348, 0159: 0x08001348
- Called by: `vcu_speed_mode_snapshot_update`
- Calls: `__aeabi_llsr`
- Confidence: high

## __aeabi_dadd

**Soft-float double-precision add or subtract with exponent alignment and rounding**

Soft-float IEEE-754 double addition (__aeabi_dadd). Subtraction uses the same routine with one operand's sign flipped. The operands are (low, high) word pairs; the larger magnitude is moved to the high side by comparing exponents and mantissas, and the smaller mantissa is shifted right with sticky bits via __aeabi_llsl and __aeabi_lasr when the exponent difference is below 64. Same-sign operands are added and differing signs are subtracted. A cancellation of two or fewer bits is normalised and rounded by vcu_0159_0800164e; otherwise the result is normalised inline. A zero operand returns the other operand, and no explicit NaN or infinity handling is visible.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | operand a low word |
| `param_2` | `u32` | operand a high word |
| `param_3` | `u32` | operand b low word |
| `param_4` | `u32` | operand b high word |

**Returns** `f64`: sum in r0 (low) and r1 (high)

**Notes:** The identification as __aeabi_dadd is inferred from the structure; the decompiled return type is only 32 bits wide, the 64-bit result is in r0:r1.

- Addresses by version: 14b: 0x08001436, 14e: 0x08001436, 14f: 0x08001436, 152: 0x08001436, 153: 0x08001436, 0159: 0x08001450
- Called by: `fp64_round_pack`, `vcu_speed_mode_snapshot_update`
- Calls: `__aeabi_llsl`, `__aeabi_lasr`, `fp64_round_pack`
- Confidence: medium

## __aeabi_f2d

**Soft-float widen single-precision float to double-precision (r0:r1 pair)**

Zero magnitude returns 0:0. Otherwise builds the double: sign bit kept, exponent = float exponent + 0x380 (1023-127) placed in bits 30..20 of the high word, mantissa top 20 bits (mantissa >> 3) in the high word and the low 3 mantissa bits shifted to the top of the low word (value << 29). Denormals, Inf and NaN are not special-cased. Called by vcu_0159_08008cc0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | float bits |

**Returns** `u64`: double bits, low word in r0, high word in r1

- Addresses by version: 14b: 0x08001354, 14e: 0x08001354, 14f: 0x08001354, 152: 0x08001386, 153: 0x08001386, 0159: 0x08001386
- Called by: `vcu_speed_mode_snapshot_update`
- Confidence: high

## __aeabi_f2iz

**Soft-float convert single-precision float to signed int, truncating toward zero**

Extracts the biased exponent and builds the 24-bit mantissa with implicit leading one. Exponent below 0x7F (|x| < 1) gives 0. Exponent below 0x97 shifts the mantissa right by 0x96 - exp, otherwise shifts left by exp - 0x96 (no saturation on overflow). If the sign bit is set the result is negated. Present from build 152 onward; called by vcu_0159_08009240.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | float bits |

**Returns** `s32`: truncated integer value

- Addresses by version: 152: 0x080012EE, 153: 0x080012EE, 0159: 0x080012EE
- Called by: `vcu_drive_command_update`
- Confidence: high

## __aeabi_f2uiz

**Soft-float convert float magnitude to unsigned int, truncating**

Same mantissa extraction and shifting as __aeabi_f2iz (right shift by 0x96 - exp for exp < 0x97, left shift otherwise, 0 if exp < 0x7F) but the sign bit is ignored, so negative inputs convert as their absolute value rather than clamping to 0. Called by vcu_0159_08009240.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | float bits |

**Returns** `u32`: truncated magnitude

**Notes:** Standard __aeabi_f2uiz would return 0 for negatives; this variant ignores the sign (may be a build-specific implementation).

- Addresses by version: 148: 0x080012D6, 14a: 0x080012CC, 14b: 0x080012EE, 14e: 0x080012EE, 14f: 0x080012EE, 152: 0x08001320, 153: 0x08001320, 0159: 0x08001320
- Called by: `vcu_drive_command_update`
- Confidence: high

## __aeabi_fmul

**Soft-float IEEE-754 single precision multiply (no FPU)**

Software float multiplication. Returns 0 if either operand has a zero magnitude. Otherwise adds the biased exponents (minus 0x7F), multiplies the 24-bit mantissas (implicit 1 | 23 bits) as a 64-bit product, normalises by one bit if needed, rounds to nearest-even and sets the sign to xor of the input signs. Underflow (negative exponent) flushes to +/-0 magnitude 0; overflow, infinities, NaN and denormals are not handled specially. The code is a Keil/ARM runtime routine used because the Cortex-M4 FPU is not enabled; called by the sensor/maths routines vcu_0159_08008cc0 and vcu_0159_08009240.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | float a (raw IEEE-754 bits) |
| `param_2` | `u32` | float b (raw IEEE-754 bits) |

**Returns** `u32`: a*b as raw float bits

**Notes:** Sign of a zero result is dropped to +0 because the early-out returns 0.

- Addresses by version: 148: 0x08001256, 14a: 0x08001256, 14b: 0x08001256, 14e: 0x08001256, 14f: 0x08001256, 152: 0x08001256, 153: 0x08001256, 0159: 0x08001256
- Called by: `vcu_speed_mode_snapshot_update`, `vcu_drive_command_update`
- Confidence: high

## __aeabi_i2f

**Soft-float convert signed 32-bit integer to single-precision float (VCU_14a build)**

Takes the absolute value of the input (branch-free abs using the sign mask), normalises it with a count-leading-zeros shift, builds the exponent as 0x9D - clz (the mantissa top bit adds the final +1), packs sign, exponent and 23-bit mantissa, and rounds to nearest-even using the discarded low bits (round bit 0x80 with sticky 0x7F). Returns 0 for input 0. Exists only in the VCU_14a build; later builds use vcu_0159_080012e4 (unsigned) with a separate signed front end. Part of the soft-float runtime group.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | signed integer |

**Returns** `u32`: float bits

- Addresses by version: 14a: 0x080012BA
- Called by: `vcu_drive_command_update`
- Confidence: high

## __aeabi_i2f_v148_159

**Soft-float convert signed 32-bit integer to IEEE-754 single, round to nearest even**

Signed 32-bit integer to float32 conversion in soft-float form. It takes the absolute value using the sign mask, normalises it with a count-leading-zeros shift, and packs exponent 0x9D minus clz (the top mantissa bit adds the final +1), the top 24 bits as mantissa, and the sign in bit 31. Rounding is to nearest, ties to even: bit 0x80 is the guard, the low 7 bits are the sticky test, and the LSB is cleared on an exact tie. Input 0 returns 0. The packet also lists __aeabi_ui2f (vcu_0159_080012e4) as a callee, so the unsigned core is shared.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | integer to convert |

**Returns** `f32`: IEEE-754 binary32 bit pattern in r0

**Notes:** Named with a build range (148, 14b, 14e, 14f, 152, 153, 159; not 14a) because the VCU_14a-only copy vcu_14a_080012ba already uses __aeabi_i2f and names must be unique. Same algorithm as that copy.

- Addresses by version: 148: 0x080012BA, 14b: 0x080012D2, 14e: 0x080012D2, 14f: 0x080012D2, 152: 0x080012D2, 153: 0x080012D2, 0159: 0x080012D2
- Called by: `vcu_drive_command_update`
- Calls: `__aeabi_ui2f`
- Confidence: high

## __aeabi_lasr

**64-bit arithmetic shift right (lo, hi, shift)**

Compiler runtime helper. Shift < 32: high = (s32)hi >> n, low = (lo >> n) | (hi << (32-n)). Shift >= 32: low = (s32)hi >> (n-32) and high is the sign fill (all ones or zeros). Called by vcu_0159_08001450 (double/64-bit arithmetic). Group with __aeabi_llsl and __aeabi_llsr.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | low word |
| `param_2` | `s32` | high word |
| `param_3` | `s32` | shift count |

**Returns** `s64`: shifted value (low word r0, high r1)

- Addresses by version: 14b: 0x080013B8, 14e: 0x080013B8, 14f: 0x080013B8, 152: 0x08001584, 153: 0x08001584, 0159: 0x0800159E
- Called by: `__aeabi_dadd`
- Confidence: high

## __aeabi_llsl

**64-bit logical shift left (lo, hi, shift)**

Compiler runtime helper for 64-bit shifts left. If the shift count is >= 32 the result high word is lo << (n-32) and low word 0, otherwise high = (hi << n) | (lo >> (32-n)) and low = lo << n. Used by the 64-bit/double arithmetic helpers vcu_0159_080011ac, vcu_0159_08001450 and vcu_0159_0800164e. Group: __aeabi_llsl / __aeabi_llsr / __aeabi_lasr.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | low word |
| `param_2` | `u32` | high word |
| `param_3` | `s32` | shift count |

**Returns** `u64`: shifted 64-bit value

- Addresses by version: 148: 0x080012FE, 14a: 0x080012F4, 14b: 0x0800137A, 14e: 0x0800137A, 14f: 0x0800137A, 152: 0x080013AC, 153: 0x080013AC, 0159: 0x080013AC
- Called by: `vcu_udiv64_shift_subtract`, `__aeabi_dadd`, `fp64_round_pack`
- Confidence: high

## __aeabi_llsr

**64-bit logical shift right (lo, hi, shift)**

Compiler runtime helper. Shift >= 32: low = hi >> (n-32), high = 0. Otherwise low = (lo >> n) | (hi << (32-n)), high = hi >> n. Called by the 64-bit/double helpers vcu_0159_080011ac, vcu_0159_08001348 and vcu_0159_0800164e. Group with __aeabi_llsl and __aeabi_lasr.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | low word |
| `param_2` | `u32` | high word |
| `param_3` | `s32` | shift count |

**Returns** `u64`: shifted 64-bit value

- Addresses by version: 148: 0x0800131C, 14a: 0x08001312, 14b: 0x08001398, 14e: 0x08001398, 14f: 0x08001398, 152: 0x080013CA, 153: 0x080013CA, 0159: 0x080013CA
- Called by: `vcu_udiv64_shift_subtract`, `__aeabi_d2iz`, `fp64_round_pack`
- Confidence: high

## __aeabi_memcpy

**Forward memory copy: word-wise if both pointers 4-byte aligned, else bytewise**

Compiler runtime memcpy (ARM EABI __aeabi_memcpy). If (dst|src)&3 is zero it copies 32-bit words while at least 4 bytes remain, then copies the remaining 0..3 bytes (or all bytes when either pointer is unaligned) one byte at a time. No overlap handling (forward copy only) and no return value. Used widely by the application (11 direct callers in this packet's callee view) for buffer and struct copies.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination |
| `param_2` | `ptr` | source |
| `param_3` | `u32` | byte count |

- Addresses by version: 148: 0x0800120E, 14a: 0x0800120E, 14b: 0x0800120E, 14e: 0x0800120E, 14f: 0x0800120E, 152: 0x0800120E, 153: 0x0800120E, 0159: 0x0800120E
- Called by: `vcu_0159_080054ec`, `vcu_fw_update_frame_handler`, `vcu_crypto_key_load`, `vcu_rx_ring0_pop_record`, `vcu_can_tx_queue_peek`, `vcu_rx_ring0_push_record`, `vcu_can_tx_queue_push`, `vcu_0159_08009da8`, `vcu_record_send_chunked`, `vcu_0159_0800cfac`, `vcu_0159_0800ef14`
- Confidence: high

## __aeabi_memset

**Fill a byte buffer with a constant value (dest, count, value argument order)**

Runtime memset helper in the ARM EABI argument order (dest, n, c), a plain byte loop that stores param_3 to param_2 consecutive bytes. The two short veneers right after it (vcu_0159_08001240 and vcu_0159_08001244) are its callers and are most likely __aeabi_memclr / __aeabi_memclr4 style wrappers that supply a zero value. No return value.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination buffer |
| `param_2` | `s32` | number of bytes to write |
| `param_3` | `u8` | fill value |

- Addresses by version: 148: 0x08001232, 14a: 0x08001232, 14b: 0x08001232, 14e: 0x08001232, 14f: 0x08001232, 152: 0x08001232, 153: 0x08001232, 0159: 0x08001232
- Called by: `vcu_buf_zero`, `memset`
- Confidence: high

## __aeabi_ui2f

**Soft-float convert unsigned 32-bit integer to single-precision float**

Normalises the input with a count-leading-zeros shift, exponent = 0x9D - clz (+1 from the mantissa implicit bit), mantissa = top 24 bits, rounds to nearest-even from the low bits (round bit 0x80, sticky 0x7F). Returns 0 for 0. The signed wrapper (vcu_0159_080012d2, __aeabi_i2f) falls into/calls this routine after taking abs and re-applying the sign. Called from the same maths routines as the other soft-float helpers (vcu_0159_08008cc0, vcu_0159_08009240).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | unsigned integer (decompiler shows int) |

**Returns** `u32`: float bits

- Addresses by version: 148: 0x080012CC, 14b: 0x080012E4, 14e: 0x080012E4, 14f: 0x080012E4, 152: 0x080012E4, 153: 0x080012E4, 0159: 0x080012E4
- Called by: `__aeabi_i2f_v148_159`, `vcu_speed_mode_snapshot_update`, `vcu_drive_command_update`
- Confidence: high

## fp64_round_pack

**Soft-float double normalise, round to nearest even and pack for the add routine**

Helper called only from the cancellation path of __aeabi_dadd (vcu_0159_08001450). It takes a 64-bit mantissa with exponent and sign, counts leading zeros to normalise it, and shifts it into the 53-bit double field with __aeabi_llsl and __aeabi_llsr, collecting shifted-out bits as a sticky flag. Rounding is to nearest, ties to even, using bit 10 of the extended mantissa as the guard and bits 0 to 9 as the tie test; a round-up carry propagates into the exponent. An underflowing result returns 0, and overflow is not handled.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | mantissa low word |
| `param_2` | `s32` | mantissa high word including the exponent field |
| `param_3` | `u32` | extra low word |
| `param_4` | `u32` | extra high word |
| `param_5` | `u32` | low-word addend (0 from the caller) |
| `param_6` | `u32` | sign bit (0x80000000 or 0) |
| `param_7` | `s32` | biased result exponent |

**Returns** `f64`: packed double in r0:r1

**Notes:** The argument meanings are inferred from the single caller in vcu_0159_08001450.

- Addresses by version: 14b: 0x08001610, 14e: 0x08001610, 14f: 0x08001610, 152: 0x08001634, 153: 0x08001634, 0159: 0x0800164E
- Called by: `__aeabi_dadd`
- Calls: `__aeabi_llsl`, `__aeabi_llsr`, `__aeabi_dadd`
- Confidence: medium

## memset

**C library memset: fill n bytes at dst with c and return dst**

Standard C memset(dst, c, n) argument order. It forwards to the ARM EABI helper __aeabi_memset, which takes (dst, n, c), swapping the value and count arguments, and returns the original destination pointer. The fill byte is param_2 and the count is param_3.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination |
| `param_2` | `u8` | fill byte |
| `param_3` | `u32` | byte count |

**Returns** `ptr`: destination pointer (param_1)

- Addresses by version: 148: 0x08001244, 14a: 0x08001244, 14b: 0x08001244, 14e: 0x08001244, 14f: 0x08001244, 152: 0x08001244, 153: 0x08001244, 0159: 0x08001244
- Calls: `__aeabi_memset`
- Confidence: high

## vcu_udiv64_shift_subtract

**64-bit unsigned divide returning the quotient by 64-step shift and subtract**

Unsigned 64-bit division by restoring shift-and-subtract, producing one quotient bit per step from bit 63 down to bit 0. At step k it tests (dividend >> k) >= divisor, which is the same as dividend >= divisor << k; when true it subtracts divisor << k from the dividend and adds 1 << k to the quotient. The shifts are done by __aeabi_llsr and __aeabi_llsl, and the remainder stays in the local dividend and is not returned. There is no zero-divisor check, so a zero divisor gives an all-ones quotient. Callers are vcu_0159_0800b440, vcu_0159_0800e8e0 and vcu_14a_080013a0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | dividend low word |
| `param_2` | `u32` | dividend high word |
| `param_3` | `u32` | divisor low word |
| `param_4` | `u32` | divisor high word |

**Returns** `u64`: quotient in r0:r1

**Notes:** The name is ours: the routine resembles libgcc __udivdi3 but was not matched to it. Only the quotient is returned.

- Addresses by version: 148: 0x080011AC, 14a: 0x080011AC, 14b: 0x080011AC, 14e: 0x080011AC, 14f: 0x080011AC, 152: 0x080011AC, 153: 0x080011AC, 0159: 0x080011AC
- Called by: `crm_clocks_freq_get`, `system_clock_config`
- Calls: `__aeabi_llsl`, `__aeabi_llsr`
- Confidence: high
