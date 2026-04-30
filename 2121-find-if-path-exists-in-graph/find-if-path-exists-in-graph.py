class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:


        # using DFS

        graph = defaultdict(list)

        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)
        
        seen = set()
        seen.add(source)

        def DFS(node):
            if node == destination:
                return True
            
            for adj_node in graph[node]:
                if adj_node not in seen:
                    seen.add(adj_node)
                    if DFS(adj_node): 
                       return True
                
            return False
        return DFS(source)
       