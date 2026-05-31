#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from dataclasses import asdict, dataclass
from pathlib import Path


DEFAULT_RUNS_DIR = Path("runs/multilingual-domain-suite-2026-05-30")
DEFAULT_REPORT_JSON = Path("reports/small-models/multilingual-domain-suite-top7-alias-normalized-2026-05-31.json")
DEFAULT_REPORT_MD = Path("reports/small-models/multilingual-domain-suite-top7-alias-normalized-2026-05-31.md")


ALIAS_SETS: dict[str, list[str]] = {
    "physics": [
        "newton",
        "newtons",
        "n",
        "뉴턴",
        "ニュートン",
        "牛顿",
        "ньютон",
    ],
    "biology": [
        "mitochondria",
        "mitochondrion",
        "mitochondrial",
        "mitocondria",
        "mitocondrias",
        "mitochondrie",
        "mitochondrien",
        "mitochondrio",
        "mitocondrio",
        "митохондрия",
        "митохондрии",
        "미토콘드리아",
        "ミトコンドリア",
        "线粒体",
        "綫粒体",
    ],
    "earth_science": [
        "nitrogen",
        "nitrogen gas",
        "n2",
        "n₂",
        "dinitrogen",
        "azote",
        "stickstoff",
        "azoto",
        "nitrogeno",
        "nitrogene",
        "nitrogênio",
        "nitrogenio",
        "азот",
        "질소",
        "窒素",
        "氮",
        "氮气",
    ],
    "chemistry": [
        "nacl",
        "na cl",
        "na+cl-",
        "na+ cl-",
        "sodium chloride",
        "chlorure de sodium",
        "cloruro de sodio",
        "cloruro di sodio",
        "natriumchlorid",
        "cloreto de sódio",
        "cloreto de sodio",
        "хлорид натрия",
        "염화나트륨",
        "塩化ナトリウム",
        "氯化钠",
    ],
    "math": [
        "2x",
        "2*x",
        "2 x",
        "2·x",
        "2×x",
        "two x",
        "2倍x",
    ],
    "coding": [
        "len(xs)",
        "len ( xs )",
        "len xs",
    ],
    "current_affairs": [
        "antonio guterres",
        "antonio gutierres",
        "antonio guterres secretary general",
        "antónio guterres",
        "antónio manuel de oliveira guterres",
        "안토니우 구테흐스",
        "アントニオ グテーレス",
        "古特雷斯",
        "антониу гутерриш",
    ],
    "economics": [
        "gross domestic product",
        "bruttoinlandsprodukt",
        "producto interno bruto",
        "produit interieur brut",
        "produit intérieur brut",
        "prodotto interno lordo",
        "produto interno bruto",
        "валовой внутренний продукт",
        "国内総生産",
        "국내총생산",
        "国内生产总值",
    ],
    "finance": [
        "exchange traded fund",
        "exchange-traded fund",
        "exchange traded funds",
        "exchange-traded funds",
        "fondo cotizado",
        "fonds négocié en bourse",
        "fonds negocie en bourse",
        "börsengehandelter fonds",
        "borsengehandelter fonds",
        "fondo negoziato in borsa",
        "fundo negociado em bolsa",
        "биржевой инвестиционный фонд",
        "상장지수펀드",
        "상장 지수 펀드",
        "上場投資信託",
        "交易所交易基金",
    ],
    "logic": [
        "yes",
        "true",
        "correct",
        "affirmative",
        "sí",
        "si",
        "oui",
        "ja",
        "sim",
        "да",
        "예",
        "네",
        "はい",
        "是",
        "是的",
    ],
}


