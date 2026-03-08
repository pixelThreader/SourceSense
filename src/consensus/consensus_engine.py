"""Consensus analysis over clustered claims.

This module aggregates support vs oppose counts for each semantic claim cluster.
Polarity is computed per claim using the contradiction detector heuristic.
"""

from src.consensus.contradiction_detector import polarity


def analyze_clusters(clusters):
    """Compute support/oppose statistics for each cluster.

    For every cluster, each claim is scored with `polarity(claim.text)`:
    positive values count as support, non-positive values count as oppose.

    Args:
        clusters (list[list[Claim]]): Clustered claims, typically from the
            clustering stage.

    Returns:
        list[dict]: One result per cluster with shape:
            `{"cluster": <list[Claim]>, "support": <int>, "oppose": <int>}`.
    """
    results = []

    for c in clusters:
        support = 0
        oppose = 0

        for claim in c:
            p = polarity(claim.text)

            if p > 0:
                support += 1
            else:
                oppose += 1

        results.append({"cluster": c, "support": support, "oppose": oppose})

    return results
