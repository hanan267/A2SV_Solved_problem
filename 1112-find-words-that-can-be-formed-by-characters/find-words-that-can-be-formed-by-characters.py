class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # store the ount of each word in words 
        # then check if count of letters are less than or eual to that of chars
        # if yes store the length
        charsCount = Counter(chars)
        res = 0
        for word in words:
           
            wordCount = Counter(word)
            length = 0
            for char,freq in wordCount.items():
                if (char not in charsCount) or (freq > charsCount[char]):
                    length = 0
                    break
                length += freq
           
            res += length
                    
        return res
            

        