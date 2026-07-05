class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        n = len(nums)
        ZeroC = 0
        left = 0
        res = 0
        for right in range(n):
            if nums[right] == 0:
                ZeroC += 1
            while ZeroC > k:
                
                if nums[left] == 0:
                    ZeroC -= 1
                left += 1
            
            res = max(right - left + 1, res)
        return res






        