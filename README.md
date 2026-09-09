# E8 Ternary Form Audit

**Exact sparse realization of the \(E_8\) Cartan 3-form**

This repository provides the computational realization, exact data artifacts,
validation suite, and reproducibility record accompanying the manuscript

> **An Exact Sparse Realization of the \(E_8\) Cartan 3-Form**  
> Salah-Eddin Gherbi  
> Independent Researcher, United Kingdom  
> Manuscript version 1.0, September 2026

## Main result

For the normalized Cartan 3-form

\[
g(X,Y,Z)=B_0(X,[Y,Z])
\]

on the Chevalley \(\mathbb Q\)-form of \(\mathfrak e_8\), in the fixed
\(\epsilon\)-canonical Chevalley basis used in this repository, the complete
ordered basis domain contains

\[
248^3=15{,}252{,}992
\]

triples, of which exactly

\[
16{,}176
\]

have nonzero coefficient.

The support decomposes as

\[
13{,}440\quad\text{root--root--root}
\]

and

\[
2{,}736\quad\text{Cartan--root--root}.
\]

The complete nonzero coefficient census is

\[
-2:24,\qquad
-1:8064,\qquad
+1:8064,\qquad
+2:24.
\]

On root vectors,

\[
g(e_\alpha,e_\beta,e_\gamma)\neq0
\quad\Longleftrightarrow\quad
\alpha+\beta+\gamma=0.
\]

The unsigned root-sector support is therefore represented by a linear
\(3\)-uniform hypergraph with

\[
240\ \text{vertices},\qquad
2240\ \text{hyperedges},
\]

with degree \(28\) at every vertex.

## Validation

The repository implements two algorithmically distinct exact constructions of
the sparse Cartan 3-form.

The resulting signed sparse tensors agree entry-for-entry.

The Lie bracket and normalized invariant form are also reconstructed
independently of the sealed tensor. The resulting \(248\)-dimensional algebra:

- closes exactly in the frozen basis;
- is antisymmetric;
- satisfies the Jacobi identity on all
  \[
  \binom{248}{3}=2{,}511{,}496
  \]
  distinct basis triples;
- reproduces the sealed Cartan 3-form exactly through
  \[
  B_0(X,[Y,Z]);
  \]
- is recovered exactly from the tensor and \(B_0^{-1}\) on all
  \[
  248^2=61{,}504
  \]
  ordered basis pairs.

All support and equality decisions use integer or rational arithmetic rather
than floating-point tolerances.

## Frozen tensor artifact

The deterministic sparse Cartan 3-form contains \(16{,}176\) nonzero ordered
entries.

Canonical artifact:

```text
data/derived/phase3d_signed_sparse_cartan_form.json
```

SHA-256:

```text
43b52b4116dfcf0dace332234b5c9dc50d95d51effb690aec8aebe39ad4f92e8
```

## Manuscript

The current manuscript is:

```text
paper/e8_cartan_3form_manuscript_v1.0.pdf
```

Source:

```text
paper/main.tex
paper/references.bib
```

The manuscript is mathematically self-contained: its principal support counts
and coefficient multiplicities are derived analytically rather than inferred
only from computer output.

## Reproducibility

Python 3.11 or later is required.

Create an environment and install the project with development dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Run the complete automated test suite:

```bash
pytest
```

Individual deterministic phase runners are available under `scripts/`.

The frozen `v1.0.0` release was reproduced from a fresh checkout. The
release-candidate audit records:

- 108/108 automated tests passing;
- exact regeneration of the canonical sparse tensor;
- byte-for-byte preservation of its SHA-256;
- zero failures in the exhaustive Jacobi audit;
- zero discrepancies in complete bracket recovery.

The detailed release-candidate reproduction record is:

```text
docs/checkpoints/v1.0.0_release_candidate_closeout.md
```

## Repository structure

```text
data/          reference and derived machine-readable artifacts
docs/          methodology, preregistration, derivations, and checkpoints
paper/         manuscript source, bibliography, and compiled manuscript
scripts/       deterministic phase and audit runners
src/           reusable Python implementation
tests/         automated validation suite
CITATION.cff   citation metadata
```

## Scientific scope and novelty boundary

The Cartan 3-form, the \(E_8\) Lie algebra, Chevalley bases, the \(E_8\) root
system, and the associated \(A_2\) root-system counts are classical.

This project does **not** claim a new \(E_8\) invariant, a new Cartan 3-form,
a new Lie bracket, or discovery of the established \(2240\) zero-sum triples
or \(1120\) \(A_2\) subsystems.

The contribution is the explicit sparse realization, complete coefficient
census, root-incidence representation, deterministic machine-readable
artifact, and exact reproducibility and cross-validation architecture.

## Project provenance

The investigation originally began from the remembered three-argument notation

\[
g(v_1,v_2,v_3).
\]

The notation was reported after a dream and was treated strictly as a
hypothesis-generating observation, not as mathematical evidence.

The preregistered project explicitly prohibited treating notation similarity,
visual analogy, numerology, or assumptions about the origin of the dream as
scientific evidence.

The original scope, candidate classes, preregistration, and interpretation
criteria are retained under `docs/` as part of the research provenance.

## Citation

Citation metadata are provided in:

```text
CITATION.cff
```

The frozen reproducibility release is archived on Zenodo:

**DOI: [10.5281/zenodo.22676423](https://doi.org/10.5281/zenodo.22676423)**

## Archival release

The frozen reproducibility release is:

**v1.0.0**

GitHub release:

https://github.com/salahealer9/e8-ternary-form-audit/releases/tag/v1.0.0

Release commit:

```text
2000d93478be897f0742191aafd173d71e481fbd
```

Zenodo DOI:

**[10.5281/zenodo.22676423](https://doi.org/10.5281/zenodo.22676423)**

The canonical sparse Cartan 3-form artifact is:

```text
data/derived/phase3d_signed_sparse_cartan_form.json
```

SHA-256:

```text
43b52b4116dfcf0dace332234b5c9dc50d95d51effb690aec8aebe39ad4f92e8
```

## Licensing

Software source code is released under the MIT License.

The manuscript, research documentation, and original machine-readable research
data are released under the Creative Commons Attribution 4.0 International
License (CC BY 4.0), unless a file explicitly states otherwise.

See `LICENSE` and `LICENSES/` for details.