class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast: # cycle exists
                break
        
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

        n = len(nums)
        realNum = [0]*(n-1)

        for i in range(n):
            correct = nums[i] - 1
          
            if realNum[correct] == 0:
                realNum[correct] = nums[i]
            else:
                return nums[i]

                

        