"""Phase 2B tests for the zero-sum-triple -> A2 quotient."""

from collections import Counter

from e8_ternary.a2 import (
    group_by_six_root_subsystem,
    opposite_triple,
    quotient_class_is_opposite_pair,
    quotient_multiplicity_spectrum,
    six_root_size_spectrum,
    subsystem_has_a2_structure,
    subsystem_pairwise_doubled_dot_spectrum,
    subsystem_rank,
    subsystem_reflection_closed,
)
from e8_ternary.roots import generate_e8_roots
from e8_ternary.ternary import enumerate_zero_sum_triples


def phase2b_data():
    roots = generate_e8_roots()
    triples = enumerate_zero_sum_triples(roots).triples
    groups = group_by_six_root_subsystem(roots, triples)
    return roots, triples, groups


def test_every_zero_sum_triple_has_its_opposite() -> None:
    roots, triples, _ = phase2b_data()
    triple_set = set(triples)

    assert all(
        opposite_triple(roots, triple) in triple_set
        for triple in triples
    )


def test_no_zero_sum_triple_is_self_opposite() -> None:
    roots, triples, _ = phase2b_data()

    assert all(
        opposite_triple(roots, triple) != triple
        for triple in triples
    )


def test_every_triple_opposite_union_has_six_roots() -> None:
    roots, triples, _ = phase2b_data()

    assert six_root_size_spectrum(
        roots,
        triples,
    ) == {6: 2240}


def test_quotient_multiplicity_is_two() -> None:
    _, _, groups = phase2b_data()

    assert quotient_multiplicity_spectrum(groups) == {
        2: 1120,
    }


def test_each_quotient_class_is_exactly_an_opposite_pair() -> None:
    roots, _, groups = phase2b_data()

    assert all(
        quotient_class_is_opposite_pair(roots, members)
        for members in groups.values()
    )


def test_a2_subsystem_replication_count() -> None:
    _, _, groups = phase2b_data()

    # Frozen external benchmark; not a grouping parameter.
    assert len(groups) == 1120


def test_all_subsystems_have_exact_rank_two() -> None:
    roots, _, groups = phase2b_data()

    rank_spectrum = Counter(
        subsystem_rank(roots, subsystem)
        for subsystem in groups
    )

    assert rank_spectrum == {2: 1120}


def test_all_subsystems_are_reflection_closed() -> None:
    roots, _, groups = phase2b_data()

    assert all(
        subsystem_reflection_closed(roots, subsystem)
        for subsystem in groups
    )


def test_all_subsystems_have_a2_pairwise_spectrum() -> None:
    roots, _, groups = phase2b_data()

    spectra = Counter(
        tuple(
            subsystem_pairwise_doubled_dot_spectrum(
                roots,
                subsystem,
            ).items()
        )
        for subsystem in groups
    )

    assert spectra == {
        ((-8, 3), (-4, 6), (4, 6)): 1120,
    }


def test_all_quotient_subsystems_pass_a2_structure() -> None:
    roots, _, groups = phase2b_data()

    assert sum(
        subsystem_has_a2_structure(roots, subsystem)
        for subsystem in groups
    ) == 1120
