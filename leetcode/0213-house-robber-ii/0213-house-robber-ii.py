class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_linear(arr):
            prev1 = 0 
            prev2 = 0  
            for num in arr:
                take = num + prev2
                skip = prev1
                curr = max(take, skip)
                prev2 = prev1
                prev1 = curr
            return prev1
        n = len(nums)

        if n == 1:
            return nums[0]

        case1 = rob_linear(nums[:-1])  
        case2 = rob_linear(nums[1:])

        return max(case1, case2)