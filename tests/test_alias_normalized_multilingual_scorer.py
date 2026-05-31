from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "score_alias_normalized_multilingual_suite.py"
spec = importlib.util.spec_from_file_location("score_alias_normalized_multilingual_suite", SCRIPT)
assert spec is not None
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def test_notation_aliases_count_as_matches() -> None:
    assert module.matches_alias("physics", "N") is True
    assert module.matches_alias("earth_science", "N2") is True
    assert module.matches_alias("chemistry", "Na+Cl-") is True
    assert module.matches_alias("math", "2*x") is True


def test_translated_aliases_count_as_matches() -> None:
    assert module.matches_alias("biology", "미토콘드리아") is True
    assert module.matches_alias("economics", "국내총생산") is True
    assert module.matches_alias("finance", "상장지수펀드") is True
    assert module.matches_alias("logic", "是的") is True


def test_acronym_only_expansion_answers_do_not_count() -> None:
    assert module.matches_alias("economics", "GDP") is False
    assert module.matches_alias("finance", "ETF") is False


def test_localized_answer_can_rescue_bad_canonical_field() -> None:
    matched, source = module.answer_matches(
        domain="finance",
        canonical_answer="ETF",
        answer="상장지수펀드입니다.",
    )

    assert matched is True
    assert source == "answer"


def test_uncertain_current_affairs_answer_does_not_count_by_name_mention() -> None:
    matched, source = module.answer_matches(
        domain="current_affairs",
        canonical_answer="Unknown",
        answer="No se puede determinar; the current Secretary-General, António Guterres, may change.",
    )

    assert matched is False
    assert source == "none"
