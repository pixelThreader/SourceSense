"""Core SourceSense processing pipeline.

This module composes the end-to-end claim analysis flow:
1) extract claims from input text,
2) generate embeddings,
3) cluster semantically similar claims,
4) analyze support vs opposition within clusters.
"""

from src.claims.extractor import extract_claims
from src.embeddings.embedder import embed
from src.clustering.clusterer import cluster_claims
from src.consensus.consensus_engine import analyze_clusters


def run_pipeline(paragraphs):
    """Run the full claim-consensus pipeline on input paragraphs.

    Args:
        paragraphs (list[str]): Source paragraphs to analyze.

    Returns:
        list[dict]: Cluster-level consensus results as returned by
            `analyze_clusters`, each containing:
            - "cluster": list[Claim]
            - "support": int
            - "oppose": int

    Workflow:
        - Extract sentence-level claims from each paragraph.
        - Compute and attach an embedding for each claim.
        - Group similar claims into clusters.
        - Compute support/oppose counts per cluster.
    """
    claims = extract_claims(paragraphs)

    for c in claims:
        c.embedding = embed(c.text)

    clusters = cluster_claims(claims)

    results = analyze_clusters(clusters)

    return results
