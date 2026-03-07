class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        mod = 10**9+7
        count = [0]*(len(nums)+1)
        for start, end in requests[0:]:
            count[start] += 1
            count[end+1] -= 1
        

        pref = 0
        for i in range(len(count)):
            pref += count[i]
            count[i] = pref

        nums.sort(reverse=True)
        count.sort(reverse=True)
       
        maxSum = 0
        for i in range(len(nums)):
            maxSum += count[i]*nums[i]
        return maxSum%mod

        
        