# Coding Generation Smoke Suite

| Rank | Model | Backend | Pass | JSON | Schema | Changed | Elapsed |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | `lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit` | mlx | 5/5 | 5/5 | 5/5 | 5/5 | 861.11s |
| 2 | `mlx-community/Qwen2.5-Coder-7B-Instruct-4bit` | mlx | 1/5 | 5/5 | 4/5 | 4/5 | 435.562s |
| 3 | `dangerusslee/FastApply-7B-v1.0-mlx-4Bit` | mlx | 0/5 | 5/5 | 5/5 | 5/5 | 424.505s |
| 4 | `mlx-community/DeepSeek-Coder-V2-Lite-Instruct-4bit-mlx` | mlx | 0/5 | 4/5 | 4/5 | 4/5 | 831.308s |
| 5 | `lmstudio-community/Qwen2.5-Coder-3B-Instruct-MLX-4bit` | mlx | 0/5 | 2/5 | 2/5 | 2/5 | 181.131s |
| 6 | `aciidix/FastApply-1.5B-v1.0-mlx-4Bit` | mlx | 0/5 | 1/5 | 0/5 | 0/5 | 172.379s |
| 7 | `mlx-community/granite-3b-code-instruct-4bit` | mlx | 0/5 | 0/5 | 0/5 | 0/5 | 258.845s |
| 8 | `mlx-community/stable-code-instruct-3b-4bit` | mlx | 0/5 | 0/5 | 0/5 | 0/5 | 265.831s |
| 9 | `lmstudio-community/Devstral-Small-2507-MLX-4bit` | mlx | 0/5 | 0/5 | 0/5 | 0/5 | 1237.774s |

## Per Model

### lmstudio-community/Qwen2.5-Coder-14B-Instruct-MLX-4bit

- Backend: `mlx`
- Pass: 5/5
- JSON valid: 5/5
- Schema valid: 5/5
- Changed: 5/5
- Download: ok in 718.402s
- Cache cleanup: deleted

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | yes | 13 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | yes | 40 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | yes | 26 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | yes | 26 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | yes | 32 |

### mlx-community/Qwen2.5-Coder-7B-Instruct-4bit

- Backend: `mlx`
- Pass: 1/5
- JSON valid: 5/5
- Schema valid: 4/5
- Changed: 4/5
- Download: ok in 371.94s
- Cache cleanup: deleted

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | no | no | no | 0 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | no | 29 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | no | 14 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | yes | 26 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | no | 21 |

### dangerusslee/FastApply-7B-v1.0-mlx-4Bit

- Backend: `mlx`
- Pass: 0/5
- JSON valid: 5/5
- Schema valid: 5/5
- Changed: 5/5
- Download: ok in 366.445s
- Cache cleanup: deleted

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | no | 11 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | no | 29 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | no | 13 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 23 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | no | 28 |

### mlx-community/DeepSeek-Coder-V2-Lite-Instruct-4bit-mlx

- Backend: `mlx`
- Pass: 0/5
- JSON valid: 4/5
- Schema valid: 4/5
- Changed: 4/5
- Download: ok in 771.425s
- Cache cleanup: deleted

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | no | 18 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | no | 29 |
| javascript_unit_patch | javascript | unit_patch | ok | no | no | no | no | 0 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 22 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | no | 22 |

### lmstudio-community/Qwen2.5-Coder-3B-Instruct-MLX-4bit

- Backend: `mlx`
- Pass: 0/5
- JSON valid: 2/5
- Schema valid: 2/5
- Changed: 2/5
- Download: ok in 151.454s
- Cache cleanup: deleted

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | no | no | no | no | 0 |
| typescript_type_contract | typescript | type_contract | ok | no | no | no | no | 0 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | no | 14 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 35 |
| rust_result_contract | rust | result_contract | ok | no | no | no | no | 0 |

### aciidix/FastApply-1.5B-v1.0-mlx-4Bit

- Backend: `mlx`
- Pass: 0/5
- JSON valid: 1/5
- Schema valid: 0/5
- Changed: 0/5
- Download: ok in 76.84s
- Cache cleanup: deleted

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | no | no | no | no | 0 |
| typescript_type_contract | typescript | type_contract | ok | yes | no | no | no | 0 |
| javascript_unit_patch | javascript | unit_patch | ok | no | no | no | no | 0 |
| go_router_contract | go | explain_route | ok | no | no | no | no | 0 |
| rust_result_contract | rust | result_contract | ok | no | no | no | no | 0 |

### mlx-community/granite-3b-code-instruct-4bit

- Backend: `mlx`
- Pass: 0/5
- JSON valid: 0/5
- Schema valid: 0/5
- Changed: 0/5
- Download: ok in 174.396s
- Cache cleanup: deleted

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | no | no | no | no | 0 |
| typescript_type_contract | typescript | type_contract | ok | no | no | no | no | 0 |
| javascript_unit_patch | javascript | unit_patch | ok | no | no | no | no | 0 |
| go_router_contract | go | explain_route | ok | no | no | no | no | 0 |
| rust_result_contract | rust | result_contract | ok | no | no | no | no | 0 |

### mlx-community/stable-code-instruct-3b-4bit

- Backend: `mlx`
- Pass: 0/5
- JSON valid: 0/5
- Schema valid: 0/5
- Changed: 0/5
- Download: ok in 155.383s
- Cache cleanup: deleted

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | no | no | no | no | 0 |
| typescript_type_contract | typescript | type_contract | ok | no | no | no | no | 0 |
| javascript_unit_patch | javascript | unit_patch | ok | no | no | no | no | 0 |
| go_router_contract | go | explain_route | ok | no | no | no | no | 0 |
| rust_result_contract | rust | result_contract | ok | no | no | no | no | 0 |

### lmstudio-community/Devstral-Small-2507-MLX-4bit

- Backend: `mlx`
- Pass: 0/5
- JSON valid: 0/5
- Schema valid: 0/5
- Changed: 0/5
- Download: ok in 1125.519s
- Cache cleanup: deleted

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | failed | no | no | no | no | 0 |
| typescript_type_contract | typescript | type_contract | failed | no | no | no | no | 0 |
| javascript_unit_patch | javascript | unit_patch | failed | no | no | no | no | 0 |
| go_router_contract | go | explain_route | failed | no | no | no | no | 0 |
| rust_result_contract | rust | result_contract | failed | no | no | no | no | 0 |
