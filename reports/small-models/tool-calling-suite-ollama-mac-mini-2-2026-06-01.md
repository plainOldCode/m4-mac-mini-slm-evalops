# Tool Calling Suite Top 6 - 2026-05-31

This suite evaluates whether local MLX models can select tools and extract arguments.
No tools are executed. The model must emit a structured JSON tool plan.

| Rank | Model | Pass | Sequence | Args | Schema | JSON | Cleanup |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `cogito:8b` | 10/12 | 11/12 | 10/12 | 12/12 | 12/12 | 0 |
| 2 | `gemma3:12b` | 9/12 | 12/12 | 9/12 | 12/12 | 12/12 | 0 |
| 3 | `mistral-nemo:12b` | 9/12 | 11/12 | 9/12 | 12/12 | 12/12 | 0 |
| 4 | `qwen2.5:14b` | 9/12 | 10/12 | 9/12 | 12/12 | 12/12 | 0 |
| 5 | `qwen3:8b` | 9/12 | 10/12 | 9/12 | 12/12 | 12/12 | 0 |
| 6 | `phi4-mini` | 7/12 | 11/12 | 7/12 | 12/12 | 12/12 | 0 |
| 7 | `deepseek-coder-v2:16b` | 6/12 | 9/12 | 7/12 | 11/12 | 12/12 | 0 |
| 8 | `granite3-dense:8b` | 6/12 | 8/12 | 6/12 | 12/12 | 12/12 | 0 |

## Notes

- `Pass` requires schema, ordered tool sequence, required argument subset, and no extra calls.
- The safety case expects no tool call for an externally consequential email request.
