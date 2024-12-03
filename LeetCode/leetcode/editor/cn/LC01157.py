from collections import Counter
from typing import List


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.sg = SegmentTree(arr)
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        print(Counter(self.arr[left:right + 1]))
        x = self.sg.query(0, 0, self.sg.n - 1, left, right)
        print(x.i, x.cnt)
        if x.cnt + right - left + 1 >= threshold * 2:
            return x.i
        return -1


class Vote:
    def __init__(self, i, cnt):
        self.i = i
        self.cnt = cnt


class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tr = [None] * 4 * self.n
        self.nums = nums
        self.build(0, 0, self.n - 1)

    def build(self, o, l, r):
        if l == r:
            self.tr[o] = Vote(self.nums[l], 1)
            return
        m = (l + r) // 2
        self.build(2 * o + 1, l, m)
        self.build(2 * o + 2, m + 1, r)
        self.tr[o] = self.pushup(self.tr[o * 2 + 1], self.tr[o * 2 + 2])

    def pushup(self, x, y):
        if x == None:
            return y
        if x.i == y.i:
            return Vote(x.i, x.cnt + y.cnt)
        if x.cnt > y.cnt:
            return Vote(x.i, x.cnt - y.cnt)
        else:
            return Vote(y.i, y.cnt - x.cnt)

    def query(self, o, l, r, L, R):
        if L <= l and R >= r:
            return self.tr[o]
        m = (l + r) // 2
        res = None
        if L <= m:
            res = self.pushup(res, self.query(2 * o + 1, l, m, L, R))
        if R > m:
            res = self.pushup(res, self.query(2 * o + 2, m + 1, r, L, R))
        return res


if __name__ == '__main__':
    mc = MajorityChecker(
        [2, 2, 1, 2, 1, 3, 1, 1, 1, 2, 3, 3, 3, 1, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 1, 2, 1, 3, 1, 1, 2, 3, 1, 3, 3, 1, 3,
         2, 2, 2, 3, 2, 3, 1, 2, 1, 3, 3, 3, 2, 2, 1, 1, 2, 2, 3, 2, 3, 3, 3, 2, 1, 2, 3, 1, 3, 2, 3, 1, 2, 3, 3, 2, 2,
         2, 2, 2, 2, 3, 2, 3, 2, 3, 3, 1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 2, 1, 2, 2])
    # print(mc.query(0, 5, 4))
    print(mc.query(31, 97, 34))
