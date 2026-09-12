# Authorized capacity maintenance

Use this procedure when the user asks to preserve/repair/deploy the pool, not
merely when they ask about its status. Maintenance scope includes renewal of
protected A capacity; it does not include interrupting A's experiment.

## Native operation

### Dashboard and boot recovery

The designated login host is `della-pli.princeton.edu`. The user's existing
`Linger=yes` allows its user manager to start at boot; do not assume this on
other hosts. Unit templates live in the same project's `scripts/systemd/`.
Installed units and the `pool` wrapper pin a verified immutable release.
The host fence is the designated machine's `/etc/machine-id` rendered into
`ConditionHost`, not its boot-time hostname. Do not remove host fencing on a
shared home directory or render on a different login host. On September 8 the
hostname-fenced units were enabled but skipped at boot; checking only `enabled`
missed the outage. The exact early-boot hostname was not observable.

- `capacity-pool-dashboard.service`: read-only localhost port 8794, restart on
  failure. Use SSH forwarding; do not open it publicly or start a competing
  server on that port. No GPU jobs or per-poll files are created.
- `capacity-pool-recovery.timer`: starts after boot and checks every minute.
  Its oneshot service calls `pool admin recover --runtime EXACT_RELEASE
  --expected-host della-pli.princeton.edu --apply --summary`. It is a finite
  control-plane repair check, not another work/keep-warm/NEXT controller.

Read `systemctl --user status capacity-pool-dashboard.service
capacity-pool-recovery.timer` and `state/recovery/status.json`. A successful
oneshot recovery service normally becomes inactive; check `Result`,
`ExecMainStatus`, timer next activation and the receipt, not just `is-active`.
The dashboard displays this receipt's heartbeat and blocked actions. Unknown
Slurm or missing storage causes a retry/alert, never an empty-capacity inference.
Also inspect `ConditionResult`, `UnitFileState` and timer next activation.
An enabled timer with `ConditionResult=no` needs authorized service repair;
it is not an invitation to resubmit existing GPU jobs. Dashboard health route:
`http://127.0.0.1:8794/api/snapshot` (`/api/state` is not an endpoint).

Healthy CURRENT or pending NEXT is preserved, including its immutable runtime,
queue age and all foreign leases. Recovery only submits when every registered
legacy/native ancestor is authoritatively terminal and no unknown same-slot
job exists. Under recovery/admin/slot locks it repeats the checks, journals
SUBMITTING before `sbatch`, and requests 4 × 8 GPUs, PLI only, 24h. Independent
standby runtimes omit Slurm dependencies; legacy runtimes retain singleton.
It follows the ordinary successor chain; it never resets its history. A lost
acknowledgement may bind only the exact live recovery token/runtime, never
blindly retry. Other unresolved intents require operator reconciliation.
Terminal NEXT generations which never published an observation are supported
by verifying the complete terminal ancestry gap in the new native agent.

`pool admin recover --runtime EXACT_RELEASE` is a dry run (no submit/lease
change). To stop automatic *replacement*, disable only the recovery timer and
wait for any current oneshot to finish; for a durable maintenance fence use
`state/recovery/PAUSED` under explicit operator authorization. Neither option
stops the native agents' normal NEXT renewal. Releasing all capacity requires
a separate, coordinated native-controller procedure; do not merely cancel
holders and let the recovery timer replace them. Do not remove an ambiguous
submission journal to force a retry.

Verify unit syntax, dry-run recovery, service restart, timer activation and
unchanged CURRENT/NEXT/leases after deploying. Do not restart GPU holders or
reboot a shared login host to test these units. A successful user-service
restart plus CPU reboot simulations is not real maintenance-reboot acceptance,
nor a guarantee of queue start time or scientific checkpoint recovery.

Stage the three units with `pool admin render-services --runtime EXACT_RELEASE
--output NEW_PROJECT_RUN_DIRECTORY`. This verifies the immutable release and
renders the local machine-ID fence; it does not install or restart anything.
Review and verify the staged units with `systemd-analyze --user verify`.
Before authorized installation, retain the old wrapper/units and record pending
job IDs, effective TimeLimit, SubmitTime/EligibleTime/AccrueTime, spooled script
identity and canonical lease bytes. Install only the three login units, pin the
CLI to the tested release, daemon-reload, enable/start the dashboard and timer,
then recheck actual timer execution and fresh HTTP/receipt evidence. Recovery's
live/pending preservation guards remain in force throughout. Never restart a
GPU controller to deploy these login-only fixes.

