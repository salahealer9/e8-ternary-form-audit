# Phase 3B Post-Closeout Signed-Structure Prior Art

## Status

STATUS: POST_PHASE3B_PRE_PHASE3C_LITERATURE_DISCOVERY

## Chronology

This literature checkpoint was made after completion of the basis-independent
Cartan 3-form support architecture and before freezing any Cartan basis,
Chevalley basis, root-vector sign convention, or numerical coefficient
protocol.

## Material prior art

Modern work gives canonical or explicitly controlled choices of Chevalley
basis and structure constants for simple Lie algebras.

### Geck and Lang

Meinolf Geck and Alexander Lang,

"Canonical structure constants for simple Lie algebras"

arXiv:

    2404.07652

The work constructs a canonical Chevalley basis using Lusztig's theory of
canonical bases.

The resulting basis is unique up to a global sign, and explicit formulae are
given for the corresponding structure constants.

This includes the simply-laced case and is therefore directly relevant to E8.

### Geck

Meinolf Geck,

"On Lusztig's canonical bases of simple Lie algebras"

arXiv:

    2602.19632

For simply-laced root systems, the work discusses a construction using a
multiplicative 2-cocycle

\[
\varepsilon:
\mathbb Z\Phi\times\mathbb Z\Phi
\to
\{\pm1\}.
\]

Such a cocycle determines explicit root-vector structure constants, and an
appropriate choice yields Lusztig's canonical basis.

## Consequence for this repository

The following must not be treated as novel:

- existence of Chevalley bases for E8;
- integer root-space structure constants;
- explicit sign systems for simply-laced Lie algebras;
- cocycle constructions producing those signs;
- canonical Chevalley-basis normalizations available in the literature.

## Methodological consequence

Phase 3C must not introduce an arbitrary root-vector sign convention merely
because it reproduces antisymmetry or Jacobi identities.

Instead, the next protocol should select a documented canonical convention
or define explicitly how the repository's convention is related to one.

## Effect on previous phases

PHASE0_MODIFIED: NO
PHASE1_MODIFIED: NO
PHASE2_MODIFIED: NO
PHASE3A_MODIFIED: NO
PHASE3B_MODIFIED: NO

The prior-art discovery affects only the design and novelty interpretation of
future signed-coefficient phases.

## Remaining research question

The repository may still investigate how the already established unsigned
ternary E8 incidence structure lifts, under a documented canonical basis, to
the signed Cartan 3-form coefficients.

That lift must be treated as a reconstruction/representation problem unless a
separately verified novel result emerges.
