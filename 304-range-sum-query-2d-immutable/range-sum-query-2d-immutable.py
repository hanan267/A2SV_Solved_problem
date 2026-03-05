class NumMatrix:

    def __init__(self, matrix):
        if not matrix:
            return

        row, col = len(matrix), len(matrix[0])

        self.pref = [[0]*(col+1) for i in range((row)+1)]

        for r in range(1, row+1):
            for c in range(1, col+1):
                self.pref[r][c] = (
                    matrix[r-1][c-1]+
                    self.pref[r-1][c]+
                    self.pref[r][c-1]
                    -self.pref[r-1][c-1]
                )
        
    def sumRegion(self, row1, col1, row2, col2):
        return (
            self.pref[row2+1][col2+1]
            -self.pref[row1][col2+1]
            -self.pref[row2+1][col1]
            +self.pref[row1][col1]
        )
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)