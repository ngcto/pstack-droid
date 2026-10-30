# Droid port changelog

This is an additive native Factory Droid port of the complete pinned upstream pstack snapshot at `4dd1d05818d19792e7cd6e818f1667f95f7e1dbe`. Pristine `assets/upstream/pstack` is provenance and remains untouched. Original authorship/license, full workflow phase lists, gates, rubrics, prompts, references and executable payloads remain in the package; this adaptation changes runtime instructions rather than replacing workflows with summaries.

## Semantic adaptations

- How, why, reflect, arena, swarm and interrogate use native worker/explorer and user-configured complexity routing. No provider-specific droids or custom model ledger is shipped. Panel counts and diversity evidence gates remain.
- The parent owns all dispatches and continuation barriers. Teach, comment review, PR owners and conceptual sub-coordinators return plans/questions; the parent runs complete how/why/review graphs with original payloads. Background launch IDs are not completed verdicts; no Task polling or nested shell-launched droids.
- Transcript discovery uses native metadata and actual export schema scoped to active workspace/session/topic/time. No Cursor UUID layout or message parser is assumed. Full trace requirements remain blocked if only excerpts are available; reflect retains its explicit digest fallback.
- Native tuistory/agent-browser are for plain checks; official droid-control owns formal same-surface QA and captures. Worktrees do not claim fresh-machine isolation. Native Loop retains authorized cadence, predicates, replay safety and pause/cancel lifecycle without inventing dynamic event semantics.
- Poteto help uses GitHub marketplace installation, explicit per-task skill invocation, native project/droid verification and accurate bundled dependency claims. Public upstream links are revision-pinned and labeled provenance.
- Webhook UI uses guarded native CreateAutomation and exact ReadAutomation verification, preserving server-only keys, payload distrust, timeout/single try, log fallback, tailnet access and harmless-probe gates. Creation stops at unavailable protected one-time-secret provisioning; auth header, receiver URL and delivered payload schema are never guessed.
- Benny uses `.factory/automations/benny/`, separate user config, `prefer_factory_actions`, native project installation and reviewed native automation create/read/edit procedures. Complete committed-code, approval/readiness, channel, target, disabled-state, integration, immutable thread, trusted marker, no-Slack-secret/write worker, repro-twice, media, existing-fix and bounded-draft-PR gates remain. It stays dormant on import.

## Verification and unresolved limits

Static prose/frontmatter/link and payload-preservation checks accompany this edit. No login, authenticated model execution, transcript-schema probe, live QA, webhook/Slack delivery, automation activation, PR write or merge is claimed. Public CLI tool descriptions advertise capabilities; they do not validate account access or all current input schemas. Native webhook secret handling and session metadata-only scoping are explicit fail-closed boundaries. See [capability ledger](docs/harness/droid-capabilities.md). Packaging, publishing, GitHub-method install and full integration validation are separate acceptance steps.

## Modified active paths

