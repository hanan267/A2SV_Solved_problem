class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        if maxDoubles == 0:
            return target - 1
        operation = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                operation += 1
            else:
                operation += 2
            maxDoubles -= 1
            target //= 2
        operation += target - 1
        return operation

        
