class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            next_result = []
            count = 1
            for i in range(1, len(result) + 1):
                if i < len(result) and result[i] == result[i - 1]:
                    count += 1
                else:
                    next_result.append(str(count))
                    next_result.append(result[i - 1])
                    count = 1
            result = ''.join(next_result)
        return result