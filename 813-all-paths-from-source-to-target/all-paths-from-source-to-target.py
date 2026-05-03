class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        res = []
        n = len(graph)
       

        def dfs(node, path):
            if node == n-1:
                res.append(path[:])
            for adj in graph[node]:
                path.append(adj)
                dfs(adj, path)
                path.pop()

        dfs(0, [0])
        
        return res

        