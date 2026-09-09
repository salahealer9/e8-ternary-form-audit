"""Phase 1A tests for the exact E8 root construction."""

from e8_ternary.roots import (
    duplicate_count,
    generate_e8_roots,
    generate_half_integer_family,
    generate_integer_family,
    negative_closure,
    norm_spectrum,
    ordered_inner_product_spectrum,
)


def test_integer_family_replication_count() -> None:
    roots = generate_integer_family()

    # External replication benchmark.
    assert len(roots) == 112
    assert duplicate_count(roots) == 0


def test_half_integer_family_replication_count() -> None:
    roots = generate_half_integer_family()

    # External replication benchmark.
    assert len(roots) == 128
    assert duplicate_count(roots) == 0


def test_complete_root_count() -> None:
    roots = generate_e8_roots()

    # Frozen external benchmark.
    assert len(roots) == 240
    assert duplicate_count(roots) == 0


def test_every_root_has_squared_norm_two() -> None:
    roots = generate_e8_roots()

    # Doubled coordinates q = 2 alpha imply:
    #
    # alpha.alpha = 2
    #
    # iff
    #
    # q.q = 8.
    assert norm_spectrum(roots) == {8: 240}


def test_root_set_is_closed_under_negation() -> None:
    assert negative_closure(generate_e8_roots())


def test_distinct_root_inner_product_spectrum() -> None:
    roots = generate_e8_roots()
    spectrum = ordered_inner_product_spectrum(roots)

    # q.r values correspond to ordinary inner products after division by 4.
    #
    # {-8, -4, 0, 4}
    #
    # therefore corresponds to
    #
    # {-2, -1, 0, 1}.
    assert set(spectrum) == {-8, -4, 0, 4}


def test_frozen_minus_one_neighbour_benchmark() -> None:
    roots = generate_e8_roots()

    neighbour_counts = []

    for alpha in roots:
        count = sum(
            1
            for beta in roots
            if alpha != beta
            and sum(a * b for a, b in zip(alpha, beta, strict=True)) == -4
        )
        neighbour_counts.append(count)

    # Frozen external benchmark: every E8 root has exactly
    # 56 roots at ordinary inner product -1.
    assert set(neighbour_counts) == {56}
