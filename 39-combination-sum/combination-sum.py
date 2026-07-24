class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        temp = []
        n = len(candidates)

        def backTrack(i, curr):
            if curr == target:
                res.append(temp[:])
                return
            
            if curr > target or n == i:
                return 
            
            backTrack(i+1, curr)

            temp.append(candidates[i])

            backTrack(i, curr + candidates[i])
            temp.pop()

        backTrack(0, 0)
        return res

        