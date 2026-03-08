class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        remainder = {0:1}

        total = 0
        res = 0
        for i in range(len(nums)):
            total += nums[i]
            diff = total-k

            if diff in remainder:
                res += remainder[diff]
            remainder[total] = remainder.get(total, 0) + 1
        return res

            
































       
        # prefSum = {0:1}
        # total = 0
        # res = 0
        # for i in range(len(nums)):
        #         total += nums[i]
        #         diff = total-k

        #         res += prefSum.get(diff, 0)
        #         prefSum[total] = prefSum.get(total, 0) + 1
        # return res