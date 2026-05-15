class Solution:
   
    def letterCombinations(self, digits: str) -> List[str]:

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        if not digits:
            return
    
        res = []
        n = len(digits)
        def backTrack(start, temp):
            if len(temp) == n:
                res.append(temp)
                return
            
            
            for letter in phone_map[digits[start]]:
                temp += letter
                backTrack(start+1, temp)
                temp = temp[:-1]
        
        backTrack(0, "")
        return res





































































        # if not digits:
        #     return []

       

        # phone_map = {
        #     "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        #     "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        # }

        # result = []

        
        # def backtrack(index, current):
           
        #     if index == len(digits):
        #         result.append(current)
        #         return

            
        #     for letter in phone_map[digits[index]]:
        #         backtrack(index + 1, current + letter)

       
        # backtrack(0, "")
        # return result
