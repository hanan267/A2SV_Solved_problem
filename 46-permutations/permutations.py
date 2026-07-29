class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res, temp = [], []

        n = len(nums)

        def backtracking():
            if len(temp) == n:
                res.append(temp[:])
                return 
            
            for num in nums:
                if num not in temp:
                    temp.append(num)
                    backtracking()
                    temp.pop()
        backtracking()
        return res

        
    