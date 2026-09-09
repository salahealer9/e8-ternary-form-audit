# Phase 3C Canonical Basis and Normalization Protocol

## Status

STATUS: PHASE3C_CANONICAL_BASIS_NORMALIZATION_PROTOCOL_FROZEN

## Purpose

Phase 3C freezes the conventions required to lift the basis-independent
support architecture of Phases 3A-3B to reproducible signed scalar
coefficients.

This phase fixes:

1. an explicit E8 simple-root system;
2. positive and negative roots;
3. root coordinates and heights;
4. a Cartan / coroot basis;
5. the epsilon-canonical Chevalley root-vector convention;
6. canonical root-root structure constants;
7. an invariant-bilinear-form normalization.

No convention may be changed retrospectively after signed Cartan-form
coefficients have been computed.

## Dependencies

Phase 3B full sector support completed at:

    9226f83

Signed-structure prior art was recorded at:

    f2bc083

Phase 3B established the basis-independent support architecture:

\[
RRR:
\quad
\alpha+\beta+\gamma=0,
\]

\[
HRR:
\quad
\beta=-\alpha,
\]

with all HHR and HHH sectors identically zero.

## Literature convention

Phase 3C adopts the epsilon-canonical Chevalley-basis framework described by
Geck and Lang.

For a simple-root index set

\[
I=\{1,\ldots,8\},
\]

choose

\[
\epsilon:I\to\{\pm1\}
\]

such that adjacent Dynkin vertices receive opposite signs.

For the connected E8 Dynkin diagram there are exactly two such functions,
related by

\[
\epsilon\mapsto-\epsilon.
\]

The associated canonical root vectors are denoted

\[
\mathbf e_\alpha^\epsilon.
\]

Changing

\[
\epsilon\mapsto-\epsilon
\]

changes all canonical root vectors by one common global sign.

The repository will freeze one of the two choices explicitly.

## Coordinate convention

The existing canonical root representation remains the doubled-coordinate
representation

\[
q=2\alpha\in\mathbb Z^8.
\]

The Phase 3C simple roots are frozen in doubled coordinates as follows:

\[
q_{\alpha_1}
=
(2,-2,0,0,0,0,0,0),
\]

\[
q_{\alpha_2}
=
(0,2,-2,0,0,0,0,0),
\]

\[
q_{\alpha_3}
=
(0,0,2,-2,0,0,0,0),
\]

\[
q_{\alpha_4}
=
(0,0,0,2,-2,0,0,0),
\]

\[
q_{\alpha_5}
=
(0,0,0,0,2,-2,0,0),
\]

\[
q_{\alpha_6}
=
(0,0,0,0,0,2,2,0),
\]

\[
q_{\alpha_7}
=
(-1,-1,-1,-1,-1,-1,-1,-1),
\]

\[
q_{\alpha_8}
=
(0,0,0,0,0,2,-2,0).
\]

In ordinary coordinates these are divided by two.

This coordinate choice is a project convention compatible with the already
validated E8 root realization.

It does not change the abstract Lie algebra.

## Simple-root validation

Before using the above vectors as a simple system, the implementation must
verify independently that:

1. all eight vectors belong to the validated E8 root set;
2. every vector has squared norm 2;
3. the eight vectors have exact rank 8;
4. their Gram matrix is an E8 Cartan matrix;
5. every E8 root has integral coordinates in this basis;
6. the coefficients of every root are either all nonnegative or all
   nonpositive.

Failure of any condition must be reported rather than repaired by modifying
the root set.

## Dynkin adjacency

With the frozen numbering, adjacency is determined by

\[
\alpha_i\cdot\alpha_j=-1.
\]

The expected edges are:

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
6-7,
\]

\[
5-8.
\]

The implementation must derive these edges from the simple-root Gram matrix.

They are validation expectations, not graph-construction instructions.

## Cartan matrix

Because E8 is simply laced and every root has squared norm 2,

\[
a_{ij}
=
\langle\alpha_i,\alpha_j\rangle
=
\alpha_i\cdot\alpha_j.
\]

Thus the frozen simple-root coordinates determine the Cartan matrix exactly.

The implementation will export that matrix as a deterministic artifact.

## Root expansion

Every root will be expanded uniquely as

\[
\alpha
=
\sum_{i=1}^8 n_i\alpha_i,
\qquad
n_i\in\mathbb Z.
\]

All coefficients must be obtained by exact rational/integer linear algebra.

Floating-point inversion and rounding are prohibited.

## Positive and negative roots

A root is POSITIVE iff

\[
n_i\ge0
\]

for every \(i\).

A root is NEGATIVE iff

\[
n_i\le0
\]

for every \(i\).

The implementation must verify that every validated E8 root belongs to exactly
one of these classes.

No root ordering from earlier phases is allowed to define positivity.

## Height

For

