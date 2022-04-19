# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-01-08 20:22
"""
import heapq
from typing import List


def dijkstar(graph: List[List[int]], n: int, k: int):
    g = [[] for _ in range(n)]
    for x, y, dist in graph:
        g[x - 1].append((y - 1, dist))
    distance = [float('inf')] * n
    distance[k - 1] = 0
    queue = [(0, k - 1)]
    while queue:
        dist, x = heapq.heappop(queue)
        if distance[x] >= dist:
            for y, pre_dist in g[x]:
                if (cur_dist := pre_dist + dist) < distance[y]:
                    distance[y] = cur_dist
                    heapq.heappush(queue, (cur_dist, y))
    return max(distance)


graph = [[2, 1, 3], [2, 4, 5], [1, 3, 1]]
print(dijkstar(graph, 4, 2))
