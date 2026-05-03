class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        graph = defaultdict(list)
        n = len(bombs)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
                if d <= r1:
                    graph[i].append(j)
               
        res = 0

        def dfs(node, seen):
            for adj in graph[node]:
                if adj not in seen:
                    seen.add(adj)
                    dfs(adj, seen)

        for i in range(n):
            visited = set([i])
            dfs(i, visited)
            res = max(res, len(visited))

        
        
        return res
    

                
        
        