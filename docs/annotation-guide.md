# Annotation guide

Every function, variable, table and type in all firmware images gets a name and a description.
Descriptions are written **once per family** (the same logical function / variable across all
firmware versions, see `analysis/families/<component>.json`) and applied to every version with
`zt3 apply`.  `zt3 check` fails until nothing is missing.

## Ground rules

1. **Describe what the code does, from evidence.**  Use the decompiled C, the register names
   (`GPIOA.ODR`, `USART1.CTRL1` ...), constants, call graph, string literals and the vendor SDK
   sources if provided.  Do not invent features.  If a purpose is a guess, say so in
   `description` and set `confidence` to `medium` or `low` - never leave a field empty.
2. **Names** are `snake_case` C identifiers, unique within the component, prefixed by the module
   (`can_tx_frame`, `motor_foc_update`, `bms_cell_balance_step`).  When the function is a known
   library routine (vendor SDK driver, newlib, BTstack, mbedTLS, CMSIS) use the library's real name
   (`crm_periph_clock_enable`, `memcpy`, `l2cap_send_signaling_packet`).
3. **summary**: one line, imperative, <= 100 chars, no trailing period needed.
4. **description**: 2-6 sentences: purpose, algorithm/state machine, side effects (registers,
   globals written), units and magic numbers, protocol bytes, error handling.  Mention callers'
   expectations (e.g. "called from the 1 ms SysTick tick").
5. **params / returns**: use decompiler order (`param_1` ...).  Types are one of
   `u8 u16 u32 u64 s8 s16 s32 s64 f32 f64 bool char ptr ptr:<Struct> void` or an annotated struct /
   enum name.  Give units where known.
6. **category** (module): short snake_case; reuse existing categories, e.g. `startup clock gpio uart
   can adc timer dma flash rtc watchdog power isr protocol crypto libc rtos util hal app`
   plus component specific ones (`motor`, `foc`, `battery`, `vehicle`, `lighting`, `ble_host`,
   `ble_controller`, `upgrade`, `fmna`, ...).
7. Trivial functions (`bx lr`, getters, setters, default handlers) still get a full entry.
8. Do not touch other agents' files; write only the output file named in your work packet.

## Function note (annotations/<c>/functions/*.json)

```json
{
  "vcu_0159_08007c70": {
    "name": "rx_queue_count",
    "summary": "Number of unread entries in the 32-slot UART receive ring buffer",
    "description": "Returns head - tail modulo 32 for the receive ring. head is DAT_20002c2c (written by the RX ISR), tail is DAT_20002c30 (advanced by the consumer). The result is masked to 16 bits.",
    "category": "uart",
    "params": [],
    "returns": {"type": "u16", "description": "pending entries, 0..31"},
    "confidence": "high",
    "notes": "optional free text, e.g. open questions"
  }
}
```

## Data note (annotations/<c>/globals/*.json and tables/*.json)

An *object* is a variable, array or struct instance living at a RAM (or flash-table) address.
`anchor` is `[image, address]` of its first byte in the image the work packet shows;
`size` is in bytes; every accessed address inside `[anchor, anchor+size)` is thereby documented
(also in all other firmware versions - the harness translates it via the family map).

```json
{
  "vcu_g_0159_20002c20": {
    "name": "uart1_rx_ring",
    "type": "UartRing",
    "count": 1,
    "size": 48,
    "anchor": ["VCU_0159", "0x20002c20"],
    "category": "uart",
    "description": "State of the UART1 receive ring buffer ..."
  }
}
```
Use `types.json` for structs / enums (`fields` need offset, type, description; the sum must fit `size`).
For arrays of scalars use e.g. `"type": "u16", "count": 8`.

## Types (annotations/<c>/types.json)

```json
{"structs": {"UartRing": {"size": 48, "description": "...", "fields": [
    {"name": "buf", "offset": 0, "type": "u8", "count": 32, "description": "..."},
    {"name": "head", "offset": 32, "type": "u32", "description": "..."}]}},
 "enums": {"CanState": {"size": 1, "description": "...",
    "values": [{"name": "CAN_IDLE", "value": 0, "description": "..."}]}}}
```
