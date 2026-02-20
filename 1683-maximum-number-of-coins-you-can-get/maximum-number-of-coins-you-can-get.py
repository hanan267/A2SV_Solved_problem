class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        bob = n // 3
        piles.sort()
        # print(piles)
        # print(piles[0:bob])
        my_piles = 0
        for i in range(bob, n, 2):
            my_piles += piles[i]
        
        return (my_piles)

        
