class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        def flip(j):
            for i in range(j//2+1):
                arr[i], arr[j-i] = arr[j-i], arr[i]
        for i in range(len(arr)-1, 0, -1):
            for j in range(0, i+1):
                if arr[j] == i+1:
                    flip(j)
                    res.append(j+1)
            flip(i)
            res.append(i+1)
        return res



