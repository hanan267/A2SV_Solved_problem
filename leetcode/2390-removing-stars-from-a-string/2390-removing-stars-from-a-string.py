class Solution:
    def removeStars(self, s: str) -> str:

        stack = []
        
        
        for n in range(len(s)):
            if s[n] == "*" and stack:
                stack.pop()
            else:
                stack.append(s[n])
        return "".join(stack)

