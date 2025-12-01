from typing import List, Sequence, Tuple, Optional


class SegmentTree:
   
    def __init__(self, data: Optional[Sequence[float]] = None) -> None:
        self.n = 0
        self.base = 1
        self.sum: List[float] = [0.0]
        self.mn: List[float] = [float("inf")]
        self.mx: List[float] = [float("-inf")]
        if data is not None:
            self.build(data)

    def build(self, data: Sequence[float]) -> None:
        self.n = len(data)
        if self.n == 0:
            self.base = 1
            self.sum = [0.0, 0.0]
            self.mn = [float("inf"), float("inf")]
            self.mx = [float("-inf"), float("-inf")]
            return

        b = 1
        while b < self.n:
            b <<= 1
        self.base = b

        size = 2 * b
        self.sum = [0.0] * size
        inf = float("inf")
        self.mn = [inf] * size
        self.mx = [-inf] * size

        for i, v in enumerate(data):
            p = b + i
            self.sum[p] = v
            self.mn[p] = v
            self.mx[p] = v

        for p in range(b - 1, 0, -1):
            lc, rc = p << 1, (p << 1) | 1
            self.sum[p] = self.sum[lc] + self.sum[rc]
            self.mn[p] = min(self.mn[lc], self.mn[rc])
            self.mx[p] = max(self.mx[lc], self.mx[rc])

    def size(self) -> int:
        return self.n

    def update(self, index: int, value: float) -> None:
        assert 0 <= index < self.n, "index out of range"
        p = self.base + index
        self.sum[p] = value
        self.mn[p] = value
        self.mx[p] = value
        p >>= 1
        while p:
            lc, rc = p << 1, (p << 1) | 1
            self.sum[p] = self.sum[lc] + self.sum[rc]
            self.mn[p] = min(self.mn[lc], self.mn[rc])
            self.mx[p] = max(self.mx[lc], self.mx[rc])
            p >>= 1

    
    def _query(self, l: int, r: int) -> Tuple[float, float, float]:
        assert 0 <= l <= r < self.n, "window out of range"
        L, R = l + self.base, r + self.base
        s = 0.0
        mn = float("inf")
        mx = float("-inf")
        while L <= R:
            if (L & 1) == 1:
                s += self.sum[L]
                mn = min(mn, self.mn[L])
                mx = max(mx, self.mx[L])
                L += 1
            if (R & 1) == 0:
                s += self.sum[R]
                mn = min(mn, self.mn[R])
                mx = max(mx, self.mx[R])
                R -= 1
            L >>= 1
            R >>= 1
        return s, mn, mx

    def query_sum(self, l: int, r: int) -> float:
        return self._query(l, r)[0]

    def query_min(self, l: int, r: int) -> float:
        return self._query(l, r)[1]

    def query_max(self, l: int, r: int) -> float:
        return self._query(l, r)[2]

    def query_all(self) -> Tuple[float, float, float]:
        if self.n == 0:
            return 0.0, float("inf"), float("-inf")
        return self.sum[1], self.mn[1], self.mx[1]
