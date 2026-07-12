class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        bCount = Counter(blocks[:k])
        minRecolor = bCount["W"]
        # print(bCount)
        
        left = 0
        for right in range(k,len(blocks)):

            bCount[blocks[right]] += 1
            bCount[blocks[left]] -= 1
            # print(blocks[left])
            left += 1
            # print(right, bCount)
            minRecolor = min(minRecolor, bCount["W"])

        return minRecolor
            



        