class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        
        last = {}


        for i in range(len(s)):
            last[s[i]] = i

        stack = []
        seen = set()


        for i in range(len(s)):
            ch = s[i]
            if ch in seen:
                continue
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                old = stack.pop()
                seen.remove(old)

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)
