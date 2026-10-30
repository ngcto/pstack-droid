---
name: sharpen
description: "Make a task deeper, not bigger, then rewrite the prompt. Use for /sharpen."
disable-model-invocation: true
---

## Droid harness contract

This is the Factory Droid port. Read `${DROID_PLUGIN_ROOT}/DROID-ADAPTER.md` before executing this workflow. This contract replaces only harness-specific mechanics below; retain every workflow gate, exception, role, rubric, evidence requirement, and supporting file. Source autonomy language never expands the actual user's authorization.

- Load skills with Droid `Skill` and full payloads with `Read`. `${DROID_PLUGIN_ROOT}` expands in SKILL.md; substitute its resolved value in supporting files and worker briefs. Keep adjacent original relative paths intact.
- Use `Execute`, `Read`, `Grep`, `Glob`, `Create`, `Edit`/`ApplyPatch`, `TodoWrite`, `AskUser`, `WebSearch`, and `FetchUrl`, according to the actual session schemas. Cursor `AskQuestion` means Droid `AskUser`; `Shell`/`Bash` means `Execute`.
- Task has no `model`, `readonly`, or `environment` fields. Select an installed custom droid with model and tool policy instead; read `DROID-ADAPTER.md` for role mapping. Every subagent is noninteractive and cannot spawn Task. The parent owns all fan-out and collection, including fan-out requested by delegated workflow prompts.
- Prefer native `droid-control` for browser/terminal/desktop evidence and `skill-creation` for authoring. `deslop` is bundled. `control-cli`/`control-ui` below refer to the native routing wrappers in this plugin, not Cursor team-kit installation.
- Cursor rule, transcript, cloud VM, Project-store and event APIs are not available just because their instructions are preserved. Follow the exact adapter route or report the missing capability. Never pass Cursor model slugs or invent equivalent APIs.

I want a deeper version of this task, not a bigger one. Before rewriting it, do four things:

1. Say what a top professional in this field would do here that I'm not asking for.
2. Name the rawest material they would start from instead of what has already been digested for me.
3. Name the specific methods and tools they would use.
4. Say what, other than you or me, would show the result is right.

Then rewrite my prompt to ask for exactly that.

Leave choices that are mine to make open instead of deciding them.
