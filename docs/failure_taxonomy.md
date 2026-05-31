# Failure Taxonomy

Use these labels to compare LLM-agent attempts across models and tasks.

| Category | Meaning |
| --- | --- |
| `no_op` | Backend completed but made no useful change. |
| `test_failure` | Candidate changed code but focused tests failed. |
| `unexpected_mutation` | Candidate changed files outside the allowed boundary. |
| `syntax_error` | Candidate introduced invalid source. |
| `timeout` | Backend or tests exceeded the configured time limit. |
| `repeat_candidate` | Candidate is materially identical to a prior failed attempt. |
| `metric_regression` | Candidate passes correctness checks but worsens target metric. |
| `contract_exploit` | Candidate passes tests by exploiting the harness or simulator contract. |
| `invalid_report` | Attempt artifacts are missing or cannot be parsed. |

The important distinction is between model failure and harness failure. A good
EvalOps project makes that distinction obvious in the report artifacts.
