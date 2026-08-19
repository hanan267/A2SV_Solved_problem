class Solution:
    def nthUglyNumber(self, n: int) -> int:

        res = [1]
        p2, p3, p5 = 0, 0, 0

        for i in range(1, n):
            num = min(
                res[p2] * 2, res[p3] * 3, res[p5] * 5
            )
            res.append(num)

            if num == res[p2] * 2:
                p2 += 1
            if num == res[p3] * 3:
                p3 += 1
            if num == res[p5] * 5:
                p5 += 1

        return res[n - 1]
        