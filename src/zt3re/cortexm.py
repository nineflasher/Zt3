"""Cortex-M / STM32F1-class knowledge: exception vector names."""
from __future__ import annotations

CORE_VECTORS = [
    "__initial_sp", "Reset_Handler", "NMI_Handler", "HardFault_Handler", "MemManage_Handler",
    "BusFault_Handler", "UsageFault_Handler", None, None, None, None,
    "SVC_Handler", "DebugMon_Handler", None, "PendSV_Handler", "SysTick_Handler",
]

# STM32F103 (high density / connectivity-agnostic) external interrupt positions 0..59.
IRQ_NAMES = [
    "WWDG", "PVD", "TAMPER", "RTC", "FLASH", "RCC", "EXTI0", "EXTI1", "EXTI2", "EXTI3", "EXTI4",
    "DMA1_Channel1", "DMA1_Channel2", "DMA1_Channel3", "DMA1_Channel4", "DMA1_Channel5",
    "DMA1_Channel6", "DMA1_Channel7", "ADC1_2", "USB_HP_CAN1_TX", "USB_LP_CAN1_RX0", "CAN1_RX1",
    "CAN1_SCE", "EXTI9_5", "TIM1_BRK", "TIM1_UP", "TIM1_TRG_COM", "TIM1_CC", "TIM2", "TIM3", "TIM4",
    "I2C1_EV", "I2C1_ER", "I2C2_EV", "I2C2_ER", "SPI1", "SPI2", "USART1", "USART2", "USART3",
    "EXTI15_10", "RTC_Alarm", "USBWakeUp", "TIM8_BRK", "TIM8_UP", "TIM8_TRG_COM", "TIM8_CC", "ADC3",
    "FSMC", "SDIO", "TIM5", "SPI3", "UART4", "UART5", "TIM6", "TIM7", "DMA2_Channel1",
    "DMA2_Channel2", "DMA2_Channel3", "DMA2_Channel4_5",
]


# STM32F091/F072-class (Cortex-M0): 31 external interrupts observed in the BMS images.
IRQ_NAMES_F0 = [
    "WWDG", "PVD_VDDIO2", "RTC", "FLASH", "RCC_CRS", "EXTI0_1", "EXTI2_3", "EXTI4_15", "TSC",
    "DMA1_Channel1", "DMA1_Channel2_3", "DMA1_Channel4_7", "ADC1_COMP", "TIM1_BRK_UP_TRG_COM",
    "TIM1_CC", "TIM2", "TIM3", "TIM6_DAC", "TIM7", "TIM14", "TIM15", "TIM16", "TIM17", "I2C1",
    "I2C2", "SPI1", "SPI2", "USART1", "USART2", "USART3_8", "CEC_CAN", "USB",
]

IRQ_TABLES = {"stm32f103": IRQ_NAMES, "stm32f0": IRQ_NAMES_F0, "bes-m33": []}


def vector_name(index: int, chip: str = "stm32f103") -> str:
    """Name of vector-table slot `index` (0 = initial SP) for `chip`."""
    if chip == "bes-m33" and index == 7:
        return "SecureFault_Handler"
    if index < len(CORE_VECTORS):
        return CORE_VECTORS[index] or f"Reserved_{index}"
    names = IRQ_TABLES[chip]
    irq = index - 16
    return f"{names[irq]}_IRQHandler" if irq < len(names) else f"IRQ{irq}_Handler"
