# -*- coding: utf-8 -*-
from functools import cache


class Solution:
    def digitDP(n):
        s = str(n)

        @cache
        def dfs(i: int, limit: bool, has_num: bool):
            if i == len(s):
                return
            if not has_num:
                dfs(i + 1, limit, False)
            up = int(s[i]) if limit else 9
            for d in range(1 - int(has_num), up + 1):
                dfs(i + 1, limit and up == d)
            return

        return dfs(0, True)
