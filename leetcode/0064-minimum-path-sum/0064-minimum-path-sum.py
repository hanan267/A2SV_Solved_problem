class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        memo = {}

        def dp(r, c):
            if r == rows or c == cols:
                return float("inf")

            if r == rows - 1 and c == cols - 1:
                return grid[r][c]

            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = grid[r][c] + min(dp(r + 1, c), dp(r, c + 1))
            return memo[(r, c)]
        return dp(0, 0)