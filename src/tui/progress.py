"""Terminal progress helpers for SourceSense.

This module provides a minimal Rich-based progress display used to indicate
pipeline execution status in the terminal UI.
"""

from rich.progress import Progress


def run_progress():
    """Render a simple progress bar from 0 to 100%.

    Creates a single task labeled "Processing..." and advances it in fixed
    increments of 10 until completion.

    Notes:
        - Intended as a lightweight visual indicator/demo.
        - Progress advances immediately in a tight loop (no delay).
    """
    progress = Progress()

    task = progress.add_task("Processing...", total=100)

    with progress:
        while not progress.finished:
            progress.update(task, advance=10)
