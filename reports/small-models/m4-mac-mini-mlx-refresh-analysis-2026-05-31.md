# M4 Mac Mini MLX Candidate Refresh Analysis - 2026-05-31

## Scope

- Refreshed Hugging Face MLX search with broader quantization terms: 8/6/5/4/3/2-bit, DWQ, AWQ, TurboQuant, RotorQuant, plus model-family searches.
- Source catalog: `data/model-candidates/hf-mlx-candidates-m4-16gb-2026-05-31.csv`.
- Detail-enriched records: 420 from 4,687 raw search hits.
- M4 16GB classification is storage-first, with guards that exclude 20B+ models and MTP/speculative-decoding draft models even when Hugging Face storage metadata is incomplete.

## Category Counts

| Category | Count |
| --- | ---: |
| `larger_later_hardware_candidate` | 247 |
| `text_m4_16gb_priority_candidate` | 72 |
| `vision_audio_m4_16gb_candidate` | 36 |
| `coding_later_hardware_candidate` | 17 |
| `vision_audio_later_candidate` | 16 |
| `coding_m4_16gb_candidate` | 12 |
| `text_m4_16gb_edge_candidate` | 9 |
| `coding_edge_candidate` | 5 |
| `embedding_or_rerank_lane` | 5 |
| `image_generation_lane` | 1 |

## Delta vs 2026-05-30 Catalog

- New models not present in the 2026-05-30 enriched top160 catalog: 260 / 420.
- Models not yet exercised by our 2026-05-30 sweep or multilingual suite summaries: 371 / 420.
- The refresh now separates M4-appropriate candidates from larger-hardware later candidates instead of relying only on download count.

## Suggested Next Test Queue

| Priority | Model | Lane | Quant | Size | Downloads | Status |
| ---: | --- | --- | --- | ---: | ---: | --- |
| 1 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` | `text_m4_16gb_priority_candidate` | 5-bit | 2.78 GB | 55990 | new, untested |
| 2 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-6bit` | `text_m4_16gb_priority_candidate` | 6-bit | 3.28 GB | 56040 | new, untested |
| 3 | `lmstudio-community/Qwen3-4B-Thinking-2507-MLX-6bit` | `text_m4_16gb_priority_candidate` | 6-bit | 3.28 GB | 60190 | new, untested |
| 4 | `lmstudio-community/LFM2.5-1.2B-Instruct-MLX-6bit` | `text_m4_16gb_priority_candidate` | 6-bit | 0.95 GB | 116576 | new, untested |
| 5 | `lmstudio-community/LFM2.5-1.2B-Instruct-MLX-8bit` | `text_m4_16gb_priority_candidate` | 8-bit | 1.24 GB | 118921 | new, untested |
| 6 | `mlx-community/gemma-4-e2b-it-4bit` | `text_m4_16gb_priority_candidate` | 4-bit | 3.61 GB | 81174 | known catalog, untested |
| 7 | `mlx-community/gemma-4-e4b-it-4bit` | `text_m4_16gb_priority_candidate` | 4-bit | 5.25 GB | 39254 | known catalog, untested |
| 8 | `lmstudio-community/Phi-4-mini-reasoning-MLX-4bit` | `coding_m4_16gb_candidate` | 4-bit | 2.17 GB | 59134 | known catalog, untested |
| 9 | `mlx-community/Phi-4-mini-instruct-4bit` | `coding_m4_16gb_candidate` | 4-bit | 2.17 GB | 3410 | new, untested |
| 10 | `lmstudio-community/Qwen3-VL-4B-Instruct-MLX-4bit` | `vision_audio_m4_16gb_candidate` | 4-bit | 3.11 GB | 152431 | known catalog, untested |
| 11 | `aufklarer/Qwen3-ASR-0.6B-MLX-4bit` | `vision_audio_m4_16gb_candidate` | 4-bit | 0.71 GB | 105521 | known catalog, untested |
| 12 | `mlx-community/Qwen3.5-9B-MLX-4bit` | `vision_audio_m4_16gb_candidate` | 4-bit | 5.97 GB | 50748 | known catalog, untested |
| 13 | `lmstudio-community/GLM-4.6V-Flash-MLX-4bit` | `text_m4_16gb_edge_candidate` | 4-bit | 7.09 GB | 130398 | known catalog, untested |
| 14 | `lmstudio-community/Qwen3-1.7B-MLX-8bit` | `text_m4_16gb_priority_candidate` | 8-bit | 1.84 GB | 30072 | new, untested |

## Practical Read

- Do not rerun the full 49-model sweep immediately. The useful path is an incremental queue focused on fresh, M4-sized text/coding/VLM candidates.
- Qwen3-4B Instruct 5/6-bit is the cleanest core-task continuation because it directly tests whether slightly higher precision improves the current Qwen3-4B baseline.
- LFM2.5 1.2B should be treated as a latency/control probe. It is cheap to run, but unlikely to replace the core model unless multilingual accuracy surprises.
- Keep reasoning/Thinking variants in a separate lane. They may be useful with different prompting, but they should not be judged as failures under the core-task scorer alone.
- VLM/ASR entries are viable capability-expansion candidates, but they should run in their own prompt suites rather than the text-only multilingual domain suite.

## Files

- `scripts/refresh_hf_mlx_candidates.py`
- `data/model-candidates/hf-mlx-candidates-raw-2026-05-31.json`
- `data/model-candidates/hf-mlx-candidates-enriched-2026-05-31.json`
- `data/model-candidates/hf-mlx-candidates-m4-16gb-2026-05-31.csv`
- `docs/model-candidates/hf-mlx-candidate-refresh-2026-05-31.md`
