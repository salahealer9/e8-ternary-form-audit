# Phase 2A Zero-Sum E8 Root Triple Closeout

## Status

STATUS: PHASE2A_ZERO_SUM_TRIPLES_PASS

## Frozen protocol

Phase 2A protocol was frozen at commit:

    701d321

The validated E8 root substrate was frozen previously at:

    7fb3c46

No A2-subsystem quotienting or Cartan-3-form coefficient construction was
performed before this closeout.

## Purpose

Phase 2A performed the first explicitly ternary computation of the project.

Every unordered 3-subset of the validated E8 root system was tested directly
for the exact relation

\[
\alpha+\beta+\gamma=0.
\]

The primary enumeration used:

- no pairwise inner-product prefilter;
- no neighbour lists;
- no A2 subsystem data;
- no Cartan-form support;
- no expected retained-triple count.

## Candidate space

The validated root count was

\[
n=240.
\]

The exhaustive unordered candidate space therefore contained

\[
\binom{240}{3}
=
2{,}275{,}280
\]

triples.

Observed:

    candidate unordered triples examined: 2275280

Thus the complete unordered 3-subset space was traversed.

## Primary zero-sum result

The number of retained unordered triples satisfying

\[
\alpha+\beta+\gamma=0
\]

was

\[
\boxed{2240}.
\]

Observed:

    retained unordered zero-sum triples: 2240

Each retained triple contains three distinct roots and is stored once in
canonical increasing-index order.

Duplicate unordered triples:

    0

## Ordered triple count

Each unordered triple of three distinct roots has

\[
3!=6
\]

orderings.

Therefore the retained set corresponds to

\[
6\times2240
=
13440
\]

ordered zero-sum triples.

Observed:

    implied ordered zero-sum triples: 13440

## Exact ternary integrity

Every retained triple was independently rechecked against the defining
relation.

Result:

    ALL_RETAINED_TRIPLES_SUM_EXACTLY_TO_ZERO: TRUE

Canonical distinct-index representation:

    TRUE

Duplicate unordered triples:

    0

## Root incidence

The total number of root incidences in the unordered triple set is

\[
3\times2240
=
6720.
\]

The observed incidence distribution was uniform:

\[
28
\]

triples per root.

Observed:

    incidence 28: 240 roots
    total root incidences: 6720

Therefore every E8 root participates in exactly

\[
\boxed{28}
\]

unordered zero-sum root triples.

## Post-enumeration pairwise characterization

Only after the zero-sum triple enumeration was complete were pairwise inner
products evaluated inside retained triples.

In doubled coordinates, every retained triple had signature

\[
(-4,-4,-4).
\]

Observed:

    (-4, -4, -4): 2240

Since doubled-coordinate dot products are divided by four to obtain ordinary
E8 inner products, every zero-sum triple satisfies

\[
\alpha\cdot\beta
=
\beta\cdot\gamma
=
\gamma\cdot\alpha
=
-1.
\]

Thus the complete observed ordinary pairwise signature is

\[
\boxed{(-1,-1,-1)}.
\]

## Degeneracy check

No retained triple contains an opposite pair of roots.

Observed:

    triples containing an opposite pair: 0

## Binary/ternary consistency

Phase 1A independently observed

\[
13440
\]

ordered distinct root pairs at inner product

\[
-1.
\]

Phase 2A independently obtained

\[
13440
\]

ordered zero-sum root triples.

The Phase 2A enumeration did not use the binary relation to construct or
prefilter triples.

This agreement is therefore a post-enumeration consistency result.

The precise bijective relationship between the binary pair relation and the
ternary zero-sum relation will be formalized only if required by a later
protocol.

## Execution-wrapper correction

The first execution of the Phase 2A script completed the full ternary
enumeration correctly and the complete test suite passed.

That execution produced:

    candidate unordered triples examined: 2275280
    retained unordered zero-sum triples: 2240
    implied ordered zero-sum triples: 13440

but the script's final PASS/FAIL wrapper contained an incorrect hard-coded
candidate-space value:

    2_276_880

rather than the correct value

\[
\binom{240}{3}
=
2{,}275{,}280.
\]

Consequently the first script execution reported:

    PHASE2A_ZERO_SUM_TRIPLES: FAIL

despite the mathematical enumeration being correct.

The validation wrapper was corrected to use

    comb(len(roots), 3)

rather than another hard-coded candidate count.

No root-generation logic, triple-enumeration logic, retention criterion, or
observed ternary result was modified.

After correction:

    23 passed in 18.02s
    PHASE2A_ZERO_SUM_TRIPLES: PASS

This correction is classified as:

    VALIDATION_WRAPPER_ARITHMETIC_CORRECTION

and does not alter the frozen Phase 2A protocol or its mathematical result.

## Test state

The complete repository test suite reported:

    23 passed in 18.02s

## Phase 2A conclusion

PHASE2A_ZERO_SUM_TRIPLES: PASS

The exhaustive direct ternary equation

\[
\alpha+\beta+\gamma=0
\]

selects exactly

\[
2240
\]

unordered triples from the validated E8 root system.

Every root participates uniformly in 28 such triples.

Every retained triple has pairwise ordinary inner products

\[
(-1,-1,-1).
\]

No benchmark-driven stopping, binary prefiltering, or manual repair was used.

## Interpretation boundary

Phase 2A establishes a finite ternary incidence relation on the E8 root set.

It does NOT yet establish:

- the quotient into A2 subsystems;
- the external count 1120 through direct construction;
- Cartan 3-form coefficients;
- signs or structure constants;
- a metric interpretation of the initiating notation;
- novelty beyond established E8 root-system mathematics.

## Next phase

Phase 2B will investigate the relationship between a zero-sum triple

\[
\{\alpha,\beta,\gamma\}
\]

and its opposite triple

\[
\{-\alpha,-\beta,-\gamma\},
\]

and determine whether each such pair forms exactly one six-root

\[
A_2
\]

root subsystem.

Only after that quotient is constructed independently will the frozen external
benchmark

\[
1120
\]

be used for validation.
