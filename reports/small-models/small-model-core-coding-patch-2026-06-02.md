# Small Model Core Suite

This suite evaluates public-safe summary, extraction, protocol, and patch tasks.

| Rank | Model | Lane | Pass | Content | Schema | JSON | Elapsed | Storage | Cache | Cleanup |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `lmstudio-community/Qwen2.5-Coder-7B-Instruct-MLX-8bit` | `coding_patch` | 1/1 | 1/1 | 1/1 | 1/1 | 706.144s | 8.1GB | 16.22GB | 0 |
| 2 | `mlx-community/Qwen2.5-Coder-14B-Instruct-4bit` | `coding_patch` | 1/1 | 1/1 | 1/1 | 1/1 | 720.078s | 8.31GB | 16.64GB | 0 |
| 3 | `lmstudio-community/Qwen2.5-Coder-1.5B-Instruct-MLX-8bit` | `coding_patch` | 0/1 | 0/1 | 1/1 | 1/1 | 146.197s | 1.65GB | 3.31GB | 0 |
| 4 | `lmstudio-community/Qwen2.5-Coder-1.5B-Instruct-MLX-4bit` | `coding_patch` | 0/1 | 0/1 | 1/1 | 1/1 | 79.786s | 0.88GB | 1.77GB | 0 |
| 5 | `lmstudio-community/Phi-4-reasoning-plus-MLX-4bit` | `coding_patch` | 0/1 | 0/1 | 0/1 | 0/1 | 811.441s | 8.25GB | 16.51GB | 0 |

## Notes

- `Pass` requires schema-valid JSON and deterministic content match.
- Reasoning cleanup is tracked through wrapper cleanup counts and per-case raw artifacts.
