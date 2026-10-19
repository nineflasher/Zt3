# BLE - `libc` functions

85 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`__aeabi_cdcmple`](#__aeabi_cdcmple) | 0x0C06FC90 | Double compare helper that sets the flags for __aeabi_dcmplt (calls __cmpdf2) |
| [`__aeabi_d2f`](#__aeabi_d2f) | 0x0C06FD80 | Convert double to single-precision float (round to nearest-even) |
| [`__aeabi_d2iz`](#__aeabi_d2iz) | 0x0C06FD30 | Convert double to signed 32-bit integer, truncating toward zero with saturation |
| [`__aeabi_dadd`](#__aeabi_dadd) | 0x0C06F464 | Soft-float IEEE-754 double-precision addition |
| [`__aeabi_dcmplt`](#__aeabi_dcmplt) | 0x0C06FCB4 | Return whether the preceding double compare left carry clear (a < b) |
| [`__aeabi_ddiv`](#__aeabi_ddiv) | 0x0C06FA24 | Soft-float IEEE double divide (__aeabi_ddiv) |
| [`__aeabi_ddiv_special_case`](#__aeabi_ddiv_special_case) | 0x0C06FB92 | Special-case path of __aeabi_ddiv: signed zero, infinity, NaN or a normalised operand |
| [`__aeabi_dmul`](#__aeabi_dmul) | 0x0C06F7D0 | Soft-float IEEE double multiply (__aeabi_dmul) |
| [`__aeabi_dmul_special_case`](#__aeabi_dmul_special_case) | 0x0C06F9AC | Slow path of double multiply: NaN/Inf/zero/denormal operand handling |
| [`__aeabi_dsub`](#__aeabi_dsub) | 0x0C06F460 | Double-precision subtraction entry: negate the second operand and fall into __aeabi_dadd |
| [`__aeabi_f2d`](#__aeabi_f2d) | 0x0C06F720 | Convert a soft-float single to double (__aeabi_f2d) |
| [`__cmpdf2`](#__cmpdf2) | 0x0C06FC04 | Soft-float double compare returning -1/0/1 (1 if unordered) |
| [`__divdi3`](#__divdi3) | 0x0C06FE20 | Signed 64-bit division (__divdi3) with saturation on a zero divisor |
| [`__env_lock`](#__env_lock) | 0x0C073774 | newlib __env_lock: take the recursive lock protecting environ |
| [`__env_unlock`](#__env_unlock) | 0x0C073780 | newlib __env_unlock: release the recursive lock protecting environ |
| [`__errno`](#__errno) | 0x0C0701F8 | newlib __errno: return pointer to the errno variable |
| [`__get_current_locale`](#__get_current_locale) | 0x0C0724B0 | Return pointer to the default locale object in flash |
| [`__locale_charset`](#__locale_charset) | 0x0C071C38 | newlib __locale_charset: pointer to the current locale charset string |
| [`__locale_msgcharset`](#__locale_msgcharset) | 0x0C071C44 | newlib __locale_msgcharset: pointer to the message charset string |
| [`__retarget_lock_acquire_recursive`](#__retarget_lock_acquire_recursive) | 0x0C0724BC | newlib lock acquire stub (no-op) |
| [`__retarget_lock_init_recursive`](#__retarget_lock_init_recursive) | 0x0C0724B8 | newlib lock init stub (no-op) |
| [`__retarget_lock_release_recursive`](#__retarget_lock_release_recursive) | 0x0C0724C0 | newlib lock release stub (no-op) |
| [`__sccl`](#__sccl) | 0x0C073504 | newlib __sccl: build scanf %[...] set table |
| [`__sfp_lock_acquire`](#__sfp_lock_acquire) | 0x0C072100 | newlib __sfp_lock_acquire: take the recursive lock guarding the FILE pool |
| [`__sfp_lock_release`](#__sfp_lock_release) | 0x0C07210C | newlib __sfp_lock_release: release the recursive lock guarding the FILE pool |
| [`__sinit_lock_acquire`](#__sinit_lock_acquire) | 0x0C072118 | newlib __sinit_lock_acquire: take the recursive lock around stdio initialisation |
| [`__sread`](#__sread) | 0x0C071670 | newlib __sread: read through the FILE descriptor and update its offset or error flag |
| [`__ssvfiscanf_r`](#__ssvfiscanf_r) | 0x0C0728B0 | newlib-nano string-only integer vfscanf core: parse a format and dispatch each conversion |
| [`__swhatbuf_r`](#__swhatbuf_r) | 0x0C07390C | newlib __swhatbuf_r: decide stdio buffer size and whether a FILE could be a tty |
| [`__tzcalc_limits`](#__tzcalc_limits) | 0x0C071AE4 | newlib __tzcalc_limits: compute DST/STD transition times of a year into the tzinfo rules |
| [`__udivdi3`](#__udivdi3) | 0x0C06FEC0 | Unsigned 64-bit division (__udivdi3) returning all ones on a zero divisor |
| [`__udivmoddi4`](#__udivmoddi4) | 0x0C06FEF0 | Unsigned 64-by-64 bit divide returning quotient and storing remainder |
| [`__unorddf2`](#__unorddf2) | 0x0C06FD04 | Return 1 if either double operand is NaN |
| [`_close`](#_close) | 0x0C0484B4 | newlib _close syscall: no-op for fds 0..2, driver close handler for fds 3..48 |
| [`_findenv_r`](#_findenv_r) | 0x0C072404 | newlib _findenv_r: look up NAME in environ, return pointer to its value and its index |
| [`_fstat`](#_fstat) | 0x0C035FE8 | newlib stub fstat reporting every descriptor as a character device |
| [`_fstat_r`](#_fstat_r) | 0x0C073A8C | newlib _fstat_r: call _fstat and copy a non-zero errno into the reent on failure |
| [`_getpid_r`](#_getpid_r) | 0x0C073A88 | newlib _getpid_r thunk: branch to the stub at 0x0c035ff4 that always returns pid 1 |
| [`_isatty`](#_isatty) | 0x0C035FF4 | newlib stub isatty that always reports a terminal |
| [`_isatty_r`](#_isatty_r) | 0x0C073AB0 | newlib _isatty_r: call _isatty and copy a non-zero errno into the reent on failure |
| [`_kill`](#_kill) | 0x0C036010 | newlib _kill stub: set errno to EINVAL and return -1 |
| [`_printf_common`](#_printf_common) | 0x0C072E5C | newlib-nano _printf_common: emit sign/prefix/padding for one printf conversion |
| [`_printf_i`](#_printf_i) | 0x0C072F3C | newlib-nano _printf_i: format one integer/char/string/%n conversion and emit it |
| [`_read`](#_read) | 0x0C048420 | newlib _read syscall: stdin from the console device, fds 3..48 via the /dev driver table |
| [`_read_r`](#_read_r) | 0x0C0734E0 | newlib _read_r: call _read and copy a non-zero errno into the reent on failure |
| [`_scanf_chars`](#_scanf_chars) | 0x0C073188 | newlib-nano _scanf_chars: scanf %c / %s / %[ conversion |
| [`_scanf_i`](#_scanf_i) | 0x0C07323C | newlib-nano _scanf_i: read an integer field for vfscanf and convert it with _strtol_r/_strtoul_r |
| [`_strtoul_r`](#_strtoul_r) | 0x0C071A48 | newlib _strtoul_r: reentrant string-to-unsigned-long with base 0/8/10/16 autodetect and ERANGE |
| [`_write`](#_write) | 0x0C04846C | newlib _write syscall: stdout/stderr to the console with CRLF translation, fds 3..48 via driver table |
| [`atol`](#atol) | 0x0C0701E0 | Parse a base-10 integer from a string, saturating and setting ERANGE on overflow |
| [`clock_gettime`](#clock_gettime) | 0x0C03FEAC | POSIX clock_gettime built on the FreeRTOS tick: CLOCK_MONOTONIC (4) raw, CLOCK_REALTIME (1) plus epoch offset |
| [`clock_settime`](#clock_settime) | 0x0C03FF68 | POSIX clock_settime: accept CLOCK_REALTIME only and store the epoch offset |
| [`console_getc`](#console_getc) | 0x0C035CB8 | Blocking read of one console byte; retries on zero-length reads, -1 on error |
| [`console_isatty_fd`](#console_isatty_fd) | 0x0C035FF8 | Report whether fd 0..2 is the console; otherwise set errno EBADF and return 0 |
| [`console_putc`](#console_putc) | 0x0C035CE8 | Write one raw byte to the console device without newline translation |
| [`console_write_crlf`](#console_write_crlf) | 0x0C035528 | Write a buffer to the console converting each LF to CRLF; return bytes consumed |
| [`crt_eh_get_entry_offset`](#crt_eh_get_entry_offset) | 0x0C0739F4 | C++/EH runtime helper: resolve an offset word stored before an address |
| [`div`](#div) | 0x0C072058 | newlib div: signed division returning quotient and remainder |
| [`gettimeofday`](#gettimeofday) | 0x0C0400CC | POSIX gettimeofday from the FreeRTOS tick plus the real-time epoch offset |
| [`libc_is_minus_or_plus_sign`](#libc_is_minus_or_plus_sign) | 0x0C070250 | Test whether a string is NULL, starts with '-', or (if allowed) starts with '+' |
| [`libc_reverse_u32_array`](#libc_reverse_u32_array) | 0x0C07022C | Reverse the order of n 32-bit words in an array in place |
| [`libc_state_block_load`](#libc_state_block_load) | 0x0C070268 | Copy seven global words into a caller-provided 28-byte block |
| [`libc_state_block_store`](#libc_state_block_store) | 0x0C0702B0 | Write a 28-byte block of seven words into the matching globals |
| [`libc_tm_normalize`](#libc_tm_normalize) | 0x0C070A1C | Normalise a struct tm in place, carrying or borrowing from seconds up to years |
| [`memchr`](#memchr) | 0x0C0739D8 | newlib memchr: find a byte in a buffer |
| [`memcmp`](#memcmp) | 0x0C07099C | newlib memcmp: compare n bytes of two buffers |
| [`memcpy`](#memcpy) | 0x0C0709BC | newlib memcpy: forward byte copy |
| [`memcpy_newlib_aligned_16`](#memcpy_newlib_aligned_16) | 0x0C03A80C | newlib memcpy: copy param_3 bytes from param_2 to param_1 |
| [`memmove`](#memmove) | 0x0C0709D6 | newlib memmove: overlap-safe byte copy |
| [`memset`](#memset) | 0x0C070A0A | newlib memset: fill n bytes with a byte value |
| [`raise`](#raise) | 0x0C073A54 | newlib raise(sig) with _raise_r inlined: run the installed handler or fall back to _kill |
| [`read`](#read) | 0x0C071ABC | newlib read(fd, buf, cnt): call _read_r with the global reentrancy structure |
| [`sqrtf`](#sqrtf) | 0x0C06F450 | Single-precision square root (VSQRT.F32) |
| [`std`](#std) | 0x0C072080 | newlib findfp.c std(): initialise a FILE as stdin/stdout/stderr with the __s* cookie functions |
| [`strcat`](#strcat) | 0x0C0716FA | newlib strcat: append a string to another |
| [`strchr`](#strchr) | 0x0C071718 | newlib strchr: find a character in a string |
| [`strcmp`](#strcmp) | 0x0C071732 | newlib strcmp: compare two NUL-terminated strings |
| [`strcpy`](#strcpy) | 0x0C071746 | newlib strcpy: copy a string including its NUL |
| [`strlen`](#strlen) | 0x0C071756 | newlib strlen: length of a NUL-terminated string |
| [`strncmp`](#strncmp) | 0x0C071766 | newlib strncmp: compare at most n characters of two strings |
| [`strtoul`](#strtoul) | 0x0C071A4C | newlib strtoul: convert string to unsigned long |
| [`trace_fmt_signed`](#trace_fmt_signed) | 0x0C0357B8 | Format a signed decimal integer with sign, width and zero-padding flags |
| [`trace_fmt_unsigned`](#trace_fmt_unsigned) | 0x0C0356DC | Format an unsigned integer in a base with minimum digits, field width and pad flags |
| [`w_sqrtf`](#w_sqrtf) | 0x0C06F288 | Single-precision square root wrapper that sets errno to EDOM for negative input |
| [`write`](#write) | 0x0C071AD0 | newlib write(fd, buf, cnt) with _write_r inlined: call _write and copy errno into the reent |

## __aeabi_cdcmple

**Double compare helper that sets the flags for __aeabi_dcmplt (calls __cmpdf2)**

Calls the soft-float compare __cmpdf2 (0x0C06FC04) for its side effect and returns its first argument unchanged. The comparison result reaches the caller through the carry flag, which the decompiler does not model, so the flag effect is inferred from the call pattern. Group: soft-float compare helpers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | passed through unchanged |

**Returns** `u32`: param_1

**Notes:** The name follows the libgcc __aeabi_cdcmple convention. The carry-flag mapping is inferred because the flags are invisible in the decompile.

- Addresses by version: 219: 0x0C06FC90
- Called by: `__aeabi_dcmplt`
- Calls: `__cmpdf2`
- Confidence: low

## __aeabi_d2f

**Convert double to single-precision float (round to nearest-even)**

Soft-float narrowing conversion. Detects Inf/NaN (returns 0x7fc00000 quiet NaN or signed infinity 0x7f800000), flushes to signed zero when the value is far below the float denormal range, builds denormals by shifting the mantissa with a sticky bit, otherwise re-biases the exponent and packs sign/exponent/mantissa with round-to-nearest-even (clearing the LSB on an exact tie). Callers: 0c035900, 0c059b60.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | double low word |
| `param_2` | `u32` | double high word |

**Returns** `u32`: IEEE-754 single bit pattern

- Addresses by version: 219: 0x0C06FD80
- Called by: `ble_219_0c035900`, `ble_rssi_filter_update`
- Confidence: high

## __aeabi_d2iz

**Convert double to signed 32-bit integer, truncating toward zero with saturation**

Soft-float double to int conversion. Values with magnitude below 1 return 0, NaN returns 0, and overflow/infinity saturate to 0x7fffffff (positive) or 0x80000000 (negative). Otherwise the 53-bit mantissa is shifted right by (0x3e1 - exponent field adjust) and negated for negative input. Called from 0c059b60.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | double low word |
| `param_2` | `u32` | double high word |

**Returns** `s32`: truncated integer

- Addresses by version: 219: 0x0C06FD30
- Called by: `ble_rssi_filter_update`
- Confidence: high

## __aeabi_dadd

**Soft-float IEEE-754 double-precision addition**

ARM runtime (libgcc/RVCT style) double add working on register pairs. Handles NaN, infinity and zero cases, aligns the smaller operand by the exponent difference (returning the larger one outright when the difference exceeds 0x36), negates operands according to sign, adds the 53-bit mantissas with carry, normalises using LZCOUNT and rounds to nearest-even, with overflow to infinity (0x7ff00000) and denormal handling. Called from 0c059b60, 0c06f2cc and 0c06f720.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | a low word |
| `param_2` | `u32` | a high word |
| `param_3` | `u32` | b low word |
| `param_4` | `u32` | b high word |

**Returns** `u64`: a + b as IEEE-754 double

- Addresses by version: 219: 0x0C06F464
- Called by: `ble_rssi_filter_update`, `ble_219_0c06f2cc`, `__aeabi_f2d`
- Confidence: high

## __aeabi_dcmplt

**Return whether the preceding double compare left carry clear (a < b)**

Calls the flag-setting compare helper (0x0C06FC90) and returns the inverted carry flag. The libgcc convention for __aeabi_dcmplt is that carry clear means the first operand is less than the second, which is what this returns. The operands are passed in r0..r3 and are not visible as parameters. Group: soft-float compare helpers.

**Returns** `bool`: true when a < b

**Notes:** Operands are in r0..r3 (the decompiler shows none). The result depends on the carry set by 0x0C06FC90, which the decompile does not show.

- Addresses by version: 219: 0x0C06FCB4
- Called by: `ble_219_0c06f220`
- Calls: `__aeabi_cdcmple`
- Confidence: low

## __aeabi_ddiv

**Soft-float IEEE double divide (__aeabi_ddiv)**

Divides the double (param_1, param_2) by (param_3, param_4). Zero, infinity, NaN and subnormal operands go through __aeabi_ddiv_special_case (0x0C06FB92). Normal operands use restoring long division that produces the quotient mantissa four bits per pass, then rebias the exponent, normalise, round and clamp overflow and underflow as __aeabi_dmul does. Group: soft-float and libgcc arithmetic.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | a, low word |
| `param_2` | `u32` | a, high word |
| `param_3` | `u32` | b (divisor), low word |
| `param_4` | `u32` | b (divisor), high word |

**Returns** `u64`: quotient bit pattern

**Notes:** The packet's callee list includes __aeabi_dmul (0x0C06F7D0), but no call to it appears in this body; the call list may be imprecise.

- Addresses by version: 219: 0x0C06FA24
- Called by: `ble_219_0c06f220`, `ble_219_0c06f2cc`
- Calls: `__aeabi_dmul`, `__aeabi_ddiv_special_case`
- Confidence: high

## __aeabi_ddiv_special_case

**Special-case path of __aeabi_ddiv: signed zero, infinity, NaN or a normalised operand**

Dual-purpose helper for non-normal operands. For zero, infinity or NaN combinations it returns a signed zero, a signed infinity or the quiet NaN 0x7FF8000000000000 as the 64-bit result. For a finite non-zero subnormal operand it shifts the mantissa left until the hidden bit is set and returns the normalised operand words in r2, r3 and r12, which the caller reads as extra results so the division can continue. Group: soft-float and libgcc arithmetic.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | a, low word |
| `param_2` | `u32` | a, high word |
| `param_3` | `u32` | b, low word |
| `param_4` | `u32` | b, high word |

**Returns** `u64`: special result, or the normalised operand (with extra registers r2, r3, r12)

**Notes:** The extra outputs in r2, r3 and r12 are visible only in the caller's decompile (0x0C06FA24 reads them).

- Addresses by version: 219: 0x0C06FB92
- Called by: `__aeabi_ddiv`
- Calls: `__aeabi_dmul_special_case`
- Confidence: medium

## __aeabi_dmul

**Soft-float IEEE double multiply (__aeabi_dmul)**

Multiplies two doubles given as (lo, hi) argument words. Zero, infinity, NaN and subnormal operands go through __aeabi_dmul_special_case (0x0C06F9AC). Normal operands have their 53-bit mantissas multiplied with 32x32-bit partial products, the exponents are summed and rebiased, and the product is normalised, rounded and clamped to infinity on overflow or to subnormal/zero on underflow. Group: soft-float and libgcc arithmetic.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | a, low word |
| `param_2` | `u32` | a, high word |
| `param_3` | `u32` | b, low word |
| `param_4` | `u32` | b, high word |

**Returns** `u64`: product bit pattern

**Notes:** Callers include the division special-case and dispatch paths (not all in this packet).

- Addresses by version: 219: 0x0C06F7D0
- Called by: `ble_rssi_filter_update`, `ble_219_0c06f2cc`, `__aeabi_ddiv`
- Calls: `__aeabi_dmul_special_case`
- Confidence: high

## __aeabi_dmul_special_case

**Slow path of double multiply: NaN/Inf/zero/denormal operand handling**

Not a standalone function: it is the out-of-line tail of the soft-float double multiply (called from 0c06f7d0 and 0c06fb92), which relies on registers set by its caller (unaffected r4/r12 hold exponent flags). If an operand is Inf/NaN it returns a quiet NaN (OR 0x7ff80000_00000000) or infinity with the XOR of the signs (invalid Inf*0 gives NaN); if an operand is zero it returns a signed zero; for denormal inputs it normalises the mantissa by shifting left until bit 20 of the high word is set.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | a low word |
| `param_2` | `u32` | a high word |
| `param_3` | `u32` | b low word |
| `param_4` | `u32` | b high word |

**Returns** `u64`: special-case result or normalised first operand

**Notes:** Decompiler shows register-passed state (unaff_r4/in_r12); exact handling of the continuation cannot be read from C.

- Addresses by version: 219: 0x0C06F9AC
- Called by: `__aeabi_dmul`, `__aeabi_ddiv_special_case`
- Confidence: medium

## __aeabi_dsub

**Double-precision subtraction entry: negate the second operand and fall into __aeabi_dadd**

Single instruction that flips the sign bit of the high word of the second operand (EOR with 0x80000000) and then falls through into __aeabi_dadd at 0x0c06f464. The decompiler merged the two routines, so the body shown here is actually the whole dadd implementation after the sign flip (a - b = a + (-b)). Called from 0c06f2cc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | a low word |
| `param_2` | `u32` | a high word |
| `param_3` | `u32` | b low word |
| `param_4` | `u32` | b high word |

**Returns** `u64`: a - b as IEEE-754 double (low word in r0, high in r1)

- Addresses by version: 219: 0x0C06F460
- Called by: `ble_219_0c06f2cc`
- Confidence: high

## __aeabi_f2d

**Convert a soft-float single to double (__aeabi_f2d)**

Expands the IEEE-754 single whose bit pattern is param_1 into a double: the sign goes to bit 63, the exponent is rebiased by 896 (xor with 0x3800000000000000), and the mantissa sits in the upper 52 bits with the low word equal to param_1 << 29. Zero, subnormal (normalised with LZCOUNT), infinity and NaN inputs take separate paths. Group: soft-float and libgcc arithmetic.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | single-precision bit pattern |

**Returns** `u64`: double-precision bit pattern

**Notes:** The packet's callee list shows __aeabi_dadd, but no call to it appears in the decompiled body; the arithmetic is the single-to-double expansion.

- Addresses by version: 219: 0x0C06F720
- Called by: `ble_rssi_filter_update`
- Calls: `__aeabi_dadd`
- Confidence: high

## __cmpdf2

**Soft-float double compare returning -1/0/1 (1 if unordered)**

Compares two IEEE-754 doubles given as register pairs. If either is NaN (exponent all ones with non-zero mantissa) it returns 1. Treats +0 and -0 as equal and returns 0 for equal values; otherwise returns -1 or 1 according to sign-magnitude ordering (the result is (sign mask) | 1). Called by the wrapper at 0c06fc90.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | a low word |
| `param_2` | `u32` | a high word |
| `param_3` | `u32` | b low word |
| `param_4` | `u32` | b high word |

**Returns** `s32`: -1 if a<b, 0 if equal, 1 if a>b or unordered

- Addresses by version: 219: 0x0C06FC04
- Called by: `__aeabi_cdcmple`
- Confidence: medium

## __divdi3

**Signed 64-bit division (__divdi3) with saturation on a zero divisor**

Divides the signed 64-bit dividend (param_1, param_2) by (param_3, param_4). A zero divisor returns INT64_MIN for a negative dividend, INT64_MAX for a positive non-zero dividend, and 0 for zero. Otherwise it divides the absolute values with __udivmoddi4 (0x0C06FEF0), keeps the remainder in a local, and negates the quotient when exactly one operand is negative. Group: soft-float and libgcc arithmetic.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | dividend, low word |
| `param_2` | `s32` | dividend, high word |
| `param_3` | `u32` | divisor, low word |
| `param_4` | `s32` | divisor, high word |

**Returns** `s64`: quotient

**Notes:** Unsigned counterpart is ble_219_0c06fec0 (__udivdi3). The divisor-zero saturation is a custom choice in this build, not standard libgcc behaviour.

- Addresses by version: 219: 0x0C06FE20
- Called by: `ble_219_0c047588`, `ble_219_0c0707e8`
- Calls: `__udivdi3`, `__udivmoddi4`
- Confidence: high

## __env_lock

**newlib __env_lock: take the recursive lock protecting environ**

Calls __retarget_lock_acquire_recursive on __lock___env_recursive_mutex, the 1-byte dummy lock object at 0x2001953c (envlock.c). The lock is a no-op stub in this firmware. Used by _findenv_r (ble_219_0c072404) and the setenv/unsetenv family; released by __env_unlock (ble_219_0c073780).

- Addresses by version: 219: 0x0C073774
- Called by: `_findenv_r`
- Calls: `__retarget_lock_acquire_recursive`
- Confidence: high

## __env_unlock

**newlib __env_unlock: release the recursive lock protecting environ**

Calls __retarget_lock_release_recursive on __lock___env_recursive_mutex at 0x2001953c, the counterpart of __env_lock (ble_219_0c073774). Called on both exit paths of _findenv_r (ble_219_0c072404).

- Addresses by version: 219: 0x0C073780
- Called by: `_findenv_r`
- Calls: `__retarget_lock_release_recursive`
- Confidence: high

## __errno

**newlib __errno: return pointer to the errno variable**

Returns the 32-bit value stored in the RAM pointer cell DAT_200049a8, which holds the address of the errno variable (the neighbouring word 0x200049ac is the errno storage whose address is taken elsewhere). Library code such as strtoul writes error codes through this pointer (e.g. ERANGE = 0x22). Called from many libc routines and from application code that needs to set or read errno.

**Returns** `ptr`: pointer to the errno int

**Notes:** Name chosen from usage (errno pointer used by strtoul); in newlib the symbol is __errno().

- Addresses by version: 219: 0x0C0701F8
- Called by: `console_isatty_fd`, `_kill`, `clock_settime`, `ble_219_0c046e04`, `ble_219_0c0482e4`, `ble_219_0c048380`, `_read`, `_write`, `_close`, `ble_219_0c04885c`, `ble_219_0c06f220`, `w_sqrtf` ...
- Confidence: medium

## __get_current_locale

**Return pointer to the default locale object in flash**

Returns the constant address 0x0c073ce0, the read-only default (C) locale structure in the image. Callers (0x0c070bcc, 0x0c071ae4, 0x0c071c50) use it to read locale fields such as numeric/ctype parameters.

**Returns** `ptr`: pointer to locale struct at 0x0c073ce0

**Notes:** Name inferred from newlib; contents of the target not decoded.

- Addresses by version: 219: 0x0C0724B0
- Called by: `ble_219_0c070bcc`, `__tzcalc_limits`, `ble_219_0c071c50`
- Confidence: low

## __locale_charset

**newlib __locale_charset: pointer to the current locale charset string**

Returns the constant RAM address 0x2001953f without dereferencing it; this is the character-set name buffer of the (C) locale object used by multibyte/ctype conversions. Only caller is the libc routine at 0x0c070bcc.

**Returns** `ptr`: pointer to charset name string in RAM

**Notes:** Identification as __locale_charset is inferred from the two sibling accessors returning the same address; may instead be a different locale field.

- Addresses by version: 219: 0x0C071C38
- Called by: `ble_219_0c070bcc`
- Confidence: low

## __locale_msgcharset

**newlib __locale_msgcharset: pointer to the message charset string**

Identical in behaviour to the neighbouring accessor at 0x0c071c38: returns the fixed RAM address 0x2001953f (locale string buffer). Only caller is 0x0c070bcc. In newlib the message charset accessor exists beside __locale_charset, which is why it is named this way.

**Returns** `ptr`: pointer to charset name string in RAM

**Notes:** Duplicate of 0x0c071c38 in this build; name inferred.

- Addresses by version: 219: 0x0C071C44
- Called by: `ble_219_0c070bcc`
- Confidence: low

## __retarget_lock_acquire_recursive

**newlib lock acquire stub (no-op)**

Empty function. Called at entry of stdio routines (fflush/vfprintf/vfscanf-like) paired with the release stub at 0x0c0724c0; locking is disabled so it does nothing.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | lock object (ignored) |

- Addresses by version: 219: 0x0C0724BC
- Called by: `__sfp_lock_acquire`, `__sinit_lock_acquire`, `ble_219_0c0722c0`, `ble_219_0c07239c`, `ble_219_0c072bfc`, `ble_219_0c073450`, `__env_lock`, `ble_219_0c073894`
- Confidence: medium

## __retarget_lock_init_recursive

**newlib lock init stub (no-op)**

Empty function (single return). In this single-threaded libc configuration the retargetable lock initialiser does nothing. Its only caller is 0x0c0721a0 (stdio initialisation), consistent with a lock-init hook.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | lock object (ignored) |

**Notes:** Identification as lock-init inferred from caller context; could be __sinit_lock-style hook.

- Addresses by version: 219: 0x0C0724B8
- Called by: `ble_219_0c0721a0`
- Confidence: low

## __retarget_lock_release_recursive

**newlib lock release stub (no-op)**

Empty function paired with the acquire stub at 0x0c0724bc; called on exit paths of the same stdio routines. Does nothing.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | lock object (ignored) |

- Addresses by version: 219: 0x0C0724C0
- Called by: `__sfp_lock_release`, `ble_219_0c072130`, `ble_219_0c0722c0`, `ble_219_0c07239c`, `ble_219_0c072bfc`, `ble_219_0c073450`, `__env_unlock`, `ble_219_0c073894`
- Confidence: medium

## __sccl

**newlib __sccl: build scanf %[...] set table**

Builds a 256-entry byte table at param_1 for a scanf scanset. A leading '^' inverts the set: all entries are first filled with 1 (inverted) or 0, then members listed are set to the opposite value. Handles ranges 'a-z' (a '-' before ']' or a descending range is literal) and stops at the closing ']' or NUL. Returns a pointer to the format character after the ']' (or the NUL if the set is unterminated).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | 256-byte table to fill |
| `param_2` | `ptr` | format string just after '%[' |

**Returns** `ptr`: pointer past the closing ']'

- Addresses by version: 219: 0x0C073504
- Called by: `__ssvfiscanf_r`, `_scanf_i`
- Confidence: high

## __sfp_lock_acquire

**newlib __sfp_lock_acquire: take the recursive lock guarding the FILE pool**

Calls __retarget_lock_acquire_recursive on the 1-byte dummy lock object __lock___sfp_recursive_mutex at 0x2001953d (newlib lock.c declares these as 'struct __lock { char dummy; }'); the retargeted lock is a no-op in this firmware. Paired with __sfp_lock_release (ble_219_0c07210c). Both are used by __sfp (ble_219_0c0721a0) when allocating a FILE from the glue list.

- Addresses by version: 219: 0x0C072100
- Called by: `ble_219_0c0721a0`
- Calls: `__retarget_lock_acquire_recursive`
- Confidence: high

## __sfp_lock_release

**newlib __sfp_lock_release: release the recursive lock guarding the FILE pool**

Calls __retarget_lock_release_recursive on __lock___sfp_recursive_mutex at 0x2001953d, the counterpart of __sfp_lock_acquire (ble_219_0c072100). The lock stubs are no-ops here. Called from __sfp (ble_219_0c0721a0).

- Addresses by version: 219: 0x0C07210C
- Called by: `ble_219_0c0721a0`
- Calls: `__retarget_lock_release_recursive`
- Confidence: high

## __sinit_lock_acquire

**newlib __sinit_lock_acquire: take the recursive lock around stdio initialisation**

Calls __retarget_lock_acquire_recursive on __lock___sinit_recursive_mutex, the 1-byte lock object at 0x2001953e (the neighbour of the __sfp lock at 0x2001953d and the env lock at 0x2001953c). Used by __sinit (ble_219_0c072130) before it initialises stdin/stdout/stderr via std(). No-op lock in this firmware.

- Addresses by version: 219: 0x0C072118
- Called by: `ble_219_0c072130`
- Calls: `__retarget_lock_acquire_recursive`
- Confidence: high

## __sread

**newlib __sread: read through the FILE descriptor and update its offset or error flag**

Stdio read callback: calls _read_r (0x0C0734E0) with the FILE's descriptor (short at +0x0E). On a negative result it clears bit 0x1000 (__SOFF, offset valid) in the FILE flags at +0x0C; on success it adds the byte count to the stream offset at +0x54. The buffer and count arguments of the original newlib function are not visible in this decompile.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | struct _reent |
| `param_2` | `ptr` | FILE stream (cookie) |

**Notes:** Same logic as newlib sread.c. Called through the FILE read hook; no direct callers in the packet.

- Addresses by version: 219: 0x0C071670
- Calls: `_read_r`
- Confidence: high

## __ssvfiscanf_r

**newlib-nano string-only integer vfscanf core: parse a format and dispatch each conversion**

The nano vfscanf.c engine built with STRING_ONLY and INTEGER_ONLY, used by sscanf/siscanf (caller ble_219_0c071618). Builds a struct _scan_data_t on the stack (flags, base, width, nassigned, nread, ccltab pointer to a 256-byte set table, conversion code) with pfn_ungetc = _sungetc_r (LAB_0c0727fc) and pfn_refill = __ssrefill_r (0x0c072877). Walks the format: whitespace in the format skips input whitespace (ctype table DAT_0c0862a9 bit 3), literal characters must match, '%' starts a conversion: optional '*' (SUPPRESS 0x10), decimal width, a size modifier from "hlL" found with memchr, then the conversion letter selects the code: %[ (builds the set with __sccl, NOSKIP 0x40, CT_CCL 1), %c (CT_CHAR 0, NOSKIP), %s (CT_STRING 2), %d/%u (base 10, CT_INT 3 / CT_UINT 4), %i (base 0), %o (base 8), %x/%X/%p (base 16, flag 0x200 PFXOK, %p adds POINTER 0x20), %e/%f/%g (CT_FLOAT 5, skipped by the integer-only build), %n (stores nread as int or short). Leading input whitespace is skipped unless NOSKIP; then _scanf_chars (FUN_0c073188) or _scanf_i (ble_219_0c07323c) consumes the field. A conversion returning 1 ends the scan; 2 means input failure, giving EOF (-1) if nothing was assigned yet or if fp->_flags has __SERR (0x40).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | struct _reent * |
| `param_2` | `ptr` | FILE * (string FILE: _p at [0], _r at [1], _flags at offset 0xc) |
| `param_3` | `ptr` | format string |
| `param_4` | `ptr` | va_list of output pointers |

**Returns** `s32`: number of assigned conversions, or -1 (EOF) on input failure before any assignment

- Addresses by version: 219: 0x0C0728B0
- Called by: `ble_219_0c071618`
- Calls: `_scanf_chars`, `_scanf_i`, `__sccl`, `memchr`
- Confidence: high

## __swhatbuf_r

**newlib __swhatbuf_r: decide stdio buffer size and whether a FILE could be a tty**

newlib makebuf.c helper. If fp->_file (short at offset 0xe) is negative or _fstat_r (ble_219_0c073a8c) on it fails, *couldbetty = 0 and the buffer size is 64 (0x40) when fp->_flags (offset 0xc) has bit 7 (0x80, __SMBF) set, else 1024 (0x400, BUFSIZ). Otherwise *couldbetty = S_ISCHR(st.st_mode) ((st_mode & 0xf000) == 0x2000, st_mode being the word at offset 4 of the stack struct stat) and the size is 1024. Always returns 0 (the nano build drops the __SOPT/__SNPT seek-optimisation result). Called by __smakebuf_r (ble_219_0c073958).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | struct _reent * |
| `param_2` | `ptr` | FILE * |
| `param_3` | `ptr` | size_t *bufsize out |
| `param_4` | `ptr` | int *couldbetty out (1 if character device) |

**Returns** `u32`: always 0

**Notes:** Which flag bit selects the 64-byte size (0x80 = __SMBF in newlib's flag layout) was taken from the code, not verified against the exact newlib revision.

- Addresses by version: 219: 0x0C07390C
- Called by: `ble_219_0c073958`
- Calls: `_fstat_r`
- Confidence: high

## __tzcalc_limits

**newlib __tzcalc_limits: compute DST/STD transition times of a year into the tzinfo rules**

newlib tzcalc_limits.c. Obtains the __tzinfo_type via __gettzinfo (FUN_0c0724b0); returns 0 if year < 1970 (0x7b2). Otherwise stores __tzyear and computes year_days = days from the epoch to 1 Jan of the year (365*years plus Gregorian leap corrections /4, /100, /400). For each of the two __tzrule entries (40 bytes each: ch, m, n, d, s, change(64-bit), offset) it converts the rule to a day number: 'J' = Julian day ignoring Feb 29 (adds 1 for leap years when d >= 60), 'D' = zero-based day, otherwise the 'M' month/week/day form using the __month_lengths[2][12] table (Ghidra shows it as a bogus offset into the string "btapp_btle_connect_status_change") and the weekday of 1 Jan ((year_days + 4) % 7). change = days * 86400 (0x15180) + s + offset, stored as a 64-bit time_t. Finally __tznorth = (rule[0].change < rule[1].change) and returns 1. Called from the tzset path (ble_219_0c070bcc) and localtime/mktime (ble_219_0c071c50).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | calendar year (e.g. 2024) |

**Returns** `u32`: 1 on success, 0 if year is before 1970

- Addresses by version: 219: 0x0C071AE4
- Called by: `ble_219_0c070bcc`, `ble_219_0c071c50`
- Calls: `__get_current_locale`
- Confidence: high

## __udivdi3

**Unsigned 64-bit division (__udivdi3) returning all ones on a zero divisor**

Divides the unsigned (param_1, param_2) by (param_3, param_4). A zero divisor returns UINT64_MAX when the dividend is non-zero and 0 when it is zero. Otherwise it calls __udivmoddi4 (0x0C06FEF0) for the quotient. Group: soft-float and libgcc arithmetic.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | dividend, low word |
| `param_2` | `u32` | dividend, high word |
| `param_3` | `u32` | divisor, low word |
| `param_4` | `u32` | divisor, high word |

**Returns** `u64`: quotient

**Notes:** The decompile shows the __udivmoddi4 call without its remainder pointer argument.

- Addresses by version: 219: 0x0C06FEC0
- Called by: `bes_clk_measure_hz`, `ble_rf_synth_retune`, `ble_rf_synth_set_freq_ratio`, `ble_analog_chip_init`, `ble_219_0c044b14`, `hal_time_ms`, `ble_219_0c062fe4`, `__divdi3`
- Calls: `__udivmoddi4`
- Confidence: high

## __udivmoddi4

**Unsigned 64-by-64 bit divide returning quotient and storing remainder**

Software long division used by __aeabi_uldivmod style wrappers (callers 0c06fe20 and 0c06fec0). The dividend is param_2:param_1, the divisor param_4:param_3. For a 32-bit divisor it normalises with LZCOUNT and does two 16-bit-digit steps with correction (the classic Knuth/ARM scheme); a zero divisor raises an undefined-instruction trap (software_udf 0xff). For a 64-bit divisor it estimates the quotient from the top word, multiplies back and corrects by one. If param_5 is non-NULL the 64-bit remainder is written to param_5[0..1].

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | dividend low |
| `param_2` | `u32` | dividend high |
| `param_3` | `u32` | divisor low |
| `param_4` | `u32` | divisor high |
| `param_5` | `ptr` | out: 64-bit remainder, or NULL |

**Returns** `u64`: quotient

- Addresses by version: 219: 0x0C06FEF0
- Called by: `__divdi3`, `__udivdi3`
- Confidence: high

## __unorddf2

**Return 1 if either double operand is NaN**

Checks whether the exponent (bits 62..52 after sign removal) of either operand is 0x7ff with a non-zero mantissa. Returns 1 when at least one is NaN (unordered) and 0 otherwise. Called by 0c06f220.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | a low word |
| `param_2` | `u32` | a high word |
| `param_3` | `u32` | b low word |
| `param_4` | `u32` | b high word |

**Returns** `u32`: 1 if unordered, else 0

- Addresses by version: 219: 0x0C06FD04
- Called by: `ble_219_0c06f220`
- Confidence: high

## _close

**newlib _close syscall: no-op for fds 0..2, driver close handler for fds 3..48**

Returns 0 immediately for fd < 3. For fd 3..48 it fetches DAT_2000f6d8[fd-3] (open-file object), its ops table (first word) and tail-calls the close handler at ops+0xC with the fd. If the slot, ops or handler is NULL, errno is set to 9 (EBADF) via __errno and -1 is returned. Has many callers throughout the app (e.g. ble_219_0c02c49c factory-test command handler, 0c02d4f8 ...), which close /dev device descriptors opened with ble_219_0c04855c. Part of the fd layer with _read, _write, open and select.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | file descriptor |

**Returns** `s32`: 0, driver close result, or -1 with errno EBADF

- Addresses by version: 219: 0x0C0484B4
- Called by: `ble_219_0c02c49c`, `ble_219_0c02d4f8`, `app_gpio_dev_ioctl`, `ble_219_0c02d604`, `nvdata_ioctl_cmd_0x200`, `nvdata_ioctl_get_buf_0x102`, `nvdata_ioctl_cmd_0x104`, `nvdata_ioctl_unlock_0x103`, `nvdata_ioctl_lock_0x106`, `ble_219_0c02d870`, `ble_219_0c02dc50`, `ble_219_0c02dea8` ...
- Calls: `__errno`
- Confidence: high

## _findenv_r

**newlib _findenv_r: look up NAME in environ, return pointer to its value and its index**

newlib getenv_r.c. Takes the environment lock (__env_lock, ble_219_0c073774), then, if environ (DAT_20003e94, the pointer array `*p_environ`) is non-NULL, measures the name up to the first '=' or NUL and scans each environment entry with strncmp(entry, name, len); the first entry whose character after len is '=' matches: *offset (param_3) receives the entry index (pointer difference >> 2), the lock is released (__env_unlock, ble_219_0c073780) and a pointer to the value text after '=' is returned. Returns 0 (after unlocking) when the name is not found or environ is NULL. Callers are _getenv_r (ble_219_0c0723ec) and _setenv_r/_unsetenv_r (ble_219_0c07247c).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | struct _reent * (passed to the lock helpers) |
| `param_2` | `ptr` | variable name; a trailing '=...' is ignored |
| `param_3` | `ptr` | int *offset: receives index of the matching environ entry |

**Returns** `ptr`: pointer to the value string after '=' or NULL

- Addresses by version: 219: 0x0C072404
- Called by: `ble_219_0c0723ec`, `ble_219_0c07247c`
- Calls: `strncmp`, `__env_lock`, `__env_unlock`
- Confidence: high

## _fstat

**newlib stub fstat reporting every descriptor as a character device**

Sets st->st_mode (offset 4 of the stat struct in param_2) to 0x2000 (S_IFCHR) and returns 0. Part of the newlib syscall stubs for the retargeted stdio; referenced from an indirect table at 0x0c073a8c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | file descriptor (ignored) |
| `param_2` | `ptr` | struct stat to fill |

**Returns** `s32`: always 0

- Addresses by version: 219: 0x0C035FE8
- Called by: `_fstat_r`
- Confidence: high

## _fstat_r

**newlib _fstat_r: call _fstat and copy a non-zero errno into the reent on failure**

newlib reent/fstatr.c. Clears the global errno DAT_20019540, calls the platform _fstat (FUN_0c035fe8, which reports every descriptor as a character device) with (fd, struct stat *), and if the result is -1 and errno is non-zero stores it in ptr->_errno. Called by __swhatbuf_r (ble_219_0c07390c) to classify stdio descriptors. The result is returned in r0 (decompiler shows void).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | struct _reent * |
| `param_2` | `s32` | file descriptor |
| `param_3` | `ptr` | struct stat * output |
| `param_4` | `u32` | unused (decompiler artefact) |

- Addresses by version: 219: 0x0C073A8C
- Called by: `__swhatbuf_r`
- Calls: `_fstat`
- Confidence: high

## _getpid_r

**newlib _getpid_r thunk: branch to the stub at 0x0c035ff4 that always returns pid 1**

Single-instruction tail-call to FUN_0c035ff4, a 'return 1' stub shared (by identical-code folding) with the stub the packet calls _isatty. In raise/_raise_r (ble_219_0c073a54) its result is used as the process id handed to _kill, so this entry is newlib's _getpid_r(struct _reent *) with the errno bookkeeping optimised away. Always yields 1.

**Returns** `u32`: always 1

**Notes:** The target 0x0c035ff4 was earlier described as _isatty; both _getpid and _isatty are 'movs r0,#1; bx lr' stubs in BES syscalls so the two names may have been folded onto one address.

- Addresses by version: 219: 0x0C073A88
- Called by: `raise`
- Calls: `_isatty`
- Confidence: medium

## _isatty

**newlib stub isatty that always reports a terminal**

Ignores its arguments and returns 1, so stdio treats all file descriptors as interactive (line buffered). Referenced from the syscall table around 0x0c073a88.

**Returns** `s32`: always 1

- Addresses by version: 219: 0x0C035FF4
- Called by: `_getpid_r`
- Confidence: high

## _isatty_r

**newlib _isatty_r: call _isatty and copy a non-zero errno into the reent on failure**

newlib reent/isattyr.c. Clears the global errno DAT_20019540, calls the platform _isatty (FUN_0c035ff8) with the descriptor, and if it returned -1 with errno set stores errno in ptr->_errno. Called by __smakebuf_r (ble_219_0c073958) as _isatty_r(ptr, fp->_file) to decide whether a possible-tty stream should be line buffered (__SLBF). Result returned in r0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | struct _reent * |
| `param_2` | `s32` | file descriptor |

**Notes:** Identified from its caller __smakebuf_r; FUN_0c035ff8 is therefore the real BES _isatty stub (the packet's earlier _isatty label at 0x0c035ff4 is probably _getpid).

- Addresses by version: 219: 0x0C073AB0
- Called by: `ble_219_0c073958`
- Calls: `console_isatty_fd`
- Confidence: medium

## _kill

**newlib _kill stub: set errno to EINVAL and return -1**

Ignores its arguments, sets errno to 0x16 (EINVAL) through __errno (0x0C0701F8) and returns -1, so no signal is ever delivered. It is the fallback called by raise (0x0C073A54) when no handler is installed.

**Returns** `s32`: always -1

- Addresses by version: 219: 0x0C036010
- Called by: `raise`
- Calls: `__errno`
- Confidence: medium

## _printf_common

**newlib-nano _printf_common: emit sign/prefix/padding for one printf conversion**

Part of the nano vfprintf: given the conversion state struct (param_2: flags at +0, dprec at +8, width at +0xC, size/precision at +0x10, 16-blank pad string at +0x19, zero pad string at +0x1A, sign char at +0x43, 'x' marker at +0x45) it computes the real output size (max of precision/size, +1 if a sign char, +2 for the 0x prefix when the alt flag 0x20 is set) and stores it in *param_3. If neither left-justify nor zero-pad flags (mask 6) are set it emits width-size leading blanks, then the sign/'0x' prefix, then zero padding when the zero-pad flag is set or precision exceeds the size. Output is done by calling the callback param_5(reent, fp, buf, len) (a __sfputs-style writer); any callback result of -1 aborts with -1, otherwise returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | reent/context passed to the callback |
| `param_2` | `ptr` | printf conversion state (_prt_data_t) |
| `param_3` | `ptr` | out: computed field size (realsz) |
| `param_4` | `ptr` | FILE/stream passed to the callback |
| `param_5` | `ptr` | output callback (ctx, fp, buf, len) returning -1 on error |

**Returns** `s32`: 0 on success, -1 on output error

**Notes:** Struct field layout matches newlib nano _prt_data_t; offsets read directly from code.

- Addresses by version: 219: 0x0C072E5C
- Called by: `_printf_i`
- Confidence: medium

## _printf_i

**newlib-nano _printf_i: format one integer/char/string/%n conversion and emit it**

nano-vfprintf_i.c. Given the per-conversion struct _prt_data_t (param_2: flags[0], prec[1], dprec[2], width[3], size[4], ret[5], code byte at 0x18, blank char at 0x19, buffer ending at 0x43, l_buf sign/prefix bytes at 0x42..0x45) and the va_list pointer param_5 it handles the conversion character: 'c' stores the char; 'd'/'i' fetch an int (short-cast when flags has 0x40), negate negatives and set the '-' sign byte; 'o'/'u' fetch unsigned (16-bit when flags has 0x40 and not 0x80), base 8 or 10; 'x'/'X'/'p' fetch unsigned, select the lower/upper hex digit table, write the 'x'/'X' prefix byte, and set the 0x20 (HEXPREFIX) flag when ALT (bit 0) is set and the value is non-zero ('p' forces 0x20); 's' takes a char pointer and limits its length to prec via memchr; 'n' writes the running count ret into an int or short. Numbers are converted right-to-left into the buffer with repeated division by the base, an octal ALT adds a leading '0'; size = digit count and a negative prec clears ZEROPAD (bit 2). It then calls _printf_common (FUN_0c072e5c) to emit sign, prefix and left padding, calls the output function param_4(reent, fp, buf, size), emits width - printed blanks when LADJUST (bit 1) is set, and returns max(width, printed) or -1 on write error. Callers: _vfiprintf_r / _svfiprintf_r (ble_219_0c0725fc, ble_219_0c072bfc).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | struct _reent * |
| `param_2` | `ptr` | struct _prt_data_t * with flags/prec/width/size and conversion buffer |
| `param_3` | `ptr` | FILE * (or string sink) passed to the output function |
| `param_4` | `ptr` | int (*pfunc)(reent, fp, buf, len) output callback |
| `param_5` | `ptr` | va_list * advanced by the consumed argument |

**Returns** `s32`: characters emitted for this conversion, -1 on output error

- Addresses by version: 219: 0x0C072F3C
- Called by: `ble_219_0c0725fc`, `ble_219_0c072bfc`
- Calls: `_printf_common`, `memchr`
- Confidence: high

## _read

**newlib _read syscall: stdin from the console device, fds 3..48 via the /dev driver table**

fd 0 is redirected to read() (ble_219_0c071abc) on the console device descriptor DAT_2000b520. fd 1 and 2 set errno (via __errno, i.e. the reent at DAT_200049a8) to 5 (EIO) and return -1. fds 3..48 index the 46-entry file table DAT_2000f6d8[fd-3]; each slot points to an open-file object whose first word is the driver ops table, and the read handler at ops+4 is tail-called with (fd, buf, len). An empty slot, missing ops or missing handler sets errno 9 (EBADF) and returns -1. Called from _read_r (ble_219_0c0734e0), which copies errno into the reent on failure. Forms the fd layer together with _write (ble_219_0c04846c), _close (ble_219_0c0484b4), open (ble_219_0c04855c, '/dev/' names) and select (ble_219_0c04885c).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | file descriptor |
| `param_2` | `ptr` | destination buffer |
| `param_3` | `u32` | bytes to read |

**Returns** `s32`: bytes read from the driver, or -1 with errno EIO/EBADF

- Addresses by version: 219: 0x0C048420
- Called by: `_read_r`
- Calls: `__errno`, `read`
- Confidence: high

## _read_r

**newlib _read_r: call _read and copy a non-zero errno into the reent on failure**

newlib reent/readr.c. Clears the global errno DAT_20019540, calls the platform _read (FUN_0c048420) with (fd, buf, cnt), and if it returned -1 and errno is now non-zero stores errno in ptr->_errno (first word of the struct _reent param_1). Called by __sread (0x0c071670, the stdio read cookie installed by std()) and by read (ble_219_0c071abc). Returns the _read result in r0 (decompiler shows void).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | struct _reent * |
| `param_2` | `s32` | file descriptor |
| `param_3` | `ptr` | destination buffer |
| `param_4` | `u32` | byte count |

- Addresses by version: 219: 0x0C0734E0
- Called by: `__sread`, `read`
- Calls: `_read`
- Confidence: high

## _scanf_chars

**newlib-nano _scanf_chars: scanf %c / %s / %[ conversion**

Reads characters from the stream pointed to by param_3 (ptr/remaining count pair, refilled through the function pointer at param_2[0x60] when the count runs out). Conversion type in param_2[6]: 0 = %c, 1 = %[ (scanset table at param_2[5], 256 flags), 2 = %s (stops at whitespace using the ctype table 0x0c0862a9 bit 8). Default width is 1 for %c else unlimited; stores characters to the va_list pointer taken from param_4 unless the suppress flag (0x10) is set, decrementing width as it goes. On finish it NUL-terminates for non-%c types, increments the assignment count (param_2[3]) when not suppressed and adds the character count to param_2[4]. Returns 1 when no character could be read at all, else 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | reent/context passed to refill |
| `param_2` | `ptr` | scan state struct (_scan_data_t) |
| `param_3` | `ptr` | stream cursor {ptr, remaining} |
| `param_4` | `ptr` | pointer to va_list of destination pointers |

**Returns** `s32`: 0 ok, 1 if input failure before any char

- Addresses by version: 219: 0x0C073188
- Called by: `__ssvfiscanf_r`
- Confidence: medium

## _scanf_i

**newlib-nano _scanf_i: read an integer field for vfscanf and convert it with _strtol_r/_strtoul_r**

nano-vfscanf_i.c. Chooses the conversion function: _strtol_r (0x0c07194c) when pdata->code == CT_INT (3), otherwise _strtoul_r (ble_219_0c071a48 at 0x0c071a49). Width is clamped to 349 (0x15d = BUF-1, excess width is remembered to be re-added for skipped leading zeros). Sets the SIGNOK|NDIGITS|NZDIGITS style flags (0xd00) and scans the optional prefixes using memchr on the three strings "+-", "0" and "xX": a leading '0' with no base selects base 8 and flag 0x200, a following 'x'/'X' switches to base 16 (flag 0x100); each accepted prefix byte is copied into pdata->buf (param_2[7]) and the input FILE (_p at param_3[0], _r at param_3[1]) is advanced, refilling through pfn_refill (param_2[0x60]) when it runs dry. With base defaulting to 10 it builds the digit set with __sccl from "A-Fa-f8901234567]" + (10 - base) into the ccltab and copies matching digits while skipping redundant leading zeros. If only a bare prefix was consumed it is pushed back with pfn_ungetc (param_2[0x5f]) and 1 (match failure) is returned. Unless SUPPRESS (0x10) is set the buffer is NUL-terminated, converted with the chosen function (base param_2[1]), stored into the next va_list pointer as int/short/long (flags 0x01 / 0x20) and nassigned incremented. nread is updated with the consumed length; returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | struct _reent * |
| `param_2` | `ptr` | struct _scan_data_t * (flags, base, width, nassigned, nread, ccltab, code, buf[350], pfn_ungetc, pfn_refill) |
| `param_3` | `ptr` | FILE * being read |
| `param_4` | `ptr` | va_list * of output pointers |

**Returns** `u32`: 0 = field consumed, 1 = matching failure (only a prefix was read)

- Addresses by version: 219: 0x0C07323C
- Called by: `__ssvfiscanf_r`
- Calls: `__sccl`, `memchr`
- Confidence: high

## _strtoul_r

**newlib _strtoul_r: reentrant string-to-unsigned-long with base 0/8/10/16 autodetect and ERANGE**

Reentrant entry of newlib's strtoul (the family heading is a 1-instruction entry; the decompiled body is the shared strtoul code it branches into). Skips leading whitespace using the ctype table at DAT_0c0862a9 (bit 3 = space), accepts an optional '-'/'+', then resolves the base: 0 -> 10 unless the text starts with '0' (8) or '0x'/'0X' (16); base 16 also tolerates a '0x' prefix. Accumulates digits (0-9, A-Z, a-z) below the base with the classic cutoff/cutlim overflow test (0xffffffff / base). On overflow sets reent->_errno = 0x22 (ERANGE) and returns 0xffffffff, otherwise returns the (possibly negated) value. If endptr (param_3) is non-NULL it is set to the first unparsed character, or to the original string when no digits were consumed. This is the conversion function _scanf_i (ble_219_0c07323c) calls at 0x0c071a49 for %u/%o/%x; _strtol_r lives at 0x0c07194c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | struct _reent *; _errno is written on overflow |
| `param_2` | `ptr` | nptr: NUL-terminated string to parse |
| `param_3` | `ptr` | endptr: receives pointer to first unparsed char (may be NULL) |
| `param_4` | `u32` | base, 0 = autodetect, 2..36 |

**Returns** `u32`: converted value, 0xffffffff (ULONG_MAX) with errno=ERANGE on overflow

**Notes:** The entry is listed as 1 instruction with callee 'strtoul'; the reentrant signature (reent, nptr, endptr, base) and its use from _scanf_i at 0x0c071a49 identify it as _strtoul_r. The name/body split between strtoul and _strtoul_r in this image is slightly uncertain.

- Addresses by version: 219: 0x0C071A48
- Calls: `strtoul`
- Confidence: medium

## _write

**newlib _write syscall: stdout/stderr to the console with CRLF translation, fds 3..48 via driver table**

fd 1 and 2 go to ble_219_0c035528(buf, len), which splits the buffer at '\n' and writes each line plus "\r\n" to the console device DAT_2000b520 through write (ble_219_0c071ad0); its result is ignored and the requested length is returned. fds 3..48 look up DAT_2000f6d8[fd-3] -> open-file object -> ops table and tail-call the write handler at ops+8 with (fd, buf, len). Anything else (fd 0, empty slot, no handler) sets errno 9 (EBADF) and returns -1. Called from write()/ _write_r (ble_219_0c071ad0). Part of the /dev fd layer with _read, _close, open and select.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | file descriptor |
| `param_2` | `ptr` | source buffer |
| `param_3` | `u32` | bytes to write |

**Returns** `s32`: len for fd 1/2, driver result for fds >= 3, -1 with errno EBADF

- Addresses by version: 219: 0x0C04846C
- Called by: `write`
- Calls: `console_write_crlf`, `__errno`
- Confidence: high

## atol

**Parse a base-10 integer from a string, saturating and setting ERANGE on overflow**

Skips leading whitespace (ctype bit 0x08 at 0x0C0862A9), accepts one optional '+' or '-', and reads decimal digits; a letter ends the number because only base 10 is accepted. Accumulation saturates at 0x7FFFFFFF (or 0x80000000 for a negative value), and on overflow it stores ERANGE (34) through the errno pointer at DAT_200049A8. Behaves like strtol(s, NULL, 10) on this 32-bit target.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | NUL-terminated string |

**Returns** `s32`: parsed value, saturated on overflow

**Notes:** Single-argument form, so atol or atoi; both are the same on this target. Callers 0c04855c, 0c055634, 0c05569c, 0c055b90.

- Addresses by version: 219: 0x0C0701E0
- Called by: `ble_219_0c04855c`, `ble_219_0c055634`, `ble_219_0c05569c`, `ble_219_0c055b90`
- Calls: `__errno`
- Confidence: high

## clock_gettime

**POSIX clock_gettime built on the FreeRTOS tick: CLOCK_MONOTONIC (4) raw, CLOCK_REALTIME (1) plus epoch offset**

Fills a struct timespec with 64-bit tv_sec (param_2[0] low, param_2[1] high) and 32-bit tv_nsec (param_2[2]). Inside the critical section at 0x0c03f640/0x0c03f65c it reads xTaskGetTickCount() (1 ms ticks): tv_sec = ticks/1000, tv_nsec = (ticks%1000)*1000000 + the sub-millisecond nanosecond value returned by 0x0c03f790 (hardware timer fraction). If tv_nsec exceeds 1000000000 it subtracts 1e9 (adds 0xC4653600) and carries into the 64-bit seconds. clockid 4 (newlib CLOCK_MONOTONIC) returns 0 with the monotonic value; clockid 1 (CLOCK_REALTIME) adds the 64-bit real-time offset DAT_2000C5E0/DAT_2000C5E4 (seconds since the epoch at boot, set by the time-setting routine) with carry and returns 0; any other clockid returns -1 (no errno). Caller 0x0c03ff38 prints 's.ns: %u.%u, hwclock=%u'. Same tick-to-time arithmetic as gettimeofday at 0x0c0400cc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | clockid_t: 1 = CLOCK_REALTIME, 4 = CLOCK_MONOTONIC |
| `param_2` | `ptr` | struct timespec out: s64 tv_sec, s32 tv_nsec |

**Returns** `s32`: 0 on success, -1 (0xffffffff) for an unsupported clock id

**Notes:** The overflow test uses '>' rather than '>=' 1e9. 0x0c03f790 is assumed to return the elapsed nanoseconds within the current tick.

- Addresses by version: 219: 0x0C03FEAC
- Called by: `ble_219_0c03ff38`, `clock_settime`, `ble_clock_realtime_offset_update`, `ble_event_window_expire`, `ble_219_0c058520`, `ble_link_param_monitor_step`, `ble_219_0c05a224`
- Calls: `vPortEnterCritical`, `vPortExitCritical`, `rtos_systick_sub_tick_ns`, `xTaskGetTickCount`
- Confidence: high

## clock_settime

**POSIX clock_settime: accept CLOCK_REALTIME only and store the epoch offset**

Accepts only CLOCK_REALTIME (1); any other id sets errno to EINVAL (22) through __errno and returns -1. For CLOCK_REALTIME it reads CLOCK_MONOTONIC (clock 4) through clock_gettime and computes the offset REALTIME minus MONOTONIC from the caller's timespec into the 64-bit words DAT_2000C5E0 and DAT_2000C5E4. It then reads the monotonic clock again, adds one second when its tv_nsec exceeds 500 ms and passes the 64-bit result to 0x0C03FEA8. The offset in DAT_2000C5E0 and DAT_2000C5E4 is the stored state; the final call goes to a zero-return stub with no visible effect. The function returns 0 on success.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | clock id; only CLOCK_REALTIME (1) is accepted |
| `param_2` | `ptr` | const struct timespec with the new time |

**Returns** `s32`: 0 on success, -1 with errno set to EINVAL.

**Notes:** The nanosecond borrow in the offset calculation is simplified. 0x0C03FEA8 is util_return_zero_u32 by its own annotation (medium confidence on the stub reading).

- Addresses by version: 219: 0x0C03FF68
- Calls: `util_return_zero_u32`, `clock_gettime`, `__errno`
- Confidence: medium

## console_getc

**Blocking read of one console byte; retries on zero-length reads, -1 on error**

Reads one byte from console device DAT_2000B520 through the read routine 0x0C071ABC, retrying while the read returns 0 bytes, and returns the byte value 0..255. A negative read result returns -1. There are no direct callers in the packet.

**Returns** `s32`: byte 0..255, or -1 on error

- Addresses by version: 219: 0x0C035CB8
- Calls: `read`
- Confidence: high

## console_isatty_fd

**Report whether fd 0..2 is the console; otherwise set errno EBADF and return 0**

Returns 1 for file descriptors 0, 1 and 2, which are the console. Otherwise it sets errno to 9 (EBADF) through __errno (0x0C0701F8) and returns 0. The caller is ble_219_0c073ab0 (_isatty_r). The name _isatty is already attached to 0x0C035FF4, a different return-1 stub (see the wave2_batch12 notes), so this entry uses a distinct name.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | file descriptor |

**Returns** `u32`: 1 for a console fd, 0 otherwise

**Notes:** This may be the real _isatty behind _isatty_r. Its EBADF error differs from newlib's ENOTTY.

- Addresses by version: 219: 0x0C035FF8
- Called by: `_isatty_r`
- Calls: `__errno`
- Confidence: medium

## console_putc

**Write one raw byte to the console device without newline translation**

Writes the byte param_1 to console device DAT_2000B520 through write routine 0x0C071AD0 as a one-byte write. The result is ignored. Unlike console_write_crlf it performs no LF to CRLF translation.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | byte to write |

- Addresses by version: 219: 0x0C035CE8
- Calls: `write`
- Confidence: high

## console_write_crlf

**Write a buffer to the console converting each LF to CRLF; return bytes consumed**

Writes param_2 bytes of param_1 to console device DAT_2000B520 through the device write routine 0x0C071AD0. Text between newlines goes out in one call, and each newline is written as the two bytes CR LF and counted as one input byte. It returns the number of input bytes consumed, a negative write error, or -5 when a CRLF write is short. Used by _write for fds 1 and 2 (0x0C04846C).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | input buffer |
| `param_2` | `s32` | length in bytes |

**Returns** `s32`: input bytes consumed, or a negative error

- Addresses by version: 219: 0x0C035528
- Called by: `_write`
- Calls: `write`
- Confidence: high

## crt_eh_get_entry_offset

**C++/EH runtime helper: resolve an offset word stored before an address**

Reads the word w located at param_2-4. Computes r = w - 4; if w is negative (high bit set) it adds the self-relative value stored at param_2 + r and returns the sum, otherwise returns r. This resembles resolving an ARM EHABI self-relative (prel31-like) table entry located just before a given address. Called only from 0x0c0724e8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | unused |
| `param_2` | `ptr` | address whose preceding word is decoded |

**Returns** `s32`: resolved offset/address delta

**Notes:** Purpose inferred from the arithmetic only; true routine unidentified.

- Addresses by version: 219: 0x0C0739F4
- Called by: `ble_219_0c0724e8`
- Confidence: low

## div

**newlib div: signed division returning quotient and remainder**

Computes quot = num / den and rem = num - den*quot, then normalises the C89 truncation result: if num < 0 and rem > 0 the quotient is decremented and den added to the remainder; if num >= 0 and rem < 0 the quotient is incremented and den subtracted. The pair is returned through the struct pointer in param_1 (out[0] = quot, out[1] = rem), i.e. the div_t result written via a hidden pointer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | div_t result {quot, rem} |
| `param_2` | `s32` | numerator |
| `param_3` | `s32` | denominator |

**Notes:** Called by the time/format routine at 0x0c070a1c.

- Addresses by version: 219: 0x0C072058
- Called by: `libc_tm_normalize`
- Confidence: high

## gettimeofday

**POSIX gettimeofday from the FreeRTOS tick plus the real-time epoch offset**

Returns -1 when the timeval pointer is NULL. Otherwise, inside the critical section at 0x0c03f640/0x0c03f65c, reads xTaskGetTickCount() (1 ms ticks) and stores tv_sec (64-bit: param_1[0] low, param_1[1] high) = DAT_2000C5E0:DAT_2000C5E4 (epoch offset in seconds) + ticks/1000 with carry, and tv_usec (param_1[2]) = (ticks%1000)*1000 + (sub-tick nanoseconds from 0x0c03f790)/1000. If tv_usec exceeds 1000000 it subtracts 1000000 and increments the 64-bit seconds. The timezone argument (param_2) and the remaining parameters are ignored. Always returns 0 for a non-NULL pointer. Unlike clock_gettime (0x0c03feac) the real-time offset is always applied. Called from 0x0c071a70 (newlib time glue).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | struct timeval out: s64 tv_sec, s32 tv_usec; NULL rejected |
| `param_2` | `ptr` | timezone, ignored |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | unused (passed through to 0x0c03f790 by register reuse only) |

**Returns** `s32`: 0 on success, -1 if param_1 is NULL

**Notes:** Carry test uses '>' 1000000 rather than '>='.

- Addresses by version: 219: 0x0C0400CC
- Called by: `ble_219_0c071a70`
- Calls: `vPortEnterCritical`, `vPortExitCritical`, `rtos_systick_sub_tick_ns`, `xTaskGetTickCount`
- Confidence: high

## libc_is_minus_or_plus_sign

**Test whether a string is NULL, starts with '-', or (if allowed) starts with '+'**

Returns true when the pointer is NULL or the first character is '-'. Otherwise, if param_2 is non-zero it returns whether the first character is '+'; if param_2 is zero it returns false. Used by the libc routine at 0x0c0702f8 as a sign/prefix check on a string argument.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | NUL-terminated string, may be NULL |
| `param_2` | `bool` | non-zero: also accept a leading '+' |

**Returns** `bool`: true if NULL or leading '-' (or leading '+' when allowed)

**Notes:** Purpose inferred from the single caller; semantics of the NULL case unknown.

- Addresses by version: 219: 0x0C070250
- Called by: `ble_219_0c0702f8`
- Confidence: medium

## libc_reverse_u32_array

**Reverse the order of n 32-bit words in an array in place**

Swaps word i with word n-1-i for i in 0..(n>>1)-1, walking one pointer forward from base and one backward from base+4*n. It is a plain in-place reversal of a u32 array; it has no bounds checks. Only caller is the large libc routine at 0x0c0702f8 (locale/time-style string handling), so it is probably a private helper of that routine.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | base address of the u32 array |
| `param_2` | `s32` | number of 32-bit elements |

**Notes:** Exact enclosing newlib routine unknown; helper name is descriptive.

- Addresses by version: 219: 0x0C07022C
- Called by: `ble_219_0c0702f8`
- Confidence: medium

## libc_state_block_load

**Copy seven global words into a caller-provided 28-byte block**

Reads RAM globals DAT_200194d8, DAT_200194dc, DAT_200049a0, DAT_200049a4, DAT_200194e0, DAT_200194e4 and DAT_200194d4 and stores them in this order into out[0..6]. Together with the matching store routine (0x0c0702b0) it saves/restores a 7-word libc configuration block (time-zone/locale style data). Only caller is 0x0c0707bc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination array of 7 u32 words |

**Notes:** The semantic meaning of the 7 words is not determined; likely newlib tz/locale state.

- Addresses by version: 219: 0x0C070268
- Called by: `ble_219_0c0707bc`
- Confidence: medium

## libc_state_block_store

**Write a 28-byte block of seven words into the matching globals**

Inverse of the load routine at 0x0c070268: copies in[0..6] to DAT_200194d8, DAT_200194dc, DAT_200049a0, DAT_200049a4, DAT_200194e0, DAT_200194e4 and DAT_200194d4 respectively. Called only from 0x0c0707bc, which loads the block, modifies it and stores it back.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | source array of 7 u32 words |

**Notes:** Meaning of the words unknown; see load routine.

- Addresses by version: 219: 0x0C0702B0
- Called by: `ble_219_0c0707bc`
- Confidence: medium

## libc_tm_normalize

**Normalise a struct tm in place, carrying or borrowing from seconds up to years**

Operates on six 32-bit fields (sec, min, hour, mday, mon, year, with year counted from 1900). Out-of-range values are carried into the next field using div by 60, 60, 24 and 12, month lengths from the table at 0x0C0745FC, and the Gregorian leap-year rule for February. param_2 is a signed flag: when it is negative the remainder is rebased by adding the divisor and the quotient is decremented by one, which handles borrowing from negative differences.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | six u32 fields: sec, min, hour, mday, mon, year |
| `param_2` | `s32` | borrow flag; negative selects the borrow form |

**Notes:** Probably newlib mktime's internal __adjust, but the name is not confirmed, so a module-style name is used. The division helper is 0x0C072058 (div).

- Addresses by version: 219: 0x0C070A1C
- Called by: `ble_219_0c070bcc`
- Calls: `div`
- Confidence: medium

## memchr

**newlib memchr: find a byte in a buffer**

Scans param_3 bytes from param_1 and returns a pointer to the first byte equal to param_2, or NULL if not found within the range. Used by the stdio format code.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | buffer |
| `param_2` | `u8` | byte value to find |
| `param_3` | `u32` | buffer length |

**Returns** `ptr`: pointer to match or NULL

- Addresses by version: 219: 0x0C0739D8
- Called by: `ble_219_0c0725fc`, `__ssvfiscanf_r`, `ble_219_0c072bfc`, `_printf_i`, `_scanf_i`
- Confidence: high

## memcmp

**newlib memcmp: compare n bytes of two buffers**

Byte-wise unsigned comparison of param_3 bytes at param_1 and param_2. Returns 0 if all bytes are equal, otherwise the difference of the first mismatching bytes (s1[i]-s2[i]). Used widely by the BT host (address and key comparisons).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | first buffer |
| `param_2` | `ptr` | second buffer |
| `param_3` | `u32` | number of bytes |

**Returns** `s32`: 0 if equal, else difference of first differing bytes

- Addresses by version: 219: 0x0C07099C
- Called by: `ble_219_0c029414`, `ble_219_0c029df8`, `app_sn_prefix_whitelist_match`, `ble_219_0c02b480`, `ble_219_0c02d358`, `bthost_link_key_db_tlv_delete_link_key`, `bthost_link_key_db_tlv_get_link_key`, `bthost_link_key_db_tlv_put_link_key`, `att_iterator_match_uuid16`, `att_iterator_match_uuid`, `att_server_handle_request`, `le_device_db_tlv_add` ...
- Confidence: high

## memcpy

**newlib memcpy: forward byte copy**

Copies param_3 bytes one at a time from param_2 (src) to param_1 (dest) in ascending order; no overlap handling and no return value (the standard return of dest is not used here). Heavily used throughout host and controller code.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination |
| `param_2` | `ptr` | source |
| `param_3` | `u32` | byte count |

**Notes:** Param order in decompiler is dst, src, n.

- Addresses by version: 219: 0x0C0709BC
- Called by: `ble_219_0c028570`, `ble_219_0c0285ec`, `ble_219_0c029200`, `app_adv_id_block_copy`, `ble_219_0c02973c`, `ble_219_0c0297b0`, `ble_219_0c02a8f8`, `ble_219_0c02b158`, `ble_219_0c02b264`, `ble_219_0c02b480`, `ble_219_0c02c338`, `ble_219_0c02e5a4` ...
- Confidence: high

## memcpy_newlib_aligned_16

**newlib memcpy: copy param_3 bytes from param_2 to param_1**

newlib-style optimised memcpy. For lengths below 16 or when source and destination alignments differ (low two bits of src^dst), it copies byte by byte. Otherwise it copies bytes until the destination is word-aligned, then 16 bytes per iteration as four words, then remaining whole words, then the trailing bytes. The decompiler shows no return value but newlib returns the destination pointer in r0. Caller 0x0c03cec8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination |
| `param_2` | `ptr` | source |
| `param_3` | `u32` | byte count |

**Returns** `ptr`: destination (r0 preserved by the original)

- Addresses by version: 219: 0x0C03A80C
- Called by: `bt_drv_rom_patch_apply_table`
- Confidence: high

## memmove

**newlib memmove: overlap-safe byte copy**

If src < dst < src+n (overlapping with destination above source) it copies backwards from the end; otherwise it copies forward byte by byte. Arguments are dst, src, n.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination |
| `param_2` | `ptr` | source |
| `param_3` | `u32` | byte count |

- Addresses by version: 219: 0x0C0709D6
- Called by: `ble_link_table_remove_index`, `ble_link_table_remove_key`, `ble_219_0c068da8`, `ble_219_0c072546`
- Confidence: high

## memset

**newlib memset: fill n bytes with a byte value**

Writes the low byte param_2 to each of param_3 bytes starting at param_1, ascending. No return value is used. Called from many init paths to zero structures.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination |
| `param_2` | `u8` | fill value |
| `param_3` | `u32` | byte count |

- Addresses by version: 219: 0x0C070A0A
- Called by: `ble_219_0c028570`, `ble_219_0c028c94`, `ble_219_0c02a484`, `ble_219_0c02b264`, `ble_219_0c02c124`, `crc32_compute_poly`, `ble_219_0c02d358`, `ble_219_0c03457c`, `ble_219_0c0367b4`, `ble_219_0c0369d8`, `ble_219_0c037798`, `ble_mem_fill` ...
- Confidence: high

## raise

**newlib raise(sig) with _raise_r inlined: run the installed handler or fall back to _kill**

newlib signal.c. Uses _impure_ptr (DAT_200049a8) as the reent. If sig >= 32 (NSIG) sets errno = 0x16 (EINVAL) and returns -1. Looks up reent->_sig_func (word at offset 0x44): when the table or the entry is NULL it performs _kill_r inline: clears the global errno DAT_20019540, calls _kill (FUN_0c036010) with (_getpid_r() via ble_219_0c073a88, sig) and copies a resulting errno into reent->_errno, returning _kill's result. SIG_IGN (1) returns 0; SIG_ERR (-1) sets errno = EINVAL and returns 1; any other handler is first reset to SIG_DFL (0) and then called with sig, returning 0. Called from abort()/the raise wrapper at ble_219_0c073764.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | signal number 0..31 |

**Returns** `s32`: 0 on success, -1 (EINVAL) for a bad signal, 1 for SIG_ERR, or the _kill result

- Addresses by version: 219: 0x0C073A54
- Called by: `ble_219_0c073764`
- Calls: `_kill`, `_getpid_r`
- Confidence: high

## read

**newlib read(fd, buf, cnt): call _read_r with the global reentrancy structure**

Non-reentrant POSIX read wrapper from newlib's syscalls/sysread.c: forwards (fd, buf, cnt) to _read_r (ble_219_0c0734e0) with _impure_ptr (DAT_200049a8) as the struct _reent argument. The actual transfer and errno propagation happen in _read_r / _read (FUN_0c048420). Called by many application-level functions (ble_219_0c0285ec, ble_219_0c02d358 ...) that use the libc file-descriptor interface; its sibling write() is ble_219_0c071ad0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | file descriptor |
| `param_2` | `ptr` | destination buffer |
| `param_3` | `u32` | byte count |

**Returns** `s32`: bytes read or -1 (tail-call result of _read_r)

**Notes:** Identification as read (rather than write) rests on _read_r being the routine that __sread (0x0c071670, installed by std()) also calls.

- Addresses by version: 219: 0x0C071ABC
- Called by: `ble_219_0c0285ec`, `ble_219_0c02d358`, `ble_219_0c02d784`, `ble_219_0c02dc50`, `ble_219_0c02dea8`, `ble_219_0c02e7d8`, `ble_219_0c03457c`, `console_getc`, `ble_219_0c0367b4`, `ble_219_0c036868`, `ble_219_0c037798`, `ble_219_0c041d50` ...
- Calls: `_read_r`
- Confidence: medium

## sqrtf

**Single-precision square root (VSQRT.F32)**

Two-instruction wrapper that executes the Cortex-M33 FPU vsqrt.f32 instruction on the argument and returns. Called from 0c06f288, a floating point routine in the same math cluster.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `f32` | input value |

**Returns** `f32`: square root of param_1

- Addresses by version: 219: 0x0C06F450
- Called by: `w_sqrtf`
- Confidence: high

## std

**newlib findfp.c std(): initialise a FILE as stdin/stdout/stderr with the __s* cookie functions**

Static helper of newlib's __sinit (findfp.c). Zeroes the FILE fields _p, _r, _w, _bf._base, _bf._size, _lbfsize and _flags2, sets _flags (offset 0xc) = param_2 and _file (offset 0xe) = param_3, memset()s the 8-byte _mbstate at offset 0x5c, sets _cookie = the FILE itself and installs the standard stdio I/O vector: _read = __sread (0x0c071670), _write = __swrite (0x0c071696), _seek = __sseek (0x0c0716ce), _close = __sclose (0x0c0716f2). Called three times by __sinit (ble_219_0c072130) for the stdin/stdout/stderr slots of the reent structure.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | FILE * to initialise |
| `param_2` | `u16` | _flags (__SRD for stdin, __SWR for stdout/stderr) |
| `param_3` | `u16` | _file descriptor number 0/1/2 |

- Addresses by version: 219: 0x0C072080
- Called by: `ble_219_0c072130`
- Calls: `memset`
- Confidence: high

## strcat

**newlib strcat: append a string to another**

Scans param_1 to its NUL terminator, then copies param_2 including its terminating NUL onto that position. No bounds checking. Return value is not used.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination string (must have room) |
| `param_2` | `ptr` | source string |

- Addresses by version: 219: 0x0C0716FA
- Called by: `ble_219_0c0558ec`
- Confidence: high

## strchr

**newlib strchr: find a character in a string**

Walks the string, returning a pointer to the first byte equal to param_2. If the terminating NUL is reached, it returns a pointer to the NUL when param_2 == 0, otherwise NULL.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | NUL-terminated string |
| `param_2` | `char` | character to find |

**Returns** `ptr`: pointer to match or NULL

- Addresses by version: 219: 0x0C071718
- Called by: `ble_219_0c0702f8`
- Confidence: high

## strcmp

**newlib strcmp: compare two NUL-terminated strings**

Compares byte by byte until the first mismatch or until the first string ends (a zero in string 1 stops the loop), returning s1[i] - s2[i] as unsigned byte difference. 0 means equal.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | first string |
| `param_2` | `ptr` | second string |

**Returns** `s32`: <0, 0, >0 ordering

- Addresses by version: 219: 0x0C071732
- Called by: `ble_219_0c0474b0`, `ble_219_0c0702f8`, `ble_219_0c071c50`
- Confidence: high

## strcpy

**newlib strcpy: copy a string including its NUL**

Copies bytes from param_2 to param_1 until and including the terminating NUL. The decompiled function does not return the destination pointer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | destination |
| `param_2` | `ptr` | source string |

- Addresses by version: 219: 0x0C071746
- Called by: `ble_219_0c071c50`
- Confidence: high

## strlen

**newlib strlen: length of a NUL-terminated string**

Advances through the string until a NUL byte and returns the pointer difference, i.e. the number of characters before the NUL. Called from many places (logging, name handling, command parsing).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | NUL-terminated string |

**Returns** `u32`: string length in bytes

- Addresses by version: 219: 0x0C071756
- Called by: `util_find_str_in_buf`, `ble_219_0c0474b0`, `ble_219_0c04b788`, `ble_219_0c054534`, `ble_219_0c055b90`, `ble_gatt_read_char_value`, `ble_nv_load_device_name`, `fp_read_radix`, `ble_219_0c067248`, `hci_cmd_pack_format`, `ble_219_0c0702f8`, `ble_219_0c071618` ...
- Confidence: high

## strncmp

**newlib strncmp: compare at most n characters of two strings**

Returns 0 if n == 0. Otherwise compares bytes pairwise, stopping at the first mismatch, at a NUL in string 1, or after n bytes, and returns s1[i]-s2[i] of the last examined pair.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | first string |
| `param_2` | `ptr` | second string |
| `param_3` | `u32` | maximum characters to compare |

**Returns** `s32`: <0, 0, >0 ordering

- Addresses by version: 219: 0x0C071766
- Called by: `util_find_str_in_buf`, `ble_219_0c0365a4`, `ble_219_0c04855c`, `ble_gatt_read_char_value`, `_findenv_r`
- Confidence: high

## strtoul

**newlib strtoul: convert string to unsigned long**

Skips leading whitespace using the ctype table at 0x0c0862a9 (bit 0x08 = space), accepts a '+'/'-' sign, and handles base 0 (auto-detect: 0x/0X hex, leading 0 octal, else decimal) and base 16 with optional 0x prefix. Digits 0-9, A-Z, a-z are accumulated with explicit overflow detection against 0xFFFFFFFF/base; on overflow the result is 0xFFFFFFFF and errno (via the pointer in DAT_200049a8) is set to 0x22 (ERANGE). A negative sign negates the result. If endptr (param_2) is non-NULL it receives the address of the first unconverted character (or the start of the string if no digits were consumed).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | nptr: string to parse |
| `param_2` | `ptr` | endptr: receives pointer past the number, may be NULL |
| `param_3` | `u32` | base: 0 or 2..36 |

**Returns** `u32`: parsed value, 0xFFFFFFFF on overflow

**Notes:** Also called from 0x0c071a48 wrapper (an _r/locale-less entry point).

- Addresses by version: 219: 0x0C071A4C
- Called by: `ble_219_0c0360d4`, `bt_bdaddr_from_string`, `ble_util_hex_string_to_bytes`, `_strtoul_r`, `ble_219_0c071c50`
- Confidence: high

## trace_fmt_signed

**Format a signed decimal integer with sign, width and zero-padding flags**

Formats signed decimal param_2. The digit count of the magnitude, raised to the precision param_3, gives the width. The sign is then emitted: '-' for negative values through hal_trace_buf_putc, and '+' for non-negative values when flag bit 2 is set. Padding follows the flags (bit 0 left justify, bit 1 zero pad), and the magnitude is printed through trace_fmt_unsigned (0x0C0356DC) in base 10. It returns the number of characters written or a negative error.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output context for hal_trace_buf_putc |
| `param_2` | `s32` | signed value |
| `param_3` | `u32` | minimum digit count (precision) |
| `param_4` | `u32` | field width |
| `param_5` | `u32` | flags: bit 0 left justify, bit 1 zero pad, bit 2 force plus sign |

**Returns** `u32`: characters written, or a negative error

- Addresses by version: 219: 0x0C0357B8
- Called by: `ble_219_0c035900`
- Calls: `hal_trace_buf_putc`, `trace_fmt_unsigned`
- Confidence: medium

## trace_fmt_unsigned

**Format an unsigned integer in a base with minimum digits, field width and pad flags**

Emits unsigned param_2 in base param_3 through hal_trace_buf_putc (0x0C035684). Argument param_4 is the minimum digit count, param_5 the field width, and param_6 the flags, with bit 0 for left justification and bit 1 for zero padding (space when a precision is given). It counts the digits, pads on the left to the field width, then emits the digits from the highest place value using the characters 0123456789ABCDEF. It returns the number of characters emitted or the sink's negative error. Called by trace_fmt_signed and by the trace printf path at 0x0C035900.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output context for hal_trace_buf_putc |
| `param_2` | `u32` | value |
| `param_3` | `u32` | base, 2..16 |
| `param_4` | `u32` | minimum digit count |
| `param_5` | `u32` | field width |
| `param_6` | `u32` | flags: bit 0 left justify, bit 1 zero pad |

**Returns** `s32`: characters emitted, or the sink's negative error

- Addresses by version: 219: 0x0C0356DC
- Called by: `trace_fmt_signed`, `ble_219_0c035900`
- Calls: `hal_trace_buf_putc`
- Confidence: medium

## w_sqrtf

**Single-precision square root wrapper that sets errno to EDOM for negative input**

Calls the VSQRT.F32 core at 0x0C06F450 and returns its result. If the argument is not NaN and is negative, it stores 33 (EDOM) into errno through __errno and returns the default NaN 0xFFC00000 instead. Group: soft-float and libm arithmetic.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `f32` | input |

**Returns** `f32`: square root, or -NaN with errno set to EDOM

**Notes:** Newlib-style sqrtf wrapper (w_sqrtf). The wave-1 name 'sqrtf' on 0x0C06F450 looks like the __ieee754_sqrtf core; left unchanged.

- Addresses by version: 219: 0x0C06F288
- Called by: `bt_rfcal_measure_residual_fmt14`, `bt_rfcal_measure_residual_fmt16`
- Calls: `sqrtf`, `__errno`
- Confidence: high

## write

**newlib write(fd, buf, cnt) with _write_r inlined: call _write and copy errno into the reent**

POSIX write wrapper: clears the global errno DAT_20019540, calls the low-level _write (FUN_0c04846c) with (fd, buf, cnt), and if the result is -1 and errno became non-zero copies errno into _impure_ptr->_errno (DAT_200049a8 points at the struct _reent, whose first word is _errno). This is newlib's _write_r body (reent/writer.c) merged into the non-reentrant write() entry. Called by the same application functions that call read (ble_219_0c071abc).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | file descriptor |
| `param_2` | `ptr` | source buffer |
| `param_3` | `u32` | byte count |

**Notes:** Could be another 3-argument syscall wrapper (open/lseek); write is the most consistent sibling of read. FUN_0c04846c is the BES _write syscall.

- Addresses by version: 219: 0x0C071AD0
- Called by: `ble_219_0c0285ec`, `ble_219_0c02d358`, `ble_219_0c02d870`, `ble_219_0c02db00`, `ble_219_0c02dc50`, `ble_219_0c02dea8`, `ble_219_0c02e5a4`, `ble_219_0c02e758`, `console_write_crlf`, `console_putc`, `ble_219_0c0366e4`, `ble_219_0c041dc0` ...
- Calls: `_write`
- Confidence: medium
