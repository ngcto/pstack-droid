---
name: setup-pstack
description: Configure native Droid subagent routing for pstack tasks.
compatibility: droid
---

# Setup Pstack on Droid

Read `${DROID_PLUGIN_ROOT}/DROID-ADAPTER.md`. Use Droid's built-in subagent configuration, not a pstack model registry or provider-pinned droids. Full upstream setup remains preserved as provenance; its Cursor model slugs/rule files are not native execution instructions.

1. Inspect the current `/settings` → Subagents configuration: Light, Medium and Heavy task models, reasoning effort, and subagent autonomy. Do not read or print credentials.
2. Ask the user which native tier/model/budget preferences they want, only when they requested configuration. Preserve existing defaults otherwise. Available model/effort choices come from the native picker, not hardcoded source examples.
3. Explain the mapping: `worker` handles implementation/repro/command/MCP work; `explorer` handles read-only source exploration. Task `complexity` selects a native routing tier. Original `poteto-agent` and `comment-sicko` inherit the same user-owned routing without model pins.
4. The user configures models in native Subagents settings. Do not write custom model ledgers, modify global preferences behind their back, or generate provider-specific droids. Use a native settings tool only if its current schema supports the exact requested operation and approval flow.
5. Validate advertised configuration separately from actual account entitlement/model execution after login. Keep repeated panel seats and independent review roles. Different task labels or tiers do not prove different model families; report diversity unavailable when routing does not provide it.
6. Confirm actual settings and task resolution after an authorized disposable check. Never claim configuration based only on a recommendation.
7. Offer `/create-verification-skill` once if the project lacks real-app verification and the user accepts.
8. Offer `/create-formal-verification-skill` once if formal verification is absent and the user accepts. A skill file is not a proof.
