class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        row = len(image)
        colom = len(image[0])
        for i in range(row):
            new_row = []
            for j in range(colom-1,-1,-1):
                new_row.append(image[i][j])
            res.append(new_row)
        for i in range(row):
            for j in range(colom):
                if res[i][j] == 0:
                    res[i][j] = 1
                elif res[i][j] == 1:
                    res[i][j] = 0
        return res



        