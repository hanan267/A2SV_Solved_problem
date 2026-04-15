class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()

        def feasible(minDis):

            ball = 1
            ball_place = position[0]

            for i in range(1, len(position)):
                if position[i] - ball_place >= minDis:
                    ball_place = position[i]
                    ball += 1
                if ball == m:
                    return True
            return False

        left, right = 0, position[-1] - position[0]

        firstTrueIdx = -1

        while left <= right:
            mid = (left+right) // 2
            if not feasible(mid):
                firstTrueIdx = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if firstTrueIdx == -1:
            return position[-1] - position[0]
        else:
            return firstTrueIdx - 1
        