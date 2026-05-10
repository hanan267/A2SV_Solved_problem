class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        minHeap = [[num1 + nums2[0], i, 0] for i, num1 in enumerate(nums1[:k])]
        heapq.heapify(minHeap)
        res = []

        while k > 0 and minHeap:
            _, idx1, idx2 = heapq.heappop(minHeap)
            res.append([nums1[idx1], nums2[idx2]])
            k -= 1
            if idx2 + 1 < len(nums2):
                num1 = nums1[idx1] + nums2[idx2+1]
                heapq.heappush(minHeap, [num1, idx1, idx2 + 1])

        return res



        

        