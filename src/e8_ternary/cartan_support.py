"""Phase 3A root-space support of the E8 Cartan 3-form.

For root vectors,

    Omega(E_alpha, E_beta, E_gamma)
        = B(E_alpha, [E_beta, E_gamma]).

This module classifies support using only:

- root-space bracket grading;
- the beta + gamma = 0 Cartan-bracket case;
- invariant-form pairing of opposite root spaces.

It does NOT import or consult the Phase 2C ternary incidence tensor.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from enum import Enum
from typing import Iterable, TypeAlias

from e8_ternary.roots import DoubledRoot, negate


OrderedRootTriple: TypeAlias = tuple[int, int, int]


class SupportClass(str, Enum):
    """Root-root-root Cartan 3-form support classification."""

    ROOT_SUPPORT_NONZERO = "ROOT_SUPPORT_NONZERO"
    FORCED_ZERO_BRACKET = "FORCED_ZERO_BRACKET"
    FORCED_ZERO_CARTAN_BRACKET = "FORCED_ZERO_CARTAN_BRACKET"
    FORCED_ZERO_PAIRING = "FORCED_ZERO_PAIRING"


@dataclass(frozen=True)
class RootSpaceCartanSupport:
    """Sparse ordered support derived from Lie-algebra rules."""

    root_count: int
    ordered_support: tuple[OrderedRootTriple, ...]

    @property
    def total_ordered_triples(self) -> int:
        return self.root_count**3

    @property
    def forced_zero_count(self) -> int:
        return self.total_ordered_triples - len(self.ordered_support)


def add_roots(
    left: DoubledRoot,
    right: DoubledRoot,
) -> DoubledRoot:
    """Return exact coordinate sum of two doubled roots."""
    return tuple(
        a + b
        for a, b in zip(left, right, strict=True)
    )  # type: ignore[return-value]


def is_zero_vector(vector: DoubledRoot) -> bool:
    """Return True iff every coordinate is zero."""
    return all(value == 0 for value in vector)


def root_lookup(
    roots: Iterable[DoubledRoot],
) -> dict[DoubledRoot, int]:
    """Construct exact root -> index lookup."""
    root_tuple = tuple(roots)
    lookup = {
        root: index
        for index, root in enumerate(root_tuple)
    }

    if len(lookup) != len(root_tuple):
        raise ValueError("Root collection contains duplicate roots")

    return lookup


def classify_root_triple(
    roots: tuple[DoubledRoot, ...],
    alpha_index: int,
    beta_index: int,
    gamma_index: int,
    *,
    lookup: dict[DoubledRoot, int] | None = None,
) -> SupportClass:
    """Classify one ordered root triple from Lie-algebra support rules.

    The cases are:

    1. beta + gamma = 0:
       [g_beta, g_gamma] lies in h, which is orthogonal to g_alpha.

    2. beta + gamma is not a root:
       the root-space bracket vanishes.

    3. beta + gamma is a root but is not -alpha:
       the bracket lies in a root space orthogonal to g_alpha.

    4. beta + gamma = -alpha:
       the root-space bracket is nonzero and opposite-root pairing is
       nondegenerate, so the Cartan 3-form is nonzero.
    """
    if lookup is None:
        lookup = root_lookup(roots)

    alpha = roots[alpha_index]
    beta = roots[beta_index]
    gamma = roots[gamma_index]

    beta_plus_gamma = add_roots(beta, gamma)

    if is_zero_vector(beta_plus_gamma):
        return SupportClass.FORCED_ZERO_CARTAN_BRACKET

    if beta_plus_gamma not in lookup:
        return SupportClass.FORCED_ZERO_BRACKET

    if alpha != negate(beta_plus_gamma):
        return SupportClass.FORCED_ZERO_PAIRING

    return SupportClass.ROOT_SUPPORT_NONZERO


def build_root_space_cartan_support(
    roots: Iterable[DoubledRoot],
) -> RootSpaceCartanSupport:
    """Construct ordered nonzero support from Lie-algebra grading rules.

    For each ordered pair (beta, gamma):

    - if beta + gamma is a nonzero root, the bracket lies nontrivially in
      g_{beta+gamma};
    - invariant-form pairing can then be nonzero only for the unique
      alpha = -(beta + gamma).

    This construction does not use Phase 2C support.
    """
    root_tuple = tuple(roots)
    lookup = root_lookup(root_tuple)

    support: list[OrderedRootTriple] = []

    for beta_index, beta in enumerate(root_tuple):
        for gamma_index, gamma in enumerate(root_tuple):
            beta_plus_gamma = add_roots(beta, gamma)

            if is_zero_vector(beta_plus_gamma):
                # Bracket lies in the Cartan subalgebra, hence root-root-root
                # Cartan 3-form support is zero.
                continue

            if beta_plus_gamma not in lookup:
                # Root-space bracket vanishes.
                continue

            alpha = negate(beta_plus_gamma)
            alpha_index = lookup.get(alpha)

            if alpha_index is None:
                # This should be impossible for a root system closed under
                # negation, but no external support assumption is made.
                continue

            support.append(
                (
                    alpha_index,
                    beta_index,
                    gamma_index,
                )
            )

    return RootSpaceCartanSupport(
        root_count=len(root_tuple),
        ordered_support=tuple(sorted(support)),
    )


def classification_census(
    roots: Iterable[DoubledRoot],
) -> dict[SupportClass, int]:
    """Classify the full ordered root^3 domain exactly.

    The census is derived efficiently from ordered (beta, gamma) bracket
    cases rather than performing 240 copies of identical root-space grading
    work unnecessarily.

    If beta + gamma is:

    - zero: all alpha choices are forced zero via Cartan orthogonality;
    - not a root: all alpha choices are forced zero via bracket vanishing;
    - a root: exactly one alpha gives nonzero opposite-root pairing, while
      all remaining alpha choices are forced zero by root-space orthogonality.
    """
    root_tuple = tuple(roots)
    lookup = root_lookup(root_tuple)
    n = len(root_tuple)

    counts: Counter[SupportClass] = Counter()

    for beta in root_tuple:
        for gamma in root_tuple:
            beta_plus_gamma = add_roots(beta, gamma)

            if is_zero_vector(beta_plus_gamma):
                counts[
                    SupportClass.FORCED_ZERO_CARTAN_BRACKET
                ] += n
                continue

            if beta_plus_gamma not in lookup:
                counts[
                    SupportClass.FORCED_ZERO_BRACKET
                ] += n
                continue

            alpha = negate(beta_plus_gamma)

            if alpha not in lookup:
                raise ValueError(
                    "Root sum is a root but its negative is missing"
                )

            counts[SupportClass.ROOT_SUPPORT_NONZERO] += 1
            counts[SupportClass.FORCED_ZERO_PAIRING] += n - 1

    return {
        support_class: counts[support_class]
        for support_class in SupportClass
    }


def support_is_s3_symmetric(
    support: Iterable[OrderedRootTriple],
) -> bool:
    """Check permutation symmetry of nonzero support positions."""
    from itertools import permutations

    support_set = set(support)

    return all(
        permutation in support_set
        for triple in support_set
        for permutation in permutations(triple, 3)
    )


def support_has_distinct_indices(
    support: Iterable[OrderedRootTriple],
) -> bool:
    """Check that every nonzero root-root-root support entry is off-diagonal."""
    return all(
        len({i, j, k}) == 3
        for i, j, k in support
    )
