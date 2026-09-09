# Phase 1A E8 Root Construction Closeout

## Status

STATUS: PHASE1A_ROOT_CONSTRUCTION_PASS

## Frozen protocol

Phase 1A execution protocol was frozen at commit:

    39bb86d

No Phase 2 zero-sum triple or A2 enumeration was performed before this
closeout.

## Construction

The E8 root system was generated independently from the two standard
coordinate families using exact doubled-coordinate integer representation

\[
q=2\alpha\in\mathbb Z^8.
\]

No precomputed root table was loaded.

No external benchmark count was used as an algorithmic stopping condition.

## Generated family counts

Integer-coordinate family:

\[
|F_1|=112.
\]

Half-integer-coordinate family:

\[
|F_2|=128.
\]

Combined unique roots:

\[
|\Phi_{\mathrm{generated}}|=240.
\]

Duplicate counts:

    F1: 0
    F2: 0

## Root norms

The doubled-coordinate squared-norm spectrum was

\[
q\cdot q=8
\]

for all 240 roots.

Since

\[
q=2\alpha,
\]

this gives

\[
\alpha\cdot\alpha=2
\]

for every generated root.

## Negation closure

Every root has its exact negative in the generated root set.

Result:

    NEGATIVE_CLOSURE: TRUE

## Ordered distinct-pair inner-product spectrum

In doubled coordinates the observed spectrum was:

| \(q_\alpha\cdot q_\beta\) | count |
|---:|---:|
| -8 | 240 |
| -4 | 13440 |
| 0 | 30240 |
| 4 | 13440 |

Dividing doubled dot products by four gives the ordinary E8 inner products:

| \(\alpha\cdot\beta\) | ordered-pair count | count per root |
|---:|---:|---:|
| -2 | 240 | 1 |
| -1 | 13440 | 56 |
| 0 | 30240 | 126 |
| 1 | 13440 | 56 |

The ordered distinct-pair total is

\[
240+13440+30240+13440=57360,
\]

which agrees with

\[
240(240-1)=57360.
\]

Thus every distinct ordered root pair is accounted for.

## Frozen benchmark comparison

| Quantity | Frozen benchmark | Observed | Result |
|---|---:|---:|---|
| E8 roots | 240 | 240 | PASS |
| squared root norm | 2 | 2 | PASS |
| roots at inner product -1 per root | 56 | 56 | PASS |

The additional observed per-root counts are:

\[
N_{-2}=1,\qquad
N_0=126,\qquad
N_{+1}=56.
\]

## Test state

The full repository test suite after Phase 1A implementation reported:

    10 passed

## Phase 1A conclusion

PHASE1A_REPLICATION: PASS

The independently generated coordinate system reproduces the standard E8 root
system benchmarks and the complete distinct-root inner-product distribution.

No benchmark repair, truncation, augmentation, or approximate deduplication
was required.

## Next phase

Phase 1B will freeze and execute an independent structural validation of the
generated root set before Phase 2 begins zero-sum triple and A2-subsystem
enumeration.
