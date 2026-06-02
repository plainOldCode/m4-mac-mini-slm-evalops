# Small Model Core Benchmark Pack

`small-model-core` is the public-safe, non-coding baseline for deciding whether
a small local model is useful before running larger candidate sweeps.

The pack covers four lanes:

- `summary`: compress dense run notes without inventing claims.
- `extraction`: return exact structured fields from prose and tables.
- `protocol`: obey strict JSON schemas, including no-tool and safety cases.
- `patch`: produce bounded file edits for small documentation/config tasks.

The pack is intentionally small. It is meant to run often, catch basic worker
failures quickly, and provide inputs for aggregate quality/protocol/hardware
scoring.

## Files

- `pack.json`: suite metadata, task cases, expected fields, and scoring hints.
- `patch_tasks/*/repo`: clean input fixtures copied into an attempt workspace.
- `patch_tasks/*/solution`: expected public-safe reference outputs.

## Output Contract

Every non-patch case asks for one JSON object and no surrounding prose:

```json
{
  "case_id": "summary-run-note-001",
  "answer": {}
}
```

Patch cases use replacement-file JSON so the harness can apply only
allowlisted paths:

```json
{
  "case_id": "patch-model-card-cleanup-001",
  "files": [
    {
      "path": "README.md",
      "content": "complete replacement text"
    }
  ]
}
```

## Scoring Intent

This pack should feed three aggregate dimensions:

- Quality: semantic correctness against deterministic expected fields.
- Protocol: valid JSON, schema adherence, and no reasoning/prose leakage.
- Hardware: wall time, timeout status, and model-cache cleanup status from the
  runner that executes the pack.
