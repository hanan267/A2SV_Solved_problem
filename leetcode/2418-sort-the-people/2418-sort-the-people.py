class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n-1):
            for j in range(i+1, n):
                if heights[i] < heights[j]:
                    heights[i], heights[j] = heights[j], heights[i]
                    names[i], names[j] = names[j], names[i]
        return names

         # selection sort
        
        for i in range(n):
            for j in range(i+1, n):
               
                if heights[i] < heights[j]:
                    
                    names[i], names[j] = names[j], names[i]
                    heights[i], heights[j] = heights[j], heights[i]

        return names
        




        