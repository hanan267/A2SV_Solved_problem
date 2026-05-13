from heapq import heappush, heappop
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        hulum = []
        for i, (l, r, h) in enumerate(buildings):
            hulum.append((l, h, "start", i))
            hulum.append((r, h, "end", i))
        hulum.sort(key=lambda x: (x[0], -x[1] if x[2] == "start" else x[1]))
        heap = []
        lazy = set()
        res = []
        prev = 0
        for point, height, pos, uniq in hulum:
            if pos == "start":
                heappush(heap, (-height, uniq))
            else:
                lazy.add((-height, uniq))
            while heap and heap[0] in lazy:
                heappop(heap)
            top = -heap[0][0] if heap else 0
            if top != prev:
                res.append([point, top])
                prev = top
        return res