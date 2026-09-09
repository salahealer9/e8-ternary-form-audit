# Phase 3A Root-Space Cartan 3-Form Support Protocol

## Status

STATUS: PHASE3A_ROOT_SPACE_CARTAN_SUPPORT_PROTOCOL_FROZEN

## Purpose

Phase 3A begins the transition from finite E8 root combinatorics to the
248-dimensional Lie algebra

\[
\mathfrak e_8.
\]

The phase investigates the support of the Cartan 3-form

\[
\Omega(X,Y,Z)=B(X,[Y,Z])
\]

when all three arguments lie in nonzero root spaces.

The primary question is:

\[
\Omega(E_\alpha,E_\beta,E_\gamma)\neq0
\quad\Longleftrightarrow\quad
\alpha+\beta+\gamma=0?
\]

This phase concerns support only.

It does not yet assign numerical structure constants or signs.

## Dependencies

The unsigned root-level ternary incidence structure was completed at:

    c8dfd1c

Phase 2C established:

- 240 root vertices;
- 2240 unordered zero-sum triples;
- 13440 ordered support triples;
- uniform hypergraph degree 28;
- pair codegrees in {0,1};
- exact equivalence between active pairs and root inner product -1;
- 1120 negation orbits agreeing with the Phase 2B A2 quotient.

## Lie algebra setting

Let

\[
\mathfrak g=\mathfrak e_8
\]

over a characteristic-zero field suitable for the split root decomposition.

Fix a Cartan subalgebra

\[
\mathfrak h.
\]

Then

\[
\mathfrak e_8
=
\mathfrak h
\oplus
\bigoplus_{\alpha\in\Phi(E_8)}
\mathfrak g_\alpha.
\]

For E8:

\[
\dim\mathfrak h=8,
\]

and each nonzero root space satisfies

\[
\dim\mathfrak g_\alpha=1.
\]

Thus

\[
8+240=248.
\]

## Root vectors

For every root

\[
\alpha\in\Phi(E_8),
\]

choose an arbitrary nonzero vector

\[
E_\alpha\in\mathfrak g_\alpha.
\]

Phase 3A does NOT yet fix a Chevalley normalization or relative signs between
these vectors.

Only basis-independent support statements may therefore be made.

## Invariant bilinear form

Let

\[
B
\]

be a nonzero invariant symmetric bilinear form on

\[
\mathfrak e_8.
\]

For the simple Lie algebra E8 such a form is unique up to overall scalar.

The support analysis uses only:

1. invariance;
2. nondegeneracy;
3. orthogonality of root spaces except opposite roots.

For roots \(\alpha,\delta\),

\[
B(\mathfrak g_\alpha,\mathfrak g_\delta)=0
\]

unless

\[
\alpha+\delta=0.
\]

The pairing

\[
B:
\mathfrak g_\alpha
\times
\mathfrak g_{-\alpha}
\to
\mathbb F
\]

is nondegenerate.

## Cartan 3-form

Define

\[
\Omega(X,Y,Z)=B(X,[Y,Z]).
\]

By invariance and symmetry of \(B\), this is an alternating trilinear form.

Phase 3A concerns the restriction

\[
\Omega_{\mathrm{root}}
=
\Omega\big|_{
\left(\bigoplus_\alpha\mathfrak g_\alpha\right)^3
}.
\]

## Root-space bracket rule

For roots \(\beta,\gamma\),

\[
[\mathfrak g_\beta,\mathfrak g_\gamma]
\subseteq
\mathfrak g_{\beta+\gamma}
\]

when

\[
\beta+\gamma
\]

is a root.

If

\[
\beta+\gamma
\]

is neither a root nor zero, then

\[
[\mathfrak g_\beta,\mathfrak g_\gamma]=0.
\]

If

\[
\gamma=-\beta,
\]

then

\[
[\mathfrak g_\beta,\mathfrak g_{-\beta}]
\subseteq
\mathfrak h.
\]

## Theorem candidate S1 — necessity

For nonzero root vectors

\[
E_\alpha,E_\beta,E_\gamma,
\]

Phase 3A will derive:

