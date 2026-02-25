class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # left = 0
        # right = int(sqrt(c))
        # while (left <= right):
        #    sumSquare = left*left + right*right
        #    if sumSquare == c:
        #       return True
        #    elif sumSquare > c:
        #        right -= 1
        #    else:
        #       left += 1
        # return False

        left, right = 0, int(sqrt(c))
        while left<=right:
            # print(left, right)
            if (left)**2 + (right)**2  < c :
                left += 1
            elif (left)**2 + (right)**2 == c:
                return True
            elif (left)**2 + (right)**2 > c:
                right -= 1
        return False

        