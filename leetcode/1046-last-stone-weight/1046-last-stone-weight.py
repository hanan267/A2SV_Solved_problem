class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-1 * n for n in stones]
        heapq.heapify(stones)
        print(stones, heapq)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first < second:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return -1 * stones[0]

        