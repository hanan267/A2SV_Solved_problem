class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        n = len(nums)
        dp = [1]*n
        prev = [-1]*n

        mx = 1
        idx = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > mx:
                mx = dp[i]
                idx = i

        ans = []
        while idx != -1:
            ans.append(nums[idx])
            idx = prev[idx]
        return ans[::-1]