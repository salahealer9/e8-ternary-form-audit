#!/usr/bin/env python3
"""Execute Phase 3B basis-independent full Cartan sector analysis."""

from collections import Counter

from e8_ternary.full_sector import (
    CARTAN,
    FullSectorClass,
    RootArgument,
    block_to_arguments,
    cartan_root_root_blocks,
    cartan_root_root_placement_spectrum,
    classify_symbolic_sector,
    opposite_index_map,
    opposite_root_lines,
    root_root_root_support,
)
from e8_ternary.roots import generate_e8_roots


def main() -> None:
    print("Phase 3B E8 full Cartan sector support")
    print()

    roots = generate_e8_roots()
    opposite = opposite_index_map(roots)

    print("Lie algebra decomposition")
    print("  Cartan dimension:", 8)
    print("  nonzero root spaces:", len(roots))
    print("  total dimension:", 8 + len(roots))
    print()

    # Frozen Phase 3A sector.
    rrr_support = root_root_root_support(roots)

    print("Root-root-root sector")
    print("  nonzero ordered support:", len(rrr_support))
    print()

    lines = opposite_root_lines(roots)

    print("Opposite-root architecture")
    print("  roots:", len(roots))
    print("  unordered opposite-root lines:", len(lines))
    print()

    blocks = cartan_root_root_blocks(roots)
    placement_spectrum = cartan_root_root_placement_spectrum(
        roots
    )

    functional_blocks = sum(
        classify_symbolic_sector(
            roots,
            *block_to_arguments(block),
        )
        == FullSectorClass.CARTAN_ROOT_ROOT_FUNCTIONAL
        for block in blocks
    )

    print("Cartan-root-root functional blocks")
    print("  ordered symbolic blocks:", len(blocks))
    print("  blocks classifying functional:", functional_blocks)
    print("  Cartan-placement spectrum:")
    for position, count in placement_spectrum.items():
        print(f"    position {position}: {count}")
    print()

    # Independently census one fixed Cartan placement over all ordered root
    # pairs. This does not use the preconstructed block list.
    fixed_placement_census: Counter[FullSectorClass] = Counter()

    for first in range(len(roots)):
        for second in range(len(roots)):
            fixed_placement_census[
                classify_symbolic_sector(
                    roots,
                    CARTAN,
                    RootArgument(first),
                    RootArgument(second),
                )
            ] += 1

    print("One-Cartan-placement root-pair census")
    for classification, count in sorted(
        fixed_placement_census.items(),
        key=lambda item: item[0].value,
    ):
        print(f"  {classification.value}: {count}")
    print()

    exact_opposite_pairs = sum(
        second == opposite[first]
        for first in range(len(roots))
        for second in range(len(roots))
    )

    print("Independent opposite-root check")
    print(
        "  ordered opposite-root pairs per Cartan placement:",
        exact_opposite_pairs,
    )
    print()

    # Two-Cartan symbolic blocks: three placements of the lone root.
    two_cartan_zero = 0

    for root_index in range(len(roots)):
        root = RootArgument(root_index)

        symbolic_cases = (
            (CARTAN, CARTAN, root),
            (CARTAN, root, CARTAN),
            (root, CARTAN, CARTAN),
        )

        for arguments in symbolic_cases:
            if (
                classify_symbolic_sector(
                    roots,
                    *arguments,
                )
                == FullSectorClass.FORCED_ZERO_TWO_CARTAN
            ):
                two_cartan_zero += 1

    print("Two-Cartan sector")
    print("  symbolic blocks checked:", 3 * len(roots))
    print("  forced-zero blocks:", two_cartan_zero)
    print()

    three_cartan = classify_symbolic_sector(
        roots,
        CARTAN,
        CARTAN,
        CARTAN,
    )

    print("Three-Cartan sector")
    print(
        "  classification:",
        three_cartan.value,
    )
    print()

    success = (
        8 + len(roots) == 248
        and len(rrr_support) == 13440
        and len(lines) == 120
        and len(blocks) == 720
        and functional_blocks == 720
        and placement_spectrum == {
            0: 240,
            1: 240,
            2: 240,
        }
        and fixed_placement_census
        == {
            FullSectorClass.CARTAN_ROOT_ROOT_FUNCTIONAL: 240,
            FullSectorClass.FORCED_ZERO_ROOT_RULE: 57360,
        }
        and exact_opposite_pairs == 240
        and two_cartan_zero == 720
        and three_cartan
        == FullSectorClass.FORCED_ZERO_THREE_CARTAN
    )

    print(
        "PHASE3B_FULL_SECTOR_SUPPORT:",
        "PASS" if success else "FAIL",
    )

    if not success:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
