# Phase 4A Lie Algebra Identity Audit Protocol

## Status

STATUS: PHASE4A_LIE_ALGEBRA_IDENTITY_AUDIT_PROTOCOL_FROZEN

## Purpose

Phase 4A performs an independent algebra-level validation of the bracket and
invariant bilinear form underlying the Phase 3D signed Cartan 3-form.

The primary objects are:

\[
[\cdot,\cdot]:
\mathfrak e_8\times\mathfrak e_8
\to
\mathfrak e_8
\]

and

\[
B_0:
\mathfrak e_8\times\mathfrak e_8
\to
\mathbb R.
\]

The phase tests directly that:

1. the frozen bracket is bilinear and antisymmetric on the basis;
2. the bracket closes in the frozen 248-dimensional basis;
3. the Jacobi identity holds;
4. \(B_0\) is symmetric and nondegenerate;
5. \(B_0\) is invariant under the bracket;
6. the independently reconstructed trilinear map
   \[
   B_0(X,[Y,Z])
   \]
   agrees exactly with the sealed Phase 3D sparse Cartan form.

The Phase 3D tensor must NOT be used to define either the bracket or the
bilinear form.

## Dependencies

Phase 3D signed sparse Cartan form completed at:

    3ef18f1

Phase 3D protocol was frozen at:

    42f7adc

Phase 3C canonical basis and normalization completed at:

    b26d208

The sealed Phase 3D sparse artifact is:

    data/derived/phase3d_signed_sparse_cartan_form.json

with recorded SHA-256:

    43b52b4116dfcf0dace332234b5c9dc50d95d51effb690aec8aebe39ad4f92e8

## Frozen basis

The basis remains:

\[
\mathscr B^\epsilon
=
(
h_1,\ldots,h_8,
e_{\alpha_0},\ldots,e_{\alpha_{239}}
).
\]

Indices:

\[
0,\ldots,7
\]

are Cartan basis vectors.

Indices:

\[
8,\ldots,247
\]

are root vectors in frozen lexicographic doubled-root order.

The dimension is:

\[
248.
\]

No basis change is permitted in Phase 4A.

## Sparse vector representation

A Lie algebra vector will be represented as a sparse exact map:

\[
\text{basis index}\mapsto\text{integer coefficient}.
\]

Zero coefficients must be removed canonically.

All coefficient arithmetic is exact integer arithmetic.

No floating-point arithmetic is required.

## Frozen bracket rules

The bracket is constructed independently from the Phase 3C conventions.

### Cartan-Cartan

For all:

\[
i,j\in\{1,\ldots,8\},
\]

\[
\boxed{
[h_i,h_j]=0.
}
\]

### Cartan-root

For every root \(\alpha\),

\[
\boxed{
[h_i,e_\alpha]
=
\alpha(h_i)e_\alpha.
}
\]

By antisymmetry:

\[
\boxed{
[e_\alpha,h_i]
=
-\alpha(h_i)e_\alpha.
}
\]

The value:

\[
\alpha(h_i)
\]

must be computed from the frozen root/simple-root geometry.

### Root-root: sum is a root

If:

\[
\alpha+\beta\in\Phi(E_8),
\]

then:

\[
\boxed{
[e_\alpha,e_\beta]
=
N_{\alpha,\beta}^{\epsilon}
e_{\alpha+\beta}.
}
\]

The coefficient:

\[
N_{\alpha,\beta}^{\epsilon}\in\{-1,+1\}
\]

is the frozen Phase 3C canonical structure constant.

### Root-root: opposite roots

If:

\[
\beta=-\alpha,
\]

then:

\[
\boxed{
[e_\alpha,e_{-\alpha}]
=
(-1)^{\operatorname{ht}(\alpha)}
h_\alpha.
}
\]

With:

\[
\alpha=\sum_i n_i\alpha_i,
\]

one has:

\[
h_\alpha
=
\sum_i n_i h_i.
\]

Thus an opposite-root bracket may contain several Cartan basis components.

### Root-root: otherwise

If:

\[
\alpha+\beta
\]

is neither a root nor zero, then:

\[
\boxed{
[e_\alpha,e_\beta]=0.
}
\]

## Bracket independence

The Phase 4A bracket constructor must use:

- frozen roots;
- exact simple-root expansions;
- canonical structure constants;
- frozen opposite-root bracket convention.

