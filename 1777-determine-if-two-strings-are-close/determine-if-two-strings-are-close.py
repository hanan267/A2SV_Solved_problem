class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False
        count1 = dict(sorted(Counter(word1).items(), key=lambda x:-x[1]))
        count2 = dict(sorted(Counter(word2).items(), key=lambda x:-x[1]))
        values = [value for value in count1.values()]
        pointer = 0

        for key, value in count2.items():
                if value != values[pointer] or key not in count1:
                    return False
                pointer += 1
        return True




        