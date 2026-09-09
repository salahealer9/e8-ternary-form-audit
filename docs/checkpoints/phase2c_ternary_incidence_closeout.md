# Phase 2C E8 Ternary Incidence Closeout

## Status

STATUS: PHASE2C_TERNARY_INCIDENCE_PASS

## Frozen protocol

Phase 2C protocol was frozen at commit:

    5fb68f0

Phase 2B A2 quotient was completed at:

    8ec6e3f

No signed alternating tensor, Lie bracket coefficients, or Cartan 3-form
coefficients were constructed before this closeout.

## Purpose

Phase 2C formalized the unsigned finite ternary incidence structure defined by

\[
\alpha+\beta+\gamma=0
\]

on the validated 240-root E8 system.

Two related objects were constructed:

1. an unordered 3-uniform hypergraph

   \[
   \mathcal H=(V,E);
   \]

2. a sparse symmetric Boolean ordered support tensor

   \[
   T_{ijk}.
   \]

No orientation or Lie-algebra sign was assigned.

## Hypergraph

The vertex set contains the 240 validated E8 roots:

\[
|V|=240.
\]

The hyperedge set consists exactly of the Phase 2A unordered zero-sum triples:

\[
|E|=2240.
\]

Observed:

    vertices: 240
    unordered hyperedges: 2240

## Symmetric Boolean tensor support

The Boolean support tensor was defined by

\[
T_{ijk}=1
\]

iff:

- \(i,j,k\) are distinct; and
- \[
  r_i+r_j+r_k=0.
  \]

Every unordered hyperedge contributes all

\[
3!=6
\]

ordered permutations.

Observed ordered support:

\[
2240\times6=13440.
\]

Observed:

    ordered support entries: 13440

The sparse support contained no duplicate ordered entries.

Result:

    UNIQUE_SPARSE_SUPPORT: TRUE

## Support density

A dense tensor of shape

\[
240^3
\]

would contain

\[
13{,}824{,}000
\]

entries.

The observed nonzero support density is therefore

\[
\frac{13440}{13{,}824{,}000}
=
0.000972222222\ldots
\]

or approximately

\[
0.0972222\%.
\]

Thus the unsigned tensor support is highly sparse.

## S3 symmetry

The complete ordered support was tested under every permutation of its three
indices.

Observed:

    full S3 symmetry: True

Therefore

\[
T_{ijk}
=
T_{\sigma(i)\sigma(j)\sigma(k)}
\]

for every

\[
\sigma\in S_3.
\]

This is a symmetric Boolean support tensor.

It is not an alternating tensor.

## Diagonal structure

Every nonzero support entry contains three distinct indices.

Observed:

    repeated-index support absent: True

Therefore all repeated-index entries vanish:

\[
T_{iik}=T_{iki}=T_{kii}=T_{iii}=0.
\]

## Vertex-degree spectrum

The unordered hypergraph degree of every root was reconstructed.

Observed:

    degree 28: 240 vertices

Therefore

\[
d_i=28
\]

for every E8 root.

The total incidence count is

\[
240\times28
=
6720
=
3\times2240,
\]

as required for a 3-uniform hypergraph.

## Pair-codegree spectrum

For each unordered pair of distinct roots,

\[
c_{ij}
=
|\{
e\in E:
i,j\in e
\}|
\]

was computed.

Observed:

    codegree 0: 21960 unordered pairs
    codegree 1: 6720 unordered pairs

The total is

\[
21960+6720
=
28680
=
\binom{240}{2}.
\]

Thus every unordered root pair is accounted for.

No pair has codegree greater than one.

Therefore

\[
\boxed{
c_{ij}\in\{0,1\}
}
\]

for all distinct roots.

## Linear hypergraph property

A 3-uniform hypergraph is linear when any pair of vertices belongs to at most
one hyperedge.

Because the observed maximum pair codegree is one,

\[
\mathcal H
\]

is a linear 3-uniform hypergraph.

This means an active root pair determines its third root uniquely.

## Active-pair count

The number of unordered pairs having positive codegree is