It must NOT use:

- Phase 3D sparse coefficients;
- Cartan-form support;
- permutation reconstruction of \(\Omega_0\).

## Expected nonzero ordered bracket-pair support

The complete ordered basis-pair domain has:

\[
248^2
=
61{,}504
\]

positions.

### Cartan-root contributions

For one fixed simple Cartan basis vector, exactly:

\[
114
\]

of the 240 roots have:

\[
\alpha(h_i)\neq0.
\]

Across eight Cartan directions:

\[
8\times114
=
912
\]

ordered \(H,R\) pairs are nonzero.

The reversed \(R,H\) sector gives another:

\[
912.
\]

Thus:

\[
1824
\]

nonzero ordered Cartan-root bracket pairs are expected.

### Root-root sum-root contributions

Phase 3C established:

\[
13440
\]

ordered root pairs with root sum.

### Opposite-root contributions

There are:

\[
240
\]

ordered opposite-root pairs.

Therefore the expected total number of ordered basis pairs with nonzero
bracket is:

\[
\boxed{
1824+13440+240
=
15504.
}
\]

This is a validation expectation only.

The bracket constructor must not stop when this count is reached.

## Bracket antisymmetry

For every ordered basis pair:

\[
(i,j),
\]

Phase 4A must verify exactly:

\[
\boxed{
[\mathscr B_i,\mathscr B_j]
=
-
[\mathscr B_j,\mathscr B_i].
}
\]

This includes multi-component opposite-root brackets.

Also required:

\[
[\mathscr B_i,\mathscr B_i]=0
\]

for all 248 basis vectors.

## Bracket closure

Every nonzero output component of every basis bracket must have a valid frozen
basis index:

\[
0,\ldots,247.
\]

No external or undefined basis direction may occur.

## Jacobi identity

Define the Jacobiator:

\[
J(X,Y,Z)
=
[X,[Y,Z]]
+
[Y,[Z,X]]
+
[Z,[X,Y]].
\]

Phase 4A must verify:

\[
\boxed{
J(
\mathscr B_i,
\mathscr B_j,
\mathscr B_k
)
=
0
}
\]

exactly.

Because the bracket must first be independently verified antisymmetric, the
Jacobiator is alternating in its three arguments.

It therefore suffices to test every canonical distinct basis triple:

\[
i<j<k.
\]

The total number is:

\[
\binom{248}{3}
=
\boxed{
2{,}511{,}496.
}
\]

No random sampling is permitted.

## Jacobi sector census

The exhaustive distinct-index Jacobi domain decomposes as follows.

### HHH

\[
\binom{8}{3}
=
56.
\]

### HHR

\[
\binom{8}{2}\times240
=
6720.
\]

### HRR

\[
8\times\binom{240}{2}
=
229440.
\]

### RRR

\[
\binom{240}{3}
=
2275280.
\]

These close exactly:

\[
56+6720+229440+2275280
=
2511496.
\]

Phase 4A must report the number of Jacobi failures separately for all four
sectors.

Required result:

\[
\boxed{
0
}
\]

failures in every sector.

## Frozen invariant bilinear form

Phase 4A independently reconstructs:

\[
B_0.
\]

### Cartan-Cartan

\[
\boxed{
B_0(h_i,h_j)
=
a_{ij},
}
\]

where \(A=(a_{ij})\) is the frozen E8 Cartan matrix.

### Cartan-root

\[
\boxed{
B_0(h_i,e_\alpha)=0.
}
\]

By symmetry:

\[
B_0(e_\alpha,h_i)=0.
\]

### Root-root

For roots \(\alpha,\beta\):

\[
B_0(e_\alpha,e_\beta)=0
\]

unless:

\[
\beta=-\alpha.
\]

For opposite roots:

\[
\boxed{
B_0(e_\alpha,e_{-\alpha})
=
(-1)^{\operatorname{ht}(\alpha)}.
}
\]

This value must be obtained through the Phase 3C invariance-derived pairing
function rather than copied from Phase 3D tensor coefficients.

## Expected sparse bilinear support

The Cartan matrix contains:

- 8 nonzero diagonal entries;
- 14 ordered off-diagonal edge entries.

Thus the \(HH\) block contains:

\[
22
\]

nonzero ordered entries.

The root block contains:

\[
240
\]

ordered opposite-root pairings.

