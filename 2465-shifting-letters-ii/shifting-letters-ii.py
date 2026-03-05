class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        pref = [0]*(len(s)+1)
        for left, right, d in shifts:
            pref[left] += -1 if d else 1
            pref[right+1] += 1 if d else -1
        
        diff = 0
        res = [ord(c) - ord("a") for c in s]
        for i in reversed(range(len(pref))):
            diff += pref[i]

            res[i-1] = (diff + res[i-1]) % 26
        
        s = [chr(ord("a") + n) for n in res]
        return "".join(s)

        
        