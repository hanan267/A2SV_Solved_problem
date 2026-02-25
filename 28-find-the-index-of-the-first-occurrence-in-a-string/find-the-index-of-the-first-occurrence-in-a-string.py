class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if haystack == needle:
            return 0
        for i in range(n):
            if haystack[i] == needle[0] and i+m <= n:
                sub  = haystack[i:m+i]
                if sub == needle:
                    
                    return i

        return -1
