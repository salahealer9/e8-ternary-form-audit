# Phase 2A Zero-Sum E8 Root Triple Protocol

## Status

STATUS: PHASE2A_ZERO_SUM_TRIPLE_PROTOCOL_FROZEN

## Purpose

Phase 2A performs the first explicitly ternary computation in the project.

The validated E8 root set will be searched exhaustively for unordered triples

\[
\{\alpha,\beta,\gamma\}
\]

satisfying

\[
\alpha+\beta+\gamma=0.
\]

This phase does not yet quotient the resulting triples into A2 root
subsystems and does not yet construct the Lie-algebraic Cartan 3-form.

## Dependency

Phase 1A root construction completed at:

    455bb57

Phase 1B independent root validation completed at:

    7fb3c46

The Phase 1B conclusion established exact equality between the family-derived
and lattice-derived E8 root sets.

The validated 240-root set is therefore the fixed substrate for Phase 2A.

## Canonical representation

Roots remain represented by doubled integer coordinates

\[
q=2\alpha\in\mathbb Z^8.
\]

For three doubled roots

\[
q_\alpha,q_\beta,q_\gamma,
\]

the zero-sum condition is exactly

\[
q_\alpha+q_\beta+q_\gamma=0.
\]

No floating-point arithmetic or tolerance is permitted.

## Primary enumeration

Let the validated roots be deterministically ordered as

\[
r_0,r_1,\ldots,r_{n-1}.
\]

Phase 2A will exhaustively enumerate every index triple

\[
0\le i<j<k<n.
\]

A triple is retained iff

\[
r_i+r_j+r_k=0
\]

coordinate by coordinate.

This direct three-combination enumeration is the primary Phase 2A algorithm.

## Independence from binary structure

The primary enumeration must NOT use:

- the condition
  \[
  \alpha\cdot\beta=-1;
  \]
- neighbour lists;
- root-pair completion;
- A2 subsystem tables;
- Cartan 3-form support;
- an expected number of triples.

Pairwise inner products may be evaluated only AFTER the complete zero-sum
triple set has been generated.

This safeguard ensures that the first ternary result is obtained directly from
the ternary equation itself.

## Canonical unordered triple representation

Each retained triple is represented by the increasing root-index tuple

\[
(i,j,k),
\qquad i<j<k.
\]

This provides a deterministic canonical representation.

No permutation of the same three roots is stored as an additional unordered
triple.

## Quantities to derive

Phase 2A will report:

- total number of candidate 3-subsets examined;
- number of unordered zero-sum triples;
- implied number of ordered zero-sum triples;
- root-incidence distribution;
- pairwise inner-product signatures within retained triples;
- whether any retained triple contains repeated or opposite roots;
- whether every retained triple consists of three distinct roots.

## Candidate-space size

The number of candidate triples is determined only after obtaining the
validated root count \(n\), using

\[
\binom n3.
\]

The enumeration must traverse the complete candidate space.

No expected retained-triple count may terminate the loop.

## Frozen derived expectations

The following are arithmetic expectations recorded before Phase 2A execution.

Phase 1A independently observed

\[
13440
\]

ordered distinct root pairs with ordinary inner product

\[
-1.
\]

For an ordered pair satisfying

\[
\alpha\cdot\beta=-1,
\]

the vector

\[
\gamma=-(\alpha+\beta)
\]

has squared norm

\[
\gamma^2
=
\alpha^2+\beta^2+2\alpha\cdot\beta
=
2+2-2
=
2.
\]

In an E8 root system, this suggests a zero-sum root completion.

If every such ordered pair completes uniquely, the expected number of ordered
zero-sum triples is

\[
13440.
\]

Since a triple of three distinct roots has

\[
3!=6
\]

orderings, the corresponding expected number of unordered zero-sum triples is

\[
\frac{13440}{6}=2240.
\]

These are validation expectations only.

They must not control the primary enumeration.

## Expected root incidence

If 2240 unordered triples are uniformly distributed over the 240-root E8
system, the total root incidences would be

\[
3\times2240=6720.
\]

The corresponding expected incidence per root would be

\[
\frac{6720}{240}=28.
\]

This is a derived post-enumeration validation target, not an algorithmic
constraint.

## Post-enumeration characterization

Only after the zero-sum triple set is frozen may Phase 2A calculate pairwise
inner products inside each retained triple.

For roots of squared norm 2 satisfying

\[
\alpha+\beta+\gamma=0,
\]

the algebraic expectation is

\[
\alpha\cdot\beta
=
\beta\cdot\gamma
=
\gamma\cdot\alpha
=
-1.
\]

The computation must verify rather than assume this signature.

## Distinction from A2 subsystems

A zero-sum root triple is NOT automatically stored or counted as an A2
subsystem in Phase 2A.

The relation between:

- unordered zero-sum triples;
- opposite zero-sum triples;
- six-root A2 subsystems;

will be handled under a separately frozen Phase 2B protocol.

In particular, the external benchmark

\[
1120
\]

must not be used anywhere in the Phase 2A enumeration logic.

## Distinction from the Cartan 3-form

Phase 2A constructs only a root-level combinatorial relation.

It does not yet claim that

\[
T_{ijk}
\]

is the Cartan 3-form.

It does not assign signs, structure constants, or Lie-algebra basis
normalizations.

Those require later phases.

## Success criteria

Phase 2A is a computational PASS if:

1. every unordered 3-subset of the validated root set is examined;
2. retention uses only exact vector summation;
3. the output contains no duplicate unordered triples;
4. every retained triple sums exactly to zero;
5. every retained triple contains three distinct roots;
6. post-enumeration characterization is internally consistent;
7. all reported counts arise from the enumeration rather than benchmark
   forcing.

Agreement or disagreement with the frozen expectations must be reported
without changing the algorithm.

## Failure handling

If the observed count differs from a frozen expectation:

- do not modify the root set;
- do not modify the zero-sum criterion;
- do not add or remove triples manually;
- report the discrepancy;
- investigate under a separate amendment or diagnostic checkpoint.

## Next phase

Following Phase 2A closeout, Phase 2B will investigate the equivalence relation
between opposite zero-sum triples and six-root A2 subsystems.

Only after that relation is independently established may the external

\[
1120
\]

A2 benchmark be used for validation.
