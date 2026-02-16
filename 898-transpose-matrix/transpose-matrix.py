class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    #    res = []
    #    column_len = len(matrix[0])
    #    row_len= len(matrix)
    #    for i in range(column_len):
    #         new_row = []
    #         for j in range(row_len):
    #            new_row.append(matrix[j][i])
    #         res.append(new_row)
    #    return res

         return [list(row) for row in zip(*matrix)]


        
       
            
        