# 拓扑
from typing import List


# 拓扑排序
def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    inedges = [[] for _ in range(n)]
    indegree = [len(node) for node in graph]
    for i in range(n):
        for y in graph[i]:
            inedges[y].append(i)
    queue = [o for o, v in enumerate(indegree) if v == 0]
    res = []
    while queue:
        cur = queue.pop(0)
        res.append(cur)
        for innode in inedges[cur]:
            indegree[innode] -= 1
            if indegree[innode] == 0:
                queue.append(innode)
    return sorted(res)


# 三色标记法
def eventualSafeNodes_tricolor(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    visited = [0] * n

    def safe(i: int) -> bool:
        if visited[i] > 0:
            return visited[i] == 2
        visited[i] = 1
        for v in graph[i]:
            if not safe(v):
                return False
        visited[i] = 2
        return True

    return [i for i in range(n) if safe(i)]


graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
print(eventualSafeNodes(graph))
print(eventualSafeNodes_tricolor(graph))
