# VCU - `upgrade` functions

1 functions.

| Function | Address (VCU_0159) | Summary |
|---|---|---|
| [`vcu_fw_update_frame_handler`](#vcu_fw_update_frame_handler) | 0x08006184 | Firmware-update frame handler: start, decrypt-and-stage blocks, finish and reset |

## vcu_fw_update_frame_handler

**Firmware-update frame handler: start, decrypt-and-stage blocks, finish and reset**

Handles one update frame: the sub-command is byte 3, the sequence number byte 4, the payload starts at byte 5 and the peer address is byte 1, and the reply carries a status byte under command 0x0B. Sub-command 7 starts a transfer: the 4-byte size must be nonzero, below 0xF000 and a multiple of 8, and the staging area at 0x08010000 is erased for size plus 0x80 bytes. Sub-command 8 carries 8-byte blocks in sequence, where the expected sequence is DAT_20001491 and the previous sequence is accepted silently; each block is XTEA-decrypted with the key at 0x200020DC in a CBC-style chain, the key is incremented by its byte index every 1 KiB, the first word must look like a stack pointer in SRAM, the first 1 KiB must match the product block at 0x08001400, the key at 0x08001440 and the identifier at 0x08001430 before writes are allowed past 1 KiB, and the plaintext is programmed with vcu_flash_program_verified while a rotated-sum checksum is accumulated. Sub-command 9 finishes a verified transfer with a 4-byte payload, sets the pending flag and size in the record and stores it, and sub-command 10 resets the MCU through AIRCR SYSRESETREQ when the pending flag is set and this session has not verified the checksum; any other sub-command returns status 7.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | frame buffer: [0] payload length, [1] peer address, [3] sub-command, [4] sequence, [5..] payload |
| `param_2` | `u32` | reply path: 0 queues the reply with vcu_ninebot_tx_queue_push, 1 uses vcu_0159_0800D018 with the extra arguments |
| `param_3` | `u32` | passed through to the reply path only when param_2 is 1 |
| `param_4` | `u32` | passed through to the reply path only when param_2 is 1 |

**Notes:** Status codes sent: 0 OK, 1 bad size or overrun or header gate, 3 flash failure, 5 sequence error (a sequence equal to the previous one is accepted), 6 busy (sent when a frame arrives while a previous one is still being handled), 7 bad length, state or vector check, 8 checksum mismatch, 0xB identifier mismatch, 0xC key mismatch. The checksum is the complement of the 16-bit-rotated sum of the preceding words, compared with the final word. The sub-command 10 reset condition looks inverted against the sub-command 9 check (which requires the checksum to pass), so it should be verified against the protocol definition. A reply-path flag DAT_2000185C and timer DAT_2000185E are set on the second path.

- Addresses by version: 148: 0x080056D8, 14a: 0x08005AF8, 14b: 0x08005E50, 14e: 0x08005E88, 14f: 0x08005EE4, 152: 0x08005F64, 153: 0x08006000, 0159: 0x08006184
- Peripheral registers: `SCB+0xc` (RW)
- Called by: `vcu_0159_080054ec`
- Calls: `__aeabi_memcpy`, `vcu_flash_program_verified`, `vcu_flash_erase_range_locked`, `vcu_crypto_key_load`, `vcu_upgrade_record_store`, `vcu_flash_record_pingpong_save`, `vcu_ninebot_tx_queue_push`, `delay_ms`, `vcu_can_ef00_message_send`, `vcu_xtea_decrypt_with_key_at`
- Confidence: medium
