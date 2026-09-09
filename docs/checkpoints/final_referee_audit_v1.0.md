# Final whole-paper referee audit — manuscript v1.0

## Status

STATUS: MANUSCRIPT_V1.0_REFEREE_AUDIT_PASS

The audit found no contradiction in the headline counts, sector decompositions,
coefficient spectrum, Jacobi census, bracket-recovery domain, or stated novelty
boundary.

## Referee-level amendments from v0.4

1. Basis-element notation is now explicit: `b_a` denotes the `a`th element of
   the frozen basis `\mathcal B`. This avoids confusion between basis elements
   and the invariant form `B_0`.
2. The zero-sum-triple / `A_2` correspondence is proved explicitly: a zero-sum
   triple has pairwise inner product `-1`, its six signed roots form an `A_2`
   subsystem, negation gives the same subsystem, and each `A_2` subsystem has
   exactly two zero-sum triples.
3. In the bracket-recovery component formula, `B_{0,ad}=B_0(b_a,b_d)` and
   `B_0^{ad}` is explicitly identified as the inverse matrix.
4. Prior-art wording now consistently describes the two tensor routes as
   algorithmically distinct rather than mathematically independent.

## Exact arithmetic cross-checks

The following manuscript counts were independently recomputed:

- `248^3 = 15,252,992`
- `C(248,3) = 2,511,496`
- `240*56 = 13,440`
- `13,440/6 = 2,240`
- `2,240/2 = 1,120`
- `3*2,240 = 6,720` active unordered root pairs
- `8*114 = 912`
- `3*8*114 = 2,736`
- `13,440 + 2,736 = 16,176`
- `8*6 = 48` magnitude-two HRR entries
- `2,736 - 48 = 2,688`
- `2,688/2 = 1,344`
- `6,720 + 1,344 = 8,064`
- `24 + 8,064 + 8,064 + 24 = 16,176`
- `248^2 = 61,504`

Jacobi sector census:

- HHH: `C(8,3) = 56`
- HHR: `C(8,2)*240 = 6,720`
- HRR: `8*C(240,2) = 229,440`
- RRR: `C(240,3) = 2,275,280`
- total: `2,511,496`

All agree with the manuscript.

## Citation and cross-reference audit

- citation keys used: 11
- bibliography entries: 11
- missing bibliography entries: 0
- unused bibliography entries: 0
- labels defined: 36
- unresolved `\ref` / `\eqref` targets: 0
- duplicate labels: 0

## Compile and visual audit

The v0.5 manuscript was rebuilt from `main_v0.5.tex` and the audited
bibliography.

Result:

- pages: 12
- final LaTeX warnings: 0
- unresolved citations: 0
- unresolved references: 0
- overfull boxes: 0
- underfull boxes: 0

Representative rendered pages were visually inspected after compilation. No
clipped text, overlap, broken glyphs, or table-layout defects were observed.

## Claims boundary

The manuscript remains appropriately conservative:

- no new `E_8` invariant is claimed;
- no new Cartan 3-form is claimed;
- no discovery claim is made for 2,240 zero-sum triples or 1,120 `A_2`
  subsystems;
- no first-ever claim is made for sparse `E_8` structure constants;
- the contribution is framed as explicit sparse realization, coefficient
  census, root-incidence representation, deterministic data, and exact
  reproducibility/validation architecture.

## Intentionally unresolved before archival release

These are release tasks, not manuscript defects:

1. replace the repository/DOI placeholder after the public tagged release is
   archived with Zenodo;
2. insert the final release tag and commit hash;
3. confirm final author/contact metadata;
4. remove the draft-version label when preparing the submission version;
5. adapt to the selected journal class/style if required.

## Conclusion

MANUSCRIPT_V1.0_REFEREE_AUDIT: PASS

The mathematical manuscript is ready to move from internal drafting to public
reproducibility-release preparation, subject only to the archival metadata
items listed above.
