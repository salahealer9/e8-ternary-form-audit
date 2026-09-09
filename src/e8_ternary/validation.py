"""Independent structural validation of the E8 root system.

This module does not use the Phase 1A coordinate-family generators.

The independent root set is reconstructed from the doubled-coordinate
E8 lattice criterion together with q.q = 8.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import product
from typing import Iterable, TypeAlias


DoubledRoot: TypeAlias = tuple[int, int, int, int, int, int, int, int]


def doubled_dot(left: DoubledRoot, right: DoubledRoot) -> int:
    """Exact dot product in doubled coordinates."""
    return sum(a * b for a, b in zip(left, right, strict=True))


def same_coordinate_parity(vector: DoubledRoot) -> bool:
    """Return True iff all coordinates have the same parity."""
    parity = vector[0] % 2
    return all(coordinate % 2 == parity for coordinate in vector)


def satisfies_doubled_e8_lattice_condition(vector: DoubledRoot) -> bool:
    """Test the doubled-coordinate E8 lattice criterion."""
    return (
        same_coordinate_parity(vector)
        and sum(vector) % 4 == 0
    )


def generate_lattice_roots() -> tuple[DoubledRoot, ...]:
    """Independently enumerate norm-2 E8 roots from the lattice criterion.

    The norm condition q.q = 8 implies |q_i| <= 2, so the search range
    {-2,-1,0,1,2} is exhaustive.

    No expected root count is used.
    """
    roots: list[DoubledRoot] = []

    for coordinates in product(range(-2, 3), repeat=8):
        vector: DoubledRoot = coordinates

        if doubled_dot(vector, vector) != 8:
            continue

        if not satisfies_doubled_e8_lattice_condition(vector):
            continue

        roots.append(vector)

    return tuple(sorted(roots))


def exact_rank(vectors: Iterable[DoubledRoot]) -> int:
    """Compute exact rational rank by Gaussian elimination."""
    matrix = [
        [Fraction(value) for value in vector]
        for vector in vectors
    ]

    if not matrix:
        return 0

    rows = len(matrix)
    columns = len(matrix[0])

    rank = 0
    pivot_column = 0

    while rank < rows and pivot_column < columns:
        pivot_row = next(
            (
                row
                for row in range(rank, rows)
                if matrix[row][pivot_column] != 0
            ),
            None,
        )

        if pivot_row is None:
            pivot_column += 1
            continue

        matrix[rank], matrix[pivot_row] = (
            matrix[pivot_row],
            matrix[rank],
        )

        pivot = matrix[rank][pivot_column]
        matrix[rank] = [
            value / pivot
            for value in matrix[rank]
        ]

        for row in range(rows):
            if row == rank:
                continue

            factor = matrix[row][pivot_column]
            if factor == 0:
                continue

            matrix[row] = [
                value - factor * pivot_value
                for value, pivot_value
                in zip(matrix[row], matrix[rank], strict=True)
            ]

        rank += 1
        pivot_column += 1

        if rank == columns:
            break

    return rank


def crystallographic_integrality(
    roots: Iterable[DoubledRoot],
) -> bool:
    """Check exact crystallographic integrality for every root pair.

    Since alpha.alpha = 2, the Cartan integer is simply alpha.beta.

    With doubled coordinates:

        alpha.beta = (q.r) / 4.
    """
    root_tuple = tuple(roots)

    return all(
        doubled_dot(alpha, beta) % 4 == 0
        for alpha in root_tuple
        for beta in root_tuple
    )


def reflect_doubled(
    beta: DoubledRoot,
    alpha: DoubledRoot,
) -> DoubledRoot:
    """Reflect beta in the hyperplane orthogonal to alpha.

    In ordinary coordinates:

        s_alpha(beta) = beta - (alpha.beta) alpha

    because alpha.alpha = 2.

    For doubled coordinates q_alpha and q_beta:

        q' = q_beta - ((q_alpha.q_beta) / 4) q_alpha.
    """
    numerator = doubled_dot(alpha, beta)

    if numerator % 4 != 0:
        raise ValueError(
            "Non-integral alpha.beta encountered during exact reflection"
        )

    coefficient = numerator // 4

    return tuple(
        b - coefficient * a
        for a, b in zip(alpha, beta, strict=True)
    )  # type: ignore[return-value]


def reflection_closure(
    roots: Iterable[DoubledRoot],
) -> bool:
    """Check closure under every root reflection."""
    root_tuple = tuple(roots)
    root_set = set(root_tuple)

    for alpha in root_tuple:
        for beta in root_tuple:
            if reflect_doubled(beta, alpha) not in root_set:
                return False

    return True


def nonorthogonality_graph_connected(
    roots: Iterable[DoubledRoot],
) -> bool:
    """Check connectivity after excluding orthogonal and opposite pairs.

    Distinct roots are adjacent when their ordinary inner product is
    nonzero and they are not negatives of one another.
    """
    root_tuple = tuple(roots)

    if not root_tuple:
        return False

    root_set = set(root_tuple)

    start = root_tuple[0]
    visited = {start}
    queue: deque[DoubledRoot] = deque([start])

    while queue:
        current = queue.popleft()

        for candidate in root_tuple:
            if candidate in visited or candidate == current:
                continue

            if all(
                a == -b
                for a, b in zip(current, candidate, strict=True)
            ):
                continue

            if doubled_dot(current, candidate) == 0:
                continue

            visited.add(candidate)
            queue.append(candidate)

    return visited == root_set


def set_differences(
    left: Iterable[DoubledRoot],
    right: Iterable[DoubledRoot],
) -> tuple[
    tuple[DoubledRoot, ...],
    tuple[DoubledRoot, ...],
]:
    """Return exact set differences left-right and right-left."""
    left_set = set(left)
    right_set = set(right)

    return (
        tuple(sorted(left_set - right_set)),
        tuple(sorted(right_set - left_set)),
    )
