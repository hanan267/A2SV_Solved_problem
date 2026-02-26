class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
           # Brute force approach
        # counter = 0
       
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)+1):
        #         substring = s[i: j]

        #         if len(set(substring)) == len(substring):
        #             counter = max(len(substring), counter)

         ### using sliding window and hash table

        #  n = len(s)
        #  sett = set()
        #  count = 0
        #  max_len = 0
        #  left = 0

        #  for right in range(n):
        #     while s[right] in sett:
        #         sett.remove(s[left])
        #         left += 1
        #     window = (right - left) + 1
        #     max_len = max(window, max_len)
        #     sett.add(s[right])
        #  return max_len

        n = len(s)
        window = set()
        length = 0
        maxLen = 0
        left, right = 0, 0
        while right < n:
            if s[right] not in window:
                window.add(s[right])
                right += 1
                length += 1
                maxLen = max(length, maxLen)
            else:
                while s[right] in window:
                    window.remove(s[left])
                    left += 1
                    length -= 1
        return maxLen





















            
       
       

       



        