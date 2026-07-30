# Awesome Agent Skills

A Codex marketplace for reusable research and technical-writing workflows.

## Plugins

| Plugin | Skills | Purpose |
|---|---|---|
| `experiment-reporting-suite` | `write-experiment-reports` | Audit experiment evidence, define algorithms and settings precisely, write a rigorous report, and render a QA-checked PDF. |
| `theory-research-suite` | `launch-theory-agent`, `write-deep-learning-papers` | Run audited multi-agent theory searches and write rigorous machine-learning papers. |

The `theory-research-suite` plugin is included from
[`dangxingyu/theory-research-suite`](https://github.com/dangxingyu/theory-research-suite)
at commit `a86e60d22c35a25c0447add9265b8ae51584e207`.

## Install

Requires a Codex version with plugin marketplace support.

```bash
codex plugin marketplace add dangxingyu/awesome-agent-skills
codex plugin add experiment-reporting-suite@awesome-agent-skills
codex plugin add theory-research-suite@awesome-agent-skills
```

Start a new Codex task after installation so the skills are loaded.

Invoke a skill explicitly:

```text
$write-experiment-reports
$launch-theory-agent
$write-deep-learning-papers
```

Codex may also invoke a skill automatically when a request matches its
description.

## Repository layout

```text
awesome-agent-skills/
├── .agents/plugins/marketplace.json
└── plugins/
    ├── experiment-reporting-suite/
    │   └── skills/write-experiment-reports/
    └── theory-research-suite/
        └── skills/
            ├── launch-theory-agent/
            └── write-deep-learning-papers/
```
