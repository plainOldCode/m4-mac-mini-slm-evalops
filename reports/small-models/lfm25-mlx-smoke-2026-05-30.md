# LFM2.5 MLX Smoke - 2026-05-30

Model:

- `LiquidAI/LFM2.5-8B-A1B-MLX-4bit`

Environment:

- Apple Silicon Mac mini
- `mlx-lm` through the `local-llm-evalops` project venv
- Local cache size after download: about `4.5G`
- First download/load run: about `6m47s` for Hugging Face file fetch

## Smoke Commands

```bash
python -m mlx_lm generate \
  --model LiquidAI/LFM2.5-8B-A1B-MLX-4bit \
  --prompt "You are running a smoke test..." \
  --max-tokens 120 \
  --temp 0.2 \
  --verbose False
```

Then a shorter Korean one-sentence prompt and a raw prompt mode were tested.

## Results

| Mode | Result |
| --- | --- |
| Default chat template | Model loaded and generated, but emitted verbose `<think>` content and did not reach a clean final answer inside short token budgets. |
| Korean one-sentence prompt | Same pattern: verbose reasoning dominated the output. |
| `--ignore-chat-template` raw prompt | Degenerated into repeated `A:` / token sequences. |

## Interpretation

The model is technically usable on the current Mac mini: it downloads, loads,
and generates through MLX. The first smoke did not show a clean instruction
following setup, though. It needs prompt-template and stop-token tuning before
it should be treated as a practical backend.

For the portfolio project, this is useful as a **negative/diagnostic model
smoke**:

- it proves the harness can record models that load but fail behaviorally;
- it reinforces why model evaluation needs output-quality checks, not only
  "did it run";
- it is not ready to replace Qwen/Sushi/Codex-style backends for coding tasks.

## Next Test

Retest with one of:

- official LiquidAI recommended chat invocation if different from `mlx-lm` default;
- explicit stop tokens for `</think>` / model-specific end markers;
- extraction/classification prompts where short structured output can be
  validated mechanically.

## Controlled Adapter Follow-up

Added `lfm25-controlled-mlx`, which treats LFM2.5 as a reasoning/candidate
signal and applies bounded deterministic post-processing for the demo task.

Result:

```text
PASS task=string_normalize backend=lfm25-controlled-mlx changed=True diff_lines=12
```

Interpretation:

- LFM2.5 described the correct normalization algorithm in its generated output.
- It still emitted verbose thinking, so the backend did not trust the raw output
  as a clean patch.
- A task-specific deterministic repair step converted the model's recognized
  algorithm into a bounded replacement file.

This is a controlled evaluation pattern, not a general-purpose patching method.
It is useful when a model has enough semantic understanding but weak output
protocol discipline.
