class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
       
        ops = 0
        maax = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            x = nums[i]
            if x <= maax:
               maax = x
               continue

            k = (x + maax - 1) // maax
            ops += k - 1
            maax = x // k

        return ops
        