import random

from segment_tree import SegmentTree  


def run_tests() -> None:
    for n in [0, 1, 2, 3, 8, 17, 64]:
        arr = [random.random() for _ in range(n)]
        st = SegmentTree(arr)

        for l in range(n):
            for r in range(l, n):
                s = sum(arr[l : r + 1])
                mn = min(arr[l : r + 1])
                mx = max(arr[l : r + 1])

                assert abs(st.query_sum(l, r) - s) < 1e-9
                assert st.query_min(l, r) == mn
                assert st.query_max(l, r) == mx

        for _ in range(10):
            if n == 0:
                break
            i = random.randrange(n)
            v = random.random()
            arr[i] = v
            st.update(i, v)

            l = random.randrange(0, i + 1)
            r = random.randrange(i, n)
            s = sum(arr[l : r + 1])
            mn = min(arr[l : r + 1])
            mx = max(arr[l : r + 1])

            assert abs(st.query_sum(l, r) - s) < 1e-9
            assert st.query_min(l, r) == mn
            assert st.query_max(l, r) == mx


if __name__ == "__main__":
    run_tests()
    print("All SegmentTree tests passed.")
