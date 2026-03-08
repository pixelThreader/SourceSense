"""Console dashboard rendering for consensus results.

This module formats consensus analysis output as a Rich table for terminal
display, including support/oppose counts and a simple confidence ratio.
"""

from rich.console import Console
from rich.table import Table


console = Console()


def show_results(results):
    """Display consensus results in a terminal table.

    Args:
        results (list[dict]): Per-cluster result objects with keys:
            - "cluster": list[Claim]
            - "support": int
            - "oppose": int

    Behavior:
        - Uses the first claim in each cluster as a representative example.
        - Truncates example text to 60 characters.
        - Computes displayed confidence as `support / (support + oppose)`,
          falling back to 0 when the total is zero.
    """
    table = Table(title="SourceSense Consensus Report")

    table.add_column("Claim Example")
    table.add_column("Support")
    table.add_column("Oppose")
    table.add_column("Confidence")

    for r in results:
        claim = r["cluster"][0].text[:60]

        support = r["support"]
        oppose = r["oppose"]

        total = support + oppose

        confidence = support / total if total else 0

        table.add_row(claim, str(support), str(oppose), f"{confidence:.2f}")

    console.print(table)
