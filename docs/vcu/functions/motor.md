# VCU - `motor` functions

1 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`vcu_drive_command_update`](#vcu_drive_command_update) | 0x08009240 | Per-tick drive command computation: derating, mode curves, ramps and output words |

## vcu_drive_command_update

**Per-tick drive command computation: derating, mode curves, ramps and output words**

Largest routine of the drive path. It reads a 12-halfword profile for the current channel group DAT_20001fa5 and variant DAT_20001fa7 from ROM at 0x0800f10c + group*0xa8 + variant*0x18, and derives a derating factor from DAT_20001f7e minus 20 in 1/128 steps (128 is full scale, 25 in the top band, plus a 0.1 float in the last band). It computes a ceiling from DAT_20001e66/100 through util_map_range_clamp_high and steps the ramp value DAT_200013ba towards that ceiling every 501 calls. The operating mode DAT_20001b68 (1..4) selects one of four curve branches that fill the byte target DAT_2000139e, the words DAT_20001f94, DAT_20001f96 and DAT_20001f9a, the ramp steps DAT_200013b6 and DAT_200013b8, and per-group float values at 0x200013dc..0x200013f0. Afterwards it sets the period byte DAT_20001fee and the words DAT_20001fef and DAT_20001fe9 from the mode bytes, derives DAT_20001fb0 as 6000 times DAT_20001b46 (clamped to 30) when that changes, updates status bit f92[14] from the speed against DAT_20001b40, caps DAT_20001f96 with a 3000-to-6000-tick interpolation (util_interp_linear_clamp_hi), and applies the override pairs at 0x200020a4..0x200020b4 when their enable bytes are nonzero.

**Notes:** This is the least certain entry in the packet: the meaning of most output words and of the ROM profile fields is inferred. Sub-mode 3 with status bit f92[7] also runs an ASCII product-code test on 0x20001ad7..0x20001ada that sets DAT_20001fdb to 0x23 or 0x34 and DAT_20001f96 low byte to 0x8c. Verify before relying on the field names.

- Addresses by version: 148: 0x08008724, 14a: 0x08008BC8, 14b: 0x08008F98, 14e: 0x08008FFC, 14f: 0x08009058, 152: 0x0800911C, 153: 0x080091B8, 0159: 0x08009240
- Called by: `vcu_0159_080047ac`
- Calls: `__aeabi_fmul`, `__ARM_scalbnf`, `__aeabi_i2f_v148_159`, `__aeabi_ui2f`, `__aeabi_f2iz`, `__aeabi_f2uiz`, `util_interp_linear_clamp_hi`, `util_map_range_clamp_high`
- Confidence: low
