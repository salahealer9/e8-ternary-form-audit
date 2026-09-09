# Phase 1A E8 Root Construction Protocol

## Status

STATUS: PHASE1A_ROOT_CONSTRUCTION_PROTOCOL_FROZEN

## Purpose

Construct the standard 8-dimensional E8 root system independently from its
coordinate rules.

This phase precedes all zero-sum triple, A2-subsystem, ternary-incidence, and
Cartan-3-form computations.

## Dependency

Phase 0 is frozen at:

    5b7eabd

Post-freeze prior-art discovery is recorded at:

    96fddd0

Neither commit is modified by Phase 1A.

## Exact internal representation

Every root

\[
\alpha\in\mathbb R^8
\]

will be stored internally as its doubled coordinate vector

\[
q=2\alpha\in\mathbb Z^8.
\]

This avoids floating-point arithmetic.

For doubled roots \(q,r\),

\[
\alpha\cdot\beta
=
\frac{q\cdot r}{4}.
\]

Squared norm is therefore

\[
\alpha^2
=
\frac{q\cdot q}{4}.
\]

The implementation may expose rational or floating views downstream, but the
canonical Phase 1A representation is integer-valued.

## Root family F1 — integer-coordinate roots

Generate all vectors obtained by:

1. choosing two distinct coordinate positions from eight;
2. assigning each selected coordinate independently one of the signs \(+1\)
   or \(-1\);
3. assigning zero to every remaining coordinate.

In ordinary coordinates these have the form

\[
(\pm1,\pm1,0,0,0,0,0,0)
\]

up to permutation.

In doubled coordinates they have the form

\[
(\pm2,\pm2,0,0,0,0,0,0).
\]

The implementation must exhaust the defining choices.

It must not terminate after reaching any externally expected number of roots.

## Root family F2 — half-integer-coordinate roots

Generate every sign vector

\[
(s_1,\ldots,s_8),
\qquad
s_i\in\{-1,+1\},
\]

having an even number of negative entries.

Associate to it the ordinary root

\[
\frac12(s_1,\ldots,s_8).
\]

Its doubled-coordinate representation is therefore exactly

\[
(s_1,\ldots,s_8).
\]

The implementation must enumerate all sign vectors and apply the parity rule.

It must not terminate after reaching any externally expected number of roots.

## Combined construction

The complete generated root collection is

\[
\Phi_{\mathrm{generated}}
=
F_1\cup F_2.
\]

The union must be formed by exact tuple identity.

No externally supplied root table is permitted.

## Quantities to derive

The program will independently report:

- number of F1 roots;
- number of F2 roots;
- total generated roots;
- number of unique roots;
- duplicate count;
- squared-norm spectrum;
- whether every root has its negative;
- pairwise inner-product spectrum.

The following values are external replication targets already frozen in
Phase 0:

\[
|\Phi(E_8)|=240,
\]

\[
\alpha^2=2.
\]

They are not construction parameters.

## Inner-product arithmetic

The canonical exact quantity for two doubled roots \(q,r\) is

\[
q\cdot r.
\]

The corresponding E8 inner product is

\[
\frac{q\cdot r}{4}.
\]

No floating-point tolerance is permitted for Phase 1A root equality, norm
validation, or inner-product classification.

## Phase 1A success criteria

Phase 1A is a replication PASS only if:

1. generation completes exhaustively from the defining rules;
2. no duplicate roots remain in the combined construction;
3. every generated root has squared norm exactly 2;
4. the generated root count agrees with the frozen external benchmark;
5. every root has its exact negative in the generated set;
6. pairwise inner products are consistent with a simply-laced root system.

Failure of any criterion must be reported rather than repaired by changing the
generation rules to force the benchmark.

## Prohibited operations

Phase 1A must not:

- load a precomputed E8 root table;
- stop after finding 112 integer-family roots;
- stop after finding 128 half-integer-family roots;
- stop after finding 240 total roots;
- remove roots merely because the total exceeds an expected count;
- add roots merely because the total falls below an expected count;
- use approximate floating-point equality to deduplicate roots;
- use Phase 2 triple or A2 counts to alter Phase 1A output.

## Separation from later phases

Phase 1A does NOT yet compute:

- zero-sum root triples;
- A2 subsystems;
- ternary incidence tensors;
- Cartan 3-form coefficients;
- E6 decomposition data;
- G2 comparison data.

Those belong to later phases.

## Closeout artifact

After implementation and execution, Phase 1A will export a deterministic
checkpoint containing:

- family counts;
- total and unique counts;
- norm spectrum;
- inner-product spectrum;
- negative-root closure result;
- benchmark comparison;
- PASS / FAIL status.

The implementation source and checkpoint will then be hashed and committed
before Phase 1B begins.
