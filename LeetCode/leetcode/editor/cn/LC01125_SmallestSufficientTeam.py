"""
  1125 - 最小的必要团队
  
# 作为项目经理，你规划了一份需求的技能清单 req_skills，并打算从备选人员名单 people 中选出些人组成一个「必要团队」（ 编号为 i 的备选人员
#  people[i] 含有一份该备选人员掌握的技能列表）。 
# 
#  所谓「必要团队」，就是在这个团队中，对于所需求的技能列表 req_skills 中列出的每项技能，团队中至少有一名成员已经掌握。可以用每个人的编号来表示团
# 队中的成员： 
# 
#  
#  例如，团队 team = [0, 1, 3] 表示掌握技能分别为 people[0]，people[1]，和 people[3] 的备选人员。 
#  
# 
#  请你返回 任一 规模最小的必要团队，团队成员用人员编号表示。你可以按 任意顺序 返回答案，题目数据保证答案存在。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],[
# "nodejs","reactjs"]]
# 输出：[0,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people 
# = [["algorithms","math","java"],["algorithms","math","reactjs"],["java",
# "csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= req_skills.length <= 16 
#  1 <= req_skills[i].length <= 16 
#  req_skills[i] 由小写英文字母组成 
#  req_skills 中的所有字符串 互不相同 
#  1 <= people.length <= 60 
#  0 <= people[i].length <= 16 
#  1 <= people[i][j].length <= 16 
#  people[i][j] 由小写英文字母组成 
#  people[i] 中的所有字符串 互不相同 
#  people[i] 中的每个技能是 req_skills 中的技能 
#  题目数据保证「必要团队」一定存在 
#  
# 
#  Related Topics 位运算 数组 动态规划 状态压缩 👍 172 👎 0

  2023-04-10 20:39:54
"""
from functools import cache
from typing import *

TEST_CASE = """
["algorithms","math","java","reactjs","csharp","aws"]
[["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # 建立二进制模型
        n, m = len(req_skills), len(people)
        mapper = {}
        x = 0
        for r in req_skills:
            mapper[r] = x
            x += 1
        pp = []
        for p in people:
            cur = 0
            for x in p:
                cur += 1 << mapper[x]
            pp.append(cur)

        @cache
        def dfs(i: int, j: int) -> int:
            if j == 0: return 0
            if i < 0: return (1 << m) - 1
            res1 = dfs(i - 1, j)
            res2 = dfs(i - 1, j & ~pp[i]) | (1 << i)
            return res1 if res1.bit_count() < res2.bit_count() else res2

        res = dfs(m - 1, (1 << n) - 1)
        return [i for i in range(m) if (1 << i) & res]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.smallestSufficientTeam(["algorithms", "math", "java", "reactjs", "csharp", "aws"],
                                   [["algorithms", "math", "java"], ["algorithms", "math", "reactjs"],
                                    ["java", "csharp", "aws"], ["reactjs", "csharp"], ["csharp", "math"],
                                    ["aws", "java"]]
                                   ))
