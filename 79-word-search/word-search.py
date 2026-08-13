class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        m = len(board)
        n = len(board[0])
        visited = [[False] * n for i in range(m)]

        def dfs(x, y, index):
            if index == len(word):
                return True
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            if visited[x][y]:
                return False
            if board[x][y] != word[index]:
                return False

            visited[x][y] = True

            if dfs(x + 1, y, index + 1):
                return True

            if dfs(x - 1, y, index + 1):
                return True

            if dfs(x, y + 1, index + 1):
                return True

            if dfs(x, y - 1, index + 1):
                return True

            visited[x][y] = False

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False