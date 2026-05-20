class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)

        for from1, to1 in edges:
            graph[to1].append(from1)
        # print(graph)

        def dfs(node, ance, visited):
            if node in visited:
                return 

            visited.add(node)
            for adje in graph[node]:
                ance.add(adje)
                dfs(adje, ance, visited)
            return ance

        res = []
        for i in range(n):
            ance = set()
            visited = set()
            dfs(i, ance, visited)
            res.append(sorted(ance))
        return res



        