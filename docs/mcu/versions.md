# MCU version evolution

Functions are tracked across builds with Ghidra Version Tracking (see methodology).

| From | To | Added | Removed | Modified | Unchanged |
|---|---|---|---|---|---|
| MCU_12b | MCU_143 | 32 | 26 | 25 | 426 |
| MCU_143 | MCU_152 | 15 | 11 | 22 | 450 |
| MCU_152 | MCU_0160 | 9 | 5 | 6 | 476 |

## Per-function changes (newest build vs previous)

| Function | Change |
|---|---|
| `mcu_0160_0800143c` | added in MCU_0160 |
| `mcu_0160_08005edc` | modified |
| `mcu_0160_0800665c` | modified |
| `mcu_0160_0800672c` | modified |
| `mcu_0160_08007df4` | added in MCU_0160 |
| `mcu_0160_080085bc` | modified |
| `mcu_0160_08008a14` | modified |
| `mcu_0160_0800b10c` | modified |
| `mcu_0160_0800d674` | added in MCU_0160 |
| `mcu_0160_0800d934` | added in MCU_0160 |
| `mcu_0160_0800d9a8` | added in MCU_0160 |
| `mcu_152_08002a4e` | removed in MCU_0160 |
| `mcu_152_08006a7c` | removed in MCU_0160 |
| `mcu_ctx_get_field_0x90` | removed in MCU_0160 |
| `mcu_get_word_at_0x90` | added in MCU_0160 |
| `mcu_read_le32` | added in MCU_0160 |
| `mcu_state_reset_load_key16` | added in MCU_0160 |
| `mcu_tea_decrypt_block` | removed in MCU_0160 |
| `mcu_timeout_tick_v152` | removed in MCU_0160 |
| `mcu_write_le32` | added in MCU_0160 |
