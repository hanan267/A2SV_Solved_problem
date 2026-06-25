class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = 0
        rest = 0
        for p in prices[1:]:
            oldhold = hold
            oldsold = sold
            oldrest = rest
            hold = max(oldhold, oldrest - p)
            sold = oldhold + p
            rest = max(oldrest, oldsold)
        return max(sold, rest)