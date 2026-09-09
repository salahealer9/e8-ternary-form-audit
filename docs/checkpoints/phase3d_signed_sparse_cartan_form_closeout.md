# Phase 3D Signed Sparse Cartan 3-Form Closeout

## Status

STATUS: PHASE3D_SIGNED_SPARSE_CARTAN_FORM_PASS

## Frozen protocol

Phase 3D protocol was frozen at commit:

    42f7adc

Phase 3C canonical E8 basis and normalization completed at:

    b26d208

Phase 3B full Cartan sector support completed at:

    9226f83

Phase 3A root-space Cartan support completed at:

    f66c18b

Phase 2C unsigned ternary incidence completed at:

    c8dfd1c

No Phase 3D signed sparse Cartan-form tensor was constructed before the
Phase 3D protocol freeze.

## Purpose

Phase 3D constructed the complete signed sparse representation of the
normalized Cartan 3-form

\[
\Omega_0(X,Y,Z)=B_0(X,[Y,Z])
\]

on the frozen 248-element E8 basis.

The phase combined the independently established layers of:

\[
E_8\text{ root geometry},
\]

\[
\text{zero-sum ternary incidence},
\]

\[
\text{Cartan-form support},
\]

\[
\text{full sector architecture},
\]

\[
\text{canonical Chevalley signs},
\]

and

\[
\text{normalized invariant pairing}.
\]

## Frozen basis

The basis consists of:

\[
8
\]

Cartan basis vectors and

\[
240
\]

root-space basis vectors.

Observed:

    Cartan basis vectors: 8
    root basis vectors: 240
    total basis dimension: 248

The complete ordered basis-triple domain is:

\[
248^3
=
15{,}252{,}992.
\]

Observed:

    complete ordered basis^3 domain: 15252992

No dense tensor of this size was allocated.

## Primary direct construction

The primary sparse tensor was constructed directly from Lie-algebraic
bracket and bilinear-pairing rules.

It did not use permutation expansion to generate the primary coefficients.

It did not use the Phase 2C Boolean tensor to assign root-root-root
coefficients.

Observed sector counts:

    RRR entries: 13440
    HRR entries: 2736
    total nonzero entries: 16176

Thus:

\[
\boxed{
|\operatorname{supp}_{RRR}\Omega_0|
=
13{,}440
}
\]

and

\[
\boxed{
|\operatorname{supp}_{HRR}\Omega_0|
=
2{,}736.
}
\]

The complete sparse support therefore contains:

\[
\boxed{
16{,}176
}
\]

ordered nonzero coefficients.

## Sparsity

The complete ordered domain contains:

\[
15{,}252{,}992
\]

basis triples.

Only

\[
16{,}176
\]

have nonzero coefficients.

Observed support density:

    0.001060513242254

Thus:

\[
\frac{16176}{15252992}
=
0.001060513242254372\ldots
\]

or approximately:

\[
0.1060513242\%.
\]

## Unordered nonzero basis triples

Because every nonzero stored coefficient has three distinct indices and the
form is alternating, each unordered nonzero basis triple generates exactly
six ordered coefficients.

Therefore the complete sparse form contains:

\[
\frac{16176}{6}
=
2696
\]

unordered nonzero basis triples.

These decompose as:

\[
\frac{13440}{6}
=
2240
\]

unordered RRR triples, and:

\[
\frac{2736}{6}
=
456
\]

unordered HRR triples.

Thus:

\[
\boxed{
2696
=
2240+456.
}
\]

## Full coefficient spectrum

Observed:

    -2: 24
    -1: 8064
    +1: 8064
    +2: 24

Therefore the complete nonzero scalar spectrum is:

\[
\boxed{
\{-2,-1,+1,+2\}.
}
\]

The exact multiplicities are:

\[
\boxed{
-2:24,
}
\]

\[
\boxed{
-1:8064,
}
\]

\[
\boxed{
+1:8064,
}
\]

\[
\boxed{
+2:24.
}
\]

The total closes exactly:

\[
24+8064+8064+24
=
16176.
\]

The coefficient distribution is sign-balanced:

\[
8088
\]

negative coefficients and

\[
8088
\]

positive coefficients.

