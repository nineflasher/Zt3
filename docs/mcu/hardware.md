# MCU hardware usage (at32f415)

| Peripheral | Used by |
|---|---|
| ADC1 | `mcu_adc1_dma_init`, `mcu_adc_injected_seq_select`, `mcu_phase_current_from_adc` |
| CAN1 | `CAN1_RX0_IRQHandler`, `CAN1_SE_IRQHandler`, `mcu_can_init`, `mcu_msg_ring2_tx_step` |
| CRM | `SystemInit`, `crm_adc_clock_div_set`, `crm_ahb_div_set`, `crm_apb1_div_set`, `crm_apb2_div_set`, `crm_auto_step_mode_enable`, `crm_clock_source_enable`, `crm_clocks_freq_get`, `crm_flag_get`, `crm_hext_bypass`, `crm_lext_bypass`, `crm_periph_clock_enable`, `crm_periph_reset`, `crm_pll_config`, `crm_reset`, `crm_sysclk_switch`, `crm_sysclk_switch_status_get`, `system_clock_config` |
| DEBUG | `mcu_read_device_identity` |
| DMA1 | `dma_reset`, `mcu_adc1_dma_init`, `mcu_adc_dma_median5` |
| DMA2 | `dma_reset` |
| EXINT | `exint_flag_clear`, `exint_flag_get`, `exint_init` |
| FLASH | `flash_flag_clear`, `flash_halfword_program`, `flash_lock`, `flash_operation_status_get`, `flash_sector_erase`, `flash_unlock`, `system_clock_config` |
| GPIOA | `mcu_gpioa_pin_cfg_init` |
| GPIOB | `mcu_indicator_update`, `mcu_status_drive_pb6_pc11` |
| GPIOC | `mcu_gpioc_pin10_follow_flag`, `mcu_hall_dispatch_pc12_output`, `mcu_indicator_update`, `mcu_poll_pc9_input_and_flag`, `mcu_pulse_burst_sample_pc3`, `mcu_status_drive_pb6_pc11` |
| IOMUX | `gpio_pin_remap_config` |
| NVIC | `mcu_pvm_init`, `nvic_irq_enable` |
| PWC | `pwc_battery_powered_domain_access`, `pwc_power_voltage_monitor_enable`, `pwc_pvm_level_select` |
| SCB | `NVIC_SystemReset`, `SystemInit`, `nvic_irq_enable`, `nvic_priority_group_config`, `nvic_vector_table_set` |
| SCnSCB | `mcu_systick_free_run_start` |
| SysTick | `mcu_busy_wait_systick_counts`, `mcu_foc_control_tick`, `mcu_systick_free_run_start`, `systick_clock_source_config` |
| TMR1 | `mcu_foc_control_tick`, `mcu_pwm_outputs_set_enable`, `mcu_pwm_trigger_and_clamp_select`, `mcu_tmr1_pwm_outputs_enable` |
| TMR2 | `flash_sector_erase`, `mcu_fb_lpf_select_update`, `mcu_param_record_load` |
| TMR4 | `mcu_tmr4_ch4_compare_clear` |
| WDT | `mcu_watchdog_feed`, `mcu_watchdog_start`, `wdt_divider_set`, `wdt_register_write_enable`, `wdt_reload_value_set` |
