# Phase 3D Signed Sparse Cartan 3-Form Protocol

## Status

STATUS: PHASE3D_SIGNED_SPARSE_CARTAN_FORM_PROTOCOL_FROZEN

## Purpose

Phase 3D constructs the complete signed sparse representation of the
normalized Cartan 3-form

\[
\Omega_0(X,Y,Z)=B_0(X,[Y,Z])
\]

on the frozen 248-element basis of

\[
\mathfrak e_8.
\]

This phase combines the previously independent layers:

1. E8 root geometry;
2. zero-sum ternary incidence;
3. root-space Cartan support;
4. full basis-independent sector support;
5. canonical Chevalley signs;
6. normalized invariant bilinear form.

The result will be an explicit scalar-valued alternating trilinear form in
the frozen basis.

## Dependencies

Phase 3C canonical basis and normalization completed at:

    b26d208

Phase 3C protocol was frozen at:

    7fb9e0b

Phase 3B full sector support completed at:

    9226f83

Phase 3A root-space Cartan support completed at:

    f66c18b

Phase 2C unsigned ternary incidence completed at:

    c8dfd1c

No Phase 3D signed sparse tensor has been constructed before this protocol
freeze.

## Frozen basis

The basis ordering is:

\[
\mathscr B^\epsilon
=
(
h_1,\ldots,h_8,
e_{\alpha_0}^\epsilon,\ldots,e_{\alpha_{239}}^\epsilon
),
\]

where the roots are in the already frozen deterministic lexicographic order.

Basis indices are:

\[
0,\ldots,7
\]

for the Cartan basis vectors

\[
h_1,\ldots,h_8,
\]

and

\[
8,\ldots,247
\]

for the 240 root vectors.

Thus

\[
\dim\mathfrak e_8=248.
\]

## Tensor domain

The complete ordered basis-triple domain contains

\[
248^3
=
15{,}252{,}992
\]

positions.

Phase 3D will NOT allocate a dense array of this size.

Only nonzero coefficients will be stored.

## Sparse entry

A nonzero coefficient is represented by an ordered quadruple

\[
(i,j,k,c),
\]

where

\[
i,j,k\in\{0,\ldots,247\}
\]

and

\[
c
=
\Omega_0(
\mathscr B_i,
\mathscr B_j,
\mathscr B_k
).
\]

Zero coefficients are omitted.

All entries must be stored in deterministic lexicographic order by

\[
(i,j,k).
\]

## Frozen nonzero sectors

Phase 3B established that only two basis-independent sectors can be nonzero:

### RRR

Three root vectors satisfying

\[
\alpha+\beta+\gamma=0.
\]

### HRR

One Cartan vector and two opposite root vectors.

The sectors

\[
HHR
\]

and

\[
HHH
\]

vanish identically.

Phase 3D must preserve this architecture.

## RRR coefficient rule

For

\[
\alpha+\beta+\gamma=0,
\]

Phase 3C established

\[
\boxed{
\Omega_0(
e_\alpha^\epsilon,
e_\beta^\epsilon,
e_\gamma^\epsilon
)
=
N_{\beta,\gamma}^\epsilon
(-1)^{\operatorname{ht}(\alpha)}.
}
\]

Every nonzero RRR coefficient must therefore belong to

\[
\{-1,+1\}.
\]

No Phase 2C Boolean support value may be used to assign the coefficient sign.

## Direct RRR construction

The primary RRR construction will proceed from ordered root pairs

\[
(\beta,\gamma).
\]

For each ordered pair:

1. compute
   \[
   \beta+\gamma;
   \]
2. retain the pair only if the sum is a root;
3. set
   \[
   \alpha=-(\beta+\gamma);
   \]
4. obtain
   \[
   N_{\beta,\gamma}^\epsilon
   \]
   from the frozen Phase 3C canonical structure-constant rule;
5. obtain
   \[
   B_0(e_\alpha,e_{-\alpha})
   \]
   from the Phase 3C invariance-derived pairing;
6. assign
   \[
   \Omega_0(e_\alpha,e_\beta,e_\gamma)
   =
   N_{\beta,\gamma}^\epsilon
   B_0(e_\alpha,e_{-\alpha}).
   \]

The Phase 2C tensor must not be consulted during this construction.

## Expected RRR support

Phase 3A independently established:

\[
13440
\]

ordered root-root-root support positions.

Therefore Phase 3D expects:

\[
\boxed{
|\operatorname{supp}_{RRR}\Omega_0|
=
13440.
}
\]

