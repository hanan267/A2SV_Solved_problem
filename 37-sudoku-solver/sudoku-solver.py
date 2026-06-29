class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        emptyCells = []
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    boxIdx = (r // 3) * 3 + (c // 3)
                    boxes[boxIdx].add(val)
                else:
                    emptyCells.append((r, c))
        def backtrack(cellIdx: int) -> bool:
                if cellIdx == len(emptyCells):
                    return True
                r, c = emptyCells[cellIdx]
                boxIdx = (r // 3) * 3 + (c // 3)
                for digit in map(str, range(1, 10)):
                    if digit not in rows[r] and digit not in cols[c] and digit not in boxes[boxIdx]:
                        board[r][c] = digit
                        rows[r].add(digit)
                        cols[c].add(digit)
                        boxes[boxIdx].add(digit)
                        if backtrack(cellIdx + 1):
                            return True
                        board[r][c] = '.'
                        rows[r].remove(digit)
                        cols[c].remove(digit)
                        boxes[boxIdx].remove(digit)
                return False
        backtrack(0)
            