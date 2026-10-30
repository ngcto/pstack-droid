# Pstack for Droid

Factory Droid harness generated from [pstack](https://github.com/cursor/plugins/tree/main/pstack), pinned at `4dd1d05818d19792e7cd6e818f1667f95f7e1dbe`. Original MIT licensing and workflows are retained.

## Install

```sh
droid plugin marketplace add https://github.com/ngcto/pstack-droid
droid plugin install pstack@pstack-droid --scope user
```

For formal QA/demo and skill-authoring routes, install the official dependencies:

```sh
droid plugin marketplace add https://github.com/Factory-AI/factory-plugins
droid plugin install droid-control@factory-plugins --scope user
droid plugin install droid-evolved@factory-plugins --scope user
```

Invoke `/poteto-mode` or an individual skill. Models remain configured through Droid's native Subagents settings. No provider-specific droids or model registry are shipped.

## Generate

Like upstream's Claude Code export, the installable harness is generated rather than hand-maintained:

```sh
python scripts/generate-pstack-harness-trees.py
python scripts/generate-pstack-harness-trees.py --check
```

Edit `upstream/pstack/` sources and `upstream/pstack/docs/harness/droid.md`, regenerate, and commit `harness/pstack/droid/`. The marketplace installs only that generated directory. Unlike the Claude export, original assets and dormant automations are retained as requested.

The generator checks selective adapter coverage, skill identity, links, bytes, file modes and generated-tree drift. No custom runtime verifier, wrapper skills, duplicate adapter tree or added cleanup helper is bundled. The adapter translates native tools/fields and names unsupported gates explicitly. Model-backed execution remains untested until login.
