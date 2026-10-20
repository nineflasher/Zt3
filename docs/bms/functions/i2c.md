# BMS - `i2c` functions

14 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_i2c_bb_bus_init`](#bms_i2c_bb_bus_init) | 0x080095B6 | Set up the bit-banged bus: enable GPIOA/GPIOB clocks, PA11 and PA12 open-drain high |
| [`bms_i2c_bb_bus_release`](#bms_i2c_bb_bus_release) | 0x08009622 | Release PA11 and PA12 back to analog (high-impedance) mode after bus use |
| [`bms_i2c_bb_read_ack`](#bms_i2c_bb_read_ack) | 0x080096F0 | Read one byte on the bit-banged bus, then send ACK or NACK and optionally a STOP |
| [`bms_i2c_bb_read_block`](#bms_i2c_bb_read_block) | 0x080094B4 | Bit-banged I2C read: address and register, repeated START, then N bytes with NACK on the last |
| [`bms_i2c_bb_read_byte`](#bms_i2c_bb_read_byte) | 0x08009740 | Receive one byte MSB first on the bit-banged bus, sampling PA12 while PA11 is high |
| [`bms_i2c_bb_send_bit0`](#bms_i2c_bb_send_bit0) | 0x08009428 | Clock one 0 bit on the bit-banged bus (SDA low with an SCL pulse) with a clock-stretch timeout |
| [`bms_i2c_bb_send_bit1`](#bms_i2c_bb_send_bit1) | 0x08009664 | Clock one 1 bit on the bit-banged bus (SDA high with an SCL pulse), with stretch timeout |
| [`bms_i2c_bb_start`](#bms_i2c_bb_start) | 0x080098F0 | Generate a START (or repeated START) condition on the bit-banged bus |
| [`bms_i2c_bb_stop`](#bms_i2c_bb_stop) | 0x0800997C | Generate a STOP condition on the bit-banged bus (SDA rises while SCL is high) |
| [`bms_i2c_bb_write_block`](#bms_i2c_bb_write_block) | 0x0800954C | Bit-banged I2C write: address, register, then N data bytes with STOP on the last |
| [`bms_i2c_bb_write_byte`](#bms_i2c_bb_write_byte) | 0x0800982C | Send one byte MSB first on the bit-banged bus with an SCL pulse per bit |
| [`bms_i2c_bb_write_byte_ack`](#bms_i2c_bb_write_byte_ack) | 0x080097D8 | Send one I2C byte with optional START and STOP, returning the ACK status |
| [`bms_i2c_frame_read_crc8`](#bms_i2c_frame_read_crc8) | 0x0800B694 | Read a framed I2C response with a CRC-8 trailer (poly 0x07), retrying up to four times |
| [`bms_i2c_frame_write_crc8`](#bms_i2c_frame_write_crc8) | 0x0800B7BC | Write a framed I2C message with a CRC-8 (poly 0x07) byte, retrying up to four times |

## bms_i2c_bb_bus_init

**Set up the bit-banged bus: enable GPIOA/GPIOB clocks, PA11 and PA12 open-drain high**

Clears a 24-byte local structure with bms_4168_08001246, enables the GPIOA and GPIOB clocks through LL_IOP_GRP1_EnableClock, and drives PA12 and PA11 high. It then configures both pins as open-drain outputs at very high speed with no pull through LL_GPIO_Init and drives them high again so the bus idles high. It is called from bms_4168_08008294 and bms_4168_080082F0 during initialisation.

- Addresses by version: 4130: 0x08008556, 4139: 0x08008A56, 4148: 0x080092A2, 4168: 0x080095B6
- Called by: `bms_peripheral_bringup`, `bms_4168_080082f0`
- Calls: `bms_mem_zero`, `LL_GPIO_Init`, `LL_GPIO_SetOutputPin`, `LL_IOP_GRP1_EnableClock`
- Confidence: medium

## bms_i2c_bb_bus_release

**Release PA11 and PA12 back to analog (high-impedance) mode after bus use**

Clears a 24-byte local structure with bms_4168_08001246, then calls LL_GPIO_Init on GPIOA twice to set PA12 (pin 0x1000) and PA11 (pin 0x0800) to analog mode with no pull. It is the counterpart of bms_i2c_bb_bus_init and is called from bms_4168_080082F0.

- Addresses by version: 4130: 0x080085C2, 4139: 0x08008AC2, 4148: 0x0800930E, 4168: 0x08009622
- Called by: `bms_4168_080082f0`
- Calls: `bms_mem_zero`, `LL_GPIO_Init`
- Confidence: medium

## bms_i2c_bb_read_ack

**Read one byte on the bit-banged bus, then send ACK or NACK and optionally a STOP**

Calls bms_i2c_bb_read_byte to store the received byte at rx_out. If that succeeds, nack selects the acknowledge bit: 0 sends an ACK through bms_i2c_bb_send_bit0 and a nonzero value sends a NACK through bms_i2c_bb_send_bit1. If the acknowledge succeeded and send_stop is 1, bms_i2c_bb_stop is issued. It returns the status of the last step run, 0 on success or 2 on a clock-stretch timeout.

| Parameter | Type | Description |
|---|---|---|
| `rx_out` | `ptr` | destination for the received byte |
| `nack` | `s32` | 0 sends ACK; nonzero sends NACK |
| `send_stop` | `s32` | 1 issues a STOP after the acknowledge; other values do not |

**Returns** `s32`: 0 on success, 2 on a clock-stretch timeout

- Addresses by version: 4130: 0x08008690, 4139: 0x08008B90, 4148: 0x080093DC, 4168: 0x080096F0
- Called by: `bms_i2c_bb_read_block`
- Calls: `bms_i2c_bb_send_bit0`, `bms_i2c_bb_send_bit1`, `bms_i2c_bb_read_byte`, `bms_i2c_bb_stop`
- Confidence: medium

## bms_i2c_bb_read_block

**Bit-banged I2C read: address and register, repeated START, then N bytes with NACK on the last**

Reads param_4 bytes from device param_1 starting at register param_2 on the bit-banged bus. It sends START and the address byte with bms_4168_080097D8 (START on, STOP off), sends the register byte, then sends a repeated START with the read address (param_1 | 1). It reads bytes 0 to N-2 with ACK through bms_i2c_bb_read_ack and the last byte with NACK and STOP. Any failing step returns its ACK status, and after a failed last byte a STOP is also issued with bms_i2c_bb_stop.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | device address byte in write form (bit 0 is set for the read phase) |
| `param_2` | `u32` | register or command byte |
| `param_3` | `ptr` | destination buffer |
| `param_4` | `s32` | number of bytes to read |

**Returns** `s32`: 0 on success, otherwise the nonzero ACK status of the failing step

- Addresses by version: 4130: 0x08008454, 4139: 0x08008954, 4148: 0x080091A0, 4168: 0x080094B4
- Called by: `bms_i2c_frame_read_crc8`
- Calls: `bms_i2c_bb_read_ack`, `bms_i2c_bb_write_byte_ack`, `bms_i2c_bb_stop`
- Confidence: high

## bms_i2c_bb_read_byte

**Receive one byte MSB first on the bit-banged bus, sampling PA12 while PA11 is high**

Switches PA12 to input, then for each of 8 bits pulses PA11 low and high, polls PA11 for up to 24001 reads until it reads high (clock stretching), and shifts the level of PA12 into the result. The byte is stored at rx_out and the function returns 0; if the clock stays low it returns 2 without storing. PA11 is left high after the last bit.

| Parameter | Type | Description |
|---|---|---|
| `rx_out` | `ptr` | receives the byte as a char |

**Returns** `s32`: 0 on success, 2 on a clock-stretch timeout

- Addresses by version: 4130: 0x080086E0, 4139: 0x08008BE0, 4148: 0x0800942C, 4168: 0x08009740
- Called by: `bms_i2c_bb_read_ack`
- Calls: `LL_GPIO_IsInputPinSet`, `LL_GPIO_ResetOutputPin`, `LL_GPIO_SetOutputPin`, `bms_systick_wait_scaled`
- Confidence: medium

## bms_i2c_bb_send_bit0

**Clock one 0 bit on the bit-banged bus (SDA low with an SCL pulse) with a clock-stretch timeout**

Software bit-bang on PA11 (clock-like) and PA12 (data-like): PA11 is driven low, PA12 is switched to output by writing MODER directly and driven low, then PA11 is released and the routine polls PA11 for up to 24001 reads until it reads high (clock stretching). On success PA11 is driven low again and the function returns 0; if the clock never rises it returns 2. The bit timing uses bms_systick_wait_scaled(1). Called by bms_i2c_bb_read_ack as the acknowledge bit.

**Returns** `u32`: 0 on success, 2 when the clock stayed low

**Notes:** The bus identity (I2C-style on PA11 and PA12) is inferred from the start, stop, acknowledge and byte sequences in the neighbouring functions, not confirmed by a device datasheet.

- Addresses by version: 4130: 0x080083C8, 4139: 0x080088C8, 4148: 0x08009114, 4168: 0x08009428
- Called by: `bms_i2c_bb_read_ack`
- Calls: `LL_GPIO_IsInputPinSet`, `LL_GPIO_ResetOutputPin`, `LL_GPIO_SetOutputPin`, `bms_systick_wait_scaled`
- Confidence: medium

## bms_i2c_bb_send_bit1

**Clock one 1 bit on the bit-banged bus (SDA high with an SCL pulse), with stretch timeout**

PA11 is driven low, PA12 is switched to output and driven high, then PA11 is released and the routine polls PA11 for up to 24001 reads until it reads high. On success PA11 is driven low and it returns 0; otherwise it returns 2. It is the NACK bit that bms_i2c_bb_read_ack sends for the last byte of a read.

**Returns** `u32`: 0 on success, 2 when the clock stayed low

- Addresses by version: 4130: 0x08008604, 4139: 0x08008B04, 4148: 0x08009350, 4168: 0x08009664
- Called by: `bms_i2c_bb_read_ack`
- Calls: `LL_GPIO_IsInputPinSet`, `LL_GPIO_ResetOutputPin`, `LL_GPIO_SetOutputPin`, `bms_systick_wait_scaled`
- Confidence: medium

## bms_i2c_bb_start

**Generate a START (or repeated START) condition on the bit-banged bus**

Drives PA12 to output, releases PA11 and PA12 high, and polls PA11 for up to 24001 reads until it reads high (clock stretching). It then pulls PA12 low while PA11 is high and finally pulls PA11 low, which is the SDA-falls-while-SCL-high start condition. It returns 0 on success, or 2 when the clock line does not rise.

**Returns** `u32`: 0 on success, 2 when the clock line does not rise

- Addresses by version: 4130: 0x08008890, 4139: 0x08008D90, 4148: 0x080095DC, 4168: 0x080098F0
- Called by: `bms_i2c_bb_write_byte_ack`
- Calls: `LL_GPIO_IsInputPinSet`, `LL_GPIO_ResetOutputPin`, `LL_GPIO_SetOutputPin`, `bms_systick_wait_scaled`
- Confidence: medium

## bms_i2c_bb_stop

**Generate a STOP condition on the bit-banged bus (SDA rises while SCL is high)**

Drives SCL low and SDA low, releases SCL and polls it for up to 24001 reads until it reads high, then releases SDA so that it rises while SCL is high. This is the stop condition at the end of a transaction. Callers are bms_4168_080094b4, bms_4168_080096f0, bms_4168_080097d8 and bms_4168_08009a0c.

**Returns** `u32`: 0 on success, 2 when SCL does not rise

- Addresses by version: 4130: 0x0800891C, 4139: 0x08008E1C, 4148: 0x08009668, 4168: 0x0800997C
- Called by: `bms_i2c_bb_read_block`, `bms_i2c_bb_read_ack`, `bms_i2c_bb_write_byte_ack`, `bms_pa12_ready_handshake`
- Calls: `LL_GPIO_IsInputPinSet`, `LL_GPIO_ResetOutputPin`, `LL_GPIO_SetOutputPin`, `bms_systick_wait_scaled`
- Confidence: medium

## bms_i2c_bb_write_block

**Bit-banged I2C write: address, register, then N data bytes with STOP on the last**

Writes param_4 bytes from param_3 to register param_2 of device param_1 on the bit-banged bus. It sends START with the address through bms_4168_080097D8, sends the register byte, then sends data bytes 0 to N-2 with no STOP and the last byte with STOP. The first nonzero ACK status is returned.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | device address byte in write form |
| `param_2` | `u32` | register or command byte |
| `param_3` | `ptr` | source bytes |
| `param_4` | `s32` | number of data bytes |

**Returns** `s32`: 0 on success, otherwise the nonzero ACK status of the failing byte

- Addresses by version: 4130: 0x080084EC, 4139: 0x080089EC, 4148: 0x08009238, 4168: 0x0800954C
- Called by: `bms_i2c_frame_write_crc8`
- Calls: `bms_i2c_bb_write_byte_ack`
- Confidence: high

## bms_i2c_bb_write_byte

**Send one byte MSB first on the bit-banged bus with an SCL pulse per bit**

Configures PA12 as output and drives PA11 low. For each of the 8 bits, from the most significant down, PA12 is set to that bit while SCL is low, PA11 is released, the routine polls PA11 for up to 24001 reads until it reads high (clock stretching), and PA11 is driven low again. The acknowledge bit is not read, and the function returns 0 after all eight bits are sent, or 2 when a clock stretch times out.

| Parameter | Type | Description |
|---|---|---|
| `tx_byte` | `u8` | byte to send; only the low 8 bits are used |

**Returns** `u32`: 0 after eight bits, 2 on a clock-stretch timeout

- Addresses by version: 4130: 0x080087CC, 4139: 0x08008CCC, 4148: 0x08009518, 4168: 0x0800982C
- Called by: `bms_i2c_bb_write_byte_ack`
- Calls: `LL_GPIO_IsInputPinSet`, `LL_GPIO_ResetOutputPin`, `LL_GPIO_SetOutputPin`, `bms_systick_wait_scaled`
- Confidence: medium

## bms_i2c_bb_write_byte_ack

**Send one I2C byte with optional START and STOP, returning the ACK status**

Single-byte transfer on the bit-banged bus. When param_2 is 1 it first generates START (bms_i2c_bb_start, or a repeated START). It shifts out param_1 MSB first with bms_i2c_bb_write_byte, samples the ACK slot with bms_pa12_ready_handshake, and generates STOP with bms_i2c_bb_stop when param_3 is 1. It returns the ACK level: 0 for ACK, 1 for NACK or a timeout.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | byte to send |
| `param_2` | `s32` | START flag (1 to send START first) |
| `param_3` | `s32` | STOP flag (1 to send STOP last) |
| `param_4` | `u32` | initial status word; the ACK sample overwrites it |

**Returns** `u32`: 0 when the byte was ACKed, 1 for NACK or timeout

- Addresses by version: 4130: 0x08008778, 4139: 0x08008C78, 4148: 0x080094C4, 4168: 0x080097D8
- Called by: `bms_i2c_bb_read_block`, `bms_i2c_bb_write_block`
- Calls: `bms_i2c_bb_write_byte`, `bms_i2c_bb_start`, `bms_i2c_bb_stop`, `bms_pa12_ready_handshake`
- Confidence: high

## bms_i2c_frame_read_crc8

**Read a framed I2C response with a CRC-8 trailer (poly 0x07), retrying up to four times**

Reads a device response using the header [param_1, param_2, 0x01]. When the mode at 0x2000062E is 1, it reads param_4 bytes (clamped to 6) with bms_4168_080094B4 and retries four times without a check. Otherwise it reads param_4 + 1 bytes (payload and trailing CRC) into the frame buffer and computes CRC-8 with polynomial 0x07, init 0, MSB first over the header and payload. A match with the trailing byte copies the payload to the destination and decrements the error counter 0x20000630 (not below 0). A mismatch on all four attempts increments the counter (capped at 5) and returns 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | device address byte |
| `param_2` | `u32` | command or register byte |
| `param_3` | `ptr` | destination for the payload |
| `param_4` | `u32` | payload length, clamped to 6 |

**Returns** `u32`: 0 on success, 1 when all attempts failed

**Notes:** The CRC loop is written inline in the decompile, so the polynomial and init are read from the shifts and the 0x07 XOR, not from a named helper.

- Addresses by version: 4130: 0x0800A72C, 4139: 0x0800AC64, 4148: 0x0800B380, 4168: 0x0800B694
- Called by: `bms_4168_0800aa26`
- Calls: `bms_i2c_bb_read_block`
- Confidence: high

## bms_i2c_frame_write_crc8

**Write a framed I2C message with a CRC-8 (poly 0x07) byte, retrying up to four times**

Builds a four-byte frame from param_1, param_2 and param_3. The CRC is computed by crc8_msb_compute with polynomial 7 and init 0 over the header and param_4 + 2 bytes, and stored in the fourth byte of the frame. When the mode at 0x2000062E is 1 it writes param_4 bytes (clamped to 6) with bms_4168_0800954C and retries four times without an error count. Otherwise it writes param_4 + 1 bytes (data plus CRC byte); success decrements the error counter 0x20000630, and four failures increment it (capped at 5) and return 1.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | first header byte (device address) |
| `param_2` | `u32` | second header byte (command or register) |
| `param_3` | `u32` | third header byte, used as the first data byte |
| `param_4` | `u32` | data length, clamped to 6 |

**Returns** `u32`: 0 on success, 1 when all attempts failed

**Notes:** The frame layout is unclear from the decompile: the write starts at byte 2 of the frame, so for a length greater than 1 the position of the CRC byte relative to the data is not certain. Check against the callers before relying on the frame format. The caller in bms_4168_0800aa26 and others are not in this packet.

- Addresses by version: 4130: 0x0800A854, 4139: 0x0800AD8C, 4148: 0x0800B4A8, 4168: 0x0800B7BC
- Called by: `bms_4168_0800af38`, `bms_4168_0800b406`, `bms_4168_0800b5fe`
- Calls: `crc8_msb_compute`, `bms_i2c_bb_write_block`
- Confidence: low
