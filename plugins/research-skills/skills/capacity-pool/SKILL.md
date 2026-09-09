---
name: capacity-pool
description: Use and maintain the shared PLI/Della GPU pool through one CLI and ledger; covers A/B capacity, leases, keep-warm, CURRENT/NEXT continuity, and authorized migration or repair.
---

# Shared PLI capacity pool

## Deployment scope

This is a published snapshot of dangxingyu's existing PLI/Della deployment,
not a standalone scheduler installer. The absolute paths, account, partitions,
slot names and runtime policy below belong to that deployment. Before using
it elsewhere, obtain the site's authorized pool CLI and deployment configuration;
do not create these paths, submit jobs under another user's account, or infer
access from installing this skill. If the documented CLI or deployment is absent,
report the missing prerequisite and stop before any scheduler mutation.

On the existing Della installation, the project-local skill remains the
operational source; publishing this snapshot does not replace its discovery
links, ledger, controllers, immutable releases or queued jobs.

## Canonical deployment

One implementation: `/scratch/gpfs/ARORA/xd7812/wuji/projects/capacity-pool`.
One CLI: `/home/xd7812/.local/bin/pool`.
One canonical ledger: `/scratch/gpfs/ARORA/xd7812/capacity-pool`.
Codex and Claude use this same skill, not project-specific copies.
Its only source is that project's `skills/capacity-pool/`; `.agents`, `.codex`
and `.claude` skill discovery paths link to it. Edit the project source.
The project README is the navigation entrypoint for code, live state, frozen
releases and archives. They are different roles, not separate pool managers.
Do not create another capacity-pool project or copy this skill per experiment.
The old `pli-gpu-capacity` discovery name is a redirect whose tools also live
in this project. Retired legacy data is in `archive/legacy-reservations`;
`~/pli-gpu-pool` retains only data aliases, its original lock and a retirement
marker. Legacy writes (including `status --sync`) are closed; plain legacy
status is historical, not current capacity or another submission entrypoint.
For a request to leave only one physical directory, source/skill consolidation
and navigation links are not completion. Report the external state/release
paths still present and use the operator's coordinated cutover gates.

Start with `pool status --json`. It joins live Slurm state, native agents, and
registered legacy holders during migration. Empty native observations do not
mean free GPUs. `allocated_gpus` excludes pending jobs; scheduler start times
are estimates. Read the errors and migration state, not just job existence.

## Choose the role from the user's request

- **Status, explanation, diagnosis:** read-only inspection. Do not silently
  submit, cancel, reassign, or restart anything.
- **Run experiments:** consumer workflow below, only on the authorized slot.
- **Maintain, deploy, unify, or repair capacity:** read
  [references/operator.md](references/operator.md). The user's maintenance
  request authorizes necessary in-scope operator actions; do not confuse consumer
  restrictions with a prohibition on authorized maintenance. It does not authorize
  stopping another project's workload or increasing the requested capacity.

Use `pli-cluster` only for cluster access when necessary. On Della, run local
commands directly; no relay is required.

## Experiment consumer

```bash
pool request --id UNIQUE --owner OWNER --slot h100-32b \
  --project PROJECT --description 'PROJECT: one sentence describing the experiment.' \
  --manifest /absolute/manifest.json --run-root /absolute/run-root \
  --lane-role /absolute/lane-role.sh --lease-minutes 480
pool renew UNIQUE --minutes 480
pool release UNIQUE
pool stop h100-32b --request-id UNIQUE
pool cancel UNIQUE
```

`--slot` is mandatory. Repeat only if the user authorized either slot. A and B
are separate 4-node × 8-GPU allocations, not one 64-GPU DDP allocation.
A manifest and lane role describe work; the slot agent launches its one owned
outer Slurm step. Consumers never attach with personal `srun`, cancel holder
jobs/steps, start watchers, or hand-edit ledger files. Renew active leases;
expiry/release drains owned work and restores warm. A pool request does not
convert a legacy holder to native or take over its old ACTIVE reservation.
An operator-registered `legacy-pool` backend can serve the same request API
during migration; inspect its certificate and exact work-step binding. It is
not a native holder. Do not start its broker as an experiment consumer.

## Invariants for both roles

- New jobs, including tests: Della account `pli`, partition `pli-c`, QOS
  `pli-short` only. No `arora` / `gpu-test` fallback. Check actual resources,
  account, QoS, walltime and the current user limit before submission.
- Production A/B holders and their NEXT must request the PLI-short ceiling:
  **24 hours (`1-00:00:00`)**, not the duration of the experiment or a legacy
  4-hour predecessor. Short isolated tests require explicit test scope and no
  auto-successor. Verify the actual Slurm `TimeLimit` after submission/update;
  a script header or an old `SubmitLine` is not the effective job setting.
  When authorized to repair an already queued short holder, use the operator
  procedure to preserve its job ID/queue age; do not cancel and resubmit.
- Capacity renewal is independent of experiments and who owns their work.
  Both A and B need CURRENT plus an already-submitted NEXT while CURRENT runs.
  Native agents queue NEXT on their first healthy cycle (24-hour lead), using
  `afterany:CURRENT,singleton`. Missing NEXT is an alarm, not a healthy state.
  A queued dependency is not a guarantee of gap-free scheduler allocation.
  A short holder reaching TIMEOUT is a lost allocation, even if NEXT exists;
  report the gap. Pending capacity cannot be kept warm before allocation.