@dataclass(frozen=True)
class AliasRow:
    case_id: str
    domain: str
    language: str
    strict_match: bool
    alias_match: bool
    alias_source: str
    expected_canonical_answer: str
    actual_canonical_answer: str
    answer: str


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Re-score multilingual suite results using conservative alias normalization."
    )
    parser.add_argument("--runs-dir", type=Path, default=DEFAULT_RUNS_DIR)
    parser.add_argument("--top-n", type=int, default=7)
    parser.add_argument("--report-json", type=Path, default=DEFAULT_REPORT_JSON)
    parser.add_argument("--report-md", type=Path, default=DEFAULT_REPORT_MD)
    args = parser.parse_args()

    reports = load_reports(args.runs_dir)
    selected = sorted(reports, key=lambda item: item["canonical_match_count"], reverse=True)[: args.top_n]
    rescored = [score_model(args.runs_dir, report) for report in selected]
    output = {
        "runs_dir": str(args.runs_dir),
        "top_n": args.top_n,
        "scoring_policy": {
            "strict_match": "Existing exact normalized canonical_answer match.",
            "alias_match": "Conservative alias match over canonical_answer first, then localized answer.",
            "acronym_policy": "Acronym-only answers are not accepted for GDP or ETF expansion prompts.",
        },
        "models": rescored,
    }

    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    args.report_md.parent.mkdir(parents=True, exist_ok=True)
    args.report_json.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    args.report_md.write_text(render_markdown(output))
    print(f"Wrote {args.report_json}")
    print(f"Wrote {args.report_md}")
    return 0


def load_reports(runs_dir: Path) -> list[dict[str, object]]:
    summary = runs_dir / "summary.jsonl"
    reports: list[dict[str, object]] = []
    for line in summary.read_text().splitlines():
        if line.strip():
            reports.append(json.loads(line))
    return reports


def score_model(runs_dir: Path, report: dict[str, object]) -> dict[str, object]:
    rows: list[AliasRow] = []
    attempt_dir = find_attempt_dir(runs_dir, str(report["model_id"]))
    for result in report["results"]:
        assert isinstance(result, dict)
        parsed = load_parsed_answer(attempt_dir, str(result["case_id"]))
        canonical_answer = str(result["actual_canonical_answer"])
        answer = str(parsed.get("answer", "")) if isinstance(parsed, dict) else ""
        alias_match, alias_source = answer_matches(
            domain=str(result["domain"]),
            canonical_answer=canonical_answer,
            answer=answer,
        )
        rows.append(
            AliasRow(
                case_id=str(result["case_id"]),
                domain=str(result["domain"]),
                language=str(result["language"]),
                strict_match=bool(result["canonical_match"]),
                alias_match=alias_match,
                alias_source=alias_source,
                expected_canonical_answer=str(result["expected_canonical_answer"]),
                actual_canonical_answer=canonical_answer,
                answer=answer,
            )
        )

    domain_counts = aggregate(rows, "domain")
    language_counts = aggregate(rows, "language")
    strict_count = sum(row.strict_match for row in rows)
    alias_count = sum(row.alias_match for row in rows)
    return {
        "model_id": report["model_id"],
        "prompt_count": report["prompt_count"],
        "strict_canonical_match_count": strict_count,
        "alias_normalized_match_count": alias_count,
        "alias_lift_count": alias_count - strict_count,
        "json_valid_count": report["json_valid_count"],
        "schema_valid_count": report["schema_valid_count"],
        "domain_alias_counts": domain_counts,
        "language_alias_counts": language_counts,
        "rows": [asdict(row) for row in rows],
    }


def find_attempt_dir(runs_dir: Path, model_id: str) -> Path:
    suffix = safe_name(model_id)
    matches = sorted(path for path in runs_dir.iterdir() if path.is_dir() and path.name.endswith(suffix))
    if len(matches) != 1:
        raise FileNotFoundError(f"Expected one attempt dir for {model_id}, found {len(matches)}")
    return matches[0]


def safe_name(value: str) -> str:
    safe = "".join(char if char.isalnum() else "-" for char in value)
    while "--" in safe:
        safe = safe.replace("--", "-")
    return safe.strip("-")[:96]


