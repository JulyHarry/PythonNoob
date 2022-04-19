# -*- coding: utf-8 -*- 
"""
Description:  LC01036 - 逃离大迷宫
URL:          https://leetcode-cn.com/problems/escape-a-large-maze/
Creator:      HarryUp
Create time:  2022-01-11 21:37:26
Content:
# 在一个 10⁶ x 10⁶ 的网格中，每个网格上方格的坐标为 (x, y) 。 
# 
#  现在从源方格 source = [sx, sy] 开始出发，意图赶往目标方格 target = [tx, ty] 。数组 blocked 是封锁的方格列表
# ，其中每个 blocked[i] = [xi, yi] 表示坐标为 (xi, yi) 的方格是禁止通行的。 
# 
#  每次移动，都可以走到网格中在四个方向上相邻的方格，只要该方格 不 在给出的封锁列表 blocked 上。同时，不允许走出网格。 
# 
#  只有在可以通过一系列的移动从源方格 source 到达目标方格 target 时才返回 true。否则，返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
# 输出：false
# 解释：
# 从源方格无法到达目标方格，因为我们无法在网格中移动。
# 无法向北或者向东移动是因为方格禁止通行。
# 无法向南或者向西移动是因为不能走出网格。 
# 
#  示例 2： 
# 
#  
# 输入：blocked = [], source = [0,0], target = [999999,999999]
# 输出：true
# 解释：
# 因为没有方格被封锁，所以一定可以到达目标方格。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= blocked.length <= 200 
#  blocked[i].length == 2 
#  0 <= xi, yi < 10⁶ 
#  source.length == target.length == 2 
#  0 <= sx, sy, tx, ty < 10⁶ 
#  source != target 
#  题目数据保证 source 和 target 不在封锁列表内 
#  
#  Related Topics 深度优先搜索 广度优先搜索 数组 哈希表 👍 143 👎 0

"""
from collections import deque


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def isEscapePossible(self, blocked, source, target):
        # discretization
        da

    # leetcode submit region end(Prohibit modification and deletion)

    def isEscapePossible2(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        BLOCKED, VALID, FOUND = -1, 0, 1
        n = len(blocked)
        BOUNDRY = 10 ** 6

        def search(blocked, source, target):
            queue = deque([(source[0], source[1])])
            countdown = n * (n - 1) // 2
            visited = {(source[0], source[1])}
            while queue and countdown > 0:
                cx, cy = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < BOUNDRY and 0 <= ny < BOUNDRY and (nx, ny) not in visited and [nx, ny] not in blocked:
                        if nx == target[0] and ny == target[1]:
                            return FOUND
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                        countdown -= 1
            if countdown > 0:
                return BLOCKED
            else:
                return VALID

        result = search(blocked, source, target)
        if result == FOUND:
            return True
        elif result == BLOCKED:
            return False
        else:
            result2 = search(blocked, target, source)
            if result2 == BLOCKED:
                return False
            else:
                return True


s = Solution()
blocked = [[10, 9], [9, 10], [10, 11], [11, 10]]
source = [0, 0]
target = [10, 10]
print(s.isEscapePossible(blocked, source, target))
