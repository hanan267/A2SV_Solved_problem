class Solution:
    def climbStairs(self, n: int) -> int:

        store = {}
        def dp(init):

            if init > n:
                return 0
            if init == n:
                return 1
            
            if init not in store:
                store[init] = dp(init+1) + dp(init+2)
            return store[init]
        return dp(0)


        