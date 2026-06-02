# HF MLX Expanded Next Queue - 2026-06-02

Source refresh: `data/model-candidates/hf-mlx-candidates-enriched-2026-06-02.json`

This queue expands the next milestone by searching Hugging Face again instead of only consuming the older May 30 catalog. Exact previously benchmarked model IDs, image-generation models, and obvious noisy/distilled merge variants are excluded.

## Lane Counts

- `text_core`: 12
- `reasoning_cleanup`: 7
- `coding_patch`: 5
- `vision_audio`: 6
- `embedding_rerank`: 4

## Recommended Order

### Text Core

| Model | Quant | Params | Storage | Downloads | Why |
| --- | --- | ---: | ---: | ---: | --- |
| [`lmstudio-community/LFM2.5-1.2B-Instruct-MLX-4bit`](https://huggingface.co/lmstudio-community/LFM2.5-1.2B-Instruct-MLX-4bit) | 4-bit | 1.2B | 0.66 GB | 116746 | Fresh text/core candidate for small-model-core before larger full-suite runs. |
| [`Qwen/Qwen3-4B-MLX-4bit`](https://huggingface.co/Qwen/Qwen3-4B-MLX-4bit) | 4-bit | 4B | 2.15 GB | 76586 | Fresh text/core candidate for small-model-core before larger full-suite runs. |
| [`mlx-community/Llama-3.2-1B-Instruct-4bit`](https://huggingface.co/mlx-community/Llama-3.2-1B-Instruct-4bit) | 4-bit | 1B | 1.41 GB | 58050 | Fresh text/core candidate for small-model-core before larger full-suite runs. |
| [`lmstudio-community/Qwen3-4B-Instruct-2507-MLX-8bit`](https://huggingface.co/lmstudio-community/Qwen3-4B-Instruct-2507-MLX-8bit) | 8-bit | 4B | 4.29 GB | 56437 | Fresh text/core candidate for small-model-core before larger full-suite runs. |
| [`lmstudio-community/Qwen3-14B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3-14B-MLX-4bit) | 4-bit | 14B | 8.32 GB | 51831 | Fresh text/core candidate for small-model-core before larger full-suite runs. |
| [`lmstudio-community/Qwen3-8B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3-8B-MLX-4bit) | 4-bit | 8B | 4.62 GB | 30875 | Fresh text/core candidate for small-model-core before larger full-suite runs. |
| [`mlx-community/LFM2.5-1.2B-Instruct-4bit`](https://huggingface.co/mlx-community/LFM2.5-1.2B-Instruct-4bit) | 4-bit | 1.2B | 0.66 GB | 25817 | Fresh text/core candidate for small-model-core before larger full-suite runs. |
| [`mlx-community/Qwen3-8B-4bit`](https://huggingface.co/mlx-community/Qwen3-8B-4bit) | 4-bit | 8B | 4.62 GB | 24480 | Fresh text/core candidate for small-model-core before larger full-suite runs. |
| [`lmstudio-community/LFM2-1.2B-MLX-8bit`](https://huggingface.co/lmstudio-community/LFM2-1.2B-MLX-8bit) | 8-bit | 1.2B | 1.24 GB | 24080 | Fresh text/core candidate for small-model-core before larger full-suite runs. |
| [`lmstudio-community/Qwen3-4B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3-4B-MLX-4bit) | 4-bit | 4B | 2.27 GB | 21662 | Fresh text/core candidate for small-model-core before larger full-suite runs. |
| [`mlx-community/Qwen3-0.6B-4bit`](https://huggingface.co/mlx-community/Qwen3-0.6B-4bit) | 4-bit | 0.6B | 0.68 GB | 20959 | Fresh text/core candidate for small-model-core before larger full-suite runs. |
| [`lmstudio-community/Qwen3-4B-MLX-8bit`](https://huggingface.co/lmstudio-community/Qwen3-4B-MLX-8bit) | 8-bit | 4B | 4.29 GB | 20959 | Fresh text/core candidate for small-model-core before larger full-suite runs. |

### Reasoning Cleanup

| Model | Quant | Params | Storage | Downloads | Why |
| --- | --- | ---: | ---: | ---: | --- |
| [`lmstudio-community/DeepSeek-R1-0528-Qwen3-8B-MLX-4bit`](https://huggingface.co/lmstudio-community/DeepSeek-R1-0528-Qwen3-8B-MLX-4bit) | 4-bit | 8B | 4.62 GB | 416219 | Reasoning/thinking variant; evaluate JSON cleanup and protocol leakage separately. |
| [`lmstudio-community/Qwen3-4B-Thinking-2507-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3-4B-Thinking-2507-MLX-4bit) | 4-bit | 4B | 2.27 GB | 62102 | Reasoning/thinking variant; evaluate JSON cleanup and protocol leakage separately. |
| [`lmstudio-community/Qwen3-4B-Thinking-2507-MLX-8bit`](https://huggingface.co/lmstudio-community/Qwen3-4B-Thinking-2507-MLX-8bit) | 8-bit | 4B | 4.29 GB | 60093 | Reasoning/thinking variant; evaluate JSON cleanup and protocol leakage separately. |
| [`mlx-community/DeepSeek-R1-Distill-Qwen-7B-4bit`](https://huggingface.co/mlx-community/DeepSeek-R1-Distill-Qwen-7B-4bit) | 4-bit | 7B | 8.58 GB | 3437 | Reasoning/thinking variant; evaluate JSON cleanup and protocol leakage separately. |
| [`mlx-community/DeepSeek-R1-Distill-Qwen-1.5B-4bit`](https://huggingface.co/mlx-community/DeepSeek-R1-Distill-Qwen-1.5B-4bit) | 4-bit | 1.5B | 2.01 GB | 3413 | Reasoning/thinking variant; evaluate JSON cleanup and protocol leakage separately. |
| [`lmstudio-community/LFM2.5-1.2B-Thinking-MLX-8bit`](https://huggingface.co/lmstudio-community/LFM2.5-1.2B-Thinking-MLX-8bit) | 8-bit | 1.2B | 1.24 GB | 2550 | Reasoning/thinking variant; evaluate JSON cleanup and protocol leakage separately. |
| [`mlx-community/DeepSeek-R1-Distill-Qwen-14B-4bit`](https://huggingface.co/mlx-community/DeepSeek-R1-Distill-Qwen-14B-4bit) | 4-bit | 14B | 8.32 GB | 2522 | Reasoning/thinking variant; evaluate JSON cleanup and protocol leakage separately. |

### Coding Patch

| Model | Quant | Params | Storage | Downloads | Why |
| --- | --- | ---: | ---: | ---: | --- |
| [`lmstudio-community/Phi-4-reasoning-plus-MLX-4bit`](https://huggingface.co/lmstudio-community/Phi-4-reasoning-plus-MLX-4bit) | 4-bit |  | 8.25 GB | 32610 | Coding or patch candidate; route to compiler-backed coding lane, not factual leaderboard first. |
| [`lmstudio-community/Qwen2.5-Coder-7B-Instruct-MLX-8bit`](https://huggingface.co/lmstudio-community/Qwen2.5-Coder-7B-Instruct-MLX-8bit) | 8-bit | 7B | 8.1 GB | 5977 | Coding or patch candidate; route to compiler-backed coding lane, not factual leaderboard first. |
| [`lmstudio-community/Qwen2.5-Coder-1.5B-Instruct-MLX-8bit`](https://huggingface.co/lmstudio-community/Qwen2.5-Coder-1.5B-Instruct-MLX-8bit) | 8-bit | 1.5B | 1.65 GB | 5906 | Coding or patch candidate; route to compiler-backed coding lane, not factual leaderboard first. |
| [`mlx-community/Qwen2.5-Coder-14B-Instruct-4bit`](https://huggingface.co/mlx-community/Qwen2.5-Coder-14B-Instruct-4bit) | 4-bit | 14B | 8.31 GB | 2884 | Coding or patch candidate; route to compiler-backed coding lane, not factual leaderboard first. |
| [`lmstudio-community/Qwen2.5-Coder-1.5B-Instruct-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen2.5-Coder-1.5B-Instruct-MLX-4bit) | 4-bit | 1.5B | 0.88 GB | 2260 | Coding or patch candidate; route to compiler-backed coding lane, not factual leaderboard first. |

### Vision Audio

| Model | Quant | Params | Storage | Downloads | Why |
| --- | --- | ---: | ---: | ---: | --- |
| [`lmstudio-community/Qwen3-VL-4B-Instruct-MLX-8bit`](https://huggingface.co/lmstudio-community/Qwen3-VL-4B-Instruct-MLX-8bit) | 8-bit | 4B | 5.12 GB | 146381 | Fits memory but belongs to future VLM/ASR lane, not text-only scoring. |
| [`lmstudio-community/Qwen3-VL-4B-Instruct-MLX-5bit`](https://huggingface.co/lmstudio-community/Qwen3-VL-4B-Instruct-MLX-5bit) | 5-bit | 4B | 3.61 GB | 145971 | Fits memory but belongs to future VLM/ASR lane, not text-only scoring. |
| [`lmstudio-community/Qwen3-VL-4B-Instruct-MLX-6bit`](https://huggingface.co/lmstudio-community/Qwen3-VL-4B-Instruct-MLX-6bit) | 6-bit | 4B | 4.11 GB | 145855 | Fits memory but belongs to future VLM/ASR lane, not text-only scoring. |
| [`mlx-community/gemma-3-4b-it-qat-4bit`](https://huggingface.co/mlx-community/gemma-3-4b-it-qat-4bit) | 4-bit | 4b | 6.43 GB | 121238 | Fits memory but belongs to future VLM/ASR lane, not text-only scoring. |
| [`lmstudio-community/Qwen3-VL-8B-Instruct-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3-VL-8B-Instruct-MLX-4bit) | 4-bit | 8B | 5.77 GB | 107927 | Fits memory but belongs to future VLM/ASR lane, not text-only scoring. |
| [`lmstudio-community/Qwen3-VL-8B-Instruct-MLX-5bit`](https://huggingface.co/lmstudio-community/Qwen3-VL-8B-Instruct-MLX-5bit) | 5-bit | 8B | 6.8 GB | 98181 | Fits memory but belongs to future VLM/ASR lane, not text-only scoring. |

### Embedding Rerank

| Model | Quant | Params | Storage | Downloads | Why |
| --- | --- | ---: | ---: | ---: | --- |
| [`mlx-community/Qwen3-Embedding-0.6B-4bit-DWQ`](https://huggingface.co/mlx-community/Qwen3-Embedding-0.6B-4bit-DWQ) | 4-bit | 0.6B | 0.35 GB | 17354 | Separate embedding/rerank lane candidate. |
| [`mlx-community/Qwen3-Embedding-4B-4bit-DWQ`](https://huggingface.co/mlx-community/Qwen3-Embedding-4B-4bit-DWQ) | 4-bit | 4B | 2.27 GB | 4131 | Separate embedding/rerank lane candidate. |
| [`mlx-community/Qwen3-Embedding-8B-4bit-DWQ`](https://huggingface.co/mlx-community/Qwen3-Embedding-8B-4bit-DWQ) | 4-bit | 8B | 4.27 GB | 2841 | Separate embedding/rerank lane candidate. |
| [`mlx-community/nomicai-modernbert-embed-base-4bit`](https://huggingface.co/mlx-community/nomicai-modernbert-embed-base-4bit) | 4-bit |  | 0.08 GB | 2498 | Separate embedding/rerank lane candidate. |
