class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # brute force approach
          # iterate over the first char
          # as going check if that specific char exists in the second s
          # if exist delete from the second 
          # if not return false 
       #return Counter(s) == Counter(t)
       # optimized solution
         # create a counter that stores the count of the strings
         # compare it

        # def counter(s):
        #     count = {}
        #     for char in s:
        #         if char in count:
        #             count[char] += 1
        #         else:
        #             count[char] = 1
        #     # return count

        return Counter(s) == Counter(t)
        

        