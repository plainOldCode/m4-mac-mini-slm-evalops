# MLX Coding SLM Smoke Analysis

Run date: 2026-06-01

Candidate source: `data/benchmark/coding-generation-mlx-coder-slm-candidates-2026-06-01.json`

Raw results:
- JSON: `reports/small-models/coding-generation-mlx-coder-slm-2026-06-01.json`
- Markdown: `reports/small-models/coding-generation-mlx-coder-slm-2026-06-01.md`
- Run artifacts: `runs/coding-generation-mlx-coder-slm-2026-06-01`

## Summary

The first MLX coding SLM sweep did not beat the general-purpose lightweight baseline from the earlier smoke run. The best coding-specific SLMs only reached 1/3 on the v1 smoke suite, while `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` previously reached 2/3 and both GPT comparison models reached 3/3.

This result is mostly about end-to-end coding-agent reliability, not raw coding knowledge. The benchmark requires the model to obey a strict JSON file-edit protocol, modify only allowed paths, and satisfy deterministic tests. Several coding models failed before their code quality could be measured because they did not return parseable JSON or could not run cleanly through the MLX backend.

## Leaderboard

| Rank | Model | Pass | Protocol | Practical Read |
| ---: | --- | ---: | --- | --- |
| 1 | `mlx-community/Qwen2.5-Coder-3B-Instruct-4bit` | 1/3 | JSON/schema 3/3 | Best small coding SLM in this sweep; passed Python, failed JS numeric types and HTML structure. |
| 2 | `lmstudio-community/Qwen2.5-Coder-7B-Instruct-MLX-4bit` | 1/3 | JSON 3/3, schema 2/3 | Passed HTML/CSS, but was much slower and failed Python schema plus JS logic. |
| 3 | `mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit` | 0/3 | JSON/schema 3/3 | Good protocol compliance for its size, but code quality was not enough. |
| 4 | `mlx-community/starcoder2-3b-4bit` | 0/3 | JSON 0/3 | Generated without runtime failure, but did not follow the JSON edit contract. |
| 5 | `mlx-community/deepseek-coder-1.3b-instruct-mlx` | 0/3 | JSON 0/3 | MLX generation failed for all tasks. |
| 6 | `mlx-community/deepseek-coder-6.7b-instruct-hf-4bit-mlx` | 0/3 | JSON 0/3 | MLX generation failed for all tasks. |

## Model Notes

### Qwen2.5-Coder 3B

Best candidate among the MLX coding SLM set. It returned valid JSON and valid schema for every task, changed the intended files, and passed the Python normalization task. Its JS solution computed the right values but returned formatted strings instead of numbers. Its HTML/CSS answer was close enough to modify the component, but missed the expected card structure.

Use this as the first local coding SLM candidate if the goal is a small model that can participate in an edit-test loop.

### Qwen2.5-Coder 7B

It tied the 3B model on pass count but was much less attractive operationally. It took 417.937s versus 170.239s for the 3B model, failed the Python task at the schema/edit-contract layer, and produced broken JS metrics. The one clear win was HTML/CSS.

This specific LM Studio MLX quant is not worth promoting over Qwen2.5-Coder 3B based on this run. A separate `mlx-community` 7B quant may still deserve a follow-up run.

### Qwen2.5-Coder 1.5B

The 1.5B model is useful as a protocol baseline: it followed JSON/schema/edit rules across all three tasks. It failed the actual tests, though, including a Python edge case, JS profit calculations, and the HTML/CSS structure checks.

This is too weak for coding generation, but it may still be useful for cheap code classification, routing, or small deterministic transformations with a repair loop.

### StarCoder2 3B

The run completed, but every output failed JSON parsing. The stderr also included tokenizer/config warnings around BOS/EOS ids. This model may need a model-specific prompt/template path before it can be fairly judged as an edit agent.

Do not spend more benchmark time here unless the next experiment is specifically about adapting the prompt/template.

### DeepSeek Coder 1.3B and 6.7B

Both DeepSeek MLX candidates failed generation for every task. Since no JSON output was produced, this run says more about MLX compatibility/runtime behavior than coding quality.

Exclude these exact MLX repos from the next coding-agent loop unless the runtime issue is fixed first.

## Comparison To Existing Smoke Results

| Model | Backend | Pass |
| --- | --- | ---: |
| `gpt-5.5` | codex-cli | 3/3 |
| `gpt-5.4-mini` | codex-cli | 3/3 |
| `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` | mlx | 2/3 |
| `mlx-community/Qwen2.5-Coder-3B-Instruct-4bit` | mlx | 1/3 |
| `lmstudio-community/Qwen2.5-Coder-7B-Instruct-MLX-4bit` | mlx | 1/3 |

The surprising result is that the general Qwen3 4B instruct model remains stronger than this first batch of coding-specialized SLMs for the current agent-style benchmark. For this harness, instruction following and structured edit reliability matter as much as coding specialization.

## Recommendation

For the current M4 Mac mini SLM EvalOps path:

1. Keep `Qwen3-4B-Instruct-2507-MLX-5bit` as the practical lightweight baseline.
2. Add `Qwen2.5-Coder-3B-Instruct-4bit` as the best small coding-specialized challenger.
3. Do not promote the LM Studio Qwen2.5-Coder 7B quant yet; it is slower and did not outperform 3B.
4. Drop the two DeepSeek MLX candidates from this loop until MLX generation compatibility is resolved.
5. Treat StarCoder2 as a separate prompt/template experiment, not a ready benchmark candidate.

Next useful benchmark step: run a v1.5 polyglot suite against only the viable candidates (`Qwen3-4B`, `Qwen2.5-Coder-3B`, optionally a different Qwen2.5-Coder 7B quant) before expanding to React/Vue frontend generation.

## Cache Cleanup

The loop deleted model caches after each candidate. Verification command found no remaining `model-cache` directories under `runs/coding-generation-mlx-coder-slm-2026-06-01`.
