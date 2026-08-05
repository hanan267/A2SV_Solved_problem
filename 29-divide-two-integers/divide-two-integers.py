class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        limit = 2**31

        if dividend == -limit and divisor == -1:
            return limit - 1
        sign = -1 if (dividend < 0) != (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0

        while dividend >= divisor:
            curr = divisor
            count = 1

            while dividend >= (curr << 1):
                curr <<= 1
                count <<= 1

            dividend -= curr
            ans += count

        return ans if sign > 0 else -ans