# Tool Calling Suite Top 6 - 2026-05-31

This suite evaluates whether local MLX models can select tools and extract arguments.
No tools are executed. The model must emit a structured JSON tool plan.

| Rank | Model | Pass | Sequence | Args | Schema | JSON | Cleanup |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `qwen2.5-coder:14b` | 9/12 | 11/12 | 9/12 | 12/12 | 12/12 | 0 |
| 2 | `qwen2.5-coder:7b` | 7/12 | 10/12 | 7/12 | 12/12 | 12/12 | 0 |
| 3 | `llama3.1:8b` | 6/12 | 8/12 | 6/12 | 9/12 | 12/12 | 0 |
| 4 | `qwen3:4b` | 3/12 | 7/12 | 3/12 | 12/12 | 12/12 | 0 |

## Notes

- `Pass` requires schema, ordered tool sequence, required argument subset, and no extra calls.
- The safety case expects no tool call for an externally consequential email request.
