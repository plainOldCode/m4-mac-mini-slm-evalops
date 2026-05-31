# M4 Mac Mini Benchmark Scope

## Positioning

This project benchmarks small local language models on the current M4 Mac mini.
It should not try to reproduce every public leaderboard. Public leaderboards
answer "which model scores highest in general?" This project answers "which
model is useful enough to keep in this local workflow?"

## Target Models

The first model class is 3B-14B local models that can plausibly run through MLX
or another local runtime on Apple Silicon:

- Qwen-family coder models
- Sushi/Qwen coder variants
- LFM2.5-style general instruction models
- future 3B-9B summary/extraction models

Larger models and cloud models are useful as comparison baselines, but they are
not the center of the project.

## Core Questions

- Does the model load and produce output on the M4 Mac mini?
- Does it complete within a practical timeout?
- Does it follow strict output contracts?
- Does it solve bounded tasks without relying on an LLM judge?
- Does it fail in a diagnosable way?
- Would a future Mac Studio or GB10-class machine materially change the answer?
- Can the evidence be kept while deleting the downloaded model afterward?

## Benchmark Pack Plan

`small-model-core` should cover:

- `json_compliance`: strict JSON object, no prose.
- `think_token_cleanup`: final-answer extraction and leakage detection.
- `korean_news_summary`: concise Korean summary with source facts preserved.
- `market_event_extraction`: company/event/number/date extraction from Korean
  market text.
- `tool_call_stub`: simple tool-call schema formatting.
- `string_normalize`: bounded coding patch with deterministic tests.

## Report Shape

Each model report should separate:

- quality score
- protocol score
- runtime score
- failure modes
- recommended use

## Storage Discipline

The project should assume exhaustive candidate testing. That means model caches
must not accumulate indefinitely.

Default rule:

- download each live candidate into an attempt-scoped cache
- run the smoke/eval pack
- save report artifacts
- delete the candidate cache completely after the test

This keeps the Mac mini usable while still preserving reproducible evidence for
every tested model.

Example recommendation labels:

- `keep_for_summary`
- `keep_for_extraction`
- `keep_for_coding_trace_only`
- `controlled_semantic_signal_only`
- `reject_for_current_mac_mini`
