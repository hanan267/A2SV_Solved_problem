class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # # add the whole and divide by n/2 
        # # sort the function 
        # # find the pair
        # # calsulate the chemistry
        # n = len(skill)

        # divides = sum(skill) / (n//2)
        # skill.sort()

        # groups = []
        # i, j = 0, n - 1
        
        # while (i < j):
        #     if(skill[i] + skill[j] == divides):
        #         groups.append(skill[i]*skill[j])
        #     else:
        #         return -1
        #     i += 1
        #     j -= 1
         
        # return sum(groups)

    

        # total = sum(skill)
        # n = len(skill)
        # # i = n//2
        # # while i < n:

        # # firstHalf = sum(skill[i:n])
        # # print(firstHalf)
        # firstHalf = skill[0]
        # for i in range(1,n):
        #     secondHalf = total - firstHalf
        #     print(firstHalf, secondHalf, total)
        #     if secondHalf > firstHalf:
        #         firstHalf += skill[i]
        #     elif secondHalf == firstHalf:
        #         return firstHalf
        #     else:
        #         return -1

        skill.sort()
        n = len(skill)
        firstSum = skill[0]+skill[n-1]
        i, j = 1, n-2
        chemistery = skill[0]*skill[n-1]
        while i < j:
            if skill[i]+skill[j] == firstSum:
                chemistery += skill[i]*skill[j]
                i += 1
                j -= 1
            else:
                return -1
        return chemistery




























        