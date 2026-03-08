"""Confidence scoring utilities for consensus outcomes.

This module computes a normalized confidence score from support and opposition
counts using a weighted linear formula and bounds the result to [0, 1].
"""


def compute_confidence(support, oppose, total):
    """Compute confidence from support/oppose evidence.

    The score rewards supporting evidence and penalizes contradictory evidence:

        score = 0.7 * (support / total) - 0.4 * (oppose / total)

    The final value is clamped to the range [0, 1].

    Args:
        support (int | float): Number of supporting claims/evidence items.
        oppose (int | float): Number of opposing claims/evidence items.
        total (int | float): Total evidence count used for normalization.

    Returns:
        float: Confidence score in [0, 1]. Returns 0 when `total == 0`.
    """
    if total == 0:
        return 0

    support_ratio = support / total
    contradiction_ratio = oppose / total

    score = 0.7 * support_ratio - 0.4 * contradiction_ratio

    return max(0, min(1, score))
