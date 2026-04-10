class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        # insertion sort 

        for i in range(1,len(names)):
            key1 = names[i]
            key = heights[i]
            j = i - 1

            while j >= 0 and heights[j] < key:
                heights[j+1] = heights[j]
                names[j+1] = names[j]
                j -= 1
            heights[j+1] = key
            names[j+1] = key1
        return names


        # bubble sort
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
        




        