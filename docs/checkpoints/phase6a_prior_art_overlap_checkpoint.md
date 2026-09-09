# Phase 6A Prior-Art Overlap Checkpoint

## Status

STATUS: PHASE6A_PRIOR_ART_OVERLAP_CHECKPOINT_OPEN_FINDINGS_FROZEN

## Purpose

This checkpoint records the first claim-by-claim novelty classification after
the Phase 6A novelty-audit protocol was frozen.

It intentionally separates:

- established mathematical theory;
- explicit published prior art;
- straightforward derived censuses;
- potentially novel computational representation.

No global novelty claim is made.

## Current global boundary

At this checkpoint:

\[
\boxed{
\text{NO NEW }E_8\text{ INVARIANT OR LIE-ALGEBRA STRUCTURE IS CLAIMED}.
}
\]

The potentially publishable novelty, if it survives further searching, lies
instead in:

1. an explicit Cartan-3-form sparse census;
2. an E8 zero-sum root hypergraph representation;
3. deterministic machine-readable realization;
4. independent reconstruction and validation architecture.

## Q1 — Cartan 3-form itself

Claim:

\[
\Omega(X,Y,Z)=B(X,[Y,Z]).
\]

Classification:

    N0 — ESTABLISHED STANDARD RESULT

Cartan 3-forms on simple Lie algebras are established prior art.

Reference anchor:

Hông Vân Lê,
"Geometric structures associated with a simple Cartan 3-form",
Journal of Geometry and Physics 70 (2013), 205–223.

No novelty claim is permitted for the existence or definition of the form.

## Q2 — Completely antisymmetric rank-3 E8 tensor

Claim:

Lowering the remaining index of the E8 structure constants using the
Cartan-Killing form produces a completely antisymmetric rank-3 invariant
tensor.

Classification:

    N0 — ESTABLISHED STANDARD RESULT

Explicit physics literature already works with the E8 structure constants in
fully antisymmetric form.

Therefore the identification

\[
g_{abc}=B_{ad}f^d{}_{bc}
\]

is not a new E8 object.

## Q3 — Explicit E8 Chevalley structure constants

Classification:

    N0 / N1 — ESTABLISHED AND EXPLICIT PRIOR ART

Explicit E8 commutation data have long appeared in the literature.

More recently, Geck and Lang give explicit formulae for canonical Chevalley
structure constants for finite-dimensional simple Lie algebras, including the
simply-laced E-series.

Therefore explicit calculation of:

\[
N_{\alpha,\beta}
\]

for E8 is not itself novel.

## Q4 — Canonical epsilon-Chevalley sign system

Classification:

    N0 — ESTABLISHED STANDARD RESULT

The canonical epsilon-dependent Chevalley basis and its corresponding
structure constants are covered by the Geck-Lang/Lusztig framework.

The repository's implementation and verification may be useful, but the
underlying sign theory is prior art.

## Q5 — Sparse E8 Lie bracket implementation

Classification:

    N1 — EXPLICIT PUBLIC PRIOR-ART OVERLAP

A public 2026 software package, DHL-MM, implements sparse Lie brackets for the
exceptional Lie algebras.

For E8 it reports:

    dimension: 248
    roots: 240
    nonzero f entries: 16694
    full tensor domain: 15252992

The repository therefore must NOT claim novelty for:

- sparse storage of the E8 bracket;
- gather/multiply/scatter evaluation of E8 multiplication;
- a 248-dimensional computational E8 multiplication table.

### Relation to this repository

The public count:

\[
16694
\]

is consistent with the scalar expansion of the bracket sectors reconstructed
here.

The present project's distinct Cartan-3-form sparse count is:

\[
16176,
\]

which is a different lowered trilinear object.

Thus DHL-MM overlaps strongly with the BRACKET layer but does not, from the
material located so far, establish prior publication of the exact Phase 3D
Cartan-form census.

## Q6 — Zero-sum E8 root triple census

Repository result:

\[
2240
\]

unordered triples satisfying:

\[
\alpha+\beta+\gamma=0,
\]

equivalently:

\[
13440
\]

ordered triples.

Classification:

    N2 — APPARENTLY UNREPORTED / ROUTINELY DERIVED CENSUS

Important prior art establishes:

\[
13440
\]

ordered pairs of E8 roots having inner product \(-1\), and:

\[
1120
\]

root subsystems of type:

\[
A_2.
\]

Every A2 root subsystem contains exactly two opposite zero-sum unordered
triples.

Therefore:

