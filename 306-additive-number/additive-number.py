class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        def add_strings(a, b):
            res = []
            carry = 0
            i, j = len(a) - 1, len(b) - 1
            while i >= 0 or j >= 0 or carry:
                x = int(a[i]) if i >= 0 else 0
                y = int(b[j]) if j >= 0 else 0
                s = x + y + carry
                res.append(str(s % 10))
                carry = s // 10
                i -= 1
                j -= 1
            return ''.join(res[::-1])
        for i in range(1, n):
            for j in range(i + 1, n):
                a = num[:i]
                b = num[i:j]              
                if (a[0] == '0' and len(a) > 1) or (b[0] == '0' and len(b) > 1):
                    continue
                k = j
                while k < n:
                    c = add_strings(a, b)
                    if not num.startswith(c, k):
                        break
                    k += len(c)
                    a, b = b, c
                if k == n:
                    return True
        return False