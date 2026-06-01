# Compiler-Backed Role/Language Coding Analysis

Run date: 2026-06-01

Stage: `v1_5_polyglot`

Toolchains installed before this run:
- Go: `go1.26.3 darwin/arm64`
- Rust: `rustc 1.95.0`, `cargo 1.95.0`
- TypeScript: `tsc 6.0.3`

Raw results:
- JSON: `reports/small-models/coding-generation-role-language-compiled-2026-06-01.json`
- Markdown: `reports/small-models/coding-generation-role-language-compiled-2026-06-01.md`
- Run artifacts: `runs/coding-generation-role-language-compiled-2026-06-01`

## Summary

Adding real compiler-backed checks made the role/language suite more discriminating. `Qwen3-4B-Instruct-2507-MLX-5bit` remains the only viable local coding-agent baseline, passing 3/5 with perfect JSON/schema adherence. Both Qwen2.5-Coder candidates failed every compiled role/language task.

The result strengthens the earlier conclusion: for small local models, coding specialization is less important than stable instruction following, file-edit protocol adherence, and the ability to respect language-specific contracts.

## Results

| Rank | Model | Pass | JSON | Schema | Read |
| ---: | --- | ---: | ---: | ---: | --- |
| 1 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` | 3/5 | 5/5 | 5/5 | Passed Python, TypeScript, and Go; failed JavaScript temporal logic and Rust syntax. |
| 2 | `mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit` | 0/5 | 4/5 | 4/5 | Often returned editable files, but none passed tests. |
| 3 | `mlx-community/Qwen2.5-Coder-3B-Instruct-4bit` | 0/5 | 2/5 | 2/5 | Protocol adherence remained weak and no task passed. |

## Task-Level Findings

### Python: Syntax Repair

Only Qwen3 4B passed. The Qwen2.5-Coder models failed before test execution because no parseable JSON edit was produced.

This task is a useful low-cost check for whether a model can fix syntax while preserving edge-case behavior.

### TypeScript: Type Contract

Qwen3 4B passed `tsc --strict --noEmit` and the structural API contract. Qwen2.5-Coder 1.5B produced parseable TypeScript, but failed the benchmark-specific rounding contract. Qwen2.5-Coder 3B did not produce valid JSON.

This suggests TypeScript is a good language for separating "compiles" from "follows API contract."

### JavaScript: Unit Patch

All models failed the drawdown patch. Qwen3 4B returned `0.09` where the expected result was `0` for a never-declining series. Qwen2.5-Coder models made larger semantic errors such as returning raw price differences or non-temporal min/max calculations.

Keep this task. It catches plausible-looking code that does not preserve time-order invariants.

### Go: Route Contract

Qwen3 4B passed real `go test ./...`. The Qwen2.5-Coder models did not pass after compiler/test enforcement.

This is a good candidate for "simple routing worker" evaluation because it tests signatures, struct fields, string normalization, and branch behavior.

### Rust: Result Contract

No model passed Rust. Qwen3 4B followed the intended shape but emitted invalid Rust with escaped newline text in the source. Qwen2.5-Coder 1.5B generated a large invalid patch and hit a compile error around tuple handling after `split_once`.

Rust should stay in the suite because it strongly exposes syntax precision and explicit error handling failures.

## Recommendation

For local coding work:

1. Keep `Qwen3-4B-Instruct-2507-MLX-5bit` as the only current local coding-agent baseline.
2. Do not use Qwen2.5-Coder 1.5B/3B as autonomous coding workers.
3. If using Qwen2.5-Coder at all, constrain it to narrow candidate-patch generation and always run compiler/tests plus a repair loop.
4. Keep JavaScript drawdown and Rust result-contract tasks as hard filters.
5. Add future candidates to this compiler-backed suite before considering them for local EvalOps automation.

## Cache Cleanup

The benchmark loop deleted model caches after each candidate. Verification found no remaining `model-cache` directories under `runs/coding-generation-role-language-compiled-2026-06-01`.
