class Solution:
    def myAtoi(self, s: str) -> int:
        
        i = 0
        sign = 1
        num = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        num *= sign
        if num > 2147483647:
            return 2147483647
        if num < -2147483648:
            return -2147483648
        return num