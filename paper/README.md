# E8 Cartan 3-form manuscript

Working title: **An Exact Sparse Realization of the \(E_8\) Cartan 3-Form**

Current manuscript baseline: **v0.3**

Status:
- mathematical structure complete
- analytic support/count derivations complete
- referee-strengthening pass complete
- bibliography and prior-art audit complete
- final abstract/introduction editorial pass pending
- public reproducibility release and archival DOI pending

## Files

- `main.tex` — current manuscript source
- `references.bib` — audited bibliography
- `e8_cartan_3form_manuscript_v0.3.pdf` — compiled manuscript snapshot
- `bibliography_audit_v0.3.md` — source and bibliography audit record

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
- two algorithmically distinct exact tensor constructions;
- independent reconstruction of the Lie bracket and invariant form;
- exhaustive Jacobi validation;
- exact recovery of all \(61{,}504\) ordered basis brackets from \(g\) and
  \(B_0\);
- a deterministic machine-readable sparse tensor realization.

The underlying Lie-theoretic structures are classical. The manuscript does
not claim a new \(E_8\) invariant or a new Cartan 3-form.

## Before public release

1. Complete the final abstract/introduction editorial pass.
2. Perform a final manuscript consistency and referee-style audit.
3. Confirm all author, affiliation, and contact metadata.
4. Confirm repository licensing and public-release contents.
5. Make the repository public.
6. Create a frozen tagged release.
7. Archive the release with Zenodo and obtain the DOI.
8. Replace the reproducibility placeholder in the manuscript with:
   - public repository URL;
   - release tag;
   - release commit hash;
   - Zenodo DOI;
   - frozen tensor SHA-256.
9. Rebuild and verify the final manuscript.
10. Adapt the generic LaTeX source to the target journal style if required.

## Submission policy

The public repository and archival DOI should refer to a frozen reproducibility
release rather than to an evolving development state.

The manuscript should be mathematically complete independently of the
repository, while the repository supplies the exact computational realization,
data artifact, validation code, and reproducibility record.