# Phase 5A Candidate-by-Criterion Evidence Matrix

## Status

STATUS: PHASE5A_CANDIDATE_CRITERION_MATRIX_COMPLETE

## Chronology

Phase 5A interpretation protocol:

    084d070

Candidate-neutral literature checkpoint:

    2852c4b

Completed algebraic audit:

    0c27dae

## Literal initiating datum

\[
g(v_1,v_2,v_3).
\]

D1 status:

    NOT_ASSESSABLE

No independently frozen contemporaneous context beyond D0 is used in this matrix.

## Reading rule

The assessment column describes whether the mathematical candidate satisfies the frozen criterion.

The chronology and discrimination columns separately record whether that property was actually present in the initiating evidence or arose from later mathematics/prior art.

## C0 — Generic ternary function

| Criterion | Assessment | Chronology | Discrimination | Confidence | Evidence / caveat |
|---|---|---|---|---|---|
| K1 — Arity match | SUPPORTS | D0 | GENERIC | HIGH | By definition C0 is a generic function with three argument slots, matching the literal form g(v1,v2,v3). Three-argument arity is extremely common and has essentially no power to select an exceptional-Lie-theoretic structure. |
| K2 — Vector-like domain match | NEUTRAL | D0 | GENERIC | HIGH | The labels v1,v2,v3 are compatible with vector arguments, but a generic ternary function has no intrinsic vector domain. The symbol v is suggestive but does not define a vector space or distinguish C0 from structured vector-valued candidates. |
| K3 — Canonicality | COUNTS_AGAINST | D0 | DISCRIMINATING | HIGH | A generic user-defined ternary function is not canonically determined by a standard mathematical structure. Particular generic functions can of course be chosen, but canonicality is not intrinsic to C0. |
| K4 — Invariance | COUNTS_AGAINST | D0 | DISCRIMINATING | HIGH | No nontrivial symmetry or invariance is intrinsic to an unspecified generic ternary function. A specially chosen function might be invariant, but that would add structure beyond C0. |
| K5 — Geometric content | COUNTS_AGAINST | D0 | DISCRIMINATING | HIGH | C0 does not intrinsically encode geometry; it is the baseline arbitrary-function interpretation. Geometric meaning would have to be supplied by an additional definition. |
| K6 — Metric relation | COUNTS_AGAINST | D0 | DISCRIMINATING | HIGH | No bilinear metric or invariant bilinear form is intrinsic to a generic ternary function. A metric relation could be imposed, but would no longer be information supplied by C0 itself. |
| K7 — Direct E8 relevance | COUNTS_AGAINST | D0 | DISCRIMINATING | HIGH | C0 has no intrinsic association with E8. The literal notation contains no explicit E8 identifier. |

## C1 — E8 Cartan 3-form

| Criterion | Assessment | Chronology | Discrimination | Confidence | Evidence / caveat |
|---|---|---|---|---|---|
| K1 — Arity match | SUPPORTS | D0+D3 | GENERIC | HIGH | The Cartan 3-form intrinsically evaluates three Lie-algebra arguments, matching the three argument slots in D0. Arity alone does not distinguish C1 from C2, C3, C4, or many other ternary structures. |
| K2 — Vector-like domain match | SUPPORTS | D0+D3 | GENERIC | HIGH | Its arguments are naturally elements of the vector space underlying the Lie algebra e8. The v-labels are compatible with this interpretation but also with C2-C4. |
| K3 — Canonicality | SUPPORTS | D3+D2 | GENERIC | HIGH | For a simple Lie algebra the Cartan 3-form B(X,[Y,Z]) is natural up to the scale of the invariant bilinear form; the project froze and validated a normalization B0. Canonicality is strong mathematical structure, but was not specified by D0. |
| K4 — Invariance | SUPPORTS | D3+D2 | GENERIC | HIGH | The Cartan 3-form is invariant under the relevant Lie-algebra automorphism/adjoint symmetry, and the reconstructed form was validated through exact invariant-form identities. Invariance is not unique to E8 and was not encoded in D0. |
| K5 — Geometric content | SUPPORTS | D3+D2 | GENERIC | HIGH | The Cartan 3-form encodes the Lie bracket together with an invariant bilinear geometry and is an established geometric structure associated with simple Lie algebras. This is genuine geometric content but is postulated only after choosing the C1 mathematical setting. |
| K6 — Metric relation | SUPPORTS | D3+D2 | GENERIC | HIGH | The relation is direct by definition: Omega(X,Y,Z)=B(X,[Y,Z]). This is a particularly clean K6 match, but D0 does not mention a metric, bracket, or bilinear form. |
| K7 — Direct E8 relevance | SUPPORTS | D3+D2 | DISCRIMINATING | HIGH | Once the Lie algebra is specified as e8, the form is directly defined on e8; the project further reproduced its E8 root-space support exactly from the independently constructed root system. The Cartan-3-form construction as a class is not E8-exclusive. The E8 specificity comes from choosing e8 and its root system, neither of which is explicitly contained in D0. |

