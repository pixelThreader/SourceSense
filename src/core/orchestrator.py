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
        list[dict]: Pipeline output produced by `run_pipeline`, containing
            per-cluster consensus summaries.
    """
    results = run_pipeline(paragraphs)

    return results
