class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        
        single = 0
        double = 0

        for num in nums:
            if num / 10 >= 1:
                double += num
            else:
                single += num
        # print(single , double)
        return True if (single > double) or (double > single) else False