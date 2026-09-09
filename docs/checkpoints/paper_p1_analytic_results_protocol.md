# Paper P1 — Analytic Results Protocol

## Status

STATUS: PAPER_P1_ANALYTIC_RESULTS_PROTOCOL_FROZEN

## Purpose

Paper P1 converts the principal computational observations into concise
mathematical propositions and proofs suitable for the manuscript:

**An Exact Sparse Realization of the \(E_8\) Cartan 3-Form**

No new theorem-level novelty is asserted merely because these propositions
are written explicitly.

Their role is to make the paper's headline counts analytically transparent
and independently checkable.

## Frozen setting

Let:

\[
\Phi=\Phi(E_8)
\]

be the 240-root system normalized by:

\[
(\alpha,\alpha)=2.
\]

Let:

\[
\mathfrak e_8
=
\mathfrak h
\oplus
\bigoplus_{\alpha\in\Phi}
\mathfrak g_\alpha.
\]

Use the frozen Chevalley basis:

\[
\mathscr B
=
(h_1,\ldots,h_8,
e_{\alpha_0},\ldots,e_{\alpha_{239}}).
\]

Let:

\[
B_0(h_i,h_j)=a_{ij}.
\]

Define:

\[
g(X,Y,Z)
=
B_0(X,[Y,Z]).
\]

All propositions concern this fixed basis and normalization.

## Proposition P1.1 — Root-sector support criterion

For roots:

\[
\alpha,\beta,\gamma\in\Phi,
\]

\[
\boxed{
g(e_\alpha,e_\beta,e_\gamma)\neq0
\iff
\alpha+\beta+\gamma=0.
}
\]

### Proof plan

If:

\[
[e_\beta,e_\gamma]\neq0
\]

and \(\beta+\gamma\) is a root, then:

\[
[e_\beta,e_\gamma]
\in
\mathfrak g_{\beta+\gamma}.
\]

Invariant-form root-space orthogonality gives:

\[
B_0(
\mathfrak g_\alpha,
\mathfrak g_{\beta+\gamma}
)
\neq0
\]

only when:

\[
\alpha+\beta+\gamma=0.
\]

If:

\[
\gamma=-\beta,
\]

then:

\[
[e_\beta,e_{-\beta}]
\in\mathfrak h,
\]

which is orthogonal to:

\[
\mathfrak g_\alpha.
\]

Conversely, when:

\[
\alpha+\beta+\gamma=0,
\]

one has:

\[
\beta+\gamma=-\alpha\in\Phi,
\]

the corresponding root bracket is nonzero and opposite root spaces pair
nondegenerately.

## Proposition P1.2 — Number of ordered RRR coefficients

The number of ordered nonzero root-root-root coefficients is:

\[
\boxed{
13440.
}
\]

### Proof

For every fixed root:

\[
\beta,
\]

the E8 root inner-product census contains exactly:

\[
56
\]

roots \(\gamma\) satisfying:

\[
(\beta,\gamma)=-1.
\]

For a simply-laced root system this is equivalent to:

\[
\beta+\gamma\in\Phi.
\]

The third root is then uniquely:

\[
\alpha=-(\beta+\gamma).
\]

Therefore:

\[
|\operatorname{supp}_{RRR}g|
=
240\cdot56
=
\boxed{13440}.
\]

## Corollary P1.3 — Unordered zero-sum triples

Since a nonzero RRR triple consists of three distinct roots and all six
permutations are nonzero:

\[
\boxed{
\frac{13440}{6}=2240
}
\]

unordered zero-sum root triples occur.

Negation pairs these into:

\[
\boxed{
1120
}
\]

orbits.

No novelty is claimed for either count.

## Proposition P1.4 — Root hypergraph degree

Let:

\[
\mathcal H
\]

be the 3-uniform hypergraph whose vertices are the 240 roots and whose edges
are unordered zero-sum triples.

Then every vertex has degree:

\[
\boxed{
28.
}
\]

### Proof

Fix:

\[
\alpha\in\Phi.
\]

There are:

\[
56
\]

roots \(\beta\) satisfying:

