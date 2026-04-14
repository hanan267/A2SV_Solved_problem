class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        res = []
        for i in range(n):
            for j in range(m):
                res.append(matrix[i][j])
        print(res)
        left, right = 0, len(res)-1

        while left <= right:
            mid = (left+right) // 2
            if res[mid] == target:
                return True
            if res[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

        