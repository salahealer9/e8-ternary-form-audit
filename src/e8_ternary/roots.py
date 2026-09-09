"""Exact coordinate construction of the E8 root system.

Canonical representation
------------------------
A root alpha is represented internally by its doubled coordinates

    q = 2 * alpha

so every coordinate is an integer.

This module constructs roots only from the defining coordinate rules.
External benchmark counts are not used by the generators.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from typing import Iterable, TypeAlias


DoubledRoot: TypeAlias = tuple[int, int, int, int, int, int, int, int]


def generate_integer_family() -> tuple[DoubledRoot, ...]:
    """Generate the integer-coordinate E8 root family.

    Ordinary coordinates are permutations of

        (+/-1, +/-1, 0, ..., 0).

    Doubled coordinates therefore contain two entries +/-2.
    """
    roots: list[DoubledRoot] = []

    for i, j in combinations(range(8), 2):
        for sign_i, sign_j in product((-2, 2), repeat=2):
            coordinates = [0] * 8
            coordinates[i] = sign_i
            coordinates[j] = sign_j
            roots.append(tuple(coordinates))  # type: ignore[arg-type]

    return tuple(roots)


def generate_half_integer_family() -> tuple[DoubledRoot, ...]:
    """Generate the half-integer-coordinate E8 root family.

    Ordinary coordinates have the form

        (1/2) * (s1, ..., s8),

    where each si is +/-1 and the number of negative signs is even.

    In doubled coordinates this is simply the sign vector itself.
    """
    roots: list[DoubledRoot] = []

    for signs in product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(signs)

    return tuple(roots)


def generate_e8_roots() -> tuple[DoubledRoot, ...]:
    """Generate the complete E8 root collection from both families.

    The output is sorted lexicographically to make downstream artifacts
    deterministic.

    Duplicate removal is by exact tuple identity only.
    """
    roots = set(generate_integer_family())
    roots.update(generate_half_integer_family())
    return tuple(sorted(roots))


def doubled_dot(left: DoubledRoot, right: DoubledRoot) -> int:
    """Return the dot product of doubled-coordinate vectors."""
    return sum(a * b for a, b in zip(left, right, strict=True))


def doubled_norm_squared(root: DoubledRoot) -> int:
    """Return q.q for q = 2 alpha.

    The ordinary squared norm is q.q / 4.
    """
    return doubled_dot(root, root)


def negate(root: DoubledRoot) -> DoubledRoot:
    """Return the exact negative of a doubled root."""
    return tuple(-coordinate for coordinate in root)  # type: ignore[return-value]


def norm_spectrum(
    roots: Iterable[DoubledRoot],
) -> dict[int, int]:
    """Return the spectrum of doubled squared norms.

    Keys are q.q, not ordinary alpha.alpha.
    """
    return dict(sorted(Counter(doubled_norm_squared(root) for root in roots).items()))


def ordered_inner_product_spectrum(
    roots: Iterable[DoubledRoot],
    *,
    include_self: bool = False,
) -> dict[int, int]:
    """Return the ordered pair spectrum of doubled inner products.

    Keys are q.r. Divide by 4 to obtain the ordinary E8 inner product.

    By default self-pairs are omitted.
    """
    root_tuple = tuple(roots)
    counts: Counter[int] = Counter()

    for i, left in enumerate(root_tuple):
        for j, right in enumerate(root_tuple):
            if not include_self and i == j:
                continue
            counts[doubled_dot(left, right)] += 1

    return dict(sorted(counts.items()))


def negative_closure(roots: Iterable[DoubledRoot]) -> bool:
    """Return True iff every root has its exact negative in the set."""
    root_set = set(roots)
    return all(negate(root) in root_set for root in root_set)


def duplicate_count(roots: Iterable[DoubledRoot]) -> int:
    """Return the number of repeated entries in a root collection."""
    root_tuple = tuple(roots)
    return len(root_tuple) - len(set(root_tuple))
