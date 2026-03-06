class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total = nums[0]
        maxTot = nums[0]

        for i in range(1, len(nums)):
            total = max(nums[i], total+nums[i])
            maxTot = max(maxTot, total)
        return maxTot
            

            
            
        