Therefore the complete bilinear form is expected to have:

\[
\boxed{
262
}
\]

nonzero ordered basis-pair entries.

Expected nonzero value spectrum:

\[
-1:
\quad
142,
\]

\[
+1:
\quad
112,
\]

\[
+2:
\quad
8.
\]

The \(-1\) count consists of:

\[
14
\]

Cartan-matrix edge entries plus:

\[
128
\]

negative opposite-root pairings.

No \(-2\) bilinear coefficient is expected.

## Bilinear symmetry

Phase 4A must verify:

\[
\boxed{
B_0(
\mathscr B_i,
\mathscr B_j
)
=
B_0(
\mathscr B_j,
\mathscr B_i
)
}
\]

for all ordered basis pairs.

## Bilinear nondegeneracy

Nondegeneracy will be verified structurally.

### Cartan block

The frozen E8 Cartan matrix must have:

\[
\det A=1.
\]

Therefore the Cartan restriction is nondegenerate.

### Root block

Every root has one unique opposite root and:

\[
B_0(e_\alpha,e_{-\alpha})
\in\{-1,+1\}.
\]

Thus every opposite-root two-dimensional block is nondegenerate.

Because:

\[
\mathfrak h
\]

is orthogonal to all nonzero root spaces, these checks establish
nondegeneracy of the complete 248-dimensional bilinear form.

## Invariance identity

The invariant-form identity is:

\[
\boxed{
B_0([X,Y],Z)
=
B_0(X,[Y,Z]).
}
\]

This must be tested independently of the Phase 3D tensor.

Define two sparse ordered trilinear scalar maps:

\[
L_{ijk}
=
B_0(
[\mathscr B_i,\mathscr B_j],
\mathscr B_k
),
\]

and:

\[
R_{ijk}
=
B_0(
\mathscr B_i,
[\mathscr B_j,\mathscr B_k]
).
\]

Construct \(L\) and \(R\) independently from:

- the Phase 4A bracket;
- the independently reconstructed Phase 4A bilinear form.

Zero scalar entries are omitted.

## Exact invariance comparison

Phase 4A must compare the complete sparse maps:

\[
L
\]

and:

\[
R.
\]

Required:

\[
\boxed{
L=R.
}
\]

The comparison must report:

- L-only keys;
- R-only keys;
- shared keys with differing scalar values.

All discrepancy counts must equal zero.

## Expected invariance-map support

Because:

\[
R_{ijk}
=
B_0(
\mathscr B_i,
[\mathscr B_j,\mathscr B_k]
)
=
\Omega_0(
\mathscr B_i,
\mathscr B_j,
\mathscr B_k
),
\]

the expected nonzero support count is:

\[
\boxed{
16176.
}
\]

The expected coefficient spectrum is:

\[
-2:
\quad24,
\]

\[
-1:
\quad8064,
\]

\[
+1:
\quad8064,
\]

\[
+2:
\quad24.
\]

These are validation expectations inherited from the sealed Phase 3D result.

They must not define either \(L\) or \(R\).

## Independent reconstruction of Omega

After invariance has been established:

\[
L=R,
\]

define the independently reconstructed algebra-level trilinear map:

\[
\Omega_{\mathrm{alg}}(X,Y,Z)
=
B_0(X,[Y,Z]).
\]

This map is constructed entirely from the Phase 4A bracket and bilinear form.

It must then be compared with the sealed Phase 3D sparse tensor.

## Comparison with Phase 3D

Let:

\[
S_{\mathrm{alg}}
\]

be the sparse coefficient map obtained in Phase 4A.

Let:

\[
S_{\mathrm{3D}}
\]

be the sealed Phase 3D sparse coefficient map loaded from:

    data/derived/phase3d_signed_sparse_cartan_form.json

Compare:

1. algebra-only keys;
2. Phase3D-only keys;
3. shared keys with differing coefficients.

Required:

\[
\boxed{
S_{\mathrm{alg}}
=
S_{\mathrm{3D}}.
}
\]

All discrepancy counts must be zero.

The Phase 3D tensor may only be loaded after the Phase 4A bracket, bilinear
form, Jacobi audit, and invariance maps have been constructed.

## Phase 3D artifact integrity

Before comparison, verify that the sealed Phase 3D JSON still has SHA-256:

    43b52b4116dfcf0dace332234b5c9dc50d95d51effb690aec8aebe39ad4f92e8

