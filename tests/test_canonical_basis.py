"""Phase 3C canonical E8 basis and normalization tests."""

from collections import Counter
from functools import lru_cache

from e8_ternary.canonical_basis import (
    SIMPLE_ROOTS,
    RootSign,
    canonical_structure_constant,
    cartan_root_value,
    classify_root_sign,
    derive_epsilon,
    dynkin_edges,
    normalized_cartan_pairing_with_coroot,
    normalized_opposite_root_pairing,
    opposite_pairing_invariance_holds,
    ordinary_inner_product,
    root_expansion_map,
    root_height,
    simple_coordinates,
    simple_root_gram_matrix,
    structure_constant_sign_spectrum,
    structure_constant_table,
)
from e8_ternary.roots import (
    generate_e8_roots,
    doubled_norm_squared,
)
from e8_ternary.validation import exact_rank


@lru_cache(maxsize=1)
def phase3c_data():
    roots = generate_e8_roots()
    expansions = root_expansion_map(roots)
    table = structure_constant_table(roots)

    return roots, expansions, table


def test_frozen_simple_roots_are_valid_e8_roots() -> None:
    roots, _, _ = phase3c_data()
    root_set = set(roots)

    assert all(
        root in root_set
        for root in SIMPLE_ROOTS
    )

    assert all(
        doubled_norm_squared(root) == 8
        for root in SIMPLE_ROOTS
    )

    assert exact_rank(SIMPLE_ROOTS) == 8


def test_simple_root_gram_matrix_and_dynkin_edges() -> None:
    assert simple_root_gram_matrix() == (
        (2, -1, 0, 0, 0, 0, 0, 0),
        (-1, 2, -1, 0, 0, 0, 0, 0),
        (0, -1, 2, -1, 0, 0, 0, 0),
        (0, 0, -1, 2, -1, 0, 0, 0),
        (0, 0, 0, -1, 2, -1, 0, -1),
        (0, 0, 0, 0, -1, 2, -1, 0),
        (0, 0, 0, 0, 0, -1, 2, 0),
        (0, 0, 0, 0, -1, 0, 0, 2),
    )

    assert dynkin_edges() == (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (4, 7),
        (5, 6),
    )


def test_all_root_expansions_are_integral_and_sign_coherent() -> None:
    roots, expansions, _ = phase3c_data()

    assert len(expansions) == 240

    signs = Counter(
        classify_root_sign(expansions[root])
        for root in roots
    )

    assert signs == {
        RootSign.POSITIVE: 120,
        RootSign.NEGATIVE: 120,
    }


def test_simple_roots_have_unit_simple_coordinates() -> None:
    for index, root in enumerate(SIMPLE_ROOTS):
        expected = tuple(
            1 if coordinate == index else 0
            for coordinate in range(8)
        )

        assert simple_coordinates(root) == expected


def test_root_height_range_is_e8_range() -> None:
    roots, expansions, _ = phase3c_data()

    heights = [
        root_height(expansions[root])
        for root in roots
    ]

    assert min(heights) == -29
    assert max(heights) == 29
    assert 0 not in heights


def test_epsilon_is_frozen_and_alternates_on_edges() -> None:
    epsilon = derive_epsilon()

    assert epsilon == (
        1,
        -1,
        1,
        -1,
        1,
        -1,
        1,
        -1,
    )

    assert all(
        epsilon[left] == -epsilon[right]
        for left, right in dynkin_edges()
    )


def test_all_admissible_structure_constants_are_plus_or_minus_one() -> None:
    roots, _, table = phase3c_data()

    assert len(table) == 13440

    assert set(
        entry.coefficient
        for entry in table
    ) == {-1, 1}

    assert structure_constant_sign_spectrum(
        roots
    ) == {
        -1: 6720,
        1: 6720,
    }


def test_structure_constants_are_antisymmetric() -> None:
    roots, expansions, _ = phase3c_data()
    root_set = set(roots)
    epsilon = derive_epsilon()

    for alpha in roots:
        for beta in roots:
            summed = tuple(
                a + b
                for a, b in zip(alpha, beta, strict=True)
            )

            if summed not in root_set:
                continue

            forward = canonical_structure_constant(
                alpha,
                beta,
                roots=roots,
                expansions=expansions,
                epsilon=epsilon,
            )

            reverse = canonical_structure_constant(
                beta,
                alpha,
                roots=roots,
                expansions=expansions,
                epsilon=epsilon,
            )

            assert reverse == -forward


def test_structure_constants_obey_simultaneous_negation_identity() -> None:
    roots, expansions, _ = phase3c_data()
    root_set = set(roots)
    epsilon = derive_epsilon()

    for alpha in roots:
        for beta in roots:
            summed = tuple(
                a + b
                for a, b in zip(alpha, beta, strict=True)
            )

            if summed not in root_set:
                continue

            negative_alpha = tuple(-value for value in alpha)
            negative_beta = tuple(-value for value in beta)

            forward = canonical_structure_constant(
                alpha,
                beta,
                roots=roots,
                expansions=expansions,
                epsilon=epsilon,
            )

            negative = canonical_structure_constant(
                negative_alpha,
                negative_beta,
                roots=roots,
                expansions=expansions,
                epsilon=epsilon,
            )

            assert negative == -forward


def test_simple_root_structure_constants_and_b0_pairing() -> None:
    roots, expansions, _ = phase3c_data()
    root_set = set(roots)
    epsilon = derive_epsilon()

    simple_checks = 0

    for simple_index, alpha in enumerate(SIMPLE_ROOTS):
        for beta in roots:
            summed = tuple(
                a + b
                for a, b in zip(alpha, beta, strict=True)
            )

            if summed not in root_set:
                continue

            simple_checks += 1

            assert canonical_structure_constant(
                alpha,
                beta,
                roots=roots,
                expansions=expansions,
                epsilon=epsilon,
            ) == epsilon[simple_index]

    assert simple_checks == 448

    assert all(
        opposite_pairing_invariance_holds(root)
        for root in roots
    )

    for root in roots:
        for simple_index in range(8):
            assert (
                normalized_cartan_pairing_with_coroot(
                    simple_index,
                    root,
                )
                ==
                cartan_root_value(
                    simple_index,
                    root,
                )
            )

    assert set(
        normalized_opposite_root_pairing(root)
        for root in roots
    ) == {-1, 1}


def test_opposite_root_pairing_is_derived_from_bracket_and_invariance() -> None:
    from e8_ternary.canonical_basis import opposite_root_bracket_sign

    roots, _, _ = phase3c_data()

    for root in roots:
        pairing = normalized_opposite_root_pairing(root)
        bracket_sign = opposite_root_bracket_sign(root)

        # This equality is now an output of the invariance derivation,
        # not the definition of normalized_opposite_root_pairing().
        assert pairing == bracket_sign

        nonzero_cartan_directions = [
            simple_index
            for simple_index in range(8)
            if cartan_root_value(simple_index, root) != 0
        ]

        assert nonzero_cartan_directions

        for simple_index in nonzero_cartan_directions:
            assert (
                bracket_sign
                * normalized_cartan_pairing_with_coroot(
                    simple_index,
                    root,
                )
                ==
                cartan_root_value(simple_index, root)
                * pairing
            )
