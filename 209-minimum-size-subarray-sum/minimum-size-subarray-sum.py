class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        # store = defaultdict(int)
        n = len(nums)
        Sum = 0
        temp = 0
        res = n
        total = sum(nums)
        if total < target:
            return 0

        for right in range(n):
            # store[nums[right]] += 1
            Sum += nums[right]

            while Sum >= target:
                temp = right - left + 1
                res = min(res, temp)
                # print(left, right, temp)
                # store[nums[left]] -= 1
                # if store[nums[left]] == 0:
                #     del store[nums[left]]
                Sum -= nums[left]
                left += 1
        return res
           

            


            