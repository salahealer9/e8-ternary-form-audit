#!/usr/bin/env python3
"""Execute Phase 3A root-space Cartan 3-form support analysis."""

from e8_ternary.cartan_support import (
    SupportClass,
    build_root_space_cartan_support,
    classification_census,
    support_has_distinct_indices,
    support_is_s3_symmetric,
)
from e8_ternary.roots import generate_e8_roots


def main() -> None:
    print("Phase 3A E8 root-space Cartan 3-form support")
    print()

    roots = generate_e8_roots()

    # Construct Lie-algebraic root-space support independently.
    cartan_support = build_root_space_cartan_support(roots)
    lie_support = set(cartan_support.ordered_support)

    print("Lie-algebraic root-space support")
    print("  roots:", len(roots))
    print(
        "  complete ordered root^3 domain:",
        cartan_support.total_ordered_triples,
    )
    print(
        "  nonzero root-root-root support:",
        len(cartan_support.ordered_support),
    )
    print(
        "  forced-zero positions:",
        cartan_support.forced_zero_count,
    )
    print(
        "  support density:",
        f"{len(lie_support) / cartan_support.total_ordered_triples:.12f}",
    )
    print()

    census = classification_census(roots)

    print("Lie-rule classification census")
    for support_class in SupportClass:
        print(
            f"  {support_class.value}:",
            census[support_class],
        )
    print(
        "  census total:",
        sum(census.values()),
    )
    print()

    symmetric = support_is_s3_symmetric(
        cartan_support.ordered_support
    )
    distinct = support_has_distinct_indices(
        cartan_support.ordered_support
    )

    print("Root-space support structure")
    print("  S3-symmetric support positions:", symmetric)
    print("  all support indices distinct:", distinct)
    print()

    # Phase 2C is introduced only after S_Omega has been constructed.
    from e8_ternary.incidence import build_ternary_incidence
    from e8_ternary.ternary import enumerate_zero_sum_triples

    zero_sum_triples = enumerate_zero_sum_triples(
        roots
    ).triples

    incidence = build_ternary_incidence(
        len(roots),
        zero_sum_triples,
    )

    boolean_support = set(
        incidence.ordered_support
    )

    lie_only = lie_support - boolean_support
    boolean_only = boolean_support - lie_support

    print("Comparison with Phase 2C Boolean support")
    print("  Lie-derived support:", len(lie_support))
    print("  Phase 2C support:", len(boolean_support))
    print("  Lie-only entries:", len(lie_only))
    print("  Phase2C-only entries:", len(boolean_only))
    print(
        "  exact support equality:",
        not lie_only and not boolean_only,
    )
    print()

    success = (
        len(cartan_support.ordered_support) == 13440
        and sum(census.values()) == len(roots) ** 3
        and census[
            SupportClass.ROOT_SUPPORT_NONZERO
        ] == len(cartan_support.ordered_support)
        and symmetric
        and distinct
        and not lie_only
        and not boolean_only
    )

    print(
        "PHASE3A_ROOT_SPACE_CARTAN_SUPPORT:",
        "PASS" if success else "FAIL",
    )

    if not success:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
