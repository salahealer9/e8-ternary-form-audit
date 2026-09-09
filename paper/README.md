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
- manuscript mathematically frozen for public-release preparation
- public reproducibility release and archival DOI pending

## Files

- `main.tex` — current manuscript source
- `references.bib` — audited bibliography
- `e8_cartan_3form_manuscript_v1.0.pdf` — compiled manuscript v1.0

Supporting audit records are stored under `docs/checkpoints/`, including:
- bibliography and prior-art audit
- final referee-style manuscript audit

## Build

```bash
latexmk -pdf main.tex
```

The current manuscript compiles to 12 pages without unresolved citations,
references, LaTeX warnings, or overfull/underfull boxes.

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
- exact recovery of all \(61{,}504\) ordered basis brackets from \(g\) and
  \(B_0\);
- a deterministic machine-readable sparse tensor realization.

The underlying Lie-theoretic structures are classical. The manuscript does
not claim a new \(E_8\) invariant, a new Cartan 3-form, a new Lie bracket,
or discovery of the established \(E_8\) root-system counts used in the work.

The contribution is the explicit sparse realization, complete coefficient
census, root-incidence representation, deterministic data representation,
and reproducible exact validation architecture.

## Manuscript status

Version 1.0 is the mathematically audited manuscript baseline.

The manuscript is intended to remain mathematically self-contained:
the principal support counts and coefficient multiplicities are derived
analytically in the paper rather than inferred solely from computation.

The repository provides the corresponding exact computational realization,
machine-readable artifact, validation code, protocol history, and
reproducibility record.

## Before public release

1. Confirm author, affiliation, and contact metadata.
2. Audit repository contents for public visibility.
3. Confirm repository licensing.
4. Finalize the public-facing root `README.md`.
5. Add citation metadata, including `CITATION.cff`.
6. Confirm the complete reproducibility command sequence from a clean checkout.
7. Run the full automated test suite from the release candidate.
8. Verify all frozen artifacts and SHA-256 hashes.
9. Make the repository public.
10. Create the frozen repository release `v1.0.0`.
11. Archive release `v1.0.0` with Zenodo and obtain its DOI.
12. Replace the manuscript reproducibility placeholder with:
    - public repository URL;
    - release tag `v1.0.0`;
    - release commit hash;
    - Zenodo DOI;
    - frozen tensor SHA-256.
13. Rebuild and verify the DOI-bearing manuscript.
14. If required, adapt the generic LaTeX source to the target journal style.

## Release versioning

The manuscript and repository use related but distinct version conventions:

- manuscript: **Version 1.0**
- reproducibility/software release: **`v1.0.0`**

The public repository and Zenodo record should refer to a frozen
reproducibility release rather than to an evolving development branch.

## Submission policy

The manuscript should remain mathematically complete independently of the
repository.

The repository and Zenodo archive supply the exact computational realization,
data artifact, validation suite, hashes, and provenance needed to reproduce
the reported finite \(E_8\) construction.

No public-release DOI or repository URL should be inserted into the manuscript
until the corresponding release has been frozen and archived.