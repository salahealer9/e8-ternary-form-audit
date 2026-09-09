# Phase 6B Literal Notation Realization Protocol

## Status

STATUS: PHASE6B_LITERAL_NOTATION_REALIZATION_PROTOCOL_FROZEN

## Purpose

Phase 6B gives the initiating notation

\[
g(v_1,v_2,v_3)
\]

a precise executable mathematical realization under the successfully
validated C1 interpretation.

The phase does NOT ask whether the original notation uniquely selected E8.

That question was addressed separately in Phase 5A.

The purpose here is:

> If C1 is adopted as the realization, what does the notation literally mean,
> and can it be used exactly as written?

## Literal definition

Phase 6B freezes:

\[
\boxed{
g(v_1,v_2,v_3)
:=
\Omega_0(v_1,v_2,v_3)
:=
B_0\!\left(v_1,[v_2,v_3]\right)
}
\]

for:

\[
v_1,v_2,v_3\in\mathfrak e_8.
\]

Thus:

\[
\boxed{
g:\mathfrak e_8^3\rightarrow\mathbb R.
}
\]

This is the normalized E8 Cartan 3-form in the basis and normalization frozen
by the repository.

## Interpretation boundary

The definition above means:

> The notation CAN literally be realized as the normalized E8 Cartan 3-form.

It does NOT mean:

> The notation uniquely or necessarily meant the E8 Cartan 3-form when it
> appeared.

The first statement is mathematically established.

The second is not established.

## Frozen normalization

The invariant bilinear form remains:

\[
B_0(h_i,h_j)=a_{ij},
\]

where \(A=(a_{ij})\) is the frozen E8 Cartan matrix.

The frozen Chevalley basis and epsilon convention remain unchanged.

No rescaling of:

\[
B_0,
\qquad
e_\alpha,
\qquad
h_i,
\]

is permitted in Phase 6B.

Therefore the scalar values of \(g\) are completely fixed.

## Frozen basis

The basis is:

\[
\mathscr B=
(
h_1,\ldots,h_8,
e_{\alpha_0},\ldots,e_{\alpha_{239}}
).
\]

Basis indices:

\[
0,\ldots,7
\]

are Cartan vectors.

Indices:

\[
8,\ldots,247
\]

are root vectors in frozen lexicographic doubled-root order.

Dimension:

\[
248.
\]

## General vectors

Each argument may be an arbitrary E8 Lie-algebra vector:

\[
v_r
=
\sum_{i=1}^{8}
a^{(r)}_i h_i
+
\sum_{\alpha\in\Phi(E_8)}
x^{(r)}_\alpha e_\alpha.
\]

The repository implementation will support exact rational coefficients.

Thus the computational realization is:

\[
g:
\mathfrak e_{8,\mathbb Q}^3
\rightarrow
\mathbb Q
\]

for exact arithmetic, while representing the real trilinear form
mathematically.

No floating-point arithmetic is required.

## Sparse vector representation

An exact vector will be represented canonically as a sparse set of:

\[
(\text{basis index},\text{coefficient})
\]

pairs.

Implementation coefficients will use:

    fractions.Fraction

The canonical representation must:

- sort basis indices;
- combine duplicate indices;
- remove zero coefficients;
- reject indices outside
  \[
  0,\ldots,247.
  \]

## Public callable

Phase 6B will expose a public function with the literal name:

    g(v1, v2, v3)

returning an exact scalar.

This is intentionally the same notation as the initiating expression.

The function is not merely an alias for an arbitrary fitted tensor.

Its frozen mathematical semantics are:

\[
\boxed{
g(v_1,v_2,v_3)
=
B_0(v_1,[v_2,v_3]).
}
\]

## Two exact evaluation routes

Phase 6B will implement two routes.

### Route A — Algebraic evaluation

Compute:

\[
[v_2,v_3]
\]

using the independently validated Phase 4A Lie bracket.

