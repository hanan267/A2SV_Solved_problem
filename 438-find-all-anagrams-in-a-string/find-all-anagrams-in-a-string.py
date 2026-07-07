class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        pCount = [0] * 26
        pLen = len(p)

        for char in p:
            idx = ord(char) - ord('a')
            pCount[idx] += 1
        
        # print(p1Count)

        left = 0
        sCount = [0] * 26
        res = []

        for right in range(len(s)):
            rIdx = ord(s[right]) - ord('a')
            sCount[rIdx] += 1

            while right - left + 1 > pLen:
                lIdx = ord(s[left]) - ord('a')
                sCount[lIdx] -= 1
                left += 1
            
            if right - left + 1 == pLen and sCount == pCount:
                res.append(left)
                
                
        return res






        