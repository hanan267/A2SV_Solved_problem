class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        
        
        total = 0
        required = 0
        for i in range(len(nums)):
            total += nums[i]
            required = min(total, required)
            
               
        return 1-required
        