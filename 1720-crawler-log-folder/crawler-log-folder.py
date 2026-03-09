class Solution:
    def minOperations(self, logs: List[str]) -> int:

        count = 0
        for char in logs:
                if char == "../" and count > 0:
                    count -= 1
                elif char == "./" or (char == "../" and count == 0):
                    continue
                else:
                    count += 1
        return max(0, count)
            
