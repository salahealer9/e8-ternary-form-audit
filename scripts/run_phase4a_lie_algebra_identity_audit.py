#!/usr/bin/env python3
"""Execute Phase 4A exhaustive E8 Lie-algebra identity audit."""

from pathlib import Path

from e8_ternary.canonical_basis import (
    simple_root_gram_matrix,
)
from e8_ternary.lie_algebra_audit import (
    BASIS_DIMENSION,
    CANONICAL_JACOBI_DOMAIN,
    ORDERED_PAIR_DOMAIN,
    bilinear_support_count,
    bilinear_symmetry_holds,
    bilinear_value_spectrum,
    bracket_antisymmetry_holds,
    bracket_closure_holds,
    build_basis_bracket_table,
    build_bilinear_table,
    build_invariance_maps,
    exact_integer_determinant,
    exhaustive_jacobi_audit,
    nonzero_bracket_pairs,
    scalar_map_discrepancies,
    scalar_map_spectrum,
    self_brackets_zero,
    sha256_file,
    structural_nondegeneracy_holds,
)
from e8_ternary.roots import generate_e8_roots
from e8_ternary.sparse_cartan_form import (
    load_sparse_cartan_form,
)


PHASE3D_JSON = Path(
    "data/derived/"
    "phase3d_signed_sparse_cartan_form.json"
)

EXPECTED_PHASE3D_SHA256 = (
    "43b52b4116dfcf0dace332234b5c9dc50"
    "d95d51effb690aec8aebe39ad4f92e8"
)


