class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        

        ans = ""
        if num1 == "0" or num2 == "0":
            return "0"
        result = [0]* (len(num1) + len(num2))
        i = len(num1) - 1
        while i >= 0:
                j =len(num2) - 1
                while j >= 0:
                    digit1 = ord(num1[i]) - ord('0')
                    digit2 = ord(num2[j]) - ord('0')
                    multiply = digit1 * digit2
                    position = i + j + 1
                    
                    total = result[position] + multiply
                    result[position] = total % 10
                    result[position - 1] += total // 10
                    j -= 1
                i -= 1
        
        started = False
        for digit in result:
            if digit != 0:
                started = True
            if started:
                ans += str(digit)
        return ans