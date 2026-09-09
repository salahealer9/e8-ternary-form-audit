# Notation

## Initiating notation

\[
g(v_1,v_2,v_3)
\]

is retained as the literal remembered notation.

Within the mathematical analysis it will initially be denoted

\[
g_{\mathrm{obs}}(v_1,v_2,v_3)
\]

when necessary to distinguish the observation from established objects.

No tensor character is assigned to \(g_{\mathrm{obs}}\).

## Vector spaces

\(V\) denotes a generic real or complex vector space.

Vectors are denoted

\[
v,\quad v_1,\quad v_2,\quad v_3.
\]

## Lie algebra

\[
\mathfrak g
\]

denotes a Lie algebra.

For the primary branch,

\[
\mathfrak g=\mathfrak e_8.
\]

Lie-algebra elements are denoted

\[
X,Y,Z.
\]

The Lie bracket is

\[
[X,Y].
\]

## Bilinear invariant form

\[
B(X,Y)
\]

denotes a chosen invariant nondegenerate symmetric bilinear form on the
semisimple Lie algebra.

Normalization choices must be stated explicitly when numerical values depend
on them.

## Cartan 3-form

\[
\Omega(X,Y,Z)=B(X,[Y,Z]).
\]

The symbol \(\Omega\) is used to prevent accidental identification of this
known object with the remembered symbol \(g\).

## E8 roots

The E8 root system is denoted

\[
\Phi(E_8).
\]

Individual roots are

\[
\alpha,\beta,\gamma\in\Phi(E_8).
\]

The Euclidean inner product on the 8-dimensional root realization is

\[
\alpha\cdot\beta.
\]

The normalization used in the primary implementation will satisfy

\[
\alpha\cdot\alpha=2.
\]

## Root vectors

For a root \(\alpha\), a corresponding Lie-algebra root vector is denoted

\[
E_\alpha\in\mathfrak g_\alpha.
\]

A root \(\alpha\in\mathbb R^8\) must not be conflated with the Lie-algebra
element \(E_\alpha\in\mathfrak e_8\).

## Zero-sum root triple

A root triple satisfies

\[
\alpha+\beta+\gamma=0.
\]

Unless explicitly stated otherwise:

- ordered triple means \((\alpha,\beta,\gamma)\);
- unordered triple means \(\{\alpha,\beta,\gamma\}\).

## Ternary incidence tensor

If introduced, the root-level support tensor will be denoted

\[
T_{ijk}.
\]

Its precise definition must be frozen before numerical analysis.

It must not automatically be called a metric tensor.

## Symmetry terminology

A trilinear form \(F\) is alternating when permutation of two arguments changes
its sign.

A trilinear form \(D\) is symmetric when it is invariant under every
permutation of its arguments.

These cases must remain distinct throughout the project.
