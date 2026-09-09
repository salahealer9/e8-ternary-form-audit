"""Phase 3C canonical E8 basis and normalization data.

This module implements the conventions frozen in the Phase 3C protocol:

- explicit simple roots;
- exact simple-root coordinates;
- positive/negative roots and heights;
- epsilon convention;
- epsilon-canonical root-root structure constants;
- normalized opposite-root pairings.

All root arithmetic is exact.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from enum import Enum
from fractions import Fraction
from itertools import combinations
from typing import Iterable, TypeAlias

from e8_ternary.roots import (
    DoubledRoot,
    doubled_dot,
    doubled_norm_squared,
)


SimpleCoordinates: TypeAlias = tuple[int, int, int, int, int, int, int, int]
DynkinEdge: TypeAlias = tuple[int, int]


SIMPLE_ROOTS: tuple[DoubledRoot, ...] = (
    (2, -2, 0, 0, 0, 0, 0, 0),
    (0, 2, -2, 0, 0, 0, 0, 0),
    (0, 0, 2, -2, 0, 0, 0, 0),
    (0, 0, 0, 2, -2, 0, 0, 0),
    (0, 0, 0, 0, 2, -2, 0, 0),
    (0, 0, 0, 0, 0, 2, 2, 0),
    (-1, -1, -1, -1, -1, -1, -1, -1),
    (0, 0, 0, 0, 0, 2, -2, 0),
)


class RootSign(str, Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"


@dataclass(frozen=True)
class StructureConstantEntry:
    """One nonzero root-root Chevalley bracket coefficient."""

    alpha_index: int
    beta_index: int
    sum_index: int
    coefficient: int


def ordinary_inner_product(
    left: DoubledRoot,
    right: DoubledRoot,
) -> int:
    """Return exact ordinary root inner product."""
    numerator = doubled_dot(left, right)

    if numerator % 4 != 0:
        raise ValueError(
            "Doubled-coordinate dot product is not divisible by four"
        )

    return numerator // 4


def simple_root_gram_matrix() -> tuple[tuple[int, ...], ...]:
    """Return the exact 8 x 8 simple-root Gram matrix."""
    return tuple(
        tuple(
            ordinary_inner_product(left, right)
            for right in SIMPLE_ROOTS
        )
        for left in SIMPLE_ROOTS
    )


def dynkin_edges() -> tuple[DynkinEdge, ...]:
    """Derive Dynkin edges from simple-root inner product -1."""
    edges = []

    for i, j in combinations(range(len(SIMPLE_ROOTS)), 2):
        if ordinary_inner_product(
            SIMPLE_ROOTS[i],
            SIMPLE_ROOTS[j],
        ) == -1:
            edges.append((i, j))

    return tuple(edges)


def _solve_exact_square_system(
    matrix: list[list[int]],
    vector: DoubledRoot,
) -> tuple[Fraction, ...]:
    """Solve A x = b exactly by rational Gaussian elimination."""
    size = len(matrix)

    augmented = [
        [
            Fraction(value)
            for value in matrix[row]
        ]
        + [Fraction(vector[row])]
        for row in range(size)
    ]

    pivot_row = 0

    for column in range(size):
        selected = next(
            (
                row
                for row in range(pivot_row, size)
                if augmented[row][column] != 0
            ),
            None,
        )

        if selected is None:
            raise ValueError("Simple-root coordinate matrix is singular")

        augmented[pivot_row], augmented[selected] = (
            augmented[selected],
            augmented[pivot_row],
        )

        pivot = augmented[pivot_row][column]

        augmented[pivot_row] = [
            value / pivot
            for value in augmented[pivot_row]
        ]

        for row in range(size):
            if row == pivot_row:
                continue

            factor = augmented[row][column]

            if factor == 0:
                continue

            augmented[row] = [
                value - factor * pivot_value
                for value, pivot_value in zip(
                    augmented[row],
                    augmented[pivot_row],
                    strict=True,
                )
            ]

        pivot_row += 1

    return tuple(
        augmented[row][-1]
        for row in range(size)
    )


def simple_coordinates(
    root: DoubledRoot,
) -> SimpleCoordinates:
    """Expand one root exactly in the frozen simple-root basis."""
    # Coordinate equation:
    #
    # root[d] = sum_i n_i SIMPLE_ROOTS[i][d]
    matrix = [
        [
            SIMPLE_ROOTS[column][row]
            for column in range(8)
        ]
        for row in range(8)
    ]

    solution = _solve_exact_square_system(
        matrix,
        root,
    )

    if any(value.denominator != 1 for value in solution):
        raise ValueError(
            "Root does not have integral simple-root coordinates"
        )

    result = tuple(
        int(value)
        for value in solution
    )

    return result  # type: ignore[return-value]


def root_expansion_map(
    roots: Iterable[DoubledRoot],
) -> dict[DoubledRoot, SimpleCoordinates]:
    """Return exact simple-root expansions for all roots."""
    return {
        root: simple_coordinates(root)
        for root in roots
    }


def classify_root_sign(
    coordinates: SimpleCoordinates,
) -> RootSign:
    """Classify a root from its simple-root coefficients."""
    positive = all(value >= 0 for value in coordinates)
    negative = all(value <= 0 for value in coordinates)

    if positive and not negative:
        return RootSign.POSITIVE

    if negative and not positive:
        return RootSign.NEGATIVE

    raise ValueError(
        "Root coefficients are not uniformly nonnegative or nonpositive"
    )


def root_height(
    coordinates: SimpleCoordinates,
) -> int:
    """Return root height in the frozen simple-root basis."""
    return sum(coordinates)


def derive_epsilon() -> tuple[int, ...]:
    """Derive epsilon from epsilon(alpha_1)=+1 and Dynkin adjacency."""
    adjacency = {
        index: set()
        for index in range(8)
    }

    for left, right in dynkin_edges():
        adjacency[left].add(right)
        adjacency[right].add(left)

    epsilon: list[int | None] = [None] * 8
    epsilon[0] = 1

    queue: deque[int] = deque([0])

    while queue:
        current = queue.popleft()

        assert epsilon[current] is not None

        required_neighbour = -epsilon[current]

        for neighbour in sorted(adjacency[current]):
            if epsilon[neighbour] is None:
                epsilon[neighbour] = required_neighbour
                queue.append(neighbour)
            elif epsilon[neighbour] != required_neighbour:
                raise ValueError(
                    "Dynkin graph is incompatible with alternating epsilon"
                )

    if any(value is None for value in epsilon):
        raise ValueError("Dynkin graph is disconnected")

    return tuple(
        int(value)
        for value in epsilon
    )


def epsilon_power(
    epsilon_value: int,
    exponent: int,
) -> int:
    """Evaluate (+/-1)^n exactly for any integer n."""
    if epsilon_value not in (-1, 1):
        raise ValueError("epsilon must equal +/-1")

    if epsilon_value == 1:
        return 1

    return -1 if exponent % 2 else 1


def canonical_structure_constant(
    alpha: DoubledRoot,
    beta: DoubledRoot,
    *,
    roots: tuple[DoubledRoot, ...],
    expansions: dict[DoubledRoot, SimpleCoordinates] | None = None,
    epsilon: tuple[int, ...] | None = None,
) -> int:
    """Return N^epsilon_{alpha,beta} when alpha+beta is a root.

    Implements the frozen simply-laced Geck-Lang formula.
    """
    root_set = set(roots)

    summed = tuple(
        a + b
        for a, b in zip(alpha, beta, strict=True)
    )

    if summed not in root_set:
        raise ValueError("alpha + beta is not a root")

    if expansions is None:
        expansions = root_expansion_map(roots)

    if epsilon is None:
        epsilon = derive_epsilon()

    alpha_coordinates = expansions[alpha]

    value = (
        (1 if classify_root_sign(expansions[alpha]) == RootSign.POSITIVE else -1)
        *
        (1 if classify_root_sign(expansions[beta]) == RootSign.POSITIVE else -1)
        *
        (1 if classify_root_sign(expansions[summed]) == RootSign.POSITIVE else -1)
    )

    for index, coefficient in enumerate(alpha_coordinates):
        pairing = ordinary_inner_product(
            SIMPLE_ROOTS[index],
            beta,
        )

        exponent = coefficient * pairing

        value *= epsilon_power(
            epsilon[index],
            exponent,
        )

    if value not in (-1, 1):
        raise AssertionError(
            "Canonical simply-laced structure constant is not +/-1"
        )

    return value


def structure_constant_table(
    roots: tuple[DoubledRoot, ...],
) -> tuple[StructureConstantEntry, ...]:
    """Return all nonzero root-root structure constants."""
    lookup = {
        root: index
        for index, root in enumerate(roots)
    }

    expansions = root_expansion_map(roots)
    epsilon = derive_epsilon()

    entries: list[StructureConstantEntry] = []

    for alpha_index, alpha in enumerate(roots):
        for beta_index, beta in enumerate(roots):
            summed = tuple(
                a + b
                for a, b in zip(alpha, beta, strict=True)
            )

            sum_index = lookup.get(summed)

            if sum_index is None:
                continue

            coefficient = canonical_structure_constant(
                alpha,
                beta,
                roots=roots,
                expansions=expansions,
                epsilon=epsilon,
            )

            entries.append(
                StructureConstantEntry(
                    alpha_index=alpha_index,
                    beta_index=beta_index,
                    sum_index=sum_index,
                    coefficient=coefficient,
                )
            )

    return tuple(entries)


def opposite_root_bracket_sign(
    root: DoubledRoot,
) -> int:
    """Return the frozen epsilon-canonical opposite-root bracket sign.

    The Phase 3C convention is

        [e_alpha, e_-alpha]
            = (-1)^ht(alpha) h_alpha.
    """
    height = root_height(simple_coordinates(root))

    return -1 if height % 2 else 1


def normalized_opposite_root_pairing(
    root: DoubledRoot,
) -> int:
    """Derive B0(e_alpha, e_-alpha) from invariance.

    Using

        [e_alpha,e_-alpha] = s_alpha h_alpha

    and

        B0(h_i,h_alpha) = alpha(h_i),

    invariance gives

        s_alpha B0(h_alpha,h_i)
        =
        alpha(h_i) B0(e_alpha,e_-alpha).

    At least one simple-Cartan evaluation alpha(h_i) is nonzero for every
    root, so the pairing is derived exactly rather than separately imposed.
    """
    bracket_sign = opposite_root_bracket_sign(root)

    pairing: int | None = None

    for simple_index in range(8):
        alpha_hi = cartan_root_value(
            simple_index,
            root,
        )

        if alpha_hi == 0:
            continue

        numerator = (
            bracket_sign
            *
            normalized_cartan_pairing_with_coroot(
                simple_index,
                root,
            )
        )

        if numerator % alpha_hi != 0:
            raise ValueError(
                "Invariant-form derivation produced a non-integral pairing"
            )

        candidate = numerator // alpha_hi

        if candidate not in (-1, 1):
            raise ValueError(
                "Derived opposite-root pairing is not +/-1"
            )

        pairing = candidate
        break

    if pairing is None:
        raise ValueError(
            "Root has zero evaluation on every simple Cartan direction"
        )

    # Independently verify the derived scalar in every Cartan direction.
    for simple_index in range(8):
        alpha_hi = cartan_root_value(
            simple_index,
            root,
        )

        left = (
            bracket_sign
            *
            normalized_cartan_pairing_with_coroot(
                simple_index,
                root,
            )
        )

        right = alpha_hi * pairing

        if left != right:
            raise ValueError(
                "Derived opposite-root pairing violates invariance"
            )

    return pairing


def cartan_root_value(
    simple_index: int,
    root: DoubledRoot,
) -> int:
    """Return alpha(h_i) for the frozen simply-laced Cartan basis."""
    return ordinary_inner_product(
        SIMPLE_ROOTS[simple_index],
        root,
    )


def normalized_cartan_pairing_with_coroot(
    simple_index: int,
    root: DoubledRoot,
) -> int:
    """Return B0(h_i, h_alpha) under B0(h_i,h_j)=a_ij."""
    coordinates = simple_coordinates(root)
    gram = simple_root_gram_matrix()

    return sum(
        coordinates[j] * gram[simple_index][j]
        for j in range(8)
    )


def opposite_pairing_invariance_holds(
    root: DoubledRoot,
) -> bool:
    """Verify the frozen opposite-root pairing via invariance.

    The identity checked for every simple Cartan direction is

        B0([e_alpha,e_-alpha], h_i)
        =
        B0(e_alpha,[e_-alpha,h_i]).
    """
    bracket_sign = opposite_root_bracket_sign(root)
    root_pairing = normalized_opposite_root_pairing(root)

    for simple_index in range(8):
        alpha_hi = cartan_root_value(
            simple_index,
            root,
        )

        left = (
            bracket_sign
            *
            normalized_cartan_pairing_with_coroot(
                simple_index,
                root,
            )
        )

        right = alpha_hi * root_pairing

        if left != right:
            return False

    return True


def structure_constant_sign_spectrum(
    roots: tuple[DoubledRoot, ...],
) -> dict[int, int]:
    """Return sign -> number of nonzero root-root brackets."""
    return dict(
        sorted(
            Counter(
                entry.coefficient
                for entry in structure_constant_table(roots)
            ).items()
        )
    )
