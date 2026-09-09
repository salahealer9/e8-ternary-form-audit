#!/usr/bin/env python3
"""Execute Phase 2A exhaustive zero-sum root-triple enumeration."""

from collections import Counter
from math import comb

from e8_ternary.roots import generate_e8_roots
from e8_ternary.ternary import (
    enumerate_zero_sum_triples,
    ordered_triple_count,
    root_incidence_counts,
    triple_contains_opposite_pair,
    triple_signature_spectrum,
    triples_all_sum_to_zero,
    triples_are_canonical_and_distinct,
    triples_are_unique,
)


def main() -> None:
    print("Phase 2A E8 zero-sum root triples")
    print()

    roots = generate_e8_roots()

    # Primary exhaustive ternary computation.
    result = enumerate_zero_sum_triples(roots)

    triples = result.triples

    print("Primary enumeration")
    print("  roots:", len(roots))
    print("  candidate unordered triples examined:", result.candidate_count)
    print("  retained unordered zero-sum triples:", len(triples))
    print("  implied ordered zero-sum triples:", ordered_triple_count(triples))
    print()

    canonical = triples_are_canonical_and_distinct(triples)
    unique = triples_are_unique(triples)
    exact = triples_all_sum_to_zero(roots, triples)

    print("Ternary integrity")
    print("  canonical distinct triples:", canonical)
    print("  duplicate unordered triples:", len(triples) - len(set(triples)))
    print("  all retained triples sum exactly to zero:", exact)
    print()

    incidences = root_incidence_counts(len(roots), triples)
    incidence_spectrum = dict(sorted(Counter(incidences).items()))

    print("Root incidence spectrum")
    for incidence, root_count in incidence_spectrum.items():
        print(f"  incidence {incidence}: {root_count} roots")
    print("  total root incidences:", sum(incidences))
    print()

    signatures = triple_signature_spectrum(roots, triples)

    print("Post-enumeration doubled-dot signature spectrum")
    for signature, count in signatures.items():
        print(f"  {signature}: {count}")
    print()

    opposite_pair_count = sum(
        1
        for triple in triples
        if triple_contains_opposite_pair(roots, triple)
    )

    print("Degeneracy checks")
    print("  triples containing an opposite pair:", opposite_pair_count)
    print()

    success = (
        result.candidate_count == comb(len(roots), 3)
        and len(triples) == 2240
        and ordered_triple_count(triples) == 13440
        and canonical
        and unique
        and exact
        and incidence_spectrum == {28: 240}
        and signatures == {(-4, -4, -4): 2240}
        and opposite_pair_count == 0
    )

    print(
        "PHASE2A_ZERO_SUM_TRIPLES:",
        "PASS" if success else "FAIL",
    )

    if not success:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
