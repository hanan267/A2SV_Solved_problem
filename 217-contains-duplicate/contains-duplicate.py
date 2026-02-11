class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # # create a set
        # # itrate 0-n
        # # if char exist in set return true
        # # else put char to the set
        # # return false at the end

        unique = set()
        for char in nums:
            if char in unique:
                return True
            else:
                unique.add(char)
        return False

        # space-complexity O(n)
        # time-complexity O(n)

        #         # brute force approach
        # # create an array
        # appered_elements = [] 
        # # iterate over
        # for elements in nums:
        #     # as iterating check if the value exists in the array
        #     if elements in appered_elements:    
        #         # if exist return true
        #         return True
        #     # else put it in to the array
        #     else:
        #         appered_elements.append(elements)
        # # return false at the end
        # return False

        # # O(n)- space
        # # O(n^2) - time
          



        