class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
       
        n = len(nums)
        sortednums = sorted(nums)
        
       
        mid = (n + 1) // 2
        small = sortednums[:mid]    
        large = sortednums[mid:]    
        
        small = small[::-1]
        large = large[::-1]
        nums[::2] = small
        nums[1::2] = large



        
        