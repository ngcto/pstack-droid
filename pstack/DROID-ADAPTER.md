# Pstack on Factory Droid

This file is the operative harness translation for every bundled workflow. The full upstream pstack snapshot remains under assets/upstream/pstack and is not the executable instruction source. Active skills retain original steps and payloads plus narrowly scoped adaptations. License and upstream authorship remain intact.

## Authority and evidence

User authorization and Droid safety policy govern every action. Pstack's autonomy prose does not authorize messages, tickets, deployments, merges, pushes, destructive cleanup, provider configuration, or recurring jobs that the user did not request. Preserve every mandatory gate and original skip exception. Never turn a missing capability into a pass. A copied source tree is not proof of runtime equivalence.

## Loading and paths

Use Skill for registered skills, Read for full files and payloads. Resolve DROID_PLUGIN_ROOT once in the parent. Pass absolute plugin, poteto-mode, leaf/payload and working-checkout paths to each worker. Supporting files do not expand plugin-root variables. The active skills tree retains sibling-relative links, prompts, playbooks, fixtures, binaries and tests. The original docs are historical context; instructions about installing Cursor or editing Cursor configuration are not active setup instructions.

## Native tools

- Shell/Bash means Execute. Execute shell/cwd/environment does not persist between calls; include setup and actual command in the same call, or use absolute paths/git -C.
- AskQuestion means AskUser in the parent. Subagents cannot ask; return genuine decisions to the parent, do not invent answers.
- File read/search/write means Read/Grep/Glob/Create/Edit/ApplyPatch according to current schemas. TodoWrite tracks all original gates and explicit skips. Read images for evidence; do not invent a separate image-inspection API.
- Skills' allowed-tools is metadata, not a sandbox. Custom droid tool policy and runtime autonomy are the actual restrictions.
- For ordinary TUI/browser work prefer built-in `tuistory` and `agent-browser` skills via Skill; neither is a builtin slash command. Droid embeds/version-matches agent-browser and provisions it on Execute. Use official `droid-control` for formal QA, claim evidence, recordings/demos and desktop control. control-cli/control-ui route accordingly, not to copied Cursor drivers. Read terminal-use/browser-use/desktop-use atoms as files, not Skill names. Terminal recordings use the plugin's tctl; browser uses agent-browser. Real terminal-rendering/byte claims require true-input/pty-capture rather than a text snapshot.
- Authoring uses official skill-creation from droid-evolved. The create-skill wrapper preserves old caller references. Native /create-skill is an interactive wizard and cannot be silently approved inside a worker.
- deslop is imported under its MIT license from the same pinned cursor/plugins revision, retaining the exact workflow.

## Delegation and model translation

Task only accepts fields exposed by the installed schema. Do not send Cursor model, readonly, environment, or foreground controls. Choose subagent_type for enforced tools/model. Current CLI 1.0.0 Task is background and delivers completed reports automatically; stop a running task with TaskStop. Use TaskOutput only for a necessary progress peek or finished report, not a busy wait. Tool schema wins over documentation from another release.

Default role mapping:

- Playbook code/helper delegates without a specified model: poteto-agent.
- Explicit Claude judgment/prose/design/review seat: pstack-claude; read-only seat: pstack-claude-readonly.
- Explicit Grok code/explorer/verification seat: pstack-grok; read-only seat: pstack-grok-readonly.
- Explicit OpenAI seat: pstack-openai or pstack-openai-readonly.
- generalPurpose with no model: worker, or explorer for hard read-only inspection.
- Comment-only audit role: comment-sicko. It is report-only unless the exact authorized workflow calls for deleting comments; it must not write application logic.

The panel count, role prompts, partitions, independent verifier and exact-SHA evidence remain unchanged. Different droid names inheriting the same model do not establish model diversity. The shipped pinned role droids use actual CLI-listed IDs claude-opus-5-5, grok-4.7, gpt-6.1-sol with high reasoning. These are advertised IDs, not proof the user's account is entitled. Custom-droid fallback can silently use the parent model if blocked/unconfigured; check actual model before claiming diversity. If unavailable, report the lost independent-model gate and use the original allowed fallback only.

