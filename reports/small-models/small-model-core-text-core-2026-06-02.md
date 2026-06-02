# Small Model Core Suite

This suite evaluates public-safe summary, extraction, protocol, and patch tasks.

| Rank | Model | Lane | Pass | Content | Schema | JSON | Elapsed | Storage | Cache | Cleanup |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `Qwen/Qwen3-4B-MLX-4bit` | `text_core` | 2/4 | 2/4 | 4/4 | 4/4 | 231.827s | 2.15GB | 4.31GB | 4 |
| 2 | `lmstudio-community/Qwen3-8B-MLX-4bit` | `text_core` | 2/4 | 2/4 | 4/4 | 4/4 | 485.804s | 4.62GB | 9.25GB | 4 |
| 3 | `mlx-community/Qwen3-8B-4bit` | `text_core` | 2/4 | 2/4 | 4/4 | 4/4 | 482.078s | 4.62GB | 9.25GB | 4 |
| 4 | `lmstudio-community/Qwen3-4B-MLX-4bit` | `text_core` | 2/4 | 2/4 | 4/4 | 4/4 | 237.351s | 2.27GB | 4.56GB | 4 |
| 5 | `lmstudio-community/Qwen3-4B-MLX-8bit` | `text_core` | 2/4 | 2/4 | 4/4 | 4/4 | 471.234s | 4.29GB | 8.58GB | 4 |
| 6 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-8bit` | `text_core` | 1/4 | 1/4 | 4/4 | 4/4 | 395.053s | 4.29GB | 8.58GB | 0 |
| 7 | `lmstudio-community/Qwen3-14B-MLX-4bit` | `text_core` | 1/4 | 1/4 | 4/4 | 4/4 | 843.927s | 8.32GB | 16.65GB | 4 |
| 8 | `mlx-community/Qwen3-0.6B-4bit` | `text_core` | 1/4 | 1/4 | 3/4 | 3/4 | 46.009s | 0.68GB | 0.70GB | 3 |
| 9 | `lmstudio-community/LFM2.5-1.2B-Instruct-MLX-4bit` | `text_core` | 0/4 | 0/4 | 3/4 | 3/4 | 64.967s | 0.66GB | 1.33GB | 0 |
| 10 | `mlx-community/LFM2.5-1.2B-Instruct-4bit` | `text_core` | 0/4 | 0/4 | 3/4 | 3/4 | 65.166s | 0.66GB | 1.33GB | 0 |
| 11 | `lmstudio-community/LFM2-1.2B-MLX-8bit` | `text_core` | 0/4 | 0/4 | 3/4 | 3/4 | 118.951s | 1.24GB | 2.50GB | 0 |
| 12 | `mlx-community/Llama-3.2-1B-Instruct-4bit` | `text_core` | 0/4 | 0/4 | 2/4 | 4/4 | 72.309s | 1.41GB | 1.43GB | 0 |

## Notes

- `Pass` requires schema-valid JSON and deterministic content match.
- Reasoning cleanup is tracked through wrapper cleanup counts and per-case raw artifacts.
