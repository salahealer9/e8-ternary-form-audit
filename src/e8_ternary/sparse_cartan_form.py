"""Phase 3D signed sparse Cartan 3-form on the frozen E8 basis.

Primary construction:
    direct ordered evaluation from Lie-algebra bracket/pairing rules.

Secondary construction:
    canonical unordered nonzero triples followed by alternating expansion.

The two routes are intentionally distinct and must agree exactly.
"""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from itertools import permutations
from pathlib import Path
from typing import Iterable

from e8_ternary.canonical_basis import (
    StructureConstantEntry,
    cartan_root_value,
    derive_epsilon,
    normalized_opposite_root_pairing,
    simple_root_gram_matrix,
    structure_constant_table,
)
from e8_ternary.full_sector import (
    opposite_index_map,
    opposite_root_lines,
)
from e8_ternary.roots import DoubledRoot
from e8_ternary.ternary import enumerate_zero_sum_triples


CARTAN_DIMENSION = 8
ROOT_DIMENSION = 240
BASIS_DIMENSION = 248
ROOT_BASIS_OFFSET = 8
TOTAL_ORDERED_DOMAIN = BASIS_DIMENSION**3


class SparseSector(str, Enum):
    RRR = "RRR"
    HRR = "HRR"


@dataclass(frozen=True, order=True)
class SparseCartanEntry:
    """One nonzero ordered Cartan 3-form coefficient."""

    first: int
    second: int
    third: int
    coefficient: int
    sector: SparseSector

    @property
    def key(self) -> tuple[int, int, int]:
        return (self.first, self.second, self.third)


@dataclass(frozen=True)
class SparseCartanForm:
    """Sparse scalar representation of Omega_0."""

    basis_dimension: int
    entries: tuple[SparseCartanEntry, ...]

    @property
    def nonzero_count(self) -> int:
        return len(self.entries)

    @property
    def support_density(self) -> float:
        return self.nonzero_count / (self.basis_dimension**3)


@lru_cache(maxsize=2)
def _cached_structure_table(
    roots: tuple[DoubledRoot, ...],
) -> tuple[StructureConstantEntry, ...]:
    return structure_constant_table(roots)


@lru_cache(maxsize=2)
def _cached_pairings(
    roots: tuple[DoubledRoot, ...],
) -> tuple[int, ...]:
    return tuple(
        normalized_opposite_root_pairing(root)
        for root in roots
    )


@lru_cache(maxsize=2)
def _cached_zero_sum_triples(
    roots: tuple[DoubledRoot, ...],
) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        enumerate_zero_sum_triples(roots).triples
    )


def _insert(
    target: dict[tuple[int, int, int], SparseCartanEntry],
    entry: SparseCartanEntry,
) -> None:
    """Insert one sparse entry, rejecting inconsistent collisions."""
    existing = target.get(entry.key)

    if existing is None:
        target[entry.key] = entry
        return

    if existing != entry:
        raise ValueError(
            "Conflicting sparse coefficients for basis triple "
            f"{entry.key}: {existing} versus {entry}"
        )


def entry_map(
    form: SparseCartanForm,
) -> dict[tuple[int, int, int], SparseCartanEntry]:
    """Return ordered basis triple -> sparse entry."""
    result = {
        entry.key: entry
        for entry in form.entries
    }

    if len(result) != len(form.entries):
        raise ValueError("Sparse form contains duplicate ordered keys")

    return result


def sector_counts(
    form: SparseCartanForm,
) -> dict[SparseSector, int]:
    """Return exact sparse count by sector."""
    return dict(
        sorted(
            Counter(
                entry.sector
                for entry in form.entries
            ).items(),
            key=lambda item: item[0].value,
        )
    )


def coefficient_spectrum(
    form: SparseCartanForm,
) -> dict[int, int]:
    """Return coefficient -> sparse-entry count."""
    return dict(
        sorted(
            Counter(
                entry.coefficient
                for entry in form.entries
            ).items()
        )
    )


