# Paper P0 — Scope and Claims Protocol

## Status

STATUS: PAPER_P0_SCOPE_AND_CLAIMS_FROZEN

## Working title

**An Exact Sparse Realization of the \(E_8\) Cartan 3-Form**

Alternative title retained for later consideration:

**A Reproducible Sparse Realization of the \(E_8\) Cartan 3-Form**

No title claiming a new invariant, new ternary structure, or discovery of the
Cartan 3-form is permitted.

## Principal object

The paper studies the normalized Cartan 3-form

\[
g(v_1,v_2,v_3)
=
\Omega_0(v_1,v_2,v_3)
=
B_0(v_1,[v_2,v_3])
\]

on the frozen canonical basis of:

\[
\mathfrak e_8.
\]

The basis dimension is:

\[
248.
\]

The paper treats \(g\) as an established Lie-theoretic object whose explicit
sparse realization is the subject of the work.

## Main contribution

The manuscript will present an exact, reproducible sparse realization of the
normalized \(E_8\) Cartan 3-form in a fixed canonical Chevalley basis.

The contribution consists of the combination of:

1. an exact root-level ternary-incidence realization;
2. a complete sparse coefficient census;
3. analytic derivations of the principal counts;
4. a deterministic machine-readable tensor representation;
5. two independent exact tensor constructions;
6. an independent reconstruction of the underlying Lie algebra;
7. exhaustive Jacobi and invariant-form validation;
8. exact recovery of the Lie bracket from \(g\) and \(B_0\).

## Principal quantitative results

### Root system

\[
240
\]

roots.

### Zero-sum root triples

\[
2240
\]

unordered zero-sum triples.

Equivalent ordered support:

\[
13440.
\]

These counts are established prior art or direct consequences of established
\(E_8\) root combinatorics and are not claimed as discoveries.

### Root-root-root Cartan-form sector

\[
\boxed{
RRR=13440.
}
\]

### Cartan-root-root sector

\[
\boxed{
HRR=2736.
}
\]

### Complete sparse support

\[
\boxed{
16176.
}
\]

### Complete nonzero coefficient spectrum

\[
\boxed{
-2:24,\qquad
-1:8064,\qquad
+1:8064,\qquad
+2:24.
}
\]

This spectrum is explicitly basis- and normalization-dependent.

It is not presented as a new invariant of \(E_8\).

## Root-incidence identity

For roots:

\[
\alpha,\beta,\gamma\in\Phi(E_8),
\]

the paper will establish explicitly:

\[
\boxed{
g(e_\alpha,e_\beta,e_\gamma)\neq0
\iff
\alpha+\beta+\gamma=0.
}
\]

Equivalently, the zero-sum ternary incidence tensor:

\[
T_{\alpha\beta\gamma}
\]

is the unsigned support of the root-root-root sector:

\[
\boxed{
T_{\alpha\beta\gamma}=1
\iff
g(e_\alpha,e_\beta,e_\gamma)\neq0.
}
\]

The underlying Lie-theoretic implication is standard.

The contribution is the explicit finite combinatorial realization and
computational representation.

## Hypergraph formulation

The root sector may be represented as a 3-uniform hypergraph:

\[
\mathcal H=(V,E)
\]

with:

\[
|V|=240,
\]

\[
|E|=2240.
\]

Observed properties include:

\[
\deg(v)=28
\]

for every root,

pair codegree:

\[
0\text{ or }1,
\]

and:

\[
1120
\]

negation edge-orbits.

The paper will make clear which of these properties are direct consequences
of established \(A_2\) combinatorics.

No theorem-level novelty will be claimed merely from this reformulation.

## Analytic derivation of RRR count

For every root \(\beta\), exactly:

\[
56
\]

roots \(\gamma\) satisfy:

\[
\beta\cdot\gamma=-1.
\]

For such an ordered pair:

\[
\beta+\gamma
\]

is a root, and:

\[
\alpha=-(\beta+\gamma)
\]

is uniquely determined.

Hence:

\[
\boxed{
240\times56=13440
}
\]

