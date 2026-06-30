class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n = len(s2)
        left = 0
        right = len(s1) - 1
        s1Set = Counter(s1)
        while right < n:
            
            if s1Set == Counter(s2[left:right+1]):
                # print(Counter(s2[left:right+1]))
                return True
            left += 1
            right += 1
        return False
        
            


        