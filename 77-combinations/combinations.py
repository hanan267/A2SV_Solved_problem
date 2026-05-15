class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        def dfs(start, temp):
            if len(temp) == k:
                res.append(temp[:])
                return
            # pruning
            if start > n:
                return
            
            temp.append(start)
            dfs(start+1, temp)
            temp.pop()
            dfs(start+1, temp)
        
        dfs(1, [])
        return res

        
        