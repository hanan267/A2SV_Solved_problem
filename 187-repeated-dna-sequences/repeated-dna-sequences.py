class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        
        seen = {s[0:10]:1}
        res = defaultdict(int)
        for i in range(1, len(s)):
            DNA = s[i:i+10]
            if DNA in seen:
                res[DNA] += 1
            else:
                seen[DNA] = 1
     
        
        ans =  [key for key, value in res.items()]
        
        return (ans)

        