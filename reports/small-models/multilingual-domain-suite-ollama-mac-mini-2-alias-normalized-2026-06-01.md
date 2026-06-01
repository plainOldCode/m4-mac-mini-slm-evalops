# Top 8 Alias-Normalized Multilingual Scoring

This report re-scores the existing multilingual/domain raw outputs without re-running models.
Aliases are conservative: notation and translated equivalents count, but acronym-only answers do not count for expansion prompts such as GDP and ETF.

| Rank | Model | Strict | Alias-normalized | Lift | JSON | Schema |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | `gemma3:12b` | 59/100 | 100/100 | +41 | 100/100 | 100/100 |
| 2 | `qwen3:8b` | 62/100 | 90/100 | +28 | 100/100 | 100/100 |
| 3 | `qwen2.5:14b` | 75/100 | 88/100 | +13 | 100/100 | 100/100 |
| 4 | `cogito:8b` | 44/100 | 87/100 | +43 | 100/100 | 100/100 |
| 5 | `deepseek-coder-v2:16b` | 41/100 | 86/100 | +45 | 100/100 | 100/100 |
| 6 | `granite3-dense:8b` | 57/100 | 83/100 | +26 | 100/100 | 100/100 |
| 7 | `phi4-mini` | 46/100 | 75/100 | +29 | 100/100 | 99/100 |
| 8 | `mistral-nemo:12b` | 50/100 | 73/100 | +23 | 100/100 | 100/100 |

## Notes

- This pass uses existing `parsed.json` artifacts and does not download or execute any model.
- `alias_source=canonical_answer` means the canonical field matched an alias.
- `alias_source=answer` means the localized answer was correct even when the canonical field was not.
