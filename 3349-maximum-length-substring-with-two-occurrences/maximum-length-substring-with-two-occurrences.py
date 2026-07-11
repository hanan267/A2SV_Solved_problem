class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        occurance = defaultdict(int)
        res = 0
        left = 0

        for right in range(len(s)):
            occurance[s[right]] += 1

            while occurance[s[right]] > 2:
                occurance[s[left]] -= 1
                if occurance[s[left]] == 0:
                    del occurance[s[left]]
                left += 1
            res = max(res, right - left + 1)
        return res

            

        