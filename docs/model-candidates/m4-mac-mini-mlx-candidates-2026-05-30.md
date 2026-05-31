# M4 Mac Mini MLX Model Candidates - 2026-05-30

This list tracks Hugging Face MLX-format model candidates for the M4 Mac mini
benchmark project. The immediate target is models that are plausible on a 16 GB
Apple Silicon machine.

For the broader exhaustive catalog, see:

- `docs/model-candidates/hf-mlx-candidate-catalog-2026-05-30.md`
- `data/model-candidates/hf-mlx-candidates-raw-2026-05-30.json`
- `data/model-candidates/hf-mlx-candidates-top160-2026-05-30.csv`

The raw catalog currently contains 1,229 MLX-related Hugging Face candidates
found through API searches. This document is the practical first-pass test queue
for the M4 Mac mini.

Selection rule:

- Prefer MLX repositories with 4-bit, 3-bit, or 2-bit quantization.
- Prioritize repository storage below roughly 8.5 GB.
- Treat 9B-14B 4-bit and 14B 3-bit as edge candidates.
- Treat 24B+ dense or large multimodal models as later Mac Studio / GB10
  comparison candidates unless they are MoE/low-bit and especially interesting.

Storage is from Hugging Face `usedStorage` where checked. It is a repository
storage indicator, not a guaranteed runtime peak-memory requirement.

## First Test Queue

These should be tested first because they are small enough or strategically
important for the benchmark.

| Model | Link | Storage | Why Test |
| --- | --- | ---: | --- |
| Qwen3-4B MLX 4bit | https://huggingface.co/Qwen/Qwen3-4B-MLX-4bit | 2.15 GB | Official Qwen MLX 4B baseline. |
| Qwen3-4B Instruct 2507 4bit | https://huggingface.co/mlx-community/Qwen3-4B-Instruct-2507-4bit | 2.27 GB | Current local automation baseline family. |
| Qwen3-4B Instruct 2507 LM Studio MLX 4bit | https://huggingface.co/lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit | 2.27 GB | Alternative packaging for server/client compatibility. |
| Qwen3-8B 4bit | https://huggingface.co/mlx-community/Qwen3-8B-4bit | 4.62 GB | Strong general 8B candidate. |
| DeepSeek-R1-0528-Qwen3-8B MLX 4bit | https://huggingface.co/lmstudio-community/DeepSeek-R1-0528-Qwen3-8B-MLX-4bit | 4.62 GB | Popular reasoning-distill 8B candidate. |
| LFM2.5-1.2B Instruct MLX 4bit | https://huggingface.co/lmstudio-community/LFM2.5-1.2B-Instruct-MLX-4bit | 0.66 GB | Tiny LiquidAI comparison against tested LFM2.5 8B-A1B. |
| LFM2.5-8B-A1B MLX 4bit | https://huggingface.co/LiquidAI/LFM2.5-8B-A1B-MLX-4bit | 4.80 GB | Already smoke-tested; keep for controlled semantic-signal lane. |
| Phi-4-mini-reasoning MLX 4bit | https://huggingface.co/lmstudio-community/Phi-4-mini-reasoning-MLX-4bit | 2.17 GB | Small reasoning/code model from Microsoft family. |
| Llama-3.2-1B Instruct 4bit | https://huggingface.co/mlx-community/Llama-3.2-1B-Instruct-4bit | 1.41 GB | Tiny control model; good for protocol baseline. |
| Gemma-3-1B IT QAT 4bit | https://huggingface.co/mlx-community/gemma-3-1b-it-qat-4bit | 0.77 GB | Tiny Gemma text baseline. |
| Ternary-Bonsai-1.7B MLX 2bit | https://huggingface.co/prism-ml/Ternary-Bonsai-1.7B-mlx-2bit | 0.50 GB | Ultra-low-bit Apple Silicon/on-device experiment. |
| Ternary-Bonsai-4B MLX 2bit | https://huggingface.co/prism-ml/Ternary-Bonsai-4B-mlx-2bit | 1.14 GB | Very compact 4B low-bit candidate. |
| Ternary-Bonsai-8B MLX 2bit | https://huggingface.co/prism-ml/Ternary-Bonsai-8B-mlx-2bit | 2.32 GB | Important low-bit 8B candidate with high likes/downloads. |
| DeepSeek-R1-Distill-Qwen-1.5B 3bit | https://huggingface.co/mlx-community/DeepSeek-R1-Distill-Qwen-1.5B-3bit | 0.79 GB | Tiny reasoning-distill baseline. |
| DeepSeek-R1-Distill-Qwen-7B 3bit | https://huggingface.co/mlx-community/DeepSeek-R1-Distill-Qwen-7B-3bit | 3.34 GB | Low-bit reasoning candidate likely to fit. |
| Mistral-7B-Instruct v0.3 4bit | https://huggingface.co/mlx-community/Mistral-7B-Instruct-v0.3-4bit | 4.08 GB | Classic 7B instruction baseline. |

