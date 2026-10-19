# VCU - `can` functions

29 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`can_base_init`](#can_base_init) | 0x0800AB0C | Configure CAN1 master control and test mode via freeze mode |
| [`can_baudrate_default_para_init`](#can_baudrate_default_para_init) | 0x0800ABB4 | Fill can_baudrate_type with defaults (div 1, RSAW 2tq, BTS1 4tq, BTS2 3tq) |
| [`can_baudrate_set`](#can_baudrate_set) | 0x0800ABC4 | Program CAN1 bit timing (BTMG) while in freeze mode |
| [`can_default_para_init`](#can_default_para_init) | 0x0800ACA8 | Zero the can_base_type configuration struct |
| [`can_filter_init`](#can_filter_init) | 0x0800ACBA | Configure one CAN receive filter bank (SDK can_filter_init) |
| [`can_flag_clear`](#can_flag_clear) | 0x0800ADE8 | Clear a CAN status flag selected by SDK flag code (SDK can_flag_clear) |
| [`can_flag_get`](#can_flag_get) | 0x0800AE50 | Read a CAN status flag selected by SDK flag code (SDK can_flag_get) |
| [`can_interrupt_enable`](#can_interrupt_enable) | 0x0800AF14 | Set or clear CAN interrupt-enable bits (SDK can_interrupt_enable) |
| [`can_message_receive`](#can_message_receive) | 0x0800AF28 | Read one frame from a CAN RX FIFO mailbox and release the FIFO (SDK can_message_receive) |
| [`can_message_transmit`](#can_message_transmit) | 0x0800AFA0 | Load a frame into the first empty CAN TX mailbox and request transmission (SDK can_message_transmit) |
| [`vcu_can1_clock_disable`](#vcu_can1_clock_disable) | 0x08002370 | Disable the CAN1 APB1 peripheral clock |
| [`vcu_can1_init`](#vcu_can1_init) | 0x080027F0 | Initialise CAN1: remapped pins, bit timing, six accept-all filters, RX0 and SE interrupts |
| [`vcu_can1_pins_remap_init`](#vcu_can1_pins_remap_init) | 0x08002778 | Remap CAN1 onto PB8 (RX) and PB9 (TX) and configure both pins |
| [`vcu_can1_recover_reinit`](#vcu_can1_recover_reinit) | 0x08002980 | Re-initialise CAN1 from reset with bus-off and error interrupts enabled |
| [`vcu_can1_reset_pulse`](#vcu_can1_reset_pulse) | 0x0800B06C | Pulse the CAN1 peripheral reset bit: assert then release |
| [`vcu_can_ef00_frame_build`](#vcu_can_ef00_frame_build) | 0x0800DA4E | Build a 29-bit CAN frame for PGN 0xEF00 with three header bytes and up to 5 payload bytes |
| [`vcu_can_ef00_message_send`](#vcu_can_ef00_message_send) | 0x0800D018 | Send a PGN 0xEF00 message as one CAN frame or as a J1939 TP session |
| [`vcu_can_msg_obj_send`](#vcu_can_msg_obj_send) | 0x0800EF5A | Send one queued CAN message object: 29-bit ID, length byte and payload |
| [`vcu_can_periodic_telemetry_tick`](#vcu_can_periodic_telemetry_tick) | 0x0800EAC4 | Run the periodic CAN telemetry scheduler: 2, 10, 20 and 100-tick frame groups |
| [`vcu_can_tp_abort_frame_build`](#vcu_can_tp_abort_frame_build) | 0x0800DAAC | Build a J1939 TP.CM connection-abort frame (0x18EC) for PGN 0xEF00 |
| [`vcu_can_tp_cts_frame_build`](#vcu_can_tp_cts_frame_build) | 0x0800DAF0 | Build a J1939 TP.CM clear-to-send frame (0x11) for PGN 0xEF00 |
| [`vcu_can_tp_dt_frame_build`](#vcu_can_tp_dt_frame_build) | 0x0800DBDC | Build a J1939 TP.DT data frame (0x18EB) from a message offset that is a multiple of 7 |
| [`vcu_can_tp_eom_ack_frame_build`](#vcu_can_tp_eom_ack_frame_build) | 0x0800DB38 | Build a J1939 TP.CM end-of-message acknowledgment (0x13) for PGN 0xEF00 |
| [`vcu_can_tp_rts_frame_build`](#vcu_can_tp_rts_frame_build) | 0x0800DB88 | Build a J1939 TP.CM request-to-send (0x10) for a multi-packet PGN 0xEF00 message |
| [`vcu_can_tp_session_table_tick`](#vcu_can_tp_session_table_tick) | 0x0800D25E | Advance every J1939 TP sender session in the table once per timer tick |
| [`vcu_can_tp_session_timeout_tick`](#vcu_can_tp_session_timeout_tick) | 0x0800A78A | Advance a J1939 TP session timer; on expiry notify, send the abort frame and mark done |
| [`vcu_can_tx_pump`](#vcu_can_tx_pump) | 0x08007B08 | Pump one frame from the CAN1 transmit queue into a free mailbox |
| [`vcu_can_tx_queue_peek`](#vcu_can_tx_queue_peek) | 0x08007B90 | Copy the oldest queued CAN frame (20 bytes) without removing it |
| [`vcu_can_tx_queue_push`](#vcu_can_tx_queue_push) | 0x08007BEC | Append one 20-byte CAN frame to the transmit queue if it is not full |

## can_base_init

**Configure CAN1 master control and test mode via freeze mode**

Artery SDK can_base_init. Clears MCTRL.DZEN and sets FZEN (bit 0) in the register at +0, waits (max 0xFFFF loops) for MSTS.FZC (+4 bit 0); then writes from the 7-byte can_base_type {mode_selection, ttc_enable, aebo_enable, aed_enable, prsf_enable, mdrsel_selection, mmssr_selection}: MCTRL bits 7 (TTCEN), 6 (AEBOEN), 5 (AEDEN), 4 (PRSFEN), 3 (MDRSEL), 2 (MMSSR), and BTMG (+0x1C) bit 30 (LBEN) / 31 (LOEN) from mode bits 0/1. Finally clears FZEN and waits for FZC to clear. Called from the CAN init routine 0x080027f0. CAN group: can_default_para_init, can_baudrate_default_para_init, can_baudrate_set.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base (CAN1) |
| `param_2` | `ptr` | can_base_type configuration |

**Returns** `u32`: 1 = SUCCESS, 0 = ERROR (freeze timeout)

- Addresses by version: 148: 0x08009B84, 14a: 0x0800A060, 14b: 0x0800A4E8, 14e: 0x0800A57C, 14f: 0x0800A6B8, 152: 0x0800A938, 153: 0x0800AA2C, 0159: 0x0800AB0C
- Called by: `vcu_can1_init`
- Confidence: high

## can_baudrate_default_para_init

**Fill can_baudrate_type with defaults (div 1, RSAW 2tq, BTS1 4tq, BTS2 3tq)**

Artery SDK can_baudrate_default_para_init: writes baudrate_div (u16 at +0) = 1, rsaw_size (+2) = 1, bts1_size (+3) = 3, bts2_size (+4) = 2. Called from 0x080027f0, which then overrides the fields for the actual bit rate.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | can_baudrate_type to initialise |

- Addresses by version: 148: 0x08009C2C, 14a: 0x0800A108, 14b: 0x0800A590, 14e: 0x0800A624, 14f: 0x0800A760, 152: 0x0800A9E0, 153: 0x0800AAD4, 0159: 0x0800ABB4
- Called by: `vcu_can1_init`
- Confidence: high

## can_baudrate_set

**Program CAN1 bit timing (BTMG) while in freeze mode**

Artery SDK can_baudrate_set. Enters freeze mode (clear DZEN, set FZEN, wait FZC up to 0xFFFF loops), then writes BTMG (+0x1C): BRDIV (bits 11:0) = baudrate_div-1, RSAW (25:24), BTS1 (19:16), BTS2 (22:20) from can_baudrate_type {u16 div, u8 rsaw @+2, u8 bts1 @+3, u8 bts2 @+4}; leaves freeze mode and waits for FZC to drop. Bit rate = fpclk / (div * (3 + bts1 + bts2)). Called from 0x080027f0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base (CAN1) |
| `param_2` | `ptr` | can_baudrate_type |

**Returns** `u32`: 1 = SUCCESS, 0 = ERROR (freeze timeout)

- Addresses by version: 148: 0x08009C3C, 14a: 0x0800A118, 14b: 0x0800A5A0, 14e: 0x0800A634, 14f: 0x0800A770, 152: 0x0800A9F0, 153: 0x0800AAE4, 0159: 0x0800ABC4
- Called by: `vcu_can1_init`
- Confidence: high

## can_default_para_init

**Zero the can_base_type configuration struct**

Artery SDK can_default_para_init: writes 0 to all seven bytes (ttc/aebo/aed/prsf disabled, discard-first-received, send-by-ID, communicate mode). Called from 0x080027f0 before can_base_init.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | can_base_type to initialise |

- Addresses by version: 148: 0x08009D20, 14a: 0x0800A1FC, 14b: 0x0800A684, 14e: 0x0800A718, 14f: 0x0800A854, 152: 0x0800AAD4, 153: 0x0800ABC8, 0159: 0x0800ACA8
- Called by: `vcu_can1_init`
- Confidence: high

## can_filter_init

**Configure one CAN receive filter bank (SDK can_filter_init)**

Matches the Artery SDK can_filter_init(can_x, init_struct). Puts the filter block in init mode (FCTRL bit0 at +0x200 set), deactivates the bank (FACFG +0x21c bit cleared), then loads the bank's two 32-bit filter words at +0x240+8*n/+0x244+8*n. Init struct bytes: [0]=activate enable, [1]=filter_mode (0 mask, 1 list -> FMCFG +0x204), [2]=filter_fifo (FIFO0/1 -> FRF +0x214), [3]=filter_number, [4]=bit width (0=16-bit -> FBWCFG +0x20c cleared, 1=32-bit -> set), halfwords at +6 id_high, +8 id_low, +10 mask_high, +12 mask_low. Finally re-activates the bank if requested and clears FCTRL init bit. Part of the CAN1 driver group (can_filter_init, can_flag_get, can_flag_clear, can_interrupt_enable, can_message_receive, can_message_transmit) that is a build of the Artery AT32 SDK at32f415_can.c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base (CAN1, 0x40006400) |
| `param_2` | `ptr` | can_filter_init_type descriptor (activate, mode, fifo, number, bit width, id/mask halfwords) |

**Notes:** Offset names (+0x200 FCTRL, +0x204 FMCFG, +0x20c FBWCFG, +0x214 FRF, +0x21c FACFG, +0x240 FFB) are from the CAN register map; in 16-bit mode FFDB1 = mask_low<<16|id_low and FFDB2 = mask_high<<16|id_high; in 32-bit mode FFDB1 = id_high<<16|id_low and FFDB2 = mask_high<<16|mask_low. Only called once, from the CAN init routine vcu_0159_080027f0.

- Addresses by version: 148: 0x08009D32, 14a: 0x0800A20E, 14b: 0x0800A696, 14e: 0x0800A72A, 14f: 0x0800A866, 152: 0x0800AAE6, 153: 0x0800ABDA, 0159: 0x0800ACBA
- Called by: `vcu_can1_init`
- Confidence: high

## can_flag_clear

**Clear a CAN status flag selected by SDK flag code (SDK can_flag_clear)**

Switch over the SDK CAN_*_FLAG codes (1 EAF, 2 EPF, 3 BOF, 4 ETR, 5 EOIF, 6-8 TM0..2TCF, 10/11 RF0FF/RF0OF, 13/14 RF1FF/RF1OF, 15 QDZIF, 16 EDZC, 17 TMEF). Flags are write-1-to-clear: EAF/EPF/BOF/EOIF write 4 to MSTS (+4, EOIF bit); ETR also zeroes ESTS (+0x18); TMnTCF write 0x1/0x100/0x10000 to TSTS (+8); TMEF writes 0x10101 (all three); RF0 flags write 8 (full) / 0x10 (overflow) to RF0 (+0xc), RF1 likewise to +0x10; QDZIF writes 8 and EDZC writes 0x10 to MSTS. Unknown codes do nothing. Part of the CAN1 driver group (can_filter_init, can_flag_get, can_flag_clear, can_interrupt_enable, can_message_receive, can_message_transmit) that is a build of the Artery AT32 SDK at32f415_can.c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base (CAN1) |
| `param_2` | `u32` | CAN_*_FLAG code 1..17 |

**Notes:** Called from vcu_0159_08002930 (CAN interrupt/status handling). The firmware's switch lumps flags 1,2,3,5 into the same MSTS write, identical to the SDK.

- Addresses by version: 148: 0x08009E60, 14a: 0x0800A33C, 14b: 0x0800A7C4, 14e: 0x0800A858, 14f: 0x0800A994, 152: 0x0800AC14, 153: 0x0800AD08, 0159: 0x0800ADE8
- Called by: `CAN1_SE_IRQHandler`
- Confidence: high

## can_flag_get

**Read a CAN status flag selected by SDK flag code (SDK can_flag_get)**

Switch over the SDK CAN_*_FLAG codes and returns 0/1 (SDK flag_status). 1-3 are ESTS (+0x18) bits EAF/EPF/BOF; 4 ETR = ESTS bits 4-6 nonzero; 5 EOIF = MSTS (+4) bit2; 6-8 are TSTS (+8) TMnTCF bits 0/8/16; 9 RF0MN = RF0 (+0xc) message count (bits0-1) nonzero; 10/11 RF0FF/RF0OF bits 3/4; 12-14 same for RF1 (+0x10); 15 QDZIF = MSTS bit3; 16 EDZC = MSTS bit1 or bit4; 17 TMEF = any of TSTS bits 26-28 (transmit mailbox empty). Unknown code returns 0. Part of the CAN1 driver group (can_filter_init, can_flag_get, can_flag_clear, can_interrupt_enable, can_message_receive, can_message_transmit) that is a build of the Artery AT32 SDK at32f415_can.c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base (CAN1) |
| `param_2` | `u32` | CAN_*_FLAG code 1..17 |

**Returns** `u32`: 1 if the flag is set, else 0

**Notes:** Callers: vcu_0159_08002904 and vcu_0159_08002930 (CAN status/IRQ handling).

- Addresses by version: 148: 0x08009EC8, 14a: 0x0800A3A4, 14b: 0x0800A82C, 14e: 0x0800A8C0, 14f: 0x0800A9FC, 152: 0x0800AC7C, 153: 0x0800AD70, 0159: 0x0800AE50
- Called by: `CAN1_RX0_IRQHandler`, `CAN1_SE_IRQHandler`
- Confidence: high

## can_interrupt_enable

**Set or clear CAN interrupt-enable bits (SDK can_interrupt_enable)**

Read-modify-write on CAN INTEN (+0x14): ORs param_2 into the register when param_3 is nonzero, otherwise clears those bits. param_2 is a bitmask of CAN_*_INT enable bits (TMEIEN, RF0DIEN, ERRIEN, ...). Called once from the CAN init routine vcu_0159_080027f0. Part of the CAN1 driver group (can_filter_init, can_flag_get, can_flag_clear, can_interrupt_enable, can_message_receive, can_message_transmit) that is a build of the Artery AT32 SDK at32f415_can.c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base (CAN1) |
| `param_2` | `u32` | INTEN bit mask |
| `param_3` | `bool` | nonzero = enable, 0 = disable |

- Addresses by version: 148: 0x08009F8C, 14a: 0x0800A468, 14b: 0x0800A8F0, 14e: 0x0800A984, 14f: 0x0800AAC0, 152: 0x0800AD40, 153: 0x0800AE34, 0159: 0x0800AF14
- Called by: `vcu_can1_init`
- Confidence: high

## can_message_receive

**Read one frame from a CAN RX FIFO mailbox and release the FIFO (SDK can_message_receive)**

Reads the FIFO mailbox at CAN+0x1b0+16*fifo. Fills a can_rx_message_type at param_3: +8 id_type (RFI bit2: 0 standard, 1 extended), +0 standard_id (RFI>>21) or +4 extended_id (RFI>>3), +9 frame_type (RFI bit1, RTR), +10 dlc (RFC low nibble), +0x13 filter_index (RFC bits 8-15), data[0..7] at +0xb..+0x12 from RFDTL/RFDTH. Then releases the FIFO by writing 0x20 (RFnR release bit) to RF0 (+0xc) for fifo 0 or RF1 (+0x10) for fifo 1 (SDK can_receive_fifo_release inlined). Part of the CAN1 driver group (can_filter_init, can_flag_get, can_flag_clear, can_interrupt_enable, can_message_receive, can_message_transmit) that is a build of the Artery AT32 SDK at32f415_can.c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base (CAN1) |
| `param_2` | `u32` | FIFO number, 0 or 1 |
| `param_3` | `ptr` | output can_rx_message_type |

**Notes:** Caller: vcu_0159_08002904 (CAN RX handler). Struct layout inferred from byte offsets, not from SDK headers; the data bytes sit at odd offsets (no padding between dlc and data).

- Addresses by version: 148: 0x08009FA0, 14a: 0x0800A47C, 14b: 0x0800A904, 14e: 0x0800A998, 14f: 0x0800AAD4, 152: 0x0800AD54, 153: 0x0800AE48, 0159: 0x0800AF28
- Called by: `CAN1_RX0_IRQHandler`
- Confidence: high

## can_message_transmit

**Load a frame into the first empty CAN TX mailbox and request transmission (SDK can_message_transmit)**

Picks the first empty mailbox from TSTS (+8) bits 26/27/28 (TM0EF/TM1EF/TM2EF), index 0..2, and returns silently if none is free (this build discards the mailbox number the SDK would return). In the chosen mailbox (CAN+0x180+16*n) it keeps only the TXRQ bit of TMI, then writes: IDE (bit2) from msg+8, standard id <<21 (msg+0) for type 0 or extended id <<3 (msg+4) for type 1, RTR (bit1) from msg+9, DLC low nibble from msg+10 into TMC, data[0..3] (msg+0xb..) into TMDTL and data[4..7] (msg+0xf..) into TMDTH, and finally sets TXRQ (bit0) to start transmission. Part of the CAN1 driver group (can_filter_init, can_flag_get, can_flag_clear, can_interrupt_enable, can_message_receive, can_message_transmit) that is a build of the Artery AT32 SDK at32f415_can.c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | CAN peripheral base (CAN1) |
| `param_2` | `ptr` | can_tx_message_type: std id, ext id, id_type, frame_type, dlc, data[8] |

**Notes:** Single caller vcu_0159_08007b08 (the CAN send routine). No mailbox-full error is reported to the caller, so frames may be dropped under load.

- Addresses by version: 148: 0x0800A018, 14a: 0x0800A4F4, 14b: 0x0800A97C, 14e: 0x0800AA10, 14f: 0x0800AB4C, 152: 0x0800ADCC, 153: 0x0800AEC0, 0159: 0x0800AFA0
- Called by: `vcu_can_tx_pump`
- Confidence: high

## vcu_can1_clock_disable

**Disable the CAN1 APB1 peripheral clock**

Clears the CAN1 clock enable (APB1ENR bit 25) by calling crm_periph_clock_enable with enable 0. It is the counterpart of the CAN1 clock enable in vcu_0159_080027f0. It is called from vcu_0159_0800688c.

- Addresses by version: 148: 0x08001F84, 14a: 0x08001FF4, 14b: 0x080022D0, 14e: 0x080022D0, 14f: 0x0800232C, 152: 0x08002368, 153: 0x08002384, 0159: 0x08002370
- Called by: `vcu_deep_sleep_enter_and_restore`
- Calls: `crm_periph_clock_enable`
- Confidence: high

## vcu_can1_init

**Initialise CAN1: remapped pins, bit timing, six accept-all filters, RX0 and SE interrupts**

Full CAN1 bring-up. It calls vcu_can1_pins_remap_init, enables the CAN1 clock (APB1 bit 25), and zeroes the can_base_type with can_default_para_init. It fills the base configuration (normal mode, TTC off, AEBO off, AED on, PRSF off) and calls can_base_init, which enters freeze mode. Bit timing comes from can_baudrate_default_para_init with values set to divider 9, RSAW 1, BTS1 10 and BTS2 3 (1 + 10 + 3 = 14 time quanta per bit) and is written by can_baudrate_set. It then configures six receive filter banks (0 to 5) with can_filter_init: each is enabled, 32-bit, identifier-mask mode, FIFO 0, with identifier and mask both zero, so all identifiers pass. It enables NVIC lines CAN1_RX0 (IRQ 20) and CAN1_SE (IRQ 22) and sets interrupt enables with can_interrupt_enable for masks 0x2, 0x400, 0x800 and 0x8000. The bit rate depends on the APB1 clock, which this function does not set.

**Notes:** Which interrupt bit each mask (0x2, 0x400, 0x800, 0x8000) selects is not verified. The bit rate is not computed because the APB1 clock is not known here.

- Addresses by version: 148: 0x08002428, 14a: 0x08002498, 14b: 0x08002750, 14e: 0x08002750, 14f: 0x080027AC, 152: 0x080027E8, 153: 0x08002804, 0159: 0x080027F0
- Peripheral registers: `CAN1.MCTRL` (A)
- Called by: `vcu_peripheral_init_sequence`, `vcu_can1_recover_reinit`
- Calls: `vcu_can1_pins_remap_init`, `can_base_init`, `can_baudrate_default_para_init`, `can_baudrate_set`, `can_default_para_init`, `can_filter_init`, `can_interrupt_enable`, `crm_periph_clock_enable`, `nvic_irq_enable`
- Confidence: medium

## vcu_can1_pins_remap_init

**Remap CAN1 onto PB8 (RX) and PB9 (TX) and configure both pins**

Enables the GPIOB and IOMUX clocks, applies remap code 0x2C000402 with gpio_pin_remap_config (enable 1) to move CAN1 onto PB8 and PB9, and then configures PB9 (mask 0x200, packed word 0x01080400, no pull) and PB8 (mask 0x100, pull-up 0x18) with gpio_default_para_init and gpio_init. The remap is taken as the CAN1 alternate mapping. It is called from vcu_0159_080027f0 (CAN1 init) and vcu_0159_08002980.

**Notes:** The remap register bit it changes is not decoded here. PB8 as RX and PB9 as TX are inferred from the CAN1 init that follows.

- Addresses by version: 148: 0x080023B0, 14a: 0x08002420, 14b: 0x080026D8, 14e: 0x080026D8, 14f: 0x08002734, 152: 0x08002770, 153: 0x0800278C, 0159: 0x08002778
- Peripheral registers: `GPIOB.CFGLR` (A)
- Called by: `vcu_can1_init`, `vcu_can1_recover_reinit`
- Calls: `crm_periph_clock_enable`, `gpio_default_para_init`, `gpio_init`, `gpio_pin_remap_config`
- Confidence: medium

## vcu_can1_recover_reinit

**Re-initialise CAN1 from reset with bus-off and error interrupts enabled**

Pulses the CAN1 reset (vcu_can1_reset_pulse), re-applies the CAN1 pin remap (vcu_can1_pins_remap_init) and enables the CAN1 clock (CRM id 0x1C0019). It writes the base configuration and bit timing (divider 9, RSAW 1, BTS1 10, BTS2 3, 14 time quanta per bit), configures six receive filter banks 0 to 5 as accept-all with can_filter_init, and then enables the interrupts. The interrupt set is RX FIFO 0 message (0x2), error-type-record (0x800), error-occur (0x8000) and bus-off (0x400), and NVIC IRQ 22 (CAN1_SE) and IRQ 20 (CAN1_RX0) are enabled at preemption priority 0.

**Notes:** The packet's callee list names vcu_can1_init, but the decompiled body does not call 0x080027F0; the same steps are written out inline here. Compared with vcu_can1_init, which enables RX0 and SE interrupts, this variant adds the bus-off and error interrupts, which suggests it is the recovery path. Its callers, vcu_0159_080047AC and vcu_0159_0800EAC4, are not described yet.

- Addresses by version: 148: 0x080025B0, 14a: 0x08002628, 14b: 0x080028E0, 14e: 0x080028E0, 14f: 0x0800293C, 152: 0x08002978, 153: 0x08002994, 0159: 0x08002980
- Peripheral registers: `CAN1.MCTRL` (A)
- Called by: `vcu_0159_080047ac`, `vcu_can_periodic_telemetry_tick`
- Calls: `vcu_can1_pins_remap_init`, `vcu_can1_init`, `vcu_can1_reset_pulse`
- Confidence: high

## vcu_can1_reset_pulse

**Pulse the CAN1 peripheral reset bit: assert then release**

Calls crm_periph_reset (FUN_0800b5f4, SDK) with the value 0x100019 twice, first with TRUE and then with FALSE. In the SDK header that value is CRM_CAN1_PERIPH_RESET, MAKE_VALUE(0x10, 25), so CAN1 is reset by setting and then clearing its bit in the CRM reset register back to back.

- Addresses by version: 148: 0x0800A0E4, 14a: 0x0800A5C0, 14b: 0x0800AA48, 14e: 0x0800AADC, 14f: 0x0800AC18, 152: 0x0800AE98, 153: 0x0800AF8C, 0159: 0x0800B06C
- Called by: `vcu_can1_recover_reinit`, `vcu_deep_sleep_enter_and_restore`
- Calls: `crm_periph_reset`
- Confidence: high

## vcu_can_ef00_frame_build

**Build a 29-bit CAN frame for PGN 0xEF00 with three header bytes and up to 5 payload bytes**

Fills a CAN frame struct (word 0 = 29-bit ID, byte 4 = DLC, bytes 5..12 = data). The ID is priority << 26 | destination << 8 | source | 0x00EF0000 (PF = 0xEF, PGN 0xEF00 proprietary-A, PDU1 format), with the extended-ID bit 29 set and bit 31 preserved. The DLC is payload + 3, the three header bytes go to data bytes 0..2 and the payload follows. The call fails when priority is 8 or more, the payload is more than 5 bytes (so DLC stays at 8 or less) or a pointer is null. This group (vcu_can_*) builds the frames of the 0xEF00 proprietary channel, and the TP functions below build its multi-packet transport.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | CAN priority 0..7 |
| `param_2` | `u8` | data byte 0 (header) |
| `param_3` | `u32` | source address (ID bits 0..7) |
| `param_4` | `s32` | destination address (ID bits 8..15) |
| `param_5` | `u8` | data byte 1 (header) |
| `param_6` | `u8` | data byte 2 (header) |
| `param_7` | `s32` | payload source pointer |
| `param_8` | `u32` | payload length, 0..5 |
| `param_9` | `ptr` | output CAN frame struct |

**Returns** `bool`: 1 on success, 0 on bad arguments

**Notes:** The header byte semantics are not known from this function alone.

- Addresses by version: 148: 0x0800CB4C, 14a: 0x0800CF9C, 14b: 0x0800D428, 14e: 0x0800D4C8, 14f: 0x0800D614, 152: 0x0800D8A4, 153: 0x0800D998, 0159: 0x0800DA4E
- Called by: `vcu_can_ef00_message_send`
- Confidence: medium

## vcu_can_ef00_message_send

**Send a PGN 0xEF00 message as one CAN frame or as a J1939 TP session**

Sends a proprietary-A (PGN 0xEF00) message. When param_3 (the byte count) is below 6, it builds one 29-bit CAN frame with vcu_can_ef00_frame_build (fixed arguments 6 and 1, with param_1, param_2, param_4, param_5 and param_6 as the data bytes and param_3 as the length) and queues it with vcu_record_send_short, masking the identifier to 29 bits. For 6 or more bytes it calls proto_session_send on the session buffer at DAT_20002970 with argument 7 and 1, so the transport-protocol state machine sends the message as several frames.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | data byte 0 (r0) |
| `param_2` | `u32` | data byte 1 (r1) |
| `param_3` | `u32` | payload byte count; below 6 sends one frame |
| `param_4` | `u32` | data byte 2 (r3) |
| `param_5` | `u32` | data byte 3 (stack) |
| `param_6` | `u32` | data byte 4 (stack) |

**Notes:** The decompile passes the data as 32-bit register values, so the truncation to bytes is assumed to happen in vcu_can_ef00_frame_build. The meaning of the fixed arguments 6, 1, 7 and 1 is not shown.

- Addresses by version: 148: 0x0800C18C, 14a: 0x0800C5D0, 14b: 0x0800CA5C, 14e: 0x0800CAF0, 14f: 0x0800CC2C, 152: 0x0800CEB8, 153: 0x0800CFAC, 0159: 0x0800D018
- Called by: `vcu_timed_window_schedule_tick`, `vcu_countdown_start_handshake`, `vcu_0159_080054ec`, `vcu_display_frame_render_tick`, `vcu_panel_key_report_telemetry_tick`, `vcu_fw_update_frame_handler`, `vcu_startup_announce_burst`
- Calls: `vcu_record_send_short`, `proto_session_send`, `vcu_can_ef00_frame_build`
- Confidence: medium

## vcu_can_msg_obj_send

**Send one queued CAN message object: 29-bit ID, length byte and payload**

Reads a message object at param_2: the first word masked with 0x1FFFFFFF is the CAN identifier, the byte at offset 4 is the length and the bytes from offset 5 are the payload. It hands these to vcu_record_send_short and always returns 1. It has no direct caller in the packet, so it is reached through a pointer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | not used |
| `param_2` | `ptr` | message object: u32 identifier, u8 length at +4, payload from +5 |

**Returns** `u32`: always 1

- Addresses by version: 148: 0x0800DF36, 14a: 0x0800E3D2, 14b: 0x0800E862, 14e: 0x0800E902, 14f: 0x0800EA4E, 152: 0x0800ECF6, 153: 0x0800EDEA, 0159: 0x0800EF5A
- Calls: `vcu_record_send_short`
- Confidence: high

## vcu_can_periodic_telemetry_tick

**Run the periodic CAN telemetry scheduler: 2, 10, 20 and 100-tick frame groups**

Periodic CAN scheduler called once per tick. When DAT_20001f48 is 1 it resets DAT_2000102c, DAT_20001030 and DAT_2000102e. Otherwise, while DAT_2000185e is nonzero it only counts it down and returns; then it updates the countdowns DAT_20001868 and DAT_2000186a, which set bits 1 and 2 of DAT_2000186e when they expire, and increments the tick counter DAT_20001848. Each value is supplied by the callback at DAT_20001864 (called with the ID) and sent with vcu_record_send_chunked: ID 0x100 (8 bytes) on even ticks, IDs 0x203, 0x204, 0x205, 0x209, 0x20A, 0x20B and 0x20C (8 bytes) every 10 ticks, IDs 0x301, 0x302 (2 bytes) and 0x485 every 20 ticks, and IDs 0x480 to 0x484 (8 bytes) every 100 ticks. When DAT_2000185b is set, DAT_2000184a counts to 50, then the flag is cleared, DAT_20001854 is incremented and vcu_0159_08002980 is called.

**Notes:** The callback at DAT_20001864 takes an ID and returns a data pointer, as the calls show. vcu_0159_08002980 is not yet described. The meaning of the countdown flags is inferred from their use.

- Addresses by version: 148: 0x0800DAA4, 14a: 0x0800DF40, 14b: 0x0800E3CC, 14e: 0x0800E46C, 14f: 0x0800E5B8, 152: 0x0800E860, 153: 0x0800E954, 0159: 0x0800EAC4
- Calls: `vcu_can1_recover_reinit`, `vcu_record_send_chunked`
- Confidence: medium

## vcu_can_tp_abort_frame_build

**Build a J1939 TP.CM connection-abort frame (0x18EC) for PGN 0xEF00**

Builds an 8-byte TP.CM frame with ID 0x18EC (priority 6, PGN 0xEC00) from source and destination addresses. Data byte 0 = 0xFF (connection abort control), byte 1 = 0xFF (reason), bytes 2..4 = 0xFF reserved and bytes 5..7 = 00 EF 00, the PGN being aborted (0xEF00). It is presumably the abort sent when a multi-packet transfer on the 0xEF00 channel must stop. It is one of the TP.CM builders (vcu_can_tp_*) that share the same ID and data layout.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | source address (ID bits 0..7) |
| `param_2` | `s32` | destination address (ID bits 8..15) |
| `param_3` | `ptr` | output CAN frame struct |

**Returns** `bool`: 1 on success, 0 when the output pointer is null

**Notes:** The reason byte is written as the fixed value 0xFF.

- Addresses by version: 148: 0x0800CBA8, 14a: 0x0800CFF8, 14b: 0x0800D484, 14e: 0x0800D524, 14f: 0x0800D670, 152: 0x0800D900, 153: 0x0800D9F4, 0159: 0x0800DAAC
- Called by: `vcu_can_tp_session_timeout_tick`, `vcu_can_tp_session_on_frame`
- Confidence: high

## vcu_can_tp_cts_frame_build

**Build a J1939 TP.CM clear-to-send frame (0x11) for PGN 0xEF00**

Builds the TP.CM clear-to-send frame (ID 0x18EC): data byte 0 = 0x11, byte 1 = number of packets the receiver accepts now, byte 2 = next packet number expected, bytes 3..4 = 0xFF and bytes 5..7 = 00 EF 00 (PGN 0xEF00). The receiver sends it to start or resume a multi-packet transfer. Part of the TP.CM group with vcu_can_tp_abort_frame_build, vcu_can_tp_eom_ack_frame_build and vcu_can_tp_rts_frame_build.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | source address (ID bits 0..7) |
| `param_2` | `s32` | destination address (ID bits 8..15) |
| `param_3` | `u8` | number of packets allowed (byte 1) |
| `param_4` | `u8` | next packet number expected (byte 2) |
| `param_5` | `ptr` | output CAN frame struct |

**Returns** `bool`: 1 on success, 0 when the output pointer is null

- Addresses by version: 148: 0x0800CBEC, 14a: 0x0800D03C, 14b: 0x0800D4C8, 14e: 0x0800D568, 14f: 0x0800D6B4, 152: 0x0800D944, 153: 0x0800DA38, 0159: 0x0800DAF0
- Called by: `vcu_can_tp_session_on_frame`
- Confidence: high

## vcu_can_tp_dt_frame_build

**Build a J1939 TP.DT data frame (0x18EB) from a message offset that is a multiple of 7**

Builds one TP.DT frame: ID 0x18EB (priority 6) from source and destination, data byte 0 = sequence number (offset / 7) + 1, computed as (offset + 6) / 7 + 1, followed by up to 7 payload bytes copied from the message. The offset must be a multiple of 7. The byte count comes from the in/out u16 *remaining (clamped to 7) and is written back. The remaining data bytes are filled with 0xFF. The decompiled index arithmetic looks off by one: the copy loop runs uVar2+1 times, and the padding loop starts one index too early, so the last copied byte is overwritten. The intended behaviour is 7 payload bytes per frame, so the exact byte count per frame should be checked against the binary. Its caller is vcu_0159_0800d34a, which advances the offset by 7 per frame.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | source address (ID bits 0..7) |
| `param_2` | `s32` | destination address (ID bits 8..15) |
| `param_3` | `u32` | byte offset of this chunk in the message, must be a multiple of 7 |
| `param_4` | `ptr` | message source at the chunk offset |
| `param_5` | `ptr` | in/out u16: bytes remaining; clamped to 7 and written back |
| `param_6` | `ptr` | output CAN frame struct |

**Returns** `bool`: 1 on success, 0 on bad arguments

**Notes:** Sequence number formula matches the TP.DT convention (1-based packet number). The byte-count and padding arithmetic is uncertain, see description.

- Addresses by version: 148: 0x0800CCD8, 14a: 0x0800D128, 14b: 0x0800D5B4, 14e: 0x0800D654, 14f: 0x0800D7A0, 152: 0x0800DA30, 153: 0x0800DB24, 0159: 0x0800DBDC
- Called by: `vcu_can_tp_sender_tick`
- Confidence: low

## vcu_can_tp_eom_ack_frame_build

**Build a J1939 TP.CM end-of-message acknowledgment (0x13) for PGN 0xEF00**

Builds the TP.CM end-of-message acknowledgment (ID 0x18EC): data byte 0 = 0x13, bytes 1..2 = total message size little-endian, byte 3 = number of packets ceil(size / 7) = (size + 6) / 7, byte 4 = 0xFF and bytes 5..7 = 00 EF 00 (PGN 0xEF00). The receiver sends it after the last data packet arrives. It is part of the TP.CM group (vcu_can_tp_*).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | source address (ID bits 0..7) |
| `param_2` | `s32` | destination address (ID bits 8..15) |
| `param_3` | `s32` | total message size in bytes |
| `param_4` | `ptr` | output CAN frame struct |

**Returns** `bool`: 1 on success, 0 when the output pointer is null

- Addresses by version: 148: 0x0800CC34, 14a: 0x0800D084, 14b: 0x0800D510, 14e: 0x0800D5B0, 14f: 0x0800D6FC, 152: 0x0800D98C, 153: 0x0800DA80, 0159: 0x0800DB38
- Called by: `vcu_can_tp_session_on_frame`
- Confidence: high

## vcu_can_tp_rts_frame_build

**Build a J1939 TP.CM request-to-send (0x10) for a multi-packet PGN 0xEF00 message**

Builds the TP.CM request-to-send (ID 0x18EC): data byte 0 = 0x10, bytes 1..2 = total size little-endian, byte 3 = number of data packets (size + 6) / 7, byte 4 = 0xFF (no limit on packets per CTS) and bytes 5..7 = 00 EF 00 (PGN 0xEF00). It is only built when the size is more than 8 bytes, because a message of 8 bytes or fewer goes in a single frame. It is part of the TP.CM group (vcu_can_tp_*) that starts a transfer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | source address (ID bits 0..7) |
| `param_2` | `s32` | destination address (ID bits 8..15) |
| `param_3` | `u32` | total message size in bytes, must be greater than 8 |
| `param_4` | `ptr` | output CAN frame struct |

**Returns** `bool`: 1 on success, 0 when the size is 8 or less or the output pointer is null

- Addresses by version: 148: 0x0800CC84, 14a: 0x0800D0D4, 14b: 0x0800D560, 14e: 0x0800D600, 14f: 0x0800D74C, 152: 0x0800D9DC, 153: 0x0800DAD0, 0159: 0x0800DB88
- Called by: `vcu_can_tp_sender_tick`
- Confidence: high

## vcu_can_tp_session_table_tick

**Advance every J1939 TP sender session in the table once per timer tick**

Iterates over a session table described by a base pointer at offset 0, a 16-bit session count at offset 4 and a timer argument at offset 8 (the table at DAT_20002970). For each 0x24-byte session it calls vcu_can_tp_sender_tick with the timer argument, so each TP sender state machine advances once per tick. It has no direct caller in the packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | session table descriptor: base, u16 count, timer argument |

- Addresses by version: 148: 0x0800C3CE, 14a: 0x0800C816, 14b: 0x0800CCA2, 14e: 0x0800CD36, 14f: 0x0800CE72, 152: 0x0800D0FE, 153: 0x0800D1F2, 0159: 0x0800D25E
- Calls: `vcu_can_tp_sender_tick`
- Confidence: high

## vcu_can_tp_session_timeout_tick

**Advance a J1939 TP session timer; on expiry notify, send the abort frame and mark done**

Ticks the transport-protocol session object param_1: the 16-bit counter at +0x16 increments and is compared with the 16-bit limit at +0x18. When the limit is reached, an optional notify callback in the ops table at param_2+4 runs with the session, its source and destination bytes and 1, vcu_can_tp_abort_frame_build (FUN_0800daac) builds the abort frame for those addresses, the send callback at ops+0xc transmits it, and the session state byte at +2 is set to 1 (done). Below the limit only the counter advances.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TP session object; bytes 0 and 1 are the source and destination |
| `param_2` | `ptr` | ops table holding the notify callback at +4 and the send callback at +0xc, or 0 |
| `param_3` | `u32` | not read; copied to a stack local and unused |
| `param_4` | `u32` | not read; copied to a stack local and unused |

**Returns** `u64`: low word is the session pointer and high word the ops pointer, both unchanged

**Notes:** The send callback receives a pointer to the session pointer rather than a frame; the exact frame reference convention is not traced.

- Addresses by version: 148: 0x08009806, 14a: 0x08009CDE, 14b: 0x0800A166, 14e: 0x0800A1FA, 14f: 0x0800A336, 152: 0x0800A5B6, 153: 0x0800A6AA, 0159: 0x0800A78A
- Called by: `vcu_can_tp_sender_tick`
- Calls: `vcu_can_tp_abort_frame_build`
- Confidence: medium

## vcu_can_tx_pump

**Pump one frame from the CAN1 transmit queue into a free mailbox**

Gate: if the ring count from vcu_0159_08007c8c is zero it returns 0. Otherwise, while CAN1.MSTS bit 8 (CUSS, currently sending) is set it returns the count without acting. Otherwise it peeks the oldest 20-byte frame with vcu_can_tx_queue_peek, transmits it on CAN1 with can_message_transmit, and advances the read index DAT_200029a8 (modulo 32) when the result is not 4, which removes the frame from the queue; a result of 4 leaves the frame for the next call. It returns the same ring count it gated on.

**Returns** `u32`: the gate value from the ring count routine

**Notes:** The gate calls vcu_0159_08007c8c, which wave 1 named uart_rx_ring1_count. A CAN transmit pump gated on a UART receive count looks wrong, so either the name or the gate needs checking. The meaning of result 4 from can_message_transmit is inferred from the code only.

- Addresses by version: 148: 0x080070DC, 14a: 0x08007518, 14b: 0x0800787C, 14e: 0x080078B4, 14f: 0x08007910, 152: 0x080079D4, 153: 0x08007A70, 0159: 0x08007B08
- Peripheral registers: `CAN1.MCTRL` (A), `CAN1.MSTS` (R)
- Called by: `vcu_0159_0800d858`
- Calls: `vcu_can_tx_queue_peek`, `uart_rx_ring1_count`, `can_message_transmit`
- Confidence: medium

## vcu_can_tx_queue_peek

**Copy the oldest queued CAN frame (20 bytes) without removing it**

If the CAN transmit queue is not empty (DAT_200029a8 differs from DAT_200029a4), it copies the 20-byte entry at 0x200029AC + 20 * DAT_200029a8 into the buffer argument and leaves the read index unchanged. vcu_can_tx_pump advances the index after a transmit.

| Parameter | Type | Description |
|---|---|---|
| `dst` | `ptr` | destination buffer of 20 bytes |

- Addresses by version: 148: 0x08007164, 14a: 0x080075A0, 14b: 0x08007904, 14e: 0x0800793C, 14f: 0x08007998, 152: 0x08007A5C, 153: 0x08007AF8, 0159: 0x08007B90
- Called by: `vcu_can_tx_pump`
- Calls: `__aeabi_memcpy`
- Confidence: high

## vcu_can_tx_queue_push

**Append one 20-byte CAN frame to the transmit queue if it is not full**

When the queue is not full (write index plus 1 modulo 32 differs from the read index DAT_200029a8), it copies 20 bytes from the argument into the slot at 0x200029AC + 20 * DAT_200029a4 and advances the write index DAT_200029a4 modulo 32. A full queue drops the frame. The consumer is vcu_can_tx_pump, through vcu_can_tx_queue_peek.

| Parameter | Type | Description |
|---|---|---|
| `src` | `ptr` | source frame of 20 bytes |

**Notes:** Callers vcu_0159_0800ac44 and vcu_0159_0800b088 are outside this packet.

- Addresses by version: 148: 0x080071C0, 14a: 0x080075FC, 14b: 0x08007960, 14e: 0x08007998, 14f: 0x080079F4, 152: 0x08007AB8, 153: 0x08007B54, 0159: 0x08007BEC
- Called by: `vcu_record_send_chunked`, `vcu_record_send_short`
- Calls: `__aeabi_memcpy`
- Confidence: high
