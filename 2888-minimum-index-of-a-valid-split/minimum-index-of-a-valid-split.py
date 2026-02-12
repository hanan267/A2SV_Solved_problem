class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)
        leftcount = defaultdict(int)
        # print(nums)
        for i in range(len(nums)):
            # sub1 = nums[0:i+1]
            leftcount[nums[i]] += 1
            # print(nums[i], sub1,leftcount[nums[i]], (i+1)/2)
            if leftcount[nums[i]] > (i+1)/2:
                diff = count[nums[i]] - leftcount[nums[i]]
                # print(diff, (n-i-1)/2)
                if diff > (n-i-1)/2:
                    return i
        return -1