\[
\alpha=\sum_i n_i\alpha_i,
\]

define

\[
\operatorname{ht}(\alpha)
=
\sum_i n_i.
\]

Negative roots therefore have negative height.

Height is determined entirely from the frozen simple-root expansion.

## Epsilon convention

Freeze

\[
\epsilon(1)=+1.
\]

Adjacency then determines the remaining values uniquely.

The frozen epsilon vector is expected to be

\[
\boxed{
(\epsilon(1),\ldots,\epsilon(8))
=
(+1,-1,+1,-1,+1,-1,+1,-1).
}
\]

The implementation must verify

\[
\epsilon(i)=-\epsilon(j)
\]

for every Dynkin edge.

The globally opposite choice

\[
-\epsilon
\]

is acknowledged as the other canonical convention but is not used for the
primary Phase 3C artifacts.

## Canonical Chevalley basis

Let

\[
\{e_i,f_i,h_i\}_{i=1}^8
\]

be Chevalley generators associated with the frozen simple roots.

The root vectors used downstream are the epsilon-canonical vectors

\[
\mathbf e_\alpha^\epsilon
\in
\mathfrak g_\alpha.
\]

The full canonical basis convention is therefore

\[
\mathscr B^\epsilon
=
\{
h_1,\ldots,h_8
\}
\cup
\{
\mathbf e_\alpha^\epsilon:
\alpha\in\Phi(E_8)
\}.
\]

## Full basis ordering

For any later scalar tensor artifact, basis indices are frozen as:

\[
0,\ldots,7
\]

for

\[
h_1,\ldots,h_8,
\]

followed by

\[
8,\ldots,247
\]

for the 240 epsilon-canonical root vectors in the existing deterministic
lexicographic root order.

No alternative ordering may be substituted silently.

## Opposite-root bracket convention

For the epsilon-canonical basis, adopt the documented relation

\[
[
\mathbf e_\alpha^\epsilon,
\mathbf e_{-\alpha}^\epsilon
]
=
(-1)^{\operatorname{ht}(\alpha)}
h_\alpha.
\]

Here

\[
h_\alpha
\]

is the coroot associated with \(\alpha\).

Because E8 is simply laced,

\[
h_\alpha
=
\sum_i n_i h_i
\]

when

\[
\alpha=\sum_i n_i\alpha_i.
\]

This relation fixes the root/opposite-root bracket sign convention.

## Root-root structure constants

For roots

\[
\alpha,\beta,\alpha+\beta\in\Phi,
\]

define

\[
[
\mathbf e_\alpha^\epsilon,
\mathbf e_\beta^\epsilon
]
=
N_{\alpha,\beta}^\epsilon
\mathbf e_{\alpha+\beta}^\epsilon.
\]

Because E8 is simply laced,

\[
N_{\alpha,\beta}^\epsilon
\in
\{\pm1\}.
\]

The primary Phase 3C sign rule will be the Geck-Lang simply-laced canonical
formula

\[
N_{\alpha,\beta}^\epsilon
=
\hat\eta^\epsilon(\alpha,\beta).
\]

Writing

\[
\alpha=\sum_i n_i\alpha_i,
\]

define

\[
\operatorname{sgn}(\alpha)
=
\begin{cases}
+1,&\alpha>0,\\
-1,&\alpha<0.
\end{cases}
\]

The implementation will use the equivalent formula

\[
\boxed{
\hat\eta^\epsilon(\alpha,\beta)
=
\operatorname{sgn}(\alpha)
\operatorname{sgn}(\beta)
\operatorname{sgn}(\alpha+\beta)
\prod_i
\epsilon(i)^{
n_i\langle\alpha_i,\beta\rangle
}.
}
\]

Since every factor is \(\pm1\), all arithmetic is exact.

## Root-root sign identities

The implementation must independently verify, for every admissible root pair,

\[
N_{\beta,\alpha}^\epsilon
=
-N_{\alpha,\beta}^\epsilon,
\]

and

\[
N_{-\alpha,-\beta}^\epsilon
=
-N_{\alpha,\beta}^\epsilon.
\]

For every simple root \(\alpha_i\) and root \(\beta\) such that

\[
\alpha_i+\beta\in\Phi,
\]

the canonical formula predicts

\[
N_{\alpha_i,\beta}^\epsilon
=
\epsilon(i).
\]

These are validation checks.

## Invariant bilinear form normalization

The invariant bilinear form is unique up to overall scalar on the simple Lie
algebra E8.

Phase 3C fixes that scalar by defining the normalized form

\[
B_0
\]

through

\[
\boxed{
B_0(h_i,h_j)=a_{ij}.
}
\]

This is a project normalization choice.

It is not claimed to be the only convention used in the literature.

Because the root system is simply laced, this implies

\[
B_0(h_i,h_\alpha)
=
\alpha(h_i).
\]

