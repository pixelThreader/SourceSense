"""Vector similarity utilities.

This module provides cosine similarity for numeric vectors, commonly used to
compare semantic closeness between embeddings.
"""

import math


def cosine_similarity(a, b):
    """Compute cosine similarity between two vectors.

    Cosine similarity is defined as:
        dot(a, b) / (||a|| * ||b||)

    Args:
        a (list[float] | tuple[float, ...]): First vector.
        b (list[float] | tuple[float, ...]): Second vector.

    Returns:
        float: Similarity score in [-1.0, 1.0] for signed vectors, or
            [0.0, 1.0] for non-negative vectors. Returns `0` when either
            vector has zero magnitude.

    Notes:
        - Uses pairwise multiplication via `zip(a, b)`.
        - If lengths differ, extra elements in the longer vector are ignored.
    """
    dot = sum(x * y for x, y in zip(a, b))

    mag_a = math.sqrt(sum(x * x for x in a))
    mag_b = math.sqrt(sum(x * x for x in b))

    if mag_a == 0 or mag_b == 0:
        return 0

    return dot / (mag_a * mag_b)
