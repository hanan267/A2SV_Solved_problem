class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
       



        Sum = 0
        for num in nums:
            if num % 2 == 0:
                Sum += num
        res = []
        for val, idx in queries[0:]:
            old =  nums[idx]
            # print("old",old)
            new = old + val
            # print("new",new)
            if old % 2 == 0:
                Sum -= old
            # print("Sum",Sum)
            if new %2 == 0:
               Sum += new
            # print("newSum",Sum)
            nums[idx] = new
            res.append(Sum)
        return res
            

