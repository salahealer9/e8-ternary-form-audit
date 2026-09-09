# Phase 4A Lie Algebra Identity Audit Closeout

## Status

STATUS: PHASE4A_LIE_ALGEBRA_IDENTITY_AUDIT_PASS

## Frozen protocol

Phase 4A protocol was frozen at commit:

    39229c0

Phase 3D signed sparse E8 Cartan form was completed at:

    3ef18f1

The sealed Phase 3D sparse artifact is:

    data/derived/phase3d_signed_sparse_cartan_form.json

with frozen SHA-256:

    43b52b4116dfcf0dace332234b5c9dc50d95d51effb690aec8aebe39ad4f92e8

No Phase 4A bracket or bilinear-form result was used to alter the sealed
Phase 3D artifact.

## Purpose

Phase 4A independently reconstructed and audited the algebraic structures
underlying the Phase 3D Cartan 3-form.

The phase tested:

1. the frozen 248-dimensional Lie bracket;
2. closure;
3. antisymmetry;
4. exhaustive Jacobi identity;
5. the normalized bilinear form \(B_0\);
6. symmetry and nondegeneracy of \(B_0\);
7. exact invariance of \(B_0\);
8. independent reconstruction of
   \[
   \Omega_0(X,Y,Z)=B_0(X,[Y,Z]);
   \]
9. exact agreement with the sealed Phase 3D sparse tensor.

## Frozen algebra basis

Observed:

    dimension: 248
    ordered basis-pair domain: 61504

Thus the complete ordered bracket domain is:

\[
248^2
=
61{,}504.
\]

## Independent bracket reconstruction

The bracket was reconstructed from:

- frozen root arithmetic;
- frozen simple-root expansions;
- canonical Phase 3C structure constants;
- Cartan-root evaluations;
- the frozen opposite-root bracket convention.

The Phase 3D tensor was not used to define the bracket.

Observed:

    nonzero ordered bracket pairs: 15504
    antisymmetry: True
    all self-brackets zero: True
    closure on frozen basis: True

Therefore:

\[
\boxed{
[\mathscr B_i,\mathscr B_j]
=
-
[\mathscr B_j,\mathscr B_i]
}
\]

for every ordered basis pair.

Also:

\[
\boxed{
[\mathscr B_i,\mathscr B_i]=0
}
\]

for every basis element.

Every bracket output remained within the frozen 248-dimensional basis.

## Nonzero bracket support

The observed number of ordered basis pairs with nonzero bracket was:

\[
\boxed{
15{,}504.
}
\]

This agrees with the independently preregistered decomposition:

\[
1824
\]

Cartan-root and root-Cartan pairs,

\[
13440
\]

root pairs whose sum is a root,

and:

\[
240
\]

ordered opposite-root pairs.

Thus:

\[
1824+13440+240
=
15504.
\]

## Exhaustive Jacobi audit

The Jacobi identity tested was:

\[
J(X,Y,Z)
=
[X,[Y,Z]]
+
[Y,[Z,X]]
+
[Z,[X,Y]].
\]

Because bracket antisymmetry was independently established first, the audit
tested every canonical distinct basis triple:

\[
i<j<k.
\]

The complete domain contained:

\[
\binom{248}{3}
=
2{,}511{,}496
\]

triples.

Observed:

    canonical distinct triples checked: 2511496

The sector decomposition was:

### HHH

Observed:

    56 checked, 0 failures

### HHR

Observed:

    6720 checked, 0 failures

### HRR

Observed:

    229440 checked, 0 failures

### RRR

Observed:

    2275280 checked, 0 failures

These counts close exactly:

\[
56
+
6720
+
229440
+
2275280
=
2511496.
\]

Total observed Jacobi failures:

\[
\boxed{0}.
\]

Therefore:

\[
\boxed{
[X,[Y,Z]]
+
[Y,[Z,X]]
+
[Z,[X,Y]]
=
0
}
\]

for every tested basis triple.

Since the bracket is bilinear, this establishes the Jacobi identity on the
full frozen vector space.

## Independent bilinear-form reconstruction

The normalized bilinear form \(B_0\) was reconstructed independently from:

\[
B_0(h_i,h_j)=a_{ij},
\]

Cartan-root orthogonality, and the Phase 3C invariance-derived opposite-root
pairings.

The Phase 3D tensor was not used to define \(B_0\).

Observed:

    nonzero ordered entries: 262

The exact nonzero coefficient spectrum was:

\[
-1:
\quad142,
\]

\[
+1:
\quad112,
\]

\[
+2:
\quad8.
\]

Observed:

    symmetry: True
    Cartan determinant: 1
    structural nondegeneracy: True

Thus:

\[
\boxed{
B_0(X,Y)=B_0(Y,X)
}
\]

on the frozen basis.

## Bilinear nondegeneracy

The Cartan block has determinant:

\[
\boxed{1}.
\]

Every nonzero root space pairs with its unique opposite root space with
coefficient:

\[
\pm1.
\]

The Cartan and root sectors are orthogonal.

Therefore the complete 248-dimensional bilinear form is nondegenerate.

## Exact invariant-form audit

Two sparse trilinear maps were independently constructed:

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

Observed:

    L = B0([X,Y],Z) support: 16176
    R = B0(X,[Y,Z]) support: 16176

Exact comparison:

    L-only keys: 0
    R-only keys: 0
    differing coefficients: 0
    exact invariance: True

Therefore:

