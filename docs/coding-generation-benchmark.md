# Coding Generation Benchmark

This lane tests whether a model can write runnable code, not just answer coding
questions. It uses deterministic fixture repos and local test commands so scores
do not depend on an LLM judge.

## Roadmap

| Stage | Scope | Purpose |
| --- | --- | --- |
| `v1_smoke` | Python, JavaScript, HTML/CSS | Fast sanity check across backend, scripting, and static UI output. |
| `v1_5_polyglot` | TypeScript, C, C++, Java, Rust | Add compiled-language and type-system pressure. |
| `v2_frontend` | React, Vue, HTML, CSS | Add component-generation and UI-contract checks. |

## Output Contract

Models must return exactly one JSON object:

```json
{
  "files": [
    {"path": "src/example.py", "content": "..."}
  ]
}
```

Only paths listed in each task's `allowed_paths` are applied. The runner copies a
clean fixture repo, applies the model output, runs the task's `test_command`, and
writes per-task diff/stdout/stderr evidence.

## Backends

| Backend | Use |
| --- | --- |
| `mlx` | Runs local Hugging Face MLX models with attempt-scoped cache cleanup. |
| `codex-cli` | Runs GPT comparison models through the local Codex CLI OAuth store. |
| `openai` | Direct OpenAI Responses API path when `OPENAI_API_KEY` is available. |
| `scripted` | Copies checked-in solutions for fixture verification only. |
| `static-json` | Scores pre-generated JSON outputs. |

For `codex-cli`, keep credentials outside the repository and pass the auth home
at runtime:

```bash
CODEX_CLI_AUTH_HOME=/Users/miniadmin/.codex \
python scripts/run_coding_generation_suite.py \
  --start 1 \
  --limit 2
```

The runner sends only the rendered task prompt to Codex in an empty read-only
workdir, so GPT comparison models cannot inspect checked-in `solution/`
directories.

## External Bench Reuse

Useful upstream sources:

- `nuprl/MultiPL-E`: broad language coverage for HumanEval/MBPP-style tasks.
- `Aider-AI/polyglot-benchmark`: practical Exercism-based multi-language tasks.
- `bigcode-project/bigcodebench`: harder Python software-engineering lane.
- `WebPAI/DesignBench`: frontend-oriented generation/edit/repair ideas.

The local lane should stay smaller and deterministic. Heavy upstream suites can
be sampled later instead of imported wholesale.
