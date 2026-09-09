#!/usr/bin/env python3
"""Execute Phase 3C canonical E8 basis and normalization validation."""

from collections import Counter

from e8_ternary.canonical_basis import (
    SIMPLE_ROOTS,
    RootSign,
    canonical_structure_constant,
    classify_root_sign,
    derive_epsilon,
    dynkin_edges,
    normalized_opposite_root_pairing,
    opposite_pairing_invariance_holds,
    root_expansion_map,
    root_height,
    simple_root_gram_matrix,
    structure_constant_sign_spectrum,
    structure_constant_table,
)
from e8_ternary.roots import generate_e8_roots
from e8_ternary.validation import exact_rank


def main() -> None:
    print("Phase 3C E8 canonical basis and normalization")
    print()

    roots = generate_e8_roots()
    root_set = set(roots)

    print("Frozen simple-root system")
    print(
        "  simple roots present in validated E8 set:",
        all(root in root_set for root in SIMPLE_ROOTS),
    )
    print("  exact simple-root rank:", exact_rank(SIMPLE_ROOTS))
    print()

    gram = simple_root_gram_matrix()

    print("Simple-root Gram / Cartan matrix")
    for row in gram:
        print(" ", row)
    print()

    edges = dynkin_edges()

    print("Derived Dynkin edges (1-based)")
    for left, right in edges:
        print(f"  {left + 1}-{right + 1}")
    print()

    expansions = root_expansion_map(roots)

    signs = Counter(
        classify_root_sign(expansions[root])
        for root in roots
    )

    heights = [
        root_height(expansions[root])
        for root in roots
    ]

    print("Root expansions")
    print("  exact integral expansions:", len(expansions))
    print(
        "  positive roots:",
        signs[RootSign.POSITIVE],
    )
    print(
        "  negative roots:",
        signs[RootSign.NEGATIVE],
    )
    print("  minimum height:", min(heights))
    print("  maximum height:", max(heights))
    print()

    epsilon = derive_epsilon()

    print("Frozen epsilon")
    print(" ", epsilon)
    print(
        "  alternates across every Dynkin edge:",
        all(
            epsilon[left] == -epsilon[right]
            for left, right in edges
        ),
    )
    print()

    table = structure_constant_table(roots)
    sign_spectrum = structure_constant_sign_spectrum(roots)

    print("Canonical root-root structure constants")
    print("  admissible ordered root pairs:", len(table))
    print("  sign spectrum:")
    for sign, count in sign_spectrum.items():
        print(f"    {sign:+d}: {count}")
    print()

    lookup = {
        (entry.alpha_index, entry.beta_index):
        entry.coefficient
        for entry in table
    }

    antisymmetry = all(
        lookup[(entry.beta_index, entry.alpha_index)]
        == -entry.coefficient
        for entry in table
    )

    root_index = {
        root: index
        for index, root in enumerate(roots)
    }

    simultaneous_negation = True

    for entry in table:
        alpha = roots[entry.alpha_index]
        beta = roots[entry.beta_index]

        negative_alpha = tuple(-value for value in alpha)
        negative_beta = tuple(-value for value in beta)

        negative_key = (
            root_index[negative_alpha],
            root_index[negative_beta],
        )

        if lookup[negative_key] != -entry.coefficient:
            simultaneous_negation = False
            break

    print("Global sign identities")
    print("  antisymmetry:", antisymmetry)
    print(
        "  simultaneous-root-negation identity:",
        simultaneous_negation,
    )
    print()

    simple_checks = 0
    simple_match = True

    for simple_index, alpha in enumerate(SIMPLE_ROOTS):
        for beta in roots:
            summed = tuple(
                a + b
                for a, b in zip(alpha, beta, strict=True)
            )

            if summed not in root_set:
                continue

            simple_checks += 1

            coefficient = canonical_structure_constant(
                alpha,
                beta,
                roots=roots,
                expansions=expansions,
                epsilon=epsilon,
            )

            if coefficient != epsilon[simple_index]:
                simple_match = False

    print("Simple-root canonical checks")
    print("  admissible checks:", simple_checks)
    print("  all agree with epsilon:", simple_match)
    print()

    opposite_pairings = Counter(
        normalized_opposite_root_pairing(root)
        for root in roots
    )

    invariance = all(
        opposite_pairing_invariance_holds(root)
        for root in roots
    )

    print("Normalized B0 opposite-root pairing")
    print("  pairing spectrum:")
    for value, count in sorted(opposite_pairings.items()):
        print(f"    {value:+d}: {count} roots")
    print("  invariance checks:", invariance)
    print()

    success = (
        all(root in root_set for root in SIMPLE_ROOTS)
        and exact_rank(SIMPLE_ROOTS) == 8
        and len(expansions) == 240
        and signs
        == {
            RootSign.POSITIVE: 120,
            RootSign.NEGATIVE: 120,
        }
        and min(heights) == -29
        and max(heights) == 29
        and epsilon == (
            1,
            -1,
            1,
            -1,
            1,
            -1,
            1,
            -1,
        )
        and len(table) == 13440
        and sign_spectrum == {
            -1: 6720,
            1: 6720,
        }
        and antisymmetry
        and simultaneous_negation
        and simple_checks == 448
        and simple_match
        and invariance
    )

    print(
        "PHASE3C_CANONICAL_BASIS_NORMALIZATION:",
        "PASS" if success else "FAIL",
    )

    if not success:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
