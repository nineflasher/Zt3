# VCU version evolution

Functions are tracked across builds with Ghidra Version Tracking (see methodology).

| From | To | Added | Removed | Modified | Unchanged |
|---|---|---|---|---|---|
| VCU_148 | VCU_14a | 7 | 6 | 37 | 368 |
| VCU_14a | VCU_14b | 16 | 7 | 26 | 379 |
| VCU_14b | VCU_14e | 0 | 0 | 11 | 410 |
| VCU_14e | VCU_14f | 1 | 0 | 5 | 416 |
| VCU_14f | VCU_152 | 7 | 6 | 17 | 399 |
| VCU_152 | VCU_153 | 0 | 0 | 7 | 416 |
| VCU_153 | VCU_0159 | 7 | 6 | 27 | 390 |

## Per-function changes (newest build vs previous)

| Function | Change |
|---|---|
| `app_apply_mode_limits` | modified |
| `crt_init_then_main` | modified |
| `rtc_day_of_year` | removed in VCU_0159 |
| `rtc_days_between_dates` | removed in VCU_0159 |
| `util_load_u32_le` | added in VCU_0159 |
| `util_store_u32_le` | added in VCU_0159 |
| `vcu_0159_080047ac` | modified |
| `vcu_0159_080054ec` | modified |
| `vcu_0159_08009da8` | modified |
| `vcu_apply_variant_config` | modified |
| `vcu_code_digit_entry_tick` | modified |
| `vcu_countdown_start_handshake` | modified |
| `vcu_crypto_key_load` | modified |
| `vcu_deep_sleep_enter_and_restore` | modified |
| `vcu_display_frame_render_tick` | modified |
| `vcu_drive_command_update` | modified |
| `vcu_error_code_clear` | modified |
| `vcu_fault_code_set` | modified |
| `vcu_fault_warning_evaluate` | modified |
| `vcu_fw_update_frame_handler` | modified |
| `vcu_input_b_hold_start_tick` | modified |
| `vcu_level_gauge_update_v0159` | added in VCU_0159 |
| `vcu_level_gauge_update_v14a_153` | removed in VCU_0159 |
| `vcu_level_hold_latch` | removed in VCU_0159 |
| `vcu_pa6_output_status_update` | modified |
| `vcu_peripheral_init_sequence` | modified |
| `vcu_revolution_stage_tracker` | modified |
| `vcu_runtime_defaults_init` | modified |
| `vcu_rx_frame_dispatch` | modified |
| `vcu_sensor_limit_derate_eval` | modified |
| `vcu_special_mode_gate` | modified |
| `vcu_speed_mode_snapshot_update` | modified |
| `vcu_state0_periodic_tick_v0159` | added in VCU_0159 |
| `vcu_state0_periodic_tick_v148_153` | removed in VCU_0159 |
| `vcu_state2_periodic_tick` | modified |
| `vcu_tea_decrypt_block` | removed in VCU_0159 |
| `vcu_wheel_odometer_limit_update` | modified |
| `vcu_xtea_decrypt_inplace` | added in VCU_0159 |
| `vcu_xtea_decrypt_with_key_at` | added in VCU_0159 |
| `vcu_xtea_key_load` | added in VCU_0159 |
