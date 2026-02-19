class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # # optimized 
        #     Sorted = sorted(nums)  # O(nlogn) , O(n)
        #     map = {}  # O(1), O(n)
        #     for i in range(len(nums)): # O(n), O(1)
        #         if Sorted[i] not in map:
        #             map[Sorted[i]] = i
        #     for i in range(len(nums)): # O(n), O(1)
        #         nums[i] = map[nums[i]]
        #     return nums

        #     # time  O(nlogn+n+n) = O(nlogn)
        #     #  space = O(2n) = O(n)

        # brute force approach
             # iterate from 0 - n/ lenth
             # iterate again
             # as you pass check if elements in the secod are less than the first one # count 
        # count = 0
        # n = len(nums)
        # arr = []
        # for i in range(n): # O(n)
        #     for j in range(n):# O(n)
        #         if nums[i] > nums[j]:
        #             count += 1
        #     arr.append(count)
        #     count = 0
           
        # return arr

        # # time complexity O(n^2)
        # # space complexity O(n)

        # naive
           # step 1: sort 
           # step 2: find the index in the sorted array of original array
           # step 2 : replace it with index+1 of original array
             
        # Sorted = sorted(nums) #O(nlogn)
        # for i in range(len(nums)):#O(n)
        #     nums[i] = Sorted.index(nums[i]) # O(n)
                
        # return nums

        # time complexity: O(n^2)
        # space complexity: O(n)
        
        Sorted = sorted(nums)

        n = len(nums)
        res = []
        small_nums = {}
        for i in range(n):
           if Sorted[i] not in small_nums:
            small_nums[Sorted[i]] = i
        # print(small_nums)
        return [small_nums[nums[i]] for i in range(n)]
        

            

















        
        