class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        
        def sumGoalArray(nums, goal):
            
            if goal < 0:
              return 0

            total = 0
            left = 0
            res = 0
            for i in range(len(nums)):
                total += nums[i]

                while total > goal:
                    total -= nums[left]
                    left += 1
                res += (i-left+1)
            return res
        return  sumGoalArray(nums, goal)- sumGoalArray(nums, goal-1) 
            