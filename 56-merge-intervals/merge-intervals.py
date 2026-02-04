class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key=lambda i:i[0])
        # output  = [intervals[0]]

        # for start, end in intervals[1:]:
        #     lastend = output[-1][1]

        #     if start <= lastend:
        #         output[-1][1] = max(lastend, end)
        #     else:
        #         output.append([start, end])
        # return output


        # intervals.sort(key=lambda i:i[0])
        # output = [intervals[0]]


        # for start, end in intervals[1:]:
        #     lastend = output[-1][1]

        #     if start <= lastend:
        #         output[-1][1] = max(lastend, end)
        #     else:
        #         output.append([start, end])
        # return output


# iterate over the given array
# compare the end of the first with the start of the second
# if the end is greater or equal overlap
# if not just add that specific array to the new one

        intervals.sort(key=lambda i:i[0])
        overlaped = [intervals[0]]

        for start, end in intervals[1:]:
            latestEnd = overlaped[-1][1]

            if start <= latestEnd:
                overlaped[-1][1] = max(latestEnd, end)
            else:
                overlaped.append([start, end])
        return overlaped













        