"""
  1971 - 寻找图中是否存在路径
  
# 有一个具有 n 个顶点的 双向 图，其中每个顶点标记从 0 到 n - 1（包含 0 和 n - 1）。图中的边用一个二维整数数组 edges 表示，其中 
# edges[i] = [ui, vi] 表示顶点 ui 和顶点 vi 之间的双向边。 每个顶点对由 最多一条 边连接，并且没有顶点存在与自身相连的边。 
# 
#  请你确定是否存在从顶点 source 开始，到顶点 destination 结束的 有效路径 。 
# 
#  给你数组 edges 和整数 n、source 和 destination，如果从 source 到 destination 存在 有效路径 ，则返回 
# true，否则返回 false 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# 输出：true
# 解释：存在由顶点 0 到顶点 2 的路径:
# - 0 → 1 → 2 
# - 0 → 2
#  
# 
#  示例 2： 
#  
#  
# 输入：n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# 
# 输出：false
# 解释：不存在由顶点 0 到顶点 5 的路径.
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2 * 10⁵ 
#  0 <= edges.length <= 2 * 10⁵ 
#  edges[i].length == 2 
#  0 <= ui, vi <= n - 1 
#  ui != vi 
#  0 <= source, destination <= n - 1 
#  不存在重复边 
#  不存在指向顶点自身的边 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 78 👎 0

  2022-12-19 12:32:31
"""
import typing
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        return False

    # def validPath(self, n: int, edges: str, source: int, destination: int) -> (int, str, int, int):
    #     return n, edges, source, destination

# leetcode submit region end(Prohibit modification and deletion)


#
#
# def convert_type(arg, var_type):
#     if var_type == int:
#         return int(arg)
#     elif var_type == typing.List[int]:
#         listing = []
#         for a in arg[1:-1].split(','):
#             listing.append(int(a))
#         return listing
#     elif var_type == typing.List[typing.List[int]]:
#         listing = []
#         for a in arg[1:-1].split('],['):
#             k = []
#             for b in a.replace('[', '').replace(']', '').split(','):
#                 k.append(int(b))
#             listing.append(k)
#         return listing
#     elif var_type == typing.List[str]:
#         listing = []
#         for a in arg[1:-1].split(','):
#             listing.append(str(a))
#         return listing
#     elif var_type == typing.List[typing.List[str]]:
#         listing = []
#         for a in arg[1:-1].split(','):
#             k = []
#             for b in a[1:-1].split(','):
#                 k.append(str(b))
#             listing.append(k)
#         return listing
#     else:
#         return str(arg)
#
#
# if __name__ == '__main__':
#     method = [m for m in dir(Solution) if '__' not in m][0]
#     func = getattr(Solution(), method)
#     arg_count = func.__code__.co_argcount - 1
#     arg_names = func.__code__.co_varnames[1:]
#     a = func.__annotations__
#     mapper = {}
#     cases = TEST_CASE.split()
#     if len(cases) % arg_count != 0:
#         print(f"测试案例数目不正确，参数应有{arg_count}个，当前数据条目为{len(cases)}个")
#     else:
#         for i, case in enumerate(cases):
#             j = i % arg_count
#             mapper[arg_names[j]] = convert_type(case, a.get(arg_names[j]))
#             if j == arg_count - 1:
#                 print(f"当前输入参数为: {mapper}")
#                 print(f"执行结果为: {func(**mapper)}")
