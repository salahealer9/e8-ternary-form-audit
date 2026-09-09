# Phase 5A Candidate-Neutral Literature Checkpoint

## Status

STATUS: PHASE5A_CANDIDATE_NEUTRAL_LITERATURE_CHECKPOINT_FROZEN

## Chronology

Phase 5A interpretation protocol was frozen at commit:

    084d070

The exact Phase 0 comparison criteria K1-K7 and interpretation classes I0-I3
were then recovered verbatim from the frozen preregistration.

This literature checkpoint is recorded BEFORE any candidate-by-criterion
assessment is performed.

Its purpose is to prevent the extensively developed C1 candidate from
receiving asymmetric treatment relative to C0, C2, C3, or C4.

## Frozen Phase 0 criteria

### K1 — Arity match

Does the object intrinsically take three arguments?

### K2 — Vector-like domain match

Are its arguments naturally vectors, tangent vectors, representation vectors,
or Lie-algebra elements?

### K3 — Canonicality

Is the object canonically or naturally defined once the relevant mathematical
structure is specified?

### K4 — Invariance

Is the ternary object preserved by a nontrivial symmetry group?

### K5 — Geometric content

Does it encode geometry rather than being an arbitrary user-defined function?

### K6 — Metric relation

Is there a precise relation to an ordinary bilinear metric or invariant
bilinear form?

### K7 — Direct E8 relevance

Is the object intrinsically associated with E8 rather than connected through
a discretionary chain of analogies?

No criterion will be reweighted.

## Frozen Phase 0 interpretation classes

### I0 — Generic notation only

No meaningful correspondence beyond the fact that many functions can have
three arguments.

### I1 — Established ternary analogue

One or more known canonical mathematical structures provide a genuine
three-vector analogue.

### I2 — Direct E8 correspondence

A canonical E8 ternary structure exists and its root-level support is
reproduced computationally.

### I3 — Additional structural result

The investigation reveals a mathematically nontrivial relationship not already
contained in the standard definitions or obvious root-system identities.

I3 requires separate verification and literature checking.

None of I0-I3 constitutes evidence about the causal origin of the dream.

## C0 — Generic ternary function

C0 requires no specialist prior art.

It represents the minimal interpretation:

\[
g(v_1,v_2,v_3)
\]

is simply a function with three argument slots.

No canonicality, invariance, metric relation, geometry, or E8 structure is
implied by C0 itself.

C0 remains the baseline alternative against which more structured
interpretations must be compared.

## C1 — E8 Cartan 3-form

### Established structure

For a semisimple Lie algebra

\[
\mathfrak g,
\]

the Cartan 3-form is an established alternating trilinear form:

\[
\omega_{\mathfrak g}(X,Y,Z)
=
\langle X,[Y,Z]\rangle,
\]

where

\[
\langle\ ,\ \rangle
\]

is an invariant bilinear form, conventionally the Killing form.

Reference:

Hông Vân Lê,

"Geometric structures associated with a simple Cartan 3-form",

Journal of Geometry and Physics 70 (2013), 205-223.

DOI:

    10.1016/j.geomphys.2013.03.028

arXiv:

    1103.1201

### Specificity boundary

The existence of a Cartan 3-form is NOT unique to E8.

It is a construction associated with semisimple/simple Lie algebras more
generally.

Therefore the fact that an E8 Cartan 3-form exists supports:

- ternary structure;
- Lie-algebra domain;
- canonicality;
- invariance;
- geometric structure;
- bilinear-form relation;

but existence of the construction alone does NOT distinguish E8 from every
other simple Lie algebra.

### E8-specific realization

What is specifically established by this repository is that, after choosing

\[
\mathfrak g=\mathfrak e_8,
\]

the root-space support of that form was independently reconstructed and
matched exactly to the Phase 2C E8 ternary incidence structure.

That is a D2 project result, not a D0 feature of the initiating notation.

## C2 — G2 invariant alternating 3-form

### Established structure

Let

\[
V\cong\mathbb R^7.
\]

The standard positive G2 3-form

\[
\varphi\in\Lambda^3V^*
\]

is an alternating trilinear form.

In an octonionic/cross-product description it may be expressed as:

\[
\varphi(a,b,c)
=
\langle a\times b,c\rangle.
\]

Its stabilizer in

\[
GL(7,\mathbb R)
\]

is:

\[
G_2.
\]

A positive G2 3-form also determines the associated metric and volume form.

Thus C2 has a particularly direct relationship between:

- a three-vector form;
- an exceptional Lie group;
- metric structure;
- geometry.

### Literature boundary

This is established mathematics and is not a project discovery.

The G2 example is therefore a serious comparator to C1 whenever the evidence
being assessed consists only of an unspecified three-vector expression.

## C3 — E6 cubic / symmetric trilinear form

### Established structure

The 27-dimensional fundamental/minuscule representation associated with E6
carries an invariant cubic norm.

Polarization gives a symmetric trilinear form:

\[
\Phi(x,y,z).
\]

The E6 action preserves this cubic/symmetric trilinear structure.

Thus C3 supplies an established exceptional-Lie-theoretic ternary structure
with:

\[
\dim V=27.
\]

