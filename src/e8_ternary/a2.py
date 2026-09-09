"""Phase 2B quotient of E8 zero-sum triples into A2 root subsystems."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from typing import Iterable, TypeAlias

from e8_ternary.roots import DoubledRoot, doubled_dot, negate
from e8_ternary.ternary import RootTriple
from e8_ternary.validation import exact_rank, reflect_doubled


SixRootSubsystem: TypeAlias = tuple[int, int, int, int, int, int]


def _root_index_map(
    roots: tuple[DoubledRoot, ...],
) -> dict[DoubledRoot, int]:
    """Return exact root -> index lookup, rejecting duplicate roots."""
    lookup = {root: index for index, root in enumerate(roots)}

    if len(lookup) != len(roots):
        raise ValueError("Root collection contains duplicate vectors")

    return lookup


def opposite_triple(
    roots: tuple[DoubledRoot, ...],
    triple: RootTriple,
) -> RootTriple:
    """Return the canonical index triple of the three opposite roots."""
    lookup = _root_index_map(roots)

    indices = tuple(
        sorted(
            lookup[negate(roots[index])]
            for index in triple
        )
    )

    if len(indices) != 3:
        raise ValueError("Opposite triple does not contain three indices")

    return indices  # type: ignore[return-value]


def six_root_union(
    roots: tuple[DoubledRoot, ...],
    triple: RootTriple,
) -> tuple[int, ...]:
    """Return the canonical union of a triple with its opposite."""
    opposite = opposite_triple(roots, triple)
    return tuple(sorted(set(triple) | set(opposite)))


def group_by_six_root_subsystem(
    roots: tuple[DoubledRoot, ...],
    triples: Iterable[RootTriple],
) -> dict[SixRootSubsystem, tuple[RootTriple, ...]]:
    """Group zero-sum triples by their triple/opposite six-root union."""
    groups: defaultdict[
        tuple[int, ...],
        list[RootTriple],
    ] = defaultdict(list)

    for triple in triples:
        key = six_root_union(roots, triple)
        groups[key].append(triple)

    result: dict[SixRootSubsystem, tuple[RootTriple, ...]] = {}

    for key in sorted(groups):
        if len(key) != 6:
            # Preserve the observed object faithfully: a malformed union is
            # not silently repaired into a six-root subsystem.
            continue

        result[key] = tuple(sorted(groups[key]))  # type: ignore[index]

    return result


def quotient_multiplicity_spectrum(
    groups: dict[SixRootSubsystem, tuple[RootTriple, ...]],
) -> dict[int, int]:
    """Return class size -> number of quotient classes."""
    return dict(
        sorted(
            Counter(
                len(members)
                for members in groups.values()
            ).items()
        )
    )


def six_root_size_spectrum(
    roots: tuple[DoubledRoot, ...],
    triples: Iterable[RootTriple],
) -> dict[int, int]:
    """Return observed size spectrum of triple/opposite unions."""
    return dict(
        sorted(
            Counter(
                len(six_root_union(roots, triple))
                for triple in triples
            ).items()
        )
    )


def subsystem_roots(
    roots: tuple[DoubledRoot, ...],
    subsystem: SixRootSubsystem,
) -> tuple[DoubledRoot, ...]:
    """Resolve a subsystem index tuple to its six root vectors."""
    return tuple(roots[index] for index in subsystem)


def subsystem_rank(
    roots: tuple[DoubledRoot, ...],
    subsystem: SixRootSubsystem,
) -> int:
    """Return exact rational rank of a six-root subsystem."""
    return exact_rank(subsystem_roots(roots, subsystem))


def subsystem_pairwise_doubled_dot_spectrum(
    roots: tuple[DoubledRoot, ...],
    subsystem: SixRootSubsystem,
) -> dict[int, int]:
    """Return unordered distinct-pair doubled-dot spectrum."""
    selected = subsystem_roots(roots, subsystem)

    counts: Counter[int] = Counter(
        doubled_dot(left, right)
        for left, right in combinations(selected, 2)
    )

    return dict(sorted(counts.items()))


def subsystem_reflection_closed(
    roots: tuple[DoubledRoot, ...],
    subsystem: SixRootSubsystem,
) -> bool:
    """Return True iff all root reflections remain in the subsystem."""
    selected = subsystem_roots(roots, subsystem)
    selected_set = set(selected)

    return all(
        reflect_doubled(beta, alpha) in selected_set
        for alpha in selected
        for beta in selected
    )


def quotient_class_is_opposite_pair(
    roots: tuple[DoubledRoot, ...],
    members: tuple[RootTriple, ...],
) -> bool:
    """Check that a two-member quotient class is exactly {tau, -tau}."""
    if len(members) != 2:
        return False

    first, second = members

    return (
        opposite_triple(roots, first) == second
        and opposite_triple(roots, second) == first
    )


def subsystem_has_a2_structure(
    roots: tuple[DoubledRoot, ...],
    subsystem: SixRootSubsystem,
) -> bool:
    """Check finite structural criteria identifying an A2 root system.

    In doubled coordinates an A2 six-root set has unordered distinct-pair
    spectrum

        -8 : 3
        -4 : 6
         4 : 6

    corresponding to ordinary inner products

        -2 : 3
        -1 : 6
         1 : 6.
    """
    return (
        len(subsystem) == 6
        and subsystem_rank(roots, subsystem) == 2
        and subsystem_reflection_closed(roots, subsystem)
        and subsystem_pairwise_doubled_dot_spectrum(
            roots,
            subsystem,
        )
        == {
            -8: 3,
            -4: 6,
            4: 6,
        }
    )