## Root-root-root coefficients

Every RRR coefficient has magnitude one.

For a zero-sum root triple:

\[
\alpha+\beta+\gamma=0,
\]

the Phase 3C conventions give:

\[
\Omega_0(
e_\alpha,
e_\beta,
e_\gamma
)
=
N_{\beta,\gamma}^{\epsilon}
B_0(e_\alpha,e_{-\alpha}).
\]

Equivalently:

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

The resulting signed RRR sector contains:

\[
13{,}440
\]

ordered coefficients.

## Cartan-root-root coefficients

The scalar HRR sector was evaluated in the frozen simple-coroot Cartan basis.

For:

\[
h_i,
\quad
e_\alpha,
\quad
e_{-\alpha},
\]

the coefficient is:

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

Only nonzero values of:

\[
\alpha(h_i)
\]

produce sparse entries.

The resulting complete HRR sector contains:

\[
2736
\]

ordered coefficients.

The magnitude-two coefficients arise only within this HRR sector.

## Distinct-index property

Observed:

    all stored indices distinct: True

Thus every stored coefficient satisfies:

\[
i\neq j,
\qquad
j\neq k,
\qquad
i\neq k.
\]

No repeated-index coefficient occurs.

This is consistent with alternation of the Cartan 3-form.

## Full alternation

The completed PRIMARY sparse tensor was tested under all permutations of every
stored basis triple.

Observed:

    full S3 alternation: True

Thus for every stored coefficient:

\[
\Omega_{ijk}=c,
\]

and every:

\[
\sigma\in S_3,
\]

the corresponding coefficient satisfies:

\[
\boxed{
\Omega_{\sigma(i,j,k)}
=
\operatorname{sgn}(\sigma)c.
}
\]

This property was checked on the primary direct construction and was not
merely inherited from the secondary permutation-based reconstruction.

## RRR cyclic consistency

The three independently evaluated cyclic expressions:

\[
N_{\beta,\gamma}^{\epsilon}
B_0(e_\alpha,e_{-\alpha}),
\]

\[
N_{\gamma,\alpha}^{\epsilon}
B_0(e_\beta,e_{-\beta}),
\]

and

\[
N_{\alpha,\beta}^{\epsilon}
B_0(e_\gamma,e_{-\gamma})
\]

were compared for every admissible root triple.

Observed:

    RRR cyclic formula consistency: True

Therefore cyclic ordering produces the same scalar coefficient, as required
for an alternating 3-form under even permutations.

## Independent alternating reconstruction

A second sparse tensor was constructed by a deliberately different route.

For the RRR sector, the secondary construction began with canonical unordered
Phase 2A zero-sum root triples.

For the HRR sector, it began with canonical unordered opposite-root lines and
the nonzero Cartan evaluations associated with them.

Only one coefficient was directly evaluated for each unordered basis triple.

The remaining five permutations were generated by permutation parity.

Observed:

    reconstructed entries: 16176

## Exact two-route coefficient comparison

The independently reconstructed tensor was compared with the primary direct
tensor.

Observed:

    direct-only keys: 0
    reconstruction-only keys: 0
    shared keys with differing coefficients: 0
    exact coefficient-map equality: True

Therefore:

\[
\boxed{
S_{\mathrm{direct}}
=
S_{\mathrm{alt}}
}
\]

as complete sparse coefficient maps.

The agreement includes both:

\[
\text{support}
\]

and

\[
\text{signed coefficient values}.
\]

This is stronger than count agreement.

## Exact comparison with Phase 2C

The root-root-root sector was stripped of the eight Cartan basis indices and
translated back to the frozen 240-root indexing.

Observed:

    Phase 3D RRR support: 13440
    Phase 2C Boolean support: 13440
    Phase3D-only entries: 0
    Phase2C-only entries: 0
    exact support equality: True

Therefore:

\[
\boxed{
\operatorname{supp}_{RRR}\Omega_0
=
\operatorname{supp}T.
}
\]

Equivalently:

\[
\boxed{
T_{\alpha\beta\gamma}=1
\iff
\Omega_0(
e_\alpha,
e_\beta,
e_\gamma
)\neq0.
}
\]