## Opposite-root pairing

Using invariance of \(B_0\) and the frozen opposite-root bracket convention,

\[
[
\mathbf e_\alpha^\epsilon,
\mathbf e_{-\alpha}^\epsilon
]
=
(-1)^{\operatorname{ht}(\alpha)}h_\alpha,
\]

Phase 3C derives

\[
\boxed{
B_0(
\mathbf e_\alpha^\epsilon,
\mathbf e_{-\alpha}^\epsilon
)
=
(-1)^{\operatorname{ht}(\alpha)}.
}
\]

This value is not separately imposed.

It must follow from the frozen bracket and bilinear-form normalization.

## Root-root-root Cartan coefficient consequence

For a zero-sum root triple

\[
\alpha+\beta+\gamma=0,
\]

one has

\[
[
\mathbf e_\beta^\epsilon,
\mathbf e_\gamma^\epsilon
]
=
N_{\beta,\gamma}^\epsilon
\mathbf e_{-\alpha}^\epsilon.
\]

Hence the normalized Cartan 3-form coefficient will later satisfy

\[
\Omega_0(
\mathbf e_\alpha^\epsilon,
\mathbf e_\beta^\epsilon,
\mathbf e_\gamma^\epsilon
)
=
N_{\beta,\gamma}^\epsilon
(-1)^{\operatorname{ht}(\alpha)}.
\]

Phase 3C freezes this formula but does not yet export the full signed
root-root-root tensor.

## Cartan-root-root coefficient consequence

For a simple-coroot Cartan basis vector \(h_i\),

\[
\Omega_0(
h_i,
\mathbf e_\alpha^\epsilon,
\mathbf e_{-\alpha}^\epsilon
)
=
(-1)^{\operatorname{ht}(\alpha)}
\alpha(h_i).
\]

Again, Phase 3C freezes the normalization required for this formula but does
not yet construct the complete 248-dimensional coefficient tensor.

## Canonical versus conventional content

The following are structural/canonical relative to the documented
epsilon-canonical framework:

- the simple Lie algebra E8;
- one-dimensional root spaces;
- the epsilon-canonical root-vector system after fixing epsilon and Chevalley
  generators;
- the canonical structure-constant formula;
- alternation identities.

The following are explicit repository conventions:

- the chosen coordinate simple-root system;
- the numbering \(1,\ldots,8\);
- the choice \(\epsilon(1)=+1\) rather than \(-1\);
- the ordering of the 248 basis vectors;
- the scalar normalization
  \[
  B_0(h_i,h_j)=a_{ij}.
  \]

These distinctions must remain explicit downstream.

## Phase 3C computational outputs

Phase 3C will construct and export:

1. the eight simple roots in doubled coordinates;
2. the exact Cartan matrix;
3. the derived Dynkin edge set;
4. the exact simple-root coefficient vector for all 240 roots;
5. positive/negative classification;
6. root heights;
7. the epsilon vector;
8. the canonical \(N_{\alpha,\beta}^\epsilon\) table for every root pair whose
   sum is a root;
9. validation identities for the sign table;
10. the normalized opposite-root pairing implied by invariance.

## Prohibited operations

Phase 3C must not:

- select root-vector signs ad hoc;
- tune signs to make the Cartan 3-form alternating;
- change epsilon after inspecting downstream coefficients;
- use floating-point root-coordinate inversion;
- silently replace the frozen simple-root system;
- silently use a different bilinear-form scale;
- describe the chosen B0 scale as uniquely canonical;
- construct a dense 248^3 tensor.

## Success criteria

Phase 3C is a PASS only if:

1. the frozen simple roots form a valid E8 simple system;
2. all 240 roots have exact integral simple-root coordinates;
3. every root is uniquely positive or negative;
4. the derived Dynkin diagram agrees with E8;
5. epsilon alternates across every Dynkin edge;
6. all admissible canonical root-root structure constants are exactly
   \(\pm1\);
7. antisymmetry and simultaneous-root-negation identities hold globally;
8. the simple-root structure-constant checks agree with epsilon;
9. the B0 normalization is internally consistent with the opposite-root
   pairing derivation;
10. no full Cartan 3-form tensor is constructed prematurely.

## Interpretation boundary

Phase 3C establishes a reproducible signed basis convention.

It does NOT establish:

- novelty of the canonical sign table;
- a new Chevalley basis;
- a new structure-constant formula;
- the final signed Cartan 3-form tensor;
- a generalized metric interpretation;
- a causal interpretation of the initiating dream.

## Next phase

After Phase 3C closeout, Phase 3D may construct the signed sparse Cartan
3-form coefficient tensor in the frozen 248-element basis.

That phase can then compare:

- unsigned Phase 2C support;
- signed root-root-root coefficients;
- Cartan-root-root coefficients;
- full alternation;
- exact sparse support.
