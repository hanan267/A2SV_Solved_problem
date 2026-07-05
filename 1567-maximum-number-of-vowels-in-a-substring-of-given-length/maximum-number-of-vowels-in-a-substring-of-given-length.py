class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        n = len(s)
        nonVowel = 0
        vowel = 0
        maxVowel = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(k):
            if s[i] in vowels:
                vowel += 1
        maxVowel = max(maxVowel, vowel)
        if maxVowel == k:
            return k

        for i in range(k, n):
            if s[i - k] in vowels:
                vowel -= 1          
            if s[i] in vowels:
                vowel += 1
            maxVowel = max(maxVowel, vowel)
            if maxVowel == k:
                return k
        return maxVowel
            


            


                

         
        # nonVowel = defaultdict(int)
        # maxVowel = 0
        # vo

        # vowelCount = 0
        # nonVowelCount = 0
        # for i in range(k):
        #     if s[i] not in vowel:
        #         nonVowel[s[i]] += 1
        #         nonVowelCount += 1
        # maxVowel = k - len(nonVowel)
        
        # for i in range(k, len(s)):
        #     if nonVowel[s[i-k]] < 2:
        #         del nonVowel[s[i-k]]
        #     else:
        #         nonVowel[s[i-k]] -= 1
            
        #     if s[i] not in vowel:
        #         nonVowel[s[i]] += 1
        #     print(nonVowel)
        #     maxVowel = max(maxVowel, k - len(nonVowel))
        #     if maxVowel == k:
        #         return k
        # return maxVowel



        