class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        c = Counter(answers)
        
        res = 0

        for key, value in c.items():
           colors = ceil(value / (key + 1))
           members = colors * (key + 1)
           res += members
        return res


        