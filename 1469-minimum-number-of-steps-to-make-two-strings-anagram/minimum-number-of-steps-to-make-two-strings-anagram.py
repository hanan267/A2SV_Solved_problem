class Solution:
    def minSteps(self, s: str, t: str) -> int:
        scount = Counter(s)
        tcounter = Counter(t)
        replace = 0

        for key, value in tcounter.items():
            if value > scount[key]:
                replace += (value-scount[key])
        return replace

        