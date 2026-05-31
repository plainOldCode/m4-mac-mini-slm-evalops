# Hugging Face MLX Candidate Refresh - 2026-05-31

Generated from Hugging Face API searches across MLX, quantization, model-family, coding, VLM, and low-bit terms.

- Raw pool: `data/model-candidates/hf-mlx-candidates-raw-2026-05-31.json`
- Enriched pool: `data/model-candidates/hf-mlx-candidates-enriched-2026-05-31.json`
- CSV: `data/model-candidates/hf-mlx-candidates-m4-16gb-2026-05-31.csv`
- Enriched candidate count: `420`
- Storage is Hugging Face repository `usedStorage`, not guaranteed peak runtime memory.
- M4 16GB labels are practical routing labels, not pass/fail judgments.

## Category Counts

- `coding_edge_candidate`: 5
- `coding_later_hardware_candidate`: 17
- `coding_m4_16gb_candidate`: 12
- `embedding_or_rerank_lane`: 5
- `image_generation_lane`: 1
- `larger_later_hardware_candidate`: 247
- `text_m4_16gb_edge_candidate`: 9
- `text_m4_16gb_priority_candidate`: 72
- `vision_audio_later_candidate`: 16
- `vision_audio_m4_16gb_candidate`: 36

## Text Priority For M4 16GB

