class Solution:
    def countGoodNumbers(self, n: int) -> int:

            MOD = 10**9+7
            odd = n // 2
            even = (n+1) // 2

            def power(b, p):
                if p == 0:
                    return 1
                half = power(b, p//2) 

                if p % 2 == 0:
                    return (half * half)  % (MOD)
                else:
                    return (half * half * b)  % (MOD)

            return (power(5, even) * power(4, odd)) % (MOD)

       