\[
(\alpha,\beta)=-1.
\]

Every hyperedge containing \(\alpha\) contains exactly two such other roots.

Conversely, either such root determines the unique third root:

\[
\gamma=-(\alpha+\beta).
\]

Hence:

\[
2\deg(\alpha)=56,
\]

so:

\[
\boxed{
\deg(\alpha)=28.
}
\]

## Proposition P1.5 — Hypergraph linearity

Any two distinct roots lie in at most one hyperedge.

### Proof

If:

\[
\{\alpha,\beta,\gamma\}
\]

is a zero-sum edge, then:

\[
\gamma=-(\alpha+\beta).
\]

Thus a pair:

\[
\{\alpha,\beta\}
\]

determines at most one possible third vertex.

Therefore pair codegree is:

\[
\boxed{
0\text{ or }1.
}
\]

## Corollary P1.6 — Number of active root pairs

A linear 3-uniform hypergraph with 2240 edges has:

\[
3\cdot2240
=
\boxed{
6720
}
\]

active unordered vertex pairs.

## Proposition P1.7 — Cartan evaluation census

For every simple root:

\[
\alpha_i,
\]

the 240 roots \(\alpha\) satisfy:

\[
\alpha(h_i)\in
\{-2,-1,0,+1,+2\}
\]

with multiplicities:

\[
1,\quad56,\quad126,\quad56,\quad1.
\]

Hence exactly:

\[
\boxed{
114
}
\]

roots have:

\[
\alpha(h_i)\neq0.
\]

### Proof

Since E8 is simply laced:

\[
\alpha(h_i)
=
(\alpha,\alpha_i).
\]

For a fixed root \(\alpha_i\), the standard E8 root inner-product census is:

\[
-2:1,
\]

\[
-1:56,
\]

\[
0:126,
\]

\[
+1:56,
\]

\[
+2:1.
\]

Therefore the nonzero multiplicity is:

\[
1+56+56+1
=
114.
\]

## Proposition P1.8 — Number of ordered HRR coefficients

The number of ordered nonzero Cartan-root-root coefficients is:

\[
\boxed{
2736.
}
\]

### Proof

For:

\[
g(h_i,e_\alpha,e_{-\alpha}),
\]

the coefficient is nonzero exactly when:

\[
\alpha(h_i)\neq0.
\]

For every:

\[
i=1,\ldots,8,
\]

there are 114 oriented roots with nonzero evaluation.

Thus for one fixed Cartan position:

\[
8\cdot114
=
912.
\]

There are three possible positions of the Cartan argument in an ordered
triple.

Therefore:

\[
|\operatorname{supp}_{HRR}g|
=
3\cdot912
=
\boxed{
2736.
}
\]

Equivalent unordered count:

\[
\boxed{
456.
}
\]

## Theorem P1.9 — Complete sparse support census

In the frozen 248-element basis:

\[
\boxed{
|\operatorname{supp}g|
=
16176.
}
\]

### Proof

The only nonzero sectors are:

\[
RRR
\]

and:

\[
HRR.
\]

Therefore:

\[
|\operatorname{supp}g|
=
13440+2736
=
\boxed{
16176.
}
\]

The complete ordered domain contains:

\[
248^3
=
15252992
\]

basis triples.

Hence the support density is:

\[
\boxed{
\frac{16176}{15252992}
}
\]

or approximately:

\[
0.001060513242254.
\]

## Proposition P1.10 — RRR sign multiplicities

Every nonzero RRR coefficient has magnitude:

\[
1.
\]

The exact ordered multiplicities are:

\[
\boxed{
-1:6720,
\qquad
+1:6720.
}
\]

### Proof

Each unordered zero-sum root triple has six permutations.

For an alternating 3-form:

- three even permutations have coefficient \(c\);
- three odd permutations have coefficient \(-c\).

Since every RRR coefficient has:

\[
|c|=1,
\]

each of the 2240 unordered root triples contributes three \(+1\) and three
\(-1\) ordered entries.

Thus:

\[
3\cdot2240
=
6720
\]

