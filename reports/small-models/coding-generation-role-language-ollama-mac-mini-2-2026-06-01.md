# Coding Generation Smoke Suite

| Rank | Model | Backend | Pass | JSON | Schema | Changed | Elapsed |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | `qwen3:8b` | ollama | 3/5 | 5/5 | 5/5 | 5/5 | 80.919s |
| 2 | `deepseek-coder-v2:16b` | ollama | 2/5 | 5/5 | 5/5 | 5/5 | 43.124s |
| 3 | `cogito:8b` | ollama | 2/5 | 5/5 | 5/5 | 5/5 | 72.67s |
| 4 | `gemma3:12b` | ollama | 2/5 | 5/5 | 5/5 | 5/5 | 123.4s |
| 5 | `qwen2.5:14b` | ollama | 2/5 | 5/5 | 3/5 | 4/5 | 130.995s |
| 6 | `phi4-mini` | ollama | 1/5 | 5/5 | 5/5 | 5/5 | 67.184s |
| 7 | `mistral-nemo:12b` | ollama | 1/5 | 5/5 | 5/5 | 5/5 | 95.218s |
| 8 | `granite3-dense:8b` | ollama | 0/5 | 5/5 | 5/5 | 5/5 | 75.871s |

## Per Model

### qwen3:8b

- Backend: `ollama`
- Pass: 3/5
- JSON valid: 5/5
- Schema valid: 5/5
- Changed: 5/5
- Download: ok in 0.835s
- Cache cleanup: not_required

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | yes | 24 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | yes | 43 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | yes | 30 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 27 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | no | 37 |

### deepseek-coder-v2:16b

- Backend: `ollama`
- Pass: 2/5
- JSON valid: 5/5
- Schema valid: 5/5
- Changed: 5/5
- Download: ok in 0.834s
- Cache cleanup: not_required

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | yes | 18 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | yes | 37 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | no | 26 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 26 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | no | 22 |

### cogito:8b

- Backend: `ollama`
- Pass: 2/5
- JSON valid: 5/5
- Schema valid: 5/5
- Changed: 5/5
- Download: ok in 0.826s
- Cache cleanup: not_required

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | yes | 19 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | yes | 34 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | no | 15 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 22 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | no | 36 |

### gemma3:12b

- Backend: `ollama`
- Pass: 2/5
- JSON valid: 5/5
- Schema valid: 5/5
- Changed: 5/5
- Download: ok in 0.799s
- Cache cleanup: not_required

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | yes | 25 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | no | 40 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | yes | 22 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 25 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | no | 28 |

### qwen2.5:14b

- Backend: `ollama`
- Pass: 2/5
- JSON valid: 5/5
- Schema valid: 3/5
- Changed: 4/5
- Download: ok in 0.815s
- Cache cleanup: not_required

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | yes | 22 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | no | 33 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | yes | 21 |
| go_router_contract | go | explain_route | ok | yes | no | no | no | 0 |
| rust_result_contract | rust | result_contract | ok | yes | no | yes | no | 19 |

### phi4-mini

- Backend: `ollama`
- Pass: 1/5
- JSON valid: 5/5
- Schema valid: 5/5
- Changed: 5/5
- Download: ok in 0.854s
- Cache cleanup: not_required

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | yes | 22 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | no | 35 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | no | 27 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 44 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | no | 37 |

### mistral-nemo:12b

- Backend: `ollama`
- Pass: 1/5
- JSON valid: 5/5
- Schema valid: 5/5
- Changed: 5/5
- Download: ok in 0.836s
- Cache cleanup: not_required

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | yes | 21 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | no | 41 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | no | 22 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 26 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | no | 18 |

### granite3-dense:8b

- Backend: `ollama`
- Pass: 0/5
- JSON valid: 5/5
- Schema valid: 5/5
- Changed: 5/5
- Download: ok in 0.838s
- Cache cleanup: not_required

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | no | 13 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | no | 36 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | no | 22 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 24 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | no | 19 |
