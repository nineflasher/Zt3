# BMS - `upgrade` functions

1 functions.

| Function | Address (BMS_4168) | Summary |
|---|---|---|
| [`bms_fw_upload_handle`](#bms_fw_upload_handle) | 0x0800EDDC | Handle firmware upload messages: start, TEA-CBC decrypt and flash 2 KB pages, verify, commit |

## bms_fw_upload_handle

**Handle firmware upload messages: start, TEA-CBC decrypt and flash 2 KB pages, verify, commit**

Message handler for the image download sequence over CAN. If the low byte of param_1 is 6 the message is forwarded to the TX queue with a 4-byte header and no processing. Sub-command 7 takes a 4-byte image length (1 to 0x1F000 bytes allowed), clears the valid flag in the 4-byte record at 0x0803F800 through bms_4168_08008DE8, and stores the length in DAT_20000590. Sub-command 8 carries chunks of up to 128 bytes: each 8-byte block is decrypted with 32-round TEA (key: four little-endian words at 0x20001C68, sum starting at 0xC6EF3720), XORed with the previous ciphertext block at 0x200005A8 (CBC chaining), and staged in 0x20001468. Every 2 KB the staged page is programmed at 0x08020000 plus the page offset, the 16 key bytes are each advanced by their index every 1 KB, and a running 32-bit sum (rotated and complemented) is checked against the final word of the image. The first page must hold the 16 bytes "STD_BMS_V3" at 0x20001568. Sub-command 9 commits by writing the page count and a valid flag to the record at 0x0803F800 once the image has verified; sub-command 10 rewrites that record when a commit is pending and sets bit 29 (and bit 30 on success) of the control word at 0x200001C8. Replies are three or four bytes 0x01, 0x0B, status (and the chunk sequence for sub-command 8) sent with bms_frame_send_when_ready on CAN ID param_1, with status 0 ok, 1 bad length or no open transfer, 3 flash failure, 5 bad sequence, 7 bad start length, 8 commit before verification and 10 wrong header.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | message ID; its low byte 6 selects the forwarding path, and it is the CAN ID for replies |
| `param_2` | `u32` | sub-command: 7 start, 8 data chunk, 9 finish, 10 commit |
| `param_3` | `u32` | payload length (for sub-command 7 it includes a 3-byte header) |
| `param_4` | `ptr` | payload bytes |
| `param_5` | `u32` | chunk sequence number (low byte) |

**Notes:** The TEA identification rests on the delta constant (0xC6EF3720 is 32*0x9E3779B9), the decrement by 0x9E3779B9 and the round equations, and the CBC chaining is read from the XOR and copy steps. The 'STD_BMS_V3' check reads the 16 bytes at 0x20001568, which is 0x100 into the 2 KB staging buffer at 0x20001468, not its start; this may be a header offset or a mismatch in the decompile, so it is open. The flash helper bms_4168_08008DE8 is not described in this packet, so the write and erase semantics of the commit record are inferred from the call sites. The sum check uses a 32-bit running sum with the last word compared against the rotated-complemented total.

- Addresses by version: 4130: 0x0800D31C, 4139: 0x0800D904, 4148: 0x0800E94C, 4168: 0x0800EDDC
- Called by: `bms_4168_0800f2e0`, `bms_4168_0800f8e0`
- Calls: `memcpy`, `bms_mem_zero`, `bms_memcmp_prefix`, `bms_session_state_reset`, `bms_flash_write_bytes`, `bms_frame_send_when_ready`, `bms_ram_200001c8_addr`, `bms_txq_enqueue`
- Confidence: medium
