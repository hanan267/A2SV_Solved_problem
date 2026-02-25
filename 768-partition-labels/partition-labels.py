class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lastIndex = {}
        
        for idx, value in enumerate(s):
            lastIndex[value] = idx

        partition, end = 0, 0
        res = []
        for idx, value in enumerate(s):
            partition += 1
            end = max(end, lastIndex[value])

            if idx == end:
                res.append(partition)
                partition = 0
        return res
            
       
            
        