This number is a validation target only.

## RRR cyclic consistency

For every zero-sum triple,

\[
\alpha+\beta+\gamma=0,
\]

the three cyclic expressions

\[
N_{\beta,\gamma}^\epsilon
B_0(e_\alpha,e_{-\alpha}),
\]

\[
N_{\gamma,\alpha}^\epsilon
B_0(e_\beta,e_{-\beta}),
\]

and

\[
N_{\alpha,\beta}^\epsilon
B_0(e_\gamma,e_{-\gamma})
\]

must agree exactly.

This is required because cyclic permutations of an alternating 3-form are
even permutations.

Any discrepancy is a Phase 3D failure.

## HRR coefficient rule

For a simple Cartan basis vector

\[
h_i
\]

and root

\[
\alpha,
\]

Phase 3C established

\[
\boxed{
\Omega_0(
h_i,
e_\alpha,
e_{-\alpha}
)
=
(-1)^{\operatorname{ht}(\alpha)}
\alpha(h_i).
}
\]

Because E8 is simply laced,

\[
\alpha(h_i)
=
\alpha\cdot\alpha_i.
\]

Possible values are

\[
-2,-1,0,+1,+2.
\]

Only nonzero values produce sparse tensor entries.

## Direct HRR construction

The primary HRR construction must evaluate all three possible Cartan
placements directly from the defining bracket rules.

Let

\[
s_\alpha
=
B_0(e_\alpha,e_{-\alpha})
=
(-1)^{\operatorname{ht}(\alpha)}.
\]

For an ordered root pair

\[
(e_\alpha,e_{-\alpha}),
\]

the three direct formulas are:

### Cartan first

\[
\boxed{
\Omega_0(
h_i,
e_\alpha,
e_{-\alpha}
)
=
+s_\alpha\alpha(h_i).
}
\]

### Cartan second

\[
\boxed{
\Omega_0(
e_\alpha,
h_i,
e_{-\alpha}
)
=
-s_\alpha\alpha(h_i).
}
\]

### Cartan third

\[
\boxed{
\Omega_0(
e_\alpha,
e_{-\alpha},
h_i
)
=
+s_\alpha\alpha(h_i).
}
\]

The opposite root ordering must be evaluated independently by replacing

\[
\alpha
\]

with

\[
-\alpha.
\]

No permutation-sign expansion may be used by the primary HRR constructor.

## Scalar HRR support count

Phase 3B established 720 basis-independent HRR functional blocks.

After fixing the Cartan basis in Phase 3C, some individual scalar
coefficients vanish because

\[
\alpha(h_i)=0.
\]

For each fixed simple Cartan vector \(h_i\):

- two roots have pairing magnitude 2:
  \[
  \pm\alpha_i;
  \]
- 112 roots have pairing magnitude 1;
- 126 roots are orthogonal.

Therefore:

\[
114
\]

of the 240 roots give nonzero scalar coefficients for a fixed Cartan basis
vector in a fixed Cartan position.

Across eight Cartan basis vectors:

\[
8\times114=912
\]

nonzero ordered coefficients occur with the Cartan argument in one fixed
position.

Across all three Cartan placements:

\[
\boxed{
|\operatorname{supp}_{HRR}\Omega_0|
=
3\times912
=
2736.
}
\]

This is a validation expectation.

It must not be used to stop or define the construction.

## Unordered HRR basis triples

Because

\[
\alpha
\]

and

\[
-\alpha
\]

belong to the same opposite-root line, the 912 fixed-position oriented
coefficients correspond to

\[
456
\]

unordered nonzero basis triples of type

\[
\{h_i,e_\alpha,e_{-\alpha}\}.
\]

The expected decomposition is:

\[
448
\]

unordered triples with coefficient magnitude 1, and

\[
8
\]

unordered triples with coefficient magnitude 2.

Each unordered triple has six distinct ordered permutations.

Therefore:

\[
448\times6=2688
\]

ordered HRR entries have magnitude 1, and

\[
8\times6=48
\]

have magnitude 2.

Total:

\[
2688+48=2736.
\]

## HRR coefficient spectrum expectation

Alternation gives three positive and three negative coefficients in every
six-element permutation orbit.

Therefore the expected HRR scalar coefficient spectrum is:

\[
-2:
\quad24,
\]

\[
-1:
\quad1344,
\]

\[
+1:
\quad1344,
\]

\[
+2:
\quad24.
\]

This is a validation target only.

## Full nonzero support count

The RRR and HRR sectors are disjoint.

