# BLE - `uart_bridge` functions

3 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`ble_app_queue_message`](#ble_app_queue_message) | 0x0C053F74 | Frame an app/UART message and queue it, splitting it when it exceeds the frame limit |
| [`uart_disp_get_channel_ctx`](#uart_disp_get_channel_ctx) | 0x0C028790 | Return the UART dispatcher context for channel 0, else NULL |
| [`uart_disp_get_channel_fd`](#uart_disp_get_channel_fd) | 0x0C02E57C | Return the /dev/uart2 file descriptor for channel 0, else -1 |

## ble_app_queue_message

**Frame an app/UART message and queue it, splitting it when it exceeds the frame limit**

Builds frames in a 0xF7-byte buffer at 0x20012348 (zeroed first with memset). Message codes 0x1FF and 0x6FF use a 1-byte header (0x01) with the payload at +1. Other codes use a 3-byte header: 0x01 followed by the 16-bit message code at +1 (little-endian), and the payload at +3. Payloads larger than the per-frame limit DAT_20004072 are split: the first chunk is queued with ble_app_start_deferred_500ms_op (0x0c05cb08, which stores the operation and arms a 500 ms timer), and the remainder is kept as pending-fragment state in 0x20012310 (code), 0x20012314 (source offset) and 0x20012318 (remaining length). Codes with high byte 0x02 are first checked by ble_slot_mgr_check_flag5 (0x0c0531b8) and dropped when it returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | context passed to the queue operation |
| `param_2` | `u16` | message code |
| `param_3` | `ptr` | payload bytes |
| `param_4` | `u32` | payload length |

**Notes:** The per-frame limit is a u8 global at 0x20004072. Frame-type meaning of codes 0x1FF and 0x6FF is inferred.

- Addresses by version: 219: 0x0C053F74
- Called by: `ble_219_0c053018`, `ble_219_0c0540f4`, `ble_219_0c054180`, `ble_219_0c05420c`, `ble_slot_store_and_queue`
- Calls: `ble_slot_mgr_check_flag5`, `ble_app_start_deferred_500ms_op`, `memcpy`, `memset`
- Confidence: medium

## uart_disp_get_channel_ctx

**Return the UART dispatcher context for channel 0, else NULL**

Returns &DAT_20003db8 when param_1 == 0 and NULL for any other value; the dispatcher has only a single channel. Called from the 'Uart dispatcher: start service' routine (0x0c02e420) and three sibling routines in the same module, which pass the returned block (+8) to a registration call. The structure layout is not visible in this function.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | channel index; only 0 is valid |

**Returns** `ptr`: pointer to the channel-0 context at 0x20003db8 or NULL

**Notes:** Context struct contents unknown; role inferred from the callers' strings ('Uart dispatcher', '/dev/uart2').

- Addresses by version: 219: 0x0C028790
- Called by: `ble_219_0c02e420`, `ble_219_0c02e5a4`, `ble_219_0c02e758`, `ble_219_0c02e7d8`
- Confidence: medium

## uart_disp_get_channel_fd

**Return the /dev/uart2 file descriptor for channel 0, else -1**

Returns -1 if param_1 != 0. Otherwise returns DAT_20009d10 (the descriptor stored by the UART dispatcher start routine 0x0c02e420 after opening '/dev/uart2'), or -1 if that value is not positive (port never opened). No direct callers; it is used as a callback/ops-table entry.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | channel index; only 0 is valid |

**Returns** `s32`: file descriptor (>0) or -1

**Notes:** Used via function pointer, so the exact consumer is unknown.

- Addresses by version: 219: 0x0C02E57C
- Confidence: medium
