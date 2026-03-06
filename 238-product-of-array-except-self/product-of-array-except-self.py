class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        preff = [1]*n
        suff = [1]*n

        for i in range(1,n):
            preff[i] = preff[i-1]*nums[i-1]
        
        for j in range(n-2, -1, -1):
            suff[j] = suff[j+1]*nums[j+1]

        res = [0]*len(nums)
        for i in range(len(nums)):
            res[i] = preff[i]*suff[i]
        return res

        