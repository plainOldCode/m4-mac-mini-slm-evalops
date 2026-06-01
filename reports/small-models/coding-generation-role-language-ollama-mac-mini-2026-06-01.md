# Coding Generation Smoke Suite

| Rank | Model | Backend | Pass | JSON | Schema | Changed | Elapsed |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | `qwen2.5-coder:14b` | ollama | 4/5 | 5/5 | 5/5 | 5/5 | 147.111s |
| 2 | `qwen2.5-coder:7b` | ollama | 2/5 | 5/5 | 5/5 | 5/5 | 81.283s |
| 3 | `qwen3:4b` | ollama | 1/5 | 5/5 | 5/5 | 5/5 | 44.951s |
| 4 | `llama3.1:8b` | ollama | 0/5 | 4/5 | 4/5 | 4/5 | 69.766s |

## Per Model

### qwen2.5-coder:14b

- Backend: `ollama`
- Pass: 4/5
- JSON valid: 5/5
- Schema valid: 5/5
- Changed: 5/5
- Download: ok in 1.048s
- Cache cleanup: not_required

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | yes | 22 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | yes | 38 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | yes | 24 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 26 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | yes | 25 |

### qwen2.5-coder:7b

- Backend: `ollama`
- Pass: 2/5
- JSON valid: 5/5
- Schema valid: 5/5
- Changed: 5/5
- Download: ok in 0.827s
- Cache cleanup: not_required

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | yes | 13 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | no | 38 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | yes | 26 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 21 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | no | 30 |

### qwen3:4b

- Backend: `ollama`
- Pass: 1/5
- JSON valid: 5/5
- Schema valid: 5/5
- Changed: 5/5
- Download: ok in 0.82s
- Cache cleanup: not_required

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | no | 13 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | yes | 44 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | no | 25 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 32 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | no | 27 |

### llama3.1:8b

- Backend: `ollama`
- Pass: 0/5
- JSON valid: 4/5
- Schema valid: 4/5
- Changed: 4/5
- Download: ok in 1.249s
- Cache cleanup: not_required

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | no | 19 |
| typescript_type_contract | typescript | type_contract | ok | no | no | no | no | 0 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | no | 16 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 21 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | no | 19 |
