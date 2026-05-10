class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
         
        n = len(heights)
        diffHeap = []
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            
            bricks -= diff
            heapq.heappush(diffHeap, -diff)
            
            if bricks < 0:
                if ladders == 0:
                    return i
                
                bricks += -heapq.heappop(diffHeap)
                ladders -= 1
        return n - 1


            