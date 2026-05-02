class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def inbound(row, col):
            return ( 0 <= row < len(board) and 0 <= col < len(board[0]))
        
        def dfs(row, col):
            if not inbound(row, col) or board[row][col] != "O":
                return 
            board[row][col] = "T"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        def isBorder(row, col):
            if ((row in [0, len(board)-1]) or (col in [0, len(board[0])-1])):
                return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if isBorder(i, j):
                    dfs(i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return board
