# Tool-Calling + 100-Prompt Composite - 2026-05-31

Composite score uses equal weight: 50% alias-normalized 100-prompt factual score and 50% tool-calling pass rate.
Tie-breakers: alias score, tool pass, tool sequence, strict canonical score.

| Rank | Model | Composite | 100p Alias | Tool Pass | Tool Seq | Strict | Schema |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `mlx-community/Qwen2.5-14B-Instruct-4bit` | 78.3 | 90/100 | 8/12 (66.7) | 10/12 | 82/100 | 99/100 |
| 2 | `prism-ml/Ternary-Bonsai-8B-mlx-2bit` | 77.3 | 88/100 | 8/12 (66.7) | 12/12 | 50/100 | 100/100 |
| 3 | `mlx-community/Mistral-7B-Instruct-v0.3-4bit` | 77.3 | 88/100 | 8/12 (66.7) | 10/12 | 59/100 | 100/100 |
| 4 | `mlx-community/Mistral-Nemo-Instruct-2407-4bit` | 76.5 | 78/100 | 9/12 (75.0) | 11/12 | 59/100 | 100/100 |
| 5 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` | 74.2 | 90/100 | 7/12 (58.3) | 9/12 | 53/100 | 100/100 |
| 6 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit` | 73.2 | 88/100 | 7/12 (58.3) | 10/12 | 55/100 | 100/100 |
| 7 | `mlx-community/Qwen3-4B-Instruct-2507-4bit` | 72.7 | 87/100 | 7/12 (58.3) | 10/12 | 54/100 | 100/100 |
| 8 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-6bit` | 72.2 | 86/100 | 7/12 (58.3) | 9/12 | 48/100 | 100/100 |
| 9 | `lmstudio-community/Qwen3-VL-4B-Instruct-MLX-4bit` | 70.7 | 83/100 | 7/12 (58.3) | 10/12 | 51/100 | 99/100 |
| 10 | `mlx-community/Qwen2.5-7B-Instruct-4bit` | 69.2 | 80/100 | 7/12 (58.3) | 9/12 | 48/100 | 100/100 |

## Readout

- `Qwen2.5-14B` is the quality leader: highest strict score and tied highest alias score, with strong tool-calling. Its weakness is weight on the M4 16GB box.
- `Ternary-Bonsai 8B 2bit` and `Mistral 7B` are effectively tied in the balanced score. Bonsai has perfect tool sequence selection; Mistral has stronger strict factual formatting.
- `Mistral-Nemo` remains the tool-calling leader, but its alias-normalized 100-prompt score is only 78/100, so it drops in the combined ranking.
- `Qwen3 4B 5bit` remains the practical lightweight balanced candidate: tied top alias score, perfect schema, and acceptable 7/12 tool-calling, but its tool pass rate keeps it below the 7B/8B/14B leaders in pure composite score.
