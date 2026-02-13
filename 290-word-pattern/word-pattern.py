class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        if len(pattern) != len(word):
            return False
        ptow = {}
        wtop = {}

        for p, w in zip(pattern, word):
            if p in ptow and ptow[p] != w:
                return False
            elif w in wtop and wtop[w] != p:
                return False
            ptow[p] = w
            wtop[w] = p
            print(ptow,wtop)
        return True