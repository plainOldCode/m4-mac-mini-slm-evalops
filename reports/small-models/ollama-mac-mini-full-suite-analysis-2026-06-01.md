# Ollama Mac Mini Full-Suite Analysis - 2026-06-01

This pass expands beyond MLX and evaluates Mac-mini-realistic Ollama models with
the same operational lanes:

- 100-prompt multilingual/domain factual QA
- structured tool-calling plan selection
- OpenClaw native tool execution
- compiler-backed coding generation

Ollama JSON-mode was enabled for the structured JSON suites. `qwen3-coder:30b-a3b`
was intentionally excluded because it is outside the 16 GB M4 Mac mini comfort
zone for a full-suite run.

## Results

| Model | 100p Alias | 100p Strict | Tool Pass | Tool Seq | OpenClaw Native | Coding Pass | JSON/Schema |
| --- | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| `qwen2.5-coder:14b` | 94/100 | 82/100 | 9/12 | 11/12 | Fail | 4/5 | 5/5 |
| `qwen2.5-coder:7b` | 87/100 | 69/100 | 7/12 | 10/12 | Fail | 2/5 | 5/5 |
| `qwen3:4b` | 90/100 | 61/100 | 3/12 | 7/12 | Fail | 1/5 | 5/5 |
| `llama3.1:8b` | 88/100 | 45/100 | 6/12 | 8/12 | Fail | 0/5 | 4/5 |

## Readout

- `qwen2.5-coder:14b` is the best Ollama candidate in this queue. It leads 100
  prompt scoring, tool calling, and coding generation, but still fails native
  OpenClaw tool execution.
- `qwen2.5-coder:7b` is materially better under Ollama JSON-mode than the MLX 7B
  coding result, but it remains a mid-tier candidate rather than a quality
  worker.
- `qwen3:4b` remains strong as a lightweight factual/general baseline, but it is
  weak in structured tool-calling and only passes 1/5 coding tasks in this
  Ollama configuration.
- `llama3.1:8b` is broadly competent on factual prompts, but it is not useful as
  a coding worker here and is weaker than Qwen2.5-Coder on tool selection.
- OpenClaw native failure is not a download/runtime failure. The models produced
  text that looked like instructions or JSON-ish tool intent, but OpenClaw did
  not receive a valid structured tool invocation and no marker file was created.

## Decision

The non-MLX Ollama pass does not replace the current MLX recommendation:

- Quality coding worker remains `lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit`
  because it reached 5/5 on the compiler-backed suite.
- Lightweight always-on/OpenClaw candidate remains
  `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` because it has already
  passed the native OpenClaw tool execution canary.
- Ollama `qwen2.5-coder:14b` is a useful fallback/secondary coding worker when
  JSON-mode structured generation is acceptable, but not for native OpenClaw
  tool execution.

## Source Reports

- [100-prompt alias-normalized scoring](multilingual-domain-suite-ollama-mac-mini-alias-normalized-2026-06-01.md)
- [Tool-calling suite](tool-calling-suite-ollama-mac-mini-2026-06-01.md)
- [OpenClaw native tool execution](openclaw-native-tool-execution-ollama-mac-mini-2026-06-01.md)
- [Coding generation suite](coding-generation-role-language-ollama-mac-mini-2026-06-01.md)
