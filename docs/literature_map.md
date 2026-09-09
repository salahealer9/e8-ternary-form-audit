# Literature Map

## Status

STATUS: PHASE0_LITERATURE_MAP_FROZEN

This file records external mathematical sources consulted before implementation.

External numerical values recorded here are validation targets only and must not
be used as algorithmic stopping conditions.

---

## L1 — E8 root realization and inner-product counts

Rosa Winter and Ronald van Luijk,
"The Action of the Weyl Group on the E8 Root System",
Graphs and Combinatorics 37 (2021), 1965–2064.

DOI:

    10.1007/s00373-021-02315-8

Relevant results:

- the E8 roots are represented by two coordinate families;
- 128 roots have coordinates
  \[
  (\pm 1/2,\ldots,\pm 1/2)
  \]
  with the required parity condition;
- 112 roots have exactly two nonzero coordinates, each equal to \(\pm1\);
- therefore
  \[
  128+112=240;
  \]
- all roots have squared norm 2 in this normalization;
- for every root \(e\), exactly 56 roots \(f\) satisfy
  \[
  e\cdot f=1;
  \]
- exactly 56 satisfy
  \[
  e\cdot f=-1;
  \]
- exactly 126 roots are orthogonal to \(e\).

Role in this repository:

PRIMARY_EXTERNAL_ROOT_BENCHMARK.

The coordinate description may motivate an implementation because it is a
standard definition of the root realization. Numerical counts derived from it
must nevertheless emerge from the code rather than being inserted as expected
loop sizes.

---

## L2 — Number of A2 subsystems

Andrew J. Bordner, Nicholas S. Manton and Ryu Sasaki,
"Calogero-Moser Models. V: Supersymmetry and Quantum Lax Pair",
Progress of Theoretical Physics 103 (2000), 463–487.

DOI:

    10.1143/PTP.103.463

The paper lists the numbers of two-dimensional root systems contained in
exceptional root systems and gives

\[
E_6:120\times A_2,
\]

\[
E_7:336\times A_2,
\]

\[
E_8:1120\times A_2.
\]

Role in this repository:

PRIMARY_EXTERNAL_A2_COUNT_BENCHMARK.

The value 1120 must not be used as an enumeration stopping condition.

---

## L3 — Independent modern derivation of the A2 count

Christian Böhning, Hans-Christian Graf von Bothmer and Lisa Marquand,
"Counting Fourier-Mukai partners of cubic fourfolds".

DOI:

    10.1016/j.aim.2026.111218

A lemma in this work derives the number of A2 root subsystems of E8 using:

- 240 roots;
- 56 roots at inner product -1 from a fixed root;
- 12 ordered qualifying root pairs per A2 subsystem.

Thus

\[
\frac{240\cdot56}{12}=1120.
\]

Role:

SECONDARY_INDEPENDENT_A2_BENCHMARK.

This derivation is recorded before computation but will not be used to drive
the enumeration.

---

## L4 — Cartan 3-form

For a simple Lie algebra \(\mathfrak g\) with invariant scalar product \(B\),
the Cartan 3-form is conventionally written

\[
\eta(X,Y,Z)=B(X,[Y,Z]).
\]

This is an established invariant alternating trilinear form.

A useful published reference is:

"Geometric structures associated with a simple Cartan 3-form",
Journal of Geometry and Physics 70 (2013), 205–223.

DOI:

    10.1016/j.geomphys.2013.03.028

Role:

PRIMARY_CANDIDATE_C1_PROVENANCE.

The existence of the Cartan 3-form is established mathematics and is not a
result of this repository.

The repository will instead test how its root-space support relates to the
finite E8 zero-sum root-triple structure.

---

## Frozen benchmark table

| Benchmark | Frozen value | Primary provenance |
|---|---:|---|
| E8 root count | 240 | L1 |
| root squared norm | 2 | L1 |
| neighbours with inner product -1 | 56 per root | L1 |
| A2 subsystems | 1120 | L2 |
| independent A2 derivation | 1120 | L3 |

## Provenance policy

A result matching a frozen benchmark is a replication result.

It must not be described as a new discovery.

Any mathematical structure encountered later that was not listed in the Phase
0 candidate set must be explicitly marked POST_HOC_CANDIDATE.
