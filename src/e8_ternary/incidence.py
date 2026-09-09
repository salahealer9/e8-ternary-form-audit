"""Phase 2C unsigned ternary incidence structures on E8 roots.

This module constructs:

1. the unordered 3-uniform zero-sum hypergraph;
2. the symmetric Boolean ordered support T_ijk;
3. the action of global root negation on hyperedges.

No Lie-algebra signs or Cartan-form coefficients are introduced here.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import combinations, permutations
from typing import Iterable, TypeAlias

from e8_ternary.roots import DoubledRoot, doubled_dot, negate
from e8_ternary.ternary import RootTriple


OrderedSupportEntry: TypeAlias = tuple[int, int, int]
NegationOrbit: TypeAlias = tuple[RootTriple, RootTriple]


@dataclass(frozen=True)
class TernaryIncidence:
    """Sparse unsigned ternary incidence object."""

    vertex_count: int
    hyperedges: tuple[RootTriple, ...]
    ordered_support: tuple[OrderedSupportEntry, ...]


def ordered_support_from_hyperedges(
    hyperedges: Iterable[RootTriple],
) -> tuple[OrderedSupportEntry, ...]:
    """Expand each unordered hyperedge into all six ordered permutations."""
    support: list[OrderedSupportEntry] = []

    for edge in hyperedges:
        support.extend(permutations(edge, 3))

    return tuple(sorted(support))


def build_ternary_incidence(
    root_count: int,
    hyperedges: Iterable[RootTriple],
) -> TernaryIncidence:
    """Construct the sparse hypergraph and symmetric Boolean support."""
    edges = tuple(sorted(hyperedges))

    return TernaryIncidence(
        vertex_count=root_count,
        hyperedges=edges,
        ordered_support=ordered_support_from_hyperedges(edges),
    )


def vertex_degrees(
    incidence: TernaryIncidence,
) -> tuple[int, ...]:
    """Return unordered-hypergraph degree of every vertex."""
    counts = [0] * incidence.vertex_count

    for i, j, k in incidence.hyperedges:
        counts[i] += 1
        counts[j] += 1
        counts[k] += 1

    return tuple(counts)


def vertex_degree_spectrum(
    incidence: TernaryIncidence,
) -> dict[int, int]:
    """Return degree -> number of vertices."""
    return dict(sorted(Counter(vertex_degrees(incidence)).items()))


def pair_codegrees(
    incidence: TernaryIncidence,
) -> dict[tuple[int, int], int]:
    """Return codegree for every unordered pair of distinct vertices."""
    counts = {
        pair: 0
        for pair in combinations(range(incidence.vertex_count), 2)
    }

    for edge in incidence.hyperedges:
        for pair in combinations(edge, 2):
            counts[pair] += 1

    return counts


def pair_codegree_spectrum(
    incidence: TernaryIncidence,
) -> dict[int, int]:
    """Return codegree -> number of unordered vertex pairs."""
    return dict(
        sorted(
            Counter(pair_codegrees(incidence).values()).items()
        )
    )


def active_pair_count(
    incidence: TernaryIncidence,
) -> int:
    """Return number of unordered pairs with positive hypergraph codegree."""
    return sum(
        codegree > 0
        for codegree in pair_codegrees(incidence).values()
    )


def active_pair_doubled_dot_spectrum(
    roots: tuple[DoubledRoot, ...],
    incidence: TernaryIncidence,
) -> dict[int, int]:
    """Characterize active pairs after the ternary support is constructed."""
    codegrees = pair_codegrees(incidence)

    counts: Counter[int] = Counter()

    for (i, j), codegree in codegrees.items():
        if codegree > 0:
            counts[doubled_dot(roots[i], roots[j])] += 1

    return dict(sorted(counts.items()))


def ordered_support_is_unique(
    incidence: TernaryIncidence,
) -> bool:
    """Return True iff sparse Boolean support contains no duplicates."""
    return (
        len(incidence.ordered_support)
        == len(set(incidence.ordered_support))
    )


def ordered_support_is_s3_symmetric(
    incidence: TernaryIncidence,
) -> bool:
    """Check closure of ordered support under all S3 permutations."""
    support = set(incidence.ordered_support)

    return all(
        permutation in support
        for entry in incidence.ordered_support
        for permutation in permutations(entry, 3)
    )


def ordered_support_has_zero_diagonals(
    incidence: TernaryIncidence,
) -> bool:
    """Check that every nonzero support entry has three distinct indices.

    Since the sparse representation lists exactly the entries where T_ijk=1,
    this is equivalent to all repeated-index tensor entries being zero.
    """
    return all(
        len({i, j, k}) == 3
        for i, j, k in incidence.ordered_support
    )


def negation_index_map(
    roots: tuple[DoubledRoot, ...],
) -> tuple[int, ...]:
    """Return nu(i), the index of the exact opposite root."""
    lookup = {root: index for index, root in enumerate(roots)}

    if len(lookup) != len(roots):
        raise ValueError("Root collection contains duplicates")

    return tuple(
        lookup[negate(root)]
        for root in roots
    )


def negate_hyperedge(
    edge: RootTriple,
    negation_map: tuple[int, ...],
) -> RootTriple:
    """Apply global root negation to an unordered hyperedge."""
    result = tuple(
        sorted(negation_map[index] for index in edge)
    )

    return result  # type: ignore[return-value]


def negation_orbits(
    incidence: TernaryIncidence,
    negation_map: tuple[int, ...],
) -> tuple[NegationOrbit, ...]:
    """Return canonical hyperedge orbits under global root negation."""
    edge_set = set(incidence.hyperedges)
    orbits: set[NegationOrbit] = set()

    for edge in incidence.hyperedges:
        opposite = negate_hyperedge(edge, negation_map)

        if opposite not in edge_set:
            raise ValueError(
                "Global negation maps a hyperedge outside the hypergraph"
            )

        orbit = tuple(sorted((edge, opposite)))
        orbits.add(orbit)  # type: ignore[arg-type]

    return tuple(sorted(orbits))


def negation_orbit_size_spectrum(
    incidence: TernaryIncidence,
    negation_map: tuple[int, ...],
) -> dict[int, int]:
    """Return orbit-size spectrum under global root negation."""
    return dict(
        sorted(
            Counter(
                len(set(orbit))
                for orbit in negation_orbits(
                    incidence,
                    negation_map,
                )
            ).items()
        )
    )


def negation_orbit_six_root_keys(
    incidence: TernaryIncidence,
    negation_map: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    """Return canonical six-root unions represented by negation orbits."""
    keys = []

    for first, second in negation_orbits(
        incidence,
        negation_map,
    ):
        keys.append(
            tuple(sorted(set(first) | set(second)))
        )

    return tuple(sorted(keys))
