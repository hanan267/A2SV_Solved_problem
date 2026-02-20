class Solution:
    def majorityElement(self, nums: List[int]) -> int:#
        count = Counter(nums)
        unique = set(nums)
        n = len(nums)//2
        
        for num in unique:
            if count[num] > n:
                return num

    
        