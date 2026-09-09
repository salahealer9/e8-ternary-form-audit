#!/usr/bin/env python3
"""Execute Phase 6B literal g(v1,v2,v3) realization."""

from fractions import Fraction

from e8_ternary.canonical_basis import (
    SIMPLE_ROOTS,
    cartan_root_value,
    normalized_opposite_root_pairing,
)
from e8_ternary.full_sector import opposite_index_map
from e8_ternary.literal_g import (
    PHASE3D_JSON,
    PHASE3D_SHA256,
    add,
    cartan_vector,
    complete_bracket_recovery_discrepancies,
    frozen_roots,
    g,
    g_from_algebra,
    g_from_tensor,
    root_vector,
    scale,
)
from e8_ternary.lie_algebra_audit import (
    BASIS_DIMENSION,
    sha256_file,
)
from e8_ternary.sparse_cartan_form import (
    load_sparse_cartan_form,
)
from e8_ternary.ternary import (
    enumerate_zero_sum_triples,
)


def main() -> None:
    print(
        "Phase 6B literal notation realization"
    )
    print()

    print("Frozen definition")
    print(
        "  g(v1,v2,v3) := B0(v1,[v2,v3])"
    )
    print(
        "  domain: e8 x e8 x e8"
    )
    print(
        "  codomain: R"
    )
    print(
        "  exact computational codomain: Q"
    )
    print()

    observed_hash = sha256_file(
        PHASE3D_JSON
    )

    integrity = (
        observed_hash
        == PHASE3D_SHA256
    )

    print("Sealed Phase 3D tensor")
    print(
        "  SHA256:",
        observed_hash,
    )
    print(
        "  hash unchanged:",
        integrity,
    )
    print()

    roots = frozen_roots()
    triples = enumerate_zero_sum_triples(
        roots
    ).triples

    # ---------------------------------------------------------------
    # Case 1: admissible root triple.
    # ---------------------------------------------------------------
    alpha, beta, gamma = triples[0]

    admissible = g(
        root_vector(alpha),
        root_vector(beta),
        root_vector(gamma),
    )

    print("Case 1 — admissible root triple")
    print(
        "  root indices:",
        alpha,
        beta,
        gamma,
    )
    print(
        "  alpha+beta+gamma=0: True"
    )
    print(
        "  g:",
        admissible,
    )
    print()

    # ---------------------------------------------------------------
    # Case 2: non-admissible root triple.
    # ---------------------------------------------------------------
    triple_set = set(triples)

    nonadmissible_indices = next(
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
        ) not in triple_set
    )

    nonadmissible = g(
        root_vector(
            nonadmissible_indices[0]
        ),
        root_vector(
            nonadmissible_indices[1]
        ),
        root_vector(
            nonadmissible_indices[2]
        ),
    )

    print("Case 2 — non-admissible root triple")
    print(
        "  root indices:",
        *nonadmissible_indices,
    )
    print(
        "  zero-sum triple: False"
    )
    print(
        "  g:",
        nonadmissible,
    )
    print()

    # ---------------------------------------------------------------
    # Case 3: Cartan / opposite-root triple.
    # ---------------------------------------------------------------
    root_lookup = {
        root: index
        for index, root in enumerate(roots)
    }

    simple_root_index = root_lookup[
        SIMPLE_ROOTS[0]
    ]

    opposite = opposite_index_map(
        roots
    )

    negative_index = opposite[
        simple_root_index
    ]

    cartan_expected = (
        normalized_opposite_root_pairing(
            roots[simple_root_index]
        )
        * cartan_root_value(
            0,
            roots[simple_root_index],
        )
    )

    cartan_value = g(
        cartan_vector(0),
        root_vector(
            simple_root_index
        ),
        root_vector(
            negative_index
        ),
    )

    print(
        "Case 3 — Cartan/opposite-root triple"
    )
    print(
        "  simple Cartan index: 0"
    )
    print(
        "  root index:",
        simple_root_index,
    )
    print(
        "  opposite root index:",
        negative_index,
    )
    print(
        "  expected:",
        cartan_expected,
    )
    print(
        "  g:",
        cartan_value,
    )
    print()

    # ---------------------------------------------------------------
    # Case 4: arbitrary exact sparse vectors.
    # ---------------------------------------------------------------
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

    tensor_value = g_from_tensor(
        v1,
        v2,
        v3,
    )

    algebra_value = g_from_algebra(
        v1,
        v2,
        v3,
    )

    print(
        "Case 4 — arbitrary exact sparse vectors"
    )
    print(
        "  tensor route:",
        tensor_value,
    )
    print(
        "  algebra route:",
        algebra_value,
    )
    print(
        "  exact agreement:",
        tensor_value == algebra_value,
    )
    print()

    # ---------------------------------------------------------------
    # Tensor census.
    # ---------------------------------------------------------------
    form = load_sparse_cartan_form(
        PHASE3D_JSON
    )

    value_set = {
        0,
        *(
            entry.coefficient
            for entry in form.entries
        ),
    }

    print("Literal basis tensor")
    print(
        "  basis dimension:",
        BASIS_DIMENSION,
    )
    print(
        "  nonzero g_ijk:",
        len(form.entries),
    )
    print(
        "  complete basis value set:",
        sorted(value_set),
    )
    print()

    # ---------------------------------------------------------------
    # Recover full Lie bracket from g and B0^-1.
    # ---------------------------------------------------------------
    (
        recovered_only,
        frozen_only,
        differing,
    ) = complete_bracket_recovery_discrepancies()

    print("Bracket recovery from g and B0^-1")
    print(
        "  ordered basis pairs checked:",
        BASIS_DIMENSION**2,
    )
    print(
        "  recovered-only nonzero pairs:",
        len(recovered_only),
    )
    print(
        "  frozen-bracket-only nonzero pairs:",
        len(frozen_only),
    )
    print(
        "  coefficient/vector mismatches:",
        len(differing),
    )

    bracket_recovery = (
        not recovered_only
        and not frozen_only
        and not differing
    )

    print(
        "  exact bracket recovery:",
        bracket_recovery,
    )
    print()

    success = (
        integrity
        and admissible in (-1, 1)
        and nonadmissible == 0
        and cartan_value
        == cartan_expected
        and tensor_value
        == algebra_value
        and len(form.entries)
        == 16176
        and value_set
        == {
            -2,
            -1,
            0,
            1,
            2,
        }
        and bracket_recovery
    )

    print(
        "Literal realization:"
    )
    print(
        "  g(v1,v2,v3) "
        "= normalized E8 Cartan 3-form"
    )
    print()

    print(
        "PHASE6B_LITERAL_NOTATION_REALIZATION:",
        "PASS" if success else "FAIL",
    )

    if not success:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
