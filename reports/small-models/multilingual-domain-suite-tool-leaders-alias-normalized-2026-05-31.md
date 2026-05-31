# Top 10 Alias-Normalized Multilingual Scoring

This report re-scores the existing multilingual/domain raw outputs without re-running models.
Aliases are conservative: notation and translated equivalents count, but acronym-only answers do not count for expansion prompts such as GDP and ETF.

| Rank | Model | Strict | Alias-normalized | Lift | JSON | Schema |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | `mlx-community/Qwen2.5-14B-Instruct-4bit` | 82/100 | 90/100 | +8 | 99/100 | 99/100 |
| 2 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` | 53/100 | 90/100 | +37 | 100/100 | 100/100 |
| 3 | `mlx-community/Mistral-7B-Instruct-v0.3-4bit` | 59/100 | 88/100 | +29 | 100/100 | 100/100 |
| 4 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit` | 55/100 | 88/100 | +33 | 100/100 | 100/100 |
| 5 | `prism-ml/Ternary-Bonsai-8B-mlx-2bit` | 50/100 | 88/100 | +38 | 100/100 | 100/100 |
| 6 | `mlx-community/Qwen3-4B-Instruct-2507-4bit` | 54/100 | 87/100 | +33 | 100/100 | 100/100 |
| 7 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-6bit` | 48/100 | 86/100 | +38 | 100/100 | 100/100 |
| 8 | `lmstudio-community/Qwen3-VL-4B-Instruct-MLX-4bit` | 51/100 | 83/100 | +32 | 99/100 | 99/100 |
| 9 | `mlx-community/Qwen2.5-7B-Instruct-4bit` | 48/100 | 80/100 | +32 | 100/100 | 100/100 |
| 10 | `mlx-community/Mistral-Nemo-Instruct-2407-4bit` | 59/100 | 78/100 | +19 | 100/100 | 100/100 |

## Notes

- This pass uses existing `parsed.json` artifacts and does not download or execute any model.
- `alias_source=canonical_answer` means the canonical field matched an alias.
- `alias_source=answer` means the localized answer was correct even when the canonical field was not.
