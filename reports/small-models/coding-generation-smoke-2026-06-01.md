# Coding Generation Smoke Suite

| Rank | Model | Backend | Pass | JSON | Schema | Changed | Elapsed |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | `gpt-5.5` | codex-cli | 3/3 | 3/3 | 3/3 | 3/3 | 37.879s |
| 2 | `gpt-5.4-mini` | codex-cli | 3/3 | 3/3 | 3/3 | 3/3 | 219.481s |
| 3 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` | mlx | 2/3 | 3/3 | 3/3 | 3/3 | 279.979s |

## Per Model

### gpt-5.5

- Backend: `codex-cli`
- Pass: 3/3
- JSON valid: 3/3
- Schema valid: 3/3
- Changed: 3/3
- Download: not_required in 0.0s
- Cache cleanup: not_required

| Task | Language | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| python_string_normalize | python | ok | yes | yes | yes | yes | 12 |
| javascript_portfolio_metrics | javascript | ok | yes | yes | yes | yes | 39 |
| html_css_status_card | html_css | ok | yes | yes | yes | yes | 138 |

### gpt-5.4-mini

- Backend: `codex-cli`
- Pass: 3/3
- JSON valid: 3/3
- Schema valid: 3/3
- Changed: 3/3
- Download: not_required in 0.0s
- Cache cleanup: not_required

| Task | Language | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| python_string_normalize | python | ok | yes | yes | yes | yes | 13 |
| javascript_portfolio_metrics | javascript | ok | yes | yes | yes | yes | 46 |
| html_css_status_card | html_css | ok | yes | yes | yes | yes | 146 |

### lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit

- Backend: `mlx`
- Pass: 2/3
- JSON valid: 3/3
- Schema valid: 3/3
- Changed: 3/3
- Download: ok in 245.396s
- Cache cleanup: deleted

| Task | Language | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| python_string_normalize | python | ok | yes | yes | yes | no | 16 |
| javascript_portfolio_metrics | javascript | ok | yes | yes | yes | yes | 28 |
| html_css_status_card | html_css | ok | yes | yes | yes | yes | 68 |
