# Small Model Core Suite

This suite evaluates public-safe summary, extraction, protocol, and patch tasks.

| Rank | Model | Lane | Pass | Content | Schema | JSON | Elapsed | Storage | Cache | Cleanup |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `lmstudio-community/Qwen3-4B-Thinking-2507-MLX-8bit` | `reasoning_cleanup` | 2/7 | 2/7 | 3/7 | 3/7 | 677.638s | 4.29GB | 8.58GB | 0 |
| 2 | `lmstudio-community/DeepSeek-R1-0528-Qwen3-8B-MLX-4bit` | `reasoning_cleanup` | 1/7 | 1/7 | 4/7 | 4/7 | 643.403s | 4.62GB | 9.24GB | 5 |
| 3 | `lmstudio-community/LFM2.5-1.2B-Thinking-MLX-8bit` | `reasoning_cleanup` | 1/7 | 1/7 | 4/7 | 4/7 | 204.372s | 1.24GB | 2.50GB | 5 |
| 4 | `mlx-community/DeepSeek-R1-Distill-Qwen-14B-4bit` | `reasoning_cleanup` | 1/7 | 1/7 | 4/7 | 4/7 | 948.458s | 8.32GB | 16.64GB | 0 |
| 5 | `mlx-community/DeepSeek-R1-Distill-Qwen-7B-4bit` | `reasoning_cleanup` | 0/7 | 0/7 | 4/7 | 4/7 | 534.253s | 8.58GB | 8.59GB | 0 |
| 6 | `lmstudio-community/Qwen3-4B-Thinking-2507-MLX-4bit` | `reasoning_cleanup` | 0/7 | 0/7 | 2/7 | 2/7 | 406.477s | 2.27GB | 4.56GB | 0 |
| 7 | `mlx-community/DeepSeek-R1-Distill-Qwen-1.5B-4bit` | `reasoning_cleanup` | 0/7 | 0/7 | 2/7 | 4/7 | 146.329s | 2.01GB | 2.02GB | 0 |

## Notes

- `Pass` requires schema-valid JSON and deterministic content match.
- Reasoning cleanup is tracked through wrapper cleanup counts and per-case raw artifacts.
