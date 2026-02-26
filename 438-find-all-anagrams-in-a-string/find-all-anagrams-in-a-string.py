class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        c1 = Counter(p)
        w = defaultdict(int)
        
        if len(p) > len(s):
            return []

        for i in range(len(p)):
            w[s[i]] += 1
        
        res = []
        l = 0
        if w == c1:
            res.append(0)
        for i in range(len(p),len(s)):
            w[s[l]] -= 1
            w[s[i]] += 1
            if w[s[l]] == 0:
                del w[s[l]]
            l += 1
            if w == c1:
                res.append(l)
            
          
                
        return res
                
        