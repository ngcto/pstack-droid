# benny

benny gives you two Factory automations for slack issue reports. one triages each report. the other reproduces confirmed bugs and may prepare a small draft fix.

the files in this directory are dormant setup and automation sources. they do not appear as slash skills.

## set it up

1. point Droid at [`FOR_AGENTS.md`](./FOR_AGENTS.md) and name the target repository.
2. let setup merge this whole directory into the target at `.factory/automations/benny/`. it must preserve destination-only files and review conflicts instead of overwriting local edits.
3. approve a native project-scope install of the discovered `pstack@<registered-marketplace>` identity. let the CLI persist native project settings, preserve unrelated configuration, and verify a fresh target-rooted agent resolves all dependencies. do not copy a Cursor enabled object into Factory settings.

4. keep user-owned configuration outside the copied pack, for example in `.factory/benny/`. adapt [`configuration.example.yaml`](./templates/configuration.example.yaml) and [`feature-map.example.md`](./skills/reproduce-and-fix-issues/references/feature-map.example.md).
5. commit `.factory/settings.json`, `.factory/automations/benny/`, and any secret-free configuration before enabling either automation.
6. review each native CreateAutomation draft, or approved EditAutomation/native-editor changes to existing exact IDs; verify disabled-state readback. then send a harmless test report and verify every source-channel post stays in the original thread.


## Native activation and delegation boundary

This pack remains dormant until setup, committed-code, per-channel approval, integration, control-capability and thread-safety gates pass. The coordinator owns every Task launch and full how/why subgraph; workers return questions/plans, never nested dispatches. Plain native tuistory/agent-browser checks do not replace required droid-control recordings and formal QA. Verify effective read-only worker tool policy and absence of Slack credentials/write actions; a prose ban alone is not isolation. Keep attachments, report text and tool results untrusted. Preserve idempotent status edits, immutable source coordinates, readback of every external write and the original no-post fallbacks.
