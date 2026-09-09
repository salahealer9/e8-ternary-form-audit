"""Phase 6B literal notation realization tests."""

from fractions import Fraction
from itertools import permutations

import pytest

from e8_ternary.canonical_basis import (
    SIMPLE_ROOTS,
    cartan_root_value,
    normalized_opposite_root_pairing,
)
from e8_ternary.full_sector import opposite_index_map
from e8_ternary.literal_g import (
    PHASE3D_JSON,
    PHASE3D_SHA256,
    B0,
    add,
    basis_vector,
    bracket,
    cartan_vector,
    complete_bracket_recovery_discrepancies,
    frozen_roots,
    g,
    g_from_algebra,
    g_from_tensor,
    root_vector,
    scale,
    vector,
)
from e8_ternary.lie_algebra_audit import (
    BASIS_DIMENSION,
    sha256_file,
)
from e8_ternary.sparse_cartan_form import (
    load_sparse_cartan_form,
)
from e8_ternary.ternary import enumerate_zero_sum_triples


def test_phase6b_sealed_tensor_hash() -> None:
    assert sha256_file(
        PHASE3D_JSON
    ) == PHASE3D_SHA256


def test_vector_canonicalization() -> None:
    assert vector(
        [
            (8, 1),
            (3, Fraction(1, 2)),
            (8, -1),
            (3, Fraction(3, 2)),
            (10, 0),
        ]
    ) == (
        (
            3,
            Fraction(2),
        ),
    )

    with pytest.raises(ValueError):
        vector(
            {
                BASIS_DIMENSION: 1,
            }
        )


def test_basis_constructors() -> None:
    assert basis_vector(0) == (
        (
            0,
            Fraction(1),
        ),
    )

    assert cartan_vector(7) == basis_vector(
        7
    )

    assert root_vector(0) == basis_vector(
        8
    )


def test_admissible_root_triple() -> None:
    roots = frozen_roots()

    alpha, beta, gamma = (
        enumerate_zero_sum_triples(
            roots
        ).triples[0]
    )

    value = g(
        root_vector(alpha),
        root_vector(beta),
        root_vector(gamma),
    )

    assert value in (
        Fraction(-1),
        Fraction(1),
    )

    assert value == g_from_algebra(
        root_vector(alpha),
        root_vector(beta),
        root_vector(gamma),
    )


def test_nonadmissible_root_triple() -> None:
    roots = frozen_roots()
    zero_sum = set(
        enumerate_zero_sum_triples(
            roots
        ).triples
    )

    candidate = next(
        (
            first,
            second,
            third,
        )
        for first in range(len(roots))
        for second in range(first + 1, len(roots))
        for third in range(second + 1, len(roots))
        if (
            first,
            second,
            third,
        ) not in zero_sum
    )

    assert g(
        root_vector(candidate[0]),
        root_vector(candidate[1]),
        root_vector(candidate[2]),
    ) == 0


def test_cartan_opposite_root_formula() -> None:
    roots = frozen_roots()
    root_lookup = {
        root: index
        for index, root in enumerate(roots)
    }

    alpha_index = root_lookup[
        SIMPLE_ROOTS[0]
    ]

    opposite = opposite_index_map(
        roots
    )

    negative_index = opposite[
        alpha_index
    ]

    expected = (
        normalized_opposite_root_pairing(
            roots[alpha_index]
        )
        * cartan_root_value(
            0,
            roots[alpha_index],
        )
    )

    observed = g(
        cartan_vector(0),
        root_vector(alpha_index),
        root_vector(negative_index),
    )

    assert observed == expected
    assert abs(observed) == 2


def test_complete_basis_value_set() -> None:
    form = load_sparse_cartan_form(
        PHASE3D_JSON
    )

    assert {
        0,
        *(
            entry.coefficient
            for entry in form.entries
        ),
    } == {
        -2,
        -1,
        0,
        1,
        2,
    }


def test_tensor_basis_entries_are_exact() -> None:
    form = load_sparse_cartan_form(
        PHASE3D_JSON
    )

    for entry in form.entries:
        assert g_from_tensor(
            basis_vector(entry.first),
            basis_vector(entry.second),
            basis_vector(entry.third),
        ) == entry.coefficient


