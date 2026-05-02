class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)
        color = [-1 for i in range(n)]
        result = True

        def dfs(node):
            temp = True
            for adj in graph[node]:
                if color[adj] == -1:
                    if color[node] == 0:
                        color[adj] = 1
                    else:
                        color[adj] = 0
                    temp = temp and dfs(adj)
                else:
                    if color[adj] == color[node]:
                        return False
            return temp
        for i in range(n):
            if color[i] == -1:
                color[i] = 0
                result = result and dfs(i)

        
        return result
            


        