ordered nonzero RRR coefficients.

## Analytic derivation of HRR count

For one fixed simple Cartan basis vector \(h_i\), the root evaluations satisfy:

- two roots with
  \[
  |\alpha(h_i)|=2;
  \]
- 112 roots with
  \[
  |\alpha(h_i)|=1;
  \]
- 126 roots with
  \[
  \alpha(h_i)=0.
  \]

Therefore:

\[
114
\]

roots contribute for each \(h_i\).

For eight simple Cartan directions:

\[
8\times114=912.
\]

There are three possible positions for the Cartan argument in an ordered
nonzero triple.

Therefore:

\[
\boxed{
HRR=3\times912=2736.
}
\]

Thus:

\[
\boxed{
13440+2736=16176.
}
\]

## Analytic magnitude-two census

Magnitude-two coefficients occur only when:

\[
\alpha=\pm\alpha_i
\]

for a simple root associated with the chosen Cartan direction.

There are:

\[
8
\]

underlying Cartan/simple-root triples.

Each unordered nonzero triple produces:

\[
6
\]

ordered alternating coefficients.

Therefore:

\[
8\times6=48
\]

ordered magnitude-two coefficients.

Alternation balances their signs:

\[
\boxed{
-2:24,\qquad+2:24.
}
\]

The remaining:

\[
16176-48=16128
\]

coefficients have magnitude one.

Sign balance gives:

\[
\boxed{
-1:8064,\qquad+1:8064.
}
\]

## Independent tensor constructions

### Construction A

Direct ordered construction from:

- root addition;
- canonical structure constants;
- normalized opposite-root pairing;
- Cartan-root evaluation.

### Construction B

Alternating reconstruction from:

- canonical unordered zero-sum root triples;
- opposite-root lines;
- permutation parity.

Observed exact comparison:

    direct-only keys: 0
    reconstruction-only keys: 0
    coefficient mismatches: 0

Therefore:

\[
\boxed{
S_A=S_B.
}
\]

## Independent algebraic validation

The bracket was reconstructed independently of the sealed Cartan-form tensor.

Observed:

\[
15504
\]

ordered nonzero bracket pairs.

It satisfied:

- closure;
- antisymmetry;
- zero self-brackets.

Jacobi was checked on all:

\[
\binom{248}{3}
=
2511496
\]

canonical distinct basis triples.

Observed:

\[
\boxed{
0
}
\]

Jacobi failures.

## Invariant-form validation

The normalized symmetric bilinear form:

\[
B_0
\]

was independently reconstructed.

The two maps:

\[
B_0([X,Y],Z)
\]

and:

\[
B_0(X,[Y,Z])
\]

were constructed independently.

Observed:

    left-only keys: 0
    right-only keys: 0
    coefficient mismatches: 0

Therefore:

\[
\boxed{
B_0([X,Y],Z)
=
B_0(X,[Y,Z]).
}
\]

## Bracket recovery from the ternary tensor

Because \(B_0\) is nondegenerate:

\[
\boxed{
[v_2,v_3]
=
B_0^{-1}
\left(
g(\,\cdot\,,v_2,v_3)
\right).
}
\]

This was checked over all:

\[
248^2
=
61504
\]

ordered basis pairs.

Observed:

    recovered-only pairs: 0
    frozen-bracket-only pairs: 0
    coefficient/vector mismatches: 0

Thus the sparse ternary tensor and \(B_0\) recover the complete frozen Lie
multiplication exactly.

## Machine-readable artifact

The paper will accompany, or point to, an exact deterministic sparse tensor
artifact containing:

- basis order;
- root coordinates;
- canonical sign convention;
- invariant-form normalization;
- sector labels;
- integer coefficients.

The frozen tensor contains:

\[
16176
\]

nonzero ordered records.

Its currently sealed SHA-256 is:

    43b52b4116dfcf0dace332234b5c9dc50d95d51effb690aec8aebe39ad4f92e8

## Prior-art boundary

The manuscript must explicitly acknowledge that the following are established
prior art:

