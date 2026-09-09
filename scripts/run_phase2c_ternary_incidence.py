#!/usr/bin/env python3
"""Execute Phase 2C unsigned E8 ternary incidence construction."""

from e8_ternary.a2 import group_by_six_root_subsystem
from e8_ternary.incidence import (
    active_pair_count,
    active_pair_doubled_dot_spectrum,
    build_ternary_incidence,
    negation_index_map,
    negation_orbit_six_root_keys,
    negation_orbit_size_spectrum,
    negation_orbits,
    ordered_support_has_zero_diagonals,
    ordered_support_is_s3_symmetric,
    ordered_support_is_unique,
    pair_codegree_spectrum,
    vertex_degree_spectrum,
)
from e8_ternary.roots import generate_e8_roots
from e8_ternary.ternary import enumerate_zero_sum_triples


def main() -> None:
    print("Phase 2C E8 ternary incidence")
    print()

    roots = generate_e8_roots()
    triples = enumerate_zero_sum_triples(roots).triples

    incidence = build_ternary_incidence(
        len(roots),
        triples,
    )

    print("Unsigned hypergraph H")
    print("  vertices:", incidence.vertex_count)
    print("  unordered hyperedges:", len(incidence.hyperedges))
    print()

    print("Symmetric Boolean support T_ijk")
    print("  ordered support entries:", len(incidence.ordered_support))
    print(
        "  support density:",
        f"{len(incidence.ordered_support) / incidence.vertex_count**3:.12f}",
    )
    print("  unique sparse entries:", ordered_support_is_unique(incidence))
    print(
        "  full S3 symmetry:",
        ordered_support_is_s3_symmetric(incidence),
    )
    print(
        "  repeated-index support absent:",
        ordered_support_has_zero_diagonals(incidence),
    )
    print()

    degrees = vertex_degree_spectrum(incidence)

    print("Vertex-degree spectrum")
    for degree, count in degrees.items():
        print(f"  degree {degree}: {count} vertices")
    print()

    codegrees = pair_codegree_spectrum(incidence)

    print("Pair-codegree spectrum")
    for codegree, count in codegrees.items():
        print(f"  codegree {codegree}: {count} unordered pairs")
    print("  active unordered pairs:", active_pair_count(incidence))
    print()

    active_dots = active_pair_doubled_dot_spectrum(
        roots,
        incidence,
    )

    print("Post-construction active-pair doubled-dot spectrum")
    for dot, count in active_dots.items():
        print(f"  {dot}: {count} active unordered pairs")
    print()

    negation_map = negation_index_map(roots)
    orbits = negation_orbits(incidence, negation_map)
    orbit_sizes = negation_orbit_size_spectrum(
        incidence,
        negation_map,
    )

    print("Global-negation action")
    print("  hyperedge negation orbits:", len(orbits))
    print("  orbit-size spectrum:")
    for size, count in orbit_sizes.items():
        print(f"    size {size}: {count} orbits")
    print()

    orbit_keys = set(
        negation_orbit_six_root_keys(
            incidence,
            negation_map,
        )
    )

    a2_groups = group_by_six_root_subsystem(
        roots,
        triples,
    )

    a2_agreement = orbit_keys == set(a2_groups)

    print("Phase 2B quotient comparison")
    print("  negation-orbit six-root sets:", len(orbit_keys))
    print("  Phase 2B A2 classes:", len(a2_groups))
    print("  exact agreement:", a2_agreement)
    print()

    success = (
        incidence.vertex_count == 240
        and len(incidence.hyperedges) == 2240
        and len(incidence.ordered_support) == 13440
        and ordered_support_is_unique(incidence)
        and ordered_support_is_s3_symmetric(incidence)
        and ordered_support_has_zero_diagonals(incidence)
        and degrees == {28: 240}
        and codegrees == {0: 21960, 1: 6720}
        and active_pair_count(incidence) == 6720
        and active_dots == {-4: 6720}
        and orbit_sizes == {2: 1120}
        and len(orbits) == 1120
        and a2_agreement
    )

    print(
        "PHASE2C_TERNARY_INCIDENCE:",
        "PASS" if success else "FAIL",
    )

    if not success:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
