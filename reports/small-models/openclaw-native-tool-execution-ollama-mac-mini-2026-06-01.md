# OpenClaw Native Tool Execution Suite

This suite checks whether each local model can drive OpenClaw's actual native tool loop.
Pass means the model caused OpenClaw to execute the `exec` tool and create a nonce marker file.

Summary: 0/4 pass, 4 fail, 0 error.

| Rank | Model | Status | Marker | Duration | Prompt toks | Output toks | Compactions |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | `qwen3:4b` | `fail` | no | 209.748s | 8192 | 5348 | None |
| 2 | `qwen2.5-coder:7b` | `fail` | no | 34.829s | 4096 | 69 | None |
| 3 | `qwen2.5-coder:14b` | `fail` | no | 67.316s | 4096 | 97 | None |
| 4 | `llama3.1:8b` | `fail` | no | 38.121s | 4096 | 106 | None |

## Notes

- `qwen3:4b`: The error message indicates that a required `sessionId` parameter is missing for the intended function call. Since the user has not provided this parameter and the context does not specify which function they are attempting, no valid fun...
- `qwen2.5-coder:7b`: {"name": "process", "arguments": {"action": "write", "path": "/Users/miniadmin/.openclaw/tmp/openclaw-native-tool-native_tool_ok_17ef4eb5b58b.txt", "content": "native_tool_ok_17ef4eb5b58b"}}
- `qwen2.5-coder:14b`: Executing the command "/bin/sh -lc 'printf native_tool_ok_5c716bc0f68b > /Users/miniadmin/.openclaw/tmp/openclaw-native-tool-native_tool_ok_5c716bc0f68b.txt'" and the output is stored in /Users/miniadmin/.openclaw/tmp/openclaw-native-too...
- `llama3.1:8b`: Based on the provided text, the following command to run the specified shell command using the exec tool would be:  `exec tool execute /bin/sh -lc 'printf native_tool_ok_f4a458dc2aac > /Users/miniadmin/.openclaw/tmp/openclaw-native-tool-...
