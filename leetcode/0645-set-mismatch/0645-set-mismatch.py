class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
       
        n = len(nums)
        numsSet = set(nums)
        print(numsSet)
        res = []

        for i in range(1, n+1):
                if i not in numsSet:
                    res.append(i)
                    
       

        for num in nums:
            if num in numsSet:
                numsSet.remove(num)
            else:
                res.append(num)
        res.reverse()
        return res



        


        