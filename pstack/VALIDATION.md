# Executed Validation

## Installation and preservation

- Droid npm package 1.0.0 installed; `droid --version`, exec help and tool listing executed successfully without authentication.
- Native `pstack@droid-pstack-marketplace` accepted by plugin manager and read back Enabled at user scope.
- Official `droid-control@factory-plugins` and `droid-evolved@factory-plugins` installed and read back Enabled, official revision `8a5f8db2e350`.
- Source revision `4dd1d05818d19792e7cd6e818f1667f95f7e1dbe`; pristine copy exact file set and SHA-256 verification PASS for all 573 files. Installed cache preservation check also PASS.
- 58 original top-level skills retained; four additions (deslop, native control-cli/control-ui, create-skill bridge) produce 62 active top-level skills. Two original role contracts adapted with model inheritance; no model-pinned variants are shipped.
- Six additive port unit checks passed. All relative Markdown links from skill entries resolved in the offline verifier.
- Native command-policy validation executed: three active builtins, zero invalid/failed rules.

## Preserved executable suites

Ran in a separate execution copy, not source/provenance/cache:

- Poteto scripts: `bun install --frozen-lockfile`; `bun test watch-pr check-plan.test.ts`: 61 pass, zero fail. `bun run typecheck`: exit zero.
- Statechart: `npm install --ignore-scripts --no-audit --no-fund`; `npm test`: 334 tests, 267 pass, zero fail, 67 skipped. Skips explicitly require TLA2TOOLS for real TLC/differential checks; replay/parser/render/unit tests passed, not real fresh formal proof.
- Renderer tests emitted a jsdom canvas getContext warning; runner still exited zero. Do not interpret that as tested raster fidelity.

## Native driver smoke tests

- Installed tuistory 0.12.0, asciinema 2.4.0, fallback global agent-browser 0.41.0.
- Official droid-control tctl launched an owned Bash session, typed/executed a marker command, waited/observed marker output and finalized a real asciicast on close. Exit zero.
- agent-browser downloaded-browser install failed because Linux ARM64 has no Chrome-for-Testing build. Used existing ARM64 Playwright Chromium with explicit executable path; opened a local data HTML page, captured the real Ready button accessibility snapshot, closed owned session. Exit zero.
- Static installed binary inspection verified built-in names agent-browser/tuistory and embedded agent-browser asset handling. Prefer Droid's version-matched embedded browser in native sessions; fallback global-driver smoke does not prove embedded driver extraction/execution.

## Explicitly not verified

- User login/authenticated inference, effective `/skills` and `/droids` validator/UI discovery, actual role model entitlement/effort and fallback, diverse-model Task panels.
- Full coding playbook, bugfix reproduction/red-green test/same-surface independent proof, exact tool-chain transcript audit, nested coordinator equivalence (unsupported Task children).
- Fresh cloud VM isolation, remote environments, event subscriptions, persistent/offline orchestration.
- Real Java/TLC differential/fuzz corpus tests; 67 real-model checks skipped.
- Native desktop or true-input compositor proof, video conversion/composition dependencies including agg/renderer build.
- Recurring automations, webhooks, Slack deliveries, PR publishing/merging, provider or credential changes. Benny remains dormant.

A preservation PASS, accepted plugin install, or zero CLI exit is not a claim of logged-in workflow equivalence. Resume the named post-login gates after the user authenticates.
