class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        brackets = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        
        if len(s) == 1:
            return False
            
        for bracket in s:
            if bracket not in brackets:
                stack.append(bracket)
            elif bracket in brackets and not stack:
                return False
            elif stack and brackets[bracket] != stack[-1]:
                return False
            elif stack:
                stack.pop()
            
        return not stack











        