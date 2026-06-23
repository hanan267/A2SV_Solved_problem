class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        c = 0
        h = -prices[0]
        for p in prices[1:]:
            pc = c
            c = max(c, h + p - fee)
            h = max(h, pc - p)
        return c