def main() -> None:
    print(
        "Phase 4A E8 Lie algebra identity audit"
    )
    print()

    roots = generate_e8_roots()

    print("Frozen algebra basis")
    print("  dimension:", BASIS_DIMENSION)
    print(
        "  ordered basis-pair domain:",
        ORDERED_PAIR_DOMAIN,
    )
    print()

    # ---------------------------------------------------------------
    # Independent bracket reconstruction.
    # ---------------------------------------------------------------
    bracket = build_basis_bracket_table(
        roots
    )

    nonzero_pairs = nonzero_bracket_pairs(
        bracket
    )

    antisymmetry = (
        bracket_antisymmetry_holds(
            bracket
        )
    )

    self_zero = self_brackets_zero(
        bracket
    )

    closure = bracket_closure_holds(
        bracket
    )

    print("Frozen bracket reconstruction")
    print(
        "  nonzero ordered bracket pairs:",
        len(nonzero_pairs),
    )
    print(
        "  antisymmetry:",
        antisymmetry,
    )
    print(
        "  all self-brackets zero:",
        self_zero,
    )
    print(
        "  closure on frozen basis:",
        closure,
    )
    print()

    # ---------------------------------------------------------------
    # Exhaustive Jacobi.
    # ---------------------------------------------------------------
    jacobi = exhaustive_jacobi_audit(
        bracket
    )

    print("Exhaustive Jacobi audit")
    print(
        "  canonical distinct triples checked:",
        jacobi.total_checked,
    )

    for sector in (
        "HHH",
        "HHR",
        "HRR",
        "RRR",
    ):
        print(
            f"  {sector}: "
            f"{jacobi.sector_checked[sector]} checked, "
            f"{jacobi.sector_failures[sector]} failures"
        )

    print(
        "  total Jacobi failures:",
        jacobi.total_failures,
    )
    print()

    # ---------------------------------------------------------------
    # Independent B0 reconstruction.
    # ---------------------------------------------------------------
    bilinear = build_bilinear_table(
        roots
    )

    bilinear_support = (
        bilinear_support_count(
            bilinear
        )
    )

    bilinear_spectrum = (
        bilinear_value_spectrum(
            bilinear
        )
    )

    bilinear_symmetry = (
        bilinear_symmetry_holds(
            bilinear
        )
    )

    cartan_determinant = (
        exact_integer_determinant(
            simple_root_gram_matrix()
        )
    )

    nondegenerate = (
        structural_nondegeneracy_holds(
            roots,
            bilinear,
        )
    )

    print("Normalized invariant bilinear form B0")
    print(
        "  nonzero ordered entries:",
        bilinear_support,
    )
    print("  nonzero coefficient spectrum:")
    for value, count in bilinear_spectrum.items():
        print(
            f"    {value:+d}: {count}"
        )

    print(
        "  symmetry:",
        bilinear_symmetry,
    )
    print(
        "  Cartan determinant:",
        cartan_determinant,
    )
    print(
        "  structural nondegeneracy:",
        nondegenerate,
    )
    print()

    # ---------------------------------------------------------------
    # Invariance maps, independently of Phase 3D.
    # ---------------------------------------------------------------
    left_map, right_map = (
        build_invariance_maps(
            bracket,
            bilinear,
        )
    )

    (
        left_only,
        right_only,
        invariance_differing,
    ) = scalar_map_discrepancies(
        left_map,
        right_map,
    )

    print("Invariant-form identity")
    print(
        "  L = B0([X,Y],Z) support:",
        len(left_map),
    )
    print(
        "  R = B0(X,[Y,Z]) support:",
        len(right_map),
    )
    print(
        "  L-only keys:",
        len(left_only),
    )
    print(
        "  R-only keys:",
        len(right_only),
    )
    print(
        "  differing coefficients:",
        len(invariance_differing),
    )
    print(
        "  exact invariance:",
        (
            not left_only
            and not right_only
            and not invariance_differing
        ),
    )
    print()

    algebra_spectrum = scalar_map_spectrum(
        right_map
    )

    print("Algebra-derived trilinear map")
    print(
        "  nonzero entries:",
        len(right_map),
    )
    print("  coefficient spectrum:")
    for value, count in algebra_spectrum.items():
        print(
            f"    {value:+d}: {count}"
        )
    print()

    # ---------------------------------------------------------------
    # Integrity check BEFORE loading/comparing Phase 3D.
    # ---------------------------------------------------------------
    phase3d_hash = sha256_file(
        PHASE3D_JSON
    )

    phase3d_integrity = (
        phase3d_hash
        == EXPECTED_PHASE3D_SHA256
    )

    print("Sealed Phase 3D artifact integrity")
    print(
        "  JSON:",
        PHASE3D_JSON,
    )
    print(
        "  observed SHA256:",
        phase3d_hash,
    )
    print(
        "  expected SHA256:",
        EXPECTED_PHASE3D_SHA256,
    )
    print(
        "  hash unchanged:",
        phase3d_integrity,
    )
    print()

    # Only now load the sealed tensor.
    phase3d = load_sparse_cartan_form(
        PHASE3D_JSON
    )

    phase3d_map = {
        entry.key: entry.coefficient
        for entry in phase3d.entries
    }

    (
        algebra_only,
        phase3d_only,
        phase3d_differing,
    ) = scalar_map_discrepancies(
        right_map,
        phase3d_map,
    )

    print("Phase 4A vs sealed Phase 3D")
    print(
        "  algebra-derived entries:",
        len(right_map),
    )
    print(
        "  Phase 3D entries:",
        len(phase3d_map),
    )
    print(
        "  algebra-only keys:",
        len(algebra_only),
    )
    print(
        "  Phase3D-only keys:",
        len(phase3d_only),
    )
    print(
        "  differing coefficients:",
        len(phase3d_differing),
    )
    print(
        "  exact coefficient-map equality:",
        (
            not algebra_only
            and not phase3d_only
            and not phase3d_differing
        ),
    )
    print()

    expected_jacobi_sectors = {
        "HHH": 56,
        "HHR": 6720,
        "HRR": 229440,
        "RRR": 2275280,
    }

    expected_scalar_spectrum = {
        -2: 24,
        -1: 8064,
        1: 8064,
        2: 24,
    }

    success = (
        BASIS_DIMENSION == 248
        and ORDERED_PAIR_DOMAIN == 61504
        and len(nonzero_pairs) == 15504
        and antisymmetry
        and self_zero
        and closure
        and jacobi.total_checked
        == CANONICAL_JACOBI_DOMAIN
        and jacobi.sector_checked
        == expected_jacobi_sectors
        and jacobi.total_failures == 0
        and bilinear_support == 262
        and bilinear_spectrum
        == {
            -1: 142,
            1: 112,
            2: 8,
        }
        and bilinear_symmetry
        and cartan_determinant == 1
        and nondegenerate
        and len(left_map) == 16176
        and len(right_map) == 16176
        and not left_only
        and not right_only
        and not invariance_differing
        and algebra_spectrum
        == expected_scalar_spectrum
        and phase3d_integrity
        and len(phase3d_map) == 16176
        and not algebra_only
        and not phase3d_only
        and not phase3d_differing
    )

    print(
        "PHASE4A_LIE_ALGEBRA_IDENTITY_AUDIT:",
        "PASS" if success else "FAIL",
    )

    if not success:
        if jacobi.failure_examples:
            print()
            print("First Jacobi failure examples:")
            for example in jacobi.failure_examples:
                print(" ", example)

        raise SystemExit(1)


if __name__ == "__main__":
    main()
