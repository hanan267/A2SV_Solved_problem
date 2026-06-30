class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        store = set()
        n = len(s)
        res = 0
        left = 0
        for right in range(n):
            while right > left and s[right] in store:
                store.remove(s[left])
                left += 1
            store.add(s[right])
            res = max(res, right - left + 1)
        return res

            
            

          




















            
       
       

       



        