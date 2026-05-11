class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
       values = set(nums)
       i = 0
       while True:
            if i+1 not in values:
                return i+1
            i += 1

        