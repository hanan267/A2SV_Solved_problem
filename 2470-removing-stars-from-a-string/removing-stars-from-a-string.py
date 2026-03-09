class Solution:
    def removeStars(self, s: str) -> str:

        stack = []
        s = list(s)
        
        for n in range(len(s)):
            if s[n] == "*" and stack:
                stack.pop()
            else:
                stack.append(s[n])
        return "".join(stack)

