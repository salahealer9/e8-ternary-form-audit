# E8 Cartan 3-form manuscript

Title: **An Exact Sparse Realization of the \(E_8\) Cartan 3-Form**

Current manuscript baseline: **v1.0**

Status:
- mathematical structure complete
- analytic support/count derivations complete
- referee-strengthening pass complete
- bibliography and prior-art audit complete
- abstract/introduction editorial pass complete
- final whole-manuscript consistency audit complete
- manuscript version 1.0 mathematically complete
- public reproducibility release `v1.0.0` complete
- GitHub repository public
- Zenodo archival DOI assigned
- DOI-bearing manuscript rebuilt and verified

## Files

- `main.tex` — current manuscript source
- `references.bib` — audited bibliography
- `e8_cartan_3form_manuscript_v1.0.pdf` — compiled manuscript version 1.0

Supporting audit records are stored under `docs/checkpoints/`, including:

- bibliography and prior-art audit;
- paper scope and claims protocol;
- analytic-results protocol;
- final referee-style manuscript audit;
- `v1.0.0` clean-clone release-candidate reproduction closeout.

## Build

```bash
latexmk -pdf main.tex
```

The current manuscript compiles to 12 pages with all citations and
cross-references resolved in the final build.

The descriptive manuscript snapshot committed to the repository is:

```text
paper/e8_cartan_3form_manuscript_v1.0.pdf
```

## Scientific scope

The manuscript presents an exact sparse realization of the normalized
\(E_8\) Cartan 3-form

\[
g(X,Y,Z)=B_0(X,[Y,Z])
\]

in a fixed \(\epsilon\)-canonical Chevalley basis.

The paper includes:

- the zero-sum root-incidence realization of the root-sector support;
- analytic derivations of the \(13{,}440\), \(2{,}736\), and \(16{,}176\)
  support counts;
- the complete coefficient census
  \[
  -2:24,\quad -1:8064,\quad +1:8064,\quad +2:24;
  \]
- a \(240\)-vertex, \(2240\)-edge linear \(3\)-uniform hypergraph
  representation of the root support;
- two algorithmically distinct exact tensor constructions;
- independent reconstruction of the Lie bracket and invariant form;
- exhaustive Jacobi validation on all
  \[
  \binom{248}{3}=2{,}511{,}496
  \]
  distinct basis triples;
- exact recovery of all
  \[
  248^2=61{,}504
  \]
  ordered basis brackets from \(g\) and \(B_0\);
- a deterministic machine-readable sparse tensor realization.

The underlying Lie-theoretic structures are classical.

The manuscript does not claim:

- a new \(E_8\) invariant;
- a new Cartan 3-form;
- a new Lie bracket;
- discovery of the established \(2240\) zero-sum root triples;
- discovery of the established \(1120\) \(A_2\) root subsystems.

The contribution is the explicit sparse realization, complete coefficient
census, root-incidence representation, deterministic data representation,
and reproducible exact validation architecture.

## Manuscript status

Version 1.0 is the mathematically audited manuscript baseline.

The manuscript is mathematically self-contained: the principal support counts
and coefficient multiplicities are derived analytically rather than inferred
solely from computation.

The repository supplies the corresponding:

- exact computational realization;
- machine-readable sparse tensor;
- validation code;
- protocol and checkpoint history;
- SHA-256 records;
- clean-clone reproducibility audit.

## Frozen reproducibility release

The frozen public reproducibility release is:

**`v1.0.0`**

GitHub repository:

<https://github.com/salahealer9/e8-ternary-form-audit>

GitHub release:

<https://github.com/salahealer9/e8-ternary-form-audit/releases/tag/v1.0.0>

Frozen release commit:

```text
2000d93478be897f0742191aafd173d71e481fbd
```

Zenodo archival DOI:

**<https://doi.org/10.5281/zenodo.22676423>**

The `v1.0.0` tag remains the immutable audited computational release.

Post-release DOI and citation metadata are maintained on the `main` branch
without altering the frozen release commit.

## Canonical tensor artifact

The canonical machine-readable sparse Cartan 3-form is:

```text
data/derived/phase3d_signed_sparse_cartan_form.json
```

It contains exactly:

```text
16176 nonzero ordered coefficients
```

with coefficient census:

```text
-2:   24
-1: 8064
+1: 8064
+2:   24
```

Frozen SHA-256:

```text
43b52b4116dfcf0dace332234b5c9dc50d95d51effb690aec8aebe39ad4f92e8
```

The artifact was regenerated from a fresh checkout and reproduced
byte-for-byte with the same SHA-256.

## Release validation

The `v1.0.0` release candidate was tested from a fresh clone outside the
development working tree.

The audit reproduced:

- 240 \(E_8\) roots;
- \(13{,}440\) ordered zero-sum root triples;
- \(2240\) unordered zero-sum triples;
- \(1120\) \(A_2\)/negation classes;
- \(13{,}440\) root--root--root Cartan-form coefficients;
- \(2{,}736\) Cartan--root--root coefficients;
- \(16{,}176\) total nonzero coefficients;
- the complete coefficient spectrum;
- exact invariant-form reconstruction;
- zero Jacobi failures;
- zero bracket-recovery discrepancies.

The automated release test suite reports:

```text
108 passed
```

The exhaustive Jacobi audit checks:

\[
\binom{248}{3}=2{,}511{,}496
\]

distinct basis triples.

Complete bracket recovery checks:

\[
248^2=61{,}504
\]

ordered basis pairs.

The detailed release closeout is stored at:

```text
docs/checkpoints/v1.0.0_release_candidate_closeout.md
```

## Citation

Repository citation metadata are provided by:

```text
CITATION.cff
```

The archived reproducibility release should be cited using:

**DOI: 10.5281/zenodo.22676423**

The manuscript itself is titled:

**An Exact Sparse Realization of the \(E_8\) Cartan 3-Form**

by Salah-Eddin Gherbi, Independent Researcher, United Kingdom.

## Release versioning

The manuscript and repository use related but distinct version conventions:

- manuscript: **Version 1.0**
- reproducibility/software release: **`v1.0.0`**

The distinction is intentional.

The manuscript version identifies the scientific paper, while the semantic
repository version identifies the exact frozen computational release and its
archival record.

## Licensing

Software source code is released under the MIT License.

The manuscript, research documentation, and original machine-readable research
data are released under the Creative Commons Attribution 4.0 International
License (CC BY 4.0), unless a file explicitly states otherwise.

See:

```text
LICENSE
LICENSES/MIT.txt
LICENSES/CC-BY-4.0.txt
```

## Submission policy

The manuscript remains mathematically complete independently of the repository.

The public GitHub repository and Zenodo archive provide the exact
computational realization, data artifact, validation suite, hashes, provenance,
and clean-clone reproducibility record supporting the finite \(E_8\)
construction reported in the paper.

The frozen `v1.0.0` release should not be rewritten or retagged. Any later
metadata, citation, or manuscript-format changes should occur after that
release while preserving the archived computational state.