# Work-packet task (read by every annotation agent)

You are documenting firmware that belongs to the repo owner (their own e-scooter) for understanding
and maintainability.  Repo: /home/user/Zt3; harness CLI: `/opt/zt3-venv/bin/zt3`.

Inputs: `COMPONENT` (ble|vcu|mcu|bms), `PACKET` (e.g. `wave2_batch05`).

1. Read `/home/user/Zt3/docs/annotation-guide.md` and `/home/user/Zt3/docs/briefs/<COMPONENT>.md`.
2. Read the packet completely: `/home/user/Zt3/analysis/work/<COMPONENT>/<PACKET>.md`
   (decompiled C, callers, callees *with the summaries already written for them*, register and RAM refs).
   Callee summaries from earlier waves are authoritative context; reuse their names consistently.
3. Write `/home/user/Zt3/annotations/<COMPONENT>/functions/<PACKET>.json`: exactly one entry per
   `## \`family_id\`` heading, keyed by family id (schema: annotation guide).
4. Validate and fix until 0 problems:
   `/opt/zt3-venv/bin/zt3 validate /home/user/Zt3/annotations/<COMPONENT>/functions/<PACKET>.json --packet /home/user/Zt3/analysis/work/<COMPONENT>/<PACKET>.md`
5. Quality bar: say what the code actually does (algorithm, constants, side effects, which globals and
   registers, protocol bytes, state machine), not a restatement of the name.  Use real names for known
   library routines (vendor SDK, newlib, BTstack, wolfSSL, FreeRTOS, CMSIS).  Names unique and
   module-prefixed.  Mark guesses `medium`/`low` and say what is uncertain.  Where several functions
   obviously form a group (a state machine, a protocol layer) say so in each description.
6. Do not modify any file except your output JSON.  Do not open `/home/user/Zt3/ghidra_project`.
7. FINAL message: at most 4 lines - output path, entry count, validation result, one-line caveat.
