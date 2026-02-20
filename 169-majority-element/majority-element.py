class Solution:
    def majorityElement(self, nums: List[int]) -> int:#
        # count = Counter(nums)
        # unique = set(nums)
        # n = len(nums)//2
        
        # for num in unique:
        #     if count[num] > n:
        #         return num

        res, count = 0, 0
        for num in nums:
            if count == 0:
                res = num
            if res == num:
                count += 1
            else:
                count -= 1
        return res

    
        