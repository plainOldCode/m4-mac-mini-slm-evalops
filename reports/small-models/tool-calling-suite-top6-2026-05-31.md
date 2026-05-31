# Tool Calling Suite Top 6 - 2026-05-31

This suite evaluates whether local MLX models can select tools and extract arguments.
No tools are executed. The model must emit a structured JSON tool plan.

| Rank | Model | Pass | Sequence | Args | Schema | JSON | Cleanup |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `lmstudio-community/Qwen3-VL-4B-Instruct-MLX-4bit` | 7/12 | 10/12 | 8/12 | 11/12 | 11/12 | 0 |
| 2 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` | 7/12 | 9/12 | 8/12 | 11/12 | 11/12 | 0 |
| 3 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-6bit` | 7/12 | 9/12 | 8/12 | 11/12 | 11/12 | 0 |
| 4 | `mlx-community/gemma-3n-E2B-it-lm-4bit` | 6/12 | 10/12 | 7/12 | 11/12 | 11/12 | 0 |
| 5 | `mlx-community/Phi-4-mini-instruct-4bit` | 6/12 | 8/12 | 6/12 | 10/12 | 10/12 | 0 |
| 6 | `lmstudio-community/LFM2.5-1.2B-Instruct-MLX-8bit` | 5/12 | 8/12 | 6/12 | 11/12 | 12/12 | 0 |

## Notes

- `Pass` requires schema, ordered tool sequence, required argument subset, and no extra calls.
- The safety case expects no tool call for an externally consequential email request.
