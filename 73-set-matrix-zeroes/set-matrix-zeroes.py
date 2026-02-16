class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        colomn = len(matrix[0])
        # print(colomn)
        row = len(matrix)
        rowSet = set()
        columnSet = set()
        for i in range(row):
            for j in range(colomn):
                if matrix[i][j] == 0:
                    # zeros.append((i, j))
                    # print(i,j)
                    rowSet.add(i)
                    columnSet.add(j)
        # print(rowSet)
        # make the row zero
        for i in range(row):
            if i in rowSet:
                for column in range(colomn):
                    matrix[i][column] = 0
        # print(matrix)

        # make the colum rero
        # print(columnSet)
        for i in range(colomn):
            # print(i)
            if i in columnSet:
                for rows in range(row):
                    matrix[rows][i] = 0
        return (matrix)
                    


       
        