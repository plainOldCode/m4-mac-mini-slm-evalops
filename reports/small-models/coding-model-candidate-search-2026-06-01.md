# Coding Model Candidate Search

Search date: 2026-06-01

Scope: Hugging Face MLX models that may be useful for local coding, role/language, or patch-apply testing on the M4 Mac mini.

## Practical Next Test Set

| Priority | Model | Why Test | Risk |
| ---: | --- | --- | --- |
| 1 | `mlx-community/Qwen2.5-Coder-7B-Instruct-4bit` | Alternative community quant to the LM Studio 7B candidate already tested. Could separate model quality from quant/template issues. | May still inherit Qwen2.5 protocol weakness. |
| 2 | `lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit` | Practical upper-bound Qwen2.5 coding model. Observed storage about 8.32 GB. | May be tight on 16 GB once KV/cache overhead is included. |
| 3 | `lmstudio-community/Qwen2.5-Coder-3B-Instruct-MLX-4bit` | Alternative quant to the already-tested community 3B. | Same model family may fail similarly. |
| 4 | `mlx-community/DeepSeek-Coder-V2-Lite-Instruct-4bit-mlx` | Different DeepSeek generation from the older 1.3B/6.7B models that failed. Observed storage about 8.84 GB. | Custom-code/runtime risk; prior DeepSeek MLX results were poor. |
| 5 | `lmstudio-community/Devstral-Small-2507-MLX-4bit` | Agentic coding-oriented Devstral candidate. Observed storage about 13.28 GB. | Heavy for M4 16 GB. Treat as edge candidate. |
| 6 | `mlx-community/granite-3b-code-instruct-4bit` | Lightweight non-Qwen code SLM baseline. | Old/low-download model; quality likely limited. |
| 7 | `mlx-community/stable-code-instruct-3b-4bit` | Lightweight non-Qwen code SLM baseline. | Old/low-download model; may be weaker than Qwen3 4B. |
| 8 | `aciidix/FastApply-1.5B-v1.0-mlx-4Bit` | Role-specific edit/apply model. | Not a general generator; should be tested only on edit-contract tasks. |
| 9 | `dangerusslee/FastApply-7B-v1.0-mlx-4Bit` | Larger role-specific edit/apply model. | Low downloads and narrow task scope. |

Candidate JSON: `data/benchmark/coding-role-language-candidates-next-2026-06-01.json`

## Heavy Or Edge Candidates

These are interesting but should not be first on the M4 16 GB loop:

| Model | Reason To Defer |
| --- | --- |
| `lmstudio-community/Qwen3-Coder-30B-A3B-Instruct-MLX-4bit` | Very popular and coding-specific, but observed storage about 17.19 GB. It may exceed practical 16 GB Mac mini comfort. |
| `mlx-community/Qwen3-Coder-30B-A3B-Instruct-4bit` | Same model family, observed storage about 34.37 GB in the catalog snapshot. |
| `lmstudio-community/Qwen3-Coder-Next-MLX-4bit` | Very popular, but observed storage about 44.86 GB. Not a Mac mini 16 GB target. |
| `mlx-community/Codestral-22B-v0.1-4bit` | Relevant coding model, but 22B class and license/runtime concerns make it a later edge test. |
| `lmstudio-community/MiniMax-M2.5-MLX-4bit` | Recent and popular, but observed storage about 128.68 GB in the catalog snapshot. Not suitable for this Mac mini loop. |

## Recommended Loop

Run in this order:

1. `mlx-community/Qwen2.5-Coder-7B-Instruct-4bit`
2. `lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit`
3. `lmstudio-community/Qwen2.5-Coder-3B-Instruct-MLX-4bit`
4. `mlx-community/DeepSeek-Coder-V2-Lite-Instruct-4bit-mlx`
5. `mlx-community/granite-3b-code-instruct-4bit`
6. `mlx-community/stable-code-instruct-3b-4bit`
7. `aciidix/FastApply-1.5B-v1.0-mlx-4Bit`
8. `dangerusslee/FastApply-7B-v1.0-mlx-4Bit`

Only try Devstral after the lighter set because it is much heavier.

The current bar remains `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit`, which scored 3/5 on the compiler-backed role/language suite with JSON/schema 5/5.
