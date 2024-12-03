from sortedcontainers import SortedDict


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        s1 = SortedList()
        s2 = SortedList()
        for num in nums:
            if num in s2:
                s2[num] += 1
            else:
                s2.add((num))
        print(s2)
        # for i in range()
