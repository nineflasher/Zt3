# BMS hardware usage (stm32g0b1)

| Peripheral | Used by |
|---|---|
| ADC | `bms_adc_deinit`, `bms_adc_hw_init`, `bms_adc_read_mv` |
| EXTI | `HAL_GPIO_DeInit`, `HAL_GPIO_Init`, `LL_EXTI_Init`, `bms_exti11_irq_arm`, `bms_exti11_irq_disarm`, `bms_gpio_exti_init`, `exti_disable_lines_2_8_12` |
| FDCAN2 | `fdcan2_is_bus_off` |
| FLASH | `HAL_FLASH_Lock`, `HAL_FLASH_Unlock` |
| IWDG | `LL_IWDG_ReloadCounter`, `bms_iwdg_start` |
| NVIC | `NVIC_SetPriority`, `__NVIC_DisableIRQ`, `__NVIC_EnableIRQ`, `__NVIC_SetPriority`, `bms_exti11_irq_arm`, `bms_exti11_irq_disarm`, `bms_gpio_exti_init`, `bms_tim6_tim7_start`, `bms_tim6_tim7_stop` |
| PWR | `PWR_EnterSTOPMode`, `bms_rtc_backup_reset_lse_on`, `bms_rtc_clock_bringup` |
| RCC | `HAL_RCC_EnableCSS`, `HAL_RTC_MspInit`, `LL_APB1_GRP1_EnableClock`, `LL_IOP_GRP1_EnableClock`, `LL_TIM_DeInit`, `LL_USART_DeInit`, `bms_adc_hw_init`, `bms_gpio_board_init`, `bms_rtc_backup_reset_lse_on`, `bms_rtc_clock_bringup`, `bms_rtc_lse_ready_get`, `bms_spi1_master_init`, `bms_sysclk_hse_pll_bringup`, `bms_sysclk_hsi16_switch`, `gpio_pb13_15_strap_read`, `rcc_hclk_divide`, `rcc_pclk_divide` |
| SCB | `HardFault_Handler`, `NVIC_SetPriority`, `NVIC_SystemReset`, `PWR_EnterSTOPMode`, `SysTick_Config`, `__NVIC_SetPriority`, `bms_nvic_system_reset_plain` |
| SPI1 | `LL_SPI_Disable`, `bms_spi1_master_init`, `bms_spi1_transfer_byte` |
| SYSCFG | `bms_css_enable_sram_parity_lock`, `bms_syscfg_set_ucpd_strobe` |
| SysTick | `SysTick_Config`, `bms_adc_hw_init`, `bms_adc_read_mv`, `bms_systick_wait_repeat`, `bms_systick_wait_scaled` |
| TIM2 | `bms_adc_hw_init`, `bms_fdcan_filters_start`, `bms_fdcan_send_frame` |
| TIM6 | `bms_tim6_tim7_start`, `bms_tim6_tim7_stop`, `bms_tim6_tim7_stop_reset`, `bms_tim6_update_flag_poll` |
| TIM7 | `bms_tim6_tim7_start`, `bms_tim6_tim7_stop`, `bms_tim6_tim7_stop_reset` |
| USART3 | `bms_usart3_rxne_irq_set`, `bms_usart3_send_bytes`, `bms_usart3_stop`, `bms_usart3_tx_setup` |
