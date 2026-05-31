# Design Decisions

## Keep The Harness Boring

The harness should use ordinary filesystem operations, subprocess calls, JSON,
and diffs. The interesting part is the evidence it produces, not framework
novelty.

## Prefer Isolated Attempts

Each attempt starts from a clean copy. This avoids cross-attempt contamination
and makes no-op/repeat behavior visible.

## Store Raw Artifacts

Every attempt writes:

- stdout
- stderr
- diff
- report JSON

Summaries are useful, but raw artifacts are what make debugging possible.

## Delete Model Caches After Evaluation

Downloaded model files are not the product. The product is the evidence: config
snapshot, prompt, raw output, metrics, diff, tests, and final recommendation.

Live model attempts should use attempt-scoped cache directories so the harness
can delete weights and temporary downloads after the report is written. This is
required if the project is going to test the broad Hugging Face MLX candidate
set on a 16GB M4 Mac mini with limited disk.

## Treat Local Models As Bounded Workers

Small local models are useful when the harness narrows the job. They should not
own the full autonomous loop until they have passed read/write/test/rollback
gates.

## Track Invalid Successes

If a candidate passes tests by exploiting the benchmark contract, record it as
evidence. Do not silently delete it or call it success.
