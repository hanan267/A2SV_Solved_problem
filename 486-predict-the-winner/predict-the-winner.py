class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        
        def winner(p1, p2):

            if p1 == p2:
                return nums[p1]
            myscore1 = nums[p1]- winner(p1+1, p2)
            myscore2 = nums[p2] - winner(p1, p2-1)
            return max(myscore1, myscore2)
        return True if winner(0, len(nums)-1) >= 0 else False


            

            

        