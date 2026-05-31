# M4 Mac Mini Small Model Initial Comparison - 2026-05-30

This is a portfolio-safe summary of the small-model layer for the current M4
Mac mini benchmark project.

| Backend | Label | Demo Status | Interpretation |
| --- | --- | --- | --- |
| `noop` | baseline | fails | Detects no-op behavior and failed tests. |
| `qwen25-coder-trace` | bounded local TDD worker | passes demo | Represents a conservative function-level patch candidate. |
| `sushi-coder-trace` | candidate artifact worker | passes demo | Represents extraction-assisted candidate generation under harness ownership. |
| `qwen25-coder-mlx` | live bounded local TDD worker | timeout in first smoke | Calls a local MLX Qwen2.5-Coder model; naive 300s run timed out on the current Mac mini. |
| `sushi-coder-mlx` | live candidate artifact worker | generated failing patch | Calls a local MLX Sushi-Coder model; first smoke produced a real patch but missed an edge case. |
| `lfm25-8b-a1b-mlx-4bit` | general local instruction candidate | generation smoke diagnostic | Loaded and generated, but first prompt/template smoke produced verbose thinking or repetition rather than clean answers. |
| `lfm25-controlled-mlx` | controlled reasoning-to-patch backend | passes demo | Uses LFM2.5 output as a semantic signal, then applies bounded deterministic post-processing for the demo task. |

The trace backends are deterministic placeholders. They make the evaluation
surface visible before live MLX/Ollama adapters are connected.

## Current M4 Mac Mini Read

- `sushi-coder-mlx` is the best first live signal: it loads, generates a patch,
  and reaches deterministic test feedback, even though its first patch failed.
- `qwen25-coder-mlx` is too slow in the naive live adapter on this machine; keep
  it as a trace or future larger-machine candidate until prompt/runtime tuning
  improves.
- `lfm25-controlled-mlx` is not a clean general answer backend, but it is useful
  as a controlled semantic-signal experiment.
- The benchmark should measure quality, protocol discipline, and runtime
  separately. A single pass/fail score hides the useful diagnostic signal.

See `reports/small-models/live-mlx-smoke-2026-05-30.md` for the first live
adapter smoke results.

See `reports/small-models/lfm25-mlx-smoke-2026-05-30.md` for the LFM2.5
generation smoke.
