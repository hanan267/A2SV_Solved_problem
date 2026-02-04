class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        #   # brute force approach
        # # iterate over from 0-n
        # # check if those numbers are in the array
        # # return the one tha does not exist

        # for i in range(len(nums)+1): #  O(n),
        #     if i in nums: # O(n)
        #         continue
        #     return i

        #  #space complexity O(1)
        #  # time complextiy O(n) x O(n) = O(n^2) 

           # other solution
        # sort the array
        # iterate from 0-n
        # check if the corresponing indesx is equal with the array element
        # if not return index
        
        # nums.sort() # O(n log n)
        # n = len(nums)
        # for i in range(n): #O(n)
            
        #     if i != nums[i]:
        #         return i
        # return n

        # # time complexity O(nlogn)
        # # space complexity O(1)

             # optimized solution

        # res = len(nums)
        # for i in range(len(nums)):
        #     res += (i - nums[i])
        # return res

# iterate in the range 0-len(nums)+1
# as going check if any index is missing from the array
# return it
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        














        