Therefore the expected complete sparse support contains

\[
13440+2736
=
\boxed{
16176
}
\]

ordered nonzero coefficients.

The full ordered basis domain contains

\[
15252992
\]

positions.

Thus the expected sparse support density is

\[
\frac{16176}{15252992}
\approx
0.001060513242.
\]

This is approximately

\[
0.1060513242\%.
\]

## Full coefficient spectrum expectation

The RRR sector consists entirely of coefficients

\[
\pm1.
\]

By alternation of the 2240 unordered zero-sum root triples, the expected RRR
spectrum is:

\[
-1:
\quad6720,
\]

\[
+1:
\quad6720.
\]

Adding the HRR sector gives the expected full sparse coefficient spectrum:

\[
\boxed{
-2:
24,
}
\]

\[
\boxed{
-1:
8064,
}
\]

\[
\boxed{
+1:
8064,
}
\]

\[
\boxed{
+2:
24.
}
\]

No other nonzero coefficient magnitude is expected.

## Primary construction independence

The primary sparse tensor must be constructed directly from:

- root arithmetic;
- frozen canonical structure constants;
- frozen invariant bilinear pairing;
- Cartan-root evaluation;
- Lie bracket sector rules.

It must NOT construct coefficients by taking an unsigned tensor and assigning
permutation signs afterward.

## Independent alternating reconstruction

Phase 3D must contain a second construction that is intentionally different
from the primary ordered construction.

### RRR reconstruction

Start with each canonical unordered Phase 2A zero-sum root triple

\[
i<j<k.
\]

Evaluate the coefficient in that one frozen ordering.

Generate all six permutations using permutation parity.

### HRR reconstruction

Start with each unordered opposite-root line

\[
\{\alpha,-\alpha\}.
\]

Choose one deterministic root representative.

For every Cartan basis vector

\[
h_i
\]

with

\[
\alpha(h_i)\neq0,
\]

form one canonical unordered basis triple

\[
\{h_i,e_\alpha,e_{-\alpha}\}.
\]

Evaluate one deterministic ordering directly.

Generate its other five orderings by alternation.

## Exact two-route comparison

Let

\[
S_{\mathrm{direct}}
\]

be the primary directly evaluated sparse coefficient map.

Let

\[
S_{\mathrm{alt}}
\]

be the independently reconstructed alternating map.

Phase 3D must compare:

1. key sets;
2. coefficient values.

Required:

\[
\boxed{
S_{\mathrm{direct}}
=
S_{\mathrm{alt}}.
}
\]

The comparison must report separately:

- direct-only keys;
- reconstruction-only keys;
- shared keys with differing coefficients.

All three discrepancy counts must be zero.

## Full alternation

For every nonzero entry

\[
(i,j,k,c),
\]

all six permutations must exist.

For every permutation

\[
\sigma\in S_3,
\]

the coefficient must satisfy

\[
\boxed{
\Omega_{\,\sigma(i,j,k)}
=
\operatorname{sgn}(\sigma)\,
\Omega_{ijk}.
}
\]

This must be checked from the completed primary sparse tensor.

It is not sufficient that the secondary reconstruction satisfies this by
construction.

## Repeated indices

Because the Cartan 3-form is alternating,

\[
\Omega_0(X,X,Y)=0.
\]

The sparse tensor must therefore contain no entry with repeated basis
indices.

Required:

\[
i,j,k
\]

are pairwise distinct for every stored coefficient.

## Phase 2C support comparison

Remove the eight Cartan basis indices from the Phase 3D sparse tensor and
translate root basis indices

\[
8,\ldots,247
\]

back to root indices

\[
0,\ldots,239.
\]

The resulting unsigned RRR support must agree exactly with the frozen
Phase 2C ordered Boolean support.

Required:

\[
\boxed{
\operatorname{supp}_{RRR}\Omega_0
=
\operatorname{supp}T.
}
\]

Comparison must report both set differences.

## Phase 3B architecture comparison

Every Phase 3D nonzero entry must belong to either:

- RRR;
- HRR.

No HHR or HHH scalar coefficient may occur.

Every HRR coefficient must involve exact opposite roots.

Thus the signed scalar tensor must refine, but not contradict, the frozen
Phase 3B basis-independent architecture.

## Integer-valued form in the frozen basis

Under the Phase 3C normalization,

\[
\Omega_0(
\mathscr B_i,
\mathscr B_j,
\mathscr B_k
)
\in
\mathbb Z
\]

for every basis triple.

The expected complete value set is:

