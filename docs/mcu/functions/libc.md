# MCU - `libc` functions

30 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`__ARM_scalbn`](#__arm_scalbn) | 0x080017DC | Soft-float scale: add an integer to the exponent of a double (ldexp style) |
| [`__ARM_scalbnf`](#__arm_scalbnf) | 0x080013CC | Soft-float scale: add an integer to the exponent of a float (ldexpf style) |
| [`__aeabi_d2iz`](#__aeabi_d2iz) | 0x0800187E | Soft-float IEEE-754 double to signed int32, truncating toward zero |
| [`__aeabi_dadd`](#__aeabi_dadd) | 0x080014CC | Soft-float IEEE-754 double add/subtract (no FPU) on 64-bit word pairs |
| [`__aeabi_ddiv`](#__aeabi_ddiv) | 0x080016FE | Soft-float IEEE-754 double precision divide (no FPU) |
| [`__aeabi_dmul`](#__aeabi_dmul) | 0x0800161A | Soft-float IEEE-754 double multiply (no FPU) using 32x32 partial products |
| [`__aeabi_f2d`](#__aeabi_f2d) | 0x080018BC | Soft-float widen single-precision float to double-precision (r0:r1 pair) |
| [`__aeabi_f2iz`](#__aeabi_f2iz) | 0x08001824 | Soft-float convert single-precision float to signed int, truncating toward zero |
| [`__aeabi_f2uiz`](#__aeabi_f2uiz) | 0x08001856 | Soft-float convert float magnitude to unsigned int, truncating |
| [`__aeabi_fadd`](#__aeabi_fadd) | 0x080012B8 | Soft-float IEEE-754 single-precision add (no FPU), raw bit patterns in and out |
| [`__aeabi_fdiv`](#__aeabi_fdiv) | 0x08001450 | Soft-float IEEE-754 single precision divide (no FPU) |
| [`__aeabi_fmul`](#__aeabi_fmul) | 0x08001368 | Soft-float IEEE-754 single precision multiply (no FPU) |
| [`__aeabi_fsub`](#__aeabi_fsub) | 0x0800135C | Soft-float single-precision subtract a - b: negate b and tail-call the add |
| [`__aeabi_i2f`](#__aeabi_i2f) | 0x08001D48 | Soft-float convert signed 32-bit integer to single-precision float |
| [`__aeabi_lasr`](#__aeabi_lasr) | 0x0800194A | 64-bit arithmetic shift right (lo, hi, shift) |
| [`__aeabi_llsl`](#__aeabi_llsl) | 0x0800190C | 64-bit logical shift left (lo, hi, shift) |
| [`__aeabi_llsr`](#__aeabi_llsr) | 0x0800192A | 64-bit logical shift right (lo, hi, shift) |
| [`__aeabi_memclr`](#__aeabi_memclr) | 0x080012A2 | Zero-fill a buffer: EABI memclr entry that calls the memset routine with value 0 |
| [`__aeabi_memcpy`](#__aeabi_memcpy) | 0x08001270 | Forward memory copy: word-wise if both pointers 4-byte aligned, else bytewise |
| [`__aeabi_memset`](#__aeabi_memset) | 0x08001294 | Fill a byte buffer with a constant value (dest, count, value argument order) |
| [`__aeabi_ui2f`](#__aeabi_ui2f) | 0x080013F6 | Soft-float convert unsigned 32-bit integer to single-precision float |
| [`__divdi3`](#__divdi3) | 0x0800120E | Signed 64-bit division wrapper around the unsigned divider, sign fixed up afterwards |
| [`__udivdi3`](#__udivdi3) | 0x080011AC | Unsigned 64-bit division: 64-step restoring divider returning the quotient |
| [`mcu_dbl_round_pack`](#mcu_dbl_round_pack) | 0x080019FA | Normalise, round to nearest-even and pack a double from a wide mantissa and exponent |
| [`mcu_fcmp_sortkeys_a`](#mcu_fcmp_sortkeys_a) | 0x080018E4 | Soft-float compare helper: convert two float bit patterns to comparison keys |
| [`mcu_fcmp_sortkeys_b`](#mcu_fcmp_sortkeys_b) | 0x080018F8 | Soft-float compare helper (second copy): convert two float words to comparison keys |
| [`mcu_float_rsub`](#mcu_float_rsub) | 0x08001362 | Reverse float subtract: returns the second argument minus the first |
| [`mcu_i2f_lzc`](#mcu_i2f_lzc) | 0x080013E4 | Signed int32 to float conversion, CLZ-normalised with round-to-nearest-even |
| [`mcu_ui2d_low_word`](#mcu_ui2d_low_word) | 0x0800180A | Packs a 32-bit integer as a double with exponent 0x433 and returns the low word |
| [`memset`](#memset) | 0x080012A6 | ISO C memset(s, c, n): fill n bytes with byte c and return s |

## __ARM_scalbn

**Soft-float scale: add an integer to the exponent of a double (ldexp style)**

Returns x * 2^n for a double x in (param_1 lo, param_2 hi) by adding param_3 << 20 to the high word. A zero-magnitude input is returned unchanged; if the exponent would go to zero or below the result is flushed to 0. No overflow/NaN handling. Double-precision counterpart of mcu_0160_080013cc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | x low word |
| `param_2` | `u32` | x high word |
| `param_3` | `s32` | exponent increment n |

**Returns** `u64`: x*2^n as double bits

- Addresses by version: 12b: 0x080017C2, 143: 0x080017C2, 152: 0x080017C2, 0160: 0x080017DC
- Called by: `mcu_0160_08003178`, `mcu_0160_08003f2c`, `mcu_0160_08004700`, `mcu_0160_08004768`, `mcu_cfg_gain_10c_q15`, `mcu_cfg_gain_108_q15`, `mcu_0160_08004a60`, `mcu_0160_08004e78`, `mcu_0160_080093f8`, `mcu_0160_0800b10c`
- Confidence: high

## __ARM_scalbnf

**Soft-float scale: add an integer to the exponent of a float (ldexpf style)**

Returns param_1 * 2^param_2 by adding param_2 to the biased exponent field (param_2 << 23). A zero-magnitude input is returned unchanged; if the new exponent would drop to or below zero the result is flushed to +0. No overflow, NaN or sign-of-zero handling. Used by other soft-float routines and by application code for power-of-two scaling.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | float x (IEEE-754 bits) |
| `param_2` | `s32` | binary exponent increment n |

**Returns** `u32`: x*2^n as float bits

- Addresses by version: 12b: 0x080013D4, 143: 0x080013CC, 152: 0x080013CC, 0160: 0x080013CC
- Called by: `mcu_speed_lpf_band_update`, `mcu_speed_estimate_update`, `mcu_0160_08003f2c`, `mcu_0160_08005830`, `mcu_dynamic_bound_clamp_update`, `mcu_sqrt_limit_setup_float`, `mcu_0160_0800729c`, `mcu_dq_power_estimate`, `mcu_0160_080078f0`, `mcu_gain_triple_q15_from_float`, `mcu_can_rx_command_dispatch`, `mcu_0160_080093f8` ...
- Confidence: high

## __aeabi_d2iz

**Soft-float IEEE-754 double to signed int32, truncating toward zero**

Takes a double as (low word, high word). Biased exponents below 0x3FF (|x| < 1) return 0. For exponents from 0x3FF to 0x433 the significand with the implicit one restored (high word bits 19..0 plus 0x100000) is shifted right by 0x433 - exponent through __aeabi_llsr and the low 32 bits are returned, negated when the sign bit is set. For exponents of 0x434 and above the low word is shifted left by exponent - 0x433 with no saturation, so out-of-range values wrap.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | double, low word |
| `param_2` | `u32` | double, high word |

**Returns** `s32`: x truncated toward zero, wrapped on overflow

- Addresses by version: 12b: 0x08001864, 143: 0x08001864, 152: 0x08001864, 0160: 0x0800187E
- Called by: `mcu_0160_08003178`, `mcu_0160_08003f2c`, `mcu_0160_08004700`, `mcu_0160_08004768`, `mcu_cfg_gain_10c_q15`, `mcu_cfg_gain_108_q15`, `mcu_0160_08004a60`, `mcu_0160_08004e78`, `mcu_0160_080093f8`, `mcu_0160_0800b10c`
- Calls: `__aeabi_llsr`
- Confidence: high

## __aeabi_dadd

**Soft-float IEEE-754 double add/subtract (no FPU) on 64-bit word pairs**

Adds two doubles passed as (low word, high word) pairs. Operands are ordered by magnitude, and the smaller significand is shifted right by the exponent difference (up to 63 bits, using __aeabi_llsl and __aeabi_lasr); larger differences drop it. Equal signs add the 53-bit significands; different signs subtract them, so subtraction is folded into this routine with no separate dsub body. Results with a small exponent difference are renormalised through mcu_dbl_round_pack (mcu_0160_080019fa), others are rounded inline to nearest-even. A zero operand returns the other one. The decompiled return is only 32 bits; the 64-bit result is returned in r0:r1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | operand a, low word |
| `param_2` | `u32` | operand a, high word (sign, exponent, top mantissa bits) |
| `param_3` | `u32` | operand b, low word |
| `param_4` | `u32` | operand b, high word |

**Returns** `u64`: a + b as an IEEE-754 double (r0 low, r1 high)

**Notes:** The packet's callee list for this body also names __aeabi_ddiv, which is not called here. The Ghidra return type is 32-bit even though the result is 64-bit.

- Addresses by version: 12b: 0x080014B2, 143: 0x080014B2, 152: 0x080014B2, 0160: 0x080014CC
- Called by: `mcu_0160_0800160e`, `mcu_0160_08004e78`, `mcu_0160_080093f8`
- Calls: `__aeabi_ddiv`, `__aeabi_llsl`, `__aeabi_lasr`, `mcu_dbl_round_pack`
- Confidence: medium

## __aeabi_ddiv

**Soft-float IEEE-754 double precision divide (no FPU)**

Divides the double in (param_1 lo, param_2 hi) by the double in (param_3 lo, param_4 hi). Returns 0 if either operand is zero. Uses a bitwise restoring long division over the 53-bit significands (20+32 quotient bits), exponent difference with bias 0x3ff, sign XOR, and round-to-nearest-even; underflow returns 0, no overflow, NaN or denormal handling. Result is returned as a 64-bit r0:r1 pair.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | a low word |
| `param_2` | `u32` | a high word |
| `param_3` | `u32` | b low word |
| `param_4` | `u32` | b high word |

**Returns** `u64`: a/b as double bits (lo in r0, hi in r1)

- Addresses by version: 12b: 0x080016E4, 143: 0x080016E4, 152: 0x080016E4, 0160: 0x080016FE
- Called by: `__aeabi_dadd`, `mcu_dbl_round_pack`, `mcu_0160_08003178`, `mcu_0160_08003f2c`, `mcu_0160_08004700`, `mcu_0160_08004768`, `mcu_cfg_gain_10c_q15`, `mcu_cfg_gain_108_q15`, `mcu_0160_08004a60`, `mcu_0160_08004e78`, `mcu_0160_080093f8`
- Confidence: high

## __aeabi_dmul

**Soft-float IEEE-754 double multiply (no FPU) using 32x32 partial products**

Multiplies two doubles given as word pairs. Splits each 53-bit significand into 32-bit pieces and forms the 106-bit product from partial products (the 32x32 products of the low and high pieces, plus the cross terms). Biased exponents are added and 0x3FF is subtracted, the sign is the xor of the two sign bits, and the wide product is passed to mcu_dbl_round_pack (mcu_0160_080019fa), which normalises, rounds and packs. The result is returned by that tail call in r0:r1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | multiplicand a, low word |
| `param_2` | `u32` | multiplicand a, high word |
| `param_3` | `u32` | multiplier b, low word |
| `param_4` | `u32` | multiplier b, high word |

**Notes:** When either operand is zero the decompiled body returns without writing r0:r1, so the zero result depends on what those registers hold. Check the disassembly for this path.

- Addresses by version: 12b: 0x08001600, 143: 0x08001600, 152: 0x08001600, 0160: 0x0800161A
- Called by: `mcu_0160_08004700`, `mcu_0160_08004768`, `mcu_0160_08004a60`, `mcu_0160_08004e78`
- Calls: `mcu_dbl_round_pack`
- Confidence: medium

## __aeabi_f2d

**Soft-float widen single-precision float to double-precision (r0:r1 pair)**

Rebases the exponent by +0x380 (1023 - 127), moves the 23-bit fraction to the top of the 52-bit double fraction (>>3 into the high word, low 3 bits into the top of the low word) and keeps the sign. Zero magnitude returns 0.0. Denormals/NaN/Inf are not special-cased.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | float bits |

**Returns** `u64`: double bits (lo in r0, hi in r1)

- Addresses by version: 12b: 0x080018A2, 143: 0x080018A2, 152: 0x080018A2, 0160: 0x080018BC
- Called by: `mcu_0160_08003f2c`, `mcu_0160_08004700`, `mcu_0160_08004768`, `mcu_cfg_gain_10c_q15`, `mcu_cfg_gain_108_q15`, `mcu_0160_08004a60`, `mcu_0160_08004e78`, `mcu_0160_080093f8`, `mcu_0160_0800b10c`
- Confidence: high

## __aeabi_f2iz

**Soft-float convert single-precision float to signed int, truncating toward zero**

Extracts exponent and 24-bit significand; magnitudes below 1.0 (exponent < 0x7f) give 0, exponents below 0x97 shift the significand right (truncation), larger ones shift left (no saturation, so values >= 2^31 overflow silently). The result is negated if the sign bit of the input is set.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | float bits |

**Returns** `s32`: truncated integer

- Addresses by version: 12b: 0x0800180A, 143: 0x0800180A, 152: 0x0800180A, 0160: 0x08001824
- Called by: `mcu_speed_lpf_band_update`, `mcu_speed_estimate_update`, `mcu_0160_08003f2c`, `mcu_target_derate_calc`, `mcu_0160_08005830`, `mcu_dynamic_bound_clamp_update`, `mcu_sqrt_limit_setup_float`, `mcu_0160_0800729c`, `mcu_dq_power_estimate`, `mcu_0160_080078f0`, `mcu_gain_triple_q15_from_float`, `mcu_0160_080093f8` ...
- Confidence: high

## __aeabi_f2uiz

**Soft-float convert float magnitude to unsigned int, truncating**

Same extraction as mcu_0160_08001824 (shift significand by 0x96 - exponent, 0 for |x| < 1) but the sign bit is ignored, so negative inputs give their absolute value. Used by a single caller, mcu_0160_080093f8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | float bits |

**Returns** `u32`: truncated |x|

- Addresses by version: 12b: 0x0800183C, 143: 0x0800183C, 152: 0x0800183C, 0160: 0x08001856
- Called by: `mcu_0160_080093f8`
- Confidence: high

## __aeabi_fadd

**Soft-float IEEE-754 single-precision add (no FPU), raw bit patterns in and out**

Adds two single-precision values given as raw bit patterns. The operand with the larger magnitude (magnitude compared with the sign shifted out) becomes the base, and the other significand is shifted right by the exponent difference, keeping guard bits. When the difference is 32 or more the result is the larger operand, adjusted by one ulp for the sticky bit when the signs differ. Equal signs add significands; different signs subtract them (the sign xor is kept in uVar4). The result is renormalised with CLZ and rounded to nearest-even from the guard and sticky bits. A zero second operand returns the first unchanged. NaN, infinity and denormal inputs are not special-cased.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | addend a, IEEE-754 bits |
| `param_2` | `u32` | addend b, IEEE-754 bits |

**Returns** `u32`: a + b as IEEE-754 bits

**Notes:** The packet's callee list for this function names __aeabi_ui2f and __aeabi_fdiv, but the decompiled body makes no calls. Treat that list as stale. The rounding and subtract paths were checked against the code only, not against a reference model.

- Addresses by version: 12b: 0x080012C0, 143: 0x080012B8, 152: 0x080012B8, 0160: 0x080012B8
- Called by: `__aeabi_fsub`, `mcu_float_rsub`, `mcu_speed_lpf_band_update`, `mcu_speed_estimate_update`, `mcu_0160_08003f2c`, `mcu_0160_08005830`, `mcu_pos_tracker_init`
- Calls: `__aeabi_ui2f`, `__aeabi_fdiv`
- Confidence: medium

## __aeabi_fdiv

**Soft-float IEEE-754 single precision divide (no FPU)**

Divides param_1 by param_2 as raw float bits. If either operand has zero magnitude the result is 0 (including division by zero, which does NOT yield infinity). Otherwise subtracts exponents, runs a 24-iteration restoring long division of the significands, computes sign as XOR, applies round-to-nearest-even from the final remainder, and returns 0 when the exponent underflows. No overflow, NaN or denormal handling.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | numerator float bits |
| `param_2` | `u32` | denominator float bits |

**Returns** `u32`: a/b as float bits

- Addresses by version: 12b: 0x08001436, 143: 0x08001436, 152: 0x08001436, 0160: 0x08001450
- Called by: `__aeabi_fadd`, `mcu_speed_lpf_band_update`, `mcu_target_derate_calc`, `mcu_0160_08005830`, `mcu_dynamic_bound_clamp_update`, `mcu_fscale_mul_div_a`, `mcu_fscale_mul_div_b`, `mcu_dq_power_estimate`, `mcu_gain_triple_q15_from_float`, `mcu_can_rx_command_dispatch`, `mcu_0160_080093f8`, `mcu_param_record_load` ...
- Confidence: high

## __aeabi_fmul

**Soft-float IEEE-754 single precision multiply (no FPU)**

Multiplies two single-precision floats passed as raw bit patterns. Returns +0 if either operand has a zero magnitude. Otherwise adds exponents (minus bias 0x7f), multiplies the two 24-bit significands in a 64-bit product, normalises with a 1-bit shift if needed, rounds to nearest-even and ORs in the XOR of the signs. Underflow (exponent < 0) flushes to 0; there is no overflow, NaN, infinity or denormal handling. Used heavily by the FOC/control code because the AT32F415 core is integer-only here.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | float a (IEEE-754 bits) |
| `param_2` | `u32` | float b (IEEE-754 bits) |

**Returns** `u32`: a*b as float bits

**Notes:** Same algorithm as the VCU image's __aeabi_fmul.

- Addresses by version: 12b: 0x08001370, 143: 0x08001368, 152: 0x08001368, 0160: 0x08001368
- Called by: `mcu_speed_lpf_band_update`, `mcu_speed_estimate_update`, `mcu_0160_08004700`, `mcu_0160_08004e78`, `mcu_0160_08005830`, `mcu_sqrt_limit_setup_float`, `mcu_fscale_mul_div_a`, `mcu_fscale_mul_div_b`, `mcu_gain_triple_q15_from_float`, `mcu_0160_08008f34`, `mcu_0160_080093f8`, `mcu_pos_tracker_init` ...
- Confidence: high

## __aeabi_fsub

**Soft-float single-precision subtract a - b: negate b and tail-call the add**

Computes a - b by flipping the sign bit of b and tail-calling __aeabi_fadd (mcu_0160_080012b8). Same special-case behaviour as the add.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | minuend a, IEEE-754 bits |
| `param_2` | `u32` | subtrahend b, IEEE-754 bits |

**Returns** `u32`: a - b as IEEE-754 bits

- Addresses by version: 12b: 0x08001364, 143: 0x0800135C, 152: 0x0800135C, 0160: 0x0800135C
- Called by: `mcu_0160_08003f2c`, `mcu_0160_08004db8`, `mcu_0160_08005830`, `mcu_0160_08009ec4`
- Calls: `__aeabi_fadd`
- Confidence: high

## __aeabi_i2f

**Soft-float convert signed 32-bit integer to single-precision float**

Returns 0 for 0; otherwise takes the sign, negates negative inputs, normalises with CLZ and builds the float from sign, exponent 0x8f - clz (clz-adjusted, one lower than the unsigned version because the magnitude is up to 31 bits) and the 23 top mantissa bits. Truncates instead of rounding. Callers include mcu_0160_08002b64 and 08004db8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | signed integer |

**Returns** `u32`: float bits

**Notes:** Mantissa is truncated, not rounded to nearest-even.

- Addresses by version: 12b: 0x08001D2C, 143: 0x08001D2C, 152: 0x08001D2C, 0160: 0x08001D48
- Called by: `mcu_speed_lpf_band_update`, `mcu_0160_08004db8`
- Confidence: high

## __aeabi_lasr

**64-bit arithmetic shift right (lo, hi, shift)**

Shifts the signed 64-bit value (param_1 low, param_2 high) right by param_3 with sign fill. For shift >= 32 the low word is the high word arithmetically shifted by param_3-32 and the high word becomes the sign (all 0 or all 1); otherwise the bits move across the word boundary. Only caller is mcu_0160_080014cc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value low word |
| `param_2` | `u32` | value high word |
| `param_3` | `s32` | shift count |

**Returns** `s64`: shifted value

- Addresses by version: 12b: 0x0800192E, 143: 0x0800192E, 152: 0x0800192E, 0160: 0x0800194A
- Called by: `__aeabi_dadd`
- Confidence: high

## __aeabi_llsl

**64-bit logical shift left (lo, hi, shift)**

Shifts the 64-bit value (param_1 low, param_2 high) left by param_3 bits. For shifts of 32 or more only the low word survives, moved into the high word and shifted by param_3-32; otherwise the high word receives the bits carried out of the low word. Used by 64-bit fixed-point code and the soft-float routines.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value low word |
| `param_2` | `u32` | value high word |
| `param_3` | `s32` | shift count |

**Returns** `u64`: shifted value

- Addresses by version: 12b: 0x080018F0, 143: 0x080018F0, 152: 0x080018F0, 0160: 0x0800190C
- Called by: `__udivdi3`, `__aeabi_dadd`, `mcu_dbl_round_pack`
- Confidence: high

## __aeabi_llsr

**64-bit logical shift right (lo, hi, shift)**

Shifts the 64-bit value (param_1 low, param_2 high) right by param_3 bits with zero fill. For shift >= 32 the result is the high word shifted by param_3-32 with a zero high word; otherwise the low word receives the bits shifted down from the high word.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value low word |
| `param_2` | `u32` | value high word |
| `param_3` | `s32` | shift count |

**Returns** `u64`: shifted value

- Addresses by version: 12b: 0x0800190E, 143: 0x0800190E, 152: 0x0800190E, 0160: 0x0800192A
- Called by: `__udivdi3`, `__aeabi_d2iz`, `mcu_dbl_round_pack`
- Confidence: high

## __aeabi_memclr

**Zero-fill a buffer: EABI memclr entry that calls the memset routine with value 0**

Two-instruction wrapper: calls __aeabi_memset (mcu_0160_08001294) with fill byte 0 for the (destination, byte count) pair it received in r0 and r1. Used by the C runtime and by struct initialisers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination buffer |
| `param_2` | `u32` | number of bytes to clear |

- Addresses by version: 12b: 0x080012AA, 143: 0x080012A2, 152: 0x080012A2, 0160: 0x080012A2
- Called by: `mcu_0160_08009f98`, `mcu_0160_0800b324`, `mcu_0160_0800e146`
- Calls: `__aeabi_memset`
- Confidence: high

## __aeabi_memcpy

**Forward memory copy: word-wise if both pointers 4-byte aligned, else bytewise**

Copies param_3 bytes from param_2 to param_1. If both pointers are word aligned it copies 32-bit words while at least 4 bytes remain, then finishes the tail (or the whole buffer when unaligned) bytewise. No overlap handling (forward copy only), so it is not a memmove. Matches the ARM Compiler runtime __aeabi_memcpy; called from many application routines.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination |
| `param_2` | `ptr` | source |
| `param_3` | `u32` | byte count |

- Addresses by version: 12b: 0x08001278, 143: 0x08001270, 152: 0x08001270, 0160: 0x08001270
- Called by: `mcu_speed_lpf_band_update`, `mcu_0160_08005edc`, `mcu_0160_0800672c`, `mcu_can_rx_command_dispatch`, `mcu_0160_08008b60`, `mcu_0160_0800b324`, `mcu_msg_ring2_enqueue_frames`, `mcu_0160_0800e146`
- Confidence: high

## __aeabi_memset

**Fill a byte buffer with a constant value (dest, count, value argument order)**

Writes param_3 to param_2 consecutive bytes starting at param_1; a count of 0 does nothing. Note the AEABI argument order (dest, count, value), which is the reverse of C memset; the two small veneers right behind it (mcu_0160_080012a2 and 080012a6) call it, presumably as __aeabi_memclr/memset wrappers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination |
| `param_2` | `u32` | byte count |
| `param_3` | `u8` | fill value |

- Addresses by version: 12b: 0x0800129C, 143: 0x08001294, 152: 0x08001294, 0160: 0x08001294
- Called by: `__aeabi_memclr`, `memset`
- Confidence: high

## __aeabi_ui2f

**Soft-float convert unsigned 32-bit integer to single-precision float**

Normalises the integer with a CLZ shift, builds exponent 0x9d - clz (bias 127 + 30 for the position of the top bit) and the top 23 mantissa bits, then rounds to nearest-even using the dropped low bits. Returns 0 for input 0. Despite the decompiler showing a signed parameter, there is no sign handling, so it is the unsigned variant; the signed one is mcu_0160_08001d48.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | unsigned integer |

**Returns** `u32`: float bits

- Addresses by version: 12b: 0x08001410, 143: 0x080013F6, 152: 0x080013F6, 0160: 0x080013F6
- Called by: `__aeabi_fadd`, `mcu_i2f_lzc`, `mcu_0160_08004700`, `mcu_0160_08004db8`, `mcu_dynamic_bound_clamp_update`, `mcu_dq_power_estimate`, `mcu_can_rx_command_dispatch`, `mcu_param_record_load`, `mcu_pos_tracker_init`
- Confidence: high

## __divdi3

**Signed 64-bit division wrapper around the unsigned divider, sign fixed up afterwards**

Signed 64-bit division. Negates each operand whose high word is negative (two's complement on the 64-bit pair, with the borrow carried into the high word), calls the unsigned divider mcu_0160_080011ac, and negates the 64-bit quotient when the two operand signs differ. The remainder is not produced.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | dividend, low word |
| `param_2` | `s32` | dividend, high word (sign carried here) |
| `param_3` | `u32` | divisor, low word |
| `param_4` | `s32` | divisor, high word (sign carried here) |

**Returns** `s64`: signed quotient, truncated toward zero

- Addresses by version: 12b: 0x08001216, 143: 0x0800120E, 152: 0x0800120E, 0160: 0x0800120E
- Called by: `mcu_0160_08009160`
- Calls: `__udivdi3`
- Confidence: high

## __udivdi3

**Unsigned 64-bit division: 64-step restoring divider returning the quotient**

Unsigned 64-bit a / b, with a = (param_1 low word, param_2 high word) and b = (param_3 low word, param_4 high word). Runs 64 iterations from bit 63 down to bit 0: for each bit i it tests (a >> i) >= b as a 64-bit unsigned compare (equivalent to a >= b << i), and when true subtracts b << i from the running remainder and sets bit i of the 64-bit quotient. The shifts go through __aeabi_llsr (mcu_0160_0800192a) and __aeabi_llsl (mcu_0160_0800190c). Division by zero yields 0xFFFFFFFFFFFFFFFF because every compare succeeds. The remainder is not returned.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | dividend, low word |
| `param_2` | `u32` | dividend, high word |
| `param_3` | `u32` | divisor, low word |
| `param_4` | `u32` | divisor, high word |

**Returns** `u64`: unsigned quotient a / b; all ones when b is zero

**Notes:** Named after the libgcc unsigned 64-bit divide. The body is a plain restoring loop, not libgcc's normalised version, so the name describes the contract, not the exact code.

- Addresses by version: 12b: 0x080011B4, 143: 0x080011AC, 152: 0x080011AC, 0160: 0x080011AC
- Called by: `__divdi3`, `system_clock_config`, `crm_clocks_freq_get`
- Calls: `__aeabi_llsl`, `__aeabi_llsr`
- Confidence: medium

## mcu_dbl_round_pack

**Normalise, round to nearest-even and pack a double from a wide mantissa and exponent**

Shared tail of the soft-float double routines. Takes a wide significand in param_1..param_4 (two words for the value and a sticky pair), normalises with CLZ on the high word, shifts right by 11 to get a 53-bit significand, and rounds to nearest-even with bit 10 as the guard bit and the low 10 bits as sticky. The exponent is param_7 minus the normalisation shift plus 10, placed in the high word bits 20 and up, and the sign comes from param_6. Results whose exponent goes negative return 0 (flush to zero). There is no overflow-to-infinity branch.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | significand low word |
| `param_2` | `s32` | significand high word (CLZ taken from here when non-zero) |
| `param_3` | `s32` | extra low bits or sticky word, low |
| `param_4` | `s32` | extra low bits or sticky word, high |
| `param_5` | `u32` | addend for the low result word (rounding carry input) |
| `param_6` | `s32` | sign bit to OR in (0 or 0x80000000) |
| `param_7` | `s32` | biased exponent before normalisation |

**Returns** `u64`: packed IEEE-754 double (r0 low, r1 high), or 0 on underflow

**Notes:** The decompile contains an unmodelled FUN_0800190c() call with no arguments at the start of the body, so the exact handling of the sticky words is inferred. Callers are __aeabi_dadd, __aeabi_dmul and mcu_ui2d_low_word.

- Addresses by version: 12b: 0x080019DE, 143: 0x080019DE, 152: 0x080019DE, 0160: 0x080019FA
- Called by: `__aeabi_dadd`, `__aeabi_dmul`, `mcu_ui2d_low_word`
- Calls: `__aeabi_ddiv`, `__aeabi_llsl`, `__aeabi_llsr`
- Confidence: medium

## mcu_fcmp_sortkeys_a

**Soft-float compare helper: convert two float bit patterns to comparison keys**

For each of two 32-bit float words, if it is non-negative as a signed integer it is replaced by 0x80000000 - value; negative words are left unchanged. This is the sign-magnitude-to-ordered-integer step used before comparing floats as integers; returns both transformed values as r0:r1. Identical body to mcu_0160_080018f8; the only caller is mcu_0160_08005830, which probably uses it as the prologue of a float compare (__aeabi_cfcmple/cfrcmple style).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | float a bits |
| `param_2` | `s32` | float b bits |

**Returns** `u64`: transformed (a in r0, b in r1)

**Notes:** Exact AEABI entry point it belongs to is not confirmed; the two copies differ only in address.

- Addresses by version: 12b: 0x080018C8, 143: 0x080018C8, 152: 0x080018C8, 0160: 0x080018E4
- Called by: `mcu_0160_08005830`
- Confidence: medium

## mcu_fcmp_sortkeys_b

**Soft-float compare helper (second copy): convert two float words to comparison keys**

Byte-for-byte equivalent of mcu_0160_080018e4: any non-negative input word x becomes 0x80000000 - x, negative words pass through, results returned in r0:r1. Called from mcu_0160_08004db8 and mcu_0160_08005830, part of the soft-float comparison cluster. Two copies exist because the ARM runtime emits one per compare entry (e.g. cfcmple vs cfrcmple).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | float a bits |
| `param_2` | `s32` | float b bits |

**Returns** `u64`: transformed (a in r0, b in r1)

**Notes:** Role inferred from the transform, not from the call sites.

- Addresses by version: 12b: 0x080018DC, 143: 0x080018DC, 152: 0x080018DC, 0160: 0x080018F8
- Called by: `mcu_0160_08004db8`, `mcu_0160_08005830`
- Confidence: medium

## mcu_float_rsub

**Reverse float subtract: returns the second argument minus the first**

Flips the sign bit of its one visible argument (r0) and tail-calls __aeabi_fadd. The second addend is not a parameter in the decompile, so it is whatever the caller left in r1; the net result is r1 + (-r0) = r1 - r0, a reverse subtract. The only caller seen in this component is mcu_0160_08005830.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value to subtract, IEEE-754 bits (r0); the minuend is passed in r1 and is not visible here |

**Returns** `u32`: r1 - r0 as IEEE-754 bits

**Notes:** The reverse-subtract reading depends on the caller leaving the minuend in r1. Check the disassembly of mcu_0160_08005830 before relying on it.

- Addresses by version: 12b: 0x0800136A, 143: 0x08001362, 152: 0x08001362, 0160: 0x08001362
- Called by: `mcu_0160_08005830`
- Calls: `__aeabi_fadd`
- Confidence: medium

## mcu_i2f_lzc

**Signed int32 to float conversion, CLZ-normalised with round-to-nearest-even**

Converts a signed 32-bit integer to IEEE-754 single precision. Takes the absolute value (sign kept in bit 31), normalises it with LZCOUNT so the leading one is bit 31, sets the biased exponent to 0x9D minus the shift (157 - clz) and packs mantissa bits 30..8 with the exponent added in, which also restores the implicit one. Rounds to nearest-even on bit 7 with bits 6..0 as sticky. Zero returns 0. The operation matches __aeabi_i2f (mcu_0160_08001d48); this is a second copy with a different code shape, so the name avoids a clash.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | integer to convert |

**Returns** `u32`: IEEE-754 single-precision bits of (float) param_1

**Notes:** The packet's callee list names __aeabi_ui2f for this function, but the body makes no calls and is signed, so that entry is stale. The rounding path was read from the decompile only.

- Addresses by version: 12b: 0x080013EC, 143: 0x080013E4, 152: 0x080013E4, 0160: 0x080013E4
- Called by: `mcu_speed_estimate_update`, `mcu_0160_08003f2c`, `mcu_target_derate_calc`, `mcu_0160_08005830`, `mcu_gain_triple_q15_from_float`, `mcu_0160_08008f34`, `mcu_0160_08009ec4`, `mcu_0160_0800b10c`
- Calls: `__aeabi_ui2f`
- Confidence: medium

## mcu_ui2d_low_word

**Packs a 32-bit integer as a double with exponent 0x433 and returns the low word**

Calls mcu_dbl_round_pack with the integer as the mantissa, sign 0 and biased exponent 0x433 (the 2^52 frame where the low mantissa word carries the integer), and returns the low 32 bits of the packed double. The caller treats the result as a 32-bit integer. This looks like a magic-constant integer-to-double conversion whose high word is discarded.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | unsigned integer to pack |

**Returns** `u32`: low word of the packed double

**Notes:** Whether the result equals the input for every value is not established; only the packing arguments are certain. Callers mcu_0160_08003178 and mcu_0160_08004768 are outside this batch.

- Addresses by version: 12b: 0x080017F0, 143: 0x080017F0, 152: 0x080017F0, 0160: 0x0800180A
- Called by: `mcu_0160_08003178`, `mcu_0160_08004768`
- Calls: `mcu_dbl_round_pack`
- Confidence: low

## memset

**ISO C memset(s, c, n): fill n bytes with byte c and return s**

Thin wrapper that reorders its arguments into the EABI order of __aeabi_memset (mcu_0160_08001294: dest, count, value) and returns the destination pointer. Entered directly, with no visible callers in this component (only through a function pointer or the C library).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination s |
| `param_2` | `s32` | fill value c (only the low byte is used) |
| `param_3` | `u32` | byte count n |

**Returns** `ptr`: the destination pointer s

- Addresses by version: 12b: 0x080012AE, 143: 0x080012A6, 152: 0x080012A6, 0160: 0x080012A6
- Calls: `__aeabi_memset`
- Confidence: high
