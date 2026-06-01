# 9B Coding Candidate Follow-Up Analysis

Run date: 2026-06-01

Stage: `v1_5_polyglot`

Candidate source: `data/benchmark/coding-role-language-candidates-9b-followup-2026-06-01.json`

Raw results:

- JSON: `reports/small-models/coding-generation-role-language-9b-followup-2026-06-01.json`
- Markdown: `reports/small-models/coding-generation-role-language-9b-followup-2026-06-01.md`
- Run artifacts: `runs/coding-generation-role-language-9b-followup-2026-06-01`

Baseline references:

- Quality leader: `lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit`, 5/5 with JSON/schema 5/5.
- Lightweight baseline: `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit`, 3/5 with JSON/schema 5/5.

## Summary

The 9B follow-up did not displace the existing leaders. `bigatuna/Qwen3.5-9b-Sushi-Coder-RL-MLX` reached 3/5, matching the Qwen3 4B lightweight baseline on pass count, but with weaker JSON/schema reliability. `tongrow/MLX-Qwopus3.5-9B-Coder-oQ4-fp16-mtp` and `nightmedia/Qwen3.5-9B-Claude-Deckard-Agent-Coder-Heretic-qx86-hi-mlx` failed the strict JSON edit-agent protocol entirely.

This narrows the local coding stack:

- Keep Qwen2.5-Coder 14B as the local coding quality leader.
- Keep Qwen3 4B 5bit as the lightweight always-on baseline.
- Treat Sushi-Coder-RL 9B as an interesting but not superior challenger.
- Drop Qwopus 9B and the agent/coder 9B merge from this direct JSON coding-generation lane.

## Leaderboard

| Rank | Model | Pass | JSON | Schema | Read |
| ---: | --- | ---: | ---: | ---: | --- |
| 1 | `bigatuna/Qwen3.5-9b-Sushi-Coder-RL-MLX` | 3/5 | 3/5 | 3/5 | Passed TypeScript, JavaScript, and Go. Failed Python and Rust due to protocol/output issues. |
| 2 | `tongrow/MLX-Qwopus3.5-9B-Coder-oQ4-fp16-mtp` | 0/5 | 0/5 | 0/5 | Output was not parseable JSON for this harness. |
| 3 | `nightmedia/Qwen3.5-9B-Claude-Deckard-Agent-Coder-Heretic-qx86-hi-mlx` | 0/5 | 0/5 | 0/5 | Produced explanatory text, but did not satisfy the strict JSON-only edit protocol. |

## Model Notes

### Sushi-Coder-RL 9B

Sushi-Coder-RL 9B is the only useful result in this follow-up. It passed:

- TypeScript strict type contract
- JavaScript temporal drawdown unit patch
- Go route contract via `go test`

It failed:

- Python syntax repair, because the model produced long analysis without a parseable JSON edit.
- Rust result contract, because the output was not accepted by the strict JSON extraction/schema path.

The signal is mixed. Its actual coding on passed tasks was strong enough to matter, especially the JavaScript drawdown task that Qwen3 4B failed. But for an autonomous local worker, JSON edit reliability is part of the task. A model that only passes when it chooses to follow the output protocol is less useful than Qwen3 4B for always-on automation.

### Qwopus 9B

Qwopus 9B emitted corrupted or non-JSON text under this prompt/template path. It did not produce an editable file for any task. This is likely a template/runtime/protocol mismatch rather than a clean coding-quality signal, but it is enough to reject it for the current EvalOps coding lane.

### Agent/Coder 9B Merge

The agent/coder merge produced explanatory text on at least the Python task, but it did not meet the "exactly one JSON object" contract. This makes it unsuitable for the current machine-applied edit workflow. Given the low-confidence merge provenance and 8.95 GB storage footprint, it is not worth further prompt tuning unless a separate unconstrained coding assistant lane is created.

## Recommendation

1. Do not replace the current leaders.
2. Keep `lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit` as the quality coding worker.
3. Keep `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` as the lightweight baseline.
4. Archive Sushi-Coder-RL 9B as a near-baseline but protocol-weaker challenger.
5. Stop direct JSON generation testing for Qwopus 9B and the agent/coder 9B merge.
6. Skip Qwen3-Coder 30B A3B 4bit on the 16 GB Mac mini; the expected memory pressure is not justified now that 14B already scored 5/5.

## Cache Cleanup

The benchmark loop deleted model caches after each candidate. Verification found no remaining `model-cache` directories under `runs/coding-generation-role-language-9b-followup-2026-06-01`.