## Coding Candidates

These belong in the coding/patch lane. Some are already integrated as trace or
live backends.

| Model | Link | Storage | Notes |
| --- | --- | ---: | --- |
| Qwen2.5-Coder-7B Instruct MLX 4bit | https://huggingface.co/lmstudio-community/Qwen2.5-Coder-7B-Instruct-MLX-4bit | 4.30 GB | Better fit than 14B for 16 GB smoke tests. |
| Qwen2.5-Coder-14B Instruct MLX 4bit | https://huggingface.co/lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit | 8.32 GB | Already timed out in naive live adapter; keep as edge candidate. |
| Qwen2.5-Coder-7B Instruct community 4bit | https://huggingface.co/mlx-community/Qwen2.5-Coder-7B-Instruct-4bit | size TBD | Alternative community package. |
| Qwen3-Coder-30B-A3B Instruct MLX 3bit | https://huggingface.co/mlx-community/Qwen3-Coder-30B-A3B-Instruct-3bit | size TBD | MoE coding edge candidate; likely later. |
| Qwen3-Coder-30B-A3B Instruct MLX 4bit | https://huggingface.co/lmstudio-community/Qwen3-Coder-30B-A3B-Instruct-MLX-4bit | size TBD | MoE coding edge candidate; likely not first on 16 GB. |
| Qwen3-Coder-Next MLX 4bit | https://huggingface.co/lmstudio-community/Qwen3-Coder-Next-MLX-4bit | size TBD | Interesting but verify architecture/size before download. |
| Qwen3-Coder-Next REAM MLX 3bit | https://huggingface.co/TomLucidor/Qwen3-Coder-Next-REAM-mlx-3Bit | size TBD | Experimental coding compression candidate. |

## General Summary / Extraction Candidates

These should be tested on `korean_news_summary`,
`market_event_extraction`, `json_compliance`, and `think_token_cleanup`.

| Model | Link | Storage | Notes |
| --- | --- | ---: | --- |
| Qwen3.5-9B MLX 4bit | https://huggingface.co/mlx-community/Qwen3.5-9B-MLX-4bit | 5.97 GB | Strong 9B candidate; vision tag but useful as general model. |
| Qwen3.5-9B OptiQ 4bit | https://huggingface.co/mlx-community/Qwen3.5-9B-OptiQ-4bit | 13.35 GB | Larger package; maybe too heavy but interesting OptiQ format. |
| Qwen3.5-9B 4bit base | https://huggingface.co/mlx-community/Qwen3.5-9B-4bit | size TBD | Base 9B package; compare to MLX/OptiQ variants. |
| Qwen3.5-4B 4bit | https://huggingface.co/mlx-community/Qwen3.5-4B-4bit | size TBD | Compact Qwen3.5 candidate. |
| Qwen3.5-2B 4bit | https://huggingface.co/mlx-community/Qwen3.5-2B-4bit | size TBD | Tiny Qwen3.5 protocol candidate. |
| Qwen3.5-0.8B MLX 4bit | https://huggingface.co/mlx-community/Qwen3.5-0.8B-MLX-4bit | size TBD | Very small baseline. |
| Qwen2.5-7B Instruct 4bit | https://huggingface.co/mlx-community/Qwen2.5-7B-Instruct-4bit | size TBD | Stable older Qwen baseline. |
| Qwen2.5-3B Instruct 4bit | https://huggingface.co/mlx-community/Qwen2.5-3B-Instruct-4bit | size TBD | Small summary/extraction candidate. |
| Qwen2.5-1.5B Instruct 4bit | https://huggingface.co/mlx-community/Qwen2.5-1.5B-Instruct-4bit | size TBD | Tiny instruction baseline. |
| Qwen2.5-0.5B Instruct 4bit | https://huggingface.co/mlx-community/Qwen2.5-0.5B-Instruct-4bit | size TBD | Very small control. |
| Llama-3.1-8B Instruct 4bit | https://huggingface.co/mlx-community/Meta-Llama-3.1-8B-Instruct-4bit | 4.52 GB | Strong non-Qwen 8B baseline. |
| Gemma-3-4B IT QAT 4bit | https://huggingface.co/mlx-community/gemma-3-4b-it-qat-4bit | 6.43 GB | Multimodal/package overhead; still worth smoke. |
| Gemma-3-12B IT QAT 4bit | https://huggingface.co/mlx-community/gemma-3-12b-it-qat-4bit | 23.72 GB | Too large for first 16 GB queue; later only. |
| Ministral-3-3B Instruct 2512 4bit | https://huggingface.co/mlx-community/Ministral-3-3B-Instruct-2512-4bit | 4.71 GB | Interesting small multilingual candidate with Korean tag. |
| Gemma-4-E2B IT MLX 4bit | https://huggingface.co/lmstudio-community/gemma-4-E2B-it-MLX-4bit | size TBD | Future tiny Gemma-4 lane. |
| Gemma-4-E4B IT MLX 4bit | https://huggingface.co/lmstudio-community/gemma-4-E4B-it-MLX-4bit | size TBD | Future small Gemma-4 lane. |
| Gemma-4 e2b 4bit | https://huggingface.co/mlx-community/gemma-4-e2b-it-4bit | size TBD | Alternative community package. |
| Gemma-4 e4b 4bit | https://huggingface.co/mlx-community/gemma-4-e4b-it-4bit | size TBD | Alternative community package. |