Public names are runtime-bound by `sbatch/job-names.json`. Purpose-name runtimes
use `optimizer-training` / `meta-grad-training`; earlier contracts retain
`wuji-research-a/b`, and unnamed old runtimes retain `h100-32a/b`. All keep the same
internal slot, lease namespace and successor token. The target runtime's
`sbatch/renewal-policy.json` is authoritative: `independent-standby` submits
without dependencies; absence of the file means legacy `afterany:CURRENT,singleton`.
Validate the matching policy, not a universal dependency rule. Never clear an
old-runtime job's dependency: its controller cannot safely wait for admission.
Recovery inventories both name generations and tokens and refuses unknown
same-slot jobs; it never creates a second chain just to adopt the new name.

`pool status --json` is the common view. The per-allocation agent owns fill,
work, recovery, and NEXT. Independent runtimes hold `locks/allocation-<job>.lock`
for their lifetime and take `locks/<slot>.lock` only after predecessor ancestry
is terminal. Legacy controllers hold the slot lock for their lifetime. They
record launches/successor submissions before external calls. Do not submit a
competing successor for a native agent: reconcile its exact durable intent and
live Slurm job first. A missing or stale heartbeat is not proof of termination.

Check CURRENT and NEXT separately for each slot: live states, exact owner,
4 nodes / 32 GPUs, PLI placement, time remaining, successor dependency and
immutable runtime, current workload, GPU activity, and controller errors.
Missing NEXT remains an alarm even if all CURRENT GPUs are busy.

### Explicitly authorized queued NEXT replacement

Replacing NEXT loses that job's ID and queue age; do this only when the user
authorizes replacement/requeue, not merely a status check or a naming preference.
Use `pool admin replace-next --slot SLOT --current CURRENT --next OLD_NEXT
--runtime EXACT_RELEASE` to preview, then the same command with `--apply`.
Deploy the tested replacement-aware CLI/dashboard/recovery first. Temporarily
stop only the login recovery timer and let its current oneshot finish to avoid
operator-lock contention; restore the timer after the operation, including on
failure. Never stop the GPU controllers, their work steps or their leases.

The command is restricted to audited immutable CURRENT runtimes, a fresh
running controller, its exact confirmed pending NEXT, and purpose-name targets.
It retains `CURRENT -> OLD_NEXT` unchanged, journals cancellation intent, cancels
only that exact PENDING job, verifies CANCELLED, and journals/submits
`OLD_NEXT -> NEW_NEXT`. Its bootstrap predecessor is the cancelled OLD_NEXT.
Independent runtimes can start immediately, but warm only their own allocation
until both earlier ancestors are terminal and the slot lock is acquired.
Legacy targets retain `afterany:CURRENT,singleton`. Do not rewire original edges,
rewrite spooled scripts, clear old-runtime dependencies or edit frozen releases.

Old CURRENT controllers continue work/fill independently while refusing to
resubmit their cancelled NEXT. The replacement-aware status/dashboard verifies
the tombstone, new journal, runtime, owner, resources and live-CURRENT dependency;
it reports `MIGRATING`, exposes expected old-controller warnings separately and
retains real work/observation errors. A confirmed pending replacement is not
real rollover acceptance. After CURRENT ends, verify the new controller's fresh
GPU receipts and its own immediately queued NEXT.

If cancellation or submission acknowledgement is lost, rerun the same exact
command to reconcile durable identity; it never blindly repeats either action.
Unresolved cancellation still pending, missing acknowledgement, foreign name
collision, identity change or unexpected descendant blocks mutation. Preserve
the intent and inspect it; do not erase it to force a retry. Keep operation
receipts in `state/replacements/` and deployment evidence in project/runs.

### Independent NEXT and deferred runtime upgrades

This mode removes both `afterany` and `singleton`, not merely the first one.
Submission checks `pli-short MaxTRESPU=gres/gpu=64` and Slurm's QoS/limits
enforcement. A RUNNING NEXT is a separate allocation, never permission to
duplicate CURRENT's work. It writes its own `allocations/<slot>-<job>.json`
heartbeat and warm receipts without overwriting `slots/<slot>.json` or leases.
Only the admitted generation submits NEXT, preventing a standby submission cascade.
An early allocation's 24-hour lifetime starts when Slurm starts it, not when
the slot admits it. A/B lease reassignment and forced CURRENT cancellation are
not implemented. If B is missing while A NEXT starts early, capacity can be
64 allocated but only 32 admitted; report the other 32 as standby, not B work.

To preserve a currently pending old-runtime job's queue age, authorize only its
future NEXT upgrade with:

```bash
pool admin stage-upgrade --slot SLOT --current EXACT_QUEUED_JOB --runtime EXACT_RELEASE
pool admin stage-upgrade --slot SLOT --current EXACT_QUEUED_JOB --runtime EXACT_RELEASE --apply
```

