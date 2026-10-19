# MCU - `libc` functions

17 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`__ARM_scalbn`](#__arm_scalbn) | 0x080017DC | Soft-float scale: add an integer to the exponent of a double (ldexp style) |
| [`__ARM_scalbnf`](#__arm_scalbnf) | 0x080013CC | Soft-float scale: add an integer to the exponent of a float (ldexpf style) |
| [`__aeabi_ddiv`](#__aeabi_ddiv) | 0x080016FE | Soft-float IEEE-754 double precision divide (no FPU) |
| [`__aeabi_f2d`](#__aeabi_f2d) | 0x080018BC | Soft-float widen single-precision float to double-precision (r0:r1 pair) |
| [`__aeabi_f2iz`](#__aeabi_f2iz) | 0x08001824 | Soft-float convert single-precision float to signed int, truncating toward zero |
| [`__aeabi_f2uiz`](#__aeabi_f2uiz) | 0x08001856 | Soft-float convert float magnitude to unsigned int, truncating |
| [`__aeabi_fdiv`](#__aeabi_fdiv) | 0x08001450 | Soft-float IEEE-754 single precision divide (no FPU) |
| [`__aeabi_fmul`](#__aeabi_fmul) | 0x08001368 | Soft-float IEEE-754 single precision multiply (no FPU) |
| [`__aeabi_i2f`](#__aeabi_i2f) | 0x08001D48 | Soft-float convert signed 32-bit integer to single-precision float |
| [`__aeabi_lasr`](#__aeabi_lasr) | 0x0800194A | 64-bit arithmetic shift right (lo, hi, shift) |
| [`__aeabi_llsl`](#__aeabi_llsl) | 0x0800190C | 64-bit logical shift left (lo, hi, shift) |
| [`__aeabi_llsr`](#__aeabi_llsr) | 0x0800192A | 64-bit logical shift right (lo, hi, shift) |
| [`__aeabi_memcpy`](#__aeabi_memcpy) | 0x08001270 | Forward memory copy: word-wise if both pointers 4-byte aligned, else bytewise |
| [`__aeabi_memset`](#__aeabi_memset) | 0x08001294 | Fill a byte buffer with a constant value (dest, count, value argument order) |
| [`__aeabi_ui2f`](#__aeabi_ui2f) | 0x080013F6 | Soft-float convert unsigned 32-bit integer to single-precision float |
| [`mcu_fcmp_sortkeys_a`](#mcu_fcmp_sortkeys_a) | 0x080018E4 | Soft-float compare helper: convert two float bit patterns to comparison keys |
| [`mcu_fcmp_sortkeys_b`](#mcu_fcmp_sortkeys_b) | 0x080018F8 | Soft-float compare helper (second copy): convert two float words to comparison keys |

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
- Called by: `mcu_0160_08003178`, `mcu_0160_08003f2c`, `mcu_0160_08004700`, `mcu_0160_08004768`, `mcu_0160_080049b8`, `mcu_0160_08004a0c`, `mcu_0160_08004a60`, `mcu_0160_08004e78`, `mcu_0160_080093f8`, `mcu_0160_0800b10c`
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
- Called by: `mcu_0160_08002b64`, `mcu_0160_080031cc`, `mcu_0160_08003f2c`, `mcu_0160_08005830`, `mcu_0160_08006c9c`, `mcu_0160_08006f74`, `mcu_0160_0800729c`, `mcu_0160_0800767c`, `mcu_0160_080078f0`, `mcu_0160_080082c8`, `mcu_0160_080085bc`, `mcu_0160_080093f8` ...
- Confidence: high

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
- Called by: `mcu_0160_080014cc`, `mcu_0160_080019fa`, `mcu_0160_08003178`, `mcu_0160_08003f2c`, `mcu_0160_08004700`, `mcu_0160_08004768`, `mcu_0160_080049b8`, `mcu_0160_08004a0c`, `mcu_0160_08004a60`, `mcu_0160_08004e78`, `mcu_0160_080093f8`
- Confidence: high

## __aeabi_f2d

**Soft-float widen single-precision float to double-precision (r0:r1 pair)**

Rebases the exponent by +0x380 (1023 - 127), moves the 23-bit fraction to the top of the 52-bit double fraction (>>3 into the high word, low 3 bits into the top of the low word) and keeps the sign. Zero magnitude returns 0.0. Denormals/NaN/Inf are not special-cased.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | float bits |

**Returns** `u64`: double bits (lo in r0, hi in r1)

- Addresses by version: 12b: 0x080018A2, 143: 0x080018A2, 152: 0x080018A2, 0160: 0x080018BC
- Called by: `mcu_0160_08003f2c`, `mcu_0160_08004700`, `mcu_0160_08004768`, `mcu_0160_080049b8`, `mcu_0160_08004a0c`, `mcu_0160_08004a60`, `mcu_0160_08004e78`, `mcu_0160_080093f8`, `mcu_0160_0800b10c`
- Confidence: high

## __aeabi_f2iz

**Soft-float convert single-precision float to signed int, truncating toward zero**

Extracts exponent and 24-bit significand; magnitudes below 1.0 (exponent < 0x7f) give 0, exponents below 0x97 shift the significand right (truncation), larger ones shift left (no saturation, so values >= 2^31 overflow silently). The result is negated if the sign bit of the input is set.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | float bits |

**Returns** `s32`: truncated integer

- Addresses by version: 12b: 0x0800180A, 143: 0x0800180A, 152: 0x0800180A, 0160: 0x08001824
- Called by: `mcu_0160_08002b64`, `mcu_0160_080031cc`, `mcu_0160_08003f2c`, `mcu_0160_0800480c`, `mcu_0160_08005830`, `mcu_0160_08006c9c`, `mcu_0160_08006f74`, `mcu_0160_0800729c`, `mcu_0160_0800767c`, `mcu_0160_080078f0`, `mcu_0160_080082c8`, `mcu_0160_080093f8` ...
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

## __aeabi_fdiv

**Soft-float IEEE-754 single precision divide (no FPU)**

Divides param_1 by param_2 as raw float bits. If either operand has zero magnitude the result is 0 (including division by zero, which does NOT yield infinity). Otherwise subtracts exponents, runs a 24-iteration restoring long division of the significands, computes sign as XOR, applies round-to-nearest-even from the final remainder, and returns 0 when the exponent underflows. No overflow, NaN or denormal handling.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | numerator float bits |
| `param_2` | `u32` | denominator float bits |

**Returns** `u32`: a/b as float bits

- Addresses by version: 12b: 0x08001436, 143: 0x08001436, 152: 0x08001436, 0160: 0x08001450
- Called by: `mcu_0160_080012b8`, `mcu_0160_08002b64`, `mcu_0160_0800480c`, `mcu_0160_08005830`, `mcu_0160_08006c9c`, `mcu_0160_0800763c`, `mcu_0160_0800765c`, `mcu_0160_0800767c`, `mcu_0160_080082c8`, `mcu_0160_080085bc`, `mcu_0160_080093f8`, `mcu_0160_0800a0f8` ...
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
- Called by: `mcu_0160_08002b64`, `mcu_0160_080031cc`, `mcu_0160_08004700`, `mcu_0160_08004e78`, `mcu_0160_08005830`, `mcu_0160_08006f74`, `mcu_0160_0800763c`, `mcu_0160_0800765c`, `mcu_0160_080082c8`, `mcu_0160_08008f34`, `mcu_0160_080093f8`, `mcu_0160_0800a594` ...
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
- Called by: `mcu_0160_08002b64`, `mcu_0160_08004db8`
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
- Called by: `mcu_0160_080014cc`
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
- Called by: `mcu_0160_080011ac`, `mcu_0160_080014cc`, `mcu_0160_080019fa`
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
- Called by: `mcu_0160_080011ac`, `mcu_0160_0800187e`, `mcu_0160_080019fa`
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
- Called by: `mcu_0160_08002b64`, `mcu_0160_08005edc`, `mcu_0160_0800672c`, `mcu_0160_080085bc`, `mcu_0160_08008b60`, `mcu_0160_0800b324`, `mcu_0160_0800bc70`, `mcu_0160_0800e146`
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
- Called by: `mcu_0160_080012a2`, `mcu_0160_080012a6`
- Confidence: high

## __aeabi_ui2f

**Soft-float convert unsigned 32-bit integer to single-precision float**

Normalises the integer with a CLZ shift, builds exponent 0x9d - clz (bias 127 + 30 for the position of the top bit) and the top 23 mantissa bits, then rounds to nearest-even using the dropped low bits. Returns 0 for input 0. Despite the decompiler showing a signed parameter, there is no sign handling, so it is the unsigned variant; the signed one is mcu_0160_08001d48.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | unsigned integer |

**Returns** `u32`: float bits

- Addresses by version: 12b: 0x08001410, 143: 0x080013F6, 152: 0x080013F6, 0160: 0x080013F6
- Called by: `mcu_0160_080012b8`, `mcu_0160_080013e4`, `mcu_0160_08004700`, `mcu_0160_08004db8`, `mcu_0160_08006c9c`, `mcu_0160_0800767c`, `mcu_0160_080085bc`, `mcu_0160_0800a0f8`, `mcu_0160_0800a594`
- Confidence: high

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
