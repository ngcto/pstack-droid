---
name: control-ui
description: Drive the real app through Factory native controls.
compatibility: droid
---

# Native control-ui

For ordinary browser/Electron interaction load Droid's built-in `agent-browser` skill using `Skill` (not a built-in slash command). Prefer Droid's embedded, version-matched agent-browser driver through Execute; global npm installation is a fallback, not the primary route. For formal QA/evidence, recordings/demos or native desktop input load official `droid-control` using `Skill`. Route to browser-use for browser/Electron, or desktop-use when native desktop input is requested. Read the exact driver atom and capture/verify atoms requested by that skill through `Read`. Atoms are files, not individually registered skills. Prefer actual Factory mechanics over preserved Cursor team-kit drivers.

Retain the caller's before/after, baseline/candidate, negative-control, screenshot, transcript, raw-byte, or video evidence contract. Use a separate environment per concurrent controller; shared desktop input stays serialized. Install only needed real drivers. Never mock live behavior or weaken a gate because native tooling is unavailable. Report the exact missing dependency rather than a false pass.
