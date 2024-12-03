from typing import List


def longestSubarray(nums: List[int]) -> int:
    s = {}
    ans = 0
    mx = 0
    for i, num in enumerate(nums):
        if num not in s:
            s[num] = i
        t = {}
        for x, left in s.items():
            c = x & num
            if c >= mx:
                if c == mx:
                    ans = max(ans, i - left + 1)
                else:
                    ans = i - left + 1
                mx = c
            if c in t:
                t[c] = min(left, t[c])
            else:
                t[c] = left
        s = t
    return ans


print(longestSubarray([1, 2, 3, 3, 2, 2]))
