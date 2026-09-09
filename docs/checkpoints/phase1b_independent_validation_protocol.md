# Phase 1B Independent E8 Validation Protocol

## Status

STATUS: PHASE1B_INDEPENDENT_VALIDATION_PROTOCOL_FROZEN

## Purpose

Independently validate the Phase 1A root set using a construction criterion
that does not reproduce the two-family generation algorithm.

Phase 1A was completed at commit:

    455bb57

Phase 1B precedes all zero-sum root-triple and A2-subsystem enumeration.

## Primary Phase 1A construction

Phase 1A constructed E8 roots as the union of:

1. permutations of
   \[
   (\pm1,\pm1,0,\ldots,0),
   \]

2. half-integer vectors
   \[
   \frac12(\pm1,\ldots,\pm1)
   \]
   satisfying the parity condition.

Phase 1B will not use those family-generation rules.

## Independent lattice criterion

Let

\[
q=2x\in\mathbb Z^8
\]

denote doubled coordinates.

The E8 lattice condition can be expressed as:

1. all eight coordinates of \(q\) have the same parity;
2. the coordinate sum satisfies
   \[
   \sum_i q_i\equiv0\pmod4.
   \]

Roots additionally satisfy

\[
x\cdot x=2.
\]

In doubled coordinates this becomes

\[
q\cdot q=8.
\]

Therefore the independent Phase 1B candidate set is

\[
\Phi_{\mathrm{lattice}}
=
\left\{
q\in\mathbb Z^8:
q\cdot q=8,\;
q_i\equiv q_j\pmod2\ \forall i,j,\;
\sum_i q_i\equiv0\pmod4
\right\}.
\]

## Enumeration rule

The independent validator will exhaustively enumerate all integer vectors

\[
q=(q_1,\ldots,q_8)
\]

within the coordinate bound implied by

\[
q\cdot q=8.
\]

Since any coordinate with

\[
|q_i|>2
\]

would already contribute more than 8 to the squared norm, it is sufficient to
enumerate

\[
q_i\in\{-2,-1,0,1,2\}.
\]

This bound is derived from the norm equation, not from an expected root count.

The validator will then apply only:

- exact squared norm 8;
- common coordinate parity;
- coordinate sum divisible by 4.

It will not classify candidates into the Phase 1A F1/F2 families during
generation.

## Primary comparison

Let

\[
\Phi_A
\]

be the Phase 1A generated root set and

\[
\Phi_B
\]

the independent lattice-derived set.

Phase 1B will compute exactly:

\[
\Phi_A\setminus\Phi_B,
\]

\[
\Phi_B\setminus\Phi_A,
\]

and test

\[
\Phi_A=\Phi_B.
\]

No approximate coordinate comparison is permitted.

## Additional structural checks

After independent set equality is tested, Phase 1B will verify the following
root-system properties.

### V1 — Rank

The generated roots must span an 8-dimensional real vector space.

The rank calculation must use exact arithmetic.

### V2 — Crystallographic integrality

For roots \(\alpha,\beta\),

\[
\frac{2(\alpha\cdot\beta)}
{\alpha\cdot\alpha}
\]

must be integral.

Since all roots have squared norm 2, this reduces to integrality of

\[
\alpha\cdot\beta.
\]

### V3 — Reflection closure

For every pair of roots \(\alpha,\beta\), compute

\[
s_\alpha(\beta)
=
\beta-
\frac{2(\alpha\cdot\beta)}
{\alpha\cdot\alpha}\alpha.
\]

With the selected normalization,

\[
s_\alpha(\beta)
=
\beta-(\alpha\cdot\beta)\alpha.
\]

Every reflected vector must belong to the generated root set.

The test must use exact doubled-coordinate arithmetic.

### V4 — Irreducibility connectivity check

Construct a graph whose vertices are the 240 roots and where two distinct
roots are connected when their inner product is nonzero and they are not
opposites.

The graph must be connected.

This is used as a finite check that the root structure does not split into
orthogonal components.

## Independence safeguards

The independent lattice enumeration must not:

- call `generate_integer_family()`;
- call `generate_half_integer_family()`;
- construct candidates using position-pair choices;
- construct candidates using sign-vector parity enumeration;
- stop after finding 240 roots;
- use 112 or 128 as control values;
- import a root table;
- use Phase 2 triple counts;
- repair discrepancies to force set equality.

The Phase 1A set may be loaded only after the independent Phase 1B set has
been completely generated.

## Frozen external values

The value

\[
240
\]

remains an external replication benchmark.

It may be reported after generation but must not terminate the enumeration.

No Phase 2 benchmark, including

\[
1120,
\]

is relevant to Phase 1B execution.

## Success criteria

Phase 1B is a PASS only if:

1. the independent lattice enumeration completes exhaustively;
2. the lattice-derived set equals the Phase 1A set exactly;
3. the exact root span has rank 8;
4. crystallographic integrality holds for every root pair;
5. every root reflection maps the root set to itself;
6. the nonorthogonality graph is connected.

Any discrepancy must be reported rather than repaired.

## Separation from ternary phase

Phase 1B does NOT enumerate:

\[
\alpha+\beta+\gamma=0.
\]

It does NOT enumerate A2 subsystems.

It does NOT define the ternary incidence tensor.

Those operations begin only after Phase 1B is frozen and closed.

## Next phase

Following a successful Phase 1B closeout, Phase 2A will preregister the first
explicitly ternary computation:

\[
\alpha+\beta+\gamma=0.
\]
