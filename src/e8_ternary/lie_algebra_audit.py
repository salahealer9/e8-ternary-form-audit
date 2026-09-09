"""Phase 4A exhaustive Lie algebra and invariant-form audit.

This module reconstructs, independently of the Phase 3D tensor:

- the frozen 248-dimensional Lie bracket;
- the normalized invariant bilinear form B0;
- exhaustive Jacobi identities;
- the two sides of bilinear-form invariance.

All arithmetic is exact integer arithmetic.
"""

from __future__ import annotations

import hashlib
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Iterable, TypeAlias

from e8_ternary.canonical_basis import (
    SIMPLE_ROOTS,
    cartan_root_value,
    normalized_opposite_root_pairing,
    opposite_root_bracket_sign,
    root_expansion_map,
    simple_root_gram_matrix,
    structure_constant_table,
)
from e8_ternary.full_sector import opposite_index_map
from e8_ternary.roots import DoubledRoot


CARTAN_DIMENSION = 8
ROOT_BASIS_OFFSET = 8
ROOT_DIMENSION = 240
BASIS_DIMENSION = 248
ORDERED_PAIR_DOMAIN = BASIS_DIMENSION**2
CANONICAL_JACOBI_DOMAIN = 2_511_496

SparseVector: TypeAlias = tuple[tuple[int, int], ...]
ScalarTrilinearMap: TypeAlias = dict[tuple[int, int, int], int]


@dataclass(frozen=True)
class JacobiAudit:
    total_checked: int
    sector_checked: dict[str, int]
    sector_failures: dict[str, int]
    failure_examples: tuple[
        tuple[int, int, int, SparseVector],
        ...,
    ]

    @property
    def total_failures(self) -> int:
        return sum(self.sector_failures.values())


def _canonical_vector(
    coefficients: dict[int, int],
) -> SparseVector:
    """Canonical sparse vector with sorted nonzero integer coefficients."""
    return tuple(
        sorted(
            (
                index,
                coefficient,
            )
            for index, coefficient
            in coefficients.items()
            if coefficient != 0
        )
    )


def scale_vector(
    vector: SparseVector,
    scalar: int,
) -> SparseVector:
    """Scale one sparse vector exactly."""
    if scalar == 0 or not vector:
        return ()

    return tuple(
        (
            index,
            scalar * coefficient,
        )
        for index, coefficient in vector
        if scalar * coefficient != 0
    )


def add_vectors(
    *vectors: SparseVector,
) -> SparseVector:
    """Add sparse vectors exactly."""
    coefficients: dict[int, int] = {}

    for vector in vectors:
        for index, coefficient in vector:
            coefficients[index] = (
                coefficients.get(index, 0)
                + coefficient
            )

    return _canonical_vector(coefficients)


def negate_vector(
    vector: SparseVector,
) -> SparseVector:
    """Negate one sparse vector."""
    return scale_vector(vector, -1)


