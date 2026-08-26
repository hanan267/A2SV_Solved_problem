class Solution:
    def convert(self, s: str, numRows: int) -> str:
        

        if numRows == 1 or numRows >= len(s):
            return s
        rows = ['' for i in range(numRows)]
        current = 0
        direction = 1

        for character in s:
            rows[current] += character
            if current == 0:
                direction = 1
            elif current == numRows - 1:
                direction = -1
            current += direction

        return ''.join(rows)