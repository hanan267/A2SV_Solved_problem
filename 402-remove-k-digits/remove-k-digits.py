class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        digits = []

        for curr in num:
            while k > 0 and digits and digits[-1] > curr:
                digits.pop()
                k -= 1

            digits.append(curr)
        while k > 0:
            digits.pop()
            k -= 1

        res = ''.join(digits).lstrip('0')

        if res == '':
            return '0'

        return res