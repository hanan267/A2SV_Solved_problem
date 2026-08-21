class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def check(a, b):
            i = 0
            for c in b:
                if i < len(a) and a[i] == c:
                    i += 1
            return i == len(a)
        ans = -1
        for i in range(len(strs)):
            ok = True

            for j in range(len(strs)):
                if i != j and check(strs[i], strs[j]):
                    ok = False
                    break
            if ok:
                ans = max(ans, len(strs[i]))
        return ans