\[
\boxed{
\{-2,-1,0,+1,+2\}.
}
\]

The sparse representation stores only:

\[
\{-2,-1,+1,+2\}.
\]

## Deterministic export

Phase 3D will export the final sparse tensor as:

    data/derived/phase3d_signed_sparse_cartan_form.json

The artifact must contain at minimum:

- schema/version identifier;
- basis dimension 248;
- Cartan dimension 8;
- root dimension 240;
- frozen basis ordering description;
- total ordered domain size;
- nonzero entry count;
- sector counts;
- coefficient spectrum;
- sparse ordered entries.

Each sparse entry must contain:

- first basis index;
- second basis index;
- third basis index;
- integer coefficient;
- sector label.

Entries must be lexicographically sorted.

## Basis metadata

The export must state explicitly that:

- indices 0-7 are
  \[
  h_1,\ldots,h_8;
  \]
- indices 8-247 are root vectors;
- root vectors follow the existing lexicographic doubled-root ordering;
- epsilon is
  \[
  (+1,-1,+1,-1,+1,-1,+1,-1);
  \]
- the invariant form normalization is
  \[
  B_0(h_i,h_j)=a_{ij}.
  \]

## Required tests

Phase 3D tests must verify at minimum:

1. basis dimension is 248;
2. direct RRR count is 13440;
3. direct HRR count is 2736;
4. total nonzero support count is 16176;
5. all RRR coefficients are \(\pm1\);
6. HRR coefficients lie in \(\pm1,\pm2\);
7. full coefficient spectrum is exactly
   \[
   \{-2:24,-1:8064,+1:8064,+2:24\};
   \]
8. every sparse entry has three distinct basis indices;
9. full alternation holds;
10. RRR cyclic coefficient consistency holds;
11. direct and alternating reconstructions agree exactly;
12. RRR support agrees exactly with Phase 2C;
13. no HHR entry occurs;
14. no HHH entry occurs;
15. every HRR entry uses opposite roots;
16. deterministic export round-trips without changing entries.

## Prohibited operations

Phase 3D must not:

- alter the Phase 3C basis;
- alter epsilon;
- alter the invariant-form normalization;
- tune coefficients to satisfy alternation;
- generate primary coefficients from the Phase 2C Boolean support;
- construct the primary tensor by permutation expansion;
- discard unexpected nonzero coefficients to force expected counts;
- add expected entries that were not produced algebraically;
- allocate a dense 248 x 248 x 248 array;
- claim novelty from reproducing the known Cartan 3-form.

## Failure policy

Any of the following requires Phase 3D to report FAIL:

- a direct/reconstruction coefficient discrepancy;
- a nonzero repeated-index entry;
- an RRR coefficient outside \(\pm1\);
- an HRR coefficient outside \(\pm1,\pm2\);
- nonzero HHR or HHH entries;
- failure of full alternation;
- failure of cyclic RRR consistency;
- mismatch with Phase 2C root support;
- mismatch with Phase 3B sector architecture;
- nondeterministic sparse export.

Unexpected results must be preserved and investigated.

They must not be repaired by changing the frozen Phase 3C conventions.

## Interpretation boundary

A successful Phase 3D will construct an explicit normalized alternating
trilinear map

\[
\boxed{
\Omega_0:
\mathfrak e_8\times
\mathfrak e_8\times
\mathfrak e_8
\to
\mathbb R
}
\]

in the frozen basis.

It will show explicitly how the unsigned 240-root ternary incidence structure
embeds inside the full signed E8 Cartan 3-form.

It will NOT establish:

- novelty of the Cartan 3-form;
- novelty of its Chevalley-basis coefficients;
- a new invariant of E8;
- that the original notation
  \[
  g(v_1,v_2,v_3)
  \]
  necessarily referred to this form;
- any causal or paranormal interpretation of the initiating dream.

## Phase 3D target statement

If all checks pass, the project may conclude:

\[
\boxed{
T_{\alpha\beta\gamma}=1
\iff
\Omega_0(e_\alpha,e_\beta,e_\gamma)\neq0
}
\]

for the 240-root sector, while the complete 248-dimensional form additionally
contains precisely the Cartan/opposite-root scalar coefficients determined by

\[
\Omega_0(h_i,e_\alpha,e_{-\alpha})
=
(-1)^{\operatorname{ht}(\alpha)}
\alpha(h_i).
\]

The final sparse tensor will therefore be the explicit signed realization of
the support architecture established in Phases 2C, 3A, 3B, and 3C.