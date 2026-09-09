# Phase 3A Root-Space Cartan 3-Form Support Closeout

## Status

STATUS: PHASE3A_ROOT_SPACE_CARTAN_SUPPORT_PASS

## Frozen protocol

Phase 3A protocol was frozen at commit:

    8d15bda

Phase 2C unsigned ternary incidence was completed at:

    c8dfd1c

No Chevalley signs, structure constants, Cartan-root-root coefficient tables,
or full 248-dimensional Cartan 3-form representation were constructed before
this closeout.

## Purpose

Phase 3A tested whether the unsigned Phase 2C ternary support

\[
T_{ijk}
\]

coincides exactly with the support of the Cartan 3-form

\[
\Omega(X,Y,Z)=B(X,[Y,Z])
\]

when all three arguments are nonzero E8 root-space vectors.

The Lie-algebraic support was derived independently from:

- root-space grading;
- bracket support;
- Cartan-valued opposite-root brackets;
- invariant-form orthogonality;
- nondegenerate opposite-root pairing.

The Phase 2C tensor was not used to classify Lie-algebra support.

## Root-space domain

The E8 root system contains

\[
240
\]

nonzero roots.

The complete ordered root-space triple domain therefore contains

\[
240^3
=
13{,}824{,}000
\]

positions.

Observed:

    complete ordered root^3 domain: 13824000

## Lie-algebraic support result

The independently derived nonzero root-root-root support contained:

\[
13{,}440
\]

ordered positions.

Observed:

    nonzero root-root-root support: 13440

Forced-zero positions:

\[
13{,}824{,}000-13{,}440
=
13{,}810{,}560.
\]

Observed:

    forced-zero positions: 13810560

Support density:

\[
\frac{13{,}440}{13{,}824{,}000}
=
0.000972222222\ldots
\]

Observed:

    support density: 0.000972222222

## Lie-rule classification census

Every ordered root triple was classified into exactly one of four
Lie-theoretic support classes.

Observed:

    ROOT_SUPPORT_NONZERO: 13440
    FORCED_ZERO_BRACKET: 10540800
    FORCED_ZERO_CARTAN_BRACKET: 57600
    FORCED_ZERO_PAIRING: 3212160

The census total was:

\[
13{,}440
+
10{,}540{,}800
+
57{,}600
+
3{,}212{,}160
=
13{,}824{,}000.
\]

Observed:

    census total: 13824000

Thus the complete ordered root-space domain was accounted for exactly.

## Classification interpretation

### ROOT_SUPPORT_NONZERO

These are the ordered triples for which

\[
\beta+\gamma
\]

is a root and satisfies

\[
\alpha=-(\beta+\gamma).
\]

Equivalently,

\[
\alpha+\beta+\gamma=0.
\]

Observed count:

\[
13{,}440.
\]

### FORCED_ZERO_BRACKET

These are triples for which

\[
\beta+\gamma
\]

is neither a root nor zero.

Then

\[
[E_\beta,E_\gamma]=0,
\]

forcing

\[
\Omega(E_\alpha,E_\beta,E_\gamma)=0.
\]

Observed count:

\[
10{,}540{,}800.
\]

### FORCED_ZERO_CARTAN_BRACKET

These arise when

\[
\gamma=-\beta.
\]

Then

\[
[E_\beta,E_{-\beta}]
\in\mathfrak h.
\]

Since root spaces are orthogonal to the Cartan subalgebra,

\[
B(E_\alpha,\mathfrak h)=0.
\]

Observed count:

\[
57{,}600.
\]

### FORCED_ZERO_PAIRING

These arise when

\[
\beta+\gamma
\]

is a nonzero root but

\[
\alpha\ne-(\beta+\gamma).
\]

The bracket is nonzero but lies in a root space orthogonal to

\[
\mathfrak g_\alpha.
\]

Observed count:

\[
3{,}212{,}160.
\]

## Root-space support theorem

The computation and algebraic derivation establish:

\[
\boxed{
\Omega(E_\alpha,E_\beta,E_\gamma)\neq0
\iff
\alpha+\beta+\gamma=0
}
\]

for nonzero root vectors

