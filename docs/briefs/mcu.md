# MCU brief (for annotation agents)

Motor controller of the scooter: **Artery AT32F415** (same chip family as the VCU; Cortex-M4F integer
code, FPU unused).  Four firmware builds (12b, 143, 152, 0160 hex).  Loaded at 0x08001000 (4 KiB
bootloader below), 92 vector slots.  Active interrupt handlers: PVM, ADC1, CAN1_RX0, CAN1_SE, TMR3,
TMR4 (see `src/zt3re/data/hw/at32f415_irqs.json`).  The code reads the debug IDCODE (0xE0042000) and
compares it to an Artery constant.  Expect: motor drive (TMR1 complementary PWM, ADC current/voltage/
hall sampling, sine/lookup tables), speed/torque control loop, CAN communication with the VCU, fault
handling and protection (over-current, over-temperature, stall), watchdog.

Hardware names: registers in the packets are shown as `PERIPH.REG` from the vendor SVD (`CRM`, `IOMUX`,
`EXINT`, `GPIOx`, `TMRx`, `USARTx`, `CAN1`, `ADC1`, `DMA1`, `WDT`, `PWC`, `FLASH`, `CRC`).  Register/bit
docs: `src/zt3re/data/hw/at32f415_registers.json`.

Vendor SDK for naming: `/home/user/arterytek/at32f415_firmware_library` (drivers in
`libraries/drivers/src/at32f415_*.c`).  If a function matches an SDK driver use its exact name.  The VCU
firmware in `annotations/vcu/functions/` (when present) shares SDK driver code with the MCU - reuse its names
for identical routines (check the VCU packet/annotation of the matching function if one exists).

Typical categories: `startup clock gpio adc timer pwm motor foc hall encoder protection can uart dma
flash watchdog power isr protocol util libc`.
