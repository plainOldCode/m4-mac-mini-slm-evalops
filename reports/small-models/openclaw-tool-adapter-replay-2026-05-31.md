# OpenClaw Tool Adapter Replay - 2026-05-31

This replay checks whether native OpenClaw failures contain enough safe text intent
for a compatibility adapter to recover a constrained `exec` file-write action.

The adapter is deliberately narrow: it only accepts the benchmark nonce marker
and a temp-directory `openclaw-native-tool-*.txt` path. It is not a general
shell-command parser.

Summary: 2/3 adapter pass, 1 fail.

| Rank | Model | Native | Adapter | Strategy | Reason |
| ---: | --- | --- | --- | --- | --- |
| 1 | `mlx-community/Mistral-Nemo-Instruct-2407-4bit` | `fail` | `pass` | `text-intent-replay:prompt-trace` | adapter recovered a safe file-write tool intent |
| 3 | `mlx-community/Mistral-7B-Instruct-v0.3-4bit` | `fail` | `pass` | `text-intent-replay:response` | adapter recovered a safe file-write tool intent |
| 4 | `mlx-community/Qwen2.5-14B-Instruct-4bit` | `fail` | `fail` | `text-intent-replay` | no safe exec-write intent found in model output or prompt trace |

## Interpretation

- `Mistral-Nemo` and `Mistral 7B` failed native OpenAI-style tool execution,
  but their text outputs exposed enough intent for an adapter to recover the
  canary action.
- `Qwen2.5 14B` failed because the MLX server hit Metal out-of-memory and did
  not produce recoverable tool intent. This needs runtime/memory mitigation,
  not a text adapter.
