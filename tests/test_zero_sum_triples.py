"""Phase 2A tests for exhaustive E8 zero-sum root triples."""

from math import comb

from e8_ternary.roots import generate_e8_roots
from e8_ternary.ternary import (
    enumerate_zero_sum_triples,
    ordered_triple_count,
    root_incidence_counts,
    triple_contains_opposite_pair,
    triple_signature_spectrum,
    triples_all_sum_to_zero,
    triples_are_canonical_and_distinct,
    triples_are_unique,
)


def test_complete_candidate_space_is_examined() -> None:
    roots = generate_e8_roots()
    result = enumerate_zero_sum_triples(roots)

    assert result.candidate_count == comb(len(roots), 3)


def test_unordered_zero_sum_triple_replication_count() -> None:
    roots = generate_e8_roots()
    result = enumerate_zero_sum_triples(roots)

    # Frozen Phase 2A validation expectation.
    assert len(result.triples) == 2240


def test_implied_ordered_zero_sum_count() -> None:
    roots = generate_e8_roots()
    result = enumerate_zero_sum_triples(roots)

    # Frozen Phase 2A validation expectation.
    assert ordered_triple_count(result.triples) == 13440


def test_retained_triples_are_canonical_unique_and_exact() -> None:
    roots = generate_e8_roots()
    result = enumerate_zero_sum_triples(roots)

    assert triples_are_canonical_and_distinct(result.triples)
    assert triples_are_unique(result.triples)
    assert triples_all_sum_to_zero(roots, result.triples)


def test_root_incidence_is_uniform() -> None:
    roots = generate_e8_roots()
    result = enumerate_zero_sum_triples(roots)

    incidences = root_incidence_counts(
        len(roots),
        result.triples,
    )

    # Frozen derived Phase 2A expectation.
    assert set(incidences) == {28}


def test_zero_sum_triple_inner_product_signature() -> None:
    roots = generate_e8_roots()
    result = enumerate_zero_sum_triples(roots)

    # Doubled dot -4 corresponds to ordinary inner product -1.
    assert triple_signature_spectrum(
        roots,
        result.triples,
    ) == {
        (-4, -4, -4): 2240,
    }


def test_no_retained_triple_contains_opposite_roots() -> None:
    roots = generate_e8_roots()
    result = enumerate_zero_sum_triples(roots)

    assert not any(
        triple_contains_opposite_pair(roots, triple)
        for triple in result.triples
    )
