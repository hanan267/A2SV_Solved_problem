class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hash map
        # iterate char 0-n/ len arr
        # check if target - char exists in the hash map
        # if not put char, index pair to the hash
        # if exit return the current i and value of diff
        nums_store = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in nums_store:
                return [idx, nums_store[diff]]
            else:
                nums_store[num] = idx

        # time-comp O(n)
        # space O(n)