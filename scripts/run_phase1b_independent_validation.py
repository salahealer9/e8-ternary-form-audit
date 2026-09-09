#!/usr/bin/env python3
"""Execute Phase 1B independent E8 validation."""

from e8_ternary.validation import (
    crystallographic_integrality,
    exact_rank,
    generate_lattice_roots,
    nonorthogonality_graph_connected,
    reflection_closure,
    set_differences,
)


def main() -> None:
    print("Phase 1B independent E8 validation")
    print()

    # IMPORTANT:
    # Complete the independent construction before obtaining Phase 1A roots.
    lattice_roots = generate_lattice_roots()

    print("Independent lattice enumeration complete")
    print("Lattice-derived roots:", len(lattice_roots))
    print()

    # Import only after independent enumeration has completed.
    from e8_ternary.roots import generate_e8_roots

    phase1a_roots = generate_e8_roots()

    lattice_only, phase1a_only = set_differences(
        lattice_roots,
        phase1a_roots,
    )

    rank = exact_rank(lattice_roots)
    crystallographic = crystallographic_integrality(lattice_roots)
    reflection = reflection_closure(lattice_roots)
    connected = nonorthogonality_graph_connected(lattice_roots)

    print("Exact set comparison")
    print("  Phase 1A roots:", len(phase1a_roots))
    print("  lattice-only roots:", len(lattice_only))
    print("  Phase1A-only roots:", len(phase1a_only))
    print("  exact set equality:", not lattice_only and not phase1a_only)
    print()

    print("Structural validation")
    print("  exact rank:", rank)
    print("  crystallographic integrality:", crystallographic)
    print("  reflection closure:", reflection)
    print("  nonorthogonality graph connected:", connected)
    print()

    success = (
        len(lattice_roots) == 240
        and not lattice_only
        and not phase1a_only
        and rank == 8
        and crystallographic
        and reflection
        and connected
    )

    print(
        "PHASE1B_INDEPENDENT_VALIDATION:",
        "PASS" if success else "FAIL",
    )

    if not success:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
