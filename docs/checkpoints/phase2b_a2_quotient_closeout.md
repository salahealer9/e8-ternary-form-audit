# Phase 2B A2 Quotient Closeout

## Status

STATUS: PHASE2B_A2_QUOTIENT_PASS

## Frozen protocol

Phase 2B protocol was frozen at commit:

    e468a7e

Phase 2A zero-sum triple enumeration was completed at:

    350df63

No ternary-incidence tensor, Cartan 3-form coefficient, or E6 decomposition
was constructed before this closeout.

## Input

Phase 2B received the complete Phase 2A set of

\[
2240
\]

unordered E8 root triples satisfying

\[
\alpha+\beta+\gamma=0.
\]

No external A2 table was supplied.

## Opposite-triple relation

For every zero-sum triple

\[
\tau=\{\alpha,\beta,\gamma\},
\]

the opposite triple

\[
-\tau=\{-\alpha,-\beta,-\gamma\}
\]

was constructed by exact root lookup.

Observed:

    triples with opposite present: 2240
    self-opposite triples: 0

Therefore every Phase 2A triple has a distinct opposite triple present in the
same ternary relation.

## Six-root unions

For every triple,

\[
S(\tau)=\tau\cup(-\tau)
\]

was constructed.

Observed union-size spectrum:

    size 6: 2240 triples

Thus every triple/opposite union contains exactly six distinct roots.

## Quotient construction

Phase 2A triples were grouped by exact equality of their canonical six-root
union.

Observed:

    distinct six-root classes: 1120

Observed class-multiplicity spectrum:

    multiplicity 2: 1120 classes

Every quotient class consisted exactly of

\[
\{\tau,-\tau\}.
\]

Observed:

    classes exactly {tau, -tau}: 1120

Therefore the ternary triple set decomposes exactly as

\[
2240
=
1120\times2.
\]

This multiplicity was observed from the data and was not imposed by the
quotient algorithm.

## Exact rank

Every six-root quotient class was tested using exact rational linear algebra.

Observed:

    rank 2: 1120 subsystems

Therefore every candidate spans a two-dimensional root space.

## Reflection closure

Every candidate six-root set was tested under all internal root reflections.

Observed:

    reflection-closed subsystems: 1120

Thus every candidate is closed under its own root reflections.

## Pairwise inner-product structure

The unordered distinct-pair doubled-dot spectrum of every candidate subsystem
was:

\[
-8:3,\qquad
-4:6,\qquad
4:6.
\]

Observed:

    {-8: 3, -4: 6, 4: 6}: 1120 subsystems

Dividing by four gives ordinary E8 inner products:

\[
-2:3,\qquad
-1:6,\qquad
+1:6.
\]

The three inner products equal to \(-2\) are the three opposite-root pairs.

The remaining twelve unordered non-opposite pairs split equally between

\[
-1
\]

and

\[
+1.
\]

## A2 structural classification

Each candidate subsystem satisfies:

- six roots;
- rank 2;
- equal squared root norm 2;
- crystallographic simply-laced inner products;
- reflection closure;
- the standard six-root pairwise spectrum.

Observed:

    structurally A2 subsystems: 1120

Therefore every quotient class is identified structurally as a root subsystem
of type

\[
A_2.
\]

## External benchmark comparison

The Phase 0 literature benchmark was

\[
N_{A_2}=1120.
\]

Observed:

    expected A2 subsystems: 1120
    observed A2 subsystems: 1120
    benchmark match: True

Result:

    A2_BENCHMARK_REPLICATION: PASS

The external value 1120 was used only after quotient construction for
validation.

It did not determine:

- the zero-sum triple enumeration;
- opposite-triple matching;
- quotient grouping;
- multiplicity;
- rank;
- reflection closure;
- subsystem classification.

## Test state

The complete repository test suite after Phase 2B implementation reported:

    33 passed in 47.72s

## Phase 2B conclusion

PHASE2B_A2_QUOTIENT: PASS

The Phase 2A ternary relation

\[
\alpha+\beta+\gamma=0
\]

contains exactly

\[
2240
\]

unordered zero-sum triples.

These partition canonically into

\[
1120
\]

opposite pairs

\[
\{\tau,-\tau\}.
\]

Each pair generates exactly one six-root, rank-two, reflection-closed root
subsystem of type

\[
A_2.
\]

Thus the frozen literature count of 1120 A2 subsystems has been independently
reconstructed from the ternary zero-sum relation.

## Structural interpretation

The validated relation can now be written schematically as

\[
\boxed{
2240\text{ zero-sum orientations}
\longleftrightarrow
1120\text{ unoriented }A_2\text{ subsystems}
}
\]

where each A2 subsystem contains exactly two zero-sum triples related by global
root negation.

This establishes an explicit finite ternary incidence structure on the 240
E8 roots.

## Interpretation boundary

Phase 2B does NOT yet establish that this unsigned root relation is itself the
Cartan 3-form.

No:

- Lie bracket coefficients;
- orientation signs;
- Chevalley basis choices;
- structure constants;
- Cartan-form normalization;
- E6 representation decomposition;
- generalized metric

have yet been introduced.

The distinction between ternary combinatorial support and an alternating
trilinear form remains essential.

## Next phase

Phase 2C will preregister and construct the finite root-level ternary incidence
object.

It will distinguish:

1. unordered support on the 2240 zero-sum triples;
2. ordered support on the 13440 permutations;
3. a possible alternating orientation;
4. the later Lie-algebraic Cartan 3-form.

The Phase 2C object will be defined before implementation so that no tensor
definition is selected retrospectively to mimic the Cartan form.
