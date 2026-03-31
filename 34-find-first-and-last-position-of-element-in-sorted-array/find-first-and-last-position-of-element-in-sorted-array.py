class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
       
        def findBegging(nums, target):
            low = 0
            high = len(nums)-1
            ans = -1
            while low <= high:
                mid = (low+high) // 2
                if nums[mid] == target:
                    ans = mid
                    high = mid - 1
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
            return ans

        def findLast(nums, target):
            low = 0
            high = len(nums)-1
            ans = -1
            while low <= high:
                mid = (low+high) // 2
                if nums[mid] == target:
                    ans = mid
                    low = mid + 1
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
            return ans
            
        left = findBegging(nums, target)
        right = findLast(nums, target)

        return [left, right]
        

                    