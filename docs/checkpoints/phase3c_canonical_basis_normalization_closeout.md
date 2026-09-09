# Phase 3C Canonical Basis and Normalization Closeout

## Status

STATUS: PHASE3C_CANONICAL_BASIS_NORMALIZATION_PASS

## Frozen protocol

Phase 3C protocol was frozen at commit:

    7fb9e0b

The signed-structure prior-art checkpoint was recorded at:

    f2bc083

Phase 3B full basis-independent Cartan-sector support was completed at:

    9226f83

No signed Cartan 3-form tensor was constructed before this closeout.

## Purpose

Phase 3C fixed and validated the basis and normalization conventions required
to assign reproducible signs and scalar coefficients to the E8 Cartan
3-form.

The phase established:

1. an explicit E8 simple-root system;
2. the corresponding exact Cartan matrix;
3. a positive/negative root decomposition;
4. exact root heights;
5. a frozen epsilon convention;
6. canonical simply-laced root-root structure constants;
7. a normalized invariant bilinear form;
8. opposite-root pairings derived from invariance.

## Frozen simple-root system

All eight frozen simple roots were found in the independently validated E8
root set.

Observed:

    simple roots present in validated E8 set: True
    exact simple-root rank: 8

Thus the simple roots form an exact basis of the eight-dimensional root
space.

## Exact Cartan matrix

The derived simple-root Gram matrix was:

\[
\begin{pmatrix}
 2&-1& 0& 0& 0& 0& 0& 0\\
-1& 2&-1& 0& 0& 0& 0& 0\\
 0&-1& 2&-1& 0& 0& 0& 0\\
 0& 0&-1& 2&-1& 0& 0& 0\\
 0& 0& 0&-1& 2&-1& 0&-1\\
 0& 0& 0& 0&-1& 2&-1& 0\\
 0& 0& 0& 0& 0&-1& 2& 0\\
 0& 0& 0& 0&-1& 0& 0& 2
\end{pmatrix}.
\]

The corresponding derived Dynkin edges were:

\[
1-2,
\]

\[
2-3,
\]

\[
3-4,
\]

\[
4-5,
\]

\[
5-6,
\]

\[
5-8,
\]

\[
6-7.
\]

This is an E8 Dynkin graph.

## Exact root expansions

All 240 validated E8 roots received exact integral coordinates in the frozen
simple-root basis.

Observed:

    exact integral expansions: 240
    positive roots: 120
    negative roots: 120

Thus every root was classified uniquely as positive or negative.

No floating-point inversion or rounding was used.

## Root heights

The observed height range was:

    minimum height: -29
    maximum height: 29

Thus

\[
-29
\le
\operatorname{ht}(\alpha)
\le
29.
\]

No root had height zero.

## Frozen epsilon convention

The derived and frozen epsilon vector was:

\[
\boxed{
\epsilon
=
(+1,-1,+1,-1,+1,-1,+1,-1).
}
\]

Observed:

    alternates across every Dynkin edge: True

Thus the frozen epsilon satisfies

\[
\epsilon(i)=-\epsilon(j)
\]

on every Dynkin edge.

## Canonical root-root structure constants

For every ordered root pair

\[
(\alpha,\beta)
\]

such that

\[
\alpha+\beta
\]

is a root, the frozen simply-laced canonical formula produced

\[
N_{\alpha,\beta}^{\epsilon}
\in
\{-1,+1\}.
\]

Observed:

    admissible ordered root pairs: 13440

The exact sign spectrum was:

\[
N=-1:
\quad
6720,
\]

\[
N=+1:
\quad
6720.
\]

Thus the 13,440 admissible ordered root brackets split evenly between the two
signs.

## Global sign identities

The complete canonical sign table satisfied:

\[
\boxed{
N_{\beta,\alpha}^{\epsilon}
=
-N_{\alpha,\beta}^{\epsilon}.
}
\]

Observed:

    antisymmetry: True

It also satisfied:

\[
\boxed{
N_{-\alpha,-\beta}^{\epsilon}
=
-N_{\alpha,\beta}^{\epsilon}.
}
\]

Observed:

    simultaneous-root-negation identity: True

These checks were performed globally over all admissible ordered root pairs.

## Simple-root canonical checks

For each frozen simple root

\[
\alpha_i
\]

and every root

\[
\beta
\]

such that

\[
\alpha_i+\beta
\]

is a root, the canonical coefficient was compared with the frozen epsilon
value.

Observed:

    admissible checks: 448
    all agree with epsilon: True

Thus all 448 simple-root structure-constant checks matched the canonical
epsilon convention.

## Normalized invariant bilinear form

The Phase 3C normalization is:

\[
\boxed{
B_0(h_i,h_j)=a_{ij}.
}
\]

This fixes the otherwise arbitrary overall scalar of the invariant bilinear
form.

For a root

\[
\alpha=\sum_i n_i\alpha_i,
\]

the corresponding coroot satisfies

\[
h_\alpha=\sum_i n_i h_i
\]

in the simply-laced E8 system.

The implementation verified exactly that

\[
B_0(h_i,h_\alpha)
=
\alpha(h_i)
\]

for every root and every simple-Cartan direction.

## Opposite-root bracket

The frozen epsilon-canonical convention is:

