class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
       
        dxn = [(0,1), (0,-1), (1,0), (-1,0)]

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        def DFS(row, colomn):
                visited[row][colomn] = True
                perimeter = 0

                for change_row, change_col in dxn:
                    new_row = change_row + row
                    new_col = change_col + colomn

                    if not inbound(new_row, new_col):
                        perimeter += 1
                    
                    elif grid[new_row][new_col] == 0:
                        perimeter += 1
                    elif grid[new_row][new_col] == 1 and not visited[new_row][new_col]:
                        perimeter += DFS(new_row, new_col)
                return perimeter
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return DFS(i, j)

