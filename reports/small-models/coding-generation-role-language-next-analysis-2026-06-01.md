# Next Coding Candidate Compiler-Backed Analysis

Run date: 2026-06-01

Stage: `v1_5_polyglot`

Candidate source: `data/benchmark/coding-role-language-candidates-next-2026-06-01.json`

Raw results:
- JSON: `reports/small-models/coding-generation-role-language-next-2026-06-01.json`
- Markdown: `reports/small-models/coding-generation-role-language-next-2026-06-01.md`
- Run artifacts: `runs/coding-generation-role-language-next-2026-06-01`

Baseline to beat: `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit`, which previously scored 3/5 with JSON/schema 5/5 on the compiler-backed role/language suite.

## Summary

The next-candidate sweep found one clear winner: `lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit` passed all five compiler-backed tasks. This is the first local MLX coding-specialized model in this project to beat the Qwen3 4B general-instruct baseline.

Most other candidates either failed the JSON edit protocol or produced plausible edits that did not pass compiler/tests. Model size alone was not enough: Devstral was heavy and failed protocol completely, while Qwen2.5-Coder 14B was heavy but reliable.

## Leaderboard

| Rank | Model | Pass | JSON | Schema | Read |
| ---: | --- | ---: | ---: | ---: | --- |
| 1 | `lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit` | 5/5 | 5/5 | 5/5 | New coding quality leader. Passed Python, TypeScript, JavaScript, Go, and Rust. |
| 2 | `mlx-community/Qwen2.5-Coder-7B-Instruct-4bit` | 1/5 | 5/5 | 4/5 | Better protocol than prior 7B quant, but only Go passed. |
| 3 | `dangerusslee/FastApply-7B-v1.0-mlx-4Bit` | 0/5 | 5/5 | 5/5 | Excellent JSON/edit protocol, but not a general code generator. |
| 4 | `mlx-community/DeepSeek-Coder-V2-Lite-Instruct-4bit-mlx` | 0/5 | 4/5 | 4/5 | Runtime works, but no compiler-backed task passed. |
| 5 | `lmstudio-community/Qwen2.5-Coder-3B-Instruct-MLX-4bit` | 0/5 | 2/5 | 2/5 | Alternative 3B quant did not fix the 3B weakness. |
| 6 | `aciidix/FastApply-1.5B-v1.0-mlx-4Bit` | 0/5 | 1/5 | 0/5 | Not compatible with this generation protocol. |
| 7 | `mlx-community/granite-3b-code-instruct-4bit` | 0/5 | 0/5 | 0/5 | Not usable in the current JSON edit-agent harness. |
| 8 | `mlx-community/stable-code-instruct-3b-4bit` | 0/5 | 0/5 | 0/5 | Not usable in the current JSON edit-agent harness. |
| 9 | `lmstudio-community/Devstral-Small-2507-MLX-4bit` | 0/5 | 0/5 | 0/5 | Heavy and failed generation/protocol in this setup. |

## Model Notes

### Qwen2.5-Coder 14B

This is the first coding-specialized model that clearly earns a place in the local EvalOps stack. It passed:

- Python syntax repair
- TypeScript strict type contract
- JavaScript temporal drawdown unit patch
- Go route contract via `go test`
- Rust `Result` contract via `cargo test`

Operationally it is not as light as Qwen3 4B. Download plus execution took 861.11 seconds in this loop, with catalog storage around 8.32 GB. Still, it is the new quality leader for local coding work if memory and latency are acceptable.

### Qwen2.5-Coder 7B Community Quant

This quant is better than the previously tested LM Studio 7B in protocol behavior: JSON 5/5 and schema 4/5. It passed only Go. It failed TypeScript zero-previous-close handling, JavaScript temporal drawdown, and Rust tuple handling.

Use it only if 14B is too heavy and the task is simple routing or structural code.

### FastApply 7B

FastApply 7B followed the JSON/schema/edit contract perfectly but passed no tasks. That is still useful information: it may be an apply/edit-format model, not a full generation model. It deserves a separate patch-application benchmark, not this role/language generation benchmark.

### DeepSeek-Coder V2 Lite

Unlike the earlier DeepSeek models, this one generated parseable edits for most tasks. But it failed all tests: Python sorting/edge behavior, TypeScript zero handling, JavaScript JSON, Go missing imports, and Rust tests.

Do not promote it as a worker, but keep it as a potential repair-loop candidate only if a different prompt/template is tested.

### Devstral, Granite, Stable Code

These did not fit the JSON edit-agent protocol. Devstral was especially costly: 1237.774 seconds and 0/5 JSON. Granite and Stable Code are small but old and failed JSON across the board.

## Recommendation

1. Promote `lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit` as the local coding quality leader.
2. Keep `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` as the lightweight always-on baseline.
3. Treat Qwen2.5-Coder 7B as a fallback only when 14B is too heavy.
4. Do not continue general-generation testing for Devstral, Granite, Stable Code, or FastApply in this harness.
5. Create a separate `patch_apply` lane before judging FastApply models fairly.

## Cache Cleanup

The benchmark loop deleted model caches after each candidate. Verification found no remaining `model-cache` directories under `runs/coding-generation-role-language-next-2026-06-01`.

## Runner Note

During analysis, the runner was updated to exclude generated build artifacts such as Rust `target/`, `Cargo.lock`, `node_modules`, and Python cache files from prompt snapshots and diff counts. This does not change pass/fail outcomes; it keeps future diff evidence focused on model-edited source files.
