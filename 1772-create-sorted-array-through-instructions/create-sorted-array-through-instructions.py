class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i
    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        MAXV = 100000
        bit = BIT(MAXV)
        total = 0
        cost = 0
        for x in instructions:
            less = bit.query(x - 1)
            greater = total - bit.query(x)
            cost += min(less, greater)
            cost %= MOD
            bit.update(x, 1)
            total += 1
        return cost