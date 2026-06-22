class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        memo = {0:nums[0], 1:max(nums[0], nums[1])}

        def dp(i):
            if i not in memo:
                memo[i] = max(nums[i]+dp(i-2), dp(i-1))
            return memo[i]
        return dp(n-1)




        