\[
6720.
\]

Observed:

    active unordered pairs: 6720

Each of the 2240 hyperedges contributes exactly three unordered pairs:

\[
2240\times3=6720.
\]

Because no pair is shared between distinct hyperedges, this accounts for every
active pair exactly once.

## Post-construction binary characterization

Only after construction of the ternary hypergraph were active pairs
characterized using the E8 inner product.

Observed doubled-dot spectrum:

    -4: 6720 active unordered pairs

Since doubled-coordinate inner products are divided by four, every active pair
has ordinary inner product

\[
-1.
\]

Phase 1A had independently established that there are exactly 13440 ordered
root pairs, hence 6720 unordered pairs, at inner product \(-1\).

Therefore for distinct E8 roots:

\[
\boxed{
c_{ij}=1
\iff
\alpha_i\cdot\alpha_j=-1.
}
\]

Equivalently,

\[
\alpha_i\cdot\alpha_j=-1
\]

iff there exists a unique root \(\alpha_k\) such that

\[
\alpha_i+\alpha_j+\alpha_k=0.
\]

The third root is necessarily

\[
\alpha_k=-(\alpha_i+\alpha_j).
\]

This equivalence was established as a post-construction comparison; the binary
condition was not used to define the ternary hypergraph.

## Global-negation action

Global root negation

\[
\alpha\mapsto-\alpha
\]

was applied to every hyperedge.

Observed:

    hyperedge negation orbits: 1120

Orbit-size spectrum:

    size 2: 1120 orbits

Therefore no hyperedge is fixed by global negation, and the 2240 hyperedges
partition into

\[
1120
\]

two-element orbits.

## Agreement with Phase 2B A2 quotient

Each negation orbit determines a canonical six-root union.

Observed:

    negation-orbit six-root sets: 1120
    Phase 2B A2 classes: 1120
    exact agreement: True

Thus the negation-orbit quotient of the ternary hypergraph agrees exactly with
the independently constructed Phase 2B A2 quotient.

Schematically,

\[
\boxed{
E
\longrightarrow
E/\{\pm1\}
\longleftrightarrow
\{A_2\text{ subsystems}\}
}
\]

with

\[
|E|=2240
\]

and

\[
|E/\{\pm1\}|=1120.
\]

## Test state

The complete repository test suite after Phase 2C implementation reported:

    44 passed in 62.32s

## Phase 2C conclusion

PHASE2C_TERNARY_INCIDENCE: PASS

The zero-sum relation defines a regular, linear, 3-uniform hypergraph on the
240 E8 roots with:

\[
v=240,
\]

\[
e=2240,
\]

uniform vertex degree

\[
28,
\]

and pair codegrees restricted to

\[
0\text{ or }1.
\]

Its associated symmetric Boolean ordered tensor has:

\[
13440
\]

nonzero entries and exact S3 symmetry.

The active unordered root pairs are exactly the 6720 pairs having ordinary
inner product

\[
-1.
\]

Global negation partitions the 2240 hyperedges into 1120 two-element orbits,
in exact agreement with the Phase 2B A2 subsystems.

## Interpretation boundary

The object constructed in Phase 2C is unsigned combinatorial support.

It is NOT yet:

- an alternating trilinear form;
- the Cartan 3-form;
- a table of Lie bracket structure constants;
- a metric tensor;
- evidence that the initiating notation specifically denoted this object.

No sign choices have been introduced.

## Next phase

Phase 3 will transition from the 240-root combinatorial substrate to the
248-dimensional Lie algebra

\[
\mathfrak e_8.
\]

The first task will be to preregister the root-space support theorem for

\[
\Omega(X,Y,Z)=B(X,[Y,Z]).
\]

In particular, Phase 3A will determine algebraically and computationally when

\[
\Omega(E_\alpha,E_\beta,E_\gamma)
\]

can be nonzero and compare that support with the Phase 2C condition

\[
\alpha+\beta+\gamma=0.
\]

No Cartan-form signs or numerical structure constants will be assigned until a
basis and normalization protocol have been separately frozen.