of each sign.

## Proposition P1.11 — Magnitude-two HRR census

Exactly:

\[
\boxed{
48
}
\]

ordered HRR coefficients have magnitude two.

Their signs split as:

\[
\boxed{
-2:24,
\qquad
+2:24.
}
\]

### Proof

For fixed:

\[
h_i,
\]

the only roots satisfying:

\[
|\alpha(h_i)|=2
\]

are:

\[
\alpha=\pm\alpha_i.
\]

Thus each simple Cartan direction contributes one underlying unordered basis
triple:

\[
\{h_i,e_{\alpha_i},e_{-\alpha_i}\}.
\]

There are eight such triples.

Each has six ordered permutations.

Therefore:

\[
8\cdot6
=
48
\]

ordered magnitude-two coefficients.

Alternation gives equal sign multiplicities:

\[
24
\]

positive and:

\[
24
\]

negative.

## Proposition P1.12 — Magnitude-one HRR census

The remaining HRR coefficients have magnitude one.

Their number is:

\[
2736-48
=
2688.
\]

Alternation gives:

\[
\boxed{
-1:1344,
\qquad
+1:1344
}
\]

within the HRR sector.

## Theorem P1.13 — Complete coefficient spectrum

The complete nonzero basis coefficient spectrum of \(g\) is:

\[
\boxed{
-2:24,
\qquad
-1:8064,
\qquad
+1:8064,
\qquad
+2:24.
}
\]

### Proof

Combine the RRR contribution:

\[
-1:6720,
\qquad
+1:6720
\]

with the HRR contribution:

\[
-2:24,
\]

\[
-1:1344,
\]

\[
+1:1344,
\]

\[
+2:24.
\]

Hence:

\[
6720+1344
=
8064.
\]

Therefore:

\[
\boxed{
-2:24,\quad
-1:8064,\quad
+1:8064,\quad
+2:24.
}
\]

The total is:

\[
24+8064+8064+24
=
16176.
\]

## Proposition P1.14 — Recovery of the Lie bracket

For all:

\[
Y,Z\in\mathfrak e_8,
\]

the bracket is uniquely determined by \(g\) and \(B_0\):

\[
\boxed{
[Y,Z]
=
B_0^{-1}
\bigl(
g(\,\cdot\,,Y,Z)
\bigr).
}
\]

### Proof

By definition:

\[
g(X,Y,Z)
=
B_0(X,[Y,Z])
\]

for every:

\[
X\in\mathfrak e_8.
\]

Since:

\[
B_0
\]

is nondegenerate, there is a unique vector \(W\) satisfying:

\[
B_0(X,W)
=
g(X,Y,Z)
\]

for every \(X\).

The vector:

\[
W=[Y,Z]
\]

satisfies this condition.

Therefore it is unique.

In components:

\[
\boxed{
C^a{}_{bc}
=
B_0^{ad}g_{dbc}.
}
\]

This proposition is standard Lie theory and is included to explain the
computational meaning of the sparse tensor.

## Computational role after analytic proofs

The repository remains essential for:

- explicit coefficient generation;
- exact sign assignment;
- deterministic dataset export;
- two-route coefficient comparison;
- exhaustive Jacobi validation;
- invariant-form validation;
- full 61,504-pair bracket recovery.

But the headline counts:

\[
13440,
\quad
2736,
\quad
16176,
\]

and:

\[
24,
\quad
8064,
\quad
8064,
\quad
24
\]

will not depend solely on computation in the manuscript.

## Proof-policy boundary

Paper P1 must not elevate a straightforward derived count to a novelty claim.

The analytic propositions establish correctness and exposition.

Novelty remains governed by the completed Phase 6A classification.

## Next manuscript step

After this protocol is frozen:

1. write the propositions in manuscript LaTeX;
2. prepare a concise notation table;
3. assemble the bibliography;
4. draft Sections 2–5 around these analytic results;
5. use computational outputs only as independent confirmations;
6. perform an internal proof audit.

STATUS:

    PAPER_P1_ANALYTIC_RESULTS_PROTOCOL_FROZEN