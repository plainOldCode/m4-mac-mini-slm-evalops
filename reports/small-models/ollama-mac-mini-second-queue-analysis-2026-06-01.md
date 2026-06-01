# Ollama Mac Mini Second-Queue Analysis - 2026-06-01

This pass expands the non-MLX/Ollama queue after the first four-model smoke.
Each model was run through:

- 100-prompt multilingual/domain factual QA
- structured tool-calling plan selection
- OpenClaw native tool execution
- compiler-backed coding generation

Ollama JSON-mode was enabled for the structured JSON suites. Models were removed
from the local Ollama cache after their run.

## Results

| Model | 100p Alias | 100p Strict | Tool Pass | Tool Seq | OpenClaw Native | Coding Pass | JSON/Schema |
| --- | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| `gemma3:12b` | 100/100 | 59/100 | 9/12 | 12/12 | Fail | 2/5 | 5/5 |
| `qwen3:8b` | 90/100 | 62/100 | 9/12 | 10/12 | Fail | 3/5 | 5/5 |
| `qwen2.5:14b` | 88/100 | 75/100 | 9/12 | 10/12 | Fail | 2/5 | 5/5 JSON, 3/5 schema |
| `cogito:8b` | 87/100 | 44/100 | 10/12 | 11/12 | Fail | 2/5 | 5/5 |
| `deepseek-coder-v2:16b` | 86/100 | 41/100 | 6/12 | 9/12 | Fail | 2/5 | 5/5 |
| `granite3-dense:8b` | 83/100 | 57/100 | 6/12 | 8/12 | Fail | 0/5 | 5/5 |
| `phi4-mini` | 75/100 | 46/100 | 7/12 | 11/12 | Fail | 1/5 | 5/5 |
| `mistral-nemo:12b` | 73/100 | 50/100 | 9/12 | 11/12 | Fail | 1/5 | 5/5 |

## Readout

- `gemma3:12b` is the strongest factual/tool-plan surprise. It reached 100/100
  alias-normalized factual scoring and perfect 12/12 tool sequence selection,
  but coding remains only 2/5.
- `qwen3:8b` is the best balanced 8B candidate in this queue. It keeps a strong
  90/100 factual score, reaches 9/12 tool calling, and improves coding to 3/5.
- `cogito:8b` is the strongest structured tool planner in the second queue at
  10/12, but factual strict scoring and coding are weaker.
- `qwen2.5:14b` is a strong general 14B model, but it does not beat
  `qwen2.5-coder:14b` from the first Ollama pass.
- `mistral-nemo:12b` confirms its tool-planning strength, but it is not a
  balanced factual/coding candidate in this harness.
- `deepseek-coder-v2:16b` runs on the Mac mini, but does not justify its size:
  coding is only 2/5 and factual/tool results are mid-pack.
- `granite3-dense:8b` and `phi4-mini` follow the protocol but are not leaders in
  any lane.
- No second-queue Ollama model passed OpenClaw native tool execution. The
  distinction remains important: JSON-mode tool plans can be good while native
  structured tool invocation still fails.

## Decision

Second-queue winners by role:

- Factual/tool-plan candidate: `gemma3:12b`
- Balanced 8B candidate: `qwen3:8b`
- Structured tool planner: `cogito:8b`
- Coding worker: no replacement for existing leaders

Overall operating recommendation remains unchanged:

- Quality coding worker: `lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit`
- Lightweight/OpenClaw candidate: `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit`
- Ollama JSON-mode fallback coding worker: `qwen2.5-coder:14b`

## Source Reports

- [Second-queue 100-prompt factual scoring](multilingual-domain-suite-ollama-mac-mini-2-alias-normalized-2026-06-01.md)
- [Second-queue tool calling](tool-calling-suite-ollama-mac-mini-2-2026-06-01.md)
- [Second-queue OpenClaw native tool execution](openclaw-native-tool-execution-ollama-mac-mini-2-2026-06-01.md)
- [Second-queue coding generation](coding-generation-role-language-ollama-mac-mini-2-2026-06-01.md)
