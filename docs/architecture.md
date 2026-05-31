# Architecture

M4 Mac Mini SLM EvalOps keeps local model behavior measurable by keeping
workflow ownership outside the model.

The project is not a generic leaderboard. It answers a narrower question:

> Which small models are actually useful on this M4 Mac mini, under bounded
> tasks, strict output protocols, and repeatable scoring?

## Ownership Boundaries

The harness owns:

- task selection
- clean workspace creation
- backend invocation
- test execution
- diff capture
- report generation
- rollback and isolation

The backend owns only one thing:

- proposing or applying a candidate change inside the isolated attempt repo

This split is intentional. Small local models often fail when they own reading,
patching, summarizing, format control, testing, retries, and final judgment all
at once. A harness-owned loop keeps those responsibilities explicit.

## Attempt Lifecycle

1. Load `task.json`.
2. Copy `task/repo` into `runs/<run>/attempt-XXXX/repo`.
3. Snapshot files before backend execution.
4. Invoke backend adapter.
5. Run the task's test command.
6. Snapshot files after execution.
7. Write `diff.patch`, `stdout.txt`, `stderr.txt`, and `report.json`.
8. Append the result to `index.json`.

## Adapter Roadmap

- `noop`: baseline failure and no-op detection
- `scripted`: public-safe successful patch demonstration
- `mlx_generate`: future direct generation adapter for local MLX models
- `ollama_generate`: future adapter for local Ollama models
- `lmstudio_api`: future adapter for LM Studio local server runs

## Benchmark Lanes

The harness separates three concerns that are often blurred in local-model
testing:

1. Quality lane: task correctness under deterministic checks.
2. Protocol lane: strict format adherence, including JSON/tool-call validity and
   leakage of reasoning markers such as `<think>`.
3. Hardware lane: whether the model is usable on the M4 Mac mini, including
   timeout behavior, wall time, and later TTFT/tok/s or memory metrics.

This keeps model selection honest. A model can be fast but unusable, accurate
but too slow, or semantically useful only when the harness applies bounded
post-processing.
