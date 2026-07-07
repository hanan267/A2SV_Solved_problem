class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Count = [0] * 27
        window = len(s1)

        for i in range(len(s1)):
            idx = ord(s1[i]) - ord('a') + 1
            s1Count[idx] += 1

        s2Count = [0] * 27
        left = 0

        for right in range(len(s2)):

            idx = ord(s2[right]) - ord('a') + 1
            s2Count[idx] += 1

            if right - left + 1 > window:
                idx = ord(s2[left]) - ord('a') + 1
                s2Count[idx] -= 1
                left += 1
                
            if right - left + 1 == window and s1Count == s2Count:
                return True
                break

        return False
           
                




        



        
            


        