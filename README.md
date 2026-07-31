# Awesome Research Skills

A plugin marketplace of reusable research and technical-writing workflows for
Codex and Claude Code. One plugin, five skills.

## Skills

| Skill | Purpose |
|---|---|
| `sharpen-research-ideas` | Sharpen a vague idea into a falsifiable project contract and a prediction-annotated experiment roadmap. |
| `launch-theory-agent` | Run audited, cyclic multi-agent theorem searches. |
| `read-arxiv-paper` | Fetch an arxiv paper's TeX source, read it end to end, and summarize it in the context of the current project. |
| `write-experiment-reports` | Audit experiment evidence, define algorithms and settings precisely, write a rigorous report, and render a QA-checked PDF. |
| `write-deep-learning-papers` | Plan, draft, revise, and review rigorous machine-learning research papers. |

The skills compose into a pipeline: sharpen an idea into a plan, run the plan
(theory branches via `launch-theory-agent`, literature checks via
`read-arxiv-paper`), report results against the pre-registered predictions
via `write-experiment-reports`, and write the paper via
`write-deep-learning-papers`.

Provenance:

- `launch-theory-agent` and `write-deep-learning-papers` originate from
  [`dangxingyu/theory-research-suite`](https://github.com/dangxingyu/theory-research-suite)
  (commit `a86e60d`), with platform-neutral wording adjustments.
- `read-arxiv-paper` is adapted from
  [`karpathy/nanochat`](https://github.com/karpathy/nanochat) (MIT, commit
  `92d63d4`), with the nanochat-specific cache path and summary framing
  generalized to the current project.

Both platforms share the same skill files; only the manifests differ
(`.codex-plugin/` for Codex, `.claude-plugin/` for Claude Code).

## Install in Codex

Requires a Codex version with plugin marketplace support.

```bash
codex plugin marketplace add dangxingyu/awesome-research-skills
codex plugin add research-skills@awesome-research-skills
```

Start a new Codex task after installation so the skills are loaded, then
invoke a skill explicitly:

```text
$sharpen-research-ideas
$launch-theory-agent
$read-arxiv-paper
$write-experiment-reports
$write-deep-learning-papers
```

Codex may also invoke a skill automatically when a request matches its
description.

## Install in Claude Code

Run inside a Claude Code session:

```text
/plugin marketplace add dangxingyu/awesome-research-skills
/plugin install research-skills@awesome-research-skills
```

Restart Claude Code (or start a new session) so the skills are loaded, then
invoke a skill by name:

```text
/sharpen-research-ideas
/launch-theory-agent
/read-arxiv-paper
/write-experiment-reports
/write-deep-learning-papers
```

Claude Code may also invoke a skill automatically when a request matches its
description.

## Repository layout

```text
awesome-research-skills/
├── .agents/plugins/marketplace.json      # Codex marketplace
├── .claude-plugin/marketplace.json       # Claude Code marketplace
└── plugins/research-skills/
    ├── .codex-plugin/plugin.json
    ├── .claude-plugin/plugin.json
    └── skills/
        ├── sharpen-research-ideas/
        ├── launch-theory-agent/
        ├── read-arxiv-paper/
        ├── write-experiment-reports/
        └── write-deep-learning-papers/
```
