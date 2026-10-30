---
name: setup-pstack
description: Configure Droid model and reasoning choices per pstack role.
compatibility: droid
---

# Setup Pstack on Droid

Configure native custom droids rather than Cursor Task model slugs or .mdc rules. Read `${DROID_PLUGIN_ROOT}/DROID-ADAPTER.md` first. Preserve the full original role/budget procedure at `${DROID_PLUGIN_ROOT}/assets/upstream/pstack/skills/setup-pstack/SKILL.md` as provenance; use the translated eight gates below for execution.

## Steps

1. **Detect models.** Run `droid exec --help` through Execute for advertised model IDs/efforts. After authentication, validate account availability with native model settings or an isolated task. Advertised is not entitled. Never append effort to a Droid model ID.
2. **Load state.** Read `~/.factory/pstack/models.json` if present and existing personal role droids. Preserve unrelated preferences. Shipped defaults are Claude Opus 5.5, Grok 4.7, and GPT-6.1 Sol with high reasoning. No preferences ledger exists until the user approves one.
3. **Budget, map, confirm.** AskUser for the original unlimited/max, large/xhigh, medium/high, small/medium budget choices, then show every role below and ask approval. Model/effort are separate Droid fields; custom-droid public docs support low/medium/high. Do not promise xhigh/max unless the installed validator accepts them. Show unsupported levels and ask for the nearest supported level instead of silently weakening the budget. Retain family choices, aliases, ordered judge pools and panel seat counts.
4. **Validate.** Every real model and effort must be observed in the current runtime surface, with entitlement separately checked after login. Missing authentication means pending validation, not success.
5. **Write after approval.** Use Create/Edit to save a versioned JSON role ledger at `~/.factory/pstack/models.json` with `budget` and `roles`, each role holding a list of `{droid, model, reasoningEffort, readOnly}`. This is pstack-owned metadata, not an invented Factory setting. Materialize each role/seat as a personal custom droid in `~/.factory/droids/` with name, description, model, reasoningEffort, and `tools: read-only` only where appropriate; omit tools for full workers, never `tools: all`. Preserve poteto-agent's full preloading and exact role prompt. Do not edit installed plugin caches.
6. **Confirm.** Read back each exact file and inspect `/droids`, `/diagnostics`. After login, run a disposable role task and record its actual model/fallback. Task uses subagent_type rather than a model argument. A ledger preference alone does not change execution.
7. **Offer verification once.** If the repo has no real-app verification skill/harness, offer `/create-verification-skill`, then proceed only if accepted.
8. **Offer formal verification once.** If no formal-model gate exists, offer `/create-formal-verification-skill`. A skill file is not a completed proof.

## Complete role list

- feature, refactoring
- bug-fix
- perf-issue
- hillclimb
- judgment and prose
- hardest tasks
- how explorer
- how explainer
- why investigators
- why synthesizer
- reflect tooling
- reflect judgment, divergent, synthesizer
- arena runners (panel)
- arena cross-judge pool (ordered candidates, one judge from a non-parent family)
- swarm workers
- architect runners (panel)
- interrogate reviewers (panel)

Re-runs update only approved owned definitions/metadata, preserve chosen families and aliases, and show retired role lines before dropping them. inherit-parent/auto mean the parent model, not guaranteed diversity. Parent loads this ledger on demand; no unsupported always-applied .mdc rule is installed.
