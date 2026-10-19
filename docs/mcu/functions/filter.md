# MCU - `filter` functions

2 functions.

| Function | Address (MCU_0160) | Summary |
|---|---|---|
| [`mcu_lpf_q30_step`](#mcu_lpf_q30_step) | 0x0800721A | First-order low-pass step in Q30 (same code as mcu_lpf_q30_step_alt) |
| [`mcu_lpf_q30_step_alt`](#mcu_lpf_q30_step_alt) | 0x08007078 | First-order low-pass step in Q30: state = (a*x + (2^30 - a)*state) >> 30 |

## mcu_lpf_q30_step

**First-order low-pass step in Q30 (same code as mcu_lpf_q30_step_alt)**

Same operation as mcu_lpf_q30_step_alt (mcu_0160_08007078): state = (a*x + (2^30 - a)*state) >> 30, with the input through param_1, the state through param_2 and the Q30 coefficient in param_3. This copy has about ten callers, the most widely used copy in this build. Callers include mcu_0160_08004e78, mcu_0160_08005090, mcu_0160_08005b3c, mcu_0160_08006c9c, mcu_0160_080070ac, mcu_0160_0800772c, mcu_0160_0800a320, mcu_0160_0800a644, mcu_12b_08005b60 and mcu_143_0800a580.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | input sample, s32 |
| `param_2` | `ptr` | state, s32, updated in place |
| `param_3` | `u32` | coefficient a in Q30 |

- Addresses by version: 12b: 0x0800735C, 143: 0x08007242, 152: 0x08007272, 0160: 0x0800721A
- Called by: `mcu_0160_08004e78`, `mcu_0160_08005090`, `mcu_0160_08005b3c`, `mcu_0160_08006c9c`, `mcu_0160_080070ac`, `mcu_0160_0800772c`, `mcu_0160_0800a320`, `mcu_0160_0800a644`
- Confidence: high

## mcu_lpf_q30_step_alt

**First-order low-pass step in Q30: state = (a*x + (2^30 - a)*state) >> 30**

Reads the input sample through param_1 and the state through param_2, with the coefficient a in Q30 (0x40000000 = 1.0) as param_3. It computes the 64-bit sum a*x + (2^30 - a)*state, including the sign corrections for a negative state and for a above 1.0, shifts it right by 30 and writes it back as the new state. This is an exponential moving average whose coefficient sets the time constant. The body is identical to mcu_lpf_q30_step (mcu_0160_0800721a), so the two are probably two copies of one helper in this build. Called from mcu_0160_08002e9c, mcu_0160_08007160 and mcu_12b_08003010.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | input sample, s32 |
| `param_2` | `ptr` | state, s32, updated in place |
| `param_3` | `u32` | coefficient a in Q30 |

- Addresses by version: 12b: 0x080071CC, 143: 0x080070A0, 152: 0x080070D0, 0160: 0x08007078
- Called by: `mcu_0160_08002e9c`, `mcu_0160_08007160`
- Confidence: high
