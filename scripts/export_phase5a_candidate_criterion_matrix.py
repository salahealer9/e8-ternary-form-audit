#!/usr/bin/env python3
"""Export the frozen Phase 5A C0-C4 x K1-K7 evidence matrix.

This script performs no numerical weighting and selects no I0-I3
interpretation class.

The 35 assessments are qualitative and use only the vocabulary frozen in the
Phase 5A protocol:

    SUPPORTS
    NEUTRAL
    COUNTS_AGAINST
    NOT_ASSESSABLE
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


JSON_OUTPUT = Path(
    "data/reference/"
    "phase5a_candidate_criterion_matrix.json"
)

MD_OUTPUT = Path(
    "docs/checkpoints/"
    "phase5a_candidate_criterion_matrix.md"
)


CRITERIA = {
    "K1": {
        "name": "Arity match",
        "definition": (
            "Does the object intrinsically take three arguments?"
        ),
    },
    "K2": {
        "name": "Vector-like domain match",
        "definition": (
            "Are its arguments naturally vectors, tangent vectors, "
            "representation vectors, or Lie-algebra elements?"
        ),
    },
    "K3": {
        "name": "Canonicality",
        "definition": (
            "Is the object canonically or naturally defined once the "
            "relevant mathematical structure is specified?"
        ),
    },
    "K4": {
        "name": "Invariance",
        "definition": (
            "Is the ternary object preserved by a nontrivial symmetry group?"
        ),
    },
    "K5": {
        "name": "Geometric content",
        "definition": (
            "Does it encode geometry rather than being an arbitrary "
            "user-defined function?"
        ),
    },
    "K6": {
        "name": "Metric relation",
        "definition": (
            "Is there a precise relation to an ordinary bilinear metric or "
            "invariant bilinear form?"
        ),
    },
    "K7": {
        "name": "Direct E8 relevance",
        "definition": (
            "Is the object intrinsically associated with E8 rather than "
            "connected through a discretionary chain of analogies?"
        ),
    },
}


CANDIDATES = {
    "C0": "Generic ternary function",
    "C1": "E8 Cartan 3-form",
    "C2": "G2 invariant alternating 3-form",
    "C3": "E6 cubic / symmetric trilinear form",
    "C4": "Scalar triple product on oriented Euclidean R3",
}


ALLOWED_ASSESSMENTS = {
    "SUPPORTS",
    "NEUTRAL",
    "COUNTS_AGAINST",
    "NOT_ASSESSABLE",
}

ALLOWED_DISCRIMINATION = {
    "GENERIC",
    "DISCRIMINATING",
}

ALLOWED_CONFIDENCE = {
    "HIGH",
    "MEDIUM",
    "LOW",
}


def cell(
    candidate: str,
    criterion: str,
    assessment: str,
    chronology: list[str],
    evidence: str,
    discrimination: str,
    confidence: str,
    caveat: str,
) -> dict:
    return {
        "candidate": candidate,
        "criterion": criterion,
        "assessment": assessment,
        "chronology": chronology,
        "evidence": evidence,
        "discrimination": discrimination,
        "confidence": confidence,
        "caveat": caveat,
    }


CELLS = [
    # ===============================================================
    # C0 — Generic ternary function
    # ===============================================================
    cell(
        "C0",
        "K1",
        "SUPPORTS",
        ["D0"],
        (
            "By definition C0 is a generic function with three argument "
            "slots, matching the literal form g(v1,v2,v3)."
        ),
        "GENERIC",
        "HIGH",
        (
            "Three-argument arity is extremely common and has essentially "
            "no power to select an exceptional-Lie-theoretic structure."
        ),
    ),
    cell(
        "C0",
        "K2",
        "NEUTRAL",
        ["D0"],
        (
            "The labels v1,v2,v3 are compatible with vector arguments, but "
            "a generic ternary function has no intrinsic vector domain."
        ),
        "GENERIC",
        "HIGH",
        (
            "The symbol v is suggestive but does not define a vector space "
            "or distinguish C0 from structured vector-valued candidates."
        ),
    ),
    cell(
        "C0",
        "K3",
        "COUNTS_AGAINST",
        ["D0"],
        (
            "A generic user-defined ternary function is not canonically "
            "determined by a standard mathematical structure."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "Particular generic functions can of course be chosen, but "
            "canonicality is not intrinsic to C0."
        ),
    ),
    cell(
        "C0",
        "K4",
        "COUNTS_AGAINST",
        ["D0"],
        (
            "No nontrivial symmetry or invariance is intrinsic to an "
            "unspecified generic ternary function."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "A specially chosen function might be invariant, but that would "
            "add structure beyond C0."
        ),
    ),
    cell(
        "C0",
        "K5",
        "COUNTS_AGAINST",
        ["D0"],
        (
            "C0 does not intrinsically encode geometry; it is the baseline "
            "arbitrary-function interpretation."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "Geometric meaning would have to be supplied by an additional "
            "definition."
        ),
    ),
    cell(
        "C0",
        "K6",
        "COUNTS_AGAINST",
        ["D0"],
        (
            "No bilinear metric or invariant bilinear form is intrinsic to "
            "a generic ternary function."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "A metric relation could be imposed, but would no longer be "
            "information supplied by C0 itself."
        ),
    ),
    cell(
        "C0",
        "K7",
        "COUNTS_AGAINST",
        ["D0"],
        (
            "C0 has no intrinsic association with E8."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "The literal notation contains no explicit E8 identifier."
        ),
    ),

    # ===============================================================
    # C1 — E8 Cartan 3-form
    # ===============================================================
    cell(
        "C1",
        "K1",
        "SUPPORTS",
        ["D0", "D3"],
        (
            "The Cartan 3-form intrinsically evaluates three Lie-algebra "
            "arguments, matching the three argument slots in D0."
        ),
        "GENERIC",
        "HIGH",
        (
            "Arity alone does not distinguish C1 from C2, C3, C4, or many "
            "other ternary structures."
        ),
    ),
    cell(
        "C1",
        "K2",
        "SUPPORTS",
        ["D0", "D3"],
        (
            "Its arguments are naturally elements of the vector space "
            "underlying the Lie algebra e8."
        ),
        "GENERIC",
        "HIGH",
        (
            "The v-labels are compatible with this interpretation but also "
            "with C2-C4."
        ),
    ),
    cell(
        "C1",
        "K3",
        "SUPPORTS",
        ["D3", "D2"],
        (
            "For a simple Lie algebra the Cartan 3-form B(X,[Y,Z]) is "
            "natural up to the scale of the invariant bilinear form; the "
            "project froze and validated a normalization B0."
        ),
        "GENERIC",
        "HIGH",
        (
            "Canonicality is strong mathematical structure, but was not "
            "specified by D0."
        ),
    ),
    cell(
        "C1",
        "K4",
        "SUPPORTS",
        ["D3", "D2"],
        (
            "The Cartan 3-form is invariant under the relevant Lie-algebra "
            "automorphism/adjoint symmetry, and the reconstructed form was "
            "validated through exact invariant-form identities."
        ),
        "GENERIC",
        "HIGH",
        (
            "Invariance is not unique to E8 and was not encoded in D0."
        ),
    ),
    cell(
        "C1",
        "K5",
        "SUPPORTS",
        ["D3", "D2"],
        (
            "The Cartan 3-form encodes the Lie bracket together with an "
            "invariant bilinear geometry and is an established geometric "
            "structure associated with simple Lie algebras."
        ),
        "GENERIC",
        "HIGH",
        (
            "This is genuine geometric content but is postulated only after "
            "choosing the C1 mathematical setting."
        ),
    ),
    cell(
        "C1",
        "K6",
        "SUPPORTS",
        ["D3", "D2"],
        (
            "The relation is direct by definition: "
            "Omega(X,Y,Z)=B(X,[Y,Z])."
        ),
        "GENERIC",
        "HIGH",
        (
            "This is a particularly clean K6 match, but D0 does not mention "
            "a metric, bracket, or bilinear form."
        ),
    ),
    cell(
        "C1",
        "K7",
        "SUPPORTS",
        ["D3", "D2"],
        (
            "Once the Lie algebra is specified as e8, the form is directly "
            "defined on e8; the project further reproduced its E8 root-space "
            "support exactly from the independently constructed root system."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "The Cartan-3-form construction as a class is not E8-exclusive. "
            "The E8 specificity comes from choosing e8 and its root system, "
            "neither of which is explicitly contained in D0."
        ),
    ),

    # ===============================================================
    # C2 — G2 invariant alternating 3-form
    # ===============================================================
    cell(
        "C2",
        "K1",
        "SUPPORTS",
        ["D0", "D3"],
        (
            "The distinguished G2 form is intrinsically a 3-form and "
            "therefore takes three arguments."
        ),
        "GENERIC",
        "HIGH",
        (
            "Arity does not discriminate C2 from C1, C3, or C4."
        ),
    ),
    cell(
        "C2",
        "K2",
        "SUPPORTS",
        ["D0", "D3"],
        (
            "Its arguments are naturally vectors in a seven-dimensional "
            "vector space."
        ),
        "GENERIC",
        "HIGH",
        (
            "The v-labels are compatible but do not specify dimension seven."
        ),
    ),
    cell(
        "C2",
        "K3",
        "SUPPORTS",
        ["D3"],
        (
            "Once a G2 structure is specified, its defining positive "
            "3-form is natural and canonical up to the usual equivalence."
        ),
        "GENERIC",
        "HIGH",
        (
            "D0 does not contain a G2 identifier or a seven-dimensional "
            "constraint."
        ),
    ),
    cell(
        "C2",
        "K4",
        "SUPPORTS",
        ["D3"],
        (
            "The stabilizer of the standard positive 3-form in GL(7,R) is "
            "G2."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "This is an exceptionally direct group/3-form relation, but no "
            "such stabilizer information appears in D0."
        ),
    ),
    cell(
        "C2",
        "K5",
        "SUPPORTS",
        ["D3"],
        (
            "The positive G2 3-form determines geometric data including a "
            "metric, orientation/volume form, and cross-product structure."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "This is strong geometric content but was not predicted by D0."
        ),
    ),
    cell(
        "C2",
        "K6",
        "SUPPORTS",
        ["D3"],
        (
            "The form has a direct metric relation, for example "
            "phi(a,b,c)=<a x b,c>, and a positive G2 3-form itself "
            "determines the associated metric."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "K6 therefore does not uniquely favor C1."
        ),
    ),
    cell(
        "C2",
        "K7",
        "COUNTS_AGAINST",
        ["D3"],
        (
            "The defining association is with G2, not E8."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "No direct E8 structure is intrinsic to the C2 candidate."
        ),
    ),

    # ===============================================================
    # C3 — E6 cubic / symmetric trilinear form
    # ===============================================================
    cell(
        "C3",
        "K1",
        "SUPPORTS",
        ["D0", "D3"],
        (
            "Polarization of the E6 cubic invariant gives an intrinsic "
            "three-argument symmetric trilinear form."
        ),
        "GENERIC",
        "HIGH",
        (
            "D0 gives no symmetry information capable of distinguishing "
            "symmetric C3 from alternating C1/C2/C4."
        ),
    ),
    cell(
        "C3",
        "K2",
        "SUPPORTS",
        ["D0", "D3"],
        (
            "Its arguments are naturally vectors in the 27-dimensional "
            "E6 representation."
        ),
        "GENERIC",
        "HIGH",
        (
            "D0 supplies no dimension 27 or E6 identifier."
        ),
    ),
    cell(
        "C3",
        "K3",
        "SUPPORTS",
        ["D3"],
        (
            "The cubic invariant and its polarization are natural invariant "
            "structures on the relevant E6 representation, up to scale."
        ),
        "GENERIC",
        "HIGH",
        (
            "Canonicality does not by itself select C3 from C1 or C2."
        ),
    ),
    cell(
        "C3",
        "K4",
        "SUPPORTS",
        ["D3"],
        (
            "The cubic/symmetric trilinear form is preserved by the E6 "
            "action."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "The symmetry group is E6 rather than E8, and D0 specifies "
            "neither."
        ),
    ),
    cell(
        "C3",
        "K5",
        "SUPPORTS",
        ["D3"],
        (
            "The cubic norm is a non-arbitrary exceptional algebraic and "
            "geometric structure, for example in the exceptional Jordan "
            "algebra realization."
        ),
        "GENERIC",
        "MEDIUM",
        (
            "Its geometric content is principally cubic/algebraic rather "
            "than the direct metric geometry present in C1, C2, or C4."
        ),
    ),
    cell(
        "C3",
        "K6",
        "COUNTS_AGAINST",
        ["D3"],
        (
            "The defining E6 cubic is not naturally of the form "
            "B(x,operation(y,z)) for an E6-invariant bilinear metric on the "
            "27-dimensional representation."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "Auxiliary bilinear identifications exist in Jordan models, but "
            "E6 does not preserve the relevant pairing in the same direct "
            "sense as C1 or C2."
        ),
    ),
    cell(
        "C3",
        "K7",
        "COUNTS_AGAINST",
        ["D3"],
        (
            "The defining exceptional-group association is E6, not E8."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "No intrinsic E8 association is supplied by C3."
        ),
    ),

    # ===============================================================
    # C4 — scalar triple product
    # ===============================================================
    cell(
        "C4",
        "K1",
        "SUPPORTS",
        ["D0", "D3"],
        (
            "The scalar triple product tau(u,v,w)=u dot (v cross w) "
            "intrinsically takes three arguments."
        ),
        "GENERIC",
        "HIGH",
        (
            "This demonstrates that K1 is far from exceptional-Lie-specific."
        ),
    ),
    cell(
        "C4",
        "K2",
        "SUPPORTS",
        ["D0", "D3"],
        (
            "Its arguments are ordinary vectors in oriented Euclidean R3."
        ),
        "GENERIC",
        "HIGH",
        (
            "The v-labels fit C4 at least as naturally as they fit C1-C3."
        ),
    ),
    cell(
        "C4",
        "K3",
        "SUPPORTS",
        ["D3"],
        (
            "Once Euclidean metric and orientation are fixed, the associated "
            "volume 3-form is canonical."
        ),
        "GENERIC",
        "HIGH",
        (
            "Canonical ternary vector forms therefore occur outside "
            "exceptional Lie theory."
        ),
    ),
    cell(
        "C4",
        "K4",
        "SUPPORTS",
        ["D3"],
        (
            "The scalar triple product is preserved by SO(3), the "
            "orientation-preserving orthogonal group."
        ),
        "GENERIC",
        "HIGH",
        (
            "It changes sign under orientation reversal, so full O(3) "
            "scalar invariance is not claimed."
        ),
    ),
    cell(
        "C4",
        "K5",
        "SUPPORTS",
        ["D3"],
        (
            "It measures oriented Euclidean volume and therefore directly "
            "encodes geometry."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "This is a strong geometric K5 match with no exceptional-group "
            "assumption."
        ),
    ),
    cell(
        "C4",
        "K6",
        "SUPPORTS",
        ["D3"],
        (
            "It is directly related to the Euclidean bilinear metric through "
            "the dot product in u dot (v cross w)."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "Therefore even a strong K6 match does not uniquely indicate C1."
        ),
    ),
    cell(
        "C4",
        "K7",
        "COUNTS_AGAINST",
        ["D3"],
        (
            "The scalar triple product has no intrinsic E8 association."
        ),
        "DISCRIMINATING",
        "HIGH",
        (
            "Its purpose here is specifically to control against inferring "
            "E8 from generic ternary geometric properties."
        ),
    ),
]


def validate() -> None:
    if set(CRITERIA) != {
        "K1", "K2", "K3", "K4", "K5", "K6", "K7"
    }:
        raise ValueError("Frozen criterion set changed")

    if set(CANDIDATES) != {
        "C0", "C1", "C2", "C3", "C4"
    }:
        raise ValueError("Frozen candidate set changed")

    if len(CELLS) != 35:
        raise ValueError(
            f"Expected 35 cells, observed {len(CELLS)}"
        )

    keys = [
        (
            item["candidate"],
            item["criterion"],
        )
        for item in CELLS
    ]

    if len(set(keys)) != 35:
        raise ValueError(
            "Candidate/criterion cells are duplicated"
        )

    expected = {
        (candidate, criterion)
        for candidate in CANDIDATES
        for criterion in CRITERIA
    }

    if set(keys) != expected:
        missing = sorted(
            expected - set(keys)
        )
        extra = sorted(
            set(keys) - expected
        )

        raise ValueError(
            f"Matrix coverage mismatch: "
            f"missing={missing}, extra={extra}"
        )

    for item in CELLS:
        if item["assessment"] not in ALLOWED_ASSESSMENTS:
            raise ValueError(
                f"Invalid assessment: {item}"
            )

        if item["discrimination"] not in ALLOWED_DISCRIMINATION:
            raise ValueError(
                f"Invalid discrimination: {item}"
            )

        if item["confidence"] not in ALLOWED_CONFIDENCE:
            raise ValueError(
                f"Invalid confidence: {item}"
            )

        if not item["chronology"]:
            raise ValueError(
                f"Missing chronology: {item}"
            )

        if any(
            value not in {"D0", "D1", "D2", "D3"}
            for value in item["chronology"]
        ):
            raise ValueError(
                f"Invalid chronology class: {item}"
            )


def assessment_summary() -> dict[str, dict[str, int]]:
    result = {}

    for candidate in CANDIDATES:
        counts = Counter(
            item["assessment"]
            for item in CELLS
            if item["candidate"] == candidate
        )

        result[candidate] = {
            label: counts[label]
            for label in (
                "SUPPORTS",
                "NEUTRAL",
                "COUNTS_AGAINST",
                "NOT_ASSESSABLE",
            )
        }

    return result


def d0_supported_criteria() -> dict[str, list[str]]:
    """Criteria for which the evidence cell includes literal D0 information.

    This does NOT mean D0 uniquely selects the candidate.
    """
    return {
        candidate: [
            item["criterion"]
            for item in CELLS
            if (
                item["candidate"] == candidate
                and "D0" in item["chronology"]
                and item["assessment"] in {
                    "SUPPORTS",
                    "NEUTRAL",
                }
            )
        ]
        for candidate in CANDIDATES
    }


def build_json_payload() -> dict:
    return {
        "schema": (
            "phase5a_candidate_criterion_matrix.v1"
        ),
        "status": (
            "PHASE5A_CANDIDATE_CRITERION_MATRIX_COMPLETE"
        ),
        "phase5a_protocol_commit": "084d070",
        "candidate_neutral_literature_commit": "2852c4b",
        "phase4a_complete_commit": "0c27dae",
        "d0_literal": "g(v1,v2,v3)",
        "d1_status": (
            "NOT_ASSESSABLE_NO_INDEPENDENTLY_FROZEN_"
            "CONTEMPORANEOUS_CONTEXT_USED"
        ),
        "criteria": CRITERIA,
        "candidates": CANDIDATES,
        "assessment_vocabulary": sorted(
            ALLOWED_ASSESSMENTS
        ),
        "cells": CELLS,
        "assessment_summary": assessment_summary(),
        "d0_compatible_criteria": d0_supported_criteria(),
        "numerical_weights_used": False,
        "candidate_ranking_performed": False,
        "interpretation_class_selected": False,
    }


def build_markdown(payload: dict) -> str:
    lines = [
        "# Phase 5A Candidate-by-Criterion Evidence Matrix",
        "",
        "## Status",
        "",
        "STATUS: PHASE5A_CANDIDATE_CRITERION_MATRIX_COMPLETE",
        "",
        "## Chronology",
        "",
        "Phase 5A interpretation protocol:",
        "",
        "    084d070",
        "",
        "Candidate-neutral literature checkpoint:",
        "",
        "    2852c4b",
        "",
        "Completed algebraic audit:",
        "",
        "    0c27dae",
        "",
        "## Literal initiating datum",
        "",
        r"\[",
        r"g(v_1,v_2,v_3).",
        r"\]",
        "",
        "D1 status:",
        "",
        "    NOT_ASSESSABLE",
        "",
        (
            "No independently frozen contemporaneous context beyond D0 is "
            "used in this matrix."
        ),
        "",
        "## Reading rule",
        "",
        (
            "The assessment column describes whether the mathematical "
            "candidate satisfies the frozen criterion."
        ),
        "",
        (
            "The chronology and discrimination columns separately record "
            "whether that property was actually present in the initiating "
            "evidence or arose from later mathematics/prior art."
        ),
        "",
    ]

    for candidate, candidate_name in CANDIDATES.items():
        lines.extend(
            [
                f"## {candidate} — {candidate_name}",
                "",
                "| Criterion | Assessment | Chronology | "
                "Discrimination | Confidence | Evidence / caveat |",
                "|---|---|---|---|---|---|",
            ]
        )

        for item in CELLS:
            if item["candidate"] != candidate:
                continue

            criterion = item["criterion"]
            evidence = (
                item["evidence"]
                + " "
                + item["caveat"]
            ).replace("|", r"\|")

            lines.append(
                "| "
                f"{criterion} — {CRITERIA[criterion]['name']} | "
                f"{item['assessment']} | "
                f"{'+'.join(item['chronology'])} | "
                f"{item['discrimination']} | "
                f"{item['confidence']} | "
                f"{evidence} |"
            )

        lines.append("")

    lines.extend(
        [
            "## Unweighted structural summary",
            "",
            (
                "These are counts of qualitative labels only. They are NOT "
                "scores, weights, probabilities, or a candidate ranking."
            ),
            "",
            "| Candidate | SUPPORTS | NEUTRAL | "
            "COUNTS_AGAINST | NOT_ASSESSABLE |",
            "|---|---:|---:|---:|---:|",
        ]
    )

    for candidate, counts in payload[
        "assessment_summary"
    ].items():
        lines.append(
            "| "
            f"{candidate} | "
            f"{counts['SUPPORTS']} | "
            f"{counts['NEUTRAL']} | "
            f"{counts['COUNTS_AGAINST']} | "
            f"{counts['NOT_ASSESSABLE']} |"
        )

    lines.extend(
        [
            "",
            "## D0 discrimination check",
            "",
            (
                "The literal datum supplies only three argument slots and "
                "vector-like labels."
            ),
            "",
            (
                "Those features are compatible with C1, C2, C3, and C4, "
                "and are also compatible with the generic C0 baseline."
            ),
            "",
            (
                "D0 supplies no explicit evidence for canonicality, "
                "invariance, geometry, metric relation, dimension, symmetry "
                "type, exceptional group, root system, or E8."
            ),
            "",
            (
                "Therefore the strong structural properties appearing in "
                "K3-K7 must not be counted as predictions made by D0."
            ),
            "",
            "## Key comparison",
            "",
            "Structurally:",
            "",
            "- C1 satisfies all seven frozen criteria.",
            "- C2 satisfies K1-K6 but not K7.",
            "- C3 satisfies K1-K5 but not K6 or K7.",
            "- C4 satisfies K1-K6 but not K7.",
            (
                "- C0 matches the literal three-argument form but carries "
                "little additional mathematical structure."
            ),
            "",
            (
                "This shows that K1-K6 do not uniquely identify C1. "
                "K7 is the criterion that makes C1 E8-specific, but D0 "
                "contains no explicit E8 information."
            ),
            "",
            "## C1 viability versus C1 selection",
            "",
            (
                "The completed Phase 1-4 work establishes C1 as "
                "MATHEMATICALLY REALIZED AND INTERNALLY VALIDATED."
            ),
            "",
            (
                "It does not establish that the literal initiating notation "
                "selected C1 uniquely over the competing ternary structures."
            ),
            "",
            "## Interpretation status",
            "",
            "CANDIDATE_RANKING_PERFORMED: NO",
            "",
            "INTERPRETATION_CLASS_SELECTED: NO",
            "",
            (
                "The next step is to map this completed matrix to the frozen "
                "I0-I3 interpretation classes without changing their "
                "definitions."
            ),
            "",
        ]
    )

    return "\n".join(lines)


def main() -> None:
    validate()

    payload = build_json_payload()

    JSON_OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    MD_OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    JSON_OUTPUT.write_text(
        json.dumps(
            payload,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )

    MD_OUTPUT.write_text(
        build_markdown(payload)
    )

    print("Phase 5A candidate-by-criterion matrix")
    print()
    print("Cells:", len(CELLS))
    print("Candidates:", len(CANDIDATES))
    print("Criteria:", len(CRITERIA))
    print("D1 status: NOT_ASSESSABLE")
    print()

    print("Unweighted structural label counts")
    for candidate, counts in assessment_summary().items():
        print(
            f"  {candidate}: "
            f"SUPPORTS={counts['SUPPORTS']} "
            f"NEUTRAL={counts['NEUTRAL']} "
            f"COUNTS_AGAINST={counts['COUNTS_AGAINST']} "
            f"NOT_ASSESSABLE={counts['NOT_ASSESSABLE']}"
        )

    print()
    print("Interpretation class selected: NO")
    print("Candidate ranking performed: NO")
    print()
    print("JSON:", JSON_OUTPUT)
    print("Markdown:", MD_OUTPUT)
    print()
    print(
        "PHASE5A_CANDIDATE_CRITERION_MATRIX: COMPLETE"
    )


if __name__ == "__main__":
    main()