def build_direct_sparse_cartan_form(
    roots: Iterable[DoubledRoot],
) -> SparseCartanForm:
    """Construct Omega_0 directly on all algebraically nonzero ordered slots.

    RRR entries are derived from ordered root brackets.

    HRR entries are evaluated separately for each Cartan placement and each
    ordered opposite-root orientation.

    No permutation expansion and no Phase 2C support lookup are used.
    """
    root_tuple = tuple(roots)

    if len(root_tuple) != ROOT_DIMENSION:
        raise ValueError(
            f"Expected {ROOT_DIMENSION} roots, got {len(root_tuple)}"
        )

    opposite = opposite_index_map(root_tuple)
    pairings = _cached_pairings(root_tuple)
    table = _cached_structure_table(root_tuple)

    sparse: dict[
        tuple[int, int, int],
        SparseCartanEntry,
    ] = {}

    # ---------------------------------------------------------------
    # RRR: primary direct ordered construction.
    #
    # Structure table entry:
    #     [e_beta, e_gamma] = N_{beta,gamma} e_{beta+gamma}
    #
    # alpha = -(beta + gamma), hence
    #
    #     Omega(e_alpha,e_beta,e_gamma)
    #       = N_{beta,gamma} B0(e_alpha,e_-alpha).
    # ---------------------------------------------------------------
    for bracket in table:
        alpha_index = opposite[bracket.sum_index]
        beta_index = bracket.alpha_index
        gamma_index = bracket.beta_index

        coefficient = (
            bracket.coefficient
            * pairings[alpha_index]
        )

        _insert(
            sparse,
            SparseCartanEntry(
                first=ROOT_BASIS_OFFSET + alpha_index,
                second=ROOT_BASIS_OFFSET + beta_index,
                third=ROOT_BASIS_OFFSET + gamma_index,
                coefficient=coefficient,
                sector=SparseSector.RRR,
            ),
        )

    # ---------------------------------------------------------------
    # HRR: primary direct ordered construction.
    #
    # For each oriented opposite-root pair (alpha,-alpha):
    #
    # Omega(h_i,e_alpha,e_-alpha) = +s_alpha alpha(h_i)
    # Omega(e_alpha,h_i,e_-alpha) = -s_alpha alpha(h_i)
    # Omega(e_alpha,e_-alpha,h_i) = +s_alpha alpha(h_i)
    #
    # Iterating alpha over all 240 roots independently supplies the
    # reverse root ordering without using permutation expansion.
    # ---------------------------------------------------------------
    for simple_index in range(CARTAN_DIMENSION):
        for alpha_index, alpha in enumerate(root_tuple):
            alpha_hi = cartan_root_value(
                simple_index,
                alpha,
            )

            if alpha_hi == 0:
                continue

            negative_index = opposite[alpha_index]
            signed_value = (
                pairings[alpha_index]
                * alpha_hi
            )

            alpha_basis = (
                ROOT_BASIS_OFFSET + alpha_index
            )
            negative_basis = (
                ROOT_BASIS_OFFSET + negative_index
            )

            _insert(
                sparse,
                SparseCartanEntry(
                    first=simple_index,
                    second=alpha_basis,
                    third=negative_basis,
                    coefficient=signed_value,
                    sector=SparseSector.HRR,
                ),
            )

            _insert(
                sparse,
                SparseCartanEntry(
                    first=alpha_basis,
                    second=simple_index,
                    third=negative_basis,
                    coefficient=-signed_value,
                    sector=SparseSector.HRR,
                ),
            )

            _insert(
                sparse,
                SparseCartanEntry(
                    first=alpha_basis,
                    second=negative_basis,
                    third=simple_index,
                    coefficient=signed_value,
                    sector=SparseSector.HRR,
                ),
            )

    return SparseCartanForm(
        basis_dimension=BASIS_DIMENSION,
        entries=tuple(
            sorted(
                sparse.values(),
                key=lambda entry: entry.key,
            )
        ),
    )


