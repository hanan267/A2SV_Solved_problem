class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        n = len(nums)
        realNum = [0]*(n-1)

        for i in range(n):
            correct = nums[i] - 1
          
            if realNum[correct] == 0:
                realNum[correct] = nums[i]
            else:
                return nums[i]

                

        