# Derivation chain

This document summarizes the principal exact dependency chain leading to the
sparse \(E_8\) Cartan 3-form.

## 1. \(E_8\) roots

The standard \(E_8\) root system contains

\[
|\Phi(E_8)|=240
\]

roots of squared norm

\[
(\alpha,\alpha)=2.
\]

For every fixed root \(\alpha\), the inner-product census is

\[
-2:1,\qquad
-1:56,\qquad
0:126,\qquad
+1:56,\qquad
+2:1.
\]

## 2. Ordered zero-sum root triples

If

\[
(\beta,\gamma)=-1,
\]

then

\[
\beta+\gamma\in\Phi(E_8).
\]

The third root

\[
\alpha=-(\beta+\gamma)
\]

is therefore uniquely determined.

Since each of the \(240\) roots has \(56\) roots at inner product \(-1\),

\[
240\cdot56=13{,}440
\]

ordered zero-sum triples are obtained.

Hence

\[
N_{\mathrm{RRR}}=13{,}440.
\]

## 3. Unordered triples

Each unordered zero-sum triple has \(3!=6\) orderings, so

\[
\frac{13{,}440}{6}=2240.
\]

Thus the root support contains

\[
2240
\]

unordered ternary incidences.

## 4. \(A_2\) classes

For

\[
\alpha+\beta+\gamma=0
\]

with all three roots of squared norm \(2\),

\[
\gamma=-(\alpha+\beta)
\]

implies

\[
2
=
(\alpha+\beta,\alpha+\beta)
=
2+2+2(\alpha,\beta),
\]

so

\[
(\alpha,\beta)=-1,
\]

and cyclically for the other pairs.

The six roots

\[
\{\pm\alpha,\pm\beta,\pm\gamma\}
\]

therefore form an \(A_2\) root subsystem.

Negation pairs the \(2240\) zero-sum triples, giving

\[
\frac{2240}{2}=1120
\]

\(A_2\)/negation classes.

## 5. Root-support hypergraph

Define the hypergraph

\[
\mathcal H=(V,E)
\]

with

\[
V=\Phi(E_8)
\]

and

\[
E=
\left\{
\{\alpha,\beta,\gamma\}:
\alpha+\beta+\gamma=0
\right\}.
\]

Then

\[
|V|=240,
\qquad
|E|=2240.
\]

Each root has \(56\) eligible partners, with two partners per hyperedge, so

\[
\deg(\alpha)=\frac{56}{2}=28.
\]

A pair of roots determines at most one third root, hence the hypergraph is
linear and pair codegrees are \(0\) or \(1\).

The number of active unordered root pairs is therefore

\[
3\cdot2240=6720.
\]

## 6. Root-sector Cartan 3-form

Let

\[
g(X,Y,Z)=B_0(X,[Y,Z]).
\]

For root vectors,

\[
g(e_\alpha,e_\beta,e_\gamma)\neq0
\]

if and only if

\[
\alpha+\beta+\gamma=0.
\]

Therefore

\[
|\operatorname{supp}_{\mathrm{RRR}}g|
=
13{,}440.
\]

Alternation implies that each unordered zero-sum triple contributes three
positive and three negative coefficients.

Hence

\[
-1:6720,
\qquad
+1:6720
\]

in the root sector.

## 7. Cartan--root--root sector

For a simple Cartan generator \(h_i\),

\[
g(h_i,e_\alpha,e_{-\alpha})
=
(-1)^{\operatorname{ht}(\alpha)}\alpha(h_i).
\]

For fixed \(h_i\), the \(E_8\) inner-product census gives

\[
1+56+56+1=114
\]

roots with nonzero evaluation.

With \(8\) Cartan directions,

\[
8\cdot114=912
\]

nonzero coefficients occur when the Cartan argument is in one fixed tensor
position.

Since it may occupy any of three positions,

\[
N_{\mathrm{HRR}}
=
3\cdot912
=
2736.
\]

## 8. Total sparse support

Combining both nonzero sector types,

\[
13{,}440+2736=16{,}176.
\]

Therefore

\[
\boxed{
|\operatorname{supp}g|=16{,}176.
}
\]

The complete tensor domain has

\[
248^3=15{,}252{,}992
\]

ordered basis triples.

## 9. Magnitude-two coefficients

For fixed \(i\), the only roots satisfying

\[
|\alpha(h_i)|=2
\]

are

\[
\pm\alpha_i.
\]

Thus there are \(8\) underlying basis triples

\[
\{h_i,e_{\alpha_i},e_{-\alpha_i}\}.
\]

Each has \(6\) permutations, giving

\[
8\cdot6=48
\]

magnitude-two coefficients.

Alternation splits them equally:

\[
-2:24,
\qquad
+2:24.
\]

## 10. Remaining Cartan coefficients

The remaining Cartan-sector coefficients number

\[
2736-48=2688.
\]

They have magnitude \(1\), and alternation gives

\[
-1:1344,
\qquad
+1:1344.
\]

Adding the root-sector contribution gives the complete coefficient census

\[
\boxed{
-2:24,\qquad
-1:8064,\qquad
+1:8064,\qquad
+2:24.
}
\]

## 11. Recovering the bracket

Because \(B_0\) is nondegenerate,

\[
g(X,Y,Z)=B_0(X,[Y,Z])
\]

determines the Lie bracket uniquely.

If

\[
B_{0,ad}=B_0(b_a,b_d)
\]

and

\[
B_0^{ad}
\]

denotes the inverse matrix, then

\[
C^a{}_{bc}
=
B_0^{ad}g_{dbc}.
\]

Hence

\[
[Y,Z]
=
B_0^{-1}\bigl(g(\,\cdot\,,Y,Z)\bigr).
\]

This equality is checked computationally on all

\[
248^2=61{,}504
\]

ordered basis pairs.

## 12. Final dependency chain

The principal derivation can therefore be summarized as

\[
\boxed{
\begin{aligned}
240\ E_8\ \text{roots}
&\longrightarrow
13{,}440\ \text{ordered zero-sum triples}\\
&\longrightarrow
2240\ \text{unordered triples}\\
&\longrightarrow
1120\ A_2\text{ classes}\\
&\longrightarrow
13{,}440\ \mathrm{RRR}\\
&\quad+\ 2736\ \mathrm{HRR}\\
&\longrightarrow
16{,}176\ \text{nonzero }g_{abc}\\
&\longrightarrow
\text{complete coefficient census}\\
&\longrightarrow
[E_8\text{ bracket recovered from }g\text{ and }B_0].
\end{aligned}
}
\]

The computational implementation independently reproduces every finite count
in this chain and validates the resulting algebra exactly.