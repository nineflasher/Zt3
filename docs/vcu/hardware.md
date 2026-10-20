# VCU hardware usage (at32f415)

| Peripheral | Used by |
|---|---|
| ADC1 | `vcu_adc1_scan_init`, `vcu_adc_dma_ring_init` |
| CAN1 | `CAN1_RX0_IRQHandler`, `CAN1_SE_IRQHandler`, `vcu_can1_init`, `vcu_can1_recover_reinit`, `vcu_can_tx_pump`, `vcu_deep_sleep_enter_and_restore` |
| CRM | `SystemInit`, `crm_adc_clock_div_set`, `crm_ahb_div_set`, `crm_apb1_div_set`, `crm_apb2_div_set`, `crm_auto_step_mode_enable`, `crm_battery_powered_domain_reset`, `crm_clock_source_enable`, `crm_clocks_freq_get`, `crm_ertc_clock_enable`, `crm_ertc_clock_select`, `crm_flag_get`, `crm_periph_clock_enable`, `crm_periph_reset`, `crm_pll_config`, `crm_reset`, `crm_sysclk_switch`, `crm_sysclk_switch_status_get`, `system_clock_config`, `vcu_deep_sleep_enter_and_restore` |
| DEBUG | `debug_periph_mode_set` |
| DMA1 | `dma_flag_clear`, `dma_flag_get`, `dma_reset`, `vcu_adc_dma_ring_init`, `vcu_dma_tx_start`, `vcu_usart2_rx_dma_init`, `vcu_usart2_tx_dma_init` |
| DMA2 | `dma_flag_clear`, `dma_flag_get`, `dma_reset` |
| ERTC | `ertc_date_set`, `ertc_divider_set`, `ertc_flag_clear`, `ertc_flag_get`, `ertc_hour_mode_set`, `ertc_init_mode_enter`, `ertc_init_mode_exit`, `ertc_interrupt_enable`, `ertc_reset`, `ertc_wait_update`, `ertc_wakeup_clock_set`, `ertc_wakeup_counter_set`, `ertc_wakeup_enable`, `ertc_write_protect_disable`, `ertc_write_protect_enable`, `vcu_ertc_default_datetime_init` |
| EXINT | `exint_flag_clear`, `exint_flag_get`, `exint_init`, `exint_interrupt_enable` |
| FLASH | `flash_fap_status_get`, `flash_flag_clear`, `flash_halfword_program`, `flash_lock`, `flash_operation_status_get`, `flash_sector_erase`, `flash_unlock`, `flash_user_system_data_erase`, `system_clock_config` |
| GPIOA | `vcu_adc_analog_pins_init`, `vcu_exint14_pb14_init`, `vcu_exint3_pa3_init`, `vcu_exint_pb12_pb14_init`, `vcu_fault_warning_evaluate`, `vcu_gpio_board_init`, `vcu_gpio_out_pins_config`, `vcu_gpio_outputs_set_levels`, `vcu_gpio_pa0_init`, `vcu_gpio_pa9_pb67_init`, `vcu_gpio_pa9_reset`, `vcu_gpio_pa9_set`, `vcu_pa11_pulse_step`, `vcu_pa1_input_high`, `vcu_pa6_output_set`, `vcu_spi_pins_remap_init`, `vcu_usart2_pins_init` |
| GPIOB | `vcu_adc_analog_pins_init`, `vcu_can1_pins_remap_init`, `vcu_exint14_pb14_init`, `vcu_exint_pb12_pb14_init`, `vcu_gpio_b10_high_b2_low`, `vcu_gpio_b10_low_b2_high`, `vcu_gpio_out_pins_config`, `vcu_gpio_outputs_set_levels`, `vcu_gpio_pa9_pb67_init`, `vcu_gpio_pb6_reset`, `vcu_gpio_pb6_set`, `vcu_gpio_pb7_reset`, `vcu_gpio_pb7_set`, `vcu_pb11_input_active_low`, `vcu_pb12_input_active_low`, `vcu_pb13_input_active_low`, `vcu_pb14_timed_edge_sequence`, `vcu_spi_pins_remap_init` |
| GPIOC | `gpio_bits_reset`, `gpio_bits_set`, `vcu_c14_c15_pulse_sequencer`, `vcu_gpio_board_init`, `vcu_gpio_c14_set`, `vcu_gpio_c15_set`, `vcu_gpio_out_pins_config`, `vcu_gpio_outputs_set_levels` |
| GPIOF | `vcu_exint14_pb14_init`, `vcu_gpio_outputs_set_levels` |
| IOMUX | `gpio_exint_line_config`, `gpio_pin_remap_config` |
| NVIC | `nvic_irq_enable` |
| PWC | `pwc_battery_powered_domain_access`, `pwc_voltage_regulate_set` |
| SCB | `SystemInit`, `nvic_irq_enable`, `nvic_priority_group_config`, `pwc_deep_sleep_mode_enter`, `vcu_deferred_system_reset`, `vcu_fw_update_frame_handler` |
| SCnSCB | `vcu_systick_resume`, `vcu_systick_suspend` |
| SPI2 | `vcu_spi2_init` |
| SysTick | `delay_ms`, `delay_us`, `systick_clock_source_config`, `vcu_systick_resume`, `vcu_systick_suspend` |
| TMR2 | `flash_sector_erase`, `flash_user_system_data_erase`, `tmr2_pwm_output_disable`, `tmr2_pwm_set_frequency`, `vcu_alert_tone_start_if_idle`, `vcu_tmr2_ch1_pwm_init`, `vcu_tmr2_ch1_pwm_start`, `vcu_tmr2_pwm_pa0_bringup_14a` |
| TMR5 | `TMR5_GLOBAL_IRQHandler`, `vcu_tmr5_1khz_tick_init` |
| USART2 | `USART2_IRQHandler`, `vcu_usart2_init`, `vcu_usart2_rx_dma_init`, `vcu_usart2_tx_dma_init` |
| WDT | `vcu_watchdog_start`, `wdt_counter_reload`, `wdt_divider_set`, `wdt_register_write_enable`, `wdt_reload_value_set` |