Then evaluate:

\[
B_0(v_1,[v_2,v_3]).
\]

Call:

    g_from_algebra(v1, v2, v3)

This route must NOT use the Phase 3D sparse tensor.

### Route B — Tensor contraction

Load the sealed Phase 3D sparse tensor:

    data/derived/phase3d_signed_sparse_cartan_form.json

and compute:

\[
g(v_1,v_2,v_3)
=
\sum_{(i,j,k,c)\in S}
c\,
(v_1)^i
(v_2)^j
(v_3)^k,
\]

where \(S\) is the 16,176-entry sparse support.

Call:

    g_from_tensor(v1, v2, v3)

The public:

    g(v1, v2, v3)

will use the exact sparse tensor contraction as the efficient literal
realization.

## Artifact integrity

Before using the Phase 3D tensor, verify its frozen SHA-256:

    43b52b4116dfcf0dace332234b5c9dc50d95d51effb690aec8aebe39ad4f92e8

A mismatch is a Phase 6B failure.

## Root-vector realization

For:

\[
v_1=e_\alpha,
\qquad
v_2=e_\beta,
\qquad
v_3=e_\gamma,
\]

Phase 6B must reproduce:

\[
\boxed{
g(e_\alpha,e_\beta,e_\gamma)\neq0
\iff
\alpha+\beta+\gamma=0.
}
\]

When nonzero:

\[
\boxed{
g(e_\alpha,e_\beta,e_\gamma)
=
N_{\beta,\gamma}^{\epsilon}
(-1)^{\operatorname{ht}(\alpha)}.
}
\]

Therefore root-sector values are exactly:

\[
\boxed{
\{-1,0,+1\}.
}
\]

## Cartan-root-root realization

For:

\[
h_i,
\quad
e_\alpha,
\quad
e_{-\alpha},
\]

the callable must reproduce:

\[
\boxed{
g(h_i,e_\alpha,e_{-\alpha})
=
(-1)^{\operatorname{ht}(\alpha)}
\alpha(h_i).
}
\]

Hence the complete basis-level value set is:

\[
\boxed{
\{-2,-1,0,+1,+2\}.
}
\]

## Alternation

The callable must satisfy exactly:

\[
g(v_1,v_2,v_3)
=
g(v_2,v_3,v_1)
=
g(v_3,v_1,v_2),
\]

and:

\[
g(v_2,v_1,v_3)
=
-g(v_1,v_2,v_3).
\]

More generally:

\[
\boxed{
g(v_{\sigma(1)},v_{\sigma(2)},v_{\sigma(3)})
=
\operatorname{sgn}(\sigma)
g(v_1,v_2,v_3).
}
\]

Consequently:

\[
g(v,v,w)=0
\]

and:

\[
g(v,w,v)=0.
\]

## Trilinearity

For exact scalars:

\[
a,b\in\mathbb Q,
\]

Phase 6B must verify linearity independently in all three slots.

For example:

\[
g(
a u+b v,
x,
y
)
=
a\,g(u,x,y)
+
b\,g(v,x,y).
\]

The corresponding identities must also hold in slots two and three.

## Tensor interpretation

In the frozen basis define:

\[
g_{ijk}
=
g(\mathscr B_i,\mathscr B_j,\mathscr B_k).
\]

Then:

\[
\boxed{
g_{ijk}
=
(\Omega_0)_{ijk}.
}
\]

The sealed sparse tensor contains exactly:

\[
16{,}176
\]

nonzero ordered \(g_{ijk}\).

The coefficient spectrum remains:

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

## Root-incidence interpretation

Define:

\[
T_{\alpha\beta\gamma}
=
\mathbf 1
\left[
g(e_\alpha,e_\beta,e_\gamma)\neq0
\right].
\]

Then:

\[
\boxed{
T_{\alpha\beta\gamma}
=
1
\iff
\alpha+\beta+\gamma=0.
}
\]

