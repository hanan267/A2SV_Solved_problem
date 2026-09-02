class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        n = len(piles)
        bob = n // 3
        piles.sort()
        # print(piles)
        # print(piles[0:bob])
        mypiles = 0
        for i in range(bob, n, 2):
            mypiles += piles[i]
        
        return mypiles

        