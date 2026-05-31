# Weekly Context - 2026-05-30

This project is distilled from a week of local and cloud LLM-agent experiments.

Observed patterns:

- Local Qwen-family models can be useful under narrow harness ownership.
- Free-form autonomous loops often collapse into no-op, repeat, or invalid
  patch behavior.
- A metric-supervised loop becomes much stronger when paired with a frontier
  backend.
- The durable engineering value is the harness: isolation, metrics, reports,
  retries, and failure taxonomy.

Portfolio conclusion:

> Evaluation-driven ML systems are a stronger signal than one-off demos. The
> goal is to make LLM behavior measurable, reproducible, and operationally safe.
