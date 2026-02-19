class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # height_map = {}
        # for i in range(len(heights)):
        #     height_map[heights[i]] = names[i]
            # buble sort
        # n = len(names)
        # for j in range(n):
        #     for i in range(n-j-1):
        #         if heights[i] < heights[i+1]:
        #             heights[i], heights[i+1] = heights[i+1], heights[i]
        #             names[i], names[i+1] = names[i+1], names[i]
        # return (names)
            # insertion sort
        # n = len(heights)
        # for i in range(n):
        #     for j in range(i+1):
        #         if heights[j] < heights[i]:
        #             heights[j], heights[i] = heights[i], heights[j]
        #             names[j], names[i] = names[i], names[j]
        # return names
        
        #   insertion sort
        
        n = len(names)
        for i in range(n):
            for j  in range(i, 0, -1):
                if heights[j] > heights[j-1]:
                    heights[j], heights[j-1] = heights[j-1], heights[j]
                    names[j], names[j-1] = names[j-1], names[j]

                
        return names

                # counting sort
        # n = len(heights)
        # big = max(heights)
        # count = [0]*big
        # # print(big)
        # for i in range(n):
        #     count[heights[i]-1] += 1
        # res = []
        # for i in range(len(count)):
        #     if count[i] != 0:
        #         for j in range(count[i]):
        #             res.append(i+1)
                
        # return res
        




        