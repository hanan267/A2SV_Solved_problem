class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        if (mat == target):
            return True
        n = len(mat)
        res = []
        for i in range(4):
            res = [[0]*n for col in range(n)]
            print(res)

            for row in range(len(mat[0])):
                for colom in range(len(mat)):
                    res[row][colom] = mat[colom][n-1-row]
            if res == target:
                return True

            mat = res
        return False
            