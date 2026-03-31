class Solution:
    def mySqrt(self, x: int) -> int:

        low = 0
        high = x // 2
        possible = 0
        if x == 0:
            return 0
        if x == 1:
            return 1
        while low <= high:
            mid = (low+high)//2
            if mid * mid <= x:
                possible = mid
                low = mid + 1
            elif mid * mid > x:
                high = mid - 1
        return possible
                
        