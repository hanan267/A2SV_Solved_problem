class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def count_less(mid):
            i, j = n - 1, 0
            count = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    count += i + 1
                    j += 1
                else:
                    i -= 1
            return count

        def feasible(count):
            return count_less(count) >= k

        left, right = matrix[0][0], matrix[n-1][n-1]
       
        while left < right:
            mid = (right + left)//2
            if feasible(mid):
                right = mid 
            else:
                left = mid + 1
        return right
