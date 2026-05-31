# Think Cleanup Verification - 2026-05-30

This follow-up verifies whether the Qwen3 1.7B variants can move into the
core task lane when the harness removes an empty reasoning wrapper before JSON
parsing.

## Cleanup Rule

The adapter removes `<think>...</think>` blocks before JSON extraction.

- Empty block: `empty_think_wrapper_removed`
- Non-empty block without schema-valid JSON: keep routed to reasoning lane
- Clean direct JSON: unchanged

## Results

| Model | Download s | Eval s | Cleanup | Schema | Routing |
| --- | ---: | ---: | --- | --- | --- |
| `lmstudio-community/Qwen3-1.7B-MLX-4bit` | 86.327 | 2.049 | `empty_think_wrapper_removed` | true | `candidate_for_core_tasks_after_cleanup` |
| `mlx-community/Qwen3-1.7B-4bit` | 82.932 | 2.035 | `empty_think_wrapper_removed` | true | `candidate_for_core_tasks_after_cleanup` |

## Raw Pattern

Both models emitted:

```text
<think>
</think>

{
  "summary": "삼성전자는 HBM 공급 확대와 서버 DRAM 수요 회복으로 실적 개선 기대가 커졌다.",
  "sentiment": "bullish",
  "companies": ["삼성전자"]
}
```

After cleanup, both produce schema-valid JSON:

```json
{
  "summary": "삼성전자는 HBM 공급 확대와 서버 DRAM 수요 회복으로 실적 개선 기대가 커졌다.",
  "sentiment": "bullish",
  "companies": ["삼성전자"]
}
```

## Conclusion

These models are not direct-output candidates, but they are valid core-lane
candidates when paired with a deterministic cleanup adapter. They should remain
in the M4 Mac mini practical candidate set because they are small, fast, and
their protocol issue is trivial to repair.