def build_basis_bracket_table(
    roots: Iterable[DoubledRoot],
) -> tuple[tuple[SparseVector, ...], ...]:
    """Construct the complete frozen basis-bracket table.

    No Phase 3D tensor information is used.
    """
    root_tuple = tuple(roots)

    if len(root_tuple) != ROOT_DIMENSION:
        raise ValueError(
            f"Expected {ROOT_DIMENSION} roots, got {len(root_tuple)}"
        )

    root_lookup = {
        root: index
        for index, root in enumerate(root_tuple)
    }

    opposite = opposite_index_map(root_tuple)
    expansions = root_expansion_map(root_tuple)

    structure_lookup = {
        (
            entry.alpha_index,
            entry.beta_index,
        ): (
            entry.sum_index,
            entry.coefficient,
        )
        for entry in structure_constant_table(root_tuple)
    }

    table: list[list[SparseVector]] = [
        [
            ()
            for _ in range(BASIS_DIMENSION)
        ]
        for _ in range(BASIS_DIMENSION)
    ]

    for first in range(BASIS_DIMENSION):
        for second in range(BASIS_DIMENSION):
            first_is_cartan = first < ROOT_BASIS_OFFSET
            second_is_cartan = second < ROOT_BASIS_OFFSET

            # H-H
            if first_is_cartan and second_is_cartan:
                continue

            # H-R
            if first_is_cartan and not second_is_cartan:
                root_index = second - ROOT_BASIS_OFFSET
                value = cartan_root_value(
                    first,
                    root_tuple[root_index],
                )

                if value != 0:
                    table[first][second] = (
                        (
                            second,
                            value,
                        ),
                    )

                continue

            # R-H
            if not first_is_cartan and second_is_cartan:
                root_index = first - ROOT_BASIS_OFFSET
                value = -cartan_root_value(
                    second,
                    root_tuple[root_index],
                )

                if value != 0:
                    table[first][second] = (
                        (
                            first,
                            value,
                        ),
                    )

                continue

            # R-R
            alpha_index = first - ROOT_BASIS_OFFSET
            beta_index = second - ROOT_BASIS_OFFSET

            alpha = root_tuple[alpha_index]
            beta = root_tuple[beta_index]

            # Opposite roots:
            # [e_alpha,e_-alpha] = s_alpha h_alpha.
            if opposite[alpha_index] == beta_index:
                sign = opposite_root_bracket_sign(alpha)
                coordinates = expansions[alpha]

                table[first][second] = tuple(
                    (
                        simple_index,
                        sign * coefficient,
                    )
                    for simple_index, coefficient
                    in enumerate(coordinates)
                    if coefficient != 0
                )

                continue

            # Non-opposite roots whose sum is a root.
            structure = structure_lookup.get(
                (
                    alpha_index,
                    beta_index,
                )
            )

            if structure is not None:
                sum_index, coefficient = structure

                expected_sum = tuple(
                    left + right
                    for left, right
                    in zip(alpha, beta, strict=True)
                )

                if root_lookup.get(expected_sum) != sum_index:
                    raise ValueError(
                        "Structure-constant sum index disagrees with "
                        "exact root addition"
                    )

                table[first][second] = (
                    (
                        ROOT_BASIS_OFFSET + sum_index,
                        coefficient,
                    ),
                )

    return tuple(
        tuple(row)
        for row in table
    )


def nonzero_bracket_pairs(
    table: tuple[tuple[SparseVector, ...], ...],
) -> tuple[tuple[int, int, SparseVector], ...]:
    """Return all ordered basis pairs with nonzero bracket."""
    return tuple(
        (
            first,
            second,
            table[first][second],
        )
        for first in range(BASIS_DIMENSION)
        for second in range(BASIS_DIMENSION)
        if table[first][second]
    )


def bracket_antisymmetry_holds(
    table: tuple[tuple[SparseVector, ...], ...],
) -> bool:
    """Check [x,y] = -[y,x] on every basis pair."""
    return all(
        table[first][second]
        == negate_vector(
            table[second][first]
        )
        for first in range(BASIS_DIMENSION)
        for second in range(BASIS_DIMENSION)
    )


def self_brackets_zero(
    table: tuple[tuple[SparseVector, ...], ...],
) -> bool:
    """Check every basis self-bracket vanishes."""
    return all(
        table[index][index] == ()
        for index in range(BASIS_DIMENSION)
    )


def bracket_closure_holds(
    table: tuple[tuple[SparseVector, ...], ...],
) -> bool:
    """Check all bracket output indices remain inside the frozen basis."""
    return all(
        0 <= output_index < BASIS_DIMENSION
        for row in table
        for vector in row
        for output_index, _ in vector
    )


def bracket_basis_with_vector(
    basis_index: int,
    vector: SparseVector,
    table: tuple[tuple[SparseVector, ...], ...],
) -> SparseVector:
    """Compute [basis_i, vector] by exact bilinear extension."""
    if not vector:
        return ()

    if len(vector) == 1:
        other_index, coefficient = vector[0]
        return scale_vector(
            table[basis_index][other_index],
            coefficient,
        )

    terms = tuple(
        scale_vector(
            table[basis_index][other_index],
            coefficient,
        )
        for other_index, coefficient in vector
    )

    return add_vectors(*terms)


def jacobiator(
    first: int,
    second: int,
    third: int,
    table: tuple[tuple[SparseVector, ...], ...],
) -> SparseVector:
    """Compute the exact basis Jacobiator."""
    return add_vectors(
        bracket_basis_with_vector(
            first,
            table[second][third],
            table,
        ),
        bracket_basis_with_vector(
            second,
            table[third][first],
            table,
        ),
        bracket_basis_with_vector(
            third,
            table[first][second],
            table,
        ),
    )


