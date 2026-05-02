class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inbound(i, j):
            return (0 <= i < len(grid) and 0 <= j < len(grid[0]))

        def dfs(i, j):
            if not inbound(i, j) or grid[i][j] != "1":
                return 
            else:
                grid[i][j] = "0"
                dfs(i, j+1)
                dfs(i, j-1)
                dfs(i+1, j)
                dfs(i-1, j)

        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    island += 1
        return island