Cursor slugs bundle effort/speed; Droid separates model and reasoningEffort. Never pass claude-opus-5-5-xhigh or grok-4.7-xhigh-fast as a Droid model. setup-pstack maintains JSON role preferences and can create/update personal role droids after user approval; shipped plugin files remain unchanged. Task cannot override a droid's model in its call. High is the supported custom-droid effort in current public docs; max/xhigh budgeting cannot be assumed supported by its validator merely because exec accepts them.

## Nested orchestration and isolation

Droid Task subagents cannot spawn Task. Flatten requested sub-coordinator topology: the parent owns all dispatches, receives each bounded coordinator plan as an artifact, and launches its workers itself. Preserve role ownership and the three-level conceptual ledger without claiming nested execution. If a workflow strictly requires autonomous nested dispatch, report the limitation instead of silently dropping it.

Task does not create cloud VMs or isolated checkouts. Parent creates a separate git worktree per concurrent writer before dispatch and passes its path. A worktree is not OS/credential isolation. When the original gate requires a fresh cloud VM, use a configured Factory computer/environment or explicitly authorized disposable container. If none exists, report that gate blocked. Never label local worktree proof cloud isolation.

Cursor Project store/tracker becomes owned project artifacts, for example notes.md and a worker ledger tracking scope, branch, head, model, task_id, outputs and disposition. Preserve original schemas when specified. Missing cross-session event subscriptions are not invented: use native session/PR tools if present, otherwise obey the original no-polling rule and report the supervision gap. Scheduled work may use native Loop/CreateAutomation only with explicit user scheduling authorization. No daemon, loop or automation is enabled by installing this plugin.

## Transcript privacy and resumption

Use native session-navigation when available, or droid search in the active repository with explicit topic/window and limits. Inspect only this workspace and named session IDs. Droid sessions do not use Cursor's agent-transcripts layout or message.content[0].text parser. Resolve actual session files through native session metadata/schema, not a guessed workspace slug. Full chain-following eval evidence needs actual tool events; a tight digest is allowed only where the original workflow explicitly permits it. Otherwise report missing transcript evidence.

Session pickup uses droid --resume or exec --session-id with a saved real ID. Fork only when the task needs inherited state; capture branch/cwd/partial changes independently. Before cleanup, missing transcript recency is UNKNOWN, never proof inactivity.

## Preserved machinery and dependencies

All original support code, test corpora, shell helpers, guide chapters/images and dormant Benny workflows are retained. Original scripts must be inspected before execution. Bun tools require their pinned frozen lock dependencies; statechart Node tools require fast-check, Java/TLC for formal-model gates, and optional rendering tools. Do not install dependencies inside assets/upstream.

Invoke scripts via the additive scripts/pstack-droid.py helper, which copies runnable trees to a separate user-owned execution directory before dependency installation. It is not a sandbox. Arguments and side effects remain the original script's contract. check-plan and watch-pr are local source tooling, not Cursor APIs. worktree-audit is adapted to accept explicitly scoped Droid transcript directories; no default global/private session scan is allowed.

Benny is preserved under automations/benny. Its Cursor cloud configuration is not a deployed Factory automation. A future activation must translate trigger, authorized tools, credentials, machine/environment, schedule and delivery with exact readback. Installation does not activate it.

## Verification boundaries

Run scripts/pstack-droid.py verify for original hashes, complete file sets, active skill links and droid frontmatter. Run preserved unit suites from the isolated execution copy. Verify plugin installation with droid plugin list and the installed cache manifest. After user login, inspect /skills, /droids, /diagnostics and execute a disposable coding task with real tests plus a two-family Task panel. Never call offline discovery authenticated behavioral equivalence.
