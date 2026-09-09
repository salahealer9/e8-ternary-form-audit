# Phase 6A Q8–Q15 Targeted Prior-Art Search

## Status

STATUS: PHASE6A_Q8_Q15_TARGETED_PRIOR_ART_SEARCH_COMPLETE

## Scope

This checkpoint records a targeted search for prior art relating specifically
to Q8-Q15.

It does not revisit applications, dream interpretation, Sri Yantra, E8 grids,
or physics.

## Correction to earlier Q6 classification

Q6 — the count of 2240 zero-sum / ternary E8 root triples — has direct public
prior art.

A CERN/KIAS presentation explicitly reports:

    E8 roots: 240
    junctions: 2240

Therefore:

    Q6: N1 — EXPLICIT PRIOR-ART OVERLAP

rather than N2.

The 1120 A2-subsystem count is likewise explicitly established in the
literature.

## Q8 — 240-root zero-sum 3-uniform hypergraph

Repository realization:

\[
|V|=240,
\qquad
|E|=2240.
\]

Additional properties:

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

### Search result

Substantial literature exists on combinatorial incidence structures associated
with E8 roots, including:

- A2 subsystems;
- orthogonal-root systems;
- Steiner systems;
- E8 root graphs.

No searched source was located that packages all 240 roots and the zero-sum
triple relation specifically as the same 3-uniform hypergraph with the
repository's complete census.

However the hyperedges themselves are equivalent to established A2/root-pair
data.

### Classification

Mathematical properties:

    N2

Possible explicit data representation:

    N3 CANDIDATE

No N4 theorem claim is supported.

## Q9 — Zero-sum hypergraph equals RRR Cartan-form support

Repository identity:

\[
T_{\alpha\beta\gamma}=1
\iff
\Omega_0(e_\alpha,e_\beta,e_\gamma)\neq0.
\]

### Underlying mathematics

The equivalence follows from standard root-space Lie theory:

- root grading of the bracket;
- invariant bilinear-form orthogonality;
- nondegeneracy on opposite root spaces.

Therefore:

    UNDERLYING THEOREM: N0

### Explicit representation

No searched source was located presenting the full 13,440 ordered support map
as an explicit equality with the 240-root zero-sum hypergraph.

Therefore:

    EXPLICIT FINITE REALIZATION: N2/N3 CANDIDATE

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

Searches using:

- "16176 E8";
- "13440 2736 E8";
- "E8 Cartan 3-form sparse";
- "E8 Cartan 3-form coefficients";
- equivalent lowered-structure-constant terminology;

did not locate an equivalent published census.

The result is nevertheless straightforwardly derivable once the basis and
normalization are fixed.

### Classification

    N2 — APPARENTLY UNREPORTED DERIVED CENSUS

Safe wording:

> In the stated canonical basis and normalization, the sparse Cartan 3-form
> contains 16,176 nonzero ordered coefficients.

Unsafe wording:

> E8 possesses a newly discovered set of 16,176 ternary relations.

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

No equivalent spectrum was located in the searched literature or public
software descriptions.

The spectrum depends on:

- basis convention;
- Chevalley signs;
- invariant-form normalization.

It is therefore not an intrinsic new E8 invariant.

### Classification

    N2 — APPARENTLY UNREPORTED BASIS-DEPENDENT CENSUS

## Q12 — Deterministic machine-readable Cartan-3-form dataset

Repository artifact:

    data/derived/phase3d_signed_sparse_cartan_form.json

It contains:

- basis ordering;
- root coordinates;
- normalization;
- epsilon convention;
- exact integer coefficients;
- sector labels;
- complete sparse support;
- deterministic serialization.

### Prior computational overlap

Public software already supplies machine-readable sparse E8 BRACKET structure
constants.

In particular DHL-MM supplies precomputed sparse structure constants and an
executable 248-dimensional E8 bracket.

No equivalent searched resource was located that publishes the LOWERED
Cartan 3-form itself as a deterministic sparse data artifact with the same
metadata and normalization.

### Classification

    N3 CANDIDATE — APPARENTLY NOVEL COMPUTATIONAL DATASET

This remains provisional until the full novelty audit closes.

## Q13 — Two-route exact signed-tensor reconstruction