\[
E_\alpha\in\mathfrak g_\alpha,
\quad
E_\beta\in\mathfrak g_\beta,
\quad
E_\gamma\in\mathfrak g_\gamma.
\]

This is a support statement.

It does not assign a numerical value or sign to the nonzero coefficient.

## Support symmetry

The set of nonzero support positions is invariant under all permutations of
the three root indices.

Observed:

    S3-symmetric support positions: True

This is symmetry of the SUPPORT SET.

It does not mean that the Cartan 3-form coefficients are symmetric.

Once signs and normalization are fixed,

\[
\Omega
\]

is alternating.

## Distinct-index property

Every nonzero root-root-root support position contains three distinct roots.

Observed:

    all support indices distinct: True

Thus no repeated-index root-space component belongs to the nonzero
root-root-root sector.

## Exact comparison with Phase 2C

The Lie-derived root-space support was constructed independently before the
Phase 2C Boolean support was introduced for comparison.

Observed:

    Lie-derived support: 13440
    Phase 2C support: 13440
    Lie-only entries: 0
    Phase2C-only entries: 0
    exact support equality: True

Therefore

\[
\boxed{
S_\Omega=S_T.
}
\]

Equivalently,

\[
\boxed{
T_{ijk}=1
\iff
\Omega(
E_{\alpha_i},
E_{\alpha_j},
E_{\alpha_k}
)\neq0
}
\]

for the root-root-root sector.

## Structural consequence

The unsigned Phase 2C ternary incidence object is therefore exactly the
support skeleton of the root-root-root restriction of the canonical Cartan
3-form on

\[
\mathfrak e_8.
\]

Schematically,

\[
\boxed{
\alpha+\beta+\gamma=0
\iff
T_{\alpha\beta\gamma}=1
\iff
\Omega(E_\alpha,E_\beta,E_\gamma)\neq0.
}
\]

This identifies the finite 240-root ternary hypergraph with a precise
Lie-algebraic support structure.

## Full 248-dimensional boundary

The full Lie algebra decomposes as

\[
\mathfrak e_8
=
\mathfrak h
\oplus
\bigoplus_{\alpha\in\Phi}
\mathfrak g_\alpha,
\]

with

\[
\dim\mathfrak h=8
\]

and

\[
240
\]

one-dimensional root spaces.

The Phase 2C Boolean tensor describes only the root-root-root sector.

The full Cartan 3-form also contains potentially nonzero components of type

\[
\Omega(H,E_\alpha,E_{-\alpha}).
\]

Therefore:

\[
\operatorname{supp}
\left(
\Omega|_{\mathrm{root}^3}
\right)
=
\operatorname{supp}T
\]

is established.

The stronger statement

\[
\operatorname{supp}\Omega
=
\operatorname{supp}T
\]

is NOT made.

## Test state

The complete repository test suite after Phase 3A implementation reported:

    51 passed in 65.37s

## Phase 3A conclusion

PHASE3A_ROOT_SPACE_CARTAN_SUPPORT: PASS

The root-root-root support of the canonical E8 Cartan 3-form is exactly the
Phase 2C zero-sum ternary support.

The equality holds with:

\[
13{,}440
\]

nonzero ordered support positions and zero discrepancies in either direction.

## Interpretation boundary

Phase 3A establishes a canonical Lie-algebraic interpretation of the
Phase 2C support.

It does NOT yet establish:

- numerical Cartan 3-form coefficients;
- Chevalley basis signs;
- structure-constant normalization;
- the full 248-dimensional support;
- a generalized metric interpretation of
  \[
  g(v_1,v_2,v_3);
  \]
- novelty of the support theorem;
- any causal claim about the initiating dream.

## Next phase

The next Lie-algebraic phase should determine the full support architecture of

\[
\Omega
\]

on

\[
\mathfrak e_8
=
\mathfrak h
\oplus
\bigoplus_\alpha\mathfrak g_\alpha.
\]

A natural next step is to classify all basis-sector types:

1. root-root-root;
2. Cartan-root-root;
3. Cartan-Cartan-root;
4. Cartan-Cartan-Cartan.

That analysis can establish the complete 248-dimensional support skeleton
before any signs or numerical structure constants are introduced.
