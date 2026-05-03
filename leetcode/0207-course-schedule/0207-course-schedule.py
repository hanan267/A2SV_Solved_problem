class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        n = numCourses
        graph = defaultdict(list)

        state = [0] * n

        for i, j in prerequisites:
            graph[i].append(j)

        unvisited = 0
        visiting = 1
        visited = 2

        def dfs(node):
            if state[node] == visited:
                return True
            elif state[node] == visiting:
                return False
            
            state[node] = visiting

            for adj in graph[node]:
                if not dfs(adj):
                    return False

            state[node] = visited
            return True
        
        for i in range(n):
            if not dfs(i):
                return False
        return True


        # Time O(E + N)
                    
        