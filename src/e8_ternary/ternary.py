"""Exact root-level ternary relations for E8.

Phase 2A begins with one relation only:

    alpha + beta + gamma = 0

The primary enumeration intentionally uses no inner-product prefilter,
neighbour table, A2 information, or Cartan-form data.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import combinations
from math import factorial
from typing import Iterable, TypeAlias

from e8_ternary.roots import DoubledRoot, doubled_dot


RootTriple: TypeAlias = tuple[int, int, int]


@dataclass(frozen=True)
class ZeroSumEnumeration:
    """Result of exhaustive unordered 3-subset enumeration."""

    candidate_count: int
    triples: tuple[RootTriple, ...]


def sums_to_zero(
    alpha: DoubledRoot,
    beta: DoubledRoot,
    gamma: DoubledRoot,
) -> bool:
    """Return True iff three doubled roots sum exactly to zero."""
    return all(
        a + b + c == 0
        for a, b, c in zip(alpha, beta, gamma, strict=True)
    )


def enumerate_zero_sum_triples(
    roots: Iterable[DoubledRoot],
) -> ZeroSumEnumeration:
    """Exhaustively enumerate unordered zero-sum root triples.

    Every index combination i < j < k is examined.

    Retention uses only the exact coordinate condition

        root[i] + root[j] + root[k] = 0.

    No expected result count is used.
    """
    root_tuple = tuple(roots)

    candidate_count = 0
    retained: list[RootTriple] = []

    for i, j, k in combinations(range(len(root_tuple)), 3):
        candidate_count += 1

        if sums_to_zero(
            root_tuple[i],
            root_tuple[j],
            root_tuple[k],
        ):
            retained.append((i, j, k))

    return ZeroSumEnumeration(
        candidate_count=candidate_count,
        triples=tuple(retained),
    )


def ordered_triple_count(
    triples: Iterable[RootTriple],
) -> int:
    """Return the number of orderings represented by distinct triples."""
    return factorial(3) * sum(1 for _ in triples)


def root_incidence_counts(
    root_count: int,
    triples: Iterable[RootTriple],
) -> tuple[int, ...]:
    """Count how many retained unordered triples contain each root."""
    counts = [0] * root_count

    for i, j, k in triples:
        counts[i] += 1
        counts[j] += 1
        counts[k] += 1

    return tuple(counts)


def pairwise_doubled_dot_signature(
    roots: tuple[DoubledRoot, ...],
    triple: RootTriple,
) -> tuple[int, int, int]:
    """Return sorted doubled-dot products for the three root pairs."""
    i, j, k = triple

    values = (
        doubled_dot(roots[i], roots[j]),
        doubled_dot(roots[j], roots[k]),
        doubled_dot(roots[k], roots[i]),
    )

    return tuple(sorted(values))


def triple_signature_spectrum(
    roots: tuple[DoubledRoot, ...],
    triples: Iterable[RootTriple],
) -> dict[tuple[int, int, int], int]:
    """Return the post-enumeration pairwise-dot signature spectrum."""
    counts: Counter[tuple[int, int, int]] = Counter(
        pairwise_doubled_dot_signature(roots, triple)
        for triple in triples
    )
    return dict(sorted(counts.items()))


def triples_are_canonical_and_distinct(
    triples: Iterable[RootTriple],
) -> bool:
    """Check that every triple has three strictly increasing indices."""
    return all(i < j < k for i, j, k in triples)


def triples_are_unique(
    triples: Iterable[RootTriple],
) -> bool:
    """Check that no unordered triple occurs more than once."""
    triple_tuple = tuple(triples)
    return len(triple_tuple) == len(set(triple_tuple))


def triples_all_sum_to_zero(
    roots: tuple[DoubledRoot, ...],
    triples: Iterable[RootTriple],
) -> bool:
    """Recheck the defining ternary relation independently."""
    return all(
        sums_to_zero(roots[i], roots[j], roots[k])
        for i, j, k in triples
    )


def triple_contains_opposite_pair(
    roots: tuple[DoubledRoot, ...],
    triple: RootTriple,
) -> bool:
    """Return True iff a retained triple contains an opposite root pair."""
    i, j, k = triple
    selected = (roots[i], roots[j], roots[k])

    for left, right in combinations(selected, 2):
        if all(
            a == -b
            for a, b in zip(left, right, strict=True)
        ):
            return True

    return False
