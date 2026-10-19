# BLE - `hal_uart` functions

15 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`hal_trace_uart0_putc`](#hal_trace_uart0_putc) | 0x0C045AC8 | Output one character on UART0 by polling (trace/console sink) |
| [`hal_uart_apply_line_config`](#hal_uart_apply_line_config) | 0x0C03418C | Apply a UART line configuration (LCR_H, DMACR, FIFO levels, flow control, baud) and enable it |
| [`hal_uart_close_internal`](#hal_uart_close_internal) | 0x0C033ACC | Close a UART instance: disable its NVIC IRQ, free its DMA channels, reset and gate its clocks |
| [`hal_uart_install_irq_handler`](#hal_uart_install_irq_handler) | 0x0C033D94 | Store UART callback, argument and ISR entry for instance param_1 |
| [`hal_uart_putc_poll`](#hal_uart_putc_poll) | 0x0C033D18 | Write one byte to a UART transmit register, waiting for FIFO space |
| [`hal_uart_rx_dma_busy`](#hal_uart_rx_dma_busy) | 0x0C0342A4 | Return 1 while the UART RX DMA channel of an instance is running |
| [`hal_uart_rx_dma_complete`](#hal_uart_rx_dma_complete) | 0x0C033610 | GPDMA completion callback for UART RX: free the channel and report bytes received |
| [`hal_uart_rx_dma_start`](#hal_uart_rx_dma_start) | 0x0C033E04 | Start a UART RX DMA into a buffer, chaining descriptors in 0xFFF-byte pieces |
| [`hal_uart_set_baud_divisor`](#hal_uart_set_baud_divisor) | 0x0C0334C8 | Program PL011 IBRD and FBRD of a UART instance for a baud rate, 16x or 8x oversampling |
| [`hal_uart_set_baud_rate`](#hal_uart_set_baud_rate) | 0x0C033CA8 | Change the baud rate of a running UART: disable, reprogram divisor, relatch LCR_H, enable |
| [`hal_uart_set_irq_mask`](#hal_uart_set_irq_mask) | 0x0C033D50 | Write the UART interrupt mask register and return its previous value |
| [`hal_uart_tx_dma_busy`](#hal_uart_tx_dma_busy) | 0x0C034290 | Return 1 while the UART TX DMA channel of an instance is running |
| [`hal_uart_tx_dma_complete`](#hal_uart_tx_dma_complete) | 0x0C033530 | GPDMA completion callback for UART TX: free the channel and report bytes sent |
| [`hal_uart_tx_dma_start_sg`](#hal_uart_tx_dma_start_sg) | 0x0C0336B0 | Start a UART TX DMA from a segment list, chunked as linear, ping-pong, ring or scatter |
| [`hal_uart_tx_dma_stop`](#hal_uart_tx_dma_stop) | 0x0C033BD8 | Stop the UART TX DMA of an instance, free its channel and return the bytes not sent |

## hal_trace_uart0_putc

**Output one character on UART0 by polling (trace/console sink)**

Thin wrapper: hal_uart_putc_poll(0, param_1), blocking until the UART0 TX FIFO has space. No direct callers: it is installed as a character-output callback for the trace/printf path.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | character to send |

- Addresses by version: 219: 0x0C045AC8
- Calls: `hal_uart_putc_poll`
- Confidence: medium

## hal_uart_apply_line_config

**Apply a UART line configuration (LCR_H, DMACR, FIFO levels, flow control, baud) and enable it**

On the first call it sets all TX and RX DMA channel slots to 0xFF and marks the DMA layer initialised (DAT_2000AA7C). It reads a config record: byte 0 (0..4) indexes a five-word ROM table at 0x0C074574 used as the base LCR_H value (probably the parity bits), byte 1 (0 or 1) sets STP2 (LCR_H bit 3), byte 2 (0..3) sets the word length (5 to 8 bits, LCR_H bits 6:5), byte 3 (0..3) sets hardware flow control (CR bit 14 RTS and/or bit 15 CTS), and byte 12 selects DMACR bits 0, 1 and 2, with bit 0 also setting LCR_H bit 15. Bytes 4 and 5 give the RX and TX FIFO levels for IFLS (0x34), and the word at +8 is the baud rate. After waiting for BUSY it disables the UART and FIFO, masks and clears interrupts, writes LCR_H, DMACR, the BES register +0x54 = 3 and the baud (hal_uart_set_baud_divisor), then IFLS, and finally CR = flow bits + 0x301 (RXE, TXE, UARTEN). It always returns 0 and traps on out-of-range config fields.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | UART instance 0..2 |
| `param_2` | `ptr` | config record: byte 0 parity index, byte 1 stop bits, byte 2 data bits, byte 3 flow control, byte 4 RX FIFO level, byte 5 TX FIFO level, u32 baud at +8, byte 12 DMA flags |
| `param_3` | `u32` | not used |
| `param_4` | `u32` | not used |

**Returns** `u32`: always 0

**Notes:** The parity meaning of the ROM table at 0x0C074574 is a guess; the other field meanings follow from the PL011 offsets used.

- Addresses by version: 219: 0x0C03418C
- Calls: `hal_uart_set_baud_divisor`
- Confidence: medium

## hal_uart_close_internal

**Close a UART instance: disable its NVIC IRQ, free its DMA channels, reset and gate its clocks**

Writes the NVIC clear-enable register (ICER, 0xE000E180 region, word n/32) for the instance IRQ byte unless it is the 0x4C sentinel or negative. If the UART DMA layer is initialised (DAT_2000AA7C), it cancels and frees the TX channel (DAT_2000AA8C) and the RX channel (DAT_2000AAB8) under a BASEPRI section and sets both slots to 0xFF. It then clears UARTEN (CR bit 0) and the FIFO enable (LCR_H bit 4), asserts the resets of module ids +6 and +5 of the instance record (hal_cmu_reset_set) and gates their clocks off (hal_cmu_clock_disable). It always returns 0; the open side is hal_uart_apply_line_config.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | UART instance 0..2 |

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C033ACC
- Peripheral registers: `0xe000e100` (A)
- Called by: `hal_uart_close`, `hal_uart_open`
- Calls: `hal_gpdma_cancel`, `hal_gpdma_free_chan`, `hal_cmu_clock_disable`, `hal_cmu_reset_set`
- Confidence: high

## hal_uart_install_irq_handler

**Store UART callback, argument and ISR entry for instance param_1**

For instance 0..2 (else infinite-loop trap) stores param_2 into the word array at 0x2000aaac, param_3 into the byte array at 0x2000aac8 and writes the address of the code at 0x0c033c34 (the common UART interrupt service routine) into the 4-byte-entry handler table at 0x2000aa80. No direct callers - invoked indirectly during UART open.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | UART instance 0..2 |
| `param_2` | `u32` | callback / context value stored per instance |
| `param_3` | `u32` | small per-instance value stored in a byte array (low byte only) |

**Notes:** Exact roles of param_2/param_3 are not clear; entry reached via function pointer.

- Addresses by version: 219: 0x0C033D94
- Confidence: low

## hal_uart_putc_poll

**Write one byte to a UART transmit register, waiting for FIFO space**

param_1 selects one of 3 UART instances (register-block pointers in a table at 0x0c085890, stride 12 bytes); larger values trap in an infinite loop. Spins until flag register +0x18 bit5 (TXFF, PL011 layout) is clear, then, if bit1 of register +0x48 is not set, stores param_2 into the data register (+0x00); if that bit is set (probably TX DMA active) the code traps in an infinite loop. Used by the trace/print path (0x0c045ac8, 0x0c033150).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | UART instance 0..2 |
| `param_2` | `u32` | byte to transmit |

**Notes:** Offset +0x48 bit1 meaning (DMA enable) is a guess; layout is PL011-like.

- Addresses by version: 219: 0x0C033D18
- Called by: `ble_uart_print_values`, `hal_trace_uart0_putc`
- Confidence: medium

## hal_uart_rx_dma_busy

**Return 1 while the UART RX DMA channel of an instance is running**

Returns 0 when no RX channel is held for instance param_1 (slot DAT_2000AAB8 is 0xFF). Otherwise it returns the result of hal_gpdma_chan_busy for that channel.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | UART instance 0..2 |

**Returns** `u32`: 1 busy, 0 idle or no channel

- Addresses by version: 219: 0x0C0342A4
- Called by: `ble_uart_tx_dma_pump`
- Calls: `hal_gpdma_chan_busy`
- Confidence: high

## hal_uart_rx_dma_complete

**GPDMA completion callback for UART RX: free the channel and report bytes received**

GPDMA callback with (channel id, remaining, error flag). It finds the UART instance whose RX channel slot (DAT_2000AAB8..BA) holds the channel and clears that slot under a BASEPRI section. Outside the section it reads the remaining count (hal_gpdma_get_sg_remain_size), frees the channel (hal_gpdma_free_chan) and, when a callback is set at DAT_2000AAC8[inst], calls it as (instance, received, error flag), where received = DAT_2000AABC[inst] minus remaining (0 if negative). Unknown channels are ignored. This is the counterpart of hal_uart_rx_dma_start.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | GPDMA channel id (controller << 4 \| channel) |
| `param_2` | `u32` | remaining units from the IRQ, not used (recomputed from the channel) |
| `param_3` | `u32` | error flag, forwarded to the user callback |

- Addresses by version: 219: 0x0C033610
- Calls: `hal_gpdma_free_chan`, `hal_gpdma_get_sg_remain_size`
- Confidence: high

## hal_uart_rx_dma_start

**Start a UART RX DMA into a buffer, chaining descriptors in 0xFFF-byte pieces**

Receives param_3 bytes from UART instance param_1 into the buffer param_2 by GPDMA, with completion callback hal_uart_rx_dma_complete. The length is split into ceil(len / 0xFFF) descriptors. When param_4 is zero and param_5 is set it only reports the count in *param_5 (1 reported as 0) and returns 0. Lengths above 0x1FFD need param_4 (a descriptor buffer) and an output count at least as large. Otherwise it takes a channel from request byte +8 of the instance record (hal_gpdma_get_chan, policy 0), records it in DAT_2000AAB8[inst] and the length in DAT_2000AABC[inst], builds the descriptors with hal_gpdma_init_desc and starts them with hal_gpdma_start (one descriptor) or hal_gpdma_sg_start_linear. Zero length returns 0 without starting, and any start failure frees the channel. It traps when DMACR bit 1 is clear or the IRQ byte is 0x4C.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | UART instance 0..2 |
| `param_2` | `ptr` | destination buffer |
| `param_3` | `s32` | length in bytes |
| `param_4` | `u32` | 0 = report descriptor count only (with param_5), nonzero = start |
| `param_5` | `ptr` | in/out descriptor count, may be NULL |

**Returns** `s32`: 0 started, zero-length or count reported; 1 RX already active; 2 no free GPDMA channel; 3 descriptor build or start failed; -1 large request without descriptor buffer; -2 descriptor buffer too small

- Addresses by version: 219: 0x0C033E04
- Called by: `ble_uart_tx_dma_pump`
- Calls: `hal_gpdma_init_desc`, `hal_gpdma_sg_start_linear`, `hal_gpdma_start`, `hal_gpdma_get_chan`, `hal_gpdma_free_chan`
- Confidence: medium

## hal_uart_set_baud_divisor

**Program PL011 IBRD and FBRD of a UART instance for a baud rate, 16x or 8x oversampling**

For UART instance param_1 (0..2) the register block comes from the 12-byte instance table at 0x0C085890 (stride 12: +0 PL011 base pointer, +4 NVIC IRQ number with 0x4C as sentinel, +5 and +6 module ids for reset and clock, +7 TX DMA request, +8 RX DMA request). The instance's clock path is selected by one of three CMU helpers (0x0C040D58, 0x0C040DB0, 0x0C040E08 for instances 0, 1, 2). The peripheral clock comes from RAM-patch thunk 0x2000022C and clk/16 is the base, switching to clk/8 when the baud rate is above clk/16. The divisor is a 6-bit fixed-point value (baud/2 + base*64) / baud; its integer part goes to register +0x24 (IBRD) and the fraction to +0x28 (FBRD). A divisor outside 1..0xFFFE traps in an infinite loop. LCR_H is not written, so the caller must rewrite it, as hal_uart_set_baud_rate does. This is part of the UART group with hal_uart_set_baud_rate, hal_uart_apply_line_config, hal_uart_close_internal, hal_uart_tx_dma_start_sg and hal_uart_rx_dma_start.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | UART instance 0..2 |
| `param_2` | `u32` | baud rate in Hz |

**Notes:** PL011 register layout is the basis for the offsets. The clock selector helpers are inferred from their names and the instance order.

- Addresses by version: 219: 0x0C0334C8
- Called by: `hal_uart_set_baud_rate`, `hal_uart_open`, `hal_uart_apply_line_config`
- Calls: `bes_cmu_set_reg70_sel_b2`, `bes_cmu_set_reg70_sel_b7`, `bes_cmu_set_reg70_sel_b12`, `ble_ram_patch_thunk_2000022c`
- Confidence: high

## hal_uart_set_baud_rate

**Change the baud rate of a running UART: disable, reprogram divisor, relatch LCR_H, enable**

Requires the instance clock (module id +6 of the record, when below 0x9A) to be on and the UART to be enabled (CR bit 0); otherwise it returns 1. If the transmitter is not busy (FR bit 3 clear) it clears CR bit 0, programs the divisor with hal_uart_set_baud_divisor, rewrites LCR_H to latch the new IBRD and FBRD (PL011 requires this), and sets CR bit 0 again, returning 0. If the UART is busy it returns 2 and changes nothing. Instance numbers above 2 trap.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | UART instance 0..2 |
| `param_2` | `u32` | baud rate in Hz |

**Returns** `u32`: 0 changed, 1 clock off or UART disabled, 2 transmitter busy

- Addresses by version: 219: 0x0C033CA8
- Calls: `hal_uart_set_baud_divisor`, `hal_cmu_clock_is_enabled`
- Confidence: high

## hal_uart_set_irq_mask

**Write the UART interrupt mask register and return its previous value**

param_1 selects UART 0..2 from the table at 0x0c085890 (otherwise trap). Reads the old value of register +0x38 (PL011 IMSC), then writes param_2. If bit6 (receive timeout) is being newly enabled while the per-UART DMA channel slot DAT_2000aa8c[param_1] is not -1 (i.e. an RX DMA is configured) the function traps in an infinite loop as an assertion. Returns the old mask.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | UART instance 0..2 |
| `param_2` | `u32` | new interrupt mask |

**Returns** `u32`: previous interrupt mask value

**Notes:** Meaning of DAT_2000aa8c as an RX DMA channel array (-1 = none) is inferred.

- Addresses by version: 219: 0x0C033D50
- Called by: `ble_uart_port_start`
- Confidence: medium

## hal_uart_tx_dma_busy

**Return 1 while the UART TX DMA channel of an instance is running**

Returns 0 when no TX channel is held for instance param_1 (slot DAT_2000AA8C is 0xFF). Otherwise it returns the result of hal_gpdma_chan_busy for that channel.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | UART instance 0..2 |

**Returns** `u32`: 1 busy, 0 idle or no channel

- Addresses by version: 219: 0x0C034290
- Called by: `ble_uart_rx_dma_pump`
- Calls: `hal_gpdma_chan_busy`
- Confidence: high

## hal_uart_tx_dma_complete

**GPDMA completion callback for UART TX: free the channel and report bytes sent**

GPDMA callback with (channel id, remaining, error flag). Under a BASEPRI section it finds the UART instance whose TX channel slot (DAT_2000AA8C, DAT_2000AA8D or DAT_2000AA8E) matches and, for mode 0, clears that slot. Outside the section, mode 0 reads the remaining count (hal_gpdma_get_sg_remain_size), frees the channel (hal_gpdma_free_chan) and calls the user callback at DAT_2000AAAC[inst] with bytes sent = DAT_2000AA94[inst] minus remaining (0 if negative). Modes 1 to 3 keep the channel: mode 1 reports half the total and the other modes report 0. The user callback receives (instance, count, error flag, 0), where the error flag is the third argument of this callback. The total in DAT_2000AA94 is the first segment's length (see hal_uart_tx_dma_start_sg), so the reported count is exact only for single-segment transfers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | GPDMA channel id (controller << 4 \| channel) |
| `param_2` | `u32` | remaining units from the IRQ, not used (recomputed from the channel) |
| `param_3` | `u32` | error flag, forwarded to the user callback |

**Notes:** The multi-segment accuracy caveat is from reading the code, not from a test.

- Addresses by version: 219: 0x0C033530
- Calls: `hal_gpdma_free_chan`, `hal_gpdma_get_sg_remain_size`
- Confidence: medium

## hal_uart_tx_dma_start_sg

**Start a UART TX DMA from a segment list, chunked as linear, ping-pong, ring or scatter**

Builds and starts a GPDMA transmit on UART instance param_1 from param_3 segments of three words {address, length, flags}, with param_8 as the maximum chunk size (1..0xFFF). Mode param_7 selects the split: 0 linear chunks, 1 two equal halves (the length must divide exactly), 2 a ring of at least two equal pieces, 3 scatter-gather with chunks for every segment. When param_4 is NULL and param_5 is set it only reports the descriptor count in *param_5 (1 is reported as 0). Otherwise it fills the LLI list (caller buffer, or a 16-byte stack buffer for one descriptor) with hal_gpdma_init_desc. Under a BASEPRI section it takes a GPDMA channel from request byte +7 of the instance record (hal_gpdma_get_chan) and records it in DAT_2000AA8C[inst], the mode in DAT_2000AA90[inst], the first segment length in DAT_2000AA94[inst] and the optional user word param_6 in DAT_2000AAA0[inst]. It writes 0x40 to the PL011 ICR (+0x44) to clear the RX-timeout interrupt and starts the list with hal_gpdma_sg_start_linear. The completion callback 0x0C033530 is installed in the descriptors. The function traps if the instance IRQ byte is 0x4C or DMACR bit 0 is clear.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | UART instance 0..2 |
| `param_2` | `ptr` | segment array, three u32 per entry: address, length, flags |
| `param_3` | `u32` | number of segments |
| `param_4` | `ptr` | LLI descriptor buffer (16 bytes each), NULL for query or stack buffer |
| `param_5` | `ptr` | in/out descriptor count, may be NULL |
| `param_6` | `ptr` | optional user word stored per instance, may be NULL |
| `param_7` | `u8` | mode: 0 linear, 1 ping-pong halves, 2 ring, 3 scatter-gather |
| `param_8` | `u32` | maximum chunk size in bytes (1..4095) |

**Returns** `u32`: 0 started or count reported; 1 TX already active; 2 descriptor build failed; 3 slot taken meanwhile; 4 no free GPDMA channel; 5 start failed; 0xFFFFFFFF no segments; 0xFFFFFFFE chunk size out of range; 0xFFFFFFFD NULL segment address; 0xFFFFFFFC zero length; 0xFFFFFFFB ping-pong split not exact; 0xFFFFFFFA ping-pong count above length; 0xFFFFFFF9 ring overflow; 0xFFFFFFF5 descriptor buffer needed; 0xFFFFFFF4 descriptor buffer too small

**Notes:** Only the first segment length is stored in DAT_2000AA94, which feeds hal_uart_tx_dma_complete. Modes 2 and 3 are read from the split arithmetic, not from a test.

- Addresses by version: 219: 0x0C0336B0
- Called by: `hal_uart_tx_dma_start`
- Calls: `hal_gpdma_init_desc`, `hal_gpdma_sg_start_linear`, `hal_gpdma_get_chan`, `hal_gpdma_free_chan`
- Confidence: medium

## hal_uart_tx_dma_stop

**Stop the UART TX DMA of an instance, free its channel and return the bytes not sent**

Under a BASEPRI section it clears the TX channel slot DAT_2000AA8C[inst] to 0xFF and keeps the old value. If a channel was held it stops it with hal_gpdma_stop, reads the remaining units with hal_gpdma_get_sg_remain_size, frees it with hal_gpdma_free_chan and returns that remaining count. With no active TX it returns 0. The user TX callback is not called for an aborted transfer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | UART instance 0..2 |

**Returns** `u32`: units not yet sent; 0 when no TX was active

- Addresses by version: 219: 0x0C033BD8
- Called by: `hal_uart_tx_dma_stop_checked`
- Calls: `hal_gpdma_stop`, `hal_gpdma_free_chan`, `hal_gpdma_get_sg_remain_size`
- Confidence: high