Its symmetry type is:

\[
\boxed{\text{SYMMETRIC}}
\]

rather than alternating.

### Metric-relation boundary

The invariant cubic is not naturally defined as:

\[
B(x,[y,z])
\]

from an E6-invariant bilinear metric on the 27-dimensional representation.

In a standard exceptional-Jordan-algebra presentation one may introduce a
bilinear pairing to identify the representation with its dual and express
cross-product operations.

However E6 itself does not preserve that auxiliary pairing; the subgroup
preserving both the cubic structure and that pairing is F4.

Therefore C3 has a substantially weaker/directly different K6 relationship
than C1 or C2.

### Literature boundary

The E6 cubic and its polarized symmetric trilinear form are established prior
art.

They are not project discoveries.

## C4 — Primary established comparator

C4 is broad by definition.

To avoid retrospective cherry-picking among unrelated ternary objects, Phase
5A freezes ONE primary C4 representative before criterion scoring:

\[
\boxed{
\tau(u,v,w)=u\cdot(v\times w)
}
\]

on oriented Euclidean

\[
\mathbb R^3.
\]

This is the classical scalar triple product / oriented Euclidean volume form.

### Reasons for choosing this representative

It is intentionally a STRONG rather than weak comparator.

It:

1. intrinsically takes three arguments;
2. takes ordinary vectors;
3. is naturally determined once Euclidean metric and orientation are fixed;
4. is preserved by the orientation-preserving orthogonal group
   \[
   SO(3);
   \]
5. measures signed volume;
6. has a direct relation to the ordinary Euclidean bilinear metric through
   the dot product.

It therefore satisfies many of K1-K6 without invoking exceptional Lie theory.

### Geometry

The absolute value:

\[
|\tau(u,v,w)|
\]

is the volume of the parallelepiped spanned by the three vectors.

The sign records orientation.

The form is alternating.

### Invariance boundary

The scalar triple product is preserved by:

\[
SO(3).
\]

Under an orientation-reversing orthogonal transformation its sign reverses.

Thus the appropriate invariance statement is orientation-preserving
orthogonal invariance, not full O(3) scalar invariance.

### E8 boundary

The scalar triple product has no intrinsic E8 association.

It therefore provides a useful control showing that strong scores on K1-K6
need not imply K7.

## Why C4 is frozen to one representative

C4 contains many possible established ternary structures.

It would be methodologically invalid to:

- use one C4 structure to score K1;
- another to score K3;
- another to score K6;

and thereby construct an artificial composite candidate.

Therefore Phase 5A uses the scalar triple product as the PRIMARY C4
representative for the formal K1-K7 matrix.

Other C4 examples may be mentioned qualitatively but may not be substituted
criterion-by-criterion.

## Candidate symmetry summary

The established primary structures have:

### C0

Unspecified symmetry.

### C1

Alternating.

### C2

Alternating.

### C3

Symmetric.

### C4

Alternating.

The initiating datum D0 does not specify permutation symmetry.

Therefore these distinctions characterize candidates but do not constitute
D0-based candidate selection.

## Candidate dimension summary

### C0

Unspecified.

### C1

\[
248
\]

for the E8 adjoint Lie algebra.

### C2

\[
7.
\]

### C3

\[
27.
\]

### C4

\[
3
\]

for the frozen scalar-triple-product representative.

D0 supplies no dimension.

Therefore dimension is descriptive but not discriminating at D0.

## Candidate metric-relation summary

### C0

No metric relation is intrinsic.

### C1

Direct:

\[
\omega(X,Y,Z)
=
B(X,[Y,Z]).
\]

### C2

Direct:

\[
\varphi(a,b,c)
=
\langle a\times b,c\rangle,
\]

and the positive 3-form itself determines a metric.

### C3

No corresponding direct E6-invariant bilinear metric construction on the
27-dimensional representation is part of the defining cubic invariant.

### C4

Direct:

\[
\tau(u,v,w)
=
u\cdot(v\times w).
\]

## Candidate E8-specificity summary

### C0

None.

### C1

Direct once the Lie algebra is specified as:

\[
\mathfrak e_8.
\]

However Cartan 3-forms as a class are not E8-exclusive.

### C2

None.

### C3

None.

### C4

None.

## Consequence for the forthcoming matrix

The candidate matrix must distinguish two different facts.

### Structural property

Whether a candidate actually satisfies K1-K7 as mathematics.

### Evidential discrimination

Whether D0 or documented D1 supplied that property BEFORE candidate
development.

For example:

C1 may strongly satisfy:

\[
K3,K4,K5,K6,K7
\]

as a mathematical structure.

But if D0 contained no evidence of:

- Lie algebra;
- invariance;
- geometry;
- bilinear form;
- E8;

then those criteria cannot be counted as independent predictions made by D0.

This distinction will be explicit in every matrix row.

## No scoring performed yet

STATUS:

    CANDIDATE_SCORING_PERFORMED: NO

No K1-K7 assessment label has been assigned in this checkpoint.

No candidate ranking has been performed.

No I0-I3 interpretation class has been selected.

This checkpoint records only candidate-neutral mathematical prior art and
freezes the C4 primary comparator before scoring.