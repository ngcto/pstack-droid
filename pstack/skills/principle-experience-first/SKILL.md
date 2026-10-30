---
name: principle-experience-first
description: "Apply when product, UX, or feature-scope tradeoffs come up. Choose user delight over implementation convenience; ship fewer polished features over more rough ones."
disable-model-invocation: true
---

## Droid harness contract

This is the Factory Droid port. Read `${DROID_PLUGIN_ROOT}/DROID-ADAPTER.md` before executing this workflow. This contract replaces only harness-specific mechanics below; retain every workflow gate, exception, role, rubric, evidence requirement, and supporting file. Source autonomy language never expands the actual user's authorization.

- Load skills with Droid `Skill` and full payloads with `Read`. `${DROID_PLUGIN_ROOT}` expands in SKILL.md; substitute its resolved value in supporting files and worker briefs. Keep adjacent original relative paths intact.
- Use `Execute`, `Read`, `Grep`, `Glob`, `Create`, `Edit`/`ApplyPatch`, `TodoWrite`, `AskUser`, `WebSearch`, and `FetchUrl`, according to the actual session schemas. Cursor `AskQuestion` means Droid `AskUser`; `Shell`/`Bash` means `Execute`.
- Task has no `model`, `readonly`, or `environment` fields. Select an installed custom droid with model and tool policy instead; read `DROID-ADAPTER.md` for role mapping. Every subagent is noninteractive and cannot spawn Task. The parent owns all fan-out and collection, including fan-out requested by delegated workflow prompts.
- Use native tuistory/agent-browser for plain terminal/browser checks when available; use official `droid-control` for formal QA/capture evidence and `skill-creation` for authoring. `deslop` is bundled. `control-cli`/`control-ui` below refer to the native routing wrappers in this plugin, not Cursor team-kit installation.
- Cursor rule, transcript, cloud VM, Project-store and event APIs are not available just because their instructions are preserved. Follow the exact adapter route or report the missing capability. Never pass Cursor model slugs or invent equivalent APIs.

# Experience First

When implementation convenience conflicts with user delight, choose delight.

- Every feature, control, and option must be justified
- Ship less, ship better (polished experience with three features beats rough one with ten)
- Prototype before committing (design decisions are cheaper in throwaway HTML than production code)
- Get the details right (transitions, alignment, spacing, feedback, error states)
- Tighten the core loop (every feature should serve the central workflow or get out of the way)

The user is whoever consumes the work. For a UI that is the end user. For a library or an internal API it is the colleague who imports it. The engineer who maintains the code next is a user too. Weigh their experience the same way, and explain impact from their perspective.

Foundations should serve the experience. Foundational thinking governs the *sequence* of work. This principle governs the *target*.
