# Pstack for Factory Droid

Native Droid plugin port of [pstack](https://github.com/cursor/plugins/tree/main/pstack), preserving its complete engineering workflows, payloads, tests, guides and MIT licensing. Upstream snapshot: `4dd1d05818d19792e7cd6e818f1667f95f7e1dbe` (pstack 0.15.36).

## Install from GitHub

Install and authenticate the [Droid CLI](https://docs.factory.com/droid-cli/quickstart), then:

```sh
droid plugin marketplace add https://github.com/ngcto/pstack-droid
droid plugin marketplace list
droid plugin install pstack@pstack-droid --scope user
droid plugin marketplace add https://github.com/Factory-AI/factory-plugins
droid plugin install droid-control@factory-plugins --scope user
droid plugin install droid-evolved@factory-plugins --scope user
droid plugin list --scope user
```

The GitHub source registers as `pstack-droid`. If you pin a tag/SHA, read the registered marketplace name back and substitute it. No plugin-manager dependency resolver is assumed; install the two official dependencies explicitly.

In a new Droid session inspect `/plugins`, `/skills`, `/droids`, `/diagnostics`. Invoke `/poteto-mode`, `/poteto-help`, or an individual workflow. Configure model-role preferences with `/setup-pstack` after login.

## What is included

- All 58 original top-level pstack skills and their adjacent support files.
- Four additions: licensed `deslop`, native `control-cli`, `control-ui`, and skill-authoring bridge.
- Two original specialized role droids, both inheriting user-configured native subagent routing. No provider-specific droids are shipped.
- All 573 pinned upstream files unchanged in a separate pristine tree, including guides/images, fixtures and dormant Benny pack.
- An explicit Droid harness adaptation, preservation verifier, separate writable execution staging and offline tests.

Ordinary terminal/browser work prefers Droid's built-in `tuistory` and `agent-browser`. Formal QA, recordings, demos and native desktop work uses official `droid-control`. Atom files are read on demand; they are not invented skill identifiers.

## Preservation is not runtime equivalence

Droid children cannot spawn Task, so the parent owns flattened dispatch graphs. Cursor Task model/cloud fields and effort-bearing model slugs are translated to native role droids and explicit isolation decisions. No automatic cloud VM, Cursor Project store, event subscription or credential API is claimed. Benny is preserved but not activated. Source autonomy wording never expands user authorization.

See [Droid setup and usage](pstack/README-DROID.md), [harness contract](pstack/DROID-ADAPTER.md), [actual validation and skips](pstack/VALIDATION.md), and the original [upstream guide](pstack/docs/guide/README.md). Source attribution and licenses remain in the plugin and pristine tree.

## Offline checks

```sh
python pstack/scripts/pstack-droid.py verify
python pstack/tests/test_port.py
```

These prove packaging/adapter checks, not authenticated model behavior. Real coding and multi-model integration await user login and account entitlement. No secrets, login state, private session history, or runtime dependencies are distributed.