## C2 — G2 invariant alternating 3-form

| Criterion | Assessment | Chronology | Discrimination | Confidence | Evidence / caveat |
|---|---|---|---|---|---|
| K1 — Arity match | SUPPORTS | D0+D3 | GENERIC | HIGH | The distinguished G2 form is intrinsically a 3-form and therefore takes three arguments. Arity does not discriminate C2 from C1, C3, or C4. |
| K2 — Vector-like domain match | SUPPORTS | D0+D3 | GENERIC | HIGH | Its arguments are naturally vectors in a seven-dimensional vector space. The v-labels are compatible but do not specify dimension seven. |
| K3 — Canonicality | SUPPORTS | D3 | GENERIC | HIGH | Once a G2 structure is specified, its defining positive 3-form is natural and canonical up to the usual equivalence. D0 does not contain a G2 identifier or a seven-dimensional constraint. |
| K4 — Invariance | SUPPORTS | D3 | DISCRIMINATING | HIGH | The stabilizer of the standard positive 3-form in GL(7,R) is G2. This is an exceptionally direct group/3-form relation, but no such stabilizer information appears in D0. |
| K5 — Geometric content | SUPPORTS | D3 | DISCRIMINATING | HIGH | The positive G2 3-form determines geometric data including a metric, orientation/volume form, and cross-product structure. This is strong geometric content but was not predicted by D0. |
| K6 — Metric relation | SUPPORTS | D3 | DISCRIMINATING | HIGH | The form has a direct metric relation, for example phi(a,b,c)=<a x b,c>, and a positive G2 3-form itself determines the associated metric. K6 therefore does not uniquely favor C1. |
| K7 — Direct E8 relevance | COUNTS_AGAINST | D3 | DISCRIMINATING | HIGH | The defining association is with G2, not E8. No direct E8 structure is intrinsic to the C2 candidate. |

## C3 — E6 cubic / symmetric trilinear form

| Criterion | Assessment | Chronology | Discrimination | Confidence | Evidence / caveat |
|---|---|---|---|---|---|
| K1 — Arity match | SUPPORTS | D0+D3 | GENERIC | HIGH | Polarization of the E6 cubic invariant gives an intrinsic three-argument symmetric trilinear form. D0 gives no symmetry information capable of distinguishing symmetric C3 from alternating C1/C2/C4. |
| K2 — Vector-like domain match | SUPPORTS | D0+D3 | GENERIC | HIGH | Its arguments are naturally vectors in the 27-dimensional E6 representation. D0 supplies no dimension 27 or E6 identifier. |
| K3 — Canonicality | SUPPORTS | D3 | GENERIC | HIGH | The cubic invariant and its polarization are natural invariant structures on the relevant E6 representation, up to scale. Canonicality does not by itself select C3 from C1 or C2. |
| K4 — Invariance | SUPPORTS | D3 | DISCRIMINATING | HIGH | The cubic/symmetric trilinear form is preserved by the E6 action. The symmetry group is E6 rather than E8, and D0 specifies neither. |
| K5 — Geometric content | SUPPORTS | D3 | GENERIC | MEDIUM | The cubic norm is a non-arbitrary exceptional algebraic and geometric structure, for example in the exceptional Jordan algebra realization. Its geometric content is principally cubic/algebraic rather than the direct metric geometry present in C1, C2, or C4. |
| K6 — Metric relation | COUNTS_AGAINST | D3 | DISCRIMINATING | HIGH | The defining E6 cubic is not naturally of the form B(x,operation(y,z)) for an E6-invariant bilinear metric on the 27-dimensional representation. Auxiliary bilinear identifications exist in Jordan models, but E6 does not preserve the relevant pairing in the same direct sense as C1 or C2. |
| K7 — Direct E8 relevance | COUNTS_AGAINST | D3 | DISCRIMINATING | HIGH | The defining exceptional-group association is E6, not E8. No intrinsic E8 association is supplied by C3. |

