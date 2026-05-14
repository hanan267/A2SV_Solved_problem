class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        n = len(wage)
        info = []
        
        for i in range(n):
            prop = wage[i] / quality[i]
            info.append([prop, quality[i]])
            
        info.sort()
        maxheap = []
        totalquality = 0
        for i in range(k):
            heappush(maxheap, -info[i][1])
            totalquality += info[i][1]
        
        res = totalquality * info[k - 1][0]
        for i in range(k, n):
            # fire the worker
            removedquality = -heappop(maxheap)
            totalquality -= removedquality

            # hire the new guy
            heappush(maxheap, -info[i][1])
            totalquality += info[i][1]

            # total wage
            tempres = totalquality * info[i][0]
            res = min(res, tempres)
        
        return res
       

        
        