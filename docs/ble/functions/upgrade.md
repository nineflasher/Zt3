# BLE - `upgrade` functions

2 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`nb_upgrade_verify_raw`](#nb_upgrade_verify_raw) | 0x0C034468 | Verify a RAW or RAW4 firmware container: magic, size bound and payload CRC32 |
| [`nb_upgrade_verify_staged_image`](#nb_upgrade_verify_staged_image) | 0x0C034548 | Verify the staged image described by DAT_20003E2C and copy out four header words |

## nb_upgrade_verify_raw

**Verify a RAW or RAW4 firmware container: magic, size bound and payload CRC32**

Checks the header param_2: magic 0x20574152 ('RAW ') or 0x34574152 ('RAW4') at +0, payload size at +0xC (at most 0x1D8000), expected CRC32 at +0x10 and payload offset at +0x18 from the header. For RAW the reflected CRC32 (polynomial 0xEDB88320, crc32_reflected_table at 0x0C0476A0) is computed over the whole payload in one call. For RAW4 with payload end above 0x1000 the code streams the first 0x1000 bytes, then one byte per 4 KB page boundary, then the tail, all through the same routine. It returns 0 when the CRC matches, -8 on mismatch and -5 for a bad magic or an oversize image, and writes the payload address to *param_1 when that pointer is given.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | optional output: payload start address |
| `param_2` | `ptr` | image header record |

**Returns** `s32`: 0 valid; -8 CRC mismatch; -5 bad magic or size

**Notes:** The RAW4 streaming path passes 0x1000 as the fourth argument of its first call, and the decompiler drops the fourth argument of the in-loop calls. Which bytes the RAW4 CRC covers is therefore uncertain (low confidence on that branch).

- Addresses by version: 219: 0x0C034468
- Called by: `nb_upgrade_verify_staged_image`
- Calls: `crc32_reflected_table`
- Confidence: medium

## nb_upgrade_verify_staged_image

**Verify the staged image described by DAT_20003E2C and copy out four header words**

Upgrade-module wrapper. If the descriptor at DAT_20003E2C has a size (+0xC) of at most 0x1D8000 it calls nb_upgrade_verify_raw on it (0x0C034468), passing param_1 through, and when param_2 is non-NULL it copies descriptor words +4, +8, +0xC and +0x10 into param_2[0..3]. An oversize descriptor returns -5 and copies nothing. Parameters param_3 and param_4 are not used in the body.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | passed through as the payload-address output of the verifier |
| `param_2` | `ptr` | output: four u32 copied from the staged descriptor |
| `param_3` | `u32` | not used |
| `param_4` | `u32` | not used |

**Returns** `s32`: verifier result, or -5 for an oversize descriptor

- Addresses by version: 219: 0x0C034548
- Calls: `nb_upgrade_verify_raw`
- Confidence: medium
