class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ']':'[',
            '}':'{',
            ')':'('
        }

        for chars in s:
            if chars in brackets.values():
                stack.append(chars)
            elif chars in brackets.keys():
                if stack and stack[-1] == brackets[chars]:
                    stack.pop()
                else:
                    return False 
        return len(stack) == 0


       














        