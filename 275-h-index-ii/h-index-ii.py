class Solution:
    def hIndex(self, citations: List[int]) -> int:


        n = len(citations)
        if n == 0:
            return 0
        
        firstTrueIdx = -1
        left, right = 0, n-1

        while left <= right:

            mid = (left+right) // 2
            if citations[mid] >= n - mid:
                firstTrueIdx = mid 
                right = mid - 1
            else:
                left = mid + 1
        return 0 if firstTrueIdx == -1 else n - firstTrueIdx

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




        