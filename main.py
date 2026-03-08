"""Executable entrypoint for running SourceSense end-to-end.

This script provides sample source paragraphs, runs the core SourceSense
pipeline, and renders consensus results in the terminal dashboard.
"""

from src.core.orchestrator import run_sourcesense
from src.tui.dashboard import show_results


paragraphs = [
    """
Rust prevents memory safety bugs through ownership and borrowing.
Many developers say Rust improves system reliability.
""",
    """
C++ allows manual memory management.
Some engineers argue Rust does not eliminate all memory bugs.
""",
]


def main():
    """Run SourceSense on bundled sample paragraphs and display results."""
    results = run_sourcesense(paragraphs)
    show_results(results)


if __name__ == "__main__":
    main()
