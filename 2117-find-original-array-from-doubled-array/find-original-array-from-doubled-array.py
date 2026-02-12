class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed = sorted(changed)
        count = Counter(changed)
        res = []

        if len(changed) % 2 != 0:
            return []
        for num in changed:
            if count[num] == 0:
                continue
            if count[num*2] > 0:
                count[num] -= 1
                count[num*2] -= 1
                res.append(num)
            else:
                return []
        return res
            
        