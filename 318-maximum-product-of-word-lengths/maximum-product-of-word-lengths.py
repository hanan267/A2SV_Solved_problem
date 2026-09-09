class Solution:
    def maxProduct(self, words: List[str]) -> int:
       
        arr = []
        ans = 0
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            arr.append(mask)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if arr[i] & arr[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans