# Pstack Droid Plugin

Full pstack 0.15.36, ported from cursor/plugins revision `4dd1d05818d19792e7cd6e818f1667f95f7e1dbe` to a native Factory Droid plugin. Original MIT authorship/license remain. No login, automation activation, remote-control registration, external publishing, or global model preference changes are performed by installation.

## Install

Droid and Node are required. The local marketplace contains this plugin under `pstack/` and its catalog under `.factory-plugin/marketplace.json`.

```sh
droid plugin marketplace add /path/to/droid-pstack-marketplace
droid plugin marketplace list
droid plugin install pstack@droid-pstack-marketplace --scope user
droid plugin marketplace add https://github.com/Factory-AI/factory-plugins
droid plugin install droid-control@factory-plugins --scope user
droid plugin install droid-evolved@factory-plugins --scope user
droid plugin list --scope user
```

Read the actual registered marketplace name back if your directory name differs. Local marketplace updates require an explicit plugin update/reinstallation; do not edit plugin cache files.

## Login and use

Launch `droid` in the target repo and sign in with `/login` if prompted. In a new session inspect `/plugins`, `/skills`, `/droids`, and `/diagnostics`. Invoke `/poteto-mode` for a full playbook, `/poteto-help` for routing, or a specific skill such as `/how`, `/architect`, `/tdd`, `/statechart`.

Native skill frontmatter preserves manual-only invocation where upstream declares it. `/setup-pstack` configures actual Droid role definitions after approval; no Cursor rule file is written. Native controls use `droid-control` driver atoms. Those atoms are files, not separate registered skills.

## Preserved and adapted

- Every original source file is retained byte-for-byte under `assets/upstream/pstack/`, with SHA-256 inventory and revision in `preservation-manifest.json`.
- Every original top-level skill has an active native entry, with the full workflow, supporting references, playbooks, scripts, fixtures, guide/image assets and dormant Benny configuration retained.
- Cursor role agents become plugin `droids/`. Additional Claude/Grok/OpenAI role seats use separate real model/effort fields.
- MIT deslop dependency is bundled from the same revision. control-cli/control-ui route to official Factory controls, rather than duplicating browser/terminal tooling. create-skill routes to official skill-creation.
- DROID-ADAPTER.md records exact translations and limits. Nested Task, Cursor cloud/environment arguments, Project store/event APIs and model-slug syntax are not falsely represented as Droid features.
- Shipped pinned model IDs are advertised by this CLI but account entitlement and possible inherited-model fallback remain unverified until login.

## Run preserved scripts safely

Do not install dependencies or execute generators inside `assets/upstream/`. The additive helper stages a separate runnable skills copy under a user-owned execution root:

```sh
python /path/to/pstack/scripts/pstack-droid.py verify
python /path/to/pstack/scripts/pstack-droid.py doctor
python /path/to/pstack/scripts/pstack-droid.py stage
python /path/to/pstack/scripts/pstack-droid.py run skills/poteto-mode/scripts/check-plan.mjs -- /path/to/plan.md
```

For watch-pr use Bun and its frozen lockfile in the staged directory. For statechart use current Node, fast-check and real Java/TLC when formal-model checks are requested. These helpers are not a sandbox; original side effects still require task authorization. The port does not start PR watchers or recurring jobs by itself.

## Native driver prerequisites

Terminal control requires `tuistory` and `asciinema`. Browser control requires `agent-browser` plus Chromium. On Linux ARM64, `agent-browser install` cannot download Chrome for Testing; use an existing verified ARM64 Chromium executable through `AGENT_BROWSER_EXECUTABLE_PATH` or `--executable-path`. Do not disable browser sandboxing as a workstation workaround. Demo video composition additionally needs agg and renderer/toolchain dependencies; desktop/true-input needs platform drivers and OS permissions. Install those only when the actual task needs them.

## Verification scope

Read VALIDATION.md for actual executed tests and explicit skips. Offline preservation and plugin manager acceptance do not establish logged-in skill invocation, model diversity or behavioral coding equivalence. After login, run a disposable repo coding task, confirm all required gates with independent tests, then test two-family Task delegation and native controls on the real requested app.