\[
\boxed{
B_0([X,Y],Z)
=
B_0(X,[Y,Z])
}
\]

exactly across the complete sparse support.

No discrepancy was observed.

## Algebra-derived trilinear map

After establishing invariance, Phase 4A defined:

\[
\Omega_{\mathrm{alg}}(X,Y,Z)
=
B_0(X,[Y,Z]).
\]

Observed nonzero entries:

\[
\boxed{
16{,}176.
}
\]

Observed coefficient spectrum:

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

Thus:

\[
\boxed{
\Omega_{\mathrm{alg}}
\in
\{-2,-1,0,+1,+2\}
}
\]

on basis triples.

## Sealed Phase 3D artifact integrity

Before the Phase 3D tensor was loaded for comparison, its SHA-256 was checked.

Observed:

    43b52b4116dfcf0dace332234b5c9dc50d95d51effb690aec8aebe39ad4f92e8

Expected:

    43b52b4116dfcf0dace332234b5c9dc50d95d51effb690aec8aebe39ad4f92e8

Observed:

    hash unchanged: True

Therefore the sealed Phase 3D artifact used for comparison was unchanged from
the previously committed result.

## Exact comparison with sealed Phase 3D

Only after:

- bracket reconstruction;
- bracket validation;
- exhaustive Jacobi audit;
- bilinear-form reconstruction;
- bilinear-form validation;
- invariant-form comparison;

was the sealed Phase 3D tensor loaded.

Observed:

    algebra-derived entries: 16176
    Phase 3D entries: 16176
    algebra-only keys: 0
    Phase3D-only keys: 0
    differing coefficients: 0
    exact coefficient-map equality: True

Therefore:

\[
\boxed{
\Omega_{\mathrm{alg}}
=
\Omega_{\mathrm{Phase3D}}
}
\]

entry-for-entry.

This includes both support and coefficient values.

## Independent validation chain

The project now contains three distinct computational layers.

### Layer 1 — root combinatorics

The E8 root system produced:

\[
2240
\]

unordered zero-sum root triples and:

\[
13440
\]

ordered root-root-root ternary support positions.

### Layer 2 — Lie algebra

The frozen 248-dimensional bracket satisfies:

\[
\boxed{\text{closure}}
\]

\[
\boxed{\text{antisymmetry}}
\]

and:

\[
\boxed{\text{Jacobi}}
\]

with:

\[
0
\]

failures across all:

\[
2{,}511{,}496
\]

canonical distinct basis triples.

### Layer 3 — invariant trilinear form

The independently reconstructed nondegenerate symmetric form satisfies:

\[
\boxed{
B_0([X,Y],Z)
=
B_0(X,[Y,Z]).
}
\]

Therefore:

\[
\boxed{
\Omega_0(X,Y,Z)
=
B_0(X,[Y,Z])
}
\]

is recovered independently.

That map agrees exactly with the previously sealed signed sparse tensor.

## Principal algebraic result

The completed audit chain establishes the explicit normalized object:

\[
\boxed{
\Omega_0:
\mathfrak e_8
\times
\mathfrak e_8
\times
\mathfrak e_8
\to
\mathbb R
}
\]

defined by:

\[
\boxed{
\Omega_0(X,Y,Z)
=
B_0(X,[Y,Z]).
}
\]

Its complete sparse support in the frozen basis contains:

\[
16{,}176
\]

ordered nonzero coefficients.

Its root-root-root sector satisfies:

\[
\boxed{
\alpha+\beta+\gamma=0
\iff
\Omega_0(e_\alpha,e_\beta,e_\gamma)\neq0.
}
\]

The unsigned Phase 2C ternary incidence tensor therefore obeys:

\[
\boxed{
T_{\alpha\beta\gamma}=1
\iff
\Omega_0(e_\alpha,e_\beta,e_\gamma)\neq0.
}
\]

## Phase 4A conclusion

PHASE4A_LIE_ALGEBRA_IDENTITY_AUDIT: PASS

The 248-dimensional bracket underlying the reconstructed Cartan 3-form:

- closes exactly;
- is antisymmetric;
- satisfies Jacobi exhaustively;
- admits the frozen symmetric nondegenerate form \(B_0\);
- preserves \(B_0\) exactly;
- reconstructs the sealed Phase 3D Cartan 3-form entry-for-entry.

The principal algebraic audit chain is therefore complete.

## Interpretation boundary

Phase 4A establishes the mathematical correctness and internal consistency of
the reconstructed E8 Lie-algebraic structure.

It does NOT establish:

- novelty of E8;
- novelty of the Lie bracket;
- novelty of the invariant bilinear form;
- novelty of the Cartan 3-form;
- that the initiating notation
  \[
  g(v_1,v_2,v_3)
  \]
  uniquely specifies the E8 Cartan 3-form;
- that the letter \(g\) denotes a metric;
- that the initiating dream had a paranormal or external causal origin.

The algebraic result and the interpretation of the initiating observation
remain distinct questions.

## Algebraic audit close

No further algebraic construction is required for the principal Phase 0
question.

The recommended next stage is interpretive synthesis.

That synthesis should return to the preregistered candidate classes:

- C0 — generic three-argument function;
- C1 — E8 Cartan 3-form;
- C2 — G2 invariant alternating 3-form;
- C3 — E6 cubic / symmetric trilinear form;
- C4 — other established ternary structures.

The comparison should assess each candidate under the preregistered criteria
without changing those criteria in light of the computational results.