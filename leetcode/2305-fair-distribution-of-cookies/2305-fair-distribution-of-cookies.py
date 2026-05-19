class Solution:
    def distributeCookies(self, cookies, k):
        children = [0] * k
        res = float('inf')
        def backtrack(idx):
            nonlocal res
            if idx == len(cookies):
                res = min(res, max(children))
                return
            for i in range(k):
                children[i] += cookies[idx]
                if max(children) < res:
                    backtrack(idx + 1)
                children[i] -= cookies[idx]
                if children[i] == 0:
                    break
        backtrack(0)
        return res