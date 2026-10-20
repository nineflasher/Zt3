# BLE module brief (for annotation agents)

Bestechnic "BES" Bluetooth SoC firmware (`BLE_219`) of a Segway-Ninebot scooter's BLE module.
ARMv8-M Cortex-M33-class, Thumb-2, image at 0x0C028000 (RAW4TFT container header 0x400, vector
table at 0x0C028400), SRAM 0x20000000..0x20080000 (`.data` at 0x20003D88).

Contents: BTstack-derived Bluetooth host (att_server.c, att_db.c, att_db_util.c, hci.c,
hci_transport_h4.c, l2cap.c, sm.c, hid_device.c, le_device_db_tlv.c, bthost_*), Bestechnic /
RivieraWaves BLE+BT controller code and ROM patches (ld_*, lld_*, lm_*, sch_*, em_* register
accessors, bt_drv_*, `*_patch`), newlib libc (memcpy, strtok, rand, gmtime ...), an RTOS
(RTX/FreeRTOS-like, BASEPRI-based critical sections), crypto (AES S-box, SHA-256, MD5, CRC32 tables),
Apple Find My Network accessory support (`ninebot_fmna`), a firmware upgrade module (`nb_upgrade`:
plain/cipher upload, md5sum + IAP crc32 verification), a UART protocol to the VCU (frames with
src/dest/cmd/index), `ble_crypto_*` (vehicle serial number + password authentication) and
factory/RF test commands (xtal calibration, non-signalling TX).

Evidence sources
- Strings: `analysis/export/ble/BLE_219.json` key `strings` (text + referencing function addresses).
  Many contain original function names and source file names; use them for naming.
- Decompiled code / call graph are in your work packet.  Peripheral addresses 0x4000xxxx..0x4008xxxx
  are BES-specific and undocumented: describe by address and observed function.
- Known open source: BTstack (bluekitchen/btstack), newlib, mbedTLS, FreeRTOS/CMSIS-RTOS.  Public source
  can be fetched from raw.githubusercontent.com (github proxy works) - use it to confirm real function
  names, but do not spend long on it.

Typical categories: `ble_host ble_controller bt_controller libc rtos crypto hal app upgrade fmna
uart_bridge factory_test util isr startup`.
