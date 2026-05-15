class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        Set = set()
        n = len(nums)
        nums.sort()
        def backTrack(start, temp):
            if start >= n:
                Set.add(tuple(temp))
                return
            temp.append(nums[start])
            backTrack(start+1, temp)
            temp.pop()
            backTrack(start+1, temp)
        backTrack(0, [])
        return list(Set)

        