class Solution:
    def minOperations(self, nums: List[int]) -> int:

        # flipped = [1 if num == 0 else 0 for num in nums]
        # print(flipped)

        # flip = False
          
        oper = 0
        for i in range(0,len(nums)-2):
            if nums[i] == 0:
                nums[i] = 1
                if nums[i+1] == 0:
                    nums[i+1] = 1
                else:
                    nums[i+1] = 0
                if nums[i+2] == 0:
                    nums[i+2] = 1
                else:
                    nums[i+2] = 0
                oper += 1
            # print(nums)
        
        for i in range(len(nums)):
            if nums[i] == 0:
                return -1
        return oper


        
        
        