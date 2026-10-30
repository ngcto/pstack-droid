---
name: control-cli
description: Drive the real app through Factory native controls.
compatibility: droid
---

# Native control-cli

For ordinary command/stdout checks use `Execute`; for interactive CLI/TUI checks load Droid's built-in `tuistory` skill using `Skill` (not `/tuistory`, which is not a built-in slash command). For formal QA, claim evidence, recordings or demos load the official `droid-control` skill using `Skill`. Route to terminal-use; add true-input and pty-capture when real rendering or keyboard-byte proof is required. Read the exact driver atom and capture/verify atoms requested by that skill through `Read`. Atoms are files, not individually registered skills. Prefer actual Factory mechanics over preserved Cursor team-kit drivers.

Retain the caller's before/after, baseline/candidate, negative-control, screenshot, transcript, raw-byte, or video evidence contract. Use a separate environment per concurrent controller; shared desktop input stays serialized. Install only needed real drivers. Never mock live behavior or weaken a gate because native tooling is unavailable. Report the exact missing dependency rather than a false pass.