The first command previews; the second persists one exact plan in `upgrades/`.
The existing host-fenced recovery timer waits for this CURRENT to run and its
native agent to confirm NEXT, then invokes the journaled replacement API on
that NEXT only. It never cancels the protected CURRENT, changes leases, targets
another generation, or starts a new watcher. Ordinary recovery alone does not
authorize replacement. A completed plan is not repeated. Query failure, changed
identity or unexpected terminal CURRENT blocks the plan and is reported in
`recovery/status.json` under `upgrades`/`errors`; do not erase an ambiguous intent.
Deploy the tested CLI/dashboard/recovery units before staging a plan.

Acceptance: check new NEXT's effective empty Dependency, 24h policy, exact
runtime/token and retained predecessor tombstones; compare protected CURRENT,
lease bytes and pending B's SubmitTime/EligibleTime/AccrueTime. Then observe
AccrueTime and `sprio` AGE at separated times. Removing dependencies eliminates
that particular age blocker, but does not prove age accrual under a saturated
QoS or guarantee a start time. Della currently lacks `ACCRUE_ALWAYS` (see
[Slurm age rules](https://slurm.schedmd.com/priority_multifactor.html)).
Do not cancel/requeue an already eligible B simply to clear an absent dependency.
Actual early-start warm receipts, admission, work and subsequent renewal are
separate live acceptance gates; pending submissions and mock tests do not prove them.

## Repair an inherited short production holder

Production A/B policy is 24h on pli-short, verified on Della's local
`/etc/slurm/job_submit.lua` (getQOS/set_plic_qos) and actual Slurm job records.
Do not infer the ceiling from an empty sacctmgr MaxWall field: the site's job
submission plugin assigns QOS by requested duration. Recheck site policy if it
changes; the pool intentionally does not request beyond 24h.

`pool admin maximize-pending --slot SLOT --job-id JOB --predecessor OLD
--runtime /exact/queued/release` is a dry run. Add `--apply` only under the
user's capacity-maintenance authorization. It locks admin and that slot,
requires no active lease, a terminal predecessor, the exact confirmed native
successor journal, cleared dependencies, unique live discovery, verified
immutable runtime and owned pending 4-node/32-GPU PLI identity. It journals
before `scontrol update`, then verifies TimeLimit=24h and unchanged job ID,
submission/eligibility/accrual times, resources, dependency and script identity.
An uncertain acknowledgement is reconciled by the same job, never new sbatch.
It refuses a live predecessor/slot or unresolved failed update; do not bypass
those guards to alter another project's running work.

Effective `TimeLimit` takes precedence over historical `SubmitLine --time=4h`.
Old pinned native agents inherit the effective current TimeLimit; verify this
in their frozen source before claiming future 24h continuity. New production
source explicitly requests/validates 24h instead of inheriting short history.
Do not rewrite frozen runtime files or restart a running controller to deploy
a read-only CLI or policy correction. Verify CURRENT/NEXT again after repair.

## Directory consolidation

The only editable project is `wuji/projects/capacity-pool`. Its `state` and
`releases` links expose the existing live ledger and immutable runtime store.
The shared skill is physically in the project's `skills/capacity-pool`;
all agent discovery paths are aliases. Preserve those discovery links, not
separate skill copies. The compatibility skill/tools are likewise physically
in `skills/pli-gpu-capacity`, with their old discovery paths preserved as links.
The old `/home/xd7812/pli-gpu-pool` path is a retired compatibility/lock stub;
its four data files alias `archive/legacy-reservations`. Do not move its original
lock or reopen it for writes. Plain legacy status/doctor read historical data;
`status --sync` and all reservation mutations reject the retirement marker.
See the project's `docs/directory-consolidation-20260905.md`
for the remaining physical migration gates.
These links are navigation, not completed physical relocation. Do not move
live ledger/lock paths or release paths referenced by queued/running scripts:
even a replacement symlink can alter resolved-path identity validation.

`pool admin organize --project /scratch/gpfs/ARORA/xd7812/wuji/projects/capacity-pool`
previews archival of only the two enumerated inactive legacy test roots; add
`--apply` under cleanup authorization. It checks live/queued scheduler paths
and test locks, preserves file hashes/inodes, records a receipt, and does not
delete evidence or leave another editable implementation. New tests belong
under this project's runs, never another home-level capacity-pool-test copy.
Full physical relocation remains a separately gated quiescent transition;
do not interrupt another project's lease merely to finish a directory cleanup.

`pool admin migration-audit --project /scratch/gpfs/ARORA/xd7812/wuji/projects/capacity-pool`
rechecks actual spooled script paths, immutable runtime identities, native
observations and local lock probes. Optional `--output` saves a new audit under
project/runs. This command does not move anything or establish a writer fence.
In particular, a free **local** flock probe is not proof that a remote native
agent has stopped. Preserve live controllers even when all leases are empty.

`pool admin retire-legacy --project /scratch/gpfs/ARORA/xd7812/wuji/projects/capacity-pool`
previews the separate legacy-data retirement; `--apply` requires maintenance
authorization. It requires the tested retirement-aware legacy writer guard,
exact terminal jobs for every bound request, retired watcher observations,
free legacy/admin/watcher locks and no live/queued script reference to the old
ledger. It preserves original state/TSV bytes and historical request labels,
archives data behind atomic aliases and retains the original lock inode.
An interrupted operation keeps its retirement marker; mismatched partial
evidence fails closed and must be reconciled, never overwritten blindly.
`RETIRED_DATA_ARCHIVED_LOCK_RETAINED` is partial consolidation, not native
cutover or a claim that only one physical directory remains.

## Legacy transition

Legacy registry files are read-only compatibility inputs to unified status,
not another canonical work ledger. Old watcher scripts remain available only
while their existing allocations run. Never launch a new legacy research
holder or treat an old ACTIVE request as a native lease.

1. Inventory `pool status --json`, live `squeue/scontrol/sacct`, exact watcher
   PIDs/locks, and legacy CURRENT/NEXT. Read the actual queued scripts with
   `scontrol write batch_script JOB /dev/stdout`; preserve their jobs and age.
   Read-only legacy probes remain in
   `~/.agents/skills/pli-gpu-capacity/scripts/` for allocation activity audits.
2. Test the implementation, then freeze it with
   `projects/capacity-pool/scripts/freeze_release.py --release-root
   /scratch/gpfs/ARORA/xd7812/capacity-pool-releases`. Pin CLI/runtime to the
   resulting content hash; do not modify an immutable release.
3. Queue one first native successor using the operator API:

   ```bash
   pool admin bootstrap --slot SLOT --after LAST_LEGACY_JOB \
     --runtime /absolute/content-hash-release \
     --legacy-status /absolute/holder/status.env \
     --legacy-job FIRST_RETAINED_JOB --legacy-job LAST_LEGACY_JOB
   ```

   For a one-job chain supply that job once, or omit `--legacy-job`. The API
   locks, validates owned 32-GPU PLI jobs/runtime, records intent before sbatch,
   requests the production 24h policy, and refuses unresolved duplicate
   submissions. Record its exact returned job and fresh Slurm validation.
4. Replace only the old login renewal process, not its GPU watcher, as a
   coordinated handover. Verify its published PID and exact command first;
   `pool admin retire-renewer --pid PID` stops only the recognized legacy B
   renewal executable after checking UID, argv and process start identity
   (PID-bound signaling where the Python build supports it). Start `pool admin supervise`
   in durable tmux with a log. The temporary bridge must acquire both the new
   migration lock and the old B-renewal lock; never bypass a held lock.
5. The bridge follows the retained legacy chain through the existing watcher's
   generation-checked request API. A same-CURRENT NEXT update preserves
   RUN/AUTO. Changing CURRENT requires terminal previous job, verified bootstrap
   fill topology, and no unexpected writer. It never changes CURRENT to a
   native job and never issues sbatch/srun/scancel.
6. Native jobs take over at allocation boundaries. Before retirement of a
   legacy watcher, verify all retained legacy jobs ended and the exact native
   agent has fresh healthy 32-GPU receipts. The bridge then exits after both
   slots migrate. Do not call this production acceptance until real PLI
   warm/work/warm, recovery, and rollover have also been verified.

If observation, identity, or ownership checks fail, preserve the allocation,
report the exact failed invariant, and reconcile. Do not change a held foreign
test job or retry a submission just to make status green. New authority is
needed only if the required remedy exceeds the user's maintenance scope.

## Work during a retained legacy B generation

When the user authorizes experiments now, migration need not postpone them until
the first native generation. The frozen `pool admin serve-legacy --slot h100-32b
--job-id CURRENT --legacy-reservation EXACT_ACTIVE_ID` transport is restricted to
the registered retained B chain and its existing B-only reservation. Never use
it on protected A. Start one durable broker holding the canonical B agent lock;
first verify its healthy idle observation and immutable transport certificate,
then submit science through the normal `pool request` API.

This is not a second fill controller: the existing watcher alone drains and
restores fill through its generation-checked HANDOFF/RUN/PARK API. The broker
launches only one journaled `generals-driver` step after verified empty topology,
and requires all four lane nonce receipts before binding ownership. It may
cancel only that exact owned step on lease revocation. It never submits or
cancels holders, changes NEXT, or launches fill. The separate migration bridge
keeps its non-GPU continuity role. A lost launch acknowledgement must be
reconciled; never erase its journal and relaunch blindly.

The broker follows retained B1/B2, publishing the current generation, then exits
and releases its lock before native operation. Its certificate explicitly says
`native_holder=false`; scientific execution must bind that certificate, release,
lease, exact job/step, and physical GPU receipts. Existing native validators must
not be weakened to accept a legacy job by name alone.
