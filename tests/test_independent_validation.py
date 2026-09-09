"""Phase 1B independent E8 validation tests."""

from e8_ternary.roots import generate_e8_roots
from e8_ternary.validation import (
    crystallographic_integrality,
    exact_rank,
    generate_lattice_roots,
    nonorthogonality_graph_connected,
    reflection_closure,
    set_differences,
)


def test_independent_lattice_count() -> None:
    lattice_roots = generate_lattice_roots()

    # Frozen external benchmark; not a generation parameter.
    assert len(lattice_roots) == 240


def test_independent_set_matches_phase1a_exactly() -> None:
    # Independent construction is completed first.
    lattice_roots = generate_lattice_roots()

    # Only now obtain the Phase 1A construction.
    phase1a_roots = generate_e8_roots()

    left_only, right_only = set_differences(
        lattice_roots,
        phase1a_roots,
    )

    assert left_only == ()
    assert right_only == ()


def test_exact_root_rank_is_eight() -> None:
    lattice_roots = generate_lattice_roots()
    assert exact_rank(lattice_roots) == 8


def test_crystallographic_integrality() -> None:
    lattice_roots = generate_lattice_roots()
    assert crystallographic_integrality(lattice_roots)


def test_reflection_closure() -> None:
    lattice_roots = generate_lattice_roots()
    assert reflection_closure(lattice_roots)


def test_nonorthogonality_graph_is_connected() -> None:
    lattice_roots = generate_lattice_roots()
    assert nonorthogonality_graph_connected(lattice_roots)
