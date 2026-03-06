class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       
        prefSum = {0:1}
        total = 0
        res = 0
        for i in range(len(nums)):
                total += nums[i]
                diff = total-k

                res += prefSum.get(diff, 0)
                prefSum[total] = prefSum.get(total, 0) + 1
        return res