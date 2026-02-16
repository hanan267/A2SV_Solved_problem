class Solution:

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        if (mat == [] or len(mat[0]) == 0):
            return []
        
        n = len(mat[0])
        m = len(mat)
        idx = 0
        col = row = 0
        res = [0]*(m*n)
        # print(res)
        upward = True

        while (idx < m*n):
            res[idx] = mat[row][col]

            if (upward):
                if col == n-1:
                    row += 1
                    upward = False
                elif row == 0:
                    col += 1
                    upward = False
                else:
                    col += 1
                    row -= 1
            else:
                if row == m-1:
                    col+=1
                    upward = True
                elif col == 0:
                    row += 1
                    upward = True
                else:
                    col -= 1
                    row += 1
            

            idx += 1 
        return res

        