class Solution:
    def isPalindrome(self, s: str) -> bool:
       

       joined = "".join(char for char in s if char.isalnum())
       lowers = joined.lower()

       return lowers == lowers[::-1]
           




        