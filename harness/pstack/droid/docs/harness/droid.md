# Pstack in Droid

Read this file once per session before following a pstack workflow. Keep the original workflow steps and evidence requirements; translate only the harness names below. `<pstack>` is the installed plugin root. User authorization and Droid safety policy override source autonomy wording. Never send fields absent from the current tool schema.

## Tools and skill routes

| Cursor | Droid |
| --- | --- |
| Task | Task; the parent owns fan-out because Droid children cannot spawn Task. A child returns the needed worker plan/questions to its parent. |
| AskQuestion | AskUser in the interactive parent; children report questions instead. |
| Shell/Bash | Execute. Shell cwd/env do not persist between calls; include setup and use together. |
| todolist | TodoWrite, with the original gates and explicit skips. |
| another pstack skill | Read `<pstack>/skills/<name>/SKILL.md` in full, then follow it; Skill when the effective catalog supports invocation. |
| control-cli | Built-in tuistory via Skill for TUI; Execute for ordinary command output. |
| control-ui | Built-in agent-browser via Skill for browser/Electron. Prefer Droid's embedded driver. |
| formal QA, recordings, demos, native desktop | Official droid-control skill; read its routed atom files, not invented atom skill names. |
| Cursor create-skill | Official skill-creation from droid-evolved; native /create-skill is a reviewed interactive wizard, not an automatic worker approval. |
| deslop from cursor-team-kit | Bundled deslop. |

## Subagent fields and models

| Cursor | Droid |
| --- | --- |
| generalPurpose | worker; explorer for source-only read-only exploration. |
| poteto-agent, comment-sicko | Original specialized droids of those names, model: inherit. |
| readonly: true/false | Drop field. Explorer enforces read-only; worker briefs retain exact scope/no-write constraints where command/MCP evidence is needed. |
| model, effort-bearing provider slug, fast setting | Drop field/value. User configures native `/settings` → Subagents; select Task complexity light/medium/heavy by difficulty. No provider-specific droids or custom model ledger. |
| per-role model rule / pstack-models.mdc | Native Subagents configuration, not an installed rule file. Panel count/roles remain; model diversity needs actual resolved-family evidence. Report unavailable diversity, use only the original permitted fallback. |
| environment: cloud/local, cloud_base_branch | Drop fields. Parent provisions/passes isolated worktrees at the exact branch/SHA; a worktree is not a fresh cloud VM. A strict fresh-machine gate requires a configured authorized environment or remains blocked. |
| run_in_background | Follow actual Task schema; current CLI delivers background completion reports automatically. Launch ID is not a result; do not busy-poll TaskOutput. |
| resume | Actual prior Task ID, only when needed by original fresh-worker rules. |
| file_attachments | Absolute file pointers; image_paths for images when supported. |

## setup-pstack

Follow the original setup intent using native `/settings` → Subagents Light/Medium/Heavy model, effort and autonomy choices. Preserve existing user preferences unless asked to configure them. No .mdc rule, JSON role ledger or model-specific droid is created. Confirm actual user-chosen routing after login; advertised model choices are not entitlement proof. Retain the original optional project verification and formal-verification offers.

## Paths, transcripts and source docs

| Cursor | Droid |
| --- | --- |
| .cursor/skills/, ~/.cursor/skills/ | .factory/skills/, ~/.factory/skills/. |
| ~/.cursor/plugins/, .cursor-plugin/plugin.json | Parent supplies the exact active plugin path; native .factory-plugin/plugin.json. Do not pick an arbitrary highest-version cache. |
| always-applied .mdc rules | Applicable AGENTS.md guidance or native settings, depending on intent; never claim Droid reads .mdc. |
| Cursor agent-transcripts layout / parser | Native session metadata/search/export in the current workspace and named session only. Inspect the actual schema; never guess a path or scan unrelated chats. Use digest fallback only where the original permits it; otherwise missing full trace is a blocker. |
| Cursor custom-mode persistence/hotkeys | Explicitly invoke the skill for the new task; do not promise sticky mode or unsupported shortcuts. |
| copied Cursor setup/guide commands | Historical source guidance; use README-DROID.md and native plugin manager for installation. |

## Host-specific features

Use native Loop/automation tools only when their current schema supports the exact user-authorized workflow. Installation does not activate Benny, schedules, remote control or external writes. Cursor update_state, SendToUser secret requests, api2.cursor.sh receiver URLs, auth headers and payload schemas have no automatic mapping. Retain webhook/Slack safety gates and stop at missing protected-secret provisioning or unverified delivery contracts, not a guessed API.

Use the forge commands the workflow gives (gh/Origin), with exact-head review and user authorization. Bugbot comments remain real review threads, not renamed Factory checks. Native project artifacts can retain notes/ownership/evidence; Cursor Project-store/event APIs are not invented. Flatten nested coordination without dropping independent review roles. Missing mandatory verification is incomplete, not passed.

## Scripts and preservation

Original scripts/payloads remain adjacent and complete. Use scripts/pstack-droid.py to stage a separate writable execution copy before dependency installation; pristine assets/upstream is never executed or modified. worktree-audit accepts only an explicitly scoped transcript directory and holds unknown recency. The verifier checks preserved source bytes/file sets and native packaging, not logged-in behavioral equivalence.
