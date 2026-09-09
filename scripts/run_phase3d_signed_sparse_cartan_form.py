#!/usr/bin/env python3
"""Execute Phase 3D signed sparse E8 Cartan 3-form construction."""

from __future__ import annotations

import hashlib

from e8_ternary.incidence import (
    build_ternary_incidence,
)
from e8_ternary.roots import generate_e8_roots
from e8_ternary.sparse_cartan_form import (
    TOTAL_ORDERED_DOMAIN,
    SparseSector,
    all_indices_distinct,
    build_alternating_reconstruction,
    build_direct_sparse_cartan_form,
    coefficient_spectrum,
    export_sparse_cartan_form,
    full_alternation_holds,
    hrr_entries_use_opposite_roots,
    load_sparse_cartan_form,
    no_hhr_or_hhh_entries,
    rrr_cyclic_formula_consistency,
    rrr_root_index_support,
    sector_counts,
    sparse_form_discrepancies,
)
from e8_ternary.ternary import (
    enumerate_zero_sum_triples,
)


OUTPUT = (
    "data/derived/"
    "phase3d_signed_sparse_cartan_form.json"
)


def main() -> None:
    print(
        "Phase 3D E8 signed sparse Cartan 3-form"
    )
    print()

    roots = generate_e8_roots()

    print("Frozen basis")
    print("  Cartan basis vectors: 8")
    print("  root basis vectors:", len(roots))
    print("  total basis dimension:", 8 + len(roots))
    print(
        "  complete ordered basis^3 domain:",
        TOTAL_ORDERED_DOMAIN,
    )
    print()

    # ---------------------------------------------------------------
    # Primary construction.
    # ---------------------------------------------------------------
    direct = build_direct_sparse_cartan_form(
        roots
    )

    counts = sector_counts(direct)
    spectrum = coefficient_spectrum(
        direct
    )

    print("Primary direct construction")
    print(
        "  RRR entries:",
        counts.get(
            SparseSector.RRR,
            0,
        ),
    )
    print(
        "  HRR entries:",
        counts.get(
            SparseSector.HRR,
            0,
        ),
    )
    print(
        "  total nonzero entries:",
        direct.nonzero_count,
    )
    print(
        "  support density:",
        f"{direct.support_density:.15f}",
    )
    print()

    print("Full coefficient spectrum")
    for value, count in spectrum.items():
        print(
            f"  {value:+d}: {count}"
        )
    print()

    distinct = all_indices_distinct(
        direct
    )
    alternating = full_alternation_holds(
        direct
    )
    cyclic = rrr_cyclic_formula_consistency(
        roots
    )

    print("Intrinsic tensor checks")
    print(
        "  all stored indices distinct:",
        distinct,
    )
    print(
        "  full S3 alternation:",
        alternating,
    )
    print(
        "  RRR cyclic formula consistency:",
        cyclic,
    )
    print()

    # ---------------------------------------------------------------
    # Secondary alternating reconstruction.
    # ---------------------------------------------------------------
    reconstructed = (
        build_alternating_reconstruction(
            roots
        )
    )

    (
        direct_only,
        reconstructed_only,
        differing,
    ) = sparse_form_discrepancies(
        direct,
        reconstructed,
    )

    print("Independent alternating reconstruction")
    print(
        "  reconstructed entries:",
        reconstructed.nonzero_count,
    )
    print(
        "  direct-only keys:",
        len(direct_only),
    )
    print(
        "  reconstruction-only keys:",
        len(reconstructed_only),
    )
    print(
        "  shared keys with differing coefficients:",
        len(differing),
    )
    print(
        "  exact coefficient-map equality:",
        (
            not direct_only
            and not reconstructed_only
            and not differing
        ),
    )
    print()

    # ---------------------------------------------------------------
    # Compare RRR unsigned support with frozen Phase 2C.
    # ---------------------------------------------------------------
    phase3d_rrr = rrr_root_index_support(
        direct
    )

    triples = enumerate_zero_sum_triples(
        roots
    ).triples

    phase2c = set(
        build_ternary_incidence(
            len(roots),
            triples,
        ).ordered_support
    )

    phase3d_only = (
        phase3d_rrr - phase2c
    )
    phase2c_only = (
        phase2c - phase3d_rrr
    )

    print("Phase 2C root-support comparison")
    print(
        "  Phase 3D RRR support:",
        len(phase3d_rrr),
    )
    print(
        "  Phase 2C Boolean support:",
        len(phase2c),
    )
    print(
        "  Phase3D-only entries:",
        len(phase3d_only),
    )
    print(
        "  Phase2C-only entries:",
        len(phase2c_only),
    )
    print(
        "  exact support equality:",
        not phase3d_only
        and not phase2c_only,
    )
    print()

    architecture = (
        no_hhr_or_hhh_entries(
            direct
        )
        and hrr_entries_use_opposite_roots(
            direct,
            roots,
        )
    )

    print("Phase 3B architecture refinement")
    print(
        "  no HHR/HHH nonzero entries:",
        no_hhr_or_hhh_entries(
            direct
        ),
    )
    print(
        "  every HRR entry uses opposite roots:",
        hrr_entries_use_opposite_roots(
            direct,
            roots,
        ),
    )
    print()

    output = export_sparse_cartan_form(
        OUTPUT,
        direct,
        roots,
    )

    loaded = load_sparse_cartan_form(
        output
    )

    round_trip = (
        loaded == direct
    )

    digest = hashlib.sha256(
        output.read_bytes()
    ).hexdigest()

    print("Deterministic sparse export")
    print("  JSON:", output)
    print("  SHA256:", digest)
    print(
        "  round-trip exact:",
        round_trip,
    )
    print()

    expected_spectrum = {
        -2: 24,
        -1: 8064,
        1: 8064,
        2: 24,
    }

    success = (
        counts
        == {
            SparseSector.HRR: 2736,
            SparseSector.RRR: 13440,
        }
        and direct.nonzero_count == 16176
        and spectrum
        == expected_spectrum
        and distinct
        and alternating
        and cyclic
        and reconstructed.nonzero_count
        == 16176
        and not direct_only
        and not reconstructed_only
        and not differing
        and not phase3d_only
        and not phase2c_only
        and architecture
        and round_trip
    )

    print(
        "PHASE3D_SIGNED_SPARSE_CARTAN_FORM:",
        "PASS" if success else "FAIL",
    )

    if not success:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