Thus the unsigned Phase 2C ternary incidence tensor is exactly the support
skeleton of the signed RRR sector constructed in Phase 3D.

## Refinement of Phase 3B

Phase 3B established the basis-independent support architecture:

\[
RRR\cup HRR.
\]

The Phase 3D scalar tensor was checked against this frozen architecture.

Observed:

    no HHR/HHH nonzero entries: True
    every HRR entry uses opposite roots: True

Thus no scalar coefficient contradicts the Phase 3B sector theorem.

The signed scalar tensor is a strict refinement of that basis-independent
architecture.

## Deterministic export

The complete sparse tensor was exported to:

    data/derived/phase3d_signed_sparse_cartan_form.json

Observed SHA-256:

    43b52b4116dfcf0dace332234b5c9dc50d95d51effb690aec8aebe39ad4f92e8

The artifact was reloaded and compared with the in-memory sparse tensor.

Observed:

    round-trip exact: True

Thus the exported artifact reproduces the complete sparse coefficient map
exactly.

## Test state

The complete repository test suite after Phase 3D implementation reported:

    86 passed in 90.83s

## Phase 3D conclusion

PHASE3D_SIGNED_SPARSE_CARTAN_FORM: PASS

The normalized E8 Cartan 3-form has now been explicitly represented in the
frozen 248-element basis as a deterministic sparse signed tensor.

The complete ordered basis domain contains:

\[
15{,}252{,}992
\]

positions.

Exactly:

\[
16{,}176
\]

are nonzero.

These decompose as:

\[
13{,}440
\]

root-root-root coefficients and:

\[
2{,}736
\]

Cartan-root-root coefficients.

The complete coefficient spectrum is:

\[
\boxed{
-2:24,\quad
-1:8064,\quad
+1:8064,\quad
+2:24.
}
\]

The tensor is fully alternating, agrees exactly with an independent
alternating reconstruction, reproduces the Phase 2C root support exactly, and
refines the Phase 3B sector architecture without contradiction.

## Structural chain established

The completed computation now gives the exact chain:

\[
\text{E8 roots}
\]

\[
\downarrow
\]

\[
\text{zero-sum root triples}
\]

\[
\downarrow
\]

\[
\text{unsigned ternary incidence }T
\]

\[
\downarrow
\]

\[
\operatorname{supp}
\left(
\Omega_0|_{\mathrm{root}^3}
\right)
\]

\[
\downarrow
\]

\[
\boxed{
\text{signed normalized Cartan 3-form }
\Omega_0
}.
\]

The first support equivalence is:

\[
\boxed{
\alpha+\beta+\gamma=0
\iff
T_{\alpha\beta\gamma}=1
\iff
\Omega_0(e_\alpha,e_\beta,e_\gamma)\neq0.
}
\]

The full 248-dimensional form additionally contains precisely the scalar
Cartan/opposite-root coefficients:

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

## Interpretation boundary

Phase 3D explicitly reconstructs a known canonical Lie-algebraic object in
the repository's frozen basis and normalization.

It does NOT establish:

- novelty of the Cartan 3-form;
- novelty of its support;
- novelty of the canonical Chevalley signs;
- a new E8 invariant;
- that the initiating notation
  \[
  g(v_1,v_2,v_3)
  \]
  necessarily denoted this object;
- that the letter \(g\) should be interpreted as a metric;
- any causal or paranormal interpretation of the initiating dream.

What has been established is mathematical compatibility of unusually high
specificity: a canonical E8 trilinear form exists, and the independently
constructed zero-sum ternary root structure is exactly its root-space support.

## Recommended next audit

Before moving to interpretive synthesis, the strongest remaining algebraic
audit is to verify the defining identities of the reconstructed E8 algebra
and form directly in the frozen basis.

A subsequent phase may test:

\[
[X,[Y,Z]]
+
[Y,[Z,X]]
+
[Z,[X,Y]]
=
0
\]

for the bracket, and:

\[
B_0([X,Y],Z)
=
B_0(X,[Y,Z])
\]

for the invariant bilinear form.

Such a phase would provide an independent algebra-level validation behind the
Phase 3D trilinear tensor before any broader interpretation is attempted.