## C4 — Scalar triple product on oriented Euclidean R3

| Criterion | Assessment | Chronology | Discrimination | Confidence | Evidence / caveat |
|---|---|---|---|---|---|
| K1 — Arity match | SUPPORTS | D0+D3 | GENERIC | HIGH | The scalar triple product tau(u,v,w)=u dot (v cross w) intrinsically takes three arguments. This demonstrates that K1 is far from exceptional-Lie-specific. |
| K2 — Vector-like domain match | SUPPORTS | D0+D3 | GENERIC | HIGH | Its arguments are ordinary vectors in oriented Euclidean R3. The v-labels fit C4 at least as naturally as they fit C1-C3. |
| K3 — Canonicality | SUPPORTS | D3 | GENERIC | HIGH | Once Euclidean metric and orientation are fixed, the associated volume 3-form is canonical. Canonical ternary vector forms therefore occur outside exceptional Lie theory. |
| K4 — Invariance | SUPPORTS | D3 | GENERIC | HIGH | The scalar triple product is preserved by SO(3), the orientation-preserving orthogonal group. It changes sign under orientation reversal, so full O(3) scalar invariance is not claimed. |
| K5 — Geometric content | SUPPORTS | D3 | DISCRIMINATING | HIGH | It measures oriented Euclidean volume and therefore directly encodes geometry. This is a strong geometric K5 match with no exceptional-group assumption. |
| K6 — Metric relation | SUPPORTS | D3 | DISCRIMINATING | HIGH | It is directly related to the Euclidean bilinear metric through the dot product in u dot (v cross w). Therefore even a strong K6 match does not uniquely indicate C1. |
| K7 — Direct E8 relevance | COUNTS_AGAINST | D3 | DISCRIMINATING | HIGH | The scalar triple product has no intrinsic E8 association. Its purpose here is specifically to control against inferring E8 from generic ternary geometric properties. |

## Unweighted structural summary

These are counts of qualitative labels only. They are NOT scores, weights, probabilities, or a candidate ranking.

| Candidate | SUPPORTS | NEUTRAL | COUNTS_AGAINST | NOT_ASSESSABLE |
|---|---:|---:|---:|---:|
| C0 | 1 | 1 | 5 | 0 |
| C1 | 7 | 0 | 0 | 0 |
| C2 | 6 | 0 | 1 | 0 |
| C3 | 5 | 0 | 2 | 0 |
| C4 | 6 | 0 | 1 | 0 |

## D0 discrimination check

The literal datum supplies only three argument slots and vector-like labels.

Those features are compatible with C1, C2, C3, and C4, and are also compatible with the generic C0 baseline.

D0 supplies no explicit evidence for canonicality, invariance, geometry, metric relation, dimension, symmetry type, exceptional group, root system, or E8.

Therefore the strong structural properties appearing in K3-K7 must not be counted as predictions made by D0.

## Key comparison

Structurally:

- C1 satisfies all seven frozen criteria.
- C2 satisfies K1-K6 but not K7.
- C3 satisfies K1-K5 but not K6 or K7.
- C4 satisfies K1-K6 but not K7.
- C0 matches the literal three-argument form but carries little additional mathematical structure.

This shows that K1-K6 do not uniquely identify C1. K7 is the criterion that makes C1 E8-specific, but D0 contains no explicit E8 information.

## C1 viability versus C1 selection

The completed Phase 1-4 work establishes C1 as MATHEMATICALLY REALIZED AND INTERNALLY VALIDATED.

It does not establish that the literal initiating notation selected C1 uniquely over the competing ternary structures.

## Interpretation status

CANDIDATE_RANKING_PERFORMED: NO

INTERPRETATION_CLASS_SELECTED: NO

The next step is to map this completed matrix to the frozen I0-I3 interpretation classes without changing their definitions.
