class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        elemnts = Counter(nums)
        res = []
        for key, value in elemnts.items():
            if value == 2:
                res.append(key)
        return res



        
        