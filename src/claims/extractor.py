"""Claim extraction utilities.

This module provides functionality to extract individual claims from source paragraphs
by splitting them into sentences and filtering by minimum length criteria.
"""

import re
from src.claims.claim import Claim


def extract_claims(paragraphs):
    """Extract individual claims from a list of text paragraphs.

    Processes each paragraph by splitting it into sentences using common sentence
    delimiters (periods, exclamation marks, question marks). Filters out very short
    sentences (less than 15 characters) to focus on substantive claims. Each claim
    is tagged with its source paragraph index.

    Args:
        paragraphs (list of str): List of paragraph strings to extract claims from.
            Each paragraph may contain multiple sentences.

    Returns:
        list of Claim: List of Claim objects, each representing a single extracted
            sentence/statement with its associated source_id indicating which paragraph
            it originated from.

    Notes:
        - Sentences are split using regex pattern r"[.!?]"
        - Only sentences with more than 15 characters (after stripping whitespace) are kept
        - source_id corresponds to the index position of the paragraph in the input list
        - All sentences from the same paragraph share the same source_id

    Example:
        >>> paragraphs = [
        ...     "The sky is blue. Water is wet.",
        ...     "The Earth is round. Gravity pulls objects down."
        ... ]
        >>> claims = extract_claims(paragraphs)
        >>> len(claims)
        4
        >>> claims[0].text
        'The sky is blue'
        >>> claims[0].source_id
        0
        >>> claims[2].source_id
        1
    """
    claims = []
    source_id = 0

    for para in paragraphs:
        sentences = re.split(r"[.!?]", para)

        for s in sentences:
            s = s.strip()

            if len(s) > 15:
                claims.append(Claim(s, source_id))

        source_id += 1

    return claims