\[
\boxed{
[
e_\alpha^\epsilon,
e_{-\alpha}^\epsilon
]
=
(-1)^{\operatorname{ht}(\alpha)}
h_\alpha.
}
\]

The bracket sign was represented separately in the implementation from the
opposite-root bilinear pairing.

## Opposite-root pairing derived from invariance

The opposite-root pairing

\[
B_0(
e_\alpha^\epsilon,
e_{-\alpha}^\epsilon
)
\]

was not separately imposed.

Instead it was derived from:

\[
[
e_\alpha^\epsilon,
e_{-\alpha}^\epsilon
]
=
s_\alpha h_\alpha,
\]

with

\[
s_\alpha
=
(-1)^{\operatorname{ht}(\alpha)},
\]

together with invariance:

\[
B_0([e_\alpha,e_{-\alpha}],h_i)
=
B_0(e_\alpha,[e_{-\alpha},h_i]).
\]

This gives

\[
s_\alpha B_0(h_\alpha,h_i)
=
\alpha(h_i)
B_0(e_\alpha,e_{-\alpha}).
\]

Since

\[
B_0(h_\alpha,h_i)
=
\alpha(h_i),
\]

and every nonzero root has at least one simple-Cartan direction with

\[
\alpha(h_i)\neq0,
\]

the pairing is uniquely derived as

\[
\boxed{
B_0(
e_\alpha^\epsilon,
e_{-\alpha}^\epsilon
)
=
(-1)^{\operatorname{ht}(\alpha)}.
}
\]

The derived pairing was then checked in every Cartan direction.

Observed:

    invariance checks: True

## Opposite-root pairing spectrum

The derived pairing spectrum was:

\[
-1:
\quad
128\text{ roots},
\]

\[
+1:
\quad
112\text{ roots}.
\]

Observed:

    -1: 128 roots
    +1: 112 roots

This spectrum is recorded as a consequence of the frozen basis and
normalization conventions.

No additional intrinsic significance is assigned to the 128/112 split by
Phase 3C.

## Invariance-derivation strengthening

During Phase 3C implementation, the initial validation implementation used the
same parity expression for both:

1. the opposite-root bracket sign; and
2. the normalized opposite-root pairing.

Although mathematically consistent with the frozen protocol, this made the
invariance check partly tautological.

Before Phase 3C closeout, the implementation was strengthened.

The two concepts are now represented separately:

- `opposite_root_bracket_sign(root)` represents the frozen canonical bracket
  convention;
- `normalized_opposite_root_pairing(root)` derives the bilinear pairing from
  invariance and the B0 Cartan normalization.

The derived scalar is subsequently verified against every simple-Cartan
direction.

Status:

    OPPOSITE_ROOT_PAIRING_INVARIANCE_DERIVATION_STRENGTHENED

This amendment changed no frozen mathematical convention and changed no
headline Phase 3C result.

## Test state

After the invariance-derivation strengthening, the complete repository test
suite reported:

    70 passed in 78.66s

## Phase 3C conclusion

PHASE3C_CANONICAL_BASIS_NORMALIZATION: PASS

Phase 3C has established a fully reproducible signed E8 basis convention.

The root-root structure constants satisfy:

\[
\boxed{
N_{\alpha,\beta}^{\epsilon}\in\{-1,+1\}.
}
\]

There are:

\[
13440
\]

nonzero ordered root-root brackets, split exactly as:

\[
6720
\]

with coefficient \(-1\), and

\[
6720
\]

with coefficient \(+1\).

The opposite-root pairing is derived from invariance as:

\[
\boxed{
B_0(e_\alpha,e_{-\alpha})
=
(-1)^{\operatorname{ht}(\alpha)}.
}
\]

## Consequence for the Cartan 3-form

For every zero-sum root triple

\[
\alpha+\beta+\gamma=0,
\]

the normalized Cartan 3-form coefficient is now determined by the frozen
conventions:

\[
\boxed{
\Omega_0(
e_\alpha,
e_\beta,
e_\gamma
)
=
N_{\beta,\gamma}^{\epsilon}
(-1)^{\operatorname{ht}(\alpha)}.
}
\]

Therefore each of the 13,440 root-root-root support positions established in
Phase 3A can now receive a reproducible coefficient in

\[
\{-1,+1\}.
\]

For the Cartan-root-root sector:

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

These formulas are frozen consequences of Phase 3C but the complete signed
sparse tensor has not yet been constructed.

## Interpretation boundary

Phase 3C establishes a reproducible representation of known E8 Lie-algebraic
structure.

It does NOT establish:

- a new Chevalley basis;
- a new structure-constant formula;
- novelty of the canonical sign system;
- novelty of the Cartan 3-form;
- the final signed sparse 248-dimensional tensor;
- a generalized metric interpretation;
- causal interpretation of the initiating dream.

## Next phase

Phase 3D may now construct the complete signed sparse Cartan 3-form in the
frozen 248-element basis:

\[
(h_1,\ldots,h_8,e_{\alpha_1},\ldots,e_{\alpha_{240}}).
\]

That phase should independently construct:

1. all signed root-root-root coefficients;
2. all scalar Cartan-root-root coefficients;
3. the full sparse support;
4. complete alternation under \(S_3\);
5. comparison of the root-root-root support with Phase 2C;
6. comparison of the unsigned full support with Phase 3B.

No dense

\[
248^3
\]

array is required.