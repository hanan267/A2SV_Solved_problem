class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in relations:
            u -= 1
            v -= 1
            graph[u].append(v)
            indegree[v] += 1
        q = deque()
        dp = [0] * n
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                dp[i] = time[i]
        while q:
            u = q.popleft()
            for v in graph[u]:
                dp[v] = max(dp[v], dp[u] + time[v])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return max(dp)