class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        
        def capable(capacity):
            day, capability = 1, capacity
            for weight in weights:
                if capability < weight:
                    day += 1
                    capability = capacity
                capability -= weight
            return day <= days

        left, right = max(weights), sum(weights)
        res = right

        while left <= right:
            mid = (left+right) // 2
            if capable(mid):
                res = min(mid, res)
                right = mid - 1
            else:
                left = mid + 1
        return res
        