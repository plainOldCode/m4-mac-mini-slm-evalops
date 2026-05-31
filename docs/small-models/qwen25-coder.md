# Qwen2.5-Coder 14B MLX

## Portfolio Label

Bounded local TDD worker.

## Why It Is Included

This model represents the strongest small local coding-worker baseline from the
week's experiments. It was not treated as a general autonomous agent. It was
useful when the harness owned:

- task boundaries
- focused tests
- retry prompts
- rollback
- output parsing

## Expected Role In This Project

The project includes two adapters:

- `qwen25-coder-trace`: deterministic replay backend for public-safe demos
- `qwen25-coder-mlx`: live MLX backend using `mlx-community/Qwen2.5-Coder-14B-Instruct-4bit`

The live adapter still uses a narrow contract: replace only
`src/text_utils.py`, then let the harness own tests, diff capture, and reports.

## Known Risks

- Long prompts can cause drift.
- Free-form tool use is unreliable.
- Visible pseudo-tool output must be filtered or prevented.
- Exact Python/pytest environment steering matters.
