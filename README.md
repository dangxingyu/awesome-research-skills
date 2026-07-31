# Awesome Research Skills

A plugin marketplace of reusable research and technical-writing workflows for
Codex and Claude Code.

## Plugins

| Plugin | Skills | Purpose |
|---|---|---|
| `experiment-reporting-suite` | `write-experiment-reports` | Audit experiment evidence, define algorithms and settings precisely, write a rigorous report, and render a QA-checked PDF. |
| `theory-research-suite` | `launch-theory-agent`, `write-deep-learning-papers` | Run audited multi-agent theory searches and write rigorous machine-learning papers. |

The `theory-research-suite` plugin is included from
[`dangxingyu/theory-research-suite`](https://github.com/dangxingyu/theory-research-suite)
at commit `a86e60d22c35a25c0447add9265b8ae51584e207`.

Both platforms share the same `plugins/` directories and `SKILL.md` files;
only the manifests differ (`.codex-plugin/` for Codex, `.claude-plugin/` for
Claude Code).

## Install in Codex

Requires a Codex version with plugin marketplace support.

```bash
codex plugin marketplace add dangxingyu/awesome-research-skills
codex plugin add experiment-reporting-suite@awesome-research-skills
codex plugin add theory-research-suite@awesome-research-skills
```

Start a new Codex task after installation so the skills are loaded, then
invoke a skill explicitly:

```text
$write-experiment-reports
$launch-theory-agent
$write-deep-learning-papers
```

Codex may also invoke a skill automatically when a request matches its
description.

## Install in Claude Code

Run inside a Claude Code session:

```text
/plugin marketplace add dangxingyu/awesome-research-skills
/plugin install experiment-reporting-suite@awesome-research-skills
/plugin install theory-research-suite@awesome-research-skills
```

Restart Claude Code (or start a new session) so the skills are loaded, then
invoke a skill by name:

```text
/write-experiment-reports
/launch-theory-agent
/write-deep-learning-papers
```

Claude Code may also invoke a skill automatically when a request matches its
description.

## Repository layout

```text
awesome-research-skills/
├── .agents/plugins/marketplace.json      # Codex marketplace
├── .claude-plugin/marketplace.json       # Claude Code marketplace
└── plugins/
    ├── experiment-reporting-suite/
    │   ├── .codex-plugin/plugin.json
    │   ├── .claude-plugin/plugin.json
    │   └── skills/write-experiment-reports/
    └── theory-research-suite/
        ├── .codex-plugin/plugin.json
        ├── .claude-plugin/plugin.json
        └── skills/
            ├── launch-theory-agent/
            └── write-deep-learning-papers/
```
