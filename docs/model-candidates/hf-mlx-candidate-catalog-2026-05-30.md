# Hugging Face MLX Candidate Catalog - 2026-05-30

Generated from Hugging Face API searches for MLX 4-bit, 3-bit, 2-bit, Apple Silicon, Qwen, Gemma, Llama, Mistral, and DeepSeek MLX variants.

- Raw MLX candidate pool: `1229` models saved in `data/model-candidates/hf-mlx-candidates-raw-2026-05-30.json`.
- Quantized candidate subset: `1229` models.
- This document lists the top 160 quantized candidates by downloads, enriched with repository storage where available.
- Storage is repository size, not guaranteed runtime memory.
- Automatic categories are only a starting point; the raw JSON is the source of truth for exhaustive testing.
- Test policy: download one candidate, run smoke/eval, save lightweight artifacts, then delete the local model cache completely.

See `docs/model-cache-cleanup-policy.md` for the storage policy.

## M4 Mac Mini 16GB Priority / Edge

Count in top 160: `49`

| Model | Quant | Params | Storage | Downloads | Likes | Link |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `lmstudio-community/DeepSeek-R1-0528-Qwen3-8B-MLX-4bit` | 4-bit | 8B | 4.62 GB | 428402 | 12 | [HF](https://huggingface.co/lmstudio-community/DeepSeek-R1-0528-Qwen3-8B-MLX-4bit) |
| `lmstudio-community/LFM2.5-1.2B-Instruct-MLX-4bit` | 4-bit | 1.2B | 0.66 GB | 116517 | 1 | [HF](https://huggingface.co/lmstudio-community/LFM2.5-1.2B-Instruct-MLX-4bit) |
| `Qwen/Qwen3-4B-MLX-4bit` | 4-bit | 4B | 2.15 GB | 76508 | 31 | [HF](https://huggingface.co/Qwen/Qwen3-4B-MLX-4bit) |
| `lmstudio-community/Qwen3-4B-Thinking-2507-MLX-4bit` | 4-bit | 4B | 2.27 GB | 63101 | 12 | [HF](https://huggingface.co/lmstudio-community/Qwen3-4B-Thinking-2507-MLX-4bit) |
| `mlx-community/Llama-3.2-1B-Instruct-4bit` | 4-bit | 1B | 1.41 GB | 59636 | 19 | [HF](https://huggingface.co/mlx-community/Llama-3.2-1B-Instruct-4bit) |
| `mlx-community/gemma-3-1b-it-qat-4bit` | 4-bit | 1B | 0.77 GB | 58723 | 4 | [HF](https://huggingface.co/mlx-community/gemma-3-1b-it-qat-4bit) |
| `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit` | 4-bit | 4B | 2.27 GB | 58336 | 3 | [HF](https://huggingface.co/lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit) |
| `lmstudio-community/Qwen3-14B-MLX-4bit` | 4-bit | 14B | 8.32 GB | 51281 | 6 | [HF](https://huggingface.co/lmstudio-community/Qwen3-14B-MLX-4bit) |
| `lmstudio-community/Qwen3-8B-MLX-4bit` | 4-bit | 8B | 4.62 GB | 30677 | 3 | [HF](https://huggingface.co/lmstudio-community/Qwen3-8B-MLX-4bit) |
| `mlx-community/Josiefied-Qwen3-8B-abliterated-v1-4bit` | 4-bit | 8B | 4.62 GB | 29944 | 5 | [HF](https://huggingface.co/mlx-community/Josiefied-Qwen3-8B-abliterated-v1-4bit) |
| `lmstudio-community/Qwen3-1.7B-MLX-4bit` | 4-bit | 1.7B | 0.98 GB | 29473 | 0 | [HF](https://huggingface.co/lmstudio-community/Qwen3-1.7B-MLX-4bit) |
| `mlx-community/Qwen3-1.7B-4bit` | 4-bit | 1.7B | 0.98 GB | 28320 | 4 | [HF](https://huggingface.co/mlx-community/Qwen3-1.7B-4bit) |
| `mlx-community/LFM2.5-1.2B-Instruct-4bit` | 4-bit | 1.2B | 0.66 GB | 28136 | 1 | [HF](https://huggingface.co/mlx-community/LFM2.5-1.2B-Instruct-4bit) |
| `mlx-community/Llama-3.2-3B-Instruct-4bit` | 4-bit | 3B | 5.44 GB | 26113 | 43 | [HF](https://huggingface.co/mlx-community/Llama-3.2-3B-Instruct-4bit) |
| `mlx-community/gemma-2-9b-it-4bit` | 4-bit | 9B | 5.22 GB | 25006 | 2 | [HF](https://huggingface.co/mlx-community/gemma-2-9b-it-4bit) |
| `lmstudio-community/Qwen3-4B-MLX-4bit` | 4-bit | 4B | 2.27 GB | 21989 | 1 | [HF](https://huggingface.co/lmstudio-community/Qwen3-4B-MLX-4bit) |
| `mlx-community/Qwen3-8B-4bit` | 4-bit | 8B | 4.62 GB | 21612 | 9 | [HF](https://huggingface.co/mlx-community/Qwen3-8B-4bit) |
| `mlx-community/Qwen3-0.6B-4bit` | 4-bit | 0.6B | 0.68 GB | 21528 | 12 | [HF](https://huggingface.co/mlx-community/Qwen3-0.6B-4bit) |
| `mlx-community/Qwen3-4B-Instruct-2507-4bit` | 4-bit | 4B | 2.27 GB | 20983 | 9 | [HF](https://huggingface.co/mlx-community/Qwen3-4B-Instruct-2507-4bit) |
| `mlx-community/Qwen2-VL-7B-Instruct-4bit` | 4-bit | 7B | 4.68 GB | 20213 | 2 | [HF](https://huggingface.co/mlx-community/Qwen2-VL-7B-Instruct-4bit) |
| `mlx-community/Qwen3-Embedding-0.6B-4bit-DWQ` | 4-bit | 0.6B | 0.35 GB | 17967 | 8 | [HF](https://huggingface.co/mlx-community/Qwen3-Embedding-0.6B-4bit-DWQ) |
| `mlx-community/Qwen3.5-4B-4bit` | 4-bit | 4B | 3.05 GB | 17209 | 6 | [HF](https://huggingface.co/mlx-community/Qwen3.5-4B-4bit) |
| `mlx-community/Qwen2.5-3B-Instruct-4bit` | 4-bit | 3B | 1.74 GB | 15812 | 1 | [HF](https://huggingface.co/mlx-community/Qwen2.5-3B-Instruct-4bit) |
| `mlx-community/Qwen2.5-0.5B-Instruct-4bit` | 4-bit | 0.5B | 0.28 GB | 13872 | 7 | [HF](https://huggingface.co/mlx-community/Qwen2.5-0.5B-Instruct-4bit) |
| `mlx-community/Qwen2.5-7B-Instruct-4bit` | 4-bit | 7B | 4.28 GB | 13386 | 15 | [HF](https://huggingface.co/mlx-community/Qwen2.5-7B-Instruct-4bit) |
| `mlx-community/Qwen3-4B-4bit` | 4-bit | 4B | 2.27 GB | 13128 | 12 | [HF](https://huggingface.co/mlx-community/Qwen3-4B-4bit) |
| `lmstudio-community/Qwen2.5-0.5B-Instruct-MLX-4bit` | 4-bit | 0.5B | 0.29 GB | 12957 | 1 | [HF](https://huggingface.co/lmstudio-community/Qwen2.5-0.5B-Instruct-MLX-4bit) |
| `mlx-community/Mistral-7B-Instruct-v0.3-4bit` | 4-bit | 7B | 4.08 GB | 12444 | 10 | [HF](https://huggingface.co/mlx-community/Mistral-7B-Instruct-v0.3-4bit) |
| `mlx-community/Qwen1.5-0.5B-Chat-4bit` | 4-bit | 0.5B | 2.07 GB | 12117 | 4 | [HF](https://huggingface.co/mlx-community/Qwen1.5-0.5B-Chat-4bit) |
| `mlx-community/Meta-Llama-3.1-8B-Instruct-4bit` | 4-bit | 8B | 4.52 GB | 11180 | 19 | [HF](https://huggingface.co/mlx-community/Meta-Llama-3.1-8B-Instruct-4bit) |
| `prism-ml/Ternary-Bonsai-8B-mlx-2bit` | 1.58-bit | 8B | 2.32 GB | 10972 | 105 | [HF](https://huggingface.co/prism-ml/Ternary-Bonsai-8B-mlx-2bit) |
| `mlx-community/Qwen2.5-1.5B-Instruct-4bit` | 4-bit | 1.5B | 0.87 GB | 9646 | 3 | [HF](https://huggingface.co/mlx-community/Qwen2.5-1.5B-Instruct-4bit) |
| `argmaxinc/mlx-FLUX.1-schnell-4bit-quantized` | 4-bit |  | 7.36 GB | 9071 | 33 | [HF](https://huggingface.co/argmaxinc/mlx-FLUX.1-schnell-4bit-quantized) |
| `Jackrong/MLX-Qwen3.5-9B-DeepSeek-V4-Flash-4bit` | 4-bit | 9B | 5.06 GB | 8004 | 9 | [HF](https://huggingface.co/Jackrong/MLX-Qwen3.5-9B-DeepSeek-V4-Flash-4bit) |
| `mlx-community/gemma-3-1b-it-4bit` | 4-bit | 1B | 0.77 GB | 8002 | 3 | [HF](https://huggingface.co/mlx-community/gemma-3-1b-it-4bit) |
| `mlx-community/Qwen2.5-14B-Instruct-4bit` | 4-bit | 14B | 8.31 GB | 7595 | 11 | [HF](https://huggingface.co/mlx-community/Qwen2.5-14B-Instruct-4bit) |
| `mlx-community/Meta-Llama-3-8B-Instruct-4bit` | 4-bit | 8B | 5.27 GB | 7265 | 81 | [HF](https://huggingface.co/mlx-community/Meta-Llama-3-8B-Instruct-4bit) |
| `mlx-community/Qwen3.5-4B-OptiQ-4bit` | 4-bit | 4B | 6.32 GB | 6818 | 15 | [HF](https://huggingface.co/mlx-community/Qwen3.5-4B-OptiQ-4bit) |
| `mlx-community/gemma-3n-E2B-it-lm-4bit` | 4-bit | 2B | 2.55 GB | 6580 | 3 | [HF](https://huggingface.co/mlx-community/gemma-3n-E2B-it-lm-4bit) |
| `mlx-community/Mistral-Nemo-Instruct-2407-4bit` | 4-bit |  | 6.89 GB | 6372 | 15 | [HF](https://huggingface.co/mlx-community/Mistral-Nemo-Instruct-2407-4bit) |
| `mlx-community/Qwen3.5-0.8B-OptiQ-4bit` | 4-bit | 0.8B | 1.94 GB | 6233 | 19 | [HF](https://huggingface.co/mlx-community/Qwen3.5-0.8B-OptiQ-4bit) |
| `Jackrong/MLX-Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-4bit` | 4-bit | 9B | 5.06 GB | 5332 | 24 | [HF](https://huggingface.co/Jackrong/MLX-Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-4bit) |
| `lmstudio-community/Qwen3-0.6B-MLX-4bit` | 4-bit | 0.6B | 0.35 GB | 4686 | 0 | [HF](https://huggingface.co/lmstudio-community/Qwen3-0.6B-MLX-4bit) |
| `Jackrong/MLX-Qwopus3.5-9B-v3-4bit` | 4-bit | 9B | 5.06 GB | 4426 | 28 | [HF](https://huggingface.co/Jackrong/MLX-Qwopus3.5-9B-v3-4bit) |
| `mlx-community/Qwen3.5-2B-OptiQ-4bit` | 4-bit | 2B | 4.64 GB | 4259 | 8 | [HF](https://huggingface.co/mlx-community/Qwen3.5-2B-OptiQ-4bit) |
| `mlx-community/Qwen2-VL-2B-Instruct-4bit` | 4-bit | 2B | 1.26 GB | 4257 | 6 | [HF](https://huggingface.co/mlx-community/Qwen2-VL-2B-Instruct-4bit) |
| `mlx-community/DeepSeek-R1-Distill-Qwen-1.5B-4bit` | 4-bit | 1.5B | 2.01 GB | 4251 | 6 | [HF](https://huggingface.co/mlx-community/DeepSeek-R1-Distill-Qwen-1.5B-4bit) |
| `Qwen/Qwen3-8B-MLX-4bit` | 4-bit | 8B | 4.36 GB | 4224 | 10 | [HF](https://huggingface.co/Qwen/Qwen3-8B-MLX-4bit) |
| `mlx-community/Qwen3-Embedding-4B-4bit-DWQ` | 4-bit | 4B | 2.27 GB | 3911 | 9 | [HF](https://huggingface.co/mlx-community/Qwen3-Embedding-4B-4bit-DWQ) |

## Coding / Agentic Patch Candidates

Count in top 160: `7`

| Model | Quant | Params | Storage | Downloads | Likes | Link |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit` | 4-bit | 14B | 8.32 GB | 164723 | 6 | [HF](https://huggingface.co/lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit) |
| `mlx-community/gemma-3-4b-it-qat-4bit` | 4-bit | 4B | 6.43 GB | 123790 | 9 | [HF](https://huggingface.co/mlx-community/gemma-3-4b-it-qat-4bit) |
| `lmstudio-community/Phi-4-mini-reasoning-MLX-4bit` | 4-bit |  | 2.17 GB | 59480 | 3 | [HF](https://huggingface.co/lmstudio-community/Phi-4-mini-reasoning-MLX-4bit) |
| `lmstudio-community/Phi-4-reasoning-plus-MLX-4bit` | 4-bit |  | 8.25 GB | 33073 | 1 | [HF](https://huggingface.co/lmstudio-community/Phi-4-reasoning-plus-MLX-4bit) |
| `lmstudio-community/Qwen2.5-Coder-7B-Instruct-MLX-4bit` | 4-bit | 7B | 4.3 GB | 20515 | 5 | [HF](https://huggingface.co/lmstudio-community/Qwen2.5-Coder-7B-Instruct-MLX-4bit) |
| `mlx-community/Qwen2.5-Coder-7B-Instruct-4bit` | 4-bit | 7B | 4.28 GB | 8238 | 14 | [HF](https://huggingface.co/mlx-community/Qwen2.5-Coder-7B-Instruct-4bit) |
| `lmstudio-community/Qwen2.5-Coder-3B-Instruct-MLX-4bit` | 4-bit | 3B | 1.75 GB | 4352 | 1 | [HF](https://huggingface.co/lmstudio-community/Qwen2.5-Coder-3B-Instruct-MLX-4bit) |

## Vision / Audio / Multimodal Candidates

Count in top 160: `17`

| Model | Quant | Params | Storage | Downloads | Likes | Link |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `lmstudio-community/Qwen3-VL-4B-Instruct-MLX-4bit` | 4-bit | 4B | 3.11 GB | 152905 | 7 | [HF](https://huggingface.co/lmstudio-community/Qwen3-VL-4B-Instruct-MLX-4bit) |
| `lmstudio-community/GLM-4.6V-Flash-MLX-4bit` | 4-bit |  | 7.09 GB | 131886 | 2 | [HF](https://huggingface.co/lmstudio-community/GLM-4.6V-Flash-MLX-4bit) |
| `lmstudio-community/Qwen3-VL-8B-Instruct-MLX-4bit` | 4-bit | 8B | 5.77 GB | 108412 | 4 | [HF](https://huggingface.co/lmstudio-community/Qwen3-VL-8B-Instruct-MLX-4bit) |
| `aufklarer/Qwen3-ASR-0.6B-MLX-4bit` | 4-bit | 0.6B | 0.71 GB | 96345 | 3 | [HF](https://huggingface.co/aufklarer/Qwen3-ASR-0.6B-MLX-4bit) |
| `mlx-community/gemma-4-e2b-it-4bit` | 4-bit | 2B | 3.61 GB | 82936 | 16 | [HF](https://huggingface.co/mlx-community/gemma-4-e2b-it-4bit) |
| `mlx-community/Qwen3.5-9B-MLX-4bit` | 4-bit | 9B | 5.97 GB | 51187 | 125 | [HF](https://huggingface.co/mlx-community/Qwen3.5-9B-MLX-4bit) |
| `mlx-community/gemma-4-e4b-it-4bit` | 4-bit | 4B | 5.25 GB | 40174 | 24 | [HF](https://huggingface.co/mlx-community/gemma-4-e4b-it-4bit) |
| `mlx-community/Qwen3.5-4B-MLX-4bit` | 4-bit | 4B | 3.05 GB | 27493 | 21 | [HF](https://huggingface.co/mlx-community/Qwen3.5-4B-MLX-4bit) |
| `mlx-community/Ministral-3-3B-Instruct-2512-4bit` | 4-bit | 3B | 4.71 GB | 21996 | 5 | [HF](https://huggingface.co/mlx-community/Ministral-3-3B-Instruct-2512-4bit) |
| `mlx-community/Qwen3.5-9B-4bit` | 4-bit | 9B | 5.97 GB | 21890 | 10 | [HF](https://huggingface.co/mlx-community/Qwen3.5-9B-4bit) |
| `mlx-community/Qwen3-VL-4B-Instruct-4bit` | 4-bit | 4B | 3.11 GB | 14364 | 7 | [HF](https://huggingface.co/mlx-community/Qwen3-VL-4B-Instruct-4bit) |
| `mlx-community/Qwen3.6-27B-AEON-Ultimate-Uncensored-BF16-mlx-2Bit` | 2-bit | 27B | 8.43 GB | 12348 | 5 | [HF](https://huggingface.co/mlx-community/Qwen3.6-27B-AEON-Ultimate-Uncensored-BF16-mlx-2Bit) |
| `mlx-community/Qwen3.5-2B-4bit` | 4-bit | 2B | 1.74 GB | 11983 | 3 | [HF](https://huggingface.co/mlx-community/Qwen3.5-2B-4bit) |
| `mlx-community/Qwen3.5-0.8B-MLX-4bit` | 4-bit | 0.8B | 0.65 GB | 8640 | 4 | [HF](https://huggingface.co/mlx-community/Qwen3.5-0.8B-MLX-4bit) |
| `deadbydawn101/gemma-4-E2B-Heretic-Uncensored-mlx-4bit` | 4-bit | 2B | 3.61 GB | 6696 | 15 | [HF](https://huggingface.co/deadbydawn101/gemma-4-E2B-Heretic-Uncensored-mlx-4bit) |
| `mlx-community/LFM2-VL-1.6B-4bit` | 4-bit | 1.6B | 1.46 GB | 6103 | 1 | [HF](https://huggingface.co/mlx-community/LFM2-VL-1.6B-4bit) |
| `mlx-community/LFM2.5-VL-1.6B-4bit` | 4-bit | 1.6B | 1.49 GB | 5087 | 3 | [HF](https://huggingface.co/mlx-community/LFM2.5-VL-1.6B-4bit) |

## Larger Later Hardware Candidates

Count in top 160: `87`

| Model | Quant | Params | Storage | Downloads | Likes | Link |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `lmstudio-community/LFM2-24B-A2B-MLX-4bit` | 4-bit | 24B-A2B | 13.42 GB | 332746 | 4 | [HF](https://huggingface.co/lmstudio-community/LFM2-24B-A2B-MLX-4bit) |
| `mlx-community/Qwen3.5-9B-OptiQ-4bit` | 4-bit | 9B | 13.35 GB | 229187 | 47 | [HF](https://huggingface.co/mlx-community/Qwen3.5-9B-OptiQ-4bit) |
| `lmstudio-community/Qwen3-Coder-Next-MLX-4bit` | 4-bit |  | 44.86 GB | 222120 | 23 | [HF](https://huggingface.co/lmstudio-community/Qwen3-Coder-Next-MLX-4bit) |
| `lmstudio-community/Qwen3-Coder-30B-A3B-Instruct-MLX-4bit` | 4-bit | 30B-A3B | 17.19 GB | 202341 | 30 | [HF](https://huggingface.co/lmstudio-community/Qwen3-Coder-30B-A3B-Instruct-MLX-4bit) |
| `mlx-community/Devstral-Small-2-24B-Instruct-2512-4bit` | 4-bit | 24B | 14.14 GB | 156481 | 4 | [HF](https://huggingface.co/mlx-community/Devstral-Small-2-24B-Instruct-2512-4bit) |
| `unsloth/Qwen3.6-35B-A3B-UD-MLX-4bit` | 4-bit | 35B-A3B | 43.07 GB | 130094 | 81 | [HF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-UD-MLX-4bit) |
| `lmstudio-community/gemma-3n-E4B-it-MLX-4bit` | 4-bit | 4B | 10.7 GB | 110292 | 2 | [HF](https://huggingface.co/lmstudio-community/gemma-3n-E4B-it-MLX-4bit) |
| `mlx-community/Qwen3.5-27B-4bit` | 4-bit | 27B | 16.07 GB | 96622 | 47 | [HF](https://huggingface.co/mlx-community/Qwen3.5-27B-4bit) |
| `mlx-community/Qwen3.6-35B-A3B-4bit` | 4-bit | 35B-A3B | 20.42 GB | 93953 | 58 | [HF](https://huggingface.co/mlx-community/Qwen3.6-35B-A3B-4bit) |
| `lmstudio-community/Hermes-4-70B-MLX-4bit` | 4-bit | 70B | 39.71 GB | 86043 | 3 | [HF](https://huggingface.co/lmstudio-community/Hermes-4-70B-MLX-4bit) |
| `lmstudio-community/NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-4bit` | 4-bit | 30B-A3B | 17.79 GB | 84048 | 2 | [HF](https://huggingface.co/lmstudio-community/NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-4bit) |
| `mlx-community/Qwen3-30B-A3B-4bit` | 4-bit | 30B-A3B | 17.19 GB | 79590 | 15 | [HF](https://huggingface.co/mlx-community/Qwen3-30B-A3B-4bit) |
| `lmstudio-community/gemma-4-26B-A4B-it-MLX-4bit` | 4-bit | 26B-A4B | 15.64 GB | 69389 | 6 | [HF](https://huggingface.co/lmstudio-community/gemma-4-26B-A4B-it-MLX-4bit) |
| `lmstudio-community/Qwen3-VL-30B-A3B-Instruct-MLX-4bit` | 4-bit | 30B-A3B | 18.26 GB | 63846 | 1 | [HF](https://huggingface.co/lmstudio-community/Qwen3-VL-30B-A3B-Instruct-MLX-4bit) |
| `unsloth/Qwen3.6-27B-UD-MLX-4bit` | 4-bit | 27B | 26.21 GB | 63265 | 54 | [HF](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-4bit) |
| `mlx-community/gemma-3-12b-it-qat-4bit` | 4-bit | 12B | 23.72 GB | 61556 | 18 | [HF](https://huggingface.co/mlx-community/gemma-3-12b-it-qat-4bit) |
| `lmstudio-community/Qwen2.5-Coder-32B-Instruct-MLX-4bit` | 4-bit | 32B | 18.44 GB | 59287 | 6 | [HF](https://huggingface.co/lmstudio-community/Qwen2.5-Coder-32B-Instruct-MLX-4bit) |
| `mlx-community/gemma-3-27b-it-qat-4bit` | 4-bit | 27B | 33.71 GB | 53013 | 23 | [HF](https://huggingface.co/mlx-community/gemma-3-27b-it-qat-4bit) |
| `aufklarer/PersonaPlex-7B-MLX-4bit` | 4-bit | 7B | 20.45 GB | 47641 | 32 | [HF](https://huggingface.co/aufklarer/PersonaPlex-7B-MLX-4bit) |
| `mlx-community/Devstral-Small-2505-4bit` | 4-bit |  | 13.28 GB | 47481 | 2 | [HF](https://huggingface.co/mlx-community/Devstral-Small-2505-4bit) |
| `mlx-community/gemma-4-26b-a4b-it-4bit` | 4-bit | 26B-A4B | 30.98 GB | 45831 | 63 | [HF](https://huggingface.co/mlx-community/gemma-4-26b-a4b-it-4bit) |
| `mlx-community/Qwen3.6-27B-4bit` | 4-bit | 27B | 16.07 GB | 45251 | 23 | [HF](https://huggingface.co/mlx-community/Qwen3.6-27B-4bit) |
| `lmstudio-community/gemma-4-E4B-it-MLX-4bit` | 4-bit | 4B | 9.45 GB | 42584 | 12 | [HF](https://huggingface.co/lmstudio-community/gemma-4-E4B-it-MLX-4bit) |
| `mlx-community/Qwen3.5-27B-Claude-4.6-Opus-Distilled-MLX-4bit` | 4-bit | 27B | 15.15 GB | 39148 | 203 | [HF](https://huggingface.co/mlx-community/Qwen3.5-27B-Claude-4.6-Opus-Distilled-MLX-4bit) |
| `lmstudio-community/Seed-OSS-36B-Instruct-MLX-4bit` | 4-bit | 36B | 20.35 GB | 37260 | 0 | [HF](https://huggingface.co/lmstudio-community/Seed-OSS-36B-Instruct-MLX-4bit) |
| `lmstudio-community/QwQ-32B-MLX-4bit` | 4-bit | 32B | 18.44 GB | 36659 | 0 | [HF](https://huggingface.co/lmstudio-community/QwQ-32B-MLX-4bit) |
| `lmstudio-community/Qwen3.6-27B-MLX-4bit` | 4-bit | 27B | 16.07 GB | 36493 | 0 | [HF](https://huggingface.co/lmstudio-community/Qwen3.6-27B-MLX-4bit) |
| `mlx-community/DeepSeek-V4-Flash-2bit-DQ` | 2-bit |  | 96.52 GB | 36466 | 45 | [HF](https://huggingface.co/mlx-community/DeepSeek-V4-Flash-2bit-DQ) |
| `lmstudio-community/Olmo-3-32B-Think-MLX-4bit` | 4-bit | 32B | 18.13 GB | 35786 | 1 | [HF](https://huggingface.co/lmstudio-community/Olmo-3-32B-Think-MLX-4bit) |
| `lmstudio-community/Qwen3-30B-A3B-Instruct-2507-MLX-4bit` | 4-bit | 30B-A3B | 17.19 GB | 31807 | 7 | [HF](https://huggingface.co/lmstudio-community/Qwen3-30B-A3B-Instruct-2507-MLX-4bit) |
| `lmstudio-community/Magistral-Small-2509-MLX-4bit` | 4-bit |  | 14.12 GB | 31378 | 0 | [HF](https://huggingface.co/lmstudio-community/Magistral-Small-2509-MLX-4bit) |
| `lmstudio-community/ERNIE-4.5-21B-A3B-MLX-4bit` | 4-bit | 21B-A3B | 12.28 GB | 29684 | 1 | [HF](https://huggingface.co/lmstudio-community/ERNIE-4.5-21B-A3B-MLX-4bit) |
| `lmstudio-community/Mistral-Small-3.2-24B-Instruct-2506-MLX-4bit` | 4-bit | 24B | 13.54 GB | 25559 | 3 | [HF](https://huggingface.co/lmstudio-community/Mistral-Small-3.2-24B-Instruct-2506-MLX-4bit) |
| `lmstudio-community/Qwen3-Next-80B-A3B-Instruct-MLX-4bit` | 4-bit | 80B-A3B | 44.86 GB | 23664 | 7 | [HF](https://huggingface.co/lmstudio-community/Qwen3-Next-80B-A3B-Instruct-MLX-4bit) |
| `mlx-community/DeepSeek-V4-Flash-4bit` | 4-bit |  | 489.08 GB | 22336 | 19 | [HF](https://huggingface.co/mlx-community/DeepSeek-V4-Flash-4bit) |
| `lmstudio-community/MiniMax-M2.5-MLX-4bit` | 4-bit |  | 128.68 GB | 22256 | 1 | [HF](https://huggingface.co/lmstudio-community/MiniMax-M2.5-MLX-4bit) |
| `Jiunsong/supergemma4-26b-uncensored-mlx-4bit-v2` | 4-bit | 26B | 30.15 GB | 21579 | 251 | [HF](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-mlx-4bit-v2) |
| `lmstudio-community/gemma-4-31B-it-MLX-4bit` | 4-bit | 31B | 28.85 GB | 21331 | 1 | [HF](https://huggingface.co/lmstudio-community/gemma-4-31B-it-MLX-4bit) |
| `lmstudio-community/Devstral-Small-2507-MLX-4bit` | 4-bit |  | 13.28 GB | 20324 | 4 | [HF](https://huggingface.co/lmstudio-community/Devstral-Small-2507-MLX-4bit) |
| `lmstudio-community/Qwen3-32B-MLX-4bit` | 4-bit | 32B | 18.44 GB | 17432 | 5 | [HF](https://huggingface.co/lmstudio-community/Qwen3-32B-MLX-4bit) |
| `mlx-community/gemma-4-31b-it-4bit` | 4-bit | 31B | 36.86 GB | 16887 | 38 | [HF](https://huggingface.co/mlx-community/gemma-4-31b-it-4bit) |
| `mlx-community/Qwen3.6-27B-OptiQ-4bit` | 4-bit | 27B | 35.55 GB | 14251 | 23 | [HF](https://huggingface.co/mlx-community/Qwen3.6-27B-OptiQ-4bit) |
| `Youssofal/Qwen3.6-35B-A3B-Abliterated-Heretic-MLX-4bit` | 4-bit | 35B-A3B | 48.34 GB | 14089 | 17 | [HF](https://huggingface.co/Youssofal/Qwen3.6-35B-A3B-Abliterated-Heretic-MLX-4bit) |
| `lmstudio-community/Qwen3-30B-A3B-MLX-4bit` | 4-bit | 30B-A3B | 17.19 GB | 13230 | 24 | [HF](https://huggingface.co/lmstudio-community/Qwen3-30B-A3B-MLX-4bit) |
| `mlx-community/gemma-4-e4b-it-OptiQ-4bit` | 4-bit | 4B | 22.71 GB | 12418 | 23 | [HF](https://huggingface.co/mlx-community/gemma-4-e4b-it-OptiQ-4bit) |
| `lmstudio-community/Devstral-Small-2505-MLX-4bit` | 4-bit |  | 13.28 GB | 12171 | 7 | [HF](https://huggingface.co/lmstudio-community/Devstral-Small-2505-MLX-4bit) |
| `mlx-community/Llama-3.2-90B-Vision-Instruct-4bit` | 4-bit | 90B | 49.86 GB | 11588 | 4 | [HF](https://huggingface.co/mlx-community/Llama-3.2-90B-Vision-Instruct-4bit) |
| `mlx-community/Qwen3.5-122B-A10B-4bit` | 4-bit | 122B-A10B | 69.61 GB | 10976 | 14 | [HF](https://huggingface.co/mlx-community/Qwen3.5-122B-A10B-4bit) |
| `lmstudio-community/gemma-4-E2B-it-MLX-4bit` | 4-bit | 2B | 8.73 GB | 9885 | 0 | [HF](https://huggingface.co/lmstudio-community/gemma-4-E2B-it-MLX-4bit) |
| `mlx-community/Qwen3.5-35B-A3B-4bit` | 4-bit | 35B-A3B | 20.41 GB | 9879 | 36 | [HF](https://huggingface.co/mlx-community/Qwen3.5-35B-A3B-4bit) |
| `mlx-community/Llama-3.3-70B-Instruct-4bit` | 4-bit | 70B | 39.71 GB | 9749 | 35 | [HF](https://huggingface.co/mlx-community/Llama-3.3-70B-Instruct-4bit) |
| `lmstudio-community/Llama-4-Scout-17B-16E-MLX-text-4bit` | 4-bit | 17B | 60.65 GB | 9515 | 1 | [HF](https://huggingface.co/lmstudio-community/Llama-4-Scout-17B-16E-MLX-text-4bit) |
| `lmstudio-community/Magistral-Small-2506-MLX-4bit` | 4-bit |  | 13.28 GB | 9275 | 15 | [HF](https://huggingface.co/lmstudio-community/Magistral-Small-2506-MLX-4bit) |
| `mlx-community/GLM-4.7-Flash-4bit` | 4-bit |  | 33.73 GB | 8928 | 63 | [HF](https://huggingface.co/mlx-community/GLM-4.7-Flash-4bit) |
| `mlx-community/Qwen3.6-35B-A3B-4bit-DWQ` | 4-bit | 35B-A3B | 20.68 GB | 8352 | 12 | [HF](https://huggingface.co/mlx-community/Qwen3.6-35B-A3B-4bit-DWQ) |
| `lmstudio-community/MiniMax-M2-MLX-4bit` | 4-bit |  | 128.68 GB | 8253 | 0 | [HF](https://huggingface.co/lmstudio-community/MiniMax-M2-MLX-4bit) |
| `lmstudio-community/Qwen3-Coder-480B-A35B-Instruct-MLX-4bit` | 4-bit | 480B-A35B | 270.1 GB | 7965 | 4 | [HF](https://huggingface.co/lmstudio-community/Qwen3-Coder-480B-A35B-Instruct-MLX-4bit) |
| `lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit` | 4-bit | 35B-A3B | 20.42 GB | 7880 | 0 | [HF](https://huggingface.co/lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit) |
| `lmstudio-community/Qwen3.5-397B-A17B-MLX-4bit` | 4-bit | 397B-A17B | 372.47 GB | 7574 | 0 | [HF](https://huggingface.co/lmstudio-community/Qwen3.5-397B-A17B-MLX-4bit) |
| `mlx-community/DeepSeek-V4-Pro-4bit` | 4-bit |  | 837.01 GB | 7022 | 1 | [HF](https://huggingface.co/mlx-community/DeepSeek-V4-Pro-4bit) |
| `mlx-community/gemma-4-26B-A4B-it-heretic-4bit` | 4-bit | 26B-A4B | 15.64 GB | 7015 | 19 | [HF](https://huggingface.co/mlx-community/gemma-4-26B-A4B-it-heretic-4bit) |
| `mlx-community/Qwen3-Coder-Next-4bit` | 4-bit |  | 44.86 GB | 6965 | 23 | [HF](https://huggingface.co/mlx-community/Qwen3-Coder-Next-4bit) |
| `deadbydawn101/gemma-4-E4B-Agentic-Opus-Reasoning-GeminiCLI-mlx-4bit` | 4-bit | 4B | 21.97 GB | 6858 | 24 | [HF](https://huggingface.co/deadbydawn101/gemma-4-E4B-Agentic-Opus-Reasoning-GeminiCLI-mlx-4bit) |
| `Jackrong/MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-4bit` | 4-bit | 27B | 15.15 GB | 6705 | 41 | [HF](https://huggingface.co/Jackrong/MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-4bit) |
| `mlx-community/DeepSeek-Coder-V2-Lite-Instruct-4bit-mlx` | 4-bit |  | 8.84 GB | 6659 | 17 | [HF](https://huggingface.co/mlx-community/DeepSeek-Coder-V2-Lite-Instruct-4bit-mlx) |
| `mlx-community/Qwen3.6-35B-A3B-OptiQ-4bit` | 4-bit | 35B-A3B | 44.93 GB | 6547 | 10 | [HF](https://huggingface.co/mlx-community/Qwen3.6-35B-A3B-OptiQ-4bit) |
| `unsloth/gemma-4-E4B-it-UD-MLX-4bit` | 4-bit | 4B | 12.2 GB | 6177 | 41 | [HF](https://huggingface.co/unsloth/gemma-4-E4B-it-UD-MLX-4bit) |
| `unsloth/Qwen3.6-35B-A3B-UD-MLX-3bit` | 3-bit | 35B-A3B | 17.39 GB | 6175 | 10 | [HF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-UD-MLX-3bit) |
| `mlx-community/DeepSeek-R1-Distill-Qwen-32B-4bit` | 4-bit | 32B | 18.44 GB | 5933 | 47 | [HF](https://huggingface.co/mlx-community/DeepSeek-R1-Distill-Qwen-32B-4bit) |
| `froggeric/Qwen3.6-35B-A3B-Uncensored-Heretic-MLX-4bit` | 4-bit | 35B-A3B | 20.42 GB | 5552 | 6 | [HF](https://huggingface.co/froggeric/Qwen3.6-35B-A3B-Uncensored-Heretic-MLX-4bit) |
| `mlx-community/Qwen3-Coder-30B-A3B-Instruct-4bit` | 4-bit | 30B-A3B | 34.37 GB | 5489 | 22 | [HF](https://huggingface.co/mlx-community/Qwen3-Coder-30B-A3B-Instruct-4bit) |
| `mlx-community/gemma-4-31B-it-OptiQ-4bit` | 4-bit | 31B | 41.4 GB | 5375 | 5 | [HF](https://huggingface.co/mlx-community/gemma-4-31B-it-OptiQ-4bit) |
| `mlx-community/Mistral-Medium-3.5-128B-4bit` | 4-bit | 128B | 78.04 GB | 5049 | 4 | [HF](https://huggingface.co/mlx-community/Mistral-Medium-3.5-128B-4bit) |
| `Jiunsong/supergemma4-26b-abliterated-multimodal-mlx-4bit` | 4-bit | 26B | 15.64 GB | 4965 | 57 | [HF](https://huggingface.co/Jiunsong/supergemma4-26b-abliterated-multimodal-mlx-4bit) |
| `mlx-community/deepseek-ai-DeepSeek-V4-Flash-4bit` | 4-bit |  | 160.14 GB | 4883 | 4 | [HF](https://huggingface.co/mlx-community/deepseek-ai-DeepSeek-V4-Flash-4bit) |
| `majentik/Qwen3.6-35B-A3B-TurboQuant-MLX-4bit` | 4-bit | 35B-A3B | 19.53 GB | 4763 | 10 | [HF](https://huggingface.co/majentik/Qwen3.6-35B-A3B-TurboQuant-MLX-4bit) |
| `mlx-community/Huihui-Qwen3.5-27B-Claude-4.6-Opus-abliterated-4bit` | 4-bit | 27B | 16.07 GB | 4664 | 18 | [HF](https://huggingface.co/mlx-community/Huihui-Qwen3.5-27B-Claude-4.6-Opus-abliterated-4bit) |
| `zecanard/gemma-4-E4B-it-ultra-uncensored-heretic-MLX-4bit-mixed_4_6` | 4-bit | 4B | 12.46 GB | 4453 | 5 | [HF](https://huggingface.co/zecanard/gemma-4-E4B-it-ultra-uncensored-heretic-MLX-4bit-mixed_4_6) |
| `mlx-community/Kimi-K2-Instruct-4bit` | 4-bit |  | 577.6 GB | 4154 | 13 | [HF](https://huggingface.co/mlx-community/Kimi-K2-Instruct-4bit) |
| `mlx-community/Qwen3-14B-4bit` | 4-bit | 14B | 16.63 GB | 4139 | 2 | [HF](https://huggingface.co/mlx-community/Qwen3-14B-4bit) |
| `froggeric/Qwen3.6-27B-Uncensored-Heretic-v2-MLX-4bit` | 4-bit | 27B | 32.13 GB | 4108 | 3 | [HF](https://huggingface.co/froggeric/Qwen3.6-27B-Uncensored-Heretic-v2-MLX-4bit) |
| `lmstudio-community/medgemma-27b-text-it-MLX-4bit` | 4-bit | 27B | 16.03 GB | 4085 | 3 | [HF](https://huggingface.co/lmstudio-community/medgemma-27b-text-it-MLX-4bit) |
| `Youssofal/Qwen3.6-27B-Abliterated-Heretic-Uncensored-MLX-4bit` | 4-bit | 27B | 19.66 GB | 4068 | 3 | [HF](https://huggingface.co/Youssofal/Qwen3.6-27B-Abliterated-Heretic-Uncensored-MLX-4bit) |
| `lmstudio-community/Qwen3-235B-A22B-Instruct-2507-MLX-4bit` | 4-bit | 235B-A22B | 132.25 GB | 4063 | 1 | [HF](https://huggingface.co/lmstudio-community/Qwen3-235B-A22B-Instruct-2507-MLX-4bit) |
| `lmstudio-community/GLM-4.7-Flash-MLX-4bit` | 4-bit |  | 33.75 GB | 3973 | 12 | [HF](https://huggingface.co/lmstudio-community/GLM-4.7-Flash-MLX-4bit) |
| `mlx-community/DeepSeek-V3.1-4bit` | 4-bit |  | 377.61 GB | 3917 | 6 | [HF](https://huggingface.co/mlx-community/DeepSeek-V3.1-4bit) |
| `coderavi/Qwen3.6-27B-mlx-4Bit` | 4-bit | 27B | 15.15 GB | 3863 | 0 | [HF](https://huggingface.co/coderavi/Qwen3.6-27B-mlx-4Bit) |

## Working Test Policy

- Exhaustive means every plausible MLX candidate is saved, not that every huge model must be downloaded immediately.
- Test all priority/edge and coding candidates that fit disk/time budget.
- Keep larger candidates as saved links for Mac Studio / GB10 comparison.
- Every live smoke should record load success, wall time, raw output, parser score, task score, and recommendation label.
- Do not equate model load success with usefulness; protocol discipline and deterministic task score are separate lanes.
