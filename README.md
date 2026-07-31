# Awesome Research Skills

A plugin marketplace of reusable research and technical-writing workflows for
Codex and Claude Code.

## Plugins

| Plugin | Skills | Purpose |
|---|---|---|
| `research-planning-suite` | `sharpen-research-ideas` | Sharpen a vague idea into a falsifiable project contract and a prediction-annotated experiment roadmap. |
| `experiment-reporting-suite` | `write-experiment-reports` | Audit experiment evidence, define algorithms and settings precisely, write a rigorous report, and render a QA-checked PDF. |
| `theory-research-suite` | `launch-theory-agent`, `write-deep-learning-papers` | Run audited multi-agent theory searches and write rigorous machine-learning papers. |
| `paper-reading-suite` | `read-arxiv-paper` | Fetch an arxiv paper's TeX source, read it end to end, and summarize it in the context of the current project. |

The suites compose into a pipeline: sharpen an idea into a plan, run the
plan (theory branches via `launch-theory-agent`), report results against the
pre-registered predictions via `write-experiment-reports`, and write the
paper via `write-deep-learning-papers`. `read-arxiv-paper` feeds the
literature checks along the way.

The `theory-research-suite` plugin is included from
[`dangxingyu/theory-research-suite`](https://github.com/dangxingyu/theory-research-suite)
at commit `a86e60d22c35a25c0447add9265b8ae51584e207`.

The `read-arxiv-paper` skill is adapted from
[`karpathy/nanochat`](https://github.com/karpathy/nanochat) (MIT) at commit
`92d63d4e8bb4df75c3b71618f31ddde2378b2bcd`, with the nanochat-specific cache
path and summary framing generalized to the current project.

Both platforms share the same `plugins/` directories and `SKILL.md` files;
only the manifests differ (`.codex-plugin/` for Codex, `.claude-plugin/` for
Claude Code).

## Install in Codex

Requires a Codex version with plugin marketplace support.

```bash
codex plugin marketplace add dangxingyu/awesome-research-skills
codex plugin add research-planning-suite@awesome-research-skills
codex plugin add experiment-reporting-suite@awesome-research-skills
codex plugin add theory-research-suite@awesome-research-skills
codex plugin add paper-reading-suite@awesome-research-skills
```

Start a new Codex task after installation so the skills are loaded, then
invoke a skill explicitly:

```text
$sharpen-research-ideas
$write-experiment-reports
$launch-theory-agent
$write-deep-learning-papers
$read-arxiv-paper
```

Codex may also invoke a skill automatically when a request matches its
description.

## Install in Claude Code

Run inside a Claude Code session:

```text
/plugin marketplace add dangxingyu/awesome-research-skills
/plugin install research-planning-suite@awesome-research-skills
/plugin install experiment-reporting-suite@awesome-research-skills
/plugin install theory-research-suite@awesome-research-skills
/plugin install paper-reading-suite@awesome-research-skills
```

Restart Claude Code (or start a new session) so the skills are loaded, then
invoke a skill by name:

```text
/sharpen-research-ideas
/write-experiment-reports
/launch-theory-agent
/write-deep-learning-papers
/read-arxiv-paper
```

Claude Code may also invoke a skill automatically when a request matches its
description.

## Repository layout

```text
awesome-research-skills/
├── .agents/plugins/marketplace.json      # Codex marketplace
├── .claude-plugin/marketplace.json       # Claude Code marketplace
└── plugins/
    ├── research-planning-suite/
    │   ├── .codex-plugin/plugin.json
    │   ├── .claude-plugin/plugin.json
    │   └── skills/sharpen-research-ideas/
    ├── experiment-reporting-suite/
    │   ├── .codex-plugin/plugin.json
    │   ├── .claude-plugin/plugin.json
    │   └── skills/write-experiment-reports/
    ├── theory-research-suite/
    │   ├── .codex-plugin/plugin.json
    │   ├── .claude-plugin/plugin.json
    │   └── skills/
    │       ├── launch-theory-agent/
    │       └── write-deep-learning-papers/
    └── paper-reading-suite/
        ├── .codex-plugin/plugin.json
        ├── .claude-plugin/plugin.json
        └── skills/read-arxiv-paper/
```
