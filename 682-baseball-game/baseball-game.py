class Solution:
    def calPoints(self, operations: List[str]) -> int:
      
      record = 0
      nums = []

      for i in range(len(operations)):
        
        if operations[i] == "+":
            nums.append(nums[-1] + nums[-2])
            
        elif operations[i] == "D":
            nums.append(2*nums[-1])
            
        elif operations[i] == 'C':
            nums.pop()
        else:
            nums.append(int(operations[i]))

      return sum(nums)
