class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        bascket = defaultdict(int)
        n = len(fruits)
        left = 0
        res = 0
        fruitNo = 0

        for right in range(n):
            bascket[fruits[right]] += 1
            fruitNo += 1

            while len(bascket) > 2:
                fruitNo -= 1
                bascket[fruits[left]] -= 1
                if bascket[fruits[left]] == 0:
                    del bascket[fruits[left]]
                left += 1
            
            res = max(res, fruitNo)
        return res





        