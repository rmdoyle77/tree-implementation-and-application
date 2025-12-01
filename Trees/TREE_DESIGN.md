# TREE_DESIGN.md

## Tree Selection

**Tree Type:** Segment Tree (array-backed, iterative implementation)  
**Language:** Python

### Why this tree?

A Segment Tree is ideal when you need to answer many **range queries** (sum, min, max, etc.) with occasional **updates** to individual elements. Instead of scanning the array each time (O(n)), the Segment Tree lets us answer these queries in **O(log n)** time and also update values in **O(log n)**.

This matches the application I chose: an analytics tool for stock price time series, where we often need to query ranges of days and only occasionally correct or adjust individual data points.

---

## Use Cases

Some problems a Segment Tree solves well:

- **Financial time-series analytics**
  - Range sum of prices or returns.
  - Range min and max for risk/volatility analysis.
- **Game scores / leaderboards**
  - Range best score over specific levels or time windows.
- **Telemetry / sensor data**
  - Range min/max to detect anomalies or bounds.
- **Any time-series where you need:**
  - Fast **range queries** (sum/min/max).
  - Fast **point updates** (correcting data).

In this project, the primary use case is:

> **StockScope** – A simple CLI that loads stock closing prices from a CSV and answers fast range queries (sum/min/max) and supports point updates.

---

## Properties & Performance Characteristics

### Structural properties

- Represented as a **complete binary tree** stored in a flat Python list.
- Leaves represent the original array elements.
- Internal nodes store aggregates (sum, min, max) over child ranges.
- Stored in an array of size at most `2 * 2^⌈log₂ n⌉` (≤ 4n).

### Time Complexity

Let **n** be the number of elements (days / prices).

- **Build tree** from array: **O(n)**
- **Range sum query** `[l, r]`: **O(log n)**
- **Range min query** `[l, r]`: **O(log n)**
- **Range max query** `[l, r]`: **O(log n)**
- **Point update** `index`: **O(log n)**
- **Query over all elements**: **O(1)** (root already stores aggregates)

### Space Complexity

- Tree arrays (`sum`, `mn`, `mx`) use **O(n)** space.
- No recursion is used; all operations are iterative.

---

## Interface Design

Below is the logical interface of the Segment Tree as implemented in `segment_tree.py`.

> Note: Some methods are “public” (called by the application) and one is an internal helper (`_query`).

```python
from typing import Sequence, Tuple, Optional


class SegmentTree:
    def __init__(self, data: Optional[Sequence[float]] = None) -> None:
        """Initialize the tree.
        If data is provided, build the tree from it.

        Time:
          - O(n) if data is not None (calls build)
          - O(1) if data is None
        Space: O(n) when built
        """
        ...

    def build(self, data: Sequence[float]) -> None:
        """Build the tree from a sequence of values.

        Time: O(n)
        Space: O(n)
        """
        ...

    def size(self) -> int:
        """Return the number of elements stored.

        Time: O(1)
        Space: O(1)
        """
        ...

    def update(self, index: int, value: float) -> None:
        """Point-update: set data[index] = value.

        Time: O(log n)
        Space: O(1)
        """
        ...

    def query_sum(self, l: int, r: int) -> float:
        """Return the sum over the inclusive range [l, r].

        Time: O(log n)
        Space: O(1)
        """
        ...

    def query_min(self, l: int, r: int) -> float:
        """Return the minimum over the inclusive range [l, r].

        Time: O(log n)
        Space: O(1)
        """
        ...

    def query_max(self, l: int, r: int) -> float:
        """Return the maximum over the inclusive range [l, r].

        Time: O(log n)
        Space: O(1)
        """
        ...

    def query_all(self) -> Tuple[float, float, float]:
        """Return (sum, min, max) over all elements.

        Time: O(1)
        Space: O(1)
        """
        ...
