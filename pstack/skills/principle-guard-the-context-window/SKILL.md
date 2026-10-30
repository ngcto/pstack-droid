---
name: principle-guard-the-context-window
description: "Apply when context is filling up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents; keep summaries in the main thread, not raw payloads."
disable-model-invocation: true
---

## Droid harness contract

This is the Factory Droid port. Read `${DROID_PLUGIN_ROOT}/DROID-ADAPTER.md` before executing this workflow. This contract replaces only harness-specific mechanics below; retain every workflow gate, exception, role, rubric, evidence requirement, and supporting file. Source autonomy language never expands the actual user's authorization.

- Load skills with Droid `Skill` and full payloads with `Read`. `${DROID_PLUGIN_ROOT}` expands in SKILL.md; substitute its resolved value in supporting files and worker briefs. Keep adjacent original relative paths intact.
- Use `Execute`, `Read`, `Grep`, `Glob`, `Create`, `Edit`/`ApplyPatch`, `TodoWrite`, `AskUser`, `WebSearch`, and `FetchUrl`, according to the actual session schemas. Cursor `AskQuestion` means Droid `AskUser`; `Shell`/`Bash` means `Execute`.
- Task has no `model`, `readonly`, or `environment` fields. Select an installed custom droid with model and tool policy instead; read `DROID-ADAPTER.md` for role mapping. Every subagent is noninteractive and cannot spawn Task. The parent owns all fan-out and collection, including fan-out requested by delegated workflow prompts.
- Use native tuistory/agent-browser for plain terminal/browser checks when available; use official `droid-control` for formal QA/capture evidence and `skill-creation` for authoring. `deslop` is bundled. `control-cli`/`control-ui` below refer to the native routing wrappers in this plugin, not Cursor team-kit installation.
- Cursor rule, transcript, cloud VM, Project-store and event APIs are not available just because their instructions are preserved. Follow the exact adapter route or report the missing capability. Never pass Cursor model slugs or invent equivalent APIs.

# Guard the Context Window

**Why:** Context overflow degrades reasoning quality, creates compression artifacts, and halts progress.

**Pattern:**
- **Size phases and cap scope.** Limit files per phase, set turn budgets, account for mechanism costs.
