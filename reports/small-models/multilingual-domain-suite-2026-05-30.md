# Multilingual Domain Suite, 2026-05-30

This report summarizes the first full multilingual/domain benchmark loop for M4 Mac mini MLX candidates.

## Scope

- Hardware target: 16GB M4 Mac mini
- Candidate lane: text-capable MLX models selected from the local sweep
- Models tested: 20
- Prompts per model: 100
- Total raw generations: 2,000
- Languages: English, Korean, Japanese, Chinese, Spanish, Russian, French, German, Italian, Portuguese
- Domains: physics, biology, earth science, chemistry, math, coding, current affairs, economics, finance, logic
- Loop discipline: download -> prompt -> verify -> report -> delete attempt cache -> commit
- Raw artifacts: `runs/multilingual-domain-suite-2026-05-30/`
- Aggregate progress table: `runs/multilingual-domain-suite-2026-05-30/analysis.md`

Each model run stores the prompt, raw stdout/stderr, cleaned text, parsed JSON, and validation result under its own attempt directory. The Hugging Face / Transformers cache used for each attempt was deleted after that model completed.

## Results

| Rank | Model | Canonical Exact | Schema Valid | JSON Valid | Cleanup Used | Notes |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 1 | `mlx-community/Qwen2.5-14B-Instruct-4bit` | 82/100 | 99/100 | 99/100 | 0 | Best quality, but heavyweight for always-on Mac mini use. |
| 2 | `mlx-community/gemma-2-9b-it-4bit` | 73/100 | 100/100 | 100/100 | 0 | Strongest practical high-quality result below 14B. |
| 3 | `mlx-community/Mistral-7B-Instruct-v0.3-4bit` | 59/100 | 100/100 | 100/100 | 0 | Balanced candidate; good structure and acceptable factual coverage. |
| 4 | `mlx-community/Mistral-Nemo-Instruct-2407-4bit` | 59/100 | 100/100 | 100/100 | 0 | Ties Mistral 7B here, but is heavier. |
| 5 | `mlx-community/gemma-3n-E2B-it-lm-4bit` | 58/100 | 100/100 | 100/100 | 0 | Best small practical candidate in this run. |
| 6 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit` | 55/100 | 100/100 | 100/100 | 0 | Good 4B Qwen3 option. |
| 7 | `mlx-community/Qwen3-4B-Instruct-2507-4bit` | 54/100 | 100/100 | 100/100 | 0 | Similar to the LM Studio build. |
| 8 | `prism-ml/Ternary-Bonsai-8B-mlx-2bit` | 50/100 | 100/100 | 100/100 | 0 | Interesting low-bit candidate; quality trails top 7B/9B. |
| 9 | `mlx-community/Qwen2.5-7B-Instruct-4bit` | 48/100 | 100/100 | 100/100 | 0 | Stable structure, weaker factual exactness than expected. |
| 10 | `mlx-community/Meta-Llama-3.1-8B-Instruct-4bit` | 47/100 | 99/100 | 99/100 | 0 | Usable, but not top tier in this prompt pack. |
| 11 | `mlx-community/Qwen2-VL-2B-Instruct-4bit` | 35/100 | 78/100 | 90/100 | 0 | Text-capable, but should mainly remain in the VLM lane. |
| 12 | `mlx-community/Qwen2.5-1.5B-Instruct-4bit` | 33/100 | 100/100 | 100/100 | 0 | Good structure for size; limited knowledge precision. |
| 13 | `mlx-community/Qwen2.5-0.5B-Instruct-4bit` | 29/100 | 98/100 | 99/100 | 0 | Ultra-light schema-following candidate. |
| 14 | `lmstudio-community/Qwen2.5-0.5B-Instruct-MLX-4bit` | 29/100 | 98/100 | 99/100 | 0 | Similar to mlx-community 0.5B. |
| 15 | `mlx-community/Llama-3.2-3B-Instruct-4bit` | 29/100 | 98/100 | 98/100 | 0 | Stable structure, lower exactness. |
| 16 | `mlx-community/Qwen2.5-3B-Instruct-4bit` | 28/100 | 26/100 | 67/100 | 0 | Some correct answers, poor schema compliance. |
| 17 | `lmstudio-community/Qwen3-1.7B-MLX-4bit` | 17/100 | 28/100 | 28/100 | 28 | Think-cleanup helped parse outputs, but not enough for core QA. |
| 18 | `mlx-community/gemma-3-1b-it-qat-4bit` | 16/100 | 72/100 | 85/100 | 0 | Structure is partly usable; knowledge exactness is weak. |
| 19 | `mlx-community/gemma-3-1b-it-4bit` | 13/100 | 71/100 | 85/100 | 0 | Similar to QAT variant, slightly lower canonical exactness. |
| 20 | `mlx-community/Qwen3-1.7B-4bit` | 7/100 | 16/100 | 16/100 | 16 | Think-cleanup candidate, not a core multilingual QA fit. |

## Interpretation

The strongest overall model in this strict benchmark is `mlx-community/Qwen2.5-14B-Instruct-4bit`, but it is better treated as a high-quality batch/reference candidate rather than an always-on Mac mini backend. Download and runtime cost are meaningfully higher than the smaller candidates.

The most practical high-quality lane is `mlx-community/gemma-2-9b-it-4bit`, followed by `mlx-community/Mistral-7B-Instruct-v0.3-4bit`. `Mistral-Nemo-Instruct-2407-4bit` did not outperform Mistral 7B in this suite, so it needs a separate reason to justify its extra weight.

The most interesting small-model result is `mlx-community/gemma-3n-E2B-it-lm-4bit`: it reached 58/100 canonical exact with perfect schema compliance. That makes it a serious candidate for local routing where memory, download time, and responsiveness matter.

The Qwen3 4B builds are solid schema-following candidates around the mid-50s exact range. They remain useful for controlled local automation, especially where we can accept strict JSON output and post-process answers.

The Qwen3 1.7B think-cleanup candidates should not be described as failed. The better label is: not core-task candidates for this prompt suite. Their outputs need a different route, such as reasoning-signal extraction, answer cleanup, or constrained post-processing. The cleanup path worked technically, but the resulting factual exactness was not competitive here.

## Validator Caveats

`canonical_match_count` is intentionally strict. It checks normalized exact canonical answers, so it can undercount correct translated answers, reasonable aliases, and explanatory variants. This benchmark is useful for first-pass routing, not a final human-quality evaluation.

Next scoring improvements should add:

- Alias sets per task, including translated canonical answers.
- Numeric/formula normalization for chemistry, math, and finance.
- Separate scores for language fidelity, answer correctness, JSON discipline, and latency.
- A qualitative review pass for near-miss outputs using the raw artifacts.

## Routing Recommendations

- Best quality reference: `mlx-community/Qwen2.5-14B-Instruct-4bit`
- Best practical high-quality lane: `mlx-community/gemma-2-9b-it-4bit`
- Best balanced 7B lane: `mlx-community/Mistral-7B-Instruct-v0.3-4bit`
- Best small practical lane: `mlx-community/gemma-3n-E2B-it-lm-4bit`
- Best Qwen 4B lane: `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit` or `mlx-community/Qwen3-4B-Instruct-2507-4bit`
- Ultra-light schema-only lane: Qwen2.5 0.5B variants
- Think-cleanup research lane: Qwen3 1.7B variants

## Next Work

Completed follow-up: `scripts/score_alias_normalized_multilingual_suite.py` now re-scores the top 7 strict canonical models over the same raw outputs. The first alias-normalized report is `reports/small-models/multilingual-domain-suite-top7-alias-normalized-2026-05-31.md`.

Remaining next work: add separate language fidelity, correctness, JSON discipline, and latency dimensions before running another expensive full sweep.