\[
1120\times2=2240.
\]

Consequently the repository's 2240 zero-sum count is mathematically
equivalent to established A2 combinatorics.

Even if the exact phrase "2240 unordered zero-sum triples" proves absent from
the literature, this is not presently a candidate new theorem.

Safe classification:

\[
\boxed{
\text{useful explicit census, but directly derivable from known A2 data}.
}
\]

## Q7 — 1120 A2 quotient classes

Classification:

    N0 — ESTABLISHED STANDARD RESULT

The number:

\[
1120
\]

of A2 root subsystems in E8 is explicitly established in the literature.

Manivel's ternary E8 model also contains 1120 relevant triads.

The Phase 2B quotient therefore reproduces known E8 structure rather than
establishing a new count.

## Q8 — Three-uniform zero-sum root hypergraph

Repository object:

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

Additional repository census:

- every vertex degree:
  \[
  28;
  \]
- pair codegree:
  \[
  0\text{ or }1;
  \]
- active root pairs:
  \[
  6720;
  \]
- negation edge-orbits:
  \[
  1120.
  \]

Current classification:

    OPEN — N2/N3 CANDIDATE

Searches so far have located extensive combinatorial treatments of E8 roots,
A2 subsystems, orthogonal-root incidence systems, and Steiner systems.

No equivalent source has yet been located that presents the FULL 240-root
zero-sum relation specifically as this 3-uniform hypergraph with the same
complete census.

However:

- the hyperedges are equivalent to known A2 data;
- degree 28 follows immediately from the known local root counts;
- linearity follows from uniqueness of the third root
  \[
  -(\alpha+\beta).
  \]

Therefore theorem-level novelty is presently unlikely.

Potential surviving contribution:

    N3 — explicit combinatorial representation / dataset

rather than:

    N4 — new mathematical theorem.

## Q9 — Root hypergraph equals RRR Cartan-form support

Repository identity:

\[
T_{\alpha\beta\gamma}=1
\iff
\Omega(e_\alpha,e_\beta,e_\gamma)\ne0.
\]

Split classification:

### Underlying theorem

    N0

The root-space grading of a semisimple Lie algebra and the orthogonality of
root spaces under the invariant bilinear form imply that:

\[
B(e_\alpha,[e_\beta,e_\gamma])
\]

is nonzero precisely in the appropriate zero-sum root case.

This is standard Lie theory.

### Explicit finite support identification

    OPEN — N2/N3 CANDIDATE

No located source has yet been found packaging the 13,440 ordered support
positions as exact equality with the 240-root zero-sum hypergraph.

The novelty, if any, is in the explicit finite combinatorial realization, not
the underlying implication.

## Q10 — Complete sparse normalized Cartan-3-form census

Repository result:

\[
RRR=13440,
\]

\[
HRR=2736,
\]

\[
TOTAL=16176.
\]

Current classification:

    OPEN — N2 CANDIDATE

No source located so far reports this exact 16,176 nonzero ordered coefficient
count in the same frozen Chevalley/simple-Cartan basis and normalization.

However the count is readily derivable once the basis, root system, invariant
pairing, and bracket conventions are fixed.

Therefore the strongest likely mathematical classification is presently:

    N2 — apparently unreported explicit census

unless a deeper structural significance is subsequently demonstrated.

## Q11 — Exact coefficient spectrum

Repository spectrum:

\[
-2:24,
\]

\[
-1:8064,
\]

\[
+1:8064,
\]

\[
+2:24.
\]

Current classification:

    OPEN — N2 CANDIDATE

No equivalent exact spectrum has yet been located.

It is nevertheless a basis/normalization-dependent census and must not be
presented as a new invariant of E8.

In particular the values depend on the chosen normalized Chevalley basis and
bilinear form convention.

Safe potential wording:

> We report the complete coefficient spectrum in the stated canonical basis
> and normalization.

Unsafe wording:

> We discover a new E8 spectrum.

## Q12 — Deterministic machine-readable Cartan-form artifact

Repository contribution:

- explicit 248-element basis order;
- exact integer coefficients;
- canonical sign metadata;
- invariant-form normalization metadata;
- sparse coefficient records;
- deterministic JSON serialization;
- SHA-256 identity.

Current classification:

    OPEN — N3 CANDIDATE

No equivalent deterministic machine-readable Cartan-3-form dataset has yet
been located.

This is one of the strongest potential computational novelty claims.

## Q13 — Two-route exact signed tensor reconstruction

Repository methodology:

### Route A

Direct ordered construction from:

- root addition;
- canonical structure constants;
- opposite-root pairing;
- Cartan-root evaluation.

### Route B

Independent reconstruction from:

- canonical unordered zero-sum triples;
- opposite-root lines;
- permutation parity.

Result:

    exact key equality
    exact coefficient equality
    zero mismatches

Current classification:

    OPEN — N3 CANDIDATE

No equivalent two-route audit methodology has yet been located.

The contribution is methodological/computational rather than a new Lie
theorem.

## Q14 — Exhaustive independent algebra validation

Repository validation includes:

\[
2,511,496
\]

canonical distinct basis triples tested for Jacobi.

Observed:

\[
0
\]

failures.

The bilinear form was reconstructed independently and exact invariance was
verified.

The algebra-derived trilinear tensor then reproduced the already sealed
16,176-entry Phase 3D tensor exactly.

Current classification:

    OPEN — N3 CANDIDATE

Existing public E8 software tests Jacobi and Killing-form consistency, but the
public material located so far does not reproduce this exact exhaustive,
preregistered, sealed-artifact comparison architecture.

Therefore the possible novelty lies in the validation protocol and
reproducibility chain.

## Q15 — Complete reproducible realization

Repository chain:

\[
E_8\text{ roots}
\]

\[
\downarrow
\]

\[
\text{zero-sum ternary incidence}
\]

\[
\downarrow
\]

\[
\text{A2 quotient}
\]

\[
\downarrow
\]

\[
\text{canonical signed Lie bracket}
\]

\[
\downarrow
\]

\[
\text{normalized sparse Cartan 3-form}
\]

\[
\downarrow
\]

\[
\text{independent exhaustive algebra validation}.
\]

Current classification:

    OPEN — N3 CANDIDATE

No single equivalent published/package implementation containing this complete
chain has yet been located.

This is presently the strongest candidate novelty claim.

## Current classification table

| Claim | Preliminary class | Confidence |
|---|---|---|
| Q1 Cartan 3-form | N0 | HIGH |
| Q2 antisymmetric E8 rank-3 tensor | N0 | HIGH |
| Q3 explicit structure constants | N0/N1 | HIGH |
| Q4 canonical epsilon signs | N0 | HIGH |
| Q5 sparse E8 bracket | N1 | HIGH |
| Q6 2240 zero-sum triple census | N2 | HIGH |
| Q7 1120 A2 classes | N0 | HIGH |
| Q8 root hypergraph | OPEN N2/N3 | MEDIUM |
| Q9 hypergraph / RRR support equality | N0 theorem + OPEN N2/N3 representation | MEDIUM |
| Q10 16176 sparse-form census | OPEN N2 | MEDIUM |
| Q11 coefficient spectrum | OPEN N2 | MEDIUM |
| Q12 deterministic dataset | OPEN N3 | MEDIUM |
| Q13 two-route reconstruction | OPEN N3 | MEDIUM |
| Q14 exhaustive validation architecture | OPEN N3 | MEDIUM |
| Q15 complete reproducible pipeline | OPEN N3 | MEDIUM |

## Interim novelty boundary

The evidence currently points away from:

\[
\boxed{
\text{a new E8 mathematical invariant}
}
\]

and toward:

\[
\boxed{
\text{a potentially new explicit computational/combinatorial realization
of an established E8 invariant}.
}
\]

More specifically, the likely contribution is a combination of:

1. the 240-root zero-sum hypergraph as an explicit data object;
2. its exact realization as root-sector support of the Cartan 3-form;
3. the complete 16,176-entry normalized sparse tensor census;
4. deterministic machine-readable publication of that tensor;
5. independent two-route reconstruction;
6. exhaustive algebra-level validation against a previously sealed artifact.

## Next audit target

The next literature pass must concentrate exclusively on Q8-Q15.

Priority searches:

1. E8 root incidence geometries and partial linear spaces;
2. combinatorial descriptions of A2 subsystems;
3. explicit Cartan-3-form coordinate tables;
4. machine-readable E8 invariant tensors;
5. Sage/GAP/Magma/Mathematica E8 tensor datasets;
6. GitHub/GitLab packages containing lowered E8 structure constants;
7. computational papers performing exhaustive E8 Jacobi validation;
8. datasets or appendices giving exact coefficient spectra.

Until this search is complete:

    N3 CLAIM: PROVISIONAL

and:

    FIRST / PREVIOUSLY UNPUBLISHED: PROHIBITED