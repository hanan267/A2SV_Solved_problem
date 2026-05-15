class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        res = []
        n = len(nums)
        def backTrack(temp, visited):
            if len(temp) == n:
                res.append(temp[:])
                return
            
            for i in range(n):
                if visited[i]:
                    continue
                
                visited[i] = True
                temp.append(nums[i])

                backTrack(temp, visited)

                temp.pop()
                visited[i] = False


        backTrack([], [False]*n)
        return res


        