class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = len(citations)
        papercnt = [0] * (n+1)
        
        for num in citations:
            papercnt[min(num, n)] += 1
        h = n
        papers = papercnt[n]

        while papers < h:
            h -= 1
            papers += papercnt[h]
        return h                    
            