- \(E_8\);
- its 240-root system;
- the Cartan 3-form;
- the relation
  \[
  B(X,[Y,Z]);
  \]
- antisymmetric lowered structure constants;
- Chevalley bases and structure constants;
- canonical epsilon sign conventions;
- the 1120 \(A_2\) subsystem count;
- the 2240 related ternary/junction count;
- sparse computational \(E_8\) Lie brackets;
- computational Jacobi verification in general.

## Provisional novelty boundary

Pending final Phase 6A closure, the manuscript may describe as contributions:

- the explicit 16176-entry sparse normalized Cartan-form realization;
- the complete coefficient census;
- the root-incidence hypergraph representation as a computational data
  structure;
- the deterministic machine-readable tensor artifact;
- the two-route exact reconstruction;
- the complete sealed-artifact validation chain;
- the end-to-end reproducible realization.

These remain computational/data/methodological contributions unless stronger
novelty is independently established.

## Prohibited manuscript claims

Until Phase 6A is formally closed, the manuscript must not use:

- "first";
- "for the first time";
- "previously unknown";
- "new \(E_8\) invariant";
- "new Cartan 3-form";
- "new ternary structure of \(E_8\)";
- "discovery of 2240 triples";
- "discovery of 1120 \(A_2\)'s";
- "new \(E_8\) coefficient spectrum" without the qualifier that it is a
  basis-dependent explicit census.

## Safe manuscript claim

The following is provisionally safe:

> We give an exact sparse realization of the normalized Cartan 3-form of
> \(\mathfrak e_8\) in a fixed canonical Chevalley basis. We derive its
> complete nonzero coefficient census, identify its root-sector support with
> the zero-sum ternary incidence relation on the \(E_8\) roots, provide a
> deterministic machine-readable realization, and validate the result through
> independent tensor and Lie-algebra constructions.

## Dream-origin exclusion

The initiating dream is not part of the mathematical evidence presented in
the paper.

The manuscript may use:

\[
g(v_1,v_2,v_3)
\]

as notation for:

\[
B_0(v_1,[v_2,v_3]),
\]

but no dream-origin claim is required or implied.

The paper must remain mathematically complete if the reader knows nothing
about the project's initiating context.

## Other-project exclusion

The paper will not include claims concerning:

- Sri Yantra;
- E8 terrestrial grids;
- planetary geometry;
- cosmological harmonics;
- consciousness;
- physical applications not directly derived in this work.

These may motivate separate future projects but are outside the present
manuscript.

## Proposed manuscript structure

1. Introduction
2. Conventions and canonical \(E_8\) basis
3. Zero-sum root incidence and \(A_2\) structure
4. The normalized Cartan 3-form
5. Exact sparse support and coefficient census
6. Root-incidence hypergraph representation
7. Independent tensor constructions
8. Exhaustive Lie-algebra and invariant-form validation
9. Machine-readable realization and reproducibility
10. Prior-art and novelty boundary
11. Discussion

## Reproducibility policy

All headline numerical claims must be either:

1. analytically derived in the manuscript; or
2. reproducible from publicly released exact code/data.

No headline conclusion will rely solely on opaque script output.

## Target article type

Primary target:

    computational / symbolic algebra research article

Current preferred journal target:

    Journal of Symbolic Computation

Final venue selection will occur only after manuscript scope and final novelty
classification are complete.

## Next steps

1. freeze this Paper P0 protocol;
2. close the remaining Phase 6A novelty audit;
3. convert the principal computational counts into concise propositions and
   proofs;
4. prepare the manuscript bibliography;
5. draft the paper from the frozen scope;
6. run an internal referee-style audit;
7. prepare a public reproducibility release;
8. submit a preprint and then journal manuscript.

## Scope-change policy

Any later proposal to add:

- new cross-project applications;
- dream interpretation;
- speculative physics;
- Sri Yantra;
- E8 grids;
- theorem-level novelty;

requires an explicit scope amendment rather than silently entering the paper.

STATUS:

    PAPER_P0_SCOPE_AND_CLAIMS_FROZEN