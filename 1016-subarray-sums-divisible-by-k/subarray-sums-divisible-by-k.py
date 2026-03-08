class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        remainder = { 0:1 }

        Sum = 0
        res = 0
        for i in range(len(nums)):
            Sum += nums[i]
            r = Sum % k
            if r in remainder:
                res += remainder.get(r)
                remainder[r] += 1
            else:
                remainder[r] = 1
        return res
                
             




        