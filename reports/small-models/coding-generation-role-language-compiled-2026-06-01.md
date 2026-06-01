# Coding Generation Smoke Suite

| Rank | Model | Backend | Pass | JSON | Schema | Changed | Elapsed |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` | mlx | 3/5 | 5/5 | 5/5 | 5/5 | 297.287s |
| 2 | `mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit` | mlx | 0/5 | 4/5 | 4/5 | 4/5 | 95.66s |
| 3 | `mlx-community/Qwen2.5-Coder-3B-Instruct-4bit` | mlx | 0/5 | 2/5 | 2/5 | 2/5 | 179.596s |

## Per Model

### lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit

- Backend: `mlx`
- Pass: 3/5
- JSON valid: 5/5
- Schema valid: 5/5
- Changed: 5/5
- Download: ok in 244.051s
- Cache cleanup: deleted

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | yes | yes | yes | yes | 24 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | yes | 53 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | no | 17 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | yes | 29 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | no | 111 |

### mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit

- Backend: `mlx`
- Pass: 0/5
- JSON valid: 4/5
- Schema valid: 4/5
- Changed: 4/5
- Download: ok in 77.583s
- Cache cleanup: deleted

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | no | no | no | no | 0 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | no | 30 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | no | 8 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 25 |
| rust_result_contract | rust | result_contract | ok | yes | yes | yes | no | 26711 |

### mlx-community/Qwen2.5-Coder-3B-Instruct-4bit

- Backend: `mlx`
- Pass: 0/5
- JSON valid: 2/5
- Schema valid: 2/5
- Changed: 2/5
- Download: ok in 150.517s
- Cache cleanup: deleted

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | no | no | no | no | 0 |
| typescript_type_contract | typescript | type_contract | ok | no | no | no | no | 0 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | no | 14 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | no | 35 |
| rust_result_contract | rust | result_contract | ok | no | no | no | no | 0 |
