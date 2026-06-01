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
domains across 10 languages. OpenClaw Native checks whether the model can drive
the real OpenClaw tool loop and create a verified `exec` side-effect marker.
Model size is Hugging Face repository storage (`usedStorage`) rounded to one
decimal place.

| Rank | Model | Size | Composite | 100p Alias | 100p Strict | Tool Calling | Tool Sequence | OpenClaw Native | Link |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | Qwen2.5 14B Instruct 4bit | 7.7 GB | 78.3 | 90/100 | 82/100 | 8/12 | 10/12 | Fail | [HF](https://huggingface.co/mlx-community/Qwen2.5-14B-Instruct-4bit) |
| 2 | Ternary Bonsai 8B 2bit | 2.2 GB | 77.3 | 88/100 | 50/100 | 8/12 | 12/12 | Pass* | [HF](https://huggingface.co/prism-ml/Ternary-Bonsai-8B-mlx-2bit) |
| 3 | Mistral 7B Instruct v0.3 4bit | 3.8 GB | 77.3 | 88/100 | 59/100 | 8/12 | 10/12 | Adapter-pass** | [HF](https://huggingface.co/mlx-community/Mistral-7B-Instruct-v0.3-4bit) |
| 4 | Mistral Nemo Instruct 2407 4bit | 6.4 GB | 76.5 | 78/100 | 59/100 | 9/12 | 11/12 | Adapter-pass** | [HF](https://huggingface.co/mlx-community/Mistral-Nemo-Instruct-2407-4bit) |
| 5 | Qwen3 4B Instruct 2507 5bit | 2.6 GB | 74.2 | 90/100 | 53/100 | 7/12 | 9/12 | Pass | [HF](https://huggingface.co/lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit) |
| 6 | Qwen3 4B Instruct 2507 4bit, LM Studio | 2.1 GB | 73.2 | 88/100 | 55/100 | 7/12 | 10/12 | Pass | [HF](https://huggingface.co/lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit) |
| 7 | Qwen3 4B Instruct 2507 4bit, MLX Community | 2.1 GB | 72.7 | 87/100 | 54/100 | 7/12 | 10/12 | Pass | [HF](https://huggingface.co/mlx-community/Qwen3-4B-Instruct-2507-4bit) |
| 8 | Qwen3 4B Instruct 2507 6bit | 3.1 GB | 72.2 | 86/100 | 48/100 | 7/12 | 9/12 | Pass | [HF](https://huggingface.co/lmstudio-community/Qwen3-4B-Instruct-2507-MLX-6bit) |
| 9 | Qwen3-VL 4B Instruct 4bit | 2.9 GB | 70.7 | 83/100 | 51/100 | 7/12 | 10/12 | Pass | [HF](https://huggingface.co/lmstudio-community/Qwen3-VL-4B-Instruct-MLX-4bit) |
| 10 | Qwen2.5 7B Instruct 4bit | 4.0 GB | 69.2 | 80/100 | 48/100 | 7/12 | 9/12 | Pass | [HF](https://huggingface.co/mlx-community/Qwen2.5-7B-Instruct-4bit) |

`Pass*`: tool side effect was verified, but the follow-up assistant turn hit a
Metal out-of-memory error after the tool ran. Treat as promising, not yet
stable enough for an always-on default.

`Adapter-pass**`: native OpenAI-style tool execution failed, but a constrained
text-intent adapter replay recovered the benchmark tool side effect. Treat as
patchable, not native-compatible yet.

Readout:

- Quality leader: `Qwen2.5-14B-Instruct-4bit`. It has the strongest strict
  factual score and ties the best alias-normalized factual score, but it is
  heavy for a 16 GB M4 Mac mini and failed the OpenClaw native tool execution
  canary.
- Practical OpenClaw candidate: `Qwen3-4B-Instruct-2507-MLX-5bit`. It ties the
  14B model at 90/100 alias-normalized factual score while staying much lighter
  and passes the real OpenClaw native tool execution canary; its weaker 7/12
  tool-calling score is the main tradeoff.
- Tool-calling leader: `Mistral-Nemo-Instruct-2407-4bit`. It scores 9/12 on the
  tool lane but drops on 100-prompt factual scoring.
- Surprise candidate: `Ternary-Bonsai-8B-mlx-2bit`. It is compact, reaches
  88/100 alias-normalized factual score, and gets a perfect 12/12 tool sequence
  score. It also executed an OpenClaw native tool, but needs stability work
  before always-on use.
- Adapter-recoverable candidates: `Mistral-Nemo-Instruct-2407-4bit` and
  `Mistral-7B-Instruct-v0.3-4bit` failed native OpenAI-style tool execution,
  but a constrained text-intent adapter replay recovered the benchmark tool
  side effect. `Qwen2.5-14B-Instruct-4bit` did not recover because its failure
  was runtime memory pressure, not text/tool formatting.

Primary reports:

- [Composite ranking](reports/small-models/tool-calling-plus-100prompt-composite-2026-05-31.md)
- [OpenClaw native tool execution](reports/small-models/openclaw-native-tool-execution-2026-05-31.md)
- [OpenClaw tool adapter replay](reports/small-models/openclaw-tool-adapter-replay-2026-05-31.md)
- [All tool-calling candidates](reports/small-models/tool-calling-suite-all-candidates-2026-05-31.md)
- [Tool leaders 100-prompt factual scoring](reports/small-models/multilingual-domain-suite-tool-leaders-alias-normalized-2026-05-31.md)
- [Next14 MLX candidate scoring](reports/small-models/multilingual-domain-suite-next14-alias-normalized-2026-05-31.md)
- [M4 MLX candidate refresh](reports/small-models/m4-mac-mini-mlx-refresh-analysis-2026-05-31.md)
- [Coding generation benchmark plan](docs/coding-generation-benchmark.md)

## Coding Generation Results

Coding generation is scored separately from factual QA and tool calling. The
lane asks models to emit complete replacement files as strict JSON, applies only
allowlisted paths, then runs deterministic local checks across Python,
TypeScript, JavaScript, Go, and Rust.

The current compiler-backed `v1_5_polyglot` suite uses:

- Python syntax and behavior checks
- `tsc --strict --noEmit` for TypeScript
- JavaScript unit tests for temporal drawdown logic
- `go test ./...` for Go route contracts
- `cargo test` for Rust `Result` contracts

| Rank | Model | Pass | JSON | Schema | Readout |
| ---: | --- | ---: | ---: | ---: | --- |
| 1 | Qwen2.5-Coder 14B Instruct MLX 4bit | 5/5 | 5/5 | 5/5 | New local coding quality leader; passed Python, TypeScript, JavaScript, Go, and Rust. |
| 2 | Qwen3 4B Instruct 2507 MLX 5bit | 3/5 | 5/5 | 5/5 | Lightweight always-on coding baseline; passed Python, TypeScript, and Go. |
| 3 | Qwen3.5 9B Sushi-Coder-RL MLX | 3/5 | 3/5 | 3/5 | Interesting 9B challenger; passed TypeScript, JavaScript, and Go, but protocol reliability is weaker than Qwen3 4B. |
| 4 | Qwen2.5-Coder 7B Instruct MLX 4bit | 1/5 | 5/5 | 4/5 | Strong protocol adherence, but only the Go task passed. |
| 5 | FastApply 7B v1.0 MLX 4bit | 0/5 | 5/5 | 5/5 | Excellent edit protocol, but not a general code generator; needs a separate patch-apply lane. |
| 6 | DeepSeek-Coder V2 Lite Instruct MLX 4bit | 0/5 | 4/5 | 4/5 | Generated parseable edits, but no compiler-backed task passed. |

Operational readout:

- `lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit` is the quality
  worker when latency and memory are acceptable.
- `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` remains the practical
  lightweight coding baseline for the M4 Mac mini.
- `bigatuna/Qwen3.5-9b-Sushi-Coder-RL-MLX` matched Qwen3 4B on pass count, but
  not on machine-readable edit reliability. Keep it as a challenger, not a
  replacement.
- 7B and smaller coding-specialized models should be treated as constrained
  patch candidates with compiler/test repair loops, not autonomous workers.
- Qwopus 9B and the 9B agent/coder merge failed the direct JSON edit protocol
  and are not useful in this lane.
- FastApply models should not be judged by this generation suite; they need a
  dedicated patch-application benchmark.
- Qwen3-Coder 30B A3B 4bit is skipped for this M4 16 GB setup; its storage size
  is too close to physical memory to justify testing after the 14B model reached
  5/5.

Primary coding reports:

- [9B follow-up analysis](reports/small-models/coding-generation-role-language-9b-followup-analysis-2026-06-01.md)
- [9B follow-up raw results](reports/small-models/coding-generation-role-language-9b-followup-2026-06-01.md)
- [Next coding candidate analysis](reports/small-models/coding-generation-role-language-next-analysis-2026-06-01.md)
- [Next coding candidate raw results](reports/small-models/coding-generation-role-language-next-2026-06-01.md)
- [Compiler-backed baseline analysis](reports/small-models/coding-generation-role-language-compiled-analysis-2026-06-01.md)
- [Compiler-backed baseline raw results](reports/small-models/coding-generation-role-language-compiled-2026-06-01.md)

## Ollama Mac Mini Full-Suite Results

The non-MLX pass evaluates Mac-mini-realistic Ollama models across all four
operational lanes: 100-prompt factual QA, structured tool calling, OpenClaw
native tool execution, and compiler-backed coding generation. Ollama JSON-mode
is enabled for the structured JSON suites. `qwen3-coder:30b-a3b` is excluded
because it is outside the 16 GB M4 Mac mini comfort zone for a full-suite run.

| Rank | Model | 100p Alias | Tool Calling | OpenClaw Native | Coding | Readout |
| ---: | --- | ---: | ---: | --- | ---: | --- |
| 1 | `qwen2.5-coder:14b` | 94/100 | 9/12 | Fail | 4/5 | Best Ollama candidate; useful fallback coding worker, but not native OpenClaw-ready. |
| 2 | `qwen2.5-coder:7b` | 87/100 | 7/12 | Fail | 2/5 | Better under Ollama JSON-mode than the MLX 7B result, still mid-tier. |
| 3 | `qwen3:4b` | 90/100 | 3/12 | Fail | 1/5 | Good lightweight factual baseline, weak at tool selection and coding here. |
| 4 | `llama3.1:8b` | 88/100 | 6/12 | Fail | 0/5 | General baseline only; not useful as a coding worker in this suite. |

Operational readout:

- The best Ollama result is still below the current MLX coding leader:
  `lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit` reached 5/5 on the
  compiler-backed coding suite, while Ollama `qwen2.5-coder:14b` reached 4/5.
- None of the Ollama candidates passed the native OpenClaw tool execution
  canary. The common failure mode was text that described or approximated a tool
  call without emitting a valid structured invocation that OpenClaw executed.
- Coding-specialized models helped most when JSON-mode structured output was
  available, but specialization alone did not guarantee native-agent behavior.

Primary Ollama reports:

- [Ollama full-suite analysis](reports/small-models/ollama-mac-mini-full-suite-analysis-2026-06-01.md)
- [Ollama second-queue analysis](reports/small-models/ollama-mac-mini-second-queue-analysis-2026-06-01.md)
- [Ollama 100-prompt factual scoring](reports/small-models/multilingual-domain-suite-ollama-mac-mini-alias-normalized-2026-06-01.md)
- [Ollama tool calling](reports/small-models/tool-calling-suite-ollama-mac-mini-2026-06-01.md)
- [Ollama OpenClaw native tool execution](reports/small-models/openclaw-native-tool-execution-ollama-mac-mini-2026-06-01.md)
- [Ollama coding generation](reports/small-models/coding-generation-role-language-ollama-mac-mini-2026-06-01.md)

Second-queue readout:

- `gemma3:12b` reached `100/100` alias-normalized factual score and `12/12`
  tool sequence selection, but coding remained `2/5`.
- `qwen3:8b` was the best balanced 8B candidate: `90/100` factual,
  `9/12` tool calling, and `3/5` coding.
- `cogito:8b` was the best structured tool planner in the second queue at
  `10/12`, but it was weaker on factual strict scoring and coding.
- `deepseek-coder-v2:16b` ran successfully but did not justify its size:
  `86/100` factual, `6/12` tool calling, and `2/5` coding.
- No second-queue Ollama model passed the OpenClaw native tool execution canary.

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

The coding-generation lane is intentionally separate from factual QA and
tool-calling. It asks models to return complete replacement files as JSON,
applies only allowlisted paths, and scores with deterministic local tests:

```bash
python scripts/run_coding_generation_suite.py \
  --candidates data/benchmark/coding-generation-smoke-candidates-2026-06-01.json \
  --runs-dir runs/coding-generation-smoke-2026-06-01 \
  --report-json reports/small-models/coding-generation-smoke-2026-06-01.json \
  --report-md reports/small-models/coding-generation-smoke-2026-06-01.md \
  --limit 1
```

The progression is `v1_smoke` for Python/JavaScript/HTML-CSS,
`v1_5_polyglot` for role/language fit across Python, TypeScript,
JavaScript, Go, and Rust, and `v2_frontend` for React/Vue/component-specific
UI checks. See `docs/coding-generation-benchmark.md`.

GPT comparison runs use the `codex-cli` backend so credentials stay outside the
repository:

```bash
CODEX_CLI_AUTH_HOME=/Users/miniadmin/.codex \
python scripts/run_coding_generation_suite.py \
  --start 1 \
  --limit 2
```

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
