class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # counts = defaultdict(int)
        # threshold = len(nums)//3
        # res = set()

        # for num in nums:
        #     counts[num] += 1
        #     if counts[num] > threshold:
        #         res.add(num)
        # return list(res)
        
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
            if len(count) <= 2:
                continue
            new_count = defaultdict(int)
            for n, c in count.items():
                if c > 1:
                    new_count[n] = c - 1
            count=new_count

        res = []
        for num in count:
            if nums.count(num) > len(nums)//3:
                res.append(num)
        return res
        