def load_parsed_answer(attempt_dir: Path, case_id: str) -> dict[str, object]:
    path = attempt_dir / "raw" / case_id / "parsed.json"
    if not path.exists():
        return {}
    try:
        parsed = json.loads(path.read_text())
    except json.JSONDecodeError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def answer_matches(domain: str, canonical_answer: str, answer: str) -> tuple[bool, str]:
    if matches_alias(domain, canonical_answer):
        return True, "canonical_answer"
    if matches_alias(domain, answer):
        return True, "answer"
    return False, "none"


def matches_alias(domain: str, value: str) -> bool:
    normalized = normalize_answer(value)
    if not normalized:
        return False
    if domain == "current_affairs" and contains_uncertain_negation(normalized):
        return False
    aliases = {normalize_answer(alias) for alias in ALIAS_SETS[domain]}
    if normalized in aliases:
        return True
    if domain in {"coding", "math", "chemistry"}:
        return False
    if len(normalized) <= 3:
        return False
    return any(len(alias) > 3 and alias in normalized for alias in aliases)


def contains_uncertain_negation(normalized: str) -> bool:
    markers = [
        "unknown",
        "cannot determine",
        "can not determine",
        "no se puede determinar",
        "no se ha anunciado",
        "not announced",
        "no successor",
        "uncertain",
    ]
    return any(marker in normalized for marker in markers)


def normalize_answer(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).strip().lower()
    normalized = unicodedata.normalize("NFC", "".join(
        char for char in unicodedata.normalize("NFD", normalized) if unicodedata.category(char) != "Mn"
    ))
    normalized = normalized.replace("₂", "2")
    normalized = normalized.replace("‑", "-").replace("–", "-").replace("—", "-")
    normalized = re.sub(r"[`\"'“”‘’]", "", normalized)
    normalized = re.sub(r"\b(the|a|an|unit|si unit|answer is|canonical answer is)\b", " ", normalized)
    normalized = re.sub(r"[^0-9a-z가-힣ぁ-ゟ゠-ヿ一-龯а-яё+\-*/×·()\s]", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    compact = normalized.replace(" ", "")
    if compact in {"etf", "gdp"}:
        return compact
    return normalized


def aggregate(rows: list[AliasRow], field: str) -> dict[str, dict[str, int]]:
    counts: dict[str, dict[str, int]] = {}
    for row in rows:
        key = getattr(row, field)
        bucket = counts.setdefault(key, {"alias_match": 0, "strict_match": 0, "total": 0})
        bucket["alias_match"] += int(row.alias_match)
        bucket["strict_match"] += int(row.strict_match)
        bucket["total"] += 1
    return counts


def render_markdown(output: dict[str, object]) -> str:
    models = output["models"]
    assert isinstance(models, list)
    top_n = output["top_n"]
    lines = [
        f"# Top {top_n} Alias-Normalized Multilingual Scoring",
        "",
        "This report re-scores the existing multilingual/domain raw outputs without re-running models.",
        "Aliases are conservative: notation and translated equivalents count, but acronym-only answers do not count for expansion prompts such as GDP and ETF.",
        "",
        "| Rank | Model | Strict | Alias-normalized | Lift | JSON | Schema |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for rank, model in enumerate(
        sorted(models, key=lambda item: item["alias_normalized_match_count"], reverse=True), start=1
    ):
        assert isinstance(model, dict)
        total = model["prompt_count"]
        lines.append(
            f"| {rank} | `{model['model_id']}` | "
            f"{model['strict_canonical_match_count']}/{total} | "
            f"{model['alias_normalized_match_count']}/{total} | "
            f"+{model['alias_lift_count']} | "
            f"{model['json_valid_count']}/{total} | "
            f"{model['schema_valid_count']}/{total} |"
        )
    lines += ["", "## Notes", ""]
    lines.append("- This pass uses existing `parsed.json` artifacts and does not download or execute any model.")
    lines.append("- `alias_source=canonical_answer` means the canonical field matched an alias.")
    lines.append("- `alias_source=answer` means the localized answer was correct even when the canonical field was not.")
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
