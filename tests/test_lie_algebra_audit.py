"""Phase 4A exhaustive E8 Lie-algebra identity audit tests."""

from functools import lru_cache
from pathlib import Path

from e8_ternary.canonical_basis import (
    simple_root_gram_matrix,
)
from e8_ternary.lie_algebra_audit import (
    BASIS_DIMENSION,
    CANONICAL_JACOBI_DOMAIN,
    ORDERED_PAIR_DOMAIN,
    bilinear_support_count,
    bilinear_symmetry_holds,
    bilinear_value_spectrum,
    bracket_antisymmetry_holds,
    bracket_closure_holds,
    build_basis_bracket_table,
    build_bilinear_table,
    build_invariance_maps,
    exact_integer_determinant,
    exhaustive_jacobi_audit,
    nonzero_bracket_pairs,
    scalar_map_discrepancies,
    scalar_map_spectrum,
    self_brackets_zero,
    sha256_file,
    structural_nondegeneracy_holds,
)
from e8_ternary.roots import generate_e8_roots
from e8_ternary.sparse_cartan_form import (
    load_sparse_cartan_form,
)


PHASE3D_JSON = Path(
    "data/derived/"
    "phase3d_signed_sparse_cartan_form.json"
)

PHASE3D_SHA256 = (
    "43b52b4116dfcf0dace332234b5c9dc50"
    "d95d51effb690aec8aebe39ad4f92e8"
)


@lru_cache(maxsize=1)
def phase4a_data():
    roots = generate_e8_roots()

    bracket = build_basis_bracket_table(
        roots
    )

    bilinear = build_bilinear_table(
        roots
    )

    jacobi = exhaustive_jacobi_audit(
        bracket
    )

    left_map, right_map = (
        build_invariance_maps(
            bracket,
            bilinear,
        )
    )

    return (
        roots,
        bracket,
        bilinear,
        jacobi,
        left_map,
        right_map,
    )


def test_phase4a_bracket_support_and_structure() -> None:
    (
        _,
        bracket,
        _,
        _,
        _,
        _,
    ) = phase4a_data()

    assert BASIS_DIMENSION == 248
    assert ORDERED_PAIR_DOMAIN == 61504

    assert len(
        nonzero_bracket_pairs(bracket)
    ) == 15504

    assert bracket_antisymmetry_holds(
        bracket
    )

    assert self_brackets_zero(
        bracket
    )

    assert bracket_closure_holds(
        bracket
    )


def test_phase4a_exhaustive_jacobi() -> None:
    (
        _,
        _,
        _,
        jacobi,
        _,
        _,
    ) = phase4a_data()

    assert jacobi.total_checked == (
        CANONICAL_JACOBI_DOMAIN
    )

    assert jacobi.sector_checked == {
        "HHH": 56,
        "HHR": 6720,
        "HRR": 229440,
        "RRR": 2275280,
    }

    assert jacobi.sector_failures == {
        "HHH": 0,
        "HHR": 0,
        "HRR": 0,
        "RRR": 0,
    }

    assert jacobi.total_failures == 0
    assert jacobi.failure_examples == ()


def test_phase4a_bilinear_form() -> None:
    (
        roots,
        _,
        bilinear,
        _,
        _,
        _,
    ) = phase4a_data()

    assert bilinear_support_count(
        bilinear
    ) == 262

    assert bilinear_value_spectrum(
        bilinear
    ) == {
        -1: 142,
        1: 112,
        2: 8,
    }

    assert bilinear_symmetry_holds(
        bilinear
    )

    assert exact_integer_determinant(
        simple_root_gram_matrix()
    ) == 1

    assert structural_nondegeneracy_holds(
        roots,
        bilinear,
    )


def test_phase4a_invariance_maps_agree_exactly() -> None:
    (
        _,
        _,
        _,
        _,
        left_map,
        right_map,
    ) = phase4a_data()

    assert len(left_map) == 16176
    assert len(right_map) == 16176

    assert scalar_map_spectrum(
        left_map
    ) == {
        -2: 24,
        -1: 8064,
        1: 8064,
        2: 24,
    }

    assert scalar_map_spectrum(
        right_map
    ) == {
        -2: 24,
        -1: 8064,
        1: 8064,
        2: 24,
    }

    (
        left_only,
        right_only,
        differing,
    ) = scalar_map_discrepancies(
        left_map,
        right_map,
    )

    assert left_only == set()
    assert right_only == set()
    assert differing == {}


def test_phase3d_artifact_integrity() -> None:
    assert PHASE3D_JSON.is_file()

    assert sha256_file(
        PHASE3D_JSON
    ) == PHASE3D_SHA256


def test_phase4a_algebra_map_matches_sealed_phase3d() -> None:
    (
        _,
        _,
        _,
        _,
        _,
        algebra_map,
    ) = phase4a_data()

    # Only after the algebra-level construction exists do we load
    # the sealed Phase 3D tensor.
    phase3d = load_sparse_cartan_form(
        PHASE3D_JSON
    )

    phase3d_map = {
        entry.key: entry.coefficient
        for entry in phase3d.entries
    }

    assert len(algebra_map) == 16176
    assert len(phase3d_map) == 16176

    (
        algebra_only,
        phase3d_only,
        differing,
    ) = scalar_map_discrepancies(
        algebra_map,
        phase3d_map,
    )

    assert algebra_only == set()
    assert phase3d_only == set()
    assert differing == {}