Repository routes:

### Route A

Direct ordered construction from:

- root arithmetic;
- canonical bracket constants;
- invariant pairing;
- Cartan-root evaluation.

### Route B

Independent alternating reconstruction from:

- unordered zero-sum root triples;
- opposite-root lines;
- permutation parity.

Result:

\[
S_A=S_B
\]

entry-for-entry.

No equivalent two-route reconstruction protocol was located.

### Classification

    N3 CANDIDATE — COMPUTATIONAL METHODOLOGY

No new Lie-theoretic theorem is claimed.

## Q14 — Exhaustive independent algebra validation

Repository audit:

- complete 248-dimensional bracket reconstruction;
- all
  \[
  2,511,496
  \]
  canonical distinct basis triples checked for Jacobi;
- zero failures;
- independent bilinear reconstruction;
- exact invariance;
- sealed Cartan tensor reproduced entry-for-entry.

### Prior overlap

Public E8 software performs computational:

- Jacobi verification;
- antisymmetry checks;
- Killing-form checks.

DHL-MM reports numerical Jacobi errors of approximately machine precision.

Thus:

    COMPUTATIONAL JACOBI CHECKING ITSELF: N1

No searched source was located reproducing the repository's exact:

- exhaustive canonical-triple census;
- independently sealed prior tensor;
- algebra reconstruction;
- final exact tensor comparison.

### Classification

    N3 CANDIDATE — VALIDATION ARCHITECTURE

## Q15 — Complete reproducible realization

Repository chain:

\[
E_8\text{ roots}
\to
\text{zero-sum triple system}
\to
\text{A2 quotient}
\to
\text{root hypergraph}
\to
\text{canonical bracket signs}
\to
\text{normalized sparse Cartan 3-form}
\to
\text{independent exhaustive algebra audit}.
\]

The individual mathematical ingredients are overwhelmingly established prior
art.

No searched source was located combining them into this complete deterministic
and independently cross-validated computational object.

### Classification

    N3 CANDIDATE — STRONGEST SURVIVING NOVELTY CLAIM

## Updated Phase 6A novelty boundary

### Not novel

- E8 Cartan 3-form;
- antisymmetric rank-3 E8 structure tensor;
- E8 Chevalley structure constants;
- canonical sign conventions;
- sparse E8 bracket;
- 240-root system;
- 2240 ternary/junction count;
- 1120 A2 subsystems;
- root-space support theorem;
- computational Jacobi testing in general.

### Apparently unreported derived results

- exact 16,176 Cartan-form support census;
- exact coefficient multiplicity spectrum;
- explicit 240-root zero-sum hypergraph census in the repository's chosen
  presentation.

These are presently N2.

### Strongest candidate computational contributions

- deterministic machine-readable normalized E8 Cartan 3-form;
- two independent exact constructions;
- exact hypergraph-to-Cartan-support realization;
- exhaustive sealed-artifact validation architecture;
- complete end-to-end reproducibility chain.

These remain provisional N3.

## Current safest publication description

> We provide an exact, deterministic sparse realization of the normalized E8
> Cartan 3-form in a fixed canonical Chevalley basis, together with its
> complete coefficient census, a zero-sum root-incidence representation, two
> independent exact constructions, and an exhaustive algebra-level
> validation.

This wording describes the contribution without claiming a new invariant or
new Lie-theoretic theorem.

## Prohibited wording

At the present audit stage do not claim:

- "new E8 invariant";
- "new E8 Cartan form";
- "discovery of 2240 E8 triples";
- "first explicit E8 Lie bracket";
- "first computational E8 structure constants";
- "new E8 coefficient spectrum" as an invariant;
- "first" or "previously unknown" without further verification.

## Remaining novelty task

Before a publication-level novelty claim is finalized, one further pass should
check:

1. full-text papers and appendices containing explicit E8 tensor tables;
2. GAP, Sage, Magma and LiE computational representations;
3. downloadable supplementary datasets;
4. Zenodo/Figshare/data repositories;
5. GitHub/GitLab code not well indexed by general search;
6. theses using fully lowered E8 structure tensors.

Until that pass is complete:

    N3 STATUS: PROVISIONAL