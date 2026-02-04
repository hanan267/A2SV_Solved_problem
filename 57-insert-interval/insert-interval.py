class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

       # try to overlap the two new intervals
          # make two pointers 
          # compare the start of new interval with start and end of intervals
          # if they are inbetween temp overlap
          # start another loop
          # do the preveious kind of overlap 


          # overlap intervals and newIntervals
        # if intervals == []:
        #     return [newInterval]
        # overlaped1 = [intervals[0]]
        # used = 1
        # # for start, end in intervals[0:]:
        # #     lastend = overlaped1[-1][1]

        # #     if (newInterval[0] <= lastend) and (used == 1):
        # #         overlaped1[-1][1] = max(newInterval[1], lastend)
        # #         used -= 1
        # #     else:
        # #         overlaped1.append([start, end])
        #     print(overlaped1)
        overlaped1 = []

        # for i in range(len(intervals)):
        #     start, end = intervals[i]
        #     if start >= newInterval[0]:
        #         overlaped1 = intervals[:i-1] + [newInterval] + intervals[i-1:]
        
        intervals.append(newInterval)
        intervals.sort()
        overlaped1 = intervals
        overlaped2 = [overlaped1[0]]

            # overlap overlaped1
        for start, end in overlaped1[1:]:
            latestEnd = overlaped2[-1][1]

            if start <= latestEnd:
                overlaped2[-1][1] = max(latestEnd, end)
            else:
                overlaped2.append([start, end])
        return overlaped2





        
        