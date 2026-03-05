class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def function(nums, k):
            left = 0
           
            count = 0
            
            w = defaultdict(int)
            for i in range(len(nums)):
            
                w[nums[i]] += 1
                while len(w) > k and i > left:
                    w[nums[left]] -= 1
                    if w[nums[left]] == 0:
                        del w[nums[left]]
                    left += 1
                
                if len(w) <= k:
                    count += i-left+1
                
            return count
        res = function(nums, k)-function(nums, k-1)
        return res
        
        