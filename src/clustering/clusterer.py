"""Claim clustering utilities based on embedding similarity.

This module groups claims into clusters by building a similarity graph:
two claims are connected when cosine similarity exceeds `SIM_THRESHOLD`.
Connected components are computed with Union-Find.
"""

from src.clustering.union_find import UnionFind
from src.embeddings.similarity import cosine_similarity


SIM_THRESHOLD = 0.30 # Tweakable threshold for claim similarity; higher means more strict clustering 


def cluster_claims(claims):
    """Cluster claims using pairwise cosine similarity.

    For each claim pair `(i, j)`, cosine similarity is computed from their
    precomputed embedding vectors. If similarity is above `SIM_THRESHOLD`,
    their indices are unioned. Final clusters are the Union-Find components.

    Args:
        claims (list[Claim]): Claim objects with `embedding` already populated.

    Returns:
        list[list[Claim]]: List of clusters, where each cluster is a list of
            semantically similar claims.

    Notes:
        - Time complexity is O(n^2) similarity checks.
        - Assumes each claim has a valid numeric embedding.
        - Similarity condition is strict (`sim > SIM_THRESHOLD`).
    """
    n = len(claims)
    uf = UnionFind(n)

    for i in range(n):
        for j in range(i + 1, n):
            sim = cosine_similarity(claims[i].embedding, claims[j].embedding)
            print(claims[i].text[:40], " | ", claims[j].text[:40], " -> ", sim)
            if sim > SIM_THRESHOLD:
                uf.union(i, j)

    clusters = {}

    for i in range(n):
        root = uf.find(i)

        if root not in clusters:
            clusters[root] = []

        clusters[root].append(claims[i])

    return list(clusters.values())
