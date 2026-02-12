class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = Counter(magazine)
        for char in ransomNote:
            print(c[char])
            if char in c:
                if c[char] > 1:
                  c[char] = c[char] - 1
                else:
                    del c[char]
            else:
                return False
        return True
        