| Model | Quant | Params | Storage GB | Downloads | Likes | Last Modified |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| [`lmstudio-community/DeepSeek-R1-0528-Qwen3-8B-MLX-4bit`](https://huggingface.co/lmstudio-community/DeepSeek-R1-0528-Qwen3-8B-MLX-4bit) | 4-bit | 8B | 4.62 | 424303 | 12 | 2025-05-29 |
| [`lmstudio-community/LFM2.5-1.2B-Instruct-MLX-8bit`](https://huggingface.co/lmstudio-community/LFM2.5-1.2B-Instruct-MLX-8bit) | 8-bit | 1.2B | 1.24 | 118921 | 2 | 2026-01-07 |
| [`lmstudio-community/LFM2.5-1.2B-Instruct-MLX-4bit`](https://huggingface.co/lmstudio-community/LFM2.5-1.2B-Instruct-MLX-4bit) | 4-bit | 1.2B | 0.66 | 117004 | 1 | 2026-01-07 |
| [`lmstudio-community/LFM2.5-1.2B-Instruct-MLX-6bit`](https://huggingface.co/lmstudio-community/LFM2.5-1.2B-Instruct-MLX-6bit) | 6-bit | 1.2B | 0.95 | 116576 | 4 | 2026-01-07 |
| [`mlx-community/gemma-4-e2b-it-4bit`](https://huggingface.co/mlx-community/gemma-4-e2b-it-4bit) | 4-bit |  | 3.61 | 81174 | 16 | 2026-05-19 |
| [`Qwen/Qwen3-4B-MLX-4bit`](https://huggingface.co/Qwen/Qwen3-4B-MLX-4bit) | 4-bit | 4B | 2.15 | 76601 | 31 | 2025-08-29 |
| [`lmstudio-community/Qwen3-4B-Thinking-2507-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3-4B-Thinking-2507-MLX-4bit) | 4-bit | 4B | 2.27 | 62795 | 12 | 2025-08-06 |
| [`lmstudio-community/Qwen3-4B-Thinking-2507-MLX-8bit`](https://huggingface.co/lmstudio-community/Qwen3-4B-Thinking-2507-MLX-8bit) | 8-bit | 4B | 4.29 | 60780 | 7 | 2025-08-06 |
| [`lmstudio-community/Qwen3-4B-Thinking-2507-MLX-6bit`](https://huggingface.co/lmstudio-community/Qwen3-4B-Thinking-2507-MLX-6bit) | 6-bit | 4B | 3.28 | 60190 | 2 | 2025-08-06 |
| [`mlx-community/Llama-3.2-1B-Instruct-4bit`](https://huggingface.co/mlx-community/Llama-3.2-1B-Instruct-4bit) | 4-bit | 1B | 1.41 | 59208 | 19 | 2025-03-05 |
| [`lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit) | 4-bit | 4B | 2.27 | 58213 | 3 | 2025-08-06 |
| [`mlx-community/gemma-3-1b-it-qat-4bit`](https://huggingface.co/mlx-community/gemma-3-1b-it-qat-4bit) | 4-bit | 1b | 0.77 | 57501 | 4 | 2025-04-18 |
| [`lmstudio-community/Qwen3-4B-Instruct-2507-MLX-8bit`](https://huggingface.co/lmstudio-community/Qwen3-4B-Instruct-2507-MLX-8bit) | 8-bit | 4B | 4.29 | 56695 | 1 | 2025-08-06 |
| [`lmstudio-community/Qwen3-4B-Instruct-2507-MLX-6bit`](https://huggingface.co/lmstudio-community/Qwen3-4B-Instruct-2507-MLX-6bit) | 6-bit | 4B | 3.28 | 56040 | 0 | 2025-08-06 |
| [`lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit`](https://huggingface.co/lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit) | 5-bit | 4B | 2.78 | 55990 | 0 | 2025-08-06 |
| [`mlx-community/gemma-4-e4b-it-4bit`](https://huggingface.co/mlx-community/gemma-4-e4b-it-4bit) | 4-bit |  | 5.25 | 39254 | 25 | 2026-05-19 |
| [`lmstudio-community/Qwen3-8B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3-8B-MLX-4bit) | 4-bit | 8B | 4.62 | 30723 | 3 | 2025-04-28 |
| [`lmstudio-community/Qwen3-1.7B-MLX-8bit`](https://huggingface.co/lmstudio-community/Qwen3-1.7B-MLX-8bit) | 8-bit | 1.7B | 1.84 | 30072 | 1 | 2025-04-28 |
| [`mlx-community/Josiefied-Qwen3-8B-abliterated-v1-4bit`](https://huggingface.co/mlx-community/Josiefied-Qwen3-8B-abliterated-v1-4bit) | 4-bit | 8B | 4.62 | 29939 | 5 | 2025-05-01 |
| [`lmstudio-community/Qwen3-1.7B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3-1.7B-MLX-4bit) | 4-bit | 1.7B | 0.98 | 29300 | 0 | 2025-04-28 |
| [`mlx-community/Qwen3-1.7B-4bit`](https://huggingface.co/mlx-community/Qwen3-1.7B-4bit) | 4-bit | 1.7B | 0.98 | 28359 | 4 | 2025-04-28 |
| [`mlx-community/LFM2.5-1.2B-Instruct-4bit`](https://huggingface.co/mlx-community/LFM2.5-1.2B-Instruct-4bit) | 4-bit | 1.2B | 0.66 | 27111 | 1 | 2026-01-06 |
| [`mlx-community/gemma-2-9b-it-4bit`](https://huggingface.co/mlx-community/gemma-2-9b-it-4bit) | 4-bit | 9b | 5.22 | 25851 | 2 | 2024-11-06 |
| [`mlx-community/Llama-3.2-3B-Instruct-4bit`](https://huggingface.co/mlx-community/Llama-3.2-3B-Instruct-4bit) | 4-bit | 3B | 5.44 | 25735 | 43 | 2025-03-05 |
| [`lmstudio-community/LFM2-1.2B-MLX-8bit`](https://huggingface.co/lmstudio-community/LFM2-1.2B-MLX-8bit) | 8-bit | 1.2B | 1.24 | 24074 | 4 | 2025-07-22 |
| [`lmstudio-community/Qwen3-4B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3-4B-MLX-4bit) | 4-bit | 4B | 2.27 | 21872 | 1 | 2025-04-28 |
| [`mlx-community/Qwen3-0.6B-4bit`](https://huggingface.co/mlx-community/Qwen3-0.6B-4bit) | 4-bit | 0.6B | 0.68 | 21288 | 12 | 2025-04-28 |
| [`lmstudio-community/Qwen3-4B-MLX-8bit`](https://huggingface.co/lmstudio-community/Qwen3-4B-MLX-8bit) | 8-bit | 4B | 4.29 | 21178 | 0 | 2025-04-28 |
| [`mlx-community/Qwen3-4B-Instruct-2507-4bit`](https://huggingface.co/mlx-community/Qwen3-4B-Instruct-2507-4bit) | 4-bit | 4B | 2.27 | 20890 | 9 | 2026-01-02 |
| [`mlx-community/Qwen3.5-9B-4bit`](https://huggingface.co/mlx-community/Qwen3.5-9B-4bit) | 4-bit | 9B | 5.97 | 20689 | 10 | 2026-03-02 |
| [`mlx-community/Qwen3-8B-4bit`](https://huggingface.co/mlx-community/Qwen3-8B-4bit) | 4-bit | 8B | 4.62 | 20682 | 9 | 2025-04-28 |
| [`mlx-community/Qwen3-0.6B-8bit`](https://huggingface.co/mlx-community/Qwen3-0.6B-8bit) | 8-bit | 0.6B | 0.64 | 17663 | 7 | 2025-05-04 |
| [`mlx-community/Qwen3.5-4B-4bit`](https://huggingface.co/mlx-community/Qwen3.5-4B-4bit) | 4-bit | 4B | 3.05 | 17179 | 6 | 2026-03-02 |
| [`mlx-community/Qwen2.5-3B-Instruct-4bit`](https://huggingface.co/mlx-community/Qwen2.5-3B-Instruct-4bit) | 4-bit | 3B | 1.74 | 16417 | 1 | 2024-09-18 |
| [`mlx-community/Qwen2.5-0.5B-Instruct-4bit`](https://huggingface.co/mlx-community/Qwen2.5-0.5B-Instruct-4bit) | 4-bit | 0.5B | 0.28 | 14465 | 7 | 2024-09-18 |
| [`mlx-community/Qwen2.5-7B-Instruct-4bit`](https://huggingface.co/mlx-community/Qwen2.5-7B-Instruct-4bit) | 4-bit | 7B | 4.28 | 13410 | 15 | 2024-11-06 |
| [`lmstudio-community/Qwen2.5-0.5B-Instruct-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen2.5-0.5B-Instruct-MLX-4bit) | 4-bit | 0.5B | 0.29 | 13002 | 1 | 2024-11-13 |
| [`mlx-community/Qwen3-4B-4bit`](https://huggingface.co/mlx-community/Qwen3-4B-4bit) | 4-bit | 4B | 2.27 | 12964 | 12 | 2025-04-28 |
| [`mlx-community/Qwen1.5-0.5B-Chat-4bit`](https://huggingface.co/mlx-community/Qwen1.5-0.5B-Chat-4bit) | 4-bit | 0.5B | 2.07 | 12856 | 4 | 2024-04-18 |
| [`mlx-community/Mistral-7B-Instruct-v0.3-4bit`](https://huggingface.co/mlx-community/Mistral-7B-Instruct-v0.3-4bit) | 4-bit | 7B | 4.08 | 12470 | 10 | 2024-06-18 |

## Coding Candidates For M4 16GB

| Model | Quant | Params | Storage GB | Downloads | Likes | Last Modified |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| [`lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit) | 4-bit | 14B | 8.32 | 163911 | 6 | 2024-11-13 |
| [`lmstudio-community/Phi-4-mini-reasoning-MLX-4bit`](https://huggingface.co/lmstudio-community/Phi-4-mini-reasoning-MLX-4bit) | 4-bit |  | 2.17 | 59134 | 3 | 2025-05-01 |
| [`lmstudio-community/Phi-4-reasoning-plus-MLX-4bit`](https://huggingface.co/lmstudio-community/Phi-4-reasoning-plus-MLX-4bit) | 4-bit |  | 8.25 | 32888 | 1 | 2025-05-01 |
| [`lmstudio-community/Qwen2.5-Coder-7B-Instruct-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen2.5-Coder-7B-Instruct-MLX-4bit) | 4-bit | 7B | 4.30 | 20418 | 5 | 2024-11-13 |
| [`mlx-community/Qwen2.5-Coder-7B-Instruct-4bit`](https://huggingface.co/mlx-community/Qwen2.5-Coder-7B-Instruct-4bit) | 4-bit | 7B | 4.28 | 8284 | 14 | 2024-09-18 |
| [`lmstudio-community/Qwen2.5-Coder-7B-Instruct-MLX-8bit`](https://huggingface.co/lmstudio-community/Qwen2.5-Coder-7B-Instruct-MLX-8bit) | 8-bit | 7B | 8.10 | 6133 | 1 | 2024-11-13 |
| [`lmstudio-community/Qwen2.5-Coder-1.5B-Instruct-MLX-8bit`](https://huggingface.co/lmstudio-community/Qwen2.5-Coder-1.5B-Instruct-MLX-8bit) | 8-bit | 1.5B | 1.65 | 5851 | 1 | 2024-11-13 |
| [`lmstudio-community/Qwen2.5-Coder-3B-Instruct-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen2.5-Coder-3B-Instruct-MLX-4bit) | 4-bit | 3B | 1.75 | 4331 | 1 | 2024-11-13 |
| [`mlx-community/Phi-4-mini-instruct-4bit`](https://huggingface.co/mlx-community/Phi-4-mini-instruct-4bit) | 4-bit |  | 2.17 | 3410 | 1 | 2025-03-05 |
| [`mlx-community/Qwen2.5-Coder-14B-Instruct-4bit`](https://huggingface.co/mlx-community/Qwen2.5-Coder-14B-Instruct-4bit) | 4-bit | 14B | 8.31 | 2827 | 8 | 2024-11-11 |
| [`mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit`](https://huggingface.co/mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit) | 4-bit | 1.5B | 0.87 | 2500 | 2 | 2024-09-18 |
| [`lmstudio-community/Qwen2.5-Coder-1.5B-Instruct-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen2.5-Coder-1.5B-Instruct-MLX-4bit) | 4-bit | 1.5B | 0.88 | 2248 | 0 | 2024-11-13 |

## Vision / Audio Candidates For M4 16GB

| Model | Quant | Params | Storage GB | Downloads | Likes | Last Modified |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| [`lmstudio-community/Qwen3-VL-4B-Instruct-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3-VL-4B-Instruct-MLX-4bit) | 4-bit | 4B | 3.11 | 152431 | 7 | 2025-10-28 |
| [`lmstudio-community/Qwen3-VL-4B-Instruct-MLX-8bit`](https://huggingface.co/lmstudio-community/Qwen3-VL-4B-Instruct-MLX-8bit) | 8-bit | 4B | 5.12 | 147751 | 1 | 2025-10-28 |
| [`lmstudio-community/Qwen3-VL-4B-Instruct-MLX-5bit`](https://huggingface.co/lmstudio-community/Qwen3-VL-4B-Instruct-MLX-5bit) | 5-bit | 4B | 3.61 | 147327 | 0 | 2025-10-28 |
| [`lmstudio-community/Qwen3-VL-4B-Instruct-MLX-6bit`](https://huggingface.co/lmstudio-community/Qwen3-VL-4B-Instruct-MLX-6bit) | 6-bit | 4B | 4.11 | 147194 | 0 | 2025-10-28 |
| [`mlx-community/gemma-3-4b-it-qat-4bit`](https://huggingface.co/mlx-community/gemma-3-4b-it-qat-4bit) | 4-bit | 4b | 6.43 | 123035 | 9 | 2025-04-21 |
| [`lmstudio-community/Qwen3-VL-8B-Instruct-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3-VL-8B-Instruct-MLX-4bit) | 4-bit | 8B | 5.77 | 108207 | 4 | 2025-10-28 |
| [`aufklarer/Qwen3-ASR-0.6B-MLX-4bit`](https://huggingface.co/aufklarer/Qwen3-ASR-0.6B-MLX-4bit) | 4-bit | 0.6B | 0.71 | 105521 | 3 | 2026-04-12 |
| [`lmstudio-community/Qwen3-VL-8B-Instruct-MLX-5bit`](https://huggingface.co/lmstudio-community/Qwen3-VL-8B-Instruct-MLX-5bit) | 5-bit | 8B | 6.80 | 98485 | 0 | 2025-10-28 |
| [`lmstudio-community/Qwen3-VL-8B-Instruct-MLX-6bit`](https://huggingface.co/lmstudio-community/Qwen3-VL-8B-Instruct-MLX-6bit) | 6-bit | 8B | 7.82 | 98336 | 0 | 2025-10-28 |
| [`mlx-community/Qwen3.5-9B-MLX-4bit`](https://huggingface.co/mlx-community/Qwen3.5-9B-MLX-4bit) | 4-bit | 9B | 5.97 | 50748 | 125 | 2026-03-23 |
| [`mlx-community/Qwen3.5-4B-MLX-4bit`](https://huggingface.co/mlx-community/Qwen3.5-4B-MLX-4bit) | 4-bit | 4B | 3.05 | 28361 | 21 | 2026-03-02 |
| [`mlx-community/Ministral-3-3B-Instruct-2512-4bit`](https://huggingface.co/mlx-community/Ministral-3-3B-Instruct-2512-4bit) | 4-bit | 3B | 4.71 | 21870 | 5 | 2025-12-03 |
| [`mlx-community/Qwen2-VL-7B-Instruct-4bit`](https://huggingface.co/mlx-community/Qwen2-VL-7B-Instruct-4bit) | 4-bit | 7B | 4.68 | 20247 | 2 | 2025-03-24 |
| [`mlx-community/Qwen3-VL-4B-Instruct-4bit`](https://huggingface.co/mlx-community/Qwen3-VL-4B-Instruct-4bit) | 4-bit | 4B | 3.11 | 13914 | 7 | 2025-10-16 |
| [`mlx-community/Qwen3.5-0.8B-MLX-4bit`](https://huggingface.co/mlx-community/Qwen3.5-0.8B-MLX-4bit) | 4-bit | 0.8B | 0.65 | 8550 | 4 | 2026-03-02 |
| [`deadbydawn101/gemma-4-E2B-Heretic-Uncensored-mlx-4bit`](https://huggingface.co/deadbydawn101/gemma-4-E2B-Heretic-Uncensored-mlx-4bit) | 4-bit |  | 3.61 | 6653 | 15 | 2026-04-09 |
| [`mlx-community/gemma-3n-E2B-it-lm-4bit`](https://huggingface.co/mlx-community/gemma-3n-E2B-it-lm-4bit) | 4-bit |  | 2.55 | 6397 | 3 | 2025-06-29 |
| [`mlx-community/LFM2-VL-1.6B-4bit`](https://huggingface.co/mlx-community/LFM2-VL-1.6B-4bit) | 4-bit | 1.6B | 1.46 | 6054 | 1 | 2025-08-16 |
| [`mlx-community/LFM2.5-VL-1.6B-4bit`](https://huggingface.co/mlx-community/LFM2.5-VL-1.6B-4bit) | 4-bit | 1.6B | 1.49 | 5124 | 3 | 2026-01-06 |
| [`aufklarer/Qwen3-ASR-1.7B-MLX-8bit`](https://huggingface.co/aufklarer/Qwen3-ASR-1.7B-MLX-8bit) | 8-bit | 1.7B | 2.46 | 4545 | 3 | 2026-04-12 |
| [`mlx-community/Qwen2-VL-2B-Instruct-4bit`](https://huggingface.co/mlx-community/Qwen2-VL-2B-Instruct-4bit) | 4-bit | 2B | 1.26 | 4164 | 6 | 2025-03-24 |
| [`mlx-community/Qwen3-TTS-12Hz-1.7B-CustomVoice-8bit`](https://huggingface.co/mlx-community/Qwen3-TTS-12Hz-1.7B-CustomVoice-8bit) | 8-bit | 1.7B | 5.11 | 4124 | 24 | 2026-01-26 |
| [`mlx-community/Qwen2.5-VL-7B-Instruct-4bit`](https://huggingface.co/mlx-community/Qwen2.5-VL-7B-Instruct-4bit) | 4-bit | 7B | 5.65 | 3890 | 4 | 2025-02-25 |
| [`aufklarer/Qwen3-ASR-0.6B-MLX-8bit`](https://huggingface.co/aufklarer/Qwen3-ASR-0.6B-MLX-8bit) | 8-bit | 0.6B | 1.01 | 3563 | 1 | 2026-04-12 |
| [`bigatuna/Qwen3.5-9b-Sushi-Coder-RL-MLX`](https://huggingface.co/bigatuna/Qwen3.5-9b-Sushi-Coder-RL-MLX) | 4-bit | 9b | 5.97 | 3362 | 14 | 2026-03-27 |

## Text Edge For M4 16GB

| Model | Quant | Params | Storage GB | Downloads | Likes | Last Modified |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| [`lmstudio-community/GLM-4.6V-Flash-MLX-4bit`](https://huggingface.co/lmstudio-community/GLM-4.6V-Flash-MLX-4bit) | 4-bit |  | 7.09 | 130398 | 2 | 2025-12-08 |
| [`lmstudio-community/Qwen3-14B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3-14B-MLX-4bit) | 4-bit | 14B | 8.32 | 51477 | 6 | 2025-04-28 |
| [`mlx-community/Qwen2.5-14B-Instruct-4bit`](https://huggingface.co/mlx-community/Qwen2.5-14B-Instruct-4bit) | 4-bit | 14B | 8.31 | 15921 | 11 | 2024-09-18 |
| [`mlx-community/Mistral-Nemo-Instruct-2407-4bit`](https://huggingface.co/mlx-community/Mistral-Nemo-Instruct-2407-4bit) | 4-bit |  | 6.89 | 6980 | 15 | 2024-11-06 |
| [`mlx-community/gemma-4-E4B-it-OBLITERATED-mlx-8Bit`](https://huggingface.co/mlx-community/gemma-4-E4B-it-OBLITERATED-mlx-8Bit) | 8-bit |  | 8.02 | 5261 | 3 | 2026-05-19 |
| [`mlx-community/gemma-3-4b-it-4bit`](https://huggingface.co/mlx-community/gemma-3-4b-it-4bit) | 4-bit | 4b | 6.84 | 3728 | 7 | 2025-03-21 |
| [`lmstudio-community/Qwen2.5-14B-Instruct-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen2.5-14B-Instruct-MLX-4bit) | 4-bit | 14B | 8.32 | 3221 | 1 | 2024-11-13 |
| [`Jackrong/MLX-Qwen3.5-9B-DeepSeek-V4-Flash-6bit`](https://huggingface.co/Jackrong/MLX-Qwen3.5-9B-DeepSeek-V4-Flash-6bit) | 6-bit | 9B | 7.30 | 2657 | 2 | 2026-04-30 |
| [`mlx-community/DeepSeek-R1-Distill-Qwen-14B-4bit`](https://huggingface.co/mlx-community/DeepSeek-R1-Distill-Qwen-14B-4bit) | 4-bit | 14B | 8.32 | 2510 | 9 | 2025-02-26 |

## Embedding / Rerank Lane

| Model | Quant | Params | Storage GB | Downloads | Likes | Last Modified |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| [`mlx-community/Qwen3-Embedding-0.6B-4bit-DWQ`](https://huggingface.co/mlx-community/Qwen3-Embedding-0.6B-4bit-DWQ) | 4-bit | 0.6B | 0.35 | 17659 | 8 | 2025-06-06 |
| [`mlx-community/Qwen3-Embedding-4B-4bit-DWQ`](https://huggingface.co/mlx-community/Qwen3-Embedding-4B-4bit-DWQ) | 4-bit | 4B | 2.27 | 3990 | 9 | 2025-06-07 |
| [`mlx-community/Qwen3-Embedding-8B-4bit-DWQ`](https://huggingface.co/mlx-community/Qwen3-Embedding-8B-4bit-DWQ) | 4-bit | 8B | 4.27 | 2857 | 8 | 2025-06-23 |
| [`mlx-community/embeddinggemma-300m-6bit`](https://huggingface.co/mlx-community/embeddinggemma-300m-6bit) | 6-bit |  | 0.29 | 2824 | 1 | 2025-09-04 |
| [`mlx-community/nomicai-modernbert-embed-base-4bit`](https://huggingface.co/mlx-community/nomicai-modernbert-embed-base-4bit) | 4-bit |  | 0.08 | 2570 | 0 | 2025-04-02 |

## Larger / Later Hardware

| Model | Quant | Params | Storage GB | Downloads | Likes | Last Modified |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| [`lmstudio-community/DeepSeek-R1-0528-Qwen3-8B-MLX-8bit`](https://huggingface.co/lmstudio-community/DeepSeek-R1-0528-Qwen3-8B-MLX-8bit) | 8-bit | 8B | 8.71 | 375803 | 18 | 2025-05-29 |
| [`lmstudio-community/LFM2-24B-A2B-MLX-4bit`](https://huggingface.co/lmstudio-community/LFM2-24B-A2B-MLX-4bit) | 4-bit | 24B-A2B | 13.42 | 331561 | 4 | 2026-02-23 |
| [`lmstudio-community/LFM2-24B-A2B-MLX-8bit`](https://huggingface.co/lmstudio-community/LFM2-24B-A2B-MLX-8bit) | 8-bit | 24B-A2B | 25.33 | 328121 | 2 | 2026-02-23 |
| [`lmstudio-community/LFM2-24B-A2B-MLX-5bit`](https://huggingface.co/lmstudio-community/LFM2-24B-A2B-MLX-5bit) | 5-bit | 24B-A2B | 16.39 | 327915 | 1 | 2026-02-23 |
| [`lmstudio-community/LFM2-24B-A2B-MLX-6bit`](https://huggingface.co/lmstudio-community/LFM2-24B-A2B-MLX-6bit) | 6-bit | 24B-A2B | 19.37 | 327831 | 3 | 2026-02-23 |
| [`mlx-community/Qwen3.5-9B-OptiQ-4bit`](https://huggingface.co/mlx-community/Qwen3.5-9B-OptiQ-4bit) | 4-bit | 9B | 13.35 | 221333 | 46 | 2026-05-26 |
| [`lmstudio-community/GLM-4.7-Flash-MLX-8bit`](https://huggingface.co/lmstudio-community/GLM-4.7-Flash-MLX-8bit) | 8-bit |  | 63.34 | 220258 | 11 | 2026-01-22 |
| [`lmstudio-community/GLM-4.7-Flash-MLX-6bit`](https://huggingface.co/lmstudio-community/GLM-4.7-Flash-MLX-6bit) | 6-bit |  | 48.71 | 210549 | 8 | 2026-01-22 |
| [`lmstudio-community/Qwen3-Coder-30B-A3B-Instruct-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3-Coder-30B-A3B-Instruct-MLX-4bit) | 4-bit | 30B-A3B | 17.19 | 201617 | 30 | 2025-07-31 |
| [`lmstudio-community/Qwen3-Coder-30B-A3B-Instruct-MLX-5bit`](https://huggingface.co/lmstudio-community/Qwen3-Coder-30B-A3B-Instruct-MLX-5bit) | 5-bit | 30B-A3B | 21.00 | 169078 | 8 | 2025-08-01 |
| [`lmstudio-community/Qwen3-Coder-30B-A3B-Instruct-MLX-8bit`](https://huggingface.co/lmstudio-community/Qwen3-Coder-30B-A3B-Instruct-MLX-8bit) | 8-bit | 30B-A3B | 32.45 | 168754 | 17 | 2025-07-31 |
| [`lmstudio-community/Qwen3-Coder-30B-A3B-Instruct-MLX-6bit`](https://huggingface.co/lmstudio-community/Qwen3-Coder-30B-A3B-Instruct-MLX-6bit) | 6-bit | 30B-A3B | 24.82 | 164992 | 5 | 2025-07-31 |
| [`mlx-community/Devstral-Small-2-24B-Instruct-2512-4bit`](https://huggingface.co/mlx-community/Devstral-Small-2-24B-Instruct-2512-4bit) | 4-bit | 24B | 14.14 | 154715 | 4 | 2025-12-10 |
| [`lmstudio-community/GLM-4.6V-Flash-MLX-8bit`](https://huggingface.co/lmstudio-community/GLM-4.6V-Flash-MLX-8bit) | 8-bit |  | 11.79 | 128037 | 1 | 2025-12-08 |
| [`lmstudio-community/GLM-4.6V-Flash-MLX-6bit`](https://huggingface.co/lmstudio-community/GLM-4.6V-Flash-MLX-6bit) | 6-bit |  | 9.44 | 126968 | 0 | 2025-12-08 |
| [`unsloth/Qwen3.6-35B-A3B-UD-MLX-4bit`](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-UD-MLX-4bit) | 4-bit | 35B-A3B | 43.07 | 125087 | 81 | 2026-04-20 |
| [`mlx-community/Qwen3.5-27B-4bit`](https://huggingface.co/mlx-community/Qwen3.5-27B-4bit) | 4-bit | 27B | 16.07 | 96628 | 47 | 2026-02-24 |
| [`mlx-community/Qwen3.6-35B-A3B-4bit`](https://huggingface.co/mlx-community/Qwen3.6-35B-A3B-4bit) | 4-bit | 35B-A3B | 20.42 | 93305 | 58 | 2026-04-16 |
| [`lmstudio-community/Hermes-4-70B-MLX-4bit`](https://huggingface.co/lmstudio-community/Hermes-4-70B-MLX-4bit) | 4-bit | 70B | 39.71 | 86032 | 3 | 2025-08-26 |
| [`lmstudio-community/NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-4bit`](https://huggingface.co/lmstudio-community/NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-4bit) | 4-bit | 30B-A3B | 17.79 | 82478 | 2 | 2025-12-16 |
| [`mlx-community/Qwen3-30B-A3B-4bit`](https://huggingface.co/mlx-community/Qwen3-30B-A3B-4bit) | 4-bit | 30B-A3B | 17.19 | 79309 | 15 | 2025-04-29 |
| [`lmstudio-community/Hermes-4-70B-MLX-8bit`](https://huggingface.co/lmstudio-community/Hermes-4-70B-MLX-8bit) | 8-bit | 70B | 74.98 | 79000 | 1 | 2025-08-26 |
| [`lmstudio-community/Hermes-4-70B-MLX-6bit`](https://huggingface.co/lmstudio-community/Hermes-4-70B-MLX-6bit) | 6-bit | 70B | 57.34 | 78266 | 1 | 2025-08-26 |
| [`lmstudio-community/Hermes-4-70B-MLX-5bit`](https://huggingface.co/lmstudio-community/Hermes-4-70B-MLX-5bit) | 5-bit | 70B | 48.52 | 77908 | 0 | 2025-08-26 |
| [`mlx-community/Qwen3.6-35B-A3B-8bit`](https://huggingface.co/mlx-community/Qwen3.6-35B-A3B-8bit) | 8-bit | 35B-A3B | 37.74 | 77005 | 15 | 2026-04-16 |
| [`lmstudio-community/NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-8bit`](https://huggingface.co/lmstudio-community/NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-8bit) | 8-bit | 30B-A3B | 33.58 | 75350 | 3 | 2025-12-16 |
| [`lmstudio-community/NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-6bit`](https://huggingface.co/lmstudio-community/NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-6bit) | 6-bit | 30B-A3B | 25.68 | 74196 | 0 | 2025-12-16 |
| [`lmstudio-community/NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-5bit`](https://huggingface.co/lmstudio-community/NVIDIA-Nemotron-3-Nano-30B-A3B-MLX-5bit) | 5-bit | 30B-A3B | 21.74 | 74004 | 0 | 2025-12-16 |
| [`lmstudio-community/gemma-4-31B-it-MLX-8bit`](https://huggingface.co/lmstudio-community/gemma-4-31B-it-MLX-8bit) | 8-bit | 31B | 33.80 | 73094 | 3 | 2026-04-10 |
| [`lmstudio-community/gemma-4-26B-A4B-it-MLX-4bit`](https://huggingface.co/lmstudio-community/gemma-4-26B-A4B-it-MLX-4bit) | 4-bit | 26B-A4B | 15.64 | 70068 | 6 | 2026-04-10 |
| [`lmstudio-community/Qwen3-VL-30B-A3B-Instruct-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3-VL-30B-A3B-Instruct-MLX-4bit) | 4-bit | 30B-A3B | 18.26 | 60985 | 1 | 2025-10-28 |
| [`unsloth/Qwen3.6-27B-UD-MLX-4bit`](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-4bit) | 4-bit | 27B | 26.21 | 60333 | 54 | 2026-04-22 |
| [`lmstudio-community/Qwen2.5-Coder-32B-Instruct-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen2.5-Coder-32B-Instruct-MLX-4bit) | 4-bit | 32B | 18.44 | 58457 | 6 | 2024-11-13 |
| [`mlx-community/Qwen3.5-122B-A10B-8bit`](https://huggingface.co/mlx-community/Qwen3.5-122B-A10B-8bit) | 8-bit | 122B-A10B | 130.67 | 58174 | 1 | 2026-02-24 |
| [`lmstudio-community/Qwen2.5-Coder-32B-Instruct-MLX-8bit`](https://huggingface.co/lmstudio-community/Qwen2.5-Coder-32B-Instruct-MLX-8bit) | 8-bit | 32B | 34.82 | 53961 | 4 | 2024-11-13 |

## Practical Next Queue

1. Re-test the already strong text models only if prompt/scorer changes materially: `gemma-2-9b-it`, `gemma-3n-E2B-it-lm`, Qwen3 4B Instruct, and Mistral 7B.
2. Add a fresh small-model pass for newly surfaced tiny models under 2 GB storage before spending time on 8B+ edge candidates.
3. Keep reasoning and thinking variants in a separate cleanup/two-pass lane; do not compare them directly against strict direct-JSON models.
4. Keep VLM/ASR/embedding/image-generation models as separate benchmark lanes, even when they fit the M4 memory budget.
