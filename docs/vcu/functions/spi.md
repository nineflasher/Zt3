# VCU - `spi` functions

5 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`spi_default_para_init`](#spi_default_para_init) | 0x0800E7B4 | Fill a spi_init_type with the Artery SDK defaults (slave, full duplex, 8-bit, software CS) |
| [`spi_enable`](#spi_enable) | 0x0800E7CA | Enable or disable the SPI peripheral through SPI.CTRL1.SPIEN (bit 6) |
| [`spi_init`](#spi_init) | 0x0800E7D4 | Program SPI.CTRL1/CTRL2 and I2SCTRL from an spi_init_type (mode, clock, frame, CS) |
| [`vcu_spi2_init`](#vcu_spi2_init) | 0x080025B8 | Initialise SPI2 from the SDK default config with two overridden words, then enable it |
| [`vcu_spi_pins_remap_init`](#vcu_spi_pins_remap_init) | 0x080024FC | Remap and configure SPI pins PB3, PB4, PB5 and PA15 before SPI2 setup |

## spi_default_para_init

**Fill a spi_init_type with the Artery SDK defaults (slave, full duplex, 8-bit, software CS)**

Sets the 8-byte SPI init structure to the SDK defaults: transmission_mode = full duplex (0), master_slave_mode = slave (0), mclk_freq_division = DIV_2 (0), first_bit = MSB (0), frame_bit_num = 8-bit (0), clock_polarity = low (0), clock_phase = first edge (0) and cs_mode_selection = software (1). This is the Artery SDK spi_default_para_init, and the callers overwrite the fields they need before calling spi_init (vcu_0159_0800e7d4).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | spi_init_type structure to fill (8 bytes) |

- Addresses by version: 148: 0x0800D794, 14a: 0x0800DC30, 14b: 0x0800E0BC, 14e: 0x0800E15C, 14f: 0x0800E2A8, 152: 0x0800E550, 153: 0x0800E644, 0159: 0x0800E7B4
- Called by: `vcu_spi2_init`
- Confidence: high

## spi_enable

**Enable or disable the SPI peripheral through SPI.CTRL1.SPIEN (bit 6)**

Read-modify-write of the first control register that sets or clears bit 6 (SPIEN) and leaves the other bits unchanged. It is normally called after spi_init to start the SPI. This is the Artery SDK spi_enable.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | SPI peripheral base |
| `param_2` | `s32` | confirm_state: non-zero enables, zero disables |

- Addresses by version: 148: 0x0800D7AA, 14a: 0x0800DC46, 14b: 0x0800E0D2, 14e: 0x0800E172, 14f: 0x0800E2BE, 152: 0x0800E566, 153: 0x0800E65A, 0159: 0x0800E7CA
- Called by: `vcu_spi2_init`
- Confidence: high

## spi_init

**Program SPI.CTRL1/CTRL2 and I2SCTRL from an spi_init_type (mode, clock, frame, CS)**

Applies the SPI init structure with read-modify-write of the control registers: I2SCTRL.I2SMSEL is cleared (SPI mode, not I2S); the transmission mode goes to SLBEN (bit 15), SLBTD (bit 14) and ORA (bit 10) for full duplex, RX-only, half-duplex RX or half-duplex TX; SWCSEN (bit 9) takes the CS mode, and SWCSIL (bit 8) is set for master with software CS; MSTEN (bit 2) takes master/slave; the baud divisor goes to MDIV_L (CTRL1 bits 5..3) and MDIV_H (CTRL2 bit 8) when the divisor is above 7; LTF (bit 7) selects LSB first; FBN (bit 11) selects 16-bit frames; CLKPOL (bit 1) and CLKPHA (bit 0) set the clock idle level and sampling edge. This is the Artery SDK spi_init. The bit positions were checked against the SDK struct.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | SPI peripheral base |
| `param_2` | `ptr` | spi_init_type: transmission mode, master/slave, divisor, bit order, frame size, clock polarity, phase, CS mode |

- Addresses by version: 148: 0x0800D7B4, 14a: 0x0800DC50, 14b: 0x0800E0DC, 14e: 0x0800E17C, 14f: 0x0800E2C8, 152: 0x0800E570, 153: 0x0800E664, 0159: 0x0800E7D4
- Called by: `vcu_spi2_init`
- Confidence: high

## vcu_spi2_init

**Initialise SPI2 from the SDK default config with two overridden words, then enable it**

Brings up SPI2: it calls vcu_spi_pins_remap_init for the pins, enables the SPI2 clock (APB1 bit 14), and loads spi_default_para_init (slave, full duplex, 8-bit, software chip select). It overrides two init words, 0x00020100 and 0x01000000, then calls spi_init(SPI2) and spi_enable(SPI2, TRUE). The overridden words are not decoded to specific bit fields here.

**Notes:** Whether SPI2 ends up master or slave depends on the overridden words, which were not decoded. Confirm the role before relying on this summary.

- Addresses by version: 148: 0x080021E4, 14a: 0x08002254, 14b: 0x08002518, 14e: 0x08002518, 14f: 0x08002574, 152: 0x080025B0, 153: 0x080025CC, 0159: 0x080025B8
- Peripheral registers: `SPI2.CTRL1` (A)
- Called by: `vcu_0159_08002060`
- Calls: `vcu_spi_pins_remap_init`, `crm_periph_clock_enable`, `spi_default_para_init`, `spi_enable`, `spi_init`
- Confidence: medium

## vcu_spi_pins_remap_init

**Remap and configure SPI pins PB3, PB4, PB5 and PA15 before SPI2 setup**

Enables the IOMUX, GPIOA and GPIOB clocks, applies pin remap code 0x28140401 with gpio_pin_remap_config (enable 1), and then configures PB3 (mask 0x8), PB4 (0x10), PB5 (0x20) and PA15 (0x8000) with gpio_default_para_init and gpio_init. The pins are configured as alternate-function outputs or inputs with packed words 0x01081800 and 0x01101800, and PA15 is set through a 0x110 word. It is called first in vcu_0159_080025b8 (SPI2 init).

**Notes:** The remap target is not decoded. The pin set is the usual SPI remap group, but that is inferred.

- Addresses by version: 148: 0x08002110, 14a: 0x08002180, 14b: 0x0800245C, 14e: 0x0800245C, 14f: 0x080024B8, 152: 0x080024F4, 153: 0x08002510, 0159: 0x080024FC
- Peripheral registers: `GPIOA.CFGLR` (A), `GPIOB.CFGLR` (A)
- Called by: `vcu_spi2_init`
- Calls: `crm_periph_clock_enable`, `gpio_default_para_init`, `gpio_init`, `gpio_pin_remap_config`
- Confidence: medium
