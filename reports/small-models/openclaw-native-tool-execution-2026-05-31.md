# OpenClaw Native Tool Execution Suite - 2026-05-31

This suite checks whether each MLX model can drive OpenClaw's actual native tool loop.
Pass means the model caused OpenClaw to execute the `exec` tool and create a nonce marker file.

Summary: 7/10 pass, 3 fail, 0 error.

Key takeaways:
- The `Qwen3 4B Instruct 2507` family passed across 4bit, 5bit, and 6bit MLX variants.
- `Ternary-Bonsai 8B 2bit` passed the actual tool execution check, but the follow-up assistant turn hit a Metal OOM after the tool ran. Treat it as a promising planner candidate, not yet a stable always-on default.
- `Mistral-Nemo`, `Mistral 7B`, and `Qwen2.5 14B` did not produce verified tool side effects in this OpenClaw native loop.
- Several passing runs required one OpenClaw compaction or ended with a generic "tool actions may have already been executed" message, so the current pass criterion is side-effect based, not polished UX.

| Rank | Model | Status | Marker | Duration | Prompt toks | Output toks | Compactions |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | `mlx-community/Mistral-Nemo-Instruct-2407-4bit` | `fail` | no | 699.591s | 10691 | 20 | None |
| 2 | `prism-ml/Ternary-Bonsai-8B-mlx-2bit` | `pass` | yes | 378.429s | 24599 | 72 | None |
| 3 | `mlx-community/Mistral-7B-Instruct-v0.3-4bit` | `fail` | no | 448.005s | 15271 | 60 | None |
| 4 | `mlx-community/Qwen2.5-14B-Instruct-4bit` | `fail` | no | 947.62s | None | None | None |
| 5 | `lmstudio-community/Qwen3-VL-4B-Instruct-MLX-4bit` | `pass` | yes | 410.169s | 24616 | 101 | 1 |
| 6 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit` | `pass` | yes | 356.227s | 24623 | 176 | 1 |
| 7 | `mlx-community/Qwen3-4B-Instruct-2507-4bit` | `pass` | yes | 358.322s | 24699 | 195 | 1 |
| 8 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` | `pass` | yes | 379.611s | 24608 | 70 | None |
| 9 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-6bit` | `pass` | yes | 421.981s | 24604 | 66 | None |
| 10 | `mlx-community/Qwen2.5-7B-Instruct-4bit` | `pass` | yes | 550.43s | 24638 | 130 | 1 |

## Notes

- `mlx-community/Mistral-Nemo-Instruct-2407-4bit`: **native_tool_ok_3107f8757c4c**
- `prism-ml/Ternary-Bonsai-8B-mlx-2bit`: ⚠️ Agent couldn't generate a response. Note: some tool actions may have already been executed — please verify before retrying.
- `mlx-community/Mistral-7B-Instruct-v0.3-4bit`: native_tool_ok_fa29878048a4 written to /Users/miniadmin/.openclaw/tmp/openclaw-native-tool-native_tool_ok_fa29878048a4.txt
- `mlx-community/Qwen2.5-14B-Instruct-4bit`: 48d2-a8c1-350fa6a204e5 sessionId=416e8dcb-f1a1-47d8-a320-233ce0b0a88b provider=mlx-native-04/mlx-community/Qwen2.5-14B-Instruct-4bit — retrying 1/1 with visible-answer continuation [provider-transport-fetch] [model-fetch] error provider=...
- `lmstudio-community/Qwen3-VL-4B-Instruct-MLX-4bit`: The command has been executed successfully.
- `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-4bit`: The shell command was executed successfully and created the file `/Users/miniadmin/.openclaw/tmp/openclaw-native-tool-native_tool_ok_7cd83f05ec80.txt`.
- `mlx-community/Qwen3-4B-Instruct-2507-4bit`: The shell command completed successfully and created the file `/Users/miniadmin/.openclaw/tmp/openclaw-native-tool-native_tool_ok_21d0e55e03c6.txt`.
- `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit`: ⚠️ Agent couldn't generate a response. Note: some tool actions may have already been executed — please verify before retrying.
- `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-6bit`: ⚠️ Agent couldn't generate a response. Note: some tool actions may have already been executed — please verify before retrying.
- `mlx-community/Qwen2.5-7B-Instruct-4bit`: The command is running in the background. It will create a file with the content "native_tool_ok_1b43edb851ac" in the specified path.