## Vision / Multimodal Candidates

These are not first priority for text-only summary/extraction, but they could be
useful if the benchmark later adds screenshot, chart, or report-image tasks.

| Model | Link | Notes |
| --- | --- | --- |
| Qwen3-VL-4B Instruct MLX 4bit | https://huggingface.co/lmstudio-community/Qwen3-VL-4B-Instruct-MLX-4bit | Small VLM candidate. |
| Qwen3-VL-4B Instruct community 4bit | https://huggingface.co/mlx-community/Qwen3-VL-4B-Instruct-4bit | Alternative package. |
| Qwen3-VL-4B Instruct 3bit | https://huggingface.co/mlx-community/Qwen3-VL-4B-Instruct-3bit | Smaller VLM package. |
| Qwen3-VL-8B Instruct MLX 4bit | https://huggingface.co/lmstudio-community/Qwen3-VL-8B-Instruct-MLX-4bit | Edge VLM candidate. |
| Qwen2-VL-7B Instruct 4bit | https://huggingface.co/mlx-community/Qwen2-VL-7B-Instruct-4bit | Older VLM baseline. |
| Gemma-3n-E4B IT MLX 4bit | https://huggingface.co/lmstudio-community/gemma-3n-E4B-it-MLX-4bit | Multimodal/audio/video tags; verify runtime support. |

## Edge / Later Hardware Candidates

These are probably not first-pass 16 GB candidates, but they are worth saving
for Mac Studio / GB10 / larger-memory comparisons.

