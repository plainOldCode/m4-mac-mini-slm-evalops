#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


SEARCH_TERMS = [
    "MLX 4bit",
    "MLX 8bit",
    "MLX 6bit",
    "MLX 5bit",
    "MLX 3bit",
    "MLX 2bit",
    "MLX DWQ",
    "MLX AWQ",
    "MLX TurboQuant",
    "MLX RotorQuant",
    "mlx-community 4bit",
    "lmstudio-community MLX 4bit",
    "Qwen MLX 4bit",
    "Qwen3 MLX",
    "Qwen3.5 MLX",
    "Qwen3.6 MLX",
    "Qwen3 Coder MLX",
    "Qwen3 Coder Next MLX",
    "Qwen3 30B A3B MLX",
    "Qwen2.5 Coder MLX",
    "Sushi Coder MLX",
    "Qwopus MLX",
    "FastApply MLX",
    "Gemma MLX 4bit",
    "gemma 4 MLX",
    "gemma 3n MLX",
    "Llama MLX 4bit",
    "Llama 4 MLX",
    "Mistral MLX 4bit",
    "Mistral Small MLX",
    "Mistral Medium MLX",
    "Ministral MLX",
    "Magistral MLX",
    "Devstral MLX",
    "Phi-4 MLX",
    "DeepSeek MLX 4bit",
    "DeepSeek V4 MLX",
    "DeepSeek Coder MLX",
    "GLM MLX 4bit",
    "GLM 4.7 MLX",
    "Seed OSS MLX",
    "Nemotron MLX",
    "Olmo 3 MLX",
    "ERNIE MLX",
    "Hermes 4 MLX",
    "Kimi K2 MLX",
    "MiniMax M2 MLX",
    "MiniMax M2.5 MLX",
    "MiniMax M2.7 MLX",
    "GPT OSS MLX",
    "LFM2.5 MLX",
    "LFM2 MLX",
    "LiquidAI MLX",
    "Ternary Bonsai MLX",
    "Qwen3 VL MLX",
    "ASR MLX",
    "embedding MLX 4bit",
]


@dataclass(frozen=True)
class Candidate:
    category: str
    model_id: str
    url: str
    quant: str
    params: str
    storage_gb: str
    downloads: int
    likes: int
    pipeline_tag: str
    last_modified: str
    tags: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh Hugging Face MLX candidate catalog.")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--limit-per-search", type=int, default=500)
    parser.add_argument("--enrich-limit", type=int, default=360)
    parser.add_argument("--sleep", type=float, default=0.12)
    args = parser.parse_args()

    data_dir = Path("data/model-candidates")
    docs_dir = Path("docs/model-candidates")
    data_dir.mkdir(parents=True, exist_ok=True)
    docs_dir.mkdir(parents=True, exist_ok=True)

    raw = collect_raw_candidates(args.limit_per_search)
    enriched = enrich_candidates(raw, args.enrich_limit, args.sleep)
    candidates = [to_candidate(item) for item in enriched]
    candidates.sort(key=sort_key)

    raw_path = data_dir / f"hf-mlx-candidates-raw-{args.date}.json"
    enriched_path = data_dir / f"hf-mlx-candidates-enriched-{args.date}.json"
    csv_path = data_dir / f"hf-mlx-candidates-m4-16gb-{args.date}.csv"
    md_path = docs_dir / f"hf-mlx-candidate-refresh-{args.date}.md"

    raw_path.write_text(json.dumps(raw, indent=2, ensure_ascii=False))
    enriched_path.write_text(json.dumps(enriched, indent=2, ensure_ascii=False))
    write_csv(csv_path, candidates)
    md_path.write_text(render_markdown(candidates, raw_path, enriched_path, csv_path, args.date))

    print(f"raw={raw_path} count={len(raw)}")
    print(f"enriched={enriched_path} count={len(enriched)}")
    print(f"csv={csv_path}")
    print(f"md={md_path}")
    return 0


def collect_raw_candidates(limit_per_search: int) -> list[dict[str, Any]]:
    by_id: dict[str, dict[str, Any]] = {}
    for term in SEARCH_TERMS:
        params = urllib.parse.urlencode(
            {
                "search": term,
                "sort": "downloads",
                "direction": "-1",
                "limit": str(limit_per_search),
                "full": "true",
            }
        )
        url = f"https://huggingface.co/api/models?{params}"
        for item in fetch_json(url):
            model_id = item.get("modelId") or item.get("id")
            if not isinstance(model_id, str):
                continue
            if not is_mlx_candidate(model_id, item):
                continue
            existing = by_id.get(model_id)
            if existing is None or int(item.get("downloads") or 0) > int(existing.get("downloads") or 0):
                item["matchedSearchTerm"] = term
                by_id[model_id] = item
    return list(by_id.values())


