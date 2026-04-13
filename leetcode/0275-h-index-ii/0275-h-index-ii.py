class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = len(citations)
        count = [0]*(n+1)
        for idx, num in enumerate(citations):
            count[min(num, n)] += 1

        h = n
        paper = count[n]

        while  paper < h:
            h -= 1
            paper += count[h]
        return h




        