- Idle allocated GPUs stay warm. A live process or requested `warm` mode is
  not evidence of activity: check fresh job/step/node bindings and all physical
  GPU receipts/probes. Failed observations mean UNKNOWN, never empty/free.
  The read-only dashboard is `pool dashboard` (loopback port 8794). It shows
  shared queue, leases, CURRENT/NEXT and per-GPU observations. `idle` means a
  sampled utilization of at most 1%, not permission to take a leased GPU.
- One GPU controller per allocation. Never run a new controller beside an old
  one. Native control lives inside the batch allocation; the login migration
  bridge is temporary and does not launch work or GPU steps.
  For a certified legacy work transport, the existing watcher remains the sole
  fill/idle controller; the pool broker is only its journaled work launcher.
  Do not add a native controller or a personal launcher to that allocation.
- The designated login host's user systemd units serve the read-only dashboard
  and run a bounded recovery check each minute/after boot. Recovery is part of
  this same project/CLI, not a second GPU controller: it never runs `srun`,
  cancels jobs, changes leases or competes with a live holder's NEXT logic.
  It only replaces an entirely terminal registered chain, with exact identity,
  Slurm/accounting, lock and submission-intent checks. A failed observation
  fences submissions. See the operator reference before managing these units.
  Enabled is not the same as started: check conditions, active timer, fresh
  recovery receipt and dashboard HTTP after maintenance. The deployed login
  units use the designated machine's ID as the boot host fence, not its early
  hostname; a host reimage requires authorized re-rendering.
- Exact identities and locks govern changes. No broad `scancel`, `pkill`, or
  job-name guesses. A lost submission acknowledgement requires reconciliation
  of its durable intent/token, never a blind retry.
- Preserve running work and retained queued legacy jobs. Their spooled scripts
  do not change when repository files change. CLI installation, native GPU
  activity, and end-to-end rollover acceptance are separate milestones.

For status, report allocated/work/warm/pending separately, with each slot's
actual holder time limit, NEXT time limit and lease owner. Once native rollout
has begun, follow canonical successor journals beyond the initial migration
generation. A stale legacy watcher must not hide a later pending native job.
Neither may a terminal native heartbeat. Follow the confirmed successor chain;
do not reuse predecessor node/work receipts for a new job. A canonical lease
still denotes ownership even when its allocation is pending or unobserved.
Do not report full deployment acceptance from unit tests or a corrected CLI
alone: verify the actual running/queued releases and their effective policy.

Deployment details and test evidence: `projects/capacity-pool/README.md`.
`pli-gpu-capacity` is a compatibility redirect, not a second operating system.

## Scheduler-facing job names

User preference: use concise, truthful purpose names such as `training`,
`meta-grad-training`, or `optimizer-training`. Do not put A/B slot suffixes,
GPU counts, or hardware labels in public job names; this supersedes the earlier
`wuji-research-a/b` suggestion. Use `self-play` only for actual self-play work.
Keep resource requests/accounting and work/warm status accurate. Independent
slot chains need distinct purpose names: check same-user name collisions before
deployment because Slurm `singleton` dependencies are keyed by user and name.

Keep `h100-32a` / `h100-32b` as stable INTERNAL slot/ledger/CLI identifiers.
The target frozen runtime's `sbatch/job-names.json` governs public names.
Purpose-name runtimes specify `optimizer-training` / `meta-grad-training`;
earlier named runtimes specify `wuji-research-a/b`, and old runtimes without a
contract require `JobName == slot`. The CLI validates the target runtime's
contract, not arbitrary aliases. Submitters must export `SLOT_NAME` explicitly.
New native NEXT journals record runtime and public name with the token.

Do not rename a queued/running job with standalone `scontrol update JobName=...`.
Installing a new CLI does not upgrade a spooled job's runtime. For explicitly
authorized NEXT replacement (new job ID/queue age), use `pool admin replace-next`
and the operator reference. It preserves CURRENT and the cancelled NEXT's
original journal, then appends a new-runtime successor fenced behind CURRENT.
`MIGRATING` with verified continuity means replacement is queued, not that GPU
runtime rollover has completed. Never erase the cancellation tombstone or
restart CURRENT to clear its expected old-NEXT warning. Preserve leases and
verify the actual replacement and its subsequent successor names.

## Experiment descriptions

Every new CLI request requires `--project` and `--description`: one line of
1–240 characters naming the project and what the experiment tests. Write a
useful scientific description in English, not just a run ID. The dashboard
interface may use Chinese; experiment descriptions default to English.
Do not include secrets.
Examples: `Kron-ISO: compare two inner learning rates on the full-F/C objective.`
or `Infinite-MG: rerun frozen centre recipes on H100 for matched-hardware comparisons.`

Descriptions are display metadata, not scheduling instructions. Immutable
`metadata/<request-id>.json` records preserve them across old frozen controllers
which do not know the new field. Legacy records remain readable; an authorized
`pool describe ID --project PROJECT --description '...'` adds a missing summary
without rewriting a queue entry, lease, manifest or result. Do not backfill
scientific claims from a run name alone. The dashboard's DONE/FAILED counts are
execution markers, not scientific acceptance or optimizer rankings.
