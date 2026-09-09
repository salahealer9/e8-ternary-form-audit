"""Phase 3B basis-independent full Cartan sector tests."""

from collections import Counter
from functools import lru_cache

from e8_ternary.cartan_support import build_root_space_cartan_support
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


@lru_cache(maxsize=1)
def phase3b_roots():
    return generate_e8_roots()


def test_opposite_root_lines() -> None:
    roots = phase3b_roots()
    opposite = opposite_index_map(roots)
    lines = opposite_root_lines(roots)

    assert len(lines) == 120

    assert all(
        opposite[left] == right
        and opposite[right] == left
        for left, right in lines
    )


def test_cartan_root_root_functional_block_count() -> None:
    roots = phase3b_roots()
    blocks = cartan_root_root_blocks(roots)

    assert len(blocks) == 720

    assert cartan_root_root_placement_spectrum(
        roots
    ) == {
        0: 240,
        1: 240,
        2: 240,
    }


def test_every_hrr_block_classifies_functional() -> None:
    roots = phase3b_roots()

    assert all(
        classify_symbolic_sector(
            roots,
            *block_to_arguments(block),
        )
        == FullSectorClass.CARTAN_ROOT_ROOT_FUNCTIONAL
        for block in cartan_root_root_blocks(roots)
    )


def test_nonopposite_hrr_pairs_are_forced_zero() -> None:
    roots = phase3b_roots()
    opposite = opposite_index_map(roots)

    counts = Counter()

    for first in range(len(roots)):
        for second in range(len(roots)):
            classification = classify_symbolic_sector(
                roots,
                CARTAN,
                RootArgument(first),
                RootArgument(second),
            )
            counts[classification] += 1

            if second == opposite[first]:
                assert (
                    classification
                    == FullSectorClass.CARTAN_ROOT_ROOT_FUNCTIONAL
                )
            else:
                assert (
                    classification
                    == FullSectorClass.FORCED_ZERO_ROOT_RULE
                )

    assert counts == {
        FullSectorClass.CARTAN_ROOT_ROOT_FUNCTIONAL: 240,
        FullSectorClass.FORCED_ZERO_ROOT_RULE: 57360,
    }


def test_two_cartan_sector_vanishes() -> None:
    roots = phase3b_roots()

    for root_index in range(len(roots)):
        root = RootArgument(root_index)

        assert classify_symbolic_sector(
            roots,
            CARTAN,
            CARTAN,
            root,
        ) == FullSectorClass.FORCED_ZERO_TWO_CARTAN

        assert classify_symbolic_sector(
            roots,
            CARTAN,
            root,
            CARTAN,
        ) == FullSectorClass.FORCED_ZERO_TWO_CARTAN

        assert classify_symbolic_sector(
            roots,
            root,
            CARTAN,
            CARTAN,
        ) == FullSectorClass.FORCED_ZERO_TWO_CARTAN


def test_three_cartan_sector_vanishes() -> None:
    roots = phase3b_roots()

    assert classify_symbolic_sector(
        roots,
        CARTAN,
        CARTAN,
        CARTAN,
    ) == FullSectorClass.FORCED_ZERO_THREE_CARTAN


def test_root_root_root_support_is_phase3a_support() -> None:
    roots = phase3b_roots()

    imported = root_root_root_support(roots)
    phase3a = build_root_space_cartan_support(
        roots
    ).ordered_support

    assert imported == phase3a
    assert len(imported) == 13440


def test_every_phase3a_support_entry_classifies_rrr_nonzero() -> None:
    roots = phase3b_roots()
    support = root_root_root_support(roots)

    lookup = {
        root: index
        for index, root in enumerate(roots)
    }

    assert all(
        classify_symbolic_sector(
            roots,
            RootArgument(i),
            RootArgument(j),
            RootArgument(k),
            lookup=lookup,
        )
        == FullSectorClass.ROOT_ROOT_ROOT_NONZERO
        for i, j, k in support
    )
