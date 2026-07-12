class Solution:
    def judgeCircle(self, moves: str) -> bool:

        res = [0, 0]

        for move in moves:
            if move == "U":
                res[1] += 1
            elif move == "D":
                res[1] -= 1
            elif move == "L":
                res[0] -= 1
            else:
                res[0] += 1
        return True if res == [0, 0] else False

            
        