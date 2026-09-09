# Phase 2B A2 Quotient Protocol

## Status

STATUS: PHASE2B_A2_QUOTIENT_PROTOCOL_FROZEN

## Purpose

Phase 2B determines the exact relationship between the Phase 2A unordered
zero-sum triples

\[
\{\alpha,\beta,\gamma\},
\qquad
\alpha+\beta+\gamma=0,
\]

and six-root subsystems of type

\[
A_2.
\]

The quotient construction will be derived from the Phase 2A output rather than
from the frozen external benchmark count.

## Dependency

Phase 2A completed at commit:

    350df63

Phase 2A established exactly:

\[
2240
\]

unordered zero-sum root triples.

Every retained triple has ordinary pairwise inner-product signature

\[
(-1,-1,-1).
\]

Every root participates in exactly

\[
28
\]

such triples.

## Input

The sole Phase 2B combinatorial input is the complete Phase 2A zero-sum triple
set over the validated E8 root system.

No externally supplied A2 table is permitted.

## Opposite triple

For a zero-sum triple

\[
\tau=\{\alpha,\beta,\gamma\},
\]

define

\[
-\tau
=
\{-\alpha,-\beta,-\gamma\}.
\]

Because

\[
\alpha+\beta+\gamma=0,
\]

the opposite triple also satisfies

\[
(-\alpha)+(-\beta)+(-\gamma)=0.
\]

Phase 2B must verify this relation computationally rather than merely assume
that every opposite triple is present in the enumerated Phase 2A set.

## Canonical root indexing

The validated E8 roots remain in deterministic lexicographic order.

A zero-sum triple is represented by increasing root indices

\[
(i,j,k),
\qquad i<j<k.
\]

The opposite triple is obtained by exact lookup of the indices corresponding
to the three negated roots, followed by canonical sorting.

## Six-root candidate subsystem

For each zero-sum triple \(\tau\), define

\[
S(\tau)=\tau\cup(-\tau).
\]

At the root-vector level this is

\[
S(\tau)
=
\{\alpha,\beta,\gamma,-\alpha,-\beta,-\gamma\}.
\]

The canonical representation of a candidate six-root subsystem is the sorted
six-index tuple.

No expected subsystem count is used when constructing these six-root sets.

## Required checks

### Q1 — Opposite existence

For every Phase 2A triple \(\tau\),

\[
-\tau
\]

must occur in the Phase 2A triple set.

### Q2 — Opposite distinctness

Verify

\[
\tau\ne-\tau.
\]

No zero-sum triple may be self-opposite.

### Q3 — Six distinct roots

Verify

\[
|S(\tau)|=6.
\]

### Q4 — Quotient multiplicity

Group Phase 2A triples by their canonical six-root set.

Determine the multiplicity distribution independently.

The preregistered algebraic expectation is that every six-root set is generated
by exactly two zero-sum triples:

\[
\tau
\quad\text{and}\quad
-\tau.
\]

This must be observed rather than imposed.

### Q5 — A2 inner-product structure

For every candidate six-root set, compute the complete pairwise
inner-product structure.

The Phase 2A result implies that one orientation contains three mutually
pairwise inner products

\[
-1.
\]

Phase 2B must independently verify that the complete six-root set has the
standard rank-two simply-laced root-system structure.

### Q6 — Rank

Each six-root candidate must span exactly a two-dimensional vector space:

\[
\operatorname{rank} S(\tau)=2.
\]

The rank check must use exact arithmetic.

### Q7 — Reflection closure within subsystem

For every pair

\[
\alpha,\beta\in S(\tau),
\]

the root reflection

\[
s_\alpha(\beta)
=
\beta-(\alpha\cdot\beta)\alpha
\]

must remain inside

\[
S(\tau).
\]

This establishes internal root-system closure.

### Q8 — Root-system cardinality

Each candidate subsystem must contain exactly six distinct roots.

Combined with:

- rank 2;
- equal root norm;
- simply-laced crystallographic inner products;
- reflection closure;

this identifies the subsystem as type

\[
A_2
\]

rather than merely labelling it from the expected answer.

## External benchmark

The frozen literature benchmark is

\[
N_{A_2}=1120.
\]

This value may be compared with the observed quotient count only after all
2240 zero-sum triples have been grouped into six-root sets.

It must not:

- terminate the grouping;
- discard candidate subsystems;
- create missing subsystems;
- determine quotient multiplicity.

## Derived expectation

If every six-root subsystem corresponds to exactly the pair

\[
\{\tau,-\tau\},
\]

then the Phase 2A count predicts

\[
\frac{2240}{2}=1120.
\]

This is a validation expectation only.

The quotient algorithm must derive its actual number of equivalence classes
without using 1120.

## Equivalence relation

Define

\[
\tau_1\sim\tau_2
\]

iff

\[
S(\tau_1)=S(\tau_2).
\]

Phase 2B must verify that each observed equivalence class contains exactly two
Phase 2A triples and that those two triples are negatives of one another.

## Quantities to report

Phase 2B will report:

- Phase 2A triple count supplied as input;
- number of triples whose opposite is present;
- number of self-opposite triples;
- six-root-set size spectrum;
- quotient-class multiplicity spectrum;
- number of distinct six-root candidate subsystems;
- exact rank spectrum;
- reflection-closure result;
- subsystem pairwise inner-product spectrum;
- number passing the A2 structural criteria;
- comparison with the frozen 1120 benchmark.

## Success criteria

Phase 2B is a PASS only if:

1. every Phase 2A triple has a unique opposite triple;
2. no triple is self-opposite;
3. every union with its opposite contains six distinct roots;
4. quotient multiplicity is derived rather than assumed;
5. every quotient class has the same observed structural type;
6. every candidate subsystem has exact rank 2;
7. every candidate subsystem is internally reflection-closed;
8. every candidate satisfies the structural criteria for A2;
9. the observed subsystem count is compared honestly with the frozen external
   benchmark.

A benchmark mismatch must be reported rather than repaired.

## Interpretation boundary

Phase 2B may establish a finite decomposition of the Phase 2A ternary relation
into A2 root subsystems.

It does NOT yet establish:

- Cartan 3-form coefficients;
- Lie bracket structure constants;
- signs or orientations of the ternary form;
- E6 representation-theoretic decomposition;
- a generalized metric interpretation of
  \[
  g(v_1,v_2,v_3);
  \]
- mathematical novelty.

Those remain later phases.

## Next phase

After Phase 2B closeout, the project will define the root-level ternary
incidence object itself under a separate protocol.

That phase will distinguish carefully between:

1. unsigned combinatorial support;
2. oriented / alternating support;
3. the actual Lie-algebraic Cartan 3-form.
