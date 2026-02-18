class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # height_map = {}
        # for i in range(len(heights)):
        #     height_map[heights[i]] = names[i]
        # for i in range(len(names)-1):
        #     if heights[i] < heights[i+1]:
        #         heights[i], heights[i+1] =heights[i+1], heights[i]
        #         names[i], names[i+1] = names[i+1], names[i]
        # return (names)
        n = len(heights)
        for i in range(n):
            for j in range(i+1):
                if heights[j] < heights[i]:
                    heights[j], heights[i] = heights[i], heights[j]
                    names[j], names[i] = names[i], names[j]
        return names



        