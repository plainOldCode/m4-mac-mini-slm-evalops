# Coding Generation Smoke Suite

| Rank | Model | Backend | Pass | JSON | Schema | Changed | Elapsed |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | `bigatuna/Qwen3.5-9b-Sushi-Coder-RL-MLX` | mlx | 3/5 | 3/5 | 3/5 | 3/5 | 775.112s |
| 2 | `tongrow/MLX-Qwopus3.5-9B-Coder-oQ4-fp16-mtp` | mlx | 0/5 | 0/5 | 0/5 | 0/5 | 831.426s |
| 3 | `nightmedia/Qwen3.5-9B-Claude-Deckard-Agent-Coder-Heretic-qx86-hi-mlx` | mlx | 0/5 | 0/5 | 0/5 | 0/5 | 1193.313s |

## Per Model

### bigatuna/Qwen3.5-9b-Sushi-Coder-RL-MLX

- Backend: `mlx`
- Pass: 3/5
- JSON valid: 3/5
- Schema valid: 3/5
- Changed: 3/5
- Download: ok in 510.071s
- Cache cleanup: deleted

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | no | no | no | no | 0 |
| typescript_type_contract | typescript | type_contract | ok | yes | yes | yes | yes | 42 |
| javascript_unit_patch | javascript | unit_patch | ok | yes | yes | yes | yes | 33 |
| go_router_contract | go | explain_route | ok | yes | yes | yes | yes | 31 |
| rust_result_contract | rust | result_contract | ok | no | no | no | no | 0 |

### tongrow/MLX-Qwopus3.5-9B-Coder-oQ4-fp16-mtp

- Backend: `mlx`
- Pass: 0/5
- JSON valid: 0/5
- Schema valid: 0/5
- Changed: 0/5
- Download: ok in 546.894s
- Cache cleanup: deleted

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | no | no | no | no | 0 |
| typescript_type_contract | typescript | type_contract | ok | no | no | no | no | 0 |
| javascript_unit_patch | javascript | unit_patch | ok | no | no | no | no | 0 |
| go_router_contract | go | explain_route | ok | no | no | no | no | 0 |
| rust_result_contract | rust | result_contract | ok | no | no | no | no | 0 |

### nightmedia/Qwen3.5-9B-Claude-Deckard-Agent-Coder-Heretic-qx86-hi-mlx

- Backend: `mlx`
- Pass: 0/5
- JSON valid: 0/5
- Schema valid: 0/5
- Changed: 0/5
- Download: ok in 815.551s
- Cache cleanup: deleted

| Task | Language | Role | Status | JSON | Schema | Changed | Pass | Diff |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| python_syntax_repair | python | syntax_repair | ok | no | no | no | no | 0 |
| typescript_type_contract | typescript | type_contract | ok | no | no | no | no | 0 |
| javascript_unit_patch | javascript | unit_patch | ok | no | no | no | no | 0 |
| go_router_contract | go | explain_route | ok | no | no | no | no | 0 |
| rust_result_contract | rust | result_contract | ok | no | no | no | no | 0 |
