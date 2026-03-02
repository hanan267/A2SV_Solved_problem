class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        ## prefix sum on each index

    # step 1: iterate from 0-n-1
    # step 2: track the sum as you go on each index and put at the index
    # step 3: put it as a new array and return at the end

        # preSum = nums[0]
        # preSumArray = [nums[0]]

        # for i in range(1, len(nums)):
        #     preSum += nums[i]
        #     preSumArray.append(preSum)
        # return preSumArray
        
        running = nums[0]
        res = [nums[0]]
        for i in range(1,len(nums)):
            running += nums[i]
            res.append(running)
        return res




        # 