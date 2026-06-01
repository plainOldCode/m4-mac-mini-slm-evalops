# Coding Role/Language Suite Analysis

Run date: 2026-06-01

Stage: `v1_5_polyglot`

Candidate source: `data/benchmark/coding-role-language-candidates-2026-06-01.json`

Raw results:
- JSON: `reports/small-models/coding-generation-role-language-2026-06-01.json`
- Markdown: `reports/small-models/coding-generation-role-language-2026-06-01.md`
- Run artifacts: `runs/coding-generation-role-language-2026-06-01`

## What Changed

The coding lane now separates language coverage from role suitability. The new `v1_5_polyglot` stage covers:

| Task | Language | Role | Test Type |
| --- | --- | --- | --- |
| `python_syntax_repair` | Python | syntax repair | `unittest` runnable task |
| `typescript_type_contract` | TypeScript | type contract | dependency-light structural contract check |
| `javascript_unit_patch` | JavaScript | unit patch | `node` runnable unit test |
| `go_router_contract` | Go | explain/route | dependency-light structural contract check |
| `rust_result_contract` | Rust | result contract | dependency-light structural contract check |

This first report used dependency-light structural checks for TypeScript, Go, and Rust because the compilers were not installed at the time. A compiler-backed rerun is recorded separately after installing Go, Rust, and TypeScript.

## Results

| Rank | Model | Pass | JSON | Schema | Read |
| ---: | --- | ---: | ---: | ---: | --- |
| 1 | `lmstudio-community/Qwen3-4B-Instruct-2507-MLX-5bit` | 4/5 | 5/5 | 5/5 | Best role-general local worker. Failed only the JS drawdown edge case. |
| 2 | `mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit` | 1/5 | 2/5 | 2/5 | Passed only Go route contract. Too weak for open coding, but can hit simple structural tasks. |
| 3 | `mlx-community/Qwen2.5-Coder-3B-Instruct-4bit` | 0/5 | 2/5 | 2/5 | Failed all tasks; JSON adherence collapsed on several prompts. |

## Role Findings

### Instruction-Following Beats Coding Specialization

`Qwen3-4B-Instruct-2507-MLX-5bit` remains the strongest practical local coding worker, even though it is not a coding-specialized model. It followed the JSON edit contract for all five tasks and passed Python, TypeScript, Go, and Rust.

This reinforces the earlier v1 smoke finding: for agent-style local coding work, structured instruction following is a first-class capability. A coding-tuned model that cannot reliably return the edit protocol is not useful as a worker.

### Qwen2.5-Coder Is Not A General Worker Here

Both Qwen2.5-Coder models struggled once the suite moved beyond simple v1 smoke tasks:

- `Qwen2.5-Coder-3B`: JSON/schema 2/5, pass 0/5.
- `Qwen2.5-Coder-1.5B`: JSON/schema 2/5, pass 1/5.

The 3B model did not beat the 1.5B model in this role/language suite. That suggests these small coder models should not be treated as reliable end-to-end code generators without a much narrower prompt and a repair loop.

### JavaScript Unit Patching Is A Good Trap Task

All three models failed `javascript_unit_patch`. The common error pattern was calculating a decline against the global min/max or current minimum rather than tracking peak-to-trough drawdown over time. This is useful because the code can look plausible while failing the temporal invariant.

Keep this task in the suite. It catches models that write syntactically reasonable but semantically wrong code.

### Structural Contract Tasks Are Useful But Lower Confidence

TypeScript, Go, and Rust currently use structural tests instead of real compiler checks. These are still useful for small-model capability mapping because they test whether a model can preserve signatures, create typed structures, and follow API contracts. They should not be interpreted as proof that the generated code compiles.

The next upgrade should add a separate `v1_6_compiled` lane once Go, Rust, and TypeScript toolchains are installed.

## Recommendation

For small-model coding work on this M4 Mac mini:

1. Keep `Qwen3-4B-Instruct-2507-MLX-5bit` as the local coding-agent baseline.
2. Use Qwen2.5-Coder models only for narrow candidate-patch generation, not autonomous coding.
3. Score future SLMs by role fit:
   - router/classifier
   - edit-contract follower
   - syntax repairer
   - unit patcher
   - type/API contract follower
   - frontend contract follower
4. Add compiled checks later for TypeScript, Go, and Rust, but keep this dependency-light lane for quick smoke tests.

## Cache Cleanup

The benchmark loop deleted model caches after each candidate. Verification found no remaining `model-cache` directories under `runs/coding-generation-role-language-2026-06-01`.
