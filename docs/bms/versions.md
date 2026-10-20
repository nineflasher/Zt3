# BMS version evolution

Functions are tracked across builds with Ghidra Version Tracking (see methodology).

| From | To | Added | Removed | Modified | Unchanged |
|---|---|---|---|---|---|
| BMS_4130 | BMS_4139 | 10 | 5 | 16 | 386 |
| BMS_4139 | BMS_4148 | 25 | 19 | 19 | 374 |
| BMS_4148 | BMS_4168 | 2 | 2 | 23 | 393 |

## Per-function changes (newest build vs previous)

| Function | Change |
|---|---|
| `bms_4168_080082bc` | modified |
| `bms_4168_0800c96c` | modified |
| `bms_4168_0800f2e0` | modified |
| `bms_4168_0800fb94` | modified |
| `bms_balance_timer_step` | removed in BMS_4168 |
| `bms_can_cmd_set_handler` | modified |
| `bms_charge_integrate_step` | modified |
| `bms_comm_pool_tick_gated_4148` | removed in BMS_4168 |
| `bms_comm_pool_tick_with_threshold` | added in BMS_4168 |
| `bms_comm_service_step` | modified |
| `bms_current_limit_derate` | modified |
| `bms_fdcan_nominal_500k_setup` | modified |
| `bms_limit_status_update` | modified |
| `bms_mode_fsm_step` | modified |
| `bms_pct_hysteresis_step` | added in BMS_4168 |
| `bms_profile_block_fill_4168` | modified |
| `bms_profile_select_from_code` | modified |
| `bms_remaining_time_4168` | modified |
| `bms_soc_main_step` | modified |
| `bms_soc_tick_update` | modified |
| `bms_soc_update_from_voltage` | modified |
| `bms_startup_init_unpack` | modified |
| `bms_state_restore_or_init` | modified |
| `bms_status_event_snapshot` | modified |
| `bms_telemetry_block_fill_16` | modified |
| `bms_telemetry_sched_16_step` | modified |
| `gpio_pb13_15_strap_read` | modified |
