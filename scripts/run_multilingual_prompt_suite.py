#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path

from local_model_backends import backend_of, generate_ollama, pull_ollama_model
from run_mlx_candidate_sweep import clean_reasoning_wrappers, directory_size, extract_json_object, safe_name


LANGUAGE_INSTRUCTIONS = {
    "en": "Answer in English.",
    "ko": "한국어로 답하세요.",
    "ja": "日本語で答えてください。",
    "zh": "请用中文回答。",
    "es": "Responde en español.",
    "ru": "Ответьте на русском языке.",
    "fr": "Répondez en français.",
    "de": "Antworten Sie auf Deutsch.",
    "it": "Rispondi in italiano.",
    "pt": "Responda em português.",
}


QUESTION_TRANSLATIONS = {
    "physics": {
        "en": "What is the SI unit of force?",
        "ko": "힘의 SI 단위는 무엇인가요?",
        "ja": "力のSI単位は何ですか？",
        "zh": "力的 SI 单位是什么？",
        "es": "¿Cuál es la unidad SI de la fuerza?",
        "ru": "Какова единица силы в системе СИ?",
        "fr": "Quelle est l'unité SI de la force ?",
        "de": "Was ist die SI-Einheit der Kraft?",
        "it": "Qual è l'unità SI della forza?",
        "pt": "Qual é a unidade SI de força?",
    },
    "biology": {
        "en": "Which organelle is most directly responsible for ATP production in eukaryotic cells?",
        "ko": "진핵세포에서 ATP 생산을 가장 직접적으로 담당하는 세포소기관은 무엇인가요?",
        "ja": "真核細胞でATP産生を最も直接担う細胞小器官は何ですか？",
        "zh": "在真核细胞中，哪个细胞器最直接负责 ATP 产生？",
        "es": "¿Qué orgánulo es responsable más directamente de producir ATP en células eucariotas?",
        "ru": "Какая органелла наиболее непосредственно отвечает за производство АТФ в эукариотических клетках?",
        "fr": "Quel organite est le plus directement responsable de la production d'ATP dans les cellules eucaryotes ?",
        "de": "Welches Organell ist in eukaryotischen Zellen am direktesten für die ATP-Produktion verantwortlich?",
        "it": "Quale organello è più direttamente responsabile della produzione di ATP nelle cellule eucariotiche?",
        "pt": "Qual organelo é mais diretamente responsável pela produção de ATP em células eucarióticas?",
    },
    "earth_science": {
        "en": "What is the most abundant gas in Earth's atmosphere?",
        "ko": "지구 대기에서 가장 많은 기체는 무엇인가요?",
        "ja": "地球の大気で最も多い気体は何ですか？",
        "zh": "地球大气中含量最多的气体是什么？",
        "es": "¿Cuál es el gas más abundante en la atmósfera terrestre?",
        "ru": "Какой газ наиболее распространен в атмосфере Земли?",
        "fr": "Quel est le gaz le plus abondant dans l'atmosphère terrestre ?",
        "de": "Welches Gas ist in der Erdatmosphäre am häufigsten?",
        "it": "Qual è il gas più abbondante nell'atmosfera terrestre?",
        "pt": "Qual é o gás mais abundante na atmosfera da Terra?",
    },
    "chemistry": {
        "en": "What is the chemical formula for table salt?",
        "ko": "식탁용 소금의 화학식은 무엇인가요?",
        "ja": "食塩の化学式は何ですか？",
        "zh": "食盐的化学式是什么？",
        "es": "¿Cuál es la fórmula química de la sal de mesa?",
        "ru": "Какова химическая формула поваренной соли?",
        "fr": "Quelle est la formule chimique du sel de table ?",
        "de": "Wie lautet die chemische Formel von Speisesalz?",
        "it": "Qual è la formula chimica del sale da cucina?",
        "pt": "Qual é a fórmula química do sal de cozinha?",
    },
    "math": {
        "en": "What is the derivative of x^2 with respect to x?",
        "ko": "x에 대한 x^2의 도함수는 무엇인가요?",
        "ja": "xについてx^2を微分すると何ですか？",
        "zh": "x^2 对 x 的导数是什么？",
        "es": "¿Cuál es la derivada de x^2 con respecto a x?",
        "ru": "Чему равна производная x^2 по x?",
        "fr": "Quelle est la dérivée de x^2 par rapport à x ?",
        "de": "Was ist die Ableitung von x^2 nach x?",
        "it": "Qual è la derivata di x^2 rispetto a x?",
        "pt": "Qual é a derivada de x^2 em relação a x?",
    },
    "coding": {
        "en": "In Python, what expression returns the number of elements in a list named xs?",
        "ko": "Python에서 xs라는 리스트의 원소 개수를 반환하는 표현식은 무엇인가요?",
        "ja": "Pythonでxsというリストの要素数を返す式は何ですか？",
        "zh": "在 Python 中，什么表达式会返回名为 xs 的列表元素数量？",
        "es": "En Python, ¿qué expresión devuelve el número de elementos de una lista llamada xs?",
        "ru": "В Python какое выражение возвращает число элементов в списке с именем xs?",
        "fr": "En Python, quelle expression renvoie le nombre d'éléments d'une liste nommée xs ?",
        "de": "Welcher Ausdruck gibt in Python die Anzahl der Elemente einer Liste namens xs zurück?",
        "it": "In Python, quale espressione restituisce il numero di elementi in una lista chiamata xs?",
        "pt": "Em Python, qual expressão retorna o número de elementos de uma lista chamada xs?",
    },
    "current_affairs": {
        "en": "As of May 30, 2026, who is the Secretary-General of the United Nations?",
        "ko": "2026년 5월 30일 기준 유엔 사무총장은 누구인가요?",
        "ja": "2026年5月30日時点の国連事務総長は誰ですか？",
        "zh": "截至 2026 年 5 月 30 日，联合国秘书长是谁？",
        "es": "A fecha de 30 de mayo de 2026, ¿quién es el Secretario General de las Naciones Unidas?",
        "ru": "По состоянию на 30 мая 2026 года кто является Генеральным секретарем ООН?",
        "fr": "Au 30 mai 2026, qui est le Secrétaire général des Nations Unies ?",
        "de": "Wer ist am 30. Mai 2026 der Generalsekretär der Vereinten Nationen?",
        "it": "Al 30 maggio 2026, chi è il Segretario generale delle Nazioni Unite?",
        "pt": "Em 30 de maio de 2026, quem é o Secretário-Geral das Nações Unidas?",
    },
    "economics": {
        "en": "In macroeconomics, what does GDP stand for?",
        "ko": "거시경제학에서 GDP는 무엇의 약자인가요?",
        "ja": "マクロ経済学でGDPは何の略ですか？",
        "zh": "在宏观经济学中，GDP 代表什么？",
        "es": "En macroeconomía, ¿qué significa GDP?",
        "ru": "В макроэкономике что означает GDP?",
        "fr": "En macroéconomie, que signifie GDP ?",
        "de": "Wofür steht GDP in der Makroökonomie?",
        "it": "In macroeconomia, che cosa significa GDP?",
        "pt": "Em macroeconomia, o que significa GDP?",
    },
    "finance": {
        "en": "In finance, what does ETF stand for?",
        "ko": "금융에서 ETF는 무엇의 약자인가요?",
        "ja": "金融でETFは何の略ですか？",
        "zh": "在金融中，ETF 代表什么？",
        "es": "En finanzas, ¿qué significa ETF?",
        "ru": "В финансах что означает ETF?",
        "fr": "En finance, que signifie ETF ?",
        "de": "Wofür steht ETF im Finanzwesen?",
        "it": "In finanza, che cosa significa ETF?",
        "pt": "Em finanças, o que significa ETF?",
    },
    "logic": {
        "en": "If all mammals are animals and whales are mammals, are whales animals?",
        "ko": "모든 포유류가 동물이고 고래가 포유류라면, 고래는 동물인가요?",
        "ja": "すべての哺乳類が動物で、クジラが哺乳類なら、クジラは動物ですか？",
        "zh": "如果所有哺乳动物都是动物，而鲸鱼是哺乳动物，那么鲸鱼是动物吗？",
        "es": "Si todos los mamíferos son animales y las ballenas son mamíferos, ¿son animales las ballenas?",
        "ru": "Если все млекопитающие являются животными, а киты являются млекопитающими, являются ли киты животными?",
        "fr": "Si tous les mammifères sont des animaux et que les baleines sont des mammifères, les baleines sont-elles des animaux ?",
        "de": "Wenn alle Säugetiere Tiere sind und Wale Säugetiere sind, sind Wale dann Tiere?",
        "it": "Se tutti i mammiferi sono animali e le balene sono mammiferi, le balene sono animali?",
        "pt": "Se todos os mamíferos são animais e as baleias são mamíferos, as baleias são animais?",
    },
}


