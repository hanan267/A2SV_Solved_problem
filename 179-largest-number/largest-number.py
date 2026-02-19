from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # # Convert all numbers to strings
        # nums = list(map(str, nums))
        
        # # Comparator function
        # def compare(x, y):
        #     if x + y > y + x:
        #         return -1  # x should come first
        #     elif x + y < y + x:
        #         return 1   # y should come first
        #     else:
        #         return 0   # equal
        
        # # Sort with custom comparator
        # nums.sort(key=cmp_to_key(compare))
        
        # # Join the numbers into a single string
        # result = "".join(nums)
        
        # # Handle the case where all numbers are zeros
        # return "0" if result[0] == "0" else result


        nums = list(map(str, nums))

        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(compare))
        

        return "0" if nums[0] == "0" else "".join(nums)

    














































