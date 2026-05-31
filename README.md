# M4 Mac Mini SLM EvalOps

Evaluation-driven benchmark harness for small local models running on an M4
Mac mini.

This project turns local SLM experiments into repeatable engineering evidence:
clean task isolation, backend adapters, deterministic scoring, live MLX smoke
tests, metric capture, failure taxonomy, and report artifacts.

## Why This Exists

Small local models are easy to download and hard to trust. A useful local
benchmark should answer operational questions for this exact machine:

- Does the model run at all on the M4 Mac mini?
- Does it produce parseable output under a strict protocol?
- Does the answer pass deterministic checks without an LLM judge?
- How long does the attempt take before success, failure, or timeout?
- Does the model no-op, repeat, drift into `<think>`, or ignore format rules?
- Is this model useful enough to keep, or should it be rejected early?
- Can the result be preserved without keeping model weights on disk?

This harness is designed around those questions.

## Architecture

```text
task fixture
  |
  v
clean isolated attempt repo
  |
  v
backend adapter
  |         \
  |          -> patch / file changes / no-op
  v
test runner
  |
  v
report.json + diff + stdout/stderr + dashboard data
```

## Current Scope

The checked-in version is a public-safe M4 Mac mini benchmark scaffold. It
includes:

- a runnable demo task
- a scripted backend that simulates a successful model patch
- a no-op backend for baseline comparison
- per-attempt isolated workspaces
- JSON reports
- a small static dashboard template
- docs for failure taxonomy and design decisions
- trace and live MLX adapters for selected small models

Future adapters can wrap MLX server mode, Ollama, LM Studio, `codex exec`, or a
mini-SWE-agent style shell loop. The primary target remains models that are
plausible on the current M4 Mac mini; cloud/frontier backends are comparison
baselines, not the center of the project.

## Storage Policy

Model weights are disposable test inputs. The default benchmark lifecycle is:

```text
download into attempt-scoped cache
  -> run smoke/eval
  -> save lightweight evidence artifacts
  -> delete the model cache completely
```

Reports should preserve config snapshots, prompts, raw stdout/stderr, parsed
model output, diffs, metrics, and cache-cleanup logs. They should not require
keeping downloaded MLX/Hugging Face model files after a test finishes.

See `docs/model-cache-cleanup-policy.md`.

## Quick Start

```bash
cd projects/local-llm-evalops
python3.12 -m venv .venv
. .venv/bin/activate
pip install -e .

llm-evalops run \
  --task examples/tasks/string_normalize \
  --backend noop \
  --runs-dir runs/noop-demo

llm-evalops run \
  --task examples/tasks/string_normalize \
  --backend scripted \
  --runs-dir runs/scripted-demo

llm-evalops run \
  --task examples/tasks/string_normalize \
  --backend qwen25-coder-trace \
  --runs-dir runs/qwen25-demo

llm-evalops run \
  --task examples/tasks/string_normalize \
  --backend sushi-coder-trace \
  --runs-dir runs/sushi-demo
```

Live MLX adapters are available after installing the optional dependency:

```bash
pip install -e '.[mlx]'

LLMEVALOPS_MLX_TIMEOUT=240 llm-evalops run \
  --task examples/tasks/string_normalize \
  --backend qwen25-coder-mlx \
  --runs-dir runs/qwen25-mlx-demo

LLMEVALOPS_MLX_TIMEOUT=240 llm-evalops run \
  --task examples/tasks/string_normalize \
  --backend sushi-coder-mlx \
  --runs-dir runs/sushi-mlx-demo

LLMEVALOPS_MLX_TIMEOUT=240 llm-evalops run \
  --task examples/tasks/string_normalize \
  --backend lfm25-controlled-mlx \
  --runs-dir runs/lfm25-controlled-demo
```

For broad Hugging Face candidate sweeps, use the saved CSV catalog:

```bash
python scripts/run_mlx_candidate_sweep.py \
  --category m4_16gb_priority_or_edge \
  --limit 1 \
  --download-timeout 1800 \
  --timeout 240 \
  --runs-dir runs/candidate-sweep-2026-05-30
```

