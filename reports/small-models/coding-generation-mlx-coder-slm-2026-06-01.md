# Coding Generation Smoke Suite

| Rank | Model | Backend | Pass | JSON | Schema | Changed | Elapsed |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | `mlx-community/Qwen2.5-Coder-3B-Instruct-4bit` | mlx | 1/3 | 3/3 | 3/3 | 3/3 | 170.239s |
| 2 | `lmstudio-community/Qwen2.5-Coder-7B-Instruct-MLX-4bit` | mlx | 1/3 | 3/3 | 2/3 | 2/3 | 417.937s |
| 3 | `mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit` | mlx | 0/3 | 3/3 | 3/3 | 3/3 | 85.793s |
| 4 | `mlx-community/deepseek-coder-1.3b-instruct-mlx` | mlx | 0/3 | 0/3 | 0/3 | 0/3 | 247.988s |
| 5 | `mlx-community/starcoder2-3b-4bit` | mlx | 0/3 | 0/3 | 0/3 | 0/3 | 314.124s |
| 6 | `mlx-community/deepseek-coder-6.7b-instruct-hf-4bit-mlx` | mlx | 0/3 | 0/3 | 0/3 | 0/3 | 335.543s |

## Per Model

### mlx-community/Qwen2.5-Coder-3B-Instruct-4bit

- Backend: `mlx`
- Pass: 1/3
- JSON valid: 3/3
- Schema valid: 3/3
- Changed: 3/3
- Download: ok in 150.564s
- Cache cleanup: deleted

| Task | Language | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| python_string_normalize | python | ok | yes | yes | yes | yes | 15 |
| javascript_portfolio_metrics | javascript | ok | yes | yes | yes | no | 26 |
| html_css_status_card | html_css | ok | yes | yes | yes | no | 41 |

### lmstudio-community/Qwen2.5-Coder-7B-Instruct-MLX-4bit

- Backend: `mlx`
- Pass: 1/3
- JSON valid: 3/3
- Schema valid: 2/3
- Changed: 2/3
- Download: ok in 375.983s
- Cache cleanup: deleted

| Task | Language | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| python_string_normalize | python | ok | yes | no | no | no | 0 |
| javascript_portfolio_metrics | javascript | ok | yes | yes | yes | no | 39 |
| html_css_status_card | html_css | ok | yes | yes | yes | yes | 40 |

### mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit

- Backend: `mlx`
- Pass: 0/3
- JSON valid: 3/3
- Schema valid: 3/3
- Changed: 3/3
- Download: ok in 77.126s
- Cache cleanup: deleted

| Task | Language | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| python_string_normalize | python | ok | yes | yes | yes | no | 6 |
| javascript_portfolio_metrics | javascript | ok | yes | yes | yes | no | 37 |
| html_css_status_card | html_css | ok | yes | yes | yes | no | 23 |

### mlx-community/deepseek-coder-1.3b-instruct-mlx

- Backend: `mlx`
- Pass: 0/3
- JSON valid: 0/3
- Schema valid: 0/3
- Changed: 0/3
- Download: ok in 245.418s
- Cache cleanup: deleted

| Task | Language | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| python_string_normalize | python | failed | no | no | no | no | 0 |
| javascript_portfolio_metrics | javascript | failed | no | no | no | no | 0 |
| html_css_status_card | html_css | failed | no | no | no | no | 0 |

### mlx-community/starcoder2-3b-4bit

- Backend: `mlx`
- Pass: 0/3
- JSON valid: 0/3
- Schema valid: 0/3
- Changed: 0/3
- Download: ok in 166.41s
- Cache cleanup: deleted

| Task | Language | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| python_string_normalize | python | ok | no | no | no | no | 0 |
| javascript_portfolio_metrics | javascript | ok | no | no | no | no | 0 |
| html_css_status_card | html_css | ok | no | no | no | no | 0 |

### mlx-community/deepseek-coder-6.7b-instruct-hf-4bit-mlx

- Backend: `mlx`
- Pass: 0/3
- JSON valid: 0/3
- Schema valid: 0/3
- Changed: 0/3
- Download: ok in 332.955s
- Cache cleanup: deleted

| Task | Language | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| python_string_normalize | python | failed | no | no | no | no | 0 |
| javascript_portfolio_metrics | javascript | failed | no | no | no | no | 0 |
| html_css_status_card | html_css | failed | no | no | no | no | 0 |
