---
name: reflect
description: Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect.
disable-model-invocation: true
---

## Droid harness contract

This is the Factory Droid port. Read `${DROID_PLUGIN_ROOT}/DROID-ADAPTER.md` before executing this workflow. This contract replaces only harness-specific mechanics below; retain every workflow gate, exception, role, rubric, evidence requirement, and supporting file. Source autonomy language never expands the actual user's authorization.

- Load skills with Droid `Skill` and full payloads with `Read`. `${DROID_PLUGIN_ROOT}` expands in SKILL.md; substitute its resolved value in supporting files and worker briefs. Keep adjacent original relative paths intact.
- Use `Execute`, `Read`, `Grep`, `Glob`, `Create`, `Edit`/`ApplyPatch`, `TodoWrite`, `AskUser`, `WebSearch`, and `FetchUrl`, according to the actual session schemas. Cursor `AskQuestion` means Droid `AskUser`; `Shell`/`Bash` means `Execute`.
- Task has no `model`, `readonly`, or `environment` fields. Select an installed custom droid with model and tool policy instead; read `DROID-ADAPTER.md` for role mapping. Every subagent is noninteractive and cannot spawn Task. The parent owns all fan-out and collection, including fan-out requested by delegated workflow prompts.
- Use native tuistory/agent-browser for plain terminal/browser checks when available; use official `droid-control` for formal QA/capture evidence and `skill-creation` for authoring. `deslop` is bundled. `control-cli`/`control-ui` below refer to the native routing wrappers in this plugin, not Cursor team-kit installation.
- Cursor rule, transcript, cloud VM, Project-store and event APIs are not available just because their instructions are preserved. Follow the exact adapter route or report the missing capability. Never pass Cursor model slugs or invent equivalent APIs.

# Reflect

Mine the current conversation for durable learnings, then route them into skill edits.

Invoke when the user says "reflect" or "/reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## 1. Locate the active transcript

Discover session metadata through the available native session-navigation tools or `droid search` after reading its current help. Limit the topic, time window, and active repository. CLI search can span local sessions even when invoked from this directory, so do not treat cwd as a privacy filter: use a verified workspace filter if exposed; otherwise scope the candidate metadata before opening any message/tool content, or stop if metadata-only discovery is unavailable. Validate the real session ID, workspace, and opening user prompt through the returned metadata. Read only the exact in-scope session export/path that the native tool reports, after inspecting its actual schema. Never guess directories, UUID layouts, or JSON fields. Search excerpts are not full tool traces. If the active conversation cannot be matched or exported, pass a tight digest of this session as the original fallback permits. Label it a digest, include evidence pointers actually observed, and do not claim exhaustive transcript auditing.

## 2. Spawn three reviewers in parallel

One parent message, three Task calls to report-only role droids. Reviewers need narrowly granted read-only MCP access for cited tickets, chat threads and observability traces. Verify exact tool policy; parent-provided reads are permitted when the connector cannot be exposed safely. The parent launches all Task calls, records task IDs and waits for automatically delivered completed reports at each phase barrier. Launch acknowledgements are not findings. No child spawns Task or shell-launches nested droids. When only reports remain, end the turn; do not poll or block on TaskOutput.

Read the role entries in `~/.factory/pstack/models.json` explicitly; this is an adapter preferences ledger, not an automatically applied rule. Resolve each seat to an installed native droid as defined in `DROID-ADAPTER.md`: Claude `pstack-claude`, Grok `pstack-grok`, OpenAI `pstack-openai`, with `-readonly` for report-only work. Use approved configured variants for other model/effort choices, never a Task model override. An `auto` or `inherit-parent` seat needs a verified inherit droid without a complexity override, not the Factory Auto router. Verify the effective model family before claiming diversity; names and advertised IDs alone are not evidence. Keep every repeated seat. If a configured droid is unavailable, disclose it, try its family default, then an available validated same-family variant; never retry a known-rejected target. Use only the calling workflow's explicit fallback if that fails.

| Lens | Role line | Default native droid | Prompt template |
|---|---|---|---|
| Judgment | `reflect judgment, divergent, synthesizer` | `pstack-claude-readonly` | `references/judgment-reviewer.md` |
| Tooling | `reflect tooling` | `pstack-grok-readonly` | `references/tooling-reviewer.md` |
| Divergent | `reflect judgment, divergent, synthesizer` | `pstack-claude-readonly` | `references/divergent-reviewer.md` |

Pass each template verbatim, substituting the transcript path or digest where marked. Reviewers return findings in their automatically delivered completed Task reports.

## 3. Synthesize

After all three complete reports, the parent launches one Task resolving `reflect judgment, divergent, synthesizer`, default `pstack-claude-readonly`. It spot-verifies citations through allowed read-only MCP tools or evidence supplied by the parent. Pass `references/synthesizer.md` verbatim, with each reviewer's full output inlined where marked. It returns an Accepted / Rejected / Backlog list.

## 4. Structural enforcement check

Move any Accepted item that a lint rule, script, metadata flag, or runtime check would enforce more reliably to Backlog. See the **encode-lessons-in-structure** principle skill.

## 5. Apply

Present the synthesizer's full Accepted / Rejected / Backlog output and wait for explicit approval before applying any Accepted edit. The user picks the subset and may redirect routings. Skill changes affect every future agent in the org. Do not auto-apply.

File each Backlog item to your team's devex or backlog tracker without waiting. Only the Accepted list waits for approval.

Never edit a skill under `plugins/cache/`. Before approval, show its destination, `.factory/skills/<skill>/` or `~/.factory/skills/<skill>/`. After approval, copy the skill folder there and edit the copy. Never open a PR or push.

Follow each approved row's Routing exactly:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): the parent does it directly.
- Substantive existing-skill edit (a new section, a new pattern table, more than ~10 lines): hand to Droid-native `skill-creation` skill and run its draft / test / iterate loop.
- `tune description: <skill path>` (the skill exists but didn't trigger when it should have): hand to `create-skill` and run its description-optimization loop.
- `new skill via create-skill: <kebab-name>`: hand creation to `create-skill`. Do not invent the shape ad hoc.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done.

## 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