Each sweep attempt first downloads the model into an attempt-scoped cache, then
starts the generation/eval timer only after download finishes. It writes a
report, then deletes the downloaded model cache before moving to the next
candidate.

Expected result:

- `noop` fails the demo tests.
- `scripted` copies the solution file into the isolated attempt repo and passes.
- `qwen25-coder-trace` and `sushi-coder-trace` replay public-safe small-model
  candidate traces so model-comparison reports can be developed before live MLX
  adapters are connected.

## Small Model Layer

This scaffold includes small-model profiles from the local-agent experiments:

| Profile | Portfolio Label | Current Adapter |
| --- | --- | --- |
| Qwen2.5-Coder 14B MLX | bounded local TDD worker | `qwen25-coder-trace`, `qwen25-coder-mlx` |
| Qwen3.5 Sushi-Coder-RL MLX | candidate artifact worker | `sushi-coder-trace`, `sushi-coder-mlx` |
| LFM2.5-8B-A1B MLX 4bit | general instruction candidate | `lfm25-controlled-mlx` |

See:

- `configs/small-models/qwen25-coder-14b-mlx.json`
- `configs/small-models/qwen35-sushi-coder-rl-mlx.json`
- `docs/small-models/qwen25-coder.md`
- `docs/small-models/sushi-coder.md`

## Benchmark Lanes

The project should grow in three lanes instead of becoming a generic leaderboard:

| Lane | Question | Example Metrics |
| --- | --- | --- |
| Quality | Can the model solve bounded real tasks? | pass/fail, exact match, parser success, regression count |
| Protocol | Can the model follow machine-readable formats? | JSON validity, tool-call validity, think-token leakage, retry count |
| Hardware | Is it usable on the M4 Mac mini? | timeout rate, wall time, TTFT/tok/s where available, peak memory where available |

The first benchmark pack should be `small-model-core`:

- `json_compliance`
- `korean_news_summary`
- `market_event_extraction`
- `string_normalize`
- `tool_call_stub`
- `think_token_cleanup`

The multilingual/domain suite can be re-scored without re-running models:

```bash
python3 scripts/score_alias_normalized_multilingual_suite.py
```

That pass keeps the strict canonical score intact, then adds a conservative
alias-normalized score over the existing `parsed.json` artifacts. It counts
notation and translated equivalents, while keeping acronym-only answers invalid
for expansion prompts such as GDP and ETF.

## Portfolio Framing

Use this line in a resume or project page:

> Built an M4 Mac mini benchmark harness for small local language models. The
> system runs isolated task attempts, evaluates strict output protocols, captures
> MLX/Ollama-style backend artifacts, tracks latency and failure modes, and
> produces reproducible model-selection reports.

## Repository Layout

```text
src/llm_evalops/          Python package
examples/tasks/           Small public-safe task fixtures
docs/                     Architecture and failure taxonomy notes
docs/model-candidates/    Hugging Face MLX candidate queues and catalogs
data/model-candidates/    Raw and CSV candidate exports from Hugging Face
scripts/                  Candidate sweep and maintenance utilities
reports/                  Curated example reports
dashboard/                Static dashboard shell
runs/                     Generated local runs; git-ignored
```

## Next Milestones

1. Add `benchmark_packs/small-model-core` with non-coding summary, extraction,
   protocol, and patch tasks.
2. Add aggregate scoring across quality, protocol, and hardware lanes.
3. Work through the saved Hugging Face candidate catalog in
   `docs/model-candidates/hf-mlx-candidate-catalog-2026-05-30.md` and
   `docs/model-candidates/m4-mac-mini-mlx-candidates-2026-05-30.md`.
4. Add attempt-scoped model cache directories and automatic post-test cleanup.
5. Expand live MLX adapters with prompt/config snapshots and model-output artifacts.
6. Add Apple Silicon runtime metrics where available.
7. Generate aggregate HTML reports across many attempts.
8. Publish a blog post: "Benchmarking small local models on an M4 Mac mini."
