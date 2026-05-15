class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        

        res = []
        n = len(nums)
        def dfs(start, temp):
            if len(temp) >= 2:
                res.append(temp[:])
            used = set()
            for i in range(start, n):
                if nums[i] in used:
                    continue
                
                if not temp or nums[i] >= temp[-1]:
                    used.add(nums[i])
                    temp.append(nums[i])
                    dfs(i+1, temp)
                    temp.pop()


          
        dfs(0, [])
        return res


        