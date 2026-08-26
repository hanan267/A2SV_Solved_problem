class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        store = {}
        
        for a in nums1:
            for b in nums2:
                s = a + b
                store[s] = store.get(s, 0) + 1
        ans = 0
        for c in nums3:
            for d in nums4:
                ans += store.get(-(c + d), 0)
        return ans