# Top 7 Alias-Normalized Multilingual Scoring

This report re-scores the existing multilingual/domain raw outputs without re-running models.
Aliases are conservative: notation and translated equivalents count, but acronym-only answers do not count for expansion prompts such as GDP and ETF.

| Rank | Model | Strict | Alias-normalized | Lift | JSON | Schema |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` | 53/100 | 90/100 | +37 | 100/100 | 100/100 |
| 2 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-6bit` | 48/100 | 86/100 | +38 | 100/100 | 100/100 |
| 3 | `lmstudio-community/Qwen3-VL-4B-Instruct-MLX-4bit` | 51/100 | 83/100 | +32 | 99/100 | 99/100 |
| 4 | `mlx-community/Phi-4-mini-instruct-4bit` | 39/100 | 76/100 | +37 | 97/100 | 97/100 |
| 5 | `lmstudio-community/LFM2.5-1.2B-Instruct-MLX-8bit` | 61/100 | 75/100 | +14 | 98/100 | 98/100 |
| 6 | `lmstudio-community/LFM2.5-1.2B-Instruct-MLX-6bit` | 47/100 | 56/100 | +9 | 78/100 | 78/100 |
| 7 | `lmstudio-community/Qwen3-1.7B-MLX-8bit` | 14/100 | 15/100 | +1 | 15/100 | 15/100 |
| 8 | `lmstudio-community/Phi-4-mini-reasoning-MLX-4bit` | 4/100 | 9/100 | +5 | 10/100 | 10/100 |
| 9 | `mlx-community/Qwen3.5-9B-MLX-4bit` | 2/100 | 2/100 | +0 | 94/100 | 2/100 |
| 10 | `lmstudio-community/Qwen3-4B-Thinking-2507-MLX-6bit` | 0/100 | 0/100 | +0 | 3/100 | 0/100 |
| 11 | `mlx-community/gemma-4-e2b-it-4bit` | 0/100 | 0/100 | +0 | 0/100 | 0/100 |
| 12 | `mlx-community/gemma-4-e4b-it-4bit` | 0/100 | 0/100 | +0 | 0/100 | 0/100 |
| 13 | `aufklarer/Qwen3-ASR-0.6B-MLX-4bit` | 0/100 | 0/100 | +0 | 0/100 | 0/100 |
| 14 | `lmstudio-community/GLM-4.6V-Flash-MLX-4bit` | 0/100 | 0/100 | +0 | 0/100 | 0/100 |

## Notes

- This pass uses existing `parsed.json` artifacts and does not download or execute any model.
- `alias_source=canonical_answer` means the canonical field matched an alias.
- `alias_source=answer` means the localized answer was correct even when the canonical field was not.
