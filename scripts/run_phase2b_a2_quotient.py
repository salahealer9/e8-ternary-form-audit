#!/usr/bin/env python3
"""Execute Phase 2B zero-sum-triple quotient into A2 subsystems."""

from collections import Counter

from e8_ternary.a2 import (
    group_by_six_root_subsystem,
    opposite_triple,
    quotient_class_is_opposite_pair,
    quotient_multiplicity_spectrum,
    six_root_size_spectrum,
    subsystem_has_a2_structure,
    subsystem_pairwise_doubled_dot_spectrum,
    subsystem_rank,
    subsystem_reflection_closed,
)
from e8_ternary.roots import generate_e8_roots
from e8_ternary.ternary import enumerate_zero_sum_triples


def main() -> None:
    print("Phase 2B E8 A2 quotient")
    print()

    roots = generate_e8_roots()
    triples = enumerate_zero_sum_triples(roots).triples
    triple_set = set(triples)

    print("Input")
    print("  roots:", len(roots))
    print("  Phase 2A zero-sum triples:", len(triples))
    print()

    opposite_present = sum(
        opposite_triple(roots, triple) in triple_set
        for triple in triples
    )

    self_opposite = sum(
        opposite_triple(roots, triple) == triple
        for triple in triples
    )

    print("Opposite-triple relation")
    print("  triples with opposite present:", opposite_present)
    print("  self-opposite triples:", self_opposite)
    print()

    size_spectrum = six_root_size_spectrum(roots, triples)

    print("Triple/opposite union size spectrum")
    for size, count in size_spectrum.items():
        print(f"  size {size}: {count} triples")
    print()

    groups = group_by_six_root_subsystem(roots, triples)
    multiplicities = quotient_multiplicity_spectrum(groups)

    print("Quotient")
    print("  distinct six-root classes:", len(groups))
    print("  class multiplicity spectrum:")
    for multiplicity, count in multiplicities.items():
        print(f"    multiplicity {multiplicity}: {count} classes")

    opposite_pair_classes = sum(
        quotient_class_is_opposite_pair(roots, members)
        for members in groups.values()
    )

    print(
        "  classes exactly {tau, -tau}:",
        opposite_pair_classes,
    )
    print()

    rank_spectrum = dict(
        sorted(
            Counter(
                subsystem_rank(roots, subsystem)
                for subsystem in groups
            ).items()
        )
    )

    print("Exact subsystem rank spectrum")
    for rank, count in rank_spectrum.items():
        print(f"  rank {rank}: {count} subsystems")
    print()

    reflection_closed_count = sum(
        subsystem_reflection_closed(roots, subsystem)
        for subsystem in groups
    )

    print("Reflection closure")
    print(
        "  reflection-closed subsystems:",
        reflection_closed_count,
    )
    print()

    pairwise_spectra = Counter(
        tuple(
            subsystem_pairwise_doubled_dot_spectrum(
                roots,
                subsystem,
            ).items()
        )
        for subsystem in groups
    )

    print("Subsystem unordered pairwise doubled-dot spectra")
    for spectrum, count in sorted(pairwise_spectra.items()):
        print(f"  {dict(spectrum)}: {count} subsystems")
    print()

    a2_count = sum(
        subsystem_has_a2_structure(roots, subsystem)
        for subsystem in groups
    )

    print("A2 structural classification")
    print("  structurally A2 subsystems:", a2_count)
    print()

    benchmark_match = len(groups) == 1120

    print("Frozen external benchmark")
    print("  expected A2 subsystems: 1120")
    print("  observed A2 subsystems:", len(groups))
    print("  benchmark match:", benchmark_match)
    print()

    success = (
        opposite_present == len(triples)
        and self_opposite == 0
        and size_spectrum == {6: len(triples)}
        and multiplicities == {2: len(groups)}
        and opposite_pair_classes == len(groups)
        and rank_spectrum == {2: len(groups)}
        and reflection_closed_count == len(groups)
        and pairwise_spectra
        == {
            ((-8, 3), (-4, 6), (4, 6)): len(groups),
        }
        and a2_count == len(groups)
        and benchmark_match
    )

    print(
        "PHASE2B_A2_QUOTIENT:",
        "PASS" if success else "FAIL",
    )

    if not success:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
