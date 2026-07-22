class Solution:
   
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        numDigit = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        n = len(digits)

        def backTracking(idx, curr):
            if len(curr) == n:
                res.append(curr)
                return 

            letters = numDigit[digits[idx]]

            for char in letters:
                backTracking(idx+1, curr+char)
            
        
        backTracking(0, "")        
        return res
        
        