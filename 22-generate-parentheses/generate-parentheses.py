class Solution:
    def generateParenthesis(self, n: int):

        res = []

        def backTrack(curr, open, close):

            if len(curr) == 2 * n:
                res.append(curr)
                return
            
            if open < n:
                backTrack(curr + "(", open+1, close)
            
            if close < open:
                backTrack(curr + ")", open, close+1)
        
        backTrack("", 0, 0)
        return res
       