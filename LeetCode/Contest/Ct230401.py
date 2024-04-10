# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        ans = 0
        mp = {}
        for i in range(26):
            x = chr(ord('a') + i)
            if x in chars:
                j = chars.index(x)
                mp[x] = vals[j]
            else:
                mp[x] = i + 1
        n = len(s)
        f = [0] * n
        for i in range(n):
            f[i] = max(f[i], mp[s[i]] + (f[i - 1] if f[i - 1] > 0 else 0))
            ans = max(ans, f[i])
        return ans


s = Solution()
print(s.maximumCostSubstring('hghhghgghh', "hg", [2, 3]))
