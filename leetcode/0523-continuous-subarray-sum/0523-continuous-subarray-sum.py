class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        remainder = { 0:-1 }

        
        pref = 0
        for i in range(len(nums)):
            pref += nums[i]
            r = pref%k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
    
            
        return False




        # remainder = {0:-1}
        # total = 0

        # for i, n in enumerate(nums):
        #     total += n
        #     r = total % k
        #     if r not in remainder:
        #         remainder[r] = i
        #     elif i-remainder[r] > 1:
        #         return True
        # return False


        
        