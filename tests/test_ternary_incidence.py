"""Phase 2C tests for the unsigned E8 ternary incidence object."""

from functools import lru_cache

from e8_ternary.a2 import group_by_six_root_subsystem
from e8_ternary.incidence import (
    active_pair_count,
    active_pair_doubled_dot_spectrum,
    build_ternary_incidence,
    negate_hyperedge,
    negation_index_map,
    negation_orbit_six_root_keys,
    negation_orbit_size_spectrum,
    negation_orbits,
    ordered_support_has_zero_diagonals,
    ordered_support_is_s3_symmetric,
    ordered_support_is_unique,
    pair_codegree_spectrum,
    vertex_degree_spectrum,
)
from e8_ternary.roots import generate_e8_roots
from e8_ternary.ternary import enumerate_zero_sum_triples


@lru_cache(maxsize=1)
def phase2c_data():
    roots = generate_e8_roots()
    triples = enumerate_zero_sum_triples(roots).triples
    incidence = build_ternary_incidence(len(roots), triples)
    return roots, triples, incidence


def test_hypergraph_replication_counts() -> None:
    _, triples, incidence = phase2c_data()

    assert incidence.vertex_count == 240
    assert len(incidence.hyperedges) == 2240
    assert incidence.hyperedges == triples


def test_ordered_support_count() -> None:
    _, _, incidence = phase2c_data()

    assert len(incidence.ordered_support) == 13440
    assert ordered_support_is_unique(incidence)


def test_ordered_support_is_fully_s3_symmetric() -> None:
    _, _, incidence = phase2c_data()

    assert ordered_support_is_s3_symmetric(incidence)


def test_tensor_support_has_zero_diagonals() -> None:
    _, _, incidence = phase2c_data()

    assert ordered_support_has_zero_diagonals(incidence)


def test_vertex_degree_spectrum() -> None:
    _, _, incidence = phase2c_data()

    assert vertex_degree_spectrum(incidence) == {
        28: 240,
    }


def test_pair_codegree_spectrum() -> None:
    _, _, incidence = phase2c_data()

    assert pair_codegree_spectrum(incidence) == {
        0: 21960,
        1: 6720,
    }


def test_every_active_pair_has_unique_completion() -> None:
    _, _, incidence = phase2c_data()

    assert active_pair_count(incidence) == 6720


def test_active_pair_binary_characterization() -> None:
    roots, _, incidence = phase2c_data()

    # Post-construction characterization only:
    # doubled dot -4 is ordinary inner product -1.
    assert active_pair_doubled_dot_spectrum(
        roots,
        incidence,
    ) == {
        -4: 6720,
    }


def test_global_negation_preserves_hyperedges() -> None:
    roots, _, incidence = phase2c_data()
    negation_map = negation_index_map(roots)
    edge_set = set(incidence.hyperedges)

    assert all(
        negate_hyperedge(edge, negation_map) in edge_set
        for edge in incidence.hyperedges
    )


def test_global_negation_orbits_have_size_two() -> None:
    roots, _, incidence = phase2c_data()
    negation_map = negation_index_map(roots)

    assert negation_orbit_size_spectrum(
        incidence,
        negation_map,
    ) == {
        2: 1120,
    }

    assert len(
        negation_orbits(
            incidence,
            negation_map,
        )
    ) == 1120


def test_negation_orbits_equal_phase2b_a2_quotient() -> None:
    roots, triples, incidence = phase2c_data()
    negation_map = negation_index_map(roots)

    orbit_keys = set(
        negation_orbit_six_root_keys(
            incidence,
            negation_map,
        )
    )

    a2_groups = group_by_six_root_subsystem(
        roots,
        triples,
    )

    assert orbit_keys == set(a2_groups)