def test_arbitrary_vector_tensor_algebra_agreement() -> None:
    roots = frozen_roots()

    alpha, beta, gamma = (
        enumerate_zero_sum_triples(
            roots
        ).triples[0]
    )

    v1 = add(
        cartan_vector(0),
        scale(
            Fraction(3, 2),
            root_vector(alpha),
        ),
    )

    v2 = add(
        scale(
            -2,
            cartan_vector(1),
        ),
        root_vector(beta),
    )

    v3 = add(
        root_vector(gamma),
        scale(
            Fraction(5, 3),
            cartan_vector(2),
        ),
    )

    assert g_from_tensor(
        v1,
        v2,
        v3,
    ) == g_from_algebra(
        v1,
        v2,
        v3,
    )


def test_first_slot_linearity() -> None:
    roots = frozen_roots()
    alpha, beta, gamma = (
        enumerate_zero_sum_triples(
            roots
        ).triples[0]
    )

    u = cartan_vector(0)
    v = root_vector(alpha)
    x = root_vector(beta)
    y = root_vector(gamma)

    a = Fraction(2, 3)
    b = Fraction(-5, 4)

    assert g(
        add(
            scale(a, u),
            scale(b, v),
        ),
        x,
        y,
    ) == (
        a * g(u, x, y)
        + b * g(v, x, y)
    )


def test_second_slot_linearity() -> None:
    roots = frozen_roots()
    alpha, beta, gamma = (
        enumerate_zero_sum_triples(
            roots
        ).triples[0]
    )

    x = root_vector(alpha)
    u = cartan_vector(0)
    v = root_vector(beta)
    y = root_vector(gamma)

    a = Fraction(-3, 5)
    b = Fraction(7, 2)

    assert g(
        x,
        add(
            scale(a, u),
            scale(b, v),
        ),
        y,
    ) == (
        a * g(x, u, y)
        + b * g(x, v, y)
    )


def test_third_slot_linearity() -> None:
    roots = frozen_roots()
    alpha, beta, gamma = (
        enumerate_zero_sum_triples(
            roots
        ).triples[0]
    )

    x = root_vector(alpha)
    y = root_vector(beta)
    u = cartan_vector(0)
    v = root_vector(gamma)

    a = Fraction(4, 7)
    b = Fraction(-9, 5)

    assert g(
        x,
        y,
        add(
            scale(a, u),
            scale(b, v),
        ),
    ) == (
        a * g(x, y, u)
        + b * g(x, y, v)
    )


def test_full_alternation_on_arbitrary_vectors() -> None:
    roots = frozen_roots()
    alpha, beta, gamma = (
        enumerate_zero_sum_triples(
            roots
        ).triples[0]
    )

    values = (
        add(
            cartan_vector(0),
            root_vector(alpha),
        ),
        add(
            cartan_vector(1),
            root_vector(beta),
        ),
        add(
            cartan_vector(2),
            root_vector(gamma),
        ),
    )

    base = g(
        values[0],
        values[1],
        values[2],
    )

    for permutation in permutations(
        range(3)
    ):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(3)
            for j in range(i + 1, 3)
        )

        sign = (
            -1
            if inversions % 2
            else 1
        )

        assert g(
            values[permutation[0]],
            values[permutation[1]],
            values[permutation[2]],
        ) == sign * base


def test_repeated_argument_vanishing() -> None:
    v = add(
        cartan_vector(0),
        root_vector(0),
        scale(
            Fraction(3, 2),
            root_vector(1),
        ),
    )

    w = add(
        cartan_vector(2),
        root_vector(5),
    )

    assert g(v, v, w) == 0
    assert g(v, w, v) == 0
    assert g(w, v, v) == 0


def test_direct_definition_B0_bracket() -> None:
    roots = frozen_roots()
    alpha, beta, gamma = (
        enumerate_zero_sum_triples(
            roots
        ).triples[0]
    )

    v1 = root_vector(alpha)
    v2 = root_vector(beta)
    v3 = root_vector(gamma)

    assert g_from_algebra(
        v1,
        v2,
        v3,
    ) == B0(
        v1,
        bracket(
            v2,
            v3,
        ),
    )


def test_complete_bracket_recovery() -> None:
    (
        recovered_only,
        frozen_only,
        differing,
    ) = complete_bracket_recovery_discrepancies()

    assert recovered_only == set()
    assert frozen_only == set()
    assert differing == {}
