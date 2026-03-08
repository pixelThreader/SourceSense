"""Top-level orchestration entrypoint for SourceSense.

This module exposes a simple public function to run the full pipeline from
raw input paragraphs to consensus analysis output.
"""

from src.core.pipeline import run_pipeline


def run_sourcesense(paragraphs):
    """Execute SourceSense analysis for the provided inputs.

    Args:
        paragraphs (list[str]): Source paragraphs/documents to process.

    Returns:
        tuple[list[dict], dict]: A tuple containing:
            - Cluster-level consensus results as returned by `run_pipeline`, each containing:
                - "cluster": list[Claim]
                - "support": int
                - "oppose": int
            - Statistics about the analysis, including:
                - "total_claims": int
                - "clusters": int
                - "contradictions": int
    """
    results, stats = run_pipeline(paragraphs)

    return results, stats
