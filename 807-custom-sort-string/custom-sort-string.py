class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # letters = set(s)
        # newstr = ""
        # for char in order:
        #     if char in letters:
        #         newstr += char
        #         letters.remove(char)
        #         # print(newstr, letters)
        # if not newstr:
        #     return newstr
        # for chars in s:
        #     if chars in letters:
        #         # print(chars, letters)
        #         newstr += chars
        #         letters.remove(chars)
        #         # print(newstr, letters)
        # return newstr
        count = Counter(s)
        res = ""
        for char in order:
            while count[char] > 0:
                res += char
                count[char] -= 1
        for char in s:
            if count[char] > 0:
                res += char
                count[char] -= 1
        return (res)




        