def _jacobi_sector(
    first: int,
    second: int,
    third: int,
) -> str:
    """Classify a canonical distinct basis triple by H/R content."""
    cartan_count = sum(
        index < ROOT_BASIS_OFFSET
        for index in (
            first,
            second,
            third,
        )
    )

    return {
        3: "HHH",
        2: "HHR",
        1: "HRR",
        0: "RRR",
    }[cartan_count]


def exhaustive_jacobi_audit(
    table: tuple[tuple[SparseVector, ...], ...],
    *,
    max_failure_examples: int = 10,
) -> JacobiAudit:
    """Check Jacobi on every canonical distinct basis triple."""
    checked: Counter[str] = Counter()
    failures: Counter[str] = Counter()

    examples: list[
        tuple[int, int, int, SparseVector]
    ] = []

    total = 0

    for first, second, third in combinations(
        range(BASIS_DIMENSION),
        3,
    ):
        sector = _jacobi_sector(
            first,
            second,
            third,
        )

        checked[sector] += 1
        total += 1

        value = jacobiator(
            first,
            second,
            third,
            table,
        )

        if value:
            failures[sector] += 1

            if len(examples) < max_failure_examples:
                examples.append(
                    (
                        first,
                        second,
                        third,
                        value,
                    )
                )

    return JacobiAudit(
        total_checked=total,
        sector_checked={
            sector: checked[sector]
            for sector in (
                "HHH",
                "HHR",
                "HRR",
                "RRR",
            )
        },
        sector_failures={
            sector: failures[sector]
            for sector in (
                "HHH",
                "HHR",
                "HRR",
                "RRR",
            )
        },
        failure_examples=tuple(examples),
    )


def build_bilinear_table(
    roots: Iterable[DoubledRoot],
) -> tuple[tuple[int, ...], ...]:
    """Construct the frozen normalized invariant bilinear form B0."""
    root_tuple = tuple(roots)

    if len(root_tuple) != ROOT_DIMENSION:
        raise ValueError(
            f"Expected {ROOT_DIMENSION} roots, got {len(root_tuple)}"
        )

    opposite = opposite_index_map(root_tuple)
    gram = simple_root_gram_matrix()

    table = [
        [
            0
            for _ in range(BASIS_DIMENSION)
        ]
        for _ in range(BASIS_DIMENSION)
    ]

    # H-H block.
    for first in range(CARTAN_DIMENSION):
        for second in range(CARTAN_DIMENSION):
            table[first][second] = gram[first][second]

    # Root-root opposite pairings.
    for alpha_index, alpha in enumerate(root_tuple):
        beta_index = opposite[alpha_index]

        table[
            ROOT_BASIS_OFFSET + alpha_index
        ][
            ROOT_BASIS_OFFSET + beta_index
        ] = normalized_opposite_root_pairing(alpha)

    return tuple(
        tuple(row)
        for row in table
    )


def bilinear_support_count(
    table: tuple[tuple[int, ...], ...],
) -> int:
    """Count ordered nonzero B0 entries."""
    return sum(
        value != 0
        for row in table
        for value in row
    )


def bilinear_value_spectrum(
    table: tuple[tuple[int, ...], ...],
) -> dict[int, int]:
    """Return nonzero B0 coefficient spectrum."""
    return dict(
        sorted(
            Counter(
                value
                for row in table
                for value in row
                if value != 0
            ).items()
        )
    )


def bilinear_symmetry_holds(
    table: tuple[tuple[int, ...], ...],
) -> bool:
    """Check B0(x,y)=B0(y,x) on all basis pairs."""
    return all(
        table[first][second]
        == table[second][first]
        for first in range(BASIS_DIMENSION)
        for second in range(BASIS_DIMENSION)
    )


def exact_integer_determinant(
    matrix: tuple[tuple[int, ...], ...],
) -> int:
    """Exact determinant by rational Gaussian elimination."""
    size = len(matrix)

    work = [
        [
            Fraction(value)
            for value in row
        ]
        for row in matrix
    ]

    determinant = Fraction(1)
    sign = 1

    for column in range(size):
        pivot_row = next(
            (
                row
                for row in range(column, size)
                if work[row][column] != 0
            ),
            None,
        )

        if pivot_row is None:
            return 0

        if pivot_row != column:
            work[column], work[pivot_row] = (
                work[pivot_row],
                work[column],
            )
            sign *= -1

        pivot = work[column][column]
        determinant *= pivot

        for row in range(column + 1, size):
            if work[row][column] == 0:
                continue

            factor = work[row][column] / pivot

            for inner in range(
                column + 1,
                size,
            ):
                work[row][inner] -= (
                    factor
                    * work[column][inner]
                )

            work[row][column] = Fraction(0)

    result = determinant * sign

    if result.denominator != 1:
        raise ValueError(
            "Expected integral determinant"
        )

    return int(result)


