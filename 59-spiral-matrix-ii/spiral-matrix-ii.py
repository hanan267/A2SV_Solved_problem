class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        a = [[0]*n for i in range(n)]
        t = 0
        b = n - 1
        l = 0

        r = n- 1
        x = 1
        while t <= b and l <= r:
            for j in range(l, r + 1):
                a[t][j] = x
                x += 1
            t += 1
            for i in range(t, b + 1):
                a[i][r] = x
                x += 1
            r -= 1
            if t <= b:
                for j in range(r, l - 1, -1):
                    a[b][j] = x
                    x += 1
                b -= 1
            if l <= r:
                for i in range(b, t - 1, -1):
                    a[i][l] = x
                    x += 1
                l += 1
        return a