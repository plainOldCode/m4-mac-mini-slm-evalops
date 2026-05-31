# Candidate Sweep v2 Progress - 2026-05-30

M4 Mac mini MLX candidate sweep. Download and eval timing are separated. Model cache is deleted after each attempt.

- Completed candidates: 49
- Direct core task candidates: 18
- Core task candidates after cleanup adapter: 2
- Total core-lane candidates: 20
- Non-core / reroute cases: 29

| # | Model | Params | Download s | Eval s | JSON | Schema | Think | Routing label |
| ---: | --- | ---: | ---: | ---: | --- | --- | --- | --- |
| 1 | `lmstudio-community/DeepSeek-R1-0528-Qwen3-8B-MLX-4bit` | 8B | 400.690 | 7.301 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 2 | `lmstudio-community/LFM2.5-1.2B-Instruct-MLX-4bit` | 1.2B | 57.900 | 1.241 | true | false | false | `partial_schema_candidate` |
| 3 | `Qwen/Qwen3-4B-MLX-4bit` | 4B | 186.834 | 4.197 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 4 | `lmstudio-community/Qwen3-4B-Thinking-2507-MLX-4bit` | 4B | 195.204 | 4.425 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 5 | `mlx-community/Llama-3.2-1B-Instruct-4bit` | 1B | 61.678 | 1.665 | true | false | false | `partial_schema_candidate` |
| 6 | `mlx-community/gemma-3-1b-it-qat-4bit` | 1B | 64.639 | 2.290 | true | true | false | `candidate_for_core_tasks` |
| 7 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit` | 4B | 194.327 | 2.749 | true | true | false | `candidate_for_core_tasks` |
| 8 | `lmstudio-community/Qwen3-14B-MLX-4bit` | 14B | 700.254 | 14.434 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 9 | `lmstudio-community/Qwen3-8B-MLX-4bit` | 8B | 388.512 | 7.197 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 10 | `mlx-community/Josiefied-Qwen3-8B-abliterated-v1-4bit` | 8B | 391.447 | 6.968 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 11 | `lmstudio-community/Qwen3-1.7B-MLX-4bit` | 1.7B | 85.727 | 2.032 | true | true | true | `candidate_for_core_tasks_after_cleanup` |
| 12 | `mlx-community/Qwen3-1.7B-4bit` | 1.7B | 83.981 | 2.035 | true | true | true | `candidate_for_core_tasks_after_cleanup` |
| 13 | `mlx-community/LFM2.5-1.2B-Instruct-4bit` | 1.2B | 57.836 | 1.259 | true | false | false | `partial_schema_candidate` |
| 14 | `mlx-community/Llama-3.2-3B-Instruct-4bit` | 3B | 157.509 | 2.159 | true | true | false | `candidate_for_core_tasks` |
| 15 | `mlx-community/gemma-2-9b-it-4bit` | 9B | 455.045 | 5.582 | true | true | false | `candidate_for_core_tasks` |
| 16 | `lmstudio-community/Qwen3-4B-MLX-4bit` | 4B | 192.357 | 4.366 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 17 | `mlx-community/Qwen3-8B-4bit` | 8B | 387.218 | 6.976 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 18 | `mlx-community/Qwen3-0.6B-4bit` | 0.6B | 30.483 | 1.733 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 19 | `mlx-community/Qwen3-4B-Instruct-2507-4bit` | 4B | 212.036 | 2.752 | true | true | false | `candidate_for_core_tasks` |
| 20 | `mlx-community/Qwen2-VL-7B-Instruct-4bit` | 7B | 405.326 | 4.186 | true | true | false | `candidate_for_core_tasks` |
| 21 | `mlx-community/Qwen3-Embedding-0.6B-4bit-DWQ` | 0.6B | 30.701 | 1.752 | false | false | false | `non_core_unstructured_output` |
| 22 | `mlx-community/Qwen3.5-4B-4bit` | 4B | 253.909 | 5.076 | true | false | false | `partial_schema_candidate` |
| 23 | `mlx-community/Qwen2.5-3B-Instruct-4bit` | 3B | 151.330 | 2.475 | true | true | false | `candidate_for_core_tasks` |
| 24 | `mlx-community/Qwen2.5-0.5B-Instruct-4bit` | 0.5B | 27.098 | 1.389 | true | true | false | `candidate_for_core_tasks` |
| 25 | `mlx-community/Qwen2.5-7B-Instruct-4bit` | 7B | 371.538 | 3.242 | true | true | false | `candidate_for_core_tasks` |
| 26 | `mlx-community/Qwen3-4B-4bit` | 4B | 192.785 | 4.351 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 27 | `lmstudio-community/Qwen2.5-0.5B-Instruct-MLX-4bit` | 0.5B | 26.567 | 1.431 | true | true | false | `candidate_for_core_tasks` |
| 28 | `mlx-community/Mistral-7B-Instruct-v0.3-4bit` | 7B | 361.302 | 3.736 | true | true | false | `candidate_for_core_tasks` |
| 29 | `mlx-community/Qwen1.5-0.5B-Chat-4bit` | 0.5B | 25.098 | 1.554 | false | false | false | `non_core_unstructured_output` |
| 30 | `mlx-community/Meta-Llama-3.1-8B-Instruct-4bit` | 8B | 393.561 | 4.328 | true | true | false | `candidate_for_core_tasks` |
| 31 | `prism-ml/Ternary-Bonsai-8B-mlx-2bit` | 8B | 201.024 | 3.081 | true | true | false | `candidate_for_core_tasks` |
| 32 | `mlx-community/Qwen2.5-1.5B-Instruct-4bit` | 1.5B | 78.715 | 1.691 | true | true | false | `candidate_for_core_tasks` |
| 33 | `argmaxinc/mlx-FLUX.1-schnell-4bit-quantized` |  | 607.854 | 0.926 | false | false | false | `task_type_or_runtime_mismatch` |
| 34 | `Jackrong/MLX-Qwen3.5-9B-DeepSeek-V4-Flash-4bit` | 9B | 430.663 | 7.862 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 35 | `mlx-community/gemma-3-1b-it-4bit` | 1B | 63.865 | 2.166 | true | true | false | `candidate_for_core_tasks` |
| 36 | `mlx-community/Qwen2.5-14B-Instruct-4bit` | 14B | 711.810 | 8.553 | true | true | false | `candidate_for_core_tasks` |
| 37 | `mlx-community/Meta-Llama-3-8B-Instruct-4bit` | 8B | 456.475 | 7.184 | false | false | false | `non_core_unstructured_output` |
| 38 | `mlx-community/Qwen3.5-4B-OptiQ-4bit` | 4B | 288.240 | 6.202 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 39 | `mlx-community/gemma-3n-E2B-it-lm-4bit` | 2B | 222.261 | 3.499 | true | true | false | `candidate_for_core_tasks` |
| 40 | `mlx-community/Mistral-Nemo-Instruct-2407-4bit` |  | 603.745 | 5.951 | true | true | false | `candidate_for_core_tasks` |
| 41 | `mlx-community/Qwen3.5-0.8B-OptiQ-4bit` | 0.8B | 62.667 | 2.994 | true | false | true | `partial_schema_candidate` |
| 42 | `Jackrong/MLX-Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-4bit` | 9B | 431.684 | 7.819 | false | false | false | `non_core_unstructured_output` |
| 43 | `lmstudio-community/Qwen3-0.6B-MLX-4bit` | 0.6B | 30.801 | 1.760 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 44 | `Jackrong/MLX-Qwopus3.5-9B-v3-4bit` | 9B | 433.515 | 7.827 | false | false | false | `non_core_unstructured_output` |
| 45 | `mlx-community/Qwen3.5-2B-OptiQ-4bit` | 2B | 137.585 | 3.873 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 46 | `mlx-community/Qwen2-VL-2B-Instruct-4bit` | 2B | 109.873 | 1.924 | true | true | false | `candidate_for_core_tasks` |
| 47 | `mlx-community/DeepSeek-R1-Distill-Qwen-1.5B-4bit` | 1.5B | 89.938 | 2.500 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 48 | `Qwen/Qwen3-8B-MLX-4bit` | 8B | 382.398 | 6.634 | false | false | true | `reasoning_lane_protocol_mismatch` |
| 49 | `mlx-community/Qwen3-Embedding-4B-4bit-DWQ` | 4B | 194.895 | 4.506 | false | false | false | `non_core_unstructured_output` |

## Interpretation Note

These labels are routing labels, not absolute model grades. The sweep used a strict direct-output task: one Korean JSON object, no prose. A model that emits reasoning, special tokens, repeated analysis, or non-text-generation artifacts may still be useful in another lane, such as reasoning-first analysis, two-pass extraction, stop-token cleanup, embedding retrieval, VLM, or image generation.

The cleanup adapter was verified after the initial sweep on `lmstudio-community/Qwen3-1.7B-MLX-4bit` and `mlx-community/Qwen3-1.7B-4bit`. Both emit an empty `<think></think>` wrapper followed by valid schema JSON. Removing that empty wrapper promotes both to `candidate_for_core_tasks_after_cleanup`.

## Current Read

- Best lightweight candidate so far: `mlx-community/gemma-3-1b-it-qat-4bit`.
- Best clean Qwen text candidates so far: `Qwen3-4B-Instruct-2507` and `Qwen2.5-Instruct` 3B/7B.
- Best Qwen cleanup candidates so far: Qwen3 1.7B variants from `lmstudio-community` and `mlx-community`.
- Strong non-Qwen candidates now include `mlx-community/Meta-Llama-3.1-8B-Instruct-4bit`, `mlx-community/Mistral-7B-Instruct-v0.3-4bit`, and `mlx-community/gemma-2-9b-it-4bit`.
- `prism-ml/Ternary-Bonsai-8B-mlx-2bit` is an important low-storage 8B candidate: clean JSON, bullish sentiment, and fast eval after a smaller download footprint than many 7B/8B 4bit models.
- `mlx-community/gemma-3-1b-it-4bit` passes schema but produced a weak summary; keep `gemma-3-1b-it-qat-4bit` ahead of it.
- `mlx-community/Qwen2.5-14B-Instruct-4bit` is quality-good but too heavy for a Mac mini primary backend; keep Qwen2.5 3B/7B ahead on efficiency.
- `mlx-community/Meta-Llama-3-8B-Instruct-4bit` produced good JSON content but repeated it with Llama special tokens, so `Meta-Llama-3.1-8B-Instruct-4bit` is the better Llama lane candidate.
- `mlx-community/gemma-3n-E2B-it-lm-4bit` is a strong 2B Gemma candidate.
- `mlx-community/Mistral-Nemo-Instruct-2407-4bit` passes structured output but answers in English for a Korean input, so it needs language-preservation testing.
- Qwen3.5 OptiQ variants tested at 0.8B, 2B, and 4B all leak reasoning under this direct-JSON harness; route them to a reasoning/scratchpad lane before judging usefulness.
- Jackrong Qwen3.5/Qwopus reasoning-style 9B variants produce analysis prose instead of direct JSON; classify them as non-core direct-output candidates, not bad models.
- `mlx-community/Qwen2-VL-2B-Instruct-4bit` is a strong lightweight VLM/text candidate and is more Mac-mini-practical than the 7B VLM variant for text-only structured extraction.
- DeepSeek R1 distill and Qwen3 base variants continue to expose reasoning, even at small sizes and across official/community distributions; they need a different harness contract.
- Qwen3 base variants generally understand the text but do not fit the current strict direct-JSON task without stop-token/template/post-processing work.
- Qwen3 1.7B variants from both `lmstudio-community` and `mlx-community` emit valid schema after an empty `<think></think>` wrapper and are usable with the cleanup adapter.
- Qwen2.5 0.5B variants are extremely fast and schema-valid, but sentiment quality was weak in this smoke.
- Qwen1.5 0.5B Chat is fast but repeats unstructured Korean text, so it is not a core direct-structured-output candidate.
- Embedding, image generation, and other non-text-generation models should be moved to separate benchmark lanes instead of being judged by the text-generation sweep.
- Priority/edge generation sweep reached the initial full set of 49 candidates on 2026-05-30.
