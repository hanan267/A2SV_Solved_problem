class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        mapping = {}
        seen_in_t = set()
        for char_s, char_t in zip(s, t):
            if char_s in mapping:
                if mapping[char_s] != char_t:
                    return False
            else:
                if char_t in seen_in_t:
                    return False
                mapping[char_s] = char_t
                seen_in_t.add(char_t)
        return True
