class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        pointer = k
        res = []
        # print(c)
        # print(c.items())

        for key, value in sorted(c.items(), key=lambda a:a[1], reverse=True):
            if pointer > 0:
                res.append(key)
                pointer -= 1
                # print(c)
        return res
            

            

        
