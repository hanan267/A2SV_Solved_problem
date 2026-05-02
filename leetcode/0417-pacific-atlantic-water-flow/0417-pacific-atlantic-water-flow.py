class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()

        n, m = len(heights), len(heights[0])

        for i in range(m):
            p_que.append((0, i))
            p_seen.add((0, i))
        for j in range(1, n):
            p_que.append((j, 0))
            p_seen.add((j, 0))

        for i in range(n):
            a_que.append((i, m-1))
            a_seen.add((i, m-1))
        for j in range(m-1):
            a_que.append((n-1, j))
            a_seen.add((n-1, j))

        def inbound(row, col):
            return ( 0 <= row < n and 0 <= col < m )
        def bfs(que, seen):
            
            while que:
                i, j = que.popleft()
                for new_row, new_col in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    r, c = i + new_row, j + new_col
                    if inbound(r, c) and heights[r][c] >= heights[i][j] and (r, c) not in seen:
                        que.append((r, c))
                        seen.add((r, c))
            return seen
        
        q = bfs(p_que, p_seen)
        a = bfs(a_que, a_seen)

        return list(q.intersection(a))


        