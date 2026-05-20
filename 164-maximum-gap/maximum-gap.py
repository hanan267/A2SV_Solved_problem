class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        ordered = sorted(nums)

        diff = 0
        n = len(nums)
        for i in range(1, n):
            diff = max(ordered[i] - ordered[i-1], diff)
        return diff
        