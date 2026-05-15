class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        

       
        chars = ["a", "b", "c"]
        res = []
        def happyString(temp):
            if len(temp) > n:
                return
            if len(temp) == n:
                res.append(temp)
            for char in chars:
                if temp and char == temp[-1]:
                    continue
                happyString(temp+char)
                
        happyString("")
        if k <= len(res):
            return res[k-1]
        else:
            return ""
       
