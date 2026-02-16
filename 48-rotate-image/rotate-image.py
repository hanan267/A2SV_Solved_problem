class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1

        while l < r:
            top, bottom = l, r
            for i in range(r-l):
                # hold the top left
                topLeft = matrix[top][l+i]
                # move bottom left to top left
                matrix[top][l+i] = matrix[bottom-i][l]
                # move right bottom to left bottom
                matrix[bottom-i][l] = matrix[bottom][r-i]
                # move right top to right bottom
                matrix[bottom][r-i] = matrix[top+i][r]
                # move left top to right top
                matrix[top+i][r] = topLeft
            l+=1
            r-=1
        return matrix
        