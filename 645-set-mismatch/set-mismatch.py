class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
       
        n = len(nums)
        i = 0
        res = []

        while i < n:
                correct = nums[i] - 1
                if nums[correct] != nums[i]:
                    nums[i], nums[correct] = nums[correct], nums[i]
                else:
                    i += 1

        for i in range(n):
            if i+1 != nums[i]:
                return [nums[i],i+1]




        


        