def enrich_candidates(raw: list[dict[str, Any]], limit: int, sleep_seconds: float) -> list[dict[str, Any]]:
    ordered = sorted(raw, key=lambda item: int(item.get("downloads") or 0), reverse=True)
    enriched: list[dict[str, Any]] = []
    for item in ordered[:limit]:
        model_id = item.get("modelId") or item.get("id")
        if not isinstance(model_id, str):
            continue
        url = f"https://huggingface.co/api/models/{urllib.parse.quote(model_id, safe='/')}"
        try:
            detail = fetch_json(url)
            merged = {**item, **detail}
        except Exception as exc:  # noqa: BLE001
            merged = {**item, "detailFetchError": repr(exc)}
        enriched.append(merged)
        time.sleep(sleep_seconds)
    return enriched


def fetch_json(url: str) -> Any:
    request = urllib.request.Request(url, headers={"User-Agent": "local-llm-evalops/0.1"})
    with urllib.request.urlopen(request, timeout=45) as response:  # noqa: S310
        return json.loads(response.read().decode("utf-8"))


def is_mlx_candidate(model_id: str, item: dict[str, Any]) -> bool:
    haystack = " ".join(
        [
            model_id,
            str(item.get("pipeline_tag") or ""),
            " ".join(str(tag) for tag in item.get("tags") or []),
        ]
    ).lower()
    quant_tokens = [
        "8bit",
        "8-bit",
        "6bit",
        "6-bit",
        "5bit",
        "5-bit",
        "4bit",
        "4-bit",
        "3bit",
        "3-bit",
        "2bit",
        "2-bit",
        "dwq",
        "awq",
        "quant",
    ]
    return "mlx" in haystack and any(token in haystack for token in quant_tokens)


def to_candidate(item: dict[str, Any]) -> Candidate:
    model_id = str(item.get("modelId") or item.get("id"))
    storage = item.get("usedStorage")
    storage_gb = "" if storage is None else f"{float(storage) / 1_000_000_000:.2f}"
    quant = infer_quant(model_id, item)
    params = infer_params(model_id)
    pipeline_tag = str(item.get("pipeline_tag") or "")
    tags = " ".join(str(tag) for tag in item.get("tags") or [])
    return Candidate(
        category=classify(model_id, params, quant, storage_gb, pipeline_tag, tags),
        model_id=model_id,
        url=f"https://huggingface.co/{model_id}",
        quant=quant,
        params=params,
        storage_gb=storage_gb,
        downloads=int(item.get("downloads") or 0),
        likes=int(item.get("likes") or 0),
        pipeline_tag=pipeline_tag,
        last_modified=str(item.get("lastModified") or item.get("last_modified") or ""),
        tags=tags,
    )


def infer_quant(model_id: str, item: dict[str, Any]) -> str:
    text = f"{model_id} {' '.join(str(tag) for tag in item.get('tags') or [])}".lower()
    patterns = [
        (r"1\.58[-_ ]?bit", "1.58-bit"),
        (r"2[-_ ]?bit", "2-bit"),
        (r"3[-_ ]?bit", "3-bit"),
        (r"4[-_ ]?bit", "4-bit"),
        (r"5[-_ ]?bit", "5-bit"),
        (r"6[-_ ]?bit", "6-bit"),
        (r"8[-_ ]?bit", "8-bit"),
        (r"dwq", "DWQ"),
        (r"awq", "AWQ"),
    ]
    for pattern, label in patterns:
        if re.search(pattern, text):
            return label
    return ""


def infer_params(model_id: str) -> str:
    text = model_id.replace("_", "-")
    match = re.search(r"(?<![A-Za-z0-9])(\d+(?:\.\d+)?B(?:-A\d+B)?)(?![A-Za-z0-9])", text, re.IGNORECASE)
    return match.group(1) if match else ""


def classify(model_id: str, params: str, quant: str, storage_gb: str, pipeline_tag: str, tags: str) -> str:
    text = f"{model_id} {pipeline_tag} {tags}".lower()
    storage = float(storage_gb) if storage_gb else None
    param_b = primary_param_billions(params)
    if param_b is not None and param_b >= 20:
        return "larger_later_hardware_candidate"
    if any(token in text for token in ["mtp", "draft-model", "speculative-decoding"]):
        return "larger_later_hardware_candidate"
    if any(token in text for token in ["embedding", "reranker", "bge-", "e5-"]):
        return "embedding_or_rerank_lane"
    if any(token in text for token in ["flux", "stable-diffusion", "image-generation", "diffusion"]):
        return "image_generation_lane"
    if any(token in text for token in ["vl", "vision", "audio", "asr", "whisper", "multimodal"]):
        if storage is not None and storage <= 8.5:
            return "vision_audio_m4_16gb_candidate"
        return "vision_audio_later_candidate"
    if any(token in text for token in ["coder", "devstral", "code"]):
        if storage is not None and storage <= 8.5:
            return "coding_m4_16gb_candidate"
        if storage is not None and storage <= 14.0:
            return "coding_edge_candidate"
        return "coding_later_hardware_candidate"
    if storage is not None and storage <= 6.5:
        return "text_m4_16gb_priority_candidate"
    if storage is not None and storage <= 8.5:
        return "text_m4_16gb_edge_candidate"
    if storage is not None and storage <= 12.5 and any(token in quant for token in ["2-bit", "3-bit", "1.58-bit"]):
        return "low_bit_stretch_candidate"
    return "larger_later_hardware_candidate"


