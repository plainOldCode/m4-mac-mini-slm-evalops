# Qwen3.5 Sushi-Coder-RL MLX

## Portfolio Label

Candidate artifact worker.

## Why It Is Included

Sushi-style experiments showed that a smaller model can be useful when asked to
produce bounded artifacts: target identification, patch candidates, command
proposals, failure summaries, and structured repair plans.

## Expected Role In This Project

The project includes two adapters:

- `sushi-coder-trace`: deterministic replay backend for public-safe demos
- `sushi-coder-mlx`: live MLX backend using `bigatuna/Qwen3.5-9b-Sushi-Coder-RL-MLX`

The live adapter keeps the model away from full ownership of repo navigation,
testing, and rollback. It only proposes a replacement file for one bounded task.

## Known Risks

- It is not a direct file editor by default.
- It should not own dirty-worktree decisions.
- It can produce plausible artifacts that still need strict validation.
- It should be escalated phase by phase, not promoted wholesale.
