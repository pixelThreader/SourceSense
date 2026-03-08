"""Hash-based text embedding utilities.

This module converts input text into a fixed-size numeric vector using a simple
bag-of-words hashing approach. Each token is mapped to one of `VECTOR_SIZE`
buckets, and bucket counts form the embedding vector.

The embedding is deterministic for the same input text and vocabulary, but
collisions can occur because multiple words may map to the same bucket.
"""

import hashlib

VECTOR_SIZE = 128


def hash_word(word):
    """Map a word to a stable vector bucket index.

    Args:
        word (str): Input token to hash.

    Returns:
        int: Bucket index in the range [0, VECTOR_SIZE - 1].

    Notes:
        - Uses MD5 for deterministic hashing (not for security use).
        - Bucket collisions are expected in hashing-based embeddings.
    """
    h = hashlib.md5(word.encode()).hexdigest()
    return int(h, 16) % VECTOR_SIZE


def embed(text):
    """Convert text into a fixed-size hashed count vector.

    The function lowercases the text, splits on whitespace, hashes each token
    to a bucket, and increments that bucket count.

    Args:
        text (str): Raw input text.

    Returns:
        list[int]: Length-`VECTOR_SIZE` vector of token frequency counts.

    Example:
        >>> embed("AI AI model")
        # returns a 128-length vector where two tokens increment the same
        # bucket for "ai" and one bucket for "model"
    """
    vec = [0] * VECTOR_SIZE

    words = text.lower().split()

    for w in words:
        idx = hash_word(w)
        vec[idx] += 1

    return vec
