class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        c = Counter(words)
        heap = [(-1*count, key) for key, count in c.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
        