| Model | Link | Reason to Save |
| --- | --- | --- |
| Qwen3-14B MLX 4bit | https://huggingface.co/lmstudio-community/Qwen3-14B-MLX-4bit | Dense 14B edge candidate. |
| DeepSeek-R1-Distill-Qwen-14B 3bit | https://huggingface.co/mlx-community/DeepSeek-R1-Distill-Qwen-14B-3bit | 6.47 GB storage, but reasoning output may be slow. |
| LFM2-24B-A2B MLX 4bit | https://huggingface.co/lmstudio-community/LFM2-24B-A2B-MLX-4bit | MoE/edge LiquidAI candidate. |
| Devstral-Small-2505 4bit | https://huggingface.co/mlx-community/Devstral-Small-2505-4bit | Coding agent model; likely heavy. |
| Devstral-Small-2505 LM Studio 4bit | https://huggingface.co/lmstudio-community/Devstral-Small-2505-MLX-4bit | Alternative package. |
| Devstral-Small-2507 LM Studio 4bit | https://huggingface.co/lmstudio-community/Devstral-Small-2507-MLX-4bit | Newer package. |
| Devstral-Small-2-24B Instruct 2512 4bit | https://huggingface.co/mlx-community/Devstral-Small-2-24B-Instruct-2512-4bit | Later coding benchmark candidate. |
| Qwen3-30B-A3B 4bit | https://huggingface.co/mlx-community/Qwen3-30B-A3B-4bit | MoE edge candidate. |
| Qwen3-30B-A3B LM Studio 4bit | https://huggingface.co/lmstudio-community/Qwen3-30B-A3B-MLX-4bit | Alternative package. |
| Qwen3.6-27B 4bit | https://huggingface.co/mlx-community/Qwen3.6-27B-4bit | Later larger-memory baseline. |
| Qwen3.6-27B OptiQ 4bit | https://huggingface.co/mlx-community/Qwen3.6-27B-OptiQ-4bit | OptiQ variant. |
| Qwen3.6-27B 3bit | https://huggingface.co/leonsarmiento/Qwen3.6-27B-3bit-mlx | Low-bit dense 27B experiment. |
| Qwen3.6-27B UD MLX 3bit | https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-3bit | Unsloth dynamic quant candidate. |
| Qwen3.6-35B-A3B 4bit | https://huggingface.co/mlx-community/Qwen3.6-35B-A3B-4bit | MoE large comparison. |
| Qwen3.6-35B-A3B UD MLX 3bit | https://huggingface.co/unsloth/Qwen3.6-35B-A3B-UD-MLX-3bit | Low-bit MoE comparison. |
| Qwen3.6-35B-A3B RotorQuant 2bit | https://huggingface.co/majentik/Qwen3.6-35B-A3B-RotorQuant-MLX-2bit | Aggressive low-bit MoE experiment. |
| Qwen3.6-35B-A3B TurboQuant 2bit | https://huggingface.co/majentik/Qwen3.6-35B-A3B-TurboQuant-MLX-2bit | Aggressive low-bit MoE experiment. |
| Qwen3.5-27B 4bit | https://huggingface.co/mlx-community/Qwen3.5-27B-4bit | Later larger-memory baseline. |
| Qwen3.5-27B 2bit TurboQuant | https://huggingface.co/majentik/Qwen3.5-27B-TurboQuant-MLX-2bit | Low-bit larger-model experiment. |
| GLM-4.7 Flash 4bit | https://huggingface.co/mlx-community/GLM-4.7-Flash-4bit | Interesting GLM text model. |
| GLM-4.5 Air 3bit | https://huggingface.co/mlx-community/GLM-4.5-Air-3bit | Later GLM low-bit candidate. |
| MiniMax-M2.5 3bit | https://huggingface.co/mlx-community/MiniMax-M2.5-3bit | Large/custom-code candidate; likely later. |
| MiniMax-M2.7 3bit | https://huggingface.co/mlx-community/MiniMax-M2.7-3bit | Large/custom-code candidate; likely later. |
| GPT-OSS-20B TurboQuant MLX 2bit | https://huggingface.co/majentik/gpt-oss-20b-TurboQuant-MLX-2bit | Save for low-bit larger-model comparison. |
| GPT-OSS-20B RotorQuant MLX 2bit | https://huggingface.co/majentik/gpt-oss-20b-RotorQuant-MLX-2bit | Save for low-bit larger-model comparison. |
| DeepSeek-V4-Flash 2bit DQ | https://huggingface.co/mlx-community/DeepSeek-V4-Flash-2bit-DQ | Popular but likely large/experimental. |

## Initial Test Order

1. `Qwen/Qwen3-4B-MLX-4bit`
2. `mlx-community/Qwen3-4B-Instruct-2507-4bit`
3. `prism-ml/Ternary-Bonsai-4B-mlx-2bit`
4. `prism-ml/Ternary-Bonsai-8B-mlx-2bit`
5. `lmstudio-community/Phi-4-mini-reasoning-MLX-4bit`
6. `mlx-community/Qwen3-8B-4bit`
7. `lmstudio-community/DeepSeek-R1-0528-Qwen3-8B-MLX-4bit`
8. `lmstudio-community/Qwen2.5-Coder-7B-Instruct-MLX-4bit`
9. `mlx-community/DeepSeek-R1-Distill-Qwen-7B-3bit`
10. `mlx-community/Qwen3.5-9B-MLX-4bit`
11. `lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit`

## Notes

- 14B 4-bit can fit on disk but may be too slow or memory-tight in practice on
  16 GB, as seen with the first Qwen2.5-Coder-14B live smoke.
- 2-bit/3-bit models are important for this project because they may shift the
  useful frontier on the current machine, but output quality and protocol
  discipline must be measured separately from load success.
- For every model, save: prompt, raw output, wall time, parser score, task score,
  and recommendation label.