Thus \(g\) simultaneously supplies:

1. a scalar trilinear form;
2. a signed orientation on admissible root triples;
3. an unsigned root-incidence relation after taking nonzero support.

## Bracket recovery

Because \(B_0\) is nondegenerate, the one-form:

\[
g(\,\cdot\,,v_2,v_3)
\]

has a unique \(B_0\)-dual vector.

Phase 6B freezes the identity:

\[
\boxed{
[v_2,v_3]
=
B_0^{-1}
\left(
g(\,\cdot\,,v_2,v_3)
\right).
}
\]

In basis notation:

\[
\boxed{
C^{a}{}_{bc}
=
B_0^{ad}g_{dbc}.
}
\]

This is not a new theorem.

Its purpose in Phase 6B is to establish the literal operational meaning of
\(g\):

\[
\boxed{
g
\text{ is the invariant-form-lowered E8 multiplication tensor}.
}
\]

## Exact bracket-recovery check

Phase 6B will reconstruct the bracket from \(g\) and \(B_0\) for all:

\[
248^2
=
61{,}504
\]

ordered basis pairs.

Required:

    recovered-only discrepancies: 0
    frozen-bracket-only discrepancies: 0
    coefficient mismatches: 0

Thus the literal ternary object must recover the full previously validated
Lie multiplication exactly.

## Convenience constructors

The implementation may expose:

    basis_vector(index)
    cartan_vector(simple_index)
    root_vector(root_index)
    vector({...})

These constructors must not alter mathematical semantics.

## Demonstration cases

The Phase 6B runner must include at least:

### Case 1 — admissible root triple

A deterministic zero-sum root triple with:

\[
g=\pm1.
\]

### Case 2 — non-admissible root triple

A deterministic triple with:

\[
g=0.
\]

### Case 3 — Cartan/opposite-root triple

A deterministic example yielding one of:

\[
\pm1,\pm2.
\]

### Case 4 — arbitrary sparse vectors

Three deterministic exact vectors containing multiple Cartan/root
components.

Required:

\[
g_{\mathrm{tensor}}
=
g_{\mathrm{algebra}}.
\]

## Required implementation artifacts

Phase 6B will create:

    src/e8_ternary/literal_g.py

    tests/test_literal_g.py

    scripts/run_phase6b_literal_notation_realization.py

and a closeout checkpoint.

## Required tests

At minimum:

1. frozen tensor hash unchanged;
2. vector canonicalization exact;
3. basis constructors correct;
4. root admissible example;
5. root non-admissible example;
6. Cartan/opposite-root formula;
7. complete basis coefficient value set;
8. tensor evaluator exact;
9. algebra evaluator exact;
10. tensor/algebra agreement;
11. first-slot linearity;
12. second-slot linearity;
13. third-slot linearity;
14. full alternation;
15. repeated-argument vanishing;
16. exact bracket recovery for all 61,504 ordered basis pairs.

## Success condition

Phase 6B passes only if the repository can literally evaluate:

    g(v1, v2, v3)

for arbitrary exact sparse E8 vectors and all checks succeed.

The required conclusion is:

\[
\boxed{
g(v_1,v_2,v_3)
\text{ is an executable realization of the normalized E8 Cartan 3-form}.
}
\]

## Novelty boundary

Phase 6B makes no new novelty claim.

The Cartan 3-form itself is established prior art.

The notation:

\[
g
\]

is a repository notation chosen to preserve the initiating expression.

Any novelty associated with the computational realization remains governed
solely by Phase 6A.

## Dream-origin boundary

A successful Phase 6B does not establish that the dream causally encoded,
predicted, or transmitted the E8 Cartan 3-form.

It establishes only the following exact mathematical statement:

\[
\boxed{
\text{Under the validated C1 realization, the original notation can be used
literally as the normalized E8 Cartan 3-form.}
}
\]