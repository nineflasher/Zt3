# Data-packet task (RAM variables and flash tables)

You are documenting firmware that belongs to the repo owner (their own e-scooter) for understanding
and maintainability.  Repo: /home/user/Zt3; harness CLI: `/opt/zt3-venv/bin/zt3`.

Inputs: `COMPONENT` (ble|vcu|mcu|bms), `PACKETS` (one or more, e.g. `data_adc_batch01 data_app_batch02`).

1. Read `/home/user/Zt3/docs/annotation-guide.md` (sections "Data note" and "Types") and
   `/home/user/Zt3/docs/briefs/<COMPONENT>.md`.
2. For each packet read `/home/user/Zt3/analysis/work/<COMPONENT>/<PACKET>.md`.  Each `## \`id\`` heading is
   one variable family: its address in the anchor build, the builds it exists in, the functions that read
   (R) / write (W) / take its address (A), and the decompiled lines that touch it.  The functions are
   already documented: their names and descriptions are in `annotations/<COMPONENT>/functions/*.json`
   (grep the name) and the decompiled C is in `analysis/decomp/<COMPONENT>/<IMAGE>.json`
   (key `"0x<addr>"`; query it with a short python script, do not read the file whole).
3. Decide the OBJECTS.  Adjacent addresses used by the same functions with a stride are one array;
   addresses accessed through one base pointer with fixed offsets are one struct.  Describe each object
   ONCE: `anchor` = [anchor image, start address], `size` = total bytes, `type` (scalar, `u8`.. `f32`,
   `ptr`, or a struct/enum you define), `count` for arrays.  Every heading in the packet must fall inside
   some object you write (the validator checks this).  Unused padding between objects is not an object.
4. Write `/home/user/Zt3/annotations/<COMPONENT>/globals/<PACKET>.json` (tables: `.../tables/<PACKET>.json`)
   keyed by the family id of the object's FIRST address (the heading id), and any structs/enums to
   `/home/user/Zt3/annotations/<COMPONENT>/types/<PACKET>.json` (struct names must be new - grep
   `annotations/<COMPONENT>/types/` first; reuse an existing struct by name when the layout is the same).
5. Validate each file and fix until 0 problems:
   `/opt/zt3-venv/bin/zt3 validate <globals file> --packet <packet .md>` and
   `/opt/zt3-venv/bin/zt3 validate <types file>` (if you wrote one).
6. Names: `snake_case`, module-prefixed, unique within the component (grep existing globals/ files);
   descriptions say what the value means (units, range, who produces it, who consumes it, when it
   resets), not just "variable used by X".  Mark guesses with wording like "probably".  Never write key
   or secret bytes into a description; say where such material lives and how it is used instead.
7. Modify no other files.  Do not open `/home/user/Zt3/ghidra_project`.
8. FINAL message: at most 4 lines - files written, object/struct counts, validation result, one caveat.
