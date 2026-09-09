"""Repository-level smoke tests."""

from pathlib import Path

import e8_ternary
import e8_ternary.roots


ROOT = Path(__file__).resolve().parents[1]


def test_package_imports() -> None:
    assert e8_ternary is not None
    assert e8_ternary.roots is not None


def test_phase0_documents_remain_present() -> None:
    required = [
        "README.md",
        "docs/scope.md",
        "docs/preregistration.md",
        "docs/research_questions.md",
        "docs/notation.md",
        "docs/literature_map.md",
        "docs/checkpoints/phase0_closeout.md",
    ]

    for relative_path in required:
        assert (ROOT / relative_path).is_file()


def test_phase1a_protocol_exists() -> None:
    assert (
        ROOT / "docs/checkpoints/phase1a_root_construction_protocol.md"
    ).is_file()
