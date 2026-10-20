# VCU brief (for annotation agents)

Vehicle control unit of the scooter: **Artery AT32F415** (Cortex-M4F, FPU not used by the code, 32 KiB
SRAM, 64+ KiB flash).  Eight firmware builds (148 ... 0159, hex).  Application image is loaded at
0x08001000 (4 KiB bootloader below); the vector table has 92 slots (see `src/zt3re/data/hw/at32f415_irqs.json`).
Role: main controller - gateway between the BLE module, the motor controller (MCU), the BMS, the
dashboard/inputs and the lights; likely CAN + UART protocols (Ninebot-style frames are common: look for
header bytes such as 0x5A 0xA5, src/dest/cmd/length fields and a checksum - confirm from the code).

Hardware names: peripheral registers appear in the packets as `PERIPH.REG` from the vendor SVD
(`CRM` clock/reset, `IOMUX`, `EXINT`, `GPIOx`, `TMRx`, `USARTx`, `CAN1`, `ADC1`, `DMA1/2`, `ERTC`, `WDT/WWDT`,
`PWC`, `FLASH`, `CRC`, `SPIx`, `I2Cx`, `USB_OTG_*`).  Full register + bit-field docs are in
`src/zt3re/data/hw/at32f415_registers.json` (use it to interpret magic constants written to registers).

Vendor SDK for naming: the Artery firmware library is cloned at
`/home/user/arterytek/at32f415_firmware_library` (drivers in `libraries/drivers/src/at32f415_*.c`, headers
`libraries/drivers/inc/`, startup/system in `libraries/cmsis/cm4/device_support/`).  When a function
matches an SDK driver (gpio_init, usart_init, crm_periph_clock_enable, tmr_base_init, can_base_init,
adc_base_config, dma_init, flash_*, ertc_*, wdt_*, pwc_*, nvic_*, system_clock_config ...), use that exact
name and summarise per the SDK source (grep it).  Other code is the scooter application.

Memory: SRAM 0x20000000..0x20008000.  0x1FFFF7E8.. is read by startup code (device ID words; used to
derive a per-device value).  Typical categories: `startup clock gpio uart can adc timer dma flash rtc
watchdog power isr protocol crypto util libc app vehicle lighting display input diagnostics bootloader_iface`.
