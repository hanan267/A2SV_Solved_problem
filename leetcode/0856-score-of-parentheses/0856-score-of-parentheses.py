class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []
        score = 0
        for par in s:
            if par == "(":
                stack.append([par, 0])
                
            
            elif par == ")":
                
                _ , vl = stack.pop()
                # print(vl)
                if stack:
                    stack[-1][1] += max(2 * vl,1)
                else:
                    score += max(2 * vl,1)
                
                
        return score
            


            

        