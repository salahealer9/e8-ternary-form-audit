"""Phase 3B basis-independent Cartan 3-form sector architecture.

The Cartan subalgebra is represented symbolically by a CARTAN argument rather
than by a chosen basis vector.

This preserves the distinction between:

- a nonzero linear functional on h;
- an individual scalar coefficient after choosing a Cartan basis.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from enum import Enum
from typing import TypeAlias

from e8_ternary.cartan_support import (
    SupportClass,
    build_root_space_cartan_support,
    classify_root_triple,
)
from e8_ternary.roots import DoubledRoot, negate


class FullSectorClass(str, Enum):
    """Basis-independent support classes."""

    ROOT_ROOT_ROOT_NONZERO = "ROOT_ROOT_ROOT_NONZERO"
    CARTAN_ROOT_ROOT_FUNCTIONAL = "CARTAN_ROOT_ROOT_FUNCTIONAL"
    FORCED_ZERO_ROOT_RULE = "FORCED_ZERO_ROOT_RULE"
    FORCED_ZERO_TWO_CARTAN = "FORCED_ZERO_TWO_CARTAN"
    FORCED_ZERO_THREE_CARTAN = "FORCED_ZERO_THREE_CARTAN"


@dataclass(frozen=True)
class CartanArgument:
    """Symbolic argument ranging over the whole Cartan subalgebra."""


@dataclass(frozen=True)
class RootArgument:
    """Argument belonging to one specified one-dimensional root space."""

    index: int


CARTAN = CartanArgument()

SectorArgument: TypeAlias = CartanArgument | RootArgument
CartanRootRootBlock: TypeAlias = tuple[int, int, int]
RootLine: TypeAlias = tuple[int, int]


def root_index_map(
    roots: tuple[DoubledRoot, ...],
) -> dict[DoubledRoot, int]:
    """Return exact root -> index lookup."""
    lookup = {
        root: index
        for index, root in enumerate(roots)
    }

    if len(lookup) != len(roots):
        raise ValueError("Root collection contains duplicate roots")

    return lookup


def opposite_index_map(
    roots: tuple[DoubledRoot, ...],
) -> tuple[int, ...]:
    """Return the exact opposite-root index for every root."""
    lookup = root_index_map(roots)

    return tuple(
        lookup[negate(root)]
        for root in roots
    )


def classify_symbolic_sector(
    roots: tuple[DoubledRoot, ...],
    first: SectorArgument,
    second: SectorArgument,
    third: SectorArgument,
    *,
    lookup: dict[DoubledRoot, int] | None = None,
) -> FullSectorClass:
    """Classify one basis-independent symbolic argument triple."""
    arguments = (first, second, third)

    cartan_count = sum(
        isinstance(argument, CartanArgument)
        for argument in arguments
    )

    if cartan_count == 3:
        return FullSectorClass.FORCED_ZERO_THREE_CARTAN

    if cartan_count == 2:
        return FullSectorClass.FORCED_ZERO_TWO_CARTAN

    root_arguments = tuple(
        argument
        for argument in arguments
        if isinstance(argument, RootArgument)
    )

    if cartan_count == 1:
        if len(root_arguments) != 2:
            raise ValueError("Expected exactly two root arguments")

        left = roots[root_arguments[0].index]
        right = roots[root_arguments[1].index]

        if right == negate(left):
            return FullSectorClass.CARTAN_ROOT_ROOT_FUNCTIONAL

        return FullSectorClass.FORCED_ZERO_ROOT_RULE

    if len(root_arguments) != 3:
        raise ValueError("Expected exactly three root arguments")

    if lookup is None:
        lookup = root_index_map(roots)

    root_class = classify_root_triple(
        roots,
        root_arguments[0].index,
        root_arguments[1].index,
        root_arguments[2].index,
        lookup=lookup,
    )

    if root_class == SupportClass.ROOT_SUPPORT_NONZERO:
        return FullSectorClass.ROOT_ROOT_ROOT_NONZERO

    return FullSectorClass.FORCED_ZERO_ROOT_RULE


def opposite_root_lines(
    roots: tuple[DoubledRoot, ...],
) -> tuple[RootLine, ...]:
    """Return canonical unordered pairs {alpha, -alpha}."""
    opposite = opposite_index_map(roots)

    lines = {
        tuple(sorted((index, opposite[index])))
        for index in range(len(roots))
    }

    return tuple(sorted(lines))  # type: ignore[return-value]


def cartan_root_root_blocks(
    roots: tuple[DoubledRoot, ...],
) -> tuple[CartanRootRootBlock, ...]:
    """Construct all ordered basis-independent HRR functional blocks.

    A block is represented as

        (cartan_position, first_root_index, second_root_index)

    where cartan_position is 0, 1, or 2.

    Both root orderings occur because every root alpha is independently used
    as the first root and paired with -alpha.
    """
    opposite = opposite_index_map(roots)

    blocks = []

    for cartan_position in range(3):
        for alpha_index in range(len(roots)):
            blocks.append(
                (
                    cartan_position,
                    alpha_index,
                    opposite[alpha_index],
                )
            )

    return tuple(blocks)


def cartan_root_root_placement_spectrum(
    roots: tuple[DoubledRoot, ...],
) -> dict[int, int]:
    """Return Cartan-position -> number of HRR functional blocks."""
    return dict(
        sorted(
            Counter(
                cartan_position
                for cartan_position, _, _
                in cartan_root_root_blocks(roots)
            ).items()
        )
    )


def block_to_arguments(
    block: CartanRootRootBlock,
) -> tuple[SectorArgument, SectorArgument, SectorArgument]:
    """Convert one HRR block into symbolic arguments."""
    cartan_position, first_root, second_root = block

    root_arguments = [
        RootArgument(first_root),
        RootArgument(second_root),
    ]

    result: list[SectorArgument] = []
    root_cursor = 0

    for position in range(3):
        if position == cartan_position:
            result.append(CARTAN)
        else:
            result.append(root_arguments[root_cursor])
            root_cursor += 1

    return tuple(result)  # type: ignore[return-value]


def root_root_root_support(
    roots: tuple[DoubledRoot, ...],
) -> tuple[tuple[int, int, int], ...]:
    """Import the frozen Phase 3A root-root-root support."""
    return build_root_space_cartan_support(
        roots
    ).ordered_support
