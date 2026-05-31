# M4 Mac Mini SLM EvalOps

Evaluation-driven benchmark harness and result archive for small local language
models running on an M4 Mac mini.

This project turns local SLM experiments into repeatable engineering evidence:
strict multilingual factual prompts, deterministic alias-normalized scoring,
tool-calling plan evaluation, attempt-scoped model-cache cleanup, candidate
catalogs, and public-safe result reports.

## Current Leaderboard

Composite score uses equal weight:

```text
50% alias-normalized 100-prompt factual score
+ 50% tool-calling pass rate
```

Tool-calling tests use 12 tool-selection cases. The 100-prompt suite covers 10
domains across 10 languages. Model size is Hugging Face repository storage
(`usedStorage`) rounded to one decimal place.

| Rank | Model | Size | Composite | 100p Alias | 100p Strict | Tool Calling | Tool Sequence | Link |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Qwen2.5 14B Instruct 4bit | 7.7 GB | 78.3 | 90/100 | 82/100 | 8/12 | 10/12 | [HF](https://huggingface.co/mlx-community/Qwen2.5-14B-Instruct-4bit) |
| 2 | Ternary Bonsai 8B 2bit | 2.2 GB | 77.3 | 88/100 | 50/100 | 8/12 | 12/12 | [HF](https://huggingface.co/prism-ml/Ternary-Bonsai-8B-mlx-2bit) |
| 3 | Mistral 7B Instruct v0.3 4bit | 3.8 GB | 77.3 | 88/100 | 59/100 | 8/12 | 10/12 | [HF](https://huggingface.co/mlx-community/Mistral-7B-Instruct-v0.3-4bit) |
| 4 | Mistral Nemo Instruct 2407 4bit | 6.4 GB | 76.5 | 78/100 | 59/100 | 9/12 | 11/12 | [HF](https://huggingface.co/mlx-community/Mistral-Nemo-Instruct-2407-4bit) |
| 5 | Qwen3 4B Instruct 2507 5bit | 2.6 GB | 74.2 | 90/100 | 53/100 | 7/12 | 9/12 | [HF](https://huggingface.co/lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit) |
| 6 | Qwen3 4B Instruct 2507 4bit, LM Studio | 2.1 GB | 73.2 | 88/100 | 55/100 | 7/12 | 10/12 | [HF](https://huggingface.co/lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit) |
| 7 | Qwen3 4B Instruct 2507 4bit, MLX Community | 2.1 GB | 72.7 | 87/100 | 54/100 | 7/12 | 10/12 | [HF](https://huggingface.co/mlx-community/Qwen3-4B-Instruct-2507-4bit) |
| 8 | Qwen3 4B Instruct 2507 6bit | 3.1 GB | 72.2 | 86/100 | 48/100 | 7/12 | 9/12 | [HF](https://huggingface.co/lmstudio-community/Qwen3-4B-Instruct-2507-MLX-6bit) |
| 9 | Qwen3-VL 4B Instruct 4bit | 2.9 GB | 70.7 | 83/100 | 51/100 | 7/12 | 10/12 | [HF](https://huggingface.co/lmstudio-community/Qwen3-VL-4B-Instruct-MLX-4bit) |
| 10 | Qwen2.5 7B Instruct 4bit | 4.0 GB | 69.2 | 80/100 | 48/100 | 7/12 | 9/12 | [HF](https://huggingface.co/mlx-community/Qwen2.5-7B-Instruct-4bit) |

Readout:

- Quality leader: `Qwen2.5-14B-Instruct-4bit`. It has the strongest strict
  factual score and ties the best alias-normalized factual score, but it is
  heavy for a 16 GB M4 Mac mini.
- Practical balanced candidate: `Qwen3-4B-Instruct-2507-MLX-5bit`. It ties the
  14B model at 90/100 alias-normalized factual score while staying much lighter;
  its weaker 7/12 tool-calling score is the main tradeoff.
- Tool-calling leader: `Mistral-Nemo-Instruct-2407-4bit`. It scores 9/12 on the
  tool lane but drops on 100-prompt factual scoring.
- Surprise candidate: `Ternary-Bonsai-8B-mlx-2bit`. It is compact, reaches
  88/100 alias-normalized factual score, and gets a perfect 12/12 tool sequence
  score.

Primary reports:

- [Composite ranking](reports/small-models/tool-calling-plus-100prompt-composite-2026-05-31.md)
- [All tool-calling candidates](reports/small-models/tool-calling-suite-all-candidates-2026-05-31.md)
- [Tool leaders 100-prompt factual scoring](reports/small-models/multilingual-domain-suite-tool-leaders-alias-normalized-2026-05-31.md)
- [Next14 MLX candidate scoring](reports/small-models/multilingual-domain-suite-next14-alias-normalized-2026-05-31.md)
- [M4 MLX candidate refresh](reports/small-models/m4-mac-mini-mlx-refresh-analysis-2026-05-31.md)

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

The checked-in version is a public-safe M4 Mac mini benchmark project. It
includes:

- a runnable demo task
- a scripted backend that simulates a successful model patch
- a no-op backend for baseline comparison
- per-attempt isolated workspaces
- deterministic multilingual/domain and tool-calling benchmark scripts
- alias-normalized scoring over saved raw model outputs
- Hugging Face MLX candidate catalogs for M4 16 GB testing
- curated JSON and Markdown reports
- a small static dashboard template
- docs for failure taxonomy and design decisions

The primary target is Hugging Face MLX models that are plausible on the current
M4 Mac mini. Coding-agent backends and trace replays are intentionally out of
scope for this public benchmark snapshot.

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
5. Add Apple Silicon runtime metrics where available.
6. Generate aggregate HTML reports across many attempts.
7. Publish a blog post: "Benchmarking small local models on an M4 Mac mini."
