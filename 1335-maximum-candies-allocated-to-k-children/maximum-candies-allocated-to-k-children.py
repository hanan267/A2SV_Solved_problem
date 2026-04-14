class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:


            def feasible(pile):
                if pile == 0:
                    return True

                total = 0

                for c in candies:
                    total += c // pile
                return total >= k 
            
            left, right = 0, max(candies)

            res = 0

            while left <= right:

                mid = (left+right) // 2
                print(mid, feasible(mid))
                if feasible(mid):
                    res = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return res
        