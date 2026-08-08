class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = {}
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            value = values[i]
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(current, target, visited):

            if current not in graph:
                return -1

            if current == target:
                return 1
            visited.add(current)
            for neighbor, value in graph[current]:
                if neighbor in visited:
                    continue
                result = dfs(neighbor, target, visited)
                if result != -1:
                    return value * result
            return -1

        answer = []

        for a, b in queries:
            answer.append(dfs(a, b, set()))

        return answer