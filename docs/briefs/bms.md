# BMS brief (for annotation agents)

Battery management system: **STM32G0B1-class** (Cortex-M0+ / ARMv6-M; G0B1 or G0C1), NOT an Artery part.
Four firmware builds (4130, 4139, 4148, 4168).  Loaded at 0x08001000 (4 KiB bootloader below), 47
vector slots (16 core + 31 IRQs; names in `src/zt3re/data/hw/stm32g0b1_irqs.json`: EXTI lines, TIM7/LPTIM2,
USART3_4_5_6/LPUART1, TIM16/FDCAN_IT0, RTC_TAMP ...).  Peripherals seen: RCC/PWR/FLASH, EXTI at
0x40021800, GPIO at 0x50000000 (IOPORT), TIM1/3/7/14-17, USART3 (+4/5/6), FDCAN1 (message RAM 0x4000B400),
ADC, DMA/DMAMUX, I2C/SPI, IWDG/WWDG, RTC, CRC.  Role: cell voltage/temperature/current monitoring
(likely through an external AFE over I2C/SPI or ADC), SOC estimation, balancing, protection (charge/discharge
FETs), communication over UART and FDCAN with the VCU/charger.

Hardware names: registers in the packets appear as `PERIPH.REG` from the ST SVD.  Register/bit docs:
`src/zt3re/data/hw/stm32g0b1_registers.json`.  ST HAL/LL driver names: if a function matches an STM32G0
HAL/LL routine (HAL_GPIO_Init, HAL_RCC_OscConfig, LL_USART_*, HAL_FDCAN_*, HAL_ADC_*, ...), use its exact
name; HAL source can be fetched from raw.githubusercontent.com (STMicroelectronics/STM32CubeG0,
STMicroelectronics/stm32g0xx_hal_driver, STMicroelectronics/cmsis_device_g0) - use it only to confirm names.

Typical categories: `startup clock gpio adc timer uart fdcan i2c spi dma flash rtc watchdog power isr afe
soc balancing protection charge discharge protocol util libc`.