def primary_param_billions(params: str) -> float | None:
    match = re.match(r"(\d+(?:\.\d+)?)B", params, re.IGNORECASE)
    return float(match.group(1)) if match else None


def sort_key(candidate: Candidate) -> tuple[int, int, float, int]:
    rank = {
        "text_m4_16gb_priority_candidate": 0,
        "coding_m4_16gb_candidate": 1,
        "vision_audio_m4_16gb_candidate": 2,
        "text_m4_16gb_edge_candidate": 3,
        "low_bit_stretch_candidate": 4,
        "coding_edge_candidate": 5,
        "embedding_or_rerank_lane": 6,
        "image_generation_lane": 7,
        "vision_audio_later_candidate": 8,
        "coding_later_hardware_candidate": 9,
        "larger_later_hardware_candidate": 10,
    }.get(candidate.category, 99)
    storage = float(candidate.storage_gb) if candidate.storage_gb else 999.0
    return rank, -candidate.downloads, storage, -candidate.likes


def write_csv(path: Path, candidates: list[Candidate]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(Candidate.__dataclass_fields__.keys()))
        writer.writeheader()
        for candidate in candidates:
            writer.writerow(candidate.__dict__)


def render_markdown(
    candidates: list[Candidate],
    raw_path: Path,
    enriched_path: Path,
    csv_path: Path,
    run_date: str,
) -> str:
    lines = [
        f"# Hugging Face MLX Candidate Refresh - {run_date}",
        "",
        "Generated from Hugging Face API searches across MLX, quantization, model-family, coding, VLM, and low-bit terms.",
        "",
        f"- Raw pool: `{raw_path}`",
        f"- Enriched pool: `{enriched_path}`",
        f"- CSV: `{csv_path}`",
        f"- Enriched candidate count: `{len(candidates)}`",
        "- Storage is Hugging Face repository `usedStorage`, not guaranteed peak runtime memory.",
        "- M4 16GB labels are practical routing labels, not pass/fail judgments.",
        "",
    ]
    counts: dict[str, int] = {}
    for candidate in candidates:
        counts[candidate.category] = counts.get(candidate.category, 0) + 1
    lines += ["## Category Counts", ""]
    for category, count in sorted(counts.items()):
        lines.append(f"- `{category}`: {count}")
    lines.append("")

    sections = [
        ("Text Priority For M4 16GB", "text_m4_16gb_priority_candidate", 40),
        ("Coding Candidates For M4 16GB", "coding_m4_16gb_candidate", 25),
        ("Vision / Audio Candidates For M4 16GB", "vision_audio_m4_16gb_candidate", 25),
        ("Text Edge For M4 16GB", "text_m4_16gb_edge_candidate", 25),
        ("Low-Bit Stretch Candidates", "low_bit_stretch_candidate", 25),
        ("Embedding / Rerank Lane", "embedding_or_rerank_lane", 20),
        ("Larger / Later Hardware", "larger_later_hardware_candidate", 35),
    ]
    for title, category, limit in sections:
        rows = [candidate for candidate in candidates if candidate.category == category][:limit]
        if not rows:
            continue
        lines += [f"## {title}", "", "| Model | Quant | Params | Storage GB | Downloads | Likes | Last Modified |", "| --- | --- | ---: | ---: | ---: | ---: | --- |"]
        for row in rows:
            lines.append(
                f"| [`{row.model_id}`]({row.url}) | {row.quant} | {row.params} | "
                f"{row.storage_gb} | {row.downloads} | {row.likes} | {row.last_modified[:10]} |"
            )
        lines.append("")

    lines += [
        "## Practical Next Queue",
        "",
        "1. Re-test the already strong text models only if prompt/scorer changes materially: `gemma-2-9b-it`, `gemma-3n-E2B-it-lm`, Qwen3 4B Instruct, and Mistral 7B.",
        "2. Add a fresh small-model pass for newly surfaced tiny models under 2 GB storage before spending time on 8B+ edge candidates.",
        "3. Keep reasoning and thinking variants in a separate cleanup/two-pass lane; do not compare them directly against strict direct-JSON models.",
        "4. Keep VLM/ASR/embedding/image-generation models as separate benchmark lanes, even when they fit the M4 memory budget.",
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
