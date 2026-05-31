# Model Cache Cleanup Policy

## Principle

The benchmark should test many models without turning the M4 Mac mini into a
permanent model archive. Model weights are disposable inputs. Evaluation
evidence is the durable output.

## Default Lifecycle

Each live model attempt should follow this lifecycle:

```text
create attempt workspace
create attempt-scoped model cache
download model into that cache
run smoke/eval
write evidence artifacts
delete the attempt-scoped model cache
record cleanup status
```

The preferred implementation is to set cache environment variables per attempt,
for example:

```text
HF_HOME=<attempt_dir>/model-cache/hf-home
HF_HUB_CACHE=<attempt_dir>/model-cache/hf-home/hub
TRANSFORMERS_CACHE=<attempt_dir>/model-cache/transformers
```

This keeps downloaded weights away from the global Hugging Face cache and makes
cleanup deterministic.

The initial sweep utility is:

```bash
python scripts/run_mlx_candidate_sweep.py \
  --category m4_16gb_priority_or_edge \
  --limit 1 \
  --download-timeout 1800 \
  --timeout 240
```

It writes per-model reports under `runs/` and appends a machine-readable
`summary.jsonl`. The download and eval phases are timed separately, so slow
network fetches do not get confused with model-generation failures.

## Preserve

Keep lightweight artifacts that make the result reproducible:

- model repository id and revision, when available
- quantization label and expected storage size
- backend configuration snapshot
- prompt and system/developer instructions sent to the model
- raw stdout and stderr
- raw model output
- parsed response or patch candidate
- diff and deterministic test results
- timing, timeout, and memory metrics where available
- cleanup log showing which cache path was removed

## Delete

After a test finishes, delete heavyweight cache files:

- downloaded model weights
- temporary Hugging Face cache blobs
- temporary tokenizer/config cache copies
- temporary MLX conversion artifacts, if created
- abandoned partial downloads for the attempt

The source of truth is the report artifact plus the Hugging Face model link, not
the local cache.

## Safety Rules

- Prefer attempt-scoped caches over deleting from the global user cache.
- Do not delete outside an allowlisted cache root.
- A cleanup target must be inside the attempt directory unless an explicit
  manual global-cache cleanup command is being run.
- Record cleanup success or failure in the attempt report.
- If direct manual cleanup is needed, prefer recoverable deletion first unless
  the user explicitly asks for permanent removal.

## Manual Global Cache Cleanup

Existing global caches should be cleaned separately from benchmark execution.
Use cache inventory first, then remove only selected model repositories.

Recommended inspection commands:

```bash
huggingface-cli scan-cache
du -sh ~/.cache/huggingface/hub/models--* 2>/dev/null | sort -h
```

For this project, the long-term goal is that routine benchmark runs do not
depend on global cache cleanup because model downloads are scoped to each
attempt and deleted after reporting.
