class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        l = -1
        r = -1
        mx = float('-inf')
        mn = float('inf')

        for i in range(n):
            if nums[i] < mx:
                r = i
            else:
                mx = nums[i]
        for i in range(n - 1, -1, -1):
            if nums[i] > mn:
                l = i
            else:
                mn = nums[i]
        if l == -1:
            return 0
        return r - l + 1