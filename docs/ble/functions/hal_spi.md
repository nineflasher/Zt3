# BLE - `hal_spi` functions

13 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`ble_spi_read_locked`](#ble_spi_read_locked) | 0x0C0460E8 | Receive-only SPI transfer on the active record, with try-lock and format reapply |
| [`hal_ispi_recv`](#hal_ispi_recv) | 0x0C0326E8 | Polled full-duplex transfer on SPI instance 0 using the receive frame format; asserts if DMA is on |
| [`hal_ispi_send`](#hal_ispi_send) | 0x0C0326C4 | Polled transmit on SPI instance 0 (internal analog/PMU SPI); asserts if TX DMA is configured |
| [`hal_spi_apply_cfg_regs`](#hal_spi_apply_cfg_regs) | 0x0C031DA0 | Program CR1/CPSR/DMACR of an SPI instance from a derived config and select its clock source in the CMU |
| [`hal_spi_apply_format`](#hal_spi_apply_format) | 0x0C031D78 | Load SPI frame-format word and extra byte config into an SPI instance |
| [`hal_spi_build_hw_cfg`](#hal_spi_build_hw_cfg) | 0x0C0320D0 | Translate a user SPI config (rate, bits, flags) into PL022 CR0/CR1/CPSR/DMACR values |
| [`hal_spi_dma_cancel_all`](#hal_spi_dma_cancel_all) | 0x0C031DF4 | Cancel and free the RX and TX GPDMA channels of an SPI instance and release its transfer wait |
| [`hal_spi_dma_rx_done_handler`](#hal_spi_dma_rx_done_handler) | 0x0C031F88 | GPDMA completion callback for SPI receive: free the RX channel and call the user's done callback |
| [`hal_spi_dma_rx_start`](#hal_spi_dma_rx_start) | 0x0C032954 | Start a GPDMA receive of N bytes into a buffer on SPI instance 1, async or blocking |
| [`hal_spi_dma_tx_done_handler`](#hal_spi_dma_tx_done_handler) | 0x0C03200C | GPDMA completion callback for SPI transmit: free TX (and RX) channels, restore format, call user callback |
| [`hal_spi_open_common`](#hal_spi_open_common) | 0x0C0321F8 | Open an SPI instance for one user: build register config, enable clocks on first user, apply config |
| [`hal_spi_tx_poll`](#hal_spi_tx_poll) | 0x0C032378 | Polled transmit-only SPI transfer of N bytes |
| [`hal_spi_txrx_poll`](#hal_spi_txrx_poll) | 0x0C032288 | Polled full-duplex SPI transfer of N bytes using an 8-deep FIFO window |

## ble_spi_read_locked

**Receive-only SPI transfer on the active record, with try-lock and format reapply**

Clocks param_1[1] bytes in from SPI, sending zeros, and stores them at param_2. The request's u16 at +0 selects a 12-byte flag record at 0x20003EE8; if its bits 3 or 4 are set they are cleared and FUN_0C032714 finishes the previous operation. The active SPI record is chosen by the byte at 0x2000391E (20-byte stride from 0x20003920), and the function try-locks 0x20003D05 through the ROM patch thunk at 0x200007F4, returning 0xFFFFFFE1 when the lock is busy. It reapplies that record's format with hal_spi_apply_format, and spins forever if the record's flags byte at +0x0B has its low two bits set (a trap, not an error return). Otherwise it calls hal_spi_txrx_poll with a NULL transmit buffer, restores the format with the saved low bits, and unlocks through the thunk at 0x2000081C.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | request: u16 channel index at +0, u16 byte count at +2 |
| `param_2` | `ptr` | receive buffer |

**Returns** `s32`: 0 on success; otherwise the hal_spi_txrx_poll status (1 early end, -1 bad length, -11 SPI busy), or -31 when the lock is busy

**Notes:** The SPI instance passed to the transfer is not recovered by the decompiler (it shows the r0 left by the format call); the format call uses instance 1. The infinite loop is an assertion-style trap. FUN_0C032714 and the two ROM-patch thunks are not yet described.

- Addresses by version: 219: 0x0C0460E8
- Calls: `hal_spi_apply_format`, `hal_spi_txrx_poll`, `ble_219_0c032714`, `ble_ram_patch_thunk_200007f4`, `ble_ram_patch_thunk_2000081c`
- Confidence: medium

## hal_ispi_recv

**Polled full-duplex transfer on SPI instance 0 using the receive frame format; asserts if DMA is on**

If both DMA bits of instance 0's DMACR byte DAT_20003cf7 (RXDMAE bit 0, TXDMAE bit 1) are clear it calls hal_spi_txrx_poll(0, DAT_20003cf0 (the alternate CR0 word at derived-config +4, i.e. the receive frame size), param_1, param_2, param_3); otherwise it hangs in an assert loop. Single caller 0x0c0401b0, the analog-interface register read, which sends a 32-bit command (reg<<18 | 0x4000000) and takes the returned word >> 2 as the 16-bit register value. Transfer status is not returned.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | transmit buffer |
| `param_2` | `ptr` | receive buffer |
| `param_3` | `u32` | length in bytes |

**Notes:** Name follows the BES hal_ispi convention; mapping of instance 0 to the analog SPI is inferred from the callers.

- Addresses by version: 219: 0x0C0326E8
- Called by: `hal_analogif_reg_read`
- Calls: `hal_spi_txrx_poll`
- Confidence: medium

## hal_ispi_send

**Polled transmit on SPI instance 0 (internal analog/PMU SPI); asserts if TX DMA is configured**

If the DMACR byte DAT_20003cf7 of instance 0's derived config (0x20003cec + 0xb) has TXDMAE (bit 1) clear it calls hal_spi_tx_poll(0, DAT_20003cec (the CR0 word, which encodes the frame size), param_1, param_2) and returns; if TX DMA is enabled it hangs in an assert loop. Callers are the analog-interface register access routines 0x0c0401b0 (read: sends a 24-bit command word first) and 0x0c040290 (write), so instance 0 is the ISPI link to the PMU/analog die; the result of the transfer is discarded here.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | transmit buffer (one or more 32-bit frames) |
| `param_2` | `u32` | length in bytes |

**Notes:** Name follows the BES hal_ispi/analogif convention; 'instance 0 = internal SPI' is inferred from the callers.

- Addresses by version: 219: 0x0C0326C4
- Called by: `hal_analogif_reg_read`, `hal_analogif_reg_write`
- Calls: `hal_spi_tx_poll`
- Confidence: medium

## hal_spi_apply_cfg_regs

**Program CR1/CPSR/DMACR of an SPI instance from a derived config and select its clock source in the CMU**

Calls hal_spi_apply_format(inst, cfg, 0) to load CR0 and the +0x88 extension byte, then writes to the PL022 block from table 0x0c08425c[inst]: CR1 (+4) = u16 at cfg+8, CPSR (+0x10) = byte at cfg+10, DMACR (+0x24) = byte at cfg+0xb. The clock-selector byte at cfg+0x10 (1 = base clock, 2 = doubled clock, 3 = leave unchanged; produced by hal_spi_build_hw_cfg) is compared with the cached DAT_20003d20[inst]; if it changed and is not 3: for instance 1 it rewrites bits 20:18 of CMU register 0x400000a8 inside a BASEPRI critical section (call site 0x0c040e6e logged to DAT_20003d70/74 as in the other BASEPRI helpers) to 0x40000 for selector 2 or 0 otherwise and returns 0; for instance 0 it forwards the selector to bes_cmu_set_rega8_bit21 and returns its result. Returns the (unchanged) selector when nothing had to be done. Callers: hal_spi_open_common, the DMA transfer path 0x0c032408 (re-applying config after a clock change) and 0x0c032774.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | SPI instance (0 = internal/analog SPI, 1 = external SPI) |
| `param_2` | `ptr` | derived hardware config (CR0 words, CR1, CPSR, DMACR, ext bytes, clock selector at +0x10) |

**Returns** `u32`: 0 / result of bes_cmu_set_rega8_bit21, or the selector byte when no clock change was needed

**Notes:** The meaning of 0x400000a8 bits 20:18 (SPI clock mux) is inferred; the decompiler mis-rendered the hal_spi_apply_format call.

- Addresses by version: 219: 0x0C031DA0
- Peripheral registers: `0x400000a8` (RW)
- Called by: `hal_spi_open_common`, `ble_219_0c032408`, `ble_219_0c032774`
- Calls: `hal_spi_apply_format`, `bes_cmu_set_rega8_bit21`
- Confidence: medium

## hal_spi_apply_format

**Load SPI frame-format word and extra byte config into an SPI instance**

Looks up the SPI register block for instance param_1 in the pointer table at 0x0c08425c and writes two values from a config struct: the 32-bit word goes to register +0x00 (CR0, frame format/clock fields) and a byte goes to register +0x88 (BES-specific extension register). param_3 selects between two sub-records of the config: 0 uses word at param_2+0x0 and byte at param_2+0xc, non-zero uses word at param_2+0x4 and byte at param_2+0xd. Table at 0x0c08425c holds the register-block base pointers of the SPI instances; register layout matches an ARM PrimeCell PL022 SSP (CR0 +0, CR1 +4, DR +8, SR +0xc, ICR +0x20) with a BES extension at +0x88. Called from SPI open/configure routines and from the transfer wrapper at 0x0c0460e8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | SPI instance index into the register-pointer table |
| `param_2` | `ptr` | config struct holding the two (word, byte) records |
| `param_3` | `u32` | 0 = first record, non-zero = second record |

**Notes:** Which two records the config holds (e.g. master vs slave / two chip-select profiles) is not visible from this function; the semantics of register +0x88 are undocumented.

- Addresses by version: 219: 0x0C031D78
- Called by: `hal_spi_apply_cfg_regs`, `hal_spi_dma_cancel_all`, `hal_spi_dma_tx_done_handler`, `ble_219_0c0328cc`, `ble_spi_read_locked`
- Confidence: medium

## hal_spi_build_hw_cfg

**Translate a user SPI config (rate, bits, flags) into PL022 CR0/CR1/CPSR/DMACR values**

param_1 is the user config: +0 rate (Hz), +4 flags byte (bit0 SPH clk_delay_half, bit1 SPO polarity, bit2 slave, bit3 rx DMA, bit4 tx DMA, bit5 extra CR1 bit 11, bit7 = do not enable), +5 chip select 0..3, +6 tx bits, +7 rx bits, +8 rx frame bits. The source clock comes from thunk 0x2000022c; if rate*2 exceeds it the doubled clock is chosen (selector 2, clock*2) else selector 1, stored at out+0x10. Asserts (infinite loops): rate <= clock/2, rate >= clock/16256, tx/rx bits in 4..32, rx frame bits 0 or in rx_bits+1..32, cs <= 3. Divider: div = ceil(clock/rate); CPSDVSR = max(2, even-rounded (div+255)>>8, capped 254); SCR = min(ceil((div-1)/CPSDVSR) - 1, 255). Writes out+0 = CR0 = SCR<<8 | SPH<<7 | SPO<<6 | (tx_bits-1)<<16, out+8 = CR1 = slave<<2 | cs<<7 | bit5<<11 | SSE (bit1) unless flags bit7, out+10 = CPSDVSR, out+0xb = DMACR (flags bits 4:3 -> TXDMAE/RXDMAE), out+0xc = 0, and the receive variant: if rx frame bits == 0, out+0xd = 0 and out+4 = CR0 with DSS = rx_bits-1; else out+0xd = (rx_bits-1) | 0x60 and out+4 = CR0 with DSS = rx_frame_bits-1 (BES extension register +0x88: receive only rx_bits of a longer frame). Single caller hal_spi_open_common.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | user SPI configuration (HAL_SPI_CFG_T-like, see description) |
| `param_2` | `ptr` | output: derived register config (0x11 bytes used) |

**Notes:** Field names follow the BES HAL_SPI_CFG_T; the exact meaning of flags bit5/bit7 and of thunk 0x2000022c (SPI source clock) is inferred.

- Addresses by version: 219: 0x0C0320D0
- Called by: `hal_spi_open_common`
- Calls: `ble_ram_patch_thunk_2000022c`
- Confidence: medium

## hal_spi_dma_cancel_all

**Cancel and free the RX and TX GPDMA channels of an SPI instance and release its transfer wait**

Inside a BASEPRI critical section (call site 0x0c031e04 logged to DAT_20003d70/DAT_20003d74) it reads and resets to 0xff the TX channel byte DAT_20003d1c[inst] and the RX channel byte DAT_20003d18[inst], and reads the user callback pointer DAT_20003d10[inst]. For each channel that was valid (!= 0xff) it calls hal_gpdma_cancel and hal_gpdma_free_chan. For instance 1 it then restores the frame format of the currently selected chip-select slot with hal_spi_apply_format(1, &DAT_20003920 + DAT_2000391e*0x14, 0). If a callback was registered it calls the RAM-patch routine 0x2000081c with the address of the per-instance byte 0x20003d04[inst], which the DMA done handlers also call (probably a wait-flag/semaphore release for the transfer owner). Single caller hal_spi_close (0x0c031ea4) when a TX DMA channel is still allocated at close time.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | SPI instance 0 or 1 |

**Notes:** Purpose of thunk 0x2000081c and of byte 0x20003d04[inst] is a guess.

- Addresses by version: 219: 0x0C031DF4
- Called by: `ble_219_0c031ea4`
- Calls: `hal_gpdma_cancel`, `hal_gpdma_free_chan`, `hal_spi_apply_format`, `ble_ram_patch_thunk_2000081c`
- Confidence: medium

## hal_spi_dma_rx_done_handler

**GPDMA completion callback for SPI receive: free the RX channel and call the user's done callback**

GPDMA callback with the signature (channel id, remaining size, error flag, LLI pointer) used by hal_gpdma_chan_irq_handler. Inside a BASEPRI critical section (call site 0x0c031f98 logged) it matches param_1 against the RX channel bytes DAT_20003d18 (instance 0) and 0x20003d19 (instance 1) and marks the matching entry 0xff; an unknown channel is ignored. For a match it calls hal_gpdma_free_chan(channel), then the RAM-patch routine 0x2000081c with &0x20003d04[inst] (releases the transfer wait), and finally the registered RX callback DAT_20003d08[inst] with param_3 (the DMA error flag) if non-NULL. No direct callers: registered as the DMA completion callback by the SPI DMA receive path. Sibling of hal_spi_dma_tx_done_handler.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | GPDMA channel id that completed |
| `param_2` | `u32` | remaining transfer size (unused) |
| `param_3` | `u32` | DMA error flag, forwarded to the user callback |

**Notes:** The role of thunk 0x2000081c is inferred.

- Addresses by version: 219: 0x0C031F88
- Calls: `hal_gpdma_free_chan`, `ble_ram_patch_thunk_2000081c`
- Confidence: medium

## hal_spi_dma_rx_start

**Start a GPDMA receive of N bytes into a buffer on SPI instance 1, async or blocking**

Receives param_2 bytes into the buffer param_1 on SPI instance 1 through GPDMA. The frame width comes from the chip-select record at DAT_20003920 + DAT_2000391E*0x14 (bits 16..20 of its first word plus 1 select 1, 2 or 4 bytes per unit); address and length must be multiples of that width, otherwise -1 or -2. The transfer is split into descriptors of at most 0xFFF units built in the static LLI pool at 0x20003970 (hal_gpdma_init_desc) and started with hal_gpdma_sg_start_linear, or hal_gpdma_start for a single descriptor. The RX channel is taken from peripheral request 0x10 (hal_gpdma_get_chan) and kept in byte 1 of DAT_20003D18, which is hard-wired to instance 1; the completion callback is hal_spi_dma_rx_done_handler and param_3 is stored in DAT_20003D0C. The body holds the object at DAT_20003D05 (RAM-patch thunks 0x200007F4 and 0x2000081C) and refuses to start while GPDMA status 0x40007000 bit 7 and 0x4000700C bit 4 are both set. When param_3 is zero it busy-waits on 0x40007004 bit 1 and channel busy, then frees the channel and returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | destination buffer address, aligned to the frame width |
| `param_2` | `u32` | length in bytes, a multiple of the frame width |
| `param_3` | `u32` | nonzero = asynchronous (completion via callback), zero = wait until done |

**Returns** `s32`: 0 on success or async start; -1 length not aligned, -2 buffer not aligned, -4 GPDMA not ready, -5 RX channel already active, -6 no free channel, -7 start failed, -31 lock not obtained

**Notes:** Receive direction and the sync/async meaning of param_3 are inferred from the callback and the wait loop. Instance 1 is hard-wired in the code (byte 1 of DAT_20003D18).

- Addresses by version: 219: 0x0C032954
- Peripheral registers: `0x40007000` (AR), `0x40007004` (R), `0x4000700c` (R)
- Calls: `hal_gpdma_init_desc`, `hal_gpdma_sg_start_linear`, `hal_gpdma_get_chan`, `hal_gpdma_free_chan`, `hal_gpdma_chan_busy`, `ble_ram_patch_thunk_200007f4`, `ble_ram_patch_thunk_2000081c`
- Confidence: medium

## hal_spi_dma_tx_done_handler

**GPDMA completion callback for SPI transmit: free TX (and RX) channels, restore format, call user callback**

GPDMA callback (channel id, remaining, error flag, LLI). Inside a BASEPRI critical section (call site 0x0c03201c logged) it matches param_1 against the TX channel bytes DAT_20003d1c (instance 0) / 0x20003d1d (instance 1); on a match it marks that entry 0xff and also fetches and resets the instance's RX channel byte DAT_20003d18[inst]. Outside the section it frees the TX channel (hal_gpdma_free_chan), and if an RX channel was allocated cancels and frees it too; for instance 1 it restores the frame format of the current chip-select slot via hal_spi_apply_format(1, &DAT_20003920 + DAT_2000391e*0x14, 0); then calls the RAM-patch routine 0x2000081c with &0x20003d04[inst] and finally the user callback DAT_20003d10[inst](param_3) if set. The DMA transfer routine 0x0c032408 installs this function (0x0c03200d) as the channel callback only when the user supplied a callback, so it only runs for asynchronous transfers. No direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | GPDMA channel id that completed |
| `param_2` | `u32` | remaining transfer size (unused) |
| `param_3` | `u32` | DMA error flag, forwarded to the user callback |

- Addresses by version: 219: 0x0C03200C
- Calls: `hal_gpdma_cancel`, `hal_gpdma_free_chan`, `hal_spi_apply_format`, `ble_ram_patch_thunk_2000081c`
- Confidence: medium

## hal_spi_open_common

**Open an SPI instance for one user: build register config, enable clocks on first user, apply config**

param_2 is the user config, param_3 the per-instance derived-config storage (0x20003cec for instance 0; &DAT_20003920 + cs*0x14 for instance 1). Asserts that flags bit 2 (slave mode) is clear, then fills param_3 with hal_spi_build_hw_cfg. On the very first open (DAT_20003d22 == 0) it sets the flag and initialises the DMA channel bytes DAT_20003d18 (RX, two instances) and DAT_20003d1c (TX) to 0xff. If the user mask DAT_20003d00[inst] is 0 it sets it to 1 << cs (cs = config byte +5) and powers the block: hal_cmu_clock_enable and hal_cmu_reset_clear for the two module ids at ROM 0x0c084270[inst*2] and [inst*2+1]; otherwise it only ORs the user bit in. Finally hal_spi_apply_cfg_regs(inst, param_3) programs the registers. Always returns 0. Callers: 0x0c032688 (instance 0 open, the internal SPI to the analog/PMU block) and 0x0c032714 (instance 1 open with up to four chip-select configs, under a critical section). Reverse operation is 0x0c031ea4 (close).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | SPI instance 0 or 1 |
| `param_2` | `ptr` | user SPI configuration |
| `param_3` | `ptr` | storage for the derived register config of this instance/cs |
| `param_4` | `u32` | unused (decompiler artefact) |

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C0321F8
- Called by: `ble_219_0c032688`, `ble_219_0c032714`
- Calls: `hal_spi_apply_cfg_regs`, `hal_spi_build_hw_cfg`, `hal_cmu_clock_enable`, `hal_cmu_reset_clear`
- Confidence: high

## hal_spi_tx_poll

**Polled transmit-only SPI transfer of N bytes**

Same frame-size decoding and argument validation as the full-duplex routine (element width 1/2/4 bytes from bits 20:16 of param_2; returns -1 if length is 0 or not width-aligned). Loops while the active flag (reg +4 bit1) is set and bytes remain, writing the next element to DR (+8) whenever SR (+0xc) bit1 (TX not full) is set; received data is not read. After the loop it waits until reg+4 bit1 clears or SR bit4 (BSY) drops, and returns 1 if not all bytes were sent else 0. Table at 0x0c08425c holds the register-block base pointers of the SPI instances; register layout matches an ARM PrimeCell PL022 SSP (CR0 +0, CR1 +4, DR +8, SR +0xc, ICR +0x20) with a BES extension at +0x88.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | SPI instance index |
| `param_2` | `u32` | SPI format/CR0 value; bits 20:16 give frame size minus one |
| `param_3` | `ptr` | tx buffer |
| `param_4` | `u32` | length in bytes |

**Returns** `s32`: 0 = sent, 1 = ended early, -1 = bad length/alignment

**Notes:** Single caller 0x0c0326c4 (SPI send wrapper).

- Addresses by version: 219: 0x0C032378
- Called by: `hal_ispi_send`
- Confidence: medium

## hal_spi_txrx_poll

**Polled full-duplex SPI transfer of N bytes using an 8-deep FIFO window**

Derives the frame size in bits from ((param_2 & 0x1fffff) >> 16) + 1 and maps it to an element width of 1 (<=8 bits), 2 (<=16 bits) or 4 bytes; returns -1 if param_5 (byte count) is zero or not a multiple of the element width. Returns -11 (0xfffffff5) if the SPI status register (+0xc) BSY bit4 is set, otherwise waits for SR bit2 to clear, clears all interrupt flags (ICR +0x20 = 0xffffffff) and runs a loop: while the enable/active flag (reg +4 bit1) is set it pushes the next tx element into DR (+8) when SR bit1 (TX not full) is set, never more than 8 bytes ahead of what was received, using zero as dummy data when param_3 (tx buffer) is NULL, and pops an element from DR into param_4 (rx buffer, must be non-NULL) when SR bit2 (RX not empty) is set. On completion it waits for the busy/active state to end. Table at 0x0c08425c holds the register-block base pointers of the SPI instances; register layout matches an ARM PrimeCell PL022 SSP (CR0 +0, CR1 +4, DR +8, SR +0xc, ICR +0x20) with a BES extension at +0x88.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | SPI instance index |
| `param_2` | `u32` | SPI format/CR0 value; bits 20:16 give frame size minus one |
| `param_3` | `ptr` | tx buffer or NULL for dummy zero data |
| `param_4` | `ptr` | rx buffer |
| `param_5` | `u32` | transfer length in bytes |

**Returns** `s32`: 0 = all bytes exchanged, 1 = transfer ended early (active flag dropped), -1 = bad length/alignment, -11 = SPI busy

**Notes:** Meaning of register +4 bit1 as a loop-continue flag (PL022 CR1.SSE) and the return value 1 are inferred from the control flow.

- Addresses by version: 219: 0x0C032288
- Called by: `hal_ispi_recv`, `ble_spi_read_locked`
- Confidence: medium
