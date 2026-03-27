class Solution:
    def lastRemaining(self, n: int) -> int:
        def lastNum(b, e, d):

            if b == e:
                return b
            if ((e-b+d)//d) % 2 != 0:
                e -= d
            b += d
            d *= 2

            if e == b:
                return b
            if ((e-b+d)//d) % 2 != 0:
                b += d
            e -= d
            d *= 2
            return lastNum(b, e, d)
        
        return lastNum(1, n, 1)