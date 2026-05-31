# Tool Calling Suite All Candidates - 2026-05-31

Models: 27

| Rank | Model | Pass | Sequence | Args | Schema | JSON |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | `mlx-community/Mistral-Nemo-Instruct-2407-4bit` | 9/12 | 11/12 | 9/12 | 12/12 | 12/12 |
| 2 | `prism-ml/Ternary-Bonsai-8B-mlx-2bit` | 8/12 | 12/12 | 8/12 | 11/12 | 12/12 |
| 3 | `mlx-community/Mistral-7B-Instruct-v0.3-4bit` | 8/12 | 10/12 | 8/12 | 12/12 | 12/12 |
| 4 | `mlx-community/Qwen2.5-14B-Instruct-4bit` | 8/12 | 10/12 | 8/12 | 12/12 | 12/12 |
| 5 | `lmstudio-community/Qwen3-VL-4B-Instruct-MLX-4bit` | 7/12 | 10/12 | 8/12 | 11/12 | 11/12 |
| 6 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit` | 7/12 | 10/12 | 8/12 | 11/12 | 11/12 |
| 7 | `mlx-community/Qwen3-4B-Instruct-2507-4bit` | 7/12 | 10/12 | 8/12 | 11/12 | 11/12 |
| 8 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` | 7/12 | 9/12 | 8/12 | 11/12 | 11/12 |
| 9 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-6bit` | 7/12 | 9/12 | 8/12 | 11/12 | 11/12 |
| 10 | `mlx-community/Qwen2.5-7B-Instruct-4bit` | 7/12 | 9/12 | 7/12 | 12/12 | 12/12 |
| 11 | `mlx-community/gemma-3n-E2B-it-lm-4bit` | 6/12 | 10/12 | 7/12 | 11/12 | 11/12 |
| 12 | `mlx-community/Phi-4-mini-instruct-4bit` | 6/12 | 8/12 | 6/12 | 10/12 | 10/12 |
| 13 | `lmstudio-community/LFM2.5-1.2B-Instruct-MLX-8bit` | 5/12 | 8/12 | 6/12 | 11/12 | 12/12 |
| 14 | `lmstudio-community/LFM2.5-1.2B-Instruct-MLX-6bit` | 5/12 | 8/12 | 6/12 | 11/12 | 12/12 |
| 15 | `mlx-community/Qwen2.5-1.5B-Instruct-4bit` | 4/12 | 5/12 | 5/12 | 4/12 | 11/12 |
| 16 | `mlx-community/Qwen2.5-3B-Instruct-4bit` | 3/12 | 10/12 | 8/12 | 5/12 | 11/12 |
| 17 | `mlx-community/gemma-2-9b-it-4bit` | 3/12 | 10/12 | 8/12 | 4/12 | 10/12 |
| 18 | `mlx-community/Qwen2-VL-2B-Instruct-4bit` | 3/12 | 7/12 | 4/12 | 10/12 | 10/12 |
| 19 | `mlx-community/Llama-3.2-3B-Instruct-4bit` | 2/12 | 8/12 | 6/12 | 6/12 | 9/12 |
| 20 | `mlx-community/Meta-Llama-3.1-8B-Instruct-4bit` | 2/12 | 7/12 | 5/12 | 9/12 | 11/12 |
| 21 | `mlx-community/gemma-3-1b-it-qat-4bit` | 2/12 | 7/12 | 3/12 | 7/12 | 9/12 |
| 22 | `mlx-community/Qwen3-1.7B-4bit` | 2/12 | 6/12 | 5/12 | 3/12 | 5/12 |
| 23 | `lmstudio-community/Qwen3-1.7B-MLX-8bit` | 2/12 | 5/12 | 5/12 | 2/12 | 2/12 |
| 24 | `lmstudio-community/Qwen3-1.7B-MLX-4bit` | 2/12 | 5/12 | 4/12 | 3/12 | 4/12 |
| 25 | `mlx-community/Qwen2.5-0.5B-Instruct-4bit` | 2/12 | 3/12 | 3/12 | 9/12 | 9/12 |
| 26 | `lmstudio-community/Qwen2.5-0.5B-Instruct-MLX-4bit` | 2/12 | 3/12 | 3/12 | 9/12 | 9/12 |
| 27 | `mlx-community/gemma-3-1b-it-4bit` | 1/12 | 8/12 | 6/12 | 3/12 | 9/12 |

## Notes

- This combines the top6 and remaining-candidate tool-calling runs.
- Tools were not executed; this is a deterministic structured tool-plan benchmark.
- Heavy models should be judged with latency and memory cost, not pass count alone.