@dataclass(frozen=True)
class PromptCase:
    index: int
    case_id: str
    domain: str
    language: str
    language_name: str
    question: str
    expected_canonical_answer: str
    prompt: str


@dataclass(frozen=True)
class PromptResult:
    case_id: str
    domain: str
    language: str
    status: str
    returncode: int | None
    elapsed_seconds: float
    output_chars: int
    json_valid: bool
    schema_valid: bool
    canonical_match: bool
    cleanup_applied: bool
    cleanup_reason: str
    expected_canonical_answer: str
    actual_canonical_answer: str
    error_tail: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Run multilingual domain prompts over M4 Mac mini MLX candidates.")
    parser.add_argument("--candidates", type=Path, default=Path("data/benchmark/core-text-candidates-2026-05-30.json"))
    parser.add_argument("--prompt-pack", type=Path, default=Path("data/benchmark/multilingual-domain-prompt-pack-v1.json"))
    parser.add_argument("--runs-dir", type=Path, default=Path("runs/multilingual-domain-suite-2026-05-30"))
    parser.add_argument("--start", type=int, default=0, help="Zero-based candidate offset.")
    parser.add_argument("--limit", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--download-timeout", type=int, default=1800)
    parser.add_argument("--max-tokens", type=int, default=180)
    parser.add_argument("--skip-existing", action="store_true")
    parser.add_argument("--commit-each", action="store_true")
    args = parser.parse_args()

    candidates = load_candidates(args.candidates)
    prompt_cases = build_prompt_cases(args.prompt_pack)
    selected = candidates[args.start : args.start + args.limit]
    args.runs_dir.mkdir(parents=True, exist_ok=True)
    (args.runs_dir / "prompt_pack.expanded.json").write_text(
        json.dumps([asdict(case) for case in prompt_cases], indent=2, ensure_ascii=False)
    )

    for local_index, candidate in enumerate(selected, start=args.start + 1):
        attempt_dir = args.runs_dir / f"{local_index:04d}-{safe_name(candidate['model_id'])}"
        model_report = attempt_dir / "model_report.json"
        if args.skip_existing and model_report.exists():
            print(f"SKIP model={candidate['model_id']} report={model_report}", flush=True)
            continue

        report = run_model(candidate, prompt_cases, attempt_dir, args.download_timeout, args.timeout, args.max_tokens)
        append_jsonl(args.runs_dir / "summary.jsonl", report)
        write_markdown_report(args.runs_dir / "analysis.md", args.runs_dir)

        print(
            "MODEL_RESULT "
            f"model={report['model_id']} "
            f"download={report['download_status']} "
            f"schema={report['schema_valid_count']}/{report['prompt_count']} "
            f"canonical={report['canonical_match_count']}/{report['prompt_count']} "
            f"cleanup={report['cleanup_count']} "
            f"cache={report['cleanup_status']} "
            f"report={model_report}",
            flush=True,
        )
        if args.commit_each:
            commit_model_result(args.runs_dir, attempt_dir, report["model_id"])

    return 0


def load_candidates(path: Path) -> list[dict[str, str]]:
    data = json.loads(path.read_text())
    return data["candidates"]


def build_prompt_cases(path: Path) -> list[PromptCase]:
    data = json.loads(path.read_text())
    cases: list[PromptCase] = []
    index = 0
    for task in data["tasks"]:
        domain = task["domain"]
        for language in data["languages"]:
            index += 1
            code = language["code"]
            question = QUESTION_TRANSLATIONS[domain][code]
            prompt = render_prompt(
                language_code=code,
                language_name=language["name"],
                domain=domain,
                question=question,
            )
            cases.append(
                PromptCase(
                    index=index,
                    case_id=f"{index:03d}-{domain}-{code}",
                    domain=domain,
                    language=code,
                    language_name=language["name"],
                    question=question,
                    expected_canonical_answer=task["expected_canonical_answer"],
                    prompt=prompt,
                )
            )
    return cases


def render_prompt(language_code: str, language_name: str, domain: str, question: str) -> str:
    instruction = LANGUAGE_INSTRUCTIONS[language_code]
    return f"""You are being evaluated for multilingual factual answering on an M4 Mac mini.

{instruction}
Return exactly one JSON object and no prose.
The JSON object must use this schema:
{{"answer":"...", "canonical_answer":"...", "confidence":"low|medium|high"}}

Rules:
- `answer` must be in {language_name}.
- `canonical_answer` must be the shortest stable answer in English, math notation, or a chemical/code symbol.
- Do not include markdown fences.

Domain: {domain}
Question: {question}
"""


def run_model(
    candidate: dict[str, str],
    prompt_cases: list[PromptCase],
    attempt_dir: Path,
    download_timeout: int,
    timeout: int,
    max_tokens: int,
) -> dict[str, object]:
    if attempt_dir.exists():
        shutil.rmtree(attempt_dir)
    attempt_dir.mkdir(parents=True)
    (attempt_dir / "candidate.json").write_text(json.dumps(candidate, indent=2, ensure_ascii=False))

    backend = backend_of(candidate)
    cache_dir = attempt_dir / "model-cache"
    env = os.environ.copy()
    if backend == "mlx":
        cache_dir.mkdir()
        env["HF_HOME"] = str(cache_dir / "hf-home")
        env["HF_HUB_CACHE"] = str(cache_dir / "hf-home" / "hub")
        env["TRANSFORMERS_CACHE"] = str(cache_dir / "transformers")

    total_start = time.perf_counter()
    if backend == "ollama":
        download_status, download_elapsed, download_stdout, download_stderr = pull_ollama_model(
            candidate["model_id"], download_timeout
        )
    else:
        download_status, download_elapsed, download_stdout, download_stderr = download_model(
            candidate["model_id"], env, download_timeout
        )
    (attempt_dir / "download_stdout.txt").write_text(download_stdout)
    (attempt_dir / "download_stderr.txt").write_text(download_stderr)

    results: list[PromptResult] = []
    if download_status == "ok":
        for case in prompt_cases:
            result = run_prompt_case(candidate, case, attempt_dir, env, timeout, max_tokens)
            results.append(result)
    else:
        for case in prompt_cases:
            results.append(
                PromptResult(
                    case_id=case.case_id,
                    domain=case.domain,
                    language=case.language,
                    status="download_not_available",
                    returncode=None,
                    elapsed_seconds=0.0,
                    output_chars=0,
                    json_valid=False,
                    schema_valid=False,
                    canonical_match=False,
                    cleanup_applied=False,
                    cleanup_reason="none",
                    expected_canonical_answer=case.expected_canonical_answer,
                    actual_canonical_answer="",
                    error_tail=tail(download_stderr),
                )
            )

    cache_bytes = directory_size(cache_dir) if cache_dir.exists() else 0
    cleanup_status = "not_required" if backend == "ollama" else "not_started"
    cleanup_error = ""
    if cache_dir.exists():
        try:
            shutil.rmtree(cache_dir)
            cleanup_status = "deleted"
        except Exception as exc:  # noqa: BLE001
            cleanup_status = "failed"
            cleanup_error = repr(exc)

    elapsed = round(time.perf_counter() - total_start, 3)
    report = {
        "model_id": candidate["model_id"],
        "backend": backend,
        "sweep_index": candidate.get("sweep_index"),
        "params": candidate.get("params", ""),
        "routing_label": candidate.get("routing_label", ""),
        "prompt_count": len(results),
        "download_status": download_status,
        "download_elapsed_seconds": download_elapsed,
        "elapsed_seconds": elapsed,
        "json_valid_count": sum(1 for item in results if item.json_valid),
        "schema_valid_count": sum(1 for item in results if item.schema_valid),
        "canonical_match_count": sum(1 for item in results if item.canonical_match),
        "cleanup_count": sum(1 for item in results if item.cleanup_applied),
        "cache_dir": str(cache_dir),
        "cache_bytes_before_cleanup": cache_bytes,
        "cleanup_status": cleanup_status,
        "cleanup_error": cleanup_error,
        "results": [asdict(item) for item in results],
    }
    (attempt_dir / "model_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False))
    (attempt_dir / "model_report.md").write_text(render_model_markdown(report))
    return report


def download_model(model_id: str, env: dict[str, str], timeout: int) -> tuple[str, float, str, str]:
    start = time.perf_counter()
    command = [
        sys.executable,
        "-c",
        (
            "from huggingface_hub import snapshot_download; "
            "import sys; "
            "snapshot_download(repo_id=sys.argv[1], local_files_only=False)"
        ),
        model_id,
    ]
    try:
        completed = subprocess.run(
            command,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            env=env,
        )
        status = "ok" if completed.returncode == 0 else "failed"
        stdout = completed.stdout or ""
        stderr = completed.stderr or ""
    except subprocess.TimeoutExpired as exc:
        status = "timeout"
        stdout = decode_maybe(exc.stdout)
        stderr = decode_maybe(exc.stderr)
    except Exception as exc:  # noqa: BLE001
        status = "error"
        stdout = ""
        stderr = repr(exc)
    return status, round(time.perf_counter() - start, 3), stdout, stderr


def run_prompt_case(
    candidate: dict[str, str],
    case: PromptCase,
    attempt_dir: Path,
    env: dict[str, str],
    timeout: int,
    max_tokens: int,
) -> PromptResult:
    model_id = candidate["model_id"]
    backend = backend_of(candidate)
    case_dir = attempt_dir / "raw" / case.case_id
    case_dir.mkdir(parents=True)
    (case_dir / "prompt.json").write_text(json.dumps(asdict(case), indent=2, ensure_ascii=False))
    (case_dir / "prompt.txt").write_text(case.prompt)
    command = ollama_command(model_id, case.prompt, max_tokens) if backend == "ollama" else [
        sys.executable,
        "-m",
        "mlx_lm",
        "generate",
        "--model",
        model_id,
        "--prompt",
        case.prompt,
        "--max-tokens",
        str(max_tokens),
        "--temp",
        "0.0",
        "--verbose",
        "False",
    ]
    (case_dir / "command.json").write_text(json.dumps(command, indent=2, ensure_ascii=False))
    start = time.perf_counter()
    stdout = ""
    stderr = ""
    returncode: int | None = None
    status = "error"
    try:
        if backend == "ollama":
            stdout, status, stderr = generate_ollama(model_id, case.prompt, timeout, max_tokens)
            returncode = 0 if status == "ok" else 1
        else:
            completed = subprocess.run(
                command,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=timeout,
                env=env,
            )
            stdout = completed.stdout or ""
            stderr = completed.stderr or ""
            returncode = completed.returncode
            status = "ok" if completed.returncode == 0 and stdout.strip() else "failed"
    except subprocess.TimeoutExpired as exc:
        status = "timeout"
        stdout = decode_maybe(exc.stdout)
        stderr = decode_maybe(exc.stderr)
    except Exception as exc:  # noqa: BLE001
        stderr = repr(exc)
    elapsed = round(time.perf_counter() - start, 3)

    cleaned, cleanup_reason = clean_reasoning_wrappers(stdout)
    parsed = extract_json_object(cleaned)
    actual = ""
    schema_valid = False
    if isinstance(parsed, dict):
        actual = str(parsed.get("canonical_answer", "")).strip()
        schema_valid = (
            isinstance(parsed.get("answer"), str)
            and isinstance(parsed.get("canonical_answer"), str)
            and parsed.get("confidence") in {"low", "medium", "high"}
        )
    canonical_match = canonical_matches(actual, case.expected_canonical_answer)

    (case_dir / "stdout.txt").write_text(stdout)
    (case_dir / "stdout.cleaned.txt").write_text(cleaned)
    (case_dir / "stderr.txt").write_text(stderr)
    (case_dir / "parsed.json").write_text(json.dumps(parsed, indent=2, ensure_ascii=False))
    result = PromptResult(
        case_id=case.case_id,
        domain=case.domain,
        language=case.language,
        status=status,
        returncode=returncode,
        elapsed_seconds=elapsed,
        output_chars=len(stdout),
        json_valid=isinstance(parsed, dict),
        schema_valid=schema_valid,
        canonical_match=canonical_match,
        cleanup_applied=cleaned != stdout,
        cleanup_reason=cleanup_reason,
        expected_canonical_answer=case.expected_canonical_answer,
        actual_canonical_answer=actual,
        error_tail=tail(stderr),
    )
    (case_dir / "result.json").write_text(json.dumps(asdict(result), indent=2, ensure_ascii=False))
    return result


def ollama_command(model_id: str, prompt: str, max_tokens: int) -> list[str]:
    return ["ollama", "api", "generate", model_id, f"prompt_chars={len(prompt)}", f"num_predict={max_tokens}"]


def canonical_matches(actual: str, expected: str) -> bool:
    return normalize_canonical(actual) == normalize_canonical(expected)


def normalize_canonical(value: str) -> str:
    normalized = value.strip().lower()
    normalized = normalized.replace("antónio", "antonio")
    normalized = normalized.replace("‑", "-").replace("–", "-").replace("—", "-")
    normalized = re.sub(r"[\s_]+", " ", normalized)
    normalized = normalized.replace(" ", "")
    normalized = normalized.replace("-", "")
    return normalized


def render_model_markdown(report: dict[str, object]) -> str:
    rows = report["results"]
    assert isinstance(rows, list)
    domain_counts: dict[str, tuple[int, int]] = {}
    language_counts: dict[str, tuple[int, int]] = {}
    for row in rows:
        assert isinstance(row, dict)
        domain = str(row["domain"])
        language = str(row["language"])
        domain_counts[domain] = increment_pair(domain_counts.get(domain, (0, 0)), bool(row["canonical_match"]))
        language_counts[language] = increment_pair(language_counts.get(language, (0, 0)), bool(row["canonical_match"]))

    lines = [
        f"# Multilingual Domain Suite - {report['model_id']}",
        "",
        f"- Prompts: {report['prompt_count']}",
        f"- Download: {report['download_status']} in {report['download_elapsed_seconds']}s",
        f"- JSON valid: {report['json_valid_count']}/{report['prompt_count']}",
        f"- Schema valid: {report['schema_valid_count']}/{report['prompt_count']}",
        f"- Canonical match: {report['canonical_match_count']}/{report['prompt_count']}",
        f"- Cleanup applied: {report['cleanup_count']}",
        f"- Cache cleanup: {report['cleanup_status']}",
        "",
        "## Domain Canonical Match",
        "",
    ]
    for key in sorted(domain_counts):
        matched, total = domain_counts[key]
        lines.append(f"- `{key}`: {matched}/{total}")
    lines += ["", "## Language Canonical Match", ""]
    for key in sorted(language_counts):
        matched, total = language_counts[key]
        lines.append(f"- `{key}`: {matched}/{total}")
    lines.append("")
    return "\n".join(lines)


def increment_pair(pair: tuple[int, int], matched: bool) -> tuple[int, int]:
    current, total = pair
    return current + int(matched), total + 1


def write_markdown_report(path: Path, runs_dir: Path) -> None:
    reports = []
    summary = runs_dir / "summary.jsonl"
    if summary.exists():
        for line in summary.read_text().splitlines():
            if line.strip():
                reports.append(json.loads(line))
    lines = [
        "# Multilingual Domain Suite Progress",
        "",
        "The suite runs 10 domains across 10 languages for each M4 Mac mini text candidate.",
        "Raw prompt/output/parsed artifacts are stored under each model attempt directory.",
        "",
        "| Model | JSON | Schema | Canonical | Cleanup | Download s | Cache |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for report in reports:
        lines.append(
            f"| `{report['model_id']}` | "
            f"{report['json_valid_count']}/{report['prompt_count']} | "
            f"{report['schema_valid_count']}/{report['prompt_count']} | "
            f"{report['canonical_match_count']}/{report['prompt_count']} | "
            f"{report['cleanup_count']} | "
            f"{report['download_elapsed_seconds']} | "
            f"{report['cleanup_status']} |"
        )
    lines.append("")
    path.write_text("\n".join(lines))


def append_jsonl(path: Path, item: dict[str, object]) -> None:
    with path.open("a") as handle:
        handle.write(json.dumps(item, ensure_ascii=False) + "\n")


def commit_model_result(runs_dir: Path, attempt_dir: Path, model_id: str) -> None:
    subprocess.run(
        [
            "git",
            "add",
            "-f",
            str(runs_dir / "prompt_pack.expanded.json"),
            str(runs_dir / "summary.jsonl"),
            str(runs_dir / "analysis.md"),
            str(attempt_dir),
        ],
        check=True,
    )
    safe_model = safe_name(model_id)[:60]
    subprocess.run(["git", "commit", "-m", f"Add multilingual suite result for {safe_model}"], check=True)


def decode_maybe(value: str | bytes | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode(errors="replace")
    return value


def tail(text: str, max_chars: int = 2000) -> str:
    return text[-max_chars:]


if __name__ == "__main__":
    raise SystemExit(main())
