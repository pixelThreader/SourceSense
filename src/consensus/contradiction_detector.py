"""Heuristic contradiction detection via text polarity.

This module provides a lightweight rule-based polarity classifier for claim text.
A claim is marked as opposing (`-1`) if it contains any known negation cue;
otherwise it is marked as supporting (`1`).
"""

NEGATIONS = ["not", "no", "never", "cannot", "fails", "false", "unlikely"]


def polarity(text):
    """Classify claim polarity using negation keyword matching.

    Args:
        text (str): Claim text to evaluate.

    Returns:
        int: `-1` if any negation cue is present, otherwise `1`.

    Notes:
        - Matching is case-insensitive.
        - Uses substring checks (`n in text`), so this is intentionally simple
          and may produce false positives/negatives compared to NLP parsing.
    """
    text = text.lower()

    for n in NEGATIONS:
        if n in text:
            return -1

    return 1
