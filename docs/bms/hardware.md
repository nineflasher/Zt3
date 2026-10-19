# BMS hardware usage (stm32g0b1)

| Peripheral | Used by |
|---|---|
| ADC | `bms_adc_deinit`, `bms_adc_hw_init`, `bms_adc_read_mv` |
| EXTI | `EXTI0_1_IRQHandler`, `EXTI2_3_IRQHandler`, `EXTI4_15_IRQHandler`, `HAL_GPIO_DeInit`, `HAL_GPIO_Init`, `HAL_RTCEx_SetWakeUpTimer_IT`, `LL_EXTI_Init`, `bms_exti11_irq_arm`, `bms_exti11_irq_disarm`, `bms_gpio_exti_init`, `exti_disable_lines_2_8_12` |
| FDCAN1 | `HAL_FDCAN_Init` |
| FDCAN2 | `bms_fdcan_nominal_500k_setup`, `fdcan2_is_bus_off` |
| FLASH | `HAL_FLASHEx_Erase`, `HAL_FLASH_Lock`, `HAL_FLASH_Program`, `HAL_FLASH_Unlock`, `bms_flash_erase_program_page`, `bms_flash_wait_idle_check`, `bms_hw_init_systick_prefetch` |
| IWDG | `LL_IWDG_ReloadCounter`, `bms_iwdg_start` |
| NVIC | `NVIC_SetPriority`, `__NVIC_DisableIRQ`, `__NVIC_EnableIRQ`, `__NVIC_SetPriority`, `bms_exti11_irq_arm`, `bms_exti11_irq_disarm`, `bms_gpio_exti_init`, `bms_tim6_tim7_start`, `bms_tim6_tim7_stop`, `bms_usart3_comm_init` |
| PWR | `PWR_EnterSTOPMode`, `bms_rtc_backup_reset_lse_on`, `bms_rtc_clock_bringup`, `bms_rtc_fallback_lsi_start` |
| RCC | `HAL_FDCAN_MspDeInit`, `HAL_FDCAN_MspInit`, `HAL_RCC_EnableCSS`, `HAL_RCC_GetSysClockFreq`, `HAL_RTC_MspInit`, `LL_APB1_GRP1_EnableClock`, `LL_IOP_GRP1_EnableClock`, `LL_TIM_DeInit`, `LL_USART_DeInit`, `RCC_CRS_IRQHandler`, `bms_adc_hw_init`, `bms_gpio_board_init`, `bms_rcc_periph_clk_get`, `bms_rtc_backup_reset_lse_on`, `bms_rtc_clock_bringup`, `bms_rtc_fallback_lsi_start`, `bms_rtc_lse_ready_get`, `bms_rtc_select_lse_and_start`, `bms_spi1_master_init`, `bms_sysclk_hse_pll_bringup`, `bms_sysclk_hsi16_switch`, `bms_ucpd_clock_irq_setup`, `bms_usart3_comm_init`, `bms_vtor_reset_cause_latch`, `gpio_pb13_15_strap_read`, `rcc_hclk_divide`, `rcc_pclk_divide` |
| RTC | `HAL_RTCEx_SetWakeUpTimer_IT`, `bms_rtc_hal_init`, `bms_rtc_wait_synchro` |
| SCB | `HardFault_Handler`, `NVIC_SetPriority`, `NVIC_SystemReset`, `PWR_EnterSTOPMode`, `SysTick_Config`, `__NVIC_SetPriority`, `bms_nvic_system_reset_plain`, `bms_vtor_reset_cause_latch` |
| SPI1 | `LL_SPI_Disable`, `bms_spi1_master_init`, `bms_spi1_transfer_byte` |
| SRAMCAN_FDCAN1 | `HAL_FDCAN_Init` |
| SRAMCAN_FDCAN2 | `HAL_FDCAN_Init` |
| SYSCFG | `bms_css_enable_sram_parity_lock`, `bms_syscfg_set_ucpd_strobe` |
| SysTick | `SysTick_Config`, `bms_adc_hw_init`, `bms_adc_read_mv`, `bms_systick_wait_repeat`, `bms_systick_wait_scaled` |
| TIM2 | `bms_adc_hw_init`, `bms_fdcan_filters_start`, `bms_fdcan_send_frame`, `bms_flash_erase_program_page`, `bms_rtc_hal_init` |
| TIM6 | `bms_tim6_tim7_start`, `bms_tim6_tim7_stop`, `bms_tim6_tim7_stop_reset`, `bms_tim6_update_flag_poll` |
| TIM7 | `TIM7_LPTIM2_IRQHandler`, `bms_tim6_tim7_start`, `bms_tim6_tim7_stop`, `bms_tim6_tim7_stop_reset` |
| USART3 | `USART3_4_5_6_LPUART1_IRQHandler`, `bms_usart3_comm_init`, `bms_usart3_rxne_irq_set`, `bms_usart3_send_bytes`, `bms_usart3_stop`, `bms_usart3_tx_setup` |
