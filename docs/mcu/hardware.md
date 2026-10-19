# MCU hardware usage (at32f415)

| Peripheral | Used by |
|---|---|
| CRM | `SystemInit`, `crm_adc_clock_div_set`, `crm_ahb_div_set`, `crm_apb1_div_set`, `crm_apb2_div_set`, `crm_auto_step_mode_enable`, `crm_clock_source_enable`, `crm_flag_get`, `crm_hext_bypass`, `crm_lext_bypass`, `crm_periph_clock_enable`, `crm_periph_reset`, `crm_pll_config`, `crm_reset`, `crm_sysclk_switch`, `crm_sysclk_switch_status_get` |
| DEBUG | `mcu_read_device_identity` |
| DMA1 | `dma_reset` |
| DMA2 | `dma_reset` |
| EXINT | `exint_flag_clear`, `exint_flag_get`, `exint_init` |
| FLASH | `flash_flag_clear`, `flash_lock`, `flash_operation_status_get`, `flash_unlock` |
| GPIOC | `mcu_poll_pc9_input_and_flag` |
| IOMUX | `gpio_pin_remap_config` |
| NVIC | `nvic_irq_enable` |
| PWC | `pwc_battery_powered_domain_access`, `pwc_power_voltage_monitor_enable`, `pwc_pvm_level_select` |
| SCB | `NVIC_SystemReset`, `SystemInit`, `nvic_irq_enable`, `nvic_priority_group_config`, `nvic_vector_table_set` |
| SysTick | `mcu_busy_wait_systick_counts`, `systick_clock_source_config` |
| TMR1 | `mcu_pwm_outputs_set_enable`, `mcu_tmr1_pwm_outputs_enable` |
| WDT | `mcu_watchdog_feed`, `wdt_divider_set`, `wdt_register_write_enable`, `wdt_reload_value_set` |
