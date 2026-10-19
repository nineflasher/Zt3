# MCU - `foc` functions

5 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_clarke_alpha_beta_step`](#mcu_clarke_alpha_beta_step) | 0x08006334 | Store the previous +0x20 sample at +0x18 and compute beta = (ia + 2*ib) / sqrt(3) in Q15 |
| [`mcu_inv_park_transform`](#mcu_inv_park_transform) | 0x080063C0 | Inverse Park transform: (d, q) to (alpha, beta) using the Q15 sin/cos at +0x34/+0x38 |
| [`mcu_math_cos_q15`](#mcu_math_cos_q15) | 0x08001B14 | Fixed-point cosine: Q15 radians in, Q15 result (sin(x+pi/2)) |
| [`mcu_math_sin_q15`](#mcu_math_sin_q15) | 0x08001C54 | Fixed-point sine: Q15 radians in, Q15 result via 513-entry table with interpolation |
| [`mcu_park_transform_deadband`](#mcu_park_transform_deadband) | 0x0800635E | Park transform of (alpha, beta) with Q15 sin/cos at +0x34/+0x38 and a dead-band on d and q |

## mcu_clarke_alpha_beta_step

**Store the previous +0x20 sample at +0x18 and compute beta = (ia + 2*ib) / sqrt(3) in Q15**

Copies the sample at +0x20 into +0x18, a one-sample delay of the first component. It then computes beta = (value at +0x20 + 2 * value at +0x24) * 0x49E6 / 2^15 and writes it to +0x1C. The constant 0x49E6 / 2^15 = 0.5773 is 1/sqrt(3) in Q15. This matches the Clarke transform beta term for phase currents ia = +0x20 and ib = +0x24, though the field roles are inferred from the arithmetic. Always returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object with ia (+0x20), ib (+0x24), delayed alpha (+0x18), beta (+0x1C), s32 |

**Returns** `bool`: always 1

- Addresses by version: 12b: 0x080063AC, 143: 0x08006264, 152: 0x08006294, 0160: 0x08006334
- Called by: `mcu_0160_08007364`
- Confidence: medium

## mcu_inv_park_transform

**Inverse Park transform: (d, q) to (alpha, beta) using the Q15 sin/cos at +0x34/+0x38**

Reads d from word 0 and q from word 1 of the int block, and sin from word 13 (+0x34) and cos from word 14 (+0x38), all Q15. Writes alpha = d*cos - q*sin to word 2 (+0x08) and beta = q*cos + d*sin to word 3 (+0x0C), each product shifted right by 15 after a 64-bit multiply. This is the inverse of mcu_park_transform_deadband. Called from mcu_0160_08007364. Always returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | int block: d, q in; alpha, beta out; sin at +0x34, cos at +0x38 |

**Returns** `bool`: always 1

- Addresses by version: 12b: 0x08006438, 143: 0x080062F0, 152: 0x08006320, 0160: 0x080063C0
- Called by: `mcu_0160_08007364`
- Confidence: high

## mcu_math_cos_q15

**Fixed-point cosine: Q15 radians in, Q15 result (sin(x+pi/2))**

Same algorithm as mcu_0160_08001c54 (sine), but 0x40000000 (pi/2 in the Q31-of-pi phase) is added to the phase first, so it returns cos(x). The input angle is multiplied by 0x517cc1b7 (1/pi in Q32) to get a phase where 2^31 = pi, quadrant-folded, then the top 10 bits index a 513-entry sine table at 0x0800ec20 (step pi/1024) and a second-order interpolation sin(a+d) ~ sin(a) + d*(cos(a) - d*sin(a)/2) is applied using table[i] and table[512-i]. The result is negated for the lower half-plane and rounded to Q15 (+/-32768 = +/-1.0). Only caller: mcu_0160_08006402, probably the Park/inverse-Park transform.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | angle in Q15 radians (pi = 102944) |

**Returns** `s32`: cos in Q15

**Notes:** Input/output Q-format inferred from the 1/pi constant and final >>16; table contents not dumped here.

- Addresses by version: 12b: 0x08001AF8, 143: 0x08001AF8, 152: 0x08001AF8, 0160: 0x08001B14
- Called by: `mcu_0160_08006402`
- Confidence: medium

## mcu_math_sin_q15

**Fixed-point sine: Q15 radians in, Q15 result via 513-entry table with interpolation**

Multiplies the input by 0x517cc1b7 (1/pi, Q32) and keeps bits 16..47 to get a phase where 2^31 = pi. Bit 30 folds the second quadrant (0x80000000 - phase), bit 31 selects the sign. The top 10 bits of the 31-bit magnitude index the table at 0x0800ec20 (sin(i*pi/1024)); with the fractional angle d = low bits * pi/1024 it evaluates sin(a) + d*(cos(a) - d*sin(a)/2) using table[i] and table[512-i], negates for the sign and rounds to Q15. When the table index is 0 it uses sin(x)~x: (x<<1)*0xc90fcd37 >> 47. Single caller mcu_0160_08006402; companion of mcu_0160_08001b14 (cos).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | angle in Q15 radians (pi = 102944) |

**Returns** `s32`: sin in Q15 (+/-32768 = +/-1.0)

**Notes:** Input scale deduced from the 1/pi constant: the angle may be a Q15 radian value; the table is not decoded here.

- Addresses by version: 12b: 0x08001C38, 143: 0x08001C38, 152: 0x08001C38, 0160: 0x08001C54
- Called by: `mcu_0160_08006402`
- Confidence: medium

## mcu_park_transform_deadband

**Park transform of (alpha, beta) with Q15 sin/cos at +0x34/+0x38 and a dead-band on d and q**

Reads alpha at +0x18, beta at +0x1C, sin at +0x34 and cos at +0x38, all Q15. Computes d = alpha*cos + beta*sin into +0x10 and q = beta*cos - alpha*sin into +0x14, each product taken as a 64-bit value shifted right by 15. Any component whose absolute value is below the threshold param_2 is then forced to zero, which suppresses small values near zero. Called from mcu_0160_08007364.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | object: alpha, beta, sin, cos in, d, q out |
| `param_2` | `s32` | dead-band threshold, same units as d and q |

**Returns** `bool`: always 1

**Notes:** Park sign convention is the standard one; the field names are inferred.

- Addresses by version: 12b: 0x080063D6, 143: 0x0800628E, 152: 0x080062BE, 0160: 0x0800635E
- Called by: `mcu_0160_08007364`
- Confidence: high