\[
\Omega(E_\alpha,E_\beta,E_\gamma)\neq0
\]

only if

\[
\alpha+\beta+\gamma=0.
\]

### Case 1

If

\[
\beta+\gamma
\]

is not a root and is nonzero, then

\[
[E_\beta,E_\gamma]=0
\]

and therefore

\[
\Omega(E_\alpha,E_\beta,E_\gamma)=0.
\]

### Case 2

If

\[
\gamma=-\beta,
\]

then

\[
[E_\beta,E_{-\beta}]\in\mathfrak h.
\]

A nonzero root space is orthogonal to the Cartan subalgebra under the invariant
form, so

\[
B(E_\alpha,\mathfrak h)=0.
\]

Therefore

\[
\Omega(E_\alpha,E_\beta,E_{-\beta})=0.
\]

### Case 3

If

\[
\beta+\gamma
\]

is a root, then

\[
[E_\beta,E_\gamma]
\in
\mathfrak g_{\beta+\gamma}.
\]

For

\[
B(E_\alpha,[E_\beta,E_\gamma])
\]

to be nonzero, root-space orthogonality requires

\[
\alpha+(\beta+\gamma)=0.
\]

Thus

\[
\boxed{
\alpha+\beta+\gamma=0.
}
\]

## Theorem candidate S2 — sufficiency

Suppose

\[
\alpha+\beta+\gamma=0.
\]

Then

\[
\beta+\gamma=-\alpha
\]

is a root.

Because

\[
\mathfrak g_\beta
\]

and

\[
\mathfrak g_\gamma
\]

are one-dimensional root spaces and

\[
\beta+\gamma
\]

is a root,

\[
[\mathfrak g_\beta,\mathfrak g_\gamma]
=
\mathfrak g_{-\alpha}.
\]

For nonzero root vectors,

\[
[E_\beta,E_\gamma]
\neq0.
\]

Since

\[
B:
\mathfrak g_\alpha
\times
\mathfrak g_{-\alpha}
\to\mathbb F
\]

is nondegenerate and both spaces are one-dimensional,

\[
B(E_\alpha,[E_\beta,E_\gamma])\neq0.
\]

Therefore

\[
\boxed{
\alpha+\beta+\gamma=0
\Longrightarrow
\Omega(E_\alpha,E_\beta,E_\gamma)\neq0.
}
\]

## Root-space support theorem to establish

Combining necessity and sufficiency gives the target statement:

\[
\boxed{
\Omega(E_\alpha,E_\beta,E_\gamma)\neq0
\iff
\alpha+\beta+\gamma=0.
}
\]

This is a support theorem only.

It does not determine the numerical value or sign of

\[
\Omega(E_\alpha,E_\beta,E_\gamma).
\]

## Comparison with Phase 2C

Phase 2C defined

\[
T_{ijk}=1
\]

iff

\[
\alpha_i+\alpha_j+\alpha_k=0
\]

for three distinct roots.

If the root-space support theorem is established, then

\[
\boxed{
T_{ijk}=1
\iff
\Omega(
E_{\alpha_i},
E_{\alpha_j},
E_{\alpha_k}
)\neq0
}
\]

for root-space arguments.

Thus the Boolean tensor \(T\) would encode exactly the support of the
root-root-root sector of the Cartan 3-form.

## Expected support count

Phase 2C established

\[
|\operatorname{supp}T|=13440
\]

ordered root triples.

Therefore the expected number of nonzero ordered root-root-root support
positions of the Cartan 3-form is

\[
13440.
\]

This is a validation consequence of the support theorem.

It must not be used to define the Lie-algebraic support.

## Alternation versus Boolean symmetry

The Phase 2C Boolean tensor satisfies

\[
T_{ijk}
=
T_{\sigma(i)\sigma(j)\sigma(k)}
\]

for every permutation

\[
\sigma\in S_3.
\]

By contrast, the Cartan 3-form satisfies

\[
\Omega(
E_{\sigma(i)},
E_{\sigma(j)},
E_{\sigma(k)}
)
=
\operatorname{sgn}(\sigma)
\Omega(
E_i,E_j,E_k
)
\]

