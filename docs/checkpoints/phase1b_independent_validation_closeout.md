# Phase 1B Independent E8 Validation Closeout

## Status

STATUS: PHASE1B_INDEPENDENT_VALIDATION_PASS

## Frozen protocol

Phase 1B protocol was frozen at commit:

    9346905

Phase 1A was completed at:

    455bb57

No zero-sum root-triple or A2-subsystem enumeration was performed before this
closeout.

## Purpose

Phase 1B independently reconstructed the E8 root system from the E8 lattice
condition and root norm, rather than from the two coordinate-family
construction used in Phase 1A.

The objective was to determine whether two logically distinct construction
paths produce exactly the same finite root set.

## Independent construction

Doubled coordinates

\[
q=2x\in\mathbb Z^8
\]

were exhaustively searched over

\[
q_i\in\{-2,-1,0,1,2\},
\]

where the coordinate bound follows from the root norm condition

\[
q\cdot q=8.
\]

Candidates were accepted only when:

1. all coordinates had common parity;
2. the coordinate sum satisfied
   \[
   \sum_i q_i\equiv0\pmod4;
   \]
3. the exact squared norm satisfied
   \[
   q\cdot q=8.
   \]

No Phase 1A family generator was used during this enumeration.

No expected root count controlled termination.

## Independent enumeration result

The lattice-derived enumeration produced:

\[
|\Phi_{\mathrm{lattice}}|=240.
\]

## Exact comparison with Phase 1A

After independent enumeration completed, the Phase 1A root set was generated
for exact comparison.

Observed:

    Phase 1A roots:       240
    lattice-derived roots: 240
    lattice-only roots:     0
    Phase1A-only roots:     0

Therefore

\[
\Phi_{\mathrm{lattice}}
=
\Phi_{\mathrm{Phase1A}}
\]

by exact integer tuple equality.

Result:

    EXACT_SET_EQUALITY: TRUE

## Exact rank

Exact rational Gaussian elimination gave

\[
\operatorname{rank}(\Phi)=8.
\]

Result:

    EXACT_RANK: 8

## Crystallographic integrality

For every root pair \(\alpha,\beta\), the Cartan quantity

\[
\frac{2(\alpha\cdot\beta)}
{\alpha\cdot\alpha}
\]

was integral.

Because all roots satisfy

\[
\alpha\cdot\alpha=2,
\]

this reduces to integrality of

\[
\alpha\cdot\beta.
\]

Result:

    CRYSTALLOGRAPHIC_INTEGRALITY: TRUE

## Reflection closure

For every pair of roots, the exact reflection

\[
s_\alpha(\beta)
=
\beta-
\frac{2(\alpha\cdot\beta)}
{\alpha\cdot\alpha}\alpha
\]

was evaluated.

Every resulting vector belonged to the generated root set.

Result:

    REFLECTION_CLOSURE: TRUE

## Irreducibility connectivity check

A graph was formed on the 240 roots.

Two distinct, non-opposite roots were connected when their inner product was
nonzero.

The graph was connected.

Result:

    NONORTHOGONALITY_GRAPH_CONNECTED: TRUE

This provides a finite structural check that the root system does not split
into mutually orthogonal components.

## Test state

The complete repository test suite after Phase 1B implementation reported:

    16 passed in 2.61s

## Phase 1B conclusion

PHASE1B_INDEPENDENT_VALIDATION: PASS

Two distinct construction paths independently produce exactly the same
240-element E8 root set.

The resulting root system additionally satisfies:

- exact rank 8;
- crystallographic integrality;
- closure under all root reflections;
- connected nonorthogonality structure.

No discrepancy repair or benchmark-forcing modification was required.

## Substrate status

The finite E8 root substrate is now considered validated for the purposes of
the preregistered ternary investigation.

The validated substrate contains no ternary interpretation by itself.

## Next phase

Phase 2A will begin the first explicitly ternary computation.

It will investigate triples of roots satisfying

\[
\alpha+\beta+\gamma=0
\]

under a separately frozen protocol.

No expected triple count or A2 count will be permitted to control that
enumeration.
