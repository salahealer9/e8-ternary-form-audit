# Phase 2C E8 Ternary Incidence Protocol

## Status

STATUS: PHASE2C_TERNARY_INCIDENCE_PROTOCOL_FROZEN

## Purpose

Phase 2C defines and constructs the discrete root-level ternary incidence
structure arising from the validated relation

\[
\alpha+\beta+\gamma=0.
\]

This phase formalizes the combinatorial object before any comparison with the
signed Lie-algebraic Cartan 3-form.

## Dependencies

Phase 2A zero-sum triple enumeration completed at:

    350df63

Phase 2B A2 quotient completed at:

    8ec6e3f

Phase 2A established:

\[
2240
\]

unordered zero-sum root triples and

\[
13440
\]

corresponding ordered permutations.

Phase 2B established that these triples form

\[
1120
\]

opposite pairs, each giving one A2 root subsystem.

## Root indexing

Let the validated E8 roots be deterministically ordered as

\[
r_0,r_1,\ldots,r_{239}.
\]

This indexing is inherited unchanged from the Phase 1 root construction.

No reordering based on ternary incidence is permitted in Phase 2C.

## Object H — unordered ternary hypergraph

Define the 3-uniform hypergraph

\[
\mathcal H=(V,E)
\]

with

\[
V=\{0,\ldots,239\}
\]

and

\[
E=
\left\{
\{i,j,k\}:
r_i+r_j+r_k=0
\right\}.
\]

Each hyperedge therefore corresponds to exactly one Phase 2A unordered
zero-sum triple.

Expected Phase 2A replication values:

\[
|V|=240,
\]

\[
|E|=2240.
\]

These values are validation targets and are not construction parameters.

## Object T — symmetric Boolean support tensor

Define

\[
T_{ijk}
=
\begin{cases}
1,
&
r_i+r_j+r_k=0
\text{ and }i,j,k\text{ are distinct},\\
0,
&
\text{otherwise}.
\end{cases}
\]

The tensor is therefore invariant under all permutations of its indices:

\[
T_{ijk}
=
T_{\sigma(i)\sigma(j)\sigma(k)}
\]

for every

\[
\sigma\in S_3.
\]

The support size is expected to equal the number of ordered zero-sum triples:

\[
|\operatorname{supp}T|=13440.
\]

This value must be obtained from the constructed support.

## Sparse representation

A dense tensor of shape

\[
240\times240\times240
\]

contains

\[
13{,}824{,}000
\]

entries.

Phase 2C will therefore use a sparse canonical representation.

The canonical ordered support will be stored as tuples

\[
(i,j,k)
\]

for which

\[
T_{ijk}=1.
\]

A dense 240^3 array is not required for the primary artifact.

## Hypergraph degree

For vertex \(i\), define

\[
d_i
=
|\{
e\in E:
i\in e
\}|.
\]

Phase 2A observed the uniform value

\[
d_i=28.
\]

Phase 2C will reconstruct the degree sequence from the hypergraph representation
and verify it independently.

## Pair codegree

For distinct roots \(i,j\), define the hypergraph pair codegree

\[
c_{ij}
=
|\{
e\in E:
i,j\in e
\}|.
\]

Phase 2C will derive the complete codegree spectrum.

No expected codegree spectrum will be supplied to the algorithm.

This quantity is important because the zero-sum equation implies that a pair,
if completable, should determine its third root uniquely.

That uniqueness must be observed from the hypergraph.

## Opposite-map action

Let

\[
\nu(i)
\]

denote the index of the opposite root

\[
-r_i.
\]

Phase 2C will determine the induced action

\[
\{i,j,k\}
\mapsto
\{\nu(i),\nu(j),\nu(k)\}
\]

on hyperedges.

The computation will verify:

- every hyperedge maps to another hyperedge;
- no hyperedge is fixed by global negation;
- the hyperedge orbits under negation have size 2;
- those orbits agree exactly with the 1120 Phase 2B A2 classes.

## Tensor symmetry

For every support triple

\[
(i,j,k),
\]

all six permutations must occur in ordered tensor support.

Phase 2C will verify full S3 symmetry of T.

## Tensor diagonal properties

Because a zero-sum Phase 2A triple contains three distinct roots,

\[
T_{iik}=0,
\]

\[
T_{iji}=0,
\]

\[
T_{kii}=0,
\]

and

\[
T_{iii}=0
\]

for all indices.

These properties must be verified from the constructed support.

## Relation to binary inner products

Phase 2C may characterize the already constructed hyperedges using pairwise
inner products after construction.

It must not use

\[
r_i\cdot r_j=-1
\]

as the definition of the ternary support.

The primary support definition remains

\[
r_i+r_j+r_k=0.
\]

## Relation to A2 subsystems

Each A2 subsystem obtained in Phase 2B contains exactly two unordered
hyperedges related by global negation.

Phase 2C will verify this relationship from the hypergraph representation.

The hypergraph itself retains the two hyperedges separately.

It is not quotient-equivalent to the set of A2 subsystems.

## Object A — alternating tensor reserved

A possible alternating tensor

\[
A_{ijk}
\]

is explicitly RESERVED for a later phase.

Phase 2C will NOT assign signs according to permutation parity.

Doing so without first fixing a Lie-algebra basis and structure constants
would create an arbitrary orientation convention.

## Cartan 3-form boundary

The Boolean tensor

\[
T_{ijk}
\]

encodes support only.

It is NOT defined as

\[
B(E_i,[E_j,E_k]).
\]

It contains no:

- Lie bracket coefficient;
- Chevalley sign;
- normalization;
- Cartan-subalgebra contribution;
- basis orientation.

A later phase must determine how much of the Cartan 3-form support is captured
by this discrete root-level object.

## Quantities to report

Phase 2C will report:

- vertex count;
- unordered hyperedge count;
- ordered support count;
- vertex-degree spectrum;
- pair-codegree spectrum;
- number of distinct active unordered root pairs;
- S3 symmetry result;
- diagonal-zero result;
- global-negation orbit spectrum;
- number of negation orbits;
- agreement of negation orbits with Phase 2B A2 classes.

## Success criteria

Phase 2C is a PASS if:

1. the hypergraph is constructed exclusively from Phase 2A zero-sum triples;
2. every hyperedge contains three distinct roots;
3. the ordered tensor support is generated from all permutations of each
   hyperedge;
4. the support tensor is exactly S3-symmetric;
5. all repeated-index tensor entries vanish;
6. the degree and codegree spectra are derived without forcing expected values;
7. global root negation acts on hyperedges with observed orbit structure;
8. negation orbits agree exactly with the Phase 2B A2 quotient;
9. no signed Cartan-form information is inserted.

## Interpretation boundary

Phase 2C establishes an unsigned finite ternary incidence object.

It does NOT establish:

- an alternating trilinear form;
- Lie algebra structure constants;
- a generalized metric;
- a unique tensor orientation;
- novelty of the incidence representation.

## Next phase

After Phase 2C closeout, Phase 3 will begin the transition from root
combinatorics to Lie algebra.

The first question will be whether the support of

\[
\Omega(X,Y,Z)=B(X,[Y,Z])
\]

on root-space vectors is exactly controlled by the zero-sum root relation

\[
\alpha+\beta+\gamma=0.
\]