A mismatch must be reported.

The artifact must not be silently regenerated before this integrity check.

## Required outputs

Phase 4A will report at minimum:

### Bracket

- basis dimension;
- complete ordered pair domain;
- nonzero ordered bracket-pair count;
- bracket antisymmetry;
- self-bracket zero;
- bracket closure.

### Jacobi

- total canonical triples checked;
- HHH triples and failures;
- HHR triples and failures;
- HRR triples and failures;
- RRR triples and failures;
- total failures.

### Bilinear form

- nonzero ordered support count;
- coefficient spectrum;
- symmetry;
- Cartan determinant;
- opposite-root nondegeneracy;
- full structural nondegeneracy.

### Invariance

- L-map support count;
- R-map support count;
- L-only keys;
- R-only keys;
- coefficient mismatches;
- exact equality.

### Phase 3D comparison

- Phase 4A algebra-derived support count;
- Phase 3D support count;
- algebra-only keys;
- Phase3D-only keys;
- coefficient mismatches;
- exact equality.

## Success criteria

Phase 4A is a PASS only if:

1. the bracket closes on all 248 frozen basis vectors;
2. the bracket is antisymmetric for all ordered basis pairs;
3. every self-bracket vanishes;
4. all 2,511,496 canonical distinct basis triples satisfy Jacobi;
5. each Jacobi sector has zero failures;
6. \(B_0\) is symmetric;
7. the Cartan block has determinant 1;
8. every root has a unique nonzero opposite-root pairing;
9. the complete bilinear form is structurally nondegenerate;
10. the independently constructed L and R invariance maps agree exactly;
11. the algebra-derived trilinear map contains 16,176 nonzero entries;
12. its coefficient spectrum is exactly
    \[
    -2:24,\quad
    -1:8064,\quad
    +1:8064,\quad
    +2:24;
    \]
13. the sealed Phase 3D artifact hash is unchanged;
14. the Phase 4A algebra-derived trilinear map agrees entry-for-entry with
    Phase 3D.

## Prohibited operations

Phase 4A must not:

- alter the frozen Phase 3C basis;
- alter canonical structure constants;
- alter epsilon;
- alter the \(B_0\) normalization;
- use Phase 3D coefficients to define the bracket;
- use Phase 3D coefficients to define \(B_0\);
- infer Jacobi from Phase 3D alternation;
- test Jacobi only on random samples;
- discard failed Jacobi triples;
- regenerate the Phase 3D JSON before checking its sealed hash;
- tune bracket coefficients to reproduce Phase 3D.

## Failure policy

Any nonzero Jacobiator, invariance discrepancy, support mismatch, coefficient
mismatch, bracket-closure failure, or artifact-integrity failure requires:

    PHASE4A_LIE_ALGEBRA_IDENTITY_AUDIT: FAIL

The discrepancy must be preserved for investigation.

Frozen Phase 3C and Phase 3D conventions must not be changed retrospectively
to force a PASS.

## Interpretation boundary

A successful Phase 4A will independently validate that the frozen
248-dimensional construction carries:

1. an exact Lie bracket satisfying Jacobi;
2. a symmetric nondegenerate invariant bilinear form;
3. the signed Cartan 3-form
   \[
   \Omega_0(X,Y,Z)=B_0(X,[Y,Z]).
   \]

It will therefore validate the algebra underneath the Phase 3D tensor rather
than only the tensor's internal symmetry.

It will NOT establish:

- novelty of the E8 Lie algebra;
- novelty of the invariant bilinear form;
- novelty of the Cartan 3-form;
- that the notation
  \[
  g(v_1,v_2,v_3)
  \]
  uniquely determines this structure;
- any causal or paranormal interpretation of the initiating dream.

## Transition after Phase 4A

If Phase 4A passes, the principal algebraic audit chain will be complete.

The project can then return explicitly to the Phase 0 candidate framework and
perform an interpretation synthesis comparing:

- C0 generic ternary function;
- C1 E8 Cartan 3-form;
- C2 G2 invariant 3-form;
- C3 E6 cubic/trilinear form;
- C4 other established ternary structures.

That comparison should distinguish:

- mathematical fit;
- E8 specificity;
- dimensional fit;
- symmetry type;
- prior art;
- assumptions required;
- what was discovered computationally;
- what remains interpretation rather than evidence.