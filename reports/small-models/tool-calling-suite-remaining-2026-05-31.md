# Tool Calling Suite Top 6 - 2026-05-31

This suite evaluates whether local MLX models can select tools and extract arguments.
No tools are executed. The model must emit a structured JSON tool plan.

| Rank | Model | Pass | Sequence | Args | Schema | JSON | Cleanup |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `mlx-community/Mistral-Nemo-Instruct-2407-4bit` | 9/12 | 11/12 | 9/12 | 12/12 | 12/12 | 0 |
| 2 | `prism-ml/Ternary-Bonsai-8B-mlx-2bit` | 8/12 | 12/12 | 8/12 | 11/12 | 12/12 | 0 |
| 3 | `mlx-community/Mistral-7B-Instruct-v0.3-4bit` | 8/12 | 10/12 | 8/12 | 12/12 | 12/12 | 0 |
| 4 | `mlx-community/Qwen2.5-14B-Instruct-4bit` | 8/12 | 10/12 | 8/12 | 12/12 | 12/12 | 0 |
| 5 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit` | 7/12 | 10/12 | 8/12 | 11/12 | 11/12 | 0 |
| 6 | `mlx-community/Qwen3-4B-Instruct-2507-4bit` | 7/12 | 10/12 | 8/12 | 11/12 | 11/12 | 0 |
| 7 | `mlx-community/Qwen2.5-7B-Instruct-4bit` | 7/12 | 9/12 | 7/12 | 12/12 | 12/12 | 0 |
| 8 | `lmstudio-community/LFM2.5-1.2B-Instruct-MLX-6bit` | 5/12 | 8/12 | 6/12 | 11/12 | 12/12 | 0 |
| 9 | `mlx-community/Qwen2.5-1.5B-Instruct-4bit` | 4/12 | 5/12 | 5/12 | 4/12 | 11/12 | 0 |
| 10 | `mlx-community/gemma-2-9b-it-4bit` | 3/12 | 10/12 | 8/12 | 4/12 | 10/12 | 0 |
| 11 | `mlx-community/Qwen2.5-3B-Instruct-4bit` | 3/12 | 10/12 | 8/12 | 5/12 | 11/12 | 0 |
| 12 | `mlx-community/Qwen2-VL-2B-Instruct-4bit` | 3/12 | 7/12 | 4/12 | 10/12 | 10/12 | 0 |
| 13 | `mlx-community/Llama-3.2-3B-Instruct-4bit` | 2/12 | 8/12 | 6/12 | 6/12 | 9/12 | 0 |
| 14 | `mlx-community/gemma-3-1b-it-qat-4bit` | 2/12 | 7/12 | 3/12 | 7/12 | 9/12 | 0 |
| 15 | `mlx-community/Meta-Llama-3.1-8B-Instruct-4bit` | 2/12 | 7/12 | 5/12 | 9/12 | 11/12 | 0 |
| 16 | `mlx-community/Qwen3-1.7B-4bit` | 2/12 | 6/12 | 5/12 | 3/12 | 5/12 | 6 |
| 17 | `lmstudio-community/Qwen3-1.7B-MLX-4bit` | 2/12 | 5/12 | 4/12 | 3/12 | 4/12 | 5 |
| 18 | `lmstudio-community/Qwen3-1.7B-MLX-8bit` | 2/12 | 5/12 | 5/12 | 2/12 | 2/12 | 3 |
| 19 | `mlx-community/Qwen2.5-0.5B-Instruct-4bit` | 2/12 | 3/12 | 3/12 | 9/12 | 9/12 | 0 |
| 20 | `lmstudio-community/Qwen2.5-0.5B-Instruct-MLX-4bit` | 2/12 | 3/12 | 3/12 | 9/12 | 9/12 | 0 |
| 21 | `mlx-community/gemma-3-1b-it-4bit` | 1/12 | 8/12 | 6/12 | 3/12 | 9/12 | 0 |

## Notes

- `Pass` requires schema, ordered tool sequence, required argument subset, and no extra calls.
- The safety case expects no tool call for an externally consequential email request.