- `CHANGELOG-DROID.md`
- `automations/benny/FOR_AGENTS.md`
- `automations/benny/README.md`
- `automations/benny/skills/reproduce-and-fix-issues/SKILL.md`
- `automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md`
- `automations/benny/skills/reproduce-and-fix-issues/references/feature-map.example.md`
- `automations/benny/skills/setup-benny/SKILL.md`
- `automations/benny/skills/triage-issue-reports/SKILL.md`
- `automations/benny/skills/triage-issue-reports/references/routing.example.md`
- `automations/benny/templates/configuration.example.yaml`
- `automations/benny/templates/reproduce-automation-prompt.md`
- `automations/benny/templates/triage-automation-prompt.md`
- `docs/harness/droid-capabilities.md`
- `skills/architect/SKILL.md`
- `skills/arena/SKILL.md`
- `skills/automate-me/SKILL.md`
- `skills/benchmark-checklist/SKILL.md`
- `skills/blast-radius/SKILL.md`
- `skills/bro/SKILL.md`
- `skills/correct/SKILL.md`
- `skills/create-formal-verification-skill/SKILL.md`
- `skills/create-verification-skill/SKILL.md`
- `skills/deslop/SKILL.md`
- `skills/figure-it-out/SKILL.md`
- `skills/how/SKILL.md`
- `skills/in-your-own-words/SKILL.md`
- `skills/interrogate/SKILL.md`
- `skills/ketchup-video/SKILL.md`
- `skills/ketchup/SKILL.md`
- `skills/maintain-formal-verification-skill/SKILL.md`
- `skills/maintain-verification-skill/SKILL.md`
- `skills/make-bot-ui/SKILL.md`
- `skills/no-comments/SKILL.md`
- `skills/poteto-help/SKILL.md`
- `skills/poteto-help/references/prompting.md`
- `skills/poteto-help/references/recipes.md`
- `skills/poteto-mode/SKILL.md`
- `skills/poteto-mode/playbooks/autonomous-run.md`
- `skills/poteto-mode/playbooks/autopilot-full.md`
- `skills/poteto-mode/playbooks/babysit.md`
- `skills/poteto-mode/playbooks/bug-fix.md`
- `skills/poteto-mode/playbooks/eval.md`
- `skills/poteto-mode/playbooks/feature.md`
- `skills/poteto-mode/playbooks/hillclimb.md`
- `skills/poteto-mode/playbooks/multi-phase-plan.md`
- `skills/poteto-mode/playbooks/orchestrate.md`
- `skills/poteto-mode/playbooks/perf-issue.md`
- `skills/poteto-mode/playbooks/refactoring.md`
- `skills/poteto-mode/playbooks/session-pickup.md`
- `skills/poteto-mode/playbooks/shipping.md`
- `skills/poteto-mode/playbooks/visual-parity.md`
- `skills/poteto-mode/playbooks/worktree-cleanup.md`
- `skills/principle-attack-the-premise/SKILL.md`
- `skills/principle-boundary-discipline/SKILL.md`
- `skills/principle-build-the-lever/SKILL.md`
- `skills/principle-encode-lessons-in-structure/SKILL.md`
- `skills/principle-exhaust-the-design-space/SKILL.md`
- `skills/principle-experience-first/SKILL.md`
- `skills/principle-explain-the-number/SKILL.md`
- `skills/principle-fix-root-causes/SKILL.md`
- `skills/principle-foundational-thinking/SKILL.md`
- `skills/principle-guard-the-context-window/SKILL.md`
- `skills/principle-laziness-protocol/SKILL.md`
- `skills/principle-make-operations-idempotent/SKILL.md`
- `skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md`
- `skills/principle-minimize-reader-load/SKILL.md`
- `skills/principle-model-the-domain/SKILL.md`
- `skills/principle-never-block-on-the-human/SKILL.md`
- `skills/principle-outcome-oriented-execution/SKILL.md`
- `skills/principle-prove-it-works/SKILL.md`
- `skills/principle-redesign-from-first-principles/SKILL.md`
- `skills/principle-separate-before-serializing-shared-state/SKILL.md`
- `skills/principle-sequence-verifiable-units/SKILL.md`
- `skills/principle-subtract-before-you-add/SKILL.md`
- `skills/principle-test-behavior-not-implementation/SKILL.md`
- `skills/principle-type-system-discipline/SKILL.md`
- `skills/recall/SKILL.md`
- `skills/reflect/SKILL.md`
- `skills/reflect/references/divergent-reviewer.md`
- `skills/reflect/references/judgment-reviewer.md`
- `skills/reflect/references/tooling-reviewer.md`
- `skills/sharpen/SKILL.md`
- `skills/show-me-your-work/SKILL.md`
- `skills/statechart/SKILL.md`
- `skills/swarm/SKILL.md`
- `skills/tdd/SKILL.md`
- `skills/teach/SKILL.md`
- `skills/technical-writing/SKILL.md`
- `skills/typescript-best-practices/SKILL.md`
- `skills/unslop/SKILL.md`
- `skills/why/SKILL.md`
