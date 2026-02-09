class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        joined = "".join(map(str,nums))
        return list(map(int,joined))
        