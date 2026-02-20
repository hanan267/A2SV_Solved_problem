class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n-1,1, -1):
            if nums[i-1]+nums[i-2] > nums[i]:
                return (nums[i]+nums[i-1]+nums[i-2])
                break
        return 0
          
            

    