"""Disjoint-set (Union-Find) data structure for clustering.

This module provides a UnionFind implementation used to efficiently build
connected components of similar claims. It supports near-constant-time
`find` and `union` operations with path compression.
"""


class UnionFind:
    """Track disjoint sets of integer indices.

    Each index starts in its own set. Sets are merged with `union`, and
    representative roots are retrieved with `find`.

    Attributes:
        parent (list[int]): Parent pointer array where `parent[i]` is the
            current parent of node `i`. A root node points to itself.
    """

    def __init__(self, n):
        """Initialize `n` singleton sets.

        Args:
            n (int): Number of elements to manage, indexed from 0 to n - 1.
        """
        self.parent = list(range(n))

    def find(self, x):
        """Find the root representative for element `x`.

        Uses path compression so future lookups on the same path are faster.

        Args:
            x (int): Element index.

        Returns:
            int: Root index of the set containing `x`.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a, b):
        """Merge the sets containing `a` and `b`.

        If both elements are already in the same set, this is a no-op.

        Args:
            a (int): First element index.
            b (int): Second element index.
        """
        pa = self.find(a)
        pb = self.find(b)

        if pa != pb:
            self.parent[pb] = pa
