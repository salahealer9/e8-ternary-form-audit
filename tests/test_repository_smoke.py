"""Phase 0 repository smoke tests.

These tests deliberately contain no E8 computation.
"""

from pathlib import Path

import e8_ternary


ROOT = Path(__file__).resolve().parents[1]


def test_package_imports() -> None:
    assert e8_ternary is not None


def test_phase0_documents_exist() -> None:
    required = [
        "README.md",
        "docs/scope.md",
        "docs/preregistration.md",
        "docs/research_questions.md",
        "docs/notation.md",
        "docs/literature_map.md",
    ]

    for relative_path in required:
        assert (ROOT / relative_path).is_file()


def test_no_phase1_root_module_yet() -> None:
    """Phase 0 must precede implementation of the E8 enumeration."""
    assert not (ROOT / "src/e8_ternary/roots.py").exists()