def structural_nondegeneracy_holds(
    roots: Iterable[DoubledRoot],
    bilinear: tuple[tuple[int, ...], ...],
) -> bool:
    """Verify nondegeneracy from Cartan and opposite-root blocks."""
    root_tuple = tuple(roots)
    opposite = opposite_index_map(root_tuple)

    cartan_determinant = exact_integer_determinant(
        simple_root_gram_matrix()
    )

    if cartan_determinant != 1:
        return False

    for alpha_index in range(len(root_tuple)):
        beta_index = opposite[alpha_index]

        value = bilinear[
            ROOT_BASIS_OFFSET + alpha_index
        ][
            ROOT_BASIS_OFFSET + beta_index
        ]

        if value not in (-1, 1):
            return False

        if opposite[beta_index] != alpha_index:
            return False

    return True


def bilinear_vector_basis(
    vector: SparseVector,
    basis_index: int,
    bilinear: tuple[tuple[int, ...], ...],
) -> int:
    """Compute B0(vector,basis_i) exactly."""
    return sum(
        coefficient
        * bilinear[vector_index][basis_index]
        for vector_index, coefficient in vector
    )


def bilinear_basis_vector(
    basis_index: int,
    vector: SparseVector,
    bilinear: tuple[tuple[int, ...], ...],
) -> int:
    """Compute B0(basis_i,vector) exactly."""
    return sum(
        coefficient
        * bilinear[basis_index][vector_index]
        for vector_index, coefficient in vector
    )


def build_invariance_maps(
    bracket: tuple[tuple[SparseVector, ...], ...],
    bilinear: tuple[tuple[int, ...], ...],
) -> tuple[
    ScalarTrilinearMap,
    ScalarTrilinearMap,
]:
    """Construct both sides of B0([X,Y],Z)=B0(X,[Y,Z]) independently."""
    nonzero_pairs = nonzero_bracket_pairs(
        bracket
    )

    left_map: ScalarTrilinearMap = {}

    # L_ijk = B0([B_i,B_j],B_k)
    for first, second, bracket_value in nonzero_pairs:
        for third in range(BASIS_DIMENSION):
            scalar = bilinear_vector_basis(
                bracket_value,
                third,
                bilinear,
            )

            if scalar != 0:
                left_map[
                    (
                        first,
                        second,
                        third,
                    )
                ] = scalar

    right_map: ScalarTrilinearMap = {}

    # R_ijk = B0(B_i,[B_j,B_k])
    for second, third, bracket_value in nonzero_pairs:
        for first in range(BASIS_DIMENSION):
            scalar = bilinear_basis_vector(
                first,
                bracket_value,
                bilinear,
            )

            if scalar != 0:
                right_map[
                    (
                        first,
                        second,
                        third,
                    )
                ] = scalar

    return left_map, right_map


def scalar_map_spectrum(
    scalar_map: ScalarTrilinearMap,
) -> dict[int, int]:
    """Return nonzero scalar spectrum."""
    return dict(
        sorted(
            Counter(
                scalar_map.values()
            ).items()
        )
    )


def scalar_map_discrepancies(
    left: ScalarTrilinearMap,
    right: ScalarTrilinearMap,
) -> tuple[
    set[tuple[int, int, int]],
    set[tuple[int, int, int]],
    dict[tuple[int, int, int], tuple[int, int]],
]:
    """Compare two sparse scalar maps exactly."""
    left_keys = set(left)
    right_keys = set(right)

    left_only = left_keys - right_keys
    right_only = right_keys - left_keys

    differing = {
        key: (
            left[key],
            right[key],
        )
        for key in (
            left_keys & right_keys
        )
        if left[key] != right[key]
    }

    return (
        left_only,
        right_only,
        differing,
    )


def sha256_file(
    path: str | Path,
) -> str:
    """Return SHA-256 of one file."""
    return hashlib.sha256(
        Path(path).read_bytes()
    ).hexdigest()