def permutation_sign(
    seed: tuple[int, int, int],
    permuted: tuple[int, int, int],
) -> int:
    """Return parity sign taking one distinct triple ordering to another."""
    if len(set(seed)) != 3:
        raise ValueError("Seed indices must be distinct")

    if sorted(seed) != sorted(permuted):
        raise ValueError(
            "Permutation does not contain the same three indices"
        )

    position = {
        value: index
        for index, value in enumerate(seed)
    }

    sequence = [
        position[value]
        for value in permuted
    ]

    inversions = sum(
        sequence[i] > sequence[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )

    return -1 if inversions % 2 else 1


def build_alternating_reconstruction(
    roots: Iterable[DoubledRoot],
) -> SparseCartanForm:
    """Independently reconstruct the sparse form by alternation.

    RRR starts from Phase 2A canonical unordered zero-sum triples.

    HRR starts from canonical unordered opposite-root lines.

    Exactly one deterministic coefficient is evaluated for each unordered
    nonzero basis triple. The other five entries are generated only here by
    permutation parity.
    """
    root_tuple = tuple(roots)

    if len(root_tuple) != ROOT_DIMENSION:
        raise ValueError(
            f"Expected {ROOT_DIMENSION} roots, got {len(root_tuple)}"
        )

    pairings = _cached_pairings(root_tuple)
    table = _cached_structure_table(root_tuple)

    structure_lookup = {
        (
            entry.alpha_index,
            entry.beta_index,
        ): entry.coefficient
        for entry in table
    }

    sparse: dict[
        tuple[int, int, int],
        SparseCartanEntry,
    ] = {}

    # ---------------------------------------------------------------
    # RRR secondary route:
    # one canonical Phase 2A unordered triple i<j<k.
    # ---------------------------------------------------------------
    for alpha_index, beta_index, gamma_index in _cached_zero_sum_triples(
        root_tuple
    ):
        base_coefficient = (
            structure_lookup[
                (beta_index, gamma_index)
            ]
            * pairings[alpha_index]
        )

        seed = (
            ROOT_BASIS_OFFSET + alpha_index,
            ROOT_BASIS_OFFSET + beta_index,
            ROOT_BASIS_OFFSET + gamma_index,
        )

        for permuted in permutations(seed):
            permuted_tuple = tuple(permuted)

            _insert(
                sparse,
                SparseCartanEntry(
                    first=permuted_tuple[0],
                    second=permuted_tuple[1],
                    third=permuted_tuple[2],
                    coefficient=(
                        base_coefficient
                        * permutation_sign(
                            seed,
                            permuted_tuple,
                        )
                    ),
                    sector=SparseSector.RRR,
                ),
            )

    # ---------------------------------------------------------------
    # HRR secondary route:
    # one representative from each unordered opposite-root line.
    # ---------------------------------------------------------------
    for alpha_index, negative_index in opposite_root_lines(
        root_tuple
    ):
        alpha = root_tuple[alpha_index]

        for simple_index in range(CARTAN_DIMENSION):
            alpha_hi = cartan_root_value(
                simple_index,
                alpha,
            )

            if alpha_hi == 0:
                continue

            base_coefficient = (
                pairings[alpha_index]
                * alpha_hi
            )

            seed = (
                simple_index,
                ROOT_BASIS_OFFSET + alpha_index,
                ROOT_BASIS_OFFSET + negative_index,
            )

            for permuted in permutations(seed):
                permuted_tuple = tuple(permuted)

                _insert(
                    sparse,
                    SparseCartanEntry(
                        first=permuted_tuple[0],
                        second=permuted_tuple[1],
                        third=permuted_tuple[2],
                        coefficient=(
                            base_coefficient
                            * permutation_sign(
                                seed,
                                permuted_tuple,
                            )
                        ),
                        sector=SparseSector.HRR,
                    ),
                )

    return SparseCartanForm(
        basis_dimension=BASIS_DIMENSION,
        entries=tuple(
            sorted(
                sparse.values(),
                key=lambda entry: entry.key,
            )
        ),
    )


def sparse_form_discrepancies(
    direct: SparseCartanForm,
    reconstructed: SparseCartanForm,
) -> tuple[
    set[tuple[int, int, int]],
    set[tuple[int, int, int]],
    dict[
        tuple[int, int, int],
        tuple[SparseCartanEntry, SparseCartanEntry],
    ],
]:
    """Compare two sparse coefficient maps exactly."""
    direct_map = entry_map(direct)
    reconstructed_map = entry_map(reconstructed)

    direct_keys = set(direct_map)
    reconstructed_keys = set(reconstructed_map)

    direct_only = (
        direct_keys - reconstructed_keys
    )
    reconstructed_only = (
        reconstructed_keys - direct_keys
    )

    differing = {
        key: (
            direct_map[key],
            reconstructed_map[key],
        )
        for key in (
            direct_keys & reconstructed_keys
        )
        if direct_map[key] != reconstructed_map[key]
    }

    return (
        direct_only,
        reconstructed_only,
        differing,
    )


def all_indices_distinct(
    form: SparseCartanForm,
) -> bool:
    """Return True iff no stored coefficient has a repeated basis index."""
    return all(
        len(
            {
                entry.first,
                entry.second,
                entry.third,
            }
        )
        == 3
        for entry in form.entries
    )


def full_alternation_holds(
    form: SparseCartanForm,
) -> bool:
    """Check full S3 alternation of the completed primary sparse tensor."""
    lookup = entry_map(form)

    for entry in form.entries:
        seed = entry.key

        for permuted in permutations(seed):
            permuted_tuple = tuple(permuted)
            expected = (
                entry.coefficient
                * permutation_sign(
                    seed,
                    permuted_tuple,
                )
            )

            other = lookup.get(
                permuted_tuple
            )

            if other is None:
                return False

            if (
                other.coefficient != expected
                or other.sector != entry.sector
            ):
                return False

    return True


def rrr_cyclic_formula_consistency(
    roots: Iterable[DoubledRoot],
) -> bool:
    """Check the three cyclic RRR coefficient formulae directly."""
    root_tuple = tuple(roots)
    opposite = opposite_index_map(root_tuple)
    pairings = _cached_pairings(root_tuple)
    table = _cached_structure_table(root_tuple)

    lookup = {
        (
            entry.alpha_index,
            entry.beta_index,
        ): entry.coefficient
        for entry in table
    }

    for bracket in table:
        beta_index = bracket.alpha_index
        gamma_index = bracket.beta_index
        alpha_index = opposite[
            bracket.sum_index
        ]

        first = (
            lookup[(beta_index, gamma_index)]
            * pairings[alpha_index]
        )

        second = (
            lookup[(gamma_index, alpha_index)]
            * pairings[beta_index]
        )

        third = (
            lookup[(alpha_index, beta_index)]
            * pairings[gamma_index]
        )

        if not (
            first == second == third
        ):
            return False

    return True


def rrr_root_index_support(
    form: SparseCartanForm,
) -> set[tuple[int, int, int]]:
    """Return RRR support translated from basis indices to root indices."""
    return {
        (
            entry.first - ROOT_BASIS_OFFSET,
            entry.second - ROOT_BASIS_OFFSET,
            entry.third - ROOT_BASIS_OFFSET,
        )
        for entry in form.entries
        if entry.sector == SparseSector.RRR
    }


def hrr_entries_use_opposite_roots(
    form: SparseCartanForm,
    roots: Iterable[DoubledRoot],
) -> bool:
    """Check every HRR entry contains exactly one H and opposite roots."""
    root_tuple = tuple(roots)
    opposite = opposite_index_map(root_tuple)

    for entry in form.entries:
        if entry.sector != SparseSector.HRR:
            continue

        indices = (
            entry.first,
            entry.second,
            entry.third,
        )

        cartan = [
            value
            for value in indices
            if value < ROOT_BASIS_OFFSET
        ]

        root_indices = [
            value - ROOT_BASIS_OFFSET
            for value in indices
            if value >= ROOT_BASIS_OFFSET
        ]

        if len(cartan) != 1:
            return False

        if len(root_indices) != 2:
            return False

        left, right = root_indices

        if opposite[left] != right:
            return False

    return True


def no_hhr_or_hhh_entries(
    form: SparseCartanForm,
) -> bool:
    """Check every sparse entry has at most one Cartan basis index."""
    return all(
        sum(
            index < ROOT_BASIS_OFFSET
            for index in entry.key
        )
        <= 1
        for entry in form.entries
    )


def export_sparse_cartan_form(
    path: str | Path,
    form: SparseCartanForm,
    roots: Iterable[DoubledRoot],
) -> Path:
    """Export deterministic Phase 3D sparse JSON artifact."""
    output = Path(path)
    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    root_tuple = tuple(roots)

    payload = {
        "schema": (
            "phase3d_signed_sparse_cartan_form.v1"
        ),
        "basis_dimension": form.basis_dimension,
        "cartan_dimension": CARTAN_DIMENSION,
        "root_dimension": len(root_tuple),
        "total_ordered_domain": (
            form.basis_dimension**3
        ),
        "nonzero_entry_count": (
            form.nonzero_count
        ),
        "support_density": (
            form.support_density
        ),
        "sector_counts": {
            sector.value: count
            for sector, count in sector_counts(
                form
            ).items()
        },
        "coefficient_spectrum": {
            str(value): count
            for value, count in coefficient_spectrum(
                form
            ).items()
        },
        "basis_ordering": {
            "cartan_indices": [0, 7],
            "cartan_labels": [
                f"h_{index}"
                for index in range(1, 9)
            ],
            "root_indices": [8, 247],
            "root_order": (
                "lexicographic doubled-root order"
            ),
            "root_vectors_doubled": [
                list(root)
                for root in root_tuple
            ],
        },
        "epsilon": list(
            derive_epsilon()
        ),
        "invariant_form_normalization": (
            "B0(h_i,h_j)=a_ij"
        ),
        "cartan_matrix": [
            list(row)
            for row in simple_root_gram_matrix()
        ],
        "entries": [
            {
                "first": entry.first,
                "second": entry.second,
                "third": entry.third,
                "coefficient": (
                    entry.coefficient
                ),
                "sector": (
                    entry.sector.value
                ),
            }
            for entry in form.entries
        ],
    }

    output.write_text(
        json.dumps(
            payload,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )

    return output


def load_sparse_cartan_form(
    path: str | Path,
) -> SparseCartanForm:
    """Load the deterministic Phase 3D JSON artifact."""
    payload = json.loads(
        Path(path).read_text()
    )

    if payload["schema"] != (
        "phase3d_signed_sparse_cartan_form.v1"
    ):
        raise ValueError(
            "Unexpected Phase 3D schema"
        )

    entries = tuple(
        SparseCartanEntry(
            first=item["first"],
            second=item["second"],
            third=item["third"],
            coefficient=item["coefficient"],
            sector=SparseSector(
                item["sector"]
            ),
        )
        for item in payload["entries"]
    )

    return SparseCartanForm(
        basis_dimension=payload[
            "basis_dimension"
        ],
        entries=entries,
    )
