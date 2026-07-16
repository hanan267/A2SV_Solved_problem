class Solution:
    def reverseString(self, s: List[str]) -> None:

        n = len(s)
        j =  n - 1
        
        for i in range(n):
            if i < j:
                s[i], s[j] = s[j], s[i]
                j -= 1
        return s

        
        