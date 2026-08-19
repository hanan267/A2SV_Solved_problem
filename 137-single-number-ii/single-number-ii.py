class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

        p2 = 2
        nums.sort()
        n = len(nums)
        # print(nums)
        i = 0
        while i < n:
            if p2 < n - 1 and nums[i] != nums[p2]:
                # print(nums[i], nums[p2])
                return nums[i]
            p2 += 3
            i += 3
        return nums[n-1]

