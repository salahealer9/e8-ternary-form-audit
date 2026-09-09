# Phase 0 Closeout

## Status

STATUS: PHASE0_FROZEN

Phase 0 was completed before implementation of the E8 root enumeration.

## Initiating datum

The sole initiating observation is

\[
g(v_1,v_2,v_3).
\]

No mathematical interpretation is assigned to this notation by the
observation itself.

## Frozen candidate classes

- C0 — generic three-argument function;
- C1 — Cartan 3-form on \(\mathfrak e_8\);
- C2 — \(G_2\) invariant alternating 3-form;
- C3 — \(E_6\) cubic / symmetric trilinear structure;
- C4 — other established ternary structures with explicit provenance.

## Frozen primary branch

\[
E_8\text{ roots}
\rightarrow
\text{pairwise inner products}
\rightarrow
\alpha+\beta+\gamma=0
\rightarrow
A_2\text{ subsystems}
\rightarrow
\text{ternary incidence structure}.
\]

The Lie-algebraic Cartan 3-form will be investigated only after the finite
root-level structure has been independently reproduced.

## Frozen external replication targets

The following values are external validation targets and must not control the
enumeration:

\[
|\Phi(E_8)|=240,
\]

\[
\alpha^2=2,
\]

\[
N_{\alpha\cdot\beta=-1}=56
\]

for each fixed root, and

\[
N_{A_2}=1120.
\]

## Independence safeguards

The Phase 1 implementation must not:

- stop after finding 240 roots;
- construct roots from an external 240-row table;
- stop after finding 56 neighbours;
- stop after finding 1120 A2 subsystems;
- insert zero-sum triples from external data;
- alter the Phase 0 candidate criteria after seeing computational results.

## Interpretation safeguard

A correspondence between the initiating notation and an established
mathematical structure does not establish the causal origin of the dream.

Any claim beyond the mathematics investigated in this repository requires
independent evidence.

## Phase 0 test state

The repository smoke-test suite passed before Phase 1 implementation:

    3 passed

The smoke test explicitly verified that no

    src/e8_ternary/roots.py

module existed at Phase 0 closeout.

## Next phase

Phase 1A will independently construct the standard coordinate realization of
the E8 root system and derive its basic invariants without using frozen
benchmark counts as algorithmic controls.
