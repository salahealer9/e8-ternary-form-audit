"""Phase 3A tests for root-space Cartan 3-form support."""

from functools import lru_cache

from e8_ternary.cartan_support import (
    SupportClass,
    build_root_space_cartan_support,
    classification_census,
    classify_root_triple,
    support_has_distinct_indices,
    support_is_s3_symmetric,
)
from e8_ternary.roots import generate_e8_roots


@lru_cache(maxsize=1)
def phase3a_data():
    roots = generate_e8_roots()
    cartan_support = build_root_space_cartan_support(roots)
    return roots, cartan_support


def test_root_space_cartan_support_count() -> None:
    _, support = phase3a_data()

    # Frozen Phase 3A expectation inherited from Phase 2C.
    assert len(support.ordered_support) == 13440


def test_root_space_support_is_s3_symmetric() -> None:
    _, support = phase3a_data()

    assert support_is_s3_symmetric(
        support.ordered_support
    )


def test_root_space_support_has_distinct_indices() -> None:
    _, support = phase3a_data()

    assert support_has_distinct_indices(
        support.ordered_support
    )


def test_classification_census_closes_complete_domain() -> None:
    roots, support = phase3a_data()
    census = classification_census(roots)

    assert sum(census.values()) == len(roots) ** 3

    assert (
        census[SupportClass.ROOT_SUPPORT_NONZERO]
        == len(support.ordered_support)
    )


def test_opposite_beta_gamma_is_forced_zero() -> None:
    roots, _ = phase3a_data()
    lookup = {
        root: index
        for index, root in enumerate(roots)
    }

    beta_index = 0
    beta = roots[beta_index]
    opposite = tuple(-x for x in beta)
    gamma_index = lookup[opposite]

    # Any root-space alpha must pair trivially with the Cartan-valued bracket.
    for alpha_index in (0, 1, 2):
        assert classify_root_triple(
            roots,
            alpha_index,
            beta_index,
            gamma_index,
            lookup=lookup,
        ) == SupportClass.FORCED_ZERO_CARTAN_BRACKET


def test_lie_support_matches_phase2c_exactly() -> None:
    # Construct the Lie-algebraic support first.
    roots, cartan_support = phase3a_data()

    lie_support = set(
        cartan_support.ordered_support
    )

    # Only after the independent Lie support exists do we construct
    # the Phase 2C Boolean support for comparison.
    from e8_ternary.incidence import build_ternary_incidence
    from e8_ternary.ternary import enumerate_zero_sum_triples

    triples = enumerate_zero_sum_triples(roots).triples
    incidence = build_ternary_incidence(
        len(roots),
        triples,
    )

    boolean_support = set(
        incidence.ordered_support
    )

    assert lie_support - boolean_support == set()
    assert boolean_support - lie_support == set()


def test_every_lie_support_entry_classifies_nonzero() -> None:
    roots, cartan_support = phase3a_data()
    lookup = {
        root: index
        for index, root in enumerate(roots)
    }

    assert all(
        classify_root_triple(
            roots,
            alpha_index,
            beta_index,
            gamma_index,
            lookup=lookup,
        ) == SupportClass.ROOT_SUPPORT_NONZERO
        for alpha_index, beta_index, gamma_index
        in cartan_support.ordered_support
    )
