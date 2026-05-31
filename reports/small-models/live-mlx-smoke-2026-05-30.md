# Live MLX Smoke - 2026-05-30

Environment:

- Host: Apple Silicon Mac mini
- Project venv: `.venv`
- MLX package: `mlx-lm`
- Task: `examples/tasks/string_normalize`

## Results

| Backend | Model | Result | Notes |
| --- | --- | --- | --- |
| `sushi-coder-mlx` | `bigatuna/Qwen3.5-9b-Sushi-Coder-RL-MLX` | failed tests after patch | Live model loaded and generated a parseable replacement file. It solved punctuation replacement but missed trimming leading/trailing underscores. |
| `qwen25-coder-mlx` | `mlx-community/Qwen2.5-Coder-14B-Instruct-4bit` | timeout | Timed out after 300 seconds before producing a parseable patch. |

## Interpretation

The live MLX adapter path is real: it can call a local model, capture generated
output, apply a bounded file replacement, and let the harness judge the result.

The first Sushi smoke is a useful failure example, not a blocker. It shows why
the project needs retry loops, failure summaries, and repair attempts rather
than one-shot generation only.

The Qwen2.5-Coder 14B timeout is also useful evidence. On the current 16GB Mac
mini, this model is too slow for a naive one-shot adapter with a 300s timeout.
It may need prompt caching, shorter prompts, lower token limits, or a larger
local inference machine.
