"""Claim data structure module.

This module defines the core Claim class used throughout the SourceSense pipeline
to represent individual factual statements extracted from source documents.
"""


class Claim:
    """Represents a single claim or factual statement extracted from a source.

    A Claim encapsulates the text content of a statement, tracks its source origin,
    and stores the embedding vector used for semantic similarity comparisons during
    clustering and consensus analysis.

    Attributes:
        text (str): The actual text content of the claim/statement.
        source_id (int): Identifier of the source document this claim was extracted from.
        embedding (numpy.ndarray or None): Vector embedding of the claim text for semantic
            similarity calculations. Initially None until computed by the embedder.

    Example:
        >>> claim = Claim("The Earth orbits the Sun", source_id=0)
        >>> claim.text
        'The Earth orbits the Sun'
        >>> claim.source_id
        0
        >>> claim.embedding is None
        True
    """

    def __init__(self, text, source_id):
        """Initialize a new Claim instance.

        Args:
            text (str): The claim text content.
            source_id (int): The identifier of the source document.
        """
        self.text = text
        self.source_id = source_id
        self.embedding = None
