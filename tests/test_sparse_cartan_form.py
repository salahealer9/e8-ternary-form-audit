"""Phase 3D signed sparse E8 Cartan 3-form tests."""

import json
from functools import lru_cache

from e8_ternary.incidence import (
    build_ternary_incidence,
)
from e8_ternary.roots import generate_e8_roots
from e8_ternary.sparse_cartan_form import (
    BASIS_DIMENSION,
    TOTAL_ORDERED_DOMAIN,
    SparseSector,
    all_indices_distinct,
    build_alternating_reconstruction,
    build_direct_sparse_cartan_form,
    coefficient_spectrum,
    export_sparse_cartan_form,
    full_alternation_holds,
    hrr_entries_use_opposite_roots,
    load_sparse_cartan_form,
    no_hhr_or_hhh_entries,
    rrr_cyclic_formula_consistency,
    rrr_root_index_support,
    sector_counts,
    sparse_form_discrepancies,
)
from e8_ternary.ternary import (
    enumerate_zero_sum_triples,
)


@lru_cache(maxsize=1)
def phase3d_data():
    roots = generate_e8_roots()
    direct = build_direct_sparse_cartan_form(
        roots
    )
    reconstructed = (
        build_alternating_reconstruction(
            roots
        )
    )

    return roots, direct, reconstructed


def test_phase3d_basis_and_domain() -> None:
    _, direct, _ = phase3d_data()

    assert BASIS_DIMENSION == 248
    assert TOTAL_ORDERED_DOMAIN == 248**3
    assert TOTAL_ORDERED_DOMAIN == 15252992
    assert direct.basis_dimension == 248


def test_phase3d_sector_counts() -> None:
    _, direct, _ = phase3d_data()

    assert sector_counts(direct) == {
        SparseSector.HRR: 2736,
        SparseSector.RRR: 13440,
    }

    assert direct.nonzero_count == 16176


def test_phase3d_full_coefficient_spectrum() -> None:
    _, direct, _ = phase3d_data()

    assert coefficient_spectrum(
        direct
    ) == {
        -2: 24,
        -1: 8064,
        1: 8064,
        2: 24,
    }


def test_rrr_coefficients_are_plus_or_minus_one() -> None:
    _, direct, _ = phase3d_data()

    assert {
        entry.coefficient
        for entry in direct.entries
        if entry.sector == SparseSector.RRR
    } == {-1, 1}


def test_hrr_coefficients_are_plus_or_minus_one_or_two() -> None:
    _, direct, _ = phase3d_data()

    assert {
        entry.coefficient
        for entry in direct.entries
        if entry.sector == SparseSector.HRR
    } == {-2, -1, 1, 2}


def test_sparse_entries_have_distinct_indices() -> None:
    _, direct, _ = phase3d_data()

    assert all_indices_distinct(direct)


def test_primary_sparse_form_is_fully_alternating() -> None:
    _, direct, _ = phase3d_data()

    assert full_alternation_holds(
        direct
    )


def test_rrr_cyclic_formula_consistency() -> None:
    roots, _, _ = phase3d_data()

    assert rrr_cyclic_formula_consistency(
        roots
    )


def test_direct_and_alternating_routes_agree_exactly() -> None:
    _, direct, reconstructed = phase3d_data()

    (
        direct_only,
        reconstructed_only,
        differing,
    ) = sparse_form_discrepancies(
        direct,
        reconstructed,
    )

    assert direct_only == set()
    assert reconstructed_only == set()
    assert differing == {}


def test_phase3d_rrr_support_matches_phase2c_exactly() -> None:
    roots, direct, _ = phase3d_data()

    phase3d_support = rrr_root_index_support(
        direct
    )

    triples = enumerate_zero_sum_triples(
        roots
    ).triples

    incidence = build_ternary_incidence(
        len(roots),
        triples,
    )

    phase2c_support = set(
        incidence.ordered_support
    )

    assert phase3d_support - phase2c_support == set()
    assert phase2c_support - phase3d_support == set()


def test_no_hhr_or_hhh_entries() -> None:
    _, direct, _ = phase3d_data()

    assert no_hhr_or_hhh_entries(
        direct
    )


def test_every_hrr_entry_uses_opposite_roots() -> None:
    roots, direct, _ = phase3d_data()

    assert hrr_entries_use_opposite_roots(
        direct,
        roots,
    )


def test_sparse_value_set_is_exact() -> None:
    _, direct, _ = phase3d_data()

    assert {
        entry.coefficient
        for entry in direct.entries
    } == {
        -2,
        -1,
        1,
        2,
    }


def test_phase3d_support_density() -> None:
    _, direct, _ = phase3d_data()

    assert direct.nonzero_count == 16176

    assert abs(
        direct.support_density
        - 0.001060513242254372
    ) < 1e-15


def test_export_round_trip(tmp_path) -> None:
    roots, direct, _ = phase3d_data()

    output = tmp_path / "cartan.json"

    export_sparse_cartan_form(
        output,
        direct,
        roots,
    )

    loaded = load_sparse_cartan_form(
        output
    )

    assert loaded == direct


def test_export_is_deterministic_and_contains_metadata(
    tmp_path,
) -> None:
    roots, direct, _ = phase3d_data()

    first = tmp_path / "first.json"
    second = tmp_path / "second.json"

    export_sparse_cartan_form(
        first,
        direct,
        roots,
    )
    export_sparse_cartan_form(
        second,
        direct,
        roots,
    )

    assert (
        first.read_bytes()
        == second.read_bytes()
    )

    payload = json.loads(
        first.read_text()
    )

    assert payload["schema"] == (
        "phase3d_signed_sparse_cartan_form.v1"
    )
    assert payload["basis_dimension"] == 248
    assert payload["cartan_dimension"] == 8
    assert payload["root_dimension"] == 240
    assert payload["nonzero_entry_count"] == 16176

    assert payload["sector_counts"] == {
        "HRR": 2736,
        "RRR": 13440,
    }

    assert payload["coefficient_spectrum"] == {
        "-2": 24,
        "-1": 8064,
        "1": 8064,
        "2": 24,
    }

    assert payload["epsilon"] == [
        1,
        -1,
        1,
        -1,
        1,
        -1,
        1,
        -1,
    ]

    assert len(
        payload["entries"]
    ) == 16176
