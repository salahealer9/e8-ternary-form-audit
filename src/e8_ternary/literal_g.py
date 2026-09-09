"""Literal realization of the initiating notation g(v1, v2, v3).

Phase 6B freezes

    g(v1,v2,v3) = B0(v1,[v2,v3])

as the normalized E8 Cartan 3-form in the repository's frozen basis.

Two exact evaluation routes are supplied:

    g_from_tensor  -- contraction against the sealed Phase 3D tensor
    g_from_algebra -- independent bracket + invariant-form evaluation

The public ``g`` uses the sealed sparse tensor.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import TypeAlias

from e8_ternary.canonical_basis import simple_root_gram_matrix
from e8_ternary.full_sector import opposite_index_map
from e8_ternary.lie_algebra_audit import (
    BASIS_DIMENSION,
    ROOT_BASIS_OFFSET,
    SparseVector as IntegerSparseVector,
    build_basis_bracket_table,
    build_bilinear_table,
    sha256_file,
)
from e8_ternary.roots import DoubledRoot, generate_e8_roots
from e8_ternary.sparse_cartan_form import load_sparse_cartan_form


PHASE3D_JSON = Path(
    "data/derived/phase3d_signed_sparse_cartan_form.json"
)

PHASE3D_SHA256 = (
    "43b52b4116dfcf0dace332234b5c9dc50"
    "d95d51effb690aec8aebe39ad4f92e8"
)

ExactScalar: TypeAlias = Fraction
ExactVector: TypeAlias = tuple[tuple[int, Fraction], ...]


def _fraction(value: int | Fraction) -> Fraction:
    """Convert one exact scalar to Fraction."""
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    raise TypeError(
        "Phase 6B exact vectors accept only int or Fraction coefficients"
    )


def vector(
    terms: Mapping[int, int | Fraction]
    | Iterable[tuple[int, int | Fraction]],
) -> ExactVector:
    """Canonicalize an exact sparse E8 vector.

    Duplicate indices are combined, zeros removed, and indices sorted.
    """
    items = terms.items() if isinstance(terms, Mapping) else terms

    coefficients: dict[int, Fraction] = {}

    for index, raw_coefficient in items:
        if not isinstance(index, int):
            raise TypeError("Basis index must be an integer")

        if not 0 <= index < BASIS_DIMENSION:
            raise ValueError(
                f"Basis index {index} outside 0..{BASIS_DIMENSION - 1}"
            )

        coefficient = _fraction(raw_coefficient)

        coefficients[index] = (
            coefficients.get(index, Fraction(0))
            + coefficient
        )

    return tuple(
        (index, coefficient)
        for index, coefficient in sorted(coefficients.items())
        if coefficient != 0
    )


def basis_vector(index: int) -> ExactVector:
    """Return one frozen basis vector."""
    return vector({index: 1})


def cartan_vector(simple_index: int) -> ExactVector:
    """Return h_(simple_index+1), using zero-based Python indexing."""
    if not 0 <= simple_index < ROOT_BASIS_OFFSET:
        raise ValueError("Cartan index must be in 0..7")

    return basis_vector(simple_index)


def root_vector(root_index: int) -> ExactVector:
    """Return the frozen root vector e_alpha at zero-based root index."""
    if not 0 <= root_index < 240:
        raise ValueError("Root index must be in 0..239")

    return basis_vector(ROOT_BASIS_OFFSET + root_index)


def scale(
    scalar: int | Fraction,
    value: ExactVector,
) -> ExactVector:
    """Scale one exact sparse vector."""
    factor = _fraction(scalar)

    return vector(
        (
            index,
            factor * coefficient,
        )
        for index, coefficient in value
    )


def add(
    *values: ExactVector,
) -> ExactVector:
    """Add exact sparse vectors."""
    return vector(
        item
        for value in values
        for item in value
    )


@lru_cache(maxsize=1)
def frozen_roots() -> tuple[DoubledRoot, ...]:
    """Return the frozen lexicographic E8 roots."""
    return tuple(generate_e8_roots())


@lru_cache(maxsize=1)
def _phase3d_tensor_map() -> dict[tuple[int, int, int], int]:
    """Load and integrity-check the sealed Phase 3D tensor."""
    observed = sha256_file(PHASE3D_JSON)

    if observed != PHASE3D_SHA256:
        raise ValueError(
            "Sealed Phase 3D tensor SHA-256 mismatch: "
            f"observed={observed}, expected={PHASE3D_SHA256}"
        )

    form = load_sparse_cartan_form(PHASE3D_JSON)

    result = {
        entry.key: entry.coefficient
        for entry in form.entries
    }

    if len(result) != 16176:
        raise ValueError(
            f"Expected 16176 sealed tensor entries, got {len(result)}"
        )

    return result


@lru_cache(maxsize=1)
def _phase3d_tensor_slices(
) -> dict[tuple[int, int], ExactVector]:
    """Return covector coefficients g(B_i,B_j,B_k) grouped by (j,k)."""
    slices: dict[
        tuple[int, int],
        list[tuple[int, int]],
    ] = {}

    for (first, second, third), coefficient in _phase3d_tensor_map().items():
        slices.setdefault(
            (second, third),
            [],
        ).append(
            (
                first,
                coefficient,
            )
        )

    return {
        key: vector(values)
        for key, values in slices.items()
    }


@lru_cache(maxsize=1)
def _bracket_table(
) -> tuple[tuple[IntegerSparseVector, ...], ...]:
    """Independent Phase 4A basis bracket."""
    return build_basis_bracket_table(
        frozen_roots()
    )


@lru_cache(maxsize=1)
def _bilinear_table(
) -> tuple[tuple[int, ...], ...]:
    """Independent normalized B0 table."""
    return build_bilinear_table(
        frozen_roots()
    )


def bracket(
    left: ExactVector,
    right: ExactVector,
) -> ExactVector:
    """Evaluate the frozen E8 Lie bracket by exact bilinear extension."""
    table = _bracket_table()

    output: list[
        tuple[int, Fraction]
    ] = []

    for left_index, left_coefficient in left:
        for right_index, right_coefficient in right:
            factor = left_coefficient * right_coefficient

            for output_index, bracket_coefficient in table[
                left_index
            ][
                right_index
            ]:
                output.append(
                    (
                        output_index,
                        factor * bracket_coefficient,
                    )
                )

    return vector(output)


def B0(
    left: ExactVector,
    right: ExactVector,
) -> Fraction:
    """Evaluate the frozen normalized invariant bilinear form exactly."""
    table = _bilinear_table()

    total = Fraction(0)

    for left_index, left_coefficient in left:
        for right_index, right_coefficient in right:
            value = table[
                left_index
            ][
                right_index
            ]

            if value:
                total += (
                    left_coefficient
                    * right_coefficient
                    * value
                )

    return total


def g_from_algebra(
    v1: ExactVector,
    v2: ExactVector,
    v3: ExactVector,
) -> Fraction:
    """Evaluate g(v1,v2,v3)=B0(v1,[v2,v3]) without Phase 3D tensor use."""
    return B0(
        v1,
        bracket(v2, v3),
    )


def g_from_tensor(
    v1: ExactVector,
    v2: ExactVector,
    v3: ExactVector,
) -> Fraction:
    """Evaluate the literal g by exact sparse tensor contraction."""
    tensor = _phase3d_tensor_map()

    total = Fraction(0)

    for first, coefficient1 in v1:
        for second, coefficient2 in v2:
            for third, coefficient3 in v3:
                coefficient = tensor.get(
                    (
                        first,
                        second,
                        third,
                    )
                )

                if coefficient is not None:
                    total += (
                        coefficient1
                        * coefficient2
                        * coefficient3
                        * coefficient
                    )

    return total


def g(
    v1: ExactVector,
    v2: ExactVector,
    v3: ExactVector,
) -> Fraction:
    """Literal executable normalized E8 Cartan 3-form."""
    return g_from_tensor(
        v1,
        v2,
        v3,
    )


def _invert_exact_matrix(
    matrix: tuple[tuple[int, ...], ...],
) -> tuple[tuple[Fraction, ...], ...]:
    """Exact Gauss-Jordan matrix inverse."""
    size = len(matrix)

    augmented = [
        [
            Fraction(value)
            for value in row
        ]
        + [
            Fraction(
                1 if row_index == column_index else 0
            )
            for column_index in range(size)
        ]
        for row_index, row in enumerate(matrix)
    ]

    for column in range(size):
        pivot_row = next(
            (
                row
                for row in range(column, size)
                if augmented[row][column] != 0
            ),
            None,
        )

        if pivot_row is None:
            raise ValueError("Singular matrix")

        if pivot_row != column:
            augmented[column], augmented[pivot_row] = (
                augmented[pivot_row],
                augmented[column],
            )

        pivot = augmented[column][column]

        augmented[column] = [
            value / pivot
            for value in augmented[column]
        ]

        for row in range(size):
            if row == column:
                continue

            factor = augmented[row][column]

            if factor == 0:
                continue

            augmented[row] = [
                left - factor * right
                for left, right in zip(
                    augmented[row],
                    augmented[column],
                    strict=True,
                )
            ]

    return tuple(
        tuple(
            row[size:]
        )
        for row in augmented
    )


@lru_cache(maxsize=1)
def _cartan_inverse(
) -> tuple[tuple[Fraction, ...], ...]:
    return _invert_exact_matrix(
        simple_root_gram_matrix()
    )


def B0_dual_vector(
    covector: ExactVector,
) -> ExactVector:
    """Raise the index of a covector using B0^{-1}.

    Input components are lambda_i = B0(B_i, w).
    Output is the unique vector w.
    """
    components = dict(covector)
    output: list[
        tuple[int, Fraction]
    ] = []

    # Cartan block:
    # lambda_i = A_ij w^j.
    cartan_covector = tuple(
        components.get(
            index,
            Fraction(0),
        )
        for index in range(ROOT_BASIS_OFFSET)
    )

    inverse = _cartan_inverse()

    for column in range(ROOT_BASIS_OFFSET):
        coefficient = sum(
            inverse[column][row]
            * cartan_covector[row]
            for row in range(ROOT_BASIS_OFFSET)
        )

        if coefficient != 0:
            output.append(
                (
                    column,
                    coefficient,
                )
            )

    # Root block:
    # B0(e_alpha, e_-alpha) = s_alpha = +/-1.
    roots = frozen_roots()
    opposite = opposite_index_map(roots)
    bilinear = _bilinear_table()

    for alpha_index in range(len(roots)):
        alpha_basis = ROOT_BASIS_OFFSET + alpha_index

        lambda_alpha = components.get(
            alpha_basis,
            Fraction(0),
        )

        if lambda_alpha == 0:
            continue

        negative_index = opposite[alpha_index]
        negative_basis = ROOT_BASIS_OFFSET + negative_index

        pairing = bilinear[
            alpha_basis
        ][
            negative_basis
        ]

        if pairing not in (-1, 1):
            raise ValueError(
                "Unexpected opposite-root B0 pairing"
            )

        output.append(
            (
                negative_basis,
                lambda_alpha / pairing,
            )
        )

    return vector(output)


def recover_bracket_from_g_basis_pair(
    second: int,
    third: int,
) -> ExactVector:
    """Recover [B_second,B_third] from g(.,B_second,B_third) and B0^{-1}."""
    if not 0 <= second < BASIS_DIMENSION:
        raise ValueError("Invalid second basis index")

    if not 0 <= third < BASIS_DIMENSION:
        raise ValueError("Invalid third basis index")

    covector = _phase3d_tensor_slices().get(
        (
            second,
            third,
        ),
        (),
    )

    return B0_dual_vector(
        covector
    )


def exact_integer_bracket_as_vector(
    second: int,
    third: int,
) -> ExactVector:
    """Return the independent Phase 4A basis bracket as an ExactVector."""
    return vector(
        _bracket_table()[
            second
        ][
            third
        ]
    )


def complete_bracket_recovery_discrepancies(
) -> tuple[
    set[tuple[int, int]],
    set[tuple[int, int]],
    dict[tuple[int, int], tuple[ExactVector, ExactVector]],
]:
    """Compare g/B0-recovered and independent brackets for all 248^2 pairs."""
    recovered_nonzero: set[
        tuple[int, int]
    ] = set()

    frozen_nonzero: set[
        tuple[int, int]
    ] = set()

    differing: dict[
        tuple[int, int],
        tuple[ExactVector, ExactVector],
    ] = {}

    for second in range(BASIS_DIMENSION):
        for third in range(BASIS_DIMENSION):
            recovered = recover_bracket_from_g_basis_pair(
                second,
                third,
            )

            frozen = exact_integer_bracket_as_vector(
                second,
                third,
            )

            key = (
                second,
                third,
            )

            if recovered:
                recovered_nonzero.add(key)

            if frozen:
                frozen_nonzero.add(key)

            if recovered != frozen:
                differing[key] = (
                    recovered,
                    frozen,
                )

    return (
        recovered_nonzero - frozen_nonzero,
        frozen_nonzero - recovered_nonzero,
        differing,
    )