once root vectors and normalization are fixed.

Therefore:

- \(T\) records unsigned support;
- \(\Omega\) is alternating;
- support symmetry and coefficient antisymmetry must not be conflated.

## Full 248-dimensional support boundary

The root-only Phase 2C tensor does NOT describe the entire Cartan 3-form.

The full Lie algebra contains the Cartan subalgebra

\[
\mathfrak h
\]

of dimension 8.

For

\[
H\in\mathfrak h
\]

and opposite roots

\[
\alpha,-\alpha,
\]

one has

\[
[E_\alpha,E_{-\alpha}]
\in\mathfrak h.
\]

Consequently expressions of the form

\[
\Omega(H,E_\alpha,E_{-\alpha})
\]

can be nonzero.

These Cartan-root-root components lie outside the 240-root Boolean tensor
constructed in Phase 2C.

Phase 3A therefore makes only the restricted statement

\[
\operatorname{supp}
\left(
\Omega\big|_{\mathrm{root}^3}
\right)
=
\operatorname{supp}T.
\]

It does NOT claim

\[
\operatorname{supp}\Omega
=
\operatorname{supp}T.
\]

## Computational role

Phase 3A will construct a symbolic support classifier based on root-space
grading rules.

For each ordered root triple

\[
(\alpha,\beta,\gamma),
\]

the classifier will determine whether the Cartan 3-form is:

- FORCED_ZERO;
- ROOT_SUPPORT_NONZERO.

The classifier must use Lie-algebra grading and invariant-form pairing rules.

It must not simply call the Phase 2C Boolean support tensor as its decision
rule.

The resulting support will then be compared exactly with Phase 2C.

## Independent comparison

Let

\[
S_\Omega
\]

be the ordered root-space support derived from Lie-algebra rules.

Let

\[
S_T
\]

be the Phase 2C ordered Boolean support.

Phase 3A will compute:

\[
S_\Omega\setminus S_T
\]

and

\[
S_T\setminus S_\Omega.
\]

The target equality is

\[
S_\Omega=S_T.
\]

Any discrepancy must be reported rather than repaired.

## Success criteria

Phase 3A is a PASS only if:

1. necessity of the zero-sum condition is derived from root-space grading and
   bilinear-form orthogonality;
2. sufficiency is derived from nonzero root-space brackets and nondegenerate
   opposite-root pairing;
3. the symbolic support classifier is independent of Phase 2C support lookup;
4. all ordered root triples are classified deterministically;
5. the resulting Lie-algebraic root-space support agrees exactly with Phase
   2C;
6. the distinction between unsigned support and alternating coefficients is
   preserved;
7. no statement about the full 248-dimensional support is inferred solely from
   the root-only tensor.

## Prohibited operations

Phase 3A must not:

- assign Chevalley signs;
- choose structure constants retrospectively;
- define Cartan support directly as
  \[
  \alpha+\beta+\gamma=0
  \]
  without deriving that condition from Lie-algebra rules;
- call the Phase 2C tensor to classify Lie-algebra support;
- treat \(T\) as an alternating tensor;
- claim that the 240-root tensor is the complete 248-dimensional Cartan
  3-form.

## Interpretation boundary

A successful Phase 3A would establish that the discrete ternary object found
in Phase 2 is exactly the support skeleton of the root-root-root sector of a
canonical invariant trilinear form on

\[
\mathfrak e_8.
\]

It would not establish that the initiating notation

\[
g(v_1,v_2,v_3)
\]

specifically denotes the Cartan 3-form.

It would also not establish novelty or any causal interpretation of the
initiating dream.

## Next phase

Following Phase 3A closeout, a separate protocol will determine the next
appropriate Lie-algebraic layer.

Possible subsequent tasks include:

1. construction of a Chevalley basis and signed root-root-root coefficients;
2. characterization of Cartan-root-root support;
3. reconstruction of the full 248-dimensional Cartan 3-form support;
4. comparison of the resulting alternating form with the unsigned Phase 2C
   incidence tensor.

No choice among these is made by Phase 3A.
