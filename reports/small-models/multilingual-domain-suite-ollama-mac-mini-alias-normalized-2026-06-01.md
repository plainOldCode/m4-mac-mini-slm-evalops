# Top 4 Alias-Normalized Multilingual Scoring

This report re-scores the existing multilingual/domain raw outputs without re-running models.
Aliases are conservative: notation and translated equivalents count, but acronym-only answers do not count for expansion prompts such as GDP and ETF.

| Rank | Model | Strict | Alias-normalized | Lift | JSON | Schema |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | `qwen2.5-coder:14b` | 82/100 | 94/100 | +12 | 100/100 | 100/100 |
| 2 | `qwen3:4b` | 61/100 | 90/100 | +29 | 100/100 | 100/100 |
| 3 | `llama3.1:8b` | 45/100 | 88/100 | +43 | 100/100 | 99/100 |
| 4 | `qwen2.5-coder:7b` | 69/100 | 87/100 | +18 | 100/100 | 100/100 |

## Notes

- This pass uses existing `parsed.json` artifacts and does not download or execute any model.
- `alias_source=canonical_answer` means the canonical field matched an alias.
- `alias_source=answer` means the localized